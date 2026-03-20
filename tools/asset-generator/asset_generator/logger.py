"""Generation log — records prompts, costs, and timestamps."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


class GenerationLog:
    """Append-only log of generation events."""

    def __init__(self, log_dir: Path) -> None:
        self.log_dir = log_dir
        self.log_file = log_dir / "generation.jsonl"

    def log(
        self,
        asset_id: str,
        asset_type: str,
        prompt: str,
        model: str,
        *,
        success: bool = True,
        error: str = "",
        cost_estimate: str = "",
        output_path: str = "",
    ) -> None:
        """Append a generation event to the log."""
        self.log_dir.mkdir(parents=True, exist_ok=True)
        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "asset_id": asset_id,
            "asset_type": asset_type,
            "model": model,
            "prompt": prompt,
            "success": success,
            "error": error,
            "cost_estimate": cost_estimate,
            "output_path": output_path,
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(record) + "\n")
