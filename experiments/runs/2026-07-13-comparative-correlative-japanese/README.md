# Japanese comparative-correlative replication (A6) — run record

**Session 215 (2026-07-13).** Program A6, the **Japanese** (`〜ば〜ほど`) arm — the stronger,
typologically-distant successor to the German replication. Governed by
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../../wiki/decisions/resolved/cross-linguistic-cc-replication-scope.md)
(Q1-C / Q2-B / Q3-A). Design: [`design/comparative-correlative-japanese-v1`](../../designs/comparative-correlative-japanese-v1.md).
`internal-contrast-only` — no human comparison.

## Files
- `build_items.py` → `../../data/comparative-correlative-japanese/items.csv` (136 items, FROZEN post-C1 sha `31597d29…`; pre-C1 `2d212d92…`).
- `build_cooc_ja.py` → `freq_control.json` (Q2-B UD-Japanese-GSD freq/co-occurrence via janome, FROZEN post-C1 sha `02d275a1…`).
- `probe.py` — the two-instrument (FC + NLI) all-Japanese probe (816 calls).
- `smoke.py` — Japanese-competence gate (36 calls; each model ≥10/12 AND panel mean ≥0.90 → GO).
- `analyze.py` — magnitudes + 95% CIs (cluster bootstrap over pairs, B=2000, seed 20260713) + Q2-B readout.
- `PREREG.md` — the frozen pre-registration + order of operations (anti-cheat).
- `raw/` — probe/smoke outputs + `results.json` (written by the run).
- `REVIEW-critic-s215.md` / `VOTE-critic-s215.json` — the independent pre-run critic + non-Anthropic vote.

## Order (anti-cheat)
build (frozen, committed) → pre-run critic + JA-fidelity vote → smoke gate → probe → analyze. Ported
byte-parallel from `../2026-07-12-comparative-correlative-german/` and the English powered instrument;
the only deliberate change is the target language.
