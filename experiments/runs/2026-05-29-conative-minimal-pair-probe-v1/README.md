# Run record — conative minimal-pair probe v1

**Date:** 2026-05-29
**Conjecture this probes:** [`conjecture/conative-construction`](../../../wiki/findings/conjectures/conative-construction.md)
**Design (frozen, pre-registered):** [`design/conative-construction-v1`](../../designs/conative-construction-v1.md)
**Result page:** [`result/conative-minimal-pair-divergence-v1`](../../../wiki/findings/results/conative-minimal-pair-divergence-v1.md)

## What ran

The project panel ([`config/models.md`](../../../config/models.md)) run **as subjects** on the project's **own** verb-held-constant conative minimal pairs, measuring the **affirm completed-contact rate** for the transitive frame (*Maria kicked the ball*) vs. the conative frame (*Maria kicked at the ball*), verb held constant.

- **Instrument:** **both** NLI (0/1/2) and forced-choice (YES/NO/CANT_TELL), the ratified divergence operationalization ([`decisions/resolved/constructional-divergence-operationalization`](../../../wiki/decisions/resolved/constructional-divergence-operationalization.md)). Same NLI system prompt as the comparative-correlative and CxNLI probes. No logprobs (panel exposes none); temperature 0 greedy + parse.
- **Items:** 56, frozen by `build_items.py` **before** the run (`experiments/data/conative/items.csv`, sha256[:16] `9ae53279dc483827`). 12 Levin (1993) conative-class verbs × {typical, atypical} object × {transitive, conative} (48) + 4 non-alternating control verbs × {transitive, conative} (8).
- **Panel:** A `anthropic/claude-sonnet-4.6`, B `openai/gpt-5.4-mini`, C `google/gemini-3.5-flash` (Gemini max_tokens 4096 for the reasoning-token caveat).

## License / data handling

The stimuli are the **project's own** (hand-authored, no third-party license), so the committed `raw/*.json` are **unredacted** — full item id / verb / frame / pred / raw completion are kept for auditability. Re-derive by running `build_items.py` then `probe.py`.

## Pre-registration / no-retuning

- Item set frozen and **committed before any probe call** (charter §8); see the pre-registration commit.
- Verb set revised **before running** after an adversarial coherence pass (bite→stab, peck→strike, swat object fly→cushion); rationale in `build_items.py` header and the design page.
- Thresholds (gap ≥30 pp, atypical within 15 pp) are the **ratified** ones; `analyze.py` reports raw rates without retuning.

## Fixed reference point (NOT retuned)

Levin (1993) conative-alternation class membership (the descriptive premise of P2); Scivetti CxNLI conative subset as the answer-key + aggregate human baseline (≈0.90/0.83) — phenomenon-level, not item-matched (these are the project's own items).

## Files

- `build_items.py` — emits + freezes `experiments/data/conative/items.csv` (run before probing).
- `probe.py` — runner (NLI + FC × 3 models); writes full outputs to `raw/`.
- `analyze.py` — affirm-contact rates, transitive−conative gap, per-verb replication, typical/atypical (P3), control (P2); emits `raw/results.json`.
- `raw/` — full per-call outputs (`nli_{A,B,C}.json`, `fc_{A,B,C}.json`), `results.json`, `run_summary.json`.

## Results / cost

336 calls, **0 NA**. Cost **$0.071** (A $0.049 / B $0.003 / C $0.020), recorded in [`config/budget.md`](../../../config/budget.md). Headline: FC gap 42–88 pp (3/3 models); NLI gap 54–67 pp (2/3); gpt-5.4-mini fails the conative under NLI but recovers under FC. Full write-up at the result page above; every number reproducible from `raw/results.json`.
