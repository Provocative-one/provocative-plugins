#!/usr/bin/env python3
"""Coherence audit for an arc42 document set (architecture plus estimate).

Generalized from the audit that gated a production document set. Configuration lives in
tools/audit-config.json at the repository root; nothing project-specific is
hard-coded here.

Usage:
    python3 audit.py --root <repo>                         # audit the set
    python3 audit.py --root <repo> --derived deck.txt      # also check a client-facing text dump
    python3 audit.py --reissue old.txt new.txt             # list what a revision changed
    add --json for machine-readable findings

Checks on the set, in order:
  allowlist   every Markdown file under the living directory is configured
  anchors     every link <document>#anchor resolves to a heading
  sections    every role-qualified or bare section reference resolves
  registers   no duplicate or misplaced row; no undefined reference;
              plan-side rows cited at least once unless their status is terminal
  direction   the architecture cites no series the estimate owns
  markers     every series a document uses appears in its notation key
  residue     unbracketed or one-digit tokens, retired prefixes, template name used
              as a document name, placeholders, relative dates, inverted date ranges,
              table cells cut off mid-phrase
  counts      stated counts match the register or the list they head
  versions    title and front matter agree; README pointers and CHANGELOG headings
              equal the document versions; the estimate pin is semantically compatible
  assets      every registered asset marked Built has its SVG and brief; every SVG has a row
  rogue       other-engagement identifiers and forbidden client-vocabulary synonyms

Prose hygiene is out of scope: the stricter-ai-language-hygiene sweep handles it.
Exit status is 1 when any FAIL is reported.
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

FINDINGS = []


def report(level, check, msg):
    FINDINGS.append({"level": level, "check": check, "message": msg})


NUM = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen".split())}
for tens, base in (("twenty", 20), ("thirty", 30), ("forty", 40), ("fifty", 50)):
    NUM[tens] = base
    for w, i in list(NUM.items()):
        if 1 <= i <= 9:
            NUM[f"{tens}-{w}"] = base + i


def to_int(token):
    t = token.lower()
    return int(t) if t.isdigit() else NUM.get(t)


NUMBER = r"(\d{1,3}|" + "|".join(sorted(NUM, key=len, reverse=True)) + r")"
VERSION = r"(\d+\.\d+\.\d+)"
TERMINAL = ("closed", "withdrawn", "superseded", "retired")


def slug(heading):
    s = re.sub(r"[^\w\s-]", "", heading.lower())
    return re.sub(r"\s+", "-", s.strip())


def headings(text):
    return re.findall(r"^#{1,6} (.+)$", text, re.M)


def section_numbers(text):
    out = set()
    for h in headings(text):
        m = re.match(r"(\d+(?:\.\d+)*)\.?\s", h)
        if m:
            out.add(m.group(1))
    return out


def strip_code_fences(text):
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)


def lines(text):
    return strip_code_fences(text).split("\n")


def row_ids(text, series):
    """Rows defined in a register table, one whose header's first cell is ID."""
    rows, in_register = {}, False
    for line in text.split("\n"):
        if not line.startswith("|"):
            in_register = False
            continue
        if re.match(r"^\|\s*ID\s*\|", line):
            in_register = True
            continue
        if not in_register:
            continue
        m = re.match(r"^\|\s*`?\[(%s-\d\d)\]`?\s*\|" % re.escape(series), line)
        if m:
            rows.setdefault(m.group(1), []).append(line)
    return rows


def cited(text, series):
    return set(re.findall(r"\[(%s-\d\d)\]" % re.escape(series), text))


def table_block_after(all_lines, i):
    """Return (kind, item_count) for a list or table starting after line i, skipping blanks."""
    j = i + 1
    while j < len(all_lines) and not all_lines[j].strip():
        j += 1
    if j >= len(all_lines):
        return None, 0
    first = all_lines[j]
    if first.startswith("|"):
        n = 0
        while j < len(all_lines) and all_lines[j].startswith("|"):
            if not re.match(r"^\|[\s\-:|]+\|?\s*$", all_lines[j]):
                n += 1
            j += 1
        return "table", max(n - 1, 0)
    if re.match(r"^\s*([-*]|\d+[.)])\s", first):
        n = 0
        while j < len(all_lines) and (re.match(r"^\s*([-*]|\d+[.)])\s", all_lines[j]) or
                                       (all_lines[j].startswith("   ") and all_lines[j].strip())):
            if re.match(r"^([-*]|\d+[.)])\s", all_lines[j]):
                n += 1
            j += 1
        return "list", n
    return None, 0


def semver(v):
    return tuple(int(x) for x in v.split("."))


def pin_satisfied(pin, current):
    p, c = semver(pin), semver(current)
    if c < p:
        return False
    if p[0] != c[0]:
        return False
    if p[0] == 0 and p[1] != c[1]:
        return False
    return True


def audit_set(root, cfg):
    docs = {role: root / rel for role, rel in cfg["documents"].items()}
    texts = {role: p.read_text(encoding="utf-8") for role, p in docs.items() if p.exists()}
    for role, p in docs.items():
        if not p.exists():
            report("FAIL", "allowlist", f"configured {role} document missing: {p.relative_to(root)}")
    extra = {}
    for rel in cfg.get("also_read", []):
        p = root / rel
        if p.exists():
            extra[rel] = p.read_text(encoding="utf-8")
    alltexts = {**texts, **extra}
    owner_of = cfg["series"]

    # allowlist
    living = root / cfg.get("living_dir", "arc42")
    configured = {p.resolve() for p in docs.values()}
    for md in sorted(living.glob("*.md")):
        if md.resolve() not in configured:
            report("FAIL", "allowlist", f"living document not in audit-config.json: {md.relative_to(root)}")

    # anchors
    names = {p.name: role for role, p in docs.items()}
    pools = {role: {slug(h) for h in headings(t)} for role, t in texts.items()}
    for src, t in alltexts.items():
        for fname, anchor in re.findall(r"([\w.-]+\.md)#([\w-]+)", t):
            role = names.get(fname)
            if role and role in pools and anchor not in pools[role]:
                report("FAIL", "anchors", f"[{src}] {fname}#{anchor} resolves to no heading")

    # sections
    nums = {role: section_numbers(t) for role, t in texts.items()}
    other = [o.lower() for o in cfg.get("other_roles", ["technology report", "report", "rfp", "proposal",
                                                         "template", "brief", "standard"])]
    keys = [(r, r) for r in texts] + [(p.name.lower(), role) for role, p in docs.items()] + [(o, None) for o in other]
    for src, t in alltexts.items():
        for n, line in enumerate(lines(t), 1):
            low = line.lower()
            for m in re.finditer(r"§(\d+(?:\.\d+)*)", line):
                ref, pos = m.group(1), m.start()
                link = re.match(r"\]\(([^)#]+\.md)", line[m.end():])
                if link:
                    role = names.get(Path(link.group(1)).name)
                    if role is None:
                        continue
                else:
                    start = max(low.rfind(". ", 0, pos), low.rfind("; ", 0, pos), low.rfind("|", 0, pos)) + 1
                    stops = [x for x in (low.find(". ", m.end()), low.find("; ", m.end()), low.find("|", m.end())) if x != -1]
                    end = min(stops) if stops else len(low)
                    before, after = None, None
                    for key, role_ in keys:
                        for k in re.finditer(re.escape(key), low[start:pos]):
                            d = pos - (start + k.end())
                            if before is None or d < before[0]:
                                before = (d, role_)
                        for k in re.finditer(re.escape(key), low[m.end():end]):
                            d = k.start()
                            if d <= 25 and (after is None or d < after[0]):
                                after = (d, role_)
                    best = before or after
                    if best and best[1] is None:
                        continue
                    if best:
                        role = best[1]
                    elif src in texts:
                        role = src
                    elif src == "CHANGELOG.md":
                        continue
                    else:
                        report("WARN", "sections", f"[{src}:{n}] §{ref} names no document; qualify it by role")
                        continue
                if role in nums and ref not in nums[role]:
                    report("FAIL", "sections", f"[{src}:{n}] {role} §{ref} resolves to no heading")

    # registers
    for series, owner in owner_of.items():
        if owner not in texts:
            continue
        defined = row_ids(texts[owner], series)
        for rid, rows in defined.items():
            if len(rows) > 1:
                report("FAIL", "registers", f"[{series}] {rid} defined {len(rows)} times")
        for role, t in texts.items():
            if role != owner and row_ids(t, series):
                report("FAIL", "registers", f"[{series}] rows defined in {role}; the series belongs to {owner}")
        used = set()
        for t in alltexts.values():
            used |= cited(t, series)
        for rid in sorted(used - set(defined)):
            report("FAIL", "registers", f"{rid} referenced but not defined in {owner}")
        if series in cfg.get("cited_required", []):
            corpus = "\n".join(alltexts[k] for k in alltexts if k != "CHANGELOG.md")
            for rid in sorted(set(defined)):
                row = defined[rid][0]
                if len(re.findall(r"\[%s\]" % re.escape(rid), corpus)) > 1:
                    continue
                if any(word in row.lower() for word in TERMINAL):
                    continue
                report("FAIL", "registers", f"{rid} defined but never cited, and its status is not terminal")

    # direction
    if "architecture" in texts:
        est_series = [s for s, o in owner_of.items() if o == "estimate"]
        if est_series:
            leak = sorted(set(re.findall(r"\[(?:%s)-\d\d\]" % "|".join(est_series), texts["architecture"])))
            if leak:
                report("FAIL", "direction", f"architecture cites estimate series: {leak}")

    # markers
    prefix = cfg.get("project_prefix", "")
    for role, t in texts.items():
        key = re.search(r"^\| (?:Marker|Series) \| Meaning \| Registered in \|\n((?:\|.*\n?)+)", t, re.M)
        head_end = re.search(r"^## 1\.", t, re.M)
        keytext = t[:head_end.start()] if head_end else (key.group(1) if key else "")
        if not key:
            report("FAIL", "markers", f"[{role}] no notation key table (| Marker | Meaning | Registered in |)")
            continue
        for series in owner_of:
            if cited(t, series) and f"[{series}-nn]" not in keytext:
                report("FAIL", "markers", f"[{role}] uses [{series}-nn] but neither its notation key nor its preamble lists it")
        if prefix and re.search(r"\[%s-[A-Z]{3}-\d\d\]" % prefix, t) and f"[{prefix}-" not in keytext:
            report("FAIL", "markers", f"[{role}] uses diagram asset IDs but its notation key does not list them")

    # residue
    series_alt = "|".join(sorted(owner_of, key=len, reverse=True))
    loose = re.compile(r"(?<![\[\w-])(%s)-?\d{1,2}(?![\]\w.])" % series_alt)
    allow = set(cfg.get("residue_allow", ["C4", "Q1", "Q2", "Q3", "Q4"]))
    retired = cfg.get("retired_prefixes", [])
    for src, t in alltexts.items():
        if src == "CHANGELOG.md":
            continue
        for n, line in enumerate(lines(t), 1):
            for m in loose.finditer(line):
                tok = m.group(0)
                if tok in allow:
                    continue
                if re.fullmatch(r"(%s)-\d\d" % series_alt, tok) or re.fullmatch(r"(%s)\d{1,2}" % series_alt, tok) \
                        or re.fullmatch(r"(%s)-\d" % series_alt, tok):
                    report("FAIL", "residue", f"[{src}:{n}] unbracketed series token {tok}")
            for m in re.finditer(r"\[(%s)-(\d)\]" % series_alt, line):
                report("FAIL", "residue", f"[{src}:{n}] one-digit reference {m.group(0)}")
            for pfx in retired:
                if re.search(r"\[?%s-\d" % re.escape(pfx), line):
                    report("FAIL", "residue", f"[{src}:{n}] retired prefix {pfx}-")
            if prefix and re.search(r"(?<![\[\w])%s-[A-Z]{3}-\d\d(?!\])" % prefix, line) \
                    and not re.search(r"%s-[A-Z]{3}-\d\d\.svg" % prefix.lower(), line):
                report("FAIL", "residue", f"[{src}:{n}] unbracketed diagram asset ID")
            if src in texts and re.search(r"\barc42 document\b", line, re.I):
                report("FAIL", "residue", f"[{src}:{n}] template name used as a document name")
            for ph in (r"\bTODO\b", r"\bTBD\b", r"\bXXX\b", r"working template", r"lorem ipsum"):
                if re.search(ph, line, re.I):
                    report("FAIL", "residue", f"[{src}:{n}] placeholder '{re.search(ph, line, re.I).group(0)}'")
            if "<fill:" in line:
                report("WARN", "residue", f"[{src}:{n}] unfilled template slot")
            m = re.search(r"\b(yesterday|tomorrow|next week|last week|next sprint|last sprint|this week)\b", line, re.I)
            if m and src in texts:
                report("WARN", "residue", f"[{src}:{n}] relative date '{m.group(1)}'")
            for a, b in re.findall(r"\b((?:19|20)\d\d)\s*(?:-|–|to)\s*((?:19|20)\d\d)\b", line):
                if int(b) < int(a):
                    report("FAIL", "residue", f"[{src}:{n}] inverted date range {a} to {b}")
            nxt = lines(t)[n] if n < len(lines(t)) else ""
            if line.startswith("|") and src in texts and not re.match(r"^\|[\s\-:|]+\|?\s*$", nxt) \
                    and not re.match(r"^\|[\s\-:|]+\|?\s*$", line):
                for cell in [c.strip() for c in line.strip("|").split("|")]:
                    if re.search(r"\b(per|of|the|a|an|and|with|for)$", cell):
                        report("WARN", "residue", f"[{src}:{n}] table cell may be cut off: '...{cell[-30:]}'")

    # counts: notation-key counts against registers
    for role, t in texts.items():
        for series, owner in owner_of.items():
            m = re.search(r"^\| `\[%s-nn\]` \|[^\n]*?,\s*%s entries\s*\|" % (re.escape(series), NUMBER), t, re.M | re.I)
            if m and owner in texts:
                claimed, actual = to_int(m.group(1)), len(row_ids(texts[owner], series))
                if claimed != actual:
                    report("FAIL", "counts", f"[{role}] notation key claims {m.group(1)} [{series}] entries; register has {actual}")
    # counts: a claim line heading a list or table
    claim = re.compile(r"(?:\b(up to)\s+)?(?<![\d.§])\b%s\s+([a-z][a-z-]+s)\b" % NUMBER, re.I)
    for src, t in alltexts.items():
        if src == "CHANGELOG.md":
            continue
        ls = lines(t)
        for i, line in enumerate(ls):
            if not line.strip() or line.startswith(("|", "#", "-", "*")) or re.match(r"^\s*\d+[.)]\s", line):
                continue
            if not (line.rstrip().endswith(":") or (line.rstrip().endswith(".") and len(line) <= 80)):
                continue
            found = claim.findall(line)
            if len(found) != 1:
                continue
            upto, number, noun = found[0]
            kind, n = table_block_after(ls, i)
            if not kind:
                continue
            claimed = to_int(number)
            if claimed is None or claimed < 2:
                continue
            if upto and n > claimed:
                report("FAIL", "counts", f"[{src}:{i + 1}] 'up to {number} {noun}' heads a {kind} of {n}")
            elif upto and n < claimed:
                report("WARN", "counts", f"[{src}:{i + 1}] 'up to {number} {noun}' heads a {kind} of {n}")
            elif not upto and n != claimed:
                level = "FAIL"
                if kind == "table":
                    j = i + 1
                    while not ls[j].strip():
                        j += 1
                    header = ls[j].lower()
                    stem = noun.lower().rstrip("s")
                    if noun.lower() not in ("entries", "rows", "items") and stem not in header:
                        level = "WARN"
                report(level, "counts", f"[{src}:{i + 1}] '{number} {noun}' heads a {kind} of {n}")

    # versions
    ver = {}
    for role, t in texts.items():
        m = re.search(r"^\| Version \| %s \|" % VERSION, t, re.M)
        if not m:
            report("FAIL", "versions", f"[{role}] no Version row in front matter")
            continue
        ver[role] = m.group(1)
        title = re.search(r"Version %s\*\*" % VERSION, t)
        if title and title.group(1) != ver[role]:
            report("FAIL", "versions", f"[{role}] title says {title.group(1)}, front matter says {ver[role]}")
    for ptr in cfg.get("pointers", []):
        src = extra.get(ptr["file"]) or texts.get(ptr["file"])
        if src is None:
            report("FAIL", "versions", f"pointer file missing: {ptr['file']}")
            continue
        m = re.search(ptr["pattern"], src)
        want = ver.get(ptr["document"])
        if not m:
            report("FAIL", "versions", f"[{ptr['file']}] no pointer for {ptr['document']} (pattern {ptr['pattern']})")
        elif want and m.group(1) != want:
            report("FAIL", "versions", f"[{ptr['file']}] points to {ptr['document']} {m.group(1)}; document is {want}")
    log = extra.get("CHANGELOG.md")
    if log is not None:
        for role, p in docs.items():
            rel = str(p.relative_to(root))
            sec = re.search(r"^## %s\s*\n(.*?)(?=^## |\Z)" % re.escape(rel), log, re.M | re.S)
            if not sec:
                report("FAIL", "versions", f"[CHANGELOG.md] no heading for {rel}")
                continue
            heads = re.findall(r"^### \[%s\]" % VERSION, sec.group(1), re.M)
            if role in ver and (not heads or heads[0] != ver[role]):
                report("FAIL", "versions", f"[CHANGELOG.md] latest {rel} entry {heads[0] if heads else None}; document is {ver[role]}")
            if role == "architecture":
                ver["_arch_history"] = heads
    if "estimate" in texts and "architecture" in ver:
        m = re.search(r"^\| Estimates against \|[^|\n]*?%s" % VERSION, texts["estimate"], re.M)
        if not m:
            report("FAIL", "versions", "[estimate] no Estimates against row naming a version")
        else:
            pin, cur = m.group(1), ver["architecture"]
            history = ver.get("_arch_history")
            if history is not None and pin not in history:
                report("FAIL", "versions", f"[estimate] pin {pin} names no architecture version in the changelog")
            elif not pin_satisfied(pin, cur):
                report("FAIL", "versions", f"[estimate] pin {pin} is not satisfied by architecture {cur}; re-derive and re-pin")
            elif pin != cur:
                report("INFO", "versions", f"[estimate] pin {pin} satisfied by architecture {cur}")

    # assets: register rows against files
    if prefix:
        rows = {}
        for role, t in texts.items():
            in_reg = False
            for line in t.split("\n"):
                if not line.startswith("|"):
                    in_reg = False
                    continue
                if re.match(r"^\|\s*ID\s*\|", line):
                    in_reg = True
                    continue
                m = re.match(r"^\|\s*`?\[(%s-[A-Z]{3}-\d\d)\]`?\s*\|" % prefix, line)
                if in_reg and m:
                    if m.group(1) in rows:
                        report("FAIL", "assets", f"{m.group(1)} registered twice")
                    rows[m.group(1)] = (role, line)
        for src, t in alltexts.items():
            if src == "CHANGELOG.md":
                continue
            for aid in sorted(set(re.findall(r"\[(%s-[A-Z]{3}-\d\d)\]" % prefix, t)) - set(rows)):
                report("FAIL", "assets", f"[{src}] {aid} cited but registered in no asset register")
        for aid, (role, line) in sorted(rows.items()):
            cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
            built = "built" in cells and "not built" not in cells
            svg = root / "arc42" / "assets" / f"{aid.lower()}.svg"
            brief = root / "briefs" / f"{aid.lower()}.md"
            if built and not svg.exists():
                report("FAIL", "assets", f"{aid} registered Built but {svg.relative_to(root)} is missing")
            if built and not brief.exists():
                report("FAIL", "assets", f"{aid} registered Built but its brief {brief.relative_to(root)} is missing")
            if not built and svg.exists():
                report("WARN", "assets", f"{aid} has an SVG but its row is not Built")
        assets_dir = root / "arc42" / "assets"
        if assets_dir.exists():
            for svg in sorted(assets_dir.glob("*.svg")):
                if svg.stem.upper() not in rows:
                    report("FAIL", "assets", f"{svg.relative_to(root)} has no row in any asset register")

    # rogue terms and client vocabulary
    for pattern in cfg.get("rogue_terms", []):
        for src, t in alltexts.items():
            if src == "CHANGELOG.md":
                continue
            if re.search(pattern, t, re.I):
                report("FAIL", "rogue", f"[{src}] other-engagement term matching {pattern}")
    for entry in cfg.get("vocabulary", []):
        for syn in entry.get("forbidden", []):
            for src, t in alltexts.items():
                if src == "CHANGELOG.md":
                    continue
                for n, line in enumerate(lines(t), 1):
                    if re.search(r"\b%s\b" % re.escape(syn), line, re.I):
                        report("FAIL", "rogue", f"[{src}:{n}] '{syn}' where the client's term is '{entry['term']}'")


def audit_derived(path, cfg):
    t = Path(path).read_text(encoding="utf-8")
    prefix = cfg.get("project_prefix", "")
    series_alt = "|".join(sorted(cfg["series"], key=len, reverse=True))
    for n, line in enumerate(t.split("\n"), 1):
        if re.search(r"\[?\b(%s)-\d{1,2}\]?" % series_alt, line) or re.search(r"\[I\]", line):
            report("FAIL", "derived", f"[{path}:{n}] internal register reference or marker")
        if prefix and re.search(r"\b%s-[A-Z]{3}-\d\d\b" % prefix, line, re.I):
            report("FAIL", "derived", f"[{path}:{n}] diagram asset ID")
        for ph in (r"working template", r"\[Owner:", r"\bTODO\b", r"\bTBD\b", r"\bdraft\b"):
            if re.search(ph, line, re.I):
                report("FAIL", "derived", f"[{path}:{n}] placeholder or draft marker '{re.search(ph, line, re.I).group(0)}'")
        for term in cfg.get("client_forbidden_terms", []):
            if re.search(r"\b%s\b" % re.escape(term), line, re.I):
                report("FAIL", "derived", f"[{path}:{n}] excluded term '{term}'")
        for entry in cfg.get("vocabulary", []):
            for syn in entry.get("forbidden", []):
                if re.search(r"\b%s\b" % re.escape(syn), line, re.I):
                    report("FAIL", "derived", f"[{path}:{n}] '{syn}' where the client's term is '{entry['term']}'")


def numbered_items(text):
    items, other = {}, []
    for block in re.split(r"\n\s*\n", text):
        b = block.strip()
        m = re.match(r"^(?:\|\s*)?(\d{1,3})[.)|]\s*(.*)", b, re.S)
        if m:
            items[int(m.group(1))] = re.sub(r"\s+", " ", m.group(2)).strip()
        elif b:
            other.append(re.sub(r"\s+", " ", b))
    return items, other


def reissue(old, new):
    oi, op = numbered_items(Path(old).read_text(encoding="utf-8"))
    ni, np_ = numbered_items(Path(new).read_text(encoding="utf-8"))
    changed = sorted(k for k in oi.keys() & ni.keys() if oi[k] != ni[k])
    added, removed = sorted(ni.keys() - oi.keys()), sorted(oi.keys() - ni.keys())
    sm = difflib.SequenceMatcher(a=op, b=np_)
    passages = [np_[j1:j2] or op[i1:i2] for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]
    print("Reissue list")
    print(f"  numbered items changed: {changed or 'none'}")
    print(f"  numbered items added:   {added or 'none'}")
    print(f"  numbered items removed: {removed or 'none'}")
    flat = [p for group in passages for p in group]
    print(f"  other passages changed: {len(flat)}")
    for p in flat:
        print(f"    - {p[:90]}{'...' if len(p) > 90 else ''}")
    return changed, added, removed, flat


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default=None)
    ap.add_argument("--derived", action="append", default=[])
    ap.add_argument("--reissue", nargs=2, metavar=("OLD", "NEW"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.reissue:
        reissue(*a.reissue)
        return 0
    root = Path(a.root).resolve()
    cfg_path = Path(a.config) if a.config else root / "tools" / "audit-config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    audit_set(root, cfg)
    for d in a.derived:
        audit_derived(d, cfg)
    fails = [f for f in FINDINGS if f["level"] == "FAIL"]
    if a.json:
        print(json.dumps(FINDINGS, indent=2))
    else:
        for level in ("INFO", "WARN", "FAIL"):
            for f in FINDINGS:
                if f["level"] == level:
                    print(f"{level:5} {f['check']:10} {f['message']}")
        print(f"\n{len(fails)} FAIL | {sum(f['level'] == 'WARN' for f in FINDINGS)} WARN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
