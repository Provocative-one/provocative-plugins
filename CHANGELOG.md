# Changelog

Repository tooling and layout. Each plugin keeps its own release history in `plugins/<name>/CHANGELOG.md`.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).

## Unreleased

### Added
- Marketplace `provocative-plugins` and the repository layout: `plugins/`, `shared/skills/`, `shared/substrates/`, `tools/`, `tests/`.
- `tools/validate.py`, `sync.py`, `index.py`, `build.py`, `check.py`, and a pre-commit hook. Plugins, tests and shared material are discovered or declared in data, so the tools need no edit when a plugin is added.
- Smoke tests for the `architecture-continuity` audit scripts.
- Evaluation sets for every skill, including the three shared skills, with a measured trigger run for `diagram-assets` and `c4-diagram-package`.

- `tools/commit_msg.py` and a `commit-msg` hook that require a Conventional Commit with What, Why and How paragraphs.
- `validate.py` fails a skill whose `metadata.version` is not a quoted string.

### Changed
- Marketplace owner gains the contact address `ronaldo@provocative.one`.
- `CLAUDE.md` documents the commit message convention, the quoted version string and the Keep a Changelog layout of the plugin changelogs.
