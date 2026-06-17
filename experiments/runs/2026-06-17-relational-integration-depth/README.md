# 2026-06-17 — relational INTEGRATION-UNDER-LOAD probe (burial depth 2)

The harder-load follow-up to [`result/relational-integration-rung-ii`](../../../wiki/findings/results/relational-integration-rung-ii.md),
attacking that result's own honesty-box caveat — "it does not rule out overwrite behaviour under
harder load (more turns…)". Tests whether rung-(ii) integration survives when the earliest of three
compatible stamped turns is **buried under two later turns**.

Internal-contrast-only (the ratified relational posture; no human comparison; no new decision owed).
Design: [`experiments/designs/relational-integration-depth.md`](../../designs/relational-integration-depth.md).

## Files

- `common.py` — panel, frozen params (K=8, ceilings, DIRECT floor), prompt templates, forced
  parse, cost ledger + hard stop. The full rationale is in its module docstring.
- `build_trials.py` — builds the frozen 2×2×2 balanced-block roster and **certifies the shortcut
  bounds empirically** (`assert_balance`): position 0.125, single-attr ≤0.25, every drop-one-turn
  reader = 0.50, full integrator = 1.000. Prints the sha256 for PREREG.
- `fixtures/make_fixtures.py` — certifies the verdict map on six idealized readers (only a genuine
  integrator-of-three → INTEGRATION-UNDER-LOAD).
- `probe.py` — `liveness` (2 calls, format gate, held-out record) then `full` (160 finding-bearing
  calls). Refuses `full` until `PREREG.md` records the frozen sha.
- `analyze.py` — the pre-registered verdict.
- `PREREG-draft.md` → `PREREG.md` (frozen after the independent pre-run critic GO).

## Run order

```
python3 build_trials.py            # writes stimuli.json + prints sha256
python3 fixtures/make_fixtures.py  # ALL FIXTURES PASS
# independent pre-run critic GO -> rename PREREG-draft.md PREREG.md (with the sha) ->
python3 probe.py liveness          # both models parse
python3 probe.py full              # the only finding-bearing dataset
python3 analyze.py
# independent post-run verifier reproduces from raw/
```
