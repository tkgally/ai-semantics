---
type: theory
id: lexicon-grammar-continuum
title: One continuum, one test — lexical sense and constructional meaning as a single form–meaning cline, probed by the same "beat the distributional shadow" skeleton
meaning-senses:
  - constructional
  - referential
  - distributional
  - inferential
status: draft
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: supports
    target: open-question/lexical-polysemy-gradience
---

# Theory (draft): the lexicon–grammar continuum, and the single test that spans it

## Why this page exists

The project has run on two tracks that looked separate: a **grammatical** wedge (constructional meaning — does a model track a construction's contributed inference?) with nine-plus own-design results, and, as of 2026-05-30, a **lexical** wedge (sense gradience — does a model track graded word-sense relatedness?) with its first result, [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md). Tom's steer is to connect them, in theory and empirically. This page argues they are **not two tracks but one**, and that the project has — without having named it — been applying a **single evidential test** on both. It is a synthesis page (a framework + a bridge), claiming a structure, not new data; the new data are on the two result pages it leans on.

## The continuum thesis (grounded, not novel)

Construction Grammar's foundational move is that the lexicon and the grammar are **not different kinds of thing**. [`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md) states it directly: constructions "range from morphemes and closed-class items through idioms and argument-structure templates to large-scale discourse patterns" — a single inventory (a *constructicon*) along a cline of **specificity** and **schematicity**. A word is, on this view, a maximally specific construction (a form–meaning pairing with a fully fixed form); an argument-structure template is a maximally schematic one. There is no principled seam between "lexical meaning" and "grammatical meaning"; there is one form–meaning space at different grains. (CxG canon — Goldberg 1995/2006, Langacker, Croft 2001 — is referenced in `constructional-meaning` as not-in-repo; the continuum claim here rests on that concept page's in-repo statement of it, not on fabricated quotation.)

If that is right, then the project's two wedges are the **two ends of one cline**:

| | grain | the "meaning" tracked | the project's anchor | the distributional **shadow** (null) |
|---|---|---|---|---|
| **Lexical wedge** | maximally specific (a word) | graded **sense relatedness** of a word across uses ([`concept/polysemy`](../../base/concepts/polysemy.md)) | DWUG graded DURel judgments | **context/topic similarity** of the two sentences |
| **Grammatical wedge** | maximally schematic (a construction) | a construction's **contributed inference** ([`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md)) | Scivetti CxNLI / own minimal pairs | **n-gram frequency / surface form** |

## The single test: "does a meaning gradient beat the distributional shadow?"

Read across that table, the two wedges run the **same experiment**. In both, a fluent model has a *distributional structure for free* — co-occurrence neighbourhoods for words, surface-form regularities for constructions — and the live question is whether the model tracks a **meaning gradient that is not reducible to that distributional structure**. This is exactly the null-hypothesis discipline [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) imposes, and it is the spine of both the constructional evidence ladder ([`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md), where Tiers 1–3 must beat a frequency/form shadow) and the lexical conjecture's load-bearing clause (c) (the sense signal must survive a context-similarity control).

The two open-questions that name the shadow are explicitly parallel — [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md) (grammar: is it construction or n-gram frequency?) and the lexical conjecture's clause (c) / [`open-question/lexical-polysemy-gradience`](../open-questions/lexical-polysemy-gradience.md) (lexicon: is it sense or context similarity?). They are the **same question at two grains**.

**The state of the evidence, unified:** the project now has a *positive that beats the distributional shadow on **both** ends of the cline* —

- **Grammatical end:** the comparative correlative deploys its covariation inference above matched controls, survives conflicting world knowledge and operator embedding, and composes ([`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md) → v2 → v3). The shadow (form/frequency) does not explain it.
- **Lexical end:** the panel's graded sense-relatedness rating tracks the human DURel median (Spearman 0.60–0.83, in/above the human inter-annotator range) and **survives partialling out the model's own topic-similarity** ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)). The shadow (context similarity) does not explain it either.

This is the first time the project can state its central finding as a **cline-spanning** one rather than a grammar-only one: *current decoders track a graded form–meaning signal that beats the distributional null at both the word grain and the construction grain* — with the same caveats on both (behavioral not representational; single runs; modest N; the hard *negative* directions — divergent-form generalization on grammar, the untested polysemy/homonymy split on lexis — still open).

## The empirical bridge: coercion is where the two grains touch

The cleanest place the cline becomes a single phenomenon is **coercion** ([`concept/coercion`](../../base/concepts/coercion.md)) — a construction overriding a word. When the caused-motion construction makes *sneeze* in *she sneezed the napkin off the table* contribute causation-of-motion it does not lexically have, that **is** a shift in the word's sense *induced by the grammar*. Constructional coercion (grammar end) and contextual sense modulation (lexicon end) are the **same event** described from the two ends of the cline. The project has measured each end separately — the caused-motion construction's inference is genuinely construction-keyed ([`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md)); a word's sense relatedness is gradiently tracked (the lexical result) — but never the **join**.

The join is directly testable with the instrument the lexical probe already built: take a coercing construction and ask, with the DWUG-style relatedness rating, **how related is the verb's sense between its neutral frame and its coerced frame**, against non-coercing controls. If the model registers coercion *as* sense modulation, the coerced pair should be rated **less sense-related** than a matched non-coercing pair, gradiently with coercion strength. That probe — [`design/coercion-as-sense-modulation-v1`](../../../experiments/designs/coercion-as-sense-modulation-v1.md) — is the empirical bridge this page proposes; it reuses the lexical instrument on constructional stimuli, so a result speaks to *both* wedges at once. (Internal-contrast-only: there is no in-repo human relatedness rating for constructed coercion pairs, so it is anchored `pending` like the off-ceiling constructional probes.)

## What this page predicts and forbids

**Predicts.** If the continuum thesis holds for these models, the two wedges should not dissociate sharply: a model that tracks the meaning gradient at one grain should tend to at the other (the lexical and grammatical positives co-occurring in the same panel is weak confirmation), and coercion should show up *in the lexical instrument* as a sense shift (the bridge probe's bet). The per-model ordering may even transfer — a point to watch is whether the model that is strongest lexically (gemini, here) is also strong on the constructional inference probes.

**Forbids.** It forbids treating a lexical null and a grammatical null as unrelated: a context-similarity shadow (lexicon) and a frequency shadow (grammar) are the *same* deflationary hypothesis at two grains, and a finding that the gradient is "just distributional" on one end should lower the prior that it is genuine on the other. It also forbids over-reading the unification: the continuum is a claim about the *targets* (form–meaning pairings at different grains), **not** a claim that the model uses one mechanism for both — that is an open representational question this behavioral evidence cannot settle.

## Status and revision hook

`status: draft`; `contingent-on: []`. It introduces no new empirical claim of its own — it reorganizes two existing results under one frame and proposes one bridge probe. Revision triggers: the bridge probe running (does coercion register as lexical sense modulation?); the lexical v2 (polysemy-vs-homonymy) landing (does the *negative*/hard direction also mirror across grains?); or a model-ordering check (do the lexical and grammatical competence orderings agree across the panel?).
