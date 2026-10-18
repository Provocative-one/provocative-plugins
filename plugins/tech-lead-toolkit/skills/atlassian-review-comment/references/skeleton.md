# Review comment skeleton

Paste as unfenced Markdown. The outer fence below only delimits the skeleton here.

```
> **📌 Review Reference**
> MR: [repo!NN](https://gitlab.example.com/.../merge_requests/NN) · File: `path/to/file.tf`
> **Baseline pass** · Ticket: [PROJ-XXXXX](https://example.atlassian.net/browse/PROJ-XXXXX) · Parent feature: [PROJ-YYYYY](https://example.atlassian.net/browse/PROJ-YYYYY)
> Reviewed as per comment <comment-id>

---

> ⚠️ **Classification**
> **❌ Must-have**: correctness or security; resolve before merge · **⚠️ Nice-to-have**: architectural quality; advisory · **Out of scope**: excluded from this ticket's DoD

---

### ✅ What's Good

1. **<Resolved or sound point>.** <Prose nested inside the item, with evidence.>
2. **<Point>** (previously: <what it superseded>). <Prose.>

---

### ❌ Must-haves

1. **<Title> (Must-have).** <The defect, the risk, and the fix, all inside this item.>
   ```hcl
   # illustrative snippet
   ```
   <Concrete remediation, still inside item 1.>

---

### ⚠️ What Could Be Done Differently: Nice-to-haves   [baseline only]

1. **<Title> (Nice-to-have).** <Structural observation, nested.>

---

### 🔒 Merge Blockers

| # | Blocker |
|---|---|
| 1 | <Blocker, traceable to a Must-have above> |

---

### 📋 Recommendations   [baseline only]

| # | Recommendation | Rationale |
|---|---|---|
| 1 | <Follow-up> | <Why> |
```

## Version finding, as it appears inside Must-haves

```
2. **Declared version understates the change (Must-have).** The MR tags `v1.4.1` (PATCH) but removes the `subnet_ids` input. Callers pinned to `~> 1.4` break on upgrade. The removed input is part of the interface callers rely on, so the change is MAJOR. Tag `v2.0.0` and record the removal in the changelog.
```
