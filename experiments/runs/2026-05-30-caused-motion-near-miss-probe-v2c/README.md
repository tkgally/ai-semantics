# Run record — caused-motion near-miss form-control probe (v2c)

**Date:** 2026-05-30
**Design (frozen, pre-registered):** [`design/caused-motion-near-miss-v2c`](../../designs/caused-motion-near-miss-v2c.md)
**Governing decision (ratified):** [`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (report-the-rate; the near-miss arm deferred by the coercion v2/v2b designs). **No new decision.**
**Conjecture probed:** [`conjecture/caused-motion-construction`](../../../wiki/findings/conjectures/caused-motion-construction.md)
**Refines:** [`result/caused-motion-minimal-pair-divergence-v1`](../../../wiki/findings/results/caused-motion-minimal-pair-divergence-v1.md)
**Result page:** [`result/caused-motion-near-miss-v2c`](../../../wiki/findings/results/caused-motion-near-miss-v2c.md)

## What ran

The near-miss form-control arm deferred by the off-ceiling coercion v2. v1 found the caused-motion construction's causation-of-motion entailment affirmed onto non-motion verbs at ceiling (90–100%), but its controls were absent-construction. v2c holds the verb + object + displacement **outcome** roughly constant and varies only the **form** — the caused-motion construction vs a coordinated *and*-frame vs a temporal-sequence frame — to test whether the causation inference keys on the **construction form** or on a looser "verb happened + object displaced → caused it" shape.

- **Indicator:** affirm-causation rate per arm (FC YES / NLI entailment 0) against an identical hypothesis ("`<Subj>`'s `<gerund>` caused `<obj>` to move") held constant across the 3 forms within each scene. Instrument reused verbatim from the caused-motion v1/v2b harness; temperature 0, no logprobs → existing 3-family panel.
- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C).
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `a60b812d4b46bcc4`): 24 items = 8 scenes × 3 forms.
- **Cost:** API-**billed** `usage.cost` (via [`experiments/lib/openrouter.py`](../../lib/openrouter.py)).

## Arms

| arm | d | form | example | affirm gold |
|---|---|---|---|---|
| `cm-construction` | 1 | the construction | *Maria sneezed the napkin off the table.* | affirm |
| `near-coord` | 2 | coordinated *and* | *Maria sneezed, and the napkin ended up off the table.* | withhold |
| `near-seq` | 3 | temporal sequence | *Maria sneezed. Moments later, the napkin was off the table.* | withhold |

**Headline (report-the-rate):** per-arm affirm-causation rate + the construction-vs-near-miss **gap** per model per instrument. Large gap ⇒ causation keyed on the construction form; small gap ⇒ the v1 ceiling is not construction-specific. No pass bar; no threshold tuned after the run. The near-miss "withhold" gold labels the entailment-correct direction only; the headline is the within-scene gap (the near-miss withhold reading is pragmatically contestable — Gricean).

## Human anchor

**Pending / internal-contrast-only.** Scivetti has no coordinated/sequence near-miss items → no in-repo human norm on the near-miss arms. The `cm-construction` arm keeps the v1 phenomenon-level caused-motion anchor. No human label invented.

## Pre-registration / no-retuning

- Form contrast, affirm-gold direction, reading rule, human-anchor scope fixed **before the build**; items frozen + committed **before any probe call** (sha256[:16] `a60b812d4b46bcc4`); the hypothesis-identical-across-forms invariant is asserted in `build_items.py`.
- **Adversarial pre-run pass:** independent read-only subagent (see below).
- `analyze.py` reports per-arm affirm rate + construction-vs-near-miss gap; no threshold tuned after the run.

## Files

- `build_items.py` — emits + freezes `experiments/data/caused-motion-near-miss-v2c/items.csv`.
- `probe.py` — runner (NLI + FC × 3 models); imports the shared `experiments/lib/openrouter.py` (billed `usage.cost`).
- `analyze.py` — per-arm affirm rate; construction-vs-near-miss gap; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Pre-run critique

An **independent read-only adversarial subagent** re-derived the affirm-gold direction for all 24 items. **VERDICT: no BLOCKER; all 24 strict-entailment golds agreed.** It raised one **SHOULD-FIX** acted on **before the run**: the original `cm-construction` anchor set was *heterogeneous* — "Ben whistled the dog out of the yard" (animate **signaling**, dog self-moves), "Leo clapped the pigeon off the ledge" (animate **startle**), and "Lena laughed the straw out of the glass" (anomalous, non-conventional coercion) are different/weaker causal relations than clean inanimate propulsion, which would muddy the "construction affirmed at ceiling" anchor (a model withholding on them could be reading the construction correctly, not failing). **Fix applied (re-freeze):** those three scenes were replaced with light inanimate-propulsion scenes (`feather`/`wrapper`/`petal`/`confetti` with puff/huff/blow), so all 8 `cm-construction` items are now uniform physical propulsion; hash updated `6d0b92e39b2d9eb8` → `a60b812d4b46bcc4`. Disclosure NIT (noted, not "fixed" — it is the point): the **`near-coord`** arm carries a strong **Gricean** causation implicature ("X sneezed, **and** the napkin ended up off the table"), so its strict-entailment `withhold` gold tests entailment-over-pragmatics; expect it noisier than `near-seq` ("Moments later…", the cleanest withhold), and read a high near-coord affirm rate as the pragmatics-vs-entailment contrast, not a model error.

## Results / cost

96 calls, **0 NA**. Cost **$0.21213 billed** (A $0.02276 / B $0.00555 / C $0.18382) — gemini again billed ~15× its rate-card estimate ($0.184 vs $0.013), driven by reasoning tokens (139 s, 48 calls). Session probe spend still low single dollars, far under the $20/mo cap.

**Headline: the caused-motion ceiling is genuinely construction-keyed — most sharply under forced-choice.** Affirm-causation rate per arm:
- **`cm-construction` = 100% across all 3 models, both instruments** (the homogeneity fix gave a clean anchor: 8 uniform inanimate-propulsion scenes).
- **Near-miss forms are withheld substantially**, with a large construction-vs-near-miss **gap**: FC gaps **68.8 / 62.5 / 100.0 pp** (claude / gpt-5.4-mini / gemini); NLI gaps **18.8 / 37.5 / 56.2 pp**. So the causation inference is keyed on the **construction form**, not a loose "verb happened + object displaced → caused it" shape — tightening v1's floor. gemini's FC is the cleanest discrimination: construction 100% → both near-miss **0%**.
- **The gap is larger under FC than NLI**, because NLI is more permissive of the **Gricean** causal reading: the coordinated *and*-frame (`near-coord`) is affirmed as causation-entailing at 87.5 / 87.5 / 62.5% under NLI but only 62.5 / 62.5 / 0% under FC; the temporal-sequence frame (`near-seq`) is the **cleaner withhold** (NLI 75 / 37.5 / 25%; FC 0 / 12.5 / 0%) — exactly the pragmatics-vs-entailment, near-coord-noisier pattern the pre-run critic predicted. This is a **general instrument/form effect across all 3 models**, not a single-model crack.

Reproducible from `raw/results.json`. **Post-run verification:** every figure independently recomputed from `raw/*.json` by a read-only adversarial subagent → **CLEAN — all figures verified** (0 NA, all rates over n=8 per cell).
