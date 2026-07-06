---
type: open-question
id: graded-privativity-gradient
title: "Is the panel's privativity gradient (fake gun suppresses the category entailment, toy violin does not, plastic apple borderline) a stable graded structure — and can it be anchored to a human privativity/typicality signal?"
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: open
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: depends-on
    target: result/monotonicity-c2-battery-v1
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: open-question/monotonicity-human-comparison-leg
---

# Open question: is the panel's privativity gradient a stable graded structure, and is it anchorable?

> **Why this page exists (a $0 scoping artifact).** The C2 matched monotonicity battery
> ([`result/monotonicity-c2-battery-v1`](../results/monotonicity-c2-battery-v1.md)) was built to test the
> add/cancel *asymmetry*, but it left a sharp, unremarked-on by-product: a **reproducible per-item
> gradient in how strongly a privative modifier cancels a noun's category entailment**. That gradient —
> not the asymmetry — is the object here. This page opens it as a distinct question: it states the
> gradient, says why a *graded* privativity is interesting for constructional/lexical meaning, sketches —
> **does not run** — a widened privativity probe, and flags its human-anchor status honestly. It opens no
> spend and commits nothing.

## The observed gradient (verbatim from the C2 battery)

The C2 cancel arm placed 8 noun→category pairs under privative modifiers (*"Sam bought a fake gun"* →
does it still entail "a weapon"?). The panel does **not** treat privative modification as a uniform
switch. From the result's per-item suppression map
([`result/monotonicity-c2-battery-v1`](../results/monotonicity-c2-battery-v1.md), NLI primary):

| privative item | claude | gpt | gemini | suppresses the category entailment? |
|---|---|---|---|---|
| *fake* gun, *fake* diamond, *artificial* rose, *imitation* pearl, *toy* sword | 1/2 | 1 | 1/2 | **clean, 3/3** |
| *toy* tiger | 2 | 0 | 1 | mixed (gpt fails) |
| *plastic* apple | 0 | 0 | 1 | weak (claude + gpt fail) |
| *toy* violin | 0 | 0 | 0 | **fails 3/3** (weakest) |

The pre-run critic flagged *toy violin* and *plastic apple* as the weakest-suppression items **in
advance**, and the result page reads the pattern as principled, not random: "a toy violin is arguably
still a playable musical instrument, a plastic apple borderline." So the model's *"fake N ⊨ not (a real)
N"* behaviour is **graded by the modifier × noun pair** — some privatives cancel the category
membership cleanly, others leave it largely intact.

## The question, sharply

> Is this graded privativity a **stable, structured property** — does the panel's per-cell suppression
> rate reproduce a graded ordering of privative strength (strong privatives such as *counterfeit / fake /
> imitation* cancelling the category entailment more reliably than weak ones such as *toy / model /
> plastic*), monotone rather than flat and rather than item-random? And can that model gradient be
> **anchored** to a human privativity / typicality signal (do humans grade "is a *fake* N still an N?"
> the same way), or is the human leg un-instrumentable on current resources, leaving the gradient a
> within-model contrast?

## Why it matters for constructional / lexical meaning

Privative adjectives are a classic lexical-semantics puzzle: a *fake gun* is not a (real) gun, a *toy
gun* arguably still is a kind of gun, a *plastic apple* is borderline — whether the noun's category
entailment survives adjectival modification is **graded and modifier-dependent**, not a clean privative
switch. This is a form–meaning composition question (`constructional`: the adjective–noun pairing) about
an `inferential` property (the category entailment the composition does or does not cancel), exactly the
add/cancel register [`concept/coercion`](../../base/concepts/coercion.md) frames and
[`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) grounds. If the model's
privativity is genuinely *graded* — and tracks the graded privativity humans exhibit — that is a
within-composition analogue of the graded sense-relatedness the project found at the lexical level: a
model treating a categorical-looking operation (cancel the category) as a **typicality-sensitive
gradient**. If instead the gradient is item-noise, the C2 confirm's known fragility (its 2/3 verdict
rests on the two weakest items counting as genuine suppression-failures) is the more honest reading.

## What a serious answer would look like (probe sketched, NOT run)

Reuse the C2 paradigm and **widen the privative set** into a designed gradient:

1. **Cross more privative modifiers** — *counterfeit, fake, imitation, artificial, simulated, toy, model,
   plastic, fictional, former, would-be* — against **more nouns** spanning the plausible privativity
   range, so each cell is a (modifier × noun) privativity strength.
2. **Read the suppression rate as a gradient.** The within-model signature of *graded* privativity is a
   suppression rate **monotone in an a-priori privative-strength ordering** (frozen before data), not
   flat (uniform switch) and not item-random (noise). The panel's per-cell rate is the dependent variable.
3. **Keep both instruments** (NLI + forced-choice) — the C2 battery already showed the cancel arm is the
   instrument-fragile one, so the gradient's instrument-stability is itself informative.

The null is first-class: a **flat or item-random** suppression profile (no stable privative-strength
ordering) would say the model has no graded privativity, only a noisy switch — a clean negative, written
as such, and one that would further temper the C2 confirm.

## Human-anchor status (honest): scout-gated, else `internal-contrast-only`

This is the load-bearing difficulty, and it must not be waved away. The C2 battery itself is
`anchor: internal-contrast-only` — a within-model contrast with no human baseline. There is **no in-repo
human privativity or typicality norm**, and the parallel scoping already done for the monotonicity line
is discouraging: [`open-question/monotonicity-human-comparison-leg`](monotonicity-human-comparison-leg.md)
found the add/cancel *asymmetry's* human leg **un-instrumentable on the project's held resources**
(single binary gold, no graded robustness signal, and the project's actual cancel arms — including
privative modifiers — absent from the one anchored inventory). A *privativity-gradient* anchor is a
narrower want than that page's, but it is still absent in-repo. So the honest paths, inventing no anchor:

- **A within-model `internal-contrast-only` contrast** — the panel's suppression gradient read against a
  **frozen a-priori privative-strength ordering** (not a human resource), a within-model structural
  claim with no human comparison. Needs no fetch.
- **A human-comparison arm**, gated on **scouting** an externally-released human signal of graded
  privativity / typicality (e.g. human "is a *fake* N still an N?" acceptability, or a typicality norm
  over modifier × noun pairs) and cataloguing it as a `resource`. None is in-repo; none is invented here.
  Absent such a scout, the `human-comparison` tag marks the arm the *question* engages, not an anchor in
  hand — and the honest default, per the sibling scoping page, is that this arm may prove
  un-instrumentable on current resources.

## Tractability and cost

High for the within-model arm. It reuses the frozen C2 paradigm and material; widening the modifier ×
noun set is cheap to author; a powered internal-contrast run on the panel is low-cost at observed prices.
The human-comparison arm is the only gated prerequisite, and it is a *scout*, not a run. Small-N, single
run, n=3-models, direction-of-effect caveats apply as everywhere.

## How this differs from the existing monotonicity pages (so it is genuinely fresh)

- **Distinct from [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
  and its battery.** Those ask about the *relative reliability of adding vs cancelling* an entailment;
  this asks about the **internal structure of the cancel-side privativity gradient itself** — is the
  cancel operation graded, and how.
- **Distinct from [`open-question/monotonicity-human-comparison-leg`](monotonicity-human-comparison-leg.md).**
  That asks whether the add/cancel *gap* can get a human leg (verdict: un-instrumentable on held
  resources). This asks a *different* object — whether the privativity gradient is a stable structure and
  whether *its* human leg (typicality) is scoutable — and inherits, rather than restates, that page's
  anchor-scepticism.
- It is `model-internal` plus (on the scouted arm) `human-comparison`; it does **not** touch the
  relational axis.

## Status: open (scoping only)

This page runs nothing, freezes no operationalization, opens no `wiki/decisions/open/` entry, and spends
nothing. It lifts the reproducible privativity gradient out of
[`result/monotonicity-c2-battery-v1`](../results/monotonicity-c2-battery-v1.md), states it as a distinct
question about graded constructional/lexical meaning, sketches a widened within-model probe with a frozen
privative-strength ordering, and flags the human-comparison (typicality) arm as scout-gated and likely
un-instrumentable on current resources — else `internal-contrast-only`.
