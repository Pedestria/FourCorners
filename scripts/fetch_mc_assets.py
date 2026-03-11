#!/usr/bin/env python3
"""Populate the legacy ForgeGradle asset cache using HTTPS Mojang asset URLs."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import ssl
import sys
import tempfile
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_ASSET_INDEX = Path(".gradle-home/caches/minecraft/assets/indexes/1.12.json")
DEFAULT_ASSET_ROOT = Path(".gradle-home/caches/minecraft/assets")
ASSET_BASE_URL = "https://resources.download.minecraft.net"
DEFAULT_HEADERS = {
    "User-Agent": "FourCornersAssetFetcher/1.0",
    "Accept": "*/*",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download any missing Minecraft asset objects into the local ForgeGradle "
            "cache using HTTPS URLs."
        )
    )
    parser.add_argument(
        "--asset-index",
        type=Path,
        default=DEFAULT_ASSET_INDEX,
        help=f"Asset index JSON to read (default: {DEFAULT_ASSET_INDEX}).",
    )
    parser.add_argument(
        "--asset-root",
        type=Path,
        default=DEFAULT_ASSET_ROOT,
        help=f"Asset cache root directory (default: {DEFAULT_ASSET_ROOT}).",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=min(16, max(4, (os.cpu_count() or 4))),
        help="Number of concurrent downloads (default: auto).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Network timeout in seconds (default: 30).",
    )
    parser.add_argument(
        "--ca-file",
        type=Path,
        help="Use a custom CA bundle for TLS verification.",
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Disable TLS certificate verification. Use only if your local trust store is broken.",
    )
    return parser.parse_args()


def build_ssl_context(ca_file: Path | None, insecure: bool) -> ssl.SSLContext:
    if insecure:
        return ssl._create_unverified_context()
    if ca_file is not None:
        return ssl.create_default_context(cafile=str(ca_file))
    return ssl.create_default_context()


def load_asset_index(asset_index_path: Path) -> dict:
    with asset_index_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_missing_assets(asset_root: Path, asset_index: dict) -> Iterable[tuple[str, Path, str]]:
    objects = asset_index.get("objects", {})
    for logical_name, metadata in objects.items():
        sha1 = metadata["hash"]
        object_path = asset_root / "objects" / sha1[:2] / sha1
        if not object_path.exists():
            url = f"{ASSET_BASE_URL}/{sha1[:2]}/{sha1}"
            yield logical_name, object_path, url


def download_asset(
    logical_name: str,
    destination: Path,
    url: str,
    timeout: int,
    ssl_context: ssl.SSLContext,
) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers=DEFAULT_HEADERS)
    with tempfile.NamedTemporaryFile(
        dir=destination.parent, prefix=destination.name, suffix=".tmp", delete=False
    ) as tmp_file:
        temp_path = Path(tmp_file.name)

    try:
        with urlopen(request, timeout=timeout, context=ssl_context) as response:
            with temp_path.open("wb") as handle:
                handle.write(response.read())
        temp_path.replace(destination)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise

    return logical_name


def main() -> int:
    args = parse_args()
    ssl_context = build_ssl_context(args.ca_file, args.insecure)

    try:
        asset_index = load_asset_index(args.asset_index)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"error: unable to read asset index: {exc}", file=sys.stderr)
        return 1

    missing = list(iter_missing_assets(args.asset_root, asset_index))
    total = len(asset_index.get("objects", {}))
    missing_count = len(missing)

    print(f"Asset index: {args.asset_index}")
    print(f"Asset root: {args.asset_root}")
    print(f"Total objects: {total}")
    print(f"Missing objects: {missing_count}")

    if missing_count == 0:
        return 0

    completed = 0
    failures: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_map = {
            executor.submit(
                download_asset,
                logical_name,
                destination,
                url,
                args.timeout,
                ssl_context,
            ): logical_name
            for logical_name, destination, url in missing
        }

        for future in concurrent.futures.as_completed(future_map):
            logical_name = future_map[future]
            try:
                future.result()
                completed += 1
                if completed % 50 == 0 or completed == missing_count:
                    print(f"Downloaded {completed}/{missing_count}")
            except (HTTPError, URLError, TimeoutError, ssl.SSLError) as exc:
                failures.append(f"{logical_name}: {exc}")

    if failures:
        print("error: failed downloads:", file=sys.stderr)
        for failure in failures[:20]:
            print(f"  {failure}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
