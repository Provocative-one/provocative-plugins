# Knowledge pack layout

## Folder

```
<pack>/
  00-README.md
  <CODE>-<subject>.md      one subject per file
```

A prefix code is letters plus a digit: `EV1`, `DR2`, `LOG3`. The letters name a theme and the digit orders subjects within it. Files that capture reusable artifact formats (templates) can take their own letter family, for example `T1` to `T7`, apart from files that capture substance. Cross-references in prose use the code in backticks, `LOG2`. The code is part of the pack's interface: renaming or removing one breaks every reference to it.

## File skeleton

```
# CODE: <Subject title>

> **Source:** <System> page `<id>` (<space>) · version <n> · status <status> · <YYYY-MM-DD>. <Ticket key, if any.>
> <One line on its relation to siblings: parent, refined by, merged from.>

---

<Sections following the source's own structure, compressed.>

> **Extraction note.** <Only when the source is superseded, merged, coupled, or needs a caveat.>
```

Header variants: **Source:** for one page, **Sources:** for merged pages with every ID listed, **Artifact:** for a template file that records a reusable format. A file with none of the three has no provenance, and the audit script warns on it.

## Compression rules

- Keep decisions, constraints, thresholds, exact figures, identifiers, and the reasoning that makes each defensible. A reader must be able to use the file with the source closed.
- Keep decision tables and option verdicts. Drop navigation, boilerplate, and repeated framing.
- Keep status, version, and date, because they decide how far a statement can be trusted.
- Add nothing the source does not support. Where provenance is missing, say so in the file.
- Where the source contradicts itself or a sibling, record the contradiction and both passages. Do not choose silently.
- Names in Given Surname form. Strip `@` prefixes and platform chip forms. Dates absolute.
- Subjects: merge pages that are one discovery at two levels of detail. Keep pages apart when each carries a decision someone could cite on its own. A discovery, the ADR that refined it, and a status companion are three subjects.

## Extraction notes: five kinds

1. **Superseded.** Say which record governs and on what. "The discovery page still frames the collector as a worker process. This ADR refined the host to a serverless orchestrator. Treat the ADR as canonical on the collector."
2. **Merged.** List the source pages folded into one file, with their IDs, and why they are one subject.
3. **Coupled.** Name the sibling the file depends on and what it supplies. "ADR-002 (`LOG2`) supplies the observability surface the async branch reports to."
4. **Design of record against operational reality.** Where names or values in the deployed system differ from the design page, state both and say which is which. "The design uses the container `evidence`. The delivered system uses `bundles`. Treat the page as the design of record and the deployed name as the operational truth."
5. **Caveat on figures.** Mark illustrative numbers. "The tiered-cost figures are pay-as-you-go rates captured at authoring time, not a committed price. Use them for order-of-magnitude planning."

A currency note replaces silent reconciliation every time. A pack that harmonizes two sources without saying so has altered the record.

## README skeleton

```
# <Pack title>

<One paragraph: what the pack distills (N sources into M subject files), who it serves, and why one subject per file keeps the knowledge inspectable after the program closes.>

*Compiled <YYYY-MM-DD>, against the pages as they stood at extraction. Version <x.y.z>. Where a later artifact supersedes an earlier one, the file carries a currency note and nothing was reconciled silently.*

## How to read this package

Cross-references use the prefix codes in backticks. Names are Given Surname. An **Extraction note** at the foot of a file flags where the source is superseded, merged, coupled, or caveated.

## The subjects

### <Theme>
- **`CODE`**: <title>. *(page <id>, <ticket>)*

> <Optional reading note for the theme: which file governs, in what sequence to read them.>

## Provenance and fidelity

- **Coverage:** all <N> requested sources are represented. <Which subjects consolidate several pages, and why.>
- **Currency:** <Living sources with their versions and refresh dates; which later records supersede earlier framings.>
- **Names and platform artifacts:** <The normalizations applied, labeled as normalization.>
- **Authority:** for live status, exact figures, and worked examples, the source systems remain authoritative. This pack is the distilled reading, not a replacement.

## Corrections carried forward

<Numbered list. Each item names a divergence from an earlier instruction document and the later, corrected state that is now canonical. Write "No open discrepancies" only when that is true.>

## Open gaps carried to the line

| # | Gap | Why it is open | Owner it reverts to | Banked artifact |
|---|---|---|---|---|
| 1 | <what remains> | <external dependency, deferred decision> | <Given Surname, role> | <live link> |
```

The subject count in the opening paragraph must equal the number of subject files, and every subject file must appear under The subjects. The audit script checks both.

## The open-gaps register and terminal states

When work is in flight at closure, the register records how each item ended.

- **Done** asserts that the acceptance criteria were met and the control demonstrably holds.
- **Canceled, descoped, or reverted** asserts that the work was set aside or blocked by a dependency that could not close within the engagement.

These are not interchangeable. A story closed Done whose criteria were not met makes a false claim to everyone who reads it after the authors are gone. On a story that asserts a control (a signing path, an access guardrail), a false Done asserts an unproven control.

For work that cannot reach Done because its remaining gates belong to someone else, record a **closure with reversion**: the artifact in the team's hands is committed as the terminal state, and each external gate is named against the person or organization that keeps it. Nothing leaves scope silently.

When a disposition looks wrong in the tracker (a Done that the criteria do not support) and nobody has filed the correction, record it in the register as a disposition-accuracy concern, with the artifact that would settle it.
