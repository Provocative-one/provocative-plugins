---
name: evidence-and-registers
description: Decide where a statement in an architecture or estimate document comes from, and file what has no source yet. Marks inferences with [I], files assumptions and open items as [A-nn] with an owner and a closure condition, converts an open item into a priced estimate assumption [EA-nn], opens and maintains decision, risk, component and quality registers, and refuses to close an entry or renumber a register without new evidence. Use whenever the user asks whether something is traceable, whether a claim is an assumption or an inference, asks to mark a statement, add something to a register, open a risk or decision register, close or withdraw an entry such as "close [A-07]", find who owns an assumption, or adds any fact to a document governed by registers. Do not use for general fact-checking outside a register-governed document set.
compatibility: Works on any Markdown document set that declares its sources in front matter. No scripts of its own; ID allocation and citation search use register_tools.py from the arc42-architecture-document skill when the plugin is installed.
metadata:
  version: 0.2.0
---

# Evidence and Registers

Every sentence in a governed document either traces to a source the document declares, or carries a marker saying what kind of unsourced statement it is. Every unknown gets a register row with an owner and a way to close it. This discipline makes a document trustworthy to a skeptical reader, and it is what the rest of the plugin builds on.

## Embedded skills

| When | Skill | Job here |
|---|---|---|
| Filing or closing a row changes a document's content | semantic-versioning | Classifies the bump: a new row or a closed entry is MINOR, a reclassified marker with an unchanged claim is PATCH |
| Before showing any prose | stricter-ai-language-hygiene | Sweeps the sentences you wrote around the markers |
| When the user asks whether the evidence holds up | blunt-critique | Attacks the sourcing, ordered by damage |

Load each by name. When one is unavailable, use its digest in `references/shared-substrate.md` Part F. The register grammar, the default series and the citation conventions are in Part A of the same file.

## The marker decision

Walk these questions in order for each statement.

1. **Does a source the document declares state it?** Then it carries no marker. This covers most of the text, and keeping markers rare is what makes them noticeable.
2. **Is it reasoning drawn from sourced facts, with nobody able to close it?** Mark it `[I]`. State the facts it rests on and the observation that would withdraw it. Give it no owner.
3. **Does it rest on someone's word, or on nothing yet, and could a named person or a checkable source close it?** File it as `[A-nn]` in the architecture's register with its current basis, owner and closing condition, and cite the ID where the statement appears.
4. **Is it an assertion the offer makes, carrying a figure and a consequence?** It is an `[EA-nn]`, and it lives only in the estimate. When it converts an open item, the `[EA-nn]` row cites the `[A-nn]` it converts.

When a case sits between 2 and 3, say so in the text and argue it. The fixture's architecture §4 shows the pattern: the same peak-traffic question is an `[A-02]` because the client holds the figures and named an owner, while the template-divergence forecast beside it is an `[I]` because nobody can close it before it happens.

## Register operations

- **Open a register** with its column headers and no rows. Column shapes are in `references/worked-cases.md`.
- **Add a row** with the next free number: `python3 ../arc42-architecture-document/scripts/register_tools.py next --root <repo> --series A`. Numbers follow the highest ever used, closed and withdrawn rows included.
- **Cite, never retype.** Other sections reference the ID.
- **Close a row** only when the user supplies evidence: a document, a measurement, a dated statement from the owner. Record the evidence in the basis cell and set the status to Closed. When the user asks to close a row without evidence, refuse, and name what would close it.
- **Withdraw a row** that stopped being relevant by setting its status and the reason. Keep the row and its number.
- **Supersede a decision** by adding a new row that cites the old one, and setting the old row's status to "Superseded by" the new ID.
- **Retire an `[I]`** only on a checkable source, rewriting the sentence as sourced or deleting the conclusion.

Find every citation before changing a row: `register_tools.py cites --root <repo> --id A-07`.

## Rules that are easy to break

- **An agent is not a source.** A sentence you produce carries the same burden as one written by hand. Opening vendor documentation and citing the page and the date is evidence. A statement about that documentation made from recall is an `[I]` at best. You never close an entry or retire an `[I]` on your own confidence, and a session is never evidence.
- **Repetition is not evidence.** An attributed statement repeated across sections starts to read as established. Each repetition still cites the row.
- **Internal sources are named.** A figure resting on a colleague's word names the person and the date. It is never presented as client-confirmed.
- **The two confusable pairs** (Part A.3 of the substrate) decide most errors: `[A-nn]` against `[I]`, and `[A-nn]` against `[EA-nn]`.

## Cousin systems

The governance and strategic-report formats carry a sibling marker system: `[S]` secondary source, `[I]` inference, `[X]` documented contradiction, and in strategic reports `[C]` company self-report. `[I]` means the same thing in all of them. The others do not transfer: a bracket around letters alone is a marker, and a bracket around letters with two digits is a register reference.

## Present

Show the marked text and any new register rows in chat or as an edit to the document. Do not commit or post without an explicit instruction.

## What this skill leaves to its siblings

Starting a document set is `arc42-architecture-document`. Pricing open items is `sibling-estimate-document`. Checking a whole set for dangling or misplaced references is `architecture-set-audit`. Which agent may write a register is `agent-division-of-labor`.

## Resources

- `references/worked-cases.md`: column shapes for every register, and five worked cases from the fixture.
- `references/shared-substrate.md`: the register grammar (Part A) and the fallback digests (Part F).
- The fixture at `../../fixture/heritage-hub/` shows every case in a complete set.
