# Ticket critique skeleton

Paste as unfenced Markdown. The outer fence only delimits the skeleton here. No `@` mentions.

```
**Critique of [PROJ-XXXXX](https://example.atlassian.net/browse/PROJ-XXXXX)** · <pass: first | revision n> · Governing record: [<session or decision>](<live link>)
Reviewed as per comment <comment-id>   (traceability slot; delete if none applies)

---

### ✅ What Works

- <Sound element, with evidence: architectural content, clear scoping, correct linkage.>

---

### ❌ Must-haves

1. **<Defect>.** <Prose with the quoted ticket text as evidence. Metadata misalignments belong here, not below.>
2. **<Missing ACs, unmodeled dependency, status contradiction, or version declaration defect>.** <Prose and the fix, nested inside the item.>

---

### ⚠️ Nice-to-haves

1. **<Quality improvement that does not block entry>.** <Prose.>

---

#### Gherkin Scenarios   (optional; draft with the story-and-gherkin-drafting skill)

---

### 🔒 Entry Blockers

| # | Blocker |
|---|---|
| 1 | <e.g., Priority must be corrected to Highest before this enters any sprint> |
```

## Convergence form

```
No entry blockers. A full pass was made against <governing records>, each earlier Must-have was verified at the field where it was raised, and the neighboring fields were checked for collateral changes. The ticket is ready.
```

## Version finding, as it appears inside Must-haves

```
3. **Deliverable is versioned but the ticket states no increment.** The story changes the module's output names, which callers consume. That alters the interface callers rely on, so the release is MAJOR. Add an AC naming the increment and the rationale.
```
