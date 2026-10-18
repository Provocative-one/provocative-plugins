---
name: atlassian-review-comment
description: Draft a paste-ready Jira or GitLab merge-request review comment that gates a body of work (an MR, a module, a policy, a pipeline change, a document) against its acceptance criteria, grading every finding Must-have, Nice-to-have, or Out of scope. Use whenever the user asks to review an MR or a ticket's deliverable, produce a review comment, run a baseline, re-review, or final pass, check whether work is ready to merge or close, or says "review this against the ACs", even if the format is never named. Carries the Atlassian paste mechanics (ADF list nesting, unfenced Markdown, the code-span link quirk) that plain drafting gets wrong, and checks the version the work declares against the change it contains.
metadata:
  version: 0.1.0
---

# Atlassian Review Comment

A review comment gates work against its acceptance criteria and must read cleanly to someone who was never in the room. It is the durable record of the review, so every finding carries its evidence and every severity label means one thing.

## Embedded skills

Three skills run inside this one at fixed points. Load each by name, or read its SKILL.md from the plugins skills directory. When one is unavailable, use its digest in `references/shared-substrate.md` (Part D).

| Step | Skill | Job here |
|---|---|---|
| 2 | blunt-critique | Finds the problems and grades them |
| 3 | semantic-versioning | Checks the declared version against the actual change |
| 5 | stricter-ai-language-hygiene | Sweeps the comment's prose before it is shown |

Operating protocol (draft-first, calibration, traceability anchors), naming rules, and paste mechanics live in `references/shared-substrate.md`. Read Parts A to C at the start of a session.

## Workflow

### 1. Fix the standard under review

Read the ticket, its acceptance criteria, the parent feature, any posted Scope Amendment, every earlier review comment, and the full MR diff. Establish the pass type: **baseline** (first review of this deliverable), **superseding** (re-review after fixes), or **final** (the pass that clears the merge).

Three rules decide what Done means:

- **The ACs govern.** Where a deliverable's framing conflicts with its written acceptance criteria, the ACs win, unless a formal Scope Amendment has been posted and acknowledged on the ticket.
- **A deliverable cannot redefine its own Done bar.** A guide or design that declares it supersedes the ACs it was written to satisfy gets flagged. The story sets the ACs.
- **A control that has never been shown to refuse has not been shown to work.** For guardrails, policies, and gates, look for negative-path evidence before accepting the positive path.

### 2. Analyse bluntly (blunt-critique)

Run the blunt-critique method on the work before drafting anything. Specifics for MR review:

- On a re-review, diff against the prior pass first. Verify every earlier Must-have at the exact spot it was raised, then inspect the surrounding lines for damage from the fix (a repair routinely breaks a parallel structure one block over).
- Order findings by damage. Quote the evidence: file path, line, text.
- Grade each finding with this test. Correctness or security that blocks Done: **Must-have**. Architectural or structural quality that is advisory: **Nice-to-have**. Excluded from this ticket's Definition of Done: **Out of scope**, named so the boundary is explicit.
- Never manufacture a Must-have. An objection you would concede under pushback is dropped before it reaches the page.
- When a full pass finds nothing real, write "No remaining must-haves", state what was checked, and say the work has converged.

The chat reply may carry the unfiltered analysis (Part A, analysis register). The posted comment carries evidence, severity, and the required fix.

### 3. Check version declarations (semantic-versioning)

When the MR changes something consumers depend on or pin (a module, a policy set, a pipeline template, an API, a schema, a document with a declared version), run the classifier.

1. Name the subject, the consumer (callers of the module, pipelines including the template), and the interface (inputs, outputs, behavior the consumer relies on).
2. Classify the change as the classifier prescribes, then compare it with the increment the MR declares (tag, changelog entry, version file).
3. Grade the mismatch:
   - **Under-declared** (a breaking change shipped as MINOR or PATCH): Must-have. Consumers on a compatible range take it silently.
   - **Over-declared** (a PATCH-sized change shipped as MINOR): Nice-to-have. It forces consumers to re-engage for nothing.
   - **First version of a new subject** tagged anything other than 0.1.0: flag it.
   - **No declaration** on a subject consumers pin: Must-have. On a subject nobody pins: Nice-to-have.
4. Write the one-sentence rationale the classifier requires, naming the interface expectation preserved or broken. If the consumer or interface cannot be established from the MR, state the assumption inside the finding. The user reviews the draft before anything posts, so the assumption is visible and correctable.

### 4. Render the comment

Seven sections, in this order. Sections 5 and 7 are **omitted on a final-pass comment**. They belong to a baseline pass, where structural and forward-looking observations still have a place.

1. **Header note panel.** MR link, module or file path, baseline or superseding designation, ticket and parent-feature cross-references. Live links.
2. **Legend.** The three-tier warning panel.
3. **✅ What's Good.** One bullet per item, prose nested inside it. Mark items resolved since a prior pass with `(previously: …)`.
4. **❌ Must-haves.** Numbered. Each title carries `(Must-have)`. Prose, code block, and the concrete fix nest inside the item. If none remain, say so.
5. **⚠️ What Could Be Done Differently, Nice-to-haves** (baseline only). Numbered, each title carries `(Nice-to-have)`.
6. **🔒 Merge Blockers.** Table `| # | Blocker |`. Every row traces to a Must-have above.
7. **📋 Recommendations** (baseline only). Table of forward-looking follow-ups with rationale.

Rules for the record:

- **What's Good states facts.** Each item is specific and evidenced ("the guard now rejects the empty-list case, verified at `path:line`"). Ceremonial praise is deleted. On a superseding or final pass, confirmed fixes are the main content of this section.
- **Merge Blockers equal Must-haves.** A blocker without a Must-have behind it, or a Must-have without a blocker row, is a defect in the comment.
- **ADF nesting.** Explanatory prose lives inside its numbered item. A standalone paragraph between items renders every later item as "1.".
- **No `@` mentions**, no relative dates, no inaccessible links. A traceability slot ("Reviewed as per comment …") sits under the header when the pass answers an earlier comment.

### 5. Hygiene pass (stricter-ai-language-hygiene)

Apply the strictest register to the comment's prose, since it is a permanent record read by the customer's engineers. Exempt from the sweep: code blocks, quoted diff text, paths, identifiers, table cells, and the `(previously: …)` tags (a review-pass ledger has the same function as a changelog, which the hygiene skill exempts).

Write the draft to a scratch `.md` file and run the skill's mechanical sweep. Judge every hit. Then run the counting check: every number in the prose against the list it heads, and Merge Blockers rows against the Must-have count.

### 6. Present

Show the finished comment in chat or as a file. Do not post it. Posting waits for an explicit instruction (Part A).

## Legend and the retired MoSCoW scheme

| Tier | Meaning |
|---|---|
| ❌ Must-have | Correctness or security. Blocks Done. Resolve before merge. |
| ⚠️ Nice-to-have | Architectural or structural quality. Advisory, a candidate for follow-up. |
| Out of scope | Excluded from this ticket's Definition of Done, named so the boundary is explicit. |

MoSCoW was retired because "Should-have" was read as "optional but expected", which blurs the one line that has to stay sharp: what blocks Done. To reconcile an older comment: Must-have stays Must-have, Should-have and Could-have become Nice-to-have, Won't-have becomes Out of scope.

## Skeleton

The paste-ready skeleton is in `references/skeleton.md`. Copy its structure exactly and replace the placeholders.
