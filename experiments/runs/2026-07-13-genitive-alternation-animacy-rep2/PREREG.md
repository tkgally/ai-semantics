# PREREG — genitive-alternation possessor-animacy probe, REP2 (fresh-item replication, program A5)

**Frozen 2026-07-13 (session 220), before any finding-bearing model call.** This is the **fresh-item
replication** that the s219 promotion review named as the exact strengthening path
([`note/genitive-alternation-animacy-promotion-refusal-v1`](../../../wiki/findings/notes/genitive-alternation-animacy-promotion-refusal-v1.md)):
the s218 line survived its load-bearing shadow control (the nonce firewall, 3/3) but was a **single
run**, and PROTOCOL §3 promotes only **REPLICATED ∧ survived-controls** (conjunctive). A second run on
disjoint items that reproduces the direction + nonce survival clears the replicated conjunct and makes
a **direction-only scoped `claim`** earnable — mirroring the dative's v1+v2 promotion.

**No new decision is opened.** The design was ratified at s218
([`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../../wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md),
ADOPT DEFAULTS Q1-A / Q2-(i) / Q3 human-anchored; freeze conditions B1–B3, S1–S7, R1–R5). This run
re-uses that ratified, byte-frozen instrument on new items — the A2a within-session powered-re-run
pattern (dative s175, sense-gradience s181), which carries a fresh-agent pre-run critic + one
non-Anthropic decorrelation vote but no new cross-session ratification.

Conjecture: [`conjecture/genitive-alternation-animacy`](../../../wiki/findings/conjectures/genitive-alternation-animacy.md).
Human anchor: [`resource/genitive-animacy-human-anchor`](../../../wiki/base/resources/genitive-animacy-human-anchor.md)
(Dubois et al. 2023, 25 native speakers, CC BY 4.0) — **direction only** (animate → s-genitive).

## Frozen artifacts (sha256 — `probe.py full` refuses unless both appear here)

- `stimuli.json`  : `54577d3b39e204b4dd33d609762eae1bdfb0fda3a5a8e4d0108477a1d2b7a478`
- `freq_control.json` : `313d4ba648eec8e20e8fb53615bfca7fcdddff06495dceed5d07ab4dda43cef0`

Built by `build_items.py` (certification PASS, incl. the new disjointness check (D)) and
`build_cooc_gen.py`. Covariate corpus = **UD English-EWT** (CC BY-SA 4.0, LICENSE verified firsthand
s218; s168 UD-treebank rule); per-file sha256 in `freq_control.json.corpus_meta`.

## What is byte-frozen from s218, and the one documented difference

- **Byte-identical (sha-verified):** `probe.py`, `analyze.py`, `build_cooc_gen.py`. The indicator,
  the prompt (`common.SYS`/`USER_TMPL`), the parser, the graded-forced-choice, the resampling unit
  (the frame), the pre-registered verdict rule, and the covariate recipe are all unchanged.
- **`common.py`:** identical **except** the pure-budget constant `HARD_STOP_USD` 1.30 → **1.90**
  (documented in-file), because the item count grew (larger nonce arm ⇒ ~$1.34 expected vs the s218
  ~$1.16). This mirrors the A2a re-run pattern where the frozen instrument differs only in a justified
  constant; it never touches measurement or the frozen stimuli sha.
- **`build_items.py`:** the only substantively new file — it builds the **fresh, disjoint** item set.

## The two item-set changes (and only these)

1. **Fresh, disjoint items.** All 108 typical possessor lemmas and all 36 nonce strings are **disjoint
   from the s218 frozen set** (certification check (D), loaded from the s218 `stimuli.json`: 0 shared
   typical lemmas, 0 shared nonce strings). Possessums are fresh too. A genuine second run on new
   items — never a touch of the frozen s218 dir.
2. **Powered gpt firewall leg.** The nonce arm is enlarged **24 → 36 frames** (derangement offset
   n//2 = 18; multiset-balanced, certified), because the s218 gpt nonce leg was the marginal member
   (mean +0.055, only 16/24 frames positive, one-sided sign-p 0.076 — it cleared the CI-LB rule only
   marginally). 36 paired nonce contrasts give the weak leg's sign test + bootstrap CI more power.
   Typical arm stays 36 frames. 360 trials × 3 models = **1080 calls**.

## Design (one paragraph, unchanged from s218)

Graded forced-choice: hold the possessum fixed, distribute 100 points by naturalness between the
**s-genitive** (*the judge's decision*) and the **of-genitive** (*the decision of the judge*);
s-pref = s_pts/(s_pts+of_pts). Resampling unit = the **frame**. Finding-bearing measure = within-frame
animacy shift `shift(frame) = mean(s-pref | animate) − mean(s-pref | inanimate)`. Human direction ⇒
shift > 0. **36 typical frames** (animate + collective + inanimate) + **36 nonce frames** (animate +
inanimate, orthographically neutralized).

## Shadow control (the crux — B1–B3, R1–R5, unchanged)

1. **NONCE arm = the shortcut-immune PRIMARY control (B1, R1, R3).** Nonce monosyllabic possessors;
   animacy conveyed **only by a gloss** ("a small wild animal called a frab" vs "a hard grey mineral
   called a frab"), never by orthography; the nonce strings are **balanced** so the animate-slot and
   inanimate-slot string multisets are identical (each string once-animate, once-inanimate; certified).
   No per-lemma corpus genitive statistic exists for a nonce possessor. **This arm carries the CONFIRM.**
2. **Frozen marginal-propensity COVARIATE = corroboration (B2, R2, R5).** Per-possessor-lemma marginal
   s-genitive propensity `(s+k·p0)/(s+of+k)` from UD-EWT, partialled out of the typical-arm shift.
   **HONEST POWER NOTE (verified at this freeze):** the covariate is again near-vacuous — only 4/36
   animate and 2/36 inanimate typical lemmas have any corpus genitive, and the mean smoothed propensity
   is essentially flat (animate 0.1728 vs inanimate 0.1760, animate slightly *below*). So partialling it
   out is near-trivial and **CONFIRM rests on the nonce arm**, stated plainly (`analyze.py` reports the
   covariate's own R²).
3. **Certified surface guards.** Within every frame, possessor length + final-sibilancy + definiteness
   are matched across animacy levels and no bare proper-name possessor is used (S1), so length /
   sibilancy / position / always-s / always-of readers yield within-frame shift 0 (certified).

## Pre-registered verdict (B3 — symmetric; a null is first-class; identical rule to s218)

Per model, three conditions: **cond_typ** (typical shift > 0 AND bootstrap 95% LB > 0); **cond_nonce**
(nonce shift > 0 AND bootstrap 95% LB > 0 — the firewall); **cond_cov** (covariate-adjusted intercept
b0 > 0 AND bootstrap 95% LB > 0). Panel:

- **CONFIRM (human-direction):** ≥2/3 meet cond_typ AND ≥2/3 meet cond_nonce AND ≥2/3 meet cond_cov.
  A REPLICATION of the s218 CONFIRM ⇒ the line clears the §3 REPLICATED ∧ controls bar and a
  **direction-only scoped `claim`** becomes earnable (successor: a cross-session promotion review).
  **Interpretation fence (R5):** the control is risk-reducing corroboration, not a proof the
  distributional shadow is defeated; CONFIRM prose stays narrowly directional, no per-item human
  gradient, no human-level claim.
- **SHADOW / ATTENUATED:** ≥2/3 meet cond_typ but the nonce and/or covariate leg fails at ≥2/3 — a
  distributional shadow of possessor genitive-propensity, not animacy tracking (a first-class negative
  that would **contradict** the s218 nonce-survival and block promotion).
- **WEAK:** typical shift > 0 (≥2/3) but not graded.
- **FALSIFY / REVERSAL:** typical shift not > 0 (or reverses) at ≥2/3 — would fail to replicate.

## Replication bar (what this run is judged against)

The s218 result was **CONFIRM 3/3** (typical +0.134/+0.181/+0.141; nonce +0.109/+0.205/+0.055). This
run **replicates** iff it reproduces (a) the animate→s-genitive typical direction (cond_typ ≥2/3) AND
(b) the nonce-firewall survival (cond_nonce ≥2/3), on the disjoint items — the two conjuncts the
promotion turns on. A **direction-only** claim is earnable on replication of the sign + firewall; the
**magnitude** is reported with intervals but (per the dative precedent) is not the promoted quantity.
Carried-forward fences a future claim must state verbatim: covariate vacuity; gpt the weak firewall
leg; the animate/non-animate binary (collective patterns with inanimate), not a smooth Zaenen ramp;
direction-only anchor.

## Primary quantities (95% CI = nonparametric bootstrap over frames)

(1) typical within-frame animacy shift + fraction of frames > 0 + sign test; (2) nonce-arm shift (the
firewall — now 36 frames); (3) covariate-adjusted intercept b0 + covariate b1/R² (its predictive
validity); (4) graded means animate/collective/inanimate (monotonicity, prediction 2); (5) per-model
default s-pref. Point estimate + interval, not a threshold pass.

## Budget (pre-flight)

1080 calls, short forced-choice. At the s218 per-call billed rate (claude/gemini ~$0.0017, gpt
~$0.00034) ≈ **$1.34** billed; pre-registered hard stop **$1.90** (`common.HARD_STOP_USD`), below the
$2.50 single-run prudence flag. Today's UTC-2026-07-13 spend before this run ≈ $1.174 (s217+s218+s219)
+ the pre-run vote; $1.174 + ~$1.34 ≈ $2.51 of the $5.00 UTC cap. Actuals from the returned
`usage.cost`.

## Anti-cheat

Item set + covariate frozen (shas above) before any finding-bearing call; no retuning after seeing
outputs. A null / SHADOW / FALSIFY is a first-class result and would be reported as a failure to
replicate. The predictions.md bet is registered at this freeze, **before** the run (never pre-filled
with an outcome).
