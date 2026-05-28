---
type: source
id: lyre-2024-semantic-grounding
title: '"Understanding AI": Semantic Grounding in Large Language Models'
authors:
  - Lyre, Holger
year: 2024
venue: arXiv preprint
arxiv: "2402.10992"
url: https://arxiv.org/abs/2402.10992
access: open-access
meaning-senses:
  - grounded
  - inferential
  - functional-vs-formal
status: received
created: 2026-05-28
updated: 2026-05-28
pdf-pages: 18
links:
  - rel: refines
    target: concept/grounding
---

# Lyre 2024 — "Understanding AI": Semantic Grounding in Large Language Models

## What it is

arXiv preprint (cs.CL), submitted 16 February 2024. A philosophical analysis of whether LLMs possess semantic understanding. Distinguished from Bender & Koller 2020 and Piantadosi & Hill 2022 by treating grounding as a **graded, multi-dimensional** property rather than a binary threshold. Provides the most structured typology of grounding currently in the project's reading list.

## Summary

Lyre examines five methodological approaches to the question of whether LLMs have semantic understanding (behaviorist, neuroscience-informed, computational, philosophical-of-mind, and grounding-theoretic), argues for the grounding-theoretic approach as most tractable, and concludes that grounding is not an all-or-nothing phenomenon.

Key moves:
1. **Grounding-as-gradual.** "Grounding proves to be a gradual affair" — not a binary property that LLMs either have or lack entirely. This is the key claim that justifies a project wedge looking for *degrees* of constructional meaning, not a yes/no answer.
2. **Three-dimensional typology.** Grounding has three components:
   - **Functional grounding**: grounding via systematic mappings between symbols and their roles in inference/behavior (closely related to `inferential` sense).
   - **Social grounding**: grounding via participation in communicative norms and joint action (overlaps with `grounded.social`).
   - **Causal grounding**: grounding via tracking of causal structure in the world (overlaps with `grounded.causal`).
3. **LLMs show basic evidence in all three dimensions.** Lyre's conclusion: LLMs "are neither stochastic parrots nor semantic zombies, but already understand the language they generate, at least in an elementary sense." The phrase "elementary sense" is important — it is a gradient claim, not an endorsement of full human-like semantics.
4. **World models.** Lyre cites evidence that LLMs develop internal world models as supporting functional and causal grounding.

## Key passages

Page numbers refer to the arXiv preprint PDF (18 pp.). Note: preprint has no formal section-level pagination; pages counted from p. 1 (title/abstract).

**p. 1 (abstract) — main thesis:**

> "Grounding proves to be a gradual affair with a three-dimensional distinction between functional, social and causal grounding. LLMs show basic evidence in all three dimensions. A strong argument is that LLMs develop world models. Hence, LLMs are neither stochastic parrots nor semantic zombies, but already understand the language they generate, at least in an elementary sense."

**p. 3 — three-dimensional typology introduced:**

> "it is by no means a simple yes-no question. Second, it is multi-criterial, and I will distinguish three basic types of grounding under the titles functional, social and causal grounding. Third, grounding is also gradual, in other words, it comes in degrees. My analysis aims to show that modern LLMs possess a decent functional, a weak social, and an indirect causal grounding."

**p. 10 — grounding as graduated:**

> "semantic grounding isn't a yes-no matter, but rather a matter of degree. Intelligent or cognitive agents and systems can be more or less semantically grounded, they can speak or think more or less meaningfully. This should be familiar to us humans: we are born without any semantic grounding and become increasingly more grounded as we grow up."

**p. 12 — indirect causal grounding via world models:**

> "modern LLMs develop world models, i.e. representations that are structurally similar to (parts of) the world. Put differently: the totality of text and language data is like a huge mirror of the world created by us humans, and modern LLMs are capable of extracting law-like world structures and regularities from the huge amounts of text data from which they learn."

**p. 14 (conclusion) — summary verdict:**

> "LLMs are neither stochastic parrots nor semantic zombies, but must rather be seen as (i) reasonably functionally grounded, (ii) weakly socially grounded, and (iii) indirectly causally grounded. A strong argument for grounding is that LLMs form world models, and the evidence for this is that the representational geometry of these models follows semantic similarities."

## What it can ground

- The `grounded` tag and all three sub-tags (`grounded.causal`, `grounded.social`, `grounded.perceptual`) — Lyre provides the most explicit typological base for these sub-distinctions.
- Any finding page that argues for *degrees* of constructional meaning rather than a presence/absence verdict — this paper is the direct warrant for a gradient framing.
- Claims that an LLM's behavior in a construction probe constitutes evidence *for* some (partial) grounding: Lyre gives philosophical grounds for treating systematic functional behavior as a grounding indicator.

## What it cannot ground

- Claims about specific constructions or acceptability — the paper is philosophical, not empirical on any particular linguistic phenomenon.
- Claims about human judgments or human meaning — no human-anchored data.
- Strong claims that LLMs are fully semantically competent — Lyre explicitly hedges to "elementary sense."

## Known limits

- arXiv preprint; not peer-reviewed at time of retrieval. Publication status should be verified before a finding leans heavily on it as an authority.
- The three-dimensional typology is Lyre's own framing, not a widely ratified taxonomy — it should be cited with attribution rather than treated as consensus.
- Functional grounding as Lyre defines it is close to (but not identical with) inferential-role semantics in the Brandom/Piantadosi sense — conflating them would be a defect.

## Status in wanted.md

Was `wanted (likely OA)`, then `catalogued`. Now `received`: full PDF fetched from arXiv (2026-05-28); page-level verbatim quotes extracted above.
