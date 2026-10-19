# {{SYSTEM}} for {{CLIENT}}: Estimate Document

**arc42 · Version 0.1.0**

| | |
|---|---|
| Version | 0.1.0 |
| Status | Structure established, registers opened empty. Figures not yet accepted |
| Date | {{DATE}} |
| Estimates against | Architecture document 0.1.0. A MAJOR bump of the architecture obligates a review of this document; a change to the `[C-nn]` register obligates a review of §5 |
| Scope | Effort, milestone structure and staffing for building {{SYSTEM}} |
| Author | {{AUTHOR}} |
| Audience | Internal. <fill: candidate sections for a client-facing derivative; §2, §7 and §11.3 are excluded by default> |
| Sibling document | [`{{prefix}}-architecture-arc42.md`]({{prefix}}-architecture-arc42.md), the system this document prices |

## Reading arc42 as a plan template

This document applies the twelve arc42 sections to a plan. §5, the building block view, holds the work breakdown. §6, the runtime view, holds the milestone sequence. §7, the deployment view, holds the staffing. The other sections keep their usual reading.

## Sourcing rule

This document inherits the architecture's sourcing rule and adds its calibration anchor: <fill: the measured build the effort unit is defined against>.

Series this document owns:

| Series | Meaning | Registered in |
|---|---|---|
| `[EA-nn]` | An estimate assumption: an assertion the offer makes, with a figure or condition, an owner, and the consequence if it proves false | §2.2, zero entries |
| `[M-nn]` | A milestone, with its exit criterion in §10 | §6 |
| `[ED-nn]` | An estimating decision, with status, rationale and consequence | §9 |
| `[ER-nn]` | An estimate risk that is not a single `[EA-nn]` proving false | §11.1 |
| `[{{PREFIX}}-RDM-nn]` | A roadmap diagram asset, tracked with build status | §8.4 |

Series this document cites and never defines: `[A-nn]`, `[C-nn]`, `[AD-nn]`, `[R-nn]` and `[Q-nn]`, all owned by the architecture document.

## 1. Introduction and Goals

### 1.1 What is being offered

## 2. Constraints

### 2.1 Inherited from the architecture

### 2.2 Estimate assumption register

| ID | Assumption | Figure or condition | Owner | If false |
|---|---|---|---|---|

## 3. Context and Scope

### 3.1 Sources in the offer

### 3.2 Client actions that gate milestones

### 3.3 Out of the offer

## 4. Estimation Strategy

## 5. Work Breakdown

### 5.1 Backlog

| Component | Milestone | Build status | Effort | Leans on |
|---|---|---|---|---|

### 5.2 Effort by milestone

| Milestone | Effort |
|---|---|

## 6. Milestone Sequence

| ID | Milestone | Content | Decision records | Effort |
|---|---|---|---|---|

## 7. Staffing

## 8. Cross-cutting Concepts

### 8.1 The effort unit

### 8.4 Diagram asset register

| ID | Asset | Status |
|---|---|---|

## 9. Estimating Decisions

| ID | Decision | Status | Rationale | Consequence |
|---|---|---|---|---|

## 10. Exit Criteria

| Milestone | Exit criterion |
|---|---|

## 11. Risks

### 11.1 Estimate risk register

| ID | Risk | Consequence | Mitigation in the plan |
|---|---|---|---|

### 11.2 Sensitivity

### 11.3 Commercial framing

## 12. Glossary

## Versioning

This document follows Semantic Versioning, adapted for documents. Below 1.0.0 a MINOR bump may carry breaking changes. It pins the architecture version it estimates against, under semantic-versioning compatibility. History is recorded in [`CHANGELOG.md`](../CHANGELOG.md).
