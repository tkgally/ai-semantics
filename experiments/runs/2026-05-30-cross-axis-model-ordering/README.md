# Run record — cross-axis model-ordering re-analysis (2026-05-30)

**Date:** 2026-05-30
**Type:** read-only re-analysis (NO new data, NO API spend, **$0.00**) — like [`instrument-disagreement-reanalysis-v1`](../2026-05-30-instrument-disagreement-reanalysis/README.md).
**Result page:** [`result/cross-axis-lexical-constructional-ordering-v1`](../../../wiki/findings/results/cross-axis-lexical-constructional-ordering-v1.md)

## Question (NEXT.md backlog unit 3)

Does each panel model's **lexical** gradience strength ([`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md)) predict its **constructional** performance across the project's own-design grammatical results? The bridge result ([`result/coercion-sense-modulation-v1`](../../../wiki/findings/results/coercion-sense-modulation-v1.md)) gave an early "no" (gemini strongest lexically yet least coercion-sensitive). This makes it a typed finding.

## Method

`analyze.py` **tabulates per-model headline numbers already on the in-repo result pages** (each value provenance-tagged to its source result id) and computes, across the panel of three (claude-sonnet-4.6, gpt-5.4-mini, gemini-3.5-flash):
- the **lexical predictor**: durel Spearman ρ (claude 0.679 / gpt 0.601 / gemini 0.804) → lexical order **gemini > claude > gpt**;
- for each constructional result, the per-model **order** and its agreement with the lexical order (MATCH / DIVERGE / CEILING);
- a Spearman ρ(lexical, constructional) across the 3 models per result, averaged over the **discriminating** (non-ceiling) results only.

**Hard caveat (in the script + the result):** with **n=3 models** a Spearman is a blunt descriptive instrument — only a few distinct orderings exist and no value is significance-testable. The finding is the **exact rank pattern**, not a p-value. Ceiling-for-all results carry no discriminating order and are excluded from ρ.

## Provenance of every tabulated number

| result id | metric | claude | gpt-5.4-mini | gemini |
|---|---|---|---|---|
| lexical-sense-gradience-v1 | durel ρ (predictor) | 0.679 | 0.601 | 0.804 |
| caused-motion-minimal-pair-divergence-v1 | affirm % FC | 100 | 90 | 100 (ceiling) |
| way-construction-traversal-v1 | affirm % FC | 100 | 77.8 | 94.4 |
| conative-minimal-pair-divergence-v1 | gap pp FC | 67 | 42 | 88 |
| conative-minimal-pair-divergence-v1 | gap pp NLI | 54 | −8 | 67 |
| comparative-correlative-covariation-v1 | gap pp | 87.5 | 90.0 | 80.0 (ceiling) |
| cxnli-distinction-divergence-v1 | drop pp (less neg = better) | −30 | −45 | −41 |
| conative-cancel-direction-v2 | suppress % FC | 66.7 | 33.3 | 83.3 |
| coercion-implicit-cue-v2b | impossible-affirm % FC (lower = more WK) | 90 | 40 | 100 |
| comparative-correlative-covariation-v3 | operator-correct % FC | 100 | 60 | 100 |
| caused-motion-near-miss-v2c | gap pp FC | 68.8 | 62.5 | 100.0 |
| **coercion-sense-modulation-v1** (bridge) | sense-shift gap cont | **31.4** | **20.5** | **8.3** |

(Numbers cross-checked by two independent read-only extraction passes over the result pages.)

## Headline

- **gpt-5.4-mini is weakest lexically (ρ 0.60) AND the most fragile constructionally** — the one consistent cross-axis thread (last in every discriminating result). This single strand *is* lexical-order-consistent and drives the +0.71 mean ρ over the 9 discriminating results.
- **But the top of the lexical order does not transfer.** gemini (strongest lexically) is **not** uniquely strongest constructionally — it ties claude at ceiling on the add-direction positives, and claude beats it on *way*/CC-v3/distinction.
- **The same-instrument bridge inverts the order** (claude 31.4 > gpt 20.5 > gemini 8.3 vs the lexical gemini > claude > gpt). The strongest pure lexical tracker registers the *smallest* coercion-induced sense shift.
- So lexical gradience strength predicts constructional competence **only at the bottom**; at the top the axes **dissociate**, and the most comparable measure inverts. Confirms the NEXT.md early sign ("no").

See `raw/results.json` for the full per-result ordering + ρ table (MATCH 5 / DIVERGE 4 / CEILING-excluded 2).
