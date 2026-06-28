---
type: result
id: monotonicity-causative-progressive-cancel-v1
title: "Causative-inchoative progressive cancel-suppression calibration — the progressive functions as a within-verbal cancel construction: aggregate suppression of the B2-confirmed result entailment is positive in all 6 model×instrument cells (NLI 33–67 pp, FC 50–100 pp) and the cue re-licenses, though uneven across verbs; the matched within-verbal battery is now buildable"
meaning-senses:
  - constructional
  - inferential
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: result/monotonicity-verbal-cancel-survey-v1
  - rel: depends-on
    target: open-question/within-verbal-cancel-at-ceiling
  - rel: refines
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: concept/coercion
---

# Result: causative-inchoative progressive cancel-suppression calibration

> **Cancel-arm calibration, `internal-contrast-only`.** The next empirical step named by
> [`result/monotonicity-verbal-cancel-survey-v1`](monotonicity-verbal-cancel-survey-v1.md) (s139)
> and [`open-question/within-verbal-cancel-at-ceiling`](../open-questions/within-verbal-cancel-at-ceiling.md):
> **measure** whether the **progressive** suppresses the held causative-inchoative result
> entailment the s139 survey B2-confirmed at ceiling, in the matched conflicting-cue paradigm of
> [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md). It calibrates the
> **cancel arm** — it pairs **no** ADD arm, so it computes **no** asymmetry and does **not** test
> [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md).
> Makes **no** human-comparison claim. Pre-registration, frozen items, every number:
> [`experiments/runs/2026-06-28-monotonicity-causative-progressive-cancel/`](../../../experiments/runs/2026-06-28-monotonicity-causative-progressive-cancel/README.md).

## Why this ran

The s139 survey B2-confirmed three held-at-ceiling verbal defaults and singled out the
**causative-inchoative** family as the one admitting a genuine **same-verb constructional
cancel** — the progressive/imperfective paradox ("Sam was breaking the vase" ⊭ "The vase
broke"). Per the binding s135/C1 lesson — **measure the cancel, don't assume it** — this probe
tests whether the progressive *actually* suppresses the result entailment before any matched
battery is built.

## What was measured

Frozen set (items.csv sha256[:16] **`5ba8a996fa70cf55`**): the **6 s139 B2-confirmed verbs**
(break, shatter, melt, tear, crack, dissolve) × **3 conditions**, same subject/object triples
(so `default` re-uses the s139 default). Hypothesis throughout = "The &lt;obj&gt; &lt;inch&gt;." —

| condition | example | affirm-result gold | role |
|---|---|---|---|
| default | Sam broke the vase. | YES | held entailment (s139 ceiling anchor) |
| progressive | Sam was breaking the vase. | NO | the suppression (imperfective paradox) — LOW = good |
| cue | Sam was breaking the vase, and the pieces scattered across the floor. | YES | explicit result-consequence re-licenses |

NLI primary + forced-choice, temperature 0, panel claude-sonnet-4.6 / gpt-5.4-mini /
gemini-3.5-flash. 18 × 2 × 3 = **108 calls**. **Report-the-rate** (no pass bar tuned after
data), matched to conative-cancel-v2. An independent fresh-agent **pre-run critic** returned
GO-WITH-NOTES (hash verified; paradigm faithful; not a re-grind of C1; flagged per-verb
lexical-aspect heterogeneity to report); an independent fresh-agent **post-run verifier**
recomputed all 18 cells + the per-verb breakdown (exact match; 108/108 priced, 0 errors, 0
parse failures, cost matched).

## One-line finding

**The progressive functions as a within-verbal cancel construction (aggregate suppression
positive in all 6 model×instrument cells, though uneven across verbs). The held result entailment
is at ceiling on the bare past (NLI affirm 100% in 3/3 models, re-confirming s139), and the
progressive suppresses it in every model and instrument — NLI affirm drops to 33/33/67%
(suppression 66.7 / 66.7 / 33.3 pp), FC to 0/0/50% (suppression 100 / 100 / 50 pp) — while an
explicit result-consequence cue re-licenses it (positive shift in all 6 model×instrument
cells).** This is the conative-shaped cancel pattern, and on NLI it is *cleaner* than the
original conative (where gpt-5.4-mini failed suppression entirely). So the missing **within-verbal
cancel arm** the matched battery needs is now in hand — the battery is buildable next (this
calibration does not itself test the conjecture).

## Numbers (verified)

Affirm-the-result rate (%), n = 6 verbs per condition per model; independently recomputed by the
post-run verifier — exact match to `raw/gate.json`, 108/108 priced, 0 missing, 0 parse failures.

| model | instr | default | progressive | cue | suppression (no-cue) | cue-following | shift |
|---|---|---|---|---|---|---|---|
| A claude-sonnet-4.6 | NLI | 100.0 | 33.3 | 83.3 | **66.7 pp** | 83.3 | +50.0 |
| A claude-sonnet-4.6 | FC | 100.0 | 0.0 | 83.3 | **100.0 pp** | 83.3 | +83.3 |
| B gpt-5.4-mini | NLI | 100.0 | 33.3 | 100.0 | **66.7 pp** | 100.0 | +66.7 |
| B gpt-5.4-mini | FC | 66.7 | 0.0 | 100.0 | **100.0 pp** | 100.0 | +100.0 |
| C gemini-3.5-flash | NLI | 100.0 | 66.7 | 83.3 | **33.3 pp** | 83.3 | +16.6 |
| C gemini-3.5-flash | FC | 100.0 | 50.0 | 66.7 | **50.0 pp** | 66.7 | +16.7 |

- **suppression-no-cue** = `100 − progressive_affirm` (construction-following, no cue) — positive
  in **all 6** model×instrument cells. gemini suppresses least (the same model-ordering wrinkle
  the conative showed), but it still suppresses.
- **cue-following / shift** — the explicit result-consequence re-licenses the entailment in every
  cell (shift +16.6 to +100.0 pp), the conflicting-cue signature.

## Per-verb heterogeneity (the pre-run critic's flag — reported honestly, and it does NOT track lexical aspect the predicted way)

The progressive-condition affirm is heterogeneous across the 6 verbs, and the pattern is the
**reverse** of the critic's lexical-aspect prediction (which expected the gradual change-of-state
verbs *melt/dissolve* to suppress *weakly*):

- **`dissolved` is a clean suppressor in all 6 cells** (progressive affirm = 0 everywhere) — the
  gradual verb the critic expected to resist.
- **`shattered` is a frequent non-suppressor** (progressive affirm = 1 in all three NLI files,
  verifier-confirmed `pred="0"`/entailment) — a *punctual* achievement, which the critic expected
  to suppress cleanly.

A linguistically coherent reading (offered as interpretation, not measured): the progressive of a
**punctual** achievement ("was shattering the window") is a coerced form the panel tends to read
as already-culminated, whereas the progressive of a genuinely **durative** process ("was
dissolving the tablet") cleanly leaves culmination open — so punctual verbs' progressives suppress
*less*, not more. `melt` is mixed (resists in claude+gemini NLI), so the split is not perfectly
clean. The honest upshot: **the aggregate suppression is robust and in the predicted direction in
all 6 model×instrument cells, but it is carried unevenly across verbs** — a future battery should
keep the per-verb breakdown visible and not over-read the 6-verb mean.

## What this does and does not license

- **Does:** establish, with a verified report-the-rate read, that the **progressive is a working
  within-verbal cancel construction** — it suppresses a B2-confirmed held entailment off-ceiling
  in all three models and re-licenses under an explicit cue. This is the **first NEW within-verbal
  cancel arm beyond the original conative**, and the missing ingredient the matched within-verbal
  battery needs. It **unblocks** that battery.
- **Does not** test [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md):
  no ADD arm was paired, so **no asymmetry was computed** and none was read. The conjecture's
  `tested`/weak status is unchanged.
- **Does not** re-grind: this is **not** the ruled-out C1 completion arm. C1's default
  ("built the house" → "finished building it", an incremental-theme accomplishment culmination)
  *floored* B2 (0.25/0.375/0.75); the default here is a *punctual causative-inchoative result-state*
  entailment that *passed* B2 at 1.00 (s139). The progressive cancel **is** aspectual, and the
  per-verb heterogeneity (punctual progressives sometimes read as culminated) is exactly the kind
  of thing that had to be *measured*, not presumed.
- **Does not** make a human comparison (`internal-contrast-only`), nor tune any threshold
  (report-the-rate; the eventual battery uses the separately-frozen s134 thresholds).

## What happens next (the now-unblocked unit, not run here)

Build the matched **within-verbal add-vs-cancel battery**: reuse the frozen B2-passing resultative
ADD arm (sha `80bd4b60b55a3e60`, verbatim) + this causative-inchoative progressive CANCEL arm,
placed in the common conflicting-cue paradigm, read by the **frozen s134 thresholds** (asymmetry
≥ 20 pp; instrument-fragility ≥ 10 pp; cue ≥ 0.70), with a fresh pre-run critic and post-run
verifier. A positive asymmetry there would be the **clean within-verbal generalization confirm** —
**no domain mismatch** (both arms verbal) — that discharges the M2 caveat the weak C2 confirm
carries. This is a legitimate next unit; the conjecture's status does not move until it runs.

## Provenance

- Every figure is reproduced verbatim from `raw/gate.json` and independently recomputed from the
  per-call `raw/*.json` by a read-only post-run verifier (exact match; 108/108 priced, 0 missing,
  0 parse failures, 0 errors).
- The matched conflicting-cue paradigm (default/construction/cue, report-the-rate) is the frozen
  template of [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md); the
  B2-confirmed default and the family selection are from
  [`result/monotonicity-verbal-cancel-survey-v1`](monotonicity-verbal-cancel-survey-v1.md).
- Spend: **$0.02586 billed** (UTC 2026-06-28), the cancel-arm calibration only; no battery run.
