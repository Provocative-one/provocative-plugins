---
name: client-facing-derivations
description: Produce what a client reads from an internal arc42 document set without retyping it or leaking excluded content. Generates the offer traceability annex by origin class, the assumptions and exclusions annex projected from the registers, the milestone plan with acceptance evidence, decks and one-pagers, and clarification-round answers anchored to register rows with an owner flag on every commitment and a reissue list. Every derivative names the document versions it was generated from, has a brief recording what was built and on what basis, and is published as a new versioned file, never edited after sending. Use whenever the user asks for a deck, annex, appendix, traceability map, assumptions and exclusions list, milestone plan for the client, a client-facing version of the architecture, a plain version for the client, answers to clarification questions, or "what did we actually say in the proposal about".
compatibility: Uses register_tools.py and audit.py from sibling skills when the plugin is installed. Word output goes through the docx skill; slides through the pptx skill or a slide artifact type.
metadata:
  version: "0.2.1"
---

# Client-facing Derivations

A derivative restates the living documents for an audience. It is generated and never maintained: when the documents move, the derivative is rebuilt from them, and the copy the client has already seen stays exactly as sent. A derivative carries no claim its sources do not hold, and it may say less than they do, provided its brief records where.

## Embedded skills

| Step | Skill | Job here |
|---|---|---|
| 3 | stricter-ai-language-hygiene | Sweeps the client prose, at its strictest register |
| 5 | blunt-critique | Reads the derivative as the client's most skeptical reviewer |
| 6 | semantic-versioning | Versions the published file and its brief |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F. Part C of that file sets the two prose registers, the no-invention rule, the writing-against-a-call distinction and owner routing.

## Workflow

### 1. Fix the sources and the audience

Name the architecture and estimate versions you are generating from. Read each document's Audience row: only candidate sections feed a client-facing derivative, and excluded sections never reach it under any framing.

### 2. Generate, never retype

Build each element from its source. For a register projection:

```bash
python3 ../arc42-architecture-document/scripts/register_tools.py project --root <repo> --series EA --trace
```

The projection is a draft: identifiers stripped, terminal rows left out, one sentence per row, plus the trace table the brief needs. Rewrite it into the client's register and vocabulary, anchored to the client's own section numbers. When a response template arrives with its own pre-drafted assumptions section, the generated one replaces it; the two are never merged.

**When the derivative needs a fact the documents lack,** the fact enters the owning document first (a section or an `[A-nn]` row), and the derivative is regenerated. When the fact contradicts a recorded decision, follow the reversal in `sibling-estimate-document`.

**When a passage cannot trace,** write a visible placeholder naming the owner and the missing source: `[Owner: commercial lead. Source missing: payment terms]`. A placeholder blocks sending.

### 3. Write in the client register (stricter-ai-language-hygiene)

Plain and advisory, the client's vocabulary, the client's section numbers, no register reference, asset ID or marker. Run the hygiene sweep at its strictest register.

### 4. Route commitments

Every commitment that binds price, a service level figure, scope, staffing or a date carries its owner, from the README's owner table, until that owner approves it. Anything still negotiable goes on a call list for the conversation, never in the letter.

### 5. Verify before sending (blunt-critique)

Dump the derivative's text and run:

```bash
python3 ../architecture-set-audit/scripts/audit.py --root <repo> --derived <text-dump.txt>
```

Zero FAIL means no internal identifier, placeholder, draft marker or excluded term reached the page. Then read it as the client's most skeptical reviewer: every number traceable, every promise owned, no paraphrase of an excluded section (the checklist item the script cannot catch).

### 6. Write the brief, publish, version

Write `briefs/<artifact>.md` from `references/derivation-templates.md`: request, decisions with attribution and date, derivations shown in full, the traceability table, the content transcribed so it reads without the originating application, how it was built and verified, divergences from the sources, open points, the regeneration rule. The brief pins the source versions.

A derivative that reaches a client lands in `published/` with its version in the filename and its properties, never on a client-facing page. A change after sending, even one word, is a new file and a new brief version. Work in progress stays in `generated/`.

## The artifacts

| Artifact | Built from | Template |
|---|---|---|
| Offer traceability annex | Every costed element, tagged by origin class | `references/derivation-templates.md` §1 |
| Assumptions and exclusions annex | `[A-nn]` and `[EA-nn]` projections, grouped by theme | §2 |
| Milestone plan | `[M-nn]`, exit criteria, client actions in estimate §3.2 | §3 |
| Clarification response | Register rows each answer touches, plus the reissue list | §4 |
| Deck or one-pager | Candidate sections only | the brief template, with the `pptx` skill or a slide artifact |

**Origin classes** for the traceability annex: `[R]` set by the client's request, `[N]` needed to make the solution work, `[E]` proposed by us, `[U]` decided with the client at discovery. The class letters appear only on the internal map; the client-facing annex groups by class in plain words. State the approximate share of effort per class once, never as price lines. `[N]` replaced an earlier `[I]`, which collided with the inference marker.

## What this skill leaves to its siblings

Changing the facts is the authoring skills' job. Reconciling a client letter against the registers and producing the reissue list is `architecture-set-audit`. Word and slide mechanics are the `docx` and `pptx` skills. A diagram on a slide is a simplified view built and accepted with `diagram-assets`.

## Resources

- `references/derivation-templates.md`: the brief, the four artifact templates, the pre-send checklist.
- `references/shared-substrate.md`: Part C (prose registers, routing), Part E (defects 7, 8, 11 and 14 came from derivatives).
- `../../fixture/heritage-hub/briefs/heritage-hub-milestone-plan.md` and its published file: a brief recording a reduced-form exit criterion.
