# 2026-07-01-projection-trigger-inventory

The **projection trigger-inventory probe** (session 160) — a **generalization test** of the
session-158 projection probe (`2026-07-01-presupposition-projection`). Same instrument, same
scoring path; only the 12 base scenarios change. It asks, for **four additional trigger families the
source explicitly names** (SEP §1.1: temporal clauses, manner adverbs, focus/exclusive *only*,
quantifiers): does a current model treat a **presupposition** as **projecting** — surviving
negation / question / conditional-antecedent embedding — *more than* a **matched ordinary
entailment** on the same base sentence (the literature's "hallmark of presuppositions", SEP §1.2)?

**Design:** 12 matched base scenarios (4 trigger families × 3 — temporal / manner / only /
quantifier) × 2 targets (presupposition P vs. matched entailment E) × 4 frames (plain / negation /
question / conditional) = **96 item-conditions** × 3 panel models. Text-only, single-turn,
forced-choice (YES / NO / UNCLEAR). Within-model contrast; **no human comparison**.

**Reuses s158 verbatim:** `probe.py` and `analyze.py` are byte-for-byte the s158 files (probe.py
differs only in its docstring run-name); the `SYS` / `QUERY` / `FRAMES` and the verdict thresholds
(SANITY 0.75 / SURVIVE 0.60 / GAP 0.30 / FLATBAND 0.15) are identical. So the ratified
`internal-contrast-only` argument transfers.

**Scope:** `internal-contrast-only` in force; **anchor is `pending`** on a decision opened when the
result is written (`projection-trigger-inventory-internal-contrast-anchor`), ratified only by a
later independent session (charter §12.3). See [`PREREG.md`](PREREG.md) §scope-cap.

## Files

- `prep.py` — frozen stimulus set + FREEZE GUARD (manifest sha
  `d0aa515e239413cda77a9b3968af56f95ae05be59ba32761ef3dd5ec6fa17b59`). `--check` / `--dump`.
- `items.json` — the 96 dumped item-conditions.
- `probe.py` — the ONLY API caller (text-only, temp 0, gemini reasoning minimal). Writes `raw/*.json`.
- `analyze.py` — scoring + pre-registered verdict (NO API calls; verbatim s158). Writes `results.json`.
- `PREREG.md` — the frozen pre-registration (question, design, metrics, verdict map, scope cap).
- `raw/` — per-model raw answers.

## Reproduce

```
python3 prep.py --check                       # freeze guard: sha intact
OPENROUTER_API_KEY=... python3 probe.py       # 288 calls -> raw/*.json
python3 analyze.py                            # -> results.json + verdict
```
