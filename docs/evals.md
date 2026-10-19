# Evals

Every skill keeps its evaluation set at `evals/evals.json`, beside its `SKILL.md`. Evals are test assets: no artifact ships them, and changing them bumps no version.

## What a set contains

```json
{
  "skill_name": "<folder name>",
  "should_trigger": ["<request that must load this skill>"],
  "should_not_trigger": ["<request that must not>"],
  "evals": [
    {
      "id": 1,
      "prompt": "<a realistic request, inputs inline>",
      "expected_output": "<one sentence on what a good response is>",
      "assertions": ["<a checkable statement about the response>"],
      "files": []
    }
  ]
}
```

**Trigger prompts.** Five or more each way. Positives include the casual phrasings a user actually types ("check it", "again", "write up this call") alongside the formal ones. Negatives are near misses: requests a sibling skill should take, requests from the same domain that need no skill, and the cross-plugin collisions listed below. A negative that no reasonable reader would confuse with the skill tests nothing.

**Conformance evals.** Two or three per skill, each with inputs written into the prompt so the eval runs without external files. Each assertion is checkable by reading the response: a structure present, a rule applied, a defect flagged, a thing not done. Assertions follow the skill's own rules, so a skill change that alters a rule alters its assertions in the same commit.

**Fixtures.** A skill whose output is a file set (a C4 package, a knowledge pack, an arc42 set) states in its assertions which audit script must report zero FAIL on the output.

## Status at the seed

| Skill set | Trigger prompts | Conformance evals | Assertions |
|---|---|---|---|
| `tech-lead-toolkit` workflow skills | Written for the seed | Two per skill | Yes |
| `architecture-continuity` workflow skills | Written for the seed | Two per skill | Yes |
| `architecture-authoring` workflow skills | Delivered with the plugin; negatives extended to five or more | Two per skill | Yes |
| Shared skills (`blunt-critique`, `semantic-versioning`, `stricter-ai-language-hygiene`) | Written under `shared/skills/<skill>/evals/` | Two or three per skill, inputs inline | Yes. The plugin copies carry them through `sync.py` |

Only the trigger sets of `diagram-assets` and `c4-diagram-package` have been run (see the first collision row). Running a set needs the skill-creator description-optimization loop, which drives the Claude CLI; it is outside what the repository tools do.

## Trigger collisions (owner: the maintainer)

These pairs compete for the same requests when their plugins are installed together. Each set's negatives already name the other side; the measured accuracy, and any description changes it calls for, are the maintainer's to establish.

| Skill | Competes with | Boundary the descriptions draw |
|---|---|---|
| `diagram-assets` (architecture-authoring) | `c4-diagram-package` (architecture-continuity) | A registered asset, a brief, or an arc42 set goes to `diagram-assets`; an estate-wide Mermaid package goes to `c4-diagram-package`. Measured 2026-10-18: no request went to the wrong side; descriptions unchanged |
| `agent-division-of-labor` (architecture-authoring) | `closure-extraction-handoff` (architecture-continuity) | A repository's `HANDOFF.md` and agent contract go to `agent-division-of-labor`; a knowledge pack or a cross-session resume file goes to `closure-extraction-handoff` |
| `atlassian-review-comment` | `ticket-readiness-critique`, `blunt-critique` | Grading delivered work against ACs; judging a ticket before work starts; critique of any other content |
| `story-and-gherkin-drafting` | `ticket-readiness-critique` | Drafting a story; judging an existing one |
| `architecture-set-audit` | `blunt-critique` | Coherence of an arc42 set; critique of arbitrary content |

First row, measured 2026-10-18 with `claude -p` (28 labelled prompts, 3 runs each, 84 runs). Both descriptions were installed together with the other skills of the two plugins, in a project that loaded no other settings or plugins; a run counts as a trigger when the first tool call is the Skill tool. Result: 66 of 84 runs matched the label (79 percent); no run sent a diagram-assets prompt to `c4-diagram-package` or the reverse. The 18 misses are under-triggering, not collision: 15 of 33 `diagram-assets` runs and 2 of 24 `c4-diagram-package` runs loaded no skill (the model opened with Bash to look for files), and 1 critique prompt went to `blunt-critique`. Both prompts that ask for a Mermaid view of an arc42 set loaded neither skill in all six runs, so that boundary case is unresolved by this measurement. Single-sample runs vary, so treat per-prompt counts as indicative.

## Backlog for the maintainer

1. Run the description loop on each plugin, starting with the second collision row, and re-run the first with a harness that does not let a file search pre-empt the Skill call.
2. Keep new plugins to this format from their first commit.
