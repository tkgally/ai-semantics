# budget.md — OpenRouter spend discipline

Charter §10: Tom monitors OpenRouter spend and will instruct if it runs high. Pause and flag in `NEXT.md` if spend or scope looks wrong.

## Starting cap

**USD 20 / month**, soft. Soft = no automatic enforcement; the lead agent is responsible for staying under it and for surfacing if a planned experiment would blow through it.

Initial cap is conservative on purpose. Most founding-conjecture experiments are minimal-pair behavioral probes; each pair is a few hundred prompt+completion tokens against three models. A 200-item probe at panel-current prices is roughly:

- `panel.A` (claude-sonnet-4.6) — ~$0.60 (in: 200 × ~200 tok × $3/MT + out: 200 × ~100 tok × $15/MT)
- `panel.B` (gpt-5.4-mini) — ~$0.12
- `panel.C` (gemini-3.5-flash) — ~$0.20

So a full 200-item probe across the panel is in the low-single-digit-dollar range. The cap lets several such probes run per month with headroom for critique calls.

## Pre-flight check

Before launching any probe that touches the API, do back-of-envelope:

```
estimated_cost = sum over models of:
    (n_items × avg_in_tokens × pricing.prompt) +
    (n_items × avg_out_tokens × pricing.completion)
```

Use `experiments/runs/2026-05-28-panel-calibration/probe.py` as the cost-template for a single one-shot probe; multiply.

If `estimated_cost` > **$5 in a single run** or > **$10 cumulative against the current month's cap**, **stop and flag in NEXT.md** with the cost estimate before running.

## After each probe

Record actual usage in the run record (under `experiments/runs/<date>-<name>/`):

```
usage:
  panel.A: prompt_tokens=..., completion_tokens=..., cost_usd=...
  panel.B: ...
  panel.C: ...
  total_cost_usd: ...
```

Aggregate to a running ledger here when the second run lands (don't pre-create).

## Spend ledger

| Date | Run | Cost (USD, est.) |
|------|-----|------------------|
| 2026-05-28 | panel calibration (4 one-shot prompts) | ≈ $0.01 |
| 2026-05-29 | comparative-correlative probe v1 (570 calls: 80 items × 2 framings + 30 Scivetti × 3 models) | ≈ $0.124 (A $0.090 / B $0.006 / C $0.029) |
| 2026-05-29 | CxNLI base-vs-distinction probe v1 (600 calls: 100 base + 100 distinction × 3 models) | ≈ $0.162 (A $0.104 / B $0.006 / C $0.052) |
| 2026-05-29 | conative minimal-pair probe v1 (336 calls: 56 items × 2 instruments × 3 models) | ≈ $0.071 (A $0.049 / B $0.003 / C $0.020) |
| 2026-05-29 | caused-motion minimal-pair probe v1 (180 calls: 30 items × 2 instruments × 3 models) | ≈ $0.044 (A $0.027 / B $0.002 / C $0.015) |
| 2026-05-29 | way-construction minimal-pair probe v1 (360 calls: 60 items × 2 instruments × 3 models) | ≈ $0.072 (A $0.052 / B $0.003 / C $0.016) |
| 2026-05-29 | argument-structure coercion probe v2 / off-ceiling (360 calls: 60 items × 2 instruments × 3 models) | ≈ $0.093 (A $0.055 / B $0.003 / C $0.035) |
| 2026-05-30 | cancel-direction conative probe v2 (264 calls) | **$0.300 actual** (token-estimate said $0.059) |
| 2026-05-30 | caused-motion implicit-cue probe v2b (180 calls) | **$0.158 actual** (token-estimate said $0.039) |
| 2026-05-30 | comparative-correlative probe v2 (114 calls) | **$0.109 actual** (token-estimate said $0.026) |
| 2026-05-30 | wasted re-run from a hardcoded-`ITEMS`-path bug (copied probe.py loaded the old coercion-v2 stimuli before the path was fixed; ~1.3 probes' worth, raw discarded) | ≈ $0.30 actual (est.; disclosed; no result contaminated) |

Running total against the $20/month soft cap: **the estimate-based total above (≈$0.56 through 2026-05-29) is a SUBSTANTIAL UNDERCOUNT** — see the note below. Real billed spend is several times higher but still far under the cap.

> **⚠ Estimate-vs-actual discrepancy (discovered 2026-05-30).** Every prior row's figure is a **token-count estimate** from a hardcoded rate card inside each `probe.py`; the **actual OpenRouter-billed cost** (the per-record `usage.cost` field the API returns) is **~4.5× higher** this session (the 3 corrected runs billed **$0.567** vs a $0.124 estimate; e.g. gemini billed ~$0.25 on the conative run vs $0.017 estimated). So the cumulative "≈$0.56" line carried since 2026-05-29 is an underestimate — true cumulative spend is plausibly in the low single dollars. This does **not** threaten the $20/month cap, but the tracking method should be fixed: future `analyze.py`/budget rows should sum the API-returned `usage.cost`, not the local rate-card estimate. **Flagged for Tom** (NEXT.md). Action item: have the probe harness record `usage.cost` going forward.

## When to ask Tom

- If a planned experiment requires more than ~$5 in a single shot.
- If cumulative monthly spend approaches the cap.
- If a probe demands a model not currently in the panel (e.g., GPT-5.5-Pro for some particular capability) — flag and let Tom approve the substitution.

## Out of scope (don't spend on it)

- Open-ended generative writing.
- Long-context reasoning experiments unrelated to a registered conjecture.
- "Smoke tests" — the calibration probe above is enough as a smoke test for the lifetime of the panel; do not repeat it idly.
