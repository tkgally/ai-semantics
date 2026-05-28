---
type: source
id: bender-koller-2020-climbing
title: "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data"
authors:
  - Bender, Emily M.
  - Koller, Alexander
year: 2020
venue: "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)"
acl-id: "2020.acl-main.463"
url: https://aclanthology.org/2020.acl-main.463
access: open-access
meaning-senses:
  - grounded
  - distributional
  - referential
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: supports
    target: concept/grounding
---

# Bender & Koller 2020 — Climbing towards NLU

## What it is

Position paper at ACL 2020 (58th Annual Meeting). The founding document of the "form vs. meaning" critique of neural LLMs. Argues that systems trained exclusively on text (form) cannot acquire semantic content (meaning), because meaning is defined by the relation between form and communicative intent — a relation that requires grounding in non-linguistic experience or at minimum in the discourse situation of an agent with goals.

## Summary

Bender & Koller draw a sharp distinction between **form** (the observable surface signal — text, tokens) and **meaning** (the relation between form and something beyond it: the world, a mental state, a communicative intent). Their claim is architecturally grounded: a system that sees only form has no access to the grounding relation, and therefore no access to meaning proper.

Key moves:
1. **Form–meaning distinction.** "A system trained only on form has a priori no way to learn meaning." The central claim: no amount of statistical pattern-learning over linguistic form yields semantic content, because semantic content is defined by a form–non-form relation.
2. **Communicative intent.** Meaning is constituted in communication between agents with intent. A text corpus strips out intent; therefore corpora cannot transmit meaning to a learner.
3. **The octopus thought experiment.** A compelling challenge case: suppose an octopus (lacking the embodied, social history of English speakers) is exposed to English text between two humans. Even if the octopus learns to predict text perfectly, it does not understand the meaning — because meaning requires causal/social grounding that the octopus lacks and the corpus does not supply. This thought experiment directly targets `grounded.causal` and `grounded.social`.
4. **Why the field mischaracterizes LLMs.** The authors identify a cluster of over-claims in NLP evaluation (conflating fluency with understanding, or task performance with semantic competence) and trace them to a failure to keep form and meaning distinct.

## Key quotes

From the abstract and ACL-accessible text:

> "A system trained only on form has a priori no way to learn meaning."

The octopus thought experiment (paraphrase from ACL abstract / accessible summary; exact page citation requires PDF): An agent lacking the embodied and social history that gives English expressions their meaning cannot acquire meaning from text alone, even given unlimited distributional exposure.

## What it can ground

- The `grounded` tag on any finding page: this paper is the canonical statement that `grounded` is a distinct, non-reducible requirement for meaning.
- The `grounded.causal` and `grounded.social` sub-tags specifically — the octopus thought experiment is the reference argument for why those sub-dimensions matter.
- The contrast case against Piantadosi & Hill 2022: any claim that an LLM "tracks" a construction's meaning must situate itself against Bender & Koller's denial that distributional training suffices.
- Claims about whether LLM performance on acceptability/form tasks constitutes evidence about semantic competence — Bender & Koller argue it does not, by definition.

## What it cannot ground

- Claims about degree of grounding or gradient grounding — the paper's argument is binary (form cannot yield meaning); for grounding-as-gradual, cite Lyre 2024 instead.
- Claims about specific construction behavior — the paper makes no predictions about AANN or other particular constructions.

## Known limits

- The form–meaning distinction has been contested (see Piantadosi & Hill 2022 for inferentialist counter; see also meaning-senses.md for why `distributional` and `inferential` do not fully collapse).
- The term "meaning" in the paper is not systematically tagged against a sub-typology; the paper's use of "meaning" spans referential and grounded senses without distinguishing them. Citing it requires specifying which sense the citation is intended to invoke.

## Status in wanted.md

Was `wanted (likely OA, fetch directly)`. Now `catalogued` via ACL Anthology abstract and accessible text. Full PDF available at the ACL Anthology URL above; page-level quotes should be extracted when a finding page requires a verbatim citation.
