# Run record — comparative-correlative probe v3 (embedded CC / operator scope)

**Date:** 2026-05-30
**Design (frozen, pre-registered):** [`design/comparative-correlative-v3`](../../designs/comparative-correlative-v3.md)
**Governing decision (ratified):** [`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (UNIFY + adopt default; "…defer embedded-CC to v3…"). **No new decision.**
**Conjecture probed:** [`conjecture/comparative-correlative-construction`](../../../wiki/findings/conjectures/comparative-correlative-construction.md)
**Refines:** [`result/comparative-correlative-covariation-v2`](../../../wiki/findings/results/comparative-correlative-covariation-v2.md)
**Result page:** [`result/comparative-correlative-covariation-v3`](../../../wiki/findings/results/comparative-correlative-covariation-v3.md)

## What ran

The embedded-CC follow-up to the v1/v2 CC ceiling positives. v1/v2 probed the CC as an **asserted** relation and found it robust (incl. composition + following the construction against world knowledge). v3 places the identical `the more X, the more Y` **under an operator that cancels/suspends its assertion** — sentential negation ("it is not the case that…") and epistemic hedging ("it remains unproven whether…") — to separate "deploys the covariation meaning + tracks operator scope" from "fires a surface the-more…the-more → INCREASE template."

- **Indicator:** operator-correct rate per arm (FC INCREASE/DECREASE/UNDETERMINED; NLI 0/1/2) against the per-arm, per-instrument gold frozen in `items.csv`. Instrument reused verbatim from v1/v2; temperature 0, no logprobs → existing 3-family panel.
- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C).
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `98d1fd150e36fe30`): 16 items across 5 arms.
- **Cost:** API-**billed** `usage.cost` (via [`experiments/lib/openrouter.py`](../../lib/openrouter.py)), not the rate-card estimate — this is the first run on the corrected harness.

## Arms (graded ladder)

| arm | d | what it tests | FC gold | NLI gold |
|---|---|---|---|---|
| `baseline-pos` | 1 | plain positive CC, asserted (ceiling anchor) | INCREASE | 0 |
| `baseline-inv` | 1 | plain inverse CC — direction anchor (guards against an INCREASE-bias readout) | DECREASE | 2 |
| `negation` | 2 | **key** — negated positive CC; positive covariation denied | UNDETERMINED | 2 |
| `modal-epistemic` | 2 | epistemically-hedged positive CC; relation merely possible | UNDETERMINED | 1 |
| `negation-inv` | 3 | negated *inverse* CC — control vs a flat "any 'not' → UNDETERMINED" rule | UNDETERMINED | 1 |

**Headline (report-the-rate):** the embedding-cancellation rate (off the bare positive direction on embedded arms), per-arm operator-correct rate, and degradation shape d1<d2<d3. FC is primary on the embedded arms (UNDETERMINED gold least contestable); NLI secondary. No pass bar; no threshold tuned after the run.

## Human anchor

**Pending / internal-contrast-only.** The Scivetti CC subset has no negated/hedged CC items → no in-repo human norm on the embedded arms → no human-level claim. Baseline arms keep the v1/v2 phenomenon-level Scivetti CC anchor. No human label invented.

## Pre-registration / no-retuning

- Difficulty axes, per-arm golds, reading rule, and human-anchor scope fixed **before the build**; items frozen + committed **before any probe call** (sha256[:16] `98d1fd150e36fe30`); golds cross-checked by an `assert` in `build_items.py`.
- **Adversarial pre-run pass:** independent read-only subagent re-derived every gold from the sentence text (see below).
- `analyze.py` reports per-arm operator-correct rate + embedding-cancellation rate + degradation; no threshold tuned after the run.

## Files

- `build_items.py` — emits + freezes `experiments/data/comparative-correlative-v3/items.csv` (per-arm gold asserts).
- `probe.py` — runner (NLI + FC × 3 models); imports the shared `experiments/lib/openrouter.py` (records billed `usage.cost`).
- `analyze.py` — per-arm operator-correct rate; embedding-cancellation rate; degradation; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Pre-run critique

_(to be filled from the independent read-only adversarial subagent before the run; re-freeze if any gold is corrected.)_

## Results / cost

_(to be filled after the run + independent post-run number verification.)_
