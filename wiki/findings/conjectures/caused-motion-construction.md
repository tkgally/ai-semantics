---
type: conjecture
id: caused-motion-construction
title: LLMs draw the caused-motion inference from verbs that cannot lexically license it
meaning-senses:
  - constructional
  - inferential
  - distributional
status: tested
contingent-on: []
created: 2026-05-28
updated: 2026-05-29
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
  - rel: supports
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: supports
    target: result/argument-structure-coercion-v2
---

# Conjecture: LLMs draw the caused-motion inference from non-motion verbs

> **Off-ceiling follow-up 2026-05-29** → [`result/argument-structure-coercion-v2`](../results/argument-structure-coercion-v2.md): the v1 ceiling is **cue-sensitive, not a brittle template** — all three models withhold the causation-of-motion inference when an explicit clause denies it (caused-motion `cue` affirm 0–10%, 70–100 pp drop), and they also largely decline cognition-verb (`resist`) coercions (*knew the napkin off the table*, mostly low) — correct anomaly detection. Calibration: only an *explicit* denial was tested; a subtler world-knowledge cue is v2b.

> **Tested 2026-05-29** (workflow mode) → [`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md). The project's own caused-motion minimal pairs were built (frozen pre-run) and the panel run as subjects on both instruments. **Confirmed decisively, at ceiling**: cm affirm-rate 90–100% with a 70–100 pp gap over controls, 3/3 models, both instruments, replicating across 9–10/10 verbs, holding for atypical/low-frequency verbs (P3). The causation-specific control (ctrl-sep: object moves by another cause) is correctly withheld (0–20%), so it is genuine causal attribution, not motion detection. **Lead caveat: ceiling on relatively easy controls is weak evidence for a strong "deep processing" reading** (a harder, coercion-resisting v2 is the natural follow-up). Note the asymmetry with the conative: *adding* a construction-contributed entailment is easy/at-ceiling, while *cancelling* a lexically-default one (conative) was harder and instrument-fragile. Status → `tested` (supported, modest).

## Statement

The English **caused-motion construction** — `Subj V Obj Obl(path/goal)`, as in *She sneezed the napkin off the table*, *He laughed the actor off the stage*, *They prayed the demons out of the house* — is Goldberg's (1995) paradigm case for argument structure being a form–meaning pairing in its own right. The construction means roughly "X causes Y to move along path Z by V-ing," and it contributes a **causation-of-motion entailment** even when the verb (*sneeze*, *laugh*, *pray*) has no lexical argument structure that would license a direct object or an oblique path, and denotes no motion.

The conjecture: current LLMs draw the caused-motion entailment — *Y moved along Z*, and *the subject's V-ing caused it* — from caused-motion instances with non-motion, non-transitive verbs, at a rate that separates the construction from minimally different surface strings in which the same verb appears without the construction.

This is distinct from the `way`-construction conjecture ([`conjecture/way-construction`](way-construction.md)): there the moving entity is the *subject* and the path is reflexive (*his way*); here the moving entity is a *distinct direct object* the subject acts on, and the entailment is **transitive causation**, not self-propelled motion. The two probe different corners of the argument-structure space.

## Why this is interesting

- It is Goldberg's canonical argument that argument-structure meaning is **not** projected from the verb's lexical frame — *sneeze* is intransitive, takes no object and no path, yet the construction coerces both. If an LLM draws the causation-of-motion entailment here, the meaning it is reading cannot be coming from the verb's lexical entry; it must be `constructional`.
- It bites the `inferential` side cleanly: confirmation requires showing the model treats the construction as *licensing the entailment* "Y moved / the subject caused it," not merely producing fluent continuations.
- It exposes the project's central `constructional`-vs-`distributional` tension (see [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md)): a skeptic can say the model is tracking the high-frequency `V NP PP` skeleton, not the construction's meaning. The non-motion-verb manipulation is the lever that pries those apart, because the verb itself never co-occurs with motion entailments in the distribution.

## Predictions

1. Given an inferential probe ("After 'She sneezed the napkin off the table', did the napkin move? Y/N" and "Did her sneezing cause it? Y/N"), caused-motion items with non-motion verbs yield a high "yes" rate on **both** the motion and the causation questions.
2. Minimal-pair controls that keep the verb but break the construction (*She sneezed near the napkin on the table*; *The napkin was off the table; she sneezed*) yield a substantially lower causation-of-motion "yes" rate.
3. The construction-specific entailment is robust to swapping in novel/low-frequency non-motion verbs (e.g., *She yawned the cat off her lap*), i.e. it generalizes beyond memorized `V NP PP` strings — distinguishing it from an n-gram effect.
4. Panel divergence: the causation entailment is recovered more cleanly in models that also handle the `way`-construction inference, suggesting a shared argument-structure-construction competence rather than item-specific memorization.

## What would confirm / falsify

- **Confirm:** >=70% causation-of-motion "yes" rate for caused-motion items with non-motion verbs, with a >=30pp gap vs. matched non-constructional controls, holding for **held-out / low-frequency verbs** as well as canonical ones, in >=2 of 3 panel models, against the ratified human anchor (the Scivetti CxNLI dataset; see below).
- **Weak:** the entailment rate tracks the verb's lexical motion/transitivity relatedness rather than the construction (model reads the verb's frame, not the construction) — or the effect holds only for canonical high-frequency items and collapses on held-out verbs.
- **Falsify:** flat causation-of-motion rate across construction and control; or a rate that tracks the unigram/bigram frequency of the `V NP PP` skeleton alone, with no residual once frequency is matched. A clean null here is a positive result for the `distributional` position and must be written as such.

## Human anchor

Resolved 2026-05-29: the **Scivetti CxNLI dataset** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)) is the ratified human anchor for the caused-motion construction (its caused-motion subset). The canonical descriptive *inventory* remains Goldberg (1995, ch. 7).

Important caveat on what this anchor delivers: the release repo was inspected (de-anonymized at github.com/melissatorgbi/beyond-memorization) and provides a **single gold-standard label per item plus an aggregate ~0.90/0.83 human baseline — an "answer key," NOT a per-item multi-rater gradient.** So it anchors an answer-key comparison, not a graded human-judgment distribution; the confirm criterion is read against that answer key, not against a rater-by-rater acceptability gradient.

→ Anchor decision (ratified 2026-05-29): [`decisions/resolved/caused-motion-anchor`](../../decisions/resolved/caused-motion-anchor.md) — the Scivetti CxNLI caused-motion subset grounds the probe.

## Notes / caveats

- The path PP can telegraph motion on its own (*off the table* implies a prior location); control by including non-constructional items that contain the same PP without the `V NP PP` frame, so the construction — not the PP — carries the manipulation.
- Probe phrasing matters; trial multiple phrasings **before** seeing results, then commit (charter §8 operationalization gate).
- "Coercion" cases where the verb mildly resists the construction (*She thought the ball into the goal*) are the most diagnostic but also the noisiest; bracket them as a secondary tier, not the confirmation criterion.
- Frequency is the dominant confound and is handled jointly with [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md); lock the frequency-matching procedure before running.
