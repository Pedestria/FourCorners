"""Asset manifest loading, querying, and hashing."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

import yaml


class AssetType(str, Enum):
    BLOCK_TEXTURE = "block_texture"
    ITEM_TEXTURE = "item_texture"
    GUI_TEXTURE = "gui_texture"
    SOUND_EFFECT = "sound_effect"


@dataclass
class AssetEntry:
    """A single asset defined in the manifest."""

    id: str
    asset_type: AssetType
    prompt: str
    element: Optional[str] = None  # earth, water, air, fire, or None
    width: int = 16
    height: int = 16
    output_path: str = ""  # relative to resource root
    tileable: bool = False
    tags: list[str] = field(default_factory=list)

    @property
    def content_hash(self) -> str:
        """Hash of the generation-relevant fields (for cache invalidation)."""
        blob = json.dumps(
            {
                "id": self.id,
                "asset_type": self.asset_type.value,
                "prompt": self.prompt,
                "element": self.element,
                "width": self.width,
                "height": self.height,
                "tileable": self.tileable,
            },
            sort_keys=True,
        )
        return hashlib.sha256(blob.encode()).hexdigest()[:16]


def _resolve_output_path(entry_id: str, asset_type: AssetType) -> str:
    """Derive the default output path from ID and type."""
    match asset_type:
        case AssetType.BLOCK_TEXTURE:
            return f"textures/block/{entry_id}.png"
        case AssetType.ITEM_TEXTURE:
            return f"textures/item/{entry_id}.png"
        case AssetType.GUI_TEXTURE:
            return f"textures/gui/{entry_id}.png"
        case AssetType.SOUND_EFFECT:
            return f"sounds/{entry_id}.ogg"


def load_manifest(path: Path) -> list[AssetEntry]:
    """Parse the YAML manifest into a list of AssetEntry objects."""
    with open(path) as f:
        raw = yaml.safe_load(f)

    entries: list[AssetEntry] = []
    for item in raw.get("assets", []):
        asset_type = AssetType(item["type"])
        entry = AssetEntry(
            id=item["id"],
            asset_type=asset_type,
            prompt=item.get("prompt", ""),
            element=item.get("element"),
            width=item.get("width", 16),
            height=item.get("height", 16),
            output_path=item.get("output_path", "")
            or _resolve_output_path(item["id"], asset_type),
            tileable=item.get("tileable", asset_type == AssetType.BLOCK_TEXTURE),
            tags=item.get("tags", []),
        )
        entries.append(entry)
    return entries


def filter_entries(
    entries: list[AssetEntry],
    ids: Optional[list[str]] = None,
    asset_type: Optional[AssetType] = None,
    element: Optional[str] = None,
    tags: Optional[list[str]] = None,
) -> list[AssetEntry]:
    """Filter manifest entries by criteria."""
    result = entries
    if ids:
        id_set = set(ids)
        result = [e for e in result if e.id in id_set]
    if asset_type:
        result = [e for e in result if e.asset_type == asset_type]
    if element:
        result = [e for e in result if e.element == element.lower()]
    if tags:
        tag_set = set(tags)
        result = [e for e in result if tag_set.intersection(e.tags)]
    return result
