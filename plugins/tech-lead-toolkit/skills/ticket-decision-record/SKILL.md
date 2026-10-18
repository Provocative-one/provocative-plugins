---
name: ticket-decision-record
description: Draft a paste-ready Jira comment that puts a decision on the record, in one of two modes. A Direction comment authorizes an agreed technical or architectural approach before build begins and states the reasoning that makes it defensible later. An Awareness comment transcribes an off-ticket exchange (a Teams thread, a meeting, a hallway alignment) onto the story it governs, with attribution and live links back to the source. Use whenever the user wants to record an agreed approach, settle a design question on a ticket, mirror a Teams or meeting decision into Jira, capture a stakeholder's position, or says "make this visible on the ticket", "write the direction comment", or "put this on the record", even when neither word direction nor awareness is used. Also use for the paired form, awareness on the parent ticket plus direction on the implementation story.
metadata:
  version: 0.1.0
---

# Ticket Decision Record

An unrecorded decision is a silent drop of its own reasoning. The authoritative record must contain the reasoning along with the result, so decisions made in chats, meetings, and corridors get written onto the ticket they bind. This skill covers the two acts that do it.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Where | Skill | Job here |
|---|---|---|
| Direction, design decision | blunt-critique | Tests the option analysis and the recommendation |
| Awareness, determination | blunt-critique | Keeps the position unsoftened and the determination plain |
| Delivery and scope, bearing | semantic-versioning | Classifies the change a decision makes to a versioned artifact |
| Final pass, both modes | stricter-ai-language-hygiene | Sweeps the author's prose, never the quoted words |

Operating protocol, naming rules, paste mechanics, and the Teams and GitLab retrieval patterns live in `references/shared-substrate.md`. Read Parts A to C at the start of a session.

## Choose the mode

| | Direction | Awareness |
|---|---|---|
| Act | Authorizes work about to be done | Brings an off-ticket exchange home |
| Contrast with a review | A review grades finished work. Direction settles the approach before build | Makes an exchange findable where the work happens |
| Source | The code and the ticket as they stand today | The retrieved thread or transcript |
| Lands on | The implementation story | The ticket the exchange bears on |

Awareness is the right mode when a stakeholder stated a position that changes how the story must be built, when a gate question was asked and answered off-ticket, or when a meeting reached a determination that is written nowhere durable. The word carries its own instruction (Old English *wær*, watchful): the comment exists so that no one working the ticket is unaware of a decision made elsewhere that binds their work.

**Pair them when the exchange authorizes a technical path.** Part 1 is an awareness comment on the discovery or parent ticket, capturing the stakeholder position where stakeholders read. Part 2 is the direction comment, with a sequence diagram when it helps, on the implementation story where engineers work. The pair keeps the discussion visible and the decision actionable.

## Direction mode

### 1. Ground the comment in the artifact

Read the current code, pipeline, or ticket. State the problem as the current artifact shows it. Verify every file name and line reference against the actual artifact before drafting, since a direction comment that cites the wrong line loses its authority.

### 2. Test the options (blunt-critique)

When the design question is open, present the alternatives, recommend one, and give the reasons. Apply the blunt-critique discipline to your own analysis:

- Each rejected option loses on a stated ground. If you would concede the point under pushback, the ground is not real, so find the real one or reconsider the recommendation.
- The recommendation names its **reversal condition**: the observation that would reopen the decision. A recommendation with no failure condition is a hedge, and it reads as a commitment while reserving the right to deny one.
- Check the Context section for definition by example: if the problem is described only through instances, state the mechanism.
- Worked example of the pattern: a team weighed modifying an existing smoke-test block in place against adding a discrete new block to a shared pipeline template. It chose additive-only on three grounds: the tests are orthogonal, the exit-code polarity of the existing check breaks under negative cases, and a shared template's blast radius favors additive diffs.

### 3. State the version consequence (semantic-versioning)

When the decision changes a versioned artifact (a shared template, a module, an interface, a published document), the Delivery and scope section names the increment the change will carry, with the classifier's one-sentence rationale. The additive-only example above would be a candidate MINOR, because existing consumers' behavior is untouched, but the classifier decides each case on its interface. When nothing versioned is touched, say nothing about versions.

### 4. Compose

Six sections separated by horizontal rules:

1. **Note header.** Bold metadata (ticket, sprint, parent) and a cross-reference list of the artifacts the decision touches. Live links.
2. **Context.** Where the problem stands now.
3. **Approach.** The agreed path, stated affirmatively.
4. **Change surface.** Exactly what changes and where.
5. **Design decision.** The one question settled, the option chosen, the alternatives and why they lost, and the reversal condition.
6. **Delivery and scope.** In, out, sequencing, and the version consequence where it applies. Keep it lean. Story-point reconciliation belongs on the parent thread (Part A).

If the decision constrains other work or will outlive the ticket, it also belongs in the relevant ADR. The comment is the authoritative record until that artifact exists, and it does not replace it.

## Awareness mode

### 1. Retrieve the actual source

Pull the Teams thread or the meeting transcript and read the substantive messages in full. Never paraphrase from a description of the exchange, because the value of the comment is fidelity: it stands in for the source. Confirm the target ticket's current framing so the comment lands on the story as it reads today. Retrieval patterns are in Part C.

### 2. Transcribe with attribution

Name, role, date, and `[HH:MM:SS]` where it sharpens the record, on their own line above the excerpt. Quote verbatim where the exact wording matters and summarize faithfully where it does not. Do not tidy, soften, or reorder a stakeholder's position (blunt-critique): the record is worth what its fidelity is worth.

### 3. State the determination

What was decided or asserted, in plain statements. When the exchange settled nothing, write "No determination reached" and name what remains open. When positions conflict, name both and the governing constraint. Do not manufacture a single path the evidence does not support.

### 4. State what it forecloses or enables

Which path is now closed, which is endorsed, what dependency this creates for the story. When the determination amends a versioned artifact (an ADR, a template, a published interface), classify the amendment with the semantic-versioning skill and state the increment in one line.

## Hygiene pass (stricter-ai-language-hygiene)

Sweep the author's prose: the framing line, the determination, the bearing, and every Direction section. **Never alter a quoted excerpt.** A verbatim quote is someone else's wording, and fidelity outranks style. Section labels such as "Direction — <summary>" are structural labels, and the em-dash in them is sanctioned. Write the draft to a scratch file, run the mechanical sweep, judge every hit, and run the counting check (for example, "three options" above a list of three).

## Present

Show the comment in chat or as a file. Do not post. Posting waits for an explicit instruction. When the user pastes the published text back for calibration, follow the calibration steps in Part A.

## Skeletons

Both skeletons are in `references/skeleton.md`.
