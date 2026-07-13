# PREREG — genitive-alternation possessor-animacy probe (program A5, session 218)

**Frozen 2026-07-13 (session 218), after ratification, before any finding-bearing model call.**
Ratified design: [`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../../wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md)
(ADOPT DEFAULTS Q1-A possessor animacy / Q2-(i) graded forced-choice + both shadow controls / Q3
human-anchored on the direction; + freeze conditions B1–B3, S1–S7, R1–R5). Conjecture:
[`conjecture/genitive-alternation-animacy`](../../../wiki/findings/conjectures/genitive-alternation-animacy.md).
Human anchor: [`resource/genitive-animacy-human-anchor`](../../../wiki/base/resources/genitive-animacy-human-anchor.md)
(Dubois et al. 2023, 25 native speakers, CC BY 4.0) — **direction only** (animate → s-genitive).

## Frozen artifacts (sha256 — `probe.py full` refuses unless both appear here)

- `stimuli.json`  : `8e27f89da365ca73c8a214b0f516c95266e324ffd15558ea69fca7f11a3ffee4`
- `freq_control.json` : `4fa63b3636a65ffd76ae67b0eba3f2d0f070ced365a1d2efe142eebaf5f16f8f`

Built by `build_items.py` (certification PASS) and `build_cooc_gen.py`. The covariate corpus is
**UD English-EWT** (CC BY-SA 4.0, LICENSE.txt "Attribution-ShareAlike 4.0 International" verified
firsthand this session; in scope under the s168 UD-treebank rule); per-file sha256 recorded in
`freq_control.json.corpus_meta`.

## Design (one paragraph)

Graded forced-choice (port of the byte-frozen dative/CC instrument): hold the possessum fixed,
distribute 100 points by naturalness between the **s-genitive** (*the judge's decision*) and the
**of-genitive** (*the decision of the judge*); s-pref = s_pts/(s_pts+of_pts). The resampling unit is
the **frame** (a fixed possessum, critic S3). Finding-bearing measure = the within-frame animacy
shift `shift(frame) = mean(s-pref | animate) − mean(s-pref | inanimate)`. Human direction ⇒ shift > 0.
**36 typical frames** (real common possessors; animate + collective + inanimate levels) + **24 nonce
frames** (rare/nonce possessors; animate + inanimate levels). 312 trials × 3 models = **936 calls**.

## Shadow control (the crux — B1–B3, R1–R5)

1. **NONCE arm = the shortcut-immune PRIMARY control (B1, R1, R3).** 24 frames whose possessors are
   nonce monosyllables; animacy is conveyed **only by a gloss** ("a small wild animal called a narb"
   vs "a hard grey mineral called a narb"), never by the string's orthography. The nonce strings are
   **balanced** so the multiset filling animate slots exactly equals the multiset filling inanimate
   slots (each string once-animate, once-inanimate; certified). A nonce possessor has **no per-lemma
   corpus genitive statistic**, so a no-animacy marginal-frequency reader (or an orthographic
   animacy-form reader) cannot score a spurious shift here. **This arm carries the CONFIRM.**
2. **Frozen marginal-propensity COVARIATE = corroboration (B2, R2, R5).** One exact sha'd recipe:
   per-possessor-lemma marginal s-genitive propensity `(s+k·p0)/(s+of+k)` from UD-EWT. `analyze.py`
   partials it out of the typical-arm shift (OLS intercept b0). **HONEST POWER NOTE:** UD-EWT is
   small and per-lemma genitive counts are sparse (only ~8/36 animate and ~7/36 inanimate typical
   lemmas have any corpus genitive; the animate/inanimate mean smoothed-propensity gap is small), so
   this covariate is **weak**. `analyze.py` reports its **own predictive validity** (slope b1, R²): if
   it barely predicts the per-frame shift, partialling it out is near-vacuous and **CONFIRM rests on
   the nonce arm** — stated plainly (R2 + the non-Anthropic vote's "corroboratory, not definitive").
3. **Certified surface guards.** Within every frame, possessor length + final-sibilancy + definiteness
   are matched across animacy levels and no bare proper-name possessor is used (S1), so length /
   sibilancy / position / always-s / always-of readers yield within-frame shift 0 (certified). The
   marginal-frequency reader is deliberately **not** covered by construction (S4) — controls 1+2 cover it.

## Pre-registered verdict (B3 — symmetric; a null is first-class)

Per model, three conditions: **cond_typ** (typical shift > 0 AND bootstrap 95% LB > 0); **cond_nonce**
(nonce shift > 0 AND bootstrap 95% LB > 0 — the firewall); **cond_cov** (covariate-adjusted intercept
b0 > 0 AND bootstrap 95% LB > 0). Panel:

- **CONFIRM (human-direction):** ≥2/3 models meet cond_typ **AND** ≥2/3 meet cond_nonce **AND** ≥2/3
  meet cond_cov → a human-anchored production-side animacy positive; a genitive row for the
  shadow-depth table. **Interpretation fence (R5):** the control is risk-reducing corroboration, not a
  proof the distributional shadow is defeated; CONFIRM prose stays narrowly directional and must not
  imply a per-item human-gradient match nor human-level competence.
- **SHADOW / ATTENUATED:** ≥2/3 meet cond_typ but the nonce and/or covariate leg fails at ≥2/3 → a
  distributional shadow of possessor genitive-propensity, not animacy tracking (a first-class negative).
- **WEAK:** typical shift > 0 (≥2/3) but not graded (animate > collective > inanimate fails).
- **FALSIFY / REVERSAL:** typical shift not > 0 (or reverses) at ≥2/3.

## Primary quantities (95% CI = nonparametric bootstrap over frames)

(1) typical within-frame animacy shift + fraction of frames > 0 + sign test; (2) nonce-arm shift
(the firewall); (3) covariate-adjusted intercept b0 + covariate b1/R² (its predictive validity);
(4) graded means animate/collective/inanimate (monotonicity, prediction 2); (5) per-model default
s-pref. Point estimate + interval, not a threshold pass.

## What this run may / may NOT claim

- **May:** a within-model, human-direction claim that the panel's genitive preference does / does not
  shift toward the s-genitive for animate possessors, with magnitudes + intervals, and whether it
  survives the nonce-arm shortcut control.
- **May NOT:** human-*level* genitive competence; "distributional shadow defeated" (R5 — the control is
  corroboratory); any per-item human-gradient claim (no openly-licensed per-item genitive gradient
  in-repo — deferred to a scout).

## Registered sensitivity check (S5/viii — deferred)

A separate-single-variant rating pass (Option ii — rate each phrasing 0–100 independently), which
mirrors Dubois' actual task, is **registered here** as a follow-up sensitivity check to run only if
this forced-choice primary CONFIRMs (a convergent direction on it would strengthen the human anchor).
Not run this session (scope/spend); its omission changes nothing about the primary verdict.

## Budget (pre-flight)

936 calls, short forced-choice. At observed dative/CC forced-choice prices ≈ **$0.35–0.70** billed;
pre-registered hard stop **$1.30** (`common.HARD_STOP_USD`), below the $2.50 single-run flag and the
$5/day UTC cap (today's UTC-2026-07-13 spend before the full run ≈ $0.005: ratify vote $0.002129 +
liveness $0.00346). Actuals from the returned `usage.cost`.

## Anti-cheat

Item set + covariate frozen (sha above) before any finding-bearing call; no retuning after seeing
outputs. A null / SHADOW is a first-class result. The predictions.md bet is registered at this freeze,
before the run (never pre-filled with an outcome).
