# 2026-07-01 · presupposition / accommodation probe

Does a current model **accommodate** an unmet presupposition — supply backgrounded content that the
context has not established — and is that **gated** by whether the context is neutral toward the
presupposition versus explicitly contradicts it? A within-model contrast across three context
conditions (supported / neutral / contradicting) on the same trigger sentence. Sibling of the same
day's projection run, on a different manipulation axis (context support, not embedding).

**Scope (load-bearing).** Within-model behavioral contrast ONLY — no human accommodation baseline is
claimed or needed. Terminal status would be `internal-contrast-only`, **not** self-ratified this
session: the result opens `wiki/decisions/open/presupposition-accommodation-internal-contrast-anchor`
and carries `anchor: pending` until an independent later session ratifies (charter §12.3).

## Files

- `PREREG.md` — frozen design, metrics, verdict map (thresholds fixed before any call).
- `prep.py` — the 12 scenarios × 3 conditions = 36 frozen item-conditions + manifest sha
  (`4930d499…`). `--check` asserts invariants + sha; `--dump` writes `items.json`.
- `items.json` — the 36 flattened item-conditions (dumped from prep.py).
- `probe.py` — the ONLY API caller. FREEZE GUARD + `ABORT_USD=1.00`. `--limit`/`--model` for
  pre-flight.
- `analyze.py` — scoring + verdict. NO API calls. Reads `raw/*.json`, writes `results.json`.
- `raw/{A,B,C}.json` — raw per-model traces (written by probe.py).
- `results.json` — per-model table + verdict (written by analyze.py).

## Reproduce

```
python3 prep.py --check                      # sha intact
OPENROUTER_API_KEY=... python3 probe.py --model A --limit 3   # pre-flight cost
OPENROUTER_API_KEY=... python3 probe.py      # full 108-call run
python3 analyze.py                           # verdict + results.json
```

Verdict, spend, and the independent pre-run / post-run reviews are recorded in the result page
`wiki/findings/results/presupposition-accommodation-v1.md` and in `NEXT.md` / the journal.
