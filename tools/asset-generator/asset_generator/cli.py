"""CLI interface for the Four Corners asset generator."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from .cache import GenerationCache
from .config import SOUNDS_JSON, Config
from .logger import GenerationLog
from .manifest import AssetEntry, AssetType, filter_entries, load_manifest
from .postprocess import process_sound, process_texture, save_texture
from .sounds import (
    build_sound_prompt,
    estimate_sound_cost,
    generate_sound,
    update_sounds_json,
)
from .textures import build_prompt, estimate_texture_cost, generate_texture

app = typer.Typer(help="Generate Minecraft-ready textures and sounds for The Four Corners mod.")
console = Console()


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _load_all(config: Config) -> tuple[list[AssetEntry], GenerationCache, GenerationLog]:
    entries = load_manifest(config.manifest_path)
    cache = GenerationCache(config.cache_dir)
    log = GenerationLog(config.log_dir)
    return entries, cache, log


def _output_path(entry: AssetEntry, config: Config, *, staging: bool = False) -> Path:
    root = config.staging_dir if staging else config.resource_root
    return root / entry.output_path


def _backup(path: Path, config: Config) -> None:
    if config.backup_before_overwrite and path.exists():
        bak = path.with_suffix(path.suffix + ".bak")
        shutil.copy2(path, bak)


def _select_entries(
    entries: list[AssetEntry],
    ids: Optional[list[str]],
    asset_type: Optional[str],
    element: Optional[str],
    tag: Optional[str],
) -> list[AssetEntry]:
    return filter_entries(
        entries,
        ids=ids,
        asset_type=AssetType(asset_type) if asset_type else None,
        element=element,
        tags=[tag] if tag else None,
    )


# ---------------------------------------------------------------------------
# generate
# ---------------------------------------------------------------------------

@app.command()
def generate(
    ids: Optional[list[str]] = typer.Argument(None, help="Specific asset IDs to generate"),
    asset_type: Optional[str] = typer.Option(None, "--type", "-t", help="Filter by asset type"),
    element: Optional[str] = typer.Option(None, "--element", "-e", help="Filter by element"),
    tag: Optional[str] = typer.Option(None, "--tag", help="Filter by tag"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Show what would be generated"),
    force: bool = typer.Option(False, "--force", "-f", help="Regenerate even if cached"),
    all_assets: bool = typer.Option(False, "--all", "-a", help="Generate all assets"),
) -> None:
    """Generate assets for specific IDs, asset types, or all."""
    config = Config.load()
    entries, cache, log = _load_all(config)

    if all_assets:
        selected = entries
    elif ids:
        selected = _select_entries(entries, ids, asset_type, element, tag)
    else:
        selected = _select_entries(entries, None, asset_type, element, tag)

    if not selected:
        console.print("[yellow]No assets matched the given filters.[/yellow]")
        raise typer.Exit(1)

    # Partition into textures and sounds
    textures = [e for e in selected if e.asset_type != AssetType.SOUND_EFFECT]
    sounds = [e for e in selected if e.asset_type == AssetType.SOUND_EFFECT]

    skipped = 0
    generated = 0
    failed = 0

    for entry in textures + sounds:
        out = _output_path(entry, config)
        cached = cache.is_current(entry, out.exists())

        if cached and not force:
            if dry_run:
                console.print(f"  [dim]SKIP (cached)[/dim]  {entry.id}")
            skipped += 1
            continue

        if dry_run:
            if entry.asset_type == AssetType.SOUND_EFFECT:
                prompt = build_sound_prompt(entry)
                cost = estimate_sound_cost(entry)
            else:
                prompt = build_prompt(entry)
                cost = estimate_texture_cost(entry, config.image_model)
            console.print(f"  [green]GENERATE[/green]  {entry.id}")
            console.print(f"    Type: {entry.asset_type.value}  →  {entry.output_path}")
            console.print(f"    Cost: {cost}")
            console.print(f"    Prompt: {prompt[:120]}...")
            generated += 1
            continue

        # Validate API keys
        if entry.asset_type == AssetType.SOUND_EFFECT and not config.elevenlabs_api_key:
            console.print(f"  [red]ERROR[/red]  {entry.id}: ELEVENLABS_API_KEY not set")
            failed += 1
            continue
        if entry.asset_type != AssetType.SOUND_EFFECT and not config.openai_api_key:
            console.print(f"  [red]ERROR[/red]  {entry.id}: OPENAI_API_KEY not set")
            failed += 1
            continue

        console.print(f"  [blue]Generating[/blue]  {entry.id}...", end=" ")
        try:
            if entry.asset_type == AssetType.SOUND_EFFECT:
                raw = generate_sound(entry, config)
                _backup(out, config)
                process_sound(raw, out)
            else:
                raw = generate_texture(entry, config)
                has_alpha = entry.asset_type == AssetType.ITEM_TEXTURE
                img = process_texture(
                    raw,
                    entry.width,
                    entry.height,
                    tileable=entry.tileable,
                    has_transparency=has_alpha,
                )
                _backup(out, config)
                save_texture(img, out)

            cache.mark_generated(entry)
            log.log(
                entry.id,
                entry.asset_type.value,
                build_prompt(entry) if entry.asset_type != AssetType.SOUND_EFFECT else build_sound_prompt(entry),
                config.image_model if entry.asset_type != AssetType.SOUND_EFFECT else "elevenlabs",
                output_path=str(out),
            )
            console.print("[green]OK[/green]")
            generated += 1
        except Exception as exc:
            log.log(
                entry.id,
                entry.asset_type.value,
                "",
                "",
                success=False,
                error=str(exc),
            )
            console.print(f"[red]FAILED: {exc}[/red]")
            failed += 1

    # Update sounds.json if any sound effects were generated
    if sounds and not dry_run:
        generated_sounds = [e for e in sounds if cache.is_current(e, _output_path(e, config).exists())]
        if generated_sounds:
            update_sounds_json(SOUNDS_JSON, generated_sounds)
            console.print(f"  [blue]Updated[/blue] sounds.json with {len(generated_sounds)} entries")

    label = "Would generate" if dry_run else "Generated"
    console.print(
        f"\n{label}: {generated}  Skipped: {skipped}  Failed: {failed}"
    )


# ---------------------------------------------------------------------------
# preview
# ---------------------------------------------------------------------------

@app.command()
def preview(
    ids: Optional[list[str]] = typer.Argument(None, help="Specific asset IDs to preview"),
    asset_type: Optional[str] = typer.Option(None, "--type", "-t"),
    element: Optional[str] = typer.Option(None, "--element", "-e"),
    tag: Optional[str] = typer.Option(None, "--tag"),
) -> None:
    """Generate assets to a staging folder for review before placement."""
    config = Config.load()
    entries, cache, log = _load_all(config)
    selected = _select_entries(entries, ids, asset_type, element, tag)

    if not selected:
        console.print("[yellow]No assets matched.[/yellow]")
        raise typer.Exit(1)

    config.staging_dir.mkdir(parents=True, exist_ok=True)
    generated = 0

    for entry in selected:
        out = _output_path(entry, config, staging=True)

        if entry.asset_type == AssetType.SOUND_EFFECT and not config.elevenlabs_api_key:
            console.print(f"  [red]SKIP[/red]  {entry.id}: ELEVENLABS_API_KEY not set")
            continue
        if entry.asset_type != AssetType.SOUND_EFFECT and not config.openai_api_key:
            console.print(f"  [red]SKIP[/red]  {entry.id}: OPENAI_API_KEY not set")
            continue

        console.print(f"  [blue]Previewing[/blue]  {entry.id}...", end=" ")
        try:
            if entry.asset_type == AssetType.SOUND_EFFECT:
                raw = generate_sound(entry, config)
                process_sound(raw, out)
            else:
                raw = generate_texture(entry, config)
                has_alpha = entry.asset_type == AssetType.ITEM_TEXTURE
                img = process_texture(
                    raw, entry.width, entry.height,
                    tileable=entry.tileable, has_transparency=has_alpha,
                )
                save_texture(img, out)
            console.print("[green]OK[/green]")
            generated += 1
        except Exception as exc:
            console.print(f"[red]FAILED: {exc}[/red]")

    console.print(f"\nPreviews generated in: {config.staging_dir}")
    console.print(f"Total: {generated}")


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------

@app.command(name="list")
def list_assets(
    asset_type: Optional[str] = typer.Option(None, "--type", "-t"),
    element: Optional[str] = typer.Option(None, "--element", "-e"),
    tag: Optional[str] = typer.Option(None, "--tag"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Show all registered assets and their generation status."""
    config = Config.load()
    entries, cache, _ = _load_all(config)
    selected = _select_entries(entries, None, asset_type, element, tag)

    table = Table(title="Asset Registry")
    table.add_column("ID", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("Element")
    table.add_column("Size")
    table.add_column("Status")
    if verbose:
        table.add_column("Output Path", style="dim")

    for entry in selected:
        out = _output_path(entry, config)
        if out.exists():
            if cache.is_current(entry, True):
                status = "[green]current[/green]"
            else:
                status = "[yellow]outdated[/yellow]"
        else:
            status = "[red]missing[/red]"

        row = [
            entry.id,
            entry.asset_type.value,
            entry.element or "-",
            f"{entry.width}x{entry.height}" if entry.asset_type != AssetType.SOUND_EFFECT else "-",
            status,
        ]
        if verbose:
            row.append(entry.output_path)
        table.add_row(*row)

    console.print(table)
    console.print(f"\nTotal: {len(selected)} assets")


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------

@app.command()
def validate(
    asset_type: Optional[str] = typer.Option(None, "--type", "-t"),
    element: Optional[str] = typer.Option(None, "--element", "-e"),
) -> None:
    """Check existing assets against manifest for missing/outdated files."""
    config = Config.load()
    entries, cache, _ = _load_all(config)
    selected = _select_entries(entries, None, asset_type, element, None)

    missing = []
    outdated = []
    current = []

    for entry in selected:
        out = _output_path(entry, config)
        if not out.exists():
            missing.append(entry)
        elif not cache.is_current(entry, True):
            outdated.append(entry)
        else:
            current.append(entry)

    if missing:
        console.print(f"\n[red]Missing ({len(missing)}):[/red]")
        for e in missing:
            console.print(f"  {e.id}  →  {e.output_path}")

    if outdated:
        console.print(f"\n[yellow]Outdated ({len(outdated)}):[/yellow]")
        for e in outdated:
            console.print(f"  {e.id}  →  {e.output_path}")

    if current:
        console.print(f"\n[green]Current ({len(current)}):[/green]")
        for e in current:
            console.print(f"  {e.id}")

    total = len(selected)
    console.print(
        f"\nSummary: {len(current)}/{total} current, "
        f"{len(outdated)}/{total} outdated, "
        f"{len(missing)}/{total} missing"
    )
    if missing or outdated:
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
