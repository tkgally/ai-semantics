---
type: source
id: ashery-2025-llm-conventions
title: Emergent Social Conventions and Collective Bias in LLM Populations
authors:
  - Ashery, Ariel Flint
  - Aiello, Luca Maria
  - Baronchelli, Andrea
year: 2025
venue: Science Advances 11(20), eadu9368
arxiv: "2410.08948"
url: https://arxiv.org/abs/2410.08948
access: open-access
meaning-senses:
  - relational
  - distributional
status: received
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: refines
    target: concept/relational-meaning
---

# Ashery, Aiello & Baronchelli 2025 — Emergent Social Conventions and Collective Bias in LLM Populations

## What it is

Peer-reviewed journal article: *Science Advances* 11(20), eadu9368 (May 2025); open-access preprint at arXiv 2410.08948 (v1 2024-10-11; v2 2025-05-29, the published version). The first major experimental demonstration that **populations of LLM agents spontaneously form shared linguistic conventions** through purely pairwise, decentralized interaction — the naming-game paradigm (Wittgenstein-via-Lewis lineage of convention formation, scaled to LLM agents). This is the project's first dedicated source on the **relational axis**: conventions arising *between* interacting models, not inside one. It was already cited (uncatalogued) as prior art in [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md).

Provenance: abstract verbatim from the arXiv HTML (v2); all body quotes below verified character-for-character against the arXiv HTML v2 full text (fetched 2026-06-12), with section locators. The arXiv v2 page notes it is the preprint version of the *Science Advances* article.

## Summary

Three results, in a minimal naming-game protocol where two randomly paired agents each output a "name" from a finite pool and are rewarded for matching, penalized for mismatching, with each agent conditioning only on a short memory of its own past plays (memory length H=5 in the main runs):

1. **Spontaneous convention emergence.** Populations (N=24 in the main runs, up to N=200; name pools up to W=26) reliably converge on a single population-wide name with no central coordination, no global incentive, and no knowledge of the population — across Llama-2-70b-Chat, Llama-3-70B-Instruct, Llama-3.1-70B-Instruct, and Claude-3.5-Sonnet (claude-3-5-sonnet-20240620).
2. **Collective bias without individual bias.** Which convention wins is systematically skewed even when isolated agents show no preference — the bias is a property of the interaction dynamics, not of any individual agent.
3. **Tipping points.** A committed adversarial minority can flip an established convention once it crosses a critical-mass threshold (2%–67% depending on model and convention strength).

The paper's frame is coordination and AI safety (group-level alignment), not semantics: the conventions are arbitrary labels whose "content" is exhausted by the coordination payoff.

## Key passages

Locators are section titles in the arXiv HTML v2.

**Abstract — the headline:**

> "Here, we present experimental results that demonstrate the spontaneous emergence of universally adopted social conventions in decentralized populations of large language model (LLM) agents. We then show how strong collective biases can emerge during this process, even when agents exhibit no bias individually."

**Introduction — what a convention is:**

> "They can be defined as unwritten, arbitrary patterns of behavior that are collectively shared by a group."

**Experimental Setting (Prompting) — the minimal coordination incentive:**

> "The prompt specifies that if the conventions match, the game score of the agent is incremented, and if they do not match, it is decremented." … "This implements an incentive for coordination in pairwise interactions, while no incentive promotes global consensus. Moreover, the prompt does not specify that agents are part of a population or provide any detail on how the interaction partner is selected from a group."

**Results (Spontaneous Emergence) — the convergence finding:**

> "Fig. 1 shows that group-wide linguistic conventions spontaneously emerge across all models."

**Results (Collective Bias in Convention Selection):**

> "Thus, both social conventions and collective biases in the selection process emerge also in absence of individual biases."

**Results (Tipping Points and Critical Mass):**

> "Interestingly, the critical mass of the committed minority needed to trigger a new convention depends on the convention itself."

**Discussion — the summary claim:**

> "Our findings show that social conventions can spontaneously emerge in populations of Large Language Models (LLMs) through purely local interactions, without any central coordination." … "Importantly, this collective bias is not easily deducible from analyzing isolated agents, and its nature varies depending on the LLM model used."

## What this bears on in-repo

- **The relational axis gets its first dedicated external source.** [`concept/relational-meaning`](../concepts/relational-meaning.md) and the `relational` tag in [`meaning-senses.md`](../../meaning-senses.md) assert that "the multi-agent literature is about coordination, not meaning-constitution." This paper is now the *citable instance* of that assertion: its conventions are arbitrary labels under a match/mismatch payoff, and the paper makes no meaning-constitution claim — convergence is the explanandum, not content.
- **Foil, not anchor, for the pilot.** [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md) already positions this result as the prior art the pilot must position against: convention emergence is reported with **no order-scramble / trajectory-dependence control** and **no human-comparison** — exactly the two disciplines the pilot added. A relational claim cannot be anchored on model-agreement; this page supplies the load-bearing citation for that gap.
- **Consistent with the commutative-convention bet.** The mechanism here — each agent conditioning on a *memory of past plays* and reinforcing matches — is an aggregation-style account in the sense of [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md): convergence driven by accumulated content, with nothing in the design that could detect (or require) path-dependence. The paper neither tests nor contradicts commutativity; it shows how far pure aggregation dynamics go (population-wide consensus, collective bias, tipping points) without any constitution test. That strengthens the foil reading of [`result/relational-reference-game-v1`](../../findings/results/relational-reference-game-v1.md): coordination phenomena, even rich ones, are the *floor*.
- **A deflationary-compatible mechanism.** The convergence story is the kind [`concept/distributional-meaning`](../concepts/distributional-meaning.md) predicts — agents conditioned on overlapping interaction content drift to a shared label; hence the co-tag `distributional`.

## What it can ground

- Citations for "LLM populations form conventions through local interaction alone" — with peer-reviewed (Science Advances) standing.
- The claim that group-level convention dynamics (bias, critical mass) are not reducible to single-agent analysis — useful when the project argues that the relational axis is not redundant with `model-internal` probes.
- The framing that existing multi-agent LLM convention work lacks a constitution test (no trajectory/order control in the design).

## What it cannot ground

- Any claim about meaning-constitution between agents — the paper does not pose the question; its conventions are payoff-defined arbitrary labels.
- Any human-comparison claim — there is no human baseline in the design (unlike the Hawkins tangrams corpus, [`resource/hawkins-tangrams`](../resources/hawkins-tangrams.md)).
- Claims about lexical or constructional content of the conventions — names are drawn from fixed arbitrary pools (e.g. single letters).

## Known limits

- **A live critique exchange exists.** Barrie & Törnberg, "Emergent LLM behaviors are observationally equivalent to data leakage" (arXiv 2505.23796), argues training-data contamination could shape such outcomes; the authors replied (arXiv 2506.18600, fetched abstract 2026-06-12): "While this concern is important and may hinder certain experiments with multi-agent models, it does not preclude the study of genuinely emergent dynamics in LLM populations." Neither the critique nor the reply has been read in full here — any in-repo use of this source for a *strong* emergence claim should first catalogue both sides.
- The naming game is deliberately minimal: a finite name pool and an explicit numeric payoff in the prompt. Generalization to open-vocabulary, task-embedded convention formation (as in the project's reference-game pilot) is an extrapolation.
- Models tested are 2023–24 generation (Llama-2/3/3.1-70B, Claude-3.5-Sonnet); magnitudes (convergence speed, bias direction, critical mass) are explicitly model-dependent in the paper's own results.
- The arXiv v2 HTML rendering strips citation numbers (rendered as "?"); quotes above omit in-text citation markers accordingly.

## Status in wanted.md

Was not previously listed (the relational section of [`wanted.md`](../wanted.md) listed only human-side dyadic anchors). Catalogued 2026-06-12 as the relational axis's first LLM-side source; noted there.
