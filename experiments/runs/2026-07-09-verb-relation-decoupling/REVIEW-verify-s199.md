# REVIEW — s199 POST-RUN VERIFIER, verb-relation decoupling probe (2026-07-09)

Independent fresh-agent post-run verifier: recomputed every headline figure from `raw/*` + `items.json`
+ `control.json` with its **own** scorer (did NOT import `analyze.py`). **VERDICT: REPRODUCED** — max ρ
discrepancy **0.0004** (pure 3-decimal storage rounding); same H1 verdict (DECOUPLING-BREAKS), same
per-model bands, same H2 verdict (DEPTH-FAILS, under-powered).

## Reproduced per-model figures

| model | ρ_cue (verifier / results.json) | ρ_depth | H1 band | depth-wins |
|---|---|---|---|---|
| A (sonnet-4.6) | 0.4857 / 0.486 | 0.257 | INCONCLUSIVE | no |
| B (gpt-5.4-mini) | 0.6000 / 0.60 | 0.029 | **BREAKS** | no |
| C (gemini-3.5-flash) | 0.5429 / 0.543 | 0.086 | **BREAKS** | no |

**H1 = DECOUPLING-BREAKS** (ρ_cue > +0.50 on 2/3; A inconclusive at 0.486). HIT@3 co-primary ρ_cue
0.714 / 0.771 / 0.543 — reproduced, even more strongly positive. **H2 = DEPTH-FAILS**: all ρ_depth are
**positive** (wrong sign for the predicted-negative depth proxy), 0/3 clear the margin; and the frozen
B1 `depth_degenerate=true` (non-antonymy CORE-4 range 0.277 < 0.50) makes it under-powered/non-falsifying
regardless. **Empties: zero** across all 776 cues × 3 models — no null-row inflation. Frozen cue-strength
reproduced from `control.json` (antonymy 0.0923 / troponymy 0.0487 / synonymy 0.0308 / hypernymy 0.0207 /
cause 0.0106 / entailment 0.0051; mean 0.0347).

## Why H1 breaks (verifier's leave-one-out diagnosis)

The positive ρ_cue is **not** a single-relation artifact. It is carried by the joint bottom-alignment of
**entailment and cause** — simultaneously the two lowest-cue-strength AND the two lowest-recovery
relations. The noun-like **disaligner is hypernymy** (lowest-but-one cue-strength 0.0207 yet the
*highest* recovery, 3/3 — the classic "scramble a taxonomic list" effect), and troponymy also disaligns;
but hypernymy is one relation, and the antonymy-top + entailment/cause-bottom alignment **outvotes** it.
Leave-one-out: dropping entailment OR cause collapses ρ_cue to ~0.10–0.30 on every model; dropping any
other relation leaves ρ_cue ≥ +0.50 (dropping hypernymy raises it to 0.7–0.9). So on verbs cue-strength
regains rank-predictive power **despite** the verified verb troponymy hierarchy.

## Adversarial concerns (verifier)

None material. One flag carried to the result: the DECOUPLING-BREAKS reading **leans on entailment + cause
sitting jointly at the bottom** of both rankings — a genuine data feature (the two sparse, thin-signal
verb relations), not a scoring artifact, but worth disclosing. Two immaterial notes: one hypernymy cue
absent from `control.json` (shifts its cue-strength by 0.0002, preserves rank); results.json stores ρ to
3 dp (the source of the ≤0.0004 "discrepancies").
