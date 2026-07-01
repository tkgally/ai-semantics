# Run: 2026-07-01-conditional-projection-rescue

**Follow-up** to `2026-07-01-presupposition-projection` (session 158). Tests whether the
across-panel **conditional-antecedent projection collapse** found there
([`result/presupposition-projection-v1`](../../../wiki/findings/results/presupposition-projection-v1.md))
is **rescuable** by an explicit framing or is a **robust** feature of the text-trained behavior.

- **Design + verdict map:** [`PREREG.md`](PREREG.md) (frozen; manifest sha
  `c88ef626…`). 12 base scenarios (reused verbatim from s158) × 4 arms (base / commit / conseq /
  belief) × 2 targets (presup / entail) = **96 item-conditions × 3 models = 288 calls**.
- **Freeze:** `prep.py` pins the manifest sha; `probe.py`'s FREEZE GUARD refuses to run on drift.
- **Scope (load-bearing):** a **within-model** contrast, `anchor: internal-contrast-only` (the parent
  line was ratified this session,
  [`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../../wiki/decisions/resolved/presupposition-projection-internal-contrast-anchor.md)).
  **No human comparison.**

## Files

| File | Role |
|------|------|
| `PREREG.md` | frozen design, metrics, verdict map, cost |
| `prep.py` | frozen 96 item-conditions + manifest sha (`--check` / `--dump`) |
| `probe.py` | the ONLY API caller (FREEZE GUARD + ABORT_USD); writes `raw/{A,B,C}.json` |
| `analyze.py` | scoring + rescue verdict (NO API calls); writes `results.json` |
| `items.json` | dumped item set (from `prep.py --dump`) |
| `raw/` | per-model raw answers |
| `results.json` | per-model/arm rates + verdict |

## Reproduce

```
python3 prep.py --check                       # frozen sha intact
OPENROUTER_API_KEY=... python3 probe.py --model A --limit 8   # pre-flight (one model, 8 items)
OPENROUTER_API_KEY=... python3 probe.py       # full run (288 calls)
python3 analyze.py                            # verdict + results.json
```
