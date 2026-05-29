#!/usr/bin/env python3
"""linkify.py — turn typed in-repo references into clickable relative markdown links.

The wiki cites other pages as backticked code spans, e.g. `source/weissweiler-2023-cxg-insight`,
`claim/formal-competence-aann-ceiling`, `decisions/open/cxg-probing-anchor`, `meaning-senses.md`.
Those render as inert code in a markdown viewer. This tool rewrites each such reference whose
target actually exists on disk into a clickable relative link that keeps the original code-span as
its visible label, e.g.

    `source/weissweiler-2023-cxg-insight`
    ->  [`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md)

Design rules:
- Only linkify references whose resolved target FILE EXISTS. Aspirational mentions of not-yet-created
  pages (e.g. a decisions/open/ entry a conjecture says it *will* queue) are left as plain code spans.
- Idempotent: an already-linkified reference (preceded by '[' or followed by '](') is never re-wrapped.
- The YAML front-matter `links:` block uses `target: type/id` WITHOUT backticks and is therefore never
  touched — it remains the machine-readable typed-link graph that senselint consumes.

Usage:
    python3 tools/linkify.py            # rewrite in place across wiki/
    python3 tools/linkify.py --check    # report what would change, exit 1 if anything would
    python3 tools/linkify.py PATH ...   # restrict to given files/dirs
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# type -> directory (relative to repo root) for the findings/base typed pages
TYPE_DIR = {
    "source": "wiki/base/sources",
    "resource": "wiki/base/resources",
    "concept": "wiki/base/concepts",
    "claim": "wiki/findings/claims",
    "result": "wiki/findings/results",
    "conjecture": "wiki/findings/conjectures",
    "theory": "wiki/findings/theory",
    "open-question": "wiki/findings/open-questions",
}

# Each rule: (compiled regex with the code-span inner text in group 'ref', resolver(match)->repo-rel path)
# Idempotency guard: (?<!\[) before the opening backtick, (?!\]\() after the closing backtick.
TYPED = re.compile(
    r"(?<!\[)`(?P<ref>(?P<type>" + "|".join(TYPE_DIR) + r")/(?P<id>[a-z0-9-]+))`(?!\]\()"
)
DECISION = re.compile(r"(?<!\[)`(?P<ref>decisions/open/(?P<id>[a-z0-9-]+))(?P<ext>\.md)?`(?!\]\()")
# Any backticked relative path ending in .md (catches index.md catalog entries like
# `base/sources/foo.md`, `findings/conjectures/bar.md`, `meaning-senses.md`).
PATHREF = re.compile(r"(?<!\[)`(?P<ref>[A-Za-z0-9][A-Za-z0-9._/-]*\.md)`(?!\]\()")


def resolve_existing(which, m):
    """Return absolute path of an existing target, or None to leave the ref untouched."""
    if which == "typed":
        cand = [os.path.join(REPO, TYPE_DIR[m.group("type")], m.group("id") + ".md")]
    elif which == "decision":
        cand = [os.path.join(REPO, "decisions/open", m.group("id") + ".md")]
    else:  # pathref: try wiki-relative first, then repo-root-relative
        ref = m.group("ref")
        cand = [os.path.join(REPO, "wiki", ref), os.path.join(REPO, ref)]
    for c in cand:
        if os.path.isfile(c):
            return c
    return None


def linkify_text(text, file_path):
    """Return (new_text, n_changed). file_path is absolute. Skips fenced code blocks."""
    file_dir = os.path.dirname(file_path)
    changed = 0

    def make_sub(which):
        def _sub(m):
            nonlocal changed
            target_abs = resolve_existing(which, m)
            if target_abs is None:
                return m.group(0)  # target does not exist -> leave as plain code span
            rel = os.path.relpath(target_abs, file_dir)
            changed += 1
            return "[`%s`](%s)" % (m.group("ref"), rel)
        return _sub

    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        for rx, which in ((TYPED, "typed"), (DECISION, "decision"), (PATHREF, "pathref")):
            line = rx.sub(make_sub(which), line)
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
    targets = args or [os.path.join(REPO, "wiki")]

    total_files, total_links, would_change = 0, 0, []
    for fp in iter_md(targets):
        with open(fp, encoding="utf-8") as fh:
            src = fh.read()
        new, n = linkify_text(src, fp)
        if n:
            total_files += 1
            total_links += n
            rel = os.path.relpath(fp, REPO)
            if check:
                would_change.append((rel, n))
            else:
                with open(fp, "w", encoding="utf-8") as fh:
                    fh.write(new)
                print("  linkified %2d ref(s) in %s" % (n, rel))

    if check:
        for rel, n in would_change:
            print("  WOULD linkify %2d ref(s) in %s" % (n, rel))
        print("linkify --check: %d link(s) across %d file(s) need conversion."
              % (total_links, total_files))
        return 1 if total_links else 0

    print("linkify: converted %d reference(s) across %d file(s)." % (total_links, total_files))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
