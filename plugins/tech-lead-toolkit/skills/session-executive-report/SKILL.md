---
name: session-executive-report
description: Convert a meeting recording, VTT file, Teams transcript, or set of raw notes into a durable Markdown executive report that a non-attendee can read and act on. The report carries a prose executive summary, a participants table, numbered topics with blockers and resolution paths, sparse verbatim timestamped quotes, an action-items table with named owners, and live-link references. Use whenever the user supplies a transcript, VTT, recording link, or meeting notes and wants minutes, a session report, executive notes, a decision record of a meeting, or says "write up this call", even without the words executive report. Also use to revise or reissue an earlier session report.
metadata:
  version: "0.1.1"
---

# Session Executive Report

A session report is synthesis. It converts a meeting into a record of decisions, forward state, and open governance questions, and it is only as sound as the reading beneath it. It enumerates nothing that can be integrated into prose and quotes only where the exact words carry weight the paraphrase would lose.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Step | Skill | Job here |
|---|---|---|
| 3 | blunt-critique | Keeps blockers, open items, and non-decisions unsoftened |
| 4 | semantic-versioning | Versions a report that is revised or reissued |
| 6 | stricter-ai-language-hygiene | Sweeps the author's prose, never the quotes |

Naming rules, retrieval patterns for transcripts and recordings, and the draft-first protocol live in `references/shared-substrate.md`. Read Parts A to C at the start of a session.

## Workflow

### 1. Read everything before composing

Read the whole transcript. For long VTT files, read in ranges until coverage is complete. Disambiguate speakers before attributing anything: automatic speaker labels mislead, so settle each speaker from content and the participant list. Record anyone invited who did not speak or was not transcribed ("invited; not transcribed"). Convert relative dates in the discussion to absolute ones.

### 2. Synthesize

Decide what the session decided, what work follows and in what order, and what remains unresolved. These three answers become the three paragraphs of the Executive Summary. If the summary needs bullets, it has not been synthesized yet.

### 3. Apply the blunt pass (blunt-critique)

The report is a record, so accuracy outranks diplomacy.

- State a blocker as a blocker, with its owner and what it blocks.
- State an open item as open. Do not smooth it into "alignment was reached" unless the transcript shows the alignment.
- If the session decided nothing, say so in the first paragraph of the summary.
- Where participants disagreed, record both positions and the governing constraint. Collapsing a live disagreement misrepresents the program.
- Attribute only what the transcript supports. A commitment nobody made does not get an owner.
- Action items are not padded: one row per real commitment, no placeholder rows, no false balance.

The chat reply can carry sharper analysis of the session than the report does (Part A, analysis register). The report states facts.

### 4. Version when it is revised (semantic-versioning)

A first issue needs no version unless the user's repository versions its artifacts. When the user versions artifacts, or asks for a revision of an issued report, classify the change:

- **Consumer:** people who acted on the report. **Interface:** the decisions, owners, and dates it records.
- Correcting a misspelled name, a typo, or a mis-timed timestamp: PATCH.
- Adding a topic the first issue omitted without altering what it recorded: MINOR.
- Reversing a recorded decision, owner, or date that people have already acted on: MAJOR.
- A first tracked state is 0.1.0.

Add a `Version` line to the header only when a version is assigned, and record the one-sentence rationale in a revision note under the header.

### 5. Compose and save

Write the report as a Markdown file in `/mnt/user-data/outputs/` and share it with `present_files`. Use the structure in `references/skeleton.md`:

- **Header block:** title, date and time in UTC (a local-time gloss such as "10:30–11:07 AM PT" is a courtesy and does not replace it), duration, format, prepared by.
- **Executive Summary:** two to three paragraphs of prose, no bullets.
- **Participants table:** Name, Organization, Role or Track.
- **Topics:** numbered and titled. Each can carry Background, Blocker Identified (if any), Resolution Path, Open Items, and verbatim quotes.
- **Action Items table:** `# | Action | Owner | Notes`.
- **References table:** live links only.

Conventions that make the report trustworthy:

- **Quotes are verbatim**, cleaned only for transcription artifacts (dropped filler, obvious mis-transcriptions) and always attributed: speaker name, role tag, `[HH:MM:SS]`, with the attribution on its own line. Quote sparingly. A line earns its place when the speaker's exact framing is itself the fact, such as a directive, a commitment, or a named threshold.
- **Timestamps deep-link** to the recording where possible: the full recording URL anchored with `&t=<seconds>`.
- **Dates are absolute.** The header carries UTC.
- **Names render Given Surname.**
- **References are live links only.** A stale or inaccessible citation does not stand as authority.

### 6. Hygiene pass (stricter-ai-language-hygiene)

Treat the report as an attachable working document: sweep the body prose in full. **Do not alter a verbatim quote** beyond the transcription cleanup above. Skip table placeholder cells. Run the mechanical sweep on the saved file, judge every hit, then run the counting check, which matters here: a summary that says "three decisions" must be followed by three, and the action-item count must match what the topics committed to.

### 7. Present

Share the file. Do not post it anywhere. Posting waits for an explicit instruction.

## Skeleton

The paste-ready skeleton is in `references/skeleton.md`.
