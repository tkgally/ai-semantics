---
type: concept
id: grounding
title: Grounding (form-vs-meaning; grounding-as-gradual)
meaning-senses:
  - grounded
  - functional-vs-formal
  - relational
created: 2026-05-28
updated: 2026-05-29
links:
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/lyre-2024-semantic-grounding
---

# Grounding

Grounding is the question of whether, and how, a linguistic expression is anchored in something beyond linguistic form — perception, action, the body, causal structure, or social embedding. It is the hinge on which the entire "do LLMs mean anything" debate turns, because a system trained on text alone has, on its face, access only to form. Two positions frame the live debate, and they are not reconcilable by fiat. The first treats grounding as a binary precondition for meaning; the second treats it as a graded, multi-dimensional property. This project adopts the gradual framing as a working stance — but, as the closing note records, that is a contestable choice, not a settled result.

## The strong binary form: Bender & Koller (2020)

Bender & Koller draw a sharp line between **form** (the observable surface signal — text, tokens) and **meaning** (the relation between form and something beyond it: the world, a mental state, a communicative intent). Their central claim is architectural and binary: "we argue that a system trained only on form has a priori no way to learn meaning" ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5185, abstract). They make this precise by defining meaning as a relation: "We take meaning to be the relation M ⊆ E × I which contains pairs (e, i) of natural language expressions e and the communicative intents i they can be used to evoke" ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5187). Because a text corpus strips out the communicative intent that fixes M, no amount of distributional pattern-learning over form can recover it.

The octopus thought experiment is the canonical illustration: an octopus that learns to predict English text exchanged between two humans does not thereby understand it, because reconstructing the underlying communicative intents from form alone "is hopeless" ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5189). On this view grounding is a non-reducible requirement, satisfied or not; a system either has access to the form–non-form relation or it does not. Note that the octopus stresses `grounded.causal` and `grounded.social` specifically — not `distributional`, which the octopus is stipulated to have mastered.

## The gradual, three-dimensional form: Lyre (2024)

Lyre rejects the binary framing. On his account "it is by no means a simple yes-no question" and grounding "is also gradual, in other words, it comes in degrees" ([`source/lyre-2024-semantic-grounding`](../sources/lyre-2024-semantic-grounding.md), p. 3). He decomposes grounding into three dimensions — **functional** (systematic mappings between symbols and their roles in inference and behavior), **social** (participation in communicative norms and joint action), and **causal** (tracking of causal structure in the world) — and concludes that LLMs are partially grounded along all three: in the abstract, "Grounding proves to be a gradual affair with a three-dimensional distinction between functional, social and causal grounding. LLMs show basic evidence in all three dimensions" ([`source/lyre-2024-semantic-grounding`](../sources/lyre-2024-semantic-grounding.md), p. 1). His verdict is hedged to an "elementary sense": LLMs "are neither stochastic parrots nor semantic zombies, but already understand the language they generate, at least in an elementary sense" (same passage). The summary verdict scores them as "reasonably functionally grounded," "weakly socially grounded," and "indirectly causally grounded" via world models ([`source/lyre-2024-semantic-grounding`](../sources/lyre-2024-semantic-grounding.md), p. 14).

## Sub-tags and how the project uses them

The controlled vocabulary in [`meaning-senses.md`](../../meaning-senses.md) (§`grounded`) carries three sub-tags, which map onto — but are not identical to — Lyre's three dimensions:

- `grounded.perceptual` — multimodal anchoring (text+image+audio+video). This is the sub-dimension Lyre's text-only analysis says least about; it is bitten by the multimodal case.
- `grounded.causal` — tracking of intervention/consequence structure. Lyre's "causal grounding" (indirect, via world models) and the octopus's causal target both live here.
- `grounded.social` — uptake in joint action, normative status. Lyre's "social grounding" lives here; the meaning-senses page flags that this sub-tag "bleeds into `relational`" (see Live tension).

The project's wedge is to ask for *degrees* of grounding rather than a presence/absence verdict — to treat systematic functional behavior on a construction probe as evidence *for some* (partial, dimension-specific) grounding rather than as silent on the question. Lyre is the explicit warrant for this gradient framing: his source page records that any "finding page that argues for *degrees* of constructional meaning rather than a presence/absence verdict — this paper is the direct warrant for a gradient framing." Functional grounding in Lyre's sense is close to, but not identical with, the `inferential` meaning-sense (Brandom/Piantadosi), and conflating the two would be a defect.

**Live tension for this project.** The binary framing (Bender & Koller) and the gradual framing (Lyre) are not reconcilable by fiat: one denies that form-only training can yield meaning *at all*, the other measures *how much* grounding such training yields. The project adopts the gradual framing as a working stance because it is the one that lets degrees-of-meaning findings be stated at all — but this is a contestable choice, and the choice should travel with two honest caveats. First, Lyre 2024 is a non-peer-reviewed arXiv preprint whose three-dimensional typology is "Lyre's own framing, not a widely ratified taxonomy" ([`source/lyre-2024-semantic-grounding`](../sources/lyre-2024-semantic-grounding.md), Known limits); it should be cited with attribution, not as consensus. Second, the typology itself has an open seam: [`meaning-senses.md`](../../meaning-senses.md) (§Open issues) asks whether `grounded.social` is really a sub-tag of `grounded` or "a separate top-level sense closer to `relational`. Plausibly the latter for this project." Until that decision is taken, a finding that turns on social grounding should consider co-tagging `relational`, and should not treat the `grounded`-vs-`relational` placement as settled.
