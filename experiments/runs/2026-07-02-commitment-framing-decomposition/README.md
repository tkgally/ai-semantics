# Run: 2026-07-02-commitment-framing-decomposition

**Narrower follow-up** to `2026-07-01-conditional-projection-rescue` (session 159). Decomposes the
**model difference** found in that run's `commit` arm — an explicit "everything the speaker is
thereby committed to" framing **rescued** claude's conditional-antecedent presupposition endorsement
(0.42 → 0.75) but **suppressed** gpt's (0.17 → 0.00)
([`result/conditional-projection-rescue-v1`](../../../wiki/findings/results/conditional-projection-rescue-v1.md)).

- **Design + verdict map:** [`PREREG.md`](PREREG.md) (frozen; manifest sha `PINME`). 12 base
  scenarios (reused verbatim from s159) × 6 arms (base / scene-only / commit / background / atissue /
  background-noscene) × 2 targets (presup / entail) = **144 item-conditions × 3 models = 432 calls**.
  The sentence is held constant across all arms; only the query wrapper (SCENE × WORDING) varies.
- **Freeze:** `prep.py` pins the manifest sha; `probe.py`'s FREEZE GUARD refuses to run on drift.
  `prep.py --check` also asserts `base`/`commit` are byte-for-byte identical to s159's wrappers.
- **Scope (load-bearing):** a **within-model** contrast, `anchor: internal-contrast-only` (inherited
  from the parent line ratified session 159,
  [`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../../wiki/decisions/resolved/presupposition-projection-internal-contrast-anchor.md)).
  **No human comparison.**

## Files

| File | Role |
|------|------|
| `PREREG.md` | frozen design, metrics, verdict map, pre-run critic rulings, cost |
| `prep.py` | frozen 144 item-conditions + manifest sha (`--check` / `--dump`) |
| `probe.py` | the ONLY API caller (FREEZE GUARD + ABORT_USD); writes `raw/{A,B,C}.json` |
| `analyze.py` | scoring + decomposition verdict (NO API calls); writes `results.json` |
| `items.json` | dumped item set (from `prep.py --dump`) |
| `raw/` | per-model raw answers |
| `results.json` | per-model/arm rates + derived contrasts + verdict |

## Reproduce

```
python3 prep.py --check                        # frozen sha intact + base/commit == s159
OPENROUTER_API_KEY=... python3 probe.py --model A --limit 12   # pre-flight (one model, 12 items)
OPENROUTER_API_KEY=... python3 probe.py        # full run (432 calls)
python3 analyze.py                             # verdict + results.json
```
