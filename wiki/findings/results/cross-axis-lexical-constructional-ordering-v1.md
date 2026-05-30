---
type: result
id: cross-axis-lexical-constructional-ordering-v1
title: Cross-axis model-ordering v1 — does a model's lexical gradience strength predict its constructional performance? Only at the bottom (the weakest model is weakest on both); at the top the two axes dissociate, and the same-instrument bridge inverts the order
meaning-senses:
  - constructional
  - referential
  - human-comparison
status: proposed
anchor: pending
contingent-on:
  - conflicting-cue-human-anchor
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: supports
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/coercion-sense-modulation-v1
  - rel: depends-on
    target: open-question/instrument-sensitivity-constructional-inference
---

# Result: cross-axis lexical↔constructional model-ordering v1

**One-line:** a read-only re-analysis (no new data, **no API spend, $0**) tabulating each panel model's **lexical** gradience strength ([`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md), durel Spearman ρ) against its per-model **constructional** numbers across eleven own-design grammatical results. The lexical order (**gemini 0.80 > claude 0.68 > gpt 0.60**) predicts constructional competence **only at the bottom** — gpt-5.4-mini is weakest lexically *and* the most fragile constructionally — but **not at the top**: gemini (strongest lexically) only ties claude on the add-direction positives, and on the one result that runs the *same instrument* on both axes (the coercion-sense-modulation bridge) the order **inverts** (claude > gpt > gemini). So lexical and constructional competence **dissociate** at the model level. Confirms the early "no" the bridge result and [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) flagged.

Run record: [`experiments/runs/2026-05-30-cross-axis-model-ordering/`](../../../experiments/runs/2026-05-30-cross-axis-model-ordering/README.md). Read-only re-analysis (no design page; like [`result/instrument-disagreement-reanalysis-v1`](instrument-disagreement-reanalysis-v1.md)). Advances [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md)'s explicit watch item ("whether the model strongest lexically is also strong on the constructional inference probes").

## What was re-analyzed

[`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) predicts that, if the lexical and grammatical wedges are two grains of one form–meaning cline, the two should **not dissociate sharply** across models: "a model that tracks the meaning gradient at one grain should tend to at the other." It also flagged a concrete watch: gemini is strongest lexically — is it strongest constructionally? This re-analysis answers it by tabulating numbers **already on the in-repo result pages** (each value provenance-tagged to its source result; cross-checked by two independent read-only extraction passes) and reading the per-model **rank order** off each.

- **Lexical predictor:** durel ρ(model, human DURel median) — claude **0.679**, gpt-5.4-mini **0.601**, gemini **0.804** → order **gemini > claude > gpt**.
- **Constructional outcomes:** the per-model headline of eleven own-design results (caused-motion v1, way v1, conative v1 [NLI+FC], CC v1, cxnli-distinction, coercion v2 cue-drop, conative-cancel v2, coercion-implicit v2b, CC v3, caused-motion near-miss v2c, and the **coercion-sense-modulation bridge**).

**Hard caveat, stated up front: with n = 3 models a rank correlation is a blunt descriptive instrument** — only a few distinct orderings exist and no single ρ is significance-testable. The finding is the **pattern of orderings**, not a coefficient. Ceiling-for-all results (caused-motion v1, CC v1) carry no discriminating order and are excluded from the ρ average.

## Result (recomputed from the source pages — see run README for every cited number)

Across the **9 discriminating** (non-ceiling) results, mean ρ(lexical, constructional) = **+0.71**; per-result order vs the lexical order: **MATCH 5, DIVERGE 4, CEILING(excluded) 2**.

| result | per-model order (best→worst) | vs lexical order |
|---|---|---|
| conative-v1 (gap, FC & NLI) | gemini > claude > gpt | **MATCH** |
| conative-cancel-v2 (suppress, FC) | gemini > claude > gpt | **MATCH** |
| coercion-implicit-v2b (WK engagement, FC) | gemini > claude > gpt | **MATCH** |
| caused-motion-near-miss-v2c (gap, FC) | gemini > claude > gpt | **MATCH** |
| way-v1 (affirm, FC) | claude > gemini > gpt | DIVERGE (top two swap) |
| CC-v3 (operator-correct, FC) | claude > gemini > gpt | DIVERGE (top two swap) |
| cxnli-distinction (less drop) | claude > gemini > gpt | DIVERGE (top two swap) |
| **coercion-sense-modulation-v1 (bridge, gap)** | **claude > gpt > gemini** | **DIVERGE (near-inversion)** |
| caused-motion v1, CC v1 | (all ~ceiling) | CEILING |

## Readings

1. **The one robust cross-axis thread is at the *bottom*: gpt-5.4-mini is weakest on both.** It is the weakest lexical tracker (ρ 0.60) and the most fragile model on the constructional side — last or failing on way-v1, the conative (NLI collapse to −8 pp), conative-cancel-v2 (0% suppression under NLI), coercion-implicit-v2b (40%), and CC-v3 (60% FC, the excluded-middle slip). In **every** discriminating result gpt-5.4-mini is ranked last. *That* strand is lexical-order-consistent and drives the +0.71 mean ρ.
2. **The *top* of the order does not transfer — the axes dissociate.** gemini's lexical supremacy (ρ 0.80, above the human inter-annotator 0.69) does **not** make it uniquely strongest constructionally: it ties claude at ceiling on the add-direction positives, and claude beats it on way-v1, CC-v3, and the distinction drop. The mean ρ is carried almost entirely by the shared bottom rank, not by the top.
3. **The same-instrument bridge inverts the order — the sharpest datum.** [`result/coercion-sense-modulation-v1`](coercion-sense-modulation-v1.md) is the only result that runs the *identical* lexical relatedness instrument on constructional stimuli, so it is the fairest cross-axis comparison. There the order is **claude (31.4) > gpt (20.5) > gemini (8.3)** — a near-inversion of the lexical order: **the strongest pure lexical tracker registers the *smallest* coercion-induced sense shift.** A model can be an excellent graded-sense rater yet treat a coerced verb as "still basically the same word." This is the cleanest evidence that lexical-gradience skill and constructional-coercion sensitivity are **distinct competences**.

**Net:** the continuum thesis's "should not dissociate sharply" prediction is **partially disconfirmed**. The grain-to-grain link holds for *failure* (a weak model is weak everywhere) but not for *strength* (the best lexical model is not the best constructional model, and on the most comparable measure the orders invert). The wedges are unified as *targets* (one form–meaning cline) but the underlying model competences are **separable** — exactly what [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) said the behavioral evidence "cannot settle" about a shared *mechanism*, now with a concrete dissociation rather than an open guess.

## Caveats (lead with these)

- **n = 3 models.** This is the binding limit: a 3-point rank order supports only descriptive pattern-reading, never a significance claim. The "+0.71 mean ρ" is reported for transparency, not as evidence — three models give Spearman only a handful of possible values. Read the *orderings*, especially the bottom-rank consistency and the bridge inversion.
- **Heterogeneous metrics.** The constructional numbers are gaps / rates / drops on different scales and instruments; only their *within-result rank* across the three models is used, which is the comparable quantity, but a rank ignores magnitude (several "MATCH" results have gemini and claude near-tied).
- **Ceiling masks order.** Two results are ceiling-for-all and excluded; several "MATCH"/"DIVERGE" calls rest on small per-model differences near ceiling, so the MATCH/DIVERGE split (5/4) is itself fragile.
- **No new data / no human anchor for the cross-axis claim itself.** Each tabulated number keeps its own source page's anchor (the lexical predictor is DWUG-anchored; several constructional rows are internal-contrast-only), but the *ordering* finding makes no new human-comparison claim — it is a model-internal meta-observation. `anchor: pending`; `contingent-on: conflicting-cue-human-anchor` (inherited from the v2 / bridge rows it tabulates).
- **Single run/date** per source result; behavioral, not representational.

## Where it sits

- **Supports** [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) by resolving its flagged watch item — and qualifies the continuum thesis: targets unified, competences dissociated (strongly at the top, invertingly on the bridge).
- **Depends on** the lexical predictor ([`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md)) and the bridge ([`result/coercion-sense-modulation-v1`](coercion-sense-modulation-v1.md)); tabulates the nine other own-design results.
- Adds a cross-axis datum to [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md): gpt-5.4-mini's bottom-rank consistency co-occurs with its instrument-fragility (the conative/CC-v3 cracks), so "weakest tracker" and "most instrument-fragile" are the same model.
