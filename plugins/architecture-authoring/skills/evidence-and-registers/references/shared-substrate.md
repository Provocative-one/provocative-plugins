# Shared substrate

One file, copied byte for byte into every workflow skill of the plugin, so each skill stands alone. Part A is the register grammar, Part B the document conventions, Part C the two prose registers, Part D platform notes, Part E the defect catalog, Part F the fallback digests for the three embedded skills.

## Part A. Register grammar

### A.1 Two token shapes

A bracket around letters alone is an **epistemic marker**: `[I]`. A bracket around letters, a hyphen and two digits is a **register reference**: `[A-03]`, `[EA-12]`. The two shapes never mix. A bare `A12`, a single-digit `[A-3]`, or an unbracketed `AD-04` is a defect wherever it appears, because a reader cannot tell which register it points to.

### A.2 Default series

| Series | Meaning | Registered in | Who may close or retire a row |
|---|---|---|---|
| `[I]` | Inference drawn from documented facts. Stated by no source. No owner, no closure path, only a conclusion to defend or withdraw | Inline, wherever used | Withdrawn when a checkable source confirms or refutes it |
| `[A-nn]` | Assumption or open item: anything the architecture leans on that no checkable source carries yet, including a statement resting on one person's word. Carries current basis, owner, and the condition that closes it | Architecture §11.5 | Closed only by new evidence |
| `[AD-nn]` | Architecture decision, with status and consequence | Architecture §9 | Superseded by a later decision, never deleted |
| `[R-nn]` | Architectural risk, with consequence | Architecture §11.1 | Retired with a status |
| `[Q-nn]` | Quality goal | Architecture §1.3 | Withdrawn with a status |
| `[C-nn]` | Component: an element the client receives, or a delivery tool that produces it. The letter follows the C4 vocabulary (container, component) | Architecture §5.4 | Withdrawn with a status |
| `[EA-nn]` | Estimate assumption: an assertion the offer makes, with a figure or condition, an owner, and the consequence if it proves false | Estimate §2.2 | Closed only by new evidence |
| `[ED-nn]` | Estimating decision, with status, rationale and consequence | Estimate §9 | Superseded by a later decision |
| `[ER-nn]` | Estimate risk that is not a single `[EA-nn]` proving false | Estimate §11.1 | Retired with a status |
| `[M-nn]` | Milestone, with its exit criterion in estimate §10 | Estimate §6 | Withdrawn with a status |
| `[PFX-TYPE-nn]` | Diagram asset under a project prefix and a type token: `CTX`, `CNT`, `CMP`, `RUN`, `DEP` in the architecture, `RDM` in the estimate | Architecture §8.8, estimate §8.4 | Status changes with the build |

The letters are defaults. A project may add a series with a one-line declaration in its notation key naming four things: prefix, meaning, home register, and who may close a row. Any further configurability makes the audit unmaintainable.

### A.3 The two confusable pairs

**`[A-nn]` against `[I]`.** An open item has an owner and a path to closure. An inference has neither. Attributing an inference to a person, or filing somebody's reasoning as an open item someone else can close, both misstate where a claim came from.

**`[A-nn]` against `[EA-nn]`.** An open item is something not yet established. An estimate assumption is an assertion carrying a figure and a consequence. Converting the first into the second is how an unknown becomes priceable, and it happens only in the estimate, which cites the `[A-nn]` it converts.

### A.4 Register rules

1. **One row, one place.** A row lives in its home register and is cited everywhere else by ID. It is never retyped. Client-facing projections are generated from the register.
2. **Never renumber.** A closed, superseded or withdrawn row keeps its number and gains a status. The number is never reused.
3. **Never close without evidence.** A register entry closes, and an `[I]` retires, when a checkable source arrives. Repetition across sections is not evidence, and neither is a session's confidence.
4. **Attribute internal sources.** A figure that rests on a colleague's word names the person and the date. It is never presented as client-confirmed.
5. **An agent is not a source.** A sentence an agent produced carries the same burden as one written by hand: it traces or it takes a marker. Retrieval is evidence, recollection is not.

### A.5 Citation conventions

- A bare `§n` means the document being read.
- A section of another living document is qualified by role: `architecture §5.4`, `estimate §2.2`.
- A section of the client's own document (an RFP, a brief) is written `Section n`, in the client's numbering.
- The template's name is never a document's name. "The arc42 document" is a defect; "the architecture document" is correct.
- Prose may name a role ("the architecture"), never a filename.

### A.6 Notation key template

Every living document carries, after its front matter, a sourcing rule and a notation key.

```
## Sourcing rule

Every statement traces to one of these sources: <the sources the set admits, each named
concretely: vendor documentation read on a date, a deployed resource, a recorded session on
a named date, a committed verification run, a named person on a named occasion>. Everything
else carries a marker, and the markers are the following.

| Marker | Meaning | Registered in |
|---|---|---|
| `[I]` | Inference drawn from documented facts. Not stated by any source | Inline, wherever used |
| `[A-nn]` | ... | §11.5, <count in words> entries |
```

The count stated in the "Registered in" column must match the register. The audit checks it.

### A.7 Supersession list

| Convention | First engagement (origin) | Second engagement (revision) | Plugin default |
|---|---|---|---|
| Decision, risk, quality identifiers | `AD-nn`, `Rn`, `Qn` unbracketed | Bracketed two-digit everywhere | Revision form |
| Asserted assumptions | `[CA-nn]` in a staffing model | `[EA-nn]` in the estimate document | Revision form |
| Sibling document | Staffing and effort model, own structure | Estimate document in arc42 form | Revision form; staffing is estimate §7 |
| Component inventory | Named in §5 prose and diagrams | `[C-nn]` register in §5.4 | Revision form |
| Effort unit | Person-weeks per milestone | Baseline-calibrated unit, person-weeks derived | Revision form, the unit a parameter |
| Diagram asset IDs | `XYZ-DLV-01` unbracketed | `[XYZ-CTX-01]` bracketed, registered in §8.8 | Revision form |
| Pin semantics | None | Exact equality, enforced by the audit | Semantic compatibility (B.4) |
| Diagram briefs and acceptance | Numbered acceptance points, SVG under a house palette, a simplified executive view | Brief before build, SVG committed, asset register with build status | Both, in the `diagram-assets` skill |
| Origin class for "needed to make it work" | `[I]`, colliding with the inference marker | Not exercised | `[N]` |
| Client vocabulary enforcement | Mandatory module names everywhere | Not exercised | First-engagement form |
| Client-facing annexes, clarification responses | Produced and iterated | Not exercised | First-engagement content, produced under the second engagement's derivative discipline |

## Part B. Document conventions

### B.1 Front matter

A two-column table at the top of each living document.

| Row | Holds |
|---|---|
| Version | The document's own semantic version |
| Status | What the version asserts: draft, structure established, figures accepted by a named person on a date |
| Date | The currency date |
| Scope | What the document covers, in one sentence |
| Author | Given Surname, organization |
| Audience | Internal, plus which sections are candidates for a client-facing derivative and which are excluded |
| Companion documents | Frozen external documents the set cites, with the statement that this document supersedes nothing in them |
| Sibling document | The other living document, with the dependency direction stated |
| Estimates against | Estimate only: the architecture version it was derived from, and what a change there obligates here |

### B.2 Versioning with document semantics

The `semantic-versioning` skill classifies every bump. For a document with no code:

- **MAJOR** invalidates a decision a reader could reasonably have made on the prior version: a component appearing or disappearing, a constraint reversing, a scope boundary moving, sections renumbering, a register series renamed.
- **MINOR** is backward-compatible addition: a new section, a new register row, a register entry closed, an `[I]` retired on new evidence.
- **PATCH** is correction without consequence: wording, links, register sorting, a marker reclassified without changing the claim, a re-verification that advances the currency date.

Below 1.0.0 a MINOR bump may carry breaking changes. Reaching 1.0.0 asserts maturity. A document whose Status row says its figures are unreviewed, or whose decisions are still Proposed, is not there yet.

### B.3 History

One `CHANGELOG.md` at the repository root, Keep a Changelog form, one heading per tracked file, versioned entries where the file carries a version and dated entries where it does not. It records history from the first commit. The documents never narrate their own past: "was added after review" and "is now stated" are defects in body text. Historical entries are never rewritten, even when a path is renamed. An imported document's own changelog stays untouched.

### B.4 Pointers and pins

These are two different facts.

A **pointer** is the README's record of a living document's current version. It moves in the same commit as the document. A pointer that differs from its target is a defect.

A **pin** is the estimate's "Estimates against" row: the architecture version it was derived from. A pin follows semantic-versioning compatibility, the same rule a dependency range follows:

- Pin `m.n.p` is satisfied by any architecture version `m.n'.p'` that is not lower, with the same MAJOR `m`. A PATCH or MINOR advance in the architecture leaves a valid pin.
- A MAJOR advance in the architecture breaks the pin. The estimate is re-derived and re-pinned, because MAJOR hops are propagated.
- Below 1.0.0, MINOR may break, so pin `0.n.p` is satisfied only by `0.n.p'` with `p'` not lower. A MINOR advance in a 0.x architecture breaks the pin.
- A pin that names a version higher than the architecture's, or a version absent from the changelog, is a defect.

A commit whose only change is advancing a pin is a PATCH to the estimate.

### B.5 Repository taxonomy

| Directory | Holds | Tracked | Edited |
|---|---|---|---|
| `arc42/` | The living documents, and `arc42/assets/` for built diagram assets | Yes | By the owning agent |
| `briefs/` | Briefs generated here: what an artifact must contain, or what a finished artifact contains and on what basis. One per artifact, named for it | Yes | Yes |
| `external-docs/` | Frozen documents the set cites | Yes | Never |
| `generated/` | The workbench: output still being cut, regenerable | Directory only | Freely |
| `published/` | Artifacts as sent, one file per version, version in the filename | Yes | Never; a revision is a new file |
| `tools/` | `audit.py` and its configuration | Yes | Yes |

At the root: `README.md` (entry point, version pointers, the map from client sections to documents), `CLAUDE.md` (the conventions file that governs every edit), `CHANGELOG.md`. A `HANDOFF.md` for session continuity lives at the root and is never tracked.

Asset files derive from the asset ID lowercased: `[HHB-CTX-01]` is `arc42/assets/hhb-ctx-01.svg`, briefed at `briefs/hhb-ctx-01.md`. No register carries a path column.

### B.6 Diagram assets

An asset is registered in the document that uses it, with a build status. Its brief is written before the build and names, element by element, the register row or section each element traces to. A diagram is an argument: an arrow with no counterpart in the component register is an unsourced claim. Review runs against the brief and the sections it cites. Dependency arrows and data-flow arrows mean different things and never share a canvas; the legend says which one the diagram uses.

SVG is the committed form: text stays text, no external font or image, a `viewBox` set. Building an asset flips its row from "Not built", which is a MINOR bump of the document holding the row, carried in one commit with the SVG, the row, the version, the README pointer and the changelog entry. Registration, briefs, builds and acceptance runs follow the `diagram-assets` skill. C4 views also follow the state grammar of the `c4-diagram-package` skill where that plugin is installed.

## Part C. Two prose registers

**Internal documents** are blunt, analytical and attribute every decision to a person and a date. **Client-facing documents** are plain and advisory, anchored to the client's own section numbers and vocabulary, and carry no internal identifier: no register reference, no asset ID, no marker.

**No invention.** A passage in a client document traces to a living document, or carries a placeholder naming its owner and the missing source: `[Owner: commercial lead. Source missing: payment terms]`. A placeholder is visible on purpose and blocks sending.

**Writing against a call.** A commitment that binds price, a service level figure, or scope is approved by its owner before it goes in writing. Anything still negotiable goes on the call list.

**Owner routing.** The project's README names an owner for each class of commitment. The default classes are commercial terms and pricing, service levels, scope, staffing, and dates. A draft that commits on behalf of a class flags the owner inline.

**Client vocabulary.** Once a client names its modules or products, those names are the standard everywhere in the set. Forbidden synonyms are listed in `tools/audit-config.json` and the audit enforces them.

## Part D. Platform notes

- **DOCX.** Markdown is the source of record. When a client requires Word, produce it with the `docx` skill on the client proposal's own styles. Never author in DOCX.
- **Reconciliation input.** Extract text from a PDF, DOCX or PPTX before reconciling (for PPTX, `markitdown` extracts text; rendering needs LibreOffice). Reconcile the text, never a screenshot.
- **GitLab.** Use numeric project IDs; namespace paths return 404 on private repositories. Blob content arrives base64-encoded.
- **Teams.** A message deep link does not return its body through web fetch. Read through the chat resource with the chat ID kept exactly, suffix included.

## Part E. Defect catalog

Each defect was found in a real document between August and October 2026, scrubbed here. The check named is the one that catches it.

| # | Defect | Caught by |
|---|---|---|
| 1 | A bare `A12` beside a bracketed `[A-06]` in one table cell | Audit: residue |
| 2 | "Thirteen metrics" above a list of twelve | Audit: counts |
| 3 | "Up to four clock types" with three named and no fourth | Audit: counts (WARN) |
| 4 | "Eleven surfaces" never enumerated in the pack | Audit: counts (WARN, claim with no list) |
| 5 | A milestone row truncated mid-sentence | Audit: residue (row ending without terminal punctuation, WARN) |
| 6 | A date range inverted, the end before the start | Audit: residue |
| 7 | A client-facing cover reading "working template" | Audit: derived mode |
| 8 | Internal identifiers printed on client-facing diagrams | Audit: derived mode |
| 9 | Contingency stated as two buffered milestones in one place and three in another | Judgment checklist |
| 10 | "Indicative" applied to a commercial item, a schedule and a footnote, then answered about prices | Judgment checklist: terminology pairs |
| 11 | A clarification answer that changed five annex items and two passages with no reissue list | Audit: reissue mode |
| 12 | A dependent document citing `§5.2` without naming whose section | Audit: section references |
| 13 | Client module vocabulary applied unevenly across the set | Audit: rogue terms |
| 14 | A template's pre-drafted assumptions section merged over the generated one | Judgment checklist |
| 15 | An absorption promise in a fixed-fee offer with no schedule consequence | Judgment checklist |

## Part F. Fallback digests

Use a digest only when the full skill is unavailable. When the full skill is present, it governs.

**stricter-ai-language-hygiene.** Replace rhetorical em-dashes with a comma, colon, period or parentheses. One strong contrast per argument; cut reflexive "X, not Y". Delete text about the text. One assertion per sentence. No revision narration in body text. Banned vocabulary: seamless, pivotal, holistic, robust, leverage, delve, crucial, journey, empower, cutting-edge, world-class, unparalleled. Check every stated count against its list. Never alter verbatim quotes, code or machine-consumed specifications.

**blunt-critique.** Read the whole work; diff a revision against the prior version first. Order findings by damage with quoted evidence. Never open with praise. Moves: missing prior art, internal contradiction, definition by example list, unfalsifiable claims, category errors, excisability, audience drift. Drop any objection you would concede under pushback. Declare convergence when a full pass finds nothing real.

**semantic-versioning.** Name the subject, its consumer and the interface. No prior version: 0.1.0. Otherwise: breaks the interface, MAJOR; adds without invalidating, MINOR; corrects without changing scope or meaning, PATCH; MAJOR pre-empts MINOR. Record one sentence naming the interface expectation preserved or broken.
