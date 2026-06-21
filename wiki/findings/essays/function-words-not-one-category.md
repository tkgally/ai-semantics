---
type: essay
id: function-words-not-one-category
title: "\"Function words\" is not one inferential category — type-specificity inside a CONFIRM, and what a single inferential instrument can read off a closed-class swap"
meaning-senses:
  - constructional
  - inferential
  - distributional
status: draft
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: refines
    target: conjecture/function-word-substitutability
  - rel: depends-on
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Essay: "function words" is not one inferential category in these models

> **Status: draft (2026-06-21). A philosophical-track essay arguing in the project's own voice.** Its
> original contribution is a single conceptual correction and a calibrated reading of it: **"function
> word" — a part-of-speech / distributional class — is not a natural kind for *inferential* bearing in
> these models.** The project's function-word-vs-content swap result confirmed 3/3 that swapping a function
> word flips 3-way NLI far more than swapping a frequency+length-matched content word, but the per-arm
> breakdown shows the inferential load is **type-specific**, not uniform across closed-class items, and the
> pooled "CONFIRM 3/3" headline rests on **different arms for different models**. The essay reads one
> probe, [`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md), which is
> `internal-contrast-only`: it makes **no human comparison** and the essay smuggles in none. Every
> empirical sentence cites that page at its stated strength and quotes it verbatim. The essay does **not**
> claim the headline is wrong; it refines what the headline can mean. Read the revision triggers before
> citing.

## The occasion

The function-word-substitutability conjecture is the project's most abstract constructional bet:
[`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) predicts
that for matched-frequency minimal pairs, swapping a **function word** "produces a **larger downstream
change in LLM behavior** ... than swapping a content word of comparable surface frequency," on the
intuition that "function words encode constructional/grammatical meaning whose downstream consequences are
systematic; content-word swaps shift topic but often leave inferential structure intact." Its build-v2 run,
[`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md), confirmed the prediction in
all three panel models: "Function-word swaps change the inference vastly more often than frequency+length-
matched content-word swaps, and the **content control behaves exactly as designed** — matched content swaps
almost never flip the label." The per-model contrasts are large and their bootstrap lower bounds clear zero
(claude +0.340, gpt +0.825, gemini +0.859). The headline is true.

But the result itself refuses to let the headline stand alone: "The pooled CONFIRM hides real structure."
This essay is about that structure, and about a conceptual hazard it exposes. The phrase "function word"
names a *distributional / part-of-speech* class — the closed class, opposed to the open content class. The
conjecture's confirm criterion, and the headline that satisfies it, are stated over that class as a whole.
The per-arm table shows the inferential load is not spread over the class at all. It pools onto a subset of
function-word *types*, and which types carry it is not the same across models.

## The structure the pooled number hides

The result reports four function-word arms, and quotes them as a per-arm contrast (flip_fn − flip_ct):

| function arm | claude | gpt | gemini |
|---|---|---|---|
| `because`→`although` (subordinator) | +1.000 | +0.875 | +1.000 |
| `some`→`every` (existential→universal quantifier) | +0.929 | +0.750 | +0.750 |
| `will`→`would` (future→conditional modal) | +0.000 | +0.000 | +0.150 |
| `few`→`many` (paucal→multal quantifier) | +0.095 | +0.960 | +0.960 |

(The contrast values in all four rows are the result's per-arm table verbatim; the parenthetical
grammatical labels are this essay's gloss, not the result's column headers.) Two of the four function-word *types*
carry little-to-no inferential load. The result states this directly for the modal: "`will`→`would` is
essentially null across the panel (claude 0/20, gpt 0/20, gemini 3/20). The modal future→conditional
substitution leaves the NLI relation intact." And it states the split for the paucal/multal quantifier:
"`few`→`many` splits the panel. gpt and gemini flip it near-totally (+0.96), but **claude is near-null
(+0.095)**." So for claude, *two* of four function-word types are near-null; the modal is near-null for all
three.

The conceptual point follows immediately. If "function word" were a natural kind for inferential bearing —
if membership in the closed class were what produced the large flip rate — the four arms would behave alike.
They do not. The asymmetry is, in the result's own words, "carried by a **subset of function-word types** —
robustly the subordinator and the existential/universal quantifier — not uniformly by all closed-class
items." A distributional/part-of-speech category is doing none of the explanatory work at the level of *which
swaps move the inference*. Something finer than "closed class" is selecting the high-load swaps.

## The headline rests on different arms for different models

There is a second, sharper way the pooled number misleads, and it is the reason this essay must be careful
not to read the result as a capability ranking. Because the `few` arm is "**126/206 (61%)** of items, the
pooled contrast is dominated by it." The result spells out the consequence: claude's lower pooled +0.34 "is
**dragged down** by its near-null `few` arm (claude is actually at ceiling on `because`/`some`), while
gpt's/gemini's high pooled ~+0.85 is **lifted** by their near-total `few` flipping. The same 'CONFIRM'
therefore rests on **different arms for different models**." And the result is explicit that this is an
artifact: "The cross-model magnitude spread is an artifact of the `few`-arm split × `few`-arm dominance, not
evidence that claude has a weaker general function-word sensitivity (it does not — see `because`/`some`)."

So three claims hold at once, and only by holding all three together do you read the result honestly: (1)
the conjecture is confirmed in every model; (2) *which* function-word type drives the confirmation differs
by model; (3) the pooled magnitude cannot be read as how strongly a model "treats function words." A single
scalar over the whole closed class — the CONFIRM contrast — is the wrong grain to ask the question at. The
right grain is the arm.

## What this does to prediction 3

The conjecture's third prediction is that "the gap is robust across panel models and across content-word
semantic classes — i.e., it is not driven by a few outlier categories." The result resolves this with a
distinction the prediction did not draw — in its section heading, the gap "holds at the class level, not the
type level." On the content axis: "Every **content semantic class** (adj, noun_person, noun_thing, verb)
shows flip_fn > flip_ct in every model, so the effect is not an artifact of one content category" — that is
prediction 3 as written, and it holds. On the function-word axis, by contrast, "across **function-word
types** the effect is *not* uniform: two of four arms (the modal `will`, and `few` for claude) are
near-null." So the gap *is* driven by a subset of function-word *types*, and prediction 3, read at that
level, fails.

This is not a defeat for the conjecture; it is a sharpening of what it asserts. Prediction 3 was implicitly
read as a uniformity claim over both axes — content classes and function-word types — and the result shows
the two axes behave differently. The content axis is uniform (the gap is not a content-category artifact).
The function-word axis is *not* uniform (the gap is a function-word-type subset). The original argument of
this essay is that this asymmetry between the two axes is exactly what you would expect if "function word"
is the wrong unit of analysis for inferential bearing: a content class is held together by what it does
*distributionally*, but inferential load is held together by something else, which crosscuts the closed
class.

## A calibrated reading: the swap must change a relation the instrument is calibrated to

What distinguishes the high-load types from the low-load ones? Here the essay leaves the result's reported
facts and offers an *interpretation* — a conjecture-level reading, not a claim, that the project's next
probe would test rather than something this run established. Stated as a hypothesis:

> **The function-word effect is mediated by whether the swap changes a relation the inferential instrument
> is calibrated to detect.** The strong swaps alter a **truth-conditional / logical-scope relation** that
> 3-way NLI is built to register: a causal claim versus a concessive one (`because`→`although`), and an
> existential versus a universal quantifier against a universal hypothesis (`some`→`every`) — a textbook
> entailment contrast. The weak swaps shift something the 3-way frame is comparatively *insensitive* to:
> **modal flavor** (`will`→`would`), where the models read the eventuality's occurrence as intact under
> either modal, and a **scalar/pragmatic quantity distinction** (`few`→`many`), whose entailment status
> against "all" turns on whether the model reads the upper-bounding scalar implicature.

The result's own descriptions are consistent with this reading and are the evidence the interpretation
leans on, at the result's stated strength. For the modal: the models read "the council *would* see the
visitor next week" as "still entailing 'the council is going to see the visitor next week,' not as the
irrealis/conditional shift the design predicted." For the quantifier split: claude "assigns the same NLI
label to '*Few* guards saw the men → All of the guards saw the men' and '*Many* guards saw the men → All …'
(it does not treat the paucal/multal contrast as inference-relevant against the universal hypothesis), while
gpt and gemini do." Note that this is exactly a case where the instrument's reading of one scalar relation
*differs by model* — which is why the essay treats `few`→`many` only as the result's reported model-split,
not as a settled mechanism.

If this interpretation is right, then a sizeable part of what looks like "function words carry more
inferential load" is really "the swaps that flip our *one* inferential instrument are the ones that change a
relation that instrument is calibrated to." That is a substantive limit on reading **constructional**
meaning off a single inferential indicator: the indicator's calibration co-determines the result. The modal
swap is a genuine grammatical/constructional change (future→conditional is a real form–meaning shift in the
sense of [`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md)); its near-null
flip rate does not mean the construction carries no constructional load, only that *this* instrument does
not register the load it carries. The essay is explicit that this is interpretation: the run did not
manipulate instrument calibration, so it cannot separate "the type of relation changed" from "the
instrument's sensitivity to that relation." The two revision triggers below are designed to pull them apart.

## This does not undercut the constructional reading — it refines it

It would be a misreading to take type-specificity as eroding the result's support for constructional meaning
over pure distributional meaning. It does the opposite, on the result's own numbers. The matched-frequency
content control is near-floor for *every* arm and *every* model — "Content-swap flip rates are near zero for
every model (1.0% / 4.4% / 3.4%)" and "the falsify arm (content ≥ function) **did not fire** in any model or
any arm." So whatever moves these inferences, it is not matched-frequency distributional neighborhood: a
content swap of equal frequency and length leaves the inference alone. That is the
[`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) null failing to account
for the function-word swaps, exactly as the conjecture's "cleanest possible probe of the `constructional`
vs. `distributional` distinction" intended.

The refinement is to *what the constructional reading can mean*. "Function words carry constructional load"
is true but coarse. The result licenses a finer statement: **closed-class items carry constructional /
inferential load unevenly, and the unevenness is partly about the *type* of grammatical relation the swap
changes and partly about the *instrument's* sensitivity to that relation.** The subordinator and the
existential→universal quantifier carry it robustly and consistently; the future→conditional modal does not
register on this instrument at all; the paucal→multal quantifier registers for two models and not the third.
"Constructional load" is not one quantity attached to a part-of-speech class — it is a relation among a
construction, the inference it licenses, and the instrument used to read that inference.

## What this essay is and is not

- **It is not a model-capability ranking.** The pooled magnitude spread (claude +0.340 vs gpt/gemini ~+0.85)
  is a `few`-arm-weighting artifact, in the result's own words: "The cross-model magnitude spread is an
  artifact of the `few`-arm split × `few`-arm dominance, not evidence that claude has a weaker general
  function-word sensitivity (it does not — see `because`/`some`)." Nothing here ranks the models.
- **It is not a claim that the headline is wrong.** All three models CONFIRM; the content control is
  near-floor; the conjecture is supported. The essay refines what the CONFIRM means, not whether it holds.
- **It is not a mechanistic account of the `few`→`many` split.** The essay stays at the level of the parent
  result's per-arm table (a model-split). A companion within-model result this session,
  [`result/function-word-few-many-split`](../results/function-word-few-many-split.md), *localizes* that split
  — it shows the divergence sits entirely on the "Many X → All X" reading (claude keeps it a contradiction;
  gpt and gemini relax it to neutral) — but it too explicitly disclaims proving *which* reading is correct or
  that any model "computes" a scalar implicature. So the within-model localization is done; the scalar
  *mechanism*, and any human comparison, remain open.
- **It is not a human comparison.** The probe is `internal-contrast-only`; it "makes **no human comparison**
  and needs no human anchor." The essay's original argument is conceptual (about the unit of analysis), so
  it owes no resource anchor; every empirical sentence it leans on cites the within-model result at that
  page's stated strength.

## Revision triggers (read before citing)

- **(a) A widened modal arm.** If a probe widens the modal arm beyond `will`→`would` (e.g.
  `must`/`may`/`can` contrasts, counterfactual *would have*) and the near-null generalizes, the essay's
  "modal flavor is the kind of shift this instrument is insensitive to" reading **strengthens** from a
  one-pair observation to a type-level fact. If instead some modal contrast flips strongly, the reading
  **narrows**: it was idiosyncratic to `will`→`would`, not modal flavor as such, and the type-specificity
  thesis survives but its diagnosis changes.
- **(b) A quantifier-scope / scalar-implicature probe.** The companion result
  [`result/function-word-few-many-split`](../results/function-word-few-many-split.md) has already *localized*
  the split within-model — it sits entirely on the multal-vs-universal ("Many X → All X") reading — but it
  has not established *why* the models diverge there, whether the dividing line is exactly upper-bounding the
  scalar, or which reading is normatively correct (no human anchor). A probe that pins the mechanism (or a
  human anchor that fixes the correct reading) would relocate the split from a localized-but-unexplained
  model difference to a named mechanism, and the calibrated reading in §"A calibrated reading" would be
  confirmed or replaced.
- **(c) A second inferential instrument.** If an indicator *beyond* 3-way NLI (e.g. a graded paraphrase-
  preference, a forced-choice continuation, a scalar-quantity questionnaire) **does** register the modal or
  scalar swaps that NLI leaves near-null, that would relocate the effect from "type of grammatical relation"
  to "instrument sensitivity," vindicating the §"A calibrated reading" caveat that the instrument's
  calibration co-determines the result. This is the single most decisive trigger and the essay's strongest
  reason for hedging the calibrated reading.
- **(d) A source on which closed-class distinctions are truth-conditional.** If an ingested source
  classifies which closed-class distinctions are truth-conditional versus pragmatic/scalar, the high-load /
  low-load split could be predicted *a priori* rather than read off the arms post hoc, which would convert
  the calibrated reading from interpretation toward claim. The essay currently rests on no external
  semantics typology, and that is where it is weakest.

## Honesty box

- The essay's **original** contribution is conceptual: "function word" is a distributional / part-of-speech
  class, not a natural kind for *inferential* bearing in these models; the per-arm structure shows the
  inferential load pooling onto a subset of function-word *types* (robustly the subordinator and the
  existential→universal quantifier), with the pooled CONFIRM resting on different arms for different models;
  prediction 3 therefore holds at the content-class level but fails at the function-word-type level; and the
  high-load / low-load split is *plausibly* mediated by whether the swap changes a relation the single
  inferential instrument is calibrated to detect — an interpretation, not an established result. No
  empirical claim here is new.
- The strongest empirical sentences leaned on, at their stated strength, all from
  [`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md): the per-arm contrasts
  ("`because`→`although`" +1.000/+0.875/+1.000; "`some`→`every`" +0.929/+0.750/+0.750; "`will`→`would`"
  +0.000/+0.000/+0.150; "`few`→`many`" +0.095/+0.960/+0.960); "Function-word swaps change the inference
  vastly more often than frequency+length-matched content-word swaps, and the **content control behaves
  exactly as designed**"; "Content-swap flip rates are near zero for every model (1.0% / 4.4% / 3.4%)" and
  "the falsify arm (content ≥ function) **did not fire** in any model or any arm"; "`will`→`would` is
  essentially null across the panel (claude 0/20, gpt 0/20, gemini 3/20). The modal future→conditional
  substitution leaves the NLI relation intact"; "`few`→`many` splits the panel. gpt and gemini flip it
  near-totally (+0.96), but **claude is near-null (+0.095)**"; the `few` arm is "**126/206 (61%)** of
  items, the pooled contrast is dominated by it"; "The same 'CONFIRM' therefore rests on **different arms
  for different models**"; "The cross-model magnitude spread is an artifact of the `few`-arm split ×
  `few`-arm dominance, not evidence that claude has a weaker general function-word sensitivity (it does not
  — see `because`/`some`)"; the asymmetry is "carried by a **subset of function-word types** ... not
  uniformly by all closed-class items"; and prediction 3 "holds at the class level, not the type level"
  (the content axis uniform — "Every **content semantic class** … shows flip_fn > flip_ct in every model" —
  the function-word axis not — "across **function-word types** the effect is *not* uniform"). The interpretive quotes for the calibrated reading —
  "still entailing 'the council is going to see the visitor next week,' not as the irrealis/conditional
  shift the design predicted" and the claude `few`/`many` same-label description — are used only to
  illustrate an interpretation, never as proof of a mechanism. Nothing here outruns those.
- **No human comparison** is made or owed: the probe read is `internal-contrast-only`, the essay's original
  argument is conceptual (about the correct unit of analysis for inferential bearing), and no sentence
  contrasts the models with humans. The frequency norm the probe matches on,
  [`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md), is mentioned only as the
  probe's matching floor, not as an anchor for any human claim.
- **Provenance note (named weakness).** The high-load / low-load split is read *off the arms* and given a
  truth-conditional-vs-scalar interpretation that rests on no ingested semantics typology — that gap is
  revision trigger (d). The calibrated reading (§"A calibrated reading") is interpretation, not a finding;
  revision triggers (a)–(c) are the experiments that would confirm, narrow, or relocate it.
