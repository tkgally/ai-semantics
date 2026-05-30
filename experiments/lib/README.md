# experiments/lib — shared probe harness

Small importable helpers for probe runs, so each dated `experiments/runs/<date>-<name>/`
does not re-implement (and re-bug) the OpenRouter plumbing. Runs stay self-contained for
the *science* (their own `build_items.py` + frozen `items.csv` + `analyze.py`); they import
only the **mechanical** call/cost plumbing from here.

## `openrouter.py`

- `PANEL` — slot→slug map mirroring [`config/models.md`](../../config/models.md) (the source of
  truth; keep in sync by hand when the panel changes).
- `call(model, system, user, max_tokens=None, ...)` → `{content, usage, error}`. Sets
  `"usage": {"include": true}` so OpenRouter returns the **billed** `usage.cost`; defaults
  google/* to a large `max_tokens` (the reasoning-token caveat in `config/models.md`); retries
  with exponential backoff.
- `billed_cost(record_lists)` → `(total_usd, n_with_cost, n_missing_cost)`. Sums the
  API-returned `usage.cost`. **This is the figure to record** in the run README and the
  `config/budget.md` ledger.
- `estimated_cost(record_lists, model)` → rate-card estimate. **Fallback only** — documented
  to undercount real spend ~4.5x (2026-05-30 finding). Use only if `billed_cost` reports
  missing costs (a provider that does not report `usage.cost`).

### Why this exists

The 2026-05-30 session found every prior `probe.py` recorded a rate-card *estimate* that
undercounts the real OpenRouter bill ~4.5x, because (a) the request never asked for
`usage.cost` and (b) the local card omits reasoning/cache/byok adjustments. This module
fixes both: future runs import `call` + `billed_cost` and record actual spend. Closes the
maintenance item flagged in `NEXT.md`. Verified 2026-05-30 on a live call
(billed $3.6e-05 vs estimate $6.6e-06 for the same gpt-5.4-mini reply).

### Copy-from pattern

```python
import csv, json, os, sys, time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

# ... build user prompts from your frozen items.csv, collect records with r["usage"] ...
total, have, missing = billed_cost([nli_recs, fc_recs])   # record `total` in the README
```
