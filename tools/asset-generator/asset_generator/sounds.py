"""Sound effect generation via ElevenLabs."""

from __future__ import annotations

import json
import time
from pathlib import Path

from .config import AESTHETIC_PROMPT, Config
from .manifest import AssetEntry


def build_sound_prompt(entry: AssetEntry) -> str:
    """Build a descriptive prompt for sound effect generation."""
    base = (
        "Minecraft-style sound effect. Short, punchy, game-appropriate. "
        "Fantasy-industrial tone — metallic, crystalline, and magical. "
    )
    return base + entry.prompt


def generate_sound(entry: AssetEntry, config: Config) -> bytes:
    """Generate a sound effect via ElevenLabs and return raw audio bytes."""
    from elevenlabs import ElevenLabs

    client = ElevenLabs(api_key=config.elevenlabs_api_key)
    prompt = build_sound_prompt(entry)

    response = client.text_to_sound_effects.convert(
        text=prompt,
        duration_seconds=2.0,
    )
    # Response is a generator of bytes chunks
    audio_bytes = b"".join(response)

    time.sleep(config.rate_limit_delay)
    return audio_bytes


def update_sounds_json(sounds_json_path: Path, entries: list[AssetEntry]) -> None:
    """Generate or update the sounds.json registry for Minecraft sound event binding."""
    existing: dict = {}
    if sounds_json_path.exists():
        existing = json.loads(sounds_json_path.read_text())

    for entry in entries:
        # Sound event name: fourcorners:entry_id
        # Sound path is relative to sounds/ without extension
        sound_path = f"fourcorners:{entry.id}"
        event_name = entry.id

        if event_name not in existing:
            existing[event_name] = {
                "category": "block",
                "sounds": [
                    {
                        "name": sound_path,
                        "stream": False,
                    }
                ],
            }
            # Assign category based on tags
            if "ambient" in entry.tags:
                existing[event_name]["category"] = "ambient"
            elif "ui" in entry.tags:
                existing[event_name]["category"] = "master"
            elif "machine" in entry.tags:
                existing[event_name]["category"] = "block"

    sounds_json_path.parent.mkdir(parents=True, exist_ok=True)
    sounds_json_path.write_text(json.dumps(existing, indent=2) + "\n")


def estimate_sound_cost(entry: AssetEntry) -> str:
    """Rough cost estimate for generating one sound effect."""
    return "$0.10 (ElevenLabs sound effect, ~2s)"
