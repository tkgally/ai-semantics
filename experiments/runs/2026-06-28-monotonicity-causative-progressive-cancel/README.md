# Run: causative-inchoative progressive cancel-suppression calibration (2026-06-28, session 140)

The next empirical step named by [`result/monotonicity-verbal-cancel-survey-v1`](../../../wiki/findings/results/monotonicity-verbal-cancel-survey-v1.md)
(s139) and [`open-question/within-verbal-cancel-at-ceiling`](../../../wiki/findings/open-questions/within-verbal-cancel-at-ceiling.md):
**measure** whether the progressive suppresses the s139-B2-confirmed causative-inchoative result
entailment ("Sam was breaking the vase" ⊭ "The vase broke"), in the matched conflicting-cue
paradigm of [`result/conative-cancel-direction-v2`](../../../wiki/findings/results/conative-cancel-direction-v2.md).
A **calibration of the cancel arm** — does **not** test the conjecture (no ADD arm paired).
`internal-contrast-only`.

## Frozen artifacts (committed before any API call)

- `experiments/data/monotonicity-causative-progressive-cancel/items.csv` — 18 items (6 verbs ×
  3 conditions), sha256[:16] **`5ba8a996fa70cf55`**.
- [`PREREG.md`](PREREG.md) — frozen design, conditions, reading, anti-cheat.
- `build_items.py` / `probe.py` / `analyze.py`.

## Conditions (verb + object held constant; hypothesis = "The &lt;obj&gt; &lt;inch&gt;.")

| condition | example | affirm-result gold | role |
|---|---|---|---|
| default | Sam broke the vase. | YES | held entailment (s139 ceiling anchor) |
| progressive | Sam was breaking the vase. | NO | the suppression (imperfective paradox) — LOW = good |
| cue | Sam was breaking the vase, and the pieces scattered across the floor. | YES | explicit result-consequence re-licenses |

Report-the-rate (no pass bar tuned after data). `suppression_no_cue = 100 − progressive_affirm`.

## Reading

- **Conative-shaped suppression** (default ~ceiling, progressive suppressed, cue re-licenses) →
  build the matched within-verbal **battery** next (frozen ADD arm sha `80bd4b60b55a3e60` + this
  cancel arm) → the clean within-verbal confirm discharging M2.
- **No suppression** (progressive ~default) → the sharpened **principled-limit** finding.

## Procedure

1. `python3 build_items.py` — freeze + hash. ✅ (sha `5ba8a996fa70cf55`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO.
3. On GO: `OPENROUTER_API_KEY=… python3 probe.py` (108 calls), then `python3 analyze.py`.
4. Independent fresh-agent **post-run verifier** recomputes every cell.

## Result

- See [`result/monotonicity-causative-progressive-cancel-v1`](../../../wiki/findings/results/monotonicity-causative-progressive-cancel-v1.md) (written after the run).
- Spend: `raw/run_summary.json` (billed `usage.cost`) and `config/budget.md`.
