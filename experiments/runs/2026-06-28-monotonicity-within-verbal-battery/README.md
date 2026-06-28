# Run: within-verbal matched ADD-vs-CANCEL monotonicity battery (2026-06-28, session 141)

The decisive **within-verbal** generalization test of
[`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md):
the frozen s135 resultative **ADD** arm (verbatim) + the s140 causative-inchoative progressive
**CANCEL** arm, **both verbal** → a positive asymmetry **discharges the M2 domain mismatch** the
weak C2 confirm carries. Frozen s134 thresholds, ratified operationalization, no new decision.
`internal-contrast-only`.

## Frozen artifacts (committed before any API call)

- `experiments/data/monotonicity-within-verbal-battery/items.csv` — 48 items (30 add verbatim +
  18 cancel), sha256[:16] **`2c0d4f70f28bb1c4`**.
- [`PREREG.md`](PREREG.md) — frozen design, frozen thresholds, pre-stated expectation, anti-cheat.
- `build_items.py` (asserts ADD source sha `80bd4b60b55a3e60`) / `probe.py` / `analyze.py`.

## The matched paradigm

| arm | control/default | construction | cue |
|---|---|---|---|
| ADD (resultative, verbal) | "Maria beat the cream." (low) | "Maria beat the cream stiff." (`add_no_cue`, want ceiling) | "…stiff, but the cream did not become stiff." (DENIAL) |
| CANCEL (progressive, verbal) | "Sam broke the vase." (B2 anchor) | "Sam was breaking the vase." (`cancel_no_cue` = 1−affirm) | "…the vase, and the pieces scattered across the floor." (RE-ASSERTION) |

## Frozen thresholds (ratified s134)

B2 (read first): add construction ≥ 0.80 & control ≤ 0.40; cancel default ≥ 0.80 (each ≥ 2/3).
Asymmetry: `add_no_cue − cancel_no_cue` ≥ 0.20 (≥ 2/3) CONFIRMS; |·|<0.20 SYMMETRIC; ≤ −0.20
REVERSAL. Fragility ≥ 0.10; cue ≥ 0.70. Per-verb cancel breakdown reported, no verb dropped.

## Procedure

1. `python3 build_items.py` ✅ (sha `2c0d4f70f28bb1c4`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO.
3. On GO: `OPENROUTER_API_KEY=… python3 probe.py` (288 calls), then `python3 analyze.py`.
4. Independent fresh-agent **post-run verifier** + leave-one-out over the 6 cancel verbs.

## Result

- See [`result/monotonicity-within-verbal-battery-v1`](../../../wiki/findings/results/monotonicity-within-verbal-battery-v1.md) (written after the run).
- Spend: `raw/run_summary.json` (billed `usage.cost`) and `config/budget.md`.
