# Run: C1 telic-completion DEFAULT B2 calibration (2026-06-28, session 137)

**STEP 1** of [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/resolved/monotonicity-cancel-arm-redesign.md) (ratified s136). A **calibration only** — measures whether the completion default of a simple-past accomplishment is a model-held entailment at the B2 ceiling, *before* any matched asymmetry battery is built or run. Does **not** test [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md). `internal-contrast-only`.

## Frozen artifacts (committed before any API call)

- `experiments/data/monotonicity-c1-completion-calibration/items.csv` — 8 completion-default items, sha256[:16] **`4e8c3935af154c46`**.
- [`PREREG.md`](PREREG.md) — the frozen design, the frozen B2 gate, anti-cheat.
- `build_items.py` — emits + hashes the CSV (no API). `probe.py` — runs the panel. `analyze_calib.py` — applies the frozen gate.

## The gate (frozen, STEP 1, not relaxable)

Completion default affirm ("…finished V-ing the …") **≥ 0.80 in ≥2/3 models**, strict NLI (label 0 = entailment), temperature 0, the ratified panel.

- **GO →** STEP 2 (build matched C1 cancel arm; reuse frozen B2-passing ADD arm, sha `80bd4b60b55a3e60`).
- **NO-GO →** record verified C1-NO-GO result; STEP 1b (C2 privative, after M2's conjecture-scope amendment). Do not relax the bar.

## Procedure

1. `python3 build_items.py` — freeze + hash the CSV. ✅ (sha `4e8c3935af154c46`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO on the frozen set + PREREG vs the decision STEP 1 spec.
3. On critic GO: `OPENROUTER_API_KEY=… python3 probe.py` (48 calls), then `python3 analyze_calib.py` → `raw_calib/gate.json`.
4. Independent fresh-agent **post-run verifier** recomputes every cell from `raw_calib/*.json`.

## Result

- See [`result/monotonicity-c1-completion-calibration-v1`](../../../wiki/findings/results/monotonicity-c1-completion-calibration-v1.md) (written after the gate fires).
- Spend: recorded in `raw_calib/run_summary.json` (billed `usage.cost`) and `config/budget.md`.
