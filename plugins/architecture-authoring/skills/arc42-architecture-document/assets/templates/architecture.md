# {{SYSTEM}} for {{CLIENT}}: Architecture Document

**arc42 · Version 0.1.0**

| | |
|---|---|
| Version | 0.1.0 |
| Status | Structure established, registers opened empty. Not yet reviewed |
| Date | {{DATE}} |
| Scope | <fill: one sentence on what the system is and for whom> |
| Author | {{AUTHOR}} |
| Audience | Internal. <fill: which sections may feed a client-facing derivative, and which may not> |
| Companion documents | None imported |
| Sibling document | [`{{prefix}}-estimate-arc42.md`]({{prefix}}-estimate-arc42.md), the estimate exercised over this architecture. It cites this document's registers; this document never cites the estimate's |

## Sourcing rule

Every statement traces to <fill: the sources this set admits, each named concretely>. Everything else carries a marker, and the markers are the following.

| Marker | Meaning | Registered in |
|---|---|---|
| `[I]` | Inference drawn from documented facts. Not stated by any source | Inline, wherever used |
| `[A-nn]` | Assumption or open item: anything this document leans on that no checkable source carries yet. Each carries its current basis, an owner, and the condition that closes it | §11.5, zero entries |
| `[AD-nn]` | Architecture decision, with status and consequence | §9 |
| `[R-nn]` | Architectural risk, with consequence | §11.1 |
| `[Q-nn]` | Quality goal | §1.3 |
| `[C-nn]` | Component: an element the client receives, or a delivery tool that produces it | §5.4, zero entries |
| `[{{PREFIX}}-TYPE-nn]` | Diagram asset, tracked with build status | §8.8 |

Cross-document section references are qualified by role: `architecture §5`, `estimate §5`. A bare `§n` refers to this document.

## 1. Introduction and Goals

### 1.1 What the system does

### 1.2 Requirements overview

### 1.3 Quality goals

| ID | Goal | Basis |
|---|---|---|

### 1.4 Stakeholders

## 2. Architecture Constraints

### 2.1 Vendor platform constraints

### 2.2 Client platform constraints

### 2.3 Organizational and commercial constraints

## 3. Context and Scope

### 3.1 Business context

### 3.2 Out of scope

## 4. Solution Strategy

## 5. Building Block View

### 5.1 Level 1

### 5.4 Component register

| ID | Component | Responsibility | Runs on |
|---|---|---|---|

## 6. Runtime View

The client has stated no runtime scenario yet. No scenario was inferred.

## 7. Deployment View

## 8. Cross-cutting Concepts

### 8.8 Diagram asset register

| ID | Asset | Status |
|---|---|---|

## 9. Architecture Decisions

| ID | Decision | Status | Consequence |
|---|---|---|---|

## 10. Quality Requirements

The quality goals in §1.3 are the client's statements. No measurable target beyond them was stated, and none was inferred.

## 11. Risks and Technical Debt

### 11.1 Architectural risks

| ID | Risk | Consequence |
|---|---|---|

### 11.2 Technical debt

### 11.5 Assumption and open-item register

| ID | Entry | Current basis | Owner | Closes when |
|---|---|---|---|---|

## 12. Glossary

## Versioning

This document follows Semantic Versioning, adapted for documents. MAJOR for a change invalidating a decision a reader could reasonably have made on the previous version; MINOR for backward-compatible addition; PATCH for correction without consequence. Below 1.0.0 a MINOR bump may carry breaking changes. History is recorded in [`CHANGELOG.md`](../CHANGELOG.md), under this document's own heading.
