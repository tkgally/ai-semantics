---
type: result
id: lexical-perceptual-grounding-moderation-v1
title: Lancaster perceptual-grounding moderation of the DWUG lexical result (multimodal prediction 1) — a NULL — a word's perceptual groundedness does NOT predict how well a text-only model tracks its graded senses (if anything a weak opposite tilt, driven by gpt-5.4-mini); the first grounded-tagged result
meaning-senses:
  - grounded
  - grounded.perceptual
  - referential.sense
  - distributional
  - human-comparison
status: proposed
anchor: resource/lancaster-sensorimotor-norms
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: anchors
    target: resource/lancaster-sensorimotor-norms
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: refines
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: conjecture/multimodal-lexical-grounding-divergence
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/embodied-cognition
---

# Result: Lancaster perceptual-grounding moderation of the lexical result (multimodal prediction 1) — a NULL

**One-line (write the null first):** re-analyzing the **already-collected** lexical-v1 ratings
(no new API spend, $0) moderated by the **Lancaster Sensorimotor Norms**, the text-only panel's
DWUG sense-relatedness monotonicity is **not stronger for perceptually grounded lemmas** — the
moderation is **null-to-slightly-negative**. Across the pre-registered primary cells
(`Max_strength.perceptual` × the ordinal `durel` framing × 3 models), **no** model shows the
predicted positive Δρ; all three are negative (Δρ = −0.05 / −0.27 / −0.04 for claude / gpt-5.4-mini /
gemini), and the **only** bootstrap CI that excludes zero (gpt-5.4-mini, Δρ −0.27, CI [−0.53, −0.01])
points the **wrong way** — monotonicity is *weaker*, not stronger, for grounded words in that one
cell. This is the project's **first `grounded`-tagged result**, and it lands as a first-class
**null**: before any image is shown, a word's static perceptual groundedness does not predict how
well a text-only model tracks its graded senses. Per the conjecture's own logic, this **lowers the
prior** on the image-grounding predictions (2–4) — but the design is **inherently underpowered**
(21 lemmas/side, compressed moderator range 2.44–4.95), so the null reads as "no detectable
moderation **or** an effect this design cannot resolve," **not** as evidence against grounding.

Run record: [`experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/`](../../../experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/README.md)
(`PREREG.md` + `analyze.py`). Tests prediction 1 of
[`conjecture/multimodal-lexical-grounding-divergence`](../conjectures/multimodal-lexical-grounding-divergence.md);
refines [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md). Anchors:
[`resource/lancaster-sensorimotor-norms`](../../base/resources/lancaster-sensorimotor-norms.md)
(moderator) + [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (the
graded human signal). Governed by [`decisions/resolved/multimodal-panel-and-grounding-theory`](../../decisions/resolved/multimodal-panel-and-grounding-theory.md),
resolved 2026-05-31 (Q3 default A ratified; this prediction-1 null stands on its Lancaster + DWUG anchors). **Cost $0.00** (re-analysis of frozen ratings). An
independent adversarial pre-write critic fixed a normalization blocker and forced the
power/collinearity caveats **before** the run; an independent post-run verifier reproduced every
figure exactly (see Provenance).

## What was tested (the conjecture's $0 text-side prediction 1)

[`conjecture/multimodal-lexical-grounding-divergence`](../conjectures/multimodal-lexical-grounding-divergence.md)
prediction 1 — the cheap, text-side, no-new-probe bridge to the multimodal axis:

> "the text-only panel's monotonicity (rating vs human DURel median) is **stronger for highly
> perceptually-grounded lemmas** than for abstract ones … a first hint, before any image, that
> grounding and sense-tracking are linked. **Null:** no moderation — a word's perceptual strength
> does not predict the model's tracking quality. A null here is itself informative and would lower
> the prior on predictions 2–4."

[`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md) established the monotonicity
(Spearman ρ(model rating, human DURel median) = 0.60–0.83 across the panel). This unit asks whether
that monotonicity is **moderated** by how perceptually grounded each target word is, using the
**Lancaster Sensorimotor Norms** (Lynott et al. 2020; human perceptual/action strength ratings;
CC BY 4.0) as the moderator — a join of two already-validated human resources, no model call.

- **Moderator (pre-registered):** `Max_strength.perceptual` (the lemma's maximum mean strength
  across the six Lancaster perceptual modalities, 0–5) — **primary**; `Visual.mean` — secondary.
- **Coverage:** 42 / 43 DWUG EN lemmas have a Lancaster entry; `lass_nn` has none (and was already
  excluded as a DWUG conflation in [`result/lexical-polysemy-homonymy-v2`](lexical-polysemy-homonymy-v2.md))
  → its 4 pairs dropped → **196 pairs** analyzed.
- **Primary test T1 (frozen):** median-split the 42 lemmas at the sample median
  `Max_strength.perceptual` = 3.557 → HIGH (21 lemmas / 85 pairs) vs LOW (21 lemmas / 111 pairs);
  pooled Spearman ρ(model rating, human DURel median) within each stratum; **Δρ = ρ_HIGH − ρ_LOW**
  with a **cluster bootstrap** 95% CI (resample *lemmas*, 10 000 iters, seed 20260530). Prediction 1
  ⇒ Δρ > 0.
- **Robustness T2 (lemma-level, non-pseudoreplicated):** per-lemma mean absolute error between the
  model's [0,1]-normalized rating and the [0,1]-normalized human median, then Spearman ρ(lemma MAE,
  lemma perceptual strength) across 42 lemmas. Prediction 1 ⇒ **negative** (more perceptual → lower
  error). One point per lemma — no pseudo-replication.
- **No pass bar; report-the-estimate; no indicator retuned after the run.**

## Result (independently re-verified from frozen inputs — every figure reproduced exactly)

### T1 — primary cells (`Max_strength.perceptual` × `durel`): null-to-negative, no support

| model | ρ_HIGH | ρ_LOW | **Δρ = HIGH − LOW** | Δρ 95% CI (cluster bootstrap) |
|---|---|---|---|---|
| claude-sonnet-4.6 | 0.638 | 0.688 | **−0.049** | [−0.26, +0.15] (spans 0) |
| gpt-5.4-mini | 0.433 | 0.700 | **−0.266** | [−0.53, −0.01] (excludes 0, **wrong direction**) |
| gemini-3.5-flash | 0.774 | 0.815 | **−0.042** | [−0.18, +0.08] (spans 0) |

Prediction 1 wants Δρ > 0 (grounded words tracked *better*). **No primary cell shows it.** Two of
three are tight nulls around zero; the third (gpt-5.4-mini) is the only one whose CI excludes zero,
and it is **negative** — that model tracks grounded words' senses *worse*, not better. The
monotonicity itself is healthy in both strata (ρ 0.43–0.82), exactly as v1 reported — what is
**absent** is any tendency for perceptual grounding to *strengthen* it.

### Exploratory / robustness cells (not confirmatory — reported in full, no cherry-picking)

- **`cont` framing (0–100), T1:** Δρ = +0.03 / −0.03 / −0.04 (claude / gpt / gemini) — all CIs span
  zero; the gpt durel negative does **not** replicate under the continuous framing (gpt cont Δρ
  −0.03), so even the one "significant" cell is framing-specific and fragile.
- **T2 lemma-level (`Max_strength.perceptual`):** ρ(MAE, perceptual) = −0.07 / +0.24 / +0.10 (claude
  durel / gpt durel / gemini durel) and +0.22 / +0.21 / +0.18 (cont). Prediction 1 wants **negative**
  (more perceptual → less error); the values are **mostly positive** (more perceptual → *more* error),
  i.e. the same weak opposite tilt, again most pronounced for gpt-5.4-mini. None is large.
- **Secondary moderator `Visual.mean` (T3):** same shape (durel Δρ −0.01 / −0.14 / −0.03). **But this
  is not independent corroboration:** across the 42 lemmas ρ(`Max_strength.perceptual`, `Visual.mean`)
  = **0.85** and **33/42 lemmas have the two columns numerically identical** (vision is the dominant
  modality for most DWUG targets), so T3 re-runs essentially the same split on essentially the same
  variable. Reported for completeness, not as a second confirmation (critic S1).
- **n≥3-annotator robustness (primary cell-set):** restricting to the 46 pairs with ≥3 raters
  (21 HIGH / 25 LOW), the `durel` Δρ stay non-positive (−0.10 / −0.50 / −0.14); the `cont` cells go
  noisy and sign-unstable on this small subset (not interpretable at n=46). The durel null/negative
  is the stable reading.

### Confounds — checked, all clear (input-only, computed before reading model outputs)

ρ(perceptual, pairs-per-lemma) = **−0.05**, ρ(perceptual, mean annotator-count) = **−0.07**,
ρ(perceptual, human-DURel spread) = **+0.09** — all negligible, so the moderator is **not** a proxy
for how many pairs a lemma has, how many annotators rated them, or how spread the human gold is.
The human-DURel-*level* distribution is balanced across the split (HIGH 1/2/3/4 = .26/.22/.28/.24;
LOW = .22/.28/.23/.27), so the ρ comparison is not confounded by differing signal range. The null is
a null about *perceptual grounding*, not an artifact of these covariates.

## Interpretation (calibrated — this is a bounded, underpowered null)

1. **The headline is a clean null on the pre-registered primary test, with a weak opposite tilt.**
   Perceptual groundedness of a *word* does not predict how well a text-only model tracks its graded
   sense relatedness; the only signal that clears its CI (gpt-5.4-mini, durel) runs *opposite* to
   prediction 1 and does not replicate across framings. Write it as the null.

2. **What the null does and does not license.** It **does** remove the "converging text-side hint"
   the conjecture hoped for, and per the conjecture's own statement it **lowers the prior on the image
   predictions (2–4)**. It does **not** establish a *redundancy* verdict ("text has already saturated
   perceptual sense distinctions") — that is the conjecture's prediction-2 null, an *image-vs-text*
   contrast this text-only re-analysis cannot reach. Nor does it falsify grounding: the moderator is a
   **static, word-level, across-senses** perceptual score, not a measure of whether *this pair's*
   senses are perceptually distinguishable (the conjecture's actual prediction-3 moderator). A word
   can be highly visual (`face` 4.95, `twist` 4.65) yet have two senses that are equally
   text-distinguishable — so even a true grounding effect could be invisible to this proxy.

3. **Power is the lead caveat, not an excuse.** With 21 lemmas/side over a compressed range
   (2.44–4.95 — DWUG targets are mostly concrete content words; there is no genuinely abstract tail
   like *justice*/*idea*), and 3 lemmas straddling the median, this test could miss a moderate true
   moderation. The honest verdict is **"no detectable moderation, and what little tilt there is runs
   the wrong way"** — not "grounding demonstrably does not matter." A cleaner test needs a word set
   with real abstract/concrete spread and (for the conjecture's real claim) **sense-level**, not
   word-level, perceptual contrast.

4. **A mild model-specific wrinkle, consistent with the project's instrument-sensitivity theme.** The
   one cell that moves is gpt-5.4-mini — already the panel's noisiest lexical tracker
   ([`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md): ρ 0.60, lowest) and the most
   instrument-fragile model elsewhere. Its grounded-word tracking degrades most. This is a weak,
   single-model observation, not a finding about grounding per se.

5. **It exercises the `grounded.perceptual` tag for the first time — as a null.** The tag has existed
   since the project began and never carried a finding; its first empirical exercise is a negative,
   which is exactly the modest, calibrated kind of first step the charter asks for. Grounding remains a
   live question; the *text-side word-level proxy* for it does not light up.

## Honest caveats / scope

- **Single re-analysis, n=3 models, text-only.** No image was shown; this bears on prediction 1 only.
- **Word-level moderator vs sense-level claim.** Lancaster scores one number per word across all its
  senses; the conjecture's discriminating prediction (3) is about whether *a given pair's* senses are
  perceptually distinguishable. This re-analysis can only test the blunter word-level version, and a
  null on the blunt version is weaker evidence than a null on the sharp one would be.
- **Compressed moderator range / low power** (lead caveat, above).
- **Secondary moderator near-collinear with the primary** (perceptual ≈ visual here, ρ 0.85) — T3 is
  not independent evidence.
- **Inherits v1's reliability caveats** (S3: half the gold rests on 2 annotators) — the n≥3 pass
  preserves the durel null but is itself small (46 pairs).
- **Contingent on the open multimodal decision** (Q3 anchor-class): provisional until Tom ratifies;
  the anchors (DWUG + Lancaster) are both in-repo and page-grounded.

## Provenance / verification

- **Anchors:** [`resource/lancaster-sensorimotor-norms`](../../base/resources/lancaster-sensorimotor-norms.md)
  (the perceptual-strength moderator; aggregate CSV fetched + sha256-pinned this session) +
  [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (the graded human DURel
  signal being moderated). Both are independent human-generated resources — never model agreement.
- **Frozen inputs (sha256 in `PREREG.md`):** Lancaster CSV `445d363f…`; lexical-v1 manifest
  `7b4ad11f…` (identical to the frozen v1 set); the six v1 raw rating JSONs; the derived join table
  `0f08944e…`.
- **Adversarial pre-write critic (independent, read-only, before the run):** caught a **BLOCKER**
  (T2's `cont` cells normalized the human gold by the 0–100 framing scale, collapsing it to ~0.01–0.04
  and reducing the "error" to the model's raw level — fixed: human always normalized on the DURel
  (1,4) scale, T1 was scale-invariant and unaffected); forced the **power**, **median-boundary
  fragility**, **multiple-comparisons** (primary cell-set designated in advance), and
  **perceptual≈visual collinearity** disclosures; prompted the **n≥3** robustness pass. All applied
  before any outcome was computed (see `PREREG.md` "Pre-run critique fixes").
- **Post-run number verifier (independent, read-only):** rewrote the Spearman + median-split + join
  from scratch (pure stdlib) and reproduced **every** headline figure to ±0.0001 — coverage (42/43,
  196 pairs), the split (3.557, 85/111), all three primary Δρ (−0.049 / −0.266 / −0.042), all four
  confound correlations, and the verdict that **no primary cell shows a positive Δρ and the only CI
  excluding zero is in the negative direction**. VERDICT: fully reproducible.
- **No retuning:** the moderator, split, tests, and reading rule were frozen in `PREREG.md` before any
  model-rating × perceptual-strength quantity was computed; the null is reported as-run.
