#!/usr/bin/env python3
"""Register and set tools for an arc42 document set.

    register_tools.py scaffold --root DIR --system NAME --client NAME --prefix XYZ --author "Given Surname, Org"
        Create a new set: both living documents with registers opened empty, README, CLAUDE.md,
        CHANGELOG.md, .gitignore, the directory taxonomy, and tools/ with the audit and its config.

    register_tools.py next --root DIR --series A
        Print the next free ID in a series. Numbers are never reused, so the next ID follows
        the highest ever registered, closed and withdrawn rows included.

    register_tools.py cites --root DIR --id A-07
        List every citation of an ID across the set, with file and line.

    register_tools.py project --root DIR --series EA [--trace]
        Print the client-facing projection of a register: plain sentences, no identifiers,
        terminal rows left out. --trace adds the source table a derivative's brief needs.

Reads tools/audit-config.json for document paths and series ownership.
"""
import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE.parent / "assets" / "templates"
AUDIT = HERE.parent.parent / "architecture-set-audit" / "scripts" / "audit.py"
TERMINAL = ("closed", "withdrawn", "superseded", "retired")


def load(root):
    cfg = json.loads((root / "tools" / "audit-config.json").read_text(encoding="utf-8"))
    docs = {role: (root / rel) for role, rel in cfg["documents"].items()}
    return cfg, docs


def register_rows(text, series):
    rows, header, in_register = [], None, False
    for line in text.split("\n"):
        if not line.startswith("|"):
            in_register, header = False, None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] == "ID":
            in_register, header = True, cells
            continue
        if in_register and re.match(r"^`?\[%s-\d\d\]`?$" % re.escape(series), cells[0]):
            rows.append(dict(zip(header, cells)))
    return rows


def scaffold(a):
    root = Path(a.root)
    if root.exists() and any(root.iterdir()):
        sys.exit(f"{root} exists and is not empty")
    today = datetime.date.today()
    subs = {"{{SYSTEM}}": a.system, "{{CLIENT}}": a.client, "{{PREFIX}}": a.prefix.upper(),
            "{{prefix}}": a.prefix.lower(), "{{AUTHOR}}": a.author,
            "{{DATE}}": f"{today.day} {today.strftime('%B %Y')}", "{{ISODATE}}": today.isoformat()}

    def render(name):
        t = (TEMPLATES / name).read_text(encoding="utf-8")
        for k, v in subs.items():
            t = t.replace(k, v)
        return t

    p = a.prefix.lower()
    for d in ("arc42/assets", "briefs", "external-docs", "generated", "published", "tools"):
        (root / d).mkdir(parents=True, exist_ok=True)
    for keep in ("arc42/assets", "briefs", "external-docs", "generated", "published"):
        (root / keep / ".gitkeep").touch()
    files = {
        f"arc42/{p}-architecture-arc42.md": "architecture.md",
        f"arc42/{p}-estimate-arc42.md": "estimate.md",
        "README.md": "README.md", "CLAUDE.md": "CLAUDE.md", "CHANGELOG.md": "CHANGELOG.md",
        ".gitignore": "gitignore", "tools/audit-config.json": "audit-config.json",
    }
    for dest, src in files.items():
        (root / dest).write_text(render(src), encoding="utf-8")
    shutil.copy(AUDIT, root / "tools" / "audit.py")
    print(f"Scaffolded {a.system} at {root}. Fill every '<fill: ...>' slot, then run:")
    print(f"  python3 {root / 'tools' / 'audit.py'} --root {root}")


def next_id(a):
    root = Path(a.root)
    cfg, docs = load(root)
    owner = cfg["series"].get(a.series)
    if not owner:
        sys.exit(f"unknown series {a.series}; declare it in tools/audit-config.json and the notation key first")
    text = docs[owner].read_text(encoding="utf-8")
    nums = [int(n) for n in re.findall(r"\[%s-(\d\d)\]" % re.escape(a.series), text)]
    n = max(nums, default=0) + 1
    if n > 99:
        sys.exit("series exhausted at 99; a third digit changes the grammar and is a MAJOR decision")
    print(f"[{a.series}-{n:02d}]")


def cites(a):
    root = Path(a.root)
    cfg, docs = load(root)
    rid = a.id.strip("[]`")
    paths = list(docs.values()) + [root / f for f in cfg.get("also_read", [])] + sorted((root / "briefs").glob("*.md"))
    for p in paths:
        if not p.exists():
            continue
        for n, line in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
            if f"[{rid}]" in line:
                print(f"{p.relative_to(root)}:{n}: {line.strip()[:120]}")


def project(a):
    root = Path(a.root)
    cfg, docs = load(root)
    owner = cfg["series"].get(a.series)
    if not owner:
        sys.exit(f"unknown series {a.series}")
    rows = register_rows(docs[owner].read_text(encoding="utf-8"), a.series)
    ref = r"`?\[[A-Z]+-\d\d\]`?"
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"\s*(?:[,;]\s*)?(?:converting|per|see|of|in|by)?\s*" + ref, "", s)).strip(" ,;")
    trace = []
    for r in rows:
        cells = " ".join(r.values()).lower()
        if any(t in cells for t in TERMINAL):
            continue
        rid = r["ID"].strip("`[]")
        statement = strip(r.get("Assumption") or r.get("Entry") or r.get("Risk") or r.get("Decision") or "")
        figure = strip(r.get("Figure or condition", ""))
        consequence = strip(r.get("If false") or r.get("Consequence") or "")
        line = statement.rstrip(".") + (f" ({figure})" if figure else "") + "."
        if consequence:
            line += f" If this does not hold: {consequence}".rstrip(".") + "."
        print(f"- {line}")
        trace.append((line, f"{owner} [{rid}]"))
    if a.trace:
        print("\n| Projected item | Source |\n|---|---|")
        for line, src in trace:
            print(f"| {line[:60]}{'...' if len(line) > 60 else ''} | {src} |")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scaffold")
    for k in ("root", "system", "client", "prefix", "author"):
        s.add_argument(f"--{k}", required=True)
    n = sub.add_parser("next")
    n.add_argument("--root", default=".")
    n.add_argument("--series", required=True)
    c = sub.add_parser("cites")
    c.add_argument("--root", default=".")
    c.add_argument("--id", required=True)
    p = sub.add_parser("project")
    p.add_argument("--root", default=".")
    p.add_argument("--series", required=True)
    p.add_argument("--trace", action="store_true")
    a = ap.parse_args()
    {"scaffold": scaffold, "next": next_id, "cites": cites, "project": project}[a.cmd](a)


if __name__ == "__main__":
    main()
