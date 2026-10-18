"""Helpers shared by the repository tools. Standard library only; PyYAML is used when present."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
SHARED = ROOT / "shared"
EXCLUDED_PARTS = {"__pycache__", "node_modules", ".DS_Store"}


def load_shared():
    return json.loads((ROOT / "tools" / "shared.json").read_text(encoding="utf-8"))


def shared_entries():
    """(source Path, [copy Paths]) for every entry in tools/shared.json."""
    return [(ROOT / e["source"], [ROOT / c for c in e["copies"]]) for e in load_shared()["shared"]]


def shared_copy_dirs():
    """Every plugin skill folder that is a copy of a shared skill."""
    return {c.resolve() for src, copies in shared_entries() if src.is_dir() for c in copies}


def plugin_names():
    return sorted(p.name for p in PLUGINS.iterdir() if (p / ".claude-plugin" / "plugin.json").exists())


def plugin_manifest(name):
    return json.loads((PLUGINS / name / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def skills_of(plugin):
    return sorted(p for p in (PLUGINS / plugin / "skills").iterdir() if (p / "SKILL.md").exists())


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        inner = v[1:-1]
        return inner.replace("\\\"", "\"") if v[0] == '"' else inner.replace("''", "'")
    return v


def frontmatter(skill_md):
    """Return (dict, error). Uses PyYAML when installed, else a parser for the shapes these skills use."""
    text = Path(skill_md).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None, "no YAML frontmatter"
    block = m.group(1)
    try:
        import yaml  # noqa
        data = yaml.safe_load(block)
        if not isinstance(data, dict):
            return None, "frontmatter is not a mapping"
        return data, None
    except ImportError:
        pass
    except Exception as e:  # yaml.YAMLError
        return None, f"invalid YAML: {e}"
    data, current = {}, None
    for line in block.split("\n"):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current is None or not isinstance(data.get(current), dict):
                return None, f"unexpected indentation: {line!r}"
            k, _, v = line.strip().partition(":")
            data[current][k.strip()] = _scalar(v)
            continue
        k, sep, v = line.partition(":")
        if not sep:
            return None, f"cannot parse line: {line!r}"
        k = k.strip()
        if v.strip() == "":
            data[k], current = {}, k
        else:
            data[k], current = _scalar(v), None
    return data, None


def files_of(directory, exclude_root_dirs=()):
    """Sorted relative paths of every file under directory, skipping caches and the named root folders."""
    out = []
    for p in sorted(Path(directory).rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(directory)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        if rel.parts and rel.parts[0] in exclude_root_dirs:
            continue
        out.append(rel)
    return out
