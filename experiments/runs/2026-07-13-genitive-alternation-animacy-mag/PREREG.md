# PREREG — genitive-alternation possessor-animacy, POWERED MAGNITUDE (MAG), program A5

**Frozen 2026-07-13 (session 222), before any finding-bearing model call.** This is the **powered
magnitude re-run** that NEXT.md/s221 named as the promoted claim's own remaining owed unit. The
genitive possessor-animacy line is a **promoted, standing `claim`**
([`claim/genitive-alternation-animacy`](../../../wiki/findings/claims/genitive-alternation-animacy.md),
`status: supported`), but scoped **DIRECTION-ONLY** because both founding runs (s218 + rep2) are
36+36 typical frames, below PROTOCOL §4's powered N (~100–150). This run attaches a **within-model
magnitude + bootstrap interval** by adding a **third disjoint typical arm** and **pooling** the three
(the A2a-merged pattern that attached the dative's magnitude, s175 N=100, and the CC's, s169 N=136).

**No new decision is opened.** The design was ratified at s218
([`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../../wiki/decisions/resolved/genitive-alternation-anchor-and-indicator.md),
ADOPT DEFAULTS Q1-A / Q2-(i) / Q3 human-anchored; freeze conditions B1–B3, S1–S7, R1–R5). This run
re-uses that ratified, byte-frozen **measurement** instrument on new items with a **new pooled
analysis** — the A2a within-session powered magnitude pattern — carrying a fresh-agent pre-run
critic + one non-Anthropic decorrelation vote, but no new cross-session ratification.

Conjecture: [`conjecture/genitive-alternation-animacy`](../../../wiki/findings/conjectures/genitive-alternation-animacy.md).
Human anchor: [`resource/genitive-animacy-human-anchor`](../../../wiki/base/resources/genitive-animacy-human-anchor.md)
(Dubois et al. 2023, 25 native speakers, CC BY 4.0) — **direction only** (animate → s-genitive). The
anchor licenses the *direction*; the *magnitude* this run reports is an **internal within-model**
quantity (Dubois gives no comparable model-scale effect size), so magnitude is reported as a
within-model contrast, not a human-comparison.

## Frozen artifacts (sha256 — `probe.py full` refuses unless both appear here)

- `stimuli.json`  : `01ee7f2b05dd4e6d06c052d3aee09a16b8f0681b9f9fd875ef2a41ef9f833c68`
- `freq_control.json` : `3a80f5fb717999daef72afe238875efdc3c90e0facb6ad5535a782865861a562`

`stimuli.json` built + certified by `build_items.py` (certification PASS; see below).
`freq_control.json` = the **merged** frozen covariate built by `build_cooc_merged.py` (the frozen
`build_cooc_gen.py` recipe, byte-identical, over the UNION of typical possessor lemmas across s218 +
rep2 + mag = 322 lemmas). Covariate corpus = **UD English-EWT** (CC BY-SA 4.0, LICENSE verified
firsthand s218; s168 UD-treebank rule); per-file sha256 in `freq_control.json.corpus_meta`
(train `d68e061…`, dev `39239e0…`, test `fa024f4…`, base rate s = 0.1786 — identical to the s218/rep2
frozen covariate, as the recipe + corpus are unchanged).

## What is byte-frozen from s218/rep2, and the documented differences

- **Byte-identical (sha-verified):** `probe.py`, `build_cooc_gen.py`. The indicator, the prompt
  (`common.SYS` / `USER_TMPL`), the parser, the graded-forced-choice, the resampling unit (the
  frame), and the covariate recipe are all unchanged.
- **`common.py`:** identical **except** the pure-budget constant `HARD_STOP_USD` 1.90 → **1.20**
  (documented in-file), because this arm is typical-only (36 frames × 6 trials × 3 models = 648
  calls, ~$0.81 expected vs rep2's ~$1.34). It never touches measurement or the frozen stimuli sha.
- **`build_items.py`:** builds the **fresh, disjoint, typical-only** item set (36 frames).
- **`build_cooc_merged.py`:** merges the frozen covariate recipe over all three arms' lemmas.
- **`analyze_merged.py`:** the **NEW pre-registered pooling analysis** (below). The frozen
  `analyze.py` computes a single-run verdict; this run's finding is a **pooled magnitude**, so the
  analysis is new. It is frozen here, before any model call, alongside the stimuli.

## The item set (build_items.py — certification PASS)

A **fresh, TYPICAL-ONLY arm of 36 frames** (animate / collective / inanimate possessor, each a
definite `the <one-word-noun>`, length-matched at 2 tokens, all non-sibilant-final). Every possessor
lemma is **DISJOINT from BOTH s218 and rep2** (108 new lemmas, 0 overlap with the 214 prior;
certification check (D)). Candidate vocabulary was generated **blind to model responses**; the
animacy classes and final selection are the lead's judgement, self-audited against the Zaenen et al.
(2004) scheme via Dubois et al. (2023). Certification (identical machinery to rep2): within-frame
length/sibilancy/definiteness matched (1); no proper name (2); all non-sibilant-final (2b); **every
surface shortcut reader — always-s, always-of, position, length, sibilancy — yields within-frame
shift exactly 0** (4); disjointness (D); no internal lemma/possessum repeat (D2/D3); ≥30 typical
frames carrying the collective level (N/S7). **NO NONCE ARM:** the shortcut firewall already
replicated 3/3 twice (s218 CI-LB>0; rep2 gpt leg decisive 25/36, sign-p 0.014). The magnitude the
claim owes is a **typical-arm quantity**; this arm attaches it and does not re-litigate the firewall.

## Pre-registered analysis (analyze_merged.py — frozen here, before any model call)

Resampling unit = the FRAME (ratified S3). Per model, the finding-bearing measure is the within-frame
typical-arm animacy shift `shift(frame) = mean(s-pref | animate) − mean(s-pref | inanimate)`
(averaged over the A/B counterbalance), pooled across the three **mutually disjoint** typical arms:

    s218 (36) + rep2 (36) + mag (36 fresh-blind) = 108 pooled typical frames.

**PRIMARY (headline) — pooled magnitude.** Per model: the pooled-frame **mean shift** = the
within-model magnitude, with a nonparametric bootstrap **95% CI over the 108 frames** + a one-sided
sign test. **Panel readout:** the three per-model magnitudes, their range, and whether every model's
pooled CI lower bound > 0 (direction — already an established claim; the new content is the magnitude
+ interval).

**REPORTED ALONGSIDE (honesty):** the **NEW-36-only** estimate (the magnitude on the never-seen
fresh items alone — the blind check) and the **PRIOR-72-only** estimate (s218 + rep2), so the reader
sees that the pooled interval reuses prior data and can read the fresh-only magnitude on its own.

**CORROBORATION (not headline) — covariate-adjusted magnitude.** OLS `shift = b0 + b1·propensity_diff`
over the 108 pooled frames (`propensity_diff` = merged frozen marginal s-genitive propensity of the
animate minus the inanimate possessor), bootstrap CI on `b0`. Also report `b1`, `R²`. The covariate
was **near-vacuous** in both prior runs (R² ≤ 0.013); if it stays so, `b0 ≈` the raw magnitude and
the headline is the raw pooled shift, stated plainly.

## Pre-registered readout (symmetric — a null/weak result is first-class)

**Amended at freeze by the non-Anthropic decorrelation vote (`gpt-5.4-mini`, GO-WITH-CONDITIONS,
[`VOTE-critic-s222.json`](VOTE-critic-s222.json)), before any model call.** The vote's condition 3 —
"the fresh blind arm should clear a **standalone** positivity criterion before pooling is reported as
the estimate, else the pooled interval is a repackaged direction claim with a tighter interval" — is
adopted; it only makes the bar **harder**, so adopting it pre-run cannot game the result. The pooled
CI is explicitly a **post-hoc conditional update** on the already-established direction, not an
independent estimate (vote condition 1); the pooled interval is **tighter by construction** because
72/108 frames are reused. The magnitude's robustness to surface confounds rests on the **prior**
nonce firewall (replicated 3/3 twice) + the frozen mechanical certification, **not** on any in-run
firewall (vote condition 2, granted).

- **MAGNITUDE ATTACHED** iff **(gate 1, standalone)** the NEW-36 blind arm independently clears
  CI-LB > 0 at ≥2/3 models — the same bar each prior 36-frame typical arm cleared — **AND (gate 2)**
  the pooled-108 CI-LB > 0 at ≥2/3 models. Then the magnitude the claim carries = the per-model
  **pooled** point shifts + intervals + panel range, reported as a conditional update, **with the
  NEW-36-only and PRIOR-72-only estimates shown alongside**.
- **PARTIAL / PROVISIONAL** if the pooled-108 CI-LB > 0 at ≥2/3 but the NEW-36 blind arm is positive
  yet does **not** clear its own CI-LB at ≥2/3 (36 frames underpowered for a tight fresh interval):
  report the pooled magnitude as **provisional**, the fresh arm shown, and the claim's fence (i)
  softened but **not** fully discharged — a larger fully-fresh arm still owed.
- **NO-LIFT** if the NEW-36 fresh arm **reverses** or is non-positive at ≥2/3, or the pooled CI-LB ≤ 0
  at ≥2/3 — the claim stays direction-only and the note records why.

The **direction** is not re-adjudicated here (it is a promoted claim); this run only estimates the
**size** and decides, on the fresh blind arm's standalone behaviour first, whether to attach it.

## Budget

Pre-flight ~**$0.81** billed (648 calls; claude/gemini ~$0.0017, gpt ~$0.00034 per call). UTC
2026-07-13 spend before this run **$2.612545** → projected **~$3.42 of $5.00**; below the $2.50
single-run prudence flag and the $5/day cap. `HARD_STOP_USD = 1.20`. Plus one non-Anthropic
decorrelation vote (~$0.002).
