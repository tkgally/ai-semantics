# Instrument-disagreement table

Recomputed 2026-05-30 by `analyze.py` from the committed `raw/results.json` of the two parent runs. No new API calls; $0.00 spend.

**Parent runs:**
- `experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/` (git commit `acbcdc4`)
- `experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/` (git commit `1f27d92`)

All figures are recomputed from the raw JSON; arithmetic shown in [Table 1](#table-1) and [Table 2](#table-2); [Table 3](#table-3) is the compact summary.

## Table 1: Conative probe — instrument disagreement on the transitive−conative gap

The 'gap' is the transitive_affirm − conative_affirm difference (pp). Signed = NLI_gap − FC_gap; abs = |NLI_gap − FC_gap|.

| model | NLI trans | NLI conative | NLI gap | FC trans | FC conative | FC gap | signed (NLI−FC) | abs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude | 100.0% | 45.8% | +54.2 pp | 100.0% | 33.3% | +66.7 pp | -12.5 pp | 12.5 pp |
| gpt | 91.7% | 100.0% | -8.3 pp | 91.7% | 50.0% | +41.7 pp | -50.0 pp | 50.0 pp |
| gemini | 100.0% | 33.3% | +66.7 pp | 100.0% | 12.5% | +87.5 pp | -20.8 pp | 20.8 pp |

## Table 2: Coercion v2 — instrument disagreement on the canonical−cue drop

The 'drop' is the canonical_minus_cue_drop (pp). Signed = NLI_drop − FC_drop; abs = |NLI_drop − FC_drop|.

| model | construction | NLI canon | NLI cue | NLI drop | FC canon | FC cue | FC drop | signed (NLI−FC) | abs |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude | caused-motion | 100.0% | 0.0% | +100.0 pp | 100.0% | 0.0% | +100.0 pp | +0.0 pp | 0.0 pp |
| claude | way | 100.0% | 0.0% | +100.0 pp | 100.0% | 10.0% | +90.0 pp | +10.0 pp | 10.0 pp |
| gpt | caused-motion | 80.0% | 0.0% | +80.0 pp | 80.0% | 10.0% | +70.0 pp | +10.0 pp | 10.0 pp |
| gpt | way | 70.0% | 0.0% | +70.0 pp | 80.0% | 20.0% | +60.0 pp | +10.0 pp | 10.0 pp |
| gemini | caused-motion | 100.0% | 0.0% | +100.0 pp | 100.0% | 0.0% | +100.0 pp | +0.0 pp | 0.0 pp |
| gemini | way | 100.0% | 20.0% | +80.0 pp | 100.0% | 20.0% | +80.0 pp | +0.0 pp | 0.0 pp |

## Table 3: Summary — absolute instrument disagreement (|NLI gap − FC gap|) per cell

| model | construction | run | NLI gap | FC gap | abs disagree |
|---|---|---|---:|---:|---:|
| claude | conative | conative-v1 | +54.2 pp | +66.7 pp | 12.5 pp |
| gpt | conative | conative-v1 | -8.3 pp | +41.7 pp | 50.0 pp |
| gemini | conative | conative-v1 | +66.7 pp | +87.5 pp | 20.8 pp |
| claude | caused-motion | coercion-v2 | +100.0 pp | +100.0 pp | 0.0 pp |
| claude | way | coercion-v2 | +100.0 pp | +90.0 pp | 10.0 pp |
| gpt | caused-motion | coercion-v2 | +80.0 pp | +70.0 pp | 10.0 pp |
| gpt | way | coercion-v2 | +70.0 pp | +60.0 pp | 10.0 pp |
| gemini | caused-motion | coercion-v2 | +100.0 pp | +100.0 pp | 0.0 pp |
| gemini | way | coercion-v2 | +80.0 pp | +80.0 pp | 0.0 pp |
