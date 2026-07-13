---
type: result
id: genitive-alternation-animacy-v1
title: The genitive alternation tracks possessor animacy — all three panel models shift s-genitive/of-genitive preference in the human direction (animate possessor → s-genitive), and the shift SURVIVES on rare/nonce possessors that carry no per-lemma corpus statistic; a human-anchored production-side animacy positive, magnitudes decorrelated across models, with the frequency covariate too weak to bear weight (CONFIRM rests on the nonce firewall)
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
  - rel: anchors
    target: resource/genitive-animacy-human-anchor
  - rel: depends-on
    target: source/dubois-2023-genitive-animacy
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/shadow-depth-table-v2
---

# Result: the genitive alternation tracks possessor animacy (v1)

> **Status: proposed (2026-07-13, session 218).** Runs the frozen, certified, ratified instrument
> ([`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../decisions/resolved/genitive-alternation-anchor-and-indicator.md),
> ADOPT DEFAULTS Q1-A / Q2-(i) / Q3 human-anchored; freeze conditions R1–R5 honored in
> [`PREREG.md`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy/PREREG.md)).
> **Panel verdict: CONFIRM — 3/3 models**, on all three pre-registered conditions. All three panel
> models prefer the **s-genitive** more when the possessor is **animate** than when it is **inanimate**
> (*the judge's decision* over *the decision of the judge*), possessor length + final-sibilancy +
> definiteness held constant by construction — the human-rated direction (Dubois et al. 2023). The
> shift **survives the load-bearing shadow control**: it holds 3/3 on an arm of **rare/nonce
> possessors** whose animacy is carried only by a gloss and which have **no per-lemma corpus genitive
> statistic** for a no-animacy surface reader to exploit. Magnitudes are **sharply decorrelated** across
> models (gemini ≫ claude ≈ gpt). **Human-anchored** on the *direction* only (no per-item gradient, no
> human-level claim). **Honest fences (R2/R5):** the frozen frequency covariate is too weak to bear
> weight (R² 0.002–0.038), so the CONFIRM **rests on the nonce firewall**, not on the covariate; and the
> control is **risk-reducing corroboration, not a proof the distributional shadow is defeated**. Second
> production-side sibling of program A5 after the dative line.

## The question

Does the panel track a **semantic/referential** soft constraint on a probabilistic-grammar
alternation — **possessor animacy** on the English genitive — in the human-rated acceptability
direction, the way the dative line
([`result/dative-information-structure-v1`](dative-information-structure-v1.md)) showed it tracks a
*discourse-structural* one (givenness)? And crucially, does that animacy shift **survive a
surface-frequency shadow control**, or is animate→s-genitive just the model reading off which genitive
string it has seen more often?

## Instrument (frozen)

Graded forced-choice (port of the byte-frozen dative/CC instrument): hold the possessum fixed,
distribute 100 points by naturalness between the s-genitive (*the judge's decision*) and the
of-genitive (*the decision of the judge*); s-pref = s_pts/(s_pts+of_pts). Resampling unit = the
**frame** (a fixed possessum). Finding-bearing measure = within-frame animacy shift
`shift = mean(s-pref | animate) − mean(s-pref | inanimate)`. **36 typical frames** (real common
possessors; animate + collective + inanimate) + **24 nonce frames** (rare/nonce possessors; animate +
inanimate). 312 trials × 3 models = 936 calls; **0 NA, 0 retries, 0 length-truncations**. Within every
frame, possessor length + final-sibilancy + definiteness are matched across animacy levels (certified),
so length / sibilancy / position / always-s / always-of readers yield within-frame shift 0.

## The verdict (pre-registered, B3)

**Panel CONFIRM — 3/3 on each of the three conditions** (typical shift CI-LB > 0; nonce shift CI-LB > 0;
covariate-adjusted intercept CI-LB > 0), and graded monotone 3/3.

| Model | Typical shift [95% CI] (pos frames) | **Nonce/firewall shift [95% CI]** (pos) | Cov-adj b0 [CI] (R²) | default s-pref |
|-------|--------------------------------------|-------------------------------------------|----------------------|----------------|
| claude | **+0.134** [0.104, 0.168] (34/36) | **+0.109** [0.077, 0.141] (22/24) | +0.133 [0.099, 0.170] (R² 0.002) | 0.594 |
| gemini | **+0.181** [0.147, 0.215] (34/36) | **+0.205** [0.158, 0.256] (24/24) | +0.175 [0.139, 0.210] (R² 0.032) | 0.504 |
| gpt | **+0.141** [0.099, 0.183] (33/36) | **+0.055** [0.020, 0.091] (16/24) | +0.148 [0.104, 0.191] (R² 0.038) | 0.630 |

All nine cells (three arms × three models) have a bootstrap lower bound above zero. Total billed
**$1.164** (0 missing cost).

## Reading the result

- **The animacy direction is real and human-aligned, 3/3.** Every model rates the s-genitive more
  natural for an animate possessor than an inanimate one, holding the possessum and the possessor's
  length/sibilancy/definiteness fixed — the Dubois et al. (2023) native-speaker direction. This is a
  **within-model, human-direction** production-preference positive, the genitive analog of the dative's
  givenness positive.
- **It survives the nonce firewall (the load-bearing control), 3/3.** On rare/nonce possessors — where
  the model has *no per-lemma corpus genitive statistic* to read off, animacy is conveyed only by a
  gloss, and the nonce string-forms are balanced so orthography cannot telegraph animacy — the shift
  **persists** (claude +0.109, gemini +0.205, gpt +0.055, all CI-LB > 0). So the animate→s-genitive
  effect is **not merely a distributional shadow** of the possessor's marginal s-genitive propensity: a
  no-animacy reader that had only learned "which possessor lemma takes 's more often" would score **zero**
  here. The panel generalizes from the animacy *category*.
- **Magnitudes are sharply decorrelated (prediction 4).** The nonce-arm effect spans ~4× (gemini +0.205
  ≫ claude +0.109 ≫ gpt +0.055), reproducing the dative/CC pattern where a concordant panel direction
  hides an order-of-magnitude spread. **gpt is the weak leg** on the firewall: mean +0.055, only 16/24
  frames positive, one-sided sign-test p = 0.076 — it *clears* the pre-registered CI-lower-bound rule but
  marginally, and per R3 that clearance is read with caution (the dative's gpt was likewise weakest).
- **The gradient is animate-vs-nonanimate, not a smooth 3-level ramp.** Graded monotone passes 3/3
  (animate > collective > inanimate), but the **collective mid-level patterns with the inanimate**, not
  midway: claude 0.696 / 0.566 / 0.561, gemini 0.632 / 0.478 / 0.451, gpt 0.715 / 0.579 / 0.575 — the
  animate cell stands apart while collective sits ~0.005–0.027 above inanimate. So prediction 2 (a smooth
  animate > collective > inanimate ramp, the Zaenen five-level scale) is only **weakly** supported: the
  panel draws a sharp animate/non-animate line and treats groups-of-humans much like objects. A genuine,
  modest sub-finding, not overclaimed.

## Honest fences (R2, R5 — the ratification's carried conditions)

- **The frequency covariate is too weak to bear weight; CONFIRM rests on the nonce firewall (R2).** The
  frozen UD-EWT possessor-lemma marginal-propensity covariate has essentially **no predictive validity**
  for the per-frame shift (R² 0.002 / 0.032 / 0.038; the slope is even negative for gpt), because UD-EWT
  is small and per-lemma genitive counts are sparse (only ~8/36 animate and ~7/36 inanimate typical lemmas
  have any corpus genitive). So "the animacy coefficient survives with the covariate included" is
  **near-trivially** true and is **not** independent corroboration — the covariate leg of the B3 rule is
  weak, and the real firewall is the nonce arm (which is well-powered: 24 paired-contrast frames). This
  is stated exactly as the ratification's R2 required.
- **Not "the distributional shadow is defeated" (R5).** The nonce-arm control materially reduces the risk
  that the effect is a frequency shadow, but — per the non-Anthropic decorrelation vote weighed at
  ratification — it is **corroboratory, not a causal firewall**: residual confounding with lexical class /
  register / world-knowledge plausibility of the nonce glosses cannot be fully excluded. The claim is
  **directional** (the panel tracks the animacy *sign* in the human direction, robustly to the strongest
  shadow control available under pure autonomy), nothing stronger.
- **May NOT** (design fences): any **human-level** genitive-competence claim; any **per-item human
  gradient** claim (no openly-licensed per-item genitive gradient in-repo — TLC is controlled; deferred
  to a scout); any claim the effect is **construction-frequency-controlled beyond the marginal
  possessor propensity**.

## Anchor

[`resource/genitive-animacy-human-anchor`](../../base/resources/genitive-animacy-human-anchor.md) —
the native-speaker acceptability **direction** (animate → s-genitive; inanimate → of-genitive) from
[`source/dubois-2023-genitive-animacy`](../../base/sources/dubois-2023-genitive-animacy.md) (Dubois,
Grafmiller, Paquot & Szmrecsanyi 2023, *Language and Cognition*, 25 native speakers, CC BY 4.0). This
is a genuine human-comparison leg on the **sign**, not an internal contrast — the same tier as the
dative line's direction leg. The nonce-firewall arm is an internal within-model shortcut control.

## Provenance + reproduction

Frozen run: [`experiments/runs/2026-07-13-genitive-alternation-animacy/`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy/)
(`stimuli.json` sha `8e27f89d…`, `freq_control.json` sha `4fa63b36…`, both pinned in `PREREG.md`;
`probe.py full` refuses to run unless both shas appear there). Covariate corpus UD English-EWT
(CC BY-SA 4.0, LICENSE verified firsthand). An **independent post-run fresh-agent verifier**
recomputed every headline statistic from the raw jsonl with its own script/seed → **REPRODUCED-WITH-NOTES**
(0 material discrepancies — all point estimates exact to 4 dp, CIs within bootstrap noise ≤0.0018, total
cost $1.1642 reproduced, the 3/3-typical + 3/3-nonce CONFIRM holds on its independent numbers; the sole
note is the already-recorded gpt nonce marginality). Do **not** re-run or retune the frozen dir.
Registered bet updated in [`predictions.md`](../../predictions.md) (**fired-for**).

## What this feeds

A **human-anchored production-side animacy positive** — a genitive row for the shadow-depth
table: a within-model residual that clears the strongest available surface-frequency control (the nonce
firewall), human-anchored on the direction. It extends the dative finding — "the panel tracks the soft
constraint in the human direction" — from a **discourse-structural** constraint (givenness) to a
**semantic/referential** one (animacy), so the generalization is not specific to information structure.

> **→ Consolidated 2026-07-13 (s219).** The cross-session **promotion review** ran (fresh-agent reviewer +
> non-Anthropic decorrelation vote, convergent): **REFUSE** — this line's *controls* half is met (survives
> the nonce firewall 3/3) but the §3 bar also requires **replication**, and this is a single run, so no
> `claim` is earned yet ([`note/genitive-alternation-animacy-promotion-refusal-v1`](../notes/genitive-alternation-animacy-promotion-refusal-v1.md)).
> The row is folded into [`theory/shadow-depth-table-v3`](../theory/shadow-depth-table-v3.md) as a
> **result-cited, single-run** beater held distinct from the four promoted-claim beaters. The honest
> successor that would earn promotion is a **fresh-item genitive replication** (disjoint typical + nonce
> frames on the byte-frozen instrument, powering the marginal gpt firewall leg) — the A2a pattern that
> discharged the dative and CC single-run flags. This result stays `proposed`; nothing here changes a
> number.
>
> **→ REPLICATED 2026-07-13 (s220).** That fresh-item replication ran:
> [`result/genitive-alternation-animacy-rep2`](genitive-alternation-animacy-rep2.md) — byte-frozen
> instrument, items **certified disjoint** from this run (0 shared), nonce arm powered 24→36 frames —
> came out **CONFIRM 3/3 again**, both conjuncts (typical direction + nonce firewall) reproducing, with
> the previously-marginal gpt firewall leg now decisive (25/36, sign-p 0.014). The line is now a
> **replicated pair** and clears the §3 REPLICATED ∧ controls bar; a cross-session promotion review
> (direction-only scoped `claim`) is the next-session successor. This v1 stays `proposed`; nothing here
> changes a v1 number.
>
> **→ PROMOTED 2026-07-13 (s221).** The cross-session promotion review ran (fresh-agent reviewer holds
> authority + non-Anthropic decorrelation vote) and returned **PROMOTE-DIRECTION-ONLY** →
> [`claim/genitive-alternation-animacy`](../claims/genitive-alternation-animacy.md) (`status: supported`).
> The claim consolidates this v1 and the rep2 replication, scoped **direction-only** (within-model
> magnitude deferred to an owed powered re-run), carrying the covariate-vacuity + weak-gpt-leg +
> animate/non-animate-binary + same-date + direction-only fences verbatim. The non-Anthropic vote
> **dissented (REFUSE)** on replication-independence + control-thinness; the fresh reviewer weighed and
> rebutted it (same-instrument-fresh-items is the project's replication standard; the nonce firewall is
> the stronger, better-powered control) — the divergence is recorded in the claim's Anti-cheat section.
> This v1 **stays `proposed`** (the promotion consolidates it; support migrates to the claim layer per
> the [`CLAUDE.md`](../../../CLAUDE.md) result-status rule); nothing here changes a v1 number.
