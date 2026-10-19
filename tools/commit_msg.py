"""Check a commit message against the repository convention. Standard library only.

    python tools/commit_msg.py <message-file>

The header is a Conventional Commit: type(scope)!: subject, in the imperative, 72 characters
or fewer. The body states What, Why and How, each as a paragraph that starts with its label.
Merge, revert, fixup and squash commits are exempt.
"""
import re
import sys
from pathlib import Path

TYPES = "feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert"
HEADER = re.compile(rf"^({TYPES})(\([a-z0-9._/-]+\))?!?: \S.*$")
LABELS = ("What:", "Why:", "How:")


def problems(message):
    lines = [l for l in message.splitlines() if not l.startswith("#")]
    text = "\n".join(lines).strip()
    header = text.split("\n", 1)[0] if text else ""
    if header.startswith(("Merge ", "Revert ", "fixup!", "squash!")):
        return []
    out = []
    if not HEADER.match(header):
        out.append(f"header must be 'type(scope): subject' with type one of {TYPES.replace('|', ', ')}")
    if len(header) > 72:
        out.append(f"header is {len(header)} characters, limit 72")
    starts = [l for l in lines if l.startswith(LABELS)]
    for label in LABELS:
        if not any(l.startswith(label) for l in starts):
            out.append(f"body is missing a paragraph that starts with '{label}'")
    return out


def main():
    found = problems(Path(sys.argv[1]).read_text(encoding="utf-8"))
    for f in found:
        print(f"commit-msg: {f}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
