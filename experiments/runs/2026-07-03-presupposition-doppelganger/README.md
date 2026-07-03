# 2026-07-03-presupposition-doppelganger

The **presupposition doppelgänger (matched surface-cue) control** (session 173, program item **A1a**).
Tests [`design/presupposition-doppelganger-control-v1`](../../designs/presupposition-doppelganger-control-v1.md)
under the ratified gate
[`decisions/resolved/presupposition-doppelganger-control-design`](../../../wiki/decisions/resolved/presupposition-doppelganger-control-design.md).

**The one question:** does the presupposition/projection corner beat a **matched surface-cue
doppelgänger** — items with the *same* trigger word-form/frame but *without* the presuppositional
structure — or does the doppelgänger endorse the same content just as much (a **measured**
shadow-saturated corner)? The measure is a within-model residual `trigger P-endorse − D1 doppelgänger
P-endorse` over the two projecting frames (negation + question).

**The two outcomes are NOT symmetric (B1/B2):** the **null** (SHADOW-SATURATED) is the cleanly-licensed
diagnostic prize (a measured saturated row); a **positive** residual is under-licensed — it claims only
"endorsement keyed to the trigger word-form", is reconstructable by a verb-sensitive surface-cue
follower, and does **not** fire the essay's revision trigger. See [`PREREG.md`](PREREG.md).

**Design:** 22 base scenarios — factive/aspectual/cleft **6 each (powered)** + definite **4
(exploratory, dropped from the verdict per S1)** — × 2 legs (trigger / D1 doppelgänger) × 4 frames
(plain / negation / question / conditional) + 1 D2 metalinguistic structure-defeat leg = **198
item-conditions × 3 panel models**. Powered, verdict-bearing residual rests on **72 residual-bearing
conditions/model** (S3). Text-only, single-turn, forced-choice (YES / NO / UNCLEAR). Within-model
contrast; **no human comparison**.

**Scope:** `internal-contrast-only` in force; **anchor `pending`** on the resolved doppelgänger
decision, terminal status confirmed only by a later independent session (charter §12.3).

## Files

- `prep.py` — frozen stimulus set + FREEZE GUARD (manifest sha
  `4500fc5b2c66a6d35355ed80b6f7d7a60090ce80476cf8faf0533ac8d97a183a`). `--check` / `--dump`.
- `items.json` — the 198 dumped item-conditions.
- `probe.py` — the ONLY API caller (text-only, temp 0, gemini reasoning minimal). Writes `raw/*.json`.
- `analyze.py` — scoring + pre-registered per-family verdict + S4 sensitivity (NO API calls). Writes `results.json`.
- `PREREG.md` — the frozen pre-registration (question, design, S1–S4/N1–N2, metrics, verdict map, scope cap).
- `raw/` — per-model raw answers.

## Reproduce

```
python3 prep.py --check          # verify frozen sha
OPENROUTER_API_KEY=... python3 probe.py     # all three models → raw/*.json
python3 analyze.py               # per-family + pooled verdict + S4 sensitivity → results.json
```
