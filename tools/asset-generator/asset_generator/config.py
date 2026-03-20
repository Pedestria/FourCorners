"""Configuration and constants for the asset generator."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv


# Resolve paths relative to the repo root (two levels up from this file)
_THIS_DIR = Path(__file__).resolve().parent
TOOL_ROOT = _THIS_DIR.parent
REPO_ROOT = TOOL_ROOT.parent.parent
RESOURCE_ROOT = REPO_ROOT / "src" / "main" / "resources" / "assets" / "fourcorners"

TEXTURE_DIR = RESOURCE_ROOT / "textures"
SOUND_DIR = RESOURCE_ROOT / "sounds"
SOUNDS_JSON = RESOURCE_ROOT / "sounds.json"

STAGING_DIR = TOOL_ROOT / ".staging"
CACHE_DIR = TOOL_ROOT / ".cache"
LOG_DIR = TOOL_ROOT / ".logs"

MANIFEST_PATH = TOOL_ROOT / "manifest.yaml"


# ---------------------------------------------------------------------------
# Elemental palettes (from Design.md section 11)
# ---------------------------------------------------------------------------

ELEMENTAL_PALETTES: dict[str, dict[str, list[str]]] = {
    "earth": {
        "colors": ["moss green", "ochre", "deep slate", "bronze"],
        "hex": ["#4A7C59", "#CC7722", "#2F4F4F", "#CD7F32"],
    },
    "water": {
        "colors": ["teal", "blue", "silver", "pale cyan"],
        "hex": ["#008080", "#2E5090", "#C0C0C0", "#B0E0E6"],
    },
    "air": {
        "colors": ["white", "pale gold", "light blue", "soft gray"],
        "hex": ["#FFFFFF", "#EEE8AA", "#ADD8E6", "#C0C0C0"],
    },
    "fire": {
        "colors": ["ember red", "orange", "black iron", "brass"],
        "hex": ["#CC3300", "#FF8C00", "#2B2B2B", "#B5A642"],
    },
}

# Base aesthetic prompt fragment (Design.md section 11)
AESTHETIC_PROMPT = (
    "arcane-industrial Minecraft style: metal, carved stone, crystal, glass, "
    "and rune motifs combined. Not pure sci-fi. Not generic medieval fantasy. "
    "Engineered and magical at the same time."
)


# ---------------------------------------------------------------------------
# Runtime config
# ---------------------------------------------------------------------------

@dataclass
class Config:
    """Runtime configuration loaded from environment."""

    openai_api_key: str = ""
    elevenlabs_api_key: str = ""
    image_model: str = "gpt-image-1"  # or "dall-e-3"
    resource_root: Path = RESOURCE_ROOT
    staging_dir: Path = STAGING_DIR
    cache_dir: Path = CACHE_DIR
    log_dir: Path = LOG_DIR
    manifest_path: Path = MANIFEST_PATH
    rate_limit_delay: float = 1.0  # seconds between API calls
    backup_before_overwrite: bool = True

    @classmethod
    def load(cls) -> Config:
        """Load config from .env and environment variables."""
        env_path = TOOL_ROOT / ".env"
        load_dotenv(env_path)
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
            elevenlabs_api_key=os.getenv("ELEVENLABS_API_KEY", ""),
            image_model=os.getenv("IMAGE_MODEL", "gpt-image-1"),
        )
