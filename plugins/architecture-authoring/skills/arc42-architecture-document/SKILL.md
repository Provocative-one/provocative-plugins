---
name: arc42-architecture-document
description: Start, write, extend or refresh an arc42 architecture document that serves as the single source of truth for a system and everything derived from it. Scaffolds a new document set (architecture and estimate with registers opened empty, README, conventions file, changelog, audit configuration), writes the twelve sections with their registers (quality goals, components, decisions, risks, assumptions and open items, diagram assets), keeps the front matter and notation key accurate, applies a client's mandated vocabulary, and versions the document with document semantics. Use whenever the user asks to write or start an architecture document, document a system in arc42, respond to an RFP or design brief with an architecture, add an architecture decision or component, work on a building block, runtime or deployment view, bump the architecture version, or use an existing arc42 set as the baseline for a design or discovery engagement.
compatibility: Scripts need Python 3.9 or later and only the standard library. Expects a Git repository for the document set; the scaffold creates one's directory layout.
allowed-tools: Bash(python3:*) Read Write Edit Glob Grep
metadata:
  version: 0.2.0
---

# arc42 Architecture Document

arc42 is a public template of twelve sections. What this skill adds is the discipline that runs on it: one document every other artifact derives from, registers that carry every claim that could drift, a notation key that says where each series lives, and versions that mean something for a document with no code.

## Embedded skills

| Step | Skill | Job here |
|---|---|---|
| 4 | evidence-and-registers | Decides every marker and register row |
| 6 | blunt-critique | Attacks the draft before it is shown |
| 7 | semantic-versioning | Classifies the bump with the document semantics of substrate Part B.2 |
| 8 | stricter-ai-language-hygiene | Sweeps every paragraph you wrote |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F. Parts A and B of that file hold the register grammar and the document conventions; read them before writing.

## Workflow

### 1. Start or open the set

For a new set, scaffold it:

```bash
python3 scripts/register_tools.py scaffold --root <repo> --system "<System>" \
  --client "<Client>" --prefix <XYZ> --author "<Given Surname, Organization>"
```

The scaffold writes both living documents with every register opened empty, the README, `CLAUDE.md`, `CHANGELOG.md`, `.gitignore`, the directory taxonomy of substrate Part B.5, and `tools/audit.py` with its configuration. Every `<fill: ...>` slot is a decision for the author, and the audit warns until each is filled.

For an existing set, read the architecture, the estimate, the README, `CLAUDE.md` and the changelog before editing anything.

### 2. Declare the sources

The sourcing rule names the sources the set admits, concretely: vendor documentation read on a date, a deployed resource, a recorded session on a named date, a committed verification run, a named person on a named occasion. An unmarked statement traces to one of them.

### 3. Write the sections

| Section | Holds | Watch for |
|---|---|---|
| 1 Introduction and goals | What the system does, requirements, quality goals `[Q-nn]` in §1.3, stakeholders | Goals come from the client; never invent one |
| 2 Constraints | Vendor, client platform, and organizational or commercial constraints | §2.3 is usually excluded from client-facing derivatives |
| 3 Context and scope | Business context, out of scope | The client's own vocabulary |
| 4 Solution strategy | The few decisions that shape everything else | Borderline inferences argued in the text |
| 5 Building block view | Levels, and the `[C-nn]` component register in §5.4 | One row per element on the diagrams |
| 6 Runtime view | Scenarios the client stated | Stays thin when the client stated none |
| 7 Deployment view | Where each component runs | |
| 8 Cross-cutting concepts | Terminology pairs, and the diagram asset register in §8.8 | |
| 9 Architecture decisions | `[AD-nn]` with status and consequence | Superseded rows stay |
| 10 Quality requirements | Measured targets the client stated | Stays thin when the client stated none |
| 11 Risks and debt | `[R-nn]` in §11.1, the `[A-nn]` register in §11.5 | |
| 12 Glossary | Terms, and the pairs a reader could conflate | |

**Thin sections stay thin.** When the client has stated no runtime scenario or no measurable target, §6 and §10 say so in one sentence, and say that nothing was inferred. Inferring targets into them is the most damaging edit available, because every derivative inherits the invented target as a commitment.

**Client vocabulary.** Once the client names its modules or products, those names are the standard everywhere. Record each name and its forbidden synonyms in `tools/audit-config.json` under `vocabulary`, and the audit enforces them.

**Diagrams.** Register every diagram in §8.8 before it is drawn, then brief, build and accept it with the `diagram-assets` skill (substrate Part B.6).

**Citations.** A bare `§n` is this document. Qualify every other reference by role: `estimate §5`, or `Section n` for the client's own document.

### 4. File every claim

Apply `evidence-and-registers` to each paragraph as you write it. Allocate IDs with `scripts/register_tools.py next`, never by hand-counting. Keep the counts in the notation key ("§11.5, eleven entries") equal to the registers.

### 5. Keep the dependency one way

The architecture never cites `[EA-nn]`, `[ED-nn]`, `[ER-nn]` or `[M-nn]`. Build status belongs to the estimate.

### 6. Attack the draft (blunt-critique)

Before showing it, read the draft as a skeptical technical reader. Look for: a statement with no source and no marker, an `[A-nn]` restated as fact two sections later, an `[I]` that acquired an owner, a target in §6 or §10 nobody stated, a component on a diagram with no row in §5.4, a decision whose consequence nobody could check. Order what you find by damage and fix it.

### 7. Version (semantic-versioning)

Classify the bump with substrate Part B.2. Update in one commit: the Version row and title, the README pointer, the changelog entry under the document's own heading, and anything that depends on the old version. A MAJOR bump of the architecture obliges re-deriving the estimate; below 1.0.0, so does a MINOR (substrate Part B.4). When a bump renumbers or renames anything, list the changed identifiers in the changelog entry.

### 8. Sweep and audit

Run the hygiene sweep on every paragraph you wrote, then the audit:

```bash
python3 tools/audit.py --root <repo>
```

Zero FAIL is the bar for cutting a version. Present the changed files and the audit result. Do not commit or push without an explicit instruction.

## Design-engagement mode

When a bid converts into a design or discovery engagement, the architecture already exists, and the client has read it. Reuse it as the baseline: map each deliverable the client asked for (design document, work breakdown per phase, resourcing plan, assumptions and exclusions log) to the sections and registers that already hold it, list what the engagement must revise, and price only the revision. Record the map in the README's "Map from the client's sections" table.

## What this skill leaves to its siblings

Marker and register judgment in detail is `evidence-and-registers`. The estimate is `sibling-estimate-document`. Whole-set checks and reconciliation against a sent document are `architecture-set-audit`. Client-facing artifacts are `client-facing-derivations`. Diagram assets are `diagram-assets`. Who may edit which file is `agent-division-of-labor`.

## Resources

- `scripts/register_tools.py`: `scaffold`, `next`, `cites`, `project`.
- `assets/templates/`: the files the scaffold renders.
- `references/shared-substrate.md`: grammar, conventions, prose registers, platform notes, defect catalog, fallbacks.
- `../../fixture/heritage-hub/`: a complete worked set.
