# Design — relational INTEGRATION-UNDER-LOAD probe (burial depth 2)

**Status:** frozen design (2026-06-17). Internal-contrast-only (the ratified relational posture; no
human comparison). The harder-load follow-up to
[`result/relational-integration-rung-ii`](../../wiki/findings/results/relational-integration-rung-ii.md),
attacking that result's own honesty-box caveat. Run dir:
`experiments/runs/2026-06-17-relational-integration-depth/`.

## The question

[`result/relational-integration-rung-ii`](../../wiki/findings/results/relational-integration-rung-ii.md)
showed both panel models INTEGRATE a compatible earlier turn at ceiling (INTEG target 1.000,
overwrite 0.000) over **two** stamped rounds — the earlier, non-terminal turn *survives*. But that
result is **saturated at ceiling**, and its honesty box names the untested weak point verbatim:

> it does not rule out overwrite behaviour under harder load (**more turns**, larger grids, or
> refinements that *partially conflict* rather than cleanly compose)

This probe attacks the **"more turns"** horn — the most tractable harder-load axis — by testing
whether integration survives **greater burial depth**. The rung-(ii) design put one turn between the
buried turn and the query; here the earliest turn is buried under **two** later compatible turns.

## Design (three-constraint refinement, depth 2)

A coined term **DAX** is pinned across **three stamped rounds** about a **2×2×2 figure grid**
(2 shapes × 2 patterns × 2 colors → 8 present figures, "a {color} {pattern} {shape}"):

- **Earliest** round (lowest stamp): *"DAX was a {shape}"* — the SHAPE constraint, the
  most-buried non-terminal turn. Matches 4 of 8.
- **Middle** round: *"DAX was {pattern}"* — the PATTERN constraint. Matches 4 of 8.
- **Latest** round (highest stamp): *"DAX was {color}"* — the terminal turn. Matches 4 of 8.
- Exactly **one** present figure satisfies all three = the integration **target**. All three
  constraints are mutually *compatible*.

The load-bearing alternative the depth-2 structure newly makes available:

- **RECENT-TWO reader** (keep the latest two turns = pattern + color, **drop** the buried earliest
  shape): narrows to {target, twin_shape} (the two figures sharing the target's pattern AND color,
  differing only in shape) → 2 candidates → **0.50**. A clean "shed the oldest" recency reader
  scores exactly 0.50 — to **exceed** 0.50 the model must retain **all three** turns, including the
  earliest buried under two later ones.

Two query arms (each its own balanced-block roster):

- **INTEG (headline, spontaneous)** — *"Which of your figures does DAX refer to?"* No instruction
  to combine. Every single-attribute reader caps at **0.25**; every two-attribute (drop-one-turn)
  reader at **0.50**. Beating 0.50 (Wilson-95 LB > 0.50) ⇒ the buried earliest turn **survived
  under depth-2 load** = INTEGRATION-UNDER-LOAD.
- **DIRECT (on-demand gate)** — same stimuli; the query explicitly restates all three constraints
  and asks for the figure. Confirms the model **can** conjoin three. Gate: `direct_acc ≥ 0.80`; if
  it fails, INTEG is **UNINTERPRETABLE**.

## Frozen parameters

- Panel: `claude-sonnet-4.6` + `gemini-3.5-flash`; gemini `reasoning:{effort:minimal}`.
- `K=8`; `N_BLOCKS_INTEG=6` → 48 INTEG/model; `N_BLOCKS_DIRECT=4` → 32 DIRECT/model. **160
  finding-bearing calls.**
- `SINGLE_ATTR_CEILING=0.25`; `TWO_ATTR_CEILING=0.50` (the integration bar); `DIRECT_FLOOR=0.80`;
  integration bar = INTEG target Wilson-95 LB > 0.50.
- Forced single-label; `MAX_TOKENS=512`; one stern retry then NA. `HARD_STOP_USD=0.50`. Pre-flight
  ≈ $0.15. `stimuli.json` sha256 frozen in `PREREG.md` before any finding-bearing call.

## Shortcut-proofing (certified at build + on idealized-reader fixtures)

`build_trials.assert_balance` proves, per subset: grid-position follower = 0.125 exactly;
figure-identity preference ≤ 0.125 (all constant-figure pickers + 20 000 random orderings); every
single-attribute reader ≤ 0.25 under four tie-breaks; every two-attribute (drop-one-turn) reader =
exactly 0.50 under four tie-breaks; full integrator = 1.000; frequency flat; earliest(shape) <
middle(pattern) < latest(color) stamps. `fixtures/make_fixtures.py` certifies the verdict map on
six idealized readers (`integrator` → INTEGRATION-UNDER-LOAD; `recent_two` / `overwrite` →
PARTIAL-OR-OVERWRITE; `gridpos` / `figpref` / `direct_fail` → UNINTERPRETABLE). **So no position /
identity / single- or two-attribute / frequency shortcut can manufacture an INTEGRATION-UNDER-LOAD
verdict.**

## Verdict map (frozen, per model)

- **UNINTERPRETABLE** — `direct_acc < 0.80`.
- **INTEGRATION-UNDER-LOAD** — DIRECT gate passed AND INTEG target Wilson-95 LB > 0.50 ⇒ the buried
  earliest turn survives depth-2 load; the rung-(ii) "more turns" caveat is bounded in the claim's
  favour.
- **PARTIAL-OR-OVERWRITE** — DIRECT gate passed AND INTEG target Wilson-95 LB ≤ 0.50 ⇒ a turn is
  shed under load; bounds the integration claim to depth 1.

## Scope & honesty (binding)

1. **Internal-contrast-only.** A within-model contrast over balanced content; **no human claim.**
2. **Tests "more turns" / burial depth, not order-sensitive composition.** Like rung (ii), the three
   constraints are *symmetric* (compatible), so a positive shows the buried earliest turn **survives
   under depth**, not that the composition is order-sensitive. And DIRECT being at ceiling would mean
   conjoining-three is within capability, so a spontaneous ceiling is still *weaker* evidence of
   spontaneous composition than a mid-range result — but the depth-2 design makes a *graded* recency
   reader (recent-two = 0.50) behaviourally available where the depth-1 design could not.
3. **Still thin.** Both outcomes sit on the single-reader-recoverable (thin) side of the
   thin/rich criterion; neither approaches constitution (rungs iii–iv).
4. **One operationalization.** Shape-always-earliest, pattern-middle, color-latest; three-round
   histories; trivially discriminable attribute values. Generality (which attribute is buried;
   >3 turns; partially-conflicting refinements; image referents) untested.

No new `wiki/decisions/open/` entry is owed: a fresh frozen design under the **already-ratified**
`internal-contrast-only` relational posture, with a pre-registered symmetric verdict map (a null
bounds integration to depth 1; a positive shows it robust to depth 2) — to be confirmed by the
independent pre-run critic.
