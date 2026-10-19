# Package layout

## Two artifacts per diagram

| Type | What it is |
|---|---|
| Importable diagram (`.mmd`) | The canonical Mermaid source and the source of record. This is the file to import. |
| Companion (`.companion.md`) | Executive Summary, an embedded copy of the diagram, Walkthrough, References. Explains what is in the diagram. |

The companion embeds a copy for inline rendering. When the two diverge, the `.mmd` wins and the companion is fixed. Regenerate the embedded copy from the `.mmd` with a script. Never edit it by hand. The audit script compares the two after dropping `%%` comments and blank lines.

## Folder layout

```
<package>/
  00-README.md
  diagrams/
    C4-L1-system-context.mmd
    C4-L2-container-view.mmd
    C4-L3-<slice>.mmd
  companions/
    C4-L1-system-context.companion.md
    ...
```

Pick one layout and make every relative link match it. A package written with `diagrams/` and `companions/` subfolders and then zipped flat leaves every companion link pointing at `../diagrams/...`, which resolves to nothing. The audit script reports unresolved relative links.

File names: `C4-L1-system-context`, `C4-L2-container-view`, `C4-L3-<slice>`. Slice names describe a concern (logging-pipeline, dr, evidence-bundling). Renaming a file changes the package's interface, so it counts as a MAJOR change.

## The `.mmd` header

```
%% <System> Ecosystem - C4 L2 - Container View
%% Hybrid as-is/to-be. <Excluded scope> held off-canvas by driver: <the driver>.
%% Governing decision: <ADR or ticket, with its identifier>.
%% State grammar: present | planned (◇) | sunsetting (⟢) | partial (◐) | parked (⏸) | superseded (✕)
%% Importable into Lucid via Mermaid import. Canonical source for this diagram.
flowchart TB
```

The `State grammar:` line lists the states the diagram uses. Add `Governing decision:` when one record explains the diagram's shape, and a line for any slice drawn wholly in one state. The class block closes the file (see `state-grammar.md`).

## The companion

```
# <System> - C4 **L2 · Container View**

**C4 level:** 2, Container · **View:** Hybrid *as-is / to-be* · **Scope note:** <Excluded scope> held off the canvas by driver: <the driver>
**State legend:** `Present` · `Sunsetting ⟢` · `Planned ◇` · `Partial ◐` · `Parked ⏸` · `Superseded ✕`
**Importable diagram:** [`C4-L2-container-view.mmd`](<relative link>): Mermaid; import into Lucid via *Insert → Mermaid*
**Supersedes:** <the prior diagram, with a live link, when one exists>
**Prepared by:** <Given Surname, role> · baseline <YYYY-MM-DD>, packaged <YYYY-MM-DD> · **Version:** <x.y.z>

---

## Executive Summary

<Two paragraphs of prose. The first fixes what the view is for and what it shows. The second says what the state encoding reveals about the estate: what is real today, what is arriving, what is retiring, what is deferred and why. Draft or parked status, when it applies, is stated here.>

## Diagram

```mermaid
<exact copy of the .mmd body>
```

## Walkthrough

- **<Element or group>.** <One line: what it is, its state, its relationships that matter.>

## References

- Confluence: [<page title>](<live link>)
- Jira: [<ticket key and title>](<live link>)
- Repository: [<path or MR>](<live link>)
```

Rules for the prose:

- **The Executive Summary describes the system.** It carries no instructions for reading a diagram and no commentary on the drawing.
- **The Walkthrough is a list of lines.** One bullet per element or relationship group, bold name first. A bullet that needs a paragraph belongs in a sibling document.
- **References are live links only,** grouped by system. Cite the evidence behind every non-obvious state.
- **The title line may use a dash.** It is a structural label. The `.mmd` title may not (ASCII only).

## The README

```
# <System> - C4 Diagram Package

<One paragraph: the count of diagrams, the two forms of each, and the system in focus.>

*Packaged <YYYY-MM-DD> against the C4 baseline of <YYYY-MM-DD>. Version <x.y.z>. Diagrams reflect the platform as a hybrid as-is / to-be. Where a later decision has overtaken an earlier one, the diagram and its companion say so.*

## Two artifact types
<table from the section above>

## State-encoding grammar
<the seven-row table from state-grammar.md, with its Look column>

## The set
### Level 1: System Context
- [`C4-L1-system-context`](<path>) · [companion](<path>)
### Level 2: Container View
...
### Level 3: Component slices (<n>)
- [`C4-L3-<slice>`](<path>) · [companion](<path>): <flag: "draft (composed, not finalized)" or "parked by decision">

## Notes on currency
<One entry per superseded or merged decision: what governs now, what the diagram draws as superseded, and the live link to the governing record.>

## Conventions
<Names Given Surname; no @-prefixed mentions; ASCII diagram titles; live links only.>
```

The count stated in the first paragraph must equal the number of diagrams in the set. The audit script checks it.

## Importing into Lucid

In the Lucid document, **Insert → Mermaid**, then paste the contents of the `.mmd`. The diagrams also render as-is in GitHub, VS Code, Obsidian, and Confluence's Mermaid macro.

Platform behavior observed in practice (verify against current tooling, since it changes):

- The importer transliterates em-dashes in titles into replacement characters. Keep titles ASCII.
- A programmatic Lucid connector may offer no Mermaid-ingestion call. Import through the UI, or create shapes from a specification with explicit bounding boxes and assisted layout off.
- People resize and regroup shapes between sessions. Re-fetch the document before any edit pass, since cached state goes stale.
- Moving documents between folders may be unavailable through the API. Leave that to the user.
