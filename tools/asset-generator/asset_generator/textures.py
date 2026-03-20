"""Texture generation via OpenAI (DALL-E 3 / GPT-image-1)."""

from __future__ import annotations

import base64
import time
from typing import Optional

from openai import OpenAI

from .config import AESTHETIC_PROMPT, ELEMENTAL_PALETTES, Config
from .manifest import AssetEntry, AssetType


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def _element_palette_fragment(element: Optional[str]) -> str:
    """Return a prompt fragment describing the elemental color palette."""
    if not element or element.lower() not in ELEMENTAL_PALETTES:
        return ""
    pal = ELEMENTAL_PALETTES[element.lower()]
    colors = ", ".join(pal["colors"])
    return f"Use the {element} elemental palette: {colors}."


def _type_constraints(entry: AssetEntry) -> str:
    """Return prompt constraints specific to the asset type."""
    match entry.asset_type:
        case AssetType.BLOCK_TEXTURE:
            tile = " The texture must tile seamlessly on all edges." if entry.tileable else ""
            return (
                f"Pixel-art block texture for Minecraft, exactly {entry.width}x{entry.height} pixels. "
                f"Top-down or front-face view. Clean pixel edges, no anti-aliasing.{tile}"
            )
        case AssetType.ITEM_TEXTURE:
            return (
                f"Pixel-art item icon for Minecraft, exactly {entry.width}x{entry.height} pixels. "
                f"Transparent background. Held-item perspective (slight 3/4 angle). "
                f"Clean pixel edges, no anti-aliasing."
            )
        case AssetType.GUI_TEXTURE:
            return (
                f"Minecraft GUI texture, {entry.width}x{entry.height} pixels. "
                f"Flat UI style with stone/metal borders. Clean lines."
            )
        case _:
            return ""


def build_prompt(entry: AssetEntry) -> str:
    """Assemble the full generation prompt for a texture asset."""
    parts = [
        AESTHETIC_PROMPT,
        _type_constraints(entry),
        _element_palette_fragment(entry.element),
        entry.prompt,
    ]
    return " ".join(p for p in parts if p)


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------

def _dalle3_generate(client: OpenAI, prompt: str, size: str) -> bytes:
    """Generate an image with DALL-E 3 and return raw bytes."""
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size=size,
        response_format="b64_json",
        quality="standard",
    )
    b64 = response.data[0].b64_json
    return base64.b64decode(b64)


def _gpt_image1_generate(client: OpenAI, prompt: str, size: str) -> bytes:
    """Generate an image with GPT-image-1 and return raw bytes."""
    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        n=1,
        size=size,
    )
    # gpt-image-1 returns b64_json by default
    b64 = response.data[0].b64_json
    return base64.b64decode(b64)


def _pick_api_size(entry: AssetEntry, model: str) -> str:
    """Choose the smallest API image size that works for the model."""
    if model == "dall-e-3":
        return "1024x1024"  # DALL-E 3 minimum is 1024
    # gpt-image-1 supports smaller sizes
    if entry.width <= 256 and entry.height <= 256:
        return "256x256"
    if entry.width <= 512 and entry.height <= 512:
        return "512x512"
    return "1024x1024"


def generate_texture(entry: AssetEntry, config: Config) -> bytes:
    """Generate a texture and return raw image bytes."""
    client = OpenAI(api_key=config.openai_api_key)
    prompt = build_prompt(entry)
    size = _pick_api_size(entry, config.image_model)

    if config.image_model == "dall-e-3":
        raw = _dalle3_generate(client, prompt, size)
    else:
        raw = _gpt_image1_generate(client, prompt, size)

    time.sleep(config.rate_limit_delay)
    return raw


def estimate_texture_cost(entry: AssetEntry, model: str) -> str:
    """Rough cost estimate for generating one texture."""
    if model == "dall-e-3":
        return "$0.040 (DALL-E 3 standard 1024x1024)"
    # gpt-image-1 pricing varies; rough estimate
    return "$0.011 (GPT-image-1 256x256 estimate)"
