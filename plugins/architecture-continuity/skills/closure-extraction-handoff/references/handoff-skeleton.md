# Handoff package skeleton

A handoff package is one Markdown file that lets a fresh Claude instance, on any surface, or a successor resume the work with no dependency on memory, prior turns, or connector access. The outer fence below only delimits the skeleton.

```
# <Subject>: Handoff Package

**Version** <x.y.z> · **Exported** <YYYY-MM-DD> · **Supersedes** <prior version, or "none">

> **Purpose.** A self-sufficient export of <the in-progress work>, built so a fresh Claude instance (any surface: chat, Code, Cowork, API, or another person's session) can resume it with full context.
>
> **How to resume.** Paste this file into a new conversation, or upload it. If the asset files listed in Part 3 are available, attach them. If the <Atlassian, Confluence, or other> connector is available, the source documents can be re-fetched live (identifiers are in Part 2), and nothing here depends on that.
>
> **Provenance.** The source documents in Part 2 are reproduced verbatim as of <date>. <Every edit, stated: image references replaced by figure markers, an oversized URL elided. Nothing else was altered.>

---

## Part 0. Instructions for the receiving Claude

You are picking up <the work> authored by <Given Surname>. <One sentence on the stance: sharp peer or editorial work, an architecture review, a drafting engagement.> The consolidated state is in Part 4 and the live open threads are in Part 5. Continue from there unless redirected.

<Include the next two lines only when the author wants them.>
Operate in the author's register (Part 1). Deliver substance. Do not open with a volley of clarifying questions. State any framing assumption in a line and proceed.

**Environment notes** (dated, since identifiers expire)
- <Connector, site identifier, field quirk, or tool behavior that changes what the next instance does.>

---

## Part 1. Who you are working with

<Name, role, location and time zone where relevant. The working preferences the task needs: register, rhetorical habits to match or avoid, banned phrases, how to handle ambiguity. Only what the user has approved for this file. No credentials, no sensitive personal detail.>

---

## Part 2. The source material (verbatim)

| # | Title | Identifier | Live link | Retrieved |
|---|---|---|---|---|
| 1 | <title> | <page ID or path> | <link> | <YYYY-MM-DD> |

### 2.1 Source document 1: <title>

````markdown
<verbatim text>
````

---

## Part 3. Asset manifest

| File | Belongs to | Depicts | Finding attached |
|---|---|---|---|
| `<file name>` | <Part 2 section> | <what the asset shows, described faithfully> | <the analytical finding that goes with it> |

Assets cannot be embedded as pixels here, so each is described with its finding attached.

---

## Part 4. Consolidated state

Group by what is settled, what changed, and what remains contested.

### 4.1 What the work is and what it earns
<The framing and the strengths that survived scrutiny, each with its evidence.>

### 4.2 Findings in force
<Numbered. Each carries severity and the quoted evidence.>

### 4.3 Concerns retired or revised

| Earlier concern | What later evidence showed | Status |
|---|---|---|
| <concern> | <the evidence> | Retired / Revised / Still open |

### 4.4 Judgments of mine that proved premature
<Earlier conclusions that a later, more careful treatment overturned, stated as bluntly as any finding about the work itself.>

---

## Part 5. Open threads and recommended next moves

Prioritized. <State plainly which have been executed. When none has, say so.>

1. **<Thread>.** What closes it: <condition>. Status: <not started | in progress | blocked by X>.
2. ...

---

## Part 6. Glossary and anchors

Carry this vocabulary forward verbatim. It belongs to the author.

- **<Term>.** <Definition, with the test that admits or excludes an instance.>

---

*End of handoff package. To continue, address Part 5 in priority order, in the author's register (Part 1), grounding every abstraction in the real context (Part 0).*
```

## Rules for filling it in

- **Consolidate, do not narrate.** Part 4 states where the work stands. It does not retell the conversation round by round.
- **Verbatim means verbatim.** Part 2 is never summarized, cleaned, or restyled. Each edit is disclosed in the Provenance note.
- **Settled, revised, open.** Every finding sits in one of the three states. A finding the later work retired appears in Part 4.3 with the evidence that retired it, so a successor does not reopen it.
- **Open threads carry closure conditions.** A thread with no stated way to close it is a wish.
- **Identifiers are state.** Cloud IDs, project IDs, and page IDs expire or change. Date them in Part 0 and keep them out of the prose of Part 4.
- **No secrets.** Tokens, keys, and passwords never enter the file. Name where they live.
- **The file stands alone.** It must not say "as discussed" or refer to a turn the reader cannot see.
