---
id: blimp-forced-choice-sweep-design
title: "BLiMP forced-choice sweep (A3b) — the value-laden gates: the paradigm set + depth axis (Q1), the forced-choice elicitation + position-bias control (Q2), and the contamination scope + human-comparison anchor declaration (Q3)"
status: resolved
opened: 2026-07-10
opened-by: session-204
resolved: 2026-07-10
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULTS — Q1-B (depth-stratified subset, realized at freeze as the maximal defensible whole-category rule: every paradigm in the on-axis linguistics_term categories → 40 paradigms, ≥16 floor cleared with margin, ρ_prof genuinely powered at n=40; off-axis categories excluded with structural reasons) / Q2-A (both-orders position-bias-netted 2AFC) / Q3-A (relative profile + depth gradient load-bearing; absolute accuracy an upper bound; HUMAN-COMPARISON anchor via resource/blimp, NOT internal-contrast-only). Ratified s205 by a fresh-agent adversarial reviewer (verdict authority) + a convergent fresh non-Anthropic decorrelation vote (panel.B, $0.0025515). Added binding freeze condition C8: a PROFILE-ALIGNED (reading 1) verdict is NON-PROMOTABLE to a claim without a training-frequency confound control (the F7 content-word-swap arm on ≥2 shallow + ≥2 deep paradigms, OR a pre-registered corpus-frequency covariate partialled from ρ_prof), frozen in PREREG before any model call; absent it, reading 1 runs but is reported descriptively/directionally only. The vote's mechanical anti-cherry-pick sharpening is satisfied by the whole-category selection rule (no within-stratum hand-picking). F1 discharged s204; F2–F7 + C8 bind the freeze."
contingent-artifacts:
  - design/blimp-forced-choice-sweep-v1
---

# Decision: the value-laden gates of the BLiMP forced-choice sweep (A3b)

> **RESOLVED — session 205 (2026-07-10), autonomous cross-session adversarial review.**
> **ADOPT DEFAULTS on all three gates: Q1-B / Q2-A / Q3-A.** A fresh-agent adversarial reviewer (verdict
> authority; independent of the s204 design author) returned **RATIFY-WITH-CONDITIONS**; a **fresh**
> non-Anthropic decorrelation vote (`panel.B` = `gpt-5.4-mini`, $0.0025515) converged per-gate
> (Q1-B / Q2-A / Q3-A). Full record:
> [`REVIEW-ratify-s205.md`](../../../experiments/runs/2026-07-10-blimp-forced-choice-sweep/REVIEW-ratify-s205.md).
> **Added binding condition C8** (frequency-confound → reading 1 non-promotable without a control; see the
> resolution field and the design's freeze conditions). The contingent design
> [`design/blimp-forced-choice-sweep-v1`](../../../experiments/designs/blimp-forced-choice-sweep-v1.md)
> drops `anchor: pending` → the earned `anchors: resource/blimp` human-comparison declaration and clears
> `contingent-on:` at freeze. Tom's standing override outranks. **Ratification fixes the yardstick, never
> the result.**
>
> **Realization of Q1-B at freeze (F6-sharp + the vote's mechanical anti-cherry-pick rule).** Rather than
> hand-pick ~16 paradigms, the freeze takes the maximal defensible subset: **every paradigm in the
> on-axis `linguistics_term` categories** (determiner–noun agreement; the local + distractor split of
> subject–verb agreement; NPI licensing; quantifiers; island effects; filler-gap dependency) → **40
> paradigms**, with off-axis categories (binding, anaphor agreement, argument structure, s-selection,
> control/raising, irregular forms, ellipsis) excluded for stated structural reasons. This removes
> within-stratum curation DoF entirely and makes ρ_prof genuinely powered (n=40).

This probe compares the panel's **behavioral forced-choice accuracy** on a selected set of BLiMP
minimal-pair paradigms against BLiMP's **per-paradigm human agreement** (the load-bearing human anchor,
now **committed in-repo** — `experiments/data/blimp/human_validation_summary.csv`, sha256 `ea0e7c21…`;
the per-paradigm profile catalogued in [`resource/blimp`](../../base/resources/blimp.md), discharging
the s204 critic's Blocker 1 / F1 this session). Three choices are value-laden and must be fixed by a
later session before the freeze. **The s204 pre-run critic (verdict authority) returned
GO-WITH-CONDITIONS with the freeze conditions F1–F7 recorded on the design; F1 is discharged, F2–F7
bind the freeze.**

## Q1 — the paradigm set + the depth axis

**The paradigm set is the instrument.** A depth-stratified subset makes the two readings (profile
alignment vs the human difficulty profile; within-panel depth gradient) sharp, but invites a curation
objection; the full sweep removes the objection at the cost of focus and spend.

- **Q1-A — AANN-adjacent agreement family only.** Tightest program link; **no depth spread** (all
  human-easy local agreement), so neither reading is testable. Rejected in the design.
- **Q1-B (provisional default) — a depth-stratified set across four strata** (shallow-local
  determiner–noun / regular subject–verb agreement; medium distractor agreement; deep-scope NPI /
  quantifier; deep-structural islands / long-distance), each with a published per-paradigm human
  agreement; includes the AANN-adjacent family. **Binding conditions (from the s204 critic):** (i) the
  set is frozen at **≥16 paradigms** (F2) — the ~9–12 first draft is under-powered for reading 1's
  per-model Spearman (at n≈10 a ρ of +0.4 is indistinguishable from 0); if n stays low, reading 1 is
  descriptive-only and non-promotable on the run alone; (ii) the exact final list **and** the stratum
  assignment are frozen in PREREG **before any model call** by a written locality rule that references
  **only structural/syntactic criteria, independent of the human-agreement values** (F6, the vote's
  load-bearing condition), and the excluded paradigms are published with reasons; (iii) the subset is
  reported as selected, not exhaustive.
- **Q1-C — the full 67-paradigm sweep.** Supports a genuine "BLiMP overall" score and removes the
  curation objection, but ~5.6× the calls, dilutes the depth focus with off-theme categories, and pushes
  cost toward the prefer-split flag. A reviewer who judges the curated subset too fishing-prone may
  prefer this.

**Why value-laden:** curation power vs curation-objection-and-cost. The reviewer weighs whether the
pre-committed locality rule + honest "selected subset" framing suffices to defend Q1-B, or whether the
depth reading needs the full sweep.

## Q2 — forced-choice elicitation + position-bias control

The closed panel is logprob-free, so BLiMP's original probability-comparison scoring is unavailable; the
behavioral analog is a 2AFC whose known artifact is position bias.

- **Q2-A (provisional default) — behavioral 2AFC, BOTH presentation orders per item, position-bias
  netted** (order-averaged accuracy primary + consistency accuracy robustness + order-flip diagnostic).
  Pays 2× calls to net out a known 2AFC artifact that would otherwise confound the per-paradigm profile.
- **Q2-B — single fixed-random order per item** (half the calls; uncontrolled position bias). Rejected
  as default.
- **Q2-C — isolated absolute acceptability rating** (discards the minimal-pair contrast; noisier).
  Rejected.

**Why value-laden:** the format fixes what "accuracy" means and whether a known artifact confounds the
headline. The 2× cost of Q2-A vs Q2-B is the trade.

## Q3 — contamination scope + the anchor declaration

BLiMP is synthetic, published 2019, and very widely trained on; absolute accuracy is a contamination
upper bound.

- **Q3-A (provisional default) — the load-bearing findings are RELATIVE (the across-paradigm profile
  alignment + the within-panel depth gradient); absolute accuracy is reported as an upper bound; the
  anchor is HUMAN-COMPARISON via [`resource/blimp`](../../base/resources/blimp.md)'s per-paradigm human
  agreement.** Memorization inflates absolute accuracy roughly uniformly, so the relative difficulty
  profile is robust where absolutes are not. The result page carries an `anchors:` link to
  [`resource/blimp`](../../base/resources/blimp.md) — it is **not** `internal-contrast-only`. **This is the distinguishing feature of the
  unit: a genuine human-anchored line, not a within-model contrast.**
- **Q3-B — add a lexical-perturbation contamination control** (novel content-word re-instantiation,
  original-vs-perturbed accuracy). Stronger, but risks breaking template grammaticality and adds build
  cost; weighed as a v2 upgrade or a bounded content-word-swap arm.
- **Q3-C — decline the unit as contamination-uninterpretable.** Rejected as over-cautious; forfeits the
  program's one in-hand human-anchored grammatical line.

**Why value-laden:** whether to anchor a human-comparison profile claim despite contamination (Q3-A),
invest in a perturbation control (Q3-B), or decline (Q3-C). **Binding caution for the eventual result
page** (not the gate): absolute per-paradigm accuracies stay flagged as upper bounds; the human-comparison
claim rides on the *relative* profile Spearman, never on "the panel matches the 96.4% human ceiling."

## What a ratification must do

1. Fix Q1 / Q2 / Q3 (adopt the defaults or a named alternative), with a fresh-agent adversarial reviewer
   (verdict authority) + one **fresh** non-Anthropic decorrelation vote (`panel.B` or `.C`, cutoff-aware
   preamble; PROTOCOL §2). Record convergence/divergence in writing.
2. On adoption: move this page to `wiki/decisions/resolved/` with the date + `resolved-by: autonomous
   (adversarial review)` + rationale; the design drops `anchor: pending` → the human-comparison `anchors:
   resource/blimp` declaration and clears `contingent-on:` at freeze.
3. Note any added freeze conditions (as the adjective-antonymy ratification added its C8).
