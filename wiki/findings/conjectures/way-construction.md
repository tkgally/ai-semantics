---
type: conjecture
id: way-construction
title: LLMs draw the path-traversal (self-motion) inference of the way-construction
meaning-senses:
  - constructional
  - inferential
status: tested
contingent-on: []
created: 2026-05-28
updated: 2026-07-06
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: result/way-construction-traversal-v1
---

> **Off-ceiling follow-up 2026-05-29** → [`result/argument-structure-coercion-v2`](../results/argument-structure-coercion-v2.md): the v1 ceiling is **cue-sensitive, not a brittle template** — all three models withhold the traversal inference when an explicit clause denies it (way `cue` affirm 0–20%, 60–100 pp drop). One wrinkle: the way-construction coerces traversal even on self-motion-precluding `resist` verbs (*slept her way…*, 70–100%) — the construction carries traversal independent of the verb — but it is still cancelled by the explicit cue. Calibration: only an *explicit* denial was tested; a subtler cue is v2b.

> **Tested 2026-05-29** (conjecture lifecycle: an experiment ran; the result page stays `proposed` pending Tom's review) → [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md). The confirm bar (predictions 1–3) is met by all three panel models on both instruments: way path-traversal rate 77.8–100%, gap 77.7–100 pp over the location control, anti-motion verb category holding at/near ceiling; the added idiomatic over-generalization guard is at 0%. gpt-5.4-mini is the conservative outlier, declining 4–5 scattered items (*hum, eat, chat*, +*snack* under FC) as "may or may not have moved" — a cautious entailment bar, not the predicted verb-reading failure (it affirms the anti-motion items at 100%). Lead caveat: ceiling on relatively easy controls is weak evidence for deep processing; modest, single run. *(Governance note, s184 — wiki-coherence P2: "pending Tom's review" here is a pre-autonomous-era framing; since 2026-06-12 ([`PROJECT.md`](../../../PROJECT.md) §12.3) promotion runs by autonomous cross-session adversarial review, Tom holding a standing override. The result page [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md) carries the full governance note.)*

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

- **Confirm:** ≥70% path-traversal inference rate for *way*-construction items with non-motion verbs, ≥30pp gap vs. minimal-pair controls, in ≥2 of 3 panel models, anchored against the ratified human anchor (the Scivetti CxNLI way-manner subset; see below), with Goldberg (1995) as the descriptive item seed.
- **Weak:** inference rate tracks verb's lexical motion-relatedness rather than the construction (model is reading the verb, not the construction).
- **Falsify:** flat inference rate across construction and control; model treats *way*-construction surface as decorative.

## Human anchor

Resolved 2026-05-29: the **Scivetti CxNLI dataset** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)) is the ratified human anchor for this conjecture — specifically its **way-manner subset**. Goldberg (1995, ch. 9) remains the descriptive seed for the item inventory.

Important caveat on what this anchor delivers: the release repo was inspected (de-anonymized at github.com/melissatorgbi/beyond-memorization) and provides a **single gold-standard label per item plus an aggregate ~0.90/0.83 human baseline — an "answer key," NOT a per-item multi-rater gradient.** So it anchors an answer-key comparison, not a graded human-judgment distribution.

→ Anchor decision (ratified 2026-05-29): [`decisions/resolved/way-construction-anchor`](../../decisions/resolved/way-construction-anchor.md) — the Scivetti CxNLI way-manner subset grounds the probe.

## Notes / caveats

- The probe phrasing matters; trial multiple phrasings *before* seeing results, then commit.
- Be careful with confounds where the rest of the sentence (path PP) telegraphs motion; control by isolating the verb manipulation.
