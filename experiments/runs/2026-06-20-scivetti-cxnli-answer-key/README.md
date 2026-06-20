# 2026-06-20 — Scivetti CxNLI answer-key probe

**What this run is.** The first time the project scores the panel against the
**actual human-annotated** Scivetti CxNLI items, rather than the project's own
synthetic minimal pairs. Zero-shot 3-way NLI on the full 390-item Experiment-1 test
set, per-item accuracy vs the released gold labels, vs the ≈0.90 native-speaker
baseline. Runs under the **ratified** anchor
[`resource/scivetti-2025-cxnli-dataset`](../../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)
(Tom, 2026-05-29); bears on the four CxG conjectures (caused-motion / conative /
way-manner / comparative-correlative) and, descriptively, on
[`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md).

Full pre-registration: `PREREG-draft.md` → freezes to `PREREG.md` after the
independent pre-run critic GO.

## Files

| file | role |
|---|---|
| `prep.py` | fetch+parse+freeze recipe (NO API); writes `stimuli-manifest.json` (hash + counts, NO item text); `--check` re-verifies the upstream sha |
| `stimuli-manifest.json` | the frozen hash + per-construction / per-label counts + provenance |
| `probe.py` | panel NLI calls — the ONLY API caller; freeze-guarded (PREREG + analyze + sha re-check); `ABORT_USD = 0.60`; raw stores item-id+gold+label only |
| `analyze.py` | frozen analysis (per-construction accuracy + Wilson CI, overall vs 0.90, confusion, add-vs-cancel descriptive); `--selftest` |
| `PREREG-draft.md` | pre-registration draft (→ `PREREG.md` after pre-run-critic GO) |
| `raw/` | per-model NLI labels (NO premise/hypothesis text) + `cost-log.txt` |

## Recipe-not-corpus

The upstream repo has **no license file**, so per project rules the raw NLI item text
is **not** committed — it lives gitignored under `experiments/data/scivetti/`
(re-clone `github.com/melissatorgbi/beyond-memorization` @ `82699473`). The committed
artifacts are the recipe (`prep.py`), the hash-manifest, and the derived accuracies.

## Stimuli freeze hash

`stimuli-manifest.json` sha256[:16] = **`1c5cffb18c5ef78e`** (390 items, 130/130/130
label balance). `python3 prep.py --check` reproduces it.

## Verified offline

- `python3 prep.py` → 390 items, balance asserts PASS, sha above.
- `python3 prep.py --check` → PASS.
- `python3 analyze.py --selftest` → `selftest PASS`.
- `probe.py` NOT run until `PREREG.md` is frozen (post pre-run-critic GO).
