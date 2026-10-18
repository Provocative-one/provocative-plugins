---
name: story-and-gherkin-drafting
description: Draft a paste-ready Jira story, or a ranked backlog of stories, that an engineer can execute without reconstructing context, together with its acceptance criteria written as Gherkin scenarios covering both the success path and the failure path. Use whenever the user asks to write, draft, rewrite, or split a story, ticket, backlog, or epic breakdown, asks for acceptance criteria or Given/When/Then scenarios, wants a Definition of Done stated as observable behavior, or asks to turn a discussion, ADR, or review finding into stories, even without naming Gherkin. For critiquing an existing ticket instead of drafting one, use ticket-readiness-critique.
metadata:
  version: "0.1.1"
---

# Story and Gherkin Drafting

A story is self-contained enough that its assignee does not need several documents open to understand what Done means. A story and its acceptance criteria are one deliverable: the scope promises what the criteria later verify, and the criteria are written so a reviewer or a pipeline can check them.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Step | Skill | Job here |
|---|---|---|
| 4 | blunt-critique | Attacks the draft's own ACs before the user sees them |
| 5 | semantic-versioning | Adds version criteria when the story ships a versioned artifact |
| 7 | stricter-ai-language-hygiene | Sweeps the prose around the Gherkin |

Operating protocol, naming rules, and paste mechanics live in `references/shared-substrate.md`. Read Parts A to C at the start of a session.

## Workflow

### 1. Gather the source

Read what the story comes from: the discussion, ADR, review finding, or parent ticket. Pull the live links the assignee will need. When the story descends from a decision made off-ticket, check whether an awareness comment exists (ticket-decision-record), since the story should point at it.

### 2. Rank the backlog first, when there are several stories

Lead with a priority-stack table before any story body:

| Rank | Item |
|---|---|
| 1 | <highest> |

When stakeholders disagree on priority, surface both positions and name the governing constraint. A backlog that hides a live disagreement misrepresents the program's state, and one that names it lets leadership decide on the record. Do not collapse to a single view.

### 3. Draft the story

Use the structure in `references/skeleton.md`: Description (role, capability, outcome), Scope, Context, Acceptance Criteria with Gherkin Scenarios, Dependencies, References.

- **Scope mirrors the review legend.** The same Must-have, Nice-to-have, and Out of scope vocabulary governs what the story promises and how its output is later reviewed. Mark each scope item with its tier.
- **Acceptance criteria are single-criterion.** One observable condition per numbered item. A potential Must-have issue is itself an AC, so meeting the criteria and clearing the risk are the same act.
- **Context is complete.** Live links only, and enough that the assignee does not hold several documents open at once.
- **Dependencies are issue links** where the dependency exists in the ticket graph. Prose alone leaves it invisible.
- **Flag a misnamed story before drafting its body.** When the title no longer matches the content, propose the rename first. The title and the description must tell the same story.
- **Leave authorship with the colleague** when one is meant to write the deliverable. Provide an outline skeleton and stop there (Part A).

### 4. Attack your own draft (blunt-critique)

Before presenting, run these blunt-critique moves against the ACs and scope you wrote. Fix what survives the attack and drop what does not.

- **Falsifiability.** For each AC, name the observation that would show it failed. An AC with no such observation ("works correctly", "is secure") is rewritten as behavior or deleted.
- **Definition by example list.** An AC that enumerates sample cases without stating the criterion is replaced by the criterion plus the boundary test.
- **Excisability.** Every Scope item maps to at least one AC or is marked Out of scope. An AC that no Scope item motivates is cut.
- **Internal contradiction.** The title, the role statement, and the ACs describe the same work.
- **Audience drift.** The story reads as work to execute.
- **Negative coverage.** Every guardrail, gate, or policy has a scenario in which it refuses. A control never shown to refuse has not been shown to work.

When the user hands over an existing story to improve, run the same moves on it and report what changed and why. When the user wants a critique of an existing ticket, switch to ticket-readiness-critique.

### 5. Add version criteria where a versioned artifact ships (semantic-versioning)

When the story delivers or changes something consumers depend on (a module, a template, an interface, a document with a declared version):

1. Name the subject, the consumer, and the interface.
2. Classify the intended change with the classifier. A new subject's first version is 0.1.0.
3. Add one AC stating the increment, for example "The release is tagged as a MAJOR increment because it removes an input callers rely on."
4. Add a scenario pair to the Gherkin: one where existing consumers are unaffected (MINOR or PATCH stories) or where the break is declared (MAJOR stories), and one where an undeclared break is rejected or flagged.

When the story touches nothing versioned, add nothing about versions. Examples of the scenario pairs are in `references/gherkin-patterns.md`.

### 6. Write the Gherkin

Apply the rules in `references/gherkin-patterns.md`. In short: operational language only, one behavior per scenario, Given sets a verifiable precondition, When names the single triggering action, Then asserts an observable outcome, and **both poles are written**. In a governance program the negative scenarios are the point.

### 7. Hygiene pass (stricter-ai-language-hygiene)

Sweep the story's prose: the Description, Scope, Context, Dependencies, and any narrative around the scenarios. Gherkin blocks count as machine-consumed specifications, so leave their step wording alone beyond keeping it operational. Write the draft to a scratch file, run the mechanical sweep, judge every hit, and run the counting check: a story that says "four acceptance criteria" has four, and the number of scenarios matches any count the prose claims.

### 8. Present

Show the story in chat or as a file. Do not post. Posting waits for an explicit instruction.

## Skeleton and patterns

- `references/skeleton.md`: the paste-ready story and backlog skeletons.
- `references/gherkin-patterns.md`: the Gherkin rules, worked scenario pairs, and the version scenario pairs.
