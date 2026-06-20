# PREREG — CROSS-FAMILY (heterogeneous-operation) order-sensitive composition (Option-C generality axis)

**Run:** `2026-06-20-relational-order-composition-cross-family`
**Frozen stimuli:** `stimuli.json`
**rstrip-sha256 = `f33785cdf43bd3ffefc5bd1c745b01326731d4cad64acc5855effb1ecc7be0ca`**
(the `probe.py full` gate refuses to run unless this exact sha is recorded here)

> **Status at freeze: design complete, balance + fixtures certified, awaiting independent pre-run
> critic GO.** No finding-bearing call may run before the critic returns GO and this PREREG (not a
> draft) records the sha above.

## The question (precise)

Every prior Option-C run composed operations of the **same family**: position permutations rendered
as opaque figure→figure tables (STEP/FLIP = D4, CYCLE/SWAP = A4, three generic permutations of S6).
The working-surface run found a **witness** and the alt-pair / K=6 / three-move runs replicated a
composition **capacity** across the operation-pair, grid-size, and depth axes — all panel-concordant
RESPECTS-ORDER. But to the model those were all the *same task*: compose two (or three) opaque
permutations of one ground set. [`claim/relational-order-sensitive-reassignment`] scope limit 2 names
the still-untested generality axis verbatim — *"generality (image referents, cross-family dyads) is
untested"* — and [`result/relational-order-composition-three-move`] + [`essay/witness-seeking-economics`]
name a **different kind** of composition (not one more move of the same kind) as the higher-information
next step.

**This probe varies the KIND of the two operations: it composes two TRANSPARENTLY HETEROGENEOUS,
non-commuting operations — one SPATIAL (a swap), one ATTRIBUTE (a recolor) — and asks: does the
working-surface composition capacity extend to binding two updates of *different kinds* in stamp
order?** This is the relational axis's core (composing heterogeneous updates) and has a higher prior
of strain than another homogeneous-permutation instrument, because the two operations act on
different dimensions of the same state.

## The two heterogeneous operations (the single manipulated variable: operation KIND)

A coined token **DAX** lives on a row of `K=4` spots; each spot holds a colored token; DAX has a
color too. Two kinds of move, both stated transparently to the model (no opaque tables):

- **SWAP** (a SPATIAL move): names two spots; the tokens on them exchange places (color travels with
  the token). Acts on POSITION.
- **RECOLOR** (an ATTRIBUTE move): names one spot and a color; the token on that spot is repainted.
  Acts on COLOR.

DAX always starts on one of the two SWAP spots, so SWAP moves DAX; RECOLOR targets one of the two
SWAP spots. They **do not commute** on DAX's final color: applying SWAP first moves DAX into/out of
the recolor spot before the repaint lands, so whether DAX catches the new color depends on the order.

Each record stamps the two operations with two distinct rounds (higher round = agreed more recently);
the true composition applies them in **stamp order** (lowest round first). The two stamped op-lines
are shown in a **display order decoupled from stamp order** (each block uses both display orders), so
"apply the moves in printed order" is not "apply them in stamp order."

- **COMP (headline, spontaneous):** the two stamped op-lines are shown (display decoupled) and the
  query asks only what color DAX is now — it does **not** say in which order to apply them. A working
  surface does not make COMP non-spontaneous: the query still does not state the order, so the model
  must still **decide** to order the two ops by their stamps.
- **DIRECT (on-demand gate):** same trials; the query states the order explicitly ("first … and then
  …") and asks the color. Confirms the model CAN compose the heterogeneous pair in THIS instrument.
  Gate `direct_acc ≥ 0.80`. If it fails, COMP is UNINTERPRETABLE.

## Why the 0.50 ceiling (same interpretive force as every prior Option-C run)

The four geometry **cells** = recolor_target {`a` = DAX's start spot, `b` = the swap partner} ×
stamp_first {SWAP, RECOLOR}. Simulating DAX's (spot, color) through the two ops in stamp order (with
DAX start color `C0`, recolor color `Cr`, always `C0 ≠ Cr`):

| cell | trace | DAX final color |
|---|---|---|
| SWAP-first, recolor@a | DAX a→b, then recolor a hits the OTHER token | **C0** |
| SWAP-first, recolor@b | DAX a→b, then recolor b hits DAX | **Cr** |
| RECOLOR-first, recolor@a | recolor a hits DAX→Cr, then DAX a→b | **Cr** |
| RECOLOR-first, recolor@b | recolor b hits OTHER, then DAX a→b | **C0** |

So the answer is `C0` in cells {SWAP@a, RECOLOR@b} and `Cr` in {SWAP@b, RECOLOR@a}. It is fixed by
**neither the stamp order alone nor the geometry alone — only by both together.** With the four cells
equally frequent the answer is `C0` half the time and `Cr` half the time, so **every non-composing
reader tops out at exactly 0.50** (brute-forced over the actual 72 COMP records in
`build_trials.assert_balance`):

- report-`C0` (= SWAP-only / ignore recolor) → 0.50
- report-`Cr` (= assume the repaint always lands on DAX) → 0.50
- recolor-only (ignore the swap) → 0.50
- apply both in a FIXED order regardless of stamps (either way) → 0.50
- apply both in PRINT/display order → 0.50
- any fixed-spot initial or fixed-order final color, or any const color → ≤ 1/6 < 0.50

Only a reader that applies the two operations in the **per-trial stamp order** clears 0.50
(= 1.0). Beating 0.50 (COMP target-rate Wilson-95 lower bound > 0.50) is therefore **cross-family
order-sensitive composition**. (Unlike the homogeneous-permutation runs where a reversed-order reader
scored 0, here a *fixed*-order reader scores 0.50 — with two heterogeneous ops and a binary {C0, Cr}
answer a fixed order is right half the time, exactly as canonical/print readers scored 0.50 in the
original two-move STEP/FLIP run; the reversed-order reader here scores 0, anti-correlated. The ceiling
and its interpretive force are identical.)

## Design parameters (frozen)

- `K = 4` spots; answer space = **6 colors** (red, blue, green, yellow, purple, orange); const-color
  picker = 1/6.
- COMP: 4 cells × 3 (a,b) geometries = 12 blocks × 6 colors = **72 records/model**.
- DIRECT: 4 cells × 3 geometries = 12 blocks × 3 colors = **36 records/model**.
- Total **108 records/model × 3 models = 324 finding-bearing calls.**
- Position neutralization: DAX's start spot `a` and the swap partner `b` are each **uniform over the
  4 spots** (proven at build); answer color **uniform over the 6 colors** (const = 1/6); cells /
  stamp_first / recolor_target / display order all balanced.
- Working-surface elicitation **held identical** to the prior Option-C working-surface runs: the
  model MAY show step-by-step working and must end `FINAL: <color>`; `MAX_TOKENS = 1024`; gemini
  `reasoning: {effort: minimal}` **held constant**; a `finish_reason == "length"` reply is never
  parsed (NA/retry). Target-blind `FINAL:`-tag parser (keys on reply position, not on the correct
  color).
- Panel: claude = positive control; gemini + gpt = the cross-family targets (all three cleared the
  two-move DIRECT gate once a working surface was opened).
- Pre-flight cost: depth-2 task, shorter CoT than the three-move run ($0.80 for 324 calls); estimate
  **≈ $0.5–0.8**; pre-registered **hard stop $1.50** on projected billed total.

## Frozen verdict map (identical to every prior Option-C run)

- `UNINTERPRETABLE` : `direct_acc < 0.80` (cannot compose the two ops on demand).
- `RESPECTS-ORDER` : DIRECT gate passed AND COMP target-rate Wilson-95 LB > 0.50.
- `ORDER-BLIND-OR-WEAKER` : DIRECT gate passed AND COMP target-rate Wilson-95 LB ≤ 0.50.

## ADJUDICATION (binding, decided BEFORE the run, biased AGAINST the rich reading)

Per [`decisions/resolved/relational-rung-iii-path-dependence`]: an operation-order gap here is
**THIN**. The stamped operation list, the spots, and the colors are **in the record**; a single
reader applies the two ops in stamp order and reads off the color (single-reader-recoverable).
RESPECTS-ORDER is reported as a thin **"respects operation order" / cross-family-composition**
finding — **never** promoted to rung (iii) / constitution. The rich-side rung (iii) program is
documented **structurally closed for text-only stimuli**. `anchor: internal-contrast-only`; **no
human-comparison claim** (a within-model contrast over balanced, order-permuted content).

## No new decision is owed (surfaced for the critic to gate)

The ratified Option-C decision adopted **"non-commuting operation semantics"** *agnostic to which
operations realize them* (it explicitly contemplated "rotate/move" edits) and **did not freeze the
operation kind**. Like the alt-pair (D4→A4), the grid size (K=4→K=6), and the move count (2→3) —
**none of which owed a new decision** — the operation-KIND change (homogeneous permutation pair →
heterogeneous spatial+attribute pair) is the same class of within-frame variation. As a forced
consequence the state carries a color attribute and the answer is a color rather than a figure, but
the stamp-order-=-composition semantics, the working-surface format, the 0.50 ceiling, the symmetric
verdict map, and the THIN adjudication are all unchanged. The design states **no new
`wiki/decisions/open/` entry is owed**; the independent pre-run critic gates this judgement and may
rule otherwise (if so, open a decision and mark the result contingent).

## Certifications run at freeze (no API)

- `python3 build_trials.py` → `assert_balance` PASS: 72 COMP + 36 DIRECT; **composer = 1.000**; every
  non-composing reader in the brute-forced family ≤ 0.50 (worst = `start-color(C0)` at **exactly
  0.5000**); cells / stamp_first / recolor_target / display / DAX-start-spot balanced; answer uniform
  over 6 colors (const = 1/6). Frozen sha printed above.
- `python3 fixtures/make_fixtures.py` → ALL FIXTURE ASSERTS PASS: only a genuine stamp-order composer
  → RESPECTS-ORDER (1.0); report-C0 / report-Cr / fixed-order / print-order → ORDER-BLIND-OR-WEAKER
  at exactly 0.50 (not significant); const-color / direct-fail → UNINTERPRETABLE (the on-demand gate
  guards the null reading).

## Anchor

`internal-contrast-only`, carried forward from the relational line and ratified for the Option-C
program. The contrast is within-model over byte-balanced/order-permuted content; no human comparison
is asserted or owed. Any future framing reaching for a human order-sensitivity comparison incurs a
fresh, currently-undischargeable anchor question.
