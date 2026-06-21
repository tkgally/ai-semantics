---
type: result
id: function-word-few-many-split
title: "The few→many panel split is a single quantifier-scalar divergence: all three models read 'Few X → All X' as contradiction; claude keeps 'Many X → All X' contradictory (scalar-bounded 'many'), gpt/gemini relax it to neutral (lower-bounded 'many')"
meaning-senses:
  - inferential
  - constructional
  - model-internal
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: refines
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: conjecture/function-word-substitutability
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: essay/function-words-not-one-category
---

# The few→many split is one quantifier reading: scalar-bounded vs lower-bounded *many*

> **A within-model contrast (`anchor: internal-contrast-only`).** This page refines
> [`result/function-word-swap-run-v2`](function-word-swap-run-v2.md) by localizing the
> mechanism of its `few`→`many` panel split. It makes **no human comparison** and needs no
> human anchor — exactly the ratified posture of the parent run
> ([`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)).
> Its force is a within- and across-model contrast on one quantifier reading, and it asserts
> nothing about which reading is *correct*. **No new model calls, no spend:** this is a
> re-analysis of the raw NLI records the parent run already wrote to
> `experiments/runs/2026-06-21-function-word-vs-content-swap/raw/`. The analysis script is
> `experiments/runs/2026-06-21-function-word-vs-content-swap/few-arm-split.py`; every number
> below was re-derived by that script.

## What the parent run left open

The parent result reported that the `few`→`many` arm (paucal→multal quantifier swap, 126/206 =
61% of items) **splits the panel**: gpt and gemini flip the 3-way NLI label near-totally
(per-arm contrast +0.96), while claude is near-null (+0.095). It noted this drags the *pooled*
cross-model magnitude apart and flagged the mechanism as the thing to make precise. This page is
that mechanism.

## Setup

For each of the 126 `few`-arm items (`arm=="matched"`, `ftype=="few"`):

- **base** = NLI(`premise_base` = "**Few** X …", `hyp_base` = "**All of the** X …")
- **fn** = NLI(`premise_fn` = "**Many** X …", `hyp_base` = "**All of the** X …") — the few→many
  swap, in the premise only.
- `flip_fn` = (fn label ≠ base label).

NLI label encoding (from `probe.py`): **0 = entailment, 1 = neutral, 2 = contradiction**.

## Result: the split is located entirely in the "Many X → All X" reading

Per-model base-label distribution, fn-label distribution, joint base→fn transition counts, and
flip rate, re-derived from raw (`few-arm-split.json`):

| model | n | flip_fn | base (Few → All) | fn (Many → All) | joint transitions (count) |
|-------|---|---------|------------------|-----------------|---------------------------|
| claude | 126 | **0.095** | contradiction 126 | contradiction 114, neutral 12 | con→con 114, con→neu 12 |
| gpt | 126 | **0.968** | contradiction 125, neutral 1 | neutral 123, contradiction 3 | con→neu 122, con→con 3, neu→neu 1 |
| gemini | 126 | **0.960** | contradiction 126 | neutral 121, contradiction 5 | con→neu 121, con→con 5 |

Two facts are exact and unanimous:

1. **All three models read "Few X → All X" as a contradiction** — claude 126/126, gpt 125/126,
   gemini 126/126. The **base is not where the models differ.** A premise asserting *few* of the X
   have the property contradicts the hypothesis that *all* of them do, for every model. The single
   gpt non-contradiction at base is a neutral, and it stays neutral under the swap (the lone
   `neu→neu`), so it is not part of the split.

2. **The entire split is in the "Many X → All X" reading.** claude keeps this a **contradiction**
   in 114/126 ≈ 90% of items (con→con); gpt moves it to **neutral** in 122/126 (con→neu) and
   gemini in 121/126 (con→neu). The flip rate is therefore just the fn-reading divergence: claude
   barely moves off contradiction, gpt/gemini almost always move to neutral.

## The mechanism: scalar-bounded vs lower-bounded *many*

The divergence is a systematic difference in how the models interpret the quantifier *many*
against the universal *all*:

- **claude's labels are consistent with a scalar-bounded reading of *many*.** The pattern is the
  one the upper-bounding scalar implicature "*many*, **but not all**" would produce: "Many X → All
  X" stays a **contradiction** (con→con, 90%), as if *many* and *all* were mutually exclusive
  scale-mates. (The label count shows this *outcome*; it does not by itself prove the model computes
  an implicature — see the disclaimer below.)
- **gpt's and gemini's labels are consistent with a lower-bounded-only reading** — the
  literal/logical "*many*, possibly all". On that reading "Many X → All X" is **neutral**: *many* is
  compatible with *all* but does not entail it, so the premise neither entails nor contradicts the
  universal hypothesis (con→neu, ~96%).

This is a **quantifier-scalar-implicature interpretive divergence**, not noise. It is
concentrated (one quantifier pair), near-deterministic within each model (claude 90% one way,
gpt/gemini ~96% the other), and located on **exactly one reading** — the multal-against-universal
reading — while the paucal-against-universal reading is unanimous across all three.

Scalar implicature (the "some but not all", "many but not all" pattern) is a well-known
phenomenon in the pragmatics literature, **but that observation is not anchored in any in-repo
human resource** and carries no human-comparison force here; it is named only to locate the
divergence conceptually.

## Why the pooled parent number splits

The parent's `few`-arm per-arm contrast is `flip_fn − flip_ct`, and the content control flips at
floor, so the per-arm contrast tracks `flip_fn` almost exactly: claude +0.095, gpt/gemini +0.96.
Because the `few` arm is **61%** of the parent set, this single reading dominates the **pooled**
contrast and pulls the models apart in opposite directions: claude's pooled +0.34 is dragged
**down** by treating the paucal/multal contrast as inference-irrelevant against *all* (both *few*
and *many* contradict *all*), while gpt's/gemini's pooled ~+0.85 is lifted by their multal→neutral
relaxation. The cross-model magnitude spread on the pooled number is therefore an **artifact of
this one quantifier reading × the few-arm's 61% weight** — making precise the parent result's own
caution that the pooled magnitude is not a model-capability ranking. The broader conceptual reading
of this and the other non-uniform arms — that "function word" is not one inferential category — is
developed in [`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md);
this page is the within-model mechanism of the one arm it leans on.

## What this establishes / does not

- **Establishes (within- and across-model, no human comparison):** the `few`→`many` panel split
  reported by the parent run is **not noise and not a general sensitivity difference**. It is a
  single, near-deterministic interpretive divergence on the *many*-against-*all* reading: claude
  reads *many* as scalar-bounded (so "Many X → All X" contradicts, 90%), gpt and gemini read it as
  lower-bounded (so it is neutral, ~96%). The paucal reading ("Few X → All X" contradicts) is
  unanimous.
- **Does not establish:** any human comparison — `internal-contrast-only`, no in-repo human anchor
  for either reading. It asserts **nothing about which reading is correct**: both the
  scalar-pragmatic ("many but not all") and the logical-literal ("many, possibly all") readings of
  *many* are defensible; the finding is only that the models **diverge systematically**. It also
  does not generalize beyond this one quantifier pair — it is the mechanism of one arm, not a claim
  that all function-word effects are scalar.

## Honesty note

- **Magnitude vs jitter.** The parent run and
  [`essay/point-estimate-is-a-draw`](../essays/point-estimate-is-a-draw.md) name ~12% label
  stochasticity at temperature 0. The divergence here — claude ~90% contradiction on the multal
  reading vs gpt/gemini ~96% neutral, a near-complete swap of the dominant label — **vastly
  exceeds** any plausible temp-0 jitter. The few off-diagonal items per model (claude 12, gpt 4,
  gemini 5) are consistent with such jitter; the dominant-label divergence is not attributable to
  it.
- **Single instrument / single norm.** One 3-way NLI instrument at temperature 0; frequency norm
  is SUBTLEX-US `Lg10WF` only ([`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md),
  the frozen set's frequency floor). The `few`-arm items pair the same carriers under *few* vs
  *many*, so the contrast is the quantifier, not the carrier.
- **Re-derivable.** Run `python3 few-arm-split.py` in the run directory; it writes
  `few-arm-split.json` and prints the table above. Every count here matches that output to the
  digit.
