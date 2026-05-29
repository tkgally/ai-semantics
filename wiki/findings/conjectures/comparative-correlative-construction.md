---
type: conjecture
id: comparative-correlative-construction
title: Current LLMs use the comparative correlative's proportional meaning, narrowing but not closing the form-vs-meaning dissociation found for encoder PLMs
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: proposed
contingent-on:
  - comparative-correlative-anchor
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/formal-vs-functional-competence
  - rel: depends-on
    target: source/weissweiler-2022-comparative-correlative
  - rel: depends-on
    target: open-question/constructional-divergence-probe
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
---

# Conjecture: current LLMs deploy the comparative correlative's proportional meaning

## Statement

The English **comparative correlative** (CC) — the two-clause `the X-er …, the Y-er …` template, *the more you practice, the better you get* — is a Construction Grammar paradigm case: its form is distinctive while its meaning is **non-compositional** and supplied by the construction itself, namely a **proportional / covariational dependency** between two scales (as the first scale increases, the second changes in a fixed direction). No lexical item in the clause carries that "as X, so Y" semantics; the construction does.

The conjecture: current instruction-tuned **decoder** LLMs (the Scivetti et al. 2025 panel class — GPT-4o, GPT-o1, Llama-3) **use** the CC's proportional-covariation meaning — they draw the inference that a change along the first scale entails a corresponding change along the second — at a rate that separates CC instances from minimally different non-CC controls, **narrowing** the form-recognised-but-meaning-not-used dissociation that [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) documented for encoder PLMs (BERT/RoBERTa/DeBERTa) — *but does not fully close it*, falling short of the human baseline.

The sharp empirical question this conjecture stakes out: Weissweiler et al. 2022 found encoder PLMs **recognise the structure of the CC but fail to use its meaning** (above-chance syntactic probe; no model above chance on the semantic task). Does that dissociation persist, narrow, or close in current decoder LLMs? The conjecture's directional bet — narrows-but-not-closes — is consistent with the [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md): newer models process constructional semantics "up to a point" but still lag humans on generalization.

## Why this is interesting

- It is the project's clearest **single-construction longitudinal** test case: it has a precedent pair on the *same* construction across model generations — the single-construction encoder-PLM probe ([`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md), 2022) and the CC subset of the multi-construction decoder-LLM benchmark ([`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md), 2025, whose 8 constructions include the CC). (The Scivetti benchmark also covers caused-motion, conative, and way-manner, but for those the project has no separate single-construction encoder precedent in-repo.)
- It lands squarely on the `functional-vs-formal` wedge ([`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)): the CC is the cleanest case where form-recognition and meaning-use were shown to **dissociate**, so it is the natural construction on which to ask whether the gap is a transient artifact of older models or a durable property.
- Confirmation requires the `inferential` reading ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)): showing the model treats the CC as *licensing the covariation inference*, not merely recognising the template — exactly the recognise-vs-use distinction Weissweiler 2022 operationalised.

## Predictions

1. **Covariation inference.** Given an inference probe over a CC sentence ("*The more the committee delayed, the angrier the investors grew.* — If the committee delayed more, what happened to the investors' anger? / Does increased delay go with increased anger? Y/N"), CC items yield a high correct-covariation rate.
2. **Minimal-pair controls.** Controls that reuse the same scalar lexical material in a non-CC syntax (two independent clauses; a single comparative) yield a substantially lower covariation-inference rate — isolating the construction, not the words, as the source of the inference.
3. **Direction sensitivity (the discriminating prediction).** The CC can be positive (*the more …, the more …*) or inverse (*the more …, the less …*). A model **using** the meaning tracks the direction of covariation, not just the template: inverse-CC items flip the predicted answer. A model only recognising the form would not reliably flip.
4. **Generalization to atypical scale pairs.** The covariation inference holds for low-frequency / pragmatically atypical scale pairings unlikely to be memorised as CC strings (Scivetti's atypical-filler lever) — distinguishing genuine constructional use from an n-gram effect (ties to [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md)).
5. **Generational contrast + panel divergence.** Decoder LLMs outperform the encoder-PLM chance-level semantic baseline of Weissweiler 2022 (the gap narrows), but remain below the human native-speaker baseline (the *candidate* Scivetti 2025 baseline, pending item-level inspection and ratification of `comparative-correlative-anchor` — so the "below human" clause is contingent, while the "clears the encoder baseline" clause is not); per-model divergence is itself data on whether residual failure is architectural or idiosyncratic.

## What would confirm / falsify

- **Confirm (narrows-but-not-closes):** CC covariation-inference rate clearly above the non-CC control gap and above the encoder-PLM chance baseline, with correct **direction flipping** on inverse-CC items and persistence on **atypical/held-out** scale pairs, in ≥2 of 3 panel models — yet measurably **below** the human baseline. This is the conjecture's central bet.
- **Stronger-than-conjectured (closes):** decoder LLMs reach human-level covariation inference including on inverse and atypical items. This would *refine* the divergent-form claim toward "the gap is construction- and generation-specific," and the conjecture's "not closing" clause would be retired.
- **Weak:** the inference rate tracks the surface template (positive-CC handled, inverse-CC not; or atypical fillers collapse), i.e. form recognised, meaning still not used — the 2022 dissociation **persists** essentially unchanged.
- **Falsify (of the "narrows" claim):** decoder LLMs are at chance on the covariation inference just as the encoder PLMs were — no narrowing. A clean null here is a first-class negative (charter §2.6): it would say the form/meaning dissociation is durable across model generations, strengthening the `distributional`/formal reading.

## Human anchor (pending)

No human-rated CC **inference** dataset is in-repo. Two in-repo sources bear on the probe but neither is a human-rated `resource`:
- [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) supplies the **encoder-PLM baseline** (form recognised, meaning at chance) — a model-side precedent, not a human norm.
- The Scivetti et al. 2025 **CxNLI CC subset** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)) contains human-annotated NLI triples for the comparative correlative with a native-speaker accuracy baseline — the natural **candidate human anchor**, but the dataset is `external-only` (release repo not yet inspected) and the CC items are not separately verified.

Until a human-rated CC inference set is in-repo and inspected, this conjecture carries `anchor: pending`.

→ Open decision queued: [`decisions/open/comparative-correlative-anchor`](../../decisions/open/comparative-correlative-anchor.md) — whether the Scivetti CxNLI CC subset (pending item-level inspection and ratification) grounds the probe, or whether to fall back to Weissweiler 2022's stimulus design as a seed with the human-comparison arm marked pending.

## Notes / caveats

- The CC's two clauses can themselves telegraph covariation lexically (e.g. causally loaded verbs); control by choosing scale pairs whose covariation is *not* world-knowledge-obvious, so the inference must come from the construction, not from plausibility.
- Probe phrasing matters; trial multiple phrasings **before** seeing results, then commit (charter §8 operationalization gate; shared with [`open-question/constructional-divergence-probe`](../open-questions/constructional-divergence-probe.md)).
- Apples-to-apples with Weissweiler 2022 requires a comparable semantic-application framing; an NLI framing (Scivetti-style) is a *different* instrument and the two baselines are not directly interchangeable — note which is used.
- Frequency is the dominant confound, handled jointly with [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md); lock the frequency-matching procedure before running.
