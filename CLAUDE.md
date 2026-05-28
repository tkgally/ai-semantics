# CLAUDE.md — schema and conventions

Read this file every run. It encodes how `ai-semantics` is shaped. The charter is `PROJECT.md`; the run discipline is `PROTOCOL.md`. This file is the day-to-day cheat sheet.

## Always-on rules

1. **Read first, write second.** Start a run by reading `NEXT.md`, then `wiki/index.md`, then only the pages your next action needs. Do not load the whole wiki.
2. **Charter takes precedence.** If something here contradicts `PROJECT.md`, fix this file; don't drift.
3. **Run discipline.** Follow `PROTOCOL.md` end-to-end every run, including the verification gates before commit.
4. **No human subjects.** Tom is the researcher, not a subject. All human bearing comes from existing resources (treebanks, sense-annotated corpora, dictionaries, acceptability sets, construction inventories). See `wiki/base/resources/`.
5. **No silent gate skipping.** When you hit an operationalization or human-anchor question, write a page to `decisions/open/` with options and a provisional default; mark downstream artifacts contingent; surface in `NEXT.md`. A contingent finding is never promoted to settled until Tom ratifies it.

## Page types

Every page under `wiki/findings/` declares its type in a YAML front-matter block. Allowed types:

| Type | Where | Purpose |
|------|-------|---------|
| `source` | `wiki/base/sources/` | Summary of an ingested external source, with page-level provenance. |
| `concept` | `wiki/base/concepts/` | A human-semantics concept (distributional meaning, sense vs. reference, etc.). |
| `resource` | `wiki/base/resources/` | A human-labeled empirical asset: what it is, what it can ground, where it lives. |
| `conjecture` | `wiki/findings/conjectures/` | Proposed but untested claim, with confirmation/falsification criteria. |
| `claim` | `wiki/findings/claims/` | Supported claim with lifecycle status (`proposed`, `supported`, `contested`, `retired`). |
| `result` | `wiki/findings/results/` | Experiment result, linked to its design and data. |
| `theory` | `wiki/findings/theory/` | Synthesis page — the recursive theoretical object. |
| `open-question` | `wiki/findings/open-questions/` | A live, unresolved question that can spawn a loop turn. |

## YAML front-matter schema

Every typed page begins with:

```yaml
---
type: conjecture            # one of the page types above
id: cxg-dative-alternation  # kebab-case, stable, unique within type
title: Human-readable title
meaning-senses:             # required on findings pages; see wiki/meaning-senses.md
  - distributional
  - constructional
status: proposed            # for claim/result: proposed | supported | contested | retired
                            # for conjecture: proposed | designed | tested | retired
                            # for theory: draft | live | superseded
contingent-on:              # decisions/open/ ids this depends on; empty if none
  - []
created: 2026-05-28
updated: 2026-05-28
links:                      # typed links to other pages (see §Typed links)
  - rel: supports
    target: claim/foo
  - rel: depends-on
    target: resource/universal-dependencies
---
```

`base/` pages use the same shape; `meaning-senses` is recommended but not required there.

## Typed links

Use only these relation strings in `links:` and in inline prose where typing matters:

- `supports` — page A makes B more likely.
- `contradicts` — page A makes B less likely.
- `refines` — page A is a sharpening of B.
- `depends-on` — page A presupposes B (resource, anchor, or earlier claim).
- `operationalizes` — page A turns construct B into an indicator.
- `anchors` — page A is the human resource grounding B (only `resource` → `claim/result`).
- `supersedes` — page A replaces B (for theory revisions).

A `claim` or `result` without at least one `anchors` link to a `resource` is a defect unless explicitly marked `anchor: pending` with a `decisions/open/` entry.

## Naming conventions

- Files: kebab-case, `.md`, with `type-` prefix only inside `findings/` where ambiguity exists (e.g. `claim-cxg-…`). Inside type-scoped directories, the prefix is redundant — omit it.
- Ids in YAML are kebab-case, globally unique within a type, stable once cited.
- Concepts in `base/concepts/` use the concept name directly (e.g. `distributional-meaning.md`).
- Source pages in `base/sources/` use `lastname-year-shorttitle.md` (e.g. `bender-koller-2020-climbing.md`).

## Meaning-sense tagging (mechanical lint)

Every page under `wiki/findings/` must declare at least one entry in `meaning-senses:` drawn from the controlled vocabulary in `wiki/meaning-senses.md`. Inline use of the word "meaning" without a clear referent or sense-tag is a defect — qualify it or replace it.

`tools/senselint.py` will eventually enforce this; until it exists, do the check by hand at the verification step.

## Verification before commit (run by hand until tooling exists)

1. **senselint** — every page in `wiki/findings/` has front-matter; every page declares ≥1 `meaning-senses` entry from the controlled vocabulary; nothing whose `contingent-on` is non-empty is written in settled language.
2. **provenance** — every claim/result cites an in-repo `source` or `resource` page that bears on it (not just exists).
3. **human-anchor** — every empirical claim about LLM meaning carries an `anchors:` link to a `resource` page, OR a `decisions/open/` entry queuing the anchor question.
4. **index** — `wiki/index.md` lists every typed page; add new entries.

## What to write, what not to write

- **Write:** typed claims, nulls, conjectures, summarized sources with page-level provenance, short exact quotes.
- **Do not write:** wholesale source text, paper drafts, marketing copy. The project is finding-centered, not paper-producing.

## When to update this file

When a convention here turns out to be wrong, fix it in the same commit that surfaces the lesson, and note the change in `log.md`. Never silent drift.
