# Run: within-verbal cancel-default B2 calibration survey (2026-06-28, session 139)

Path (ii) of [`open-question/within-verbal-cancel-at-ceiling`](../../../wiki/findings/open-questions/within-verbal-cancel-at-ceiling.md):
a small structured **survey** triaging candidate NEW *verbal* cancel defaults through cheap
**B2 default-at-ceiling calibrations**, before any matched asymmetry battery is built. A
**calibration only** — does **not** test [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md).
`internal-contrast-only`.

## Frozen artifacts (committed before any API call)

- `experiments/data/monotonicity-verbal-cancel-survey/items.csv` — 18 items, 3 families × 6
  (implicative / factive / causative-inchoative), sha256[:16] **`f6f11a985f47dc89`**.
- [`PREREG.md`](PREREG.md) — frozen design, per-family B2 gate, anti-cheat, do-not-re-grind.
- `build_items.py` / `probe.py` / `analyze_calib.py`.

## The gate (frozen, per family, not relaxable — same bar as C1/C2 STEP 1b)

Default affirm ≥ **0.80 in ≥ 2/3 models**, strict NLI (label 0 = entailment), temperature 0,
the ratified panel, computed **independently per family**.

- **PASS** → candidate B2-passing NEW verbal default; result then scrutinizes whether it admits a
  clean **constructional** cancel (vs a lexical swap). Only PASS + clean constructional cancel
  flags a next-session battery (reuse frozen ADD arm sha `80bd4b60b55a3e60`).
- **FLOOR** → feeds the principled-limit closure.

## Procedure

1. `python3 build_items.py` — freeze + hash the CSV. ✅ (sha `f6f11a985f47dc89`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO on the frozen set + PREREG.
3. On critic GO: `OPENROUTER_API_KEY=… python3 probe.py` (108 calls), then
   `python3 analyze_calib.py` → `raw_calib/gate.json`.
4. Independent fresh-agent **post-run verifier** recomputes every per-family cell.

## Result

- See [`result/monotonicity-verbal-cancel-survey-v1`](../../../wiki/findings/results/monotonicity-verbal-cancel-survey-v1.md) (written after the gates fire).
- Spend: `raw_calib/run_summary.json` (billed `usage.cost`) and `config/budget.md`.
