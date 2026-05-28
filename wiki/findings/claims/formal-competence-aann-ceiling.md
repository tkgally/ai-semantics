---
type: claim
id: formal-competence-aann-ceiling
title: AANN acceptability ceiling is evidence of formal, not functional, linguistic competence
meaning-senses:
  - functional-vs-formal
  - constructional
  - human-comparison
status: proposed
contingent-on: []
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
  - rel: refines
    target: conjecture/aann-construction
---

# Claim: AANN acceptability ceiling is evidence of formal, not functional, linguistic competence

## Statement

If an LLM matches or exceeds human rater agreement on AANN structural-acceptability items, this constitutes evidence of **formal linguistic competence** — the model has internalized structural constraints governing the AANN form. It does not, by itself, constitute evidence of **functional linguistic competence** or **constructional meaning-tracking** in the CxG sense. A model that reaches ceiling on AANN structural acceptability has not thereby demonstrated that it has internalized the construction's characteristic meaning (unification, evaluation, scalar framing). The acceptability task is a necessary but not sufficient test for that claim.

## Grounding

### Formal competence defined (Mahowald et al. 2024)

The theoretical framework is supplied by Mahowald et al. 2024 (`source/mahowald-2024-dissociating`), the defining statement of the formal-vs-functional competence distinction as applied to LLMs. From the Abstract:

> "We evaluate LLMs using a distinction between formal linguistic competence—knowledge of linguistic rules and patterns—and functional linguistic competence—understanding and using language in the world."

The paper defines formal competence operationally in the section "What does linguistic competence entail?":

> "We define formal linguistic competence as a set of capacities required to produce and comprehend a given language. Broadly, being formally competent means getting the form of language right: knowing which strings could be valid words of a language (e.g., bnick cannot be a word in English but blick can)."

The AANN task fits this definition exactly: the acceptability contrast between *a beautiful three days* and its degenerate variants (*a three beautiful days*, *a three days*, *a beautiful three day*, *beautiful three days*) asks whether the model knows which strings are structurally valid in English — form-correctness, not meaning-tracking.

The paper's verdict on LLM performance on formal-competence tasks:

> "Although LLMs are surprisingly good at formal competence, their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules."

LLM success on grammaticality judgment and structural acceptability tasks is the paper's primary evidence *for* formal competence. The AANN structural-acceptability task belongs to that category.

### Human anchor (Mahowald 2023 AANN stimuli)

The human behavioral anchor is the MTurk acceptability rating corpus in `resource/mahowald-2023-aann-stimuli`. In that study, 126 US-English raters assigned acceptability scores on a 1–10 scale to AANN sentences and their degenerate variants. These are **form-acceptability judgments**: raters were asked whether a sentence "sounds good," not what meaning it carries or what inference it licenses. Correlation with these ratings therefore confirms that a model tracks human structural intuitions; it does not confirm that the model tracks the construction's meaning.

### The gap this identifies

The AANN construction carries a characteristic meaning beyond well-formedness: the measured quantity is presented as a unified, coherent, often evaluatively-loaded stretch. This is the *constructional* meaning — the form–meaning pairing that CxG identifies at the argument-structure or multi-word template level. Structural acceptability probes only whether the form sounds well-formed; the meaning side requires additional evidence: adjective-type gradient tracking (evaluative > measure-quantifying > stubborn/color), noun-type sensitivity that reflects semantic constraints (temporal/measure nouns most acceptable), and generalization to held-out lexical items.

## What this claim does not say

- It does not assert that LLMs lack constructional meaning-tracking. The acceptability task is silent on whether the model has or lacks that capacity; it simply cannot provide evidence either way.
- It does not say the AANN probe is uninformative. The adjective-type and noun-type gradients *within* the Mahowald stimulus set do begin to probe semantic constraints — but that probe is conceptually distinct from the plain form-acceptability contrast, and must be identified as the separate meaning-diagnostic that it is.
- It does not invoke the grounded/ungrounded distinction (Bender & Koller). The formal/functional distinction is orthogonal to the grounded/ungrounded distinction. A model can be formally competent without being grounded; the two questions are separable and should not be conflated.

## Payoff for the AANN project line

This claim is the **theoretical wedge** that makes the AANN probe scientifically interesting. Were acceptability tracking sufficient evidence for constructional meaning, a ceiling result would be a complete confirmation of `conjecture/aann-construction`. This claim blocks that inference. The conjecture's confirmation criteria must therefore target evidence that goes beyond form-acceptability — specifically, gradient tracking of the construction's characteristic semantics. This sharpens what the probe is for before it runs, and specifies the conditions under which an AANN ceiling result would still be a null on the constructional meaning question.

## Scope and limits

- The formal/functional distinction is a theoretical frame applied here to AANN; its empirical support comes from the neuroscience dissociations reviewed in Mahowald 2024, not from this project's probes.
- Mahowald 2024 acknowledges the formal/functional boundary is not always crisp (pragmatics sits at the interface). For constructions whose meaning is heavily conventionalized at the pragmatic level, this caveat applies.
- This claim covers the *class* of structural-acceptability probes of which the AANN contrast task is an instance. It does not cover the adjective-type gradient or noun-type sensitivity measures, which are mixed formal/semantic probes and require separate treatment.
- Status is `proposed` because the application of the Mahowald 2024 framework to the AANN domain is an inference made here; it has not been independently tested or published in that specific form.
