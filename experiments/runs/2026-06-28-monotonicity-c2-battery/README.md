# Run: C2 matched-difficulty add-vs-cancel monotonicity battery (2026-06-28, session 137)

**STEP 2** of [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/resolved/monotonicity-cancel-arm-redesign.md), reached on the C1 NO-GO + **C2 GO** ([`result/monotonicity-c2-privative-calibration-v1`](../../../wiki/findings/results/monotonicity-c2-privative-calibration-v1.md)), after M2. The decisive matched-difficulty test of [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md), as broadened by M2. `internal-contrast-only`.

## Frozen artifacts (committed before any API call)

- `experiments/data/monotonicity-c2-battery/items.csv` — 54 items (30 ADD verbatim s135 + 24 CANCEL C2 privative), sha256[:16] **`4b823d3d48422eaf`**.
- [`PREREG.md`](PREREG.md) — frozen pair, B2 gate, frozen s134 thresholds, M1/M2, anti-cheat.
- `build_items.py` (reads the s135 ADD arm byte-for-byte with a sha self-check; appends the C2 cancel arm). `probe.py` / `analyze_calib.py` / `analyze.py` reused from the s135 battery (thresholds unchanged).

## Frozen thresholds (ratified s134, untouched)

- **B2 gate** (calib subset, before the main read): add construction ≥ 0.80 AND control ≤ 0.40; cancel category default ≥ 0.80; each ≥2/3 models.
- **Asymmetry** (no-cue): add_no_cue − cancel_no_cue ≥ 0.20 (≥2/3) CONFIRMS; |·|<0.20 SYMMETRIC; ≤−0.20 REVERSAL.
- **Fragility:** cancel NLI-vs-FC disagreement − add's ≥ 0.10 (≥2/3) = leg 2.
- **Cue:** ≥ 0.70 follow-cue (≥2/3) robust.

## Procedure

1. `python3 build_items.py` — freeze + hash; verbatim-reuse self-check on the ADD source. ✅ (sha `4b823d3d48422eaf`)
2. `python3 probe.py --calib` (72 calls) → `python3 analyze_calib.py` → `raw_calib/gate.json` (re-run the B2 gate on the frozen combined set).
3. On B2 GO: independent fresh-agent **pre-run critic** GO/NO-GO on the frozen full set + PREREG + gate.
4. On critic GO: `python3 probe.py` (324 calls) → `python3 analyze.py` → `raw/results.json`.
5. Independent fresh-agent **post-run verifier** recomputes every cell from `raw/*.json`.

## Result

- See [`result/monotonicity-c2-battery-v1`](../../../wiki/findings/results/monotonicity-c2-battery-v1.md) (written after the read).
- Spend: `raw_calib/run_summary.json` + `raw/run_summary.json` (billed `usage.cost`) and `config/budget.md`.
