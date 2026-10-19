# Sample Platform - C4 **L1 · System Context**

**C4 level:** 1, System Context · **View:** Hybrid *as-is / to-be* · **Scope note:** Regional replica held off the canvas by driver: data-residency decision of 2026-09-01
**Importable diagram:** [`C4-L1-system-context.mmd`](../diagrams/C4-L1-system-context.mmd)
**Prepared by:** Jane Doe, Architect · baseline 2026-10-01 · **Version:** 0.1.0

---

## Executive Summary

A smoke-test sample for the package audit. Editors author content that the platform stores and will index.

## Diagram

```mermaid
%% Sample Platform - C4 L1 - System Context
%% Hybrid as-is/to-be. Regional replica held off-canvas by driver: data-residency decision of 2026-09-01.
%% State grammar: focus | present | planned (◇) | sunsetting (⟢)
%% Importable into Lucid via Mermaid import. Canonical source for this diagram.
flowchart TB
  U(["Editors"]):::present
  SYS["<b>Sample Platform</b><br/>- system in focus -"]:::focus
  CMS["Content service"]:::present
  SRCH["Search<br/>◇ PLANNED"]:::planned
  OLD["Legacy publisher<br/>⟢ SUNSETTING"]:::sunsetting
  U -->|"author content"| SYS
  SYS -->|"store content"| CMS
  SYS -.->|"index content"| SRCH
  OLD -.->|"publishes nightly (retiring)"| SYS
  classDef focus fill:#111111,stroke:#111111,stroke-width:3px,color:#ffffff;
  classDef present fill:#eef2ff,stroke:#111111,stroke-width:2px,color:#111111;
  classDef sunsetting fill:#fff4e5,stroke:#e08600,stroke-width:2px,stroke-dasharray:6 3,color:#111111;
  classDef planned fill:#f5faff,stroke:#1f6feb,stroke-width:2px,stroke-dasharray:2 3,color:#0b4ea2;
  classDef parked fill:#f2f2f2,stroke:#8a8a8a,stroke-width:2px,stroke-dasharray:2 3,color:#555555;
  classDef superseded fill:#ffecec,stroke:#c0111a,stroke-width:2px,stroke-dasharray:6 3,color:#8a0f16;

```

## Walkthrough

- **Content service.** Present; stores authored content.

## References

- Sample: [Example decision record](https://example.com/adr/1)
