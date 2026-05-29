# Run record — CxNLI base-vs-distinction probe v1

**Date:** 2026-05-29
**Open question this answers:** [`open-question/constructional-divergence-probe`](../../../wiki/findings/open-questions/constructional-divergence-probe.md) — "what minimal project-run probe would turn the external constructional-divergence gap into a project result?"
**External claim it operationalizes:** [`claim/constructional-divergent-form-generalization-gap`](../../../wiki/findings/claims/constructional-divergent-form-generalization-gap.md) (Scivetti's >40% GPT-o1 drop on syntactically-identical/semantically-divergent forms).
**Result page:** [`result/cxnli-distinction-divergence-v1`](../../../wiki/findings/results/cxnli-distinction-divergence-v1.md)

## What ran

The project panel ([`config/models.md`](../../../config/models.md)) run **as subjects** on Scivetti's own NLI items, measuring per-construction **base (Exp1, CxNLI) vs. distinction (Exp2, CxNLI-Distinction)** accuracy — the base-vs-distinction *drop* Scivetti reports as >40% for GPT-o1.

- **Instrument:** NLI (0/1/2), the ratified instrument ([`decisions/resolved/constructional-divergence-operationalization`](../../../wiki/decisions/resolved/constructional-divergence-operationalization.md)). Same system prompt as the comparative-correlative probe (one instrument across both project probes). No logprobs (panel exposes none); temperature 0 greedy + parse.
- **Items:** the **5 argument-structure constructions present in BOTH experiments** (causative-with, caused-motion, conative, intransitive-motion, resultative). Distinction = all 100 Exp2 items (20/cxn). Base = the first 20 Exp1 items per construction (by item number), fixed before the run, so base and distinction are N-matched (100 vs 100).
- **Panel:** A `anthropic/claude-sonnet-4.6`, B `openai/gpt-5.4-mini`, C `google/gemini-3.5-flash` (reasoning enabled, max_tokens 4096).

## License / data handling

The Scivetti repo (`github.com/melissatorgbi/beyond-memorization`) carries **no license**. It is **read in place** from a local clone (`--scivetti-dir`), **not mirrored** into this repo. The committed `raw/*.json` are **redacted**: only `cxn / num / gold / pred / correct` are kept — no premise/hypothesis text. Re-derive by running `probe.py --scivetti-dir` against a local clone.

## Fixed reference points (NOT retuned)

- Scivetti human baselines: Exp1 ≈0.90, Exp2 ≈0.83 (resource page).
- Scivetti published model result: GPT-o1 aggregate drop **>40%** on Exp2; notably GPT-o1 scored *worse* than GPT-4o on Exp2, all well below the 83% human ceiling (source page §5.3).

## Files

- `probe.py` — runner (base + distinction × 3 models), redacts Scivetti text before writing raw.
- `analyze.py` — per-construction + overall base/distinction accuracy and the drop; emits `raw/results.json`.
- `raw/` — redacted scoring outputs + `run_summary.json`.

## Results / cost

See `analyze.py` output, `raw/results.json`, and the cost in `raw/run_summary.json` (recorded in [`config/budget.md`](../../../config/budget.md)). Written up at the result page above.
