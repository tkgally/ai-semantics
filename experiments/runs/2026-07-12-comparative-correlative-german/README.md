# 2026-07-12 — German comparative-correlative replication (A6, s213)

Cross-linguistic replication of the flagship English CC construction-isolation result in **German**
(`je…desto/umso`), testing whether the covariation reading is construction-driven rather than
English-n-gram-driven. Governed by
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../../wiki/decisions/resolved/cross-linguistic-cc-replication-scope.md)
(Q1-C / Q2-B / Q3-A, ratified s213). Design:
[`design/comparative-correlative-german-v1`](../../designs/comparative-correlative-german-v1.md).
**Internal-contrast-only** (no non-English CC human dataset exists).

## Files
- `build_items.py` → `data/comparative-correlative-german/items.csv` — 34 German scale pairs × 4 forms
  = 136 items (FROZEN, sha in PREREG). A faithful port of the English powered instrument; only the
  target language changes.
- `build_cooc_de.py` → `freq_control.json` — Q2-B UD-German-GSD (CC BY-SA 4.0) frequency/co-occurrence
  control (FROZEN before the run).
- `smoke.py` → `raw/smoke_results.json` — German-competence gate (each model ≥10/12 AND mean ≥0.90).
- `probe.py` → `raw/` — the German FC + NLI probe (run only after the critic GO + smoke GO).
- `analyze.py` → `raw/results.json` — magnitudes + 95% CIs (cluster bootstrap over pairs) + freq control.
- `PREREG.md` — frozen pre-registration + item self-audit (condition viii).
- `REVIEW-ratify-s213.md` / `VOTE-ratify-s213.json` — the scope-decision ratification record.
- `REVIEW-critic-s213.md` / `VOTE-critic-s213.json` — the pre-run critic record (added at critic step).

## Order of operations (anti-cheat)
build_items → build_cooc_de → **freeze (sha)** → pre-run critic → smoke gate → probe → analyze.
