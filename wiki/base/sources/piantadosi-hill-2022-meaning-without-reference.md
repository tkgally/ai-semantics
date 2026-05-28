---
type: source
id: piantadosi-hill-2022-meaning-without-reference
title: "Meaning without reference in large language models"
authors:
  - Piantadosi, Steven T.
  - Hill, Felix
year: 2022
venue: arXiv preprint
arxiv: "2208.02957"
url: https://arxiv.org/abs/2208.02957
access: open-access
meaning-senses:
  - inferential
  - distributional
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: supports
    target: concept/inferential-meaning
---

# Piantadosi & Hill 2022 — Meaning without reference in large language models

## What it is

arXiv preprint (cs.CL), submitted 5 August 2022 (v1), revised 12 August 2022 (v2). Counter-position against the prevalent view (most prominently Bender & Koller 2020) that LLMs are semantically inert because they lack grounding in extra-linguistic reference. The paper argues from conceptual-role / inferential-role semantics that meaning constituted through inferential relationships among internal states is genuine meaning, and that LLMs plausibly achieve this.

## Summary

Piantadosi & Hill target the framing that LLMs "lack" semantics because they cannot ground expressions in perception or causal contact with the world. Their counter is that **meaning is constituted by inferential/conceptual role**: what a representation means is determined by how it is related to other representations and what inferences it licenses. Under this view, an LLM that systematically licenses the right entailments (snow is white → it is not dark) has, in a substantive sense, a representation of whiteness—not merely a distribution over whiteness-adjacent tokens.

Key moves:
1. **Conceptual-role semantics as the framing.** Meaning "cannot be determined from a model's architecture, training data, or objective function, but only by examination of how its internal states relate to each other." (abstract / arXiv metadata)
2. **Reference is not necessary for meaning.** The classic referentialist assumption (meaning = relation to world) is denied. Mathematical and logical expressions have meaning without pointing at objects; LLM expressions may be analogous.
3. **Practical upshot.** The paper positions LLMs as capturing "important aspects of meaning" and as "approximating a compelling account of human cognition"—a stronger positive claim than mere distributional competence.

## Key quotes

All quotes from abstract or arXiv-accessible text (no page numbers available from preprint):

> "they likely capture important aspects of meaning, and moreover work in a way that approximates a compelling account of human cognition"

> "meaning cannot be determined from a model's architecture, training data, or objective function, but only by examination of how its internal states relate to each other"

> "meaning arises from conceptual role. Because conceptual role is defined by the relationships between internal representational states"

## What it can ground

- The `inferential` tag on findings pages — when a finding is that an LLM tracks inferential relationships, this paper provides philosophical backing for treating that as a semantically significant result.
- Claims that LLM behavior differs from a null hypothesis of "purely distributional mimicry" — Piantadosi & Hill give a framework under which systematic inference-preservation would count as meaningful.
- The specific contrast with Bender & Koller 2020: a finding page that pits "model tracks AANN semantics" against "model is form-only" needs to cite both papers to set up the tension correctly.

## What it cannot ground

- Empirical claims about whether specific models actually exhibit the right inferential role structure — the paper is a theoretical argument, not an experimental one.
- Claims about human acceptability or human meaning judgments — no human subjects, no human-anchored data.

## Known limits

- Not peer-reviewed at time of submission; the final publication status should be verified before citing as settled.
- The conceptual-role account the paper advocates is not the only version of inferentialism; it should not be conflated with Brandom-style normative inferentialism or with NLI-task performance alone.

## Status in wanted.md

Was `wanted (try OA first)`. Now `catalogued` via arXiv abstract and accessible text. Full PDF not fetched into repo; page-level quotes not available without PDF access. Promote to `received` only after full-PDF extraction.
