---
type: concept
id: distributional-meaning
title: Distributional meaning
meaning-senses:
  - distributional
  - inferential
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: depends-on
    target: source/weissweiler-2023-cxg-insight
  - rel: refines
    target: concept/formal-vs-functional-competence
  - rel: refines
    target: concept/constructional-meaning
---

# Distributional meaning

The distributional view holds that a linguistic expression's meaning is constituted — or at minimum reliably tracked — by its pattern of co-occurrence across contexts. The canonical formulation is Firth's: "you shall know a word by the company it keeps" (1957; not in-repo). Harris (1954; not in-repo) supplies the formal distributional hypothesis. In the computational tradition the view is instantiated in word embeddings and the next-token-prediction objective: a model trained to predict context implicitly encodes distributional structure, and that structure is often treated as a proxy for lexical or compositional distributional meaning.

For this project the `distributional` tag underwrites the null hypothesis against which constructional and functional-competence claims are tested. When an LLM tracks a construction's characteristic form and statistical environment, that is distributional competence. The live empirical question is whether the tracked structure also encodes the construction's meaning — form-meaning pairing in the CxG sense — or only its formal recurrence. Weissweiler et al. (2023) flag exactly this as the central confound: a model may reproduce collocational patterns without encoding "the extent of the construction" or the inferential role of its slots (source/weissweiler-2023-cxg-insight, §3.1).

A critical constraint on citing distributional meaning: distributional structure is, by itself, **silent on reference and on truth**. The controlled vocabulary in [`meaning-senses.md`](../../meaning-senses.md) (§`distributional`) makes this explicit. Bender & Koller (2020) argue that no amount of distributional pattern-learning yields meaning proper because meaning is defined by a relation to communicative intent and the world — a relation that form-only training cannot supply ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5185). Piantadosi & Hill (2022) contest this, arguing that systematic inferential-role structure — which distributional training plausibly produces — constitutes meaning in the conceptual-role sense, without requiring extra-linguistic reference ([`source/piantadosi-hill-2022-meaning-without-reference`](../sources/piantadosi-hill-2022-meaning-without-reference.md), abstract). The tension between these two positions is live for every empirical finding in this project that involves an LLM.

**Live tension for this project.** Distributional training is also the route by which formal competence is acquired (Mahowald et al. 2024; [`source/mahowald-2024-dissociating`](../sources/mahowald-2024-dissociating.md)): the distributional objective produces strong formal-linguistic competence — structural acceptability, morphological generalization — without demonstrably producing functional competence. A distributional success therefore does not settle the formal/functional question, and it does not settle the grounded/ungrounded question. Findings tagged `distributional` should specify which of those further questions they bear on, or explicitly mark themselves as silent on them. Co-tagging with `inferential` is appropriate when the finding turns on whether the distributional representations also encode inferential roles.
