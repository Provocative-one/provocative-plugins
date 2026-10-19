#!/usr/bin/env python3
"""Build the installable artifacts into dist/, or verify the tree against delivered artifacts.

    python tools/build.py                 # dist/<plugin>-<version>.plugin and dist/skills/<skill>[-<version>].skill
    python tools/build.py --verify DIR    # compare plugins/ and standalone skills with every .plugin
                                          # and .skill file found under DIR, file by file

evals/ folders are repository test assets: no artifact carries them, and verification
ignores them on both sides. A .plugin is a plugin folder zipped from its root; a .skill is
one skill folder zipped with the folder as its top-level entry. Zip bytes differ between
builds (timestamps), so verification compares file names and contents.
"""
import argparse
import hashlib
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from common import ROOT, PLUGINS, plugin_names, plugin_manifest, frontmatter, load_shared, files_of

DIST = ROOT / "dist"


def skill_version(path):
    fm, _ = frontmatter(path / "SKILL.md")
    meta = (fm or {}).get("metadata") or {}
    return str(meta.get("version", "")) if isinstance(meta, dict) else ""


def without_evals(directory, rels):
    return [r for r in rels if "evals" not in r.parts[:-1] or not _under_skill_evals(directory, r)]


def _under_skill_evals(directory, rel):
    """True when rel sits inside an evals/ folder that belongs to a skill (a sibling of SKILL.md)."""
    parts = rel.parts
    for i, part in enumerate(parts[:-1]):
        if part == "evals" and (Path(directory, *parts[:i]) / "SKILL.md").exists():
            return True
    return False


def artifact_files(directory):
    return without_evals(directory, files_of(directory))


def zip_dir(src, dest, arc_prefix=""):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in artifact_files(src):
            z.write(src / rel, str(Path(arc_prefix) / rel) if arc_prefix else str(rel))


def build():
    for p in plugin_names():
        v = plugin_manifest(p)["version"]
        zip_dir(PLUGINS / p, DIST / f"{p}-{v}.plugin")
        print(f"built dist/{p}-{v}.plugin")
    for rel in load_shared()["standalone"]:
        src = ROOT / rel
        v = skill_version(src)
        name = f"{src.name}-{v}.skill" if v else f"{src.name}.skill"
        zip_dir(src, DIST / "skills" / name, arc_prefix=src.name)
        print(f"built dist/skills/{name}")


def hashes(directory):
    return {str(r): hashlib.sha256((directory / r).read_bytes()).hexdigest() for r in artifact_files(directory)}


def compare(label, a, b):
    ha, hb = hashes(a), hashes(b)
    diff = sorted(set(ha) ^ set(hb)) + sorted(k for k in ha.keys() & hb.keys() if ha[k] != hb[k])
    print(f"{'ok  ' if not diff else 'DIFF'} {label}" + (f": {diff[:6]}" if diff else ""))
    return not diff


def verify(shipped):
    shipped, ok = Path(shipped), True
    standalone = {Path(r).name: ROOT / r for r in load_shared()["standalone"]}
    with tempfile.TemporaryDirectory() as tmp:
        for art in sorted(shipped.rglob("*.plugin")):
            name = re.sub(r"-\d+\.\d+\.\d+$", "", art.stem)
            out = Path(tmp) / "p" / name
            zipfile.ZipFile(art).extractall(out)
            if not (PLUGINS / name).exists():
                print(f"DIFF {art.name}: no plugins/{name}")
                ok = False
                continue
            ok &= compare(f"{art.name} against plugins/{name}", out, PLUGINS / name)
        for art in sorted(shipped.rglob("*.skill")):
            name = re.sub(r"-\d+\.\d+\.\d+$", "", art.stem)
            if name not in standalone:
                print(f"DIFF {art.name}: not listed as standalone in tools/shared.json")
                ok = False
                continue
            out = Path(tmp) / "s" / art.stem
            zipfile.ZipFile(art).extractall(out)
            ok &= compare(f"{art.name} against {standalone[name].relative_to(ROOT)}", out / name, standalone[name])
    print("verify: " + ("tree matches every artifact" if ok else "differences found"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", metavar="DIR")
    a = ap.parse_args()
    if a.verify:
        return verify(a.verify)
    build()
    return 0


if __name__ == "__main__":
    sys.exit(main())
