# Wisdom Crucible and Wisdom Fluid System

> A working Wisdom Crucible block that converts quest-earned Wisdom points into Wisdom fluid, with a custom fluid type, fluid tank, GUI with fluid level display, and Forge fluid capability support for piping to other machines.

**Status**: Not Started
**Depends on**: nothing (asset generation available via `tools/asset-generator/`)
**Blocks**: nothing

## Tasks

- [ ] Wisdom fluid registration
  - [ ] Create `WisdomFluid` extending ForgeFlowingFluid with source and flowing variants
  - [ ] Register fluid, fluid type, bucket item, and fluid block in registry layer
  - [ ] Define fluid properties (color, density, viscosity, luminosity) — visually distinct from water/lava; Design.md doesn't specify a color, so propose one for approval
  - [ ] Add fluid texture (still + flowing) to `assets/fourcorners/textures/block/`
  - [ ] Add fluid block model and blockstate
  - [ ] Add lang entries for Wisdom fluid and Wisdom bucket

- [ ] Remove deprecated Wisdom Ore and Wisdom Shard
  - [ ] Remove `wisdom_ore_block` and `wisdom_shard` from FCBlocks/FCItems registries
  - [ ] Remove associated blockstates, models, textures, loot tables, recipes, and tags
  - [ ] Remove `wisdom_ingot` from FCItems registry and all associated resources
  - [ ] Update creative tab to exclude removed items
  - [ ] Note: Design.md section 8.2 explicitly calls for this removal

- [ ] Wisdom Crucible block and block entity
  - [ ] Create `WisdomCrucibleBlock` extending `FCMenuBlock` with directional placement
  - [ ] Create `WisdomCrucibleBlockEntity` extending `FCMenuBlockEntity`
  - [ ] Internal fluid tank (FluidTank from Forge) for Wisdom fluid storage
  - [ ] Wisdom point input: accept Wisdom points (earned from tome quests) and convert to fluid at a defined ratio
  - [ ] Expose IFluidHandler capability for automated fluid extraction by pipes
  - [ ] NBT serialization for fluid tank state and any processing state
  - [ ] Register block, block entity, and menu type in registry layer

- [ ] Wisdom Crucible menu and GUI
  - [ ] Create `WisdomCrucibleMenu` extending `FCMenuBase`
  - [ ] Fluid tank display slot showing current Wisdom fluid level
  - [ ] Wisdom point input display (how many points available to convert)
  - [ ] Convert button or automatic conversion behavior
  - [ ] Progress indicator if conversion is timed rather than instant
  - [ ] Create `WisdomCrucibleScreen` extending `AbstractContainerScreen`
  - [ ] GUI texture for the Wisdom Crucible interface
  - [ ] Register screen in `FCClientSetup`

- [ ] Wisdom point tracking system
  - [ ] Define how Wisdom points are stored per player (capability, saved data, or NBT on the tome)
  - [ ] Create API for awarding Wisdom points (called by future tome quest completion)
  - [ ] Create API for spending Wisdom points at the Crucible
  - [ ] Placeholder command or item for testing Wisdom point grants before the tome quest system exists

- [ ] Crafting recipe for the Wisdom Crucible block
  - [ ] Define crafting recipe using Overworld materials (Avalon Ingots, Avalon Gem, Iron, etc.)
  - [ ] Add recipe JSON to `data/fourcorners/recipes/`
  - [ ] Add loot table for the block

- [ ] Data-driven content
  - [ ] Loot table for Wisdom Crucible block
  - [ ] Block tags (mineable tool, harvest level)
  - [ ] Recipe JSON for crafting the block

- [ ] Asset requirements (registered in `tools/asset-generator/manifest.yaml`)
  - [ ] `wisdom_crucible_block` — block texture: stone and metal basin with carved runes, golden-white fluid inside, ritual vessel aesthetic
  - [ ] `wisdom_crucible` — GUI texture (176x166): fluid tank display, wisdom point counter, convert button, rune decorations
  - [ ] `wisdom_bucket` — item texture: iron bucket filled with glowing golden-white wisdom fluid
  - [ ] `wisdom_fluid_still` — fluid still texture (not yet in manifest — must add when implementing fluid)
  - [ ] `wisdom_fluid_flow` — fluid flowing texture (not yet in manifest — must add when implementing fluid)
  - [ ] `wisdom_convert` — sound effect: alchemical conversion, liquid pouring with crystalline bubbling (1.5s)
  - [ ] `wisdom_gain` — sound effect: ascending crystal tones, enlightenment chime (1s)
  - [ ] Deprecated assets to remove after cleanup: `wisdom_ore_block`, `wisdom_shard`, `wisdom_ingot` (tagged `deprecated` in manifest)
  - [ ] Note: Run `asset-gen generate wisdom_crucible_block wisdom_crucible wisdom_bucket` to generate textures, or `asset-gen generate --tag knowledge` for all knowledge-related assets
  - [ ] Note: Fluid textures (still/flowing) need a different format than standard block textures — animated vertical strips with `.mcmeta`. These must be added to the manifest before generation.

## Decisions

- (none yet — key open decision: should Wisdom-to-fluid conversion be instant or timed? Design.md section 8.2 leans toward alchemical/ritual feel, suggesting a timed process may fit better)

## Notes

- Design.md section 8.2 is the canonical reference. Wisdom is earned through tome quests, not mining. The Crucible converts accumulated Wisdom points into Wisdom fluid.
- Wisdom Ore, Wisdom Shards, and Wisdom Ingots are explicitly deprecated in Design.md and should be removed as part of this task.
- The Wisdom fluid will be consumed by the Wisdom Enchanter (section 8.4) and by Elemental Core recipes in the Core Fabricator (section 8.6). Those are separate tasks but this fluid system is a prerequisite.
- Forge's FluidTank + IFluidHandler capability is the standard pattern for 1.20.1 fluid handling. This enables piping with other mods (Mekanism, Create, etc.) for free.
- The Crucible should feel "part alchemical refinery and part ritual vessel" per Design.md — the GUI and block model should reflect this.
- Consider: higher-tier catalysts or stabilized machine setups could improve Wisdom fluid yield per point spent (future upgrade path, not needed now).
- Asset generation pipeline is available at `tools/asset-generator/`. All Wisdom Crucible textures and sounds are pre-registered in `manifest.yaml`. Run `asset-gen list --tag knowledge` to see status.
- Fluid textures (still + flowing) are a gap in the current manifest — Minecraft fluid textures are animated vertical strips (typically 16x512 or 16x1024) with a `.mcmeta` file controlling frame timing. These need to be added to the manifest with a new `fluid_texture` convention before the fluid system is implemented.
- The three deprecated items (`wisdom_ore_block`, `wisdom_shard`, `wisdom_ingot`) are tagged `deprecated` in the asset manifest. After removing them from the registry, their texture files and manifest entries can be cleaned up together.
