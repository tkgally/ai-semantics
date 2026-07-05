---
type: result
id: multimodal-grounding-image-v1
title: The first image-input probe — showing the depicting picture does NOT improve the panel's sense-relatedness behavior (a redundancy null; text already separates the senses perfectly), with one small gpt-5.4-mini scale-framing exception
meaning-senses:
  - grounded
  - grounded.perceptual
  - referential.sense
  - distributional
  - human-comparison
status: proposed
anchor: resource/wordnet-sense-inventory
contingent-on: []
created: 2026-05-31
updated: 2026-07-05
links:
  - rel: anchors
    target: resource/wordnet-sense-inventory
  - rel: supports
    target: conjecture/multimodal-lexical-grounding-divergence
  - rel: refines
    target: result/lexical-perceptual-grounding-moderation-v1
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/symbol-grounding-problem
  - rel: depends-on
    target: concept/embodied-cognition
  - rel: depends-on
    target: concept/polysemy
---

# Result: the project's first image-input probe — a redundancy null

> **Status: proposed (2026-05-31).** The project's **first probe that sends image input to the
> panel** (predictions 2–3 of [`conjecture/multimodal-lexical-grounding-divergence`](../conjectures/multimodal-lexical-grounding-divergence.md)).
> Design [`design/multimodal-grounding-image-v1`](../../../experiments/designs/multimodal-grounding-image-v1.md);
> run record + `PREREG.md` in [`experiments/runs/2026-05-31-multimodal-grounding-image-v1/`](../../../experiments/runs/2026-05-31-multimodal-grounding-image-v1/README.md).
> Cost **$0.2286 billed**, 144 calls, 0 NA. Independent pre-run critic (forced the anchor relabel +
> stimulus fixes) + independent post-run verifier (every figure reproduced from raw, 0 re-parse
> mismatches). The anchor decision [`decisions/resolved/multimodal-image-anchor`](../../decisions/resolved/multimodal-image-anchor.md)
> was **ratified 2026-05-31 (Tom: "A stands")** — `contingent-on: []`; the null stands on its
> WordNet sense-inventory anchor, scoped to the binary same/different-synset separation.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The grounding axis moved after this
> page: [`result/vwsd-grounding-headroom-v1`](vwsd-grounding-headroom-v1.md) (session 100) saturated
> its caption baseline and was inconclusive on the gating prediction, then
> [`result/vwsd-grounding-headroom-v2`](vwsd-grounding-headroom-v2.md) (session 121) returned the
> first confirming-direction positive (gated-rescue shape, 3/3 models in direction), and
> [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
> was promoted `tested` (gating shape only) in session 130. The fine-polysemy magnitude was
> documented un-instrumentable on current open resources —
> [`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md)
> (an externally-released graded-image set is the only route).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## One-line finding

Showing the panel **two small pictures depicting each usage** does **not** make its graded
sense-relatedness behavior separate same-sense from different-sense word pairs any better than the
**byte-identical text-only** prompt — because the text-only panel **already separates them perfectly**
(AUC = 1.000 in every cell, text *and* image). This is the conjecture's **redundancy null** in its
strong form, for clear homonyms. The only movement in the predicted direction beyond noise is a
**single model on the continuous scale** (gpt-5.4-mini, 0–100 framing); one model (claude) shows the
opposite micro-wobble on the surface-similarity control.

## Setup (frozen; see PREREG)

- **Anchor (realized):** constructed minimal pairs keyed to **Princeton WordNet** synsets
  ([`resource/wordnet-sense-inventory`](../../base/resources/wordnet-sense-inventory.md)) — *not* WiC
  (WiC's actual items under-covered clean visually-distinct homonyms). **The same/different gold is the
  author's synset assignment** (verified distinct vs identical synsets, e.g. `bat.n.01` mammal vs
  `bat.n.05` club), **not a per-item human label** — weaker than a released human judgment, scoped
  accordingly. The image is a **designed manipulation**, never a human judgment.
- **12 word pairs, 2 strata:** 6 **distinct-F** visually-distinct homonyms (gold = *different* synset:
  bat, crane, bank, pitcher, mouse, seal) + 6 **same-T** controls (gold = *same* synset, two contexts +
  **two different photos** of that referent — the surface-similarity / distraction control). 24 images,
  Wikimedia Commons PD/CC0/CC-BY(-SA), ≤256px, sha256-frozen before any model call.
- **Conditions:** TEXT-ONLY vs IMAGE+TEXT, **byte-identical user prompt** (a constant system clause
  notes that *if* images are attached they depict Context 1/2). Instrument: DURel 4-pt + 0–100 scale,
  temp 0. Panel: claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash. 12 × 2 × 2 × 3 = 144 calls.

## Results

**Mean relatedness rating, text → image (same-sense / different-sense pairs):**

| model | framing | same (text→img) | different (text→img) | AUC text | AUC img | Δsep (img−txt) |
|---|---|---|---|---|---|---|
| claude | DURel | 4.00 → 4.00 | 1.33 → 1.33 | 1.000 | 1.000 | +0.00 |
| gpt | DURel | 4.00 → 4.00 | 1.50 → 1.33 | 1.000 | 1.000 | +0.17 (CI∋0) |
| gemini | DURel | 3.83 → 3.83 | 1.33 → 1.33 | 1.000 | 1.000 | +0.00 |
| claude | scale | 98.8 → **95.8** | 6.67 → 6.67 | 1.000 | 1.000 | **−3.0** (CI [−5,−1]) |
| gpt | scale | 99.7 → 99.0 | 18.0 → **10.2** | 1.000 | 1.000 | **+7.2** (CI [+0.03,+13.3]) |
| gemini | scale | 99.2 → 98.3 | 7.50 → 8.33 | 1.000 | 1.000 | −1.7 (CI∋0) |

1. **The text-only baseline is at ceiling — AUC = 1.000 in all 12 cells.** Every model, both framings,
   **from the sentences alone**, perfectly ranks same-synset pairs above different-synset pairs (e.g.
   DURel claude same=4 vs diff∈[1,2]; scale gpt-text same∈[98,100] vs diff∈[15,21]). For clear
   homonyms, the binary sense distinction is **fully carried by the text distribution** — there is
   essentially no separation headroom for an image to add. **This is the redundancy null.**
2. **DURel framing: no image effect at all.** Ratings are byte-identical text vs image except a single
   gpt item (diff 1.50→1.33). The 4-pt scale is saturated (same=4, different=1), so it cannot register
   any image movement.
3. **0–100 scale, the one positive cell — gpt-5.4-mini.** Where the continuous scale leaves headroom,
   the image moves gpt's **different-synset** ratings **down ~8 points toward "unrelated"** (18.0→10.2)
   while same-synset pairs barely move — Δsep **+7.2, bootstrap CI excludes 0**, prediction-3 contrast
   +7.2. The drop is broad, not an outlier (bat −13, crane −13, mouse −16, seal −10). This is the
   predicted direction (prediction 2/3): the picture nudges already-separated senses *further* apart.
4. **0–100 scale, the distraction wobble — claude.** claude's **same-sense** ratings drop ~3 points
   under image (98.8→95.8, across 4 items) while different-sense ratings hold — i.e. two *different
   photos of the same referent* made claude rate the pair slightly *less* related. That is a faint
   reading of the **distraction null** (image surface-dissimilarity, not sense) on the control stratum,
   not grounding. gemini is essentially flat both framings.

## Interpretation (modest, bounded)

- **The headline is the redundancy null, in its strong form.** The conjecture's redundancy clause —
  "a fluent text model has already saturated the perceptually-relevant sense distinctions from the
  distribution alone" — is borne out here as literally as possible: the text-only panel's binary
  separation is **already perfect (AUC 1.0)**, so the depicting image has nothing to improve. Combined
  with the prediction-1 null ([`result/lexical-perceptual-grounding-moderation-v1`](lexical-perceptual-grounding-moderation-v1.md)),
  the multimodal axis now has **two negatives**: a word's perceptual groundedness doesn't predict
  text-only sense-tracking, and *showing the picture* doesn't improve sense separation for clear
  homonyms.
- **The lone gpt-scale positive is real but small and cannot be read as "grounding."** It is one model,
  one framing, n=6 per stratum, and — the load-bearing caveat — **distinct-F gold is confounded with
  image surface-dissimilarity by construction**: a model that does *zero* sense computation and simply
  rates "two visibly different pictures → less related" reproduces exactly this pattern. The same-T
  distraction control is the only guard, and gpt passes it (same-T stable while distinct-F dropped) —
  consistent with, but **not proof of**, sense-relevant use of the image. The honest claim is
  **behavioral and binary**: on a continuous scale with headroom, the image pushes gpt's already-distinct
  pairs further toward "unrelated," surviving the surface-similarity control — *not* "gpt is perceptually
  grounded."
- **Why the test is least sensitive exactly where it looks cleanest.** Clear homonyms maximize visual
  distinctness *and* text separability together, so text saturates and the image is redundant. The cell
  where an image could matter — **fine polysemy / abstract senses where text does *not* saturate** — is
  exactly the cell this set does not contain (the abstract-F stratum was deferred to v2 because abstract
  senses can't be faithfully depicted). So this null **bounds the strong "grounding repairs sense"
  reading for clear homonyms** and does **not** speak to fine polysemy — the open clause-(b) territory
  the text-only [`result/lexical-polysemy-homonymy-v2`](lexical-polysemy-homonymy-v2.md) and the WiC
  [`design/lexical-polysemy-homonymy-v3`](../../../experiments/designs/lexical-polysemy-homonymy-v3.md)
  target.

## Caveats (lead with these)

- **Underpowered + redundancy-by-design.** 12 items (6/stratum), n=3 models, single run. The text
  ceiling (AUC 1.0) means the primary contrast had almost no room to move — a null here is "no
  detectable image effect on an already-saturated separation," not evidence that grounding is
  impossible.
- **Image-dissimilarity confound** (above): the probe cannot distinguish perceptual grounding of *sense*
  from graded image-*surface*-dissimilarity tracking. Stated in PREREG before the run.
- **Gold is author synset-assignment, not per-item human labels** (WordNet inventory is the human part;
  the sentence→synset mapping is the author's). Weaker than WiC/SemCor; the anchor choice was ratified in
  [`decisions/resolved/multimodal-image-anchor`](../../decisions/resolved/multimodal-image-anchor.md)
  (Tom: "A stands").
- **Binary-scoped, not graded; not a grounding verdict.** Per [`concept/embodied-cognition`](../../base/concepts/embodied-cognition.md)
  and [`concept/symbol-grounding-problem`](../../base/concepts/symbol-grounding-problem.md), even the gpt
  effect shows behavior *sensitive to* image input on a continuous scale, not a perceptual symbol system.

## Relation to other findings

- **Supports** [`conjecture/multimodal-lexical-grounding-divergence`](../conjectures/multimodal-lexical-grounding-divergence.md)
  by realizing its **redundancy null** (prediction 2's first-class negative) and a faint **distraction
  null** (claude same-T), with one small positive cell consistent with predictions 2–3 (gpt scale).
- **Refines** [`result/lexical-perceptual-grounding-moderation-v1`](lexical-perceptual-grounding-moderation-v1.md):
  the text-side grounding null is now joined by an image-side redundancy null — the grounding axis is
  **two negatives** for the lexical wedge's clear-homonym end, with fine polysemy still open.
- Anchored to [`resource/wordnet-sense-inventory`](../../base/resources/wordnet-sense-inventory.md).
  `contingent-on: []` (anchor ratified 2026-05-31, [`decisions/resolved/multimodal-image-anchor`](../../decisions/resolved/multimodal-image-anchor.md):
  "A stands"). Cost $0.2286.
