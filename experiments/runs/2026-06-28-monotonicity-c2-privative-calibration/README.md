# Run: C2 privative-modifier category-default B2 calibration (2026-06-28, session 137)

**STEP 1b** of [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/resolved/monotonicity-cancel-arm-redesign.md) (ratified s136), reached on the **C1 NO-GO** ([`result/monotonicity-c1-completion-calibration-v1`](../../../wiki/findings/results/monotonicity-c1-completion-calibration-v1.md)). **M2 applied first** (conjecture scope broadened in writing). A **calibration only** — measures whether a bare head noun's category-membership default is a model-held entailment at the B2 ceiling, *before* any matched asymmetry battery is built. Does **not** test the conjecture. `internal-contrast-only`.

## Frozen artifacts (committed before any API call)

- `experiments/data/monotonicity-c2-privative-calibration/items.csv` — 8 category-default items + frozen STEP-2 privative modifiers, sha256[:16] **`39598ee7ad97f33d`**.
- [`PREREG.md`](PREREG.md) — frozen design, frozen B2 gate, anti-cheat.
- `build_items.py` / `probe.py` / `analyze_calib.py`.

## The gate (frozen, STEP 1b, not relaxable)

Category-membership default affirm ("a gun" → "a weapon") **≥ 0.80 in ≥2/3 models**, strict NLI (label 0 = entailment), temperature 0, the ratified panel.

- **GO →** STEP 2 (build matched C2 cancel arm; reuse frozen B2-passing ADD arm, sha `80bd4b60b55a3e60`; domain-mismatch live caveat).
- **NO-GO →** STEP 3 principled-limit closure (M3: both C1 and C2 failed). Do not relax the bar.

## Procedure

1. `python3 build_items.py` — freeze + hash the CSV. ✅ (sha `39598ee7ad97f33d`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO on the frozen set + PREREG vs the decision STEP 1b spec.
3. On critic GO: `OPENROUTER_API_KEY=… python3 probe.py` (48 calls), then `python3 analyze_calib.py` → `raw_calib/gate.json`.
4. Independent fresh-agent **post-run verifier** recomputes every cell from `raw_calib/*.json`.

## Result

- See [`result/monotonicity-c2-privative-calibration-v1`](../../../wiki/findings/results/monotonicity-c2-privative-calibration-v1.md) (written after the gate fires).
- Spend: `raw_calib/run_summary.json` (billed `usage.cost`) and `config/budget.md`.
