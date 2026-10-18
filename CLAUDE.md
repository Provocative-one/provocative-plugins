# CLAUDE.md

This file governs every edit in this repository.

## Shared material

A plugin must install on its own, so it carries a committed copy of every shared skill and shared reference file it uses. Copies are never edited in place. Edit the source under `shared/`, run `python tools/sync.py --write`, and commit the source and every copy together. `tools/shared.json` maps each source to its copies; a plugin that starts carrying shared material is added there in the same commit.

Shared skills are maintained here like any other skill: their source under `shared/skills/` is canonical, and they carry their own `metadata.version`.

## Versions

Every change is classified with the `semantic-versioning` skill. The consumers of a plugin are the people and prompts that depend on its skill names, triggers, conventions, script interfaces and output formats.

- A skill's version lives in `metadata.version` of its frontmatter. A plugin's version lives in its `.claude-plugin/plugin.json`.
- A change to a skill bumps that skill and every plugin that ships it, in the same commit. A change to a shared source bumps the source, and every plugin that carries a copy.
- First versions are 0.1.0.
- Each plugin release has an entry in that plugin's `CHANGELOG.md` and a tag `<plugin>-v<x.y.z>` on the commit that sets the version. A shared skill released on its own is tagged `shared/<skill>-v<x.y.z>`.
- `evals/` folders are test assets. No artifact ships them, so adding or changing evals bumps nothing.

## Frontmatter

Fields stay within the open Agent Skills standard: `name`, `description`, `compatibility`, `metadata`, `license` and `allowed-tools`. Skills that ship scripts declare `allowed-tools`. `tools/validate.py` enforces the field rules.

## Adding a plugin

1. Create `plugins/<name>/.claude-plugin/plugin.json` with version 0.1.0, and its skills under `plugins/<name>/skills/`.
2. List it in `.claude-plugin/marketplace.json` with source `./plugins/<name>`; `validate.py` fails until the two agree.
3. Copy any shared material it carries with `sync.py --write`, after adding the copies to `tools/shared.json`.
4. Give each skill an `evals/evals.json` in the format of `docs/evals.md`.
5. Put a fixture regression at `plugins/<name>/fixture/run_regression.py`, or repository tests at `tests/<name>/run.py`; `check.py` discovers both.
6. Add `plugins/<name>/CHANGELOG.md`, run `python tools/check.py`, commit, and tag `<name>-v0.1.0`.

## Before every commit

The hook regenerates the README index and runs `python tools/check.py`. A commit that fails it does not go in. Prose in skills, READMEs, changelogs and commit messages follows `stricter-ai-language-hygiene`.

## Never

- Commit `dist/`, `__pycache__/`, or `HANDOFF.md`.
- Push, tag a remote, or change remote access without the maintainer's explicit instruction.
- Rewrite a released version: a correction after a release is a new version.
