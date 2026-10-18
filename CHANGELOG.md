# Changelog

Repository tooling and layout. Each plugin keeps its own release history in `plugins/<name>/CHANGELOG.md`.

## Unreleased

### Added
- Marketplace `provocative-plugins` and the repository layout: `plugins/`, `shared/skills/`, `shared/substrates/`, `tools/`, `tests/`.
- `tools/validate.py`, `sync.py`, `index.py`, `build.py`, `check.py`, and a pre-commit hook. Plugins, tests and shared material are discovered or declared in data, so the tools need no edit when a plugin is added.
- Smoke tests for the `architecture-continuity` audit scripts.
- Evaluation sets for every skill, including the three shared skills, with a measured trigger run for `diagram-assets` and `c4-diagram-package`.

### Changed
- Marketplace owner gains the contact address `ronaldo@provocative.one`.
