# budget.md — OpenRouter spend discipline

Charter §12.4: the project runs autonomously; the lead agent enforces the cap on itself and
records every billed cost here. Pause and flag in `NEXT.md` if spend or scope looks wrong.

## Cap

**USD 5.00 per calendar day (UTC)**, soft, all-in across every part of the project and across
**all sessions that day combined** (Routines may start several sessions in one day — check
today's ledger rows before spending). Soft = no automatic enforcement; the lead agent is
responsible for staying under it. Unused budget does **not** roll over. There is no one to ask
for an exception: a probe that does not fit within today's remaining headroom is split, scaled
down, or deferred to a later day, with the deferral noted in `NEXT.md`.

> **Ratified 2026-06-12 (Tom, autonomous-era transition):** cap set to **$5.00/day (UTC)**,
> replacing the $20/week regime, with full autonomy to spend within it. Keep logging the
> API-returned `usage.cost` (use `experiments/lib/openrouter.py`). Gemini reasoning + image
> tokens remain the known cost drivers — keep `reasoning:{effort:"minimal"}` on large gemini
> runs and images small / low-detail. (Historical ledger rows below were run under the earlier
> $20/month and $20/week caps; they are left unchanged as an audit trail.)
>
> **History:** founding cap $20/month (2026-05-28) → $20/week (ratified 2026-05-31) →
> **$5/day (ratified 2026-06-12)**.

The cap is conservative on purpose. Most founding-conjecture experiments are minimal-pair behavioral probes; each pair is a few hundred prompt+completion tokens against three models. A 200-item probe at panel-current prices is roughly:

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

Use `experiments/runs/2026-05-28-panel-calibration/probe.py` as the cost-template for a single one-shot probe; multiply. This is only a *pre-flight estimate* — the recorded figure must be the **actual billed** cost (see below).

Remember the estimate undercounts real billing by up to ~4.5× (2026-05-30 finding) — budget
against the *billed* expectation, not the rate-card one. If the billed expectation exceeds
**$2.50 in a single run** (half the daily cap), prefer to split or scale the probe; if it would
take **today's combined billed total over $5.00**, do not run it — defer to a later day and note
the deferral in `NEXT.md`.

## After each probe

Record **actual billed** usage in the run record (under `experiments/runs/<date>-<name>/`).
**Use the API-returned `usage.cost`, not the rate-card estimate** — the estimate undercounts
real spend ~4.5x (2026-05-30 finding). The shared harness [`experiments/lib/openrouter.py`](../experiments/lib/openrouter.py)
does this for you: `call()` requests `usage.cost` (via `"usage": {"include": true}`) and
`billed_cost()` sums it. New probes should import from there rather than re-implement the
estimate. (Legacy ledger rows below this date are estimates and are flagged as undercounts.)

```
usage:
  panel.A: prompt_tokens=..., completion_tokens=..., cost_usd=...   # cost_usd = summed usage.cost
  panel.B: ...
  panel.C: ...
  total_cost_usd: ...   # = billed_cost([...]) ; flag any n_missing_cost > 0
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
| 2026-05-30 | comparative-correlative probe v3 / embedded-CC operator-scope (96 calls) | **$0.09326 billed** (A $0.01705 / B $0.00419 / C $0.07202; first run summing API `usage.cost` — gemini billed 14× its $0.005 estimate) |
| 2026-05-30 | caused-motion near-miss form-control probe v2c (96 calls) | **$0.21213 billed** (A $0.02276 / B $0.00555 / C $0.18382; gemini ~15× its $0.013 estimate, reasoning-token heavy) |
| 2026-05-30 | lexical-sense-gradience probe v1 / first LEXICAL probe (1800 calls: 200 pairs × 3 framings × 3 models) | **$3.13410 billed** (A $0.42291 / B $0.10500 / C **$2.60619**; gemini ~14.5× its $0.18 estimate). Priciest single run to date; under the $5 single-run flag but flags **gemini reasoning-token cost as the dominant budget driver on multi-call probes** — consider `reasoning:{effort:"none"}` or a lower gemini `max_tokens` for large runs. |
| 2026-05-30 | coercion-as-sense-modulation bridge probe v1 (180 calls: 30 items × 2 framings × 3 models) | **$0.24864 billed** (A $0.024 / B $0.012 / C $0.212). Lexicon–grammar bridge. |
| 2026-05-30 | wasted re-run from a hardcoded-`ITEMS`-path bug (copied probe.py loaded the old coercion-v2 stimuli before the path was fixed; ~1.3 probes' worth, raw discarded) | ≈ $0.30 actual (est.; disclosed; no result contaminated) |
| 2026-06-12 | **relational history-perturbation probe v2** (210 finding-bearing calls + retries: full **$0.27686** billed; gpt-controls preflight $0.00443; liveness $0.00267 + one pre-fix truncated liveness $0.00604 — all `usage.cost`-summed, 0 missing) | **$0.290 billed total** (session 1; cap $5.00/day) |
| 2026-06-12 | **AANN behavioral probe v2** (second session same UTC day; 1,782 calls: 3 models × [408 anchored + 102 robustness + 60 held-out + 24 Tier-0]; `usage.cost`-summed, **0 missing in every arm**; gemini `effort: minimal` + 512-token cap) | **$0.3125 billed** (A $0.1934 / B $0.0476 / C $0.0715). Pre-flight estimated $1.0–1.5 — actual came in ~4× *under*; single-integer outputs are cheap. **Day total 2026-06-12: ≈$0.60 of $5.00.** |
| 2026-05-31 | **relational reference-game pilot v1** — the most call-heavy probe to date (3 models × 2 games × live dyad + nickname + 4-arm replay probe + monologue baseline = 864 calls) | **$0.94544 billed** (A $0.583 / B $0.117 / C $0.245; `usage.cost` summed, 0 missing). **Gemini held to `reasoning:{effort:"minimal"}` — the cost-driver mitigation worked** (C only $0.245 for 288 calls, vs the lexical-v1 run where gemini alone billed $2.6). Plus a crashed-after-calls claude preflight (~$0.30, disclosed, no data kept) + two cheap gpt preflights (~$0.11). First run under the **$20/week** cap; week-1 billed ≈ $1.4 for this work, far under cap. |
| 2026-06-13 | **AANN temporal held-out widening v2b** (432 calls: heldout-temporal 240 + fresh Tier-0 72 + 4-point robustness 120, × 3 models; `usage.cost`-summed, **0 missing**) | **$0.0793 billed**. Pre-flight estimated $0.08–0.15; came in at the low end. |
| 2026-06-13 | **relational history-perturbation v3** (the commutativity test, 2nd attempt; harvest 18 + topup 8 + certification 207 + liveness 3 + preflight 15 + **full probe 384** finding-bearing calls; `usage.cost`-summed, **0 missing in every phase**; 0 truncation) | **$0.61133 billed total** (full arm $0.38599; certification $0.15322; harvest/topup $0.05181; liveness+preflight $0.02029). Under the $1.50 hard-stop; gemini held to `effort: minimal`. **Day total 2026-06-13 (sessions 1–2): ≈$0.69 of $5.00.** |
| 2026-06-13 | **AANN inferential v3** (3rd session same UTC day; the repaired-and-rerun inferential probe; 624 calls = 208/model × 3: paraphrase 138 + nli 276 + agreement 138 + tier0 72; `usage.cost`-summed, **0 missing in every arm, 0 missing-cost calls**; gemini `effort: minimal` + 512-token cap) | **$0.0910 billed** (A claude / B gpt / C gemini single-token FC/NLI arms). Pre-flight estimated $0.11–0.20; came in just under. ABORT_USD=$0.50 never approached. **Day total 2026-06-13 (sessions 1–3): ≈$0.78 of $5.00.** |
| 2026-06-13 | **AANN inferential v4** (5th session same UTC day; the distributive-default-control redesign; 831 calls = 277/model × 3: paraphrase 207 + nli 414 + agreement 138 + tier0 72, three premise frames AANN/DDC/LCC on paraphrase+NLI; `usage.cost`-summed, **0 missing in every arm, 0 missing-cost calls**; gemini `effort: minimal` + 512-token cap) | **$0.1266 billed**. Pre-flight estimated $0.12–0.20 (831 × v3's measured $0.0001458/call ≈ $0.121); came in at the point estimate. ABORT_USD=$0.50 never approached. **Day total 2026-06-13 (sessions 1–5): ≈$0.91 of $5.00.** |
| 2026-06-14 | **AANN agreement-reflex generalization v5** (sixth session, new UTC day; the held-out reflex generalization probe, NEXT.md 2a; 246 calls = 82/model × 3: agreement 180 + diagnostic 30 + tier0 36; `usage.cost`-summed, **0 missing in every arm, 0 missing-cost calls**; gemini `effort: minimal` + 512-token cap) | **$0.0320 billed**. Pre-flight estimated $0.03–0.06 (246 × v4's measured ~$0.00015/call ≈ $0.037); came in at the low end. ABORT_USD=$0.25 never approached. **Day total 2026-06-14 (session 6): $0.032 of $5.00.** |
| 2026-06-14 | **relational history-perturbation v4** (seventh session, same UTC day; the within-arm chronology/text-position decoupling; claude+gemini only [gpt dropped]; stimulus construction: harvest 12 + topup 6 + certification 204 = $0.2169; then liveness 2 + preflight 23 + **full 460 finding-bearing** = 485 probe calls; `usage.cost`-summed, **0 missing in every phase, 0 NA, 0 retried, strict-compliance 1.000**; gemini `effort: minimal` + 512-token cap) | **$0.62964 billed (full)**; session all-phases **$0.94225** (harvest $0.0417 / topup $0.0198 / certification $0.2169 / liveness $0.0027 / preflight $0.0315 / full $0.6296). Pre-flight estimated ≈$0.78; came in at $0.94 (gemini per-call ran a touch higher). $1.50 hard stop never approached. **Day total 2026-06-14 (sessions 6–7): ≈$0.974 of $5.00.** |

Running total (all rows above predate the 2026-05-31 raise and ran under the old $20/month
cap): **the estimate-based total above (≈$0.56 through 2026-05-29) is a SUBSTANTIAL
UNDERCOUNT** — see the note below. Real billed spend is several dollars but still far under
any cap. **From 2026-05-31 the cap is $20/week (soft); track weekly billed `usage.cost`.**

> **⚠ Estimate-vs-actual discrepancy (discovered 2026-05-30).** Every prior row's figure is a **token-count estimate** from a hardcoded rate card inside each `probe.py`; the **actual OpenRouter-billed cost** (the per-record `usage.cost` field the API returns) is **~4.5× higher** this session (the 3 corrected runs billed **$0.567** vs a $0.124 estimate; e.g. gemini billed ~$0.25 on the conative run vs $0.017 estimated). So the cumulative "≈$0.56" line carried since 2026-05-29 is an underestimate — true cumulative spend is plausibly in the low single dollars. This does **not** threaten the $20/month cap, but the tracking method should be fixed: future `analyze.py`/budget rows should sum the API-returned `usage.cost`, not the local rate-card estimate. **Flagged for Tom** (NEXT.md). Action item: have the probe harness record `usage.cost` going forward.

## When to defer or queue a decision (there is no one to ask)

- A planned experiment whose billed expectation exceeds **$2.50 in a single shot** → split or
  scale it; if it genuinely cannot be split, run it as the day's only spend and say so in the
  run record.
- Today's combined billed total would exceed **$5.00** → defer the probe to a later day.
- A probe demands a model not currently in the panel → that is a panel-change
  operationalization question: queue it in `wiki/decisions/open/` (with a provisional default)
  for cross-session ratification; do not swap models silently.

## Out of scope (don't spend on it)

- Open-ended generative writing.
- Long-context reasoning experiments unrelated to a registered conjecture.
- "Smoke tests" — the calibration probe above is enough as a smoke test for the lifetime of the panel; do not repeat it idly.
