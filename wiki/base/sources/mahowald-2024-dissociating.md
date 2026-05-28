---
type: source
id: mahowald-2024-dissociating
title: "Dissociating language and thought in large language models"
authors:
  - Mahowald, Kyle
  - Ivanova, Anna A.
  - Blank, Idan A.
  - Kanwisher, Nancy
  - Tenenbaum, Joshua B.
  - Fedorenko, Evelina
year: 2024
venue: "Trends in Cognitive Sciences"
volume: 28
issue: 6
arxiv: "2301.06627"
doi: "10.1016/j.tics.2024.01.011"
url: https://arxiv.org/abs/2301.06627
access: open-access
license: "CC BY 4.0"
meaning-senses:
  - functional-vs-formal
  - distributional
  - human-comparison
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: supports
    target: concept/formal-vs-functional-competence
---

# Mahowald et al. 2024 — Dissociating language and thought in large language models

## What it is

Review article in *Trends in Cognitive Sciences*, Vol. 28, No. 6 (2024). Open access (CC BY 4.0); preprint at arXiv 2301.06627. The defining statement of the **formal-vs-functional competence** distinction as applied to LLMs. Co-authored by Mahowald, Ivanova, Blank, Kanwisher, Tenenbaum, and Fedorenko — six researchers whose backgrounds span linguistics, cognitive neuroscience, and AI. The paper grounds the distinction in neuroscience: formal and functional competences rely on different neural mechanisms in humans, and the paper argues that LLMs replicate the former more than the latter.

## Summary

The paper's organizing intervention is a two-part taxonomy:

1. **Formal linguistic competence** — "knowledge of linguistic rules and patterns." Includes phonology, morphology, syntax, and compositional (formal) semantics: the structural knowledge *about* language. Probed by grammaticality judgments, structural acceptability tasks, and standard NLP benchmarks focused on form.

2. **Functional linguistic competence** — "understanding and using language in the world." Requires reasoning, world knowledge, common-sense inference, theory of mind, and pragmatics — knowledge of what language is *for*. Probed by tasks like math word problems, factual Q&A, social reasoning, and pragmatic inference.

Key moves:

1. **Neuroscience grounding of the dissociation.** In humans, formal competence is served primarily by the language network (inferior frontal gyrus, superior temporal regions); functional competence recruits other systems — the multiple demand (MD) network for reasoning, and the default mode network (DMN) for social cognition. The two are dissociable in lesion studies and functional imaging. This grounds the claim that the distinction is not merely terminological.

2. **LLMs excel at formal competence.** The paper marshals evidence that LLMs achieve or approach human-level performance on grammaticality judgment tasks, morphological generalization, and structural priming — i.e., the formal-competence tests.

3. **LLMs' functional competence is variable.** "Their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules." Tasks probing reasoning, factual knowledge, and theory of mind show large variance across models and conditions.

4. **The dissociation matters for evaluation.** A model that excels on formal-competence benchmarks does not thereby demonstrate functional competence. Conversely, failure on a world-knowledge task does not show that a model lacks formal linguistic competence. Conflating the two leads to both over-attribution and under-attribution.

5. **Design implication.** "Models that use language in human-like ways would need to master both of these competence types, which, in turn, could require the emergence of mechanisms specialized for formal linguistic competence, distinct from functional competence." The paper is not pessimistic — it sketches a research agenda rather than a verdict.

## Key quotes

From the abstract (verbatim, retrieved from arXiv 2301.06627):

> "Large Language Models (LLMs) have come closest among all models to date to mastering human language, yet opinions about their linguistic and cognitive capabilities remain split."

> "formal linguistic competence — knowledge of linguistic rules and patterns — and functional linguistic competence — understanding and using language in the world"

> "Although LLMs are surprisingly good at formal competence, their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules."

> "models that use language in human-like ways would need to master both of these competence types, which, in turn, could require the emergence of mechanisms specialized for formal linguistic competence, distinct from functional competence."

Page-level quotes require the full PDF; promote to `received` after PDF extraction.

## What it can ground

- The `functional-vs-formal` tag on any finding page — this paper *is* the primary reference for that tag. `meaning-senses.md` explicitly attributes this distinction to "the Mahowald / Ivanova / Fedorenko distinction."
- Claims that LLM performance on structural acceptability tasks (e.g., AANN) constitutes evidence of **formal** competence without warranting conclusions about **functional** competence. This is directly useful for AANN results: acceptability judgments probe formal competence; what follows about meaning-tracking is a separate question.
- Any finding that needs to situate LLM grammatical behavior against a competence theory: this paper provides the theoretical vocabulary.
- Claims about the relevance of neuroscience dissociations to LLM evaluation methodology.

## What it cannot ground

- Claims about specific constructions in detail — the paper reviews the distinction at a high level; it does not examine AANN, dative alternation, or *way*-constructions specifically.
- Claims about grounding in the Bender & Koller sense — the formal/functional distinction is orthogonal to the grounded/ungrounded distinction. A model can be formally competent but not grounded; or it can have functional competence in some domains without full causal grounding.
- Gradient claims about meaning — Mahowald et al. do not argue for degrees of semantic content; they argue for dissociable competence types. For gradient grounding, cite Lyre 2024.
- Claims about human judgments or human meaning — this paper's human anchor is the neuroscience dissociation, not behavioral norms for specific constructions.

## Known limits

- The paper reviews evidence as of its 2023–24 drafting. LLM capabilities change rapidly; specific benchmarks cited may be superseded.
- "Formal semantics" as used in the paper (compositional structure-to-meaning mapping) overlaps with but is not identical to `constructional` meaning in the CxG sense. Citing it for construction probing requires care.
- The distinction formal/functional is a dichotomy for expository purposes; the paper acknowledges that the boundary is not always crisp (pragmatics, e.g., sits at the interface).

## Status in wanted.md

Was `wanted (try OA / preprint)`. Now `catalogued` via arXiv abstract (2301.06627) and abstract-level text. Full PDF available via DOI (10.1016/j.tics.2024.01.011) under CC BY 4.0; page-level quotes should be extracted when a finding page requires verbatim citation. Promote to `received` after PDF extraction.
