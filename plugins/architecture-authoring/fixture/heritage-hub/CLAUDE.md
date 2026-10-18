# CLAUDE.md

This file governs every edit in this repository.

## Sourcing rule

Every statement in the architecture and estimate documents traces to a source the architecture's sourcing rule declares, or carries a marker. An agent is not a source: retrieval is evidence, recollection is not. No agent closes a register entry or retires an `[I]`.

## Who writes what

| Path | Writing agent |
|---|---|
| `arc42/`, `CHANGELOG.md`, `README.md`, `tools/` | Claude Code |
| `briefs/`, `generated/` | Cowork |
| `published/` | Cowork builds, Claude Code commits |

A change an agent wants in a file it does not own arrives as a proposal block naming the file, the anchor text, the replacement, the reason, and what the change obligates elsewhere. Handoffs do not become files. A `HANDOFF.md` for session continuity is never tracked.

## Terminology

**Published** and **live** name different states, defined in the architecture's §8.1. The client's name for the search is the Collections Explorer, and no synonym is used.
