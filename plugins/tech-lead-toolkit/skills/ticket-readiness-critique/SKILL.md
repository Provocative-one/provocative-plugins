---
name: ticket-readiness-critique
description: Critique a Jira ticket's readiness to enter a sprint or close, judging the ticket as an instrument (its story, scope, acceptance criteria, links, and metadata). Produces a structured critique (What Works, Must-haves, Nice-to-haves, Entry Blockers) where metadata that misrepresents the ticket, such as an inverted priority, a status contradicting the MR, or an unmodeled dependency, is flagged as a Must-have and never as a footnote. Use whenever the user asks to critique, check, review, groom, or sanity-check a ticket or story, asks "is this ready for the sprint", "can an engineer pick this up", or "check it" or "again" on a ticket critiqued before, or hands over a ticket link or export for feedback.
metadata:
  version: 0.1.0
---

# Ticket Readiness Critique

A ticket works as a unit of delivery when an engineer can pick it up and know when they are done, and when its metadata tells the truth about its place in the program. Priority, status, assignee, epic link, sprint, and links are how a ticket represents itself to everyone who never opens it. When they are wrong, they actively mislead, so a metadata misalignment is a first-class defect.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Step | Skill | Job here |
|---|---|---|
| 2 and 4 | blunt-critique | Runs the critique method and governs revision rounds |
| 3 | semantic-versioning | Checks that a ticket delivering a versioned artifact declares the right increment |
| 6 | stricter-ai-language-hygiene | Sweeps the critique's prose |

This skill is the natural home of blunt-critique among the five ticket skills, so the full skill applies, including its revision-round rules. Operating protocol, naming rules, Atlassian field quirks, and paste mechanics live in `references/shared-substrate.md`. Read Parts A to C at the start of a session.

## Workflow

### 1. Read the whole ticket and what it answers to

Pull the ticket with every field requested explicitly (Part C): summary, description, status, issue type, priority, assignee, reporter, parent, subtasks, issue links, comments, sprint, epic link, story points. Then pull what the ticket answers to when it is in reach: the planning session that ranked it, the decision or direction comment that scoped it, the MR that implements it and that MR's review state, and the parent's ACs. A ticket does not stand alone. Its priority answers to a ranking set elsewhere, and its scope answers to a decision recorded elsewhere. The critique that cites the governing record is the one that holds.

### 2. Critique bluntly (blunt-critique)

Run the blunt-critique method. Its recurring high-value moves map onto tickets as follows:

| blunt-critique move | What it finds in a ticket |
|---|---|
| Internal contradiction | Title and content describe different work; priority contradicts the program ranking; status contradicts the MR |
| Definition by example list | ACs that list sample behaviors without stating the criterion or its boundary |
| Unfalsifiable claims | An AC with no observable condition, such as "works correctly" or "is secure" |
| Excisability | A scope item no AC references, or an AC with no scope behind it |
| Missing prior art | The governing ADR, decision comment, or earlier ticket the story ignores |
| Audience drift | A ticket written as a design essay that an engineer cannot execute |
| Category error | A "Done" that mixes an artifact delivered with an outcome proven |

Order findings by damage. Quote the ticket text as evidence. Grade each finding with the three-tier legend below.

When the ticket is clean, say it is ready: "No entry blockers", with what was checked.

### 3. Check version declarations (semantic-versioning)

When the ticket's deliverable is a versioned artifact (a module, a template, a published interface, a versioned document), check whether the ACs or fix-version state the increment and whether it matches the work described.

1. Name the subject, its consumer, and the interface the consumer relies on.
2. Classify the described change as the classifier prescribes. A new subject's first version is 0.1.0.
3. Grade: no declared increment on an artifact consumers pin, or a declared increment that contradicts the described change, is a **Must-have** (the ticket cannot be reviewed or closed against a version bar it does not state). On an artifact nobody pins, it is a **Nice-to-have**.
4. In the finding, give the one-sentence rationale naming the interface expectation preserved or broken. When the work is too thinly described to classify, say that, and make "state the interface and the increment" the fix.

### 4. Run the metadata checks

These are defects seen in practice, and all of them are Must-haves:

- Priority contradicting the program's stated ranking. A top-ranked item marked Low is an error, not a style opinion, and it must be corrected before the ticket enters any sprint.
- Acceptance criteria absent, so the ticket cannot be reviewed or closed without a Definition of Done.
- A hard external dependency mentioned in prose but not modeled as a *blocks* or *is blocked by* link, which leaves it invisible in the ticket graph.
- A named deliverable from an action item (a dual-view analysis, say) missing from the ticket's scope.
- A status contradicting the actual state of the work or the MR, such as Done while a reviewer has requested changes.
- A title that no longer matches the content. Flag the rename before critiquing the body, so the description and the title tell the same story.
- A deliverable that declares it supersedes the ticket's own ACs. The ACs govern unless a formal Scope Amendment is posted and acknowledged.

### 5. Render the critique

```
### ✅ What Works
### ❌ Must-haves
### ⚠️ Nice-to-haves
#### Gherkin Scenarios   (optional)
### 🔒 Entry Blockers
```

Section order follows the house format. The content rules of blunt-critique govern what goes inside:

- **What Works** lists specific, evidenced strengths: sound architectural content, clear scoping, correct linkage. Ceremonial praise is deleted.
- **Must-haves** hold the metadata misalignments and every defect that stops the ticket from being worked or closed. Numbered, with the prose and the fix nested inside each item (Part C, ADF nesting).
- **Nice-to-haves** hold improvements that do not block entry.
- **Gherkin Scenarios** appear when the ticket's ACs are missing or untestable and the user wants replacements. Draft them with the story-and-gherkin-drafting skill.
- **Entry Blockers** is a table (`| # | Blocker |`) where every row traces to a Must-have, for example "Priority must be corrected to Highest before this enters any sprint."

**Legend note.** This format used to carry a "Should-have" tier. The three-tier legend of the review comment replaced it (Must-have, Nice-to-have, Out of scope) because "Should-have" was read as optional-but-expected and blurred the line between blocking and advisory. Use the three tiers here. To reconcile an older critique: Should-have and Could-have become Nice-to-have.

### 6. Hygiene pass (stricter-ai-language-hygiene)

Treat the critique as a deep-register working document. Sweep its prose, leaving quoted ticket text, field values, and identifiers untouched. Write the draft to a scratch file, run the mechanical sweep, judge every hit, and run the counting check: Entry Blockers rows against Must-haves, and every count in the prose against its list.

### 7. Present, then handle revision rounds

Show the critique. Do not post it. When the author revises the ticket and asks again, follow blunt-critique's revision rules:

- Diff the new ticket against the version you critiqued.
- Verify each earlier Must-have at the field or sentence where it was raised, then inspect the neighborhood for new damage. A repaired priority can expose a stale sprint assignment beside it.
- Do not re-litigate settled points.
- Escalate altitude as local issues exhaust: field-level, then scope, then purpose and audience.
- When a full fresh pass finds nothing real, end the loop explicitly: state the pass was done, each fix was checked, and the ticket has converged.

## Skeleton

The paste-ready skeleton is in `references/skeleton.md`.
