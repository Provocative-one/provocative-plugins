#!/usr/bin/env python3
"""Mechanical audit of a knowledge-extraction pack (one subject per file plus a README).

Usage: python3 audit_pack.py <pack_dir> [--readme 00-README.md]

Checks index closure (files vs README entries), cross-reference closure (prefix codes in
backticks that point nowhere), source headers, @-mentions, relative dates, placeholder
links, and counting claims. Exit code 1 when any FAIL is reported.
WARN items need judgment, not automation.
"""
import re, sys, argparse
from pathlib import Path

NUMWORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}
NUMWORDS.update({"twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24, "twenty-five": 25,
                 "thirty": 30, "thirty-six": 36, "forty": 40})
REL_DATES = re.compile(r"\b(yesterday|tomorrow|last week|next week|this week|next sprint|last sprint|"
                       r"this sprint|the prior day|earlier today|later today)\b", re.I)
FILE_CODE = re.compile(r"^([A-Za-z]+\d*)-")
CODE_TOKEN = re.compile(r"^([A-Z]+)(\d+)$")

fails, warns, infos = [], [], []

def strip_fences(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)

def strip_inline(line):
    """Drop inline code spans and quoted spans, which cite examples rather than assert them."""
    line = re.sub(r"`[^`]*`", "", line)
    line = re.sub(r'"[^"]*"|\u201c[^\u201d]*\u201d|\u2018[^\u2019]*\u2019', "", line)
    return line

def prose_lines(text):
    for i, l in enumerate(strip_fences(text).split("\n"), 1):
        yield i, strip_inline(l)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack_dir")
    ap.add_argument("--readme", default="00-README.md")
    a = ap.parse_args()
    root = Path(a.pack_dir)
    readme = root / a.readme
    if not readme.exists():
        print(f"FAIL: {a.readme} not found in {root}")
        sys.exit(1)
    rtext = readme.read_text(encoding="utf-8")

    files = sorted(p for p in root.glob("*.md") if p.name != a.readme)
    file_codes = {}
    for p in files:
        m = FILE_CODE.match(p.name)
        if not m:
            warns.append(f"{p.name}: filename has no prefix code (expected CODE-subject.md)")
            continue
        code = m.group(1)
        if code in file_codes:
            fails.append(f"{p.name}: prefix code {code} duplicates {file_codes[code]}")
        file_codes[code] = p.name

    # README entries: backticked codes in list or table lines
    readme_codes = set()
    for l in rtext.split("\n"):
        for c in re.findall(r"`([A-Z]+\d*)`", l):
            if l.lstrip().startswith(("-", "|", "*")):
                readme_codes.add(c)
    unlisted = sorted(set(file_codes) - readme_codes)
    dangling_readme = sorted(c for c in readme_codes if CODE_TOKEN.match(c) and c not in file_codes)
    for c in unlisted:
        warns.append(f"{file_codes[c]}: not listed in {a.readme}")
    for c in dangling_readme:
        fails.append(f"{a.readme} lists `{c}` but no file carries that code")

    # Cross-reference closure
    letters = {CODE_TOKEN.match(c).group(1) for c in file_codes if CODE_TOKEN.match(c)}
    known = set(file_codes)
    for p in files + [readme]:
        t = strip_fences(p.read_text(encoding="utf-8"))
        for tok in set(re.findall(r"`([A-Z]+\d+)`", t)):
            m = CODE_TOKEN.match(tok)
            if m and m.group(1) in letters and tok not in known:
                fails.append(f"{p.name}: cross-reference `{tok}` points to no file")

    # Per-file hygiene of the record
    header_ok = ("**Source:**", "**Sources:**", "**Artifact:**")
    for p in files:
        text = p.read_text(encoding="utf-8")
        head = "\n".join(text.split("\n")[:14])
        if not any(k in head for k in header_ok):
            warns.append(f"{p.name}: no Source or Artifact line in the first lines")
        for i, l in prose_lines(text):
            if re.search(r"(?<![\w.])@[A-Z][a-z]+", l):
                fails.append(f"{p.name}:{i}: @-mention in prose (drafts never emit @)")
            m = REL_DATES.search(l)
            if m:
                warns.append(f"{p.name}:{i}: relative date '{m.group(0)}'; resolve to an absolute date unless it is quoted")
        for t in re.findall(r"\]\(([^)]*)\)", strip_fences(text)):
            if t.strip() in ("", "#", "about:blank"):
                fails.append(f"{p.name}: empty or placeholder link target")
    for i, l in prose_lines(rtext):
        if re.search(r"(?<![\w.])@[A-Z][a-z]+", l):
            fails.append(f"{a.readme}:{i}: @-mention in prose")

    # Counting claims in the README
    for m in re.finditer(r"\b(\d+|" + "|".join(sorted(NUMWORDS, key=len, reverse=True)) +
                         r")\s+(subject|subjects)\s+files?\b", rtext, flags=re.I):
        n = int(m.group(1)) if m.group(1).isdigit() else NUMWORDS[m.group(1).lower()]
        listed = len(readme_codes & set(file_codes))
        if n != len(files):
            warns.append(f"{a.readme} claims {n} subject files; the folder holds {len(files)} ({listed} of them listed in the README)")

    notes = sum(1 for p in files if "Extraction note" in p.read_text(encoding="utf-8"))
    infos.append(f"{len(files)} subject files, {len(file_codes)} prefix codes, {notes} carry an Extraction note")

    for l in infos: print("INFO ", l)
    for l in warns: print("WARN ", l)
    for l in fails: print("FAIL ", l)
    print(f"\n{len(fails)} FAIL | {len(warns)} WARN")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
