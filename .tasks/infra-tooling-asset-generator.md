# Asset Generator Pipeline

> A Python CLI tool that generates Minecraft-ready textures (via OpenAI image generation) and sound effects (via ElevenLabs) for The Four Corners mod, outputting directly into the correct resource pack structure.

**Status**: Complete
**Depends on**: nothing
**Blocks**: nothing

## Tasks

- [x] Project scaffolding
  - [x] Create `tools/asset-generator/` directory with Python project structure
  - [x] Set up `pyproject.toml` with dependencies (openai, elevenlabs, Pillow, typer)
  - [x] Create `.env.example` for API keys (OPENAI_API_KEY, ELEVENLABS_API_KEY)
  - [x] Add `tools/asset-generator/` to `.gitignore` for generated cache/temp files

- [x] Asset registry / manifest system
  - [x] Define a YAML manifest that maps mod content IDs to generation prompts
  - [x] Include asset type (block_texture, item_texture, gui_texture, sound_effect), target dimensions, and output path
  - [x] Pre-populate manifest with all current and planned items from Design.md (Avalite Ore, Avalon Gem, Core Frame, dimensional materials, etc.)
  - [x] Support the elemental palette from Design.md section 11 (Earth: moss/ochre/bronze, Water: teal/blue/silver, Air: white/pale gold, Fire: ember red/orange/black iron)

- [x] Texture generation module (OpenAI)
  - [x] Implement base prompt builder that enforces the "arcane-industrial" aesthetic from Design.md section 11
  - [x] Support block textures (16x16 tileable) with Minecraft pixel-art style constraints
  - [x] Support item textures (16x16) with transparency and Minecraft icon conventions
  - [x] Support GUI textures (variable size) for machine interfaces
  - [x] Post-process generated images: resize to target dimensions, quantize to Minecraft-appropriate palette, ensure tileability for block textures
  - [x] Output directly to `src/main/resources/assets/fourcorners/textures/{block,item,gui}/` with correct filenames

- [x] Sound generation module (ElevenLabs)
  - [x] Implement sound effect generation for machine operations, elemental ambience, and UI feedback
  - [x] Post-process audio: normalize levels, trim silence, convert to OGG Vorbis (Minecraft's sound format)
  - [x] Output to `src/main/resources/assets/fourcorners/sounds/` with correct structure
  - [x] Generate/update `sounds.json` registry file for Minecraft sound event binding

- [x] CLI interface
  - [x] `generate` command: generate assets for specific IDs, asset types, or all
  - [x] `preview` command: generate to a staging folder for review before placement
  - [x] `list` command: show all registered assets and their generation status
  - [x] `validate` command: check existing assets against manifest for missing/outdated files
  - [x] Dry-run mode that shows what would be generated without API calls
  - [x] Cost estimation before generation (API token/character counts)

- [x] Quality and safety
  - [x] Caching layer to avoid re-generating unchanged assets (hash manifest entries)
  - [x] Rate limiting for API calls
  - [x] Backup existing assets before overwriting
  - [x] Generation log with timestamps, prompts used, and API costs

- [x] Legacy texture directory cleanup
  - [x] Migrate any assets from `textures/blocks/` → `textures/block/` and `textures/items/` → `textures/item/`
  - [x] Remove the legacy `blocks/` and `items/` directories
  - [x] Verify all model JSON files reference the correct paths after migration

## Decisions

- Image model is configurable via IMAGE_MODEL env var: supports both "dall-e-3" and "gpt-image-1" (default)
- DALL-E 3 uses 1024x1024 minimum (downscaled in post-processing), GPT-image-1 uses 256x256 for textures
- Audio conversion: ffmpeg preferred, pydub fallback, raw bytes last resort
- Legacy `textures/blocks/` and `textures/items/` confirmed as byte-identical copies of `block/`/`item/` and removed
- Manifest uses YAML format with ~120 entries covering all Phase 1 + planned assets from Design.md

## Notes

- The mod's aesthetic is "arcane-industrial" — metal, carved stone, crystal, glass, and rune motifs. Not pure sci-fi, not generic medieval fantasy. Prompts must enforce this consistently.
- Elemental palettes are defined in Design.md section 11 and should be baked into the prompt templates per element.
- Legacy `textures/blocks/` and `textures/items/` directories have been removed. Model JSONs already referenced correct `block/`/`item/` paths.
- Minecraft requires OGG Vorbis for sounds. ElevenLabs outputs will need format conversion.
- The manifest should be the single source of truth for what assets exist — useful beyond generation for auditing the resource pack.
