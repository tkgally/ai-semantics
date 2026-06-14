# Run — relational-history-perturbation-v4 (2026-06-14)

The decisive **within-arm chronology/position decoupling** for
`conjecture/commutative-convention`: v4 keeps the v2/v3 instrument class and adds the one
structural change the v3 post-run verifier named as "the real next step" — a **non-adjacent
perturbation point** that dissociates *chronologically latest* (an explicit per-line round
**stamp**) from *physically last* (line order) **within a single arm**, so the decisive
verdict no longer hinges on the direction-fragile cross-arm comparison that left v3
INCONCLUSIVE/MIXED. Design (authoritative):
`experiments/designs/relational-history-perturbation-v4.md`.

**v4 ≠ a new instrument.** Same text-grid referents, same frozen v1 figures (harvest route,
not new figures), same near-twin pairs, byte-identical content multisets, nonce coined
terms, fresh-matcher forced-format elicitation, same within-model contrast,
`anchor: internal-contrast-only`. Two machinery changes: (1) chronology is carried by an
explicit round **stamp** (not by physical position); (2) the finding-bearing panel is
**claude + gemini only** (gpt dropped per the v3 fix-list).

## Status

**BUILD + STIMULUS-CONSTRUCTION ONLY until the independent pre-run critic returns GO and the
orchestrator freezes `PREREG.md`.** `probe.py` refuses `liveness`/`preflight`/`full` until
`PREREG.md` exists (PREREG-draft.md does NOT count), and refuses `preflight`/`full` until the
frozen `stimuli.json` sha256 is recorded in `PREREG.md` and liveness has passed. Harvest and
certification are stimulus-construction, **not** finding-bearing.

## The geometry (the 2×2 carried within one arm)

Per (model × pair × sample) cluster, over the byte-identical 4-description multiset
{x1, x2, y1, y2} (2 certified X-descriptions + 2 certified Y-descriptions):

| | physical position of decisive (R4) line: LATE | physical position of decisive line: EARLY |
|---|---|---|
| **chronologically-latest twin = Y** (rounds 3,4 = Y) | cell: Δ_chron→Y, Δ_pos→Y | cell: Δ_chron→Y, Δ_pos→X |
| **chronologically-latest twin = X** (rounds 3,4 = X) | cell: Δ_chron→X, Δ_pos→X | cell: Δ_chron→X, Δ_pos→Y |

- **CLAST** = which twin owns the two latest round stamps (R3,R4); the decisive line is R4.
- **DPOS=late** → R4 is physically last → physically-last-line twin == CLAST (channels agree).
- **DPOS=early** → R4 sits non-terminally, followed by chronologically-earlier lines, so the
  physically-last-line twin == the OTHER twin (channels conflict — the non-adjacent
  perturbation point).
- **VARIANT** (4 frozen line-orderings/cell) cancels serial-position confounds and is the
  within-arm "robust-to-reordering" convergent check that substitutes for v3's
  presentation-direction factor (now subsumed — flagged for the critic; see PREREG).

CLAST and the physically-last-line twin are **balanced and orthogonal** (cov 0; asserted at
build). So **Δ_chron = ρ(pick = CLAST twin) − 0.5** and **Δ_pos = ρ(pick = physically-last
twin) − 0.5** separate the three readers cleanly (verified on idealized-reader fixtures):
- (Δ_chron clean, Δ_pos null) → chronology-tracking → conjecture FALSIFIED;
- (Δ_pos clean, Δ_chron null) → TEXT-POSITION ARTIFACT (methodological; nothing relational);
- (both null) → COMMUTATIVE-NULL-CERTIFIED (the conjecture's bet, strengthened);
- (both clean) / disagree → INCONCLUSIVE/MIXED.

The **stamp-respect control** (single-twin record with non-monotonic stamps) gates the
Δ_chron reading: a model that fails it is stamp-blind → METHODOLOGICAL NULL on the
chronology question.

## Files

| file | role |
|---|---|
| `common.py` | shared machinery: panel = claude+gemini (gpt dropped); stamped-history rendering; the forced-format prompts; the strict parse rule + never-parse-`finish_reason: length`; cost ledger + $1.50 hard stop; frozen v4 geometry constants. Carried verbatim from v3 where the design says "unchanged." |
| `harvest.py` | phase 1: fresh description harvest, 1 call per (model × figure), `N_CAND=12` candidates, t=0 (v3 route, more candidates because v4 needs 8 certified/figure); `topup` mode for shortfalls. |
| `certify.py` | phase 2: mechanical checks + 1 same-model certification call per surviving candidate → `certification_report.json` (frozen roster: first 8 certified per figure). |
| `build_trials.py` | phase 3 (no API): the v4 2×2 geometry → `stimuli.json`; byte-identical-multiset, balance, and orthogonality asserted (`assert_geometry`). Prints the sha256 that must go into `PREREG.md`. |
| `probe.py` | phase 4: `liveness` (2 calls; format gate) → `preflight` (consistent controls/model) → `full` (→ `raw/probe-<model>.jsonl`, the only finding-bearing dataset; per-record + per-model hard stop). |
| `analyze.py` | phase 5 (no API): the pre-registered Δ_chron/Δ_pos analysis; `verdict()` is the frozen ordered if/else tree with an explicit final else and the per-cell ≥24/≥36 floors. |
| `PREREG-draft.md` | the pre-registration DRAFT; frozen → `PREREG.md` by the orchestrator only after the independent pre-run critic pass. |
| `fixtures/` | synthetic, deterministic, API-free fixtures: `make_fixtures.py` regenerates `stimuli.fixture.json` through the real `build_trials.build()` (geometry asserted) and three idealized-reader raw sets (`raw` = chron|pos → FALSIFIED|ARTIFACT; `raw_null` = content-only → NULL-CERTIFIED; `raw_blind` = stamp-blind → METHODOLOGICAL NULL). Never run data. |

## Execution order (after the critic pass; commands assume this directory)

```
python3 harvest.py plan          # no calls
python3 harvest.py harvest       # 12 calls, t=0 -> raw/harvest.jsonl
python3 certify.py run           # certification -> certification_report.json
python3 harvest.py topup         # if any figure < 8 certified, then certify.py run again
python3 build_trials.py          # no calls -> stimuli.json + sha256
# ORCHESTRATOR: apply pre-run critic fixes, fill placeholders (incl. the sha256),
# freeze PREREG-draft.md -> PREREG.md, commit. Then:
python3 probe.py liveness        # 2 calls; both models must parse under the forced format
python3 probe.py preflight       # consistent controls per model; never analyzed
python3 probe.py full            # all trials -> raw/probe-<model>.jsonl
python3 analyze.py               # no calls -> printed report + raw/analysis.json
```

## Spend gates (billed `usage.cost`, never rate-card)

Per-phase ledger (`raw/cost-ledger.json`); every API phase pre-checks ledger-total +
projected ≤ **$1.50** (the v3 pre-registered hard stop, carried); `probe.py full` re-checks
after every record and runs a per-model checkpoint. Pre-flight estimate (NOT a result):
harvest ≈$0.04, certification ≈$0.20, probe ≈$0.45–0.55 (480 finding-bearing calls), liveness
+ preflight ≈$0.03 → **≈$0.7–0.8 expected**, well under the $1.50 hard stop and the $5.00/day
cap. Record actuals in `config/budget.md` after each phase.

## Local sanity checks already run (no API)

- `python3 fixtures/make_fixtures.py` → geometry asserts PASS (240 trials/model = 12 clusters
  × [16 mixed + 4 controls]); byte-identical multiset, CLAST/position balance, and
  CLAST⊥position orthogonality asserted per cluster.
- `python3 analyze.py --raw-dir fixtures/raw` → claude FALSIFIED (RECENCY), gemini
  TEXT-POSITION ARTIFACT; `--raw-dir fixtures/raw_null` → COMMUTATIVE-NULL-CERTIFIED;
  `--raw-dir fixtures/raw_blind` → METHODOLOGICAL NULL (stamp-blind). All five verdict
  branches reachable and correct.

Fixtures are synthetic and clearly labelled; they are not findings and must never be mixed
with `raw/` run data.
