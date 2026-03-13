# Asset Generator Pipeline

> A Python CLI tool that generates Minecraft-ready textures (via OpenAI image generation) and sound effects (via ElevenLabs) for The Four Corners mod, outputting directly into the correct resource pack structure.

**Status**: Not Started
**Depends on**: nothing
**Blocks**: nothing

## Tasks

- [ ] Project scaffolding
  - [ ] Create `tools/asset-generator/` directory with Python project structure
  - [ ] Set up `pyproject.toml` with dependencies (openai, elevenlabs, Pillow, click/typer)
  - [ ] Create `.env.example` for API keys (OPENAI_API_KEY, ELEVENLABS_API_KEY)
  - [ ] Add `tools/asset-generator/` to `.gitignore` for generated cache/temp files

- [ ] Asset registry / manifest system
  - [ ] Define a YAML/JSON manifest that maps mod content IDs to generation prompts
  - [ ] Include asset type (block_texture, item_texture, gui_element, sound_effect), target dimensions, and output path
  - [ ] Pre-populate manifest with all current and planned items from Design.md (Avalite Ore, Avalon Gem, Core Frame, dimensional materials, etc.)
  - [ ] Support the elemental palette from Design.md section 11 (Earth: moss/ochre/bronze, Water: teal/blue/silver, Air: white/pale gold, Fire: ember red/orange/black iron)

- [ ] Texture generation module (OpenAI)
  - [ ] Implement base prompt builder that enforces the "arcane-industrial" aesthetic from Design.md section 11
  - [ ] Support block textures (16x16 tileable) with Minecraft pixel-art style constraints
  - [ ] Support item textures (16x16) with transparency and Minecraft icon conventions
  - [ ] Support GUI textures (variable size) for machine interfaces
  - [ ] Post-process generated images: resize to target dimensions, quantize to Minecraft-appropriate palette, ensure tileability for block textures
  - [ ] Output directly to `src/main/resources/assets/fourcorners/textures/{block,item,gui}/` with correct filenames

- [ ] Sound generation module (ElevenLabs)
  - [ ] Implement sound effect generation for machine operations, elemental ambience, and UI feedback
  - [ ] Post-process audio: normalize levels, trim silence, convert to OGG Vorbis (Minecraft's sound format)
  - [ ] Output to `src/main/resources/assets/fourcorners/sounds/` with correct structure
  - [ ] Generate/update `sounds.json` registry file for Minecraft sound event binding

- [ ] CLI interface
  - [ ] `generate` command: generate assets for specific IDs, asset types, or all
  - [ ] `preview` command: generate to a staging folder for review before placement
  - [ ] `list` command: show all registered assets and their generation status
  - [ ] `validate` command: check existing assets against manifest for missing/outdated files
  - [ ] Dry-run mode that shows what would be generated without API calls
  - [ ] Cost estimation before generation (API token/character counts)

- [ ] Quality and safety
  - [ ] Caching layer to avoid re-generating unchanged assets (hash manifest entries)
  - [ ] Rate limiting for API calls
  - [ ] Backup existing assets before overwriting
  - [ ] Generation log with timestamps, prompts used, and API costs

- [ ] Legacy texture directory cleanup
  - [ ] Migrate any assets from `textures/blocks/` → `textures/block/` and `textures/items/` → `textures/item/`
  - [ ] Remove the legacy `blocks/` and `items/` directories
  - [ ] Verify all model JSON files reference the correct paths after migration

## Decisions

- (none yet)

## Notes

- The mod's aesthetic is "arcane-industrial" — metal, carved stone, crystal, glass, and rune motifs. Not pure sci-fi, not generic medieval fantasy. Prompts must enforce this consistently.
- Elemental palettes are defined in Design.md section 11 and should be baked into the prompt templates per element.
- Current codebase has textures in both `textures/block/` and `textures/blocks/` (and `item/` vs `items/`). The generator should use the standard Forge paths (`block/`, `item/`).
- Minecraft requires OGG Vorbis for sounds. ElevenLabs outputs will need format conversion.
- The manifest should be the single source of truth for what assets exist — useful beyond generation for auditing the resource pack.
