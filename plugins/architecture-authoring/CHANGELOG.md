# Changelog

## [0.2.1] - 2026-10-18

### Changed
- `stricter-ai-language-hygiene` moves to 1.1.1: the origin note and the client-, city- and framework-specific examples are replaced with neutral ones. No rule, trigger or output format changes.
- `blunt-critique` and `semantic-versioning` now declare `metadata.version` 0.2.0 in their frontmatter. Their text is unchanged.

## [0.2.0] - 2026-10-04

### Added
- `diagram-assets` skill, with `diagram_tools.py` (`brief`, `check`) and the house-style reference.
- Asset register check in `audit.py`: a row marked Built needs its SVG and brief, every SVG needs a row, and every cited asset ID needs a row.
- `diagram_palette` configuration key.
- Fixture: a brief for the unbuilt container view, a thirteenth planted defect, and three planted SVG defects for the acceptance check.

### Changed
- Shared substrate: Part B.6 routes diagram work to `diagram-assets`; the supersession list gains a row for diagram briefs. Every workflow skill carrying the substrate moves to 0.2.0.

## [0.1.0] - 2026-10-04

### Added
- Six workflow skills: `evidence-and-registers`, `arc42-architecture-document`, `sibling-estimate-document`, `architecture-set-audit`, `client-facing-derivations`, `agent-division-of-labor`.
- Embedded skills: `blunt-critique`, `semantic-versioning`, `stricter-ai-language-hygiene`, verbatim from their sources.
- The Heritage Hub fixture and its regression run.
