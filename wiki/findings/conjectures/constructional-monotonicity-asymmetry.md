---
type: conjecture
id: constructional-monotonicity-asymmetry
title: LLM constructional inference is additive-easy but defeasance-hard (a monotonicity asymmetry)
meaning-senses:
  - constructional
  - inferential
status: proposed
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/coercion-implicit-cue-v2b
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
---

# Conjecture: LLM constructional inference is additive-easy but defeasance-hard (a monotonicity asymmetry)

## Statement

This is the **project's own, original** theoretical proposal — a forward bet generalizing a pattern that recurs across the argument-structure results, not an established finding. The descriptive observation it builds on is already recorded in [`concept/coercion`](../../base/concepts/coercion.md) and on the theory page ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), "the tentative generalization the ladder should now carry"); this page names it, frames it as a **monotonicity** asymmetry, and states sharp confirmation/falsification criteria so the empirical loop can later pick it up. The two pages are kept complementary: the theory page states the asymmetry descriptively in the course of placing each result on its ladder; this page is the typed conjecture that *abstracts over* those results and proposes a mechanism and a generalization test. It does not duplicate the ladder; it points at it.

The proposal, in one sentence: **current decoder LLMs treat a construction's inferences as readily *additive* — they license a construction-contributed entailment layered onto a non-licensing verb — but resist *retraction* — they suppress a lexically-default entailment far less reliably.** Cast in the vocabulary of inference: the models look better at *monotone accumulation* of entailments (add a new one) than at *defeasance* (cancel a default one). Adding is the easy direction; cancelling is the hard direction.

The connection to non-monotonic / defeasible reasoning is offered here as a **characterization, not a claimed result**: cancelling a default entailment is, formally, a defeasibility operation (the verb's lexical default is a defeasible inference the construction is meant to override), whereas adding a construction-contributed entailment is monotone (the construction's content is layered on without retracting anything). Under that framing the recurring asymmetry reads as: *these models are stronger at monotone accumulation than at the defeasance that cancellation requires.* The defeasible-reasoning literature is named as a framing only — no in-repo source grounds it, so the formal claim is held at the level of analogy (see *Provenance and what is not claimed*).

## The evidence this abstracts over

The asymmetry is visible across five own-design argument-structure results. Each is cited with its verified numbers (a direction-of-effect signal in every case — single panel/date/run, small N).

**The ADD direction is easy — at or near ceiling.**

- Caused-motion: the panel affirms the construction's causation-of-motion entailment onto non-motion verbs at **90–100%**, with a **70–100 pp** gap over controls, in **3/3 models**, both instruments, robust to atypical verbs ([`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md)).
- The *way*-construction: the path-traversal (self-motion) entailment onto non-motion verbs holds at **77.8–100%**, gap **77.7–100 pp** over the location control, **3/3 models**, both instruments ([`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md)).

**The CANCEL direction is harder — off-ceiling and instrument-fragile.**

- The conative cancels the completed-contact entailment the transitive carries (*kicked at the ball* vs *kicked the ball*). The forced-choice gap is **42–88 pp** across all 3 models, but **gpt-5.4-mini fails the cancellation entirely under NLI** (calls all conative items "entailment") while partly recovering under forced-choice ([`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md)).

**The asymmetry is de-confounded from ceiling by a matched probe.** This is the load-bearing piece: "license-easier-than-suppress" is about *direction*, not about the add items merely being easier. [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md) put the cancel direction into the *same* conflicting-cue paradigm the add-direction v2 used. At matched task structure the transitive lexical default is at ceiling (**91.7–100%**), but conative **suppression-with-no-cue** is off-ceiling and model/instrument-dependent — NLI **[58.3, 0.0, 66.7] pp**, forced-choice **[66.7, 33.3, 83.3] pp** — where the add-direction's matched licensing-no-cue was ~ceiling. So the asymmetry survives matching for difficulty: it is a property of the *direction* (add vs cancel), not an artifact of where on the scale the items happened to sit.

**Both directions are bounded — this is not "deep cancellation competence" either.** The add direction's apparent "computes-and-withholds" ability is itself shallow: while an *explicit* in-premise outcome denial floors the added affirmation (argument-structure-coercion-v2, cited on the theory page), [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) shows the panel still affirms a **physically impossible** caused-motion coercion at **near-ceiling (implicit-wk 90–100%)** when immovability is only *implied* by an in-premise descriptor, flooring (**0%**) only under an explicit outcome denial. So the add-direction's withholding is **explicit-outcome parsing, not world-model integration**. The conjecture is therefore *not* that cancellation is a deep competence the models lack; it is the narrower, more honest claim that *across matched probes the add direction is more uniformly executed than the cancel direction*, while both remain bounded.

## Mechanism (LABELED speculation)

The following is **speculation**, offered as a candidate explanation, not as a tested claim. It is deflationary-compatible — it does not require attributing reasoning to the model beyond next-token prediction over distributional structure.

Adding a construction-licensed inference is **distributionally cheap**: the construction's own co-occurrence statistics support the added entailment (the caused-motion frame co-occurs with caused-motion outcomes; the *way*-frame co-occurs with traversal), so a next-token predictor can affirm the added inference from the construction's distribution alone. Suppressing a lexical default, by contrast, requires representing a **cancellation against a strong lexical prior**: the verb (*kick*, *sip*) carries a robust completed-contact expectation in its own distribution, and the conative frame must override that prior rather than reinforce it. Holding down a strong prior is plausibly harder for a system whose objective is to predict the high-probability continuation. On this story the asymmetry is a signature of *distributional* meaning ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)) — accumulation aligns with the predictive objective; retraction works against it — rather than evidence of a constructional-meaning competence that is present in one direction and absent in the other. (The mechanism is compatible with the deflationary reading the theory page brackets; it is not an argument *for* deflationism, only consistent with it.)

This mechanism is itself a hypothesis the falsification criteria below can bear on: if the asymmetry reversed for some construction class, or vanished under matched difficulty, the distributional-prior story would be wrong or incomplete.

## What would confirm / falsify

Sharp criteria, so a later experiment can adjudicate. The decisive design feature in every case is **matched difficulty / ceiling control** — the conative-cancel-v2 probe is the template: compare add vs cancel at the *same* task structure, never add-at-ceiling vs cancel-off-ceiling.

**Confirms** (jointly):

1. The asymmetry **generalizes to new add-vs-cancel construction pairs** beyond caused-motion / way / conative — for example, other Levin alternations, or resultatives that *add* an entailment versus aspectual/conative-type coercions that *cancel* a default — tested at **matched difficulty and ceiling** (the add and cancel arms placed in a common paradigm, as conative-cancel-v2 did); AND
2. The cancel direction is reliably **more instrument-fragile** (larger NLI-vs-forced-choice disagreement) than the add direction on the same items — the pattern already seen for the conative ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md); [`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md)).

**Falsifies** (either):

- A matched, ceiling-controlled battery shows **symmetric** add/cancel performance — once difficulty is equated, the add and cancel arms are statistically indistinguishable; OR
- The asymmetry **reverses** for some construction class — a construction whose *cancel* direction is easy and whose *add* direction is hard.

A null on the generalization test (the asymmetry fails to extend beyond the three constructions seen so far) would retire the conjecture as an artifact of those particular items, not establish a competing claim.

## Candidate human anchor

A conjecture page needs no resource anchor (only `claim`/`result` pages do); naming a candidate is the project convention. The candidate human anchor for a matched-difficulty test is the **Scivetti CxNLI dataset** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)), which carries human-annotated NLI triples for both add-type constructions (Caused-Motion, Way-Manner) and the cancel-type Conative, with an aggregate native-speaker baseline (≈0.90 on Exp 1). It can anchor an answer-key comparison — model NLI labels against the per-item gold labels on the *same* add vs cancel constructions — but it delivers a single adjudicated gold label per item, **not** a per-item human-rating gradient (confirmed by inspection; see the resource page's *Known limits*).

Important scope note: the off-ceiling internal arms that establish the de-confounded asymmetry have so far been **internal-contrast-only** — the conative-cancel-v2 cue arm has no in-repo human norm, and that result carries `anchor: internal-contrast-only` by ratified decision ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). So a future *result* testing this conjecture would need either (a) to confine its human-comparison claim to the Scivetti answer-key arms, or (b) to declare its off-ceiling arms internal-contrast-only, exactly as the existing cancel-direction result does. The conjecture does not assume a human gradient the anchor cannot supply.

## Provenance and what is not claimed

- Every number above is quoted from an in-repo result page and matches it verbatim; none is invented.
- The framing in terms of **non-monotonic / defeasible reasoning** is a *characterization*, not a grounded result: no in-repo source treats the LLM-defeasance connection, so the formal mapping (cancellation = defeasibility operation; add = monotone) is held as analogy. If the project later leans on this formally, a defeasible-reasoning / non-monotonic-logic reference should be fetched first (flagged for `wanted.md`).
- The asymmetry is a **direction-of-effect** observation across five small-N, single-run, three-model probes. The conjecture is a forward bet that it *generalizes*; it is explicitly **not** presented as established. The de-confounding from ceiling ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)) is the strongest leg, but it too is small-N and internal-contrast-only.
- The conjecture does **not** claim cancellation is a deep competence the models lack, nor that addition reflects genuine constructional-meaning computation: [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) bounds the add direction's depth (explicit-outcome parsing, not world-model integration). Both directions are bounded; the claim is only about their *relative* reliability.
