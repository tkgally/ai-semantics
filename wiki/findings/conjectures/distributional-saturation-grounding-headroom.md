---
type: conjecture
id: distributional-saturation-grounding-headroom
title: The grounding-headroom hypothesis — perceptual input can move an LLM's lexical-sense behavior only in the residual the text distribution under-determines, and for concrete sense that residual is empirically narrow
meaning-senses:
  - grounded.perceptual
  - distributional
  - referential
status: proposed
contingent-on: []
created: 2026-05-31
updated: 2026-06-24
links:
  - rel: refines
    target: conjecture/multimodal-lexical-grounding-divergence
  - rel: depends-on
    target: result/lexical-perceptual-grounding-moderation-v1
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v1
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: theory/lexicon-grammar-continuum
---

# Conjecture: the grounding-headroom hypothesis (the project's own forward bet on *where* perceptual input can help)

> **Status: proposed (2026-05-31; first confirming-direction evidence 2026-06-27).** This is the
> project's **own theoretical proposal**, not an imported claim and not an established result. It
> generalizes **two bounded, partly-underpowered clear-homonym grounding nulls** (joined first by one
> **inconclusive** image-native VWSD run — [`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md)
> — and now by a **re-operationalized VWSD run that SUPPORTS the gating *shape*** of prediction 1,
> 3/3 models in direction and distraction-controlled — [`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md),
> detailed under "Human anchor" below) into a single
> structural explanation and a forward, falsifiable prediction. It is
> a forward bet whose gating shape now has **first supporting evidence on a binary selection task** but
> is **not** otherwise confirmed (the "narrow headroom" magnitude sub-bet is untested; prediction-1-as-written
> on a graded gradient is untested), and it could still be wrong (see "What would confirm / falsify"
> and "Honesty"). It **sharpens** the sibling conjecture
> [`conjecture/multimodal-lexical-grounding-divergence`](multimodal-lexical-grounding-divergence.md):
> that page states the *divergence* bet and registers a *redundancy* and a *distraction* null as
> first-class negatives; this page proposes the **positive `where`-to-look prediction** those nulls
> imply — it does not restate the sibling's predictions, it gives them a structural cause and a
> sharper target.

## The proposal

The project's grounding axis currently stands at **two clear-homonym negatives plus one inconclusive
image-native VWSD run** (session 100, [`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md),
which neither confirms nor falsifies the gating prediction below — detailed under "Human anchor"). The
two negatives, both obtained on **clear homonyms**, are:

- a **text-side moderation null** — a word's static perceptual groundedness does not predict how well
  a text-only model tracks its graded senses
  ([`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md)),
  and
- an **image-side redundancy null** — showing the depicting picture does not improve the panel's
  same-sense / different-sense separation, because the text-only panel already separates clear
  homonyms perfectly
  ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)).

The image result's own lead caveat already names the structural reason: *the test is least sensitive
exactly where it looks cleanest* — clear homonyms maximize both visual distinctness **and** text
separability, so the text distribution saturates the distinction and the image has nothing to add.
This conjecture takes that observation and turns it into a general principle, on the project's own
authority.

> **The grounding-headroom hypothesis.** Let Δ be the change in a model's graded lexical-sense
> behavior caused by adding disambiguating perceptual input (an image of each usage). Then **Δ is an
> increasing function of how far the text distribution *under-determines* the sense distinction.**
> Perceptual grounding can move an LLM's lexical-sense behavior **only in the residual** the text
> distribution leaves under-determined — the *headroom*. Where text already determines the distinction
> (clear homonyms; text-only separation at ceiling), Δ ≈ 0 (the redundancy null). Where text
> under-determines it (fine polysemy; abstract or perceptually-subtle senses; rare words), Δ > 0 is
> predicted. And — the project's further empirical bet — **for concrete lexical sense the headroom is
> narrow**: a model fluent enough to be worth probing has, for most clearly-pictureable words, already
> extracted the sense-relevant distinction from text, so the cases where grounding *can* help are a
> minority, not the rule.

Stated at the regime endpoints:

| text regime | text-only separability | predicted grounding effect Δ |
|---|---|---|
| **saturated** (clear homonyms; text-only AUC ≈ 1.0) | at ceiling | **Δ ≈ 0** — the redundancy null (already observed) |
| **under-determined** (fine polysemy; abstract / perceptually-subtle senses; rare words; text-only AUC < 1.0) | headroom present | **Δ > 0** — predicted positive, *not yet tested* |

The hypothesis is deliberately a claim about *where* grounding can act, not *that* these models are
or are not grounded. It says: grounding's reach is bounded by the distributional shadow, and that
shadow happens to be tall — to the point of saturation — for the very cases (concrete, depictable
homonyms) the literature treats as the obvious place a picture should help.

## Why this is interesting

- **It converts two negatives into one positive bet.** A redundancy null and a moderation null read
  separately are just "grounding didn't show up." Read together through this hypothesis, they are
  evidence for a *structural ceiling* — text saturation — that predicts grounding **will** show up
  elsewhere, in the under-determined residual. That is the difference between "we found nothing" and
  "we found *why* we found nothing, and where to look next." (It remains a bet: the residual prediction
  is untested.)
- **It explains the design gap the sibling conjecture flagged, structurally.** The sibling page noted
  that its clause-(b) route via the text-only DWUG anchor failed for a *design* reason — DWUG supplied
  no clean cross-sense homonym pairs — and that a constructed image-paired set could supply the
  contrast. The image probe then ran on exactly such a set and still saw redundancy, because the
  constructed clear-homonym set saturates text too. This conjecture says that is **not** another design
  accident: clear homonyms saturate text *by their nature* (unrelated senses, maximally distinct
  contexts), so any clear-homonym set will show redundancy. The only way out is to move to the regime
  where text genuinely under-determines — which is the falsification handle below.
- **It rests on a real positive, not only on nulls.** The saturation story needs the easy cases to be
  genuinely text-solvable, and they are:
  [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md) found the text-only
  panel's graded sense-relatedness rating strongly rank-correlated with the human DURel median
  (Spearman 0.60–0.83, in or above the human inter-annotator range) and surviving a context-similarity
  control. So for the easy/concrete cases text *carries* the distinction — which is exactly the premise
  that leaves no headroom for an image. The conjecture is the conjunction of this positive and the two
  nulls.
- **It is a sharpening of the project's distributional-shadow discipline into the third axis.** The
  [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) page frames the
  multimodal axis as the same "beat the distributional shadow" skeleton with a *different* null — "the
  text already gave it away" (perceptual redundancy). This conjecture makes that null **quantitative
  and predictive**: redundancy is not a fixed property of the modality, it is a *function of the text
  regime*, maximal at saturation and falling toward zero as text under-determination grows. The
  headroom is the residual of the distributional shadow.

## What this sharpens in the sibling conjecture

[`conjecture/multimodal-lexical-grounding-divergence`](multimodal-lexical-grounding-divergence.md)
states the divergence bet (image moves behavior toward the human signal, keyed to perceptual
distinguishability) and books a redundancy null and a distraction null as first-class negatives. It
does **not** say *where* on the lexical space the divergence should be found, beyond "where senses are
perceptually distinguishable." This conjecture adds the missing coordinate: **the divergence lives in
the text-under-determination residual**, not merely wherever vision *could* contrast two referents.
The two are distinct — a clear homonym's referents are maximally visually distinct (the sibling's
"perceptually distinguishable") *and* maximally text-separable (zero headroom), so the sibling's
own discriminating prediction (its prediction 3) is, on this hypothesis, **pointed at the wrong cell**
when run on clear homonyms: visual distinctness and text headroom are positively correlated for
homonyms, so "most visually distinct" selects for *least* headroom. The grounding-headroom hypothesis
predicts the effect is found instead where **visual contrast is present but text separability is
not** — fine polysemy and perceptually-subtle senses — which is a narrower and harder target than the
sibling's framing implies. This is a refinement (a sharpening of *where*), not a contradiction: both
pages predict Δ ≈ 0 on clear homonyms (the observed redundancy null); they differ on the positive
target, and this page's is the more specific.

## Predictions

1. **Headroom gating (the core prediction).** Run the existing image probe's instrument on a set
   stratified by **text-only baseline separability**. Δ (image-induced movement toward the human
   sense-relatedness signal) should be **near zero in the saturated stratum** (text-only AUC ≈ 1.0 —
   the already-observed redundancy null) and **positive in the under-determined stratum** (text-only
   AUC < 1.0 — fine polysemy; abstract or perceptually-subtle sense pairs). The within-set signature is
   a **negative correlation, across items, between text-only baseline separability and image-induced
   improvement**: the less text already separates a pair, the more the picture moves it toward the
   human signal. **Null:** Δ is flat across the separability range (grounding never helps these models
   for sense, even in the residual) — which would *falsify* the hypothesis, not merely fail to support
   it (see below).

2. **The redundancy null is regime-specific, not modality-specific.** The redundancy null already
   observed ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md))
   should **reappear on any clear-homonym set** (it is structural, not an artifact of the particular 12
   pairs) and should **not** appear on a matched under-determined set drawn from the same panel and
   instrument. This is the discriminating contrast: same models, same instrument, two text regimes,
   opposite Δ. (Contrast with the sibling conjecture, which books the redundancy null as a possible
   global outcome; this page predicts it is *local to the saturated regime*.)

3. **Narrow headroom for concrete sense (the bet that could most easily be wrong).** Even in the
   under-determined stratum, the **magnitude** of Δ for concrete, depictable senses should be **modest**
   — because most concrete words a fluent model is worth probing on are already largely text-determined,
   so the residual is small. The hypothesis predicts grounding's lexical-sense payoff is real but
   *bounded* and *concentrated*, not a broad lift. (If grounding turns out to help broadly, including
   for clearly text-saturated cases, the hypothesis is wrong — that is prediction 2's falsifier; if it
   helps in the residual but *largely*, the "narrow headroom" sub-bet is wrong while the gating shape
   survives. The two sub-claims fail independently and should be reported separately.)

## What would confirm / falsify

- **Confirms.** Run the image probe on **fine-polysemy / abstract or perceptually-subtle sense pairs
  where the text-only AUC < 1.0**, and find that the image moves behavior **toward** the human signal
  *there* (a positive Δ), unlike the saturated clear-homonym case (Δ ≈ 0); **and** a **negative
  correlation across items between text-only baseline separability and image-induced improvement**.
  That conjunction — positive in the residual, null at saturation, with the gating correlation — is the
  signature.
- **Falsifies (two distinct ways).**
  - **The image helps even where text already saturates** (a positive Δ in the AUC ≈ 1.0 stratum that
    survives a distraction control). That breaks the "only in the residual" clause — grounding would be
    adding sense signal *on top of* a determined distinction, contradicting the headroom mechanism.
  - **The image fails to help where text demonstrably under-determines** (Δ ≈ 0 in the AUC < 1.0
    stratum, distraction-controlled). That breaks the "headroom is sufficient" clause — grounding would
    *never* move lexical sense for these models, even given room, so the redundancy null was not about
    saturation at all but about the modality being inert for sense. (This is the live possibility the
    Honesty section flags: grounding might never help, or might help via a route this hypothesis does
    not predict.)
- **A distraction-driven positive is not a confirmation.** As the image probe established, a model that
  does *zero* sense computation and merely rates "two visibly different pictures → less related"
  reproduces a positive Δ on distinct-referent pairs by surface dissimilarity alone. Any positive must
  survive the same-referent distraction control the image probe built (same referent, two different
  photos), or it is the distraction null, not headroom.

The load-bearing clause is **prediction 1's gating**: an undifferentiated image effect does not
establish the hypothesis, and an undifferentiated null does not either — the claim is specifically
that Δ is **conditioned on text under-determination**, so the test must vary that condition and read
the interaction, not a main effect.

## Human anchor

`anchor: pending` — this is a conjecture; **no resource anchor is required or asserted here**, and the
candidates below are named only as the anchors a *future result* testing this hypothesis would need
(none is claimed to already cover it). Candidates, all in-repo except the fine-polysemy image set:

- **Visual word-sense disambiguation (VWSD)** is the natural image-native task this grounding axis
  should move to. It is image-native (sense selection *requires* the image) rather than image-as-add-on,
  so it directly instantiates the under-determined regime. **Now in-repo as a typed resource**
  ([`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md), scouted/catalogued s97).
  **Scope note (decision [`decisions/resolved/vwsd-grounding-headroom-dv`](../../decisions/resolved/vwsd-grounding-headroom-dv.md), ratified s99, ADOPT MODIFIED):**
  VWSD's human gold is **binary correct-image selection**, not the **graded** relatedness signal
  prediction 1 is written around. A VWSD probe therefore tests the conjecture's **gating *shape*** via a
  **selection-accuracy interaction** (per-item text-only separability × image-induced selection
  improvement, predicted negative) and is **explicitly not a test of prediction-1-as-written** (the
  graded-Δ × separability interaction against a human relatedness gradient), which remains open for a
  **future graded-image resource**. The VWSD operationalization, its binding pre-spend conditions, and
  the distraction control are fixed by that resolved decision.
  **First run (session 100): [`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md).**
  On a frozen 50-item EN-gold subset the **caption-text baseline saturated** (per-model .86–.88; 40/50
  text-separable), leaving only 7 under-determined items — **below the stratification floor**, so the
  binned gating interaction was **not** reported. The **distraction control was clean** (word-ablated
  gold-selection at chance .093) and **real images gave no broad lift** over their captions (gpt was
  *worse* with images), rescuing only 4/16 text-failed cells. The run therefore **neither confirms nor
  falsifies** the gating prediction on VWSD (caption-leakage confound + floor + underpower); it adds a
  bounded reappearance of the redundancy null in an image-native selection task.
  **Second run (sessions 107/112/121): [`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md) — the re-operationalization (non-caption Option-B visual-form descriptor baseline, stratified N=120 clearing the ≥15 floor, raised claude `max_tokens`) makes the interaction testable and it SUPPORTS the gating *shape*, 3/3 models in direction:** with the word-ablated DISTRACT control clean (pooled .097 ≈ chance), the real image rescues the descriptor-text-failed (under-determined) cells (pooled .453; per-model .500/.303/.609, all > chance) while adding no lift where the descriptor already separates (saturated Δ −.122). This is the **first confirming-direction** evidence on the grounding axis, supporting prediction 1 (gating shape) and prediction 2 (regime-specific redundancy). Honest bounds carried: gemini's floor is elevated (.158, LB > chance), gpt degrades overall (gating sign-only for it), and the headroom **magnitude** is inflated by the de-referented descriptor channel — so prediction 3 ("narrow headroom") is **not** supported here, and the read is gating-shape-on-binary-selection, **not** prediction-1-as-written, **not** reference. The conjecture stays
  **`proposed`** (one supporting run on binary selection; a later session may weigh `proposed → tested` and design the natural-language-baseline magnitude test).
- **The human sense anchor** for the relatedness/separation judgments would be WiC's binary
  same/different labels ([`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md))
  and/or the Princeton WordNet synset inventory
  ([`resource/wordnet-sense-inventory`](../../base/resources/wordnet-sense-inventory.md)) — both
  in-repo and verified, already used by the image probe and the lexical-v3 design.
- **A fine-polysemy image set** (target words depicted in two *related-but-distinct* usages, in the
  regime where text under-determines) is **not yet in-repo**; images would be sourced PD/CC0 as in the
  prior image probe (Wikimedia Commons, downscaled + sha256-frozen before any model call). Building it
  is the unit a confirming run would require.

Anchor caveats, stated plainly:
- **Model agreement is never the anchor.** The hypothesis's force is movement toward an *independent
  human signal* (WiC / WordNet / a graded relatedness rating), never the panel agreeing with itself
  across modalities or strata.
- **Text-only baseline separability is a *measured covariate*, not a human label.** Prediction 1's
  stratification is on the panel's own text-only AUC — a model-side quantity. The interaction it
  predicts is between that covariate and the human-anchored Δ; the covariate must be computed and
  frozen *before* the image condition is run, on pain of retuning the indicator after seeing results
  (the operationalization gate the protocol forbids).
- **Per-item human sense labels would strengthen any test.** The image probe's gold was author
  synset-assignment, not per-item human judgment; a VWSD or WiC-anchored run with released per-item
  labels would be a cleaner anchor for the under-determined stratum.

## Notes / caveats

- **This generalizes two bounded, partly-underpowered nulls — it is the project's forward bet, not a
  finding.** The moderation null is **underpowered** (≈21 lemmas/side, compressed moderator range) and
  is explicitly "no detectable moderation OR unresolvable," not evidence against grounding
  ([`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md)).
  The redundancy null is **n=12 pairs, 3 models, single run**, on a set engineered to be clear homonyms
  ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)). Neither is a
  proven *absence* of grounding; they are bounded negatives in one regime. A hypothesis built on two
  such nulls is a calibrated guess about structure, and the right posture is to under-claim until the
  residual prediction is tested.
- **It could be wrong in at least two ways the predictions cannot pre-empt.** (a) Grounding might never
  move lexical sense for these models — the redundancy null would then reflect an inert modality, not a
  saturated text channel, and the residual prediction (1) would fail (its second falsifier). (b)
  Grounding might help via a route this hypothesis does not predict — e.g., changing *abstract* sense
  behavior with no visual contrast at all (a non-perceptual prompt-shift effect), or helping uniformly
  rather than gated by headroom (prediction 1's null). Both are first-class outcomes; the hypothesis is
  offered as the sharpest *testable* structure consistent with current evidence, not as the only one.
- **Headroom is a property of the *text distribution × model*, not of the word alone.** "Saturated"
  means *this panel's* text-only separation is at ceiling for *this pair*; a weaker model, or a rarer
  word, could leave headroom on a pair another model saturates. So the stratification must be computed
  per-model (the text-only AUC is model-specific in the image result — and indeed it was 1.000 for all
  three there). The hypothesis is about the model's own residual, which is why prediction 1 reads an
  *interaction*, not a fixed word list.
- **`grounded.perceptual` / `referential.sense` only — not reference.** Like the sibling conjecture,
  this bears on perceptual grounding of *sense* ([`concept/polysemy`](../../base/concepts/polysemy.md):
  Fregean `Sinn` at fine grain) and on the
  [`concept/grounding`](../../base/concepts/grounding.md) gradual framing; it does **not** touch
  `referential.externalist` (Putnam/Evans, still un-anchored in-repo). A positive Δ would show behavior
  *sensitive to* perceptual input in the residual, **not** a Harnad-style perceptual symbol system or
  reference-fixing — keep "the image moved the rating in the human direction" separate from "the model
  is perceptually grounded."
- **It integrates, it does not replace.** Like the sibling, any test reuses the *same* DURel-style
  graded-relatedness instrument the lexical program validated, toggling modality and stratifying by
  text regime — so a result lands on the lexical end of the
  [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) cline and refines the
  third-axis section there (which currently records the two negatives this conjecture is built on).
