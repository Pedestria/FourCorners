"""Post-processing for generated images and audio."""

from __future__ import annotations

import io
import subprocess
from pathlib import Path

from PIL import Image


# ---------------------------------------------------------------------------
# Image post-processing
# ---------------------------------------------------------------------------

def resize_to_target(img: Image.Image, width: int, height: int) -> Image.Image:
    """Resize image to exact target dimensions using nearest-neighbor (pixel art)."""
    return img.resize((width, height), Image.NEAREST)


def quantize_palette(img: Image.Image, max_colors: int = 32) -> Image.Image:
    """Reduce color count to a Minecraft-appropriate palette."""
    if img.mode == "RGBA":
        # Preserve transparency: quantize RGB, reapply alpha
        alpha = img.split()[3]
        rgb = img.convert("RGB").quantize(colors=max_colors, method=Image.MEDIANCUT)
        rgb = rgb.convert("RGB")
        result = rgb.convert("RGBA")
        result.putalpha(alpha)
        return result
    return img.quantize(colors=max_colors, method=Image.MEDIANCUT).convert("RGB")


def check_tileability(img: Image.Image) -> bool:
    """Basic tileability check: compare edge pixels for continuity."""
    w, h = img.size
    if w < 2 or h < 2:
        return True
    pixels = img.load()
    mismatches = 0
    total = 0
    # Check left-right edge continuity
    for y in range(h):
        total += 1
        left = pixels[0, y]
        right = pixels[w - 1, y]
        if isinstance(left, int):
            if abs(left - right) > 40:
                mismatches += 1
        else:
            if any(abs(a - b) > 40 for a, b in zip(left[:3], right[:3])):
                mismatches += 1
    # Check top-bottom edge continuity
    for x in range(w):
        total += 1
        top = pixels[x, 0]
        bottom = pixels[x, h - 1]
        if isinstance(top, int):
            if abs(top - bottom) > 40:
                mismatches += 1
        else:
            if any(abs(a - b) > 40 for a, b in zip(top[:3], bottom[:3])):
                mismatches += 1
    return (mismatches / total) < 0.3 if total > 0 else True


def process_texture(
    raw_bytes: bytes,
    width: int,
    height: int,
    *,
    tileable: bool = False,
    has_transparency: bool = False,
) -> Image.Image:
    """Full post-processing pipeline for a generated texture."""
    img = Image.open(io.BytesIO(raw_bytes))
    if has_transparency:
        img = img.convert("RGBA")
    else:
        img = img.convert("RGB")
    img = resize_to_target(img, width, height)
    img = quantize_palette(img)
    return img


def save_texture(img: Image.Image, output_path: Path) -> None:
    """Save a processed texture as PNG."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG")


# ---------------------------------------------------------------------------
# Audio post-processing
# ---------------------------------------------------------------------------

def process_sound(raw_bytes: bytes, output_path: Path) -> None:
    """Convert audio to OGG Vorbis, normalize, and trim silence.

    Requires ffmpeg on PATH. Falls back to raw save if ffmpeg is unavailable.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_input = output_path.with_suffix(".tmp.mp3")
    try:
        tmp_input.write_bytes(raw_bytes)
        # Use ffmpeg: normalize audio, trim silence, convert to ogg vorbis
        cmd = [
            "ffmpeg", "-y", "-i", str(tmp_input),
            # Trim leading silence
            "-af", "silenceremove=start_periods=1:start_threshold=-50dB,"
                   "silenceremove=stop_periods=1:stop_threshold=-50dB,"
                   "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-c:a", "libvorbis", "-q:a", "4",
            str(output_path),
        ]
        subprocess.run(cmd, capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        # ffmpeg not available or failed — try pydub as fallback
        try:
            from pydub import AudioSegment
            audio = AudioSegment.from_file(io.BytesIO(raw_bytes))
            audio = audio.normalize()
            audio.export(str(output_path), format="ogg", codec="libvorbis")
        except Exception:
            # Last resort: save raw bytes
            output_path.write_bytes(raw_bytes)
    finally:
        tmp_input.unlink(missing_ok=True)
