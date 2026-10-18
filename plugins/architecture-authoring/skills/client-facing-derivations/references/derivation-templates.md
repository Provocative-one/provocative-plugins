# Derivation templates

## The brief

```
# Brief: <artifact>

**Generated from:** architecture <x.y.z>, estimate <x.y.z>. **Published as:** `published/<artifact>-<version>.<ext>`. **Version:** <x.y.z>

## Request
<The request as given, by whom, on what date.>

## Decisions
- <Decision, who took it, on what date.>

## Derivations
<Every conversion shown in full: a unit converted to weeks, with its rounding and the slack it leaves.>

## Divergence from the source
<Where the artifact says less than its source, and why. The source keeps the full statement; the engagement is held to the source.>

## Traceability
| Artifact element | Source |
|---|---|
| <slide 2, bullet 3> | <estimate [M-02], §10> |

## Content
<The artifact's text transcribed, so the brief reads without the originating application.>

## Build and verification
<How it was built; the derived-mode audit result; who reviewed it.>

## Open points
<Anything unresolved, each with its owner.>

## Regeneration
Rebuild when either source moves; publish as a new file and a new brief version.
```

## §1 Offer traceability annex

Internal map, one row per costed element:

| Element | Origin class | Protects | Client may change | Proposal section | Client section |
|---|---|---|---|---|---|
| <element> | `[R]` / `[N]` / `[E]` / `[U]` | <what it protects> | <what the client may change> | <§> | <Section n> |

Reading rules. `[R]` follows from the client's request, cited by their section number. `[N]` is needed to make the solution work, and its row says what fails without it. `[E]` is proposed by us and the client may decline it. `[U]` was decided with the client at discovery, with the date. State the approximate share of effort per class once, in a sentence, never as price lines. The client-facing annex groups the rows under plain headings ("Required by your request", "Needed to make it work", "Proposed", "Agreed at discovery") and drops the letters.

## §2 Assumptions and exclusions annex

Grouped by theme: integration, scope boundaries, non-functional, environment, cadence, commercial, phase pricing basis, technical, client dependencies and decision timeframes, explicit exclusions. Each item states the assumption and its consequence if it fails. Generate the items with `register_tools.py project`, then rewrite into the client register. Number the items; the numbers are what a clarification round refers to.

## §3 Milestone plan

Per milestone: outcome, acceptance evidence written to be objectively testable, planned duration, dependencies. Then one paragraph stating which dates hold with confidence and which are confirmed again at gates, and the rule that a client-side slip moves the date through change control and never into price.

## §4 Clarification response

| Question | Answer | Anchored to | Commitment owner | Written or call |
|---|---|---|---|---|
| <their question, their numbering> | <answer in client register> | <register row or section> | <owner, when the answer commits> | Written / Call |

Then the reissue list from `audit.py --reissue`: every annex item and passage the answers change. Items marked Call go on a decision list for the meeting.

## Pre-send checklist

1. The brief pins the versions the artifact was generated from, and they are current.
2. `audit.py --derived` on the text dump reports zero FAIL.
3. No excluded section reached the artifact, including by paraphrase.
4. Every commitment carries an approved owner.
5. Every divergence from the sources is recorded in the brief.
6. The file lands in `published/` with its version in the name, and the changelog records it.
