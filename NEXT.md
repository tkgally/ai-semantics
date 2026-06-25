# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25**: sessions 104 + 105 + 106 each spent **$0** (no probe). On the UTC day this
session opens, **check `date -u` first** — if still 2026-06-25, headroom is the full $5 minus any earlier-session spend; a fresh
UTC day resets to $5. Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 106 (JST/UTC 2026-06-25) — EMPIRICAL-leaning workflow. $0, no probe.** Branch even with `main` at start (s105/#158 merged;
no PR to land). `decisions/open/` EMPTY → **no ratification owed**; no Tom override. 1-wave workflow, 2 parallel disjoint subagents +
a fresh read-only adversarial coherence pass (**0 BLOCKERS, 1 SHOULD-FIX [front-matter `depends-on` cycle on the concept revision —
fixed], 1 pre-existing NIT [not this session]**).

- **FROZE the VWSD v2 design** — [`experiments/designs/vwsd-grounding-headroom-v2.md`](experiments/designs/vwsd-grounding-headroom-v2.md),
  implementing the resolved gate [`decisions/resolved/vwsd-grounding-headroom-dv-v2`](wiki/decisions/resolved/vwsd-grounding-headroom-dv-v2.md)
  (ADOPT-DEFAULT) **exactly** (coherence pass: gate-faithfulness PASS, quote integrity PASS, arithmetic PASS). This was the
  explicitly-cleared next step ("a build session is now cleared to author `design/vwsd-grounding-headroom-v2`"). **Freezes the
  YARDSTICK only — $0, no probe, no descriptors generated, no images fetched.** Fixes this design's two left-open judgement calls:
  **N = 120** stratified EN-gold draw (from a ~200 pool, oversampling the under-determined band) and **per-stratum floor ≥ 15**
  (raised from v1's ≥ 8); plus **claude image-arm `max_tokens` 16→512** (condition d), the gemini descriptor-generator prompt
  (barred from naming the referent), the held-out gpt leak-audit procedure, and the pre-image covariate-freeze mechanism. Budget
  pre-flight: the full pipeline **far exceeds $5/day** → an explicit **≈5-UTC-day split** (descriptor+freeze day ≈$4.0 text-only; IMAGE
  2 days; DISTRACT 2 days), with a **mandatory re-measure of claude's raised-`max_tokens` per-call cost** before committing (the ~3×
  placeholder must not drive the go-decision). **The `result/vwsd-grounding-headroom-v2` does NOT exist and is NOT cleared.**
- **Concept revision (phil track, $0):** folded the s105 "argument-structure construction as frame-evoker" reading into
  [`concept/constructional-meaning`](wiki/base/concepts/constructional-meaning.md) (new section + logged revision; inline essay
  citation, **no** front-matter typed link — the coherence pass caught and we removed a `depends-on` cycle, since the essay already
  `depends-on` the concept). No new empirical claim; quote ("the semantic backbone of Construction Grammar") verbatim.
- Added the v2 design to [`wiki/index.md`](wiki/index.md) designs catalog. Resolved-decision count unchanged at **41**; `decisions/open/`
  still **EMPTY**. senselint 0 errors; linkify clean. Website updated (journal + home + plans) with the JST stamp.

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3).
- **Graded-sense-image resource STILL WANTED.** VWSD v2 is the clean follow-up — its design is now **FROZEN (s106)**; only the run
  remains, gated as below.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — **no ratification owed**. (Apply any Tom override first if one appears.)

**Track lean — recent: 102 PHIL · 103 PHIL · 104 PHIL+emp-decision · 105 emp-reconcile[ratify]+PHIL · 106 emp-design+PHIL.** The
empirical loop is **UNGATED and the design is now FROZEN**; the lever is the **build-and-run**, which is **spend-bearing and day-split**.
In rough priority:

1. **EXECUTE VWSD v2 — UTC DAY 1 (descriptor authoring + covariate freeze, text-only, ≈$4.0, NO image touched).** Under the frozen
   design [`experiments/designs/vwsd-grounding-headroom-v2.md`](experiments/designs/vwsd-grounding-headroom-v2.md): (a) fetch +
   checksum the EN test data/gold (commit overlay) and the resized EN test images (**out of git**, fetch-at-runtime only); (b)
   generate the **Option-B visual-form descriptors** over the ~200-item pool's unique candidate images (gemini, low detail), the
   **Option-C leak-audit** scores (held-out gpt), freeze + checksum both to `frozen/descriptors.json` **before any image arm**; (c)
   run the **TEXT/separability arm** + the **Option-A FLOOR arm** (text-only), compute the per-model `sep_i`, **draw the stratified
   N=120 clearing ≥15/stratum**, freeze `run_items.json` + `raw/text.json`. **Pre-flight first; record actual after.** Day-1 ≈$4.0 fits
   the $5 cap; if the pool's unique-image count pushes over, split the descriptor pass across two days (design says so). **Then STOP for a
   fresh independent pre-run-critic GO/NO-GO** against the observed `sep_i`/`leak_i` (condition e) — a NO-GO defers the image arms and
   may legitimately rule the descriptor un-authorable-without-leakage on VWSD (→ reserve for a future graded-image resource). **Build the
   run code by adapting the v1 run dir** `experiments/runs/2026-06-24-vwsd-grounding-headroom-v1/` (run.py / analyze.py / build_items.py).
2. **EXECUTE VWSD v2 — later UTC days (only after the pre-run-critic GO).** **Re-measure claude's raised-`max_tokens=512` per-call cost
   in a small preflight** (condition d; do NOT run on the ~3× placeholder). Then the **IMAGE arm** (≈$6.9 → split ~2 UTC days, ~45–60
   items/day, each sub-batch under the $2.50 single-run flag) and the **DISTRACT arm** (≈$6.9 → ~2 UTC days). **DISTRACT null reported
   FIRST.** Then write `result/vwsd-grounding-headroom-v2` + an independent post-run verifier; the conjecture
   [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) stays
   `proposed` until the result lands.
3. **PHILOSOPHICAL fallback ($0), if leaning phil or as the wave's second unit:** a primary OA ingest — still-wanted charter-core
   **Goldberg 2006 *Constructions at Work*** (P1; Google-Books id `LHrcqeZmUN4C` noted, not read) or **Croft 2001** (P2); mark
   `unreachable`/`secondary-only` honestly if the full text can't be reached. Or a short **theory page** connecting the now-in-concept
   frame-evoker thread to the project's empirical caused-motion/way results (disjoint from the two existing essays + the revised concept).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Sessions 104 + 105 + 106 each spent **$0** (UTC day 2026-06-25; full $5 untouched at session 106's close, modulo any later spend).
- Plain-language: this session wrote out **in full and locked** the method for the cleaner re-run of the picture-and-words experiment
  that the last two sessions diagnosed and approved — how each image is described by visual *form* only (not named), the leak audit, the
  calibration check, a larger balanced 120-item sample, and a truncation fix. Locking the *method* runs nothing; the actual experiment
  still needs its descriptions generated, images fetched, a fresh go/no-go check, and (by an honest cost estimate) **roughly five days of
  budget split across days** before it can run. It also brought a reference page up to date with last session's grammar-as-frame idea.

## Reminder for the next cold-start

**You are session 107.** The previous slot was **`s106`** (froze the VWSD v2 design [yardstick only, $0] + a constructional-meaning
concept revision).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u`.
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The empirical loop is **UNGATED and the v2 design is FROZEN**:
the lever is the **spend-bearing, day-split BUILD-and-RUN** — start with **UTC day 1** (descriptors + leak-audit + covariate freeze +
stratified draw, text-only ≈$4.0, NO images), then a **fresh pre-run-critic GO/NO-GO** before any image arm; re-measure claude's raised
`max_tokens` cost before the IMAGE/DISTRACT days. Good $0 phil fallback: **Goldberg 2006 / Croft 2001** ingest or a short **frame-evoker
theory page**. Composition SATURATED + forced-both CLOSED + graded-sense-image resource STILL WANTED — no re-grind. End squash-merged to
`main`, website updated **with the JST clock-time stamp**.
