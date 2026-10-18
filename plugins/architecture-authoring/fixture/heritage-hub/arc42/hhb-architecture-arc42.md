# Heritage Hub for the Example Heritage Trust: Architecture Document

**arc42 · Version 0.3.1**

| | |
|---|---|
| Version | 0.3.1 |
| Status | Structure established, registers opened, components registered. Not yet reviewed by the Trust |
| Date | 18 September 2026 |
| Scope | A headless content management platform serving the websites of the Trust's six museums and a shared collections search |
| Author | Lena Okafor, Example Consulting |
| Audience | Internal. §1, §3, §4, §5 and §7 are candidates for a client-facing derivative. §2.3 is not |
| Companion documents | None imported |
| Sibling document | [`hhb-estimate-arc42.md`](hhb-estimate-arc42.md), the estimate exercised over this architecture. It cites this document's registers; this document never cites the estimate's |

## Sourcing rule

Every statement traces to the CMS vendor's published documentation read on the date given, the discovery workshop recorded on 2 September 2026, the pilot site deployed at pilot.example.com, or a named person on a named occasion. Everything else carries a marker, and the markers are the following.

| Marker | Meaning | Registered in |
|---|---|---|
| `[I]` | Inference drawn from documented facts. Not stated by any source | Inline, wherever used |
| `[A-nn]` | Assumption or open item: anything this document leans on that no checkable source carries yet. Each carries its current basis, an owner, and the condition that closes it | §11.5, eleven entries |
| `[AD-nn]` | Architecture decision, with status and consequence | §9 |
| `[R-nn]` | Architectural risk, with consequence | §11.1 |
| `[Q-nn]` | Quality goal | §1.3 |
| `[C-nn]` | Component: an element the Trust receives | §5.4, six entries |
| `[HHB-TYPE-nn]` | Diagram asset, tracked with build status | §8.8 |

Cross-document section references are qualified by role: `architecture §5`, `estimate §5`. A bare `§n` refers to this document.

## 1. Introduction and Goals

### 1.1 What the system does

Heritage Hub gives the Trust one content repository for six museum websites and a shared collections search, the Collections Explorer. Editors author once and publish to any site. The pilot site at pilot.example.com runs on the same platform today.

### 1.2 Requirements overview

The Trust asked for shared authoring across sites, a single collections search, and localization into English and Welsh, at the workshop of 2 September 2026.

### 1.3 Quality goals

| ID | Goal | Basis |
|---|---|---|
| `[Q-01]` | An editor's change is live on every affected site within five minutes of publishing | Workshop, 2 September 2026 |
| `[Q-02]` | Collections search answers within one second at the Trust's stated peak | Workshop, 2 September 2026; peak load is `[A-02]` |
| `[Q-03]` | Every page is available in English and Welsh | Workshop, 2 September 2026 |

### 1.4 Stakeholders

Maya Lindqvist, Head of Digital at the Trust, owns scope. Tom Achebe, the Trust's collections systems lead, owns the collections data. Lena Okafor leads the architecture for Example Consulting.

## 2. Architecture Constraints

### 2.1 Vendor platform constraints

The CMS delivers content through a read API with a documented limit on requests per second, published on the vendor's limits page read on 4 September 2026. The vendor hosts the authoring interface.

### 2.2 Trust platform constraints

The collections database stays in the Trust's own data center, per Tom Achebe at the workshop of 2 September 2026.

### 2.3 Organizational and commercial constraints

The Trust's digital budget for this financial year is fixed and the incumbent web agency's support contract ends on 31 March 2027, per Maya Lindqvist on 2 September 2026. The Trust has not told the incumbent agency.

## 3. Context and Scope

### 3.1 Business context

Editors at six museums author content. Visitors read the sites and search collections. The collections database feeds the Collections Explorer through a nightly export `[A-05]`.

### 3.2 Out of scope

Ticketing and the online shop stay on their current platforms.

## 4. Solution Strategy

Content lives once in the CMS and is published to every site through a shared delivery layer, as `[AD-05]` settled. Search runs on an index fed from the collections export, so the collections database never serves public traffic. The five-minute goal in `[Q-01]` rests on edge cache invalidation at publish time `[A-03]`.

Six sites sharing one content model will diverge in their page templates within a year `[I]`. The inference rests on two documented facts: the pilot already needed three site-specific templates, and the Trust plans a separate exhibition calendar per museum. It is an inference and no one owns it; it is withdrawn if the template count stops growing.

The vendor's limits page states the read API limit, and the pilot measured its peak at a fraction of it. Whether the six sites together stay under the limit is the open question `[A-02]`, filed as an open item and not as an inference, because the Trust holds the traffic figures that would close it and has named an owner for them.

## 5. Building Block View

### 5.1 Level 1

The platform has three blocks: authoring (the CMS), delivery (the site renderer and the edge cache), and search (the index and its loader).

### 5.4 Component register

| ID | Component | Responsibility | Runs on |
|---|---|---|---|
| `[C-01]` | CMS content model | Content types shared by all six sites | Vendor-hosted CMS |
| `[C-02]` | Site renderer | Builds pages per site from the content API | Trust cloud subscription |
| `[C-03]` | Edge cache | Serves pages and purges on publish | CDN |
| `[C-04]` | Search index | Answers Collections Explorer queries | Trust cloud subscription |
| `[C-05]` | Collections loader | Loads the nightly export into the index | Trust cloud subscription |
| `[C-06]` | Translation workflow | Routes Welsh translations to the Trust's translators | Vendor-hosted CMS |

## 6. Runtime View

The Trust has stated no runtime scenario beyond publishing and searching. No scenario was inferred.

## 7. Deployment View

The CMS is vendor-hosted. The renderer, index and loader run in the Trust's cloud subscription; the collections database stays on premises per §2.2.

## 8. Cross-cutting Concepts

### 8.1 Published and live

A page is **published** when an editor approves it in the CMS. It is **live** when the edge cache serves the new version. The two differ by the purge time that `[Q-01]` bounds, and the documents never use one word for the other.

### 8.8 Diagram asset register

| ID | Asset | Status |
|---|---|---|
| `[HHB-CTX-01]` | System context | Built |
| `[HHB-CNT-01]` | Container view | Not built |

## 9. Architecture Decisions

| ID | Decision | Status | Consequence |
|---|---|---|---|
| `[AD-01]` | One content model serves all six sites | Accepted | Template divergence is handled in the renderer |
| `[AD-02]` | Search runs on a separate index, never on the collections database | Accepted | `[C-05]` is needed |
| `[AD-03]` | Each site gets its own CMS space | Superseded by `[AD-05]` | Kept for the record |
| `[AD-04]` | Welsh translation is routed inside the CMS | Accepted | `[C-06]` carries it |
| `[AD-05]` | One CMS space with per-site publishing rules, replacing `[AD-03]` | Accepted | Editors author once |

## 10. Quality Requirements

The quality goals in §1.3 are the Trust's statements. No measurable target beyond them was stated, and none was inferred.

## 11. Risks and Technical Debt

### 11.1 Architectural risks

| ID | Risk | Consequence |
|---|---|---|
| `[R-01]` | Read API limit exceeded at combined peak | Pages served stale until the limit resets |
| `[R-02]` | The nightly export misses a day | Search shows the previous day's collection |
| `[R-03]` | Template divergence outgrows the shared renderer | Renderer forks per site |

### 11.5 Assumption and open-item register

| ID | Entry | Current basis | Owner | Closes when |
|---|---|---|---|---|
| `[A-01]` | The Trust's editors number about forty | Maya Lindqvist, 2 September 2026 | Maya Lindqvist | The Trust's staff list is shared |
| `[A-02]` | Combined peak traffic stays under the read API limit | Pilot measurement only | Tom Achebe | Six months of site traffic figures are shared |
| `[A-03]` | The CDN purges a page within two minutes | Vendor marketing page | Lena Okafor | A purge timing test runs on the pilot |
| `[A-04]` | The pilot runs on the current CMS release | Closed: vendor release notes, 4 September 2026 | Lena Okafor | Closed |
| `[A-05]` | The collections database can export nightly | Tom Achebe, 2 September 2026 | Tom Achebe | One export lands in the test index |
| `[A-06]` | Welsh translators work inside the CMS | Maya Lindqvist, 2 September 2026 | Maya Lindqvist | Translators confirm in writing |
| `[A-07]` | The renderer can run in the Trust subscription | No source yet | Tom Achebe | The Trust's cloud team confirms quota |
| `[A-08]` | Six sites launch in two waves | Maya Lindqvist, 2 September 2026 | Maya Lindqvist | The Trust approves the wave plan |
| `[A-09]` | A seventh site joins in 2027 | Withdrawn: Maya Lindqvist, 10 September 2026 | Maya Lindqvist | Withdrawn |
| `[A-10]` | Image rights metadata exists for the collection | No source yet | Tom Achebe | A sample export carries it |
| `[A-11]` | The vendor keeps the content API stable through 2027 | No source yet | Lena Okafor | The vendor's deprecation policy is read |

## 12. Glossary

**Live.** Served by the edge cache. See §8.1.

**Published.** Approved in the CMS. See §8.1.

**Collections Explorer.** The Trust's name for the shared collections search. The documents use no other name for it.

## Versioning

This document follows Semantic Versioning, adapted for documents. MAJOR for a change invalidating a decision a reader could reasonably have made on the previous version; MINOR for backward-compatible addition; PATCH for correction without consequence. Below 1.0.0 a MINOR bump may carry breaking changes. History is recorded in [`CHANGELOG.md`](../CHANGELOG.md), under this document's own heading.
