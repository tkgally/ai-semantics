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
status: draft
contingent-on: []
created: 2026-05-30
updated: 2026-05-31
links:
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
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
- **Lexical end:** the panel's graded sense-relatedness rating tracks the human DURel median (Spearman 0.60–0.83, in/above the human inter-annotator range) and **survives partialling out the model's own topic-similarity** ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)). The shadow (context similarity) does not explain it either.

This is the first time the project can state its central finding as a **cline-spanning** one rather than a grammar-only one: *current decoders track a graded form–meaning signal that beats the distributional null at both the word grain and the construction grain* — with the same caveats on both (behavioral not representational; single runs; modest N; the hard *negative* directions — divergent-form generalization on grammar, and on lexis the **polysemy/homonymy discreteness split**, now tested on a homonymy-enriched WiC anchor and returning a **powered null** ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md): no separate discrete regime over plain graded distance), so the *graded* signal stands but the *discrete-regime* bet does not).

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
**two negatives** (below).

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

**As of 2026-05-31 the grounding axis stands at two negatives, both for *clear homonyms*.** The
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
where text does not saturate** — is exactly the cell neither probe contains, and stays open. So the
third axis is, so far, integrated as a pair of first-class negatives: on these models, for clear
homonyms, perceptual input adds no sense signal the text distribution does not already supply.

## What this page predicts and forbids

**Predicts.** If the continuum thesis holds for these models, the two wedges should not dissociate sharply: a model that tracks the meaning gradient at one grain should tend to at the other (the lexical and grammatical positives co-occurring in the same panel is weak confirmation), and coercion should show up *in the lexical instrument* as a sense shift (the bridge probe's bet). The per-model ordering may even transfer — a point to watch is whether the model that is strongest lexically (gemini, here) is also strong on the constructional inference probes.

> **Update (2026-05-30) — the per-model-ordering watch is now tested → [`result/cross-axis-lexical-constructional-ordering-v1`](../results/cross-axis-lexical-constructional-ordering-v1.md), and the prediction is *partially disconfirmed*.** A read-only re-analysis tabulating each model's lexical ρ against eleven own-design constructional results finds the lexical order (gemini > claude > gpt) transfers **only at the bottom** — gpt-5.4-mini is weakest lexically *and* most fragile constructionally (last in every discriminating result) — but **not at the top**: gemini's lexical supremacy does not make it uniquely strongest constructionally (it ties claude on the add-direction positives; claude beats it on *way*/CC-v3/distinction), and on the **same-instrument bridge the order inverts** (claude 31.4 > gpt 20.5 > gemini 8.3 coercion sense-shift, vs the lexical gemini > claude > gpt). So the grain-to-grain link holds for *failure* but not *strength*, and the most comparable cross-axis measure inverts. The wedges are unified as **targets** (one form–meaning cline) but the underlying model **competences are separable** — a concrete dissociation where this page had only an open guess. (Caveat: n=3 models — read the orderings, not a coefficient.)

**Forbids.** It forbids treating a lexical null and a grammatical null as unrelated: a context-similarity shadow (lexicon) and a frequency shadow (grammar) are the *same* deflationary hypothesis at two grains, and a finding that the gradient is "just distributional" on one end should lower the prior that it is genuine on the other. It also forbids over-reading the unification: the continuum is a claim about the *targets* (form–meaning pairings at different grains), **not** a claim that the model uses one mechanism for both — that is an open representational question this behavioral evidence cannot settle.

## Status and revision hook

`status: draft`; `contingent-on: []`. It reorganizes existing results under one frame; the probes and re-analyses it proposed or pointed to have since run, and the triggers it once listed as open are now mostly discharged:

- **The bridge probe** ([`result/coercion-sense-modulation-v1`](../results/coercion-sense-modulation-v1.md)) confirmed its direction with a surface-confound bound, and its proposed **v2 with a non-coercing transitive control** then **ran** ([`result/coercion-sense-modulation-v2`](../results/coercion-sense-modulation-v2.md)): the gap **partially de-confounds** — a small, **fine-scale-only, fragile** sense-specific residual survives a structure-matched conventional-transitive control (isolation gap cont +13.6/+6.1/+1.9, ≈0 on the coarse scale, carried by 3–4 of 8 verbs) **alongside a real surface component**. So v1's drop was a *mix* (mostly sense for claude, mostly surface for gemini); the bridge holds but is fainter than v1's raw gap implied. (See the bridge section above.)
- **The lexical hard direction.** The **lexical v2** ([`result/lexical-polysemy-homonymy-v2`](../results/lexical-polysemy-homonymy-v2.md)) found the polysemy-vs-homonymy discreteness split **untestable at the DWUG anchor** (only 3 clean homonym lemmas) and pointed to a homonymy-enriched v3. That **v3 ran** ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)) on a homonymy-enriched WiC noun subset and returned a **powered null**: the panel separates WiC same/different equally well for homonyms and polysemes (AUC diff ≈ 0 in all six cells), and the lone positive (homonym different-senses floored more) **cannot be separated from plain graded distance** — it is lemma-concentrated, scale-quirk-amplified, and CI-fragile. So clause (b)'s distinctive **discrete-regime** bet is **not established** (now *powered*, not merely untestable), while the central bet (the graded signal, clauses a+c) still stands.
- **The cross-axis model-ordering** check ([`result/cross-axis-lexical-constructional-ordering-v1`](../results/cross-axis-lexical-constructional-ordering-v1.md)) settled the ordering watch (failure transfers, strength does not, the bridge inverts — see the Update box above).
- **The grounding axis** opened as two negatives for clear homonyms (prediction-1 moderation null + image-probe redundancy null — see the third-axis section above).

The remaining open trigger is a **relational pilot**. The net for the continuum thesis: it is right that the two wedges are **one target cline** (a positive that beats the distributional shadow on both ends), but wrong if read as "one competence" — the model orderings dissociate. The lexical *hard* direction (homonymy discreteness) has now been **tested on a homonymy-enriched anchor → not established as a separate discreteness regime**; and the discreteness/graded-distance confound is **intrinsic to a lemma-level WiC contrast** (a clean test would need pair-level senses holding human graded distance constant), so unlike the grammatical hard direction it remains hard to isolate even with a purpose-built anchor.
