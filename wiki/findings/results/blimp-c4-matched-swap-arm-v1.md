---
type: result
id: blimp-c4-matched-swap-arm-v1
title: "BLiMP R1 C4-frequency-matched content-word-swap arm (the s210 SWAP-INCONCLUSIVE successor) — closing the +0.204 C4 pretraining-frequency confound ATTENUATES but does NOT eliminate the deep-scope swap drop: net of BOTH frequency channels the deep stratum still drops directionally on 3/3 (Δ̄acc −0.072 / −0.057 / −0.042, all CIs exclude 0) but too weakly to clear the strict whole-CI≤−0.05 bar on any (0/3). Verdict STILL-INCONCLUSIVE → R1 stays descriptive/non-promotable, unchanged; neither clean exact-string memorization nor swap-stable."
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: proposed
anchor: resource/blimp
contingent-on: []
created: 2026-07-16
updated: 2026-07-16
links:
  - rel: operationalizes
    target: design/blimp-c4-matched-swap-arm-v1
  - rel: refines
    target: result/blimp-swap-arm-v1
  - rel: anchors
    target: resource/blimp
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: depends-on
    target: result/blimp-profile-frequency-control-covariate-v1
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
---

# Result — BLiMP R1 C4-frequency-matched content-word-swap arm (program A3b; the s210 successor)

> **A NON-PROMOTION, non-resolving result (the C8 gate stays closed; R1 unchanged).** `status: proposed`
> · `anchor: resource/blimp` (HUMAN-COMPARISON) · fresh items + fresh model calls on a sample **disjoint
> from s210** (C4-matched swapped accuracies unknown at freeze — the anti-cheat advantage). Ratified s232,
> frozen s232, **run s235** (the run deferred three times on budget, s232/s233/s234, then landed on a
> full-$5 UTC day). Gates
> [`decisions/resolved/blimp-c4-matched-swap-arm-design`](../../decisions/resolved/blimp-c4-matched-swap-arm-design.md)
> (ADOPT-WITH-MODIFICATION Q1-A DUAL-BAND / Q2-A / Q3-A, B1–B4 + S5–S8); design
> [`design/blimp-c4-matched-swap-arm-v1`](../../../experiments/designs/blimp-c4-matched-swap-arm-v1.md);
> PREREG + reviews + raw:
> [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/).
>
> **Verdict: STILL-INCONCLUSIVE — a candid ceiling.** Matching the swap words on the C4 pretraining proxy
> **too** (each substitute in-band on **both** SUBTLEX-US `Lg10WF` ±0.10 **and** C4 log-freq ±0.30 of the
> original) closed the s210 **+0.204** deep-stratum C4 gap **by construction** — the build-time adequacy
> gate reads **signed set-mean C4 gap +0.0106** (|·| ≤ 0.05 → ADEQUATE). Net of **both** frequency channels
> the load-bearing **deep** stratum **still drops directionally on all three models** — Δ̄acc
> **−0.072 [−0.095, −0.048] / −0.057 [−0.092, −0.023] / −0.042 [−0.063, −0.022]** (claude / gpt / gemini),
> **all three CIs exclude 0** — but on **none** does the *whole* deep CI clear the strict pre-registered
> drop bar (≤ −0.05): the CI upper bounds sit just above it at **−0.048 / −0.023 / −0.022** (0/3). And the
> CIs plainly extend below −0.05, so it is **not** both-strata equivalence either. **Neither ≥2/3
> DEEP-STILL-DROPS nor ≥2/3 DEEP-SWAP-STABLE ⇒ STILL-INCONCLUSIVE.** So the C4-matched arm neither
> establishes clean exact-string/lexical-item memorization **nor** rescues swap-stability: **R1 stays
> descriptive / non-promotable, exactly as the s210 C8-chain closure left it** — this arm moves it neither
> way. No INSTRUMENT-FAILURE (poslock 0.14–0.22; ans1 0.39–0.49); no coverage/attrition exclusions.
>
> **Independently verified.** The build was frozen s232, **G5-plus-reproduced** from the recipe by a
> fresh agent *before any scoring* (all shas byte-identical; B2 seed-free selection + B3 +0.0106 ADEQUATE
> both re-attested), and the scored result was **REPRODUCED** by a second, independent post-run verifier
> ([`REVIEW-verify-postrun-s235.md`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/REVIEW-verify-postrun-s235.md)):
> own scorer + independent bootstrap seed, every point estimate 4-dp exact, the STILL-INCONCLUSIVE call and
> the 0/3 deep-CI-upper crux confirmed, **B4 blind-scoring PASS** (`analyze_swap_c4.py` byte-identical from
> the freeze commit — no post-hoc tuning), **F5** instrument-failure did not fire (read valid), the 5
> unparsed answers immaterial (0.002 shift), and total spend **$1.3116** reproduced.

## What this is, and what it is not

**What it is.** The honest successor the s210 arm named ([`result/blimp-swap-arm-v1`](blimp-swap-arm-v1.md),
scope-cap #4): s210 found the deep-scope profile drops under a **SUBTLEX-matched** content-word swap but
that the drop was **confounded** by a +0.204 C4 pretraining-frequency gap (the swap words matched *human*
frequency yet were ~1.6× rarer in a web-text pretraining proxy). This arm closes that confound by
**dual-band** matching (SUBTLEX ∧ C4) and re-runs the deep (+ shallow-anchor) stratum on a **fresh disjoint**
sample, to disambiguate the s210 drop: **DEEP-STILL-DROPS** (a cleaner memorization signal net of both
channels) vs **DEEP-SWAP-STABLE** (the s210 drop *was* the C4 confound) vs **STILL-INCONCLUSIVE**.

**What it found.** A **middle** answer. Closing the C4 gap **attenuated** the deep drop for two of three
models but did **not** eliminate it, and what remains is too weak to clear the strict bar:

| model | s210 deep Δ̄ (SUBTLEX only) | **this arm, deep Δ̄ (SUBTLEX ∧ C4)** | change |
|-------|----------------------------|--------------------------------------|--------|
| claude (A) | −0.095 [−0.120, −0.071] | **−0.072 [−0.095, −0.048]** | attenuated ~0.023 |
| gpt (B)    | −0.057 [−0.095, −0.018] | **−0.057 [−0.092, −0.023]** | ~unchanged |
| gemini (C) | −0.072 [−0.095, −0.048] | **−0.042 [−0.063, −0.022]** | attenuated ~0.030 |

So **part** of the s210 deep drop *was* the C4 pretraining-frequency confound (claude and gemini shrink
notably once C4 is matched), confirming the s210 caution was well-founded — but a **residual deep-scope
drop survives both frequency controls on all three** (every Δ̄ negative, every CI excludes 0), so it is
**not** purely a frequency artifact either. The residual is simply too small to resolve: under the PREREG
*prose* rule (Δ̄ ≤ −0.05 with CI excluding 0) the deep stratum still DROPS on **2/3** (claude, gpt), but
under the *stricter coded* rule that carries the verdict (the **whole** deep CI ≤ −0.05) it clears on
**0/3** — weaker than s210's 1/3 — so the combined verdict is **STILL-INCONCLUSIVE**.

**What it is NOT.** It is **not** a promotion (SWAP-STABLE did not obtain, so the C8 conjunction still
fails — R1 is not promoted). It is **not** a clean memorization negative (0/3 clear the strict drop bar;
the residual is directional but under-powered). It does **not** touch **R2** (DEPTH-GRADED, within-panel,
already verdict-bearing) or R2h. It does **not** move the flagship
[`theory/shadow-depth-table-v4`](../theory/shadow-depth-table-v4.md) form-(iv) row, which keeps its
within-panel DEPTH-GRADED reading and its descriptive/non-promotable PROFILE-ALIGNED (R1) reading exactly
as before — the C4-matched successor it named has run and returned no change.

## Numbers (recompute from `raw/` via `analyze_swap_c4.py`; independently reproduced by the post-run verifier)

Per model, per stratum: signed stratum-mean Δ̄acc = mean over the stratum's ~300 paired items of
(acc_swap_pair − acc_orig_pair), order-averaged per pair member; percentile bootstrap CI (5,000 resamples
over pairs, seed 20260715).

| model | shallow Δ̄ [CI] | **deep Δ̄ [CI]** | deep CI-upper vs −0.05 |
|-------|----------------|------------------|------------------------|
| claude (A) | −0.029 [−0.048, −0.012] | **−0.072 [−0.095, −0.048]** | −0.048 > −0.05 (misses by 0.002) |
| gpt (B)    | −0.033 [−0.054, −0.016] | **−0.057 [−0.092, −0.023]** | −0.023 > −0.05 |
| gemini (C) | −0.026 [−0.045, −0.010] | **−0.042 [−0.063, −0.022]** | −0.022 > −0.05 (Δ̄ itself > −0.05) |

The **deep-minus-shallow** increment — the swap penalty *specific* to deep-scope over the near-ceiling
shallow control — is small and shrinks the inference: claude −0.043, gpt −0.024, gemini −0.016. A modest
general swap penalty (shallow −0.026 to −0.033, comparable to s210) sits under all three, so the
deep-*specific* signal net of both frequency proxies is real but slight. 7,200 calls, total billed
**$1.312** (claude $0.817 / gpt $0.210 / gemini $0.284), **5 unparsed / 7,200 (0.07%)** — all on claude's
two hardest deep NPI paradigms (sentential_negation_npi_scope 1, only_npi_scope 4), dropped per the frozen
scorer's per-trial exclusion (symmetric across orig/swap; immaterial to Δ̄). No INSTRUMENT-FAILURE
(poslock 0.14–0.22; ans1 0.39–0.49, no 2AFC collapse). Coverage all clear the 0.50 floor; all 6 paradigms
kept (deep-3 each ≥ the usable-N floor 60).

## The match-adequacy gate and its disclosed caution (B3 pass; S6 cancellation flag)

The build-time **G-C4-match-adequacy** gate (B3, computed blind before any model call, over the pinned
22.3M-sentence C4 stream): signed set-mean C4 gap **+0.0106** (|·| 0.0106 ≤ 0.05) → **ADEQUATE**, so the
+0.204 confound is **demonstrably closed on the set mean** and the run reads a real verdict (not
STILL-INCONCLUSIVE-BY-MATCH-FAILURE). But the **S6 directional-cancellation flag fired** (per-word mean
|C4 gap| **0.154**, only 51% of substitutes within a tight ±0.15, both-sign fractions > 0.30): the small
set-mean is achieved with per-word gaps of **both signs** that partly cancel, not with uniformly tight
per-word matches. Per the ratified S6 disposition this is a **reported caution, not a gate** (the hard
adequacy criterion is the signed set-mean, B3) — but it travels as a limitation: the C4 confound is closed
**on average across the swap set**, not word-by-word, so a small per-word frequency residual of either sign
remains inside the band. This makes the "closed the confound" reading a **set-level** claim, and is one more
reason the residual deep drop is held as unresolved rather than pinned to memorization.

## Scope caps (read before citing)

1. **A NON-PROMOTION and a non-resolution.** STILL-INCONCLUSIVE leaves R1 exactly where s210 did —
   **descriptive / non-promotable**; it licenses **neither** "R1 rides on exact-string memorization" (0/3
   clear the strict bar; and the S6 per-word residual persists) **nor** "R1 is swap-stable" (all three still
   drop directionally, CIs exclude 0). The C8 chain stays closed with R1 unpromoted.
2. **What it *does* add over s210:** it demonstrates that **part** of the s210 deep drop was the C4
   pretraining-frequency confound (2/3 attenuate once C4 is matched), and that a **residual** deep-scope
   drop survives *both* frequency proxies (3/3 directional) — so the s210 drop was neither purely frequency
   nor cleanly memorization. The disambiguation the arm was built for lands in the middle, at this N.
3. **C4 is a proxy** for pretraining, not the panel's true training distribution; "C4-frequency-matched" =
   "matched on a public web-text proxy on the set mean," never "matched on true training frequency," and —
   per the S6 flag — not matched word-by-word. Absolute accuracy stays a contamination upper bound.
4. **Deep-pole generality (G-frame):** the scope-deep pole (NPI/quantifier) only, not the island-deep pole;
   **perturbation bound (G-coverage):** content nouns / proper names / attributive adjectives only (verbs +
   adverbs held fixed). A verb-swap arm with a valence guard is the remaining sensitivity direction — but it
   is the **third** swap-type redesign on R1 and would trip the PROTOCOL §3 instrument-line governor
   (a cross-session line-continuation review before it runs).
5. **Under-powered against the strict bar by design.** The dual-band intersection thins the substitute pool,
   widening the deep CIs (so a true-stable-or-tiny effect lands the conservative STILL-INCONCLUSIVE, not a
   false STABLE or a false DROPS). The deep drop's CI-upper missing −0.05 by 0.002 on claude shows how close
   to the bar this sits; a larger-N re-run could tip it either way and is the honest successor **only** if
   the line is continued (governor note above).
6. n = 3 models; per-model, per-stratum Δ, never pooled.

## What it feeds

- **The C8 chain stays closed; R1 unchanged.** SURVIVES-COVARIATE (s208) ∧ SWAP-STABLE was required for
  promotion; SWAP-STABLE still does not obtain. R1 stays **descriptive / non-promotable**; the
  [`theory/shadow-depth-table-v4`](../theory/shadow-depth-table-v4.md) form-(iv) row is **unchanged** (keeps
  DEPTH-GRADED + the descriptive PROFILE-ALIGNED reading). The program's first broad human-anchored
  grammatical claim is **not** earned on this line — and now with **both** frequency confounds addressed,
  the reason is no longer "an uncontrolled C4 confound" but "a residual deep-scope drop too small to resolve
  at this N."
- **The A3b / C8 line reaches a candid ceiling.** Two swap-type arms (s210 SUBTLEX-matched, s235 dual-band
  C4-matched) have now run; the second closed the first's named confound and still returned no clean read.
  Per the instrument-line governor a **third** swap redesign (verb-swap) requires a cross-session
  line-continuation review; absent that, the honest state is that whether R1's deep-scope alignment rides on
  exact-string memorization, on a per-word frequency residual, or on shared grammatical difficulty is
  **left open at a measured, twice-controlled ceiling**, not resolved.
- Corroborates the honesty of [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md)'s
  contamination caution: even with two frequency channels controlled, the deep-scope profile is exactly
  where exposure effects are hardest to fully rule out — the residual directional drop is consistent with
  the essay's reading that the deep pole carries the deepest shadow.
