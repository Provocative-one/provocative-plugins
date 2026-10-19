# Tech Lead Toolkit

Eight skills for tech leads and architects who keep the written record of an engineering effort. Five produce the artifacts a lead writes every week: review comments, decision records, session reports, ticket critiques, and stories. Three are embedded inside those five and also work alone: blunt critique, semantic-versioning classification, and AI-marker language hygiene.

The toolkit assumes a reader with a Software Engineering or Software Architecture background. It does not teach what an ADR or an acceptance criterion is. It makes the drafts hold up when someone who was not in the room reads them months later.

## The five workflow skills

| Skill | Produces | Reach for it when |
|---|---|---|
| `atlassian-review-comment` | A Jira or GitLab MR review comment graded Must-have, Nice-to-have, or Out of scope, with a version check | You review an MR or a deliverable against its acceptance criteria |
| `ticket-decision-record` | A Direction comment (authorizes an approach) or an Awareness comment (puts an off-ticket decision on the ticket) | A design question is settled, or a Teams thread or meeting decided something the ticket does not show |
| `session-executive-report` | A Markdown executive report from a transcript or recording | You hold a transcript and need minutes a non-attendee can act on |
| `ticket-readiness-critique` | A structured critique of a ticket's readiness, with Entry Blockers | Before a ticket enters a sprint or closes |
| `story-and-gherkin-drafting` | A story or ranked backlog with Gherkin acceptance criteria covering success and refusal | You turn a decision, ADR, or review finding into work |

## The three embedded skills

| Skill | Job |
|---|---|
| `blunt-critique` | Evidence-grounded critique ordered by damage, with no praise sandwich and an explicit "converged" verdict when nothing real is left |
| `semantic-versioning` | Classifies a change as PATCH, MINOR, or MAJOR (or assigns the first version, 0.1.0) for any versioned subject, with a one-sentence rationale naming the interface involved |
| `stricter-ai-language-hygiene` | Removes machine-written markers from prose and runs a mechanical sweep before a draft is shown |

## Where the embedded skills run

| Workflow skill | blunt-critique | semantic-versioning | stricter-ai-language-hygiene |
|---|---|---|---|
| `atlassian-review-comment` | Finds and grades the findings | Checks the declared version against the actual change | Sweeps the comment's prose |
| `ticket-decision-record` | Tests the option analysis; each recommendation names its reversal condition | Classifies the change a decision makes to a versioned artifact | Sweeps the author's prose, never quoted words |
| `session-executive-report` | Keeps blockers, open items, and non-decisions unsoftened | Versions a revised or reissued report | Sweeps the author's prose, never quotes |
| `ticket-readiness-critique` | Runs the full method, including revision rounds | Checks that a ticket shipping a versioned artifact states the increment | Sweeps the critique's prose |
| `story-and-gherkin-drafting` | Attacks the draft's own acceptance criteria before you see them | Adds a version criterion and scenario pair when something versioned ships | Sweeps the prose around the Gherkin |

Each workflow skill loads the three by name. If one is missing, a short digest in `references/shared-substrate.md` (Part D) keeps the workflow running.

## Working rules shared by the five

- **Draft first.** Nothing is posted to Jira, Teams, Confluence, or GitLab until you say so.
- **Quotes stay verbatim.** The language sweep never touches quoted text, code, or Gherkin step wording.
- **One meaning per label.** Must-have blocks Done. Nice-to-have is advisory. Out of scope is named so the boundary is explicit.
- **Evidence travels with the finding.** File and line, quoted ticket text, or a timestamped quote.
- **Calibration.** When you paste the published version back, the skills diff it against the draft and name each divergence.

## Assumptions

The platform mechanics are written for Jira, Confluence, GitLab, and Microsoft Teams: paste behavior, field quirks, ID formats. The formats and the reasoning transfer to other trackers, and `references/shared-substrate.md` Part C is the only place that is platform-specific. Connect Atlassian, GitLab, and Microsoft 365 MCP servers if you want Claude to retrieve source material itself. Without them, paste the material in.

## Install

This repository root is a marketplace that contains the plugin.

```
claude plugin marketplace add <path-or-repository-containing-this-folder>
claude plugin install tech-lead-toolkit@tech-lead-toolkit-marketplace
```

The manifest layout follows Anthropic's public reference plugins. For Cowork, or to load the folder as a local plugin, follow the current plugin documentation, since those steps change.

## Maintenance

The toolkit is at version 0.1.0 and follows its own semantic-versioning skill. Its consumers are the people and prompts that depend on skill names, triggers, and output formats, so renaming a skill or changing a template's section order is MAJOR, adding a skill or a section is MINOR, and wording fixes are PATCH.

Two things to know before editing:

- `references/shared-substrate.md` is identical in the five workflow skills, so each skill stands alone. Edit one copy, then copy it to the other four.
- The three embedded skills are verbatim copies of the originals (`stricter-ai-language-hygiene` carries its own version, 1.1.0). Update them from their source and keep the copies in sync.
