# The Four Corners

The Four Corners is a Forge mod for Minecraft 1.20.1 built around one idea: technology, magic, and the four classical elements all belong to the same progression system.

Instead of splitting factory gameplay and fantasy gameplay into separate lanes, Four Corners mixes them. Players begin with strange ores, shards, and fragments of lost knowledge, then build toward elemental machines, ritual infrastructure, automation networks, and dimensional projects.

## The Pitch

Four Corners is meant to feel like a mega mod with a strong identity:

- Earth drives structure, pressure, growth, and stability.
- Water drives flow, purification, chemistry, and cooling.
- Air drives motion, signaling, levitation, and weather.
- Fire drives heat, metallurgy, power, and volatility.

The long-term goal is not just better tools. It is elemental mastery through arcane industry: machine networks, rituals, hybrid crafting, dangerous high-tier systems, and world-scale infrastructure.

## Current State

The project is currently on Forge 1.20.1 and Java 17. The codebase already includes:

- core materials, blocks, and items
- a custom creative tab
- a ported Core Fabricator block entity, menu, and screen
- a ported Dimension Accessor block entity, menu, and screen

The next major step is implementing the real machine logic, progression loops, and research structure that turn the current foundation into the full mod vision.

## Development

Build the project from the repo root with:

```bash
./gradlew build
```

Run the dev client with:

```bash
./gradlew runClient
```

## Design

The full internal design doc lives at [docs/four-corners-design.md](docs/four-corners-design.md).
