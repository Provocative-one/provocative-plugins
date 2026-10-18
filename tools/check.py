#!/usr/bin/env python3
"""Run every repository check. The pre-commit hook calls this; exit 1 if any check fails.

  validate     frontmatter, plugin versions, marketplace coverage
  sync         copies of shared material equal their source
  index        the README index is current
  tests        every plugins/<name>/fixture/run_regression.py and every tests/<name>/run.py,
               discovered at run time, so a new plugin adds its tests by convention
"""
import subprocess
import sys
from common import ROOT, PLUGINS

PY = sys.executable


def steps():
    yield "validate", [PY, "tools/validate.py"]
    yield "sync", [PY, "tools/sync.py", "--check"]
    yield "index", [PY, "tools/index.py", "--check"]
    for r in sorted(PLUGINS.glob("*/fixture/run_regression.py")):
        yield f"{r.parts[-3]} regression", [PY, str(r.relative_to(ROOT))]
    for r in sorted((ROOT / "tests").glob("*/run.py")):
        yield f"tests/{r.parent.name}", [PY, str(r.relative_to(ROOT))]


def main():
    failed = []
    for label, cmd in steps():
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        tail = (r.stdout.strip().splitlines() or [""])[-1]
        print(f"{'ok  ' if r.returncode == 0 else 'FAIL'} {label:34} {tail}")
        if r.returncode != 0:
            failed.append(label)
            print(r.stdout[-2000:], r.stderr[-1000:])
    for cache in list(ROOT.rglob("__pycache__")):
        if PLUGINS in cache.parents or (ROOT / "tests") in cache.parents:
            for f in cache.iterdir():
                f.unlink()
            cache.rmdir()
    print("check: " + ("all passed" if not failed else f"failed: {', '.join(failed)}"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
