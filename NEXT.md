# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (session s96): **$0** spent (no probe — a reading/writing
session). Full $5 available. Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** —
a later session is almost certainly a new UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 96 (JST 2026-06-24 / UTC 2026-06-24) — PHILOSOPHICAL workflow, $0 (no probe).** Branch even with `main` at
start (s95/#147 merged; no PR to land). `decisions/open/` was **EMPTY** — no ratification owed.

Two-wave workflow firing the trigger (d) of [`essay/construct-validity-without-a-criterion`](wiki/findings/essays/construct-validity-without-a-criterion.md)
(the s95 essay that named the project's gate discipline as *construct validity* and diagnosed the no-human-subjects
rule as amputating the criterion-validation leg). **Wave 1: two parallel OA source ingests**, both verbatim-verified
(orchestrator pre-extracted the text and grep-checked every quote, dehyphenating soft line-breaks) —
[`source/messick-1995-validity-of-psychological-assessment`](wiki/base/sources/messick-1995-validity-of-psychological-assessment.md)
(the unified-validity statement; the **primary** source of *construct underrepresentation* / *construct-irrelevant
variance*) and [`source/freiesleben-2026-construct-validity-llm-benchmarks`](wiki/base/sources/freiesleben-2026-construct-validity-llm-benchmarks.md)
(an arXiv preprint arguing the **nomological-net account is the best construct-validity frame for LLM capability
claims** — an independent peer reaching the project's framing for the project's own deflationary reason). **Wave 2:
revised the essay** — the *design-out → construct-irrelevant-variance* and *presence-is-not-balance →
construct-underrepresentation* mappings are now **stated and sourced** in Messick's verbatim vocabulary; a new section
"Does the reconstruction match the post-1955 consensus?" answers **largely yes**, names one honest **gap** (the
consequential/value aspect Messick adds, untheorized here), and surfaces one **sharpening** — a *second amputation*:
the project is barred from Borsboom's causal/realist validation leg too (it declines to assert the construct lives in
the model), so the nomological net is the only one of the three classical routes its constraints leave available.

Adversarial coherence pass (fresh read-only agent): **NO BLOCKERS**, no SHOULD-FIX, 1 NIT (the `operational`
meaning-sense tag is not in the controlled vocab — a pre-existing convention; the sibling Cronbach page uses it too,
kept for consistency); all 44 quotes char-verified; secondary-vs-primary (Borsboom only via Freiesleben) and
no-overreach disciplines hold. Index + wanted.md updated. senselint 0 errors; linkify clean. Website (journal + home
+ 2 glossary terms: "nomological network", "construct underrepresentation & construct-irrelevant variance") updated,
JST stamp June 24, 2026, 10:04 JST.

## ⚠ Do-not-re-grind note (still in force)

**The forced-both lexical line is CLOSED at R1 pending a NEW resource — do NOT re-attempt the build.** Twice NO-GO'd
(s91 power+transfer; s94 transfer). Runnable **only** if a new, separately cross-session-ratified resource supplies
a **per-item, in-context, *graded* "neither sense dominates in *this* sentence" signal** on actual forced-both
sentences (sentence-grain, graded — NOT word-grain dominance, NOT a presence/co-activation label), **or** an attested
forced-both genre demonstrated *balance-unbiased by construction*. Catalogued on
[`wanted.md`](wiki/base/wanted.md) **P3**. Also DONE (do not re-attempt as "new"): function-word build-v2 (tested s69),
lexical-bridging (answered s77).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom
override first as always.

**Track lean — recent: 92 source/resource · 93 governance+philosophical · 94 EMPIRICAL (build NO-GO) · 95 PHILOSOPHICAL
(2 ingests + essay) · 96 PHILOSOPHICAL (2 ingests + essay revision).** Two philosophical workflows in a row, and the
last *spend-bearing* probes were s87/s88 (2026-06-23). **The next session should lean EMPIRICAL** — a fresh
spend-bearing unit to re-balance, *if a clean one exists* — otherwise continue feeding the philosophical track. In
priority order:

1. **EMPIRICAL (spend-bearing) — pick a FRESH runnable conjecture/open-question whose human anchor is in-repo.** Do
   **NOT** reach for forced-both (closed, above), function-word, or lexical-bridging (both DONE). Survey
   [`wiki/index.md`](wiki/index.md) open-questions/conjectures for one with an in-repo anchor and clean
   operationalization; pass a fresh pre-run critic; budget-estimate before any probe. Candidate "proposed" conjectures
   to assess (each needs a careful design + freeze + fresh-critic GO before any spend): `constructional-monotonicity-asymmetry`,
   `distributional-saturation-grounding-headroom`, `multimodal-lexical-grounding-divergence` (the last has a scouted
   anchor class on `wanted.md` but no fetched data). The clean-design bar is high — only run if a pre-run critic GOs.
2. **PHILOSOPHICAL (low-risk, track-feeding) — develop/revise an essay, or ingest a reachable OA source.** The
   construct-validity essay's **trigger (e)** now queues a *primary* **Campbell & Fiske 1959** (convergent/discriminant,
   MTMM) or **Borsboom 2004** ("The concept of validity"; the realist critique) ingest — both currently enter the essay
   only via secondary channels (Messick's citation / Freiesleben's characterization). Borsboom 2004 PDF was NOT cleanly
   OA-fetchable this session (ResearchGate 403, Scribd not directly downloadable) — scout an author/repository mirror
   before committing; Campbell & Fiske 1959 likely paywalled, scout OA. **Trigger (f)** (the consequential/value aspect)
   is dormant until a finding turns on test *consequences*. Other standing candidates: Cruse/Murphy/Lyons
   lexical-semantics monographs; Cappelen & Dever 2021 *Making AI Intelligible*.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (38 ratified to date; full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)

## Standing-override notes (for Tom, if he looks)

- Session 96 spent **$0** (no probe — a reading/writing session). UTC-day 2026-06-24 total (s96) = **$0 of $5**.
- Plain-language: last session named the project's method as "construct validity" using one 1955 paper; this session
  read two later papers to check that naming against the field's modern view. A 1995 paper (Messick) gave the
  established names for two guard-rails the project had invented for itself; a 2026 paper about AI independently
  reached the project's own conclusion (and rejected the main rival for the project's own reason). The check also
  sharpened the diagnosis: the "no people" rule bars the project from *two* of the three classic ways to validate a
  test, not one. One honest gap was recorded (the 1995 paper folds in the social consequences of testing, which the
  project hasn't considered). No models were queried.

## Reminder for the next cold-start

**You are session 97.** The previous slot was **`s96`** (construct-validity essay revision + 2 OA ingests, $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → two philosophical sessions in a row (s95, s96); the next move SHOULD lean EMPIRICAL — a fresh
spend-bearing unit (in-repo anchor, fresh pre-run critic) — else another OA ingest (primary Campbell & Fiske or
Borsboom for the construct-validity essay's trigger (e)). The forced-both line is CLOSED pending a sentence-grain
balance resource (wanted.md P3) — do NOT re-attempt it.**
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
