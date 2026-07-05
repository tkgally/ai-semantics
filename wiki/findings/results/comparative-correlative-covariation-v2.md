---
type: result
id: comparative-correlative-covariation-v2
title: Comparative-correlative v2 — the v1 ceiling survives off-ceiling stress; the panel follows the construction against world knowledge (~100%) and composes two-step covariation chains (100%, including the diagnostic negative×negative=positive case)
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
  - human-comparison
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-30
updated: 2026-07-05
links:
  - rel: refines
    target: result/comparative-correlative-covariation-v1
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: supports
    target: claim/comparative-correlative-covariation
---

# Result: comparative-correlative probe v2 (off-ceiling)

The off-ceiling follow-up to the v1 CC ceiling positive ([`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md)). Design (frozen): [`design/comparative-correlative-v2`](../../../experiments/designs/comparative-correlative-v2.md); governing operationalization (ratified): [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md); run record: [`experiments/runs/2026-05-30-comparative-correlative-probe-v2/`](../../../experiments/runs/2026-05-30-comparative-correlative-probe-v2/README.md).

## What it tests

v1 showed the panel asserts the covariation direction for ~100% of clear CCs and matched the Scivetti human baseline; its lead caveat is that **ceiling on an easy instrument cannot separate robust competence from task-easiness**. v2 raises difficulty along four arms (graded ladder): `baseline` (clear CC), `conflicting-cue` (real-world direction unambiguous, construction states the **opposite** → does the model follow the construction or world knowledge?), `paraphrase` (same covariation in a non-paired-`the` form), and `multi-step` (two chained CCs; the hypothesis probes the chain endpoints, so the model must **compose** two covariation signs). Indicator: construction/composition-correct rate (FC INCREASE/DECREASE/UNDETERMINED; NLI 0/1/2), both instruments, the 3-family panel.

## One-line finding

**The v1 ceiling survives the off-ceiling stress — it overshoots the "find the breaking point" expectation again.** The panel **follows the construction against conflicting world knowledge at ~100%** (NLI 100% in 3/3; FC 100/83.3/83.3 — a single 1-in-6 slip toward world knowledge for gpt-5.4-mini and gemini), and **composes two-step covariation chains at 100%** (3/3 models, both instruments) — including the diagnostic `multi-bears` item where both steps are negative but the composed answer is **positive** (negative × negative = positive), which a single-clause heuristic would get wrong. So the CC covariation competence is robust, not a brittle template — the strongest positive the project has on the constructional axis.

## Numbers

Construction/composition-correct rate (%), 19 items across 4 arms, 0 NA / 114 calls:

| model | instr | baseline | conflicting-cue (vs world) | paraphrase | multi-step (compose) |
|---|---|---|---|---|---|
| claude-sonnet-4.6 | NLI | 100.0 | 100.0 | 100.0 | 100.0 |
| claude-sonnet-4.6 | FC | 100.0 | 100.0 | 100.0 | 100.0 |
| gpt-5.4-mini | NLI | 100.0 | 100.0 | 100.0 | 100.0 |
| gpt-5.4-mini | FC | 100.0 | 83.3 | 100.0 | 100.0 |
| gemini-3.5-flash | NLI | 100.0 | 100.0 | 100.0 | 100.0 |
| gemini-3.5-flash | FC | 100.0 | 83.3 | 75.0 | 100.0 |

- **conflicting-cue** is the key arm: the construction states a covariation whose real-world direction is the opposite (*"The harder it rained, the less the reservoir filled"* — world knowledge says fuller). Follow-**construction** is ~100% except a single item (16.7% = 1/6) where gpt-5.4-mini and gemini follow **world knowledge** under FC. The panel privileges the stated construction over plausibility.
- **multi-step** composition is 100% everywhere. The set mixes sign products (+×+, +×−, −×−, −×+) and the panel gets the inverse and the double-negative cases right, so it is not a "always assert increase" bias.

## Not just a covariation-asserting bias

Two checks rule out the shallow reading the v1 caveat worried about:
1. **Direction discrimination.** The conflicting-cue and multi-step arms include items whose correct answer is **decrease** (inverse CCs; +×− and −×+ chains); the panel returns DECREASE on those, not a blanket INCREASE.
2. **Genuine composition.** `multi-bears` ("The colder the winter, the **less** the bears foraged. And the less they foraged, the **thinner** they became") has two negative steps composing to a **positive** dim1→dim2 relation; a model reading only one clause would answer *decrease*. All three models answer *increase* (100%) — evidence of actual two-step composition, not last-clause matching.

## Caveats (lead first)

- **Still near-ceiling → still weak evidence for the strongest reading.** Like v1, a ceiling result on a (now harder, but still modest) instrument bounds how strong a "deep covariation reasoning" claim it can support. The only cracks are under FC (gpt/gemini 1/6 conflicting-cue slip; gemini 3/4 paraphrase) — small, not a cliff.
- **No `undetermined`-gold items.** Every item's correct answer is increase or decrease, so the NLI-neutral / FC-UNDETERMINED path is unexercised; an UNDETERMINED-biased model would not be penalized by this run (none showed that bias — all gave directional answers). Noted as a scope limit.
- **Internal-contrast-only on the hard arms; no human baseline.** The `baseline` arm keeps the v1 phenomenon-level Scivetti CC anchor ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)); the conflicting-cue / multi-step arms have **no in-repo human norm** → **no human-level claim** on them (`anchor: internal-contrast-only`, [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). No human label invented.
- **Small N** (19 items × 3 models); direction-of-effect, not precise magnitude.

## Bearing

**Refines** [`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md) (the v1 ceiling is not task-easiness — it survives conflicting-cue + composition). Feeds [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md) *(Superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) — cited here as the edition this page engaged.)*: the CC sits as the project's most robust constructional positive, contrasting with the **shallower** caused-motion coercion-cancellation ([`result/coercion-implicit-cue-v2b`](coercion-implicit-cue-v2b.md)) — both consistent with one disposition: *follow the stated construction over world knowledge*, right for the CC, questionable for the impossible coercion. Internal-contrast-only by ratified decision ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md), 2026-05-31). Cost **$0.109 billed** (token-estimate $0.026 undercounts; see [`config/budget.md`](../../../config/budget.md)); 0 NA / 114 calls.
