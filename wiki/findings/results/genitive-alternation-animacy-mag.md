---
type: result
id: genitive-alternation-animacy-mag
title: The genitive possessor-animacy effect now carries a within-model MAGNITUDE — a third disjoint typical arm (36 fresh-blind frames, session 222) pooled with s218+rep2 = 108 typical frames gives a pooled within-frame animacy shift of +0.145 / +0.169 / +0.139 (claude / gemini / gpt), every model's bootstrap CI lower bound above zero; the fresh-36 blind arm independently clears CI-LB>0 3/3 (sign-p ≤ 6e-4), so the magnitude is a CLEAN attach, not fresh-arm-weak; the typical-arm magnitude is far more cross-model consistent (~1.2×) than the nonce arm (~3.6–4×); the covariate is again near-vacuous and the gradient again a sharp animate/non-animate binary — this lifts the promoted claim's fence (i) from magnitude-deferred to magnitude-attached (within-model), the direction/anchor scope unchanged
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: depends-on
    target: conjecture/genitive-alternation-animacy
  - rel: depends-on
    target: design/genitive-alternation-animacy-v1
  - rel: refines
    target: result/genitive-alternation-animacy-rep2
  - rel: supports
    target: claim/genitive-alternation-animacy
  - rel: anchors
    target: resource/genitive-animacy-human-anchor
  - rel: depends-on
    target: source/dubois-2023-genitive-animacy
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/shadow-depth-table-v3
---

# Result: the genitive possessor-animacy effect carries a within-model MAGNITUDE (powered pooled arm)

> **Status: proposed (2026-07-13, session 222).** The **powered magnitude re-run** that the s221
> promotion review named as the promoted claim's own remaining owed unit — the
> [`claim/genitive-alternation-animacy`](../claims/genitive-alternation-animacy.md) was promoted
> `supported` but **direction-only**, its fence **(i)** flagging that both founding runs (s218 + rep2)
> are 36+36 typical frames, below [`PROTOCOL.md §4`](../../../PROTOCOL.md)'s powered N (~100–150), so no
> within-model magnitude+interval was attached. This run attaches it the way the dative (s175, N=100)
> and the comparative correlative (s169, N=136) attached theirs: a **third disjoint typical-only arm**
> of **36 fresh frames**, every possessor lemma certified disjoint from **both** prior arms (108 new
> lemmas, 0 of 214 shared), authored **blind** to model responses, then **pooled** with s218+rep2 →
> **108 typical frames** for a bootstrap magnitude+interval. The measurement instrument is byte-frozen
> (`probe.py`/`build_cooc_gen.py` sha-identical; `common.py` differs only in the documented budget
> constant); the pooling analysis (`analyze_merged.py`) was frozen in
> [`PREREG.md`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-mag/PREREG.md) before
> any model call, with a **fresh-agent pre-run critic GO** and a **non-Anthropic decorrelation vote
> GO-WITH-CONDITIONS** (both conditions on the write-up, honoured below). **Outcome: CLEAN MAGNITUDE
> ATTACHED** — all three models' fresh-36 blind arms independently clear CI-LB>0 (gate 1, 3/3), and all
> three pooled-108 intervals clear CI-LB>0 (gate 2, 3/3). This is a **reading-bearing** result and
> rests at `proposed`; the magnitude **support migrates to the claim layer**
> ([`claim/genitive-alternation-animacy`](../claims/genitive-alternation-animacy.md)), where fence (i)
> is lifted.

## The magnitude (the new content)

Per model, the finding-bearing measure is the within-frame typical-arm animacy shift
`shift(frame) = mean(s-pref | animate) − mean(s-pref | inanimate)` (averaged over the A/B
counterbalance), the s-preference in [0,1] being s-points/(s-points+of-points) on the byte-frozen
graded forced-choice. The magnitude = the **pooled-frame mean** with a nonparametric bootstrap 95% CI
over the 108 frames (resampling unit = the frame, ratified S3). **Read the numbers with the labels
the two pre-run reviewers required (below): the pooled column is a magnitude UPDATE conditional on the
already-established direction — it is tighter by construction because 72/108 frames are the very data
that set the direction — and the NEW-36 blind column is the genuine fresh check.**

| model | **NEW-36 (blind check)** | prior-72 (s218+rep2) | **POOLED-108 (magnitude, conditional update)** |
|---|---:|---:|---:|
| `claude-sonnet-4.6` | **+0.155** [0.120, 0.194], 35/36, sign-p 0 | +0.140 [0.114, 0.167] | **+0.145** [0.124, 0.167], 102/108 |
| `gemini-3.5-flash` | **+0.175** [0.118, 0.235], 30/36, sign-p 3.5e-5 | +0.166 [0.133, 0.198] | **+0.169** [0.140, 0.198], 93/108 |
| `gpt-5.4-mini` | **+0.178** [0.117, 0.242], 28/36, sign-p 6.0e-4 | +0.120 [0.090, 0.150] | **+0.139** [0.110, 0.170], 88/108 |

- **Gate 1 (standalone fresh blind arm — the pre-registered attach bar).** All three fresh-36 arms
  independently clear **CI-LB > 0** with **decisive** one-sided sign tests (p ≤ 6e-4) — the same bar
  each prior 36-frame typical arm cleared. So this is a **CLEAN attach**, not the "attached-but-
  fresh-arm-weak" tier the critic's condition (c) reserved for a marginal fresh arm.
- **Gate 2 (pooled interval).** All three pooled-108 intervals clear CI-LB > 0; panel magnitude **mean
  0.151**, **range [0.139, 0.169]**.
- **The typical-arm magnitude is CROSS-MODEL CONSISTENT (~1.2× spread), unlike the nonce arm.** Pooled
  0.139 / 0.145 / 0.169 span ~1.2× — much tighter than the **~3.6–4×** spread on the *nonce firewall*
  arm (claim fence b). So the size of the animate→s-genitive **preference** on real possessors is
  fairly uniform across the panel (~14–17 points out of 100), even though the shortcut-immune
  *firewall* magnitude decorrelates sharply. This asymmetry is displayed, not averaged.
- **gpt's fresh arm is notably larger than its prior (+0.178 vs +0.120).** The panel's smallest
  prior-72 magnitude comes up on the fresh items; the pooled gpt figure (0.139) sits between. Read as
  sampling variation across item sets, not a trend — the honest reading is the pooled interval.

## What did NOT change (reproduced controls)

- **The covariate is again near-vacuous.** OLS `shift ~ propensity_diff` over the 108 pooled frames
  (merged frozen UD-EWT covariate, base rate s = 0.1786, identical recipe) gives R² **0.001 / 0.006 /
  0.014** (gemini / claude / gpt) with the slope sign flipping across models — the covariate-adjusted
  intercept `b0` (claude 0.142, gemini 0.167, gpt 0.133) ≈ the raw magnitude, all CI-LB>0. Partialling
  out the possessor's marginal genitive propensity changes essentially nothing; the covariate leg is
  **not** independent corroboration (claim fence a), as on both prior runs.
- **The gradient is again a sharp animate/non-animate BINARY.** On the fresh arm, graded monotone
  animate > collective > inanimate is nominally 3/3, but the *collective* mid-level patterns **with the
  inanimate** — collective − inanimate = **+0.026 / +0.028 / +0.052** (gemini / claude / gpt), against
  an animate − inanimate of ~0.13–0.17. The panel draws a sharp animate/non-animate line and treats
  groups-of-humans much like objects, exactly as on s218 + rep2 (claim fence c). The magnitude attached
  is the animate/non-animate one.

## The reviewers' conditions (honoured verbatim)

Both pre-run gates cleared **GO-WITH-CONDITIONS**, all conditions on this write-up, none touching a
frozen artifact or a number (fresh-agent critic
[`REVIEW-critic-s222.md`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-mag/REVIEW-critic-s222.md);
non-Anthropic vote `gpt-5.4-mini` $0.002554
[`VOTE-critic-s222.json`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-mag/VOTE-critic-s222.json)):

- **(a) The pooled-108 CI is a magnitude UPDATE conditional on the already-established direction, not
  an independent estimate.** It is tighter by construction (72/108 frames reused); the **NEW-36 blind
  arm, its CI, and its sign-p are foregrounded** as the genuine fresh check (table left column). Both
  are reported side by side; neither is presented alone.
- **(b) The pooled magnitude is a TYPICAL-arm WITHIN-MODEL quantity and adds NO new surface/lexical-
  confound guarantee on the new items.** This run has **no in-run nonce firewall** (it was dropped:
  the firewall already replicated 3/3 twice, and magnitude is a typical-arm quantity). Robustness to
  surface cues rests on the **prior** firewall + the frozen mechanical certification (all length/
  sibilancy/position/always-s/always-of readers give within-frame shift exactly 0 on these items);
  the residual lexical/semantic animacy confound is undischarged and lives on the claim as **fences
  (e)/(f)**, carried verbatim.
- **(c)** Not triggered — no model's fresh arm is marginal; all three clear CI-LB>0 with decisive
  sign tests, so this is reported as a **clean** attach.
- **(d) Possessum-polysemy caveat.** A few possessums are polysemous in a way that could interact with
  animacy — most notably **t16 "makeup"** ("the cook's makeup" = cosmetics, a very natural alienable-
  possession s-genitive, vs "the makeup of the dock" = composition), and to a lesser degree *state /
  standing / form / mark*. Each is ~1/108 of the pooled estimate (negligible leverage) and the
  paradigm holds the possessum fixed within-frame; flagged, not a defect. Inherent to the byte-frozen
  design that already confirmed twice.

## Method + provenance

- **Items** ([`build_items.py`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-mag/build_items.py),
  certification PASS): 36 fresh typical frames, animate (individual human/animal) / collective (group
  of humans) / inanimate (object/place) possessor, each a definite `the <one-word-noun>`, length-
  matched at 2 tokens, all non-sibilant-final; 108 possessor lemmas, **0 overlap** with the 214 prior
  (check D); no shortcut reader yields any within-frame shift (check 4); candidate vocabulary generated
  blind, animacy classes the lead's judgement (self-audited against Zaenen et al. 2004 via Dubois et
  al. 2023).
- **Covariate** ([`build_cooc_merged.py`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-mag/build_cooc_merged.py)):
  the frozen UD-English-EWT marginal s-genitive propensity recipe (CC BY-SA 4.0; corpus shas match the
  s218/rep2 frozen covariate) over the union of all three arms' lemmas.
- **Run:** 216 trials × 3 models = **648 calls, $0.84203 billed, 0 NA, 0 missing** (liveness $0.0035
  separate). Panel = the standing ratified roster (`claude-sonnet-4.6`, `gpt-5.4-mini`,
  `gemini-3.5-flash`).
- **Post-run verification:** an independent fresh-agent verifier recomputed the pooled and fresh-36
  magnitudes from the raw jsonl with its own script and a different bootstrap seed, and re-checked the
  disjointness, row counts, and billed cost — see the claim's Grounds for the verdict.

## What this result does and does not say

- **Does:** attach a **within-model magnitude** to the genitive possessor-animacy effect — a pooled
  within-frame animate−inanimate s-preference shift of ~**+0.14 to +0.17** per model (108 frames, all
  CI-LB>0), independently reproduced on 36 fresh blind items (CI-LB>0, 3/3). This **lifts claim fence
  (i)** from magnitude-deferred to magnitude-attached.
- **Does NOT:** change the **direction/anchor scope** (the human anchor is a direction only; the
  magnitude is a **within-model** contrast, not a human comparison of sizes — Dubois gives no
  model-scale effect size); defeat the shadow explanation (no in-run firewall; fences e/f live); assert
  a smooth animacy gradient (sharp binary, fence c); or make the replication temporally/version-robust
  (the third arm is again same-date/same-versions, fence h). The direction remains the promoted claim;
  this run sizes it.
