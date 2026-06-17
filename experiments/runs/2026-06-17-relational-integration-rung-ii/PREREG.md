
## Frozen stimuli

- `stimuli.json` sha256 = **`b80772e67497810462ce2fa441766c2afebb44b98216a8b4e5e7cf5d89feeb16`**
- Built by `build_trials.py` (no API), seed `SEED0 = 20260617`. 80 records/model (48 INTEG + 32
  DIRECT), 2 models → **160 finding-bearing calls**.

## Hypothesis & question

Does an earlier, **non-terminal** turn **survive** into a coined term's recovered referent when it
is *compatible* with the latest turn (refinement, not replacement), or does the established
latest-binding-wins **OVERWRITE** rule discard it? Climbs from rung (i) toward rung (ii) of
[`essay/update-is-not-constitution`](../../../wiki/findings/essays/update-is-not-constitution.md);
fills [`claim/relational-order-sensitive-reassignment`](../../../wiki/findings/claims/relational-order-sensitive-reassignment.md)
scope limit 2; tests essay revision trigger (a). **Internal-contrast-only; no human comparison.**

## Design (frozen)

DAX is constrained over two stamped rounds about a 2×2 figure grid: **earlier** (low stamp) gives a
**shape**, **latest** (high stamp) gives a **pattern**; exactly one present figure is the both-match
**target**. Each constraint matches 2 of 4 figures, so any single-attribute reader scores 0.50; only
conjoining both turns is unique.

- **INTEG (headline):** "Which figure does DAX refer to?" — no combine instruction. Score
  `target_rate = P(pick == both-match)`. Diagnostics: `latest_only` (overwrite kept the latest
  pattern only), `earlier_only`, `neither`, grid-position rates.
- **DIRECT (gate):** explicit restatement of both constraints. Score `direct_acc`.

## Pre-registered thresholds (frozen)

- `OVERWRITE_CEILING = 0.50` — every single-attribute reader's INTEG score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand conjunction gate.
- Integration bar = INTEG `target_rate` Wilson-95 **lower bound > 0.50**.

## Verdict map (frozen, per model)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** INTEG target Wilson-LB **> 0.50** | **INTEGRATION** (rung ii: earlier turn survives) |
| DIRECT pass **and** INTEG target Wilson-LB **≤ 0.50** | **OVERWRITE-OR-WEAKER** (rung i only; thin verdict sharpened) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution. A null
(OVERWRITE-OR-WEAKER) *sharpens* the thin overwrite reading (essay trigger (a)); a positive
(INTEGRATION) climbs one thin rung.

## Shortcut-proofing (certified pre-run)

`build_trials.assert_balance`: constant-grid-slot follower = 1/K exactly; figure-identity
preference = 1/K (within-block target uniformity; 16 constant-figure pickers + 20 000 random
orderings); every single-attribute reader (4 tie-breaks × 2 attributes) = 0.50 exactly; frequency
flat. `fixtures/make_fixtures.py`: only a genuine integrator yields INTEGRATION; every
position/identity/single-attribute shortcut → OVERWRITE-OR-WEAKER (if on-demand passes) or
UNINTERPRETABLE. **ALL FIXTURE ASSERTS PASS.**

## Spend (frozen)

Pre-flight ≈ $0.11 billed (160 calls; Option-A billed $0.124 for 160 like calls). `HARD_STOP_USD =
0.50` on projected total. Record actual `usage.cost` after.

## Anti-cheat

The verdict map is symmetric and pre-registered: a null is a first-class result (sharpens thin),
a positive climbs one thin rung — neither is "the win." No threshold may be retuned after seeing
data. `anchor: internal-contrast-only` (ratified for the relational line 2026-06-16).
