---
type: result
id: dais-graded-preference-correlation-rep2
title: "DAIS-anchored graded-preference correlation, fresh-item REP2 — the verb-bias leg REPLICATES (3/3, all conjuncts, on fully disjoint stimuli), and the definiteness/length band is shown to be filler-UNSTABLE across runs (s248 LENGTH-ONLY → rep2 TRACKS-HUMAN-SURFACE). VERB-BIAS-REPLICATES licenses the cross-session promotion review of the verb-bias correspondence; the definiteness/length leg is NOT promoted"
meaning-senses:
  - constructional
  - distributional
  - human-comparison
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-18
updated: 2026-07-18
links:
  - rel: operationalizes
    target: conjecture/dative-alternation-information-structure
  - rel: anchors
    target: resource/dais-dative-ratings
  - rel: depends-on
    target: design/dais-graded-preference-correlation-v1
  - rel: depends-on
    target: result/dais-graded-preference-correlation-v1
  - rel: supports
    target: result/dais-graded-preference-correlation-v1
---

# DAIS-anchored graded-preference correlation — fresh-item REP2 (s250)

> **Ran s250 (2026-07-18). Single fresh-item replication of [`result/dais-graded-preference-correlation-v1`](dais-graded-preference-correlation-v1.md) (s248) → `proposed`.**
> The instrument is **byte-frozen** (`probe.py` / `analyze.py` sha256-identical to s248; `common.py`
> differs only in two budget hard-stops); the **only** change is the project fillers — a fresh subject
> (`Priya`), fresh recipient realizations (`them / the clerk / a clerk / the clerk from downtown / a
> clerk from downtown`), 10 fresh theme nouns, and a fresh Arm-B verb subset (0/40 shared with v1). Two
> disjointness firewalls PASS: 0 verbatim vs DAIS's released sentences AND 0 vs the s248 v1 stimuli. The
> human anchor ([`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md); Hawkins,
> Yamakoshi, Griffiths & Goldberg 2020; CC BY 4.0) is byte-identical to v1 (same ratings — only the
> model-side items are fresh). 1,200 calls, 0 NA, $1.85321; freeze `PREREG.md` sha
> `a5779f04…`; pre-run critic (verdict authority) **GO** + non-Anthropic vote **NO-GO** with three
> tightening conditions **folded pre-data** (Arm-B verbs made v1-disjoint; R3 tightened to
> point-in-v1-CI; promotion-non-automatic wording); post-run verifier **REPRODUCED**.
>
> **SCOPE FENCE (load-bearing — carried verbatim from s248).** A **bare** (no-discourse-context) graded
> DO-preference correlated against DAIS's definiteness/length + verb-bias surface. It is **NOT** a
> human-effect-size comparison for the discourse-context **givenness shift**
> ([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)),
> which has no human effect-size anchor by design and is **untouched** here.
>
> **TWO HEADLINES.** (1) **The Arm-A verb-bias correspondence REPLICATES — 3/3 on all three conjuncts,
> on fully disjoint fresh items** → licenses the cross-session promotion review (conducted this session).
> (2) **The Arm-B definiteness/length band is filler-UNSTABLE**: s248 read LENGTH-ONLY, rep2 reads
> TRACKS-HUMAN-SURFACE — two single runs, opposite bands. The honest reading is *under-determination*,
> **not** that TRACKS is now the answer; the definiteness/length leg is **NOT** promoted.

## Headline 1 — the verb-bias correspondence REPLICATES (the promotable leg)

Per-verb model DO-preference at the canonical `shortDefinite` condition vs the human per-verb mean
`DOpreference` at the matched condition, Spearman ρ over 200 verbs, with the **binding** alternating-only
control (B2). The frozen replication predicate (`replication_check.py`, committed before any model call):
per model, then ≥2/3 — **R1** rep2 matched-ρ CI-LB > 0; **R2** rep2 alternating-only ρ CI-LB > 0; **R3**
rep2 matched-ρ **point estimate ∈ v1's 95% CI** (the sense-gradience-rep2 "within v1's CI" standard,
tightened pre-data from CI-overlap per the freeze vote).

| model | v1 matched ρ (s248) [95% CI] | **rep2 matched ρ** [95% CI] | R3 (rep2 point ∈ v1 CI) | rep2 alt-only ρ (n=100) | R2 (CI-LB>0) | rep2 partial ρ |
|---|---|---|---|---|---|---|
| claude | +0.608 [+0.501,+0.700] | **+0.684 [+0.600,+0.755]** | ✓ | +0.630 | ✓ | +0.526 |
| gemini | +0.763 [+0.683,+0.825] | **+0.815 [+0.761,+0.858]** | ✓ | +0.691 | ✓ | +0.666 |
| gpt | +0.628 [+0.542,+0.702] | **+0.701 [+0.627,+0.761]** | ✓ (near boundary: +0.701 vs +0.702) | +0.539 | ✓ | +0.524 |

- **VERB-BIAS-REPLICATES = True (3/3 on R1 ∧ R2 ∧ R3).** Every rep2 per-verb ρ lands inside the s248 95%
  CI (magnitude-consistent), clears CI-LB > 0 (the correspondence exists on fresh items), and the binding
  alternating-only control survives on all three (the correspondence is **not** merely the memorizable
  alternating/non-alternating lexical-subcategorization split — there is a graded per-verb rank
  correspondence *within* the alternating class, in **both** runs). **No contamination ceiling** (max ρ
  0.815 < 0.95). gpt's R3 is a **near-boundary** pass (+0.701 vs v1 upper +0.702) — noted, not hidden:
  its rep2 ρ is slightly higher than v1's but within the interval.
- **Cross-model spread reproduces:** gemini (+0.82) > gpt (+0.70) ≈ claude (+0.68), matching v1's ordering
  (gemini > gpt ≈ claude); a within-panel observation, not a model ranking.
- **What "replicates" means here (bounded).** ρ is a **rank** correspondence — the model's per-verb
  *ordering* matches the human per-verb *ordering*. It is **not** a claim that model and human effect
  *sizes* match, and — per the standing S1 caveat — a replicated per-verb ρ raises confidence in the
  **correspondence's stability**, not in "competence beyond memorized lexical bias" (DAIS is public since
  2020; per-verb bias is memorizable even under the disjoint-sentence firewall).

## Headline 2 — the definiteness/length band is filler-UNSTABLE (NOT promoted)

The same probe's Arm B (recipient definiteness/length surface). Its S3 instrument band **flipped** between
two single runs on disjoint fillers:

| | s248 (v1) | rep2 (s250) |
|---|---|---|
| Arm-B monotonicity beats chance (≥2/3) | ✓ (28/29/18 of 40) | ✓ (28/29/24 of 40) |
| within-length definiteness control (both lengths CI-LB>0, ≥2/3) | **✗ (0/3 — failed at long length)** | **✓ (2/3 — claude, gemini pass; gpt fails at long)** |
| **instrument band** | **LENGTH-ONLY** | **TRACKS-HUMAN-SURFACE** |

- In rep2 the within-length definiteness contrast clears at **both** lengths for claude (short +0.090
  [+0.036,+0.143]; long CI-LB>0) and gemini (short +0.098 [+0.043,+0.156]; long CI-LB>0), but **not** gpt
  (long +0.026, CI incl. 0). In v1 the long-length contrast's CI included 0 on **all three**.
- **The honest reading is under-determination, not TRACKS.** Two single runs on different recipient
  fillers give **opposite bands**. The load-bearing quantity — the definite−indefinite contrast at **long**
  recipient length — is **small** (human +2.47 points/100) and **filler-sensitive** (it cleared with
  `the clerk from downtown` vs `a clerk from downtown`, not with v1's `the girl from college` vs `a girl
  from college`). So the definiteness/length band is **not reliably estimable** at this N/filler; neither
  LENGTH-ONLY nor TRACKS is a stable verdict. **This leg is NOT promoted, and the verb-bias claim does not
  ride on the rep2 TRACKS band.** It is a first-class caution: a single-run band on a small, filler-sensitive
  contrast can flip — exactly the kind of instability the powered/replicated verb-bias leg does **not** show.
- This does **not** convert the s248 predictions §B LOSS: the primary bet was TRACKS-HUMAN-SURFACE as a
  *stable* reading, and band-level TRACKS is **not** replicated — it is unstable. The registered §B
  **replication sub-bet** (VERB-BIAS-REPLICATES = True) is a **WIN**, scored on the verb-bias leg only.

## Gates (frozen; per-model booleans)

- Replication predicate (`replication.json`): R1 3/3, R2 3/3, R3 3/3 → **VERB-BIAS-REPLICATES = True**,
  `licenses_promotion_review = True`.
- Instrument band (`analyze.py::decide`, byte-frozen): rep2 **TRACKS-HUMAN-SURFACE**; `length_only_
  dissociation_replicates = False` (v1 LENGTH-ONLY ≠ rep2 TRACKS → the band did not replicate).
- Per-model transparency: no single model drives the verb-bias replication — R1/R2/R3 clear on all three;
  the Arm-B within-length control splits 2/1 (gpt the dissenter at long length), which is exactly why the
  band is called unstable, not TRACKS. (Pre-run critic's non-binding note: the ≥2/3 gate counts each
  conjunct independently across models; here all three conjuncts clear on all three models, so no split.)

## What it feeds

- **The verb-bias correspondence → a scoped `claim` (PROMOTED this session).** VERB-BIAS-REPLICATES
  licensed the cross-session promotion review; the fresh-agent reviewer (verdict authority) + a
  non-Anthropic vote both returned **PROMOTE-WITH-CONDITIONS**
  ([`REVIEW-promote-s250.md`](../../../experiments/runs/2026-07-18-dais-option-b-rep2/REVIEW-promote-s250.md)),
  and the 7 binding conditions (soften magnitude → **ordering correspondence**; contamination-vulnerable;
  per-model spread; scope to the verb-bias arm; distinctness from the givenness claim; cite the Arm-B
  band instability as a bound; claim `supported` / results stay `proposed`) are applied in
  [`claim/dative-verb-bias-graded-correspondence`](../claims/dative-verb-bias-graded-correspondence.md).
- **The definiteness/length band instability** is a first-class caution for the shadow-depth reading and
  for any single-run band on a small human contrast — it does not feed a promotion.
- **The conjecture's secondary-confirm graded-acceptability clause**
  ([`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md)):
  the verb-bias correspondence is now **twice-observed**; still secondary/non-decisive (it neither converts
  nor rescues the primary givenness test, which it does not touch).

## Provenance + reproduction

- **Run:** [`experiments/runs/2026-07-18-dais-option-b-rep2/`](../../../experiments/runs/2026-07-18-dais-option-b-rep2/)
  — byte-frozen `probe.py`/`analyze.py` (sha-identical to s248), `common.py` (budget-only diff),
  `build_trials.py` (fresh fillers + both disjointness firewalls), `replication_check.py` (the frozen
  R1/R2/R3 predicate), `PREREG.md` (sha-pinned before any call, gate outcomes + run outcome),
  `REVIEW-critic-s250.md` (pre-run critic + gate reconciliation), `VOTE-freeze-s250.json` /
  `VOTE-promote-s250.json`. Raw model preferences in `raw/probe-{A,B}-<model>.jsonl`. No DAIS rows or
  building-blocks in git.
- **Human anchor:** [`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md)
  (`anchors:`, Q3-A), scoped to the verb-bias + definiteness/length surface only.
- **Verifier:** independent recomputation from raw (separate code path) + deterministic re-run —
  [`VERIFY-s250.txt`](../../../experiments/runs/2026-07-18-dais-option-b-rep2/VERIFY-s250.txt).
