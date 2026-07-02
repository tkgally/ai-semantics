---
type: theory
id: lexicon-grammar-continuum
title: One continuum, one test — lexical sense and constructional meaning as a single form–meaning cline, probed by the same "beat the distributional shadow" skeleton
meaning-senses:
  - constructional
  - referential
  - distributional
  - inferential
  - grounded
  - human-comparison
status: draft
contingent-on: []
created: 2026-05-30
updated: 2026-07-02
links:
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v2
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v3
  - rel: depends-on
    target: result/cross-axis-lexical-constructional-ordering-v1
  - rel: depends-on
    target: result/coercion-sense-modulation-v1
  - rel: depends-on
    target: result/coercion-sense-modulation-v2
  - rel: depends-on
    target: result/lexical-perceptual-grounding-moderation-v1
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: supports
    target: open-question/lexical-polysemy-gradience
  - rel: depends-on
    target: open-question/lexical-bridging-context-gradience
  - rel: depends-on
    target: essay/graded-scale-ungraded-commitment
  - rel: depends-on
    target: source/cao-2025-semantic-relation-knowledge
  - rel: depends-on
    target: source/diera-2026-encode-semantic-relations
  - rel: depends-on
    target: source/justeson-katz-1991-antonym-cooccurrence
---

# Theory (draft): the lexicon–grammar continuum, and the single test that spans it

## Why this page exists

The project has run on two tracks that looked separate: a **grammatical** wedge (constructional meaning — does a model track a construction's contributed inference?) with nine-plus own-design results, and, as of 2026-05-30, a **lexical** wedge (sense gradience — does a model track graded word-sense relatedness?) with its first result, [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md). Tom's steer is to connect them, in theory and empirically. This page argues they are **not two tracks but one**, and that the project has — without having named it — been applying a **single evidential test** on both. It is a synthesis page (a framework + a bridge), claiming a structure, not new data; the new data are on the two result pages it leans on.

## The continuum thesis (established in CxG, not novel here)

Construction Grammar's foundational move is that the lexicon and the grammar are **not different kinds of thing**. [`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md) states it directly: constructions "range from morphemes and closed-class items through idioms and argument-structure templates to large-scale discourse patterns" — a single inventory (a *constructicon*) along a cline of **specificity** and **schematicity**. A word is, on this view, a maximally specific construction (a form–meaning pairing with a fully fixed form); an argument-structure template is a maximally schematic one. There is no principled seam between "lexical meaning" and "grammatical meaning"; there is one form–meaning space at different grains. (CxG canon — Goldberg 1995/2006, Langacker, Croft 2001 — is referenced in `constructional-meaning` as not-in-repo; the continuum claim here rests on that concept page's in-repo statement of it, not on fabricated quotation.)

If that is right, then the project's two wedges are the **two ends of one cline**:

| | grain | the "meaning" tracked | the project's anchor | the distributional **shadow** (null) |
|---|---|---|---|---|
| **Lexical wedge** | maximally specific (a word) | graded **sense relatedness** of a word across uses ([`concept/polysemy`](../../base/concepts/polysemy.md)) | DWUG graded DURel judgments | **context/topic similarity** of the two sentences |
| **Grammatical wedge** | maximally schematic (a construction) | a construction's **contributed inference** ([`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md)) | Scivetti CxNLI / own minimal pairs | **n-gram frequency / surface form** |

## The single test: "does a meaning gradient beat the distributional shadow?"

Read across that table, the two wedges run the **same experiment**. In both, a fluent model has a *distributional structure for free* — co-occurrence neighbourhoods for words, surface-form regularities for constructions — and the live question is whether the model tracks a **meaning gradient that is not reducible to that distributional structure**. This is exactly the null-hypothesis discipline [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) imposes, and it is the spine of both the constructional evidence ladder ([`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md), where Tiers 1–3 must beat a frequency/form shadow) and the lexical conjecture's load-bearing clause (c) (the sense signal must survive a context-similarity control).

The two open-questions that name the shadow are explicitly parallel — [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md) (grammar: is it construction or n-gram frequency?) and the lexical conjecture's clause (c) / [`open-question/lexical-polysemy-gradience`](../open-questions/lexical-polysemy-gradience.md) (lexicon: is it sense or context similarity?). They are the **same question at two grains**.

**The state of the evidence, unified:** the project now has a *positive that beats the distributional shadow on **both** ends of the cline* —

- **Grammatical end:** the comparative correlative deploys its covariation inference above matched controls, survives conflicting world knowledge and operator embedding, and composes ([`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md) → v2 → v3). The shadow (form/frequency) does not explain it.
- **Lexical end:** the panel's graded sense-relatedness rating tracks the human DURel median (Spearman 0.60–0.83, in/above the human inter-annotator range) and **survives partialling out the model's own topic-similarity** ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)). The shadow (context similarity) does not explain it either. One scope note belongs here, because the word "gradience" carries two senses the project now keeps apart: v1 established a graded *scale* — a **cross-item** property, that the model's relatedness ratings rank-order many usage pairs the way humans do — and *only* that. Whether the model also shows graded *commitment* — a **within-item** property, intermediate / lower-confidence behavior on the single use that is itself a bridging context — was the unrun Prediction 4, scoped by [`open-question/lexical-bridging-context-gradience`](../open-questions/lexical-bridging-context-gradience.md) and argued in [`essay/graded-scale-ungraded-commitment`](../essays/graded-scale-ungraded-commitment.md). The two are logically independent: a model *could* rank-order smoothly yet still force every ambiguous item to a confident discrete pick (a graded scale, ungraded commitment). **That probe has now run (session 77, 2026-06-22) → exactly that: graded scale, ungraded commitment, a clean null on all three models** ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md)). On human-rated usage-similarity-midpoint ("bridging") pairs, every panel model places the pair at an **intermediate relatedness position** (inside the frozen [40,60] band, between saturated clear poles — the within-item echo of v1's cross-item scale) **yet meets it with clear-item confidence (≤5-pt spread, not robustly lower), almost never takes the explicit "UNCLEAR" decline option (≈0% on bridging), and shows near-zero forced-pick dispersion.** Commitment is ungraded on all three commitment instruments — agreement, not B–C disagreement, so it is reported as cleanly as a positive. An honest asymmetry runs through the result: the **position/scale half is the qualified half** — it partly tracks the model's own topic-similarity rating (Q3 Pearson r 0.32–0.53, n=24, a bound-but-weak within-item distributional shadow, the same caveat v1 carried, not a clean independent control) — while the **ungraded-commitment half is the robust half**, corroborated by three independent commitment instruments. The clear-class precondition was met 3/3, so the result is **DWUG-anchored** (capped to usage-similarity intermediacy, never certified sense co-presence; [`decisions/resolved/lexical-bridging-context-anchor`](../../decisions/resolved/lexical-bridging-context-anchor.md)), not collapsed to internal-contrast-only. It is behavioral not representational, on a small lemma-clustered N (24 bridging pairs / 17 lemmas), and its within-item discreteness is **complementary to, not a substitute for**, v3's between-stratum powered null.

This is the first time the project can state its central finding as a **cline-spanning** one rather than a grammar-only one: *current decoders track a graded form–meaning signal that beats the distributional null at both the word grain and the construction grain* — with the same caveats on both (behavioral not representational; single runs; modest N; the hard *negative* directions — divergent-form generalization on grammar, and on lexis the **polysemy/homonymy discreteness split**, now tested on a homonymy-enriched WiC anchor and returning a **powered null** ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md): no separate discrete regime over plain graded distance), so the *graded* signal stands but the *discrete-regime* bet does not). With Prediction 4 now run, the lexical cell reads: **graded scale beats the shadow on position; commitment is ungraded** — a within-item discreteness ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md)) to set beside v3's between-stratum discreteness null, with the honest asymmetry that the graded/position half is the bound-but-weak (Q3-shadowed) half and the ungraded-commitment half is the robust, three-instrument-corroborated half.

### The lexical pole is a relation-type gradient, not one cell

> **Update (2026-06-29, session 147).** The lexical pole above is read through one axis of the lexical wedge — the **graded sense-relatedness scale** (DWUG/DURel: does the model rank-order usage pairs the way humans do?). The wedge has a **second, complementary axis** the continuum should record: **relation-type recovery** — given the lexicographer's sense-relation vocabulary (hypernymy, hyponymy, holonymy, meronymy, antonymy, synonymy), how well does a model recover the relation? This axis is **word-form-level and sense-agnostic** — Cao's task "is performed at the word form level … and not the sense level" — so it is *complementary to*, not a restatement of, the graded-polysemy axis above. Two open-access sources ingested session 145 supply it, and they **converge**.

The two sources reach the same finding from opposite directions and are **prior-art on non-panel models** (so the gradient below is a literature datum and a *bet* for the panel, never a panel result): behaviorally and human-compared, [`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md) reports "**Antonymy is the outlier relation where all models perform reasonably well**" (Abstract) — in numbers, antonymy soundness 𝒮=0.57 against ~0.30 for the other relations (§8), the positive outlier *inside* a "**significant knowledge gap between humans and models for all semantic relations**" (Abstract) — on BERT/RoBERTa/Llama-3; representationally, [`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md) finds "**Difficulty is consistent across models (antonymy easiest, synonymy hardest)**" (Abstract) — on Pythia-70M/GPT-2/Llama-3.1-8B. So a behavioral relatum-production probe and an internal-representation probe agree on antonymy as the relation best recovered.

Read through *this page's own test*, that convergence is **deflationary**, not a competence win — the reading is argued in [`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md). The lexical pole's "beat the distributional shadow" skeleton asks whether relation structure is tracked **over and above** co-occurrence; antonymy is the relation where the shadow is **largest** — antonym pairs recur in tight, near-symmetric *contrastive frames* (conjoined "X and Y" and repeated-with-substitution phrases; "neither X nor Y", "from X to Y", "X versus Y" illustrative), a characterization now carrying a **primary corpus anchor** (Justeson & Katz 1991 on the Brown Corpus: antonyms co-occur far above chance, "**63% (139/219) … in lexically identical structures**", "**Fully 164 (75%) … in conjoined syntactic structures**" — [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md), §3, pp. 11-12; predicative adjectives, pre-LLM, not a panel claim), so antonymy is **maximally Harris-recoverable** and the "over-and-above" residual a competence claim must show is **smallest** there. So the lexical pole is not a single "graded scale beats the shadow" cell but a **relation-type gradient**: antonymy sits at the **shadow-saturated end** (smallest residual), with **meronymy and hyponymy** retaining a **larger residual** (part-whole and the hierarchical relations are less written into a symmetric contrastive frame). At the relation grain, the relation a model looks best at is the relation where "looking good" is *least* informative about anything beyond co-occurrence — the deflationary mirror of the graded-sense axis's positive. One rigor point the essay adds: the *cross-method* agreement (behavioral + representational) does **not** screen off the shared cause — both probes are downstream of the same training-time co-occurrence — so it *raises the prior* on the shadow reading rather than triangulating a competence (an *application* of the convergence ladder's screening-off concept to a cross-method case, **not** a claim the ladder itself makes).

The **panel-level** version of this gradient is the bet registered in [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md): on the project's own panel, against a contrastive-frame distributional control, antonymy is the relation whose recovery is **least separable** from the control (smallest control-adjusted residual), while meronymy/hyponymy keep a larger one. It is **recorded, not run** — spend-bearing; `anchor: pending` (the natural human anchor, Cao's released `ProbeResponses` relata, is **not adopted**: no LICENSE file, and a 10,507-vs-10,546 probe-count discrepancy still to reconcile); and no transfer from the prior-art models. So the relation-type axis enters the continuum as **prior-art plus a blocked conjecture**: it `refines` the lexical pole by predicting *which* relation least beats the shadow, complementing — not displacing — the established graded-sense positive ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)). Nothing here is a panel finding, and the panel test of the gradient is owed.

### Both poles are internally graded by shadow-depth — a second axis orthogonal to grain

> **Update (2026-07-02, session 165).** The relation-type gradient above is one instance of a more
> general structure that the presupposition line now makes visible at the *other* pole too, argued in
> [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md). Run this page's
> single test — *does the gradient beat the distributional shadow?* — across the whole cline and it
> sorts phenomena **not by grain but by shadow-depth**: how much of the phenomenon is already written
> into surface co-occurrence. That axis **cross-cuts** grain. Each pole turns out to hold *both* a
> demonstrated **shadow-beater** and a **shadow-saturated corner**:
>
> - **Lexical pole:** graded sense gradience ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md), beater — survives the topic-partial) vs antonymy relation-recovery (shadow-saturated — smallest over-and-above residual; [`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md)).
> - **Grammatical pole:** the comparative-correlative covariation inference ([`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md), beater — clears matched same-word controls) vs the **presupposition corner** (shadow-saturated — environment-gated in both signatures, cue-strength-graded; [`essay/presupposition-environment-gated`](../essays/presupposition-environment-gated.md), [`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md)).
>
> So **presupposition marks the grammatical pole's shadow-saturated end just as antonymy marks the
> lexical pole's** — the same structural move at both grains. This **sharpens** the continuum (adds a
> second ordering axis, orthogonal to grain, and locates the grammatical pole's shadow-saturated corner
> where the page previously recorded only the lexical pole's) and **complicates** the headline below:
> "beats the distributional null at both grains" is true of the *beaters* at both grains, but the
> grammatical pole is **not uniformly** a shadow-beater — its presupposition corner, on this reading, is
> not. **Calibration inherited from the essay:** the two shadow-*saturated* placements are
> **readings/bets, not controlled failures** — no matched distributional control has been run on the
> panel for either the antonymy corner (prior-art + the blocked
> [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md))
> or the presupposition corner (`internal-contrast-only`, no human comparison); the beaters, by
> contrast, *pass* a measured control. Shadow-depth is a property of the **phenomenon**, silent on which
> model tracks which (it does not touch the cross-axis competence dissociation below).

## The empirical bridge: coercion is where the two grains touch

The cleanest place the cline becomes a single phenomenon is **coercion** ([`concept/coercion`](../../base/concepts/coercion.md)) — a construction overriding a word. When the caused-motion construction makes *sneeze* in *she sneezed the napkin off the table* contribute causation-of-motion it does not lexically have, that **is** a shift in the word's sense *induced by the grammar*. Constructional coercion (grammar end) and contextual sense modulation (lexicon end) are the **same event** described from the two ends of the cline. The project has measured each end separately — the caused-motion construction's inference is genuinely construction-keyed ([`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md)); a word's sense relatedness is gradiently tracked (the lexical result) — but never the **join**.

The join is directly testable with the instrument the lexical probe already built: take a coercing construction and ask, with the DWUG-style relatedness rating, **how related is the verb's sense between its neutral frame and its coerced frame**, against non-coercing controls. That probe — [`design/coercion-as-sense-modulation-v1`](../../../experiments/designs/coercion-as-sense-modulation-v1.md) — **ran (2026-05-30)** → [`result/coercion-sense-modulation-v1`](../results/coercion-sense-modulation-v1.md): **the predicted direction holds**. All three models rate a coerced verb use as **less sense-related** to its bare use than a length-matched non-coercing elaboration (positive gap, every model/framing; cm > way; the three-way ordering control ≥ coerced ≥ a genuine-sense-shift `polysemy-anchor` holds in all cells) — so constructional coercion **registers, partially, as a lexical sense shift**: the two wedges empirically touch. **One bound keeps it honest:** the design cannot separate this from the coerced sentences' added object+path *argument structure* (the gap may be partly surface, not sense), so the bridge is established as an internal-contrast direction-of-effect, not a clean sense claim — a non-coercing transitive control was the v2. **That v2 ran (2026-05-31)** → [`result/coercion-sense-modulation-v2`](../results/coercion-sense-modulation-v2.md): with a structure-matched conventional-transitive control, the gap **partially de-confounds** — a small, **fine-scale-only, fragile** sense-specific residual survives (isolation gap cont +13.6/+6.1/+1.9, ≈0 on the coarse 4-point scale, carried by only 3–4 of 8 verbs) **alongside a real surface component**. So the bridge is genuine but **fainter than v1's raw gap implied**: v1's drop was a *mix* of sense and surface (mostly sense for claude, mostly surface for gemini). The two wedges still touch — more weakly than first measured. A second, unforced finding (v1, surviving into v2's ordering): the model strongest at pure lexical gradience (gemini) is the *least* coercion-sensitive, so the two competences come apart across the panel.

## The prospective third axis: multimodal / perceptual grounding

As of 2026-05-30 the project adds a **third** scope axis alongside the lexical and grammatical
ones: **multimodal / physical-AI meaning** (Tom's headline steer). The continuum thesis above is
about *grain* (specific word ↔ schematic construction), all on **text-only** form. The third axis
is orthogonal to grain: it varies the **modality of the form** — does adding perceptual input
(images; where tractable audio/video) change a model's meaning behavior beyond what the text
distribution already supplies? This is the same beat-the-distributional-shadow skeleton with a
*different* null: not "context similarity" (lexicon) or "n-gram/surface form" (grammar) but
**"the text already gave it away" (perceptual redundancy)**. The driving theories are the ones
this repo already catalogs that tie meaning to the world — Bender & Koller / Lyre grounding
([`concept/grounding`](../../base/concepts/grounding.md)), Harnad's symbol grounding
([`concept/symbol-grounding-problem`](../../base/concepts/symbol-grounding-problem.md)), Barsalou's
perceptual symbols ([`concept/embodied-cognition`](../../base/concepts/embodied-cognition.md)) —
positioned to give the `grounded.perceptual` tag its first empirical exercise — which it now has, as
**two bounded clear-homonym negatives plus one inconclusive image-native selection run** (below).

The axis is **designed to join this continuum, not sit beside it.** The first multimodal conjecture,
[`conjecture/multimodal-lexical-grounding-divergence`](../conjectures/multimodal-lexical-grounding-divergence.md),
reuses the **same DURel-style graded-relatedness instrument** the lexical wedge validated and toggles
**one factor (modality)** — exactly how coercion bridged the two text wedges by reusing one
instrument and toggling the coercing construction. So a multimodal result lands on the *lexical end*
of the cline (graded word-sense relatedness, now with vs without a picture) and, via prediction 4
(coercion under depiction), reaches toward the *grammatical end* too. The integration claim is
deliberately conditional: the third axis joins the continuum **only to the extent the evidence
supports it** — a perceptual-redundancy null (the image changes nothing) would say grounding adds no
sense signal these text models lack, which is a first-class negative, not a failure to integrate.

**As of 2026-06-24 the grounding axis stands at two bounded clear-homonym negatives plus one
inconclusive image-native selection run.** The first two are nulls, both for *clear homonyms*. The
cheapest first contact, prediction 1 — a $0 Lancaster-norms moderation of the existing lexical
result — **ran** → [`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md):
a word's perceptual groundedness does **not** predict how well a text-only model tracks its graded
senses (Δρ negative or null in every primary cell; the lone CI excluding zero runs the *wrong* way;
underpowered, so a bounded null, not a falsification). Then the first **image-input** probe
(predictions 2–3) **ran** → [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md):
showing the depicting picture does **not** improve the panel's separation of same- vs different-synset
pairs, because the **text-only panel already separates clear homonyms perfectly** (AUC = 1.000 in
every cell) — the predicted redundancy null in its strong form, with one small gpt-5.4-mini
continuous-scale positive that survives the surface-distraction control but cannot be read as
grounding. The honest bound runs through both: the test is **least sensitive exactly where it looks
cleanest** — clear homonyms maximize both visual distinctness and text separability, so text
saturates and the image has nothing to add. These are **bounded negatives for clear homonyms**, not a
verdict on grounding: the cell where an image could still matter — **fine polysemy / abstract senses
where text does not saturate** — is exactly the cell neither probe contains, and stays open. So
those first two outcomes are integrated as **two** first-class negatives for clear homonyms (a third,
inconclusive grounding outcome follows): on these models, for clear homonyms, perceptual input adds no
sense signal the text distribution does not already supply.

The third grounding outcome (session 100) is **inconclusive, not a clean negative**: the first **run**
of an image-native VWSD probe of the gating *shape* of the grounding-headroom conjecture
([`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md)) **neither confirms
nor falsifies** the gating prediction on VWSD. The intended saturated-vs-under-determined interaction
was **not reported**: the caption-text baseline **saturated** (per-model accuracy .86–.88; 40/50 items
text-separable by all three models), leaving only **7 under-determined items — below the
pre-registered stratification floor of 8** — so the frozen fallback suppressed the binned interaction.
What did read out: the **distraction control was clean** (word-ablated gold-selection pooled .093 ≈
chance, picks spread across all ten positions, so image-conditioned selection is word/sense-driven,
not surface-salience), and **real images gave no broad lift** over their captions (gpt was markedly
*worse* with images, .60 vs .86; claude/gemini ≈ flat), with image-rescue in text-failed cells only
4/16 = .25 — too thin to test. It is best read as a **bounded reappearance of the redundancy null**
([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)) in an
image-native *selection* task — but **caption-leakage-confounded** (the "text" channel was
gemini-authored captions that often name the referent) **and underpowered**. So it is **consistent
with the conjecture's general posture** (once candidates are described in words the task largely solves
from text, and the images add no broad lift) yet is **not a test of the gating interaction**, and
prediction-1-as-written stays open for a future graded-image resource. The corrected count is
therefore **two bounded clear-homonym negatives plus one inconclusive image-native selection run**, not
three clean negatives.

## What this page predicts and forbids

**Predicts.** If the continuum thesis holds for these models, the two wedges should not dissociate sharply: a model that tracks the meaning gradient at one grain should tend to at the other (the lexical and grammatical positives co-occurring in the same panel is weak confirmation), and coercion should show up *in the lexical instrument* as a sense shift (the bridge probe's bet). The per-model ordering may even transfer — a point to watch is whether the model that is strongest lexically (gemini, here) is also strong on the constructional inference probes.

> **Update (2026-05-30) — the per-model-ordering watch is now tested → [`result/cross-axis-lexical-constructional-ordering-v1`](../results/cross-axis-lexical-constructional-ordering-v1.md), and the prediction is *partially disconfirmed*.** A read-only re-analysis tabulating each model's lexical ρ against eleven own-design constructional results finds the lexical order (gemini > claude > gpt) transfers **only at the bottom** — gpt-5.4-mini is weakest lexically *and* most fragile constructionally (last in every discriminating result) — but **not at the top**: gemini's lexical supremacy does not make it uniquely strongest constructionally (it ties claude on the add-direction positives; claude beats it on *way*/CC-v3/distinction), and on the **same-instrument bridge the order inverts** (claude 31.4 > gpt 20.5 > gemini 8.3 coercion sense-shift, vs the lexical gemini > claude > gpt). So the grain-to-grain link holds for *failure* but not *strength*, and the most comparable cross-axis measure inverts. The wedges are unified as **targets** (one form–meaning cline) but the underlying model **competences are separable** — a concrete dissociation where this page had only an open guess. (Caveat: n=3 models — read the orderings, not a coefficient.)

**Forbids.** It forbids treating a lexical null and a grammatical null as unrelated: a context-similarity shadow (lexicon) and a frequency shadow (grammar) are the *same* deflationary hypothesis at two grains, and a finding that the gradient is "just distributional" on one end should lower the prior that it is genuine on the other. It also forbids over-reading the unification: the continuum is a claim about the *targets* (form–meaning pairings at different grains), **not** a claim that the model uses one mechanism for both — that is an open representational question this behavioral evidence cannot settle.

## Theoretical situating

The "beat the distributional shadow" test this page is built on sits inside a recognizable philosophical frame, mapped on [`theory/situating-llm-meaning`](situating-llm-meaning.md): the graded sense signal it vindicates is a **use / prototype** picture of word meaning ([`concept/truth-conditional-and-use-meaning`](../../base/concepts/truth-conditional-and-use-meaning.md), [`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md)) rather than a discrete truth-conditional inventory; the conceptual-role upgrade it implies inherits the **holism** objection ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)), which the cross-axis dissociation mildly strains; and the third (grounding) axis's two negatives are generalized into the project's own [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md) — perceptual input can act only in the residual the text distribution under-determines. Whether any of this amounts to "meaning" is the eliminativist↔deflationary↔descriptivist question, left to [`concept/deflationary-and-eliminativist-llm-meaning`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md).

## Status and revision hook

`status: draft`; `contingent-on: []`. It reorganizes existing results under one frame; the probes and re-analyses it proposed or pointed to have since run, and the triggers it once listed as open are now mostly discharged:

- **The bridge probe** ([`result/coercion-sense-modulation-v1`](../results/coercion-sense-modulation-v1.md)) confirmed its direction with a surface-confound bound, and its proposed **v2 with a non-coercing transitive control** then **ran** ([`result/coercion-sense-modulation-v2`](../results/coercion-sense-modulation-v2.md)): the gap **partially de-confounds** — a small, **fine-scale-only, fragile** sense-specific residual survives a structure-matched conventional-transitive control (isolation gap cont +13.6/+6.1/+1.9, ≈0 on the coarse scale, carried by 3–4 of 8 verbs) **alongside a real surface component**. So v1's drop was a *mix* (mostly sense for claude, mostly surface for gemini); the bridge holds but is fainter than v1's raw gap implied. (See the bridge section above.)
- **The lexical hard direction.** The **lexical v2** ([`result/lexical-polysemy-homonymy-v2`](../results/lexical-polysemy-homonymy-v2.md)) found the polysemy-vs-homonymy discreteness split **untestable at the DWUG anchor** (only 3 clean homonym lemmas) and pointed to a homonymy-enriched v3. That **v3 ran** ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)) on a homonymy-enriched WiC noun subset and returned a **powered null**: the panel separates WiC same/different equally well for homonyms and polysemes (AUC diff ≈ 0 in all six cells), and the lone positive (homonym different-senses floored more) **cannot be separated from plain graded distance** — it is lemma-concentrated, scale-quirk-amplified, and CI-fragile. So clause (b)'s distinctive **discrete-regime** bet is **not established** (now *powered*, not merely untestable), while the central bet (the graded signal, clauses a+c) still stands.
- **The cross-axis model-ordering** check ([`result/cross-axis-lexical-constructional-ordering-v1`](../results/cross-axis-lexical-constructional-ordering-v1.md)) settled the ordering watch (failure transfers, strength does not, the bridge inverts — see the Update box above).
- **The grounding axis** opened as two negatives for clear homonyms (prediction-1 moderation null + image-probe redundancy null) and, as of session 100, adds a **third, inconclusive** outcome: an image-native VWSD run of the gating shape ([`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md)) that **neither confirms nor falsifies** the gating prediction (caption-text saturated, stratification floor not met, no broad image lift) — a caption-confounded, underpowered reappearance of the redundancy null, not a clean third negative. See the third-axis section above.

- **The lexical bridging probe** (Prediction 4 of [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md)) — once listed here as an open trigger — has now **run** ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md), session 77, 2026-06-22) → **graded scale, ungraded commitment, a clean null 3/3**: models place bridging pairs at an intermediate *position* yet commit at clear-item confidence with ≈0 decline. This is a within-item discreteness, complementary to v3's between-stratum null. The position half is the bound-but-weak (Q3-shadowed) half; the ungraded-commitment half is robust.

- **The lexical pole gained a second axis** (session 147): a **relation-type gradient** drawn from two s145 OA sources (the behavioral [`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md), which `refines` this page, and the representational [`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md), which `supports` it) and read through the beat-the-shadow test in [`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md): antonymy = shadow-saturated end (smallest over-and-above residual), meronymy/hyponymy = larger residual. Its panel test is the **blocked** [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md) (`anchor: pending`, spend-bearing) — so this is prior-art plus a recorded bet, not a panel result. See the lexical-pole subsection above.

The remaining open trigger is a **relational pilot**. The net for the continuum thesis: it is right that the two wedges are **one target cline** (a positive that beats the distributional shadow on both ends), but wrong if read as "one competence" — the model orderings dissociate. The lexical *hard* direction (homonymy discreteness) has now been **tested on a homonymy-enriched anchor → not established as a separate discreteness regime**; and the discreteness/graded-distance confound is **intrinsic to a lemma-level WiC contrast** (a clean test would need pair-level senses holding human graded distance constant), so unlike the grammatical hard direction it remains hard to isolate even with a purpose-built anchor.
