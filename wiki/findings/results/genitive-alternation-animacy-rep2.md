---
type: result
id: genitive-alternation-animacy-rep2
title: The genitive alternation tracks possessor animacy — REPLICATED on fresh, disjoint items (second run, session 220); PANEL CONFIRM 3/3 again on the typical animate→s-genitive direction AND the nonce firewall, and the previously-marginal gpt firewall leg now clears its sign test decisively (25/36, p=0.014) with the nonce arm powered 24→36 frames; the covariate is again near-vacuous (CONFIRM again rests on the nonce firewall) and the gradient is again an animate/non-animate binary — the two conjuncts a promotion turns on both reproduce, clearing the §3 REPLICATED ∧ controls bar
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
    target: result/genitive-alternation-animacy-v1
  - rel: anchors
    target: resource/genitive-animacy-human-anchor
  - rel: depends-on
    target: source/dubois-2023-genitive-animacy
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/shadow-depth-table-v3
---

# Result: the genitive alternation tracks possessor animacy — REPLICATED on fresh items (rep2)

> **Status: proposed (2026-07-13, session 220).** The **fresh-item replication** of the s218
> genitive-animacy line ([`result/genitive-alternation-animacy-v1`](genitive-alternation-animacy-v1.md)),
> the A2a powered-re-run pattern the s219 promotion review named as the exact path that would earn a
> `claim` ([`note/genitive-alternation-animacy-promotion-refusal-v1`](../notes/genitive-alternation-animacy-promotion-refusal-v1.md)).
> The byte-frozen s218 instrument (probe/parser/analysis sha-identical) was run on a **new item set
> whose every typical possessor lemma and every nonce string is certified disjoint from s218** (0
> shared), with the nonce arm **enlarged 24→36 frames to power the previously-marginal gpt firewall
> leg**. **Panel verdict: CONFIRM — 3/3 again**, on all three pre-registered conditions. The two
> conjuncts a promotion turns on **both reproduce**: the typical animate→s-genitive direction (3/3,
> CI-LB > 0) AND the nonce-firewall survival (3/3, CI-LB > 0) — and the **gpt firewall leg, marginal
> at s218 (sign-p 0.076), now clears its sign test decisively (25/36, p = 0.014)**. The honest fences
> reproduce too: the frequency covariate is again near-vacuous (R² ≤ 0.013), so CONFIRM **again rests
> on the nonce firewall**, and the gradient is again an **animate/non-animate binary** (collective
> patterns with inanimate). So the line now clears the PROTOCOL §3 **REPLICATED ∧ controls-survived**
> bar; a cross-session promotion review (a **direction-only scoped `claim`**) is the successor.

## What this run is, and why it exists

The s218 result was a clean CONFIRM 3/3 that survived its load-bearing shadow control (the nonce
firewall), but it was a **single run**, and PROTOCOL §3 promotes a result to a standing `claim` only
when it has **REPLICATED ∧ survived its controls** — conjunctive. The s219 promotion review therefore
returned **REFUSE** and named the exact strengthening probe: one fresh-item replication of the frozen
instrument on disjoint frames, targeting the weak point (the gpt nonce leg). This is that run.

- **Byte-frozen instrument.** `probe.py`, `analyze.py`, `build_cooc_gen.py` are sha256-identical to
  s218; `common.py` differs only in the budget constant `HARD_STOP_USD` (1.30→1.90, larger item set).
  The indicator, prompt, parser, resampling unit (the frame), verdict rule (B3), and covariate recipe
  are unchanged.
- **Fresh, disjoint items.** 36 typical frames (real possessors, animate/collective/inanimate) + 36
  nonce frames (rare/nonce possessors, animate/inanimate, animacy by gloss only, orthographically
  neutralized). All 108 typical possessor lemmas and all 36 nonce strings are **certified disjoint**
  from s218 (`certification.json` check (D): 0 shared). 360 trials × 3 models = 1080 calls; **0 NA, 0
  length-truncations, 1 retry** (gemini, resolved).
- **Powered gpt firewall leg.** The nonce arm is enlarged 24→36 frames (multiset-balanced, offset
  n//2=18), because in s218 the gpt nonce leg was the marginal member (+0.055, 16/24, sign-p 0.076).

## The verdict (pre-registered, B3) — PANEL CONFIRM 3/3, replicating s218

| Model | Typical shift [95% CI] (pos) | **Nonce/firewall shift [95% CI]** (pos, sign-p) | Cov-adj b0 [CI] (R²) | default s-pref |
|-------|------------------------------|-------------------------------------------------|----------------------|----------------|
| claude | **+0.146** [0.106, 0.189] (33/36) | **+0.151** [0.124, 0.179] (36/36, p 0.000) | +0.144 [0.102, 0.184] (R² 0.013) | 0.579 |
| gemini | **+0.150** [0.098, 0.205] (29/36) | **+0.279** [0.226, 0.330] (35/36, p 0.000) | +0.150 [0.092, 0.204] (R² 0.000) | 0.468 |
| gpt | **+0.099** [0.055, 0.142] (27/36) | **+0.078** [0.043, 0.113] (25/36, **p 0.014**) | +0.098 [0.048, 0.140] (R² 0.001) | 0.636 |

All nine cells (three arms × three models) have a bootstrap lower bound above zero, and graded
monotone (animate > collective > inanimate) passes 3/3. Total billed **$1.431** (0 missing cost).

*s218 for comparison:* typical +0.134/+0.181/+0.141; nonce +0.109/+0.205/**+0.055** (gpt 16/24, p 0.076).

## Reading the replication

- **Both promotion-bearing conjuncts reproduce, 3/3.** The typical animate→s-genitive direction holds
  (claude +0.146, gemini +0.150, gpt +0.099, all CI-LB > 0), and — the load-bearing control — the
  **nonce firewall holds** (claude +0.151, gemini +0.279, gpt +0.078, all CI-LB > 0). On rare/nonce
  possessors with no per-lemma corpus statistic and animacy carried only by a gloss, the shift
  persists on **new** items. This is a genuine second observation of the s218 effect on a disjoint
  frame set, not a re-run of the same items.
- **The powering worked: the gpt firewall leg is no longer marginal.** s218's gpt nonce leg cleared
  the CI-LB rule but only marginally (16/24 frames, one-sided sign-p 0.076). With the nonce arm
  enlarged to 36 frames, rep2's gpt nonce leg is **+0.078, 25/36 frames positive, sign-p 0.014** — a
  decisive sign test. The member most likely to flicker (the dative's gpt-at-founding-N pattern)
  clears robustly on the powered arm. gpt's *typical* shift is a touch lower here (+0.099 vs s218
  +0.141) but still CI-LB > 0 — within the run-to-run band, and gpt remains the weakest leg.
- **Magnitudes are again sharply decorrelated (prediction 4).** The nonce-arm effect spans ~3.6×
  (gemini +0.279 ≫ claude +0.151 ≫ gpt +0.078), reproducing the s218 gemini ≫ claude ≈ gpt pattern —
  a concordant panel *direction* over an order-of-magnitude spread ([`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)).
  gemini's nonce shift is even larger here (+0.279 vs s218 +0.205).
- **The gradient is again an animate/non-animate binary, not a smooth ramp.** Graded monotone passes
  3/3, but the **collective mid-level again patterns with the inanimate**, not midway: claude
  0.654 / 0.541 / 0.508, gemini 0.539 / 0.405 / 0.389, gpt 0.671 / 0.597 / 0.572 — animate stands
  apart, collective sits ~0.02–0.03 above inanimate. So the panel draws a sharp animate/non-animate
  line and treats groups-of-humans much like objects, exactly as at s218. Prediction 2 (a smooth
  Zaenen five-level ramp) is only weakly supported, on both runs.

## Honest fences (reproduced from s218 — a future claim must carry these verbatim)

- **The frequency covariate is again too weak to bear weight; CONFIRM rests on the nonce firewall
  (R2).** On the fresh typical lemmas the frozen UD-EWT marginal-propensity covariate again has
  essentially no predictive validity (R² 0.013 / 0.000 / 0.001; slopes negative), because UD-EWT is
  small and per-lemma genitive counts are sparse (only 4/36 animate and 2/36 inanimate typical lemmas
  have any corpus genitive; animate mean propensity 0.173 sits slightly *below* inanimate 0.176). So
  cond_cov passing is near-trivial (b0 ≈ the raw typical shift) and is **not** independent
  corroboration — the real firewall is the nonce arm.
- **Not "the distributional shadow is defeated" (R5).** The nonce firewall materially reduces the risk
  that the effect is a frequency shadow, but it is **corroboratory, not a causal firewall**: the
  animal-vs-mineral gloss that carries animacy also varies concreteness / taxonomic class /
  plausibility, so residual confounding of the gloss semantics with animacy cannot be fully excluded —
  a point the s220 non-Anthropic pre-run vote raised and the fresh-agent critic weighed (both
  converging that it is the already-ratified R5 fence, not a fixable defect within a *replication*,
  since the gloss is part of the byte-frozen instrument). The claim is **directional** — the panel
  tracks the animacy *sign* in the human direction, robustly to the strongest shadow control available
  under pure autonomy — nothing stronger.
- **May NOT** (design fences, unchanged): any **human-level** genitive-competence claim; any **per-item
  human gradient** claim (no openly-licensed per-item genitive gradient in-repo); any claim the effect
  is construction-frequency-controlled beyond the marginal possessor propensity.

## Anchor

[`resource/genitive-animacy-human-anchor`](../../base/resources/genitive-animacy-human-anchor.md) —
the native-speaker acceptability **direction** (animate → s-genitive; inanimate → of-genitive) from
[`source/dubois-2023-genitive-animacy`](../../base/sources/dubois-2023-genitive-animacy.md) (Dubois,
Grafmiller, Paquot & Szmrecsanyi 2023, *Language and Cognition*, 25 native speakers, CC BY 4.0). A
genuine human-comparison leg on the **sign** (direction-only), the same tier as the dative line's
direction leg; the nonce-firewall arm is an internal within-model shortcut control.

## Provenance + reproduction

Frozen run: [`experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/)
(`stimuli.json` sha `54577d3b…`, `freq_control.json` sha `313d4ba6…`, both pinned in `PREREG.md`;
`probe.py full` refuses unless both shas appear there). Pre-run gates: fresh-agent critic **GO**
([`REVIEW-critic-s220.md`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy-rep2/REVIEW-critic-s220.md))
+ non-Anthropic decorrelation vote GO-WITH-CONDITIONS (the R5 gloss fence). Covariate corpus UD
English-EWT (CC BY-SA 4.0, LICENSE verified firsthand). An **independent post-run fresh-agent verifier**
recomputed every headline statistic from the raw jsonl with its own script and a different bootstrap
seed (99887766 vs analyze.py's 20260713) → **REPRODUCED** (0 discrepancies: all point estimates match
to 4 decimals; CI bounds differ only at the 3rd–4th decimal by seed noise; panel CONFIRM 3/3 holds on
its independent numbers; billed cost $1.431107 matched exactly; 0 NA / 1 retry / 0 length-truncations
confirmed; the over-claim check confirmed genuine replication of both conjuncts + the powered gpt leg +
the covariate-vacuity and animate/non-animate-binary fences). Registered replication bet updated in
[`predictions.md`](../../predictions.md) (**fired-for**). Do **not** re-run or retune the frozen dir.

## What this feeds

The genitive-alternation animacy line is now a **replicated pair** (s218 + this rep2), both CONFIRM
3/3, with the nonce firewall surviving on two disjoint item sets and the previously-weak gpt leg now
decisive on the powered arm. This clears the PROTOCOL §3 **REPLICATED ∧ controls-survived** bar that
the s219 review found unmet. The honest successor is a **cross-session promotion review** (independent,
adversarial, with a non-Anthropic decorrelation vote) that would write a **direction-only scoped
`claim`** — mirroring the dative's v1+v2 promotion, carrying the covariate-vacuity + gpt-weak-leg +
animate/non-animate-binary + direction-only fences forward verbatim. It also extends the dative
finding from a **discourse-structural** soft constraint (givenness) to a **semantic/referential** one
(animacy), now on two runs — a second production-side alternation where the panel tracks the human
direction. Enters the shadow-depth table ([`theory/shadow-depth-table-v3`](../theory/shadow-depth-table-v3.md))
as the genitive beater row, updated in-place from single-run to **replicated** (still result-cited
until the promotion review lands a claim).
