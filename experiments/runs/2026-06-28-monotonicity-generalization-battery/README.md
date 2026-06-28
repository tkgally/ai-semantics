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

## B2 gate result — **NO-GO** (cancel arm fails)

Calibration probe ran 72 calls (12 items × NLI+FC × 3 models), 0 NA, independently
verified. Affirm rates (NLI primary; FC identical here):

| arm | cell | A claude | B gpt-mini | C gemini | target | pass |
|---|---|---|---|---|---|---|
| ADD | construction (license) | 1.00 | 1.00 | 1.00 | ≥ 0.80 | ✓ 3/3 |
| ADD | control (bare) | 0.00 | 0.00 | 0.00 | ≤ 0.40 | ✓ 3/3 |
| CANCEL | default ("only once") | 0.00 | 0.00 | 0.00 | ≥ 0.80 | ✗ 0/3 |

**VERDICT = NO-GO.** Every cancel `default` item, all 3 models, returned NLI label 1
(neutral): "X flashed" does **not entail** "X flashed only once" — single-occurrence is a
defeasible implicature, not an entailment, so it cannot reach the matched ceiling under
strict NLI. The failure is **structural, not verb-selection** (uniform across
flash/jump/cough/nod), so a within-frame re-pair is futile. Per the frozen rule a B2 NO-GO
**defers the run rather than relaxing the bar**.

Independent fresh-agent post-run verifier recomputed every number from `raw_calib/*.json`:
exact match to `raw_calib/gate.json`; 72/72 priced, 0 parse failures.

## Main battery

**NOT RUN** (B2 NO-GO). The cancel-suppression cell was held out of the calibration, so the
asymmetry magnitude was never computed — the anti-cheat separation held. The pre-run critic
(step 3) was never reached (it is gated on a B2 GO).

→ Result: [`result/monotonicity-generalization-b2-nogo-v1`](../../../wiki/findings/results/monotonicity-generalization-b2-nogo-v1.md).
→ Cancel-arm re-design surfaced: [`decisions/open/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/open/monotonicity-cancel-arm-redesign.md).

## Cost

**$0.01720 billed** (UTC 2026-06-28), calibration probe only: claude $0.01054 + gpt $0.00260
+ gemini $0.00407 (72 calls, 0 missing cost). The asymmetry battery was not run, so its
~$0.1–0.3 was not spent.
