# Run record — monotonicity-generalization battery (2026-06-28, session 135)

The **sole decisive test** of [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md): the matched-difficulty add-vs-cancel generalization battery on a **new** construction pair (ADD = resultative; CANCEL = *for*-durative aspectual coercion). Yardstick fixed (ratified s134) by [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../../wiki/decisions/resolved/constructional-monotonicity-generalization-operationalization.md). Design + frozen thresholds: [`PREREG.md`](PREREG.md). Result page: [`result/constructional-monotonicity-generalization-v1`](../../../wiki/findings/results/constructional-monotonicity-generalization-v1.md). **`internal-contrast-only`** — no human-comparison claim.

## Files

- `build_items.py` — freezes `experiments/data/monotonicity-generalization-battery/items.csv` (sha256[:16] **`80bd4b60b55a3e60`**), 51 items.
- `probe.py` — `--calib` runs the 12-item B2 calibration subset → `raw_calib/`; no flag runs the full 51-item battery → `raw/`. NLI + FC, temp 0, 3-family panel, billed `usage.cost`.
- `analyze_calib.py` — applies the frozen **B2 ceiling gate** → `raw_calib/gate.json`.
- `analyze.py` — applies the frozen **asymmetry (20 pp) / fragility (10 pp) / cue (≥0.70)** rules → `raw/results.json`.

## Procedure (gate-before-run)

1. `python3 build_items.py` (freeze + hash) — done before any API call.
2. `OPENROUTER_API_KEY=… python3 probe.py --calib` → `python3 analyze_calib.py` (B2 gate).
3. On GO: independent fresh-agent **pre-run critic** reviews frozen items + PREREG + gate.
4. On GO: `OPENROUTER_API_KEY=… python3 probe.py` (full battery) → `python3 analyze.py`.
5. Independent fresh-agent **post-run verifier** recomputes from `raw/*.json`.

## B2 gate result

_(filled after step 2)_

## Main battery result

_(filled after step 4)_

## Cost

_(billed usage.cost, filled after each probe)_
