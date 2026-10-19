#!/usr/bin/env python3
"""Tools for diagram assets registered in an arc42 document set.

    diagram_tools.py brief --root DIR --id HHB-CNT-01
        Write briefs/<id>.md from the asset's register row, if no brief exists yet.
        The brief is written before the build and is what review runs against.

    diagram_tools.py check --root DIR --id HHB-CTX-01 [--client-facing] [--json]
        Acceptance run of arc42/assets/<id>.svg against briefs/<id>.md:
          svg        the file exists, sets a viewBox, keeps text as text, and loads nothing external
          brief      every element has a label and a source; the arrow kind is declared
          elements   every label in the brief is on the canvas, and nothing else is
          palette    every color is in the configured house palette (when one is configured)
          identifiers  no register reference, asset ID or marker on a client-facing canvas
        Exit status 1 on any FAIL.

Reads tools/audit-config.json for the project prefix, the documents and the palette.
Register-level coherence (a Built row without its file, a file without a row) is
checked by audit.py.
"""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

FINDINGS = []


def report(level, check, msg):
    FINDINGS.append({"level": level, "check": check, "message": msg})


def load_cfg(root):
    return json.loads((root / "tools" / "audit-config.json").read_text(encoding="utf-8"))


def norm_color(c):
    c = c.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return c


def norm_text(t):
    return re.sub(r"\s+", " ", t).strip()


def find_row(root, cfg, aid):
    for role, rel in cfg["documents"].items():
        text = (root / rel).read_text(encoding="utf-8")
        version = re.search(r"^\| Version \| (\d+\.\d+\.\d+) \|", text, re.M)
        for line in text.split("\n"):
            if re.match(r"^\|\s*`?\[%s\]`?\s*\|" % re.escape(aid), line):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                return role, version.group(1) if version else "?", cells
    return None, None, None


def brief(a):
    root = Path(a.root)
    cfg = load_cfg(root)
    aid = a.id.strip("[]`").upper()
    role, version, cells = find_row(root, cfg, aid)
    if not role:
        sys.exit(f"[{aid}] is in no asset register; register it first, in the document that uses it")
    path = root / "briefs" / f"{aid.lower()}.md"
    if path.exists():
        sys.exit(f"{path} exists; a brief is revised, never regenerated over")
    title = cells[1] if len(cells) > 1 else aid
    path.write_text(f"""# Brief: `[{aid}]` {title.lower()}

**Source:** {role} {version}. **Asset:** `arc42/assets/{aid.lower()}.svg`. **Status:** Not built. **Audience:** internal

## What the diagram must show

| Element | Label on canvas | Kind | Traces to |
|---|---|---|---|
| <fill: what the element is> | <fill: exact text on the canvas> | <fill: system, person, container, component, boundary, relationship> | <fill: register row or section> |

**Arrows:** <fill: dependencies, or data flow; never both on one canvas>

**Other text on canvas:** none

## Acceptance run

1. Every element above appears on the canvas, and nothing else.
2. Every arrow has a counterpart in the sections the elements trace to.
3. Text stays text, a viewBox is set, and nothing external is referenced.
4. No internal identifier appears on a client-facing canvas.
""", encoding="utf-8")
    print(f"wrote {path.relative_to(root)}; fill every '<fill: ...>' slot before building")


def parse_brief(path):
    text = path.read_text(encoding="utf-8")
    rows, in_table = [], False
    for line in text.split("\n"):
        if re.match(r"^\|\s*Element\s*\|\s*Label on canvas\s*\|", line):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
                continue
            if re.match(r"^\|[\s\-:|]+\|?\s*$", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(dict(zip(["element", "label", "kind", "traces"], cells)))
    arrows = re.search(r"\*\*Arrows:\*\*\s*([^\n]+)", text)
    other = re.search(r"\*\*Other text on canvas:\*\*\s*([^\n]+)", text)
    others = []
    if other and other.group(1).strip().lower() != "none":
        others = [norm_text(x) for x in other.group(1).split(";") if x.strip()]
    audience = re.search(r"\*\*Audience:\*\*\s*(\w+)", text)
    return rows, arrows.group(1).strip() if arrows else None, others, (audience.group(1).lower() if audience else "internal")


def check(a):
    root = Path(a.root)
    cfg = load_cfg(root)
    aid = a.id.strip("[]`").upper()
    svg_path = root / "arc42" / "assets" / f"{aid.lower()}.svg"
    brief_path = root / "briefs" / f"{aid.lower()}.md"
    if not brief_path.exists():
        report("FAIL", "brief", f"no brief at {brief_path.relative_to(root)}; the brief is written before the build")
        return
    rows, arrows, others, audience = parse_brief(brief_path)
    if not rows:
        report("FAIL", "brief", "the brief has no element table (| Element | Label on canvas | Kind | Traces to |)")
    for r in rows:
        if not r.get("label") or "<fill" in r.get("label", ""):
            report("FAIL", "brief", f"element '{r.get('element')}' has no label on canvas")
        if not r.get("traces") or "<fill" in r.get("traces", ""):
            report("FAIL", "brief", f"element '{r.get('element')}' traces to no register row or section")
    if not arrows or "<fill" in arrows:
        report("FAIL", "brief", "the brief does not declare the arrow kind (dependencies or data flow)")
    elif "depend" in arrows.lower() and "flow" in arrows.lower():
        report("FAIL", "brief", "the brief declares dependencies and data flow on one canvas")
    if not svg_path.exists():
        report("FAIL", "svg", f"no SVG at {svg_path.relative_to(root)}")
        return
    raw = svg_path.read_text(encoding="utf-8")
    try:
        tree = ET.fromstring(raw)
    except ET.ParseError as e:
        report("FAIL", "svg", f"not well-formed XML: {e}")
        return
    if "viewBox" not in tree.attrib:
        report("FAIL", "svg", "no viewBox on the root element")
    if re.search(r"<image\b", raw):
        report("FAIL", "svg", "embeds an <image>; build the diagram from shapes and text")
    for m in re.finditer(r"(?:href|src)\s*=\s*\"(https?:|file:|//)[^\"]*\"|@import|url\(\s*['\"]?(https?:|//)", raw):
        report("FAIL", "svg", f"references something external: {m.group(0)[:60]}")
    texts = [norm_text("".join(el.itertext())) for el in tree.iter() if el.tag.endswith("}text") or el.tag == "text"]
    texts = [t for t in texts if t]
    if not texts and len(re.findall(r"<path\b", raw)) > 0:
        report("FAIL", "svg", "no <text> elements; text appears to be converted to paths")
    labels = {norm_text(r["label"]) for r in rows if r.get("label") and "<fill" not in r["label"]}
    for lab in sorted(labels):
        if lab not in texts:
            report("FAIL", "elements", f"brief element '{lab}' is not on the canvas")
    for t in texts:
        if t not in labels and t not in others:
            report("FAIL", "elements", f"canvas text '{t}' is in no brief element; a diagram asserts nothing its brief does not")
    palette = {norm_color(c) for c in cfg.get("diagram_palette", [])}
    if palette:
        used = set()
        for m in re.finditer(r"(?:fill|stroke|stop-color|color)\s*[:=]\s*\"?\s*(#[0-9a-fA-F]{3,8}|rgb\([^)]*\))", raw):
            used.add(norm_color(m.group(1)))
        for c in sorted(used - palette):
            report("FAIL", "palette", f"color {c} is outside the house palette")
    if a.client_facing or audience == "client":
        prefix = cfg.get("project_prefix", "")
        series = "|".join(sorted(cfg["series"], key=len, reverse=True))
        for t in texts:
            if re.search(r"\[?\b(%s)-\d{1,2}\]?|\[I\]" % series, t) or (prefix and re.search(r"\b%s-[A-Z]{3}-\d\d\b" % prefix, t)):
                report("FAIL", "identifiers", f"internal identifier on a client-facing canvas: '{t}'")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("brief")
    b.add_argument("--root", default=".")
    b.add_argument("--id", required=True)
    c = sub.add_parser("check")
    c.add_argument("--root", default=".")
    c.add_argument("--id", required=True)
    c.add_argument("--client-facing", action="store_true")
    c.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "brief":
        brief(a)
        return 0
    check(a)
    fails = [f for f in FINDINGS if f["level"] == "FAIL"]
    if a.json:
        print(json.dumps(FINDINGS, indent=2))
    else:
        for f in FINDINGS:
            print(f"{f['level']:5} {f['check']:11} {f['message']}")
        print(f"\n[{a.id.strip('[]`').upper()}] acceptance: {'passed' if not fails else f'{len(fails)} FAIL'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
