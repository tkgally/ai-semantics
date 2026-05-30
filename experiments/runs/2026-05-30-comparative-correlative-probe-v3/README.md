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

An **independent read-only adversarial subagent** re-derived every `nli_gold`/`fc_gold` from the sentence text alone (ignoring the build comments). **VERDICT: sound to run as-is — all 16 golds correct, no BLOCKER / SHOULD-FIX, hash unchanged.** It confirmed: the `negation` contradiction golds (the premise denies exactly the positive hypothesis), the `modal-epistemic` neutral golds (the operator raises the relation without asserting it), the `negation-inv` neutral golds (negating a decrease does not entail an increase), and the `baseline-inv` polarity recodes (incl. the double-recode `negi-alarm`). Disclosure NITs (noted, not fixed): (1) **the `negation` arm assumes the strict-proposition reading** — under a weaker pragmatic reading "it is not true that the more they trained the better they performed" denies only a strict/lawlike link and could be read as neutral; the contradiction gold is the intended (strict) reading and is defensible. (2) Several embedded items have a real-world direction a model ignoring the operator would default to (training→performance, exercise→lifespan, etc.) — by design (the trap); no baseline item is accidentally ambiguous (baselines align world-knowledge with the stated direction). (3) Cosmetic plural-subject/singular-verb in three positive hypotheses ("…sales increases") — does not affect any entailment/gold; left as-is to preserve the freeze hash.

## Results / cost

96 calls, **1 NA** (claude NLI on `negi-alarm` over-reasoned past `max_tokens=64` and emitted no digit — the single hardest, doubly-recoded item; FC for the same item is present). Cost **$0.09326 billed** (A $0.01705 / B $0.00419 / C $0.07202) — first run on the corrected harness; gemini billed **14×** its rate-card estimate ($0.072 vs $0.005), the sharpest confirmation yet of the budget-tracking fix.

**Headline: the CC covariation reading mostly survives operator embedding — but not in every model, and the third model cracks under FC via logical OVER-inference (not template-firing).** Per-arm operator-correct rate:
- **claude & gemini track operator scope at/near ceiling.** Both: 100% on `baseline-pos`/`baseline-inv` and on `negation`/`modal-epistemic` (withhold the covariation direction under negation + epistemic hedging). gemini is **100% on every arm, both instruments**. claude's only slips are both on the doubly-recoded `negi-alarm` (FC→DECREASE; NLI→NA). So the v1/v2 robustness is **not** a bare "the-more…the-more → INCREASE" template — it survives the operator that cancels the assertion.
- **gpt-5.4-mini cracks under the FC instrument, via the excluded-middle fallacy.** FC: `negation-inv` **0%** — all three negated-inverse items answered **INCREASE** (treats ¬(X decreases) as entailing X increases); one `negation` item flipped to **DECREASE** (¬increase ⟹ decrease); one `modal` read as asserted (INCREASE). Its NLI is much stronger (only a "unproven ⟹ false" slip on `mod-exercise`). The errors are **over-inference, not template-firing** — it withholds correctly on 3/4 direct negations and is at ceiling on both baselines.

This both supports CC robustness (2/3 models perfect; operator scope genuinely tracked) and localizes a sharp, instrument-dependent failure in the third model to a specific logical error. Reproducible from `raw/results.json`.

**Post-run verification:** every figure independently recomputed from `raw/*.json` by a read-only adversarial subagent (see result page).
