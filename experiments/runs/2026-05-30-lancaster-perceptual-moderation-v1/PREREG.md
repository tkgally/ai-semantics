# Pre-registration — Lancaster perceptual-strength moderation of the lexical-v1 result (v1)

**Date frozen:** 2026-05-30 (before computing any model-rating × perceptual-strength quantity)
**Unit:** prediction 1 of [`conjecture/multimodal-lexical-grounding-divergence`](../../../wiki/findings/conjectures/multimodal-lexical-grounding-divergence.md) — the $0, text-side, no-new-probe moderation.
**Governing decision:** [`decisions/resolved/multimodal-panel-and-grounding-theory`](../../../wiki/decisions/resolved/multimodal-panel-and-grounding-theory.md) Q3 default **A** (Lancaster text-side moderator first), run under the standing delegation (defaults hold; non-blocking). `anchor: pending` until Q3 ratified — result stays `proposed`/contingent.

## Question

Re-analyzing the **already-collected** lexical-v1 ratings (no new API call), is the text-only
panel's sense-relatedness monotonicity — Spearman ρ(model rating, human DURel median),
established in [`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md)
(ρ 0.60–0.83) — **stronger for perceptually grounded lemmas** than for abstract ones?

This is a *within-text-model* test (no image is shown): does the human-rated perceptual
groundedness of a *word* predict how well a text-only model tracks its graded sense
relatedness? Prediction 1 ⇒ yes (positive moderation). **Null (first-class):** no moderation —
perceptual strength does not predict tracking quality; sense-tracking is uniform across the
abstract/concrete divide. A null here lowers the prior on the image predictions (2–4).

## Frozen inputs (sha256)

- Lancaster Sensorimotor Norms aggregate CSV (Lynott, Connell, Brysbaert, Brand & Carney 2020,
  *Behavior Research Methods*; **CC BY 4.0**; OSF node `rwhs6`, file `48wsc`):
  `445d363fb1f9f3e50b86d88e2f46cdc9a22b5dd8a713ce4e7be2a773d57f43c5` (gitignored, re-downloadable).
- lexical-v1 manifest (200 within-period DWUG EN pairs, 43 lemmas; frozen v1):
  `7b4ad11f25e8734c52f2f87da338aebd9056f764e2130bf36e32aaead6109fd2`.
- lexical-v1 raw model ratings (durel = primary, cont = robustness; A=claude-sonnet-4.6,
  B=gpt-5.4-mini, C=gemini-3.5-flash):
  - durel_A `254b7684…`  durel_B `e182073c…`  durel_C `cd323280…`
  - cont_A  `b4bdc25d…`  cont_B  `745c7d75…`  cont_C  `e657a674…`
- join table `lemma_perceptual.csv` (emitted by `build_join.py`):
  `0f08944ec9323a8d524d7eeb0631eee9a723084d71c5b1a3796ebc92b1b26da8`.

## Moderator (pre-registered, fixed before any outcome was computed)

- **Primary:** `Max_strength.perceptual` — the lemma's maximum mean strength across the six
  Lancaster perceptual modalities (0–5). The standard Lancaster summary of overall perceptual
  grounding; matches the conjecture's "perceptually grounded" wording.
- **Secondary (robustness, not headline):** `Visual.mean` — vision-specific strength, because
  the downstream image predictions (2–3) use *visual* depiction. Reported alongside; not the
  primary verdict.

**Coverage:** 42 / 43 lemmas have a Lancaster entry. `lass_nn` has **none** (and was already
excluded as a DWUG sense-conflation in [`result/lexical-polysemy-homonymy-v2`](../../../wiki/findings/results/lexical-polysemy-homonymy-v2.md));
its 4 pairs are **dropped** → **196 pairs** analyzed. Stated, not worked around.

## Tests (fixed; no pass bar; report-the-estimate)

**T1 — primary: median-split stratified ρ difference.**
Split the 42 covered lemmas at the sample median `Max_strength.perceptual` = 3.557 into
HIGH (> median; 21 lemmas, 85 pairs) and LOW (≤ median; 21 lemmas, 111 pairs). For each
model × framing (durel primary; cont robustness), compute pooled Spearman
ρ(model rating, human DURel median) within each stratum and report
**Δρ = ρ_HIGH − ρ_LOW**, with a **cluster bootstrap** 95% CI (resample *lemmas* with
replacement — never pairs — 10 000 iters, seed 20260530, recomputing the split-fixed strata
from the resampled lemmas). Prediction 1 ⇒ Δρ > 0; null ⇒ CI spans 0.

**T2 — robustness, non-pseudoreplicated (continuous, lemma-level).**
For each lemma, min-max-normalize each pair's model rating and human median to [0,1] within the
framing's own scale, take the lemma's **mean absolute error** MAE = mean|model−human| over its
pairs. Then Spearman ρ(lemma MAE, lemma `Max_strength.perceptual`) across the 42 covered lemmas
(one point per lemma — no pseudo-replication). Prediction 1 ⇒ **negative** ρ (more perceptual →
lower error → better tracking).

**T3 — secondary moderator.** Repeat T1+T2 with `Visual.mean`. Robustness only.

**Confounds checked / disclosed (from the human anchor + manifest only, pre-outcome):**
- Human-DURel-level distribution is **balanced across the split** (HIGH 1/2/3/4 = .26/.22/.28/.24;
  LOW = .22/.28/.23/.27) → the ρ comparison is not confounded by differing signal range. (Recorded
  before any model rating was touched.)
- **Moderator range is compressed** (2.44–4.95; DWUG targets are mostly concrete content words) →
  limited power; a null may be range-restriction, not absence of effect. Disclosed as a lead caveat.
- **Pairs/lemma are uneven** (1–15) → pooled within-stratum ρ (T1) is weighted toward high-count
  lemmas; T2 weights every lemma equally → the two together bracket the weighting choice.

## Discipline

- One **independent adversarial pre-write critic** reviews this prereg + `build_join.py` +
  `analyze.py` **before** the analysis is run.
- One **independent post-run number-verifier** recomputes every reported figure from the frozen
  inputs after the run.
- No indicator is retuned after seeing an outcome. If the primary is null, the null is the result.

## Pre-run critique fixes (applied before any outcome was computed)

An independent adversarial pre-write critic reviewed this prereg + `build_join.py` + `analyze.py`
(input-only; no moderation outcome computed). It independently re-verified the T1 mechanics are
correct (fixed-threshold median; lemma-level — not pair-level — cluster resampling; correct
Spearman tie handling; A/B/C↔model labels; 196 pairs after dropping `lass`). Fixes applied
**before the run**:

- **B1 (BLOCKER, fixed) — T2 human-side normalization.** The human gold is the DURel median on
  the **1–4 scale in every framing**; the original T2 normalized the human term by the *framing's*
  scale, so under `cont` (0–100) the human collapsed to ~0.01–0.04 and the "error" reduced to the
  model's raw level. Fixed: model pred normalized on its framing scale, **human always on (1,4)**
  (`HUMAN_SCALE`). T1 is Spearman on raw values (scale-invariant) → was never affected.
- **S1 (disclosed) — the secondary moderator is near-collinear with the primary.** Across the 42
  lemmas, ρ(`Max_strength.perceptual`, `Visual.mean`) ≈ 0.85 and ~33/42 are numerically identical
  (vision is the dominant modality for most DWUG targets). **T3 is therefore a near-duplicate, not
  independent corroboration** — reported as such, never as a second confirmation. (`analyze.py`
  now reports the collinearity in the `confounds` block.)
- **S2 (disclosed) — underpowered + median-boundary fragility.** 21 lemmas/side, compressed
  moderator range (2.44–4.95), and 3 lemmas (`bar`, `chef`, `rag`) within 0.05 of the median
  (their HIGH/LOW side is near-arbitrary). A **null must be read as "no detectable moderation OR
  an effect this design cannot resolve," not as evidence against prediction 1.**
- **S3 (fixed) — primary cell-set designated in advance:** `Max_strength.perceptual` × `durel` ×
  {A,B,C}, test T1. Everything else (`cont`, `Visual.mean`, T2) is exploratory/robustness. All 24
  cells are reported; no cell is cherry-picked as confirmatory.
- **S4 (added) — n≥3 robustness pass.** Half the gold rests on 2 annotators (v1's S3). Added a
  `robustness_n_ge_3` pass repeating the primary cell-set on pairs with ≥3 raters. (Critic checked
  ρ(perceptual, mean human_n) = −0.07 → not a *differential* confound across the split.)
- **N1 (recorded) — input-only confounds, all checked null:** ρ(perceptual, pairs/lemma),
  ρ(perceptual, mean human_n), ρ(perceptual, human spread) are all emitted in the `confounds`
  block so a reader sees they were checked, not assumed.
- **S5 (resolved) — the second human anchor is page-grounded:** the Lancaster norms now have a
  typed [`resource/lancaster-sensorimotor-norms`](../../../wiki/base/resources/lancaster-sensorimotor-norms.md)
  page; the result will cite both DWUG (gradience) and Lancaster (moderator) as human anchors.

Verdict after fixes: sound to run; inherently low-powered (report estimates + CIs, write the null
first-class, do not over-read).
