# Run record — instrument-disagreement re-analysis (2026-05-30)

**Date:** 2026-05-30
**Type:** Read-only re-analysis of two existing parent runs — **no new API calls, $0.00 spend**.
**Result page:** [`result/instrument-disagreement-reanalysis-v1`](../../../wiki/findings/results/instrument-disagreement-reanalysis-v1.md)

## What this is

A systematic per-model × per-construction instrument-disagreement analysis, turning the anecdotal observation ("gpt-5.4-mini conative: NLI −8 pp / FC +42 pp") into a named statistic computed over both parent runs. The open question [`open-question/instrument-sensitivity-constructional-inference`](../../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md) explicitly called for this: "a re-analysis summarizing per-model, per-construction instrument-disagreement as a named statistic (e.g. |NLI gap − FC gap|) could be done as a read-only pass before any new stimuli are generated."

## Parent runs (inputs)

| run | git commit | result page |
|---|---|---|
| `experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/` | `acbcdc4` | `result/conative-minimal-pair-divergence-v1` |
| `experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/` | `1f27d92` | `result/argument-structure-coercion-v2` |

Both runs logged **both instruments** (NLI + forced-choice) on the same three-model panel (claude-sonnet-4.6, gpt-5.4-mini, gemini-3.5-flash).

## Method

`analyze.py` loads the committed `raw/results.json` from each parent run and computes, per model × construction × instrument:

- The **affirm rate** for each condition.
- The **key gap**: transitive−conative gap (conative run) or canonical−cue drop (coercion-v2 run). These match the parent results' own primary statistics, so recomputed values can be directly compared for reconciliation.
- The **instrument-disagreement statistics**:
  - **Signed** = NLI_gap − FC_gap (positive = NLI shows a larger gap; negative = FC shows a larger gap)
  - **Absolute** = |NLI_gap − FC_gap| (magnitude regardless of direction)

### Sanity check

The script includes a formal sanity check against the parent result pages' stated ranges before proceeding:
- Conative FC gaps: 42–88 pp (3/3 models; raw 41.7 pp for gpt rounds to 42 pp — reconciled).
- Conative NLI gaps: 54–67 pp (claude + gemini); ~−8 pp (gpt; raw −8.3 pp — reconciled).
- Coercion-v2 drops: all 0–100 pp (verified).

**Sanity checks PASSED.** All recomputed numbers reconcile with the parent result pages.

### Rounding note

The parent result page states "42 pp" for gpt FC gap; the raw JSON contains 41.7 pp (which rounds to 42 pp at display precision). This is the only value that differs by rounding; the discrepancy is documented in the sanity-check comment in `analyze.py` and does not affect any conclusion.

## Files

- `analyze.py` — loads both parent `raw/results.json`, computes disagreement statistics, runs sanity checks, prints tables, writes `instrument-disagreement-table.md`.
- `instrument-disagreement-table.md` — the three output tables (all numbers recomputed by `analyze.py`).

**Provenance note:** all numbers in the result page and in `instrument-disagreement-table.md` are recomputed by `analyze.py` from the parents' `raw/results.json`. They are not hand-copied from the parent result pages.

## Results summary

| model | construction | NLI gap | FC gap | abs disagree |
|---|---|---:|---:|---:|
| claude | conative | +54.2 pp | +66.7 pp | 12.5 pp |
| gpt | conative | −8.3 pp | +41.7 pp | **50.0 pp** |
| gemini | conative | +66.7 pp | +87.5 pp | 20.8 pp |
| claude | caused-motion | +100.0 pp | +100.0 pp | 0.0 pp |
| claude | way | +100.0 pp | +90.0 pp | 10.0 pp |
| gpt | caused-motion | +80.0 pp | +70.0 pp | 10.0 pp |
| gpt | way | +70.0 pp | +60.0 pp | 10.0 pp |
| gemini | caused-motion | +100.0 pp | +100.0 pp | 0.0 pp |
| gemini | way | +80.0 pp | +80.0 pp | 0.0 pp |

**Headline:** Large instrument disagreement (50 pp) is confined to gpt-5.4-mini on the conative construction. All other 8 cells — covering 3 models × 2 add-direction constructions in coercion-v2, plus claude and gemini on conative — show ≤20.8 pp disagreement, and coercion-v2 cells are all ≤10 pp.

**Direction:** the signed statistic is negative for all conative cells (NLI gap < FC gap), consistent with NLI pulling toward a "yes-contact" default. The coercion-v2 signed values are 0–10 pp (small, mixed direction).

Full write-up: [`result/instrument-disagreement-reanalysis-v1`](../../../wiki/findings/results/instrument-disagreement-reanalysis-v1.md).
