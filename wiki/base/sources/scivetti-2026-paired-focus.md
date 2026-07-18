---
type: source
id: scivetti-2026-paired-focus
title: "Language Models Learn Constructional Semantics, Not To Mention Syntax: Investigating LM Understanding of Paired-Focus Constructions"
authors:
  - Scivetti, Wesley
  - Wilcox, Ethan
  - Schneider, Nathan
  - Misra, Kanishka
  - Weissweiler, Leonie
year: 2026
venue: "Proceedings of CoNLL 2026, to appear; arXiv 2605.31586"
url: https://arxiv.org/abs/2605.31586
access: open-access
meaning-senses:
  - constructional
  - functional-vs-formal
  - distributional
status: received
created: 2026-07-18
updated: 2026-07-18
links:
  - rel: supports
    target: concept/constructional-meaning
  - rel: supports
    target: concept/compositionality
---

# Scivetti, Wilcox, Schneider, Misra & Weissweiler 2026 — Paired-Focus Constructions

## What it is

A five-author computational-linguistics paper (to appear, CoNLL 2026; arXiv 2605.31586, submitted
29 May 2026) that tests whether language models learn the **form** and the **meaning** of a family
of four rare **Paired-Focus constructions** in English — **Let-Alone**, **Much-Less**,
**Not-To-Mention**, and **Never-Mind** (constructions that "conjoin two phrases that are both in
focus", e.g. *He doesn't like shrimp, let alone squid*) — and, using open-checkpoint models, **when
in pretraining** each is acquired. The lead author (Wesley Scivetti, Georgetown) and the framing
are the direct successor to [`source/scivetti-2025-beyond-memorization`](scivetti-2025-beyond-memorization.md);
the last author (Leonie Weissweiler) is the author of the comparative-correlative CxG work the
project already leans on ([`source/weissweiler-2022-comparative-correlative`](weissweiler-2022-comparative-correlative.md),
[`source/weissweiler-2023-cxg-insight`](weissweiler-2023-cxg-insight.md)).

Two headline structural results: (1) **form and meaning dissociate and are learned at vastly
different amounts of input** — even very small models master Paired-Focus *syntax*, but Paired-Focus
*semantics* only emerges above ~400M parameters and, in the learning-dynamics experiment, "much
later in training relative to Paired-Focus form"; (2) **Paired-Focus semantics correlates with
world-knowledge acquisition** (the EWoK benchmark, especially its physical-relations domain) but
**not** with the syntactic BLiMP benchmark — from which the authors argue that the failure of
text-only, human-scale models to jointly acquire form and meaning "calls into question the ability
of human-scale pure text LMs to serve as model systems" of constructionist linguistic theories.

## ⚠ Configuration caveat — this is a SMALL-model, raw-probability study, NOT the project's panel

**Read before wiring.** The subjects are **36 comparatively small open-source models** (the paper's
learning-dynamics trio is Pythia-12b, Ettin-encoder-400m, Ettin-decoder-1b; the wider set spans
BabyLMs, OLMo, Pythia, Ettin — all far below frontier scale), evaluated by **raw output
probabilities / surprisal** (a ΔP contrast on minimal-pair follow-ups), **not** by prompting. This
is the **opposite end of the scale and a different instrument** from the project's frontier prompted
panel (claude / gemini / gpt in [`config/models.md`](../../../config/models.md)): there is **no
claude, gemini, or GPT-frontier subject**, and no prompted / forced-choice elicitation. So this is a
**companion / counterpoint source, NOT a human anchor, with NO transfer to the frontier panel** —
the same catalogue status as [`source/azin-2026-presupposition-conditionals`](azin-2026-presupposition-conditionals.md),
[`source/guo-2026-statistical-preemption`](guo-2026-statistical-preemption.md), and
[`source/mosolova-2025-wsi-unsolved`](mosolova-2025-wsi-unsolved.md). In particular, its **positive**
result (medium open models *do* grasp Let-Alone form and meaning) is on a distinct regime and
instrument and **must not** be cited as replicating or contradicting the project's own frontier
let-alone finding ([`result/scivetti-let-alone-working-surface-v1`](../../findings/results/scivetti-let-alone-working-surface-v1.md)) —
see "What it bears on in-repo" for the careful reading.

## Provenance

Title, full author list, venue ("Conference on Natural Language Learning (CoNLL) 2026"), submission
date (29 May 2026), and the **abstract** were fetched and verified firsthand against the arXiv
abstract page (https://arxiv.org/abs/2605.31586) on 2026-07-18; the abs page declares the license
**CC BY 4.0** (`creativecommons.org/licenses/by/4.0/`, verified in the page source). Body quotes
were extracted from the arXiv HTML rendering (https://arxiv.org/html/2605.31586) and each
load-bearing string below was confirmed character-for-character present in a local fetch of that
HTML. Locators are the paper's own section numbers (the CoNLL camera-ready is not yet in the ACL
Anthology). **MathML note:** per the standing arXiv-HTML caveat, numeric fragments inside math spans
survive in a LaTeX fallback, so the correlation and regression coefficients below **were**
recoverable and are quoted; the paper's main quantitative results (Figure 1, the training-dynamics
curves in Figures 2–4) live in **figures** and were **not** text-recoverable, so the accuracy
levels and learning curves are reported only qualitatively, as the prose states them.

## Abstract (verbatim)

> "Grasping the semantics of rare constructions (form-meaning pairings) has been shown to be a
> challenging problem that has currently only been solved by the largest LLMs. It remains an open
> question if open-source models have robust constructional understanding, and if so, what learning
> dynamics underlie the acquisition of this knowledge. Focusing on a set of rare Paired-Focus
> constructions in English (e.g. "let alone", "much less"), we construct a novel dataset to test
> their meanings using both scalar adjectival semantics and general world knowledge. Testing a wide
> range of models differing in parameter count, architecture, and pretraining dataset size, we find
> that several modestly sized models are sensitive to both the forms and the meanings of
> Paired-Focus constructions, though models trained on human-scale data fail at all meaning
> evaluations. Turning to training dynamics for a set of open-checkpoint models, we find that
> Paired-Focus understanding emerges later in training than Paired-Focus syntactic knowledge, and
> that learning of Paired-Focus semantics is correlated with gains in some domains of world
> knowledge. Overall, our empirical results support the conclusion that modestly sized open-source
> models can grasp the rare Paired-Focus constructions, and demonstrate a connection between
> knowledge of Paired-Focus constructions and other meaning domains."

## The construction and the semantic target (verbatim; §2.1)

> "we focus on four related Paired-Focus constructions: Let-Alone, Much-Less, Never-Mind, and
> Not-To-Mention."

> "Regarding Paired-Focus semantics, the constructions indicate a relationship between two conjoined
> and focused elements which are being compared. The comparison between the focused elements evokes
> a scalar relationship with the two elements representing "two points on a scale"
> (fillmoreRegularityIdiomaticityGrammatical1988). Generally, the second focused element has a
> higher value on the scale than the first focused element."

## The instrument (verbatim; §3.1) — a surprisal ΔP contrast against an "or" control

> "To test model sensitivity to Paired-Focus semantics, we measure the effect that the constructions
> have on model output probabilities on a follow-up sentence that would be entailed by the
> Paired-Focus construction."

> "To control for this fact, we compare example pairs with a Paired-Focus construction to examples
> without a construction with scalar semantics, specifically the simple conjunction "or"."

The metric ΔP is a surprisal difference between the minus-plausible and plus-plausible follow-ups,
and accuracy is the fraction of items for which ΔP is larger under the construction than under the
"or" control (§3.1, Eqs. 1–2). Two confounds are explicitly balanced out: **lexical bias** (e.g.
"easier" more frequent than "harder") and **ordering** of the two focused elements. The dataset is
built from scalar adjectives and scales taken from the Wilkinson & Tim 2016 gold-scale set (198
templates across 4 scales; ~3.5k sentence pairs per construction).

## Experiment 1 — model size and training data (verbatim; §4.2)

> "Below a parameter threshold of roughly 400M, model performance is generally at or below chance
> regardless of the amount of training data (with the exception of Ettin-encoder-150M). Beyond this
> parameter threshold, there is a generally positive relationship between training data and accuracy
> as well as parameter count and accuracy."

Figure 1's caption reports the rank correlation of parameters with average accuracy: **"Spearman's
ρ = 0.67"**. The linear mixed-effects analysis:

> "we find that only parameter count has a significant main effect (β = 6.055, p = .011)."

> "we find that both parameter count (β = 6.607, p = 003) and pretraining data (β = 2.651, p = .034)
> are significant, though the effect of parameter count remains larger. While we note that MLM and
> autoregressive scoring is not directly comparable, we find no significant effect of pretraining
> objective."

*(The "p = 003" for parameter count is the paper's own text — evidently a typo for p = .003; quoted
faithfully.)* The **form / meaning dissociation** in the small models:

> "even very small models have strong performance on our syntactic evaluation suite … The
> dissociation between tasks for small models underscores the need to evaluate both form and
> semantics when assessing LMs' overall knowledge of rare constructions."

> "a few models as small as 400M parameters succeed at learning (with 90%+ accuracy) both the form
> and semantics of the constructions, and most of the larger models are above chance. … Knowledge
> of the form of Paired-Focus constructions is present even in the smallest models we test."

The abstract-level summary of the human-scale (BabyLM) result: **"models trained on human-scale data
fail at all meaning evaluations."**

## Experiment 2 — learning dynamics (verbatim; §5.3–§5.5)

> "We find strong evidence that Paired-Focus form is learned prior to Paired-Focus semantics.
> Syntactic accuracy reaches a peak much earlier in training than Paired-Focus accuracy."

> "For both BLiMP and COMPS, accuracy plateaus relatively early in training, substantially before
> the Paired-Focus accuracy rises above chance. For EWoK, performance gains are more gradual, similar
> to gradual gains on Paired-Focus semantics."

> "We find negligible correlation between Paired-Focus form and semantics, and between Paired-Focus
> semantics and BLiMP. … When subdividing EWoK into its different world knowledge domains, we find a
> moderate correlation between Paired-Focus semantics and the physical relations domain (ρ = .48)."

> "these results provide strong evidence that Paired-Focus form and meaning are learned with vastly
> different amounts of training input."

The largest model (Pythia-12b) is robust to implausible follow-ups, whereas the smaller Ettin models
"seem more reliant on world knowledge cues for their interpretations", especially early in training.

## The paper's overall reading (verbatim; §1, §6)

> "the failure of all "human-scale" models on our semantic evaluation points calls into question the
> ability of human-scale pure text LMs to serve as model systems of linguistic theories that posit
> joint acquisition of form and meaning."

> "While our results do not provide definitive evidence that form and meaning are necessarily learned
> separately by LMs, they underscore that modeling joint learning of constructional form and meaning
> … has not been clearly demonstrated by LMs thus far."

## What this bears on in-repo

- **[`concept/constructional-meaning`](../concepts/constructional-meaning.md) — `supports`.** The
  cleanest external data point yet on the project's organizing cut between a construction's **form**
  and its **meaning**: here the two are shown to dissociate not only across models (small models get
  form, miss meaning) but across *training time* (form learned first, meaning later), on a
  probability-based instrument entirely independent of the project's prompted panel. That the
  form/meaning cut shows up as a learning-dynamics separation is convergent motivation for treating
  form-acceptability as the *floor* of constructional evidence rather than its proof.
- **[`theory/constructional-meaning-in-llms-v2`](../../findings/theory/constructional-meaning-in-llms-v2.md) —
  external company for the wedge, NOT a revision trigger.** The theory's central instrument is the
  Mahowald formal-vs-functional wedge and an evidence ladder whose lowest rung (Tier 0,
  form-acceptability) is explicitly "a necessary but not sufficient test" for meaning. This paper
  supplies **independent, differently-instrumented corroboration** of exactly that separation: form
  is cheap (small models, early training), meaning is expensive (>400M params, late training), and
  the two are uncorrelated in the learning dynamics. It does **not fire any of the theory's named
  revision triggers** — those are the partial-climb resolving, a hard-direction positive, a beater
  failing, or a second-date AANN replication, all of which concern the *project's own panel and
  numbers*. A small-model surprisal study touches none of them, so the theory is **not revised**;
  this is recorded as external convergence only (the [`source/azin-2026-presupposition-conditionals`](azin-2026-presupposition-conditionals.md)
  precedent).
- **[`result/scivetti-let-alone-working-surface-v1`](../../findings/results/scivetti-let-alone-working-surface-v1.md)
  — a careful thematic convergence on "let-alone failures are evaluation artifacts", NOT a
  replication.** The project's frontier let-alone finding is that the near-chance let-alone *negative*
  was largely an **output-channel artifact** — 2/3 models reached the human baseline once given a
  working surface. This paper attacks the same broad puzzle (why do models look bad on let-alone
  semantics?) from the opposite scale and instrument, and reaches a **compatible** diagnosis: it
  attributes prior small-model let-alone negatives to **evaluation design** — the earlier dataset
  ([`resource/scivetti-2025-cxnli-dataset`](../resources/scivetti-2025-cxnli-dataset.md)'s
  `scivetti-etal-2025-unpacking` source, whose "arbitrary" contrasts the project's own let-alone
  probes inherited) "relies on arbitrary contrasts which do not clearly implicate scalar semantics",
  and shows medium models succeed once the scalar relationship is made coherent. So **both lines
  point the same way — apparent let-alone semantic failures are substantially artifacts of how the
  test is posed** (channel format for the frontier/prompted panel; arbitrary-scale stimuli for the
  small/surprisal models). This is a **resonance across two different fixes to two different
  instruments**, recorded here; it is **not** an item- or model-matched replication and must not be
  cited as one.
- **[`concept/compositionality`](../concepts/compositionality.md) — `supports`.** The finding that
  Paired-Focus *semantic* accuracy correlates with world-knowledge (EWoK physical relations, ρ = .48)
  but not with syntactic BLiMP is a data point for the recurring theme that constructional meaning
  is not reducible to form-tracking — it recruits a separate, later-acquired, world-knowledge-linked
  competence.
- **BLiMP as a shared comparator (no wiring, noted).** The project ran a BLiMP forced-choice sweep
  ([`result/blimp-forced-choice-sweep-v1`](../../findings/results/blimp-forced-choice-sweep-v1.md));
  this paper uses BLiMP as a *learning-dynamics* comparison point and finds it plateaus early — a
  different use of the same benchmark, recorded for context, not a cross-citable result.

## What it can ground

- A citation that, on a **new probability-based benchmark of four rare English Paired-Focus
  constructions** (Let-Alone, Much-Less, Not-To-Mention, Never-Mind), across **36 open-source models**
  spanning parameter count, data scale, and architecture, (a) **form/syntax is learned by even the
  smallest models while meaning/semantics only emerges above ~400M parameters** (Spearman ρ = 0.67
  between parameters and accuracy; parameter count the only significant LME main effect, β = 6.055,
  p = .011); (b) **models trained on human-scale data (BabyLMs) fail all meaning evaluations**; and
  (c) in learning dynamics, **form is acquired before meaning**, meaning correlates with world
  knowledge (EWoK physical relations, ρ = .48) but not with BLiMP — verbatim as above, on the stated
  (non-project) small-model set and surprisal instrument.
- A citation for the reading that **text-only LMs have not been shown to jointly acquire
  constructional form and meaning**, and that human-scale pure-text models are poor "model systems"
  for constructionist theories — an independent, learning-dynamics-based statement of the wedge the
  project runs behaviorally on frontier models.
- A **method precedent** for a surprisal-based, "or"-controlled ΔP contrast that isolates a
  construction's scalar-semantic contribution from world-knowledge plausibility, with lexical-bias
  and ordering confounds balanced — a probability-native analogue of the project's shadow-controlled
  behavioral designs.

## What it cannot ground

- **Any claim about the project's frontier panel.** No claude / gemini / GPT-frontier subject, no
  prompting; the subjects are small open-source models scored by raw probability. No transfer to the
  project's panel is established, in either direction.
- **A replication or refutation of the project's frontier let-alone result.** Different scale,
  different instrument, different regime — see the careful thematic reading above. The convergence is
  at the level of "evaluation design matters", not matched items or models.
- **A human anchor.** The Meaning_Alone dataset (the paper's release, at
  `github.com/WesScivetti/Meaning_Alone`, **Apache License 2.0** — verified firsthand by raw-file
  fetch on 2026-07-18, HTTP 200 on both `main` and `master`) contains **no human ratings**: its
  ground truth is a theory-derived constructional entailment (which follow-up the construction
  favors), and the "accuracy" scored is model-probability agreement with that key, not agreement with
  human judgments. So — unlike the human-rated proviso-bench recorded on the A3a scout — it is **not**
  a candidate human-comparison anchor, notwithstanding its verified permissive license. Cataloguing
  the license accurately ≠ adoption; it grounds no human-comparison claim.
- **A causal or mechanistic claim.** The learning-dynamics results are **first-difference
  correlations** across checkpoints (the authors' Limitations are explicit: "our evidence in this
  paper is not causal"); the form/meaning "dissociation" is a behavioral-probability finding, not a
  demonstration of separate internal representations.

## Known limits

- **To appear, CoNLL 2026** (arXiv preprint at fetch time). Abstract + CC BY 4.0 license verified
  firsthand against the arXiv abs page; body quotes confirmed present in the arXiv HTML full text.
  Locators are §-numbers (no camera-ready pagination yet). The main quantitative results are
  **figure-only** (Figures 1–4) and were not text-recoverable, so accuracies and learning curves are
  reported qualitatively; only the recoverable regression/correlation coefficients are quoted.
- **English only, small models only.** Four English Paired-Focus constructions; the authors' own
  Limitations flag the small number of scales, the English-only scope, and the lack of causal
  evidence.
- **Instrument gap to this project.** Surprisal / probability scoring on small open models is a
  categorically different measurement from the project's prompted behavioral panel — the reason this
  is filed as a companion source and not an anchor or a comparator with transfer.

## Status in wanted.md

Firsthand-verified to exist at s249 (arXiv 2605.31586, CC BY 4.0; authors/title matching the s240
scout). Ingested 2026-07-18 (session 251) as a **companion / counterpoint source** on constructional
form-vs-meaning learning; the entry in [`wanted.md`](../wanted.md) is updated to RECEIVED. The
remaining s240-scout candidate (Rhee 2026, referential profiles — single-author, arXiv
nonexclusive-distribution license, no empirical/anchor content) stays UNVERIFIED-and-unopened, to be
ingested only on demand.
</content>
</invoke>
