# Run record — way-construction minimal-pair probe v1

**Date:** 2026-05-29
**Conjecture:** [`conjecture/way-construction`](../../../wiki/findings/conjectures/way-construction.md)
**Design (frozen, pre-registered):** [`design/way-construction-v1`](../../designs/way-construction-v1.md)
**Result page:** [`result/way-construction-traversal-v1`](../../../wiki/findings/results/way-construction-traversal-v1.md)

## What ran

The panel ([`config/models.md`](../../../config/models.md)) as subjects on the project's **own** way-construction stimuli, measuring the **affirm path-traversal rate** on the hypothesis "*&lt;Subj&gt; moved from one place to another.*" for the way-construction frame vs. controls, with the (non-motion) verb held constant.

- **Instrument:** both NLI (0/1/2) and forced-choice (YES/NO/CANT_TELL), the ratified divergence operationalization ([`decisions/resolved/constructional-divergence-operationalization`](../../../wiki/decisions/resolved/constructional-divergence-operationalization.md)). Same prompts as the conative/caused-motion/CC/CxNLI probes; temperature 0; no logprobs (the way design's §2 logprob indicator is unavailable on OpenRouter, so its ratified greedy-completion fallback is used).
- **Items:** 60, frozen by `build_items.py` **before** the run (`experiments/data/way-construction/items.csv`, sha256[:16] `536977843dff18a5`). 18 non-motion verbs (6 manner, 6 activity, 6 anti-motion) × {way, ctrl-loc, ctrl-motion} + 6 idiomatic over-generalization guards.
- **Panel:** A claude-sonnet-4.6, B gpt-5.4-mini, C gemini-3.5-flash (Gemini max_tokens 4096).

## Forms

| form | example | gold traversal |
|---|---|---|
| `way` | Mia whistled her way down the hall. | YES (NLI 0) |
| `ctrl-loc` | Mia whistled in the hall. | CANT_TELL (NLI 1) — discriminating control |
| `ctrl-motion` | Mia walked down the hall, whistling. | YES (NLI 0) — positive floor (motion lexicalized) |
| `idiomatic` | Elena talked her way out of trouble. | CANT_TELL (NLI 1) — over-generalization guard |

Primary indicator: **affirm path-traversal rate**; confirm bar: way ≥70%, gap (way − ctrl-loc) ≥30 pp, in ≥2/3 models, holding for the anti-motion category (P3).

## License / data handling

Stimuli are the **project's own** (no third-party license); committed `raw/*.json` are **unredacted** (full item/verb/form/pred/raw). Re-derive via `build_items.py` then `probe.py`.

## Pre-registration / no-retuning

- Items frozen and **committed before any probe call** (charter §8).
- Revised **before running** after an adversarial pre-run pass (read-only). The pass found BLOCKERS — several path-PPs were temporal/eventive/abstract ("through the afternoon/journey/party/flight"), making the path-traversal gold indefensible; conveyance controls ("on the train/flight") mis-golded the location control; some ctrl-motion sentences were incoherent. Fixes applied **before freezing**: every path-PP made genuinely spatial; locative controls of the same scene (no conveyance); ctrl-motion reframed to "motion-verb main + non-motion gerund adjunct"; the verb *work* (abstract-progress only) demoted to an idiomatic guard. Documented limit S2 (way's directional PP vs ctrl-loc's locative; the bare directional form is ungrammatical for non-motion verbs without the construction) recorded in the result's Limits, not tuned away. Full rationale in `build_items.py` header.
- Thresholds (way ≥70%, gap ≥30 pp, anti-motion holds) are the **ratified/conjecture** ones; `analyze.py` reports raw rates without retuning.

## Files

- `build_items.py` — emits + freezes `experiments/data/way-construction/items.csv`.
- `probe.py` — runner (NLI + FC × 3 models); full outputs to `raw/`.
- `analyze.py` — affirm path-traversal rates, gap vs. ctrl-loc, by verb-category (P3), per-verb, idiomatic guard, ctrl-motion floor; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Results / cost

360 calls, **0 NA**, cost **$0.072** (A $0.052 / B $0.003 / C $0.016), recorded in [`config/budget.md`](../../../config/budget.md). Headline: way path-traversal rate **77.8–100%**, gap (way − ctrl-loc) **77.7–100 pp**, **3/3 models, both instruments**; the anti-motion stress category holds at/near ceiling for every model; idiomatic over-generalization guard **0%** everywhere; ctrl-motion positive floor **100%** everywhere; ctrl-loc near floor (0–11.1%). gpt-5.4-mini is the conservative outlier (declines consumption-verb items *eat/chat/snack/hum* as CANT_TELL). Full write-up at the result page; every number reproducible from `raw/results.json`.
