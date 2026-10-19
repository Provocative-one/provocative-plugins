# Heritage Hub for the Example Heritage Trust: Estimate Document

**arc42 · Version 0.2.0**

| | |
|---|---|
| Version | 0.2.0 |
| Status | Structure and figures drafted. Figures not yet accepted by the commercial lead |
| Date | 19 September 2026 |
| Estimates against | Architecture document 0.3.0. A MAJOR bump of the architecture obligates a review of this document; a change to the `[C-nn]` register obligates a review of §5 |
| Scope | Effort, milestone structure and staffing for building Heritage Hub |
| Author | Lena Okafor, Example Consulting |
| Audience | Internal. §1, §3, §6 and §10 are candidates for a client-facing derivative. §2, §7 and §11.3 are not |
| Sibling document | [`hhb-architecture-arc42.md`](hhb-architecture-arc42.md), the system this document prices |

## Reading arc42 as a plan template

This document applies the twelve arc42 sections to a plan. §5, the building block view, holds the work breakdown. §6, the runtime view, holds the milestone sequence. §7, the deployment view, holds the staffing. The other sections keep their usual reading.

## Sourcing rule

This document inherits the architecture's sourcing rule and adds one source: the commit history of the pilot site build, used as the calibration anchor.

Series this document owns:

| Series | Meaning | Registered in |
|---|---|---|
| `[EA-nn]` | An estimate assumption: an assertion the offer makes, with a figure or condition, an owner, and the consequence if it proves false | §2.2, six entries |
| `[M-nn]` | A milestone, with its exit criterion in §10 | §6 |
| `[ED-nn]` | An estimating decision, with status, rationale and consequence | §9 |
| `[ER-nn]` | An estimate risk that is not a single `[EA-nn]` proving false | §11.1 |
| `[HHB-RDM-nn]` | A roadmap diagram asset, tracked with build status | §8.4 |

Series this document cites and never defines: `[A-nn]`, `[C-nn]`, `[AD-nn]`, `[R-nn]` and `[Q-nn]`, all owned by the architecture document.

## 1. Introduction and Goals

### 1.1 What is being offered

The build of the six components the architecture registers in §5.4, in the milestone order the commercial lead set.

## 2. Constraints

### 2.1 Inherited from the architecture

Every open item the architecture carries in its §11.5 is a constraint here until it closes.

### 2.2 Estimate assumption register

| ID | Assumption | Figure or condition | Owner | If false |
|---|---|---|---|---|
| `[EA-01]` | One site-build equivalent (SBE) is the effort of the pilot site build | 1 SBE = 12 person-days, from the pilot commit history | Lena Okafor | Every figure rescales; the structure holds |
| `[EA-02]` | Combined peak traffic stays under the read API limit, converting `[A-02]` | Peak at most 60 percent of the published limit | Tom Achebe | A caching tier is added at 1.5 SBE |
| `[EA-03]` | The Trust approves the wave plan of `[A-08]` | Within ten business days of the request | Maya Lindqvist | The second milestone date moves through change control |
| `[EA-04]` | Welsh translators are onboarded, per `[A-06]` | Before the second milestone starts | Maya Lindqvist | Welsh pages ship after the second milestone |
| `[EA-05]` | The collections database exports nightly, per `[A-05]` | First export lands before the first milestone closes | Tom Achebe | The loader is reworked at 1 SBE |
| `[EA-06]` | One SBE takes two and a half calendar weeks with the stated team | 2.5 weeks per SBE | Lena Okafor | Written durations slip; see `[ER-02]` |

## 3. Context and Scope

### 3.2 Trust actions that gate milestones

The Trust approves the wave plan `[EA-03]` and onboards its translators `[EA-04]`. Effort and these lead times never share a column.

## 4. Estimation Strategy

Every figure is a multiple of the SBE in `[EA-01]`, so correcting the anchor rescales the total without touching the structure.

## 5. Work Breakdown

### 5.1 Backlog

| Component | Milestone | Build status | Effort (SBE) | Leans on |
|---|---|---|---|---|
| `[C-01]` | `[M-01]` | Built in the pilot | 0.5 | `[AD-05]` |
| `[C-02]` | `[M-01]` | Partly built | 1.5 | `[AD-01]` |
| `[C-03]` | `[M-01]` | Not built | 0.5 | `[A-03]` |
| `[C-04]` | `[M-02]` | Not built | 1.0 | `[AD-02]` |
| `[C-05]` | `[M-02]` | Not built | 1.0 | `[EA-05]` |
| `[C-06]` | `[M-03]` | Not built | 1.0 | `[EA-04]` |

### 5.2 Effort by milestone

| Milestone | Effort (SBE) |
|---|---|
| `[M-01]` | 2.5 |
| `[M-02]` | 2.0 |
| `[M-03]` | 1.0 |

## 6. Milestone Sequence

| ID | Milestone | Content | Decision records | Effort |
|---|---|---|---|---|
| `[M-01]` | First wave live | Three museum sites on the shared platform | `[ED-01]` | 2.5 SBE |
| `[M-02]` | Collections Explorer live | Search over the nightly export | `[ED-03]` | 2.0 SBE |
| `[M-03]` | Second wave and Welsh | Remaining sites, Welsh pages | `[ED-03]` | 1.0 SBE |

## 7. Staffing

Two developers and one architect at half time, per Lena Okafor on 19 September 2026.

## 8. Cross-cutting Concepts

### 8.1 The site-build equivalent

The SBE is defined in `[EA-01]` and anchored on the pilot commit history.

### 8.4 Diagram asset register

| ID | Asset | Status |
|---|---|---|
| `[HHB-RDM-01]` | Milestone roadmap | Not built |

## 9. Estimating Decisions

| ID | Decision | Status | Rationale | Consequence |
|---|---|---|---|---|
| `[ED-01]` | Effort is stated in SBE | Accepted | The pilot is the only measured build | Figures rescale with `[EA-01]` |
| `[ED-02]` | Duration is offered only in conversation | Superseded by `[ED-03]` | Durations depend on Trust lead times | Kept for the record |
| `[ED-03]` | Duration is stated in writing per milestone, converted through `[EA-06]` | Accepted | The Trust asked for durations in writing on 12 September 2026 | A written duration creates exposure, registered as `[ER-02]` |

## 10. Exit Criteria

| Milestone | Exit criterion |
|---|---|
| `[M-01]` | Three named museum sites are live on the shared platform, and an editor's change is live within five minutes, measured by the Trust |
| `[M-02]` | The Collections Explorer answers the Trust's twenty test queries within one second each |
| `[M-03]` | All six sites are live, and every page has a Welsh version reviewed by the Trust's translators |

## 11. Risks

### 11.1 Estimate risk register

| ID | Risk | Consequence | Mitigation in the plan |
|---|---|---|---|
| `[ER-01]` | The CMS vendor changes its content API during the build | Renderer rework of unknown size | `[A-11]` is closed before the second milestone |
| `[ER-02]` | Written durations become a fixed commitment | Slippage absorbed at Example Consulting's cost | Durations are restated at each milestone gate |

A late or missing nightly export is not an estimate risk. It is `[EA-05]` proving false, and its consequence lives in that row's If false cell.

### 11.2 Sensitivity

In order: the anchor `[EA-01]`, conditional scope `[EA-02]`, the quality goal `[Q-01]`, and Trust lead time `[EA-03]`. The vendor risk `[ER-01]` sits outside the sensitivity order because no figure carries it.

### 11.3 Commercial framing

The engagement is offered at a fixed fee per milestone.

## 12. Glossary

**SBE.** Site-build equivalent. See §8.1.

## Versioning

This document follows Semantic Versioning, adapted for documents. Below 1.0.0 a MINOR bump may carry breaking changes. It pins the architecture version it estimates against; the pin advances when this document is re-derived. History is recorded in [`CHANGELOG.md`](../CHANGELOG.md).
