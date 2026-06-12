# Run record — relational-history-perturbation-v2 (2026-06-12)

The decisive test of `conjecture/commutative-convention` (the v2 history-perturbation arm
recommended by the ratified `decisions/resolved/relational-pilot-operationalization`).
Design: `experiments/designs/relational-history-perturbation-v2.md`. Frozen protocol:
`PREREG.md` (includes the pre-run critic's revisions — presentation-direction control arm,
per-cluster manipulation gate, constant matcher arrays, retry-once, 64→128 token cap).
Result page: `wiki/findings/results/relational-history-perturbation-v2.md`.

## Outcome (one line)

**INCONCLUSIVE/MIXED for all three models** — the falsification clause did not fire and the
commutative null was not certified; claude's CI-clean forward-arm elevation vanishes in the
reversed arm (where it points anywhere, it points to physical prompt position, not
chronology); gpt effectively uninformative (1/6 clusters passed its own gate); gemini
descriptive-only by pre-registration.

## Pipeline

1. `build_stimuli.py` → `stimuli.json` (sha256 `0e4d315c…`, committed before any
   finding-bearing call; includes the per-description v1 live-quality census).
2. `probe.py liveness` (3 calls; first attempt caught a claude truncation → 64→128 cap fix,
   logged in PREREG; re-run clean) → `probe.py preflight` (gpt consistent controls, 12 calls)
   → `probe.py full` (210 calls + 11 retries → `raw/results.json`).
3. `analyze.py` (pre-registered measures only) → output mirrored in the result page.
4. Independent post-run verifier: re-derived every field from raw from scratch — **zero
   mismatches across all 210 records**; CI bounds reproduce under a different seed; verdict
   rule-walk correct per PREREG, "no dodging in either direction"; sensitivity cuts (pair-2
   exclusion; NAs-as-out-of-pair; truncated-parsed drops) leave every verdict unchanged.

## Billed cost (`usage.cost` summed, 0 missing)

| phase | calls | billed |
|---|---|---|
| liveness (pre-fix, truncated; raw discarded by rule) | 3 | $0.00604 |
| liveness (post-fix; not analyzed) | 3 | $0.00267 |
| preflight (gpt controls; not analyzed) | 12 | $0.00443 |
| **full (the finding-bearing dataset)** | 210 (+11 retries) | **$0.27686** |
| **total** | | **$0.290** |

Day total 2026-06-12: $0.290 of the $5.00/day cap (ledger row in `config/budget.md`).

## Known limitations (full list on the result page)

- Claude truncation non-random: 11/72 mixed trials NA (all pair-2, 8 fwd) at the 128 cap;
  10 truncated-but-parsed picks may be deliberation-mentions (sensitivity cuts hold).
- gpt manipulation quality poor (control acc 0.42) — effectively uninformative.
- Single/identical-cluster bootstrap CIs are degenerate (zero-width) and carry no weight.
- Falsification clause lacks a minimum-cluster guard (latent; flag for any v3).
