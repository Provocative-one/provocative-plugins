---
name: closure-extraction-handoff
description: Preserve knowledge so it survives the people who hold it, in two modes. Extract mode turns a living source set (Confluence pages, Notion exports, design documents, ADRs) into a durable knowledge pack with one subject per file, recorded sources and currency, flagged supersessions, a stated authority, a README index, and an audit script. Handoff mode builds a self-sufficient resume package from an in-progress conversation or engagement, so a fresh Claude instance or a successor can continue with no dependency on memory, prior turns, or connector access. Use whenever the user mentions an engagement closing, rolling off, leaving a team, knowledge transfer, handoff, closure documentation, archiving or extracting pages, "export this so I can continue elsewhere", "summarize everything so a new session can pick up", or making a body of work survive after its authors depart.
metadata:
  version: "0.1.1"
---

# Closure Extraction and Handoff

When the last author leaves, the written record is the only surviving input. Accuracy matters more under those conditions, because nobody remains to correct a statement that was close enough while the team was present. Extract mode compresses a living source into a durable reading. Handoff mode packages live work so the next reader can continue it.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Where | Skill | Job here |
|---|---|---|
| Extract step 9, Handoff step 6 | blunt-critique | Audits fidelity in a pack and runs the cold-reader attack on a handoff |
| Both modes, final pass | semantic-versioning | Versions the pack or the handoff and classifies each refresh |
| Both modes, final pass | stricter-ai-language-hygiene | Sweeps the author's prose, never the verbatim material |

## Choose the mode

| | Extract | Handoff |
|---|---|---|
| Input | Living sources: pages, documents, ADRs | An in-progress conversation or body of work with open threads |
| Output | A folder of subject files plus a README | One self-sufficient Markdown file plus an asset manifest |
| Reader | A successor team, an auditor, a future model | A fresh Claude instance or a colleague |
| Test | Each file is usable with its source closed, and a reader can tell what superseded what | A reader with nothing else can state the task, the current state, the standards, and the next move |

A closing engagement often needs both. Extract the stable sources into a pack, then write a handoff for the live threads. Part 2 of the handoff can point to the pack and skip reproducing it.

## Before either mode

1. **Check data handling.** Confirm the sources may be processed here. When an access-rules policy or skill covers the source system (client agreements, restricted spaces), follow it first and keep restricted material out of the outputs.
2. **Keep secrets out.** Tokens, keys, and passwords never enter a package. Name where they live.
3. Read Parts A to C of `references/shared-substrate.md`. Part C covers fetching Confluence pages by numeric ID and the GitLab and Teams retrieval quirks.

## Extract mode

### 1. Inventory and decide the subjects

List the sources with identifier, title, version or last-edited date, status, and parent. Merge pages that are one discovery at two levels of detail. Keep pages apart when each carries a decision someone could cite on its own. Give each subject a prefix code and a file name, `CODE-subject.md`, with codes grouped by theme.

### 2. Read every source completely and compress faithfully

Keep decisions, constraints, thresholds, exact figures, identifiers, and the reasoning behind each. The reader must be able to use the file with the source closed. Add nothing the source does not support. Where provenance is missing, say so in the file. Where the source contradicts itself or a sibling, record both passages.

### 3. Mark currency

Open each file with a Source line (system, identifier, space, version, status, date). Where a later artifact supersedes an earlier one, say which governs and on what, in an Extraction note at the foot of the file. Never reconcile silently. The five kinds of note are in `references/pack-layout.md`.

### 4. Normalize

Names in Given Surname form. No `@` prefixes. No platform chip forms. Absolute dates. Live links only. Apply the project's fixed spellings in your own prose and leave quotes untouched.

### 5. Carry corrections forward

When the pack supersedes an earlier instruction document, list each divergence in the README and treat the later, corrected state as canonical. Write "No open discrepancies" only when that is true.

### 6. Record dispositions and gaps for work in flight

Add an open-gaps register to the README. Each item names its owner, what remains, and where the banked artifact lives. Terminal states say what happened. Done asserts the criteria were met. Work that was descoped, reverted, or blocked by an external dependency is recorded as such, with the owner it reverts to. A false Done is a false claim to everyone who reads it after the authors are gone. The full rule is in `references/pack-layout.md`.

### 7. Write the README

Use the skeleton in `references/pack-layout.md`: how to read, the subjects by theme, provenance and fidelity, corrections, open gaps.

### 8. Run the audit

```bash
python3 scripts/audit_pack.py <pack_dir>
```

FAIL items are defects: a cross-reference that points nowhere, an `@`-mention, a placeholder link, a duplicated code. WARN items need judgment: files missing from the README, files without a Source line, relative dates, a README count that disagrees with the folder. Fix the pack and re-run.

### 9. Audit fidelity (blunt-critique)

The script checks structure and this step checks truth. Read each file against its source and trace a sample of figures, thresholds, and names. Use these blunt-critique moves:

- **Internal contradiction.** Two files that state a threshold or an owner differently. Quote both passages side by side.
- **Silent reconciliation.** A file that harmonizes two sources with no Extraction note.
- **Unsupported statement.** Anything the source does not say.
- **Stale currency.** A note that claims a supersession the source does not show.
- **Definition by example list.** A glossary entry that lists instances and never states the term's boundary.
- **Excisability.** Narrative no reader needs. Compression means cutting.

Rank by damage. A wrong threshold outranks a clumsy sentence. A contradiction between sources is a finding of the pack and is recorded as a documented contradiction, never smoothed. When a full pass finds nothing real, say the pack has converged and name what was checked.

### 10. Version, sweep, present

**Version (semantic-versioning).** The subject is the pack. The consumers are the successor team, auditors, and any model that cites the pack as the record. The interface is the decisions, thresholds, owners, and coordinates it records, plus the prefix-code scheme that cross-references depend on. These are default readings. The classifier decides each case.

| Change | Increment |
|---|---|
| A refresh reverses a recorded decision, owner, or coordinate readers acted on; a prefix code is renamed or removed | MAJOR |
| A subject file or section is added; an open gap is closed with new content | MINOR |
| A transcription fix, a link repair, a wording fix | PATCH |

The first pack is 0.1.0. The README states the version and the compile date.

**Hygiene (stricter-ai-language-hygiene).** Sweep the compression prose, the Extraction notes, and the README at the deep register. Leave untouched: verbatim quotes, identifiers, figures, threshold tables, code, and the typography of terms the source itself defines. Run the mechanical sweep and the counting check.

**Present.** Write the pack to `/mnt/user-data/outputs/<pack>/`, then share the README and a zip of the folder with `present_files`. Do not post it anywhere without an explicit instruction (Part A).

## Handoff mode

### 1. Define the resume target

State what task continues, for whom (a fresh Claude instance on any surface, or a colleague), and what the reader will have. Assume nothing beyond the file.

### 2. Assemble the file

Follow `references/handoff-skeleton.md`: Part 0 instructions for the receiving Claude, Part 1 who they work with, Part 2 the source material verbatim, Part 3 the asset manifest, Part 4 the consolidated state, Part 5 the open threads, Part 6 the glossary and anchors. Part 1 holds only what the task needs and what the user has approved. Part 2 discloses every edit.

### 3. Consolidate the state, and do not narrate

Part 4 says where the work stands: what is settled, what changed and why, what remains contested. Include a table of concerns retired or revised, with the evidence that retired each, so a successor does not reopen them. Record your own earlier judgments that a later, more careful treatment overturned, with the same bluntness you apply to the work.

### 4. Order the open threads

Prioritize them. Give each a closure condition and a status. When none has been executed, say so.

### 5. Version the handoff (semantic-versioning)

The consumer is the receiving instance or colleague. The interface is the task statement, the settled state, the open threads, and the standards they resume from. A re-export that adds rounds and threads is MINOR. A re-export that reverses a conclusion in Part 4 or reorders the threads so that a resumer following the earlier version would act wrongly is MAJOR. A typo or link fix is PATCH. The first export is 0.1.0. Put the version, the export date, and the version it supersedes in the header.

### 6. Attack the file as a cold reader (blunt-critique)

Read the file as an instance with nothing else. Find what a cold reader would get wrong:

- Terms used before they are defined, or defined only by example.
- Referents that need the conversation ("the script", "that document").
- A finding marked resolved with no evidence.
- An open thread with no closure condition.
- A contradiction between Part 4 and Part 5.
- Anything in Part 2 that is not verbatim.

Fix what survives. When a full pass finds nothing real, say the file has converged and name what was checked.

### 7. Sweep and present (stricter-ai-language-hygiene)

Part 2 is verbatim and exempt. Part 0 is addressed to a model, so keep it precise and sweep it lightly. Parts 1, 4, 5, and 6 get the full sweep and the counting check. Share the file with `present_files`. Do not post it anywhere without an explicit instruction.

## Resources

- `references/pack-layout.md`: pack folder, file skeleton, compression rules, the five Extraction notes, the README skeleton, the open-gaps register and terminal states.
- `references/handoff-skeleton.md`: the seven-part handoff skeleton and the rules for filling it.
- `scripts/audit_pack.py`: mechanical audit for a knowledge pack.
