# 2026-06-17 — relational rung-(ii) INTEGRATION probe

Tests the next rung of the relational ladder
([`essay/update-is-not-constitution`](../../../wiki/findings/essays/update-is-not-constitution.md)):
does an earlier, **non-terminal** turn **survive** into a coined term's recovered referent when it
is *compatible* with the latest turn (refinement), or does the established **OVERWRITE** rule
(latest-binding-wins, [`claim/relational-order-sensitive-reassignment`](../../../wiki/findings/claims/relational-order-sensitive-reassignment.md))
discard it? Fills that claim's scope limit 2 ("non-overwrite repairs untested") and tests the
essay's revision trigger (a). **Internal-contrast-only; no human comparison.**

DAX is constrained over two stamped rounds about a 2×2 figure grid: earlier (low stamp) = a
**shape**, latest (high stamp) = a **pattern**; exactly one present figure is the both-match
**target**. Each constraint matches 2 of 4 figures → any single-attribute (overwrite or
earlier-only) reader scores 0.50; only conjoining both turns is unique. **INTEG** asks "which figure
is DAX?" (no combine instruction; target Wilson-LB > 0.50 = INTEGRATION). **DIRECT** restates both
constraints (on-demand gate, floor 0.80).

## Files
- `common.py` — shared machinery (rendering, forced parse, cost ledger, hard stop).
- `build_trials.py` — frozen balanced-block stimuli + `assert_balance` shortcut-proof (no API).
- `fixtures/make_fixtures.py` — idealized-reader certification of the verdict map (no API).
- `probe.py liveness | full` — finding-bearing probe (refuses `full` until `PREREG.md` records the
  frozen sha256).
- `analyze.py` — pre-registered verdict (no API) → `raw/analysis.json`.
- `PREREG-draft.md` → `PREREG.md` (renamed only after the independent pre-run critic GO).

## Run order
1. `python3 build_trials.py` — freeze stimuli; prints sha256 (already in PREREG-draft).
2. `cd fixtures && python3 make_fixtures.py` — certify the verdict map.
3. independent pre-run critic → GO → rename `PREREG-draft.md` to `PREREG.md`.
4. `python3 probe.py liveness` then `python3 probe.py full`.
5. `python3 analyze.py`; independent post-run verifier re-derives from `raw/`.

## Verdict map
UNINTERPRETABLE (direct < 0.80) · INTEGRATION (direct pass & INTEG target Wilson-LB > 0.50) ·
OVERWRITE-OR-WEAKER (direct pass & INTEG target Wilson-LB ≤ 0.50). Both INTEGRATION and
OVERWRITE-OR-WEAKER are **thin / single-reader-recoverable** — neither approaches constitution.

`stimuli.json` sha256 `b80772e67497810462ce2fa441766c2afebb44b98216a8b4e5e7cf5d89feeb16`.
