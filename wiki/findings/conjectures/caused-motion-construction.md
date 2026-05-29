---
type: conjecture
id: caused-motion-construction
title: LLMs draw the caused-motion inference from verbs that cannot lexically license it
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
contingent-on:
  - caused-motion-anchor
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
---

# Conjecture: LLMs draw the caused-motion inference from non-motion verbs

## Statement

The English **caused-motion construction** — `Subj V Obj Obl(path/goal)`, as in *She sneezed the napkin off the table*, *He laughed the actor off the stage*, *They prayed the demons out of the house* — is Goldberg's (1995) paradigm case for argument structure being a form–meaning pairing in its own right. The construction means roughly "X causes Y to move along path Z by V-ing," and it contributes a **causation-of-motion entailment** even when the verb (*sneeze*, *laugh*, *pray*) has no lexical argument structure that would license a direct object or an oblique path, and denotes no motion.

The conjecture: current LLMs draw the caused-motion entailment — *Y moved along Z*, and *the subject's V-ing caused it* — from caused-motion instances with non-motion, non-transitive verbs, at a rate that separates the construction from minimally different surface strings in which the same verb appears without the construction.

This is distinct from the `way`-construction conjecture ([`conjecture/way-construction`](way-construction.md)): there the moving entity is the *subject* and the path is reflexive (*his way*); here the moving entity is a *distinct direct object* the subject acts on, and the entailment is **transitive causation**, not self-propelled motion. The two probe different corners of the argument-structure space.

## Why this is interesting

- It is the canonical demonstration that argument-structure meaning is **not** projected from the verb's lexical frame — *sneeze* is intransitive, takes no object and no path, yet the construction coerces both. If an LLM draws the causation-of-motion entailment here, the meaning it is reading cannot be coming from the verb's lexical entry; it must be `constructional`.
- It bites the `inferential` side cleanly: confirmation requires showing the model treats the construction as *licensing the entailment* "Y moved / the subject caused it," not merely producing fluent continuations.
- It exposes the project's central `constructional`-vs-`distributional` tension (see [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md)): a skeptic can say the model is tracking the high-frequency `V NP PP` skeleton, not the construction's meaning. The non-motion-verb manipulation is the lever that pries those apart, because the verb itself never co-occurs with motion entailments in the distribution.

## Predictions

1. Given an inferential probe ("After 'She sneezed the napkin off the table', did the napkin move? Y/N" and "Did her sneezing cause it? Y/N"), caused-motion items with non-motion verbs yield a high "yes" rate on **both** the motion and the causation questions.
2. Minimal-pair controls that keep the verb but break the construction (*She sneezed near the napkin on the table*; *The napkin was off the table; she sneezed*) yield a substantially lower causation-of-motion "yes" rate.
3. The construction-specific entailment is robust to swapping in novel/low-frequency non-motion verbs (e.g., *She yawned the cat off her lap*), i.e. it generalizes beyond memorized `V NP PP` strings — distinguishing it from an n-gram effect.
4. Panel divergence: the causation entailment is recovered more cleanly in models that also handle the `way`-construction inference, suggesting a shared argument-structure-construction competence rather than item-specific memorization.

## What would confirm / falsify

- **Confirm:** >=70% causation-of-motion "yes" rate for caused-motion items with non-motion verbs, with a >=30pp gap vs. matched non-constructional controls, holding for **held-out / low-frequency verbs** as well as canonical ones, in >=2 of 3 panel models, against a human-rated caused-motion inventory (anchor pending; see below).
- **Weak:** the entailment rate tracks the verb's lexical motion/transitivity relatedness rather than the construction (model reads the verb's frame, not the construction) — or the effect holds only for canonical high-frequency items and collapses on held-out verbs.
- **Falsify:** flat causation-of-motion rate across construction and control; or a rate that tracks the unigram/bigram frequency of the `V NP PP` skeleton alone, with no residual once frequency is matched. A clean null here is a positive result for the `distributional` position and must be written as such.

## Human anchor (pending)

No in-repo resource currently covers the caused-motion construction with item-level human acceptability or entailment ratings. The canonical *inventory* is Goldberg (1995, ch. 7) — descriptive, not rated. A usable empirical anchor would be either (a) an acceptability-rated caused-motion stimulus set, or (b) the caused-motion subset of a broader argument-structure-construction norming study. Until one is in-repo and inspected, this conjecture carries `anchor: pending`.

→ Open decision queued: [`decisions/open/caused-motion-anchor`](../../decisions/open/caused-motion-anchor.md) — which human-anchored caused-motion stimulus set (if any exists and is public) should ground the probe, and what to do if none does (fall back to a verb-frame resource such as PropBank/VerbNet for the non-motion/intransitivity contrast, and queue a wanted-resource request to Tom).

## Notes / caveats

- The path PP can telegraph motion on its own (*off the table* implies a prior location); control by including non-constructional items that contain the same PP without the `V NP PP` frame, so the construction — not the PP — carries the manipulation.
- Probe phrasing matters; trial multiple phrasings **before** seeing results, then commit (charter §8 operationalization gate).
- "Coercion" cases where the verb mildly resists the construction (*She thought the ball into the goal*) are the most diagnostic but also the noisiest; bracket them as a secondary tier, not the confirmation criterion.
- Frequency is the dominant confound and is handled jointly with [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md); lock the frequency-matching procedure before running.
