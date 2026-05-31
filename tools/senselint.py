#!/usr/bin/env python3
"""
senselint.py — verification gate for the ai-semantics wiki.

Checks:
  1. Front-matter presence and required fields (type, id, title).
  2. meaning-senses tags drawn from the controlled vocabulary.
  3. Typed links: allowed relations and resolvable targets.
  4. Anchor discipline for claim/result pages.
  5. Contingent-language note: pages with non-empty contingent-on.
  6. Index coverage: every typed page mentioned in wiki/index.md.
  7. Inline-link integrity: every relative markdown link to a .md target resolves
     (keeps the clickable wiki navigation from rotting; see tools/linkify.py).

Usage:
  python3 tools/senselint.py [--repo /path/to/repo]

Exit code:
  0 — no ERRORs (warnings/infos may be present).
  1 — one or more ERRORs found.
"""

import os
import sys
import re
import argparse

# ---------------------------------------------------------------------------
# Minimal front-matter parser (stdlib-only; tries PyYAML first).
# ---------------------------------------------------------------------------

try:
    import yaml as _yaml
    def _parse_yaml(text):
        return _yaml.safe_load(text)
except ImportError:
    _yaml = None
    def _parse_yaml(text):
        """Very small YAML subset parser for front-matter only.

        Handles:
          - scalar values (strings, numbers, booleans, null)
          - lists (block style: '  - item')
          - nested mappings one level deep (for links: entries with rel/target)
        Does NOT handle flow style, anchors, or multi-line strings.
        Returns a dict or raises ValueError.
        """
        result = {}
        lines = text.splitlines()
        i = 0
        n = len(lines)

        def _scalar(s):
            s = s.strip()
            if s in ('true', 'True', 'TRUE'):
                return True
            if s in ('false', 'False', 'FALSE'):
                return False
            if s in ('null', 'Null', 'NULL', '~', ''):
                return None
            # strip surrounding quotes
            if (s.startswith('"') and s.endswith('"')) or \
               (s.startswith("'") and s.endswith("'")):
                return s[1:-1]
            try:
                return int(s)
            except ValueError:
                pass
            try:
                return float(s)
            except ValueError:
                pass
            return s

        while i < n:
            line = lines[i]
            # skip blank / comment lines
            if not line.strip() or line.strip().startswith('#'):
                i += 1
                continue
            # key: value
            m = re.match(r'^(\S[^:]*?):\s*(.*)', line)
            if not m:
                i += 1
                continue
            key = m.group(1).strip()
            val_raw = m.group(2).strip()
            i += 1
            if val_raw == '' or val_raw == '|' or val_raw == '>':
                # block list or mapping follows
                items = []
                obj_buf = {}
                while i < n:
                    l2 = lines[i]
                    if not l2.startswith(' ') and not l2.startswith('\t'):
                        break
                    stripped = l2.strip()
                    if stripped.startswith('#') or stripped == '':
                        i += 1
                        continue
                    if stripped.startswith('- '):
                        # could be a simple item or start of a mapping block
                        item_val = stripped[2:].strip()
                        if ':' in item_val:
                            # inline mapping: "- rel: supports"
                            if obj_buf:
                                items.append(obj_buf)
                            obj_buf = {}
                            km, vm = item_val.split(':', 1)
                            obj_buf[km.strip()] = _scalar(vm)
                        else:
                            if obj_buf:
                                items.append(obj_buf)
                                obj_buf = {}
                            items.append(_scalar(item_val))
                        i += 1
                    elif re.match(r'^\s+\S', l2) and ':' in stripped and not stripped.startswith('-'):
                        # continuation of a mapping block (indented key: val)
                        km2, vm2 = stripped.split(':', 1)
                        obj_buf[km2.strip()] = _scalar(vm2)
                        i += 1
                    else:
                        break
                if obj_buf:
                    items.append(obj_buf)
                result[key] = items if items else None
            else:
                result[key] = _scalar(val_raw)
        return result


def parse_front_matter(path):
    """Return (meta_dict, error_str).

    meta_dict is None on parse failure; error_str is None on success.
    """
    try:
        with open(path, encoding='utf-8') as fh:
            content = fh.read()
    except OSError as e:
        return None, f"cannot read file: {e}"

    if not content.startswith('---'):
        return {}, "no YAML front-matter block (file does not start with '---')"

    # Find closing ---
    rest = content[3:]
    end = rest.find('\n---')
    if end == -1:
        return {}, "front-matter block not closed (missing closing '---')"

    fm_text = rest[:end]
    try:
        meta = _parse_yaml(fm_text)
        if meta is None:
            meta = {}
        return meta, None
    except Exception as e:
        return {}, f"YAML parse error: {e}"


# ---------------------------------------------------------------------------
# Vocabulary and directory maps.
# ---------------------------------------------------------------------------

ALLOWED_RELATIONS = {
    'supports', 'contradicts', 'refines', 'depends-on',
    'operationalizes', 'anchors', 'supersedes',
}

# Mapping from link target type-prefix → directory path (relative to repo root).
# 'design' is not in CLAUDE.md's page types but exists in experiments/; treat as known.
TYPE_DIR_MAP = {
    'source':        'wiki/base/sources',
    'resource':      'wiki/base/resources',
    'concept':       'wiki/base/concepts',
    'claim':         'wiki/findings/claims',
    'result':        'wiki/findings/results',
    'conjecture':    'wiki/findings/conjectures',
    'theory':        'wiki/findings/theory',
    'open-question': 'wiki/findings/open-questions',
    # experiments/designs — referenced by some pages
    'design':        'experiments/designs',
}

FINDINGS_DIR = 'wiki/findings'
BASE_DIR = 'wiki/base'
INDEX_PATH = 'wiki/index.md'
MEANING_SENSES_PATH = 'wiki/meaning-senses.md'


def build_file_index(repo):
    """Return a set of all .md files (relative to repo) under wiki/ and experiments/."""
    result = set()
    for root, dirs, files in os.walk(repo):
        # skip .git
        dirs[:] = [d for d in dirs if d != '.git']
        for fname in files:
            if fname.endswith('.md'):
                full = os.path.join(root, fname)
                rel = os.path.relpath(full, repo)
                result.add(rel)
    return result


def resolve_link_target(target, repo):
    """Return (resolved_relpath_or_None, error_message_or_None).

    target looks like 'claim/foo' or 'source/bender-koller-2020-climbing'.
    We try <type_dir>/<id>.md and also <type_dir>/<id> (for dirs like resources/index).
    """
    if '/' not in target:
        return None, f"malformed target (no type prefix): '{target}'"
    type_prefix, slug = target.split('/', 1)
    if type_prefix not in TYPE_DIR_MAP:
        return None, f"unknown type prefix '{type_prefix}' in target '{target}'"
    type_dir = TYPE_DIR_MAP[type_prefix]
    candidate = os.path.join(repo, type_dir, slug + '.md')
    if os.path.isfile(candidate):
        return os.path.relpath(candidate, repo), None
    # also try without .md (edge case)
    candidate2 = os.path.join(repo, type_dir, slug)
    if os.path.isfile(candidate2):
        return os.path.relpath(candidate2, repo), None
    return None, f"dangling link target '{target}' (expected {os.path.join(type_dir, slug + '.md')})"


# ---------------------------------------------------------------------------
# Meaning-senses vocabulary parser.
# ---------------------------------------------------------------------------

def load_allowed_senses(repo):
    """Parse wiki/meaning-senses.md and return a set of allowed tag strings.

    Parses '### `tagname`' headings under the '## Tags' section.
    Also adds dot-sub-tags as described in CLAUDE.md (grounded.perceptual, etc.)
    — any tag of form '<prefix>.<suffix>' is valid if prefix is a known tag.
    """
    path = os.path.join(repo, MEANING_SENSES_PATH)
    tags = set()
    try:
        with open(path, encoding='utf-8') as fh:
            content = fh.read()
    except OSError:
        return tags, f"cannot read {MEANING_SENSES_PATH}"

    in_tags_section = False
    for line in content.splitlines():
        if line.startswith('## Tags'):
            in_tags_section = True
            continue
        if in_tags_section:
            if line.startswith('## ') and not line.startswith('## Tags'):
                break  # end of Tags section
            m = re.match(r'^###\s+`([^`]+)`', line)
            if m:
                tags.add(m.group(1))

    return tags, None


def is_valid_sense(tag, allowed_tags):
    """Return True if tag is in allowed_tags or is a valid sub-tag (prefix.suffix)."""
    if tag in allowed_tags:
        return True
    if '.' in tag:
        prefix = tag.split('.')[0]
        return prefix in allowed_tags
    return False


# ---------------------------------------------------------------------------
# Collectors.
# ---------------------------------------------------------------------------

def collect_findings_pages(repo):
    """Yield (relpath, abspath) for all .md files under wiki/findings/."""
    findings_abs = os.path.join(repo, FINDINGS_DIR)
    for root, dirs, files in os.walk(findings_abs):
        dirs[:] = sorted(d for d in dirs if d != '.git')
        for fname in sorted(files):
            if fname.endswith('.md'):
                abspath = os.path.join(root, fname)
                relpath = os.path.relpath(abspath, repo)
                yield relpath, abspath


def collect_base_pages(repo):
    """Yield (relpath, abspath) for .md files under wiki/base/ (excluding index.md)."""
    base_abs = os.path.join(repo, BASE_DIR)
    for root, dirs, files in os.walk(base_abs):
        dirs[:] = sorted(d for d in dirs if d != '.git')
        for fname in sorted(files):
            if fname.endswith('.md') and fname != 'index.md':
                abspath = os.path.join(root, fname)
                relpath = os.path.relpath(abspath, repo)
                yield relpath, abspath


def load_index_text(repo):
    path = os.path.join(repo, INDEX_PATH)
    try:
        with open(path, encoding='utf-8') as fh:
            return fh.read()
    except OSError:
        return ''


def decisions_open_ids(repo):
    """Return set of filenames (without .md) in wiki/decisions/open/."""
    d = os.path.join(repo, 'wiki', 'decisions', 'open')
    ids = set()
    if os.path.isdir(d):
        for fname in os.listdir(d):
            if fname.endswith('.md'):
                ids.add(fname[:-3])
    return ids


# ---------------------------------------------------------------------------
# Report accumulator.
# ---------------------------------------------------------------------------

class Report:
    def __init__(self):
        self.errors = []
        self.warns = []
        self.infos = []

    def error(self, path, msg):
        self.errors.append((path, msg))

    def warn(self, path, msg):
        self.warns.append((path, msg))

    def info(self, path, msg):
        self.infos.append((path, msg))

    def has_errors(self):
        return bool(self.errors)

    def print_report(self):
        print("=" * 70)
        print("senselint — ai-semantics wiki verification report")
        print("=" * 70)

        if self.errors:
            print(f"\n### ERROR ({len(self.errors)} issues) ###\n")
            for path, msg in self.errors:
                print(f"  [ERROR] {path}")
                print(f"          {msg}")
        else:
            print("\n### ERROR — none ###")

        if self.warns:
            print(f"\n### WARN ({len(self.warns)} issues) ###\n")
            for path, msg in self.warns:
                print(f"  [WARN]  {path}")
                print(f"          {msg}")
        else:
            print("\n### WARN — none ###")

        if self.infos:
            print(f"\n### INFO ({len(self.infos)} notes) ###\n")
            for path, msg in self.infos:
                print(f"  [INFO]  {path}")
                print(f"          {msg}")
        else:
            print("\n### INFO — none ###")

        print("\n" + "=" * 70)
        total = len(self.errors) + len(self.warns) + len(self.infos)
        print(f"Summary: {len(self.errors)} error(s), {len(self.warns)} warning(s), "
              f"{len(self.infos)} info(s)  [total issues: {total}]")
        print("=" * 70)


# ---------------------------------------------------------------------------
# Check routines.
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = ['type', 'id', 'title']

def check_front_matter(relpath, meta, parse_err, report, is_findings):
    """Check 1: front-matter presence and required fields."""
    if parse_err and not meta:
        level = report.error if is_findings else report.warn
        level(relpath, f"front-matter parse problem: {parse_err}")
        return False  # can't do further checks

    if parse_err:
        # partial parse — warn and continue
        report.warn(relpath, f"front-matter parse warning: {parse_err}")

    if not meta:
        level = report.error if is_findings else report.warn
        level(relpath, "missing front-matter block")
        return False

    ok = True
    for field in REQUIRED_FIELDS:
        if field not in meta:
            level = report.error if is_findings else report.warn
            level(relpath, f"front-matter missing required field: '{field}'")
            ok = False
    return ok


def check_meaning_senses(relpath, meta, allowed_tags, report):
    """Check 2: meaning-senses present and from controlled vocabulary."""
    senses = meta.get('meaning-senses')
    if not senses:
        report.error(relpath, "missing 'meaning-senses' (must declare ≥1 entry from wiki/meaning-senses.md)")
        return

    if not isinstance(senses, list):
        report.error(relpath, f"'meaning-senses' is not a list: {senses!r}")
        return

    # Flatten any nested lists (e.g. contingent-on: [[]]) — guard
    flat = []
    for s in senses:
        if isinstance(s, list):
            flat.extend(s)
        elif s is None:
            pass
        else:
            flat.append(s)

    if not flat:
        report.error(relpath, "meaning-senses list is empty; must have ≥1 entry")
        return

    for tag in flat:
        if tag is None:
            continue
        tag_str = str(tag).strip()
        if not tag_str:
            continue
        if not is_valid_sense(tag_str, allowed_tags):
            report.error(relpath,
                f"meaning-senses tag '{tag_str}' not in controlled vocabulary "
                f"(allowed: {sorted(allowed_tags)})")


def check_links(relpath, meta, repo, report):
    """Check 3: typed links have allowed relations and resolvable targets."""
    links = meta.get('links')
    if not links:
        return  # no links — nothing to check

    if not isinstance(links, list):
        report.warn(relpath, f"'links' is not a list: {links!r}")
        return

    for entry in links:
        if entry is None:
            continue
        if not isinstance(entry, dict):
            report.warn(relpath, f"link entry is not a mapping: {entry!r}")
            continue

        rel = entry.get('rel')
        target = entry.get('target')

        if rel is None:
            report.error(relpath, f"link entry missing 'rel': {entry}")
        elif str(rel) not in ALLOWED_RELATIONS:
            report.error(relpath,
                f"link relation '{rel}' not in allowed set {sorted(ALLOWED_RELATIONS)}")

        if target is None:
            report.error(relpath, f"link entry missing 'target': {entry}")
        else:
            _, err = resolve_link_target(str(target), repo)
            if err:
                report.error(relpath, err)


def check_anchor_discipline(relpath, meta, repo, report):
    """Check 4: claim/result pages must have an anchors link to resource OR anchor:pending + contingent-on."""
    page_type = meta.get('type', '')
    if page_type not in ('claim', 'result'):
        return

    links = meta.get('links') or []
    has_anchors_link = any(
        isinstance(lk, dict) and str(lk.get('rel', '')) == 'anchors'
        and str(lk.get('target', '')).startswith('resource/')
        for lk in links
    )

    anchor_field = meta.get('anchor')
    contingent_on = meta.get('contingent-on') or []
    # Flatten contingent-on (may be [[]] due to template default)
    if isinstance(contingent_on, list):
        flat_co = [x for x in contingent_on if x is not None and x != [] and str(x).strip()]
    else:
        flat_co = [contingent_on] if contingent_on else []

    anchor_norm = str(anchor_field).strip().lower() if anchor_field else ''
    anchor_pending = (anchor_norm == 'pending')
    # Terminal states: a result that makes NO human-comparison claim by ratified
    # design needs no resource anchor. This is an explicit, auditable declaration
    # (ratified case-by-case by Tom), replacing the ambiguous 'pending' for results
    # whose force is a within-model internal contrast. See CLAUDE.md §Typed links /
    # anchor discipline; introduced 2026-05-31 when conflicting-cue-human-anchor was
    # resolved (the internal-contrast-only off-ceiling/bridge results).
    anchor_terminal = anchor_norm in ('internal-contrast-only',)

    if not has_anchors_link:
        if anchor_pending and flat_co:
            # Acceptable: marked as pending with contingency
            # Check if there's a matching decisions/open/ entry
            open_ids = decisions_open_ids(repo)
            for cid in flat_co:
                cid_str = str(cid).strip()
                if cid_str not in open_ids:
                    report.warn(relpath,
                        f"anchor:pending references contingent-on id '{cid_str}' "
                        f"but no matching wiki/decisions/open/{cid_str}.md found")
            report.info(relpath,
                "anchor:pending — human anchor not yet in-repo (contingent-on set)")
        elif anchor_terminal:
            if flat_co:
                report.warn(relpath,
                    "anchor: internal-contrast-only but contingent-on is non-empty "
                    "— a terminal-anchor result should not also be contingent")
            report.info(relpath,
                "anchor: internal-contrast-only — makes no human-comparison claim "
                "by ratified design (no resource anchor required)")
        else:
            report.error(relpath,
                "claim/result page has no 'anchors' link to a resource/ page "
                "and is not marked 'anchor: pending' (with non-empty contingent-on) "
                "or 'anchor: internal-contrast-only'")


def check_contingent_language(relpath, meta, report):
    """Check 5: pages with non-empty contingent-on get an informational note."""
    contingent_on = meta.get('contingent-on') or []
    if isinstance(contingent_on, list):
        flat_co = [x for x in contingent_on if x is not None and x != [] and str(x).strip()]
    else:
        flat_co = [contingent_on] if contingent_on else []

    if flat_co:
        report.info(relpath,
            f"contingent-on is non-empty {flat_co} — review for settled language "
            f"(must remain provisional until Tom ratifies)")


def check_index_coverage(relpath, meta, index_text, report):
    """Check 6: the page's filename or id is mentioned in wiki/index.md."""
    basename = os.path.basename(relpath)
    stem = basename[:-3] if basename.endswith('.md') else basename
    page_id = str(meta.get('id', '')).strip() if meta else ''

    # Check if the filename stem or id appears anywhere in the index text.
    if stem and stem in index_text:
        return
    if page_id and page_id in index_text:
        return
    # Also check just the last path component (e.g. 'formal-competence-aann-ceiling')
    report.warn(relpath,
        f"page not found in wiki/index.md (neither filename '{stem}' nor id '{page_id}' appears there)")


INLINE_LINK_RE = re.compile(r'\]\(([^)]+)\)')

def check_inline_links(repo, report):
    """Check 7: every inline markdown link to a relative .md target must resolve.

    Skips fenced code blocks, external URLs, and non-.md targets. Pure-anchor and
    image links are ignored. This guards the clickable navigation produced by
    tools/linkify.py against bit-rot when pages are renamed or moved.
    """
    wiki_abs = os.path.join(repo, 'wiki')
    for root, dirs, files in os.walk(wiki_abs):
        dirs[:] = [d for d in dirs if d != '.git']
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            abspath = os.path.join(root, fname)
            relpath = os.path.relpath(abspath, repo)
            try:
                with open(abspath, encoding='utf-8') as fh:
                    text = fh.read()
            except OSError:
                continue
            in_fence = False
            for line in text.split('\n'):
                if line.lstrip().startswith('```'):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                for tgt in INLINE_LINK_RE.findall(line):
                    link = tgt.split('#')[0].strip()
                    if not link or link.startswith(('http://', 'https://', 'mailto:')):
                        continue
                    if not link.endswith('.md'):
                        continue
                    resolved = os.path.normpath(os.path.join(os.path.dirname(abspath), link))
                    if not os.path.isfile(resolved):
                        report.error(relpath, f"broken inline link target: '{tgt}'")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="senselint — wiki verification gate")
    parser.add_argument('--repo', default=None,
                        help="repo root (default: auto-detect from script location or cwd)")
    args = parser.parse_args()

    if args.repo:
        repo = os.path.abspath(args.repo)
    else:
        # Try to find repo root: go up from this script's location looking for wiki/
        script_dir = os.path.dirname(os.path.abspath(__file__))
        candidate = os.path.dirname(script_dir)  # parent of tools/
        if os.path.isdir(os.path.join(candidate, 'wiki')):
            repo = candidate
        elif os.path.isdir(os.path.join(script_dir, 'wiki')):
            repo = script_dir
        else:
            # Fall back to cwd
            repo = os.getcwd()

    print(f"Repo root: {repo}")
    print(f"Scanning wiki/ and checking all gates...\n")

    report = Report()

    # Load vocabulary
    allowed_tags, vocab_err = load_allowed_senses(repo)
    if vocab_err:
        report.warn('(senselint)', f"could not load meaning-senses vocabulary: {vocab_err}")
    if not allowed_tags:
        report.warn('(senselint)', "meaning-senses vocabulary is empty — all tags will be flagged")

    # Load index text
    index_text = load_index_text(repo)
    if not index_text:
        report.warn('(senselint)', f"could not read {INDEX_PATH} — index coverage check skipped")

    # -----------------------------------------------------------------------
    # Check all wiki/findings/ pages (full checks, errors on violations).
    # -----------------------------------------------------------------------
    findings_count = 0
    for relpath, abspath in collect_findings_pages(repo):
        findings_count += 1
        meta, parse_err = parse_front_matter(abspath)

        ok = check_front_matter(relpath, meta, parse_err, report, is_findings=True)

        if meta and ok:
            check_meaning_senses(relpath, meta, allowed_tags, report)
            check_links(relpath, meta, repo, report)
            check_anchor_discipline(relpath, meta, repo, report)
            check_contingent_language(relpath, meta, report)

        if index_text:
            check_index_coverage(relpath, meta or {}, index_text, report)

    # -----------------------------------------------------------------------
    # Check all wiki/base/ pages (warnings only on missing front-matter).
    # -----------------------------------------------------------------------
    base_count = 0
    for relpath, abspath in collect_base_pages(repo):
        base_count += 1
        meta, parse_err = parse_front_matter(abspath)

        ok = check_front_matter(relpath, meta, parse_err, report, is_findings=False)

        if meta and ok:
            # Links are checked even on base pages (they can have links)
            check_links(relpath, meta, repo, report)
            # Index coverage
            if index_text:
                check_index_coverage(relpath, meta or {}, index_text, report)

    # -----------------------------------------------------------------------
    # Inline-link integrity across all of wiki/ (check 7).
    # -----------------------------------------------------------------------
    check_inline_links(repo, report)

    print(f"Scanned {findings_count} findings page(s) and {base_count} base page(s).")
    print()

    report.print_report()

    sys.exit(1 if report.has_errors() else 0)


if __name__ == '__main__':
    main()
