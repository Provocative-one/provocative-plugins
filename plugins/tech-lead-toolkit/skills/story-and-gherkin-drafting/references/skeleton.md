# Story and backlog skeletons

Paste as unfenced Markdown. The outer fences only delimit each skeleton here. Fenced Gherkin blocks inside the story number their own lines, so add no inline numbering to them.

## Backlog of several stories

```
### Priority stack

| Rank | Item |
|---|---|
| 1 | <highest> |
| 2 | <next> |

**Live disagreement on priority** (include only when one exists)
<Position A, attributed.> <Position B, attributed.> Governing constraint: <the constraint that decides, with its source.>

---

<Story 1 skeleton below>
---
<Story 2 skeleton below>
```

## Single story

```
## Description
**As a <role>, I want <capability>, so that <outcome>.**

### Scope
- <Item> (Must-have)
- <Item> (Nice-to-have)
- <Item> (Out of scope)

### Context
- <Reference or decision the assignee must hold>: [link](...)
- <Reference>: [link](...)

### Acceptance Criteria
1. <A single, unambiguous, observable criterion.>
2. <A potential Must-have issue, stated as a criterion.>
3. <Version criterion, only when a versioned artifact ships: "The release is tagged <increment> because <interface expectation preserved or broken>.">

#### Gherkin Scenarios

##### Positive Scenarios — Governance & Assurance Success

```gherkin
Scenario: <control behaves as specified>
  Given <verifiable precondition>
  When <single triggering action>
  Then <observable outcome>
```

##### Negative Scenarios — Governance & Assurance Failures

```gherkin
Scenario: <violation is refused>
  Given <verifiable precondition>
  When <single triggering action>
  Then <observable refusal>
  And <the refusal names what was violated>
```

### Dependencies
- Blocked by [PROJ-XXXXX](...)   (modeled as an issue link, not left in prose)

### References
- [<Resource>](<live link>)
```

## Outline skeleton for work a colleague will author

Use when the colleague keeps authorship (an ADR, a design note). Provide headings and one-line prompts under each, and stop there.

```
## <Section heading>
<One line saying what the author must settle here.>
```
