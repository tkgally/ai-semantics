---
type: result
id: blimp-swap-arm-v1
title: "BLiMP R1 content-word-swap arm (C8 promotion-prep, the exact-string-memorization control) — R1 is NOT SWAP-STABLE: the deep-scope grammatical profile does NOT survive frequency-matched content-word swap (deep Δ̄acc −0.06 to −0.09, all CIs exclude 0), and the drop is CONFOUNDED by a +0.20 C4 pretraining-frequency gap. Verdict SWAP-INCONCLUSIVE → R1 REFUSED promotion; stays descriptive/non-promotable."
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
    target: design/blimp-swap-arm-v1
  - rel: contradicts
    target: result/blimp-forced-choice-sweep-v1
  - rel: anchors
    target: resource/blimp
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: result/blimp-profile-frequency-control-covariate-v1
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
---

# Result — BLiMP R1 content-word-swap arm (program A3b, C8 promotion-prep)

> **A NON-PROMOTION result (the C8 gate is not passed).** `status: proposed` · `anchor: resource/blimp`
> (HUMAN-COMPARISON) · fresh items + fresh model calls (swapped accuracies unknown at freeze — the
> anti-cheat advantage). Ratified + frozen + built + gate-reviewed + run + verifier-checked this session
> (s210; gates
> [`decisions/resolved/blimp-swap-arm-design`](../../decisions/resolved/blimp-swap-arm-design.md) Q1-A /
> Q2-B / Q3-A + G-coverage + G-margin-justification; design
> [`design/blimp-swap-arm-v1`](../../../experiments/designs/blimp-swap-arm-v1.md)). PREREG + reviews +
> raw: [`experiments/runs/2026-07-11-blimp-swap-arm/`](../../../experiments/runs/2026-07-11-blimp-swap-arm/).
>
> **Verdict: SWAP-INCONCLUSIVE — R1 is NOT SWAP-STABLE.** Replacing the exact BLiMP content words with
> **novel, SUBTLEX-frequency-matched** same-POS words (holding the contrast locus + closed-class skeleton +
> main verbs + adverbs fixed, both presentation orders, N≈100 fresh paired items/paradigm) **lowers
> forced-choice accuracy on the load-bearing deep-scope stratum on all three models**: per-model
> per-stratum signed Δ̄acc = **−0.095 [−0.120, −0.071] / −0.057 [−0.095, −0.018] / −0.072 [−0.095, −0.048]**
> (claude / gpt / gemini), **all three CIs exclude 0**. The shallow stratum sits near ceiling and moves
> little (Δ̄ −0.030 / −0.033 / −0.027). So the panel's per-paradigm grammatical-difficulty profile does
> **not** cleanly survive the exact-string swap — **R1 does not achieve SWAP-STABLE, and per the ratified
> G8 it is REFUSED promotion** and stays **descriptive / non-promotable**. The flagship
> [`theory/shadow-depth-table-v2`](../theory/shadow-depth-table-v2.md) form-(iv) row keeps **only** its
> within-panel DEPTH-GRADED sibling.
>
> **Why INCONCLUSIVE and not a clean SWAP-DROPS — two honest hedges that both cut *against* promotion.**
> (1) **Rule sensitivity.** Under the PREREG *prose* rule (Δ̄ ≤ −0.05 with the CI excluding 0) the deep
> stratum **DROPS on 3/3**; under the *stricter coded* rule that ran (the *whole* CI ≤ −0.05) only claude's
> deep CI clears the bar (1/3), so the combined verdict is **SWAP-INCONCLUSIVE**. Both rules agree on the
> outcome that matters: **R1 is not SWAP-STABLE → not promoted.** (2) **A load-bearing pretraining-frequency
> confound (G-freq-pretraining).** The swap words are matched to the originals on the *human* SUBTLEX-US
> `Lg10WF` norm (achieved deep-stratum mean |Δ`Lg10WF`| ≈ **0.049**, within the ±0.10 band), but on the
> models' *pretraining-proxy* they are **materially rarer**: over 3,000,000 C4 sentences the originals'
> mean log-frequency is **2.817** vs the swap set's **2.614** — a **+0.204 log-unit gap** (swap words ~1.6×
> rarer; 2.3% never occur). So the deep drop **cannot be cleanly attributed to exact-string / lexical-item
> memorization** — it is confounded with the swap set simply being rarer in pretraining. The swap arm
> therefore neither confirms stability **nor** cleanly establishes memorization; it **removes SWAP-STABLE
> from the table**, which is what the promotion gate turned on.

## What this is, and what it is not

**What it is.** The second, promotion-required arm of the ratified C8 control on reading **R1
PROFILE-ALIGNED** of [`result/blimp-forced-choice-sweep-v1`](blimp-forced-choice-sweep-v1.md) (the panel's
per-paradigm forced-choice accuracy tracks BLiMP per-paradigm human agreement, ρ_prof +0.606 / +0.543 /
+0.628). Per **G8**, promotion of R1 to the program's first broad human-anchored grammatical-competence
claim required **SURVIVES-COVARIATE (s208) ∧ SWAP-STABLE (this arm)**. The s208 covariate arm returned
SURVIVES; **this arm does not return SWAP-STABLE**, so the conjunction fails and **R1 is not promoted.**

**What it is NOT.** It is **not** a clean demonstration that R1 rides on exact-string memorization — the
C4 pretraining-frequency confound blocks that reading. It does **not** touch R2 (DEPTH-GRADED, within-panel,
already verdict-bearing) or R2h. It is **not** a refutation of R1 as a *descriptive* reading — the profile
alignment stands as a descriptive/directional fact; what fails is its **promotion** to a memorization- and
frequency-controlled human-comparison claim.

## Numbers (recompute from `raw/` via `analyze_swap.py`; independently reproduced by the post-run verifier)

Per model, per stratum: signed stratum-mean Δ̄acc = mean over the stratum's ~300 paired items of
(acc_swap_pair − acc_orig_pair), order-averaged; percentile bootstrap CI (5,000 resamples over pairs).

| model | shallow Δ̄ [CI] | deep Δ̄ [CI] |
|-------|----------------|-------------|
| claude (A) | −0.030 [−0.050, −0.015] | **−0.095 [−0.120, −0.071]** |
| gpt (B)    | −0.033 [−0.053, −0.015] | **−0.057 [−0.095, −0.018]** |
| gemini (C) | −0.027 [−0.045, −0.012] | **−0.072 [−0.095, −0.048]** |

Per deep paradigm (orig → swap accuracy; all three drop on all three models):
`superlative_quantifiers_1` 0.895→0.775 / 0.875→0.795 / 0.995→0.930; `sentential_negation_npi_scope`
0.945→0.862 / 0.870→0.800 / 0.960→0.885; `only_npi_scope` 0.615→0.546 / 0.785→0.765 / 0.570→0.495 (this
paradigm is intrinsically hard — orig accuracy 0.57–0.79 — and noisier). 7,200 calls, 0 errors, 13 unparsed
(0.18%). No INSTRUMENT-FAILURE (poslock 0.15–0.22; ans1 0.39–0.49). Coverage all clear the 0.50 floor (deep
0.97–0.98; none excluded).

## Build limitations that travel (from the G5-plus verifier + freeze critic, all *shallow-only* + *conservative*)

The near-ceiling **shallow** stratum carries build defects that bias its small Δ̄ **downward** (never toward
STABLE) and are therefore *not* load-bearing for the verdict, which rests on the **deep-3** (audited clean):
(i) ~11% of `determiner_noun_agreement` items have a finite verb mis-tagged as a noun and swapped
(a POS-tagger leak the NP-context gate did not catch); (ii) ~4% of `regular_plural_subject_verb_agreement_1`
items are pseudo-partitive "a lot of X" whose head swap flips notional agreement; (iii) the det-noun
carve-out's substitutes are only loosely SUBTLEX-matched (mean |Δ`Lg10WF`| ≈ 0.37 vs ≈0.049 for the deep
noun/name/adjective swaps). Per the ratified Q3-A ("audit-flagged anomalies are reported as a limitation,
not silently fixed") and the freeze critic's condition 1, the instrument was **not rebuilt** after these
were found (re-touching it after seeing items would forfeit the unknown-at-freeze anti-cheat advantage).
The **deep-scope-3 audited clean** (0 defects; verbs/`not`/`only`/`ever` held fixed) and are well
SUBTLEX-matched, so the deep drop is a genuine signal — its only confound is the C4 pretraining-frequency
gap above, not the build.

## Scope caps (read before citing)

1. **A NON-PROMOTION, not a positive negative.** SWAP-INCONCLUSIVE removes SWAP-STABLE and refuses R1's
   promotion; it does **not** license "R1 is memorization" (C4-confounded) nor "R1 is false" (the
   descriptive alignment stands).
2. **Deep-pole generality (G-frame).** The swap covers the **scope-deep** pole (NPI/quantifier) only, not
   the **island-deep** pole (excluded — a POS-swap can break gap-licensing). "Deep" here = scope-deep.
3. **Perturbation bound (G-coverage).** Stability/instability is under replacement of content nouns / proper
   names / attributive adjectives only; main verbs and adverbs were held fixed. A stronger arm would also
   swap verbs (with a subcategorization guard) — a deferred sensitivity arm.
4. **The pretraining-frequency confound (G-freq-pretraining) is the headline limitation:** the swap matched
   *human* frequency (SUBTLEX-US) but left a +0.20 log-unit *pretraining-proxy* (C4) gap. A clean successor
   arm would **C4-frequency-match** the swaps; only then could a deep drop be read as exact-string
   memorization rather than pretraining rarity.
5. **Contamination upper bound persists.** Absolute accuracy stays an upper bound; SWAP never speaks to
   grammatical competence, only to whether the exact strings were load-bearing.
6. n = 3 models; per-model, per-stratum Δ, never pooled.

## What it feeds

- **The C8 chain closes with R1 REFUSED promotion.** SURVIVES-COVARIATE (s208) ∧ SWAP-STABLE was required;
  SWAP-STABLE did not obtain. R1 stays **descriptive / non-promotable**; the
  [`theory/shadow-depth-table-v2`](../theory/shadow-depth-table-v2.md) form-(iv) row is **unchanged** (keeps
  DEPTH-GRADED + the descriptive PROFILE-ALIGNED reading; no advance toward a claim). The program's first
  broad human-anchored grammatical claim is **not** earned on this line.
- **A sharpened successor question (registered):** the arm was under-powered against its *own* confound —
  it matched human frequency but not pretraining frequency. The clean test is a **C4-frequency-matched
  swap arm** (and/or a verb-swap arm with a valence guard). Until then, whether R1's deep-scope alignment
  rides on exact-string memorization vs pretraining-frequency vs shared grammatical difficulty is **open**.
- Corroborates the honesty of [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md)'s
  contamination caution: the deep-scope profile is exactly where exact-string / frequency exposure is
  hardest to rule out.
