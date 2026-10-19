---
name: sibling-estimate-document
description: Build and maintain the estimate that prices an arc42 architecture, as a second arc42 document that depends one way on it. Calibrates an effort unit against a measured build, keys the backlog on components against milestones, writes milestones with exit criteria someone outside the project can check, keeps estimate assumptions, estimating decisions and estimate risks in their own registers, states sensitivity in a fixed order, and pins the architecture version it was derived from. Use whenever the user asks for an estimate, effort model, staffing model or allocation, to price an architecture, calibrate against a proof of concept or prior build, size milestones in person-weeks, ask what a milestone costs, turn an architecture into a plan, or reconcile the estimate after the architecture changed. Do not use for a commercial price or rate; the estimate prices effort and leaves money to the commercial owner.
compatibility: Uses register_tools.py from the arc42-architecture-document skill and audit.py from the architecture-set-audit skill when the plugin is installed. Python 3.9 or later.
metadata:
  version: "0.2.1"
---

# Sibling Estimate Document

The estimate is the architecture read as a plan. It keeps the twelve arc42 numbers, bends three section names, and depends on the architecture in one direction only: it cites the architecture's registers, and the architecture never cites its own. That one-way rule is what lets a second estimate be run over the same architecture without touching it.

## Embedded skills

| Step | Skill | Job here |
|---|---|---|
| 2 to 5 | evidence-and-registers | Every `[EA-nn]`, `[ED-nn]`, `[ER-nn]` and `[M-nn]` row |
| 7 | blunt-critique | Attacks the figures and their structure |
| 8 | semantic-versioning | Classifies the estimate's own bump, and decides whether the pin still holds |
| 9 | stricter-ai-language-hygiene | Sweeps the prose |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F. Part B.4 of that file defines the pin.

## The bent reading

The front matter or an opening section states it: §5 holds the work breakdown, §6 the milestone sequence, §7 the staffing. The rest keep their usual reading: §2.2 the estimate assumption register, §3 the sources in the offer and the client actions that gate milestones, §4 the estimation strategy, §9 estimating decisions, §10 exit criteria, §11 estimate risks, sensitivity and commercial framing. Staffing is a section of this document, never a separate model.

## Workflow

### 1. Read the architecture at a named version

Record it in the "Estimates against" row. Every component in architecture §5.4 must appear in the backlog, and every open item the estimate leans on is cited by its `[A-nn]`.

### 2. Calibrate the unit

Define one unit anchored on something measured: the commit history of a proof of concept, a pilot build, a prior engagement's actuals. Register the definition as `[EA-01]` with its evidence, and state every figure as a multiple of it. Correcting the anchor then rescales the total without touching the structure. Person-weeks or person-days are derived from the unit.

### 3. Build the backlog as the join

The backlog in §5.1 is a table, with no register of its own: one row per component per milestone, carrying build status, effort in the unit, and the register entries the row leans on. It is the join between the architecture's components and the estimate's milestones. Build status lives here and nowhere in the architecture.

### 4. Write the milestones

Milestones come in the order the commercial owner set, which is given, never derived. Each `[M-nn]` carries two or three decision records and one exit criterion in §10, checkable by someone outside the project ("the search answers the client's twenty test queries within one second each").

### 5. Keep effort and lead time apart

Effort and client lead time never share a column. Client actions that gate a milestone go in §3.2 as preconditions with named owners, and each becomes an `[EA-nn]` with a decision timeframe ("within ten business days") and a schedule consequence if false. A client-side slip moves a date through change control, never into price.

When contingency exists, name the buffered milestones identically everywhere they are mentioned.

### 6. Separate risks from failed assumptions

If a risk is one assumption proving false, it belongs in that assumption's "If false" cell. An `[ER-nn]` is a risk whose materialization is not a single `[EA-nn]` failing, such as a vendor changing an API mid-build. Say so in the text when a would-be risk is routed to an "If false" cell.

Sensitivity in §11.2 runs in a fixed order: the anchor, conditional scope, quality targets, client lead time.

### 7. Attack the figures (blunt-critique)

Check that every backlog row cites its dependencies, that the effort table sums to the milestone rows, that no cell adds effort to lead time, that each exit criterion could be checked by an outsider, that no absorption promise ("if an input is missing we will cover it") appears without a schedule consequence, and that the commercial framing in §11.3 cites no figure the registers do not hold.

### 8. Version and pin (semantic-versioning)

Classify the estimate's own bump with substrate Part B.2. Then check the pin against substrate Part B.4:

- Architecture moved by PATCH, or by MINOR at 1.0.0 or above: the pin still holds. Advance it only when you re-derive.
- Architecture moved by MAJOR, or by MINOR below 1.0.0: the pin is broken. Re-derive the estimate against the new version and re-pin.
- A commit whose only change is advancing the pin is a PATCH to the estimate.

### 9. Sweep, audit, present

Run the hygiene sweep and `python3 tools/audit.py --root <repo>`; the audit checks the one-way rule and the pin. Present the changes. Do not commit without an explicit instruction.

## Reversing an estimating decision

Reversals happen, and this is how one is done. When a client needs in writing something an `[ED-nn]` said would be offered only in conversation (a duration, say):

1. Add a new `[ED-nn]` that states the new position and cites the old one; set the old row to "Superseded by" the new ID.
2. Open an `[EA-nn]` carrying the conversion (for example, weeks per unit) with its "If false" consequence.
3. Open an `[ER-nn]` for the exposure the written commitment creates, such as fixed-fee slippage.
4. Only then let a derivative state the figure.

The fixture's estimate §9 and §11.1 show the four steps in place.

## What this skill leaves to its siblings

The architecture itself is `arc42-architecture-document`. Client-facing milestone plans and annexes are `client-facing-derivations`. Whole-set checks are `architecture-set-audit`.

## Resources

- `references/shared-substrate.md`: Parts A and B, including the pin rule in B.4.
- `../../fixture/heritage-hub/arc42/hhb-estimate-arc42.md`: a complete estimate with calibration, backlog, reversal and sensitivity.
