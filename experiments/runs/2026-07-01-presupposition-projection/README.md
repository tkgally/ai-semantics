# 2026-07-01-presupposition-projection

The **presupposition / projection probe** (session 158). Tests
[`open-question/presupposition-projection-corner`](../../../wiki/findings/open-questions/presupposition-projection-corner.md)
and [`conjecture/presupposition-projection-vs-entailment`](../../../wiki/findings/conjectures/presupposition-projection-vs-entailment.md):
does a current model treat a **presupposition** as **projecting** — surviving negation / question /
conditional-antecedent embedding — *more than* a **matched ordinary entailment** on the same base
sentence (the literature's "hallmark of presuppositions", SEP §1.2)?

**Design:** 12 matched base scenarios (4 trigger families × 3 — factive / aspectual / definite /
cleft) × 2 targets (presupposition P vs. matched entailment E) × 4 frames (plain / negation /
question / conditional) = **96 item-conditions** × 3 panel models. Text-only, single-turn,
forced-choice (YES / NO / UNCLEAR). Within-model contrast; **no human comparison**.

**Scope:** `internal-contrast-only` in force; **anchor is `pending`** on a decision opened when the
result is written (`presupposition-projection-internal-contrast-anchor`), ratified only by a later
independent session (charter §12.3). See [`PREREG.md`](PREREG.md) §scope-cap.

## Files

- `prep.py` — frozen stimulus set + FREEZE GUARD (manifest sha
  `e3a04cdd7e3ebbc955b916c15c7d11349ee4d5eb2dbf612c5de12cc1cf6877f9`). `--check` / `--dump`.
- `items.json` — the 96 dumped item-conditions.
- `probe.py` — the ONLY API caller (text-only, temp 0, gemini reasoning minimal). Writes `raw/*.json`.
- `analyze.py` — scoring + pre-registered verdict (NO API calls). Writes `results.json`.
- `PREREG.md` — the frozen pre-registration (question, design, metrics, verdict map, scope cap).
- `raw/` — per-model raw answers.

## Reproduce

```
python3 prep.py --check                       # freeze guard: sha intact
OPENROUTER_API_KEY=... python3 probe.py       # 288 calls -> raw/*.json
python3 analyze.py                            # -> results.json + verdict
```
