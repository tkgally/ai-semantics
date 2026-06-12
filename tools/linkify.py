#!/usr/bin/env python3
"""linkify.py — keep in-repo references in the wiki clickable and correct.

The wiki cites other pages as backticked code spans, e.g. `source/weissweiler-2023-cxg-insight`,
`claim/formal-competence-aann-ceiling`, `decisions/open/cxg-probing-anchor`, `meaning-senses.md`,
`base/sources/foo.md`. Those render as inert code in a markdown viewer. This tool:

  1. WRAPS each such bare code span whose target exists into a clickable relative link that keeps
     the original code-span as its visible label, e.g.
        `source/weissweiler-2023-cxg-insight`
        ->  [`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md)
  2. REPAIRS already-linked references whose path is stale (e.g. after a page or folder is moved)
     by recomputing the relative path from the recognized label. This makes the wiki robust to
     reorganization: move files, re-run linkify, links self-heal.

Design rules:
- Only act on references whose resolved target FILE EXISTS. Aspirational mentions of not-yet-created
  pages are left as plain code spans, so the tool never creates a dead link.
- Idempotent: re-running changes nothing once paths are correct.
- The YAML front-matter `links:` block uses `target: type/id` WITHOUT backticks and is never touched —
  it remains the machine-readable typed-link graph that senselint consumes.

Usage:
    python3 tools/linkify.py            # rewrite in place across wiki/
    python3 tools/linkify.py --check    # report what would change, exit 1 if anything would
    python3 tools/linkify.py PATH ...   # restrict to given files/dirs
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(REPO, "wiki")

# type prefix -> directory (relative to repo root) for the typed findings/base pages
TYPE_DIR = {
    "source": "wiki/base/sources",
    "resource": "wiki/base/resources",
    "concept": "wiki/base/concepts",
    "claim": "wiki/findings/claims",
    "result": "wiki/findings/results",
    "conjecture": "wiki/findings/conjectures",
    "theory": "wiki/findings/theory",
    "open-question": "wiki/findings/open-questions",
    "essay": "wiki/findings/essays",
}

_TYPED = re.compile(r"^(?P<type>" + "|".join(TYPE_DIR) + r")/(?P<id>[a-z0-9-]+)$")
_DECISION = re.compile(r"^decisions/(?P<sub>open|resolved)/(?P<id>[a-z0-9-]+)(?:\.md)?$")


def resolve_ref(ref):
    """Map a reference label to an existing absolute target path, or None.

    Handles: typed refs (`type/id`), decision refs (`decisions/open|resolved/id`),
    and any relative `.md` path (resolved against wiki/ first, then the repo root).
    """
    ref = ref.strip()
    m = _TYPED.match(ref)
    if m:
        cand = [os.path.join(REPO, TYPE_DIR[m.group("type")], m.group("id") + ".md")]
    elif _DECISION.match(ref):
        m = _DECISION.match(ref)
        cand = [os.path.join(REPO, "wiki", "decisions", m.group("sub"), m.group("id") + ".md")]
    elif ref.endswith(".md"):
        cand = [os.path.join(WIKI, ref), os.path.join(REPO, ref)]
    else:
        return None
    for c in cand:
        if os.path.isfile(c):
            return c
    return None


# already-linked reference: [`label`](path)
_LINKED = re.compile(r"\[`(?P<ref>[^`\n]+)`\]\((?P<path>[^)\n]+)\)")
# bare code span not already part of a link
_BARE = re.compile(r"(?<!\[)`(?P<ref>[^`\n]+)`(?!\]\()")


def process_text(text, file_path):
    """Return (new_text, n_changed). Repairs stale links, then wraps bare refs.

    Skips fenced code blocks.
    """
    file_dir = os.path.dirname(file_path)
    changed = 0

    def relto(target_abs):
        return os.path.relpath(target_abs, file_dir)

    def repair(m):
        nonlocal changed
        target = resolve_ref(m.group("ref"))
        if target is None:
            return m.group(0)  # unknown/external link — leave untouched
        new_rel = relto(target)
        if new_rel == m.group("path"):
            return m.group(0)
        changed += 1
        return "[`%s`](%s)" % (m.group("ref"), new_rel)

    def wrap(m):
        nonlocal changed
        target = resolve_ref(m.group("ref"))
        if target is None:
            return m.group(0)  # not an in-repo page — leave as plain code span
        changed += 1
        return "[`%s`](%s)" % (m.group("ref"), relto(target))

    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        line = _LINKED.sub(repair, line)
        line = _BARE.sub(wrap, line)
        out.append(line)
    return "\n".join(out), changed


def iter_md(paths):
    for p in paths:
        ap = os.path.abspath(p)
        if os.path.isdir(ap):
            for root, _, files in os.walk(ap):
                for f in sorted(files):
                    if f.endswith(".md"):
                        yield os.path.join(root, f)
        elif ap.endswith(".md"):
            yield ap


def main(argv):
    check = "--check" in argv
    args = [a for a in argv if not a.startswith("--")]
    targets = args or [WIKI]

    total_files, total_links = 0, 0
    for fp in iter_md(targets):
        with open(fp, encoding="utf-8") as fh:
            src = fh.read()
        new, n = process_text(src, fp)
        if n:
            total_files += 1
            total_links += n
            rel = os.path.relpath(fp, REPO)
            verb = "WOULD update" if check else "updated"
            print("  %s %2d link(s) in %s" % (verb, n, rel))
            if not check:
                with open(fp, "w", encoding="utf-8") as fh:
                    fh.write(new)

    if check:
        print("linkify --check: %d link(s) across %d file(s) need attention."
              % (total_links, total_files))
        return 1 if total_links else 0
    print("linkify: updated %d link(s) across %d file(s)." % (total_links, total_files))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
