# Run — relational stamp-comprehension pre-probe / Option B (2026-06-16)

The **Option-B** gate from the ratified decision
[`relational-v5-text-position-neutralization`](../../../wiki/decisions/resolved/relational-v5-text-position-neutralization.md)
(adopt-default, 2026-06-16 cross-session adversarial review: **B then A, staged; C binding
fallback**). It answers one question, cheaply, before any geometry-decoupled chronology arm:

> Do the panel models read the round **stamp** as a recency value **at all**, when physical
> line-position is neutralized so only the stamp value disambiguates?

v4 found both models follow physical text-position, and its binding scope limit is that
*"position-following here is indistinguishable from stamp-blindness."* B resolves exactly that
ambiguity. It is a **gate**, not a relational result.

## Verdict and routing (frozen — see PREREG)

Per model: **PASS** iff accuracy ≥ 0.80 **and** Wilson-95 lower bound > 1/K (0.25); else
**FAIL** (stamp-blind on this instrument).

- PASS → that model earns an Option-A position-rotated, stamp-gated chronology arm (later phase).
- FAIL → v4's position-following is explained as stamp-blindness for it.
- **Both FAIL → close the relational-history line at Option C** (no stamp-format retune, no B
  re-run — anti-cheat carry-forward).

## Instrument (no near-twin harvest needed)

Each record = K=4 stamped lines, each coupling a non-contiguous round number to a frozen nonce
convention; two query directions (MR = latest, LR = earliest). A **balanced-block** design (12
present-sets × a 4×4 Latin square) makes the correct line's physical slot **and** the correct
nonce identity both uniform, so it is proven at build that **every** position strategy **and**
**every** one of the 8! nonce-preference orderings scores **exactly 1/K = 0.25** — only reading
the stamp value as recency clears 0.80. 48 records/model × 2 models = **96 finding-bearing
calls**. `anchor: internal-contrast-only`.

## Files

| file | role |
|---|---|
| `common.py` | panel (claude+gemini); stamped-record rendering; forced parse + never-parse-`length`; cost ledger + $0.50 hard stop; frozen constants. |
| `build_trials.py` | (no API) frozen 2-query × K-position-balanced geometry → `stimuli.json`; asserts position balance + a 1/K position-follower baseline; prints sha256 for PREREG. |
| `probe.py` | `liveness` (2 calls; format gate) → `full` (96 calls → `raw/probe-<model>.jsonl`). Refuses `full` until `PREREG.md` records the frozen sha256. |
| `analyze.py` | (no API) per-model accuracy, Wilson CI, position-follower diagnostic, PASS/FAIL verdict + routing. |
| `fixtures/make_fixtures.py` | (no API) idealized stamp-reader → PASS/PASS; position-followers (last & first) → FAIL/FAIL at exactly 1/K. Never findings. |
| `PREREG-draft.md` | the DRAFT; frozen → `PREREG.md` by the orchestrator only after the independent pre-run critic GO. |

## Execution order (after critic GO)

```
python3 fixtures/make_fixtures.py   # no API — all asserts PASS
python3 build_trials.py             # no API — stimuli.json + sha256
# ORCHESTRATOR: critic fixes; confirm sha256; freeze PREREG-draft.md -> PREREG.md; commit
python3 probe.py liveness           # 2 calls
python3 probe.py full               # 96 calls
python3 analyze.py                  # no API -> verdict
```

## Spend gate

Billed `usage.cost` only; per-phase ledger (`raw/cost-ledger.json`); $0.50 projected-total hard
stop. Pre-flight ≈ $0.015 for the full run.
