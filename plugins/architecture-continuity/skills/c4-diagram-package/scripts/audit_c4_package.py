#!/usr/bin/env python3
"""Mechanical audit of a C4 diagram package (Mermaid sources plus companions).

Usage: python3 audit_c4_package.py <package_dir> [--max-nodes 20]

Finds *.mmd and *.companion.md files recursively and pairs them by basename.
Exit code 1 when any FAIL is reported. WARN items need judgment, not automation.
"""
import re, sys, argparse
from pathlib import Path

STATES = ["focus", "present", "sunsetting", "planned", "parked", "superseded"]
GLYPH_CLASS = [("◇", "planned"), ("◐", "planned"), ("⟢", "sunsetting"), ("⏸", "parked"), ("✕", "superseded")]
WORD_CLASS = [("PLANNED", "planned"), ("PARTIAL", "planned"), ("SUNSETTING", "sunsetting"),
              ("PARKED", "parked"), ("SUPERSEDED", "superseded")]
REQUIRED_SECTIONS = ["Executive Summary", "Diagram", "Walkthrough", "References"]
NODE_RE = re.compile(r'^\s*(?!subgraph\b)(?!classDef\b)(?!direction\b)(?!end\b)([A-Za-z_]\w*)\s*(\[\[|\(\[|\[|\(\(|\(|\{\{|\{)')

fails, warns, infos = [], [], []
def fail(m): fails.append(m)
def warn(m): warns.append(m)
def info(m): infos.append(m)

def norm(text):
    """Drop %% comments and blank lines, strip trailing whitespace."""
    out = []
    for l in text.split("\n"):
        if l.lstrip().startswith("%%") or not l.strip():
            continue
        out.append(l.rstrip())
    return out

def audit_mmd(path, max_nodes, ref_classdefs):
    s = path.read_text(encoding="utf-8")
    lines = s.split("\n")
    name = path.name
    title = lines[0] if lines else ""
    if not title.startswith("%%"):
        warn(f"{name}: first line is not a %% title comment")
    bad = sorted({c for c in title if ord(c) > 127})
    if bad:
        warn(f"{name}: non-ASCII characters in title line {bad}; the Lucid importer transliterates dashes and may mangle others")
    if "State grammar:" not in s:
        warn(f"{name}: no 'State grammar:' header comment")
    if "Canonical source" not in s:
        warn(f"{name}: no 'Canonical source' header comment")
    defs = dict(re.findall(r'classDef\s+(\w+)\s+([^\n]+)', s))
    missing = [c for c in STATES if c not in defs]
    if missing:
        fail(f"{name}: classDef missing for {missing} (the grammar is declared in full in every diagram)")
    if ref_classdefs is not None:
        for c in STATES:
            if c in defs and c in ref_classdefs and defs[c].strip() != ref_classdefs[c].strip():
                warn(f"{name}: classDef '{c}' differs from the first diagram's definition (grammar drift)")
    nodes, used, node_lines = [], [], []
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("%%"):
            continue
        m = NODE_RE.match(l)
        if not m:
            continue
        nid = m.group(1)
        cm = re.search(r':::(\w+)', l)
        nodes.append(nid)
        if not cm:
            fail(f"{name}:{i}: node '{nid}' has no state class (:::state)")
            continue
        cls = cm.group(1)
        used.append(cls)
        if cls not in STATES:
            fail(f"{name}:{i}: node '{nid}' uses unknown state class '{cls}'")
            continue
        for g, c in GLYPH_CLASS:
            if g in l and cls != c:
                warn(f"{name}:{i}: node '{nid}' carries glyph {g} but class is '{cls}' (expected '{c}'); fine only if the glyph annotates a sub-part named in the label")
        for w, c in WORD_CLASS:
            if w in l and cls != c:
                warn(f"{name}:{i}: node '{nid}' says {w} but class is '{cls}' (expected '{c}'); fine only if the word annotates a sub-part named in the label")
        node_lines.append((i, nid, cls, l))
    # Monochrome survival: a withdrawn or deferred state must be readable without color.
    # A slice drawn entirely in one state needs the glyph once (title, note, or subgraph); a mixed diagram needs it per node.
    for state in ("sunsetting", "parked", "superseded"):
        glyph = next(g for g, c in GLYPH_CLASS if c == state)
        members = [(i, nid, l) for i, nid, cls, l in node_lines if cls == state]
        if not members:
            continue
        if set(used) == {state}:
            if glyph not in s:
                warn(f"{name}: whole slice is {state} but the glyph {glyph} appears nowhere; the state would vanish in monochrome print")
        else:
            for i, nid, l in members:
                if glyph not in l:
                    warn(f"{name}:{i}: node '{nid}' is {state} but carries no glyph {glyph}; the state would vanish in monochrome print")
    if len(nodes) > max_nodes:
        warn(f"{name}: {len(nodes)} nodes exceeds {max_nodes}; consider splitting into slices")
    head = "\n".join(l for l in lines if l.startswith("%%"))
    m = re.search(r'State grammar:([^\n]*)', head)
    if m:
        listed = m.group(1).lower()
        for c in sorted(set(used)):
            if c not in listed and not (c == "planned" and "partial" in listed):
                warn(f"{name}: state '{c}' is used but not listed in the 'State grammar:' comment")
    info(f"{name}: {len(nodes)} nodes, states used: " + ", ".join(sorted(set(used))))
    return s, defs

def audit_companion(path, mmd_text):
    s = path.read_text(encoding="utf-8")
    name = path.name
    heads = [h.strip() for h in re.findall(r'^##\s+(.+)$', s, flags=re.M)]
    pos = [heads.index(x) if x in heads else -1 for x in REQUIRED_SECTIONS]
    if -1 in pos:
        fail(f"{name}: missing section(s) {[x for x, p in zip(REQUIRED_SECTIONS, pos) if p == -1]}")
    elif pos != sorted(pos):
        fail(f"{name}: sections out of order; expected {REQUIRED_SECTIONS}, found {heads}")
    if "Scope note" not in s:
        warn(f"{name}: no 'Scope note' line in the header (exclusions held off-canvas must name their driver)")
    m = re.search(r"```mermaid\n(.*?)```", s, flags=re.S)
    if not m:
        fail(f"{name}: no embedded mermaid block")
    elif mmd_text is not None and norm(m.group(1)) != norm(mmd_text):
        fail(f"{name}: embedded diagram differs from the .mmd (the .mmd is the source of record)")
    refs = re.split(r'^##\s+References\s*$', s, flags=re.M)
    if len(refs) > 1:
        body = refs[1]
        if not re.search(r'https?://', body):
            warn(f"{name}: References section has no live link")
        for t in re.findall(r'\]\(([^)]*)\)', body):
            if t.strip() in ("", "#", "about:blank"):
                fail(f"{name}: empty or placeholder link target in References")
    for t in re.findall(r'\]\(([^)#]+\.(?:mmd|md))\)', s):
        if not t.startswith("http") and not (path.parent / t).resolve().exists():
            warn(f"{name}: relative link target not found: {t}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("package_dir")
    ap.add_argument("--max-nodes", type=int, default=20)
    a = ap.parse_args()
    root = Path(a.package_dir)
    mmds = {p.stem: p for p in root.rglob("*.mmd")}
    comps = {p.name[:-len(".companion.md")]: p for p in root.rglob("*.companion.md")}
    if not mmds:
        print("FAIL: no .mmd files found")
        sys.exit(1)
    for k in sorted(set(mmds) - set(comps)): fail(f"{k}: .mmd has no companion")
    for k in sorted(set(comps) - set(mmds)): fail(f"{k}: companion has no .mmd")
    ref_defs = None
    for k in sorted(mmds):
        s, defs = audit_mmd(mmds[k], a.max_nodes, ref_defs)
        if ref_defs is None:
            ref_defs = defs
        if k in comps:
            audit_companion(comps[k], s)
    readmes = list(root.rglob("00-README.md")) + list(root.rglob("README.md"))
    if readmes:
        r = readmes[0].read_text(encoding="utf-8")
        words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                 "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
        m = re.search(r'\b(\d+|' + "|".join(words) + r')\s+diagrams\b', r, flags=re.I)
        if m:
            n = int(m.group(1)) if m.group(1).isdigit() else words[m.group(1).lower()]
            if n != len(mmds):
                fail(f"README states {n} diagrams; found {len(mmds)}")
        for k in mmds:
            if k not in r:
                warn(f"README does not mention {k}")
    else:
        warn("no README found")
    for l in infos: print("INFO ", l)
    for l in warns: print("WARN ", l)
    for l in fails: print("FAIL ", l)
    print(f"\n{len(mmds)} diagrams | {len(fails)} FAIL | {len(warns)} WARN")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
