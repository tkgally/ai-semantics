---
type: essay
id: point-estimate-is-a-draw
title: The point estimate is a draw — why a single-run accuracy at temperature 0 is not a fixed quantity, and the reading discipline that follows
meaning-senses:
  - model-internal
  - functional-vs-formal
status: revised
contingent-on: []
created: 2026-06-21
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/scivetti-let-alone-powered-rerun-v1
  - rel: depends-on
    target: result/scivetti-let-alone-repeated-runs-v1
  - rel: depends-on
    target: source/he-2025-defeating-nondeterminism
  - rel: refines
    target: essay/concordant-verdict-hides-spread
  - rel: depends-on
    target: essay/capability-split
  - rel: depends-on
    target: essay/witness-seeking-economics
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: depends-on
    target: concept/formal-vs-functional-competence
---

# Essay: the point estimate is a draw

> **Status: revised (2026-06-21, session 65 — trigger (c) discharged; previously revised session 64;
> originally draft, session 63). A philosophical-track / methodological essay arguing in the project's own
> voice.** Its original contribution is a *measurement-epistemics reading discipline*,
> not an empirical claim: a single-run behavioral accuracy at temperature 0 is a **draw**, not a fixed
> quantity, because temperature-0 decoding is **not** deterministic — re-running a byte-identical
> instrument can move the accuracy — so a single-run point estimate carries a **run-to-run jitter** that
> single-run confidence intervals (Wilson, bootstrap) **do not capture and structurally understate**.
> The discipline that follows: a between-X gap (between-model, between-condition, between-item-set)
> **smaller than the run-to-run jitter floor is not yet a finding**; to rest weight on a small effect,
> either the effect must exceed the plausible jitter or the jitter must itself be measured by repeated
> runs. There is **no new empirical claim** here and **no human comparison** — the one quantification
> the essay leans on is a single in-repo measurement, cited at its stated strength, and the asymmetry
> it draws is about how to *read* the project's own model-internal numbers. Read the revision triggers
> before citing — in particular, the ~12% magnitude is **one instrument's** jitter, not a transferable
> constant.

> **Revision (2026-06-21, session 64) — trigger (a) FIRED; scope narrowed and sharpened.** The
> repeated-run measurement trigger (a) named was run:
> [`result/scivetti-let-alone-repeated-runs-v1`](../results/scivetti-let-alone-repeated-runs-v1.md)
> scored the byte-identical instrument **K = 5** times at temperature 0 over the same 63 items. It
> confirms the essay's central premises and **narrows** its scope exactly as trigger (a) prescribed, on
> three points. **(1) The jitter is ceiling-protected.** The comparative-correlative ceiling control did
> **not** jitter (range 0.000 for claude/gemini; 0.033 — one item once — for gpt) while the near-chance
> let-alone swung up to 0.121 — so the headline claim sharpens from "single-run point estimates are
> draws" to "single-run point estimates **on hard, near-chance, functional instruments** are draws,"
> leaving ceilings and clean separations explicitly untouched. **(2) The ~±0.12 is model-specific, not a
> panel constant.** It is confirmed for **gpt** (range 0.121) but claude's range is 0.061 and gemini's
> 0.030 — so trigger (b) (a transferable constant) stays **un-fired**, and the discipline reads "ask
> whether the gap clears the jitter *for this model on this instrument*." **(3) "gemini is deterministic"
> is corrected to "gemini is the *most stable*."** Over five runs gemini churns 2/33 (not zero) — small,
> but non-zero. The discipline itself is **unchanged** (ask whether a gap clears the jitter); what moved
> is the established *prevalence* (large jitter is confined to the small-near-chance cell) plus a worked
> confirmation — the trigger-(d) case — that a real small effect, gpt's below-baseline residual, **survives**
> the jitter (de-noised majority-vote 0.606; every one of five runs < 0.90). The ~±0.12 / ~12% sentences
> below remain accurate as **gpt's** number; read them with the model-specificity this revision adds.

> **Revision (2026-06-21, session 65) — trigger (c) DISCHARGED; the mechanism is now sourced, the
> discipline unchanged.** The temperature-0-nondeterminism source trigger (c) named was fetched and
> catalogued: [`source/he-2025-defeating-nondeterminism`](../../base/sources/he-2025-defeating-nondeterminism.md)
> (He & Thinking Machines Lab 2025, an open-access engineering write-up). It documents *why* greedy
> temperature-0 decoding is not bit-reproducible in served inference: not per-kernel randomness (the
> forward-pass kernels are themselves run-to-run deterministic) but **load-dependent batch-size variation
> interacting with non-batch-invariant kernels** — the same input row reduces in a different order, and so
> to a different rounded logit, depending on the batch it happened to be served in; floating-point
> non-associativity is the ultimate numeric cause. This **grounds the essay's empirical premise** beyond
> the single in-repo behavioral observation: the run-to-run jitter the project measured is an *expected*
> property of hosted API inference, not an artifact of its harness. **What does not change:** the source
> is a *mechanism* characterization for an open-ended-generation setting, so it grounds *that* and *why*
> the jitter occurs — **not** its magnitude on the project's forced-choice instruments (that stays the
> per-instrument K=5 measurement), and it makes **no** claim about the specific panel models' or
> OpenRouter's batching. The reading discipline is untouched; only the premise is now cited rather than
> rested on a single observation. See the trigger (c) entry below, now marked discharged.

## The occasion

The project reports accuracies, shifts, and rates to three decimal places, each wrapped in a Wilson or
bootstrap interval, and the interval is read — reasonably — as "the uncertainty in this number." Until
the 62nd session that reading was safe enough to leave unexamined. Then a powered re-run did something
the project had not deliberately measured before: it ran a **byte-identical** instrument a second time
and compared the two runs item by item.

[`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md)
re-ran the forced-decomposition *let-alone* instrument from session 60 and found that the labels were
**not** reproducible at temperature 0. `claude-sonnet-4.6` — the run's manipulation-check control and a
baseline-matcher — "read **0.708** on the *same* 24 items this run, because 3 of its labels flipped and
**all 3 went the wrong way**"; `gpt-5.4-mini` "likewise flipped 3/24 (its flips happened to cancel);
only gemini was deterministic." The result page draws the moral in one sentence: *"So a single run's
accuracy is a **draw**, and the Wilson CI (which assumes a fixed per-item Bernoulli rate) **understates**
the true across-run uncertainty"* — and it names the consequence: *"the binding precision limit on this
construction is now temp-0 label stochasticity (~12% per run), not item count."*

That is a measurement fact, and it has an epistemic edge the project had not stated on its own terms.
This essay states it.

## The thing a single-run interval hides

A Wilson interval (or a bootstrap CI over items) answers one question: **given this run's per-item
outcomes, how uncertain is the rate they imply?** It models the accuracy as a sample from a fixed
per-item Bernoulli process and reports the sampling error of *that* estimate. It is a faithful answer to
the question it asks. The error is reading it as an answer to a question it never asked: **how much would
this number move if I ran the identical instrument again?**

Those two uncertainties are different objects, and the session-62 data shows they can come apart:

- The **within-run sampling interval** treats each item's label as a fixed draw from a fixed rate. On 24
  items it is wide, but it is computed *as if the labels were settled*.
- The **run-to-run jitter** is the spread of the whole accuracy across repeated, byte-identical runs.
  It exists because temperature-0 decoding is not, in practice, deterministic: the same prompt to the
  same model can yield a different label on a re-run, so the "fixed per-item rate" the CI presupposes is
  itself a draw. On this instrument the jitter ran to *"~±0.12 spread"* for claude and gpt, while
  *"gemini reproduced deterministically (0 flips)"*.

The single-run interval cannot see the jitter, because the jitter is variation *across the very runs the
interval holds fixed*. On the identical 24 test items, one run read **0.833** and the next read **0.708**
— two draws of the same quantity, differing by more than a tenth, from a source no single-run band models.
A within-run interval computed on either run is a faithful summary of *that draw* and silent about the gap
to the other; reading it as "the uncertainty in this number" mistakes the sampling error of one draw for
the spread across draws.

## Why this is a measurement-level cousin of the spread essays, not the same point

The project already has two essays about variation hiding under a tidy label, and it is worth being exact
about how this one differs, because the three are easy to blur.

- [`essay/capability-split`](capability-split.md) is about **between-model** variation at the level of the
  *phenomenon*: when a panel splits, one model's existential must not be averaged into a panel claim.
- [`essay/concordant-verdict-hides-spread`](concordant-verdict-hides-spread.md) is about **between-model
  magnitude** variation at the level of the phenomenon: even a concordant CONFIRM can hide an
  order-of-magnitude spread in *how cleanly* models track the same constraint, and that spread is a real,
  registered finding (decorrelation), not noise.

Both of those are claims about the **world the probe measures** — genuine heterogeneity in what the
models do. This essay is one level down, about the **instrument that measures it**: the jitter is *not* a
fact about the phenomenon, it is a fact about the *reading* of the phenomenon on a given run. The two
spread essays carry their spread because the spread is signal; this essay carries its jitter because the
jitter is **noise that masquerades as signal at small magnitudes**. They are complementary, not
redundant: capability-split asks *across how many models* a verdict holds; concordant-verdict-hides-spread
asks *how much, and how alike*; this essay asks *how much of the reported number would survive a second
identical run*. A finding has to pass all three reads, and they are independent.

The sharpest interaction is with concordant-verdict-hides-spread. That essay's discipline — *carry the
per-model magnitudes, and never read a shared label as a shared degree* — invites a reader to compare
magnitudes like gpt's dative shift of +0.056 against gemini's +0.524. This essay adds the prior question
the comparison presupposes: **is the smaller magnitude bigger than its own run-to-run jitter?** A
between-model gap is only a between-model *finding* if both endpoints would survive a re-run; a gap built
on a +0.056 that might itself be a low or high draw is, until a repeated run is done, a gap the project
cannot yet distinguish from measurement noise. (The dative was a different, larger, graded instrument than
the small near-chance let-alone NLI on which the ~12% was measured, so the project has **no** dative
jitter number; that is exactly the point — the jitter is *unmeasured there*, and a small magnitude with
unmeasured jitter is not yet load-bearing.)

## The reading discipline

> **A single-run point estimate is a draw; report it as one, and do not rest a small effect on a gap
> smaller than its run-to-run jitter.** When a number carries weight, ask whether the claim survives the
> distinction between (a) the within-run sampling interval and (b) the across-run jitter. A between-model,
> between-condition, or between-item-set gap **larger** than the plausible jitter is a candidate finding;
> a gap **comparable to or smaller** than the jitter is **not yet a finding** — it is a draw-sized
> difference, and resolving it requires either an effect that clears the jitter or a repeated-run
> measurement that pins the jitter. Where the jitter is **unmeasured**, a small effect is reported as
> *provisional pending a repeated run*, never as settled. Where re-running the **same** instrument is the
> right move, it is to **characterize the jitter**, not to "firm up" a result — a use sharply distinct
> from the futile re-run [`essay/undischargeable-negative`](undischargeable-negative.md) warns against
> (re-running to establish a universal buys nothing; re-running to *measure the noise floor* buys the
> floor).

That last clause matters, because it threads a needle. The undischargeable-negative essay is right that
"more of the same probe cannot" establish a capability-absence — another failing run adds another
∀-instance, never the universal. But session 62 shows a *different* thing a same-instrument re-run can
buy: not the universal, and not a "firmer" point estimate, but the **measurement-noise floor itself** —
the one quantity that tells you whether your existing point estimates were ever precise enough to carry
the small effects you read off them. Re-running for a *witness* (an easier elicitation) and re-running to
*measure jitter* are both licit; re-running the identical hard instrument hoping the same null "firms up"
is the one move neither essay licenses.

## Where the discipline bites, and where it does not

The bite is **uneven, and that unevenness is the discipline's content** — it is not a blanket "all
numbers are mush."

- **It bites hardest at small effects on hard, functional instruments.** The jitter was measured on a
  *let-alone* 3-way NLI — a single, hard, near-chance construction — and there it ran to ~±0.12, large
  enough to **rival the effect** it was meant to resolve (the result page: *"the run-to-run swing rivals
  the effect"*). This is the
  [`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)
  functional end, where effects are small and gradient and the project's most interesting positives live;
  it is exactly where a draw-sized difference is most tempting to over-read.
- **It barely bites at ceilings and clean separations.** On the *same* run, the comparative-correlative
  ceiling control was *"PRESERVED at 1.000 for all three"* and *"gemini reproduced deterministically"*.
  A model sitting at 1.000, or a separation of many sigma, has little room to jitter; a formal-acceptability
  ceiling where every model sits at the top (the
  [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) regime) is robust
  to this read. So the discipline does **not** retroactively soften the project's large, concordant, or
  ceiling results; it targets the small-and-functional cell where it actually applies.
- **It is model- and instrument-specific.** Within one run, one model (gemini) was deterministic and two
  were not; the magnitude is a property of *this* instrument, not a constant of the panel. The discipline
  is therefore "ask whether the gap clears the jitter *here*," not "subtract 0.12 from every CI."

## What this essay is not

- **Not a new empirical claim.** Its original contribution is the measurement-epistemics reading
  discipline; the one quantification it leans on is the single in-repo session-62 measurement, cited at
  its stated strength. The ~12% is one instrument's jitter, **not** asserted as a general rate.
- **Not a claim that the project's numbers are unreliable.** The reverse: it sharpens *which* numbers
  carry weight (large effects, ceilings, deterministic models) and *which* need a repeated-run check
  (small functional effects on jittery models), and it leaves every large or ceiling result untouched.
- **Not a retraction of any past finding.** No in-repo result is rescinded; the discipline is
  forward-looking, and where it touches a past page (the dative's small gpt magnitude) it adds a
  *provisional-pending-repeated-run* caveat, not a correction — the dative's *direction* and its two large
  shifts are unaffected.
- **Not a human comparison.** The jitter is a model-internal measurement fact; the let-alone residual it
  was found alongside carries its own (inherited) human-baseline caveats on its own page. This essay
  asserts nothing about humans, and the run-to-run-jitter point would, if anything, apply to repeated
  human testing too — but the project does no human testing, so the application is to its own probes only.

## Revision triggers (read before citing)

- **(a) A repeated-run measurement on a non-near-chance instrument.** The trigger-(g) redirect the
  source result names — *"repeated runs / multi-sample"* to pin the let-alone residual's magnitude — is the
  natural next empirical step. If it (or any multi-run probe) shows jitter is **negligible** on
  easier/ceiling instruments and large only near chance, this essay **narrows** from "single-run point
  estimates are draws" to "single-run point estimates *on hard, near-chance, functional instruments* are
  draws," sharpening the bite to the cell where it was measured. The discipline (ask whether the gap
  clears the jitter) is unaffected; only the claimed *prevalence* of large jitter moves.
  **→ FIRED (see the revision block above — 2026-06-21, session 64).**
- **(b) Jitter shown to be a transferable constant.** If repeated runs across several instruments found a
  stable jitter magnitude, the discipline would harden from a qualitative "ask whether the gap clears it"
  into a quantitative correction (inflate small-effect intervals by a measured factor). Nothing in-repo
  licenses that yet; the ~12% is a single instrument's number.
- **(c) A source on temperature-0 nondeterminism. — DISCHARGED (2026-06-21, session 65).** The *mechanism*
  (why temp-0 decoding is not bit-exact) is now ingested in-repo:
  [`source/he-2025-defeating-nondeterminism`](../../base/sources/he-2025-defeating-nondeterminism.md)
  documents it as **load-dependent batch-size variation × non-batch-invariant kernels**, with
  floating-point non-associativity (`(a+b)+c ≠ a+(b+c)`) as the ultimate numeric cause and the
  often-blamed *concurrency* the lesser factor (the forward-pass kernels are themselves run-to-run
  deterministic). The essay now grounds its empirical premise — that temp-0 jitter occurs — on a
  documented general mechanism, not only the single in-repo behavioral observation. The source is a
  *mechanism* account on open-ended generation, so it does **not** transfer the *magnitude* of jitter to
  the project's forced-choice instruments (that remains the K=5 measurement) and asserts nothing about the
  panel's or OpenRouter's batching; the essay claims only "consistent with a documented general mechanism."
  The reading discipline is unaffected by this discharge — it grounds *why*, not *how much*.
- **(d) A jitter-free re-run of a result currently read as small-but-real.** If a small functional effect
  the project rests weight on (e.g. a future small CONFIRM) were re-run and found **stable** across
  repeats, that effect graduates from "provisional pending a repeated run" to a finding that has cleared
  this read — and stands as a worked example that the discipline *passes* results, not only flags them.
  *(The s64 revision block above records gpt's below-baseline residual as a worked confirmation of this
  (d) case; the bet ledger keeps (d) itself open.)*

## Honesty box

- The essay's **original** contribution is the measurement-epistemics reading discipline: a single-run
  temperature-0 point estimate is a **draw**; single-run CIs capture within-run sampling error but
  **structurally miss** across-run jitter; a between-X gap no larger than the jitter is not yet a finding;
  re-running the same instrument is licit to *measure* the jitter, not to firm a result. No empirical claim
  here is new or original.
- The strongest empirical sentences leaned on, at their stated strength, all from
  [`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md):
  claude *"read 0.708 on the same 24 items this run, because 3 of its labels flipped and all 3 went the
  wrong way"*; gpt *"flipped 3/24 (its flips happened to cancel); only gemini was deterministic"*; *"a
  single run's accuracy is a draw, and the Wilson CI (which assumes a fixed per-item Bernoulli rate)
  understates the true across-run uncertainty"*; *"Single-run accuracies on this construction are draws
  with ~±0.12 spread"*; the comparative-correlative control *"PRESERVED at 1.000 for all three"*. Nothing
  here outruns those.
- The ~12% / ~±0.12 magnitude is **one instrument's jitter**, on a hard near-chance let-alone NLI, on one
  date. It is explicitly **not** asserted as a transferable constant or a property of the panel; the
  discipline targets the *small-effect-on-jittery-model* cell and leaves large/ceiling/deterministic
  results untouched.
- **No human comparison** is made or owed: the jitter is a model-internal measurement fact, and the essay
  applies its discipline only to the project's own LLM probes.
- The *mechanism* of temperature-0 nondeterminism is now sourced in-repo (trigger (c) discharged
  2026-06-21): [`source/he-2025-defeating-nondeterminism`](../../base/sources/he-2025-defeating-nondeterminism.md)
  attributes it to load-dependent batch-size variation × non-batch-invariant kernels (FP non-associativity
  the ultimate cause). The essay grounds *that* and *why* the jitter occurs on this source, but the
  *magnitude* on its own instruments rests on the in-repo K=5 measurement, not on the source, and no claim
  is made about the panel's or OpenRouter's specific batching — only "consistent with a documented general
  mechanism."
