# Post-run verifier — adjective-antonymy replication probe (s196, 2026-07-09)

An **independent fresh-agent verifier** recomputed every headline number from `raw/` + `items.json` +
`control.json` with its **own second implementation** (not a re-run of `analyze.py`). PROTOCOL §5/§A3.

## REPRODUCED — 0 discrepancies (max diff 0.0000)

- **Recovery (neutral), 24 cells** — exact match. Antonymy 𝒮 ≈ 0.31 / HIT ≈ 0.88; other three 𝒮
  0.16–0.22 / HIT 0.42–0.51.
- **Cue-strength** — antonymy 0.1214, synonymy 0.0465, similar 0.0462, also-see 0.0615; **mean over all
  cues 0.068855 ≥ 0.05 → calibration gate CLEARS** (residual arm verdict-bearing). Matches.
- **Antonymy-shadow HIT@3 residual** — +0.5194 / +0.5194 / +0.5349 (A/B/C), the **largest** of the four
  relations on all three models (margin ~0.15–0.20 to runner-up; bootstrap CI floor ~0.42 above the
  others' means) → **ANT-CLEARS-CONTROL 3/3**. Robust, not marginal.
- **Frame-ablation** — neutral vs frame HIT@3 A 0.877/0.785, B 0.885/0.777, C 0.892/0.892; all survive
  Δ=0.15 → **SURVIVES-SUPPRESSION 3/3**.
- **H1 ρ_cue** — soundness 0.400/0.800/0.400 (HIT 0.400/1.000/0.200); bands PARTIAL/BREAKS/PARTIAL →
  **H1-PARTIAL/AMBIGUOUS** (only B > 0.50, not ≥2/3 either way). "Correct frozen call, honestly reported;
  intrinsically shaped by the n=4 tie structure that PREREG C4 pre-names and bars from carrying claim
  promotion alone; the one BREAKS is a single low-resolution point, not a 2/3 break. No threshold tuned
  post-hoc."
- **Item-level pooled Spearman** — 0.268/0.272/0.241 (n≈518).
- **Fabrication / sanity** — 1,950 calls, **0 errors**, $0.3664 (< ABORT 1.20); all raw n=130/relation;
  **1 empty in the whole neutral set** (A-synonymy). Productions genuine (cross-model divergence on
  shared cues; the frame arm is distinctly frame-shaped). **Antonymy residual n=129 = 1 control-frame
  null cue** (`anal`, no C4 co-occurrence candidates), **not** a model empty — consistent with every
  per-cell n in results.json.

**Disposition:** the committed `results.json` and the result page
[`result/adjective-antonymy-replication-v1`](../../../wiki/findings/results/adjective-antonymy-replication-v1.md)
are faithful to raw. ANT-CLEARS-CONTROL robust; H1-PARTIAL the correct, honestly-reported frozen call.
