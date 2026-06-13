# Run — relational-history-perturbation-v3 (2026-06-13)

Second attempt at the decisive history-perturbation test of
`conjecture/commutative-convention`: the v2 instrument with the post-run verifier's
five-item fix-list repaired (truncation-proof forced-format elicitation; fresh
per-description-certified stimuli for all three models; 9 clusters/model/direction;
the ≥3-gated-cluster guard on every CI-bearing clause; the both-directions arm
retained). Design (authoritative):
`experiments/designs/relational-history-perturbation-v3.md`. Supersedes
`experiments/runs/2026-06-12-relational-history-perturbation-v2/` (outcome there:
INCONCLUSIVE/MIXED for all three models).

**Status: BUILD ONLY — no API calls have been made from this directory.**
`PREREG-draft.md` is a draft; it must be frozen as `PREREG.md` by the orchestrator only
after the independent pre-run critic's fixes are applied. `probe.py` refuses to run
without `PREREG.md` (the draft does not count), and refuses `preflight`/`full` until
the frozen `stimuli.json` sha256 is recorded in `PREREG.md` and liveness has passed.

## Files

| file | role |
|---|---|
| `common.py` | shared machinery: panel (from `lib/openrouter.py` PANEL), forced-format prompts, the pre-registered strict parse rule + one stern retry, cost ledger + $1.50 hard stop, frozen constants (orders, directions, nonces, seeds). |
| `harvest.py` | phase 1: fresh description harvest, 1 call per (model × figure), 8 candidates per numbered-list call, t=0; `topup` mode (one t=0.8 call per shortfall figure, pre-registered). |
| `certify.py` | phase 2: mechanical checks (non-empty, ≤12 words, dedup within figure + against twin) then ONE same-model certification call per surviving candidate → `raw/certification.jsonl` + `certification_report.json` (frozen roster: first 6 certified per figure, deterministic harvest order; anti-null bias disclosure embedded). Idempotent. |
| `build_trials.py` | phase 3 (no API): frozen trial set → `stimuli.json` (9 clusters/model: 108 mixed + 18 consistent controls per model = 378 calls; byte-identical multisets asserted; per-cluster matcher arrays frozen in; certification census embedded). Prints the sha256 that must go into `PREREG.md`. |
| `probe.py` | phase 4: `liveness` (3 calls; format gate) → `preflight` (gpt controls, 18 calls) → `full` (378 + retries → `raw/probe-<model>.jsonl`, the only finding-bearing dataset). Freeze + format + cost gates enforced in code. |
| `analyze.py` | phase 5 (no API): the pre-registered analysis; the verdict mapper is code (`verdict()`), not prose. Writes `<raw-dir>/analysis.json`. |
| `PREREG-draft.md` | the pre-registration DRAFT (decision rule mirrored verbatim from the design); placeholders for the stimuli hash, critic revisions, any recorded shortfall. |
| `fixtures/` | synthetic, deterministic, API-free sanity fixtures (see below). Never run data. |

All scripts run from the repo root or from this directory (paths are
`__file__`-anchored). Python stdlib only.

## Execution order (after the critic pass; commands assume this directory)

```
python3 harvest.py plan          # no calls: planned calls + estimate
python3 harvest.py harvest       # 18 calls, t=0            -> raw/harvest.jsonl
python3 certify.py run           # <=144 calls              -> raw/certification.jsonl,
                                 #                              certification_report.json
# if any figure < 6 certified:
python3 harvest.py topup         # <=18 calls, t=0.8 (one per shortfall figure), then:
python3 certify.py run           # certifies only the new candidates (idempotent)
                                 # persisting shortfall => reduced cluster count,
                                 # recorded in PREREG before the freeze
python3 build_trials.py          # no calls -> stimuli.json + sha256 printed
# ORCHESTRATOR: apply pre-run critic fixes, fill placeholders (incl. the sha256),
# freeze PREREG-draft.md -> PREREG.md, commit. Then:
python3 probe.py liveness        # 3 calls; all three must parse under the forced format
python3 probe.py preflight       # 18 calls (gpt controls); never analyzed
python3 probe.py full            # 378 calls (+retries) -> raw/probe-<model>.jsonl
python3 analyze.py               # no calls -> printed report + raw/analysis.json
```

Note on phase/file naming vs the design: the design's run plan names `harvest.py`
(harvest **+ certification**) and `build_stimuli.py`; this build splits certification
into `certify.py` and names the trial constructor `build_trials.py`, with the frozen
artifact keeping the design's name `stimuli.json` and the same freeze discipline
(sha256 in `PREREG.md` before any finding-bearing call). Substance unchanged; flagged
for the orchestrator.

## Spend gates (billed `usage.cost`, never rate-card)

- Every API phase appends to `raw/cost-ledger.json` (phase, calls, billed, missing-cost
  count, UTC timestamp).
- Every API phase pre-checks: ledger-total + projected-phase-cost must stay ≤ **$1.50**
  (the design's pre-registered hard stop) or the script exits before calling.
- `probe.py full` additionally re-checks cumulative billed cost **after every record**
  and aborts mid-run at $1.50 (raw kept; re-design, don't push through). Its pre-check
  projects from the preflight billed per-call figure × 1.2 retry headroom.
- Estimates (design table): harvest ≈$0.05, certification ≈$0.17, probe ≈$0.55,
  liveness+preflight ≈$0.02 → ≈$0.80 expected, <$1.00 stated expectation, $1.50 hard
  stop, all under the $2.50 single-run flag and the $5.00/day cap. Record actuals in
  `config/budget.md` after each phase (ledger rows are the source).

## Planned call count

18 harvest (+≤18 top-up) + ≤144 certification (+top-up candidates) + 3 liveness + 18
preflight + **378 finding-bearing** (+ ≤378 worst-case retries; the forced format and
liveness gate exist to keep retries near zero) ≈ 575–650 total.

## Local sanity checks already run (no API)

- `python3 fixtures/make_fixtures.py` regenerates: a synthetic
  `certification_report.fixture.json`, `stimuli.fixture.json` built through the real
  `build_trials.build()` (geometry asserted: 126 trials/model, 378 total, byte-identical
  multisets per cluster), and synthetic `fixtures/raw/probe-*.jsonl`.
- `python3 analyze.py --raw-dir fixtures/raw` exercises three verdict branches and
  prints them: claude → FALSIFIED (RECENCY), gpt → COMMUTATIVE-NULL-CERTIFIED
  (54 in-pair trials/direction ≥ 36 floor), gemini → METHODOLOGICAL NULL (2 gated
  clusters < k=3). Degenerate-CI handling visible in the gemini block and the
  pair-level cross-check.
- Freeze gate verified: `probe.py liveness` refuses while only `PREREG-draft.md`
  exists; `build_trials.py` hash-checks the frozen v1 `figures.json`
  (`a2709582…`) before building.

Fixtures are synthetic and clearly labelled; they are not findings and must never be
mixed with `raw/` run data.
