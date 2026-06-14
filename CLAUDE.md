# CLAUDE.md — schema and conventions

Read this file every run. It encodes how `ai-semantics` is shaped. The charter is `PROJECT.md` (autonomous-era amendment: §12); the run discipline is `PROTOCOL.md`; the session entry point is `continue-prompt.md`. This file is the day-to-day cheat sheet.

## Always-on rules

1. **Read first, write second.** Start a run by reading `continue-prompt.md`, then `NEXT.md`, then `wiki/index.md`, then only the pages your next action needs. Do not load the whole wiki.
2. **Charter takes precedence.** If something here contradicts `PROJECT.md`, fix this file; don't drift.
3. **Run discipline.** Follow `PROTOCOL.md` end-to-end every run, including the verification gates before commit. **Every autonomous session defaults to workflow mode** — a multiagent dynamic workflow (orchestrator + parallel subagents + an adversarial coherence pass); 2–3 waves unless an explicit end time says otherwise. See `PROTOCOL.md §0` and `§A`. Single-unit mode is the fallback for small or surgical tasks. Workflow mode parallelizes *generation*, never *judgement*: the gates, the human-anchor discipline, the no-fabrication rule, and "surface decisions, never ratify them in the session that opened them" all still bind.
4. **No human subjects.** Tom is the monitor, not a subject. All human bearing comes from existing resources (treebanks, sense-annotated corpora, dictionaries, acceptability sets, construction inventories). See `wiki/base/resources/`.
5. **No silent gate skipping.** When you hit an operationalization or human-anchor question, write a page to `wiki/decisions/open/` with options and a provisional default; mark downstream artifacts contingent; surface in `NEXT.md`. **Ratification is autonomous and cross-session** (`PROJECT.md` §12.3): only a *later* session may ratify, via an independent adversarial-review pass with written rationale, recorded `resolved-by: autonomous (adversarial review)`. Tom's standing override outranks any autonomous ratification.
6. **Modest, realistic claims.** Keep every claim calibrated to its evidence; never inflate for novelty. The project's purpose is to extend **genuine human knowledge and understanding** using AI tools — not to produce publishable research or pad a CV (`PROJECT.md` §1). When in doubt, under-claim, and write the null. Ratifying an anchor or operationalization fixes the *yardstick*, never the *result*.
7. **Two tracks, inter-feeding** (`PROJECT.md` §12.1). The empirical loop and the philosophical exploration are both first-class: empirical results revise essays and theory; essays spawn conjectures. No fixed endpoint; scope may extend outward while meaning — especially lexical and grammatical meaning — stays the focus.
8. **Budget: USD 5.00 per calendar day (UTC)** in OpenRouter spend, tracked as billed `usage.cost` in `config/budget.md`. Pre-flight estimate before any probe; record the actual after.
9. **The website is part of every session.** Update `docs/` (journal entry + home-page status, plus whatever pages the session's work touched) before the final commit — `PROTOCOL.md §5b`. Plain language; glossary-linked; no repo links; never name or refer to the monitor; never state a finding more strongly than the wiki does.
10. **End merged, end clean.** Every session ends commit → push → PR → **squash-merge to `main`**, confirmed (`PROTOCOL.md §6`). If the merge cannot land, "land PR #N" goes at the top of `NEXT.md`. Before stopping, kill every background task/loop the session started and verify a clean process table + clean `git status` (`PROTOCOL.md §7`). **Never detect process completion by name-match** — `pgrep -f`/`pkill -f` on a command substring matches the `claude` launcher and spins forever; prefer the harness's `run_in_background`, or wait on an exact captured PID (`PROTOCOL.md §6b`).

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
| `essay` | `wiki/findings/essays/` | Original philosophical work (the philosophical track's first-class artifact): a position the project argues in its own voice, citing in-repo sources/findings, with explicit revision triggers. Re-examined as evidence moves; revisions are logged in-page, retractions kept visible. |

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
                            # for essay: draft | live | revised | retracted
contingent-on:              # wiki/decisions/open/ ids this depends on; empty if none
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

A `claim` or `result` without at least one `anchors` link to a `resource` is a defect unless **either** (a) explicitly marked `anchor: pending` with a `wiki/decisions/open/` entry it names in `contingent-on:`, **or** (b) explicitly marked `anchor: internal-contrast-only` — a ratified terminal declaration that the result makes **no human-comparison claim** (its force is a within-model contrast), so no resource anchor is required. The terminal state (b) is for results ratified as internal-contrast-only (introduced 2026-05-31 with `decisions/resolved/conflicting-cue-human-anchor`, ratified by Tom; from 2026-06-12 such ratifications follow the autonomous cross-session procedure, `PROJECT.md` §12.3); use it only after such ratification, never to dodge a genuine human-anchor obligation. `senselint.py` check 4 enforces all three states.

## Naming conventions

- Files: kebab-case, `.md`, with `type-` prefix only inside `findings/` where ambiguity exists (e.g. `claim-cxg-…`). Inside type-scoped directories, the prefix is redundant — omit it.
- Ids in YAML are kebab-case, globally unique within a type, stable once cited.
- Concepts in `base/concepts/` use the concept name directly (e.g. `distributional-meaning.md`).
- Source pages in `base/sources/` use `lastname-year-shorttitle.md` (e.g. `bender-koller-2020-climbing.md`).

## Cross-references (clickable links)

The wiki is meant to be **read by clicking page to page**, so inline cross-references are clickable relative markdown links, not inert code spans. Convention: keep the typed reference as the visible label and point it at the target's relative path —

```
[`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md)
[`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md)
[`base/sources/foo.md`](base/sources/foo.md)   # the index.md catalog form
```

- Only link to a target that **exists**; an aspirational mention of a not-yet-created page stays a plain code span until the page exists.
- This is body prose only. The YAML front-matter `links:` block stays `target: type/id` **without** backticks — it is the machine-readable typed-link graph senselint consumes. The two are kept in sync by hand.
- `tools/linkify.py` normalizes references to this form (existence-gated, idempotent); `tools/senselint.py` check 7 fails the build on a broken inline link. Run both at the verification step — you need not hand-format every link if you run `linkify.py` before commit.

## Meaning-sense tagging (mechanical lint)

Every page under `wiki/findings/` must declare at least one entry in `meaning-senses:` drawn from the controlled vocabulary in `wiki/meaning-senses.md`. Inline use of the word "meaning" without a clear referent or sense-tag is a defect — qualify it or replace it.

`tools/senselint.py` enforces this mechanically (check 2). Inline use of the word "meaning" without a clear referent or sense-tag is still a defect the tool cannot catch — qualify it or replace it by hand.

## Verification before commit

`tools/senselint.py` and `tools/linkify.py` now exist; run them, then do the two judgement checks by hand. (Full detail in `PROTOCOL.md §5` and `tools/README.md`.)

1. **senselint** — `python3 tools/senselint.py` reports **0 errors**. Mechanically covers front-matter, meaning-senses vocabulary, typed-link relations + resolution, anchor discipline, index coverage, and inline-link integrity. Expected residue: a WARN on `wanted.md` (no front-matter) and INFO notes on contingent pages.
2. **linkify** — `python3 tools/linkify.py` then `--check` shows 0 remaining: cross-references are clickable links to existing pages.
3. **provenance** (by hand) — every claim/result cites an in-repo `source` or `resource` page that bears on it (not just exists), with quotes matching the source page verbatim. Essays cite in-repo sources/findings the same way; an essay's *original* argument needs no anchor, but any empirical assertion inside it does.
4. **human-anchor** (by hand) — every empirical claim about LLM meaning carries an `anchors:` link to a `resource` page, OR a `wiki/decisions/open/` entry queuing the anchor question.
5. **website-consistency** (by hand) — the `docs/` update for this session exists and states nothing more strongly than the wiki (`PROTOCOL.md §5b`).

## What to write, what not to write

- **Write:** typed claims, nulls, conjectures, summarized sources with page-level provenance, short exact quotes.
- **Do not write:** wholesale source text, paper drafts, marketing copy. The project is finding-centered, not paper-producing.

## When to update this file

When a convention here turns out to be wrong, fix it in the same commit that surfaces the lesson, and note the change in `log.md`. Never silent drift.
