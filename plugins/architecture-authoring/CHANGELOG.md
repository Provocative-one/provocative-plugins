# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and this plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-10-19

### Added
- `agent-division-of-labor` 0.3.0 gains a second handoff mode. In working-log mode, a repository that carries a working-log under the Corponomia specification closes a unit for each episode of work and advances one pointer per surface, in place of `HANDOFF.md`. A line of `CLAUDE.md` declares the mode.
- `references/working-log-mode.md` in that skill: a digest of Sections 6, 10.9 and 10.10 of the specification (unit anatomy, composite identifiers, central register, pointers, awareness unit).

### Changed
- Setup offers working-log mode once and records the answer. Fallback mode, which writes the untracked `HANDOFF.md`, stays the default, so a repository without a declaration behaves as before.

## [0.2.1] - 2026-10-18

### Added
- `blunt-critique` and `semantic-versioning` declare `metadata.version` 0.2.0. Their text is unchanged.

### Changed
- `metadata.version` is written as a quoted string in every skill, so an installed copy is byte-equal to its source. Each skill moves one PATCH, which is why the plugin has to be reinstalled: `agent-division-of-labor`, `arc42-architecture-document`, `architecture-set-audit`, `client-facing-derivations`, `evidence-and-registers` and `sibling-estimate-document` each to 0.2.1, and `diagram-assets` to 0.1.1.
- `stricter-ai-language-hygiene` moves to 1.1.1. The origin note and the client-, city- and framework-specific examples are replaced with neutral ones. No rule, trigger or output format changes.

## [0.2.0] - 2026-10-04

### Added
- `diagram-assets` skill, with `diagram_tools.py` (`brief`, `check`) and the house-style reference.
- Asset register check in `audit.py`: a row marked Built needs its SVG and brief, every SVG needs a row, and every cited asset ID needs a row.
- `diagram_palette` configuration key.
- Fixture: a brief for the unbuilt container view, a thirteenth planted defect, and three planted SVG defects for the acceptance check.

### Changed
- Shared substrate: Part B.6 routes diagram work to `diagram-assets`; the supersession list gains a row for diagram briefs. Every workflow skill carrying the substrate moves to 0.2.0.

## 0.1.0 - 2026-10-04

### Added
- Six workflow skills: `evidence-and-registers`, `arc42-architecture-document`, `sibling-estimate-document`, `architecture-set-audit`, `client-facing-derivations`, `agent-division-of-labor`.
- Embedded skills: `blunt-critique`, `semantic-versioning`, `stricter-ai-language-hygiene`, verbatim from their sources.
- The Heritage Hub fixture and its regression run.

[Unreleased]: https://github.com/Provocative-one/provocative-plugins/compare/architecture-authoring-v0.3.0...HEAD
[0.3.0]: https://github.com/Provocative-one/provocative-plugins/compare/architecture-authoring-v0.2.1...architecture-authoring-v0.3.0
[0.2.1]: https://github.com/Provocative-one/provocative-plugins/compare/architecture-authoring-v0.2.0...architecture-authoring-v0.2.1
[0.2.0]: https://github.com/Provocative-one/provocative-plugins/releases/tag/architecture-authoring-v0.2.0
