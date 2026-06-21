# PREREG — REPEATED-RUNS temp-0 jitter measurement (let-alone forced-decomposition)

**Run:** `2026-06-21-scivetti-let-alone-repeated-runs` (session 64).
**Frozen at:** session 64, before any of the K runs were collected.
**Status at freeze:** `prep.py --check` PASS (frozen 63-item sha `1b87dc871e4ec8dd`, full-set
`1c5cffb18c5ef78e`, s60-subset `9be31a8fea8d7f16`, train-LA `6b0c8d82536f25e6` — all byte-identical
to session 62); `NLI_SYS_DECOMP` programmatically confirmed byte-identical to session 60/62 (len 910);
`analyze.py --selftest` PASS.

## Motivation

Session 62 (`result/scivetti-let-alone-powered-rerun-v1`) surfaced **temp-0 run-to-run label
stochasticity** as the new binding precision limit on the let-alone construction — but inferred it from
a **single** cross-session run-pair (s60 → s62): on the identical 24 test items, claude flipped 3/24
(all adverse, 0.833 → 0.708) and gpt flipped 3/24 (net 0, 0.583 → 0.583); gemini was deterministic.
"~12% per run" rests on that one comparison. `essay/point-estimate-is-a-draw` now leans on this figure
as a project-wide reading discipline, and its **revision trigger (a)** explicitly names a repeated-run /
multi-sample measurement as the next step — to pin the jitter magnitude and test whether jitter is
**concentrated at the hard near-chance let-alone** and **negligible at the ceiling control**.

This run **measures the noise floor** with K independent same-session draws of the byte-identical
instrument. It is a licit same-instrument re-run because it measures jitter — it does **not** try to
turn the let-alone null into a positive (`essay/undischargeable-negative`'s threaded needle:
re-running to *measure the floor* buys the floor; re-running to *firm a null* buys nothing).

## Design (single change vs session 62: REPEAT count)

- **Instrument:** `NLI_SYS_DECOMP` forced-decomposition working surface, **byte-identical** to
  sessions 60/62 (len 910, programmatically diff-checked). Same 0/1/2 label definitions, gold not shown.
- **Item set:** the **same frozen 63 items** as session 62 — 24 let-alone test + 9 let-alone train
  (disjoint) + 30 comparative-correlative ceiling control. No item added or removed (all shas match s62).
- **Repeats:** **K = 5** independent draws per (model, item), scored sequentially within this one
  session. Panel A/B/C, **temperature 0**, gemini `reasoning: effort minimal` held constant,
  `max_tokens` 1024 (A/B). Every call is a fresh independent HTTP request; nothing cached/deduped.
- **Committed artifact:** `raw/run{k}-{slot}-labels.json` (run index + item_id + cxn + split + gold +
  parsed label + parse_mode + uptake lengths/booleans + content sha256 + usage — **NO text**). Full CoT
  to `raw/cot/` (gitignored, recipe-not-corpus).

## Pre-registered questions & frozen analysis (`analyze.py`, exists at freeze)

- **Q1 — per-run accuracy spread (the jitter on the headline number).** For each model × cell
  (let-alone combined 33 / test 24 / train 9 / comp-corr 30): the K per-run accuracies and their
  {mean, min, max, **range = max − min**, sample SD}. The across-run range/SD *are* the jitter.
- **Q2 — per-item label stability.** Per-item label counts over K runs; modal label; CONSTANT flag;
  **churn rate** (fraction non-constant); **mean pairwise label agreement** over the C(K,2)=10 run-pairs
  (the symmetric generalization of s62's "21/24 agreement").
- **Q3 — trigger (a): does jitter shrink at the ceiling?** Contrast let-alone range/churn vs comp-corr
  range/churn (frozen reading map below).
- **Q4 — the de-noised / pinned estimate.** Majority-vote accuracy (modal label vs gold) + Wilson CI per
  cell. For **gpt let-alone combined**, does the across-run **MAX** accuracy stay **< 0.90**? (Pins the
  residual the s62 result left at ~±0.12.)
- **Q5 — uptake + ceiling guard.** Each run must have let-alone uptake INDUCED (≥80% worked) and comp-corr
  at/near ceiling (Wilson LB ≥ 0.80) and 0 missing labels; a run breaking either is flagged.
- **Q6 — cross-session corroboration (honest framing).** The K runs are same-session, so their spread is a
  **within-session** figure that may **UNDERESTIMATE** true run-to-run jitter. The s60 (24 LA test + 30 CC)
  and s62 (all 63) draws are **cross-session** (different days). Report s60/s62 accuracies and the extended
  (K + historical) band; note whether cross-session spread exceeds within-session spread.

### Frozen reading map (Q3 — descriptive; no result is retuned)

| read | condition |
|---|---|
| **TRIGGER-A-FIRES** | all runs clean AND let-alone combined range > 0 AND comp-corr range ≤ 0.034 (≤1/30) AND let-alone churn > comp-corr churn → jitter concentrates at near-chance, negligible at ceiling; essay trigger (a) fires (narrow "draws" to *hard near-chance functional* instruments). |
| **JITTER-FLAT** | let-alone range ≈ comp-corr range, both small → the s62 ~12% was a high draw; essay SOFTENS (jitter smaller, not specially near-chance-concentrated). |
| **JITTER-EVERYWHERE** | comp-corr range > 0.034 → jitter not ceiling-protected; essay's "barely bites at ceilings" clause needs revision (would itself be the finding). |
| **GUARD-FAIL** | any run with uptake not induced or control broken → flagged; jitter read restricted to clean runs. |

This map fixes the **interpretation yardstick**, not the result. The headline deliverable is the jitter
**distribution** (Q1/Q2), reported whatever it is.

## Cost & integrity

- **Pre-flight:** K=5 × session-62's **measured** $0.392/run ≈ **$1.96** billed (claude CoT the driver).
  945 finding-bearing calls (5 × 3 × 63). **ABORT_USD = $2.40** (per-invocation cumulative; under the
  $2.50 single-run flag). UTC-day 2026-06-21 spend before this run = **$0.00** of $5.00 → ample headroom.
- **Freeze guard** in `probe.py`: refuses to run unless PREREG.md + analyze.py exist AND `prep.py --check`
  passes (all four shas). Resumable per (run, slot) file; completed files are never overwritten.
- Billed via `usage.cost` (`openrouter.billed_cost`); flag any missing-cost calls.

## Governance — no new decision owed

- Same **ratified** Scivetti answer-key anchor (`resource/scivetti-2025-cxnli-dataset`, ratified
  2026-05-29) and the same ratified `constructional-divergence-operationalization`. This run changes
  **only the repeat count**; it scores the same labels against the same gold. comp-corr carries the
  ratified anchor; let-alone is descriptive from the same release (as s57/58/60/62).
- **No human-comparison claim** beyond pinning the magnitude of an already-reported residual. The run's
  force is a **within-model MEASUREMENT of instrument jitter** — model-internal. No panel change, no new
  indicator, no item selection, no demonstration items.

## Honesty box (frozen)

- Same-session K draws measure a **within-session** jitter floor; true run-to-run jitter (cross-session,
  cross-hardware) may be larger. Reported as a lower bound, with the s60/s62 cross-session draws alongside.
- The ~12% s62 figure is **one instrument's** jitter on one date; this run tests whether it reproduces and
  whether it is near-chance-concentrated — it does **not** establish a transferable constant (that would be
  essay trigger (b), explicitly not claimed).
- This is a measurement, not a re-litigation of the let-alone residual: the let-alone accuracy is read off
  whatever the runs produce; no operationalization is tuned after seeing data.
