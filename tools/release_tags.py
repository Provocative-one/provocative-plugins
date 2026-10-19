"""Create, and optionally push, the release tag of every plugin whose current version is untagged.

    python tools/release_tags.py [plugin ...] [--commit REV] [--remote NAME] [--dry-run] [--push]

For each plugin (all of them when none is named) the tag is <plugin>-v<version>, read from
plugin.json at REV (default HEAD). The tag is annotated, and its message is the plugin's
[<version>] section of CHANGELOG.md at REV. A tag that already exists on REV, or on an
ancestor of REV (a release the plugin has not moved past), is kept. A tag on any other
commit stops the run. Nothing is pushed without --push; --dry-run changes nothing.
"""
import argparse
import json
import re
import subprocess
import sys

from common import ROOT, plugin_names


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {r.stderr.strip() or r.stdout.strip()}")
    return r


def changelog_section(text, version):
    """The body of '## [version] - date', and its date, or (None, None)."""
    m = re.search(rf"^## \[{re.escape(version)}\] - (\d{{4}}-\d{{2}}-\d{{2}})[ \t]*\n(.*?)(?=^## |^\[[^\]]+\]: |\Z)", text, re.S | re.M)
    if not m:
        return None, None
    body = re.sub(r"^### ", "", m.group(2).strip(), flags=re.M)
    return m.group(1), body


def plan_for(plugin, rev):
    manifest = json.loads(git("show", f"{rev}:plugins/{plugin}/.claude-plugin/plugin.json").stdout)
    version = manifest["version"]
    log = git("show", f"{rev}:plugins/{plugin}/CHANGELOG.md", check=False)
    if log.returncode != 0:
        raise SystemExit(f"{plugin}: no CHANGELOG.md at {rev}")
    date, body = changelog_section(log.stdout, version)
    if not body:
        raise SystemExit(f"{plugin}: CHANGELOG.md has no '## [{version}] - YYYY-MM-DD' section at {rev}")
    return f"{plugin}-v{version}", f"{plugin} {version} - {date}\n\n{body}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("plugins", nargs="*")
    ap.add_argument("--commit", default="HEAD")
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--push", action="store_true")
    a = ap.parse_args()

    rev = git("rev-parse", "--verify", f"{a.commit}^{{commit}}").stdout.strip()
    names = a.plugins or plugin_names()
    unknown = sorted(set(names) - set(plugin_names()))
    if unknown:
        raise SystemExit(f"unknown plugin: {', '.join(unknown)}")

    plans = [(n, *plan_for(n, rev)) for n in names]
    created = []
    for plugin, tag, message in plans:
        have = git("rev-parse", "--verify", "--quiet", f"refs/tags/{tag}^{{commit}}", check=False)
        if have.returncode == 0:
            at = have.stdout.strip()
            if at == rev or git("merge-base", "--is-ancestor", at, rev, check=False).returncode == 0:
                print(f"keep   {tag} (on {at[:7]})")
                created.append(tag)
                continue
            raise SystemExit(f"{tag} exists on {at[:7]}, which is not {rev[:7]} or one of its ancestors")
        print(f"create {tag} on {rev[:7]}")
        if not a.dry_run:
            git("tag", "-a", tag, "-m", message, rev)
        created.append(tag)

    if not a.push:
        return 0
    remote_tags = {l.split("\trefs/tags/")[1] for l in git("ls-remote", "--tags", a.remote).stdout.splitlines() if "\trefs/tags/" in l}
    missing = [t for t in created if t not in remote_tags]
    if not missing:
        print(f"{a.remote} already has every tag")
        return 0
    print(f"push   {', '.join(missing)} to {a.remote}")
    if not a.dry_run:
        git("push", a.remote, *[f"refs/tags/{t}" for t in missing])
        print(git("ls-remote", "--tags", a.remote, *missing).stdout.rstrip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
