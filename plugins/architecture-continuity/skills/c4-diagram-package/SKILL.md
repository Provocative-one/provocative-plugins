---
name: c4-diagram-package
description: Build, refresh, or critique a C4 architecture documentation package. It produces Mermaid diagrams (system context, container view, component slices) under a uniform state-encoding grammar (present, sunsetting, planned, partial, parked, superseded) so an estate in transition shows what is real, arriving, retiring, and deferred in one picture. Each diagram has a source-of-record `.mmd`, a narrated companion, and a README index. Use whenever the user asks for C4 diagrams, a system context or container view, component diagrams, Mermaid or Lucid architecture documentation, an as-is/to-be architecture baseline, or a diagram set for an architecture handoff or closure, or says "document the architecture", "draw the platform", or "update the C4". Includes an audit script that catches drift between diagram sources and their companions.
metadata:
  version: 0.1.0
---

# C4 Diagram Package

An estate in transition misleads when its diagrams flatten present and future into one plane. This skill produces a package where every element carries its lifecycle state, every diagram has a source of record and a narrated companion, and every exclusion is named with its driver. The state grammar is the distinctive part: the same encoding on every diagram, double-encoded in style and glyph, so the picture survives monochrome print.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Step | Skill | Job here |
|---|---|---|
| 6 | blunt-critique | Attacks the package with the C4 checklist and the audit output |
| 7 | semantic-versioning | Versions the package and classifies each refresh |
| 8 | stricter-ai-language-hygiene | Sweeps companion and README prose; leaves the Mermaid alone |

Read Parts A and B of `references/shared-substrate.md` at the start of a session. Part C is only needed when sources come from Atlassian or GitLab.

## Workflow

### 1. Frame the package

Fix five things: the system in focus, the audience, the baseline date, the view (as-is, to-be, or hybrid, with hybrid as the default for an estate that is mid-transition), and the exclusions with their drivers. When the system in focus cannot be inferred from the material, ask. Otherwise state the framing assumption in one line and proceed.

### 2. Choose the set

Always draw L1 and L2. Add L3 slices where decisions concentrate, one slice per concern. Include a draft slice or a parked slice when the record needs to show it, drawn wholly in its state. Do not draw L4. The level rules and the slice test are in `references/c4-method-checklist.md`.

### 3. Establish each element's state, with evidence

Decide every element's state from evidence: an ADR status, a ticket state, a deployment fact, a recorded decision. Keep the evidence for the companion's References. An element with no evidence is `planned`, whatever the team believes. When a decision overtakes an earlier one, draw the old path as `superseded` and name the governing record, so a reader who remembers the old path sees what replaced it.

### 4. Write the Mermaid sources

Follow `references/state-grammar.md`: the header comments, all six class definitions, a state class on every node, a glyph and word on every non-present state, dotted connectors for anything not present at both ends, ASCII titles. One file per diagram. Name any excluded scope and its driver in the header.

### 5. Write the companions and the README

Follow `references/package-layout.md`. The companion order is fixed: Executive Summary, Diagram, Walkthrough, References. The embedded diagram is generated from the `.mmd` with a script, never typed. The `.mmd` is the source of record. The Executive Summary describes the system and what its state encoding reveals. The Walkthrough has one line per element or relationship group.

When refreshing an existing package, read it first, diff its states against the current evidence, keep file names stable, add a currency note for every state that moved, and update the `Supersedes:` line when a diagram is replaced.

### 6. Attack the package (blunt-critique)

Run the audit, then apply blunt-critique with the table in `references/c4-method-checklist.md`.

```bash
python3 scripts/audit_c4_package.py <package_dir>
```

FAIL items are defects. WARN items are candidates that need judgment: a glyph on a node of another class is correct when the label names a sub-part, and wrong otherwise. Fix the `.mmd` first, regenerate the companion's embedded copy, then re-run. Order what remains by damage. When a full pass finds nothing real, say the package has converged and name what was checked.

When the user hands over an existing C4 set to critique, run the same pass and report findings in damage order with quoted evidence.

### 7. Version the package (semantic-versioning)

Run the classifier. The subject is the package. The consumers are readers who plan against the diagrams and anyone who imports the `.mmd` files. The interface is the system boundary, the elements and their states, the relationships, and the file names. These are the default readings for this subject. The classifier decides each case.

| Change | Increment |
|---|---|
| Boundary moves, an element is removed or renamed, a state moves toward withdrawal (present to sunsetting, planned to parked, anything to superseded), a recorded decision is reversed, a diagram is split, merged, or renamed | MAJOR |
| An element, relationship, or slice is added; an element advances (planned or partial to present) | MINOR |
| Label, wording, link, layout, or glyph-alignment fixes that change no claim | PATCH |

The first package is 0.1.0. Crossing to 1.0.0 is a MAJOR event, taken when the user declares the baseline accepted. Put `Version` in the README and in each companion header, and add one line under Notes on currency giving the increment and the one-sentence rationale naming the interface expectation preserved or broken.

### 8. Hygiene pass (stricter-ai-language-hygiene)

Sweep the prose of the companions and the README at the deep register (attachable working documents). Leave the Mermaid alone, since machine-consumed sources keep their precision. The one exception is the title line, which stays ASCII. Structural labels in headings keep their dash. Write each companion to a file, run the mechanical sweep, judge every hit, and run the counting check: the README's diagram count against the set, and any count in the prose against its list.

### 9. Present

Write the package to `/mnt/user-data/outputs/<package>/` and share the README plus a zip of the folder with `present_files`. Do not publish to Lucid, Confluence, or a repository without an explicit instruction (Part A).

## Resources

- `references/state-grammar.md`: the seven states, the canonical class block, the rules.
- `references/package-layout.md`: folder layout, `.mmd` header, companion and README skeletons, Lucid import notes.
- `references/c4-method-checklist.md`: level discipline, slice selection, the blunt-pass table.
- `scripts/audit_c4_package.py`: mechanical audit.
