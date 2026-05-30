# Pre-registration — Lancaster perceptual-strength moderation of the lexical-v1 result (v1)

**Date frozen:** 2026-05-30 (before computing any model-rating × perceptual-strength quantity)
**Unit:** prediction 1 of [`conjecture/multimodal-lexical-grounding-divergence`](../../../wiki/findings/conjectures/multimodal-lexical-grounding-divergence.md) — the $0, text-side, no-new-probe moderation.
**Governing decision:** [`decisions/open/multimodal-panel-and-grounding-theory`](../../../wiki/decisions/open/multimodal-panel-and-grounding-theory.md) Q3 default **A** (Lancaster text-side moderator first), run under the standing delegation (defaults hold; non-blocking). `anchor: pending` until Q3 ratified — result stays `proposed`/contingent.

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
