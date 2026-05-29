---
type: claim
id: constructional-divergent-form-generalization-gap
title: LLMs track constructional form–meaning pairings up to a point but show a large generalization gap on syntactically identical, semantically divergent forms
meaning-senses:
  - constructional
  - functional-vs-formal
  - human-comparison
status: proposed
contingent-on: []
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: supports
    target: source/scivetti-2025-beyond-memorization
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: supports
    target: claim/formal-competence-aann-ceiling
---

# Claim: LLMs track constructional form–meaning pairings up to a point but show a large generalization gap on syntactically identical, semantically divergent forms

## Statement

Current state-of-the-art LLMs track phrasal-constructional form–meaning pairings **up to a point**, but exhibit a large generalization gap — a drop of **over 40%** (reported for GPT-o1) — when the *same* syntactic form carries a *divergent* constructional meaning, measured against a native-speaker baseline (≈0.90 on the base inference task, ≈0.83 on the divergent-form task). This is evidence that the construction-level competence current LLMs display is, in those models, partly **form-bound** rather than fully meaning-general: it falls short of the human ability to deploy the appropriate constructional semantics for syntactically identical but semantically divergent instances.

The claim is about the *aggregate, cross-construction* published result (the >40% headline drop) and the *aggregate* native-speaker baseline, not about any single construction. Per-construction breakdowns (caused-motion, conative, way-manner) are a separate, finer claim gated by the three open anchor decisions ([`decisions/resolved/caused-motion-anchor`](../../decisions/resolved/caused-motion-anchor.md), [`decisions/resolved/conative-anchor`](../../decisions/resolved/conative-anchor.md), [`decisions/resolved/way-construction-anchor`](../../decisions/resolved/way-construction-anchor.md)); this claim deliberately does not rest on them and is therefore `contingent-on: []`.

## Grounds

### The headline >40% drop (Scivetti et al. 2025, abstract)

The supporting source is [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md). The published ACL Anthology abstract states the design and the headline result verbatim:

> "Our evaluation dataset uses CxG to evaluate two central questions: first, if models can \"understand\" the semantics of sentences for instances that are likely to appear in pretraining data less often, but are intuitive and easy for people to understand. Second, if LLMs can deploy the appropriate constructional semantics given constructions that are syntactically identical but with divergent meanings. Our results demonstrate that state-of-the-art models, including GPT-o1, exhibit a performance drop of over 40% on our second task, revealing a failure to generalize over syntactically identical forms to arrive at distinct constructional meanings in the way humans do." (ACL Anthology 2025.ijcnlp-long.65, abstract; arXiv 2501.04661 v2 HTML)

The "second task" is precisely the syntactically-identical / semantically-divergent condition (Experiment 2, "CxNLI-Distinction"), which the dataset resource documents as adding surface-identical, meaning-divergent variants:

> "Thus, for the 5 argument structure Cxns of our 8 Cxns, we add test instances which share a surface syntax with our Cxns, but convey a different meaning." (arXiv 2501.04661 v2 HTML, §5.1)

### "Up to a point" — the paper's own bounded framing (§9)

The paper does **not** conclude that LLMs lack constructional semantics. Its §9 conclusion frames the result as a *breaking point*, not an absence:

> "Thus, our targeted series of experiments demonstrated that LLMs do process constructional semantics up to a point, yet our challenge datasets revealed the breaking point of understanding—where speakers are able to generalize the appropriate semantics to constructional slots filled by pragmatically atypical lexical items, but LLMs are much less proficient at this generalization." (arXiv 2501.04661 v1 HTML, §9 Conclusions and Future Work)

This is the bound the claim is careful to preserve: the gap is a shortfall in *generalization* over a form to its divergent meaning, against a backdrop of partial success — not a wholesale failure of constructional processing.

### The human baseline the drop is measured against (resource)

The human bearing of the claim is the native-speaker accuracy baseline documented on [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md). Experiment 1 (base CxNLI task):

> "Thus, if we take the original author's assigned relation to be the gold standard, then native speaker accuracy on the NLI task is 90%." (arXiv 2501.04661 v2 HTML, §4.1)

Experiment 2 (the divergent-form task, CxNLI-Distinction):

> "achieving an IAA of 83% with the original judgments." (arXiv 2501.04661 v2 HTML, §5.1)

The ≈0.90 / ≈0.83 figures are the human reference against which the model drop is read as a *gap* rather than a raw difficulty: humans deploy the divergent-form constructional semantics at near-the-base-task rate, whereas the leading model drops by over 40%. (Caveat preserved from the resource page: the verified Exp-2 sentence is phrased as an IAA "with the original judgments"; the source page and task framing gloss this as the Exp-2 human baseline. The 0.83 figure is verified; whether it is best read as IAA or native-speaker accuracy is flagged for re-check against Table 1.)

## Where it sits on the evidence ladder

On the ladder in [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), this claim sits at the **Tier 3 → Tier 4 boundary**. The task is behavioral NLI — *inference-licensing* in the theory's Tier 4 sense (does the model treat the construction as licensing its characteristic inferences, where the inference is contributed by the construction and not by a lexical part?). The divergent-form manipulation makes it a *generalization* test in the theory's Tier 3 sense: the same surface form must be mapped to a distinct constructional meaning, which is exactly the productivity/abstraction criterion (the schema, not the stored instance) that Tier 3 isolates and that Tier 4 inference-licensing presupposes.

The result is therefore evidence at the top of the text-internal ladder: it is the kind of finding the theory predicts would distinguish a model that "has the schema" from one that has stored instances. The >40% drop is a *negative* result at that boundary for current models — consistent with the theory's claim that the upper rungs are "hard to fake with distributional structure alone," and that current evidence in hand sits below them. It does not bear on the relational second ladder.

## What it does NOT claim

- **It does not claim LLMs lack constructional meaning entirely.** The paper's own framing is that LLMs "do process constructional semantics up to a point." The claim is a bounded *gap*, not an absence; over-reading it to "LLMs fail at constructional meaning" is a misstatement the source explicitly forecloses.
- **It is not a per-construction claim.** The figure is the aggregate cross-construction drop and the aggregate human baseline. Per-construction claims about caused-motion, conative, or way-manner are finer claims gated by the open anchor decisions and the small per-construction N; they are out of scope here.
- **It is not a representational / model-internal claim.** The evidence is behavioral NLI accuracy only. It says nothing about internal representations and cannot ground a `model-internal` claim about *how* the gap arises.
- **It is not a grounding claim in Bender & Koller's sense.** "Form-bound" here means *constructional-form-bound within a text-internal inference task* (the same form not generalizing to its divergent constructional meaning), not ungrounded-relative-to-communicative-intent. The grounded/ungrounded axis is orthogonal and untouched.

## Anchor

The human anchor is [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md): the native-speaker accuracy baseline (≈0.90 Experiment 1, ≈0.83 Experiment 2) over human-annotated NLI triples on the same constructional items the models are scored on. The model drop is defined relative to this human reference, so the human bearing of the claim is direct and on the same items. Per the resource page, the bearing verified this run is the **aggregate** accuracy/agreement figure, not per-item graded human ratings; the claim is scoped to match.

## Limits

- **Aggregate result.** The >40% drop and the ≈0.90 / ≈0.83 baselines are aggregate across constructions; the claim cannot be sharpened to any single construction without the per-construction counts (the anchor decisions for caused-motion / conative / way / comparative-correlative are now ratified, 2026-05-29, but the per-construction NLI items must still be enumerated from the dataset).
- **Small N per construction.** ≈435 triples / 8 constructions (Exp 1) and ≈99 triples / 5 constructions (Exp 2) — on the order of tens of items per construction — so any narrowing carries wide uncertainty.
- **Single gold label, not a human gradient.** The release repository was inspected 2026-05-29 (de-anonymized): it provides a single adjudicated gold answer per item plus the aggregate ≈0.90 / ≈0.83 baseline — not a per-item multi-rater distribution. The aggregate scoping of this claim is unaffected.
- **Single paper, behavioral.** The claim rests on one paper's behavioral NLI accuracies; it is not corroborated by an independent dataset and says nothing about model internals.
- **Exp-2 figure provenance caveat.** The 0.83 number is verified as printed but phrased as an IAA "with the original judgments"; its reading as a native-speaker-accuracy baseline is the source/resource gloss, flagged for re-check.

## Status

`status: proposed`. The empirical figures are published and verified verbatim; what is `proposed` (rather than `supported`) is this project's framing of the drop as evidence that current LLMs' constructional competence is partly form-bound. `contingent-on: []` — the claim uses only the aggregate published result and aggregate baseline, so it is not contingent on the caused-motion / conative / way-manner anchor decisions, which gate only the finer per-construction claims.
