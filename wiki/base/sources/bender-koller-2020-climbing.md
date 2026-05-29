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
status: received
created: 2026-05-28
updated: 2026-05-28
pdf-pages: 5185–5198
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

## Key passages

All page numbers refer to the ACL Anthology proceedings pagination (pp. 5185–5198). Abstract text confirmed verbatim from ACL Anthology abstract field (https://aclanthology.org/2020.acl-main.463/, 2026-05-28).

**p. 5185 (abstract) — full abstract verbatim:**

> "The success of the large neural language models on many NLP tasks is exciting. However, we find that these successes sometimes lead to hype in which these models are being described as "understanding" language or capturing "meaning". In this position paper, we argue that a system trained only on form has a priori no way to learn meaning. In keeping with the ACL 2020 theme of "Taking Stock of Where We've Been and Where We're Going", we argue that a clear understanding of the distinction between form and meaning will help guide the field towards better science around natural language understanding."

**p. 5185 (abstract) — central thesis (short form):**

> "we argue that a system trained only on form has a priori no way to learn meaning"

**p. 5187 — formal definition of meaning as a relation:**

> "We take meaning to be the relation M ⊆ E × I which contains pairs (e, i) of natural language expressions e and the communicative intents i they can be used to evoke."

**p. 5187 — impossibility argument (core of the paper):**

> "We argue that a model of natural language that is trained purely on form will not learn meaning: if the training data is only form, there is not sufficient signal to learn the relation M between that form and the non-linguistic intent of human language users, nor C between form and the standing meaning the linguistic system assigns to each form."

**p. 5189 — octopus resolution (grounding required):**

> "Having only form available as training data, O did not learn meaning. The language exchanged by A and B is a projection of their communicative intents through the meaning relation into linguistic forms. Without access to a means of hypothesizing and testing the underlying communicative intents, reconstructing them from the forms alone is hopeless, and O's language use will eventually diverge from the language use of an agent who can ground their language in coherent communicative intents."

**p. 5190 — language acquisition corollary:**

> "Human children do not learn meaning from form alone and we should not expect machines to do so either."

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

Was `wanted (likely OA, fetch directly)`, then `catalogued`. Now `received`: abstract confirmed verbatim from ACL Anthology abstract field (2026-05-28); body quotes (pp. 5187–5190) extracted from PDF at prior ingestion step. PDF is binary-only (no HTML rendering available at ACL Anthology); body-quote page numbers were recorded at prior ingestion and are retained as-is. Abstract now added verbatim (2026-05-28 upgrade).
