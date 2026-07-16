---
type: note
id: blimp-swap-line-continuation-review-v1
title: "Instrument-line-continuation review of the A3b/C8 BLiMP content-word-swap line — STOP-FOR-NOW-WITH-CONDITIONS (records a governance decision, not a claim): two swap-type arms (s210 SUBTLEX, s235 dual-band C4) reached a twice-controlled STILL-INCONCLUSIVE ceiling, and the decisive point is that NO swap arm can promote R1 — construction-frequency, not lexical identity, is the binding uncontrolled alternative and every swap arm holds the construction fixed — so the proposed third (verb-swap) arm is poor information economics; the line stops until a construction-frequency instrument (a DIFFERENT instrument) becomes available"
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: recorded
anchor: human-anchored
contingent-on: []
created: 2026-07-16
updated: 2026-07-16
links:
  - rel: depends-on
    target: result/blimp-swap-arm-v1
  - rel: depends-on
    target: result/blimp-c4-matched-swap-arm-v1
  - rel: depends-on
    target: result/blimp-profile-frequency-control-covariate-v1
  - rel: depends-on
    target: result/blimp-forced-choice-sweep-v1
  - rel: anchors
    target: resource/blimp
---

# Instrument-line-continuation review — A3b/C8 BLiMP content-word-swap line — **STOP-FOR-NOW-WITH-CONDITIONS**

> **Verdict: STOP-FOR-NOW-WITH-CONDITIONS (2026-07-16, s237).** A cross-session, independent,
> adversarial **instrument-line-continuation review** ([`PROTOCOL.md §3`](../../../PROTOCOL.md),
> the instrument-line-stopping governor) of whether the A3b/C8 BLiMP content-word-swap line —
> which asks whether the panel's human-aligned BLiMP grammatical-difficulty profile (reading **R1**,
> [`result/blimp-forced-choice-sweep-v1`](../results/blimp-forced-choice-sweep-v1.md)) rides on
> genuine grammatical competence versus exact-string / lexical-item memorization or a frequency
> shadow — should **continue** to a **third swap-type arm** (a valence-guarded **verb-swap** arm) or
> **stop** at its current ceiling. Two swap arms have run
> ([`result/blimp-swap-arm-v1`](../results/blimp-swap-arm-v1.md), s210 SUBTLEX-matched →
> SWAP-INCONCLUSIVE; [`result/blimp-c4-matched-swap-arm-v1`](../results/blimp-c4-matched-swap-arm-v1.md),
> s235 dual-band SUBTLEX∧C4-matched → STILL-INCONCLUSIVE), the second closing the first's named
> +0.204 C4 pretraining-frequency confound **by construction** and still returning no clean read — a
> **twice-controlled ceiling**. A verb-swap arm would be the **third swap-type redesign on R1**, which
> is exactly what trips the §3 governor and requires **this** review before any design or run.
>
> **The decision is to STOP the swap line — not forever, and with named reopening conditions.** The
> fresh reviewer holds verdict authority; the non-Anthropic decorrelation vote (`gpt-5.4-mini`,
> **$0.003953**, convergent **STOP-AT-CEILING**) is QA input. The decisive ground is **not** budget-fear
> and **not** the ceiling being logically terminal: it is that **no swap arm can promote R1 to a clean
> human-comparison claim**, because the binding un-addressed alternative to R1 is **construction-frequency**
> — whether the panel is good at a paradigm because that *construction type* is frequent in pretraining —
> and **every** swap arm holds the construction fixed while varying only content words, so it cannot touch
> that channel. A third arm buys tidiness (the one remaining perturbation axis), not the missing control.
>
> **This note carries NO new measurement.** It is a **$0.003953** governance-review record (the only
> spend is the one non-Anthropic decorrelation vote). Per the `note` discipline
> ([`CLAUDE.md`](../../../CLAUDE.md) §Page types) it must **never** be cited as support for any claim; it
> neither strengthens nor weakens the underlying results, which stand exactly as written (both
> `proposed`), and it changes **no** measurement, no essay reading, and no theory-table row. R1 stays
> **descriptive / non-promotable**, unchanged, on its twice-controlled footing.
>
> `anchor: human-anchored` — inherited from the line: R1 is a genuine human-comparison against BLiMP's
> per-paradigm native-speaker agreement ([`resource/blimp`](../../base/resources/blimp.md)). This note
> makes **no new** human comparison; it records a governance decision about the existing one.

## The governor, and why it fired (a note on the trigger)

[`PROTOCOL.md §3`](../../../PROTOCOL.md)'s instrument-stopping rule reads, literally: *"After 3
instrument redesigns yielding nulls on one construct, a further redesign requires a cross-session review
that weighs the line against alternatives … Each redesign may be individually justified; the sequence
needs a governor."* Two honesties about how it applies here, so the record does not overstate its own
warrant:

1. **The trigger is invoked by prudent extension, not by the literal null-count.** The two arms did not
   yield *nulls* — they returned SWAP-INCONCLUSIVE / STILL-INCONCLUSIVE with a **residual directional
   deep-scope drop on 3/3** (CIs exclude 0). A verb-swap arm would be the **third swap-type redesign** on
   one reading (R1); the governor is fired by that sequence, on the rule's own "the sequence needs a
   governor" rationale, not by a literal count of three clean nulls. If anything an
   inconclusive-with-a-residual is *worse* than a clean null for the promotion question, so the by-extension
   invocation is conservative, not a stretch.
2. **The review's job is economics, not a result.** A ceiling is a first-class, non-failure resting state
   (the [`note/genitive-alternation-animacy-promotion-refusal-v1`](genitive-alternation-animacy-promotion-refusal-v1.md)
   discipline, mirrored: a refusal is a first-class outcome). The question is whether spending the next
   ~$1.3–1.6 on this line's third arm beats the alternatives — not whether R1 is "really" competent.

## The twice-controlled ceiling (recap; no numbers change here)

R1 = per-model Spearman of per-paradigm forced-choice accuracy vs BLiMP per-paradigm **human** agreement,
**+0.606 / +0.543 / +0.628** (claude / gpt / gemini), all CIs exclude 0 — the panel is hard where people
are hard. The binding C8 gate makes R1 **non-promotable** until it is shown not to ride on a
training-frequency confound, and requires **both**: a covariate arm (RAN s208 →
[`result/blimp-profile-frequency-control-covariate-v1`](../results/blimp-profile-frequency-control-covariate-v1.md),
**SURVIVES-COVARIATE 3/3**, partial ρ_prof·F +0.572 / +0.510 / +0.606) **and** a content-word **swap**
arm showing SWAP-STABILITY. The swap arm is the outstanding requirement, and it has now run twice:

| arm | match | deep-stratum Δ̄acc (claude / gpt / gemini) | verdict |
|-----|-------|--------------------------------------------|---------|
| s210 | SUBTLEX-US `Lg10WF` ±0.10 | **−0.095 / −0.057 / −0.072**, all CIs excl 0 | SWAP-INCONCLUSIVE — but confounded by a **+0.204** C4 pretraining-freq gap (swap words ~1.6× rarer in pretraining) |
| s235 | **dual-band** SUBTLEX ∧ C4 (closing +0.204 to a set-mean **+0.0106** by construction) | **−0.072 / −0.057 / −0.042**, all CIs excl 0; **0/3** clear the strict whole-CI ≤ −0.05 bar (deep CI-uppers −0.048 / −0.023 / −0.022) | STILL-INCONCLUSIVE |

Closing the C4 channel **attenuated** the s210 deep drop for 2/3 (claude −0.095→−0.072, gemini
−0.072→−0.042; gpt ~unchanged) — so **part** of the s210 drop *was* the C4 confound — but a **residual
survives both frequency proxies on all three**, too small to resolve at this N (0/3 clear the strict bar;
claude's CI-upper misses −0.05 by just **0.002**). And the C4 match is on the **set mean only**, not
word-by-word: the s235 **S6** cancellation flag fired (per-word mean |C4 gap| **0.154**, only 51% within
±0.15, gaps of both signs partly cancelling), so "C4-controlled" is a set-level claim with a per-word
residual of either sign still inside the band. Net: R1's deep-scope alignment being exact-string
memorization vs a per-word frequency residual vs shared grammatical difficulty is **left open at a
measured, twice-controlled ceiling.**

## The decisive point: no swap arm can promote R1

This is why the line stops now rather than paying for the last swap axis. Even the **best case** for a
verb-swap arm — SWAP-STABLE 3/3, the deep profile surviving valence-guarded verb substitution — would
**not** deliver a clean R1 claim, for three compounding reasons:

1. **The construction-frequency channel stays uncontrolled — architecturally, by every swap arm.** A swap
   arm varies content words and **holds the construction fixed**. R1 is profile-alignment: panel
   per-paradigm accuracy tracks human per-paradigm agreement. The live deflationary alternative is that
   *both* track **construction frequency** (frequent construction types are easy for panel and humans
   alike). Swapping nouns, adjectives, or verbs cannot address this. So even a best-case verb-swap leaves
   R1 controlled for surface/lexical frequency (SUBTLEX) and pretraining-proxy frequency (C4, set-mean)
   but **not** construction frequency — a promotion would be to a claim carrying an unaddressed
   construction-frequency confound as a permanent fence, i.e. a weak claim.
2. **A single stable run would not clear §3's replication conjunct anyway.** The genitive-refusal precedent
   is exact and uniform: **REPLICATED ∧ controls-survived**, conjunctive; one met and one absent ⇒ the bar
   is not cleared, and replication is the non-negotiable first conjunct. One verb-swap-stable run is a
   single run — at most a "not yet," needing a fresh-item replication before any claim.
3. **The prior points the wrong way, and a DROP would be interpretively muddy.** Both prior arms found
   deep-scope drops. Verbs carry more of the grammatical load in the scope-deep paradigms (NPI licensing,
   quantifier scope), so a verb swap is *more* aggressive and *less* likely to be stable — and a verb-swap
   DROP is partly confounded by whether the valence-guarded swap subtly broke the grammatical contrast
   itself (the s210 arm already excluded the island-deep pole because a POS-swap can break gap-licensing;
   verbs in NPI/quantifier frames are exactly where that bites).

**Net: R1 stays non-promotable-to-a-clean-claim regardless of the verb-swap outcome.** The best case opens
a gate onto a promotion review that could only produce a construction-frequency-uncontrolled,
replication-owed, heavily-fenced claim; the likely case is a fourth inconclusive. Construction-frequency —
not lexical identity — is the binding uncontrolled alternative, so **paying for the one remaining swap
axis buys tidiness, not the missing control.**

## The economic ranking (marginal use of ~$1.3–1.6)

The verb-swap arm is ~1/3 of the $5.00 UTC daily cap (each prior arm billed ≈$1.31), not "a full day" of
budget — the "full day" framing that surrounds this line reflects the *scheduling* reality (s235 was
deferred three times before a clear day), not the nominal spend. Ranked against alternatives:

1. **Redeploy to a powered magnitude re-run on an already-promoted claim.** Best marginal dollar: the
   claims layer is what compounds. Several direction-only claims (dative, genitive s221, particle-placement
   s229) have their **magnitude** explicitly deferred to a powered re-run; ~$1.3 there buys a real
   strengthening, not a bar-placement tweak.
2. **STOP and bank the budget** — the correct governance call for *this line*, and the honest resting state.
3. **A larger-N dual-band C4 re-run.** Could tip claude's deep CI-upper (−0.048, missing −0.05 by 0.002) to
   a decisive read, but adds **no new perturbation axis** and only resolves a *bar-placement* question on a
   residual already directionally clear (3/3 negative). Low marginal information; defensible only if the
   line continued, which it should not for a 0.002 gain.
4. **The verb-swap arm (the proposal).** New axis, but the best case is both unlikely and insufficient
   (above), a DROP is partly confounded by construction-breakage, and it is the third redesign. Poor
   economics.
5. **The A2b grounding-magnitude image run** — **not purchasable at this price.** Per
   [`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md)
   the magnitude is un-instrumentable with in-repo resources and blocked on an externally-released
   license-checked image-sense set (in-house build barred by the no-human-subjects rule); the only
   available A2b unit is a **$0 license-checked scout**, which does not absorb this budget.

## The decorrelation vote (convergent — recorded)

The non-Anthropic decorrelation vote (`gpt-5.4-mini`, **$0.003953**,
[`VOTE-continuation-s237.json`](../../../experiments/runs/2026-07-16-blimp-swap-line-continuation-review/VOTE-continuation-s237.json))
returned **STOP-AT-CEILING**, independently reaching the two load-bearing conclusions: a third swap arm
ranks **below** all alternatives ("the line's already-established ceiling means the expected value is
low"), and **"no, any swap arm alone cannot promote R1"** because "even a clean verb-swap stability result
would still leave open construction-frequency / residual frequency shadow / shared-difficulty explanations
unless those are separately controlled at the relevant construction level." It also flagged, unprompted,
"some sign of line-holding / result-chasing risk … exactly the kind of inertia the stopping rule is meant
to resist." **Convergence here is signal, not merely comfort** — a fresh Anthropic reviewer and a
non-Anthropic model reached the same operative decision (do not run the third arm) and the same decisive
reason (construction-frequency is untouchable by any swap), from the same verified pages. Verdict authority
rests with the fresh review; the vote is recorded as corroboration. (The fresh reviewer refines the vote's
STOP-AT-CEILING to **STOP-FOR-NOW-WITH-CONDITIONS**: the ceiling is honest but not logically terminal — see
below.)

## The anti-cheat check (one mild flag, cutting toward STOP)

The underlying result pages are scrupulously even-handed (both arms refuse *both* "memorization" and
"stable," and repeatedly under-claim), so there is no sign the review or the reporting angles for a
promotion. The one flag is on the **urge to run the third arm**: its stated justification is that "verbs
are the one remaining perturbation axis" — a **coverage / completionism** motive (tidy up the axis), not
an **information-economics** motive (here is the decision a result would flip). That is precisely the
"busy, not deep / never pad" failure mode [`continue-prompt.md`](../../../continue-prompt.md) §4 and the §3
governor exist to catch: the arm's rationale is the axis's *existence*, not a named decision it resolves,
and (as shown above) it resolves none. So the anti-cheat finding is that the pull to run is **tidiness
dressed as rigor** — and that pull **supports STOP.**

## Conditions that would reopen the line

STOP-FOR-**NOW**, because the ceiling is honest but not logically terminal. Any one of these reopens the
question (and note that the first is a **different instrument**, not a third swap):

1. **A construction-frequency instrument becomes available.** If a per-paradigm **construction**-frequency
   covariate over a real pretraining corpus can be built and R1's profile-alignment survives partialling
   it out, the promotion question genuinely reopens — this is the binding un-addressed alternative, and it
   is *not* a swap arm. (Whether such an instrument is even constructible with in-repo, no-human-subjects
   resources is itself an open scout, not assumed here.)
2. **The goal flips from "promote R1" to "cleanly establish R1 rides on exposure."** A within-model DROP
   becomes decision-relevant only under that different goal; it is **not** the current C8 gate (which asks
   for SWAP-STABLE), so it does not by itself reopen *promotion*.
3. **Tom's standing override, or a change to the C8 gate itself.**

Absent one of these, a verb-swap arm is **not** owed and **not** to be run — running it would be the padded
"busy" move the governor forbids.

## The honest resting statement about R1

R1 — that the BLiMP panel's per-paradigm grammatical-difficulty profile tracks the human profile
(ρ_prof +0.54–0.63) — is a **descriptive, directional, non-swap-stable** reading that **survives two
frequency controls** (human SUBTLEX and a C4 pretraining proxy, on the set mean) yet still shows a residual
deep-scope drop too small to resolve (0/3 clear the strict whole-CI ≤ −0.05 bar), and its promotion to a
human-comparison claim is honestly **not made** and is **not cleanly reachable by any further swap arm**,
because **construction-frequency — not lexical identity — is the binding uncontrolled alternative.**

## Status

`status: recorded`. **STOP-FOR-NOW-WITH-CONDITIONS** — the A3b/C8 BLiMP content-word-swap line is
**stopped at its twice-controlled ceiling** this session; the proposed third (verb-swap) arm is **not**
run and **not** owed until a reopening condition fires. The underlying results are unchanged (both
`proposed`); the [`theory/shadow-depth-table-v4`](../theory/shadow-depth-table-v4.md) form-(iv) row is
**unchanged** (DEPTH-GRADED (R2) load-bearing; PROFILE-ALIGNED (R1) descriptive-only; promotion CLOSED).
`contingent-on: []`. This note carries **no new measurement** and **must not be cited as support for any
claim.**
