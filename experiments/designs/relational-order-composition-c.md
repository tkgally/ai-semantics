# Design — relational ORDER-SENSITIVE COMPOSITION probe (Option C: non-commuting operation semantics)

**Status:** frozen design (2026-06-18). Internal-contrast-only (the ratified relational posture; no
human comparison). Implements **Option C** of the ratified decision
[`decisions/resolved/relational-rung-iii-path-dependence`](../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
under its **binding pre-run adjudication gate**. Run dir:
`experiments/runs/2026-06-18-relational-order-composition-c/`.

## The question

The relational ladder ([`essay/update-is-not-constitution`](../../wiki/findings/essays/update-is-not-constitution.md))
has firm, replicated rungs, **all thin**: rung (i) order-sensitive OVERWRITE
([`claim/relational-order-sensitive-reassignment`](../../wiki/findings/claims/relational-order-sensitive-reassignment.md))
and rung (ii) non-overwrite INTEGRATION
([`result/relational-integration-rung-ii`](../../wiki/findings/results/relational-integration-rung-ii.md),
robust to depth 2). The rung-(ii) probe's own **scope note 3** names the gap this probe fills
(verbatim): *"Tests non-overwrite, not order-sensitive composition … it does NOT test whether the
composition is itself order-sensitive (a commutative conjunction would pass equally)."* The claim's
**scope limit 2** calls order-sensitive composition *"a further, untested refinement."* This probe
tests exactly that — **does the model's recovery of a coined token's referent depend on the ORDER in
which two non-commuting operations were applied?**

## What this is and is NOT (the binding adjudication)

The decision ratified Option C as the only design making arrival-order load-bearing *by
construction* (two orders of the same move-set reach genuinely different end states), under a
**pre-run adjudication gate biased AGAINST the rich reading**. The adjudication, made here **before
any run**:

> An operation-order gap in this design is **THIN**. The stamped operation list is *in the record*;
> a single reader applies it in stamp order and reads off the answer — single-reader-recoverable.
> A RESPECTS-ORDER positive is therefore a thin **"respects operation order" / order-sensitive
> COMPOSITION** finding. It is **NOT** promoted to rung (iii) / constitution. The decision's default
> *"does not pre-authorize calling an Option-C gap rich,"* and this design does not.

In parallel, this design **documents the rich-side closure**: because a transcript *is* a final
content+stamps record (the [`essay/transcript-ceiling`](../../wiki/findings/essays/transcript-ceiling.md)
thesis), **no** text-only stimulus can carry an arrival-order surplus *outside* the final
content+stamps. So the rich-side **rung (iii) is structurally closed for text-only stimuli** — a
promotable §A5 outcome, not a failure. This probe is the strongest order-load-bearing text design,
and even a clean gap here is thin: that *is* the closure made concrete.

## Design (non-commuting operation semantics)

K=6 distinct figures (shapes) lie along a **track** in a stated order (position 1..6). A coined
token **DAX** starts on a stated figure. Across two stamped rounds it undergoes two relative moves
from a **non-commuting pair** (the dihedral generators of a 6-ring):

- **STEP** — DAX moves one position toward the back of the track (wraps back→front). `p → (p+1)%6`.
- **FLIP** — DAX moves to its mirror position (1↔6, 2↔5, 3↔4). `p → 5−p`.

STEP and FLIP do **not** commute, so applying them in **stamp order** (lower round first) lands DAX
on a **different** figure than applying them reversed. The two move-lines are **displayed in round
order in half the records and reversed in the other half** (print order decoupled from stamp order).
All 6 shapes are present in every record (answer space = the 6 shapes).

Two query arms (each its own balanced roster):

- **COMP (headline, spontaneous)** — the two stamped move-lines are shown (possibly out of round
  order); the query asks only which figure DAX sits on now, **without** saying which move came
  first. A reader who applies the moves in **print order**, or in a **fixed canonical order**, is
  correct only when that order happens to equal stamp order = **exactly half** the records = **0.50**
  (proven at build). Beating 0.50 (Wilson-95 **lower bound > 0.50**) requires ordering the two moves
  **by their stamps** = order-sensitive **COMPOSITION**.
- **DIRECT (on-demand manipulation check)** — same stimuli; the query states the order explicitly
  (*"first … then …"*) and asks for the figure. Confirms the model **can** compose the two moves in
  this instrument. Gate: `direct_acc ≥ 0.80`. If it fails, COMP is **UNINTERPRETABLE**.

## Frozen parameters

- Panel: `claude-sonnet-4.6` + `gemini-3.5-flash` (the A-eligible relational pair). gemini
  `reasoning: {effort: minimal}`.
- `K = 6`; `N_BLOCKS_COMP = 12` → 72 COMP records/model; `N_BLOCKS_DIRECT = 6` → 36 DIRECT
  records/model. **108 records/model × 2 models = 216 finding-bearing calls.**
- `PRINT_CEILING = 0.50` (print-order / canonical-order bar); `DIRECT_FLOOR = 0.80`; composition bar
  = COMP target-rate Wilson-95 LB > 0.50.
- Forced single-figure-name format; `MAX_TOKENS = 512` (length-truncated replies never parsed); one
  stern retry then NA. `HARD_STOP_USD = 0.55` on projected billed cost. Pre-flight ≈ $0.17.
- `stimuli.json` sha256 frozen in `PREREG.md` before any finding-bearing call.

## Shortcut-proofing (certified at build + on idealized-reader fixtures)

`build_trials.assert_balance` proves, per subset: target figure **uniform over the 6 shapes**
(every figure-identity picker = 1/K); target **track position balanced** (every fixed-position
picker ≤ 1/K; COMP exactly 1/K); **print-order and both canonical fixed-order readers = exactly
0.50** (print matched to stamp order in half the records; true order balanced 6 SF / 6 FS); the
**start / single-move / reversed-order readers = 0** on the target (excluded by valid-config
construction); frequency flat. `fixtures/make_fixtures.py` certifies the verdict map on six
idealized readers: `stamp_order` → RESPECTS-ORDER (target 1.000); `print_order` / `canonical_sf` →
ORDER-BLIND-OR-WEAKER (target 0.500); `figpref` / `trackpos` → UNINTERPRETABLE (DIRECT fails, target
1/K); `direct_fail` → UNINTERPRETABLE (on-demand gate guard). So **no figure / track-position /
print-order / canonical-order / start / single-move / reversed-order shortcut can manufacture a
RESPECTS-ORDER verdict** — only ordering the two moves by their stamps can.

## Verdict map (frozen, per model)

- **UNINTERPRETABLE** — `direct_acc < 0.80` (cannot compose the two moves on demand).
- **RESPECTS-ORDER** — DIRECT gate passed **and** COMP target-rate Wilson-95 LB **> 0.50** ⇒ the
  model orders the two non-commuting moves by their stamps: **order-sensitive composition** (thin).
- **ORDER-BLIND-OR-WEAKER** — DIRECT gate passed **and** COMP target-rate Wilson-95 LB **≤ 0.50** ⇒
  the model reads the moves in print/canonical order, not stamp order (thin; sharpens that
  composition is order-*insensitive* here).

## Scope & honesty (binding)

1. **Internal-contrast-only.** A within-model contrast over balanced / order-permuted content; **no
   human claim.** (Brennan & Clark report an order-*insensitive* human statistic; none is owed.)
2. **Adjudicated THIN, not rung (iii).** Either verdict is single-reader-recoverable. A RESPECTS-
   ORDER positive is reported as "respects operation order," never promoted to constitution. The
   rich-side rung (iii) is documented **structurally closed** for text-only stimuli (the parallel
   headline).
3. **Tests order-sensitive composition, not "between-agent" surplus.** The gap, if any, is function
   composition the record fully encodes. This is the acknowledged thin nature of Option C.
4. **One operationalization.** STEP/FLIP on a 6-track, two moves, two rounds. Generality (other
   operation pairs, >2 moves, image referents, cross-family dyads) untested.

No new `wiki/decisions/open/` entry is owed: this is a frozen design under the **already-ratified**
Option-C decision and the **already-ratified** `internal-contrast-only` relational posture, with a
pre-registered symmetric verdict map and the adjudication the decision required — to be confirmed by
the independent pre-run critic before any spend.
