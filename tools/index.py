#!/usr/bin/env python3
"""Regenerate the plugin and skill index inside README.md, between the index markers.

The index is built from each plugin's manifest and each skill's frontmatter, so adding a
plugin needs no edit here.

    python tools/index.py --write   # rewrite the index (the pre-commit hook does this)
    python tools/index.py --check   # exit 1 if the README index is stale
"""
import argparse
import sys
from common import ROOT, plugin_names, plugin_manifest, skills_of, frontmatter, load_shared, shared_copy_dirs

START, END = "<!-- index:start -->", "<!-- index:end -->"


def version_of(skill):
    fm, _ = frontmatter(skill / "SKILL.md")
    meta = (fm or {}).get("metadata") or {}
    return str(meta.get("version", "")) if isinstance(meta, dict) else ""


def render():
    standalone = set(load_shared()["standalone"])
    copies = shared_copy_dirs()
    out = ["### Plugins", "", "| Plugin | Version | Description |", "|---|---|---|"]
    for p in plugin_names():
        m = plugin_manifest(p)
        out.append(f"| `{p}` | {m['version']} | {m.get('description', '')} |")
    out += ["", "### Skills", "", "| Plugin | Skill | Version | Kind | Also standalone |", "|---|---|---|---|---|"]
    for p in plugin_names():
        for s in skills_of(p):
            kind = "shared copy" if s.resolve() in copies else "plugin skill"
            rel = f"plugins/{p}/skills/{s.name}"
            out.append(f"| `{p}` | `{s.name}` | {version_of(s) or 'none declared'} | {kind} | {'yes' if rel in standalone else ''} |")
    shared_skills = sorted((ROOT / "shared" / "skills").iterdir()) if (ROOT / "shared" / "skills").exists() else []
    if shared_skills:
        out += ["", "### Shared skills", "", "| Skill | Version | Copies | Also standalone |", "|---|---|---|---|"]
        for s in shared_skills:
            n = sum(1 for c in copies if c.name == s.name)
            out.append(f"| `{s.name}` | {version_of(s) or 'none declared'} | {n} | {'yes' if f'shared/skills/{s.name}' in standalone else ''} |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    a = ap.parse_args()
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("index: README.md lacks the index markers")
        return 1
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{render()}\n{END}{tail}"
    if a.write:
        if new != text:
            readme.write_text(new, encoding="utf-8")
            print("index: README.md updated")
        return 0
    stale = new != text
    print("index: stale, run python tools/index.py --write" if stale else "index: current")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
