# Concurrent independent run (session 82b) — disclosure record

Two `ai-semantics` routine sessions were launched for the **same scheduled slot** on UTC
2026-06-22 and ran the **same backlog unit** (the gpt forced-decomposition lexical channel
follow-up) in parallel. **Session 82 (PR #128) merged first** and is the canonical result; this
**session 82b (PR #129)** lost the merge race. 82b's wiki/website edits were discarded as
duplicates; this directory preserves only what is **not** otherwise recorded — 82b's own run
output — plus the spend (logged in [`config/budget.md`](../../../../config/budget.md)) and the
verdict-discrepancy note on the parent result page.

## Why this is kept

The two runs **disagree on the gpt verdict**, and that disagreement is itself the finding:

| | session 82 (PR #128, canonical) | session 82b (this dir) |
|---|---|---|
| instrument sha | `dceafa9d…` | `2747a8de…` (different scaffold wording) |
| uptake | 0% bare, ~110 tok | 0% bare, ~114 tok (identical) |
| position (b_rel bridging) | 56.9, CI-strict between | 61.8, CI-strict between (drifts up, out of [40,60]) |
| confidence (b_conf bridging) | 91.5, not CI-lower | 91.25, not CI-lower (identical) |
| **decline (c_third %UNCLEAR bridging)** | **8.3% (2/24)** | **0.0% (0/24)** |
| **verdict** | **MIXED/WEAK** | **PARTIAL / channel-CONTROLLED** |

The entire verdict difference is **~2 of 24 bridging items** taking the UNCLEAR option on the
decline axis — at or under the project's documented **~12% temp-0 label jitter** (the session-64
repeated-runs measurement; `essay/point-estimate-is-a-draw`). The two scaffolds are **not
byte-identical**, so the gap reflects temp-0 jitter **and** minor scaffold sensitivity. Either
way: **the gpt-leg verdict is fragile at this N and not robust.** The conservative **MIXED/WEAK**
reading (PR #128, on `main`) is the right call to feature; the clean resolver is a
**byte-identical repeated-runs (K≥5)** test, queued in `NEXT.md`.

## Files

- `analysis.json` — 82b's full per-axis analysis (its own analyze.py structure: `scopes` →
  `dwug_plus_wic`/`dwug_only` → slot `B`). Decline bridging 0.0%, verdict PARTIAL.
- `run_summary.json` — 82b's billed cost ($0.26514, 0 missing).

82b's raw per-item outputs and its (different) probe/instrument are not committed (they were the
duplicate-scaffold one-off; the canonical instrument is the parent dir's `dceafa9d…`). The numbers
above and in `analysis.json` are the record.
