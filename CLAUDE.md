# CLAUDE.md — schema and conventions

Read this file every run. It encodes how `ai-semantics` is shaped. The charter is `PROJECT.md` (autonomous-era amendment: §12); the run discipline is `PROTOCOL.md`; the standing program is `wiki/program.md` (adopted 2026-07-02); the session entry point is `continue-prompt.md`. This file is the day-to-day cheat sheet.

## Always-on rules

1. **Read first, write second.** Start a run by reading `continue-prompt.md`, then `NEXT.md`, then `wiki/program.md`, then only the pages your next action needs — navigating via `wiki/index.md`, a tool-generated one-line-per-page catalog (scan or grep the sections you need; never hand-edit its generated part — `tools/build-index.py` owns it). Do not load the whole wiki.
2. **Charter takes precedence.** If something here contradicts `PROJECT.md`, fix this file; don't drift.
3. **Run discipline.** Follow `PROTOCOL.md` end-to-end every run, including the verification gates before commit. **Every autonomous session defaults to workflow mode** — a multiagent dynamic workflow (orchestrator + parallel subagents + an adversarial coherence pass); 2–3 waves unless an explicit end time says otherwise. See `PROTOCOL.md §0` and `§A`. Single-unit mode is the fallback for small or surgical tasks — or one deep unit. Workflow mode parallelizes *generation*, never *judgement*: the gates, the human-anchor discipline, the no-fabrication rule, and "surface decisions, never ratify them in the session that opened them" all still bind. Unit selection is **program-guided** (`wiki/program.md`; `PROTOCOL.md §3`): prefer fewer, deeper units, and when nothing substantive is owed, reconcile, verify, and stop rather than pad.
4. **No human subjects.** Tom is the monitor, not a subject. All human bearing comes from existing resources (treebanks, sense-annotated corpora, dictionaries, acceptability sets, construction inventories). See `wiki/base/resources/`.
5. **No silent gate skipping.** When you hit an operationalization or human-anchor question, write a page to `wiki/decisions/open/` with options and a provisional default; mark downstream artifacts contingent; surface in `NEXT.md`. **Ratification is autonomous and cross-session** (`PROJECT.md` §12.3): only a *later* session may ratify, via an independent adversarial-review pass with written rationale, recorded `resolved-by: autonomous (adversarial review)`. Tom's standing override outranks any autonomous ratification.
6. **Modest, realistic claims.** Keep every claim calibrated to its evidence; never inflate for novelty. The project's purpose is to extend **genuine human knowledge and understanding** using AI tools — not to produce publishable research or pad a CV (`PROJECT.md` §1). When in doubt, under-claim, and write the null. Ratifying an anchor or operationalization fixes the *yardstick*, never the *result*.
7. **Two tracks, inter-feeding** (`PROJECT.md` §12.1). The empirical loop and the philosophical exploration are both first-class: empirical results revise essays and theory; essays spawn conjectures. No fixed endpoint; scope may extend outward while meaning — especially lexical and grammatical meaning — stays the focus.
8. **Budget: USD 5.00 per calendar day (UTC)** in OpenRouter spend, tracked as billed `usage.cost` in `config/budget.md`. Pre-flight estimate before any probe; record the actual after. The cap is a ceiling, not a target — a claim-carrying probe uses powered N (~100–150 items, `PROTOCOL.md §4`), and chronic under-use on load-bearing lines is itself a defect.
9. **The website rolls up daily** (`PROTOCOL.md §5b`; amended by Tom 2026-07-02). One journal entry per JST calendar day: a session that lands substantive work (spend, or findings/essays/theory/decision changes) **creates or extends today's entry**, refreshes the home-page status block, and replaces "The latest" with the day's entry; a maintenance-only session skips the site. Plain language; glossary-linked; no repo links; never name or refer to the monitor; never state a finding more strongly than the wiki does. Datelines carry the date and session number(s) only — the clock-stamp mandate was dropped 2026-07-02 (`tools/session-clock.sh` stays available, optional).
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
| `essay` | `wiki/findings/essays/` | Original philosophical work (the philosophical track's first-class artifact): a position the project argues in its own voice, citing in-repo sources/findings, with explicit revision triggers. Re-examined as evidence moves; revisions are logged in-page, retractions kept visible. New essays must clear the bar in `PROTOCOL.md §3` (fired trigger, new literature, or new falsifiable bet). |
| `note` | `wiki/findings/notes/` | A session record containing **no new measurement** — build gates, calibration GO/NO-GOs, $0 re-analyses, method records (added 2026-07-02, program B6). Keeps the audit trail without inflating the evidence base; a `note` is never cited as sole support for a claim. |

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
                            # for note: recorded
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

**Essay status discipline** (documented 2026-07-05, s183, from corpus practice — the dominant
convention made explicit): front-matter `status:` is authoritative, and the opening blockquote's
first line restates it with the original dates kept visible (e.g. `**Status: revised (drafted
2026-06-20; revised 2026-06-23 …)**`). A dated in-page Revision/Update block that **changes,
scopes, or corrects content** ⇒ `status: revised`; a pure-confirmation trigger annotation may
leave `draft`. A fired trigger gets its `→ FIRED …` annotation **at the trigger itself** (not
only in a revision block). `updated:` equals the date of the newest dated change. The two July
presupposition essays' blockquote-free **Thesis.**-plus-revision-log opening is a blessed
variant.

**Result and theory status discipline** (ratified 2026-07-06, s184, autonomous cross-session
adversarial review — [`decisions/resolved/result-status-upgrade-semantics`](wiki/decisions/resolved/result-status-upgrade-semantics.md);
fresh reviewer + non-Anthropic vote both ADOPT-A). A `result` page's `status:` describes the
**reading's lifecycle**, and only a **recorded dated event** moves it — a replication, a promotion
review citing it, or a contested/retired call, noted in-page with the session and ground. Two kinds
of result sort differently:

- **Reading-bearing results** (an interpretive confirm / mechanism / beater reading): the honest
  resting state is `proposed` — what is `proposed` is the *reading*, not the numbers. When such a
  line replicates and survives its controls, `supported` is earned by the **promotion review that
  writes the `claim`** and lives **on the claim layer**; the result page itself stays `proposed`
  (or moves to `contested`/`retired`). So a replicated-and-promoted result is still `proposed`,
  with support migrated to its claim — the flagship pattern (`result/comparative-correlative-covariation-v1`
  is `proposed`; `claim/comparative-correlative-covariation` is `supported`).
- **Mechanical-gate / feasibility / calibration results** (the finding *is* a check that passed or a
  build/feasibility outcome): `supported` may be the honest description, and such a page **may be
  created at `supported`** — the in-page gate outcome is itself the dated recorded event (no
  artificial create-`proposed`-then-annotate two-step).

`supported`-at-creation is **deprecated for reading-bearing results** going forward; the ~15
existing `supported`-at-creation result pages are **not mass-edited** — each gets a one-line dated
normalization note (keep `supported` if a genuine gate, else set `proposed`) **at its next touch**.
Result front-matter `status` is therefore **non-ranking and possibly-stale until normalized**: it is
not a strength ordering, and readers/tools must not treat it as one — the page's opening blockquote
and the claim layer are authoritative (`senselint.py` does not read `status`). Untouched siblings in
one line may sit at divergent statuses until normalized; that is expected, not a contradiction.
`theory` syntheses may move `draft → live` at their **next substantive touch** (a `live` page that
later gains a `supersedes` successor becomes `superseded`) — deferred to each page's next
substantive edition, not applied in a maintenance pass. The `claim` convention (`supported` earned
by the promotion review) and the `conjecture` axis (`proposed | designed | tested | retired`) are
untouched by this rule.

## Typed links

Use only these relation strings in `links:` and in inline prose where typing matters:

- `supports` — page A makes B more likely.
- `contradicts` — page A makes B less likely.
- `refines` — page A is a sharpening of B.
- `depends-on` — page A presupposes B (resource, anchor, or earlier claim).
- `operationalizes` — page A turns construct B into an indicator. Its target **may be a
  `design/<id>` artifact** (a frozen design under `experiments/designs/`, outside the wiki type
  system) — this is a blessed exception (s184, wiki-coherence P2): a conjecture/result is
  operationalized by the frozen design that turns it into a probe, and `senselint.py` tolerates the
  `design/` target. All other typed-link targets stay in-wiki (`type/id`).
- `anchors` — page A declares B as the human resource grounding it (used **on** the
  `claim`/`result`/`conjecture`/`open-question` page, **targeting** a `resource` — corrected
  2026-07-05 s183: this line previously stated the reverse direction, contradicting universal
  practice and what `senselint.py` check 4 actually enforces).
- `supersedes` — page A replaces B (for theory revisions).

**Edition citations** (documented 2026-07-05, s183). When a theory page is superseded (new `-v2`
page with a `supersedes` link; old page banner + `status: superseded`), inbound references are
**not** mass-retargeted: quotes and historical engagements keep citing the edition they quote —
the v1 stays a legitimate citation target for provenance, and its banner routes readers to the
live edition. Only prose that presents the superseded edition **as the current position** gets a
one-time bracketed edition pointer at first use (`*(superseded sNNN by … — cited here as the
edition this page engaged)*`). Front-matter links to the old edition stay as historical graph
edges.

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

Run the three tools, then do the judgement checks by hand. (Full detail in `PROTOCOL.md §5` and `tools/README.md`.)

1. **build-index** — `python3 tools/build-index.py` regenerates the `wiki/index.md` catalog from front-matter (one line per page); new/renamed pages self-register. Hand-edit only the header above its markers.
2. **senselint** — `python3 tools/senselint.py` reports **0 errors**. Mechanically covers front-matter, meaning-senses vocabulary, typed-link relations + resolution, anchor discipline, index coverage, and inline-link integrity. Expected residue: a WARN on `wanted.md` (no front-matter) and INFO notes on contingent pages.
3. **linkify** — `python3 tools/linkify.py` then `--check` shows 0 remaining: cross-references are clickable links to existing pages.
4. **provenance** (by hand) — every claim/result cites an in-repo `source` or `resource` page that bears on it (not just exists), with quotes matching the source page verbatim. Essays cite in-repo sources/findings the same way; an essay's *original* argument needs no anchor, but any empirical assertion inside it does.
5. **human-anchor** (by hand) — every empirical claim about LLM meaning carries an `anchors:` link to a `resource` page, OR a `wiki/decisions/open/` entry queuing the anchor question.
6. **website-consistency** (by hand) — if this session landed substantive work, today's `docs/` journal entry exists (created or extended) and states nothing more strongly than the wiki (`PROTOCOL.md §5b`).

## What to write, what not to write

- **Write:** typed claims, nulls, conjectures, notes (method records), summarized sources with page-level provenance, short exact quotes.
- **Do not write:** wholesale source text, paper drafts, marketing copy. The project is finding-centered, not paper-producing.

## Program discipline (one-liners; full rules in `PROTOCOL.md §3–§4`)

- Replicated + controlled results get queued **promotion reviews** → `claim` pages (cross-session, adversarial). The claims layer is what compounds.
- A `theory` page with >3 update boxes gets a **clean second edition** (`supersedes` link) at the next touch.
- A new `essay` needs a fired trigger, new literature, or a new falsifiable bet — else revise in-page.
- After 3 null-yielding instrument redesigns on one construct, a cross-session review decides whether the line continues.
- Every registered bet gets a row in `wiki/predictions.md`; outcomes update it the same session.
- Claim-carrying probes use powered N (~100–150 items); ratifications and pre-run critiques route one vote through a non-Anthropic panel model.

## When to update this file

When a convention here turns out to be wrong, fix it in the same commit that surfaces the lesson, and note the change in `log.md`. Never silent drift.
