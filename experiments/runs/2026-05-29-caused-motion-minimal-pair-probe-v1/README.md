# Run record — caused-motion minimal-pair probe v1

**Date:** 2026-05-29
**Conjecture:** [`conjecture/caused-motion-construction`](../../../wiki/findings/conjectures/caused-motion-construction.md)
**Design (frozen, pre-registered):** [`design/caused-motion-construction-v1`](../../designs/caused-motion-construction-v1.md)
**Result page:** [`result/caused-motion-minimal-pair-divergence-v1`](../../../wiki/findings/results/caused-motion-minimal-pair-divergence-v1.md)

## What ran

The panel ([`config/models.md`](../../../config/models.md)) as subjects on the project's **own** caused-motion stimuli, measuring the **affirm caused-motion rate** on "*&lt;Subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move.*" for the caused-motion frame (cm) vs. two controls, with the (non-motion) verb's lexical inability to license motion held constant.

- **Instrument:** both NLI (0/1/2) and forced-choice (YES/NO/CANT_TELL), the ratified divergence operationalization ([`decisions/resolved/constructional-divergence-operationalization`](../../../wiki/decisions/resolved/constructional-divergence-operationalization.md)). Same prompts as the conative/CC/CxNLI probes; temperature 0; no logprobs.
- **Items:** 30, frozen by `build_items.py` **before** the run (`experiments/data/caused-motion/items.csv`, sha256[:16] `ebb37ae501d455ca`). 10 non-motion verbs (5 typical, 5 atypical) × {cm, ctrl-loc, ctrl-sep}. Object-animacy recorded for the inanimate-propulsion-core split.
- **Panel:** A claude-sonnet-4.6, B gpt-5.4-mini, C gemini-3.5-flash (Gemini max_tokens 4096).

## License / data handling

Stimuli are the **project's own** (no third-party license); committed `raw/*.json` are **unredacted** (full item/verb/form/pred/raw). Re-derive via `build_items.py` then `probe.py`.

## Pre-registration / no-retuning

- Items frozen and **committed before any probe call** (charter §8).
- Revised **before running** after an adversarial coherence pass: ctrl-sep gold contradiction→neutral/CANT_TELL (an overt alternative cause does not *contradict* a joint-causation hypothesis); wink→huff (summoning reading too soft); object-animacy split added; shudder/shiver flagged (verbs denote body-motion). Rationale in `build_items.py` header + design page.
- Thresholds (cm ≥70%, gap ≥30 pp, atypical within 15 pp) are the **ratified/conjecture** ones; `analyze.py` reports raw rates without retuning.

## Files

- `build_items.py` — emits + freezes `experiments/data/caused-motion/items.csv`.
- `probe.py` — runner (NLI + FC × 3 models); full outputs to `raw/`.
- `analyze.py` — affirm caused-motion rates, gap vs. controls, typical/atypical (P3), animacy split, per-verb; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Results / cost

180 calls, **0 NA**, cost **$0.044** (A $0.027 / B $0.002 / C $0.015), recorded in [`config/budget.md`](../../../config/budget.md). Headline: cm 90–100%, gap 70–100 pp, 3/3 models, ceiling; the causation-specific control (ctrl-sep) correctly withheld (0–20%). Full write-up at the result page; every number reproducible from `raw/results.json`.
