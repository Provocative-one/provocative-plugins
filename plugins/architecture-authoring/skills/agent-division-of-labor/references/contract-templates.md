# Contract templates

## `CLAUDE.md`: who writes what

```
## Who writes what

**Every file has one writing agent.** The other reads it and proposes.

| Path | Writing agent |
|---|---|
| `arc42/`, `CHANGELOG.md`, `README.md`, `tools/` | <agent with shell and git> |
| `briefs/`, `generated/` | <agent that renders and builds documents> |
| `published/` | <builder> builds, <committer> commits |

### Capabilities, as observed on this repository

| Agent | Can | Cannot |
|---|---|---|
| <agent> | <run git and the audit> | <render an SVG> |
| <agent> | <render and inspect an SVG, build office files> | <run a shell where the repository lives> |

A change an agent wants in a file it does not own arrives as a proposal block. The owner applies, verifies and commits.

Handoffs do not become files. Transient instructions stay in the conversation; the durable half of a handoff is the brief and the commit body. `HANDOFF.md` at the root is a session-continuity note, ignored by git, overwritten at each handoff.
```

## Proposal block

```
**Proposal for `<path>`** (owner: <agent>)

Anchor (must match exactly once):
> <exact current text>

Replacement:
> <new text>

Reason: <one or two sentences, with the source that supports the change>

Obligates: <README pointer to x.y.z; changelog entry under <file>; version bump <PATCH|MINOR|MAJOR>; pin review in the estimate; regenerate <derivative>>
```

## `HANDOFF.md`

```
# Handoff, <YYYY-MM-DD HH:MM> <time zone>

Ignored by git. Overwritten at each handoff.

## Uncommitted changes

| File | Change |
|---|---|
| <path> | <what changed> |

Ready commit message:

    <type>(<scope>): <summary>

    <why, what, and how it changes the set>

## Open decisions

| Decision | Owner | Blocks |
|---|---|---|
| <decision> | <Given Surname> | <what waits on it> |

## Next work, in order

1. <step, with the file and the check that closes it>
2. <step>

## State checks

Audit: <result of `python3 tools/audit.py --root .`>. Versions: architecture <x.y.z>, estimate <x.y.z>, pin <x.y.z>.
```

## Project instructions for a fresh Cowork or Claude Code project

```
You work on the <System> document set in this folder. Read CLAUDE.md first; it governs every edit.
Your role: <writing agent for briefs/ and generated/ | writing agent for arc42/, CHANGELOG.md, README.md, tools/>.
For any file you do not own, produce a proposal block and stop; the owner applies it.
An agent is not a source: cite what you retrieve, with the date; mark anything else.
Read HANDOFF.md if it exists, and continue from its "Next work" list.
Run the audit before declaring any version ready: python3 tools/audit.py --root .
Never commit or push without an explicit instruction.
```
