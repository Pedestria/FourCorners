#!/usr/bin/env python3
"""Fetch a Forge artifact for a Minecraft version from official Forge endpoints."""

from __future__ import annotations

import argparse
import json
import ssl
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Tuple
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PROMOTIONS_URL = (
    "https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json"
)
MAVEN_BASE_URL = "https://maven.minecraftforge.net/net/minecraftforge/forge"
DEFAULT_MC_VERSION = "1.12.2"
DEFAULT_CHANNEL = "recommended"
DEFAULT_ARTIFACT = "installer"
DEFAULT_OUTPUT_DIR = Path("downloads/forge")
DEFAULT_HEADERS = {
    "User-Agent": "FourCornersForgeFetcher/1.0 (+https://maven.minecraftforge.net)",
    "Accept": "*/*",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch a stable Forge 1.12.2 build from official Forge metadata. "
            "Defaults to the recommended installer."
        )
    )
    parser.add_argument(
        "--minecraft-version",
        default=DEFAULT_MC_VERSION,
        help=f"Minecraft version to resolve (default: {DEFAULT_MC_VERSION}).",
    )
    parser.add_argument(
        "--channel",
        choices=("recommended", "latest"),
        default=DEFAULT_CHANNEL,
        help="Promotion channel to resolve (default: recommended).",
    )
    parser.add_argument(
        "--artifact",
        choices=("installer", "mdk", "universal"),
        default=DEFAULT_ARTIFACT,
        help="Forge artifact to download (default: installer).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to write the download into (default: {DEFAULT_OUTPUT_DIR}).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing downloaded file.",
    )
    parser.add_argument(
        "--resolve-only",
        action="store_true",
        help="Print the resolved Forge version and URL without downloading it.",
    )
    parser.add_argument(
        "--allow-latest-fallback",
        action="store_true",
        help=(
            "If the recommended build is missing, fall back to the latest build "
            "instead of failing."
        ),
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


def open_url(url: str, timeout: int, ssl_context: ssl.SSLContext):
    request = Request(url, headers=DEFAULT_HEADERS)
    return urlopen(request, timeout=timeout, context=ssl_context)


def fetch_promotions(timeout: int, ssl_context: ssl.SSLContext) -> dict:
    with open_url(PROMOTIONS_URL, timeout, ssl_context) as response:
        return json.load(response)


def resolve_version(
    promotions: dict,
    minecraft_version: str,
    channel: str,
    allow_latest_fallback: bool,
) -> Tuple[str, str]:
    promos = promotions.get("promos", {})
    requested_key = f"{minecraft_version}-{channel}"
    version = promos.get(requested_key)
    resolved_channel = channel

    if version is None and channel == "recommended" and allow_latest_fallback:
        fallback_key = f"{minecraft_version}-latest"
        version = promos.get(fallback_key)
        resolved_channel = "latest"

    if version is None:
        available = sorted(
            key for key in promos if key.startswith(f"{minecraft_version}-")
        )
        suffix = ""
        if available:
            suffix = f" Available promotions: {', '.join(available)}."
        raise RuntimeError(
            f"No Forge promotion found for '{requested_key}'.{suffix}"
        )

    return version, resolved_channel


def build_download_url(minecraft_version: str, forge_version: str, artifact: str) -> str:
    full_version = f"{minecraft_version}-{forge_version}"
    filename = f"forge-{full_version}-{artifact}.jar"
    return f"{MAVEN_BASE_URL}/{full_version}/{filename}"


def download_file(
    url: str,
    destination: Path,
    timeout: int,
    ssl_context: ssl.SSLContext,
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=destination.parent, prefix=destination.name, suffix=".tmp", delete=False
    ) as tmp_file:
        temp_path = Path(tmp_file.name)

    try:
        with open_url(url, timeout, ssl_context) as response, temp_path.open("wb") as handle:
            shutil.copyfileobj(response, handle)
        temp_path.replace(destination)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def main() -> int:
    args = parse_args()
    ssl_context = build_ssl_context(args.ca_file, args.insecure)

    try:
        promotions = fetch_promotions(args.timeout, ssl_context)
        forge_version, resolved_channel = resolve_version(
            promotions,
            args.minecraft_version,
            args.channel,
            args.allow_latest_fallback,
        )
    except (
        HTTPError,
        URLError,
        TimeoutError,
        RuntimeError,
        json.JSONDecodeError,
        ssl.SSLError,
    ) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    url = build_download_url(args.minecraft_version, forge_version, args.artifact)
    filename = Path(url).name
    destination = args.output_dir / filename

    print(f"Minecraft: {args.minecraft_version}")
    print(f"Forge: {forge_version}")
    print(f"Channel: {resolved_channel}")
    print(f"Artifact: {args.artifact}")
    print(f"URL: {url}")

    if args.resolve_only:
        return 0

    if destination.exists() and not args.force:
        print(f"Already downloaded: {destination}")
        print("Use --force to overwrite.")
        return 0

    try:
        download_file(url, destination, args.timeout, ssl_context)
    except (HTTPError, URLError, TimeoutError, ssl.SSLError) as exc:
        print(f"error: failed to download {url}: {exc}", file=sys.stderr)
        return 1

    print(f"Saved to: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
