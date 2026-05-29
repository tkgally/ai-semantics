---
type: conjecture
id: way-construction
title: LLMs draw the path-traversal (self-motion) inference of the way-construction
meaning-senses:
  - constructional
  - inferential
status: designed
contingent-on: []
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
---

# Conjecture: LLMs draw the path-traversal (self-motion) inference of the *way*-construction

## Statement

The English ***way*-construction** — *He whistled his way down the hall*, *She elbowed her way through the crowd*, *They drank their way through the night* — is a paradigmatic CxG case where the **construction** contributes the meaning ("subject moves along a path while/by V-ing"), not the verb. The verbs *whistle*, *elbow*, *drink* are not lexically motion verbs.

The conjecture: LLMs draw the path-traversal (self-motion) inference from *way*-construction instances even when the verb is non-motion, and they do so at a rate that distinguishes the construction from minimally-different non-constructional alternatives.

## Why this is interesting

- It is the cleanest case where meaning is plausibly *located in the construction* rather than in any of its lexical parts. If an LLM draws the path-traversal inference, that is direct evidence for `constructional` meaning being computed.
- It bites the `inferential` side specifically: confirming the conjecture requires showing the model treats the construction as licensing the path-traversal inference, not merely producing fluent text.
- Pairs naturally with the panel-divergence question: do all models converge on the construction's inferential consequences, or only some?

## Predictions

1. Given an inferential probe ("After the sentence X, is it true that the subject moved along the path? Y/N"), the *way*-construction yields a high "yes" rate even for non-motion verbs.
2. Minimally-different controls (*He whistled in the hall*) yield a substantially lower "yes" rate.
3. The construction-specific inference is robust to manipulation of verb semantics: even with verbs that *contradict* motion (e.g., *He paused his way down the hall* — likely odd, but the construction may still pull the inference).

## What would confirm / falsify

- **Confirm:** ≥70% path-traversal inference rate for *way*-construction items with non-motion verbs, ≥30pp gap vs. minimal-pair controls, in ≥2 of 3 panel models, anchored against the Goldberg (1995) stimulus inventory.
- **Weak:** inference rate tracks verb's lexical motion-relatedness rather than the construction (model is reading the verb, not the construction).
- **Falsify:** flat inference rate across construction and control; model treats *way*-construction surface as decorative.

## Human anchor (pending)

Goldberg (1995, ch. 9) gives the canonical inventory of *way*-construction stimuli with discussion. A modern rated version would be ideal. Queue [`decisions/open/way-construction-anchor`](../../../decisions/open/way-construction-anchor.md) at design time.

## Notes / caveats

- The probe phrasing matters; trial multiple phrasings *before* seeing results, then commit.
- Be careful with confounds where the rest of the sentence (path PP) telegraphs motion; control by isolating the verb manipulation.
