"""Caching layer to avoid re-generating unchanged assets."""

from __future__ import annotations

import json
from pathlib import Path

from .manifest import AssetEntry


class GenerationCache:
    """Tracks content hashes of previously generated assets."""

    def __init__(self, cache_dir: Path) -> None:
        self.cache_dir = cache_dir
        self.cache_file = cache_dir / "generation_cache.json"
        self._data: dict[str, str] = {}
        self._load()

    def _load(self) -> None:
        if self.cache_file.exists():
            self._data = json.loads(self.cache_file.read_text())

    def _save(self) -> None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file.write_text(json.dumps(self._data, indent=2))

    def is_current(self, entry: AssetEntry, output_exists: bool) -> bool:
        """Return True if this entry has already been generated with the same prompt/params."""
        if not output_exists:
            return False
        return self._data.get(entry.id) == entry.content_hash

    def mark_generated(self, entry: AssetEntry) -> None:
        """Record that this entry was generated."""
        self._data[entry.id] = entry.content_hash
        self._save()

    def invalidate(self, entry_id: str) -> None:
        """Remove an entry from the cache (forces regeneration)."""
        self._data.pop(entry_id, None)
        self._save()

    def clear(self) -> None:
        """Clear the entire cache."""
        self._data.clear()
        self._save()
