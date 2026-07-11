---
type: result
id: blimp-profile-frequency-control-covariate-v1
title: "BLiMP R1 frequency control, covariate arm (ROBUSTNESS/CORROBORATION) — the panel's human-aligned grammatical difficulty profile (ρ_prof +0.54–0.63) SURVIVES partialling a C4 surface-lexical frequency proxy: partial ρ_prof·F +0.51–0.61, all CIs exclude 0, 3/3. A robustness datum only — C8's promotion gate is NOT satisfied (the swap arm is outstanding)."
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: proposed
anchor: resource/blimp
contingent-on: []
created: 2026-07-11
updated: 2026-07-11
links:
  - rel: operationalizes
    target: design/blimp-profile-frequency-control-v1
  - rel: supports
    target: result/blimp-forced-choice-sweep-v1
  - rel: anchors
    target: resource/blimp
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
---

# Result — BLiMP R1 frequency control, covariate arm (program A3b, C8 promotion-prep)

> **A ROBUSTNESS / CORROBORATION result, not a promotion (G8/G9).** `status: proposed` ·
> `anchor: resource/blimp` (HUMAN-COMPARISON) · reuses the frozen s205 accuracies + committed human anchor
> (no new grammatical measurement) · covariate arm only ($0 model cost). Ratified + frozen + run +
> verifier-checked this session (s208; gates
> [`decisions/resolved/blimp-profile-frequency-control-design`](../../decisions/resolved/blimp-profile-frequency-control-design.md)
> Q1-C / Q2-A / Q3-A + G8 binding + G9; design
> [`design/blimp-profile-frequency-control-v1`](../../../experiments/designs/blimp-profile-frequency-control-v1.md)).
> PREREG + reviews:
> [`experiments/runs/2026-07-11-blimp-frequency-control/`](../../../experiments/runs/2026-07-11-blimp-frequency-control/).
>
> **Verdict: SURVIVES-COVARIATE 3/3.** The per-model Spearman of per-paradigm forced-choice accuracy
> against BLiMP per-paradigm human agreement (`H`) — R1 PROFILE-ALIGNED from
> [`result/blimp-forced-choice-sweep-v1`](blimp-forced-choice-sweep-v1.md), ρ_prof **+0.606 / +0.543 /
> +0.628** — stays clearly positive after partialling out a per-paradigm **C4 surface-string frequency
> proxy** `F(p)`: partial ρ_prof·F **+0.572 [+0.308,+0.774] / +0.510 [+0.225,+0.718] / +0.606
> [+0.329,+0.794]** (claude / gpt / gemini), all bootstrap CIs exclude 0. The raw→partial drop is tiny
> (**+0.035 / +0.033 / +0.021**). The alignment is **over-and-above** the surface-lexical frequency proxy.
>
> **⚠ WHAT THIS IS NOT (G9, read before citing).** This is the **covariate arm only**. Per the ratified
> **G8**, the covariate arm alone earns a **robustness/corroboration** result and **C8's promotion gate is
> NOT satisfied.** The **content-word-swap arm** (Q1-C — exact-string-memorization control, fresh items +
> fresh calls) is the **outstanding requirement** for any human-comparison promotion of R1. Until it runs
> and R1 is SWAP-STABLE, R1 stays **descriptive/non-promotable**, and the shadow-depth flagship table's
> grammar-side form-(iv) row is **unchanged** (it keeps DEPTH-GRADED + the descriptive PROFILE-ALIGNED
> reading; this result does **not** advance it toward a claim).
>
> **Two load-bearing proxy caveats (G3′).** (i) `F(p)` is computed from **C4**, a *proxy* for the panel's
> unknown pretraining distribution — so SURVIVES reads "over-and-above a **C4-frequency proxy**," never
> "over-and-above the panel's actual training frequency." (ii) The Q2-A proxy is **surface-lexical
> familiarity, NOT construction frequency** (C8's literal confound) — so the covariate arm's honest reach
> is "over-and-above **lexical/surface exposure**." Construction frequency is reached only indirectly, and
> a promotion would inherit both caveats.

## What was run

The covariate arm of the pre-registered training-frequency confound control (
[`PREREG.md`](../../../experiments/runs/2026-07-11-blimp-frequency-control/PREREG.md), frozen and committed
**before** `F(p)` was computed). `F(p)` (Q2-A) = the per-paradigm mean, over each paradigm's 30 frozen
`good` sentences, of the mean `log(1 + c(g))` where `c(g)` is the count of each content-word adjacent
bigram/trigram `g` as consecutive tokens across the frozen C4 set (shards 00000–00002, **22,329,495
sentences**, 347.7M tokens; ODC-BY + Common-Crawl terms). `build_freq.py` reuses **only** the C4 streaming
adapter + tokenizer from `build_cooc_c4.py` (import-pinned; that script has no n-gram counter — the counting
is new code, G1′), and reads **neither** the accuracies **nor** `H` — `F(p)` is computed blind. The partial
Spearman ρ_prof·F, its bootstrap CI (5000 resamples, seed 20260711), the collinearity branch, the two
negative controls, and the G7 audit are recomputed from the frozen s205 accuracies + committed `H` +
`F(p)` in `analyze_partial.py`.

**Gate order.** A fresh-agent verifier independently reproduced `build_freq.py` from the PREREG spec on a
synthetic fixture (identical to 2.22e-16), certified zero post-freeze latitude, and confirmed the reuse
boundary — **before** `F(p)` touched the real paradigm→H mapping
([`REVIEW-verify-G1prime-s208.md`](../../../experiments/runs/2026-07-11-blimp-frequency-control/REVIEW-verify-G1prime-s208.md)).
A post-run verifier reproduced every figure below from the frozen inputs
([`REVIEW-verify-postrun-s208.md`](../../../experiments/runs/2026-07-11-blimp-frequency-control/REVIEW-verify-postrun-s208.md)).

## The numbers

**Collinearity branch first (G6).** `corr(F,H)` (Spearman) = **+0.2595** — inside the pre-registered
interpretable regime (`0.20 ≤ |corr| ≤ 0.70`; above the `<0.20` "no-confound-to-control" floor, below the
`>0.70` over-control ceiling). So the C8-posited frequency–difficulty structure is **present but modest**,
and the partial is interpretable (neither absent nor collinear-degenerate).

| model | raw ρ_prof | partial ρ_prof·F [95% CI] | drop | P(CI excl 0) | bi-only sensitivity |
|-------|-----------|---------------------------|------|--------------|---------------------|
| claude (A) | +0.606 | **+0.572 [+0.308, +0.774]** | +0.035 | 1.000 | +0.573 |
| gpt (B) | +0.543 | **+0.510 [+0.225, +0.718]** | +0.033 | 0.9996 | +0.509 |
| gemini (C) | +0.628 | **+0.606 [+0.329, +0.794]** | +0.021 | 1.000 | +0.610 |

All three partial CIs exclude 0 → **SURVIVES-COVARIATE 3/3**. The bi-only sensitivity variant is
essentially identical (the verdict does not depend on the bigram/trigram choice).

**Negative controls (G1′, necessary-not-sufficient).**
- **NC2 scramble-F** (a random covariate should control nothing): partial ≈ raw — **+0.610 / +0.583 /
  +0.650** vs raw +0.606 / +0.543 / +0.628. The partialling machinery does not spuriously deflate ρ.
- **NC1 scramble-H** (shuffle the paradigm→H mapping): partials **−0.401 / −0.275 / −0.093** — **not
  systematically positive**, i.e. the pipeline does not manufacture a positive partial from a scrambled
  mapping. (A single-draw scramble is noisy; the point is the absence of a spurious positive, which holds.)

**Proxy-validity audit (G7, read before the verdict).** `F` vs per-paradigm mean content-word **unigram
log-frequency** Spearman = **+0.481** (predicted positive — `F` tracks lexical frequency, moderately, as a
bigram/trigram proxy should without being redundant with unigram frequency); `F` vs mean content-word
**length** = **−0.353** (predicted negative — Zipf). Both in the predicted directions; the audit passes,
and `F` is not downgraded to descriptive.

## Reading

R1's human-profile alignment is **not** an artifact of the paradigms' surface-lexical corpus frequency:
partialling out a 22.3M-sentence C4 surface-string frequency proxy barely moves ρ_prof (drop ≤ +0.035),
and the residual alignment is clearly positive on all three models. Because the frequency–difficulty
correlation the control exists for is itself only modest here (`corr(F,H)` = +0.26), there was limited
signal for the covariate to remove — which is itself informative: the panel's human-aligned grammatical
difficulty profile is **largely orthogonal** to how frequent the paradigms' surface material is in web
text. This **corroborates** the honesty of the R1 reading against one of the two sub-confounds C8 named.

It does **not** promote R1. Per **G8** this arm addresses only the surface-lexical/exposure channel; the
**exact-string-memorization** channel (does the alignment survive swapping the actual content words for
fresh ones?) is untested, and per the ratified gate the swap arm is **required** for a human-comparison
promotion. R1 remains descriptive/non-promotable.

## Scope & limitations (load-bearing)

1. **Controls R1 only** — not R2 (DEPTH-GRADED, within-panel, already verdict-bearing) or R2h (TRACKS-DIP).
2. **Surface-lexical, not construction frequency** (G3′-ii); **C4 proxy, not actual training frequency**
   (G3′-i). Both caveats travel into any future promotion review.
3. **The proxy is thin for function-word-heavy paradigms.** 180 of 1,200 good sentences (15%) had **zero**
   content-word bigrams/trigrams and were dropped-and-logged (never repaired, per PREREG); the drop
   concentrates on NPI-licensor / echo-question / matrix-question paradigms (e.g.
   `left_branch_island_echo_question` retained only 5 of 30), whose `good` sentences are mostly function
   words. So `F(p)` for those paradigms rests on few n-grams and is a **noisier** estimate. All 40
   paradigms were retained (min 5 sentences), so n = 40 stands, but this thinness is exactly why a
   *noisy/weak* `F` removes little — reinforcing (not undermining) the G8 decision to cap this arm at
   robustness and require the swap arm for a promotion.
4. **Reuses the frozen s205 order-averaged per-paradigm accuracies** (verifier-reproduced s205) — the
   covariate arm adds no new grammatical measurement; its force is entirely in the partialling. The
   designer's prior knowledge of the accuracies is the anti-cheat exposure (G1′) fenced by the frozen
   PREREG + the fresh-agent reproduction, and is the standing reason (G8) the covariate arm cannot promote.
5. **Absolute BLiMP accuracy (0.87–0.94) remains a contamination upper bound**, never a headline (carried
   from s205).

## What this feeds

- **[`predictions.md`](../../predictions.md):** the s208-registered covariate-SURVIVES bet **fires-for**.
- [`result/blimp-forced-choice-sweep-v1`](blimp-forced-choice-sweep-v1.md): R1 gains a robustness datum
  (survives the surface-lexical frequency control) but stays descriptive/non-promotable pending the swap
  arm; the result is unchanged in force.
- [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md) /
  [`theory/shadow-depth-table-v2`](../theory/shadow-depth-table-v2.md): **no revision trigger fires** — a
  robustness corroboration of an existing descriptive reading does not move the grammar-side form-(iv) row
  toward a claim (G9). The table row is unchanged.
- **Next:** the **content-word-swap arm** (Q1-C) — the outstanding C8 requirement for a promotion; a later
  session designs/critics/freezes/runs it (≥2 shallow + ≥2 deep paradigms, grammaticality re-validated per
  G5, ~$0.3–0.6). SURVIVES-COVARIATE ∧ SWAP-STABLE → R1 becomes a promotion-review candidate.
