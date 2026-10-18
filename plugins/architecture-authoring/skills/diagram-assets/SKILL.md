---
name: diagram-assets
description: Register, brief, build and accept the diagram assets of an arc42 document set as traceable claims. Each asset gets a register row under a project prefix and type token (such as [XYZ-CTX-01], [XYZ-CNT-01], [XYZ-RDM-01]), a brief written before the build that ties every element to a register row or section, an SVG under the house palette and typography, and an acceptance run that fails on any element the brief does not support. Covers context, container, component, runtime, deployment and roadmap views, the simplified executive view for slides, and keeping dependency and data-flow arrows on separate canvases. Use whenever the user asks to register, brief, build, draw, check or accept a diagram that belongs to an arc42 architecture or estimate document, asks whether an asset such as [XYZ-CTX-01] is built, wants a diagram for a slide derived from the set, or wants a diagram reviewed against what the document says. For a Mermaid C4 package documenting an estate outside an arc42 set, use c4-diagram-package instead.
compatibility: Python 3.9 or later, standard library only. Reads tools/audit-config.json for the project prefix and the house palette. Rendering an SVG for visual review needs a renderer such as cairosvg or a browser.
allowed-tools: Bash(python3:*) Read Write Edit Glob Grep
metadata:
  version: 0.1.0
---

# Diagram Assets

A diagram in an architecture set is an argument. Every box asserts that a component exists, every line that something depends on or flows to something else, every boundary that it holds. So an asset is held to the same rule as a sentence: each element traces to a register row or section, and an element with no source is an unsourced claim that happens to be drawn. The brief is the object review runs against, which matters most when the reviewer cannot see the image.

## Embedded skills

| Step | Skill | Job here |
|---|---|---|
| 2 | evidence-and-registers | Decides what each element traces to; a missing source becomes a register row, never a drawn guess |
| 5 | blunt-critique | Attacks the asset against its brief and its sections |
| 6 | semantic-versioning | Building an asset flips its row to Built, a MINOR bump of the document holding the row |
| 2 and 6 | stricter-ai-language-hygiene | Sweeps the brief's prose and every label |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F. Part B.6 of that file states the asset rules every skill shares.

## Workflow

### 1. Register

Add a row to the asset register of the document that uses the asset: architecture §8.8 for system views, estimate §8.4 for roadmaps. The ID is `[PREFIX-TYPE-nn]`: the project prefix from `tools/audit-config.json`, then a type token (`CTX` context, `CNT` container, `CMP` component, `RUN` runtime, `DEP` deployment, `RDM` roadmap), then two digits. The status starts at Not built. The file name derives from the ID lowercased, so no register carries a path column: `[XYZ-CTX-01]` is `arc42/assets/xyz-ctx-01.svg`, briefed at `briefs/xyz-ctx-01.md`.

### 2. Brief before build

```bash
python3 scripts/diagram_tools.py brief --root <repo> --id XYZ-CNT-01
```

The brief lists every element with its exact label on the canvas, its kind, and the register row or section it traces to. A component element traces to its `[C-nn]` row; an arrow traces to the section that states the relationship. It declares the arrow kind (dependencies, or data flow) and any other text allowed on the canvas, such as a title or legend. It states the audience: internal, or client.

When an element the diagram needs has no source, the fact enters the document first (a section, a component row, an `[A-nn]` entry), and the brief cites it. Nothing is drawn on the strength of a conversation.

### 3. Choose the view

| View | Holds | Leaves out |
|---|---|---|
| Full | Every element the brief lists, actors included, with a legend | Nothing the brief lists |
| Simplified executive | The client's module names, three colors at most, no actor figures, one relationship kind | Internal component names, technology labels, identifiers |

The simplified view is its own asset with its own row and brief, derived from the full one. A slide carries the simplified view; a reviewer reads the full one.

**Arrows mean one thing per canvas.** Dependency arrows say "needs"; data-flow arrows say "sends". Mixing them makes every arrow ambiguous. When both matter, draw two assets.

### 4. Build the SVG

Follow `references/house-style.md`: the palette and typography come from the project's configuration as parameters, text stays text, nothing external is referenced, a `viewBox` is set. Draw from the brief only; every label on the canvas appears in the brief, and nothing else does.

For C4 views, the C4 conventions of the `c4-diagram-package` skill (level discipline, state grammar) apply where that plugin is installed. This skill produces the registered SVG asset; that one produces Mermaid packages documenting an estate.

### 5. Accept (blunt-critique)

```bash
python3 scripts/diagram_tools.py check --root <repo> --id XYZ-CTX-01 [--client-facing]
```

The check fails when a brief element is missing from the canvas, when canvas text appears in no brief element, when an element traces to nothing, when the arrow kind is undeclared or doubled, when the SVG references anything external, embeds an image, lacks a `viewBox` or has its text converted to paths, when a color falls outside the house palette, and, for a client-facing canvas, when any register reference, asset ID or marker appears on it.

Then review it by eye against the sections the elements trace to: does each arrow have a counterpart in the text, does each boundary hold, does anything on the canvas assert more than the document does? Record the result point by point in the brief's acceptance run.

### 6. Record the build

Flip the row to Built. That is additive content, so the document holding the row takes a MINOR bump (semantic-versioning). One commit carries the SVG, the brief, the row, the version, the README pointer and the changelog entry. Rendered exports for a deck or for print go to `generated/`, which git ignores; they are regenerable and never enter history. The audit checks the register against the files:

```bash
python3 ../architecture-set-audit/scripts/audit.py --root <repo>
```

Present the asset and the acceptance result. Do not commit without an explicit instruction.

## What this skill leaves to its siblings

Mermaid C4 packages for an estate are `c4-diagram-package` in `architecture-continuity`. The facts a diagram depicts are `arc42-architecture-document` and `sibling-estimate-document`. A diagram placed on a client slide also goes through `client-facing-derivations` for its brief and published copy.

## Resources

- `scripts/diagram_tools.py`: `brief` and `check`.
- `references/house-style.md`: palette and typography parameters, SVG constraints, the simplified view.
- `references/shared-substrate.md`: Part B.6 and the fallback digests.
- `../../fixture/heritage-hub/briefs/`: a brief for a built asset and one for an asset not yet built.
