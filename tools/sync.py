#!/usr/bin/env python3
"""Keep every copy of shared material identical to its canonical source.

tools/shared.json maps each source under shared/ (a skill folder or a single file) to
the copies committed inside plugins. Plugins must install on their own, so the copies
are committed; this tool is the only way they change.

    python tools/sync.py --check   # exit 1 on any drift (run by tools/check.py)
    python tools/sync.py --write   # overwrite every copy from its source
"""
import argparse
import filecmp
import shutil
import sys
from common import ROOT, shared_entries, files_of


def drift(src, dst):
    if src.is_file():
        return [] if dst.exists() and filecmp.cmp(src, dst, shallow=False) else [dst]
    a, b = files_of(src), (files_of(dst) if dst.exists() else [])
    out = [dst / r for r in sorted(set(a) ^ set(b))]
    out += [dst / r for r in a if r in b and not filecmp.cmp(src / r, dst / r, shallow=False)]
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    a = ap.parse_args()
    found = 0
    for src, copies in shared_entries():
        if not src.exists():
            print(f"MISSING source {src.relative_to(ROOT)}")
            found += 1
            continue
        for dst in copies:
            d = drift(src, dst)
            if not d:
                continue
            if a.write:
                if src.is_dir():
                    shutil.rmtree(dst, ignore_errors=True)
                    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(src, dst)
                print(f"synced {dst.relative_to(ROOT)}")
            else:
                found += len(d)
                for x in d:
                    print(f"DRIFT {x.relative_to(ROOT)}")
    if a.check:
        print(f"sync: {found} drifted file(s)")
        return 1 if found else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
