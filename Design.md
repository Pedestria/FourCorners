# The Four Corners

### Design Document

A structured concept and progression plan for a tech-magic mega mod where elemental mastery drives exploration, industry, and world-scale transformation.

## 1. Purpose

The Four Corners is a large-scale Minecraft mod centered on one core promise: the player masters a world where technology, magic, and the four classical elements are all parts of the same system.

This document defines the mod's intended fantasy, progression, major systems, content priorities, and implementation direction for a multi-version Minecraft mod strategy that supports every major version from 1.12.x forward.

## 2. Vision

The mod should feel like a full expansion layer over vanilla Minecraft rather than a set of isolated features. The player starts with strange elemental materials and limited understanding, then builds toward industrial magic, world-scale infrastructure, and control over elemental forces.

The player journey should answer five questions:
- How do I discover elemental power?
- How do I refine and stabilize it?
- How do I automate it?
- How do I combine elements into stronger hybrid systems?
- What does true mastery let me change in the world?

## 3. Design Pillars

### 3.1 Tech and Magic Are One Tree

Magic is not an alternative to machinery, and machinery is not a replacement for magic. The mod's identity depends on both being required.
- Magic provides attunement, rituals, transmutation, world-shaping, and access to hidden states.
- Technology provides throughput, automation, storage, routing, measurement, and safety.
- Late-game systems should fail or underperform if the player ignores either side.

### 3.2 The Four Elements Must Matter Mechanically

The elemental theme cannot be cosmetic. Each element needs a strong gameplay identity with its own constraints, strengths, and visual language.
- Earth is stability, pressure, stone, structure, and growth.
- Water is flow, purification, chemistry, healing, and cooling.
- Air is motion, signaling, levitation, precision, and weather.
- Fire is heat, metallurgy, energy, volatility, and transformation.

### 3.3 Progression Should Layer, Not Replace

The mod should build depth by recontextualizing earlier materials and machines.
- Early resources stay relevant in later recipes.
- First-generation machines remain part of larger networks.
- Knowledge unlocks should expand player options instead of invalidating prior work.

### 3.4 The World Should Push Back

Elemental power should create risk, not just convenience.
- Unstable machines can overload.
- Rituals can distort weather or terrain.
- Rare content should live in dangerous places.
- The strongest rewards should require managing environmental hazards or system instability.

### 3.5 Scale Is a Feature

Four Corners is a mega mod. It should support both small handcrafted labs and large integrated bases.
- Solo players should be able to make compact elemental workshops.
- Multiplayer groups should be able to specialize and build districts.
- Infrastructure should become more interesting as the base grows.

## 4. Core Player Fantasy

The player is reconstructing a lost elemental framework and turning it into modern infrastructure.

Examples of the intended fantasy:
- an earth-stabilized forge complex that uses fire for smelting and water for thermal control
- an air relay network that coordinates remote machines and rituals
- a ritual chamber that converts purified elemental cores into high-tier machine components
- a dimension gateway that requires balanced elemental input instead of a single fuel type

The endgame should feel like elemental dominion rather than simple item accumulation.

## 5. Progression Model

### 5.1 Phase One: Discovery

The player encounters the mod through strange materials, low-tech crafting, and the first hints of elemental structure. This phase ends with the construction of the Dimension Accessor, giving the player their first gateway into the elemental realms.

Avalon Ingots should serve as the foundational item for constructing machines, structural blocks, and most major recipes across the mod.

Primary goals:
- find Avalite, begin forging Avalon Ingots, and uncover the first rare dimensional catalysts
- obtain the starter tome and begin completing its quests
- learn the first refinement steps
- build and activate the Dimension Accessor for the first time

Representative content:
- `avalite_ore_block`
- `avalon_ingot` (Deprecated)
- `avalon_gem`
- `core_frame`
- `start_tome`
- `dimension_accessor`

### 5.2 Phase Two: Exploration

The player enters the elemental dimensions for the first time, starting with the more accessible realms. Air and Water are the entry points: lower danger, readable environments, and rewarding early exploration. Earth and Fire come later, gated by both crafting requirements and the genuine difficulty of surviving those realms. Elemental knowledge is earned through discovery, not pre-unlocked through a formal attunement system.

Dimension access is gated by a combination of crafting prerequisites and danger level. Players are not forced into a fixed sequence, but the environment itself communicates readiness: Air and Water offer survivable first contact, while Earth and Fire demand preparation, gear, and materials gathered from earlier exploration.

Primary goals:
- explore the Flutter Isles (Air) and the Drowned World (Water)
- discover elemental materials, ruins, and dimensional mechanics through exploration
- unlock tome entries through dimensional finds and quest completion
- gather the crafting requirements and survivability needed to access Earth and Fire

Representative systems:
- dimension accessor travel
- dimensional ruins and guide structures
- tome quests unlocking elemental knowledge
- elemental materials and catalysts sourced from each realm

### 5.3 Phase Three: Fabrication

Magic becomes industrial. This is where the mod starts feeling like a mega mod instead of a resource pack with recipes.

Primary goals:
- automate the first real loop
- build machine networks
- route item, fluid, and elemental resources
- manage heat, pressure, or instability

Representative systems:
- core fabricators
- elemental storage
- transfer networks
- machine upgrades

### 5.4 Phase Four: Synthesis

The player combines disciplines and builds hybrid infrastructure.

Primary goals:
- intentionally mix elemental mechanics
- solve multi-system engineering problems
- unlock advanced transport, crafting, and control tools

Representative systems:
- hybrid machines
- cross-element rituals
- compound materials
- network logic and safety automation

### 5.5 Phase Five: Dominion

The player uses elemental mastery to alter the world at large scale.

Primary goals:
- control environmental systems
- access elemental realms or nexus spaces
- build prestige infrastructure
- complete major progression milestones

Representative systems:
- deeper dimensional secrets and locked realm areas
- biome and weather control
- world events
- endgame reactors or ascendant structures

## 6. Elemental Identity

### 6.1 Earth

Earth is the element of stability, material growth, weight, and defense.

Gameplay roles:
- ore amplification
- terrain shaping
- structural reinforcement
- pressure-based machines
- passive production and growth systems

Content examples:
- pressure drill
- stabilizer pylon
- crystal growth chamber
- defensive stone-infused gear

### 6.2 Water

Water is the element of control through flow, cleansing, and reaction management.

Gameplay roles:
- fluid routing
- purification
- coolant behavior
- reagent preparation
- healing or restoration

Content examples:
- purifier
- alchemical basin
- coolant loop
- ritual pool

### 6.3 Air

Air is the element of speed, signaling, motion, and awareness.

Gameplay roles:
- transport acceleration
- levitation and gliding
- sensors and relay logic
- remote activation
- weather interaction

Content examples:
- wind engine
- relay beacon
- storm harness
- sensor array

### 6.4 Fire

Fire is the element of power, transformation, and dangerous output.

Gameplay roles:
- smelting and forging
- energy generation
- fuel conversion
- heat-based crafting
- volatile overdrive

Content examples:
- forge reactor
- crucible
- thermal battery
- overheat venting systems

### 6.5 Proposed Dimension Names

To give each realm a stronger identity than the current placeholder element names, the following names are recommended:

Air: The Flutter Isles

A high-altitude realm of floating landmasses, cloudstone ruins, and violent wind channels. This name fits a dimension built around sky islands, gliding, updrafts, and storm-driven traversal.

Earth: The Saharamu

A split realm where enchanted forests give way to vast golden deserts filled with weathered sandstone strongholds and sandcastle-like ruins. The name supports both organic growth and ancient, sun-scorched earth magic.

Water: The Drowned World

A dark oceanic world shaped by abyssal waters, flooded caverns, and massive underground chambers. The name conveys depth, pressure, mystery, and the damp, hostile tone of an underwater cave dimension.

Fire: The Mordo

An intensified Nether-like realm defined by volcanic foundries, collapsing basalt ranges, ash storms, and extreme heat. The name suggests both raw destruction and a forge where powerful materials are transformed.

Naming Note

Together, these names create a more cohesive tone for the mod. They feel like places players would travel to, learn, and master, rather than generic elemental labels.

### 6.6 Proposed Elemental Tools, Machines, and Spells

The mod will benefit from giving each element a recognizable gameplay kit. These proposals translate elemental identity into tools, machines, rituals, and utility systems that players can immediately associate with each realm.

Earth - construction, substance, agriculture, and terraforming

Tools and machines:
- Terra Hammer - a heavy utility tool that rapidly places or reshapes blocks in a short area, useful for excavation, retaining walls, terraces, and bunker-style construction.
- Geodrill - an earth-aligned mining machine that bores through stone veins, improves ore extraction, and can expose buried structures or compressed resource pockets.
- Rootbinder Plow - an agriculture-focused implement that tills larger plots, enriches soil, and improves crop stability in harsh terrain.
- Stonewake Press - a compaction and fabrication machine that turns raw earth materials into bricks, reinforced blocks, road surfaces, and structural components.
- Verdant Engine - a terraforming machine that spreads grass, moss, fertile soil, or controlled biome conversion across a defined area.

Spells and rituals:
- Raise Bastion - summons temporary walls, pillars, or earthen shields for defense or battlefield shaping.
- Seismic Survey - reveals underground cavities, ore clusters, pressure pockets, or buried ruins in a wide radius.
- Grovewake Rite - accelerates plant growth, tree restoration, and land healing around farms, forests, or damaged terrain.

Air - motion, signaling, traversal, and precision

Tools and machines:
- Gale Harness - a wearable traversal tool that improves gliding, midair correction, launch height, and fall control between islands or cliffs.
- Jetstream Rail - a transport system that pushes entities, minecarts, or item carriers along high-speed aerial lanes.
- Relay Spire - a signaling structure that links distant bases, transmits machine states, and enables remote activation or automation logic.
- Wind Loom - a precision crafting machine that uses controlled airflow for sorting, lightweight assembly, and fine component handling.
- Storm Condenser - a weather machine that stores charge from wind and storms, then converts it into power or atmospheric rituals.

Spells and rituals:
- Zephyr Step - grants short aerial dashes, boosted jumps, and limited hover control for exploration and combat.
- Eye of the Current - highlights moving entities, airborne hazards, projectiles, or redstone-like state changes for awareness and timing.
- Tempest Call - bends local weather, creating gust fronts, cloud cover, lightning risk, or traversal updrafts.

Water - flow, depth, chemistry, and restoration

Tools and machines:
- Tidecutter - an underwater utility tool that clears waterlogged spaces, harvests aquatic resources, and cuts channels through sediment or coral growth.
- Abyssal Pump - a high-capacity fluid machine for draining, redirecting, filtering, or pressurizing water in bases and caverns.
- Brine Still - a chemistry and purification station that separates fluids into reagents, clean water, coolant, and alchemical inputs.
- Current Lattice - a routing network that moves fluids and dissolved materials efficiently across large facilities.
- Renewal Basin - a restorative machine that supports healing, cleansing, potion refinement, and recovery from heat or corruption.

Spells and rituals:
- Undertow Grasp - slows enemies, drags targets, or manipulates movement through currents and pressure.
- Purge Tides - removes poison, heat buildup, instability, or contamination from players, machines, or ritual spaces.
- Hollowsea Rite - floods, drains, or stabilizes cavern systems to make hidden paths, flooded dungeons, and pressure zones navigable.

Fire - heat, metallurgy, power, and violent transformation

Tools and machines:
- Ember Lance - a high-risk combat and utility tool that projects focused heat for cutting, ignition, and short-range burst damage.
- Inferno Forge - an advanced smelting and alloying station for high-tier metals, catalysts, and heat-treated machine parts.
- Magma Turbine - a power generator that turns lava, combustion, or thermal gradients into sustained industrial output.
- Ash Reactor - a volatile overdrive machine that trades safety for extreme production speed, heat, and conversion throughput.
- Crucible Kiln - a transformation chamber for refining unstable materials, burning impurities, and forcing difficult transmutations.

Spells and rituals:
- Cinder Surge - releases a cone or wave of heat that ignites terrain, scorches enemies, and can jump-start certain machines.
- Forgeheart - temporarily boosts smelting speed, energy output, and metalworking efficiency at the cost of rising instability.
- Caldera Rite - triggers volcanic or Nether-like environmental events such as lava emergence, ashfall, or thermal fractures for controlled large-scale transformation.

Design note

Together, these kits give each element a strong promise: Earth builds and reshapes, Air moves and coordinates, Water controls and restores, and Fire powers and transforms. That makes it easier for players to understand specialization, machine lines, and spell schools at a glance.

## 7. Major Systems

### 7.1 Knowledge and Research

The mod needs a knowledge layer so players are guided without trivializing discovery. The tome is the primary interface for this, presenting quests that players complete as they explore each dimension and engage with the mod’s systems. Completing quests is the main way Wisdom is earned.

Design goals:
- use the starter tome as the primary interface for progression and quest tracking
- unlock tome entries based on dimensional discoveries, crafted milestones, and completed quests
- gate advanced recipes behind understanding earned through play, not only materials
- award Wisdom for completing quests, making the tome an active reward loop rather than a passive reference

Without a knowledge layer, a mega mod becomes opaque. The tome turns content volume into readable progression, and its quests give players clear direction without forcing a rigid path through the world.

### 7.2 Machines

Machines are the backbone of the industrial side of the mod.

Machine rules:
- every machine should have a strong elemental role
- machines should refine, convert, stabilize, route, or synthesize
- late-game machine chains should require multiple infrastructure layers
- upgrades should change behavior, not only speed

Suggested tiers:
- Primitive
- Stabilized
- Resonant
- Ascendant

### 7.3 Rituals

Rituals are the slow, high-impact, context-sensitive counterpart to machines.

Ritual rules:
- rituals should care about placement, timing, surrounding blocks, and elemental balance
- rituals should enable actions machines cannot do alone
- rituals should integrate with machines instead of replacing them

Representative ritual uses:
- dimensional calibration and realm stabilization
- transmutation
- weather modification
- dimensional tuning
- summoning or challenge events

### 7.4 Elemental Resource Networks

Avoid collapsing the mod into one generic power bar. Distinct resources produce better decisions and better base design.

Recommended model:
- matter flows through items and fluids
- machine state depends on heat, pressure, charge, essence, or balance
- high-tier devices consume mixed elemental inputs
- conversion is possible, but always lossy or risky

This keeps the elements mechanically relevant all the way into the late game.

### 7.5 Automation

Automation is a major long-term goal, but it should stay expressive.

Automation goals:
- item transport
- fluid transport
- elemental routing
- machine sequencing
- load balancing
- overload protection

The strongest automation setups should feel engineered, not merely scaled-up crafting tables.

### 7.6 World Content

The mod should create places worth traveling to and learning from.

World content targets:
- biome-linked elemental deposits
- ruined sanctums and industrial remnants
- instability zones
- rare catalysts in dangerous structures
- future elemental realm access

Structures should do four things:
- reward exploration
- teach the mod's themes
- foreshadow future mechanics
- deliver unique loot or knowledge

### 7.7 Vehicles

Vehicles are multi-component structures built from individual blocks placed in the world. Once assembled and activated, the vehicle moves as a single entity that the player can board and pilot. They operate in every dimension — Overworld, Nether, End, and all four elemental realms — making them core tools for long-range exploration and infrastructure work. The first two vehicle types are the Air Ship and the Water Ship.

Vehicle design rules:
- vehicles are assembled from component blocks placed by the player, not crafted as single items
- component blocks include structural hull pieces, a helm or control block, propulsion blocks, and optional utility modules
- the helm block activates the assembled structure and determines what counts as part of the vehicle
- vehicles function in all dimensions; elemental realm environments may impose additional requirements or offer bonuses to matched vehicle types
- utility modules are interchangeable, allowing players to configure vehicles for different missions rather than building separate ships for each role

Universal vehicle roles:
- mobile storage: chest and barrel modules carried with the ship, accessible while docked or in transit
- mobile crafting platform: machine modules mounted on the ship allow basic processing or crafting while underway
- combat platform: weapon mounts and shielding modules allow ships to engage hostile dimensional environments or enemy structures
- exploration tool: scanner modules detect ore deposits, hidden structures, elemental anomalies, or dimensional instability in a radius around the ship
- cargo transport: large hold configurations allow bulk movement of resources between bases across dimensions

### 7.7.1 Air Ship

The Air Ship is a flying vehicle built around Air elemental propulsion. It excels at rapid traversal of open sky environments, making it the primary vehicle for the Flutter Isles and high-altitude Overworld exploration, while remaining functional in any other dimension with open airspace.

Key components:
- Hull Planks: lightweight structural blocks that form the body of the ship; material tier affects durability and maximum size
- Air Helm: the control block that activates the ship and defines its bounding structure; the player boards here to pilot
- Wind Engine: propulsion block that drives horizontal movement; more engines increase top speed and acceleration
- Lift Balloon: provides altitude control and buoyancy; required for flight; quantity and quality affect ceiling height and ascent speed
- Gale Condenser: optional module that harvests wind charge from the environment during flight, storing it as fuel or feeding it to onboard machines
- Relay Spire Mount: optional module that extends the ship’s signaling range, useful for coordinating remote bases or automation networks while airborne

Design notes:
- Air Ships built with Flutter Isles materials gain passive speed bonuses while flying in the Flutter Isles dimension
- operating in the Mordo or other fire-heavy environments imposes heat buildup on hull components over time without cooling modules installed
- minimum viable ship requires one Air Helm, at least one Wind Engine, and at least one Lift Balloon; all other components are optional modules

### 7.7.2 Water Ship

The Water Ship is a surface and submersible vessel built around Water elemental propulsion. It is the primary vehicle for ocean traversal, the Drowned World, and any flooded cave systems or dimensional waterways. Unlike the Air Ship, the Water Ship can optionally operate below the surface, making it uniquely suited for deep exploration.

Key components:
- Hull Planks: structural blocks forming the body; water-treated or coral-reinforced variants resist pressure damage at depth
- Water Helm: the control block that activates the ship and governs surface versus submersible mode switching
- Current Drive: propulsion block that pushes the ship through water using directed flow; more drives increase speed and maneuverability
- Pressure Ballast: controls depth for submersible operation; required to dive; quantity affects dive speed and maximum depth
- Brine Collector: optional module that harvests fluid reagents and purified water from the surrounding environment while the ship is underway, feeding onboard processing machines
- Sonar Array: optional exploration module that maps underwater terrain, detects submerged ruins, and highlights ore deposits or dimensional anomalies below the ship

Design notes:
- Water Ships built with Drowned World materials resist pressure damage at depth and gain passive sonar range bonuses in that dimension
- surface mode and submersible mode are toggled from the Water Helm; switching requires the ship to be stationary or nearly so
- minimum viable ship requires one Water Helm and at least one Current Drive; Pressure Ballast is required only if submersible operation is intended
- operating in lava-heavy environments such as the Mordo requires heat-resistant hull materials; standard hull planks degrade rapidly in those conditions

## 8. Flagship Blocks

### 8.1 Core Fabricator

The Core Fabricator should become the central midgame synthesis machine.

Intended role:
- combine refined elemental components into structured cores
- bridge basic resources into advanced machines and rituals
- reward balanced inputs instead of raw quantity alone

Design direction:
- accepts multiple ingredients
- can gain efficiency or recipe access from elemental alignment
- may require temperature or stability management
- should be the first machine that makes hybrid progression obvious

Current implementation note:

The current implementation already has a block entity, menu, and screen for the Core Fabricator, but not full crafting behavior yet. Version support should preserve its gameplay identity even when backend hooks differ across releases.

### 8.2 Wisdom Crucible

The Wisdom Crucible is the machine that converts accumulated Wisdom into the fluid resource required for higher-order crafting. Wisdom itself is earned by completing quests listed in the tome — it is a reward for engagement with the world, not a product of grinding XP or mining specific ores.

Wisdom Ore and Wisdom Shards should be removed from the item set entirely. The mechanic should remain tied to quest completion and dimensional exploration, keeping Wisdom scarce and meaningful rather than farmable.

Intended role:
- receive Wisdom earned through tome quests and convert it into Wisdom fluid for crafting
- act as the bottleneck resource generator for Elemental Cores and other advanced recipes
- make players choose which advanced systems to invest in, since Wisdom supply scales with quest effort

Design direction:
- should feel part alchemical refinery and part ritual vessel
- higher-tier catalysts or stabilized machine setups could improve Wisdom fluid yield per point spent
- different dimensions and quest chains should produce different grades or types of Wisdom, allowing travel balance to scale with destination danger

### 8.3 Dimension Accessor

The Dimension Accessor is the player’s gateway into the elemental realms, unlocked early in Phase One as a first major crafting milestone. It is not a late-game reward — it is the starting gun for the exploration-driven progression model.

Intended role:
- provide early access to the elemental dimensions once the basic Avalite progression is complete
- tune access to each elemental realm through dimension-specific crafting requirements and danger gating
- serve as a machine-ritual hybrid rather than a simple portal block

Design direction:
- requires Elemental Cores crafted in the Core Fabricator; each core targets a specific dimension
- Air and Water cores are crafted with early-game materials; Earth and Fire cores require materials gathered from earlier dimensional exploration
- interacts with world state, location, or elemental balance
- may expose failure states such as unstable breaches or hostile events on poorly prepared access attempts

Gating loop:
- the Dimension Accessor is built early as the culmination of Phase One crafting
- Air and Water are accessible first — lower crafting cost, lower danger, open exploration
- Earth and Fire require materials and knowledge sourced from Air and Water exploration, creating a natural cross-dimensional dependency
- core-quarters create room for sub-element identity and recipe variety instead of reducing each realm to one generic ingot
- the Core Fabricator becomes the mandatory bridge between elemental crafting and exploration, reinforcing it as a signature machine

Current implementation note:

The current implementation already has a block entity, menu, and screen for the Dimension Accessor, but not its final gameplay behavior. Cross-version support should keep the player-facing function consistent even if portal, menu, or registry plumbing changes by release.

### 8.4 Wisdom Enchanter

The Wisdom Enchanter is a mid-game machine that infuses items with Wisdom fluid to produce upgraded “Wise” variants. It bridges the Wisdom Crucible’s fluid output with the Core Fabricator’s recipe requirements, and is the sole source of Wise Avalon Gems. Because it consumes Wisdom fluid over time during processing, the Enchanter creates a meaningful tension between Wisdom supply and crafting throughput — rushing a batch with low reserves risks wasting both the input item and the fluid.

8.4.1 Interface and Inputs

The Wisdom Enchanter has three slots: one item input, one fluid input, and one item output. The fluid slot accepts Wisdom fluid only, supplied either by piping directly from a Wisdom Crucible or fluid transport network, or by manually inserting a Wisdom-filled bucket. Both supply methods are fully supported and functionally equivalent.
- Item input slot: accepts the item to be enchanted; currently only Avalon Gems are valid inputs
- Fluid input slot: accepts a Wisdom bucket for manual filling, or connects to a fluid pipe for automated supply; the internal fluid tank displays current Wisdom level in the GUI
- Output slot: produces the Wise variant of the input item once enchantment completes successfully; must be emptied before a new cycle can begin

8.4.2 Processing Behavior

Enchantment is not instantaneous. Once a valid item and sufficient Wisdom fluid are present, the Enchanter begins a timed process during which it steadily draws down the fluid tank. The GUI displays a progress bar alongside the current fluid level so the player can monitor both at a glance.
- a full Wise Avalon Gem cycle consumes 16 Wisdom fluid and takes approximately 30 seconds at base speed
- Wisdom fluid is consumed gradually throughout the process, not all at once at the start; this means supply interruptions mid-cycle have consequences
- if the output slot is occupied when a cycle completes, the machine halts and holds the result internally until the slot is cleared; no fluid or input is wasted in this case

8.4.3 Failure States

The Wisdom Enchanter has two failure conditions, both of which punish poor planning without being permanently destructive.

**Interrupted cycle (Wisdom fluid runs dry mid-process):**
- if Wisdom fluid is exhausted before the cycle completes, the process stalls and the progress bar freezes
- progress is not lost immediately; the machine holds its state for a short grace window (approximately 10 seconds) during which supplying more Wisdom fluid will resume the cycle without penalty
- if the grace window expires without fluid being restored, the cycle fails: the input item is returned to the input slot in a Fractured state (Fractured Avalon Gem), and all Wisdom fluid consumed up to that point is lost
- a Fractured Avalon Gem can be re-smelted back into a regular Avalon Gem in a furnace, recovering the material at the cost of time; nothing is permanently destroyed

**Degraded output (Wisdom fluid critically low at cycle start):**
- if a cycle is started with fluid levels below the minimum threshold (8 Wisdom fluid for a Wise Avalon Gem), the machine will attempt the enchantment but produce a Cracked Wise Avalon Gem instead of a full Wise Avalon Gem
- a Cracked Wise Avalon Gem functions at reduced potency and cannot be substituted for a full Wise Avalon Gem in Core Fabricator recipes; it can be re-enchanted in the Wisdom Enchanter with a smaller Wisdom cost (8 fluid) to upgrade it to a full Wise Avalon Gem
- the GUI warns the player with a visual indicator when the tank is below the minimum threshold before a cycle begins, giving them a chance to top up before starting

8.4.4 Automation Notes

The Wisdom Enchanter is designed to fit into automated production lines, with some intentional friction to prevent trivial mass production of Wise Avalon Gems.
- Wisdom fluid can be piped in continuously from a Wisdom Crucible; a stable supply pipeline eliminates interruption risk entirely
- items can be piped into the input slot and extracted from the output slot automatically using item transport systems
- the Enchanter processes one item at a time; batching multiple Wise Avalon Gems requires either multiple Enchanters in parallel or sequential processing through a single machine
- because Wisdom production from the Crucible is quest-gated and cannot be infinitely accelerated, the Enchanter’s throughput is naturally bounded by how much Wisdom the player has earned; automation does not break this ceiling, it just removes manual interaction from the equation

8.4.5 Expansion Note

The Wisdom Enchanter is currently scoped to Wise Avalon Gems only. The two-slot input architecture (item + fluid) is intentionally generic and can support additional “Wise” item variants in future updates without requiring machine redesign. Any new enchantable item should follow the same pattern: a defined Wisdom fluid cost, a timed process, and a degraded output state when fluid is insufficient.

### 8.5 Dimensional Materials Reference

Every recipe in the Core Fabricator draws from a defined pool of materials sourced from the Overworld and the four elemental dimensions. This section serves as the canonical reference for what each dimension produces and how those materials are obtained. Rarity tiers are noted to inform recipe cost and balance decisions.

Overworld (Phase One):
- Avalite Ore — mined from the Overworld; smelts into Avalon Ingots [common]
- Avalon Gem — crafted from 4 Avalon Ingots in a 2x2 pattern; used in higher-tier recipes [uncommon]
- Core Frame — crafted from 1 Avalon Gems in the middle, and 7 Iron Ingots all around; the structural base for all Elemental Cores [uncommon]
- Wise Avalon Gem— refined in the Wisdom Enchanter from Avalon Gems and Wisdom; used across mid- and late-game recipes [uncommon]

Air /Flutter Isles:
- Flutterstone — the native stone of the Flutter Isles; mined from floating landmasses [common]
- Aero-Dust — Drops from Weightless Sand and wind-aligned mobs; used in most Air recipes [common]
- Aero-Thread — harvested from flying creatures and cloud-flora; used in flexible and structural recipes [uncommon]
- Storm Crystal — found in cloudstone ruins and generated during storm events; used in precision and power recipes [rare]

Water /Drowned World:
- Tearstone — the native stone of the Drowned World; mined from flooded cavern walls [common]. (Backstory: Made from Tear Angels that created this world)
- Tear Quartz— harvested from Tear Quartz formations; used in purification and alloy recipes [common]
- Angel Hair — harvested from aquatic creatures; used in membrane and hull recipes [uncommon]
- Heart of the Ocean — found in deep-level mob drops and buried chests; used in cross-element and advanced recipes [rare]

Earth /Saharamu:
- Heavy Sand/Heavy Dirt — the native stone/dirt of the Saharamu desert/forest zones; mined freely [common]
- Amberlite — broken from fossilized formations in the Saharamu; used in stabilization recipes [common]
- Rustic Ore / Rustic Ingot — mined from the Saharamu and smelted; primary Earth metal for tools, machines, and alloys [uncommon]
- Pressurized Geode — found in deep underground pressure zones; used in cross-element and Ascendant recipes [rare]

Fire / Mordo:
- Molten Rock — the native stone of the Mordo; mined from cooled volcanic zones [common]
- Volcanic Glass — formed where lava meets cooled rock; used in heat-resistant and transformation recipes [common]
- Volcanic Iron Ore / Volcanic Iron Ingot — mined from volcanic foundry zones and smelted; primary Fire metal for energy and heat recipes [uncommon]
- Volcanic Ash — a byproduct of extreme volcanic activity, found in the deepest foundry zones; used in cross-element and Ascendant recipes [rare]

### 8.6 Elemental Core Recipes

Each Elemental Core is assembled in the Core Fabricator from one Core Frame and four Core-Quarters specific to the target dimension. Core-Quarters are intermediate components also made in the Core Fabricator. The final core also consumes a quantity of Wisdom fluid, with cost scaling upward for more dangerous dimensions. Earth and Fire Core-Quarters intentionally require rare materials from earlier dimensions, creating a cross-dimensional dependency that rewards thorough exploration before attempting those realms.

Air Core-Quarters (Flutter Isles materials):
- Gale Quarter: 3 Aero-Dust + 1 Avalon Ingot → 1 Gale Quarter
- Current Quarter: 4 Aero-Thread + 1 Avalon Ingot → 1 Current Quarter
- Storm Quarter: 1 Storm Crystal + 2 Aero-Dust + 1 Avalon Gem → 1 Storm Quarter
- Aether Quarter: 2 Storm Crystal + 1 Wise Avalon Gem → 1 Aether Quarter

Air Elemental Core:
- 1 Core Frame + 1 Gale Quarter + 1 Current Quarter + 1 Storm Quarter + 1 Aether Quarter + 4 Wisdom fluid → 1 Air Elemental Core

Water Core-Quarters (Drowned World materials):
- Tide Quarter: 3 Tear Quartz + 1 Avalon Ingot → 1 Tide Quarter
- Depth Quarter: 1 Heart of the Ocean + 3 Tearstone + 1 Avalon Ingot → 1 Depth Quarter
- Flow Quarter: 4 Angel Hair + 1 Avalon Gem → 1 Flow Quarter
- Hollow Quarter: 2 Heart of the Ocean + 1 Wise Avalon Gem → 1 Hollow Quarter

Water Elemental Core:
- 1 Core Frame + 1 Tide Quarter + 1 Depth Quarter + 1 Flow Quarter + 1 Hollow Quarter + 8 Wisdom fluid → 1 Water Elemental Core

Earth Core-Quarters (Saharamu materials + cross-dimensional ingredients from Air and Water):
- Root Quarter: 3 Heavy Sand + 1 Amberlite + 1 Avalon Ingot → 1 Root Quarter
- Stone Quarter: 2 Amberlite + 2 Rustic Ingot + 1 Avalon Gem → 1 Stone Quarter
- Growth Quarter: 1 Pressurized Geode + 2 Amberlite + 1 Aero-Dust [Air] → 1 Growth Quarter
- Press Quarter: 2 Rustic Ingot + 1 Heart of the Ocean [Water] + 1 Wise Avalon Gem → 1 Press Quarter

Earth Elemental Core:
- 1 Core Frame + 1 Root Quarter + 1 Stone Quarter + 1 Growth Quarter + 1 Press Quarter + 16 Wisdom fluid → 1 Earth Elemental Core

Fire Core-Quarters (Mordo materials + cross-dimensional ingredients from Air, Water, and Earth):
- Ember Quarter: 3 Volcanic Iron Ingot + 2 Volcanic Glass + 1 Avalon Ingot → 1 Ember Quarter
- Ash Quarter: 4 Volcanic Glass + 2 Molten Rock + 1 Avalon Gem → 1 Ash Quarter
- Forge Quarter: 2 Volcanic Iron Ingot + 1 Rustic Ingot [Earth] + 1 Storm Crystal [Air] → 1 Forge Quarter
- Infernal Quarter: 1 Volcanic Ash + 2 Volcanic Glass + 1 Heart of the Ocean [Water] + 1 Wise Avalon Gem → 1 Infernal Quarter

Fire Elemental Core:
- 1 Core Frame + 1 Ember Quarter + 1 Ash Quarter + 1 Forge Quarter + 1 Infernal Quarter + 24 Wisdom fluid → 1 Fire Elemental Core

### 8.7 Core Fabricator Recipe Reference

The Core Fabricator handles all synthesis that goes beyond vanilla crafting. Its recipes are organized into four tiers based on the dimensions required to source the ingredients. Tier 1 uses only Overworld materials. Tier 2 requires one elemental dimension. Tier 3 requires two or more. Tier 4 requires all four and consumes Wisdom fluid. Recipes within each tier are listed by elemental category.

Tier 1 — Basic Synthesis (Overworld only):
- Wise Avalon Gem: 1 Avalon Gem + Wisdom (in Wisdom Enchanter) → 1 Wise Avalon Gem
- Core Frame: 4 Avalon Ingots (ring) → 1 Core Frame

Tier 2 — Single-Element Synthesis:

Air recipes (Flutter Isles):
- Skyweave Plate: 4 Aero-Thread + 2 Aero-Dust + 1 Wise Avalon Gem → 1 Skyweave Plate (lightweight structural panel used in Air Ship hulls and armor)
- Storm Coil: 2 Storm Crystal + 3 Aero-Dust + 1 Wise Avalon Gem → 1 Storm Coil (machine component used in sensors, relay beacons, and the Scout Array)
- Gale Capacitor: 3 Storm Coil + 2 Skyweave Plate + 1 Avalon Gem → 1 Gale Capacitor (Air Ship vehicle component; stores elemental charge for flight outside the Flutter Isles)

Water recipes (Drowned World):
- Abyssal Alloy Ingot: 3 Tearstone + 2 Tear Quartz + 1 Avalon Ingot → 2 Abyssal Alloy Ingots (dense Water-element metal used in hull plating, machine casings, and anchor components)
- Tidebound Membrane: 4 Angel Hair + 1 Heart of the Ocean + 1 Wise Avalon Gem → 1 Tidebound Membrane (flexible Water-element material used in the Pressure Hull vehicle component and fluid-routing machines)
- Buoyancy Core: 3 Tidebound Membrane + 2 Abyssal Alloy Ingot + 1 Avalon Gem → 1 Buoyancy Core (Water Ship vehicle component; provides surface float and ballast control)

Earth recipes (Saharamu):
- Rustic Steel Ingot: 3 Rustic Ingot + 1 Amberlite + 1 Wise Avalon Gem → 2 Rustic Steel Ingots (high-strength Earth alloy used in structural machine blocks, reinforced hulls, and Earth-tier gear)
- Pressured Core Block: 2 Pressurized Geode + 3 Heavy Sand + 1 Rustic Steel Ingot → 1 Pressured Core Block (structural machine component used in Earth-tier fabricators and terrain-shaping devices)

Fire recipes (Mordo):
- Ember Alloy Ingot: 3 Volcanic Iron Ingot + 2 Volcanic Glass + 1 Wise Avalon Gem → 2 Ember Alloy Ingots (high-heat Fire metal used in forge machines, energy storage, and Fire-tier gear)
- Infernal Casing: 2 Volcanic Ash + 3 Volcanic Glass + 1 Ember Alloy Ingot → 1 Infernal Casing (volatile machine casing used in Ash Reactors, overdrive components, and Fire-tier machine housings)

Tier 3 — Cross-Element Synthesis (two or more dimensions required):

Air + Water:
- Aero-Tear Catalyst: 2 Aero-Dust + 2 Tear Quartz + 1 Wise Avalon Gem → 1 Aero-Tear Catalyst (a versatile cross-element reagent used in ritual preparation, alchemical basins, and hybrid machine recipes)
- Cloudweave Hull Plate: 3 Aero-Thread + 3 Abyssal Alloy Ingot + 1 Wise Avalon Gem → 1 Cloudweave Hull Plate (a buoyant yet lightweight panel used in advanced Air Ship and Water Ship hulls)

Air + Water + Earth:
- Triweave Composite: 1 Skyweave Plate + 1 Tidebound Membrane + 1 Rustic Steel Ingot + 1 Wise Avalon Gem → 1 Triweave Composite (a three-element structural material used in Resonant-tier machine housings and advanced vehicle upgrades)
- Stabilized Elemental Lens: 1 Storm Crystal + 1 Heart of the Ocean + 1 Pressurized Geode + 2 Wise Avalon Gems → 1 Stabilized Elemental Lens (a precision component used in scanner arrays, sensor systems, and ritual calibration devices)

Air + Water + Earth + Fire:
- Ember-Rustic Alloy Ingot: 2 Ember Alloy Ingot + 2 Rustic Steel Ingot + 1 Aero-Tear Catalyst → 2 Ember-Rustic Alloy Ingots (a four-element metal used in late-game machine frames and weapon mounts)

Tier 4 — Ascendant Synthesis (all four dimensions + Wisdom fluid required):
- Ascendant Core Shard: 1 Storm Crystal + 1 Heart of the Ocean + 1 Pressurized Geode + 1 Volcanic Ash + 2 Wise Avalon Gems + 32 Wisdom fluid → 1 Ascendant Core Shard (a high-tier crafting component used in endgame reactors, ascendant machines, and prestige infrastructure)
- Elemental Convergence Plate: 1 Skyweave Plate + 1 Tidebound Membrane + 1 Rustic Steel Ingot + 1 Ember Alloy Ingot + 1 Wise Avalon Gem + 48 Wisdom fluid → 1 Elemental Convergence Plate (a four-element structural panel used in ascendant-tier machines, dimensional infrastructure, and high-end vehicle components)
- Nexus Capstone: 2 Ascendant Core Shard + 1 Elemental Convergence Plate + 4 Ember-Rustic Alloy Ingot + 64 Wisdom fluid → 1 Nexus Capstone (the primary crafting component for endgame structures; intended as the culminating synthesis target of the progression system)

## 9. Vehicles

Vehicles are large, player-built structures assembled from multiple placed components. They function as mobile platforms that carry players, cargo, machines, and storage across any dimension. Air Ships and Water Ships are the two vehicle types planned for initial release, but the component system is designed to support future vehicle types without significant rework.

Vehicles are not crafted as items and placed like blocks. They are constructed in the world from individual components, each with its own function, and activated as a unified craft once the required components are in place. This means no two ships need to look or perform identically — a small fast scout and a heavy cargo hauler are both valid expressions of the same system.

### 9.1 Shared Vehicle Design Principles

All vehicles share the same underlying component system and design philosophy regardless of type.

Core rules:
- vehicles are assembled from individually placed components in the world; there is no single “vehicle item” to craft
- a helm or control block activates the assembled structure as a vehicle once minimum component requirements are met
- vehicles operate across all dimensions; they are not restricted to their elemental home realm
- components determine capability: a ship with more storage blocks carries more; a ship with weapon mounts supports combat; a ship with a scanner array gains detection abilities
- elemental materials sourced from each dimension can be used to upgrade or specialize vehicle components

Vehicle roles:
- mobile storage: cargo holds and item storage blocks can be installed on any vehicle, allowing ships to carry large quantities of materials between locations
- mobile crafting and machine platform: machines and crafting stations can be placed on the vehicle hull and remain functional during travel, enabling players to work while in transit
- combat platform: weapon mounts, elemental cannons, and defensive plating can be added to vehicles for use in hostile dimensions or against world threats
- exploration and detection: scanner arrays and sensor components allow vehicles to detect ore deposits, elemental anomalies, hidden structures, or dimensional instabilities within a radius
- cargo transport: dedicated hauler configurations with high-capacity holds support base-to-base logistics and inter-dimensional supply runs

### 9.2 Air Ships

Air Ships are flying platforms powered by Air elemental components. They excel at high-speed traversal, vertical movement, and precision navigation across open skies. In the Flutter Isles they gain additional performance from the natural wind currents of the dimension. In other dimensions they operate on stored elemental charge.

Identity: speed, height, agility, and awareness. Air Ships are the scouts and couriers of the vehicle system. They are harder to arm heavily without sacrificing performance, and their open-sky nature makes them well-suited to scanner and sensor loadouts.

Core components:
- Air Helm — the control block that activates the vehicle; the player pilots from this position
- Wind Engine — the propulsion component; more engines increase speed and payload capacity
- Lift Vane — provides altitude control and hover stability; required for vertical ascent
- Gale Capacitor — stores elemental Air charge used to power the ship outside wind-rich dimensions
- Scout Array — an optional sensor component for detecting terrain features, structures, and elemental signatures below the ship

Design constraints:
- total hull mass affects speed and maneuverability; heavier builds are slower and less agile
- Air Ships passively recharge their Gale Capacitors in the Flutter Isles; elsewhere they consume stored charge
- weapon mounts are compatible but add mass; a heavily armed Air Ship sacrifices its speed advantage

### 9.3 Water Ships

Water Ships are buoyant platforms powered by Water elemental components. They are slower than Air Ships but significantly more durable, with higher cargo capacity and better support for heavy machine installations. In the Drowned World they can operate underwater as well as on the surface, using pressure-sealed hull components to submerge into flooded cavern systems.

Identity: durability, capacity, and depth. Water Ships are the workhorses and mobile bases of the vehicle system. They carry more, take more punishment, and support heavier machine setups than Air Ships. Their weakness is speed and the need for a water surface or flooded environment to operate.

Core components:
- Tidal Helm — the control block for Water Ships; includes a depth gauge for submersible configurations
- Current Drive — the propulsion component; generates forward thrust through elemental water flow
- Buoyancy Core — provides surface float and ballast control; required for the ship to sit on water rather than sink
- Pressure Hull — an optional component that seals the ship for submersion, enabling underwater travel in the Drowned World and other flooded environments
- Abyssal Scanner — an optional sensor component that maps underwater terrain, detects submerged structures, and identifies pressure anomalies

Design constraints:
- Water Ships require a water surface or flooded space to operate; they cannot fly or cross dry land
- submersion requires Pressure Hull components; a ship without them will flood if it goes below the waterline
- Water Ships recharge their elemental reserves passively while in the Drowned World; in dry or arid dimensions they consume stored charge at an increased rate

### 9.4 Vehicle Progression

Vehicles fit into the mid-game as a natural extension of dimensional exploration. Basic ship components are reachable after the player has explored at least one elemental dimension and gathered elemental materials. Advanced components — scanner arrays, combat mounts, machine-grade cargo holds — require materials from multiple dimensions and integration with the Core Fabricator.

Progression tiers:
- Basic hull: Avalon Ingots and first-dimension elemental materials; functional for travel and light cargo
- Stabilized hull: cross-dimensional materials; supports heavier loads, machines, and basic sensors
- Resonant hull: Core Fabricator components and Wisdom-gated recipes; enables full combat, scanner, and mobile-base configurations

### 9.5 Multiplayer and Vehicle Interaction

Vehicles are well-suited to multiplayer use. Multiple players can ride the same vehicle, operate different stations simultaneously, or split into separate ships with distinct roles — one scout running a fast Air Ship ahead while another crew operates a heavy Water Ship hauler.
- the pilot controls movement; other players can man weapon mounts, operate onboard machines, or manage cargo during transit
- vehicle fleets create a natural specialization loop: scouts find targets, haulers carry the yield, and armed ships escort through dangerous dimensions

## 10. Multiplayer Role Fit

The mod should naturally support player specialization without forcing it.

Possible specializations:
- explorer and prospector
- machinist and logistics builder
- ritualist and knowledge keeper
- metallurgist and forge operator

Healthy multiplayer behavior:
- players can contribute through distinct loops
- bases benefit from district-style organization
- shared infrastructure creates collaboration rather than inventory dumping

## 11. Aesthetic Direction

The visual identity should be arcane-industrial.

Visual rules:
- use metal, carved stone, crystal, glass, and rune motifs together
- avoid pure sci-fi styling
- avoid generic medieval fantasy styling
- make machines look engineered and magical at the same time

Elemental palette:
- Earth: moss, ochre, deep slate, bronze
- Water: teal, blue, silver, pale cyan
- Air: white, pale gold, light blue, soft gray
- Fire: ember red, orange, black iron, brass

## 12. UX Principles

The mod will become large. Clarity must scale with complexity.

UX rules:
- machine names should be evocative but readable
- first-use flows should be understandable without external guides
- tooltips should provide a short layer and an advanced layer
- GUIs should expose state clearly: input, output, stability, heat, charge, and errors
- players should usually know why a system failed

## 13. Technical Direction

### 13.1 Content Architecture

The mod should remain organized so that shared gameplay logic can survive across every major Minecraft version from 1.12.x onward, while version-specific integrations stay isolated.

Preferred code areas:
- `registry`
- `world.level.block`
- `world.level.block.entity`
- `world.inventory`
- `client.screen`
- `data`

### 13.2 Data-Driven Content First

As the mod grows, data-driven content becomes mandatory for maintainability.

Prioritize data-driven definitions for:
- recipes
- loot tables
- tags
- advancements
- future worldgen
- future machine recipes where practical

### 13.3 Registry Stability

This mod is expected to grow over time, so public IDs must stay stable.

Rules:
- do not casually rename blocks, items, menus, or block entities
- maintain backward compatibility where possible
- treat naming as save-data API

## 13.4 Version Support Strategy

The Four Corners should support every major Minecraft version going back to 1.12.x rather than treating a single release as the only target.

Support targets:

1.12.x as the compatibility floor for legacy players and modpacks

all major versions after 1.12.x as active support candidates

modern releases should remain the reference implementation for new systems, with older versions receiving equivalent gameplay where technically reasonable

Implementation guidance:

separate shared game design logic from version-specific loader, registry, GUI, and worldgen code

keep block, item, machine, and dimension behavior functionally consistent across supported versions even when APIs differ

treat data, balance values, recipes, and progression rules as portable content wherever possible

document version exceptions clearly when a specific mechanic cannot be reproduced exactly on an older release

Why it matters:

Broad version support increases the mod's reach, preserves access for older expert modpacks, and makes Four Corners feel like a long-term platform rather than a single-version experiment.

## 14. Current Implementation Snapshot

As of the current implementation snapshot, the codebase already contains:
- a modern Forge-based foundation, with the long-term support target expanded to every major Minecraft version back to 1.12.x
- base items, Avalite ore content, and Avalon Ingots as the foundational construction material
- a custom creative tab
- the Core Fabricator block entity, menu, and screen shell
- the Dimension Accessor block entity, menu, and screen shell

This means the immediate design task is not inventing the mod from nothing. The immediate task is filling in real machine behavior, research structure, elemental loops, and world-facing progression.

## 15. Recommended Development Priorities

### 15.1 Short Term

- implement real Core Fabricator recipes and machine logic, including Air and Water Elemental Core recipes for first-access dimensional travel
- implement Dimension Accessor travel behavior and define the gating loop for all four elemental realms
- build the first pass of each elemental dimension with basic exploration content, materials, and ruins
- turn the starter tome into a quest-driven progression guide with Wisdom rewards for completion
- implement the Wisdom Crucible and its fluid conversion behavior

### 15.2 Mid Term

- deepen each elemental dimension with structures, unique loot, locked areas, and dimension-specific quests
- add elemental storage, transport systems, and machine networks that make use of dimension-sourced materials
- add rituals that complement machine infrastructure and reward dimensional knowledge
- build cross-element crafting loops that require materials sourced from multiple dimensions
- implement the Air Ship and Water Ship vehicle systems, including component blocks, helm activation, and utility module slots
- expand the tome quest system across all four dimensions with branching quest lines

### 15.3 Long Term

- add deeper locked areas and endgame secrets within each elemental dimension
- add weather and biome control systems
- add large endgame synthesis or reactor structures
- add multiplayer-scale infrastructure goals

## 16. Open Questions

- Is Avalite best framed as an Earth material, or as a universal elemental substrate?
- How much Wisdom should each quest type award, and how should quest difficulty scale across the four dimensions?
- How much of each dimension should be freely explorable versus locked behind in-dimension crafting or quest gates?
- Should late-game balance reward full elemental symmetry or powerful asymmetric builds?
- How does the danger curve scale across Air, Water, Earth, and Fire — what specific mechanics make Earth and Fire feel genuinely harder to survive without feeling unfair?
- What level of automation complexity fits the intended audience before it becomes noise?

## 17. Success Criteria

Four Corners is successful if players consistently feel that:
- the elements change how they build, not just what they craft
- magic and tech depend on each other in meaningful ways
- the progression is ambitious but understandable
- each phase unlocks new ways to use older systems
- their base evolves into an elemental infrastructure project
- the mod feels like a world expansion with its own identity

## 18. Summary

The Four Corners should become a true tech-magic mega mod where the four elements shape progression, infrastructure, and world interaction from start to finish. Its best version is not a collection of cool machines and spells. Its best version is a coherent elemental civilization simulator built inside Minecraft.