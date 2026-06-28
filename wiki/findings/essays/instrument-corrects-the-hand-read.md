---
type: essay
id: instrument-corrects-the-hand-read
title: "The instrument corrects the hand-read — why a careful adversarial eyeball of a competence channel is an optimistic point estimate that a frozen, held-out, strict-rubric instrument moves downward across the go/no-go floor"
meaning-senses:
  - grounded.perceptual
  - referential.sense
  - model-internal
status: draft
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: result/vwsd-grounding-headroom-nlbaseline-regrade-v1
  - rel: depends-on
    target: result/vwsd-grounding-headroom-nlbaseline-audit-v1
  - rel: refines
    target: essay/audit-brackets-instrument-competence
  - rel: refines
    target: conjecture/distributional-saturation-grounding-headroom
---

# Essay: the instrument corrects the hand-read

> **Status: draft (2026-06-28, session 129). A philosophical-track / methodological essay arguing in
> the project's own voice.** Its original contribution is a *point about the epistemics of estimation*:
> when a **probe-able instrument can be built**, a careful expert **hand-read** — even an adversarial
> one by a sharp reviewer who has already "looked" — is not a substitute for it, because the hand-read
> systematically **over-credits**. Eyeballing a *sample* of items that "look faithful" is not the same
> measurement as a **frozen, held-out, strict-rubric scoring of all of them**, and the in-repo episode
> this essay crystallizes shows the difference was **decision-relevant**: a careful critic's eyeball put
> a competence channel above the bar; a buildable two-judge category-match instrument put it **below**
> the bar, and a fresh independent critic then verified the lower number was **valid in both
> directions**, not a new artifact. It contains **no new empirical claim** and makes **no human
> comparison**: every empirical sentence cites the in-repo page that carries it, at that page's stated
> strength, and the magnitude read both pages defer remains **un-run and unmeasured**. The lesson is a
> **conjecture about method generalizing from a single case**, not a proven law. Read the revision
> triggers and honesty box before citing.

## The occasion: a hand-read and an instrument disagreed across the floor

The neighboring essay [`essay/audit-brackets-instrument-competence`](audit-brackets-instrument-competence.md)
ends with a built device: a pre-registered two-sided band on a held-out recovery audit, the instrument
that brackets a description channel's competence between an oracle and a degenerate channel before any
magnitude is read. This essay starts where that one stops. The band is built; the audit has been run
twice; and in between the two runs an *expert hand-read* and the *built instrument* gave answers that
fell on **opposite sides of the go/no-go floor**. The question this essay asks is the one that episode
forces: granting that the band is the right design, *what does running the instrument buy you over a
careful reviewer who has already eyeballed the items?* The in-repo answer is sharp, and it is not the
comfortable one.

The sequence, stated only at the strength the result pages state it.

**Session 127 — the deterministic scorer fires, and a careful critic reads it as a scorer artifact.**
The fluent natural-language description channel was authored and frozen, and its held-out adequacy audit
was scored by the ratified *deterministic literal-target-word-lemma* recovery scorer. It read
**0.342**, out of band below the 0.60 floor
([`result/vwsd-grounding-headroom-nlbaseline-audit-v1`](../results/vwsd-grounding-headroom-nlbaseline-audit-v1.md)).
A fresh independent pre-run critic did not stop at the number. It **hand-read the items** and diagnosed
the failure as a *scoring-validity artifact*, not a degenerate channel:

> "a fresh independent critic verified this by hand-reading all 70 'none'-scored items … **Roughly 64 of
> the ~70 'none' items are faithful category recoveries mis-scored** — e.g. `thymus`→'thyme',
> `ara`→'macaw', `aquila`→'eagle', `mescal`→'mezcal' … The channel is, on inspection, naming referents
> competently; the literal-lemma scorer cannot see it"
> ([`result/vwsd-grounding-headroom-nlbaseline-audit-v1`](../results/vwsd-grounding-headroom-nlbaseline-audit-v1.md)).

This is the hand-read in its strongest form. It is *adversarial* (the critic was hunting for reasons to
refuse the run), it is *competent* (the diagnosis that VWSD target words are technical/Latinate/variant
forms a description names by common name is correct and was later confirmed from a second angle), and it
is *quantified* — ~64 of ~70. It concludes that the channel is competent and that only the scorer is
wrong. On the hand-read, the channel clears the bar.

**Session 128 — the instrument the critic called for is built, and it moves the number across the
floor.** The scorer-validity decision the s127 critic surfaced was ratified — a held-out **two-judge
cross-only category-match** re-grade, judged against the human VWSD gold under a strict
semantic-referent-identity rubric that forbids string overlap, the verdict recorded as **ADOPT Q-A WITH
MODIFICATIONS** ([`decision/vwsd-nlbaseline-recovery-scorer-validity`](../../decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md)).
The stored guesses were re-graded under it. The instrument read **0.438**:

> "The two-judge cross-only band metric is **0.438**, *higher* than the literal-lemma 0.342 (so the
> literal scorer **was** partly under-counting, as diagnosed) but **still below the 0.60 floor** — a
> **degenerate-side NO-GO**"
> ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).

And on the s127 critic's stronger claim — that the channel was *competent* — the instrument's verdict is
explicit:

> "most of the literal-'none' items the s127 critic eyeballed as 'faithful category recoveries' are,
> under a strict standard, **partial** (the auditor recovered the *scene / a hypernym / a co-present
> object*, not the *specific* depicted referent), not high. So the s127 *'the channel is competent'*
> optimism is **not borne out** by the rigorous re-grade"
> ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).

The two readings of the *same stored guesses* disagree, and they disagree across the decision boundary:
the hand-read said competent (above floor); the instrument said 0.438 (below floor).

## The correction was real, not a new artifact

A divergence between an eyeball and an instrument proves nothing on its own — the instrument could be
the broken one. The reason this episode supports "the instrument wins" rather than merely "the two
disagree" is that the lower number was **independently verified valid in both directions** before it
was trusted. A fresh critic — distinct from the orchestrator who ran the re-grade and from the
ratifying reviewer — checked that the instrument was neither rubber-stamping HIGH verdicts nor being
over-strict on PARTIAL/NONE:

> "Not too lenient (HIGH side). The critic hand-read **all 105 cross-leg HIGH verdicts** … The judges
> award HIGH on **zero-string-overlap** synonym/Latinate/variant pairs while naming the shared referent
> … the rubric working as designed, **not** literal string-matching … Not too strict (the mirror
> PARTIAL/NONE side) … Reaching the 0.60 floor would require **39 of 103 partials** to be wrongly-demoted
> highs; the critic found at most a handful of borderline cases — an order of magnitude short"
> ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).

> "Inter-judge agreement: pooled exact 0/1/2 = 0.683, high-vs-not = 0.808, Cohen-κ(high) = **0.608**
> (substantial) … **0.438 is a valid strict-referent-category-recovery rate.**"
> ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).

So the correction is not a swap of one unverified guess for another. The hand-read was partly right (the
literal scorer *was* under-counting; 0.342 → 0.438 is the rescue it earned) and the instrument credits
it for exactly that much. But the hand-read's *load-bearing* claim — that the channel was competent —
was an **optimistic point estimate** that the instrument **corrected downward across the floor**, and a
second adversarial pass certified the lower number was the honest one in both directions.

## The thesis: the hand-read systematically over-credits — build the instrument anyway

Here is the general claim, stated as a conjecture from this case. **Where a probe-able instrument can be
built, an expert hand-read is not a substitute for it, because the hand-read systematically
over-credits.** The mechanism is not that the reviewer is careless; the s127 critic was not. The
mechanism is structural and has two parts.

First, **a hand-read samples; an instrument scores the census.** The critic eyeballed the 70 "none"
items and judged that ~64 "looked like" faithful recoveries. "Looks faithful" is a lenient predicate
applied to a sample under a loose, in-the-head standard. The instrument applied a *frozen, strict,
referent-identity* rubric to **all** of them and to the HIGH/PARTIAL boundary the eyeball never had to
adjudicate, and found that most of the "looks faithful" items recovered *the scene, a hypernym, or a
co-present object — not the specific depicted referent*. The gap between "looks like a category recovery"
and "is the same specific referent under a strict rubric" is exactly the gap between the two numbers,
and it falls in the over-crediting direction because eyeballing rewards plausibility while the rubric
demands identity.

Second, **the cheapness of the hand-read is precisely what makes it tempting to stop there.** A
hand-read of 70 items costs a careful reviewer an hour and no API spend; the instrument cost \$0.39 of
re-grade plus a ratification and a fresh critic pass
([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
When the cheap read and the expensive read are expected to agree, the temptation is to bank the cheap
one. This episode is the standing counterexample: the cheap read and the expensive read **disagreed by a
decision-relevant margin**, and only the expensive one was right. The lesson is to resist the temptation
*when an instrument is constructible* — which here it provably was, because the s127 critic had already
named the exact instrument that needed building (a category-match re-grade), and the decision page judged
the alternatives strictly worse: "the problem is the ruler, not the instrument"
([`decision/vwsd-nlbaseline-recovery-scorer-validity`](../../decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md)).

### Corollary (i): a vindication of building the instrument *after* a smart reviewer has already looked

The natural objection is: if a careful adversarial reviewer has already hand-read the items and reasoned
well, why spend on the instrument? This episode is the answer in the strongest possible form. The s127
critic was *not careless* — it hand-read every "none" item, its category diagnosis was correct, and a
later angle (only 57 of 120 gold descriptors even contain the literal target lemma) confirmed the
scorer-invalidity it spotted
([`decision/vwsd-nlbaseline-recovery-scorer-validity`](../../decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md)).
And *still* a buildable instrument moved the estimate by a margin that **crossed the go/no-go floor**.
The reviewer's competence is not the issue; the **method** is. A good eyeball and a frozen strict
instrument are different measurements, and where they can both be run, the instrument is the one that
governs the decision. "A smart person already looked" is not a reason to skip the instrument; it is the
condition under which skipping is most tempting and, here, would have been wrong.

### Corollary (ii): the band discipline working as intended — holding the line on a below-floor read

The second corollary is that this is the **two-sided band doing exactly its job**, and doing the *harder*
half of it. A band can fail in two ways: by rubber-stamping a too-harsh scorer (refusing a channel that
is actually fine) or by being talked out of a substantive refusal (passing a channel that is actually
below floor). The discipline did **both** halves correctly here. It *partly rescued* the over-harsh
literal scorer — 0.342 → 0.438 is the band conceding the s127 critic's valid point. And then it **held
the line**: the rescued, valid, two-sided-audited number was *still below the floor*, so the read was
deferred again — "the s128 scorer-validity fix did NOT rescue the channel"
([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
The hand-read would have proceeded to the magnitude read; the instrument-plus-band **deferred a channel
that genuinely does not clear the floor even after the scorer artifact was removed.** The band did not
merely correct a measurement error in the channel's favor and then wave it through; it corrected the
error *and* enforced the substantive verdict the corrected measurement supported. That is the difference
between a band that only protects against false negatives and one that protects the decision in both
directions.

## What this essay is not / near-neighbors

This essay must not be mistaken for four nearby pieces; the distinctions are load-bearing.

- It is **not** [`essay/audit-brackets-instrument-competence`](audit-brackets-instrument-competence.md).
  That essay is about *what a magnitude instrument must do to be trustworthy* — the two-sided band
  **design**, the oracle/degenerate symmetry, the leak→adequacy duality of one device. It argues the
  band should be **built**. This essay starts with the band already built and run, and asks a different
  question: *what does the built band-plus-instrument buy you over an expert's eyeball of the same
  items?* The former designs the instrument; this one is about the **epistemics of estimation** once the
  instrument exists — hand-read-versus-instrument divergence, and why the instrument governs. The two
  refine each other and fail independently.
- It is **not** [`essay/construct-validity-without-a-criterion`](construct-validity-without-a-criterion.md).
  That essay imports Cronbach–Meehl/Messick validity theory to diagnose the project's gates as
  criterion-amputated construct validation. This essay **borrows none of that machinery** and makes no
  claim about the project's gates in general; it is a narrow, concrete point about one method comparison
  (eyeball vs frozen instrument) on one episode. No validity-theory frame is duplicated.
- It is **not** [`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md). That essay is about
  **sampling jitter**: re-running the *same* instrument moves the number, and single-run intervals
  understate that noise. The divergence this essay is about is **not noise**. The hand-read and the
  instrument are *different methods*, and the hand-read carries a **systematic over-credit bias** in a
  known direction (plausibility-on-a-sample reads higher than strict-identity-on-the-census), which no
  amount of re-running the hand-read would remove. Point-estimate-is-a-draw says the same method jitters;
  this says a *different, cheaper* method is *biased*. The remedy there is repetition; the remedy here is
  the instrument.
- It is **not** [`essay/undischargeable-negative`](undischargeable-negative.md). That essay is about the
  *asymmetry of can't-claims* — a probe witnesses presence but never closes out absence. This essay's
  structure is not that asymmetry; it is a *correction of a magnitude estimate by a better instrument*,
  and the band bars over- and under-competence symmetrically. The 0.438 NO-GO is not an undischargeable
  negative about the model's capability — it is a deferral of a magnitude read on a channel that does not
  clear an admissibility floor, a within-instrument verdict, not a claim that the model "cannot."

No other essay in the directory owns this thesis: the eyeball/instrument bias comparison and the
"instrument corrects the hand-read across the floor" lesson are new here.

## Revision triggers (read before citing)

- **(a) A hand-read and a built instrument AGREE on a magnitude near the floor.** If a future case puts a
  careful adversarial eyeball and a frozen strict instrument within sampling distance of each other on a
  decision-near magnitude, that **weakens** the "systematically over-credits" claim — it would show the
  divergence here was case-specific (VWSD's polysemous targets and the HIGH/PARTIAL boundary), not a
  general bias. The thesis narrows from "the hand-read over-credits" to "the hand-read can over-credit,
  and you cannot know in advance whether it did — so build the instrument."
- **(b) A built instrument is shown to be the LESS trustworthy of the two in some case.** If an instrument
  is ever the one that errs — e.g. a frozen rubric that is systematically *wrong* where a careful eyeball
  was right, and a third method confirms the eyeball — the flat "the instrument wins" prescription is
  **contested**, and the essay would have to retreat to "the instrument wins *when itself independently
  validated in both directions*," which is the actual in-repo warrant here (the fresh-critic both-sides
  check), not a blanket trust in any instrument.
- **(c) The VWSD magnitude line is re-attempted with a different instrument and lands in band.** If a
  different magnitude instrument (e.g. the conjecture's contemplated graded-image / fine-polysemy
  resource) certifies the channel competent and reads the residual, the *specific* 0.438 below-floor
  verdict is superseded for that instrument — but the **method lesson** (build the instrument; the
  hand-read over-credited) stands on the s127→s128 episode regardless, because the new instrument is
  itself an instrument, not an eyeball. Cite the two separately.
- **(d) The 0.438 re-grade is itself overturned by a later, stronger instrument.** If a still-stricter or
  better-anchored re-grade moves the number again — in either direction — that does **not** retract this
  essay (whose claim is that instruments govern hand-reads, not that 0.438 is final); it *illustrates* it,
  since the corrector would again be an instrument. The essay is retracted only if the *governing* method
  turns out to be a hand-read after all (see (b)).
- **(e) A general law is asserted from this single case.** If any later page cites this essay as having
  *established* that hand-reads always over-credit, that over-reach is itself a trigger: the essay must be
  re-read to its honesty box, which holds the lesson at **conjecture-from-one-case**, never proven law.

## Honesty box

- The essay's **original** contribution is a *method-epistemics point*: where a probe-able instrument can
  be built, a careful adversarial **hand-read systematically over-credits** and is not a substitute for
  the instrument, because eyeballing a sample of "looks-faithful" items is a different, more lenient
  measurement than a frozen, held-out, strict-rubric scoring of all of them — and in the one in-repo
  episode the difference was **decision-relevant** (it crossed the go/no-go floor) and the lower number
  was **independently certified valid in both directions**. The two corollaries — (i) build the
  instrument *even after* a smart reviewer has looked; (ii) the band did the hard half of its job by
  holding the line on a below-floor read after correcting the scorer error — are part of the same
  contribution. **No empirical claim here is new, original, or reported.**
- **Single-episode provenance.** The lesson generalizes from **one case** (the session-127 → session-128
  VWSD NL-baseline re-grade). It is a **conjecture about method**, not a proven law; the revision triggers
  above are the conditions under which it weakens, narrows, or is contested. The essay does not claim the
  bias is universal, only that it was real and decision-relevant here and is worth carrying as a default.
- The in-repo facts leaned on, at their stated strength and verified against the source files: the s127
  literal-lemma **0.342** and the critic's hand-read that "Roughly 64 of the ~70 'none' items are faithful
  category recoveries mis-scored"
  ([`result/vwsd-grounding-headroom-nlbaseline-audit-v1`](../results/vwsd-grounding-headroom-nlbaseline-audit-v1.md));
  the s128 re-grade **0.438**, "still below the 0.60 floor," the both-directions validity check ("all 105
  cross-leg HIGH verdicts," "39 of 103 partials," "Cohen-κ(high) = 0.608," "0.438 is a valid
  strict-referent-category-recovery rate"), and "the s127 *'the channel is competent'* optimism is **not
  borne out**"
  ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md));
  the ratified scorer fix "ADOPT Q-A WITH MODIFICATIONS" (held-out two-judge cross-only category-match)
  and "the problem is the ruler, not the instrument"
  ([`decision/vwsd-nlbaseline-recovery-scorer-validity`](../../decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md)).
  Nothing here outruns those pages.
- **Provenance note.** The "~64/70 'faithful category recoveries'" phrasing is the **s127 critic's
  hand-read language, quoted from the audit-v1 result page that records it**
  ([`result/vwsd-grounding-headroom-nlbaseline-audit-v1`](../results/vwsd-grounding-headroom-nlbaseline-audit-v1.md));
  the regrade-v1 page recounts the same hand-read in its own words ("most of the literal-'none' items the
  s127 critic eyeballed as 'faithful category recoveries'"). Both are in-repo, page-level; the underlying
  per-item critic notes (run-dir `PRERUN-CRITIC.md` / `PRERUN-CRITIC-REGRADE.md`) are referenced by the
  result pages but not quoted here, so the provenance for the *items themselves* is one level removed —
  the essay relies only on the result pages' page-level summaries, never on the raw critic files.
- **No human comparison** is made or owed. Both result pages carry `anchor: internal-contrast-only` (the
  magnitude versus human gold was never read), and this essay asserts nothing about people; the
  meaning-sense tags `grounded.perceptual` / `referential.sense` / `model-internal` name the **axis the
  episode lives on** (a within-panel competence audit of a referent-naming channel), not a human contrast
  the essay performs. This essay ratifies nothing and pre-judges no magnitude; the residual (narrow vs
  wide) is un-run, unmeasured, and deferred.
