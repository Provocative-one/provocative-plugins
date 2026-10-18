---
name: stricter-ai-language-hygiene
description: Enforce strict AI-marker hygiene on every piece of prose Claude produces or edits, including typographic treatment of foreign terms (italics) and of concepts/constructs introduced by the text (bold at definition, Capitalized thereafter). Apply this skill whenever generating or revising ANY artifact (documents, reports, proposals, architecture docs, narratives, README files, commit messages, changelogs) and whenever drafting ANY email, Teams, Slack, or chat message, even short ones, even when the user does not mention hygiene. The rules are standing practice, not a requested step. Also apply when the user asks for a "hygiene pass", "marker sweep", "de-AI", "make it sound human", mentions text reading as AI-generated, or asks for review of tone, style, or coherence in written material.
metadata:
  version: 1.1.1
---

# Stricter AI-marked Language Hygiene

Prose that reads as machine-written costs the author credibility before the content is judged. The rules below apply to every artifact and every drafted message, on every pass, before the pass is considered complete. They are not a step the user requests.

Language-marker rule families, then the typographic choreography for foreign terms and constructs, then register calibration, then the mechanical sweep.

## 1. Em-dashes: prefer alternate constructs

The mid-sentence rhetorical em-dash is the single loudest AI marker. Default replacements, in order of preference: a comma, a colon, a period and new sentence, parentheses.

Sanctioned uses, which stay:
- **Series within a phrase**, paired dashes: "the three control domains — access, change, operations — over a recognized baseline".
- **Structural labels and headers**: "Phase 1 — Weeks 1 to 4", "**Owner — Operations.**".
- **Table placeholder cells** (`| — |`). Never count these as prose.
- **At most one or two abrupt-change dashes per document**, kept only where the sentence is the argument's sharpest point: "visibility, not control — unusual for a platform in this category".

Norm for body prose: after the sweep, non-series, non-label dashes number zero to two per document. New sections start at zero.

Treat even the sanctioned abrupt-change dash as a last resort, not a default option: reach for it only when no comma, colon, period, or parenthetical carries the same emphasis without loss. Whenever an alternative construction exists, prefer it.

Rewrite patterns from practice:
- "it now says one — the register row was corrected and the sentence was not" → "it now says one. The register row was corrected; the sentence citing it was missed."
- "grew by 23 to 32 against v2.0.2 — 43 to 58 against v1.2.0 — entirely from peer review" → "grew by 23 to 32 against v2.0.2 (43 to 58 against v1.2.0), entirely from peer review".
- "the Lisbon office — relevant for the site demonstrations" → "the Lisbon office, which is relevant for the site demonstrations".

## 2. The antithesis reflex

"X, not Y", "rather than", "instead of", "not just X but Y" firing every few paragraphs is a rhythm tell, independent of any single instance being fine. Rule: one strong contrast per argument. Keep the instance that IS the argument; delete the reflexive ones.

- Keep: "an operated instrument, not a clause"; "a deliverable, not a byproduct"; "our proposal, not a question". Each carries the point of its sentence.
- Cut or flatten: "priced rather than absorbed at 3–5 person-weeks" → "priced at 3–5 person-weeks". "is configured, not rebuilt, for more" → "adding more is configuration". "measured from the start instead of asserted at the end" → "visible from the first phase, measured against where things stood before anything changed".

Audit the whole document: count "instead of" and "rather than". Several instances spread across sections, each carrying a distinct argument, is normal prose. Two in one paragraph, or the same construction shape recurring, is the tic.

## 3. Metalanguage

Text about the text: delete or ground it. The content should do the work the announcement claims.

Default assumption: the text does not talk about itself. A self-referential aside earns its place only when removing it would remove part of the argument, not merely when it felt natural to write. Mitigate to the maximum; let survive only what is central to the argument being made.

Delete on sight: "Read this part first", "worth reading/noting/saying", "Two notes on X." as a counter before uncounted prose, "a reader should know where", "the point of this section/board is", "this section describes", "in this view", "It is worth answering directly" (→ "deserves a direct answer" or restructure).

Exception: **reading rules in reference registers** ("Read the column on the right first" above a register table) where that is the document's established convention and the instruction changes how the table is used. Functional navigation survives; self-narration does not.

## 4. Epanorthoses, including soft ones

Epanorthosis is stating something and then correcting or restating it. The hard forms ("or rather", "more precisely", "in fact") are rare in careful drafts; the soft forms are common and equally marking. A soft epanorthosis asserts, then adds a correction-shaped clause qualifying its own assertion.

- "The other five are not less designed; they are specified elsewhere" → "The other five are specified elsewhere."
- "stated as a rule rather than a hope" → "stated as a rule".
- "A lightweight view, and deliberately so: most of the design predates this section" → delete the frame; open with the content.
- "X — and that matters" appended to a claim → make the claim in a form where it visibly matters, or cut the tag.

One assertion per sentence. If the sentence corrects itself, rewrite it as the corrected version only.

Sweep for the subtlest register too, not only the marked forms: a hedge that softens a claim the instant after making it, an aside that half-retracts a distinction just drawn, a parenthetical that qualifies the sentence's own certainty. If a second clause exists only to soften the first, cut the second clause or rewrite the first as the sentence's single, unqualified assertion.

## 5. Editorial residue embedded in arguments

Body text that narrates its own revision history or review process is changelog content leaking into the argument. Changelogs and commit messages own provenance; body sections state the design, estimate, or position **as it stands**, with its rationale.

Diff-talk markers to remove from body text: "is new", "rose to", "rises because", "now also carries", "since v1.2.0", "was added after review", "came from peer review", "the correction that matters most", "previously unpriced", "flagged in the changelog as". Self-referential process praise ("which this project has now demonstrated three times") is the same defect.

Rewrites from practice:
- "Four additions since v1.2.0, all from security review: secrets and service identity, ..." → "Beyond the substrate itself, the second phase carries secrets and service identity, ...".
- "That line rose to carry source authentication" → "The line includes source authentication".
- "The interim metrics view is new. Full reporting lands in the final phase while ..." → "The interim metrics view exists because full reporting lands in the final phase while ...".
- "Security advisory rises because the control set is now ours to author" → "Security advisory covers authorship of the control set, not review against one supplied".

Changelogs are exempt: describing diffs is their function.

## 6. Vocabulary and scaffold phrases

Banned outright, including close equivalents: seamless, pivotal, holistic, robust, leverage, delve, crucial, journey, empower, cutting-edge, world-class, unparalleled, innovative (as self-praise).

Scaffold phrases to cut or vary: "load-bearing", "by design" (at most once per document; vary with "on purpose", "kept small on purpose", or restructure), "deliberately so", "genuinely" and "materially" as hedges, "That is what makes", "which is what makes", "honest/honestly" as self-description, enumeration openers ("Three rules keep this section honest" → "Three rules bind this section to §X").

## 7. Coherence checks travel with hygiene

Counting claims are the cheapest thing a skeptical reader verifies, and hygiene passes are when they get caught. On every pass, check every stated count against the list it heads:

- "Eight capabilities" above a table of eleven rows.
- "two of these four are competitive advantages" above a list of six items, with the two never named.
- A pivot line saying "five desks" after a paragraph that built three.

Fix the number, or better, name the members. Also re-verify after the pass: figures, cross-references, version anchors, and any arithmetic must be untouched by wording edits. Run whatever mechanical verification the document set uses.

## 8. Register calibration: not every text gets the same depth

| Register | Depth of pass |
|---|---|
| Client-facing or decision-maker-facing (narratives, proposals, cover letters) | Strictest. Every rule, every instance judged |
| Attachable working documents (staffing models, architecture docs likely to be shared) | Deep. Body prose fully swept; structural conventions kept |
| Internal working documents | Newest text swept hard; text that has survived human review rounds is left alone |
| Generation tooling (diagram prompts, machine-consumed specs, code) | Untouched. Precision over prose; sanding buys nothing and risks the payload |

Two principles behind the table. First, **do not churn human-approved text**: wording that survived a human editorial pass is theirs now, and a document where every paragraph has identical rhythm is itself a tell. Second, **your newest text is your densest text**: additions written minutes ago carry the most markers, so sweep them hardest.

## 9. Messages: email, Teams, Slack, chat

All rules above apply to drafted messages, plus:
- Direct register. Short sentences. Bold sparingly, for the one rule or number the reader must not miss.
- No essay-shaped bullet lists; a bullet is a line, not a paragraph.
- Name the people whose action is needed; put their item where they will see it.
- Commit messages and changelogs may narrate diffs (that is their job) but still obey the dash, antithesis, vocabulary, and epanorthosis rules.

## 10. The mechanical sweep

No pass is complete until this runs clean. Adjust filenames; the logic is fixed.

```bash
python3 - << 'EOF'
import re, sys
files = sys.argv[1:] if len(sys.argv) > 1 else ["DOC.md"]
for f in files:
    s = open(f).read()
    body = 0; total = 0
    for l in s.split('\n'):
        t = re.sub(r'\|\s*—\s*(?=\|)', '', l)          # ignore table placeholder cells
        n = t.count('—'); total += n
        if n and not l.startswith('#') and not re.search('—.*—', t) \
             and not re.match(r'\*\*[^*]+—', l) and not l.startswith('|'):
            body += n                                    # non-series, non-label, non-table
    print(f, "| em-dashes:", total, "| rhetorical body dashes:", body, "(target 0-2)")
    for w in ['seamless','pivotal','holistic','robust','leverage','delve',
              'crucial','journey','empower','cutting-edge','world-class']:
        if w in s.lower(): print("  BANNED WORD:", w)
    print("  instead of:", s.count('instead of'), "| rather than:", s.count('rather than'))
EOF
```

```bash
# Editorial residue and metalanguage grep (exclude changelog/commit zones by line range or by eye)
grep -n "is new\|rose to\|rises because\|since v[0-9]\|now also\|came from peer review\|worth noting\|worth reading\|Read this part\|notes on \|deliberately so\|load-bearing\|not less\|predates this section\|by design" FILES
```

Interpretation, not automation: every hit is a candidate, not a verdict. A "rather than" carrying a real argument stays. The sweep exists so nothing escapes judgment, not so judgment is replaced.

## 11. Typographic treatment: foreign terms and established concepts

Two conventions distinguish borrowed vocabulary from vocabulary the text itself defines. Both are typographic, not lexical: they mark status, not meaning.

**Foreign terms.** When a foreign-language term is unavoidable, because no term in the working language carries the same precision, italicize it at every occurrence, not only the first. A loanword that has naturalized into the working language's technical register (*software*, *deploy*, and similar terms inside a Portuguese text on systems) is not foreign in this sense and stays unitalicized, unless the register specifically calls for marking it as still borrowed.

**Concepts and constructs.** A term the text introduces as its own concept or construct, rather than one it borrows from established usage, follows a fixed choreography:
- First occurrence, immediately before the definition, set in **bold**.
- The definition itself, in plain prose, no special marking.
- Every occurrence after the definition, Capitalized. Capitalization signals that the word now names the concept the text established, not the ordinary term or expression it derives from.

Example: "what follows, the analysis treats as a **Boundary Condition**: a constraint imposed from outside the system that the system cannot revise from within. A Boundary Condition, once identified, changes what counts as a legitimate move inside the system." The shift from bold-at-definition to Capitalized-thereafter is the point; reverting to lowercase after the definition erases the distinction the choreography exists to mark, and re-bolding later occurrences confuses definition with mere emphasis.

This choreography applies to constructs original to the piece, the author's own terms, a distinction an essay draws for the first time, a category proposed inside an architecture document, and not to vocabulary already governed by an external convention: *Enterprise Architecture* stays capitalized because the discipline capitalizes it, not because this rule does; ordinary philosophical vocabulary (ethics, praxis, telos) stays lowercase unless the text is itself redefining the term as a construct.

## Order of operations on any writing or editing task

1. Write or edit for content first.
2. Sweep your own new text with all rule families before presenting it, including the typographic choreography (§11): italicize unavoidable foreign terms, and bold-then-Capitalize each construct at and after its first definition.
3. Run the mechanical sweep; judge every hit.
4. Run the coherence counting check (§7) and re-verify untouched figures and references.
5. Only then is the pass complete. Never present prose and offer hygiene as a follow-up.
