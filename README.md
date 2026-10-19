# provocative-plugins

A Claude plugin marketplace. Each plugin under `plugins/` installs on its own; this repository lists them all through `.claude-plugin/marketplace.json`, and holds the shared material several plugins carry.

## Index

Regenerated from each plugin's manifest and each skill's frontmatter by `tools/index.py`. The pre-commit hook keeps it current.

<!-- index:start -->
### Plugins

| Plugin | Version | Description |
|---|---|---|
| `architecture-authoring` | 0.3.0 | Author arc42 architecture document sets under an evidence discipline: sourced statements or marked ones, registers with owners and closure conditions, a one-way estimate priced against a calibrated unit, diagram assets briefed and accepted as traceable claims, a coherence audit that gates every version, client-facing derivations generated and never retyped, and a contract for agents sharing the repository. Embeds blunt critique, semantic-versioning classification, and AI-marker language hygiene. |
| `architecture-continuity` | 0.1.1 | Architecture documentation and knowledge continuity for architects and tech leads: C4 diagram packages under a state-encoding grammar, and closure extraction and handoff packages that let work survive the people who hold it, with blunt critique, semantic-versioning classification, and AI-marker language hygiene built into both. |
| `tech-lead-toolkit` | 0.1.1 | Drafting and review skills for tech leads and architects who keep the written record of an engineering effort: Jira and GitLab review comments, decision records, session reports, ticket critiques, and stories with Gherkin acceptance criteria, with blunt critique, semantic-versioning classification, and AI-marker language hygiene built into each. |

### Skills

| Plugin | Skill | Version | Kind | Also standalone |
|---|---|---|---|---|
| `architecture-authoring` | `agent-division-of-labor` | 0.3.0 | plugin skill |  |
| `architecture-authoring` | `arc42-architecture-document` | 0.2.1 | plugin skill |  |
| `architecture-authoring` | `architecture-set-audit` | 0.2.1 | plugin skill |  |
| `architecture-authoring` | `blunt-critique` | 0.2.0 | shared copy |  |
| `architecture-authoring` | `client-facing-derivations` | 0.2.1 | plugin skill |  |
| `architecture-authoring` | `diagram-assets` | 0.1.1 | plugin skill |  |
| `architecture-authoring` | `evidence-and-registers` | 0.2.1 | plugin skill |  |
| `architecture-authoring` | `semantic-versioning` | 0.2.0 | shared copy |  |
| `architecture-authoring` | `sibling-estimate-document` | 0.2.1 | plugin skill |  |
| `architecture-authoring` | `stricter-ai-language-hygiene` | 1.1.1 | shared copy |  |
| `architecture-continuity` | `blunt-critique` | 0.2.0 | shared copy |  |
| `architecture-continuity` | `c4-diagram-package` | 0.1.1 | plugin skill | yes |
| `architecture-continuity` | `closure-extraction-handoff` | 0.1.1 | plugin skill | yes |
| `architecture-continuity` | `semantic-versioning` | 0.2.0 | shared copy |  |
| `architecture-continuity` | `stricter-ai-language-hygiene` | 1.1.1 | shared copy |  |
| `tech-lead-toolkit` | `atlassian-review-comment` | 0.1.1 | plugin skill | yes |
| `tech-lead-toolkit` | `blunt-critique` | 0.2.0 | shared copy |  |
| `tech-lead-toolkit` | `semantic-versioning` | 0.2.0 | shared copy |  |
| `tech-lead-toolkit` | `session-executive-report` | 0.1.1 | plugin skill | yes |
| `tech-lead-toolkit` | `story-and-gherkin-drafting` | 0.1.1 | plugin skill | yes |
| `tech-lead-toolkit` | `stricter-ai-language-hygiene` | 1.1.1 | shared copy |  |
| `tech-lead-toolkit` | `ticket-decision-record` | 0.1.1 | plugin skill | yes |
| `tech-lead-toolkit` | `ticket-readiness-critique` | 0.1.1 | plugin skill | yes |

### Shared skills

| Skill | Version | Copies | Also standalone |
|---|---|---|---|
| `blunt-critique` | 0.2.0 | 3 | yes |
| `semantic-versioning` | 0.2.0 | 3 | yes |
| `stricter-ai-language-hygiene` | 1.1.1 | 3 | yes |
<!-- index:end -->

## Layout

| Path | Holds |
|---|---|
| `plugins/<name>/` | Each plugin exactly as it installs, with its copies of shared material |
| `shared/skills/` | The canonical source of every skill that more than one plugin carries |
| `shared/substrates/` | The canonical source of every reference file that a family of skills shares |
| `tools/` | `validate.py`, `sync.py`, `index.py`, `build.py`, `check.py`, the hook, and `shared.json`, which maps each shared source to its copies and lists every skill also built as a standalone `.skill` |
| `tests/<name>/` | Repository-level tests, one folder per subject, each with a `run.py` |
| `docs/` | Repository guides; `docs/evals.md` defines the evaluation format and the open trigger collisions |
| `.claude-plugin/marketplace.json` | The marketplace manifest |
| `dist/` | Build output, ignored by git |

## Working on it

```
git config core.hooksPath tools/hooks     # once per clone
python tools/check.py                     # every check, as the hook runs them
python tools/sync.py --write              # after editing anything under shared/
python tools/build.py                     # dist/<plugin>-<version>.plugin and dist/skills/*.skill
```

Conventions for every change, including how to add a plugin, are in `CLAUDE.md`. The tools need Python 3.9 or later and nothing outside the standard library; PyYAML is used for frontmatter parsing when installed.

## Install

```
claude plugin marketplace add <path or URL of this repository>
claude plugin install <plugin>@provocative-plugins
```

For claude.ai, upload a `dist/<plugin>-<version>.plugin`, or a standalone `.skill` from `dist/skills/`.
