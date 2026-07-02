#!/usr/bin/env python3
"""
build-index.py — regenerate the wiki/index.md page catalog from front-matter.

The catalog between the BEGIN/END markers in wiki/index.md is GENERATED, one
line per page, and must never be hand-edited (adopted 2026-07-02 with the
program, enforcing the 2026-06-18 `wiki-frontmatter-ergonomics` slimming
intent after the hand-maintained catalog regrew to ~600 KB). The header above
the BEGIN marker is hand-maintained; everything between the markers is owned
by this tool.

Usage:
  python3 tools/build-index.py [--repo /path/to/repo] [--check]

  (no flag)  rewrite the generated block in place; print per-section counts.
  --check    report-only: exit 1 if the block on disk differs from what would
             be generated (use in verification alongside senselint/linkify).

Line format (one line per page, details live on the pages):
  - [`<path>`](<href>) — <title> · **<status>** · <anchor-state> (<date>)
where status / anchor-state / date appear only where the front-matter carries
them. Titles and statuses are truncated; the link label always contains the
filename stem, which is what senselint check 6 matches on.

Exit codes: 0 ok; 1 --check found drift; 2 structural problem (markers missing).
"""

import os
import sys
import re
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from senselint import parse_front_matter  # same parser the lint gate uses

BEGIN_MARK = '<!-- BEGIN GENERATED CATALOG (tools/build-index.py) — do not hand-edit below -->'
END_MARK = '<!-- END GENERATED CATALOG -->'

INDEX_RELPATH = os.path.join('wiki', 'index.md')
TITLE_MAX = 170
STATUS_MAX = 70

# (section heading, directory relative to repo, href prefix relative to wiki/)
# Order mirrors the long-standing catalog order.
PAGE_SECTIONS = [
    ('Base — concepts', 'wiki/base/concepts', 'base/concepts'),
    ('Base — sources', 'wiki/base/sources', 'base/sources'),
    ('Base — resources', 'wiki/base/resources', 'base/resources'),
    ('Findings — conjectures', 'wiki/findings/conjectures', 'findings/conjectures'),
    ('Findings — claims', 'wiki/findings/claims', 'findings/claims'),
    ('Findings — results', 'wiki/findings/results', 'findings/results'),
    ('Findings — theory', 'wiki/findings/theory', 'findings/theory'),
    ('Findings — open-questions', 'wiki/findings/open-questions', 'findings/open-questions'),
    ('Findings — essays', 'wiki/findings/essays', 'findings/essays'),
    ('Findings — notes', 'wiki/findings/notes', 'findings/notes'),
    ('Experiments — designs', 'experiments/designs', '../experiments/designs'),
]


def _truncate(text, limit):
    text = ' '.join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit - 1].rstrip() + '…'


def _first_heading(path):
    """Fallback title for pages without front-matter: first '# ' heading."""
    try:
        with open(path, encoding='utf-8') as fh:
            for line in fh:
                if line.startswith('#'):
                    return line.lstrip('#').strip()
    except OSError:
        pass
    return None


def _anchor_state(meta):
    """For claim/result pages: 'anchored' | 'internal-contrast-only' | 'anchor: pending' | None."""
    if str(meta.get('type', '')) not in ('claim', 'result'):
        return None
    links = meta.get('links') or []
    for lk in links:
        if isinstance(lk, dict) and str(lk.get('rel', '')) == 'anchors' \
                and str(lk.get('target', '')).startswith('resource/'):
            return 'anchored'
    anchor = str(meta.get('anchor', '') or '').strip().lower()
    if anchor == 'internal-contrast-only':
        return 'internal-contrast-only'
    if anchor == 'pending':
        return 'anchor: pending'
    return None


def page_line(abspath, href):
    """One catalog line for a .md page. href is relative to wiki/."""
    meta, _err = parse_front_matter(abspath)
    meta = meta or {}
    stem = os.path.basename(abspath)[:-3]
    title = meta.get('title') or _first_heading(abspath) or stem
    label = href[3:] if href.startswith('../') else href  # readable label

    parts = ['- [`{}`]({}) — {}'.format(label, href, _truncate(title, TITLE_MAX))]
    status = meta.get('status')
    if status:
        parts.append('**{}**'.format(_truncate(status, STATUS_MAX)))
    anchor = _anchor_state(meta)
    if anchor:
        parts.append(anchor)
    date = meta.get('updated') or meta.get('created')
    if date:
        parts.append('({})'.format(str(date)))
    return ' · '.join(parts)


def build_catalog(repo):
    """Return (catalog_text, stats) — the full generated block content."""
    out = []
    stats = []

    def add_section(heading, lines, note=None):
        out.append('### {}'.format(heading))
        out.append('')
        if note:
            out.append(note)
            out.append('')
        if lines:
            out.extend(lines)
        else:
            out.append('*(none)*')
        out.append('')
        stats.append((heading, len(lines)))

    # Decisions — open (regenerated every run so the dashboard can't go stale),
    # plus a one-line pointer for the resolved changelog.
    open_dir = os.path.join(repo, 'wiki', 'decisions', 'open')
    open_lines = []
    if os.path.isdir(open_dir):
        for fname in sorted(os.listdir(open_dir)):
            if fname.endswith('.md'):
                open_lines.append(page_line(os.path.join(open_dir, fname),
                                            'decisions/open/' + fname))
    resolved_dir = os.path.join(repo, 'wiki', 'decisions', 'resolved')
    n_resolved = len([f for f in os.listdir(resolved_dir)
                      if f.endswith('.md') and f != 'index.md']) \
        if os.path.isdir(resolved_dir) else 0
    add_section(
        'Decisions — open', open_lines,
        note=('{} resolved to date — full rationale changelog: '
              '[`decisions/resolved/index.md`](decisions/resolved/index.md).'.format(n_resolved)))

    # Typed-page sections.
    for heading, dirpath, href_prefix in PAGE_SECTIONS:
        absdir = os.path.join(repo, dirpath)
        if not os.path.isdir(absdir):
            continue  # e.g. findings/notes before its first page
        lines = []
        for fname in sorted(os.listdir(absdir)):
            if fname.endswith('.md') and fname != 'index.md':
                lines.append(page_line(os.path.join(absdir, fname),
                                       href_prefix + '/' + fname))
        add_section(heading, lines)

    # Base — wants (a single standing page).
    if os.path.isfile(os.path.join(repo, 'wiki', 'base', 'wanted.md')):
        add_section('Base — wants',
                    ['- [`base/wanted.md`](base/wanted.md) — source backlog: '
                     'what the project wants next, with unreachable items marked as such.'])

    # Experiments — run records (directories; linked via their README).
    runs_dir = os.path.join(repo, 'experiments', 'runs')
    run_lines = []
    if os.path.isdir(runs_dir):
        for dname in sorted(os.listdir(runs_dir), reverse=True):
            dabs = os.path.join(runs_dir, dname)
            if not os.path.isdir(dabs):
                continue
            readme = os.path.join(dabs, 'README.md')
            if os.path.isfile(readme):
                run_lines.append('- [`experiments/runs/{}/`](../experiments/runs/{}/README.md)'
                                 .format(dname, dname))
            else:
                run_lines.append('- `experiments/runs/{}/` (no README)'.format(dname))
    add_section('Experiments — run records', run_lines,
                note='(Newest first. Not part of the wiki tree; indexed for navigability.)')

    total = sum(n for _h, n in stats)
    header = ('*Generated by `tools/build-index.py` — {} entries, one line per page; '
              'details live on the pages. Regenerate at every verification step; '
              'never hand-edit this block.*'.format(total))
    catalog = header + '\n\n' + '\n'.join(out).rstrip() + '\n'
    return catalog, stats


def main():
    ap = argparse.ArgumentParser(description='regenerate the wiki/index.md catalog')
    ap.add_argument('--repo', default=None)
    ap.add_argument('--check', action='store_true',
                    help='report-only; exit 1 if the on-disk block differs')
    args = ap.parse_args()

    if args.repo:
        repo = os.path.abspath(args.repo)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo = os.path.dirname(script_dir)
        if not os.path.isdir(os.path.join(repo, 'wiki')):
            repo = os.getcwd()

    index_path = os.path.join(repo, INDEX_RELPATH)
    try:
        with open(index_path, encoding='utf-8') as fh:
            text = fh.read()
    except OSError as e:
        print('ERROR: cannot read {}: {}'.format(index_path, e), file=sys.stderr)
        sys.exit(2)

    if BEGIN_MARK not in text or END_MARK not in text:
        print('ERROR: generation markers not found in wiki/index.md.\n'
              '  Expected: {}\n  and:      {}\n'
              '  Add them to the hand-maintained header first.'.format(BEGIN_MARK, END_MARK),
              file=sys.stderr)
        sys.exit(2)

    head, rest = text.split(BEGIN_MARK, 1)
    _old_block, tail = rest.split(END_MARK, 1)

    catalog, stats = build_catalog(repo)
    new_text = head + BEGIN_MARK + '\n\n' + catalog + '\n' + END_MARK + tail

    if args.check:
        if new_text != text:
            print('build-index --check: catalog is STALE — run `python3 tools/build-index.py`.')
            sys.exit(1)
        print('build-index --check: catalog is up to date.')
        sys.exit(0)

    with open(index_path, 'w', encoding='utf-8') as fh:
        fh.write(new_text)

    for heading, n in stats:
        print('  {:32s} {:4d}'.format(heading, n))
    print('Wrote {} ({} bytes).'.format(INDEX_RELPATH, len(new_text.encode('utf-8'))))


if __name__ == '__main__':
    main()
