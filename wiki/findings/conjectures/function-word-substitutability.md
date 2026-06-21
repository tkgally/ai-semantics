---
type: conjecture
id: function-word-substitutability
title: Function-word swaps produce sharper meaning shifts than matched content-word swaps in LLM behavior
meaning-senses:
  - constructional
  - distributional
  - inferential
status: designed
contingent-on: []
created: 2026-05-28
updated: 2026-06-21
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: resource/subtlex-us-frequency
---

# Conjecture: function-word swaps produce sharper meaning shifts than content-word swaps

## Statement

For matched-frequency minimal pairs, swapping a **function word** (e.g., *the* → *a*; *will* → *would*; *because* → *although*; *some* → *every*) produces a **larger downstream change in LLM behavior** (entailment, paraphrase preference, continuation distribution) than swapping a content word of comparable surface frequency. The intuition: function words encode constructional/grammatical meaning whose downstream consequences are systematic; content-word swaps shift topic but often leave inferential structure intact.

## Why this is interesting

- Function words are exactly where lexicography is historically thinnest and meaning-theory is most underdeveloped — yet they carry the constructional load.
- The frequency-controlled comparison is the cleanest possible probe of the `constructional` vs. `distributional` distinction: the distributional theory predicts comparable behavior shifts for comparable frequency; a substantially larger shift on function-word swaps is evidence for constructional meaning being computed beyond surface co-occurrence.
- It is the most *general* of the project's constructional conjectures — any LLM, any matched corpus, any inferential probe; the conjecture survives or fails across many specific stimulus sets.

## Predictions

> **Revision 2026-06-21 (session 66, M1 of the ratified [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)).**
> Prediction 1 was written around a continuation-distribution **KL** instrument, which is
> **dead on the panel** (OpenRouter exposes no prompt/echo-logprobs —
> [`decisions/resolved/aann-panel-logprob-blocker`](../../decisions/resolved/aann-panel-logprob-blocker.md)).
> It is re-mapped below to the **behavioral divergence proxy** that stands in for it, and is
> demoted to **secondary / characterizing-only** (it may describe but never *decide* a result).
> The **primary** confirm/weak/falsify-bearing prediction is now prediction 2 (entailment-flip /
> forced-choice rate). Original wording preserved for the record: *"KL divergence (or similar)
> on continuation distributions is larger after function-word swaps than after frequency-matched
> content-word swaps."*

1. *(secondary, characterizing-only)* A **behavioral continuation-divergence proxy** — e.g.
   sampled-continuation disagreement or paraphrase-preference shift at fixed temperature — is
   larger after function-word swaps than after frequency-matched content-word swaps. This is a
   noisy, tunable surrogate for the unavailable continuation-distribution KL; it may
   *characterize* a result but may never on its own confirm or falsify the conjecture.
2. *(primary)* **Entailment / inference behavior flips more often** after function-word swaps
   than after frequency-matched content-word swaps, measured as the entailment-flip / graded
   forced-choice rate (the sole confirm/weak/falsify-bearing indicator), behind a binding
   manipulation-check that the judgment moves *because the inferential relation changed*.
3. The gap is robust across panel models and across content-word semantic classes — i.e., it is
   not driven by a few outlier categories.

## What would confirm / falsify

- **Confirm:** statistically robust gap (effect size meaningfully > 0) on a corpus of ≥200 matched minimal pairs, replicated in ≥2 of 3 panel models.
- **Weak:** gap present but small and inconsistent across models — function-word effects are real but not dominant over distributional.
- **Falsify:** flat or inverse pattern — content-word swaps move behavior at least as much as function-word swaps, after frequency control. Would be a strong (and surprising) finding for the distributional camp; write it.

## Operationalization (ratified) and result posture

The operationalization gate is **resolved**:
[`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)
(ratified 2026-06-21, session 66, autonomous adversarial review — ADOPT WITH MODIFICATIONS).
It fixes the yardstick:

- **Frequency norm:** [`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md)
  (SUBTLEX-US `Lg10WF`), fetched + sha256-pinned in-repo. Content controls are matched to the
  function-word swap targets within **|ΔLg10WF| ≤ 0.10**, plus length (±1 char) and a reported
  predictability non-difference; pair-level where feasible (*will→would*), condition-level with
  mirrored frequency spread where not (*because→although*, *some→every*). The full set is
  **frozen + hashed before the first probe call** (≥200 matched pairs after attrition, ≥4
  content-word semantic classes with per-class counts reported).
- **Indicator:** entailment-flip / graded forced-choice rate (prediction 2) is the sole
  confirm/weak/falsify-bearing test, behind a binding manipulation-check; the continuation-
  divergence proxy (prediction 1) is secondary/characterizing-only.
- **Result posture: `internal-contrast-only`** — the predictions are a within-model contrast
  (function-swap shift vs content-swap shift), so no human anchor is required for the minimal
  claim. A **BLiMP / NLI** human backing remains **fetch-and-catalogue-first** (neither is
  in-repo yet) and is an **optional Posture-2 upgrade** that never blocks the within-model run.

The conjecture is therefore **`designed`** but not yet runnable in one session: the build
session must still construct + certify the frozen matched set under an independent pre-run
critic (no item added/dropped after the first probe call). What counts as a "frequency-matched"
pair was the place a loop could quietly cheat by selecting items that bias the result — the
ratified freeze-and-hash + pre-run-critic GO/NO-GO is what binds that.

> **Build v1 (2026-06-21, session 67) — NO-GO; run DEFERRED.** The build pipeline is complete and
> the set passes minimal-pair integrity, the length-only-reader check (asymmetry 0.0), and no-leak,
> but `certification.json` is `"ok": false` on **three** checks: the **count** (66 < 200), the
> **≥4-class span** (only 3 viable classes — adjective dead), **and** the **freq-only-reader**
> check (0.1212 > 0.12; the `because`-arm content gap 1.335 < function gap 1.406). *(Correction,
> session 68: an earlier wording here said "certified SOUND on every matching/shortcut-reader/
> integrity check" — that overstated it; see the corrected
> [`result/function-word-swap-build-v1`](../results/function-word-swap-build-v1.md).)* Under
> faithful matching only **~66 clean items** survive: a *length-only* reader forces a signed **+1**
> content length-match (every function swap is +1 char), and the frequency∩length∩coherence
> intersection is thin — the person-noun route dies (no open-class noun at Lg10WF ≈ 3.33 with +1
> length near 4.74), the `the`→`a` swap admits **no** frequency-matched content control at all (no
> content word reaches Lg10WF ≈ 6.0), the adjective class has no clean matched swap, and
> `some`/`will` each yield a single matched out-word.
>
> **Decision resolved (2026-06-21, session 68 — adversarial review).** The blocker is resolved:
> [`decisions/resolved/function-word-count-vs-matching`](../../decisions/resolved/function-word-count-vs-matching.md).
> The reviewer **overturned** the relax-length default (length is degenerate in the function arm —
> Δlen ≡ +1 with zero variance — so it cannot be regressed out; it must stay a hard freeze-time
> gate) and adopted **inventory-widening** (add new function-word pairs at the unchanged ±0.10
> frequency tolerance + per-pair signed-Δlen gate) + capped carrier-authoring, also requiring the
> freq-only residual to be fixed and the ≥200/≥4-class bar kept. The conjecture stays **`designed`**
> and untested; build-v2 (the widened set) runs under a fresh pre-run critic. See
> [`result/function-word-swap-build-v1`](../results/function-word-swap-build-v1.md).

## Notes / caveats

- This is the most *abstract* of the project's constructional conjectures and so the most vulnerable to operationalization tuning. Lock the matched-pair set **before** seeing model outputs.
- A null here is a positive result for the distributional position, not a failure — write it as such.
