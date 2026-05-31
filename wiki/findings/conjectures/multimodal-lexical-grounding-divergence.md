---
type: conjecture
id: multimodal-lexical-grounding-divergence
title: Visual grounding moves a model's graded lexical-sense behavior toward the human signal — most where senses are perceptually distinguishable — beyond what the text-only distribution already supplies
meaning-senses:
  - grounded
  - grounded.perceptual
  - referential.sense
  - distributional
  - human-comparison
status: tested
anchor: pending
contingent-on: []
created: 2026-05-30
updated: 2026-05-31
links:
  - rel: refines
    target: open-question/lexical-polysemy-gradience
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/symbol-grounding-problem
  - rel: depends-on
    target: concept/embodied-cognition
  - rel: depends-on
    target: concept/multimodal-compositionality
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Conjecture: visual grounding shifts graded lexical-sense behavior toward the human signal (the project's first multimodal wedge)

> **Status: partially tested (updated 2026-05-31).** The project's **first multimodal conjecture**
> and the first finding-type page tagged `grounded` / `grounded.perceptual` — the `grounded` tag had
> existed in [`meaning-senses.md`](../../meaning-senses.md) since the project began but carried no
> finding until this conjecture's predictions ran. **Predictions 1–3 have now run, all landing as negatives:**
> prediction 1 landed as a text-side null (2026-05-30, [`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md)),
> and predictions 2–3 landed as a **redundancy null** in the project's first image-input probe
> (2026-05-31, [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)).
> Only **prediction 4 (coercion under depiction)** remains genuinely unrun. It is the direct multimodal extension of the lexical wedge
> [`conjecture/lexical-sense-gradience`](lexical-sense-gradience.md): that conjecture asked
> whether a *text-only* model tracks graded sense relatedness above a context-similarity
> shadow (answer: yes, clauses a+c — [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md));
> this one asks whether **adding the picture changes that behavior, in the human direction,
> beyond what the text already gave away.** **Panel / grounding-theory / anchor-class are
> now ratified** ([`decisions/resolved/multimodal-panel-and-grounding-theory`](../../decisions/resolved/multimodal-panel-and-grounding-theory.md),
> 2026-05-31: Q1=A existing 3-family panel, Q2=A Lyre gradual grounding, **Q3=B GO** on the
> image probe). The image probe's human-anchor choice is now **ratified** too
> ([`decisions/resolved/multimodal-image-anchor`](../../decisions/resolved/multimodal-image-anchor.md),
> 2026-05-31, Tom: "A stands" — the WordNet-keyed constructed set), so `contingent-on: []`. The
> image predictions (2–4) still carry `anchor: pending` only in the sense that each *future* image
> result scopes its own claim; the v1 result ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md))
> is anchored and promoted.

## Statement

The conventional theories of meaning the project catalogs that tie meaning to the physical
world — Bender & Koller's form-vs-meaning and Lyre's grounding-as-gradual
([`concept/grounding`](../../base/concepts/grounding.md)), Harnad's symbol-grounding problem
([`concept/symbol-grounding-problem`](../../base/concepts/symbol-grounding-problem.md)),
Barsalou's perceptual symbols ([`concept/embodied-cognition`](../../base/concepts/embodied-cognition.md)) —
all predict the same thing at the limit: a system with **only form** is missing the relation
to the perceptual world that fixes much of word meaning, and supplying that relation should
*change* its semantic behavior. The deflationary rival — the distributional view
([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)), and the
"sense-tracking is enough" reading of [`concept/referential-meaning`](../../base/concepts/referential-meaning.md) —
predicts the opposite at the limit for a strong text model: a model fluent enough to track
graded sense from text alone has *already* extracted the perceptually-relevant distinctions
from the distribution, so the image is **redundant** and adds nothing.

This conjecture stakes out a falsifiable, directional middle claim:

> For a target word used in two contexts, a vision-language model that is *also given images
> depicting each usage* will produce graded sense-relatedness behavior that is **closer to the
> human-rated relatedness signal** than the *same model family's text-only* behavior on the
> same pairs — and the shift is **concentrated where the two senses are perceptually
> distinguishable** (a homonym whose two senses have visually distinct referents; a polyseme
> whose uses depict differently), and **negligible where they are not** (abstract words; senses
> with no visual contrast). The text-only behavior is the **null to beat**: the conjecture is
> supported only if the image moves behavior in the human direction *over and above* the
> text-only baseline, not if image-conditioned and text-only behavior coincide (the redundancy
> null) or if the image moves behavior *away* from the human signal (the distraction null).

The claim is deliberately *directional and bounded*, not "VLMs understand words and text models
don't." It says: **where perception carries sense-relevant information that the text
distribution under-determines, visual grounding should supply it, and the gap should show up
as movement toward the independent human signal.**

## Why this is interesting

- **It has given** the `grounded.perceptual` tag its **first empirical exercise** — by two negatives.
  Until predictions 1–3 ran, grounding was a base-layer concept only; the project has now asked the
  grounding question of its own panel's behavior, with a human anchor, rather than rehearsing the
  philosophy. The grounding axis currently stands at **two bounded negatives for clear homonyms**
  (a text-side moderation null and an image-side redundancy null — see the Predictions section), not
  at confirmation; fine polysemy and a genuinely image-native task are the honest next directions.
- It is a clean test on the seam between [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)
  and [`concept/grounding`](../../base/concepts/grounding.md): does perceptual input add `referential.sense`-relevant
  signal *beyond the distributional shadow*, or has a strong text model already saturated it?
  Either answer is informative — a clean **redundancy null** ("text already had it") would be a
  first-class negative that bounds how much grounding the multimodal models' extra modality buys.
- It offers a **second route to the lexical hard direction (polysemy vs. homonymy)** that the
  text-only [`result/lexical-polysemy-homonymy-v2`](../results/lexical-polysemy-homonymy-v2.md)
  could not reach. That null was *not* "homonyms sat at the floor": DWUG EN held only **3 clean
  homonym lemmas** (`ball`/`plane`/`prop`), and their cross-period usage pairs were often the
  **same sense within a pair** (etymological homonyms whose two instances do not actually contrast
  senses) — so the homonyms carried substantial *intermediate and high* human mass, the bimodality
  precondition failed, and **no separable discreteness regime existed to detect in either the human
  or the model ratings**. The gap was a *design* gap: DWUG (built for diachronic change) supplies
  no clean, cross-sense, perceptually-contrasting homonym pairs. A purpose-built **image-paired**
  set of genuinely cross-sense homonym pairs with visually distinct referents could supply exactly
  that contrast — vision adding a sense-distinguishing signal the diachronic text anchor never
  carried. (This is a *prediction about a constructed set*, not a claim that DWUG's homonyms are
  floored — they are not.)
- It is built to **integrate**, not replace. The instrument is the *same* DURel-style graded
  relatedness rating the lexical program validated, with the image as the only added variable —
  so a result here joins the lexicon↔grammar continuum
  ([`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md)) as a **third
  axis** the same way coercion bridged the two text wedges: by reusing one instrument and
  toggling one factor (here, modality; there, the coercing construction).

## Predictions

Ordered cheapest-first, matching the anchor-class sequencing ratified in
[`decisions/resolved/multimodal-panel-and-grounding-theory`](../../decisions/resolved/multimodal-panel-and-grounding-theory.md)
(Q3=B GO). **What has landed (as of 2026-05-31):** prediction 1 ran text-side **$0** (a null,
2026-05-30); predictions 2–3 ran in the first image-input probe and landed as a **redundancy null**
(2026-05-31, [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)).
Only **prediction 4** (coercion under depiction) remains unrun; it requires image input
(image probe design [`design/multimodal-grounding-image-v1`](../../../experiments/designs/multimodal-grounding-image-v1.md)).

1. **Perceptual-strength moderation (text-side, the cheap bridge — runnable with no new probe).**
   Re-analyzing the *already-collected* lexical-v1 ratings
   ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)) moderated by
   the **Lancaster Sensorimotor Norms** (human perceptual/action strength ratings; CC BY 4.0;
   see [`base/resources/lancaster-sensorimotor-norms`](../../base/resources/lancaster-sensorimotor-norms.md)),
   the text-only panel's monotonicity (rating vs human DURel median) is **stronger for highly
   perceptually-grounded lemmas** than for abstract ones. *This is a within-text-model test of
   whether perceptual groundedness of a word predicts how well the model tracks its sense* — a
   first hint, before any image is shown, that grounding and sense-tracking are linked. **Null:**
   no moderation — a word's perceptual strength does not predict the model's tracking quality
   (sense-tracking is uniform across the abstract/concrete divide). A null here is itself
   informative and would lower the prior on predictions 2–4.
   **→ TESTED 2026-05-30 ($0): a NULL** — [`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md).
   No primary cell (`Max_strength.perceptual` × `durel` × 3 models) shows the predicted positive
   Δρ; all three are negative (−0.05 / −0.27 / −0.04), the only CI excluding zero (gpt-5.4-mini)
   runs the *wrong* way. The design is **underpowered** (21 lemmas/side, compressed range 2.44–4.95)
   so this is "no detectable moderation OR unresolvable," not a falsification — but it removes the
   hoped-for converging text-side hint and **lowers the prior on predictions 2–4**, exactly as the
   null clause anticipated. Crucially it does **not** reach the prediction-2 *redundancy* null (that
   is an image-vs-text contrast); and the word-level Lancaster proxy is blunter than prediction 3's
   *sense-level* perceptual-distinguishability moderator, so a sharp image test is still warranted.
2. **Image-grounding divergence (the core multimodal claim).** Same panel, same graded-relatedness
   instrument, run **with disambiguating images of each usage vs text alone**: the image-conditioned
   rating **diverges** from the same model's text-only rating, and the divergence is **toward** the
   human DURel relatedness (lower absolute error / higher rank-agreement). **Null (redundancy):**
   image-conditioned and text-only ratings coincide within noise — the model already had the sense
   distinction from text. **Null (distraction):** the image moves ratings *away* from the human
   signal (e.g., toward image surface-similarity rather than sense relatedness).
3. **Perceptual-distinguishability is the moderator (the discriminating prediction).** The
   prediction-2 shift is **concentrated in sense pairs whose referents are visually distinct**
   (the vision adds contrast text under-determined) and **negligible for visually non-distinct or
   abstract pairs** (no perceptual contrast to add). This is what separates "vision adds
   sense-relevant signal" from "vision adds generic noise/help": the effect must be *keyed to where
   perception actually carries the distinction*. In particular, **homonym pairs with visually
   distinct referents should drop toward the human "different" floor under image input** — the
   route to clause (b) the text anchor could not reach.
   **→ TESTED 2026-05-31 (image probe): a REDUNDANCY NULL** — [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md). For clear homonyms the **text-only** panel already separates same- from different-synset pairs **perfectly (AUC 1.0)**, so the image cannot improve the binary separation (prediction-2 redundancy null in its strong form); the lone predicted-direction movement is one model on the continuous scale (gpt-5.4-mini, different-synset −8 toward "unrelated", surviving the distraction control), and claude shows a faint distraction-direction wobble. Bounds the strong reading **for clear homonyms**; fine polysemy (where text need not saturate) is untouched.
4. **Coercion under depiction (the grammar-end touchpoint, later).** Showing an image consistent
   vs. inconsistent with a coerced reading changes the model's coercion-sense-modulation behavior
   ([`result/coercion-sense-modulation-v1`](../results/coercion-sense-modulation-v1.md)) — connecting
   the multimodal axis to the existing lexicon↔grammar bridge. Lowest priority; listed to fix the
   integration target, not as a near-term unit.

## What would confirm / falsify

- **Confirm (grounding adds human-aligned sense signal):** prediction 2 (image moves behavior
  toward the human signal) **keyed by** prediction 3 (the movement is concentrated where senses are
  perceptually distinguishable), ideally with prediction 1's text-side moderation as a converging
  hint. The conjecture is supported only if the image beats the **text-only baseline** in the human
  direction — model-vs-model-modality contrast, not model-vs-model.
- **Redundancy null (a first-class negative):** image-conditioned behavior ≈ text-only behavior
  (prediction 2 null). The strong reading would be "a fluent text model has already saturated the
  perceptually-relevant sense distinctions from distribution alone" — a bound on how much the extra
  modality buys, and a notable result given the grounding literature's expectation that it should buy
  a lot. Write it as the null, not as failure.
- **Distraction null:** the image moves behavior *away* from the human signal — perception is acting
  as surface-similarity noise, not sense signal. Also first-class; it would say image input is not
  automatically grounding in the meaning-relevant sense (the Harnad/Barsalou caveat that good
  perceptual-task behavior ≠ a perceptual symbol system, made concrete).
- **Falsify the directional shape:** prediction 2 holds but prediction 3 fails — the image changes
  ratings uniformly, *not* keyed to perceptual distinguishability. That would mean the image is a
  generic prompt-perturbation, not a sense-relevant grounding signal, and the "grounding" reading is
  unwarranted.

The discriminating clause is **prediction 3**: an undifferentiated image effect (prediction 2 alone)
does not establish grounding; the effect must be *keyed to where perception carries the sense
distinction*. This is the multimodal analogue of the lexical conjecture's load-bearing context-control
clause (c) and the constructional wedge's beat-the-distributional-shadow discipline.

## Human anchor

`anchor: pending` — the anchor-*class* choice is **ratified**
([`decisions/resolved/multimodal-panel-and-grounding-theory`](../../decisions/resolved/multimodal-panel-and-grounding-theory.md),
Q3=B GO); the **which-anchor** choice is now ratified too
([`decisions/resolved/multimodal-image-anchor`](../../decisions/resolved/multimodal-image-anchor.md),
2026-05-31, Tom: "A stands" — WordNet-keyed constructed set, binary-scoped). The candidate anchors,
scouted and verified for license/fetchability/meaning-bearing in
[`base/resources/multimodal-anchor-scouting.md`](../../base/resources/multimodal-anchor-scouting.md):

- **Prediction 1** anchors to the **Lancaster Sensorimotor Norms** (Lynott et al. 2020, CC BY 4.0)
  as a *moderator* on the existing human DWUG signal — a join of two already-validated human
  resources, $0, no new probe. This is the immediately-runnable unit (default Q3-A).
- **Predictions 2–3** need an **image-paired graded-sense resource**: either a constructed
  image-sense set (target words depicted in two usages, rated against a human sense inventory — new
  stimuli + a new image probe) or an existing graded human perceptual-similarity set
  (**THINGS-data** triplet judgments, CC0 [per a secondary source; the OSF README was not directly
  verified this run — see the scouting note] — but those are object-similarity, not word-sense, so
  they test a *related* claim, not this one directly). Which to build/fetch is the Q3-B decision.

Anchor caveats, stated plainly:
- The two gates that once held this at `proposed` are now both met: (a) the anchor-class decision is
  ratified ([`decisions/resolved/multimodal-panel-and-grounding-theory`](../../decisions/resolved/multimodal-panel-and-grounding-theory.md),
  Q3=B GO; image anchor "A stands"), and (b) the predictions-2–3 anchor (the WordNet-keyed constructed
  set) was fetched + verified + frozen and its v1 result is anchored and promoted. The conjecture is
  now **partially tested** (predictions 1–3 ran, both negative); the page-level `anchor: pending`
  scopes only the still-unrun **prediction 4** (coercion under depiction), whose image-paired anchor is
  not yet built.
- **Human usage-similarity is the operational stand-in for sense relatedness** (carried from the
  lexical conjecture); the multimodal version adds that **image depiction is itself a designed
  variable**, not a human judgment — the human anchor stays the relatedness/similarity rating, the
  image is the manipulation.
- Model-agreement is never the anchor: the conjecture's force is movement toward an **independent
  human signal** (DURel relatedness, Lancaster perceptual strength), never the panel agreeing with
  itself across modalities.

## Notes / caveats

- **Feasibility is settled, capability-wise.** All three current panel families already accept image
  input (verified 2026-05-30; [`experiments/notes/multimodal-panel-feasibility.md`](../../../experiments/notes/multimodal-panel-feasibility.md)),
  and the harness now sends images, so the text-vs-image contrast can be run **within the same model
  family** — the cleanest design (modality toggled, family held constant). No model-family swap is
  forced (unlike the AANN logprob blocker).
- **Discriminative-vs-generative gap.** The VLM-compositionality literature
  ([`concept/multimodal-compositionality`](../../base/concepts/multimodal-compositionality.md);
  Winoground/ARO/SugarCrepe) measures *image-text matching* in contrastive encoders, which is a
  narrower behavior than this project's *generative* panel rating relatedness. This conjecture probes
  the generative panel directly; the compositionality benchmarks are a **caution** (VLMs often behave
  like bags-of-words) and a **prior**, not a substitute instrument. Do not equate the two.
- **Grounding ≠ a perceptual symbol system.** Per [`concept/embodied-cognition`](../../base/concepts/embodied-cognition.md),
  even a confirmed image effect shows the model's behavior is *sensitive to* perceptual input, not
  that it has Barsalou-style modal simulators or has closed the Harnad regress. Any result must keep
  "the image changed the rating in the human direction" separate from "the model is perceptually
  grounded in the theoretical sense."
- **Externalist gap unchanged.** This conjecture bears on `grounded.perceptual` and
  `referential.sense`; it does **not** touch `referential.externalist` (Putnam/Evans, still
  un-anchored in-repo). Perceptual grounding is not reference-fixing; do not let an image effect be
  read as the model tracking *reference*.
- **Single-axis, modest N — borne out.** Like the lexical probes, the realized image result was a
  single run on a modest item set (n=12 WordNet-keyed pairs, 3 models;
  [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)) — a
  grounding-signal probe, not a coverage benchmark. The redundancy null is correspondingly bounded: the
  text-only panel was already at ceiling (AUC 1.000 every cell), so there was no separation headroom for
  the image to add, the gold is author synset-assignment (not per-item human labels), and fine polysemy
  was untouched.
