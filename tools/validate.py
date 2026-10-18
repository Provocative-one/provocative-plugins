#!/usr/bin/env python3
"""Validate every skill's frontmatter against the open Agent Skills fields.

Rules follow the skill-creator validator: allowed keys name, description, license,
allowed-tools, metadata, compatibility; kebab-case name of at most 64 characters that
matches its folder; description of at most 1024 characters with no angle brackets;
compatibility of at most 500 characters; exactly one SKILL.md per skill. Also checks
that every plugin.json carries a semantic version and that the marketplace lists exactly
the plugins under plugins/, and warns when a skill has no metadata.version. Exit 1 on
any failure.
"""
import re
import sys
import json
from common import ROOT, PLUGINS, SHARED, plugin_names, plugin_manifest, skills_of, frontmatter, shared_copy_dirs

ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
fails, warns = [], []


def check_skill(path, label):
    nested = [p for p in path.rglob("SKILL.md") if p != path / "SKILL.md"
              and not any(x in ("evals", "__pycache__") for x in p.relative_to(path).parts)]
    if nested:
        fails.append(f"{label}: extra SKILL.md files {[str(p.relative_to(path)) for p in nested]}")
    fm, err = frontmatter(path / "SKILL.md")
    if err:
        fails.append(f"{label}: {err}")
        return
    extra = set(fm) - ALLOWED
    if extra:
        fails.append(f"{label}: keys outside the open standard {sorted(extra)}")
    name = str(fm.get("name", "")).strip()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        fails.append(f"{label}: invalid name '{name}'")
    if name != path.name:
        fails.append(f"{label}: name '{name}' differs from folder '{path.name}'")
    desc = str(fm.get("description", "")).strip()
    if not desc:
        fails.append(f"{label}: missing description")
    if "<" in desc or ">" in desc:
        fails.append(f"{label}: angle brackets in description")
    if len(desc) > 1024:
        fails.append(f"{label}: description {len(desc)} characters, limit 1024")
    comp = fm.get("compatibility")
    if comp is not None and (not isinstance(comp, str) or len(comp) > 500):
        fails.append(f"{label}: compatibility must be a string of at most 500 characters")
    meta = fm.get("metadata") or {}
    ver = str(meta.get("version", "")) if isinstance(meta, dict) else ""
    if not SEMVER.match(ver):
        warns.append(f"{label}: no semantic metadata.version")


def main():
    copies = shared_copy_dirs()
    for p in plugin_names():
        v = str(plugin_manifest(p).get("version", ""))
        if not SEMVER.match(v):
            fails.append(f"plugins/{p}: plugin.json version '{v}' is not semantic")
        for s in skills_of(p):
            if s.resolve() in copies:
                continue  # a copy of a shared skill: validated at its source, kept equal by sync.py
            check_skill(s, f"plugins/{p}/skills/{s.name}")
    if (SHARED / "skills").exists():
        for e in sorted((SHARED / "skills").iterdir()):
            check_skill(e, f"shared/skills/{e.name}")
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    listed = {e["name"]: e.get("source", "") for e in market.get("plugins", [])}
    for p in plugin_names():
        if p not in listed:
            fails.append(f"marketplace: plugins/{p} is not listed")
        elif listed[p].rstrip("/") != f"./plugins/{p}":
            fails.append(f"marketplace: {p} has source '{listed[p]}', expected './plugins/{p}'")
    for name in sorted(set(listed) - set(plugin_names())):
        fails.append(f"marketplace: lists '{name}', which has no folder under plugins/")
    for w in warns:
        print("WARN ", w)
    for f in fails:
        print("FAIL ", f)
    print(f"validate: {len(fails)} FAIL, {len(warns)} WARN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
