---
type: result
id: function-word-swap-run-v2
title: "Function-word swaps flip NLI far more than frequency+length-matched content-word swaps (CONFIRM 3/3) — but the effect is non-uniform across function-word types: strong for because→although and some→every, near-null for will→would, and few→many splits the panel"
meaning-senses:
  - constructional
  - distributional
  - inferential
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: supports
    target: conjecture/function-word-substitutability
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: refines
    target: result/function-word-swap-build-v1
---

# Function-word swaps flip NLI far more than matched content-word swaps — CONFIRM 3/3, non-uniformly

> **A within-model contrast (`anchor: internal-contrast-only`, the ratified posture of
> [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)).**
> It compares, *inside each model*, how often swapping a **function word** flips a 3-way NLI
> judgment vs how often swapping a **frequency+length-matched content word** does. It makes **no
> human comparison** and needs no human anchor (a BLiMP/NLI human baseline stays an optional
> Posture-2 upgrade, not in-repo). Run:
> `experiments/runs/2026-06-21-function-word-vs-content-swap/` (build-v2). The set was frozen +
> hashed (file sha `4763740e…`, canonical `1cfb287e…`) and certified `"ok": true` **before any
> model output**, under two independent fresh-agent pre-run critics (the first NO-GO, fixed; the
> second GO). Analysis reproduced from raw by an independent fresh-agent post-run verifier (every
> number to the digit, billed cost confirmed). **Billed: $0.50213** (3 models × 638 calls, 0
> unparsed). This is the first **model** result for
> [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md);
> it follows the build feasibility result
> [`result/function-word-swap-build-v1`](function-word-swap-build-v1.md).

## Design (frozen, ratified)

206 matched minimal-pair items across 4 content semantic classes (adj, noun_person, noun_thing,
verb) and four function-word arms — `because`→`although` (subordinator, n=32), `some`→`every`
(quantifier existential→universal, singular, n=28), `will`→`would` (modal future→conditional,
n=20), `few`→`many` (quantifier paucal→multal, plural, the build-v2 inventory-widening pair,
n=126) — plus a 10-item `the`→`a` function-only characterizing arm. Per item, three 3-way NLI
calls per model (instrument reused verbatim from the CxNLI line): base = (premise_base, hyp_base);
**function swap** in the premise only = (premise_fn, hyp_base); **content swap** applied
consistently in premise AND hypothesis = (premise_ct, hyp_ct). `flip_fn` / `flip_ct` = label
changed vs base. Primary per model: mean(flip_fn) − mean(flip_ct), bootstrap 95% CI (seed
20260621). CONFIRM: contrast > 0 and bootstrap lower bound > 0; panel CONFIRM iff ≥2/3 models and
the ≥200 / ≥4-class count gate is met. Each content swap is matched to its function pair within
**|ΔLg10WF| ≤ 0.10** at both ends and on **signed length** (+1), with every arm's content gap held
**≥** its function gap so no frequency-only or length-only reader can manufacture the asymmetry
(certified max-positive shortcut asymmetry 0.0). Panel: claude-sonnet-4.6, gpt-5.4-mini,
gemini-3.5-flash (gemini `effort: minimal`), temperature 0.

## Headline: CONFIRM 3/3 — but read the arms

The conjecture's confirm criterion (effect size > 0 on ≥200 matched pairs, ≥2/3 models, ≥4 content
classes) is **met by all three models**. Function-word swaps change the inference vastly more often
than frequency+length-matched content-word swaps, and the **content control behaves exactly as
designed** — matched content swaps almost never flip the label.

| model | flip_fn (function) | flip_ct (content) | contrast | bootstrap 95% CI | verdict |
|-------|-----|-----|-----|-----|-----|
| claude | 0.350 | 0.010 | **+0.340** | [0.277, 0.408] | CONFIRM |
| gpt | 0.869 | 0.044 | **+0.825** | [0.767, 0.879] | CONFIRM |
| gemini | 0.893 | 0.034 | **+0.859** | [0.811, 0.903] | CONFIRM |

Content-swap flip rates are near zero for every model (1.0% / 4.4% / 3.4%) — the falsify arm
(content ≥ function) **did not fire** in any model or any arm. So the matched-frequency
distributional control is not what moves these inferences; the function-word swap is.

## The effect is non-uniform across function-word types

The pooled CONFIRM hides real structure. Per-arm contrast (flip_fn − flip_ct):

| function arm (n) | claude | gpt | gemini |
|------------------|--------|-----|--------|
| `because`→`although` (32) | **+1.000** | **+0.875** | **+1.000** |
| `some`→`every` (28) | **+0.929** | **+0.750** | **+0.750** |
| `will`→`would` (20) | +0.000 | +0.000 | +0.150 |
| `few`→`many` (126) | +0.095 | **+0.960** | **+0.960** |

Three facts the pooled number masks:

1. **`because`→`although` and `some`→`every` are strong and panel-consistent.** The causal→concessive
   subordinator swap and the existential→universal quantifier swap flip the inference almost every
   time, in every model. This is the cleanest evidence for the conjecture: closed-class swaps that
   change a grammatical/constructional relation reliably change the entailment, where matched
   content swaps do not.
2. **`will`→`would` is essentially null across the panel** (claude 0/20, gpt 0/20, gemini 3/20).
   The modal future→conditional substitution leaves the NLI relation intact: the models read "the
   council *would* see the visitor next week" as still entailing "the council is going to see the
   visitor next week," not as the irrealis/conditional shift the design predicted. The *weakest*
   function-word effect measured here is a modal one.
3. **`few`→`many` splits the panel.** gpt and gemini flip it near-totally (+0.96), but **claude is
   near-null (+0.095)**: claude assigns the same NLI label to "*Few* guards saw the men → All of
   the guards saw the men" and "*Many* guards saw the men → All …" (it does not treat the
   paucal/multal contrast as inference-relevant against the universal hypothesis), while gpt and
   gemini do.

Because the `few` arm is **126/206 (61%)** of items, the pooled contrast is dominated by it, and
this distorts the cross-model comparison in opposite directions: claude's low pooled +0.34 is
**dragged down** by its near-null `few` arm (claude is actually at ceiling on `because`/`some`),
while gpt's/gemini's high pooled ~+0.85 is **lifted** by their near-total `few` flipping. The same
"CONFIRM" therefore rests on **different arms for different models**. The cross-model magnitude
spread is an artifact of the `few`-arm split × `few`-arm dominance, not evidence that claude has a
weaker general function-word sensitivity (it does not — see `because`/`some`).

## Prediction 3 (not driven by a few categories): holds at the class level, not the type level

Every **content semantic class** (adj, noun_person, noun_thing, verb) shows flip_fn > flip_ct in
every model, so the effect is not an artifact of one content category. But across **function-word
types** the effect is *not* uniform: two of four arms (the modal `will`, and `few` for claude) are
near-null. The honest statement is that the asymmetry is carried by a **subset of function-word
types** — robustly the subordinator and the existential/universal quantifier — not uniformly by all
closed-class items.

## Manipulation check and the determiner arm

Base-label agreement with the predicted base label is high (claude 0.869, gpt 0.908, gemini 0.918),
so the frames are inference-load-bearing as intended. fn-direction agreement (does the function
swap move the label in the *predicted* direction) tracks the arm pattern: gemini 0.801, gpt 0.733,
but claude only 0.330 — claude's low value reflects its near-null `few` and `will` arms, where it
does not move (or does not move as predicted). The `the`→`a` determiner arm (function-only, no
content control) rarely flips "there was a specific, identifiable X": claude 0.0, gpt 0.2, gemini
0.0 — characterizing only, consistent with these models not treating definite→indefinite as an
existence/specificity shift here.

## What this establishes / does not

- **Establishes (within-model):** for these three models, swapping a function word that changes a
  grammatical/constructional relation flips a 3-way NLI judgment far more often than swapping a
  frequency+length-matched content word — CONFIRM in all three, with the matched-content control
  near-floor. The asymmetry is **real and large** for the causal subordinator and the
  existential→universal quantifier, **absent** for the future→conditional modal, and
  **model-dependent** for the paucal→multal quantifier.
- **Does not establish:** any human comparison (`internal-contrast-only`; a BLiMP/NLI human
  baseline is the optional Posture-2 upgrade, still not in-repo). It also does not show the effect
  is uniform across *all* function words — the `will`→`would` null and the `few`→`many` split are
  the principal limits. And the pooled magnitude should not be read as a model-capability ranking:
  it is confounded by the 61% `few`-arm weighting.

## Limitations (honest)

- **Distribution.** The `few` arm is 61% of items; the closed-class arms `because`/`some`/`will`
  rest on a single content out-word each (and `some:noun_person`, `some:verb`, `will:verb` likewise),
  an Option-A supply ceiling under faithful matching reported in `matching-report.json`
  (`single_out_word_classes`). Per-arm reads (above) are the corrective; the pooled number alone
  over- or under-states per model.
- **Two near-null arms.** `will`→`would` (all models) and `few`→`many` (claude) flip little; the
  conjecture is supported by the other arms, and these nulls are themselves findings (modal subtlety
  and a model-specific quantifier-reasoning difference).
- **Single corpus norm / single instrument.** Frequency is SUBTLEX-US `Lg10WF` only; the indicator
  is one NLI instrument at temperature 0 (subject to the ~temp-0 jitter
  [`essay/point-estimate-is-a-draw`](../essays/point-estimate-is-a-draw.md) names, though the
  effect sizes here far exceed any plausible jitter for the strong arms).
- **Methodological lineage.** The build-time defense of this contrast is the worked example of
  [`essay/design-out-not-model-out`](../essays/design-out-not-model-out.md): the length confound was
  designed out (a hard signed-Δlen gate) rather than modelled out, because it is degenerate within
  the function arm.
