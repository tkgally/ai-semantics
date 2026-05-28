# tools/README.md

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
