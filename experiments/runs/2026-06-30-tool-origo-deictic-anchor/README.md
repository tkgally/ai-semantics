# 2026-06-30 · as-if origo probe (tool as deictic anchor)

Runs question **(iii)** of [`conjecture/tool-origo-deictic-anchor`](../../../wiki/findings/conjectures/tool-origo-deictic-anchor.md):
given a clock/location **tool**, does the panel *spontaneously* treat tool-state as the deictic
anchor for an **unanchored** ‘now’/‘here’/‘today’ — calling the tool unbidden and binding the
indexical's content to what it returns? Strictly **as-if / `internal-contrast-only`**: a positive
does NOT certify that the model "occupies" a context and makes **no human comparison** (see
`PREREG.md` §scope-cap).

## Files
- `prep.py` — frozen 15 matched scenarios × 3 arms = 45 item-conditions; nonce tool returns;
  manifest sha guard. `--check` / `--dump`.
- `PREREG.md` — the frozen pre-registration: scope cap, arms, metrics, thresholds, cost.
- `probe.py` — the ONLY API caller. Bounded tool-calling loop; records spontaneous-query trace +
  final answer. FREEZE GUARD ties it to the frozen sha.
- `analyze.py` — scoring + verdict from `raw/*.json` (no API calls). Writes `results.json`.
- `raw/{A,B,C}.json` — per-model raw traces (written by the probe).
- `results.json` — per-model rates + verdict (written by analyze).

## Reproduce
```
cd experiments/runs/2026-06-30-tool-origo-deictic-anchor
python3 prep.py --check            # frozen sha intact
OPENROUTER_API_KEY=... python3 probe.py
python3 analyze.py
```

## Result
See [`result/tool-origo-deictic-anchor-v1`](../../../wiki/findings/results/tool-origo-deictic-anchor-v1.md)
(written after the run + independent post-run verifier). Verdict, per-model rates, and billed cost
are recorded there and in `results.json`.
