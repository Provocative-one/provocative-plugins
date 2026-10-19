---
name: agent-division-of-labor
description: Govern how two or more agents (for example Claude Code with a shell and git, and Cowork or a chat session that can render documents but has no shell where the repository lives) share one document repository. Assigns one writing agent per file, turns every change an agent wants in a file it does not own into a proposal block the owner applies, records each agent's capabilities as observed, keeps transient handoffs out of the repository, and writes the untracked HANDOFF.md that lets the next session resume. Use whenever the user sets up or revises the division of work between agents on a repository, asks who may edit a file, wants to propose a change to a file another agent owns, asks for project instructions for Cowork or Claude Code, or asks for a handoff so the next session can continue.
compatibility: Applies to any Git repository edited by more than one agent. No scripts.
metadata:
  version: "0.3.0"
---

# Agent Division of Labor

Two agents with different capabilities can keep one repository coherent when every file has a single writer, and when everything else an agent wants arrives as a proposal. The contract lives in the repository's `CLAUDE.md`, the conventions file every agent reads first.

## Embedded skills

| When | Skill | Job here |
|---|---|---|
| Writing the contract or a proposal | stricter-ai-language-hygiene | Sweeps the prose; the contract is read by agents and people alike |
| Reviewing a proposal before applying it | blunt-critique | Checks the change and everything it obligates |
| Applying a proposal | semantic-versioning | Classifies the bump the change causes |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F.

## The contract

### One writing agent per file

`CLAUDE.md` carries a table of paths and their writing agent. Typical assignment: the agent with a shell and git owns the living documents, the changelog, the README and `tools/`; the agent that renders and builds documents owns `briefs/` and `generated/`; the second builds what lands in `published/` and the first commits it. The other agent reads and proposes.

### Proposals, never edits in place

A change an agent wants in a file it does not own arrives as a block (template in `references/contract-templates.md`) naming:

1. the file;
2. the exact text to anchor on;
3. the replacement;
4. the reason;
5. what the change obligates elsewhere: the README pointer, the changelog entry, the version, the pin, any derivative to regenerate.

The owner applies it, verifies it with the audit, and commits. Proposals stay in the conversation.

### Capabilities as observed

Record each agent's capabilities as observed on this repository: which can run git and the audit, which can render an SVG or build an office file, which has no shell where the repository lives, which delivers into its own landing folder. An agent that cannot run the audit cannot certify a version.

### An agent is not a source

The declared sources never include a model. A sentence produced by an agent traces or takes a marker. An agent that can open vendor documentation cites the page and the date it was read; a statement made without opening it is an `[I]` at best. No agent closes a register entry or retires an `[I]`.

### Handoffs do not become files in history

Transient instructions stay in the conversation, because process notes accumulating outside the changelog are the residue the writing rules exist to prevent. The durable half of a handoff is the brief and the commit body.

The one exception is **`HANDOFF.md`** at the repository root: a session-continuity note for the next agent session, listed in `.gitignore` and never committed. It records the uncommitted changes with a ready commit message, the open decisions with their owners, and the next work in order. It is overwritten at each handoff, never accumulated. The template is in `references/contract-templates.md`.

### Handoff modes

A repository declares one handoff mode in a line of its `CLAUDE.md`. Fallback mode is the default and uses `HANDOFF.md` as described above. Working-log mode applies where the repository carries a working-log under the Corponomia specification (Sections 10.9 and 10.10). Each surface closes a unit at the end of an episode of work, records the next surface's tasks in the unit's Leaves open field, and advances its own pointer to the last unit it has read. Any surface may create a unit, and the surface that runs the audit certifies and commits it. A surface that senses the need to record an architectural decision opens an open item (`m.n.p#A-a`) on creating an architecture document with a decision register and creates no decision identifier. An untracked `HANDOFF.md` says nothing about the mode chosen: without a declaration, fallback mode applies and the question stays closed until the owner raises it.

## Workflow

1. **Setting up a repository.** Write the "Who writes what" section of `CLAUDE.md` from the table above, adjusted to the agents actually present. Record capabilities as observed. Offer working-log mode once and record the answer in a line of `CLAUDE.md`. In fallback mode, add `HANDOFF.md` to `.gitignore`. In working-log mode, write an awareness unit that cites the specification version in Presupposes: version 0.1.0 when the chain is empty, the next version otherwise.
2. **Proposing.** Produce the block. Run blunt-critique on your own proposal first: does the anchor match exactly once, does the reason stand, is every obligation listed?
3. **Applying, as owner.** Apply, run the audit, classify the bump, update the pointer and changelog in the same commit, write a commit body that says why, what, and how it changes the set. Do not push without an explicit instruction.
4. **Handing off.** In fallback mode, write or overwrite `HANDOFF.md`. In working-log mode, close a unit for the episode and advance this surface's pointer. For a fresh Cowork or Claude Code project, also produce paste-ready project instructions from the template.

## What this skill leaves to its siblings

What may be written in the documents is the other skills' business. Knowledge packs and resumable handoffs across engagements are the `closure-extraction-handoff` skill of the `architecture-continuity` plugin.

## Resources

- `references/contract-templates.md`: the `CLAUDE.md` section, the proposal block, `HANDOFF.md`, and project instructions.
- `references/shared-substrate.md`: Part B.5 for the repository taxonomy.
- `references/working-log-mode.md`: digest of Sections 6, 10.9 and 10.10 of the Corponomia specification (unit anatomy, composite identifiers, central register, pointers, awareness unit).
