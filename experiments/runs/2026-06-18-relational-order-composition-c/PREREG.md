
## Frozen stimuli

- `stimuli.json` sha256 = **`89f078e3621f7fb8bbbfd59dcc87bd3e628253f7904c739c76f19e9576374cfc`**
- Built by `build_trials.py` (no API), seed `SEED0 = 20260618`. 108 records/model (72 COMP + 36
  DIRECT), 2 models → **216 finding-bearing calls**.

## Hypothesis & question

Does a coined token's recovered referent depend on the **order** in which two **non-commuting**
operations (STEP, FLIP on a 6-track) were applied across stamped rounds? Fills
[`claim/relational-order-sensitive-reassignment`](../../../wiki/findings/claims/relational-order-sensitive-reassignment.md)
scope limit 2 and the rung-(ii) probe's scope note 3 (order-sensitive composition, untested).
Implements **Option C** of
[`decisions/resolved/relational-rung-iii-path-dependence`](../../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
under its pre-run adjudication gate. **Internal-contrast-only; no human comparison.**

## The binding adjudication (decided BEFORE the run, biased AGAINST the rich reading)

An operation-order gap here is **THIN** (the stamped operation list is in the record;
single-reader-recoverable). A RESPECTS-ORDER positive is a thin **"respects operation order"**
finding — **NOT** rung (iii) / constitution. The rich-side rung (iii) is documented **structurally
closed** for text-only stimuli (a transcript IS a final content+stamps record). Both verdicts thin.

## Design (frozen)

K=6 figures on a stated track; DAX starts on a stated figure; two stamped moves from {STEP:
`p→(p+1)%6`, FLIP: `p→5−p`} (non-commuting). Move-lines displayed in stamp order in half the
records, reversed in half. All 6 shapes present every record (answer space).

- **COMP (headline):** "Which figure does DAX sit on now?" — order not stated. Score `target_rate =
  P(pick == stamp-order end figure)`. Diagnostics: `swapped` (reversed-order), `start`, `step-only`,
  `flip-only`.
- **DIRECT (gate):** order stated explicitly ("first … then …"). Score `direct_acc`.

## Pre-registered thresholds (frozen)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.

## Verdict map (frozen, per model)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution. A null
sharpens the order-insensitive reading; a positive climbs the thin side (order-sensitive
composition). Rich-side rung (iii) is documented closed regardless.

## Shortcut-proofing (certified pre-run)

`build_trials.assert_balance`: target figure uniform (identity picker = 1/K); target track position
balanced (position picker ≤ 1/K); print-order & both canonical-order readers = exactly 0.50; start /
single-move / reversed-order readers = 0; frequency flat. `fixtures/make_fixtures.py`: only genuine
stamp-order composition yields RESPECTS-ORDER; every other reader → ORDER-BLIND-OR-WEAKER (if
on-demand passes) or UNINTERPRETABLE. **ALL FIXTURE ASSERTS PASS.**

## Spend (frozen)

Pre-flight ≈ $0.17 billed (216 calls; relational arms billed ≈$0.10–0.13 for 160 like calls).
`HARD_STOP_USD = 0.55` on projected total. Record actual `usage.cost` after.

## Anti-cheat

The verdict map is symmetric and pre-registered: a null sharpens the order-insensitive reading, a
positive climbs one thin rung — neither is "the win," and **neither reaches rung (iii)** (adjudicated
thin before the run). The rich-side closure is promotable independent of the verdict. No threshold
may be retuned after seeing data. `anchor: internal-contrast-only`.
