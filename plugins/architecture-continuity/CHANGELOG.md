# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and this plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-10-18

### Added
- `blunt-critique` and `semantic-versioning` declare `metadata.version` 0.2.0. Their text is unchanged.

### Changed
- `metadata.version` is written as a quoted string in every skill, so an installed copy is byte-equal to its source. Each skill moves one PATCH, which is why the plugin has to be reinstalled: `c4-diagram-package` and `closure-extraction-handoff` each to 0.1.1.
- `stricter-ai-language-hygiene` moves to 1.1.1. The origin note and the client-, city- and framework-specific examples are replaced with neutral ones. No rule, trigger or output format changes.

## [0.1.0] - 2026-10-02

### Added
- Workflow skills: `c4-diagram-package`, with `scripts/audit_c4_package.py`, and `closure-extraction-handoff`, with `scripts/audit_pack.py`, each carrying `references/shared-substrate.md`.
- Embedded skills: `blunt-critique`, `semantic-versioning`, `stricter-ai-language-hygiene`, verbatim from their sources.

[Unreleased]: https://github.com/Provocative-one/provocative-plugins/compare/architecture-continuity-v0.1.1...HEAD
[0.1.1]: https://github.com/Provocative-one/provocative-plugins/compare/architecture-continuity-v0.1.0...architecture-continuity-v0.1.1
[0.1.0]: https://github.com/Provocative-one/provocative-plugins/releases/tag/architecture-continuity-v0.1.0
