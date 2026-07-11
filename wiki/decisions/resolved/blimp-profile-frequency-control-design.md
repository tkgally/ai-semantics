---
id: blimp-profile-frequency-control-design
title: "BLiMP profile-alignment frequency control (C8 promotion-prep) — the value-laden gates: the control strategy (Q1: covariate vs swap arm vs both), the frequency proxy (Q2 — the crux), and the promotion rule + proxy-scope (Q3)"
status: resolved
opened: 2026-07-11
opened-by: session-207
resolved: 2026-07-11
resolved-by: autonomous (adversarial review)
resolution: "RATIFY-WITH-MODIFICATION — Q1-C (covariate + swap arm; adopted over the Q1-A default, converging with both s207 reviewers) / Q2-A primary, honestly scoped as SURFACE-LEXICAL familiarity, Q2-B sensitivity-only, Q2-C-as-primary REJECTED (construction frequency ≈ collinear with depth → reproduces the over-control hazard) / Q3-A (promotion GATE; standalone result either way; a later cross-session adversarial review writes the claim). G8 ADOPTED BINDING: the covariate arm alone earns only a ROBUSTNESS / CORROBORATION result; the Q1-C swap arm is REQUIRED for any human-comparison PROMOTION (promotion candidacy requires SURVIVES ∧ SWAP-STABLE, inheriting the G3′ surface-vs-construction scope). NEW freeze condition G9 (staging/labeling honesty): a covariate-arm-only result page must be typed/titled ROBUSTNESS/CORROBORATION, state on its face that C8's promotion gate is NOT satisfied and the swap arm is the outstanding requirement, carry both G3′ caveats, and NOT advance the shadow-depth table's form-(iv) row toward a claim; plus a G7 sharpening — F(p) fixed to a single zero-post-freeze-latitude recipe, with the fresh-agent verifier certifying that property and running the external-benchmark proxy-validity audit before any partial outcome is inspected. Ratified s208 by a fresh-agent adversarial reviewer (verdict authority, independent of the s207 design author) + a convergent fresh non-Anthropic decorrelation vote (panel.B = gpt-5.4-mini, $0.003099). Freeze conditions G1′–G9 bind the freeze. STAGING RULING: 'ratify Q1-C, run the covariate arm only this session ($0) as a robustness/corroboration result, defer the swap arm for promotion' is coherent and honest — ratifying Q1-C raises the promotion bar to both arms before either runs, and G8 forecloses reading a covariate SURVIVES as C8-satisfied."
contingent-artifacts:
  - design/blimp-profile-frequency-control-v1
---

# Decision: the value-laden gates of the BLiMP R1 frequency control (A3b, C8 promotion-prep)

> **RESOLVED — session 208 (2026-07-11), autonomous cross-session adversarial review.**
> **RATIFY-WITH-MODIFICATION: Q1-C / Q2-A (surface-scoped primary) / Q3-A; G8 BINDING; new G9.** A
> fresh-agent adversarial ratification reviewer (verdict authority, independent of the s207 design author)
> returned **RATIFY-WITH-MODIFICATION**; a **fresh** non-Anthropic decorrelation vote (`panel.B` =
> `gpt-5.4-mini`, $0.003099) returned **RATIFY-WITH-CONDITIONS** and converged per-gate (Q1-C / Q2-A /
> Q3-A, G8=Y). Both s207 reviewers had already converged on Q1-C. Full record:
> [`REVIEW-ratify-s208.md`](../../../experiments/runs/2026-07-11-blimp-frequency-control/REVIEW-ratify-s208.md)
> + [`VOTE-ratify-s208.json`](../../../experiments/runs/2026-07-11-blimp-frequency-control/VOTE-ratify-s208.json).
> The design is promoted (`contingent-on` cleared). **Freeze conditions G1′–G9 bind the freeze**; the
> covariate arm ($0) is frozen + run s208, the swap arm (Q1-C, required for a promotion per G8) is a later
> session. Tom's standing override outranks this autonomous ratification.

## What was decided (the yardstick, never the result)

Binding condition **C8** of the s205 BLiMP ratification
([`decisions/resolved/blimp-forced-choice-sweep-design`](blimp-forced-choice-sweep-design.md)) makes the
PRIMARY human-anchored reading of
[`result/blimp-forced-choice-sweep-v1`](../../findings/results/blimp-forced-choice-sweep-v1.md) —
**R1 PROFILE-ALIGNED** (ρ_prof **+0.606 / +0.543 / +0.628**, n = 40) — **non-promotable to a `claim`
without a training-frequency confound control.** C8's binding text (the parent design's freeze conditions)
names *"a pre-registered corpus-frequency covariate **for each construction** partialled from ρ_prof"* — the
reviewer confirmed the "for each construction" wording is in the binding text (the open-decision
resolution-summary had paraphrased it out), which **strengthens** the ruling: Q2-A's surface-lexical proxy
must be honestly under-scoped (G3′) and the covariate arm alone cannot satisfy the promotion gate (G8).

- **Q1 = C (covariate + swap arm).** Adopted over the Q1-A default; both s207 reviewers and both s208
  reviewers converged. Non-redundant reasons: the covariate arm carries an irreducible reuse-of-known-
  accuracies exposure (G1′) **and**, under Q2-A, controls only surface-lexical familiarity; the swap arm
  tests a different causal channel (exact-string memorization) with fresh items/calls and no accuracy
  exposure. The program's first broad human-anchored grammatical claim deserves the conjunction.
- **Q2 = A primary (surface-scoped), Q2-B sensitivity-only, Q2-C-as-primary REJECTED.** The critic's
  collinearity argument is decisive: construction frequency is near-collinear with structural depth (rare =
  deep = human-harder), so partialling it reproduces the Q2-B over-control hazard — a BREAKS under Q2-C
  could not separate "frequency artifact" from "the shared structure *is* the depth structure." Q2-A is the
  least depth-entangled proxy; its honest under-scoping (lexical/surface exposure, not construction
  frequency) is exactly why Q1-C is required.
- **Q3 = A (promotion gate; standalone result either way).** Q3-C is over-reach, Q3-B a needless forfeit.
  Adopted with the G6 collinearity branch and both G3′ proxy caveats load-bearing.

## Freeze conditions that bind (G1′–G9)

G1′ (anti-cheat: PREREG the F(p) recipe before computing it; fresh-agent independent reproduction of
`build_freq.py` from the frozen spec before F(p) meets the paradigm→H mapping; the reuse pins only the C4
streaming adapter + tokenization, not the G² kernel; a scrambled-mapping negative control,
necessary-not-sufficient) · G2 (Q2-B detectability margin = labelled conservative sensitivity arm only) ·
G3′ (every SURVIVES/BREAKS statement carries BOTH caveats: against a C4-frequency proxy, not actual
pretraining frequency; and controls surface-lexical familiarity, not construction frequency) · G4′
(CI-exclusion power stated per model) · G5 (swap grammaticality re-validated before scoring) · G6
(frozen high-`corr(F,H)` threshold → INCONCLUSIVE over-control-suspect, distinct from SURVIVES/BREAKS and
from `corr(F,H)≈0` corroboration) · G7 (single primary F + one pre-specified sensitivity variant; no
post-hoc tuning; external-frequency-benchmark proxy-validity audit before the partial is read) · **G8
(BINDING: the Q1-C swap arm required for a human-comparison PROMOTION; covariate arm alone =
robustness/corroboration only)** · **G9 (NEW, staging/labeling honesty): a covariate-arm-only result page
must be typed/titled ROBUSTNESS/CORROBORATION, state that C8's promotion gate is NOT satisfied and name
the swap arm as outstanding, carry both G3′ caveats, and NOT advance the shadow-depth table's form-(iv)
row toward a claim.**

## Anti-cheat verdict

ADEQUATE for a robustness/corroboration result only (NOT for promotion — which G8 forbids). The scaffold
fences the residual reuse-of-known-accuracies exposure proportionately to a demoted robustness datum;
it would be fatal if the covariate arm were allowed to promote — hence G8. Provenance independently
confirmed by the reviewer: (a) ρ_prof +0.606/+0.543/+0.628 CONFIRMED; (b) `build_cooc_c4.py` has NO n-gram
frequency counter CONFIRMED (F(p) is genuinely new code with DoF); (c) C8 verbatim CONFIRMED (with the
"for each construction" clarifying note above).
