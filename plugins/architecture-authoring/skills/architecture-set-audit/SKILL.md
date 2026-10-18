---
name: architecture-set-audit
description: Audit an arc42 document set (architecture, estimate, README, conventions file, changelog) for coherence before a version is cut, and reconcile anything that claims to derive from it. A script checks register closure, dangling and misplaced references, the one-way dependency, unbracketed or one-digit identifiers, retired prefixes, section references that resolve to nothing, counting claims against their lists, version pointers, the estimate's pin, client vocabulary, and internal identifiers leaking into client-facing text; a judgment checklist covers what a script cannot see. Also emits a reissue list when a clarification or revision changed numbered items. Use whenever the user asks to audit or check the set, run the coherence or conventions check, do a pre-freeze sweep, check the counts or references, ask whether a proposal, deck or letter matches the architecture, or ask what a reissue has to carry.
compatibility: Python 3.9 or later, standard library only. Reads tools/audit-config.json at the repository root.
allowed-tools: Bash(python3:*) Read Glob Grep
metadata:
  version: 0.2.0
---

# Architecture Set Audit

The audit is the regression test for everything the other skills assert. The mechanical half is a script that gates a version: zero FAIL or no release. The judgment half is a checklist for what no regular expression can see.

## Embedded skills

| Step | Skill | Job here |
|---|---|---|
| 3 | blunt-critique | Runs the judgment checklist, ordered by damage |
| 4 | stricter-ai-language-hygiene | Its mechanical sweep is the prose check; the script does not duplicate it |
| 5 | semantic-versioning | Decides whether a finding's fix is PATCH, MINOR or MAJOR |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F. Part E of that file is the defect catalog the checks were built against.

## Workflow

### 1. Configure

The script reads `tools/audit-config.json`. The scaffold in `arc42-architecture-document` writes one; `references/config.md` documents every key. Keep the `documents` list complete: the allowlist check fails on any living document the configuration omits, because the original audit's allowlist left out one of the two living documents for its entire life.

### 2. Run the mechanical audit

```bash
python3 scripts/audit.py --root <repo>
python3 scripts/audit.py --root <repo> --derived <client-facing-text.txt>   # plus a client-facing dump
python3 scripts/audit.py --reissue <old.txt> <new.txt>                      # what a revision changed
```

Extract text first from a PDF, DOCX or PPTX before passing it with `--derived` (substrate Part D).

| Check | Fails when |
|---|---|
| allowlist | A Markdown file under the living directory is missing from the configuration |
| anchors | A link to `document.md#anchor` resolves to no heading |
| sections | A role-qualified or bare `§n` resolves to no heading in the document it names |
| registers | A row is defined twice or in the wrong document; a reference has no row; a plan-side row is never cited and its status is not terminal |
| direction | The architecture cites a series the estimate owns |
| markers | A document uses a series its notation key or preamble does not declare |
| residue | Unbracketed or one-digit tokens, retired prefixes, the template name used as a document name, placeholders, inverted date ranges |
| counts | A notation-key count differs from its register, or a claim heads a list or table of another length |
| versions | Title and front matter disagree; a README pointer or the latest changelog heading differs from the document; the pin is not semantically satisfied |
| assets | An asset row marked Built lacks its SVG or brief, an SVG has no row, or an asset ID is cited without a row |
| rogue | Another engagement's identifiers, or a forbidden synonym for the client's vocabulary |
| derived | A client-facing dump carries a register reference, marker, asset ID, placeholder, or excluded term |

WARN findings (relative dates, a table cell that may be cut off, a "§n" outside a living document with no role, an unfilled template slot, a table-heading count whose noun is not in the header) are candidates for judgment. The INFO line on a lagging but valid pin measures staleness and needs no fix.

### 3. Run the judgment checklist (blunt-critique)

Work through `references/judgment-checklist.md`. Order findings by damage, quote the evidence with file and line, and report "converged" only when both halves are clean.

### 4. Sweep the prose

Run the `stricter-ai-language-hygiene` mechanical sweep on the living documents. The script deliberately leaves prose to it.

### 5. Report

Lead with FAILs, then judgment findings, then WARNs. For each fix, name the bump it implies (semantic-versioning) and what else must move in the same commit: the README pointer, the changelog entry, the pin. Do not apply fixes or commit without an explicit instruction.

## Reconciliation mode

When a client's questions, a clarification letter or a revised proposal claims to derive from the set:

1. Map each question or answer to the register rows and sections it touches (`register_tools.py cites` finds every citation of a row).
2. Name the rows each answer changes, and whether the change is a new row, a closed entry, or a superseded decision.
3. Produce the reissue list with `--reissue` against the previous and revised texts: every changed, added or removed numbered item, plus the other passages that changed. A clarification that changes five annex items and two body passages ships with that list.
4. Hand the client-facing wording to `client-facing-derivations`.

## Regression

The plugin's fixture is the suite. From the plugin root:

```bash
python3 fixture/run_regression.py
```

It audits the clean fixture (zero FAIL expected), plants the thirteen mechanical defects from `fixture/defects.json` (each must be found, and nothing else), runs the diagram acceptance check on a built asset and on three planted SVG defects, and checks the reissue diff. Run it after every change to the script or the conventions.

## What this skill leaves to its siblings

Fixing the content is the authoring skills' job: `arc42-architecture-document`, `sibling-estimate-document`, `client-facing-derivations`. Accepting a single diagram against its brief is `diagram-assets`. Marker decisions are `evidence-and-registers`.

## Resources

- `scripts/audit.py`: the audit, generalized from one that gated a production document set.
- `references/config.md`: every configuration key.
- `references/judgment-checklist.md`: the checks a script cannot make.
- `references/shared-substrate.md`: grammar, conventions, defect catalog, fallbacks.
