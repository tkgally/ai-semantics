---
type: design
id: comparative-correlative-v2
title: comparative-correlative probe v2 — escaping the v1 ceiling (harder covariation, conflicting cues, multi-step chains, distractor controls)
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
  - human-comparison
status: provisional
anchor: resource/scivetti-2025-cxnli-dataset
contingent-on:
  - cc-v2-difficulty-operationalization
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: refines
    target: design/comparative-correlative-v1
  - rel: operationalizes
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v2 — comparative correlative, harder

**Why a v2.** [`result/comparative-correlative-covariation-v1`](../../wiki/findings/results/comparative-correlative-covariation-v1.md) returned a *ceiling* positive: all three panel models cleared T1/T2/T3 and matched the Scivetti human baseline. The result's own lead caveat is that **ceiling on an easy instrument is weak evidence for the strong reading** — a saturated task cannot discriminate "robust constructional competence" from "the task was too easy." v2 exists to find the breaking point, if any: it deliberately raises difficulty along axes a form-only or shallow-pattern reader should fail while a model genuinely deploying the construction's covariation semantics should survive.

This page is a **design**, contingent on a v2-difficulty operationalization gate (below) that must be ratified/frozen before any v2 probe runs. It does not run here; v1 is the run that landed this session.

## 1. What v1 could not distinguish

v1 showed the panel asserts the correct covariation direction for ~100% of clear CC tokens, withholds it for matched non-CC controls, flips on inverse CC, and survives absurd scale pairs. What it leaves open:

- Whether the inference survives when **lexical/world-knowledge cues conflict** with the construction (v1's atypical pairs were *neutral*, not *anti-cued*).
- Whether it survives **multi-step** covariation (chained or composed CCs) rather than a single two-scale step.
- Whether the ~100% reflects covariation *reasoning* or a shallow "the-X-er…the-Y-er ⇒ assert covariation" template match that v1's controls (which removed the template entirely) cannot rule out.
- Whether a **graded** difficulty manipulation produces a *monotone* decline (evidence the model is computing something that can be stressed) vs. a cliff (evidence of a brittle pattern).

## 2. Harder manipulations (each isolates a v1 blind spot)

1. **Conflicting-cue CC (the key manipulation).** Scale pairs where world knowledge suggests one direction but the construction states the other — e.g. inverse-CC over a pair whose plausible real-world covariation is positive (*the more it rained, the less the reservoir filled*). A model using the construction follows the stated direction; a model leaning on plausibility follows world knowledge. This is the sharpest discriminator and the one v1 omitted.
2. **Multi-step / composed covariation.** Two chained CCs (*the more X, the more Y; and the more Y, the less Z*) with a probe about the X→Z relation, requiring composition of two covariation steps. Tests whether covariation is a usable inferential relation, not just a recognised template.
3. **Distractor / embedded CC.** The CC embedded under negation, a modal, a counterfactual, or a reported-speech frame ("She doubted that the harder they came, the harder they fell"), where the bare covariation inference must be adjusted for the embedding operator.
4. **Near-miss form controls (tighten T1).** Controls that are *closer* to the CC than v1's (which removed the template entirely): e.g. single-`the` pseudo-correlatives, `the more X, then Y`, or `as X-er, Y-er` paraphrases — to test whether the panel keys on the precise paired-`the` form or on any vaguely comparative two-clause shape.
5. **Graded difficulty ladder.** Order items by an a-priori difficulty score (steps of composition, cue-conflict strength) fixed before the run, and report the inference rate as a function of difficulty — the shape (monotone decline vs. cliff vs. flat-at-ceiling) is the result.

## 3. Indicator and thresholds — OPERATIONALIZATION GATE (charter §8)

v1's thresholds (T1 ≥30pp, T2 ≥70%, T3 within-15pp) were tuned to a near-ceiling regime and are uninformative if v2 is built to push off ceiling. v2 needs **new, pre-registered** difficulty-sensitive measures, and choosing them after seeing v1's ceiling is exactly the retuning trap. So this design is `contingent-on: cc-v2-difficulty-operationalization` — a decision page the next run must open (provisional default below) and Tom must ratify before v2 runs. The live choices:

- **Conflicting-cue accuracy** — fraction following the *constructional* direction against the world-knowledge cue. Candidate confirm bar: ≥ X% (X to be fixed; the honest expectation is this is where the panel finally drops below ceiling).
- **Composition accuracy** — fraction correct on 2-step chains, vs. a single-step baseline; report the *drop*.
- **Difficulty-curve shape** — pre-commit to what counts as "graceful degradation" (monotone, shallow slope) vs. "brittle" (cliff).
- **Instrument** — keep both NLI + forced-choice (v1 ratified), add a short free-text justification arm ONLY as a qualitative side-channel, not a scored indicator (avoids introducing an un-anchored generation metric).

**Provisional default (not in force until ratified):** confirm = panel stays ≥ 2/3 above a pre-set conflicting-cue bar AND shows monotone (not cliff) degradation on the difficulty ladder; a *cliff* or a *world-knowledge-follows* pattern on conflicting-cue items is the informative **partial-null** that would qualify v1's ceiling as task-easiness rather than robust competence. Write that null as first-class (charter §2.6).

## 4. Human anchor

Same as v1: [`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md) CC subset (answer-key + ≈0.90 aggregate baseline), read in place (no license; not mirrored). **Caveat sharpened for v2:** the Scivetti CC items do not include conflicting-cue or multi-step items, so the human-comparison arm anchors only the items that overlap Scivetti's style; the harder v2 manipulations are *internal* contrasts with **no human norm in-repo** — their human-comparison clause is "no human baseline; pending." Do not state a "below/at human level" claim for the conflicting-cue or composition arms without a fetched human anchor (queue in `wanted.md` if v2 is pursued).

## 5. Panel and cost

Same panel as v1 ([`config/models.md`](../../config/models.md)); same logprob-free greedy-parse instrument (v1 confirmed 0 NA). Cost scales with item count; v1 was $0.12 for 570 calls, so a ~150-item v2 across both framings × 3 models stays well under $1. Pre-flight per [`config/budget.md`](../../config/budget.md) before running.

## 6. What v2 does not do

- Does not revisit v1's settled contrasts (clear-CC vs. removed-template control) — those passed; v2 only adds harder layers.
- Does not introduce a scored free-generation metric (no un-anchored indicator).
- Does not claim a longitudinal comparison to Weissweiler 2022 beyond v1's fenced statement (instruments remain non-interchangeable).

## 7. Handoff hooks

1. Open `wiki/decisions/open/cc-v2-difficulty-operationalization.md` with the §3 choices and the provisional default; do not auto-ratify.
2. Build + freeze a v2 `items.csv` (conflicting-cue, multi-step, embedded, near-miss controls, difficulty score) before any probe call.
3. If pursuing the conflicting-cue / composition human-comparison, queue a human-rated anchor in `wanted.md` first.
4. Mirror the v1 run structure under `experiments/runs/<date>-comparative-correlative-probe-v2/`.
