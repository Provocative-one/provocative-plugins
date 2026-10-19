#!/usr/bin/env python3
"""Smoke tests for the architecture-continuity audit scripts: each sample must audit clean."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent.parent / "plugins" / "architecture-continuity" / "skills"
RUNS = [
    (SKILLS / "c4-diagram-package" / "scripts" / "audit_c4_package.py", HERE / "samples" / "c4-package"),
    (SKILLS / "closure-extraction-handoff" / "scripts" / "audit_pack.py", HERE / "samples" / "knowledge-pack"),
]
ok = True
for script, sample in RUNS:
    r = subprocess.run([sys.executable, str(script), str(sample)], capture_output=True, text=True)
    print(f"{'ok  ' if r.returncode == 0 else 'FAIL'} {script.name} on {sample.name}: {(r.stdout.strip().splitlines() or [''])[-1]}")
    ok &= r.returncode == 0
print("architecture-continuity smoke tests " + ("passed" if ok else "failed"))
sys.exit(0 if ok else 1)
