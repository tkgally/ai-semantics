---
id: vwsd-nlbaseline-audit-params
title: What are the three deferred numbers of the VWSD NL-baseline adequacy audit — the held-out recovery-scoring rule, the held-out audit model(s) and the coupled author identity, and the two-sided target-band edges — pinned BEFORE authoring so the magnitude read's competence standard is fixed, not tuned?
status: resolved
opened: 2026-06-27
opened-by: autonomous (session 126, surfacing the three operationalization numbers the ratified competence-standard SHAPE explicitly deferred to the run session)
resolved: 2026-06-28
resolved-by: autonomous (adversarial review)
resolution: ADOPT-DEFAULTS as a slate — P1 = Q-P1-A (graded none/partial/high, band metric = high-recovery rate); P2 = author panel.A (claude-sonnet-4.6), held-out auditors panel.B (gpt-5.4-mini) + panel.C (gemini-3.5-flash), band on the two-auditor mean high-recovery; P3 = `[0.60, 0.95]`.
anchor: human-anchored (VWSD gold-test selection accuracy; binary, not graded — scoped to the gating-shape magnitude, NOT prediction-1-as-written, NOT reference)
contingent-artifacts:
  - design/vwsd-grounding-headroom-nlbaseline
contingent-on:
  - []
---

> **Status: RESOLVED (ratified 2026-06-28, session 127, autonomous adversarial review — cross-session; opened session 126, ratified session 127, the boundary held). Verdict: ADOPT-DEFAULTS as a slate.**
> An independent fresh-agent reviewer (not the build/run orchestrator) ratified all three deferred
> numbers as written — **P1 = Q-P1-A** (graded none/partial/high, band metric = high-recovery rate),
> **P2 = author panel.A (claude-sonnet-4.6) + two held-out auditors panel.B + panel.C, band on their
> mean recovery**, **P3 = `[0.60, 0.95]`**. The slate is consistent with the parent's ratified Q1-C
> *shape* and re-opens none of it; it pins only the operationalization figures the parent explicitly
> deferred to the run session. P1 correctly mirrors v2's discriminative high-leak rate (.130) and
> reuses the named in-repo template; P3's lower edge is anchored to that same .130 de-referented floor
> and its upper edge to the symmetric oracle guard, with both edges bracketing *channel competence
> only* and carrying no preference about residual width. P2's addition of the author identity is
> legitimate rather than scope-creep, because "held out from the author" mechanically couples auditor
> and author, and the two-auditor mean is the more robust answer to the parent's single-vs-multiple
> shared-distribution circularity flag at trivial marginal cost. **Anti-cheat PASS** (the most
> tilt-prone scoring option, exact-gold identification, is the one rejected; the reviewer formed no
> preference about the eventual magnitude) and **quote-integrity PASS** against the parent decision,
> the v2 result, the v2 design, and the panel roster. Ratifying fixes the **yardstick** — which
> scoring rule, which auditors/author, which band edges — **never the result**; a held-out recovery
> rate outside `[0.60, 0.95]` remains a pre-run-critic NO-GO that defers and relaxes nothing.
>
> *(Original surfacing note, retained:)* This page pins **no result and no spend**: it proposes
> defaults for the three numbers the ratified competence-standard *shape*
> ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](vwsd-nlbaseline-competence-dv.md),
> ADOPT-DEFAULT Q1-C) explicitly left to the run session, so that those numbers are **fixed before
> the NL descriptions are authored** (the anti-cheat requirement: the band is set before authoring,
> never adjusted to land a narrow-or-wide result), and the run session *ratifies* them by
> independent review rather than *inventing* them under spend pressure.

# Decision: the three deferred numbers of the VWSD NL-baseline adequacy audit

## Why this exists

The competence-standard *shape* for the VWSD natural-language baseline magnitude probe is **already
ratified** — [`decisions/resolved/vwsd-nlbaseline-competence-dv`](vwsd-nlbaseline-competence-dv.md)
adopted **Q1-C** (fresh fluent descriptions under a fixed plain-naming policy **plus** a held-out
adequacy audit with a pre-registered two-sided target band). But that ratification fixed only the
*shape*. It deferred, in writing, **three numeric/identity judgement calls** to the run session
(its Caveats block, verbatim):

> "(i) the numeric **band edges**; (ii) the **held-out audit model** identity — must be held out
> from the *author*, and the run session should weigh whether a single held-out model suffices given
> shared-distribution circularity; (iii) the **recovery-scoring rule** (category-match vs exact-gold;
> v2's graded none/partial/high scheme is a reasonable template)."

These three are an **operationalization gate** ([`CLAUDE.md`](../../../CLAUDE.md) always-on rule 5; charter §8). The
anti-cheat discipline of the parent decision is explicit that the band must be **"fixed before
authoring and read against the audit; it is *never* adjusted to land a narrow-or-wide result"**
(condition (f), verbatim). So they cannot be left to be set *inside* the run session that also
authors the descriptions and reads the rescue rate — that would collapse "set before authoring" into
"set while authoring." Surfacing them now, for cross-session ratification by the run session,
restores the boundary: the run session ratifies a pre-existing proposal (independent adversarial
review), then authors to it. This is the same discipline that governed the parent decision (opened
s122, ratified s123).

**This page does not re-open the shape.** Q1-C is settled. It pins only the three deferred numbers,
each with options, risk flags, and a provisional default.

## The audit instrument (carried verbatim-in-force from v2's Option-C, run in the opposite direction)

The adequacy audit is the **mirror of v2's Option-C leak audit** — the *same held-out
referent-recovery instrument*, pointed the other way. In v2 the worry was that the de-referented
Option-B descriptors still *leaked* the referent (recovery too high = contamination); here the worry
is two-sided (recovery too low = degenerate-weak channel; recovery ≈ perfect = oracle restatement).
The v2 instrument, from [`design/vwsd-grounding-headroom-v2`](../../../experiments/designs/vwsd-grounding-headroom-v2.md)
(§B.4), verbatim:

> "a **held-out referent-name-recovery check** — a fresh model instance (held out from the generator
> … to avoid generator self-consistency), shown **only** the … descriptor with no image and no
> target word, is asked to recover the depicted referent's name/category; … scored on whether/how
> closely it recovers the gold referent (graded: exact category match = high leak, related-but-wrong
> = partial, unrelated = no leak)."

In the actual v2 run that instrument behaved **discriminatively, not degenerately** — from
[`result/vwsd-grounding-headroom-v2`](../../findings/results/vwsd-grounding-headroom-v2.md) (§5),
verbatim: "154 / 20 / 26 → high-leak rate **.130**; Spearman(`leak_i`, `sep_i`) = **.160** over the
120." So the held-out recovery audit is a **working measurement on this exact dataset and panel** (a
graded, non-saturated signal), which is what makes pinning its parameters tractable rather than
speculative.

---

## P1 — the recovery-scoring rule

The held-out model sees **only** the NL description (no image, no target word, no gold), and must
recover the depicted referent. How is "recovery" scored, and what single number does the band
bracket?

- **Q-P1-A — graded none/partial/high, band metric = high-recovery rate.** Reuse v2's graded scheme
  verbatim: each unique candidate image's NL description scored **high** (held-out model recovers the
  exact depicted-referent category), **partial** (related/superordinate but not the specific
  referent), or **none** (unrelated). The **band metric is the high-recovery rate** (fraction scoring
  "high"), the direct analogue of v2's "high-leak rate .130." The full none/partial/high distribution
  is reported alongside. *Risk flags:* (i) a graded human-ish judgement of "exact category match" is
  itself a small operationalization — mitigated by a fixed rubric committed before authoring and by
  reporting the full distribution; (ii) collapsing to fraction-high discards the partial mass —
  mitigated by reporting it.
- **Q-P1-B — mean graded score (high = 1, partial = 0.5, none = 0).** Same graded scheme, but the
  band brackets the **mean** score rather than the fraction-high. *Risk flags:* a single mean blurs
  the oracle/degenerate ends the band is meant to separate (a channel with many partials reads the
  same as one split between high and none); the fraction-high is the cleaner two-sided discriminator.
- **Q-P1-C — exact gold-image identification (recover *which* of the candidate set).** Score recovery
  as whether the held-out model, given the description, can pick the exact gold image from the
  candidate pool. *Risk flags:* this is much closer to the **oracle** failure mode (it rewards a
  description complete enough to single out the gold image — exactly the artifact the upper band
  exists to bar); it conflates "competent description" with "oracle restatement." Least defensible.

**Provisional default: Q-P1-A** — graded none/partial/high, **band metric = high-recovery rate**,
full distribution reported. It is the in-repo template the parent decision named, it produced a
discriminative signal in v2 (154 none / 20 partial / 26 high; high-recovery rate .130), and the
fraction-high is the cleanest
two-sided quantity for the band to bracket.

## P2 — the held-out audit model(s), and the coupled author identity

The audit model "**must be held out from the author**" (parent decision), so the author identity and
the auditor identity are coupled and must be pinned together. Panel (from
[`config/budget.md`](../../../config/budget.md)): **panel.A = claude-sonnet-4.6**, **panel.B =
gpt-5.4-mini**, **panel.C = gemini-3.5-flash**.

- **Author identity.** The parent decision adopted "fresh fluent descriptions" but did **not** name
  the author model (the design's §"new TEXT-NL arm" says the author "is whatever the cross-session
  ratification fixes"). **Provisional default: author = panel.A (claude-sonnet-4.6)** — the strongest
  fluent describer, and deliberately **not** gemini, to avoid re-importing the v1/v2 gemini caption
  lineage that already saturated v1. *Risk flag:* claude also runs the TEXT-NL selection arm over its
  own descriptions (self-selection), a feature carried unchanged from v2's structure (gemini authored,
  all three selected) — it is reported, not removed, and the held-out auditor is never the author.
- **How many held-out auditors.** The parent decision explicitly asks the run session to "weigh
  whether a single held-out model suffices given shared-distribution circularity."
  - *Q-P2-single:* one held-out auditor (panel.B, gpt-5.4-mini), mirroring v2's single held-out gpt
    leak audit. Cheapest, in-repo precedent. *Risk flag:* one held-out model leaves the
    shared-training-distribution circularity (a description an oracle for gpt may not be for gemini)
    unmeasured.
  - *Q-P2-both (default):* **two held-out auditors, panel.B (gpt-5.4-mini) + panel.C
    (gemini-3.5-flash), both held out from the panel.A author**; the band is applied to the **mean
    high-recovery across the two auditors**, with each auditor's recovery reported separately. The
    audit is text-only and tiny (v2 budgeted the leak audit at "≪ $0.1"), so the second auditor is
    near-free and directly narrows the circularity the parent decision flagged. *Risk flag:* a mean
    across two could mask one auditor landing out-of-band — mitigated by reporting both and by a
    pre-run-critic rule that **either** auditor landing above the oracle upper bound is treated as a
    NO-GO signal to scrutinize (the run-session critic's call, not pre-decided here).

**Provisional default: author = panel.A (claude-sonnet-4.6); held-out auditors = panel.B + panel.C
(Q-P2-both), band on the two-auditor mean high-recovery, per-auditor recoveries reported.** It
answers the parent decision's circularity question in the more robust direction at trivial cost.

## P3 — the two-sided band edges

On the held-out **high-recovery rate** (P1 default), a **lower** bound `L` bars a degenerate-weak
channel (artificially WIDE residual — v2's failure re-imported) and an **upper** bound `U` bars an
oracle channel (artificially NARROW residual — the new mirror failure). The channel is certified
competent only if the observed high-recovery rate falls inside `[L, U]`; outside it is a pre-run
critic **NO-GO that defers and relaxes nothing**.

The one in-repo calibration point: the **de-referented** Option-B channel of v2 — built precisely to
*strip* the referent name — still scored **.130** high-recovery. That fixes a floor of reference:
a channel that is *allowed and required to name the referent plainly* must recover the referent far
above the de-referented .130, or it is not actually naming things (degenerate-weak). And a channel
whose held-out recovery is near-perfect is restating the gold so completely it is an oracle.

- **Q-P3-default — `[0.60, 0.95]`.** `L = 0.60`: a competent referent-naming channel must let a
  held-out reader recover the exact referent category for a **clear majority** of items — roughly
  4.6× the de-referented .130 floor, a wide margin above demonstrable incompetence. `U = 0.95`: the
  channel must leave a **non-trivial** fraction (≥ 5%) unrecovered, i.e. it is not a near-perfect
  oracle restatement. *Risk flag:* both edges are judgement calls with no NL-channel data yet (the
  band is necessarily pre-registered before the channel exists — that is the anti-cheat requirement,
  not a defect); too-wide a band admits a near-oracle or near-degenerate channel, too-tight defers
  unnecessarily.
- **Q-P3-tight — `[0.70, 0.90]`.** Stricter on both ends. *Risk flag:* higher chance of an
  unnecessary defer (a genuinely competent channel that happens to land at .92 or .67 is rejected);
  the parent decision treats an over-tight band as the "defers unnecessarily" failure.
- **Q-P3-loose — `[0.50, 0.98]`.** More permissive. *Risk flag:* admits channels close to either
  artifact (a .97-recovery channel is barely distinguishable from an oracle; a .51-recovery channel
  is barely above "half the referents are unrecoverable").

**Provisional default: Q-P3-default `[0.60, 0.95]` on the two-auditor mean high-recovery.** Grounded
on the one available reference point (the de-referented .130 floor) and the symmetric requirement
that a competent channel be neither near-degenerate nor near-oracle. **The ratifying review and the
run-session pre-run critic must scrutinize these edges specifically for result-motivation** — the
edges are set to bracket *channel competence*, and carry **no** preference about whether the residual
the probe then measures reads narrow or wide.

## Honesty note (binds all three)

The band gates the **admissibility of the channel**, never the **residual-width result**. A channel
that lands inside `[L, U]` is certified competent; the magnitude it then yields — narrow residual or
wide residual — is **first-class either way** (write-the-null discipline, parent condition (f)).
Pinning these three numbers fixes the **yardstick, never the result**. None of the proposed defaults
is chosen because it would make the residual read narrow or wide; each is chosen to separate a
competent channel from the two symmetric artifacts (oracle → narrow-by-artifact; degenerate →
wide-by-artifact) as cleanly as the in-repo evidence allows. And the magnitude the probe measures
remains, per the parent decision's load-bearing caveat, **"narrow/wide under this competence
standard, relative to the audited band, on these 120 items," never absolute.**

## Anti-cheat note

Ratifying this decision fixes which scoring rule, which auditors/author, and which band edges — the
**yardstick**. It must **not** be ratified in the session that opened it (s126); the earliest
ratifier is the run session (s127+), by independent adversarial review, and that review must form
**no** preference about whether the residual should read narrow or wide. The band, once ratified, is
**set before the NL descriptions are authored and never re-tuned after the reused IMAGE-arm rescue
rate is read** (parent conditions (b)/(f)). A held-out recovery rate that lands outside `[L, U]` is a
pre-run-critic **NO-GO that defers the run and relaxes nothing** — and may legitimately conclude the
competence standard is un-hittable on VWSD without leaking gold (parent condition (d)). All reuse
stays **verbatim-by-sha** (frozen 120 `7f9e52fa…`, IMAGE `6884eea0…430870`, DISTRACT `f8fbb6be…`);
the draw is **not** re-stratified on `sep_nl_i`; the DISTRACT null is credited first.

## contingent-on

[`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)
**depends on this decision**: its adequacy-audit numbers (scoring rule, auditors/author, band edges)
are fixed only when this resolves cross-session. The design is cleared to be *frozen* under the
parent decision's ratified shape, but the freeze cannot complete — and no spend opens — until these
three numbers are pinned and a fresh independent pre-run critic returns GO against the frozen design
plus the observed `sep_nl_i` + adequacy-audit distributions.
