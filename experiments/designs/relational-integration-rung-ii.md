# Design — relational rung-(ii) INTEGRATION probe (non-overwrite / refinement)

**Status:** frozen design (2026-06-17). Internal-contrast-only (the ratified relational posture; no
human comparison). Implements the next rung named in
[`essay/update-is-not-constitution`](../../wiki/findings/essays/update-is-not-constitution.md) above
the established bottom rung [`claim/relational-order-sensitive-reassignment`](../../wiki/findings/claims/relational-order-sensitive-reassignment.md).
Run dir: `experiments/runs/2026-06-17-relational-integration-rung-ii/`.

## The question

The relational track has a firm bottom rung: when a coined term is **reassigned** across stamped
rounds (the turns *conflict* — DAX = star, then DAX = seashell), both panel models recover the term
by its **most-recent** binding — a thin **OVERWRITE** rule ("the latest agreement supersedes earlier
ones"). The essay's **rung (ii)** asks whether the update is *only* overwrite, or whether an earlier,
**non-terminal** turn **survives** into the interpretation when it is *compatible* with the latest
(refinement, not replacement):

> Rung (ii) — order-sensitive INTEGRATION / non-overwrite repair … Signature: recovery that is a
> function of **more than the max-stamp binding** — measurably **sensitive to a non-terminal turn
> whose content an overwrite rule would throw away**. Proposed discriminating design: hold the final
> turn fixed and vary an earlier refining turn; an overwrite reader is invariant, an integrating
> reader is not. (verbatim, `essay/update-is-not-constitution`, rung (ii))

This fills [`claim/relational-order-sensitive-reassignment`](../../wiki/findings/claims/relational-order-sensitive-reassignment.md)
**scope limit 2** ("non-overwrite repairs … untested") and tests essay **revision trigger (a)**.

Both rung (i) and rung (ii) are on the **thin / single-reader-recoverable** side of the essay's
thin/rich criterion — **a positive here does not approach constitution.** No human comparison is
made or owed (`internal-contrast-only`).

## Design (two-constraint refinement)

A coined term **DAX** is pinned down across **two stamped rounds** about a **2×2 figure grid**
(2 shapes × 2 patterns → 4 present figures, e.g. `{striped triangle, striped circle, dotted
triangle, dotted circle}`). Figures are described "a {pattern} {shape}"; shapes/patterns are
trivially discriminable (the only hard step is **combining** the two constraints, never telling the
figures apart — near-twins deliberately excluded, as in Option A).

- **Earlier** round (lower stamp): *"we agreed DAX was a {shape}"* — a shape constraint (the
  non-terminal turn an overwrite rule discards). Matches **2** of the 4 figures.
- **Latest** round (higher stamp): *"we agreed DAX was {pattern}"* — the terminal turn. Matches
  **2** of the 4 figures.
- Exactly **one** present figure satisfies **both** = the integration **target** (the {pattern}
  {shape}). The two constraints are *compatible* (a figure can be both) — so the rung-(i) overwrite
  rule and a rung-(ii) composition rule give **different** answers, which is the whole point.

Two query arms (each its own balanced-block roster):

- **INTEG (headline, spontaneous)** — query: *"Which of your figures does DAX refer to?"* No
  instruction to combine. An **overwrite** reader keeps only the latest (pattern) → 2 candidates →
  **0.50**. An **earlier-only** reader keeps the shape → **0.50**. **Any single-attribute reader
  caps at 0.50** (each constraint is 2-way; only the conjunction is unique). Beating 0.50 (Wilson-95
  **lower bound > 0.50**) requires using **both** turns = the earlier, non-terminal turn **survived**
  = INTEGRATION.
- **DIRECT (on-demand manipulation check)** — same stimuli; the query explicitly restates both
  constraints and asks for the figure. Confirms the model **can** conjoin in this instrument.
  Gate: `direct_acc ≥ 0.80`. If it fails, INTEG is **UNINTERPRETABLE**.

## Frozen parameters

- Panel: `claude-sonnet-4.6` + `gemini-3.5-flash` (the A-eligible relational pair; both passed
  Option B). gemini `reasoning: {effort: minimal}`.
- `K = 4`; `N_BLOCKS_INTEG = 12` → 48 INTEG records/model; `N_BLOCKS_DIRECT = 8` → 32/model.
  **80 records/model × 2 models = 160 finding-bearing calls.**
- `OVERWRITE_CEILING = 0.50` (single-attribute bar); `DIRECT_FLOOR = 0.80`; integration bar =
  INTEG target-rate Wilson-95 LB > 0.50.
- Forced single-label format; `MAX_TOKENS = 512` (length-truncated replies never parsed); one stern
  retry then NA. `HARD_STOP_USD = 0.50` on projected billed cost. Pre-flight ≈ $0.11.
- `stimuli.json` sha256 frozen in `PREREG.md` before any finding-bearing call.

## Shortcut-proofing (certified at build + on idealized-reader fixtures)

Balanced-block roster: within each 2×2 block, K=4 records cycle the target through all 4 present
figures once under a Latin square that also cycles the target's grid slot through all 4 slots once.
`build_trials.assert_balance` proves, per subset:

1. every constant-grid-slot follower scores exactly **1/K = 0.25** (target slot uniform);
2. within each block the target is **uniform over the 4 present figures** ⇒ every fixed
   figure-identity preference scores exactly **1/K** (analytic; spot-checked over all 16
   constant-figure pickers + 20 000 random orderings);
3. every concrete single-attribute reader (latest-pattern-only = overwrite; earlier-shape-only),
   under each of four tie-breaks (lower/higher slot, lower/higher pool index), scores **exactly
   0.50** (a placement search balances the slot tie-breaks; pool-index tie-breaks are structurally
   0.50);
4. frequency flat (4 distinct figures once each; 2 distinct rounds; latest round > earlier round).

`fixtures/make_fixtures.py` certifies the verdict map on six idealized readers: `integrator` →
INTEGRATION (target 1.000); `overwrite` / `earlier_only` (on-demand correct, spontaneous
single-attribute) → OVERWRITE-OR-WEAKER (target 0.50); `gridpos` / `figpref` → UNINTERPRETABLE
(DIRECT fails, target = 1/K); `direct_fail` → UNINTERPRETABLE (on-demand gate guard). So **no
position / identity / single-attribute / frequency shortcut can manufacture an INTEGRATION verdict.**

## Verdict map (frozen, per model)

- **UNINTERPRETABLE** — `direct_acc < 0.80` (on-demand conjunction failed here).
- **INTEGRATION** — DIRECT gate passed **and** INTEG target-rate Wilson-95 LB **> 0.50** ⇒ rung (ii)
  occupied: the earlier, non-terminal turn **survives**; agreements **compose**.
- **OVERWRITE-OR-WEAKER** — DIRECT gate passed **and** INTEG target-rate Wilson-95 LB **≤ 0.50** ⇒
  rung (ii) **not** reached; the thin overwrite verdict (rung i only) is **sharpened**.

## Scope & honesty (binding)

1. **Internal-contrast-only.** A within-model contrast over balanced content; **no human claim.**
2. **Compatible constraints by design.** The two turns are *compatible* (composable), unlike the
   reassignment regime where they conflict. A positive shows the models **compose** compatible turns
   (do not blindly overwrite the earlier one); a null shows they overwrite even when composition was
   available. This is exactly the overwrite/integration cut.
3. **Tests non-overwrite, not order-sensitive composition.** The headline measures whether the
   earlier turn *survives*. It does **not** test whether the composition is itself order-sensitive
   (a commutative conjunction would pass equally). "Order-sensitive integration" in the strong sense
   stays a further, untested refinement.
4. **Still thin.** Rung (ii) is on the single-reader-recoverable (thin) side of the essay's
   criterion. Neither outcome approaches constitution (rungs iii–iv).
5. **One operationalization.** Shape+pattern attributes, pattern-always-latest, two-round histories.
   Generality (shape-latest, >2 turns, image referents, cross-family dyads) untested.

No new `wiki/decisions/open/` entry is owed: this is a fresh frozen design under the **already-
ratified** `internal-contrast-only` relational posture, with a pre-registered symmetric verdict map
(a null sharpens the thin reading; a positive climbs one thin rung) — confirmed by the independent
pre-run critic.
