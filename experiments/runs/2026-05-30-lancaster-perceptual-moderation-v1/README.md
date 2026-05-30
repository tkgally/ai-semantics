# Run record — Lancaster perceptual-grounding moderation v1 (multimodal prediction 1; the first `grounded`-tagged result)

**Date:** 2026-05-30
**Type:** $0 read-only re-analysis (no new API spend) of the already-collected lexical-v1 ratings.
**Prereg (frozen):** [`PREREG.md`](PREREG.md)
**Conjecture / prediction:** [`conjecture/multimodal-lexical-grounding-divergence`](../../../wiki/findings/conjectures/multimodal-lexical-grounding-divergence.md) prediction 1.
**Governing decision:** [`decisions/open/multimodal-panel-and-grounding-theory`](../../../wiki/decisions/open/multimodal-panel-and-grounding-theory.md) Q3 default **A** (run under the standing delegation; non-blocking).
**Anchors:** [`resource/lancaster-sensorimotor-norms`](../../../wiki/base/resources/lancaster-sensorimotor-norms.md) (moderator) + [`resource/dwug-usage-graphs`](../../../wiki/base/resources/dwug-usage-graphs.md) (the graded human signal).
**Result page:** [`result/lexical-perceptual-grounding-moderation-v1`](../../../wiki/findings/results/lexical-perceptual-grounding-moderation-v1.md)

## Question

Is the text-only panel's DWUG sense-relatedness monotonicity ([`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md), Spearman 0.60–0.83) **stronger for perceptually grounded lemmas**, using the Lancaster Sensorimotor Norms (Lynott et al. 2020, CC BY 4.0) as the moderator? Prediction 1 ⇒ yes (positive moderation). Null (first-class) ⇒ perceptual strength does not predict tracking quality.

## Headline — a NULL (null-to-slightly-negative)

No pre-registered primary cell (`Max_strength.perceptual` × `durel` × 3 models) shows the predicted positive Δρ. All three are negative (Δρ = −0.049 / −0.266 / −0.042 for claude / gpt-5.4-mini / gemini); the only bootstrap CI excluding zero (gpt-5.4-mini, [−0.53, −0.01]) is in the **wrong direction**. The exploratory `cont` framing, the `Visual.mean` secondary moderator, and the lemma-level T2 all reproduce the same null-to-weak-opposite tilt. Confounds (pairs/lemma, annotator count, human spread) all clear. **The design is inherently underpowered** (21 lemmas/side, compressed moderator range 2.44–4.95) → the null reads as "no detectable moderation OR an effect this design cannot resolve," not as evidence against grounding. Per the conjecture's logic, this lowers the prior on the image predictions (2–4); it does not falsify them. Full reading on the result page.

## Files

- `build_join.py` — reads the gitignored Lancaster aggregate CSV + the frozen lexical-v1 manifest; emits the committed `lemma_perceptual.csv` (42 lemmas × Lancaster scores; `lass_nn` uncovered). Prints input sha256s.
- `lemma_perceptual.csv` — **committed** derived join table (CC BY 4.0 permits it; a tiny extract, attributed). No corpus text.
- `analyze.py` — pure-stdlib Spearman + cluster bootstrap (resamples lemmas) + lemma-level MAE + confound block + n≥3 robustness. Reads the frozen v1 raw ratings.
- `PREREG.md` — pre-registration + the pre-run critique-fix log (B1 normalization fix, S1–S5 disclosures).
- `raw/results.json` — full output (all 24 T1 cells + CIs, T2, confounds, n≥3 robustness, example lemma rows).

## Reproduce

```
# 1. re-download the Lancaster aggregate CSV (gitignored; sha256-pinned):
curl -sL https://osf.io/download/48wsc/ -o experiments/data/lancaster/Lancaster_sensorimotor_norms_for_39707_words.csv
#    expect sha256 445d363fb1f9f3e50b86d88e2f46cdc9a22b5dd8a713ce4e7be2a773d57f43c5
# 2. rebuild the join table (idempotent; expect lemma_perceptual.csv sha256 0f08944e…):
python3 experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/build_join.py
# 3. run the moderation:
python3 experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/analyze.py
```

The v1 raw ratings (`experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/raw/*.json`) are committed and unchanged (manifest sha256 `7b4ad11f…` matches the frozen v1 set).

## Data / licence handling

- Lancaster aggregate CSV: **CC BY 4.0**, gitignored (re-downloadable, sha256 pinned). The committed `lemma_perceptual.csv` is a 42-row derived extract (perceptual scores for the DWUG EN lemmas) — CC BY permits derivative distribution with attribution (citation in the resource page + PREREG).
- DWUG corpus text: **not** committed (CC BY-ND / CCOHA); this re-analysis uses only the already-committed v1 model outputs + the manifest's human DURel gold. No corpus sentences touched.

## Discipline (per the steer: freeze + ≥1 pre-write critique + ≥1 post-run verification)

- **Inputs frozen** (sha256 in `PREREG.md`) before any model-rating × perceptual-strength quantity was computed.
- **Independent adversarial pre-write critic** (read-only): caught one BLOCKER (T2 human-side normalization), independently re-verified the T1 cluster-bootstrap mechanics, and forced the power / collinearity / multiple-comparisons / n≥3 disclosures — all applied **before** the run.
- **Independent post-run number verifier** (read-only, from-scratch recompute): reproduced every headline figure to ±0.0001 and confirmed the null-to-negative verdict. No discrepancy.
- **Cost: $0.00** (re-analysis of frozen ratings; 0 API calls).
