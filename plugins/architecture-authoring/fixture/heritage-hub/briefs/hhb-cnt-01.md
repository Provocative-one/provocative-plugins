# Brief: `[HHB-CNT-01]` container view

**Source:** architecture 0.3.1. **Asset:** `arc42/assets/hhb-cnt-01.svg`. **Status:** Not built. **Audience:** internal

## What the diagram must show

| Element | Label on canvas | Kind | Traces to |
|---|---|---|---|
| Shared content types | CMS content model | Container | `[C-01]` |
| Page builder per site | Site renderer | Container | `[C-02]` |
| Page delivery and purge | Edge cache | Container | `[C-03]` |
| Collections search | Search index | Container | `[C-04]` |
| Nightly load into the index | Collections loader | Container | `[C-05]` |
| Welsh translation routing | Translation workflow | Container | `[C-06]` |
| The Trust's collections database | Collections database | External system | architecture §2.2 |

**Arrows:** dependencies

**Other text on canvas:** Heritage Hub

## Acceptance run

1. Every element above appears on the canvas, and nothing else.
2. Every arrow has a counterpart in architecture §5.4 or §3.1.
3. Text stays text, a viewBox is set, and nothing external is referenced.
4. No internal identifier appears on the canvas.
