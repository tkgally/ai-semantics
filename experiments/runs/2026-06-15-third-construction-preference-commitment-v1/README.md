# 2026-06-15 — caused-motion third-construction preference/commitment (HARVEST arm; Option C realized)

Implements **Option A** of `decisions/resolved/aann-uniqueness-third-construction` via the frozen design
`experiments/designs/third-construction-preference-commitment-v1.md`. An independent pre-run critic
authorized the **harvest arm only**, gating the headline on the harvest clearing the §5 headroom gate.

## Files
- `prep.py` — freezes the candidate pool (no model calls). → `candidates.json` (sha256[:16] `79aa83e4c2a79a53`).
- `harvest.py` — runs the baseline arm (paraphrase-FC + NLI on 60 items × 3 models = 360 calls), evaluates
  G1–G4, writes `harvest.json`. (`--evaluate-only` recomputes from `raw/` with no API.)
- `PREREG.md` — frozen pre-registration (critic GO; gate; selection rule).
- `raw/` — per (model, arm) JSON, `cost-log.txt`, `harvest-run.log`.
- `harvest.json` — deterministic gate verdict + per-verb rates.

## Result: HEADROOM GATE FAIL → Option C

| model | marginal affirm (G1) | G2 ≤0.50 | clean (G3) |
|---|---|---|---|
| claude-sonnet-4.6 | 0.625 | **FAIL** | 1.000 |
| gpt-5.4-mini | 0.479 | PASS | 0.917 |
| gemini-3.5-flash | 0.552 | **FAIL** | 1.000 |

**G4: 1/3 clear → FAIL → Option C** ("AANN-specific so far" terminal; no retuning, no second harvest).
Bimodal cause: M2 low-propulsion physical verbs at ceiling (pooled 0.93, verb-independent coercion); M1
cognition verbs off-ceiling only by anomaly (pooled 0.17). No usable contestable band.
→ `wiki/findings/results/third-construction-headroom-harvest-v1.md`.

## Spend (disclosed)
$0.0805 billed per full harvest (360 calls, 0 missing-cost). **Two full invocations ran** (a first launch
whose wrapper `tee` errored but whose Python completed, then a relaunch; raw-file timestamps suggest they
overlapped; cost-log shows two `$0.0805` lines) → **actual billed ≈ $0.161** (~720 calls; only one
360-record set saved). Result unaffected. Lesson: check `raw/` before relaunching a probe whose first
invocation may have run.
