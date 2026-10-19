# Architecture Continuity

Five skills for architects and tech leads who document an estate and hand it on. Two do the work: a C4 documentation method with a state-encoding grammar, and a closure method that preserves knowledge after its authors leave. Three are embedded inside both and also work alone: blunt critique, semantic-versioning classification, and AI-marker language hygiene.

The plugin assumes a reader with a Software Engineering or Software Architecture background. It does not teach what a container diagram or an ADR is. It makes the record hold up when the people who wrote it are gone.

## The two workflow skills

| Skill | Produces | Reach for it when |
|---|---|---|
| `c4-diagram-package` | A C4 package: Mermaid diagrams (system context, container view, component slices) under one state grammar (present, sunsetting, planned, partial, parked, superseded). Each diagram has a source-of-record `.mmd`, a narrated companion, and a README index. An audit script catches drift | You document an estate that is mid-transition, refresh an existing baseline, or hand an architecture over |
| `closure-extraction-handoff` | **Extract mode:** a knowledge pack with one subject per file, recorded sources and currency, supersessions flagged, and an open-gaps register. **Handoff mode:** one self-sufficient resume file for a fresh Claude instance or a successor. An audit script checks the pack | An engagement closes, you roll off a team, or you need work to survive without you |

### What is distinctive in each

- **State grammar.** Every element carries its lifecycle state in style and in a glyph, so the picture survives monochrome print. Exclusions are held off the canvas by a named driver. A state claim needs evidence, and an element without evidence is `planned`.
- **Source of record.** The `.mmd` governs and the companion is regenerated from it. The audit compares the two.
- **No silent reconciliation.** When a later artifact supersedes an earlier one, the pack carries a currency note and says which governs.
- **Honest terminal states.** Done asserts that the criteria were met. Work that was descoped or blocked is recorded with the owner it reverts to.
- **Cold-reader test.** A handoff is attacked as a reader with nothing else would read it, and every open thread carries a closure condition.

## The three embedded skills

| Skill | Job |
|---|---|
| `blunt-critique` | Evidence-grounded critique ordered by damage, with no praise sandwich and an explicit "converged" verdict when nothing real is left |
| `semantic-versioning` | Classifies a change as PATCH, MINOR, or MAJOR (or assigns the first version, 0.1.0) for any versioned subject, with a one-sentence rationale naming the interface involved |
| `stricter-ai-language-hygiene` | Removes machine-written markers from prose and runs a mechanical sweep before a draft is shown |

## Where the embedded skills run

| Workflow skill | blunt-critique | semantic-versioning | stricter-ai-language-hygiene |
|---|---|---|---|
| `c4-diagram-package` | Attacks the package with the C4 checklist and the audit output | Versions the package and classifies each refresh | Sweeps companion and README prose, leaves the Mermaid alone |
| `closure-extraction-handoff` | Audits a pack's fidelity to its sources and attacks a handoff as a cold reader | Versions the pack or handoff and classifies each re-export | Sweeps the author's prose, never the verbatim material |

Each workflow skill loads the three by name. If one is missing, a short digest in `references/shared-substrate.md` (Part D) keeps the workflow running.

## Mechanical audits

- `c4-diagram-package/scripts/audit_c4_package.py` pairs each `.mmd` with its companion and checks section order, embedded-copy drift, the six state classes in every diagram, a state class on every node, glyph and class agreement, grammar drift across diagrams, relative link targets, and the README's diagram count.
- `closure-extraction-handoff/scripts/audit_pack.py` checks index closure between the README and the files, dangling cross-references, source headers, `@`-mentions, relative dates, placeholder links, and counting claims in the README.

Both exit non-zero on a FAIL. A WARN is a candidate that needs judgment.

## Working rules shared by both

- **Draft first.** Nothing is posted to Confluence, Jira, Lucid, GitLab, or Teams until you say so.
- **Verbatim stays verbatim.** The language sweep never touches quoted text, code, Mermaid, or source reproductions.
- **Secrets stay out.** Tokens, keys, and passwords never enter a package. The skills name where they live.
- **Check data handling first.** Before extracting from a source system, the closure skill confirms the material may be processed here and defers to any access-rules policy that covers it.

## Assumptions

The retrieval quirks are written for Confluence, Jira, GitLab, Microsoft Teams, and Lucid, in `references/shared-substrate.md` Part C and the Lucid notes in the C4 skill. The methods transfer to other tools. Connect the relevant MCP servers if you want Claude to retrieve source material itself. Without them, paste or upload the material.

## Install

This repository root is a marketplace that contains the plugin.

```
claude plugin marketplace add <path-or-repository-containing-this-folder>
claude plugin install architecture-continuity@architecture-continuity-marketplace
```

The manifest layout follows Anthropic's public reference plugins. For Cowork, or to load the folder as a local plugin, follow the current plugin documentation, since those steps change.

## Maintenance

The plugin is at version 0.1.0 and follows its own semantic-versioning skill. Its consumers are the people and prompts that depend on skill names, triggers, state-grammar conventions, and prefix-code schemes. Renaming a skill, changing the state classes, or changing the package or pack layout is MAJOR. Adding a skill, a state, or a section is MINOR. Wording fixes are PATCH.

Two things to know before editing:

- `references/shared-substrate.md` is identical in the two workflow skills, so each stands alone. Edit one copy, then copy it to the other.
- The three embedded skills are verbatim copies of the originals (`stricter-ai-language-hygiene` carries its own version, 1.1.0). Update them from their source and keep the copies in sync.
