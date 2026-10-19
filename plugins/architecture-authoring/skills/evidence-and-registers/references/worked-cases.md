# Worked cases and register shapes

## Column shapes

| Register | Home | Columns |
|---|---|---|
| Quality goals `[Q-nn]` | architecture §1.3 | ID, Goal, Basis |
| Components `[C-nn]` | architecture §5.4 | ID, Component, Responsibility, Runs on |
| Diagram assets | architecture §8.8, estimate §8.4 | ID, Asset, Status |
| Decisions `[AD-nn]` | architecture §9 | ID, Decision, Status, Consequence |
| Risks `[R-nn]` | architecture §11.1 | ID, Risk, Consequence |
| Assumptions and open items `[A-nn]` | architecture §11.5 | ID, Entry, Current basis, Owner, Closes when |
| Estimate assumptions `[EA-nn]` | estimate §2.2 | ID, Assumption, Figure or condition, Owner, If false |
| Milestones `[M-nn]` | estimate §6 | ID, Milestone, Content, Decision records, Effort |
| Estimating decisions `[ED-nn]` | estimate §9 | ID, Decision, Status, Rationale, Consequence |
| Estimate risks `[ER-nn]` | estimate §11.1 | ID, Risk, Consequence, Mitigation in the plan |

Every register table's header starts with `ID`. The audit treats a row as a definition only inside such a table, so a backlog that lists `[C-nn]` against `[M-nn]` cites both series without defining either.

Build status of a component lives in the estimate's backlog, never in the architecture: the architecture says what a component is, the estimate says whether it is built and when. Diagram assets are the exception, since each asset belongs to the document that uses it.

## Case 1. One person's word

> The Trust's editors number about forty.

Maya Lindqvist said it at the workshop. No document states it. Filed as `[A-01]`: basis "Maya Lindqvist, 2 September 2026", owner Maya Lindqvist, closes when the staff list is shared. The prose cites `[A-01]` wherever the number is used.

## Case 2. A genuine inference

> Six sites sharing one content model will diverge in their page templates within a year.

Two documented facts support it: the pilot needed three site-specific templates, and each museum plans its own exhibition calendar. Nobody can close it before a year passes, and nobody owns it. Marked `[I]`, with the facts stated beside it and the withdrawal condition ("withdrawn if the template count stops growing").

## Case 3. The borderline, argued

> The six sites together stay under the vendor's read limit.

It looks like an inference from the limits page and the pilot measurement. It is filed as `[A-02]` because the client holds the traffic figures that would settle it, and a named person owns producing them. The test is closure: a statement someone can close with a checkable source is a register entry. The text says so in architecture §4, so a reviewer sees the reasoning.

## Case 4. An open item becomes priceable

`[A-02]` cannot be priced. The estimate converts it: `[EA-02]` asserts "peak at most 60 percent of the published limit", owned by the client's systems lead, with the consequence "a caching tier is added at 1.5 SBE" if false. The `[EA-02]` row cites `[A-02]`. The architecture never cites `[EA-02]`.

## Case 5. Closed, withdrawn, superseded

- `[A-04]` closed: the basis cell names the vendor release notes and the date. The row stays.
- `[A-09]` withdrawn: the client dropped the seventh site, and the row says who withdrew it and when. Its number is never reused; the next free ID is `[A-12]`.
- `[AD-03]` superseded: its status reads "Superseded by `[AD-05]`", and `[AD-05]` names what it replaced.

## A refusal, as it should read

> Close `[A-05]`, the export works.

"I can close `[A-05]` when there is something checkable: the closing condition is one export landing in the test index. If that has happened, send the run log or the date and who confirmed it, and I will record it in the basis cell and set the row to Closed."
