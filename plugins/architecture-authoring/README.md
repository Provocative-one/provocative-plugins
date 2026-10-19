# Architecture Authoring

Ten skills for writing an architecture document set that a skeptical reader can trust and every client artifact can be derived from. arc42 is the template the documents run on. What the plugin adds is the discipline on top: every statement traces to a declared source or carries a marker, every unknown has a register row with an owner and a closure condition, the estimate depends on the architecture in one direction only, an audit gates every version, and nothing the client reads is retyped.

The method was built over two engagements, the second revising the first, and the plugin encodes the revised form. Its worked example and regression suite is an invented set, Heritage Hub, a content management platform for the fictional Example Heritage Trust.

## The seven workflow skills

| Skill | Use it to |
|---|---|
| `evidence-and-registers` | Decide whether a statement is sourced, an inference `[I]`, an open item `[A-nn]` or a priced estimate assumption `[EA-nn]`; open, extend, close and supersede register rows |
| `arc42-architecture-document` | Scaffold a set, write the twelve sections with their registers, keep the notation key and front matter accurate, version with document semantics |
| `sibling-estimate-document` | Price the architecture as a second arc42 document: calibrated unit, components-by-milestones backlog, outside-checkable exit criteria, sensitivity, a semantically compatible pin |
| `architecture-set-audit` | Run the coherence audit before any version, reconcile a letter or deck against the set, and emit a reissue list |
| `client-facing-derivations` | Generate annexes, milestone plans, decks and clarification answers from the registers, with a brief per artifact and a frozen published copy |
| `diagram-assets` | Register, brief, build and accept each diagram as a traceable claim: SVG under a house palette, an acceptance run against its brief, a simplified view for slides |
| `agent-division-of-labor` | Assign one writing agent per file, route changes as proposal blocks, keep handoffs out of history, write the untracked `HANDOFF.md` |

## The three embedded skills

| Skill | Job |
|---|---|
| `blunt-critique` | Evidence-grounded critique ordered by damage, used to attack every draft before it is shown |
| `semantic-versioning` | Classifies every bump, and defines when the estimate's pin still holds |
| `stricter-ai-language-hygiene` | Sweeps every paragraph the skills write |

They are verbatim copies of their sources; `stricter-ai-language-hygiene` carries its own version, 1.1.0.

## Scripts

- `arc42-architecture-document/scripts/register_tools.py`: `scaffold` a new set, find the `next` free ID, list `cites` of an ID, `project` a register into client prose with a trace table.
- `architecture-set-audit/scripts/audit.py`: the coherence audit, configured per repository by `tools/audit-config.json`; `--derived` for a client-facing text dump, `--reissue` for what a revision changed.
- `diagram-assets/scripts/diagram_tools.py`: `brief` an asset from its register row, `check` an SVG against its brief and the house palette.

Both need Python 3.9 or later and nothing outside the standard library.

## Regression

```
python3 fixture/run_regression.py
```

The clean fixture must audit to zero FAIL; each of the thirteen mechanical defects in `fixture/defects.json` must be found, and nothing else; the diagram acceptance check must pass on the built asset and find each of three planted SVG defects; the reissue diff must list exactly the changed annex items. `fixture/defects.json` also lists five judgment defects for the review checklist and the hygiene sweep.

## Conventions the skills share

`references/shared-substrate.md` is identical in the seven workflow skills. Part A is the register grammar and the supersession list from the first engagement's forms; Part B the document conventions, including the pin rule; Part C the internal and client-facing prose registers; Part D platform notes; Part E the defect catalog; Part F fallback digests for the embedded skills.

## Relation to the other plugins

`architecture-continuity` holds `c4-diagram-package`, for Mermaid C4 packages documenting an estate, and `closure-extraction-handoff`, for knowledge packs. This plugin's `diagram-assets` builds the SVG assets registered inside an arc42 set, and applies the C4 conventions of `c4-diagram-package` when that plugin is installed. With both plugins installed, a request for an estate-wide Mermaid package goes to `c4-diagram-package`, and a request naming a registered asset or a diagram brief goes to `diagram-assets`.

## Install

```
claude plugin marketplace add <path-or-repository-containing-the-marketplace>
claude plugin install architecture-authoring@architecture-authoring-marketplace
```

The manifest layout follows Anthropic's public reference plugins. Skill frontmatter stays within the open Agent Skills fields: `name`, `description`, `compatibility`, `allowed-tools` where a skill ships scripts, and `metadata.version`.

## Maintenance

The plugin is at version 0.2.0 and follows its own semantic-versioning skill; `CHANGELOG.md` records each release. Its consumers are the people and prompts that depend on skill names, triggers, the register grammar, the audit's configuration keys and the template layout. Renaming a skill, changing a default series or a configuration key, or changing the set layout is MAJOR; adding a skill, a check or a series is MINOR; wording fixes are PATCH. After any change, run the regression. Edit `references/shared-substrate.md` once and copy it to the other six skills.
