---
type: concept
id: formal-vs-functional-competence
title: Formal vs. functional linguistic competence
meaning-senses:
  - functional-vs-formal
  - distributional
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: refines
    target: concept/distributional-meaning
  - rel: refines
    target: concept/constructional-meaning
---

# Formal vs. functional linguistic competence

The distinction is drawn by Mahowald, Ivanova, Blank, Kanwisher, Tenenbaum, and Fedorenko (2024), the paper that grounds the `functional-vs-formal` tag in this project's controlled vocabulary. The abstract states the organizing contrast: "Here, we evaluate LLMs using a distinction between formal linguistic competence—knowledge of linguistic rules and patterns—and functional linguistic competence—understanding and using language in the world" (`source/mahowald-2024-dissociating`, abstract). The paper grounds the dissociation neurologically: in humans, formal competence is served by a dedicated language network (inferior frontal gyrus, superior temporal regions), while functional competence recruits the multiple-demand network for reasoning and the default mode network for social cognition. These networks are dissociable in lesion and imaging studies, establishing that the distinction is not merely taxonomic.

**Formal competence** covers the structural knowledge *about* language: phonotactics, morphology, syntax, and compositional structure. Operationally: "being formally competent means getting the form of language right: knowing which strings could be valid words of a language" (`source/mahowald-2024-dissociating`, §"What does linguistic competence entail?"). Grammaticality judgment, structural acceptability tasks, morphological paradigm completion, and structural priming are all formal-competence probes. LLMs show strong — sometimes human-level — performance on such tasks, and the paper treats this as genuine evidence *for* formal competence rather than a proxy for something else. **Functional competence** covers what language is *for*: reasoning, world-knowledge retrieval, common-sense inference, theory of mind, pragmatic adaptation to interlocutor and discourse situation. The paper's verdict: "Although LLMs are surprisingly good at formal competence, their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules" (`source/mahowald-2024-dissociating`, abstract).

For this project the distinction does two pieces of work. First, it prevents over-attribution: a model that reaches acceptability ceiling on the AANN structural contrast has demonstrated formal competence on that construction, not constructional meaning-tracking — the `formal-competence-aann-ceiling` claim encodes this directly. Second, it prevents under-attribution: failure on a world-knowledge task does not show that a model lacks formal linguistic competence. The two questions must be separated before results can be interpreted. Any finding tagged `functional-vs-formal` should specify which side of the line the probe sits on and what additional evidence would be required to establish the other side.

**Live tension for this project.** The formal/functional boundary is not always crisp. Mahowald et al. acknowledge that pragmatics sits at the interface: pragmatic interpretation requires both form-knowledge (what is literally said) and functional resources (what is meant, given interlocutor and context). Constructions whose meaning is heavily conventionalized at the pragmatic level — e.g., indirect speech acts, scalar implicature-bearing forms — straddle the line. For constructions like the AANN, where the constructional meaning is partly formal (the adjective-type and noun-type constraints) and partly semantic-pragmatic (the evaluative-unitization frame), assigning a finding purely to one side requires explicit argument. The distinction is also orthogonal to the grounded/ungrounded distinction of Bender & Koller (2020): a model can be formally competent without being grounded in communicative intent, and the two questions should not be conflated when interpreting probe results.
