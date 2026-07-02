# tools/README.md

## linkify.py

`tools/linkify.py` makes the wiki **clickable**: it rewrites in-repo references written as backticked code spans into relative markdown links, so a reader can navigate page-to-page in any markdown viewer.

```
python3 tools/linkify.py          # rewrite in place across wiki/
python3 tools/linkify.py --check  # report-only; exit 1 if anything would change
```

It converts three reference shapes, **only when the target file exists on disk**:

- typed refs — `` `source/foo` ``, `` `claim/bar` ``, `` `conjecture/baz` ``, etc. → the page under the matching `wiki/` directory;
- decision refs — `` `decisions/open/foo` `` (with or without `.md`) → `decisions/open/foo.md`;
- path refs — any backticked relative `.md` path such as `` `base/sources/foo.md` `` or `` `meaning-senses.md` `` (resolved against `wiki/` first, then the repo root) — this is what makes the `index.md` catalog clickable.

The visible label keeps the original backticked text, so `` `source/foo` `` becomes ``[`source/foo`](../../base/sources/foo.md)`` — still reads as a typed reference, now clickable.

Design guarantees:

- **Existence-gated.** Aspirational mentions of not-yet-created pages (e.g. a `decisions/open/` entry a conjecture says it *will* queue) are left as plain code spans, so the tool never creates a dead link.
- **Idempotent.** Already-linkified references are never re-wrapped; safe to run every wave.
- **YAML untouched.** The front-matter `links:` block uses `target: type/id` *without* backticks and is never modified — it remains the machine-readable typed-link graph that senselint consumes. The clickable links are body prose; the typed links are metadata. Both are kept in sync by hand (and verified by senselint checks 3 and 7).

Run `linkify.py` (and `senselint.py`) as part of the verification step before every commit; see `PROTOCOL.md`.

## senselint.py

`tools/senselint.py` is the mechanical verification gate for the `ai-semantics` wiki, implementing the checks described in `PROTOCOL.md §5` and `CLAUDE.md §Verification before commit`.

### How to run

```
python3 tools/senselint.py
```

Run from anywhere inside the repo. The tool auto-detects the repo root by looking for a `wiki/` directory relative to its own location. You can also pass an explicit repo path:

```
python3 tools/senselint.py --repo /path/to/ai-semantics
```

**Exit code:** 0 if no ERRORs; 1 if any ERROR is found. WARNs and INFOs do not affect the exit code.

### What it checks

#### Check 1 — Front-matter presence and required fields

Every `.md` file under `wiki/findings/` must begin with a YAML front-matter block (delimited by `---`) that contains at least:

- `type` — one of the declared page types
- `id` — kebab-case stable identifier
- `title` — human-readable title

Violations in `wiki/findings/` are **ERROR**. For `wiki/base/` pages (concepts, sources, resources), missing front-matter is a **WARN** (stubs are tolerated).

#### Check 2 — meaning-senses vocabulary

Every `wiki/findings/` page must declare at least one tag under `meaning-senses:`. All tags must be drawn from the controlled vocabulary in `wiki/meaning-senses.md`, specifically the `### \`tagname\`` headings under `## Tags`.

Sub-tags are also allowed. A tag like `grounded.perceptual` is valid if its prefix (`grounded`) is in the vocabulary. The vocabulary is parsed dynamically each run; adding a new top-level tag to `meaning-senses.md` immediately makes it valid here.

Violations are **ERROR**.

#### Check 3 — Typed links

Every entry in a page's `links:` list is checked for:

- **Allowed relation:** `rel` must be one of: `supports`, `contradicts`, `refines`, `depends-on`, `operationalizes`, `anchors`, `supersedes`. Unknown relations are **ERROR**.
- **Resolvable target:** `target` must look like `<type>/<id>` and the corresponding file `<type-dir>/<id>.md` must exist in the repo. Dangling targets are **ERROR**.

The type-to-directory mapping used:

| Target prefix | Directory |
|--------------|-----------|
| `source` | `wiki/base/sources/` |
| `resource` | `wiki/base/resources/` |
| `concept` | `wiki/base/concepts/` |
| `claim` | `wiki/findings/claims/` |
| `result` | `wiki/findings/results/` |
| `conjecture` | `wiki/findings/conjectures/` |
| `theory` | `wiki/findings/theory/` |
| `open-question` | `wiki/findings/open-questions/` |
| `design` | `experiments/designs/` |

#### Check 4 — Anchor discipline

Every `claim` or `result` page must satisfy one of:

1. Has an `anchors` link (in `links:`) pointing to a `resource/…` target, **OR**
2. Has `anchor: pending` in its front-matter **AND** a non-empty `contingent-on:` list with a corresponding file in `decisions/open/`.

Violations are **ERROR**. A page with `anchor: pending` and a matching `decisions/open/` entry gets an **INFO** note. If the `contingent-on` id has no matching `decisions/open/<id>.md` file, that is a **WARN**.

#### Check 5 — Contingent-language note

Any page (findings or base) with a non-empty `contingent-on:` list gets an **INFO** note reminding that the page must use provisional, not settled, language until Tom ratifies the open decision. The tool cannot parse prose sentiment, so this is a human-review prompt, not an automated judgment.

#### Check 6 — Index coverage

Every `wiki/findings/` and `wiki/base/` page (by filename stem or `id` field) should appear in `wiki/index.md`. Pages missing from the index are **WARN**.

#### Check 7 — Inline-link integrity

Every inline markdown link in a `wiki/` page that points to a relative `.md` target (e.g. `[`source/foo`](../../base/sources/foo.md)`) must resolve to a file that exists. Broken targets are **ERROR**. External URLs, pure-anchor links, and non-`.md` targets are ignored; fenced code blocks are skipped. This keeps the clickable navigation produced by `linkify.py` (below) from rotting when pages are renamed or moved.

### Output format

The report is grouped into three sections:

```
### ERROR (<n> issues) ###
  [ERROR] wiki/findings/claims/foo.md
          <message>

### WARN (<n> issues) ###
  [WARN]  wiki/base/concepts/bar.md
          <message>

### INFO (<n> notes) ###
  [INFO]  wiki/findings/conjectures/baz.md
          <message>
```

Followed by a one-line summary count.

### Dependencies

Stdlib-only Python 3. The tool tries `import yaml` (PyYAML) for robust front-matter parsing and falls back to a built-in minimal parser if PyYAML is not installed. The minimal parser handles block scalars, block lists, and one-level-deep block mappings — sufficient for all current wiki front-matter.

### Extending senselint

- **New page type:** add the type and its directory to `TYPE_DIR_MAP` in the script.
- **New relation:** add it to `ALLOWED_RELATIONS`.
- **New meaning-sense:** add a `### \`tagname\`` heading under `## Tags` in `wiki/meaning-senses.md`; senselint picks it up dynamically.
- **New check:** add a `check_*` function and call it in `main()` under the appropriate loop.

## session-clock.sh

`tools/session-clock.sh` records how long a session takes, wall-clock, from its start to the
website wind-up — the number reported on the public journal (`PROTOCOL.md §5b`). Sessions carry no
other record of their *start*: the journal stamp, the commits, and the merge all land at the *end*,
so without this the total duration could not be read back.

```
tools/session-clock.sh start            # FIRST action of a session (PROTOCOL §1)
tools/session-clock.sh report [N]       # at the website step (PROTOCOL §5b); N = session number
tools/session-clock.sh start --force    # deliberately reset the start (rarely needed)
```

- **`start`** writes the start epoch to `.session-clock` at the repo root. That file is
  **gitignored and ephemeral** — it lives only inside the run's container and is never committed;
  the duration it feeds is persisted only in the committed journal entry. `start` does **not**
  overwrite an existing clock, so calling it again mid-session (e.g. after a context summary)
  keeps the true start.
- **`report [N]`** reads `.session-clock`, takes *now* as the end, and prints the start and end
  JST clock times, the total elapsed (`Xh Ym`), and a ready-to-paste journal stamp
  (`Month D, YYYY, HH:MM–HH:MM JST (session N) · total Xh Ym`; both dates are spelled out if the
  session crossed JST midnight). If no clock was started it says so and gives an end-only stamp —
  it never invents a duration.

All clock times are Japan time (JST) to match the website convention; elapsed is computed from
epoch seconds, so it is timezone-safe. Stdlib `date` only; no Python.
