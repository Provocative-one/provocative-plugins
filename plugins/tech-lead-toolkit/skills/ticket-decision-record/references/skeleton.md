# Decision record skeletons

Paste as unfenced Markdown. The outer fences only delimit each skeleton here. No `@` mentions; the user adds them on paste.

## Direction comment

```
**Direction — <one-line summary>**
Ticket: [PROJ-XXXXX](https://example.atlassian.net/browse/PROJ-XXXXX) · Sprint <n> · Parent: [PROJ-YYYYY](...)
Reviewed as per comment <comment-id>   (traceability slot; delete if none applies)

Cross-references:
- MR: [repo!NN](...)
- Pipeline: [`path/pipeline.yml`](...)
- ADR: [ADR-00X](...)

---

**Context**
<Where this stands right now, grounded in the actual artifact.>

---

**Approach**
<The agreed path, stated affirmatively.>

---

**Change surface**
<Exactly what changes and where: files, jobs, line references verified against source.>

---

**Design decision**
<The question settled. The option chosen. The alternatives and why each lost. The reversal condition: what observation would reopen this.>

---

**Delivery and scope**
<In, out, sequencing. Version consequence where a versioned artifact changes: increment plus one sentence naming the interface expectation preserved or broken. No story-point reconciliation here.>
```

## Awareness comment

```
**Awareness — <what is being made visible>**
Making visible on this story the discussion held in [<thread name>](<Teams link>).

---

**Discussion**

<Given Surname, Role> — <YYYY-MM-DD> [HH:MM:SS]
> <verbatim or faithful excerpt>

<Given Surname, Role> — <YYYY-MM-DD> [HH:MM:SS]
> <verbatim or faithful excerpt>

---

**Determination**
<What was decided or asserted, plainly. "No determination reached" when that is the fact, followed by what remains open.>

---

**Bearing on this story**
<Which path is now closed or endorsed. Any dependency created. When a versioned artifact is amended: the increment and one sentence of rationale.>
```

## The paired form

1. Awareness comment on the parent or discovery ticket: the stakeholder position, in the stakeholder's words.
2. Direction comment on the implementation story: the technical answer, with a sequence diagram when it clarifies, referencing the awareness comment by link.
