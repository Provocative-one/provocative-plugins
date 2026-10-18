#!/usr/bin/env python3
"""Regression run for the architecture-authoring plugin.

1. The clean fixture audits with zero FAIL, including its published derivative.
2. The fixture with every mechanical defect from defects.json planted reports
   exactly the expected FAILs and no others.
3. The diagram acceptance run passes on the built asset, and finds each planted SVG defect.
4. The reissue mode lists exactly the changed, added and removed annex items.

Usage: python3 run_regression.py   (from any directory)
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent / "skills" / "architecture-set-audit" / "scripts" / "audit.py"
FIX = HERE / "heritage-hub"
spec = json.loads((HERE / "defects.json").read_text(encoding="utf-8"))
DERIVED = "published/heritage-hub-milestone-plan-1.0.0.md"


def run(root, extra=()):
    out = subprocess.run([sys.executable, str(AUDIT), "--root", str(root), "--json", *extra],
                         capture_output=True, text=True)
    return [f for f in json.loads(out.stdout) if f["level"] == "FAIL"]


ok = True
with tempfile.TemporaryDirectory() as tmp:
    clean = Path(tmp) / "clean"
    shutil.copytree(FIX, clean)
    fails = run(clean, ["--derived", str(clean / DERIVED)])
    print(f"clean fixture: {len(fails)} FAIL")
    if fails:
        ok = False
        for f in fails:
            print("  unexpected:", f["check"], f["message"])

    bad = Path(tmp) / "bad"
    shutil.copytree(FIX, bad)
    expected = []
    for d in spec["mechanical"]:
        p = bad / d["file"]
        if "create" in d:
            p.write_text(d["create"], encoding="utf-8")
        else:
            t = p.read_text(encoding="utf-8")
            assert t.count(d["find"]) == 1, f"{d['id']}: anchor not unique in {d['file']}"
            p.write_text(t.replace(d["find"], d["replace"]), encoding="utf-8")
        expected += [(d["id"], e["check"], e["contains"]) for e in d["expect"]]
    fails = run(bad, ["--derived", str(bad / DERIVED)])
    matched = set()
    for did, check, contains in expected:
        hit = [i for i, f in enumerate(fails) if f["check"] == check and contains in f["message"]]
        if hit:
            matched.update(hit)
            print(f"  found    {did} {check}: {contains}")
        else:
            ok = False
            print(f"  MISSED   {did} {check}: {contains}")
    for i, f in enumerate(fails):
        if i not in matched:
            ok = False
            print(f"  EXTRA    {f['check']}: {f['message']}")
    print(f"planted fixture: {len(expected)} expected, {len(matched)} matched, {len(fails) - len(matched)} extra")

DIAG = HERE.parent / "skills" / "diagram-assets" / "scripts" / "diagram_tools.py"
g = spec["diagram"]
with tempfile.TemporaryDirectory() as tmp:
    clean = Path(tmp) / "clean"
    shutil.copytree(FIX, clean)
    res = subprocess.run([sys.executable, str(DIAG), "check", "--root", str(clean), "--id", g["id"], "--json"],
                         capture_output=True, text=True)
    fails = [f for f in json.loads(res.stdout) if f["level"] == "FAIL"]
    print(f"diagram {g['id']} clean: {len(fails)} FAIL")
    ok = ok and not fails
    bad = Path(tmp) / "bad"
    shutil.copytree(FIX, bad)
    svg = bad / "arc42" / "assets" / f"{g['id'].lower()}.svg"
    t = svg.read_text(encoding="utf-8")
    for p_ in g["plants"]:
        assert t.count(p_["find"]) == 1, p_["id"]
        t = t.replace(p_["find"], p_["replace"])
    svg.write_text(t, encoding="utf-8")
    res = subprocess.run([sys.executable, str(DIAG), "check", "--root", str(bad), "--id", g["id"], "--json"],
                         capture_output=True, text=True)
    fails = [f for f in json.loads(res.stdout) if f["level"] == "FAIL"]
    hit = set()
    for p_ in g["plants"]:
        idx = [i for i, f in enumerate(fails) if f["check"] == p_["expect"]["check"] and p_["expect"]["contains"] in f["message"]]
        hit.update(idx)
        print(f"  {'found ' if idx else 'MISSED'}   {p_['id']} {p_['expect']['check']}: {p_['expect']['contains']}")
        ok = ok and bool(idx)
    for i, f in enumerate(fails):
        if i not in hit:
            ok = False
            print(f"  EXTRA    {f['check']}: {f['message']}")

r = spec["reissue"]
out = subprocess.run([sys.executable, str(AUDIT), "--reissue", str(HERE / r["old"]), str(HERE / r["new"])],
                     capture_output=True, text=True).stdout
want = [f"numbered items changed: {r['changed']}", f"numbered items added:   {r['added']}",
        f"other passages changed: {r['passages']}"]
for w in want:
    if w not in out:
        ok = False
        print("  reissue MISSED:", w)
print("reissue mode:", "ok" if all(w in out for w in want) else "mismatch")
print("\nREGRESSION PASSED" if ok else "\nREGRESSION FAILED")
sys.exit(0 if ok else 1)
