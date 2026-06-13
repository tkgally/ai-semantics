# Run: AANN temporal held-out widening (v2b) — 2026-06-13

The named follow-up to **caveat 2** of
[`result/aann-behavioral-gradient-v2`](../../../wiki/findings/results/aann-behavioral-gradient-v2.md):
v2's held-out adjective gradient replicated overall but the **temporal noun-class stratum was
≈ −0.2 over only 4 thin cells**. This run widens the temporal stratum 5× (16 → 80 items) under
the **same ratified v2 instrument** (no new operationalization decision) and re-reads it.

**Result:** [`result/aann-temporal-heldout-v2b`](../../../wiki/findings/results/aann-temporal-heldout-v2b.md)
— STILL-TOO-THIN/MIXED; the widened temporal stratum is **uniformly negative at every grain**
for all three models (claude FAILS-TO-REPLICATE; gpt, gemini too-thin). Held-out AANN
productivity is **noun-class-dependent** — strong for the object/distance classes that carried
v2's positive, absent for the temporal class. Does not overturn v2's overall SUPPORTED verdict;
sharpens caveat 2 into a finding.

## Design / governance

- Design addendum: [`experiments/designs/aann-temporal-heldout-v2b.md`](../../designs/aann-temporal-heldout-v2b.md).
- Governed by the ratified instrument
  [`decisions/resolved/aann-behavioral-operationalization`](../../../wiki/decisions/resolved/aann-behavioral-operationalization.md)
  (nine binding conditions) + the frozen v2 design
  [`experiments/designs/aann-construction-v2.md`](../../designs/aann-construction-v2.md). No new decision.
- Pre-run critic returned GO-after-fixes (5 blockers + 8 should-fixes; all applied before freeze).

## Files

- `PREREG.md` — frozen pre-registration (committed before any model call; `probe.py` refuses to
  run without it and without `analyze.py`). `PREREG-draft.md` is the pre-freeze draft, kept verbatim.
- `prep.py` — mirror-independent stimulus generation (builds from the committed v2 artifacts;
  reproduces every v2 Zipf value exactly; aborts otherwise). → `stimuli.json`.
- `stimuli.json` — 80 main held-out temporal items (byte-identical to the pre-critic build) +
  24 verbatim v2 Tier-0 pairs + a 40-item 4-point robustness subsample; embedded freq audit +
  human anchored-half yardstick.
- `probe.py` — three arms (heldout-temporal 240 / tier0 72 / robustness 120 calls), 0–100 +
  4-point + forced-choice prompts byte-identical to v2; `usage.cost` billing; freeze + analyze.py guards.
- `analyze.py` — the frozen pre-registered analysis (verdict mapper as code; `--selftest`, 47 checks).
- `raw/` — per-model per-arm JSONL + `cost-log.txt`.
- `results.json` — the reported analysis output.
- `VERIFIER-REPORT.md` — independent post-run verification (re-derived from raw from scratch, 0 mismatches).

## Spend

432 calls, **$0.0793 billed**, 0 missing-cost. See `config/budget.md` (2026-06-13 row).

## Execution order

```
python3 prep.py            # writes stimuli.json (no model calls)
# orchestrator freezes PREREG.md after the pre-run critic
python3 probe.py           # all arms, all models (refuses without PREREG.md + analyze.py)
python3 analyze.py         # reads raw/, writes results.json
```
