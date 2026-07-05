---
type: result
id: relational-integration-depth
title: Integration survives burial depth 2 — both models retain a compatible earliest turn buried under two later turns; the rung-(ii) "more turns" caveat is bounded in the claim's favour (still thin)
meaning-senses:
  - relational
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-17
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/relational-integration-rung-ii
  - rel: supports
    target: result/relational-integration-rung-ii
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: supports
    target: essay/update-is-not-constitution
  - rel: refines
    target: concept/relational-meaning
---

# Result: integration survives burial depth 2 (the earliest of three compatible turns is not shed under load)

> **Status: proposed (2026-06-17).** A harder-load follow-up to
> [`result/relational-integration-rung-ii`](relational-integration-rung-ii.md), attacking that
> result's own honesty-box caveat. Rung (ii) showed both models compose **two** compatible stamped
> turns at ceiling, but it was **saturated**, and named the untested weak point verbatim — "it does
> not rule out overwrite behaviour under harder load (**more turns**…)". This probe tests the "more
> turns" horn: with **three** compatible turns and the earliest buried under **two** later ones,
> does the buried earliest turn still survive? **It does: both models recover the unique
> all-three-match figure at ceiling, and a "drop-the-oldest, keep-recent-two" reader (which would
> score 0.50) is taken 0.000 of the time.** Integration is robust to burial depth 2 — but the result
> is again **saturated at ceiling** and remains **thin / single-reader-recoverable**; it does not
> approach constitution. `anchor: internal-contrast-only`.

## The question (precise)

[`result/relational-integration-rung-ii`](relational-integration-rung-ii.md) established rung (ii)
*in its survival sense* (the earlier turn survives when compatible with the latest), but its honesty
box flags exactly what a ceiling over **two** turns cannot rule out:

> it does not rule out overwrite behaviour under harder load (more turns, larger grids, or
> refinements that *partially conflict* rather than cleanly compose) (verbatim,
> [`result/relational-integration-rung-ii`](relational-integration-rung-ii.md), honesty box)

This probe attacks the **"more turns"** horn — the most tractable harder-load axis — by testing
whether integration survives **greater burial depth**. Rung (ii) (depth 1) put exactly one turn
between the buried turn and the query, so *any* reader that dropped a turn fell to the 0.50 floor and
the only contrast was integrate-vs-not. Here the earliest turn is buried under **two** later
compatible turns, which makes a graded, behaviourally-natural **recency-bounded** alternative
available and *distinct* from the target: a reader that keeps the latest two turns and **sheds the
oldest** scores exactly 0.50. The question: with the earliest turn buried two-deep, do the models
still retain it, or does an overwrite/recency-decay behaviour reappear under load?

## Instrument (frozen; pre-run-critic-gated)

Run dir: [`experiments/runs/2026-06-17-relational-integration-depth/`](../../../experiments/runs/2026-06-17-relational-integration-depth/).
Design: [`relational-integration-depth`](../../../experiments/designs/relational-integration-depth.md).

- **Three-constraint refinement, depth 2.** A coined term **DAX** is pinned across **three stamped
  rounds** about a **2×2×2 figure grid** (2 shapes × 2 patterns × 2 colors → 8 present figures,
  e.g. *"a red striped triangle"*): the **earliest** round (lowest stamp) gives a **shape**, the
  **middle** round a **pattern**, the **latest** round a **color**. Each single constraint matches
  **4** of 8 figures; exactly **one** figure matches all three (the integration **target**). The
  three constraints are mutually *compatible*.
- **The load-bearing alternative.** A **RECENT-TWO** reader (keep the latest two turns = pattern +
  color, **drop** the buried earliest shape) narrows to the two figures sharing the target's pattern
  and color — target plus the figure differing only in shape — → 2 candidates → **0.50**. To
  *exceed* 0.50 the model must retain **all three** turns, including the earliest buried under two
  later ones.
- **Two arms.** **INTEG** (headline, 48/model): *"Which of your figures does DAX refer to?"* — no
  instruction to combine. **DIRECT** (on-demand gate, 32/model): explicitly restates all three
  constraints. `direct_acc < 0.80` ⇒ INTEG UNINTERPRETABLE.
- **Shortcut-proof by construction.** Balanced-block roster (K=8; within each 2×2×2 block the target
  cycles through all 8 figures and all 8 grid slots once under a Latin square). Proven at build,
  separately per arm: grid-position follower = **0.125** exactly; figure-identity preference ≤
  0.125 (all constant-figure pickers + 20 000 random orderings); every **single-attribute** reader ≤
  **0.25** under four tie-breaks; every **two-attribute (drop-one-turn)** reader — including
  RECENT-TWO — = exactly **0.50** under four tie-breaks; full integrator = 1.000; frequency flat;
  earliest(shape) < middle(pattern) < latest(color) stamps. **So only conjoining all three turns can
  clear the 0.50 bar.** Six idealized-reader fixtures certify the verdict map.
- **Independent pre-run critic GO** (fresh agent): reproduced the build and frozen sha256
  (`7f0197fb…`, deterministic), re-derived every shortcut bound from scratch (position 0.125,
  single-attr ≤ 0.25, every drop-one-turn reader exactly 0.50 incl. RECENT-TWO, full integrator
  1.000; the integration criterion's false-positive rate against a true-0.50 reader ≈ **3%**, ≥ 31/48
  needed to clear), confirmed the verdict map is symmetric, and ruled the design a **fresh frozen
  design under the already-ratified `internal-contrast-only` posture — no new decision owed.**
- Forced single-label elicitation; strict parse; `finish_reason == "length"` never parsed; one stern
  retry then NA; `HARD_STOP_USD = 0.50`.

## The headline (verified — numbers not altered)

Both separately-trained models recover the all-three-match figure in **every** INTEG trial; the
buried earliest turn is shed **zero** times:

| model | INTEG target (integration) rate | Wilson 95% | RECENT-TWO (dropped earliest) | twin-pattern | twin-color | pick==last/first line | DIRECT on-demand acc | NA | verdict |
|---|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.000 | 0.000 | 0.125 / 0.125 | **1.000** (32/32) | 0 | **INTEGRATION-UNDER-LOAD** |
| gemini-3.5-flash | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.000 | 0.000 | 0.125 / 0.125 | **1.000** (32/32) | 0 | **INTEGRATION-UNDER-LOAD** |

- **INTEG target rate = 1.000** for both, Wilson lower bound 0.926 — far above the **0.50** ceiling
  every drop-one-turn reader is pinned to. Beating 0.50 requires retaining all three turns, so the
  earliest turn (buried under two later compatible turns) demonstrably **survived**.
- **RECENT-TWO (drop-the-oldest) rate = 0.000.** Neither model ever shed the buried earliest turn
  and kept only the latest two — the natural recency-decay reading was taken **zero** times.
- **All one-attribute-flipped twin rates = 0.000; grid-position-following at exactly chance** (0.125
  / 0.125) — the answer is the three-way conjunction, not a single/double attribute and not a
  position artifact.
- **DIRECT on-demand gate = 1.000** both models — conjoining three constraints is within capability
  in this instrument, so the INTEG result is interpretable.
- **Clean record:** 160/160 strict parses, 0 NA, 0 retried, 0 length-truncation.

**Discipline.** Independent pre-run critic GO (re-derived shortcut bounds; ruled no new decision
owed). Independent **post-run verifier** reproduced every number from raw via its own route
(re-derived each all-three-match target directly from the rendered grid + the three history
constraints, recomputed the RECENT-TWO pick, audited parses/cost, confirmed the frozen sha256) —
**REPRODUCED**.

## What this shows — and what it does NOT (binding scope)

**Shows (within-model, internal-contrast-only):** rung-(ii) integration is **robust to burial depth
2**. When the earliest of three compatible stamped turns is buried under two later turns, both models
still retain it — the recency-bounded "shed the oldest, keep the recent two" behaviour, which was
behaviourally available (scoring 0.50) and would have been the signature of overwrite reappearing
under load, was taken **zero** times. This **bounds [`result/relational-integration-rung-ii`](relational-integration-rung-ii.md)'s
"more turns" caveat in the claim's favour**: the integration is not a depth-1 artifact. It
strengthens, rather than triggers a revision of,
[`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)'s
**supersede-on-conflict, compose-on-compatibility** characterization — the compose-on-compatibility
half now holds across one more turn of depth.

It does **NOT** show:

- **Not unbounded depth, and the ceiling is saturated.** 48/48 censors the magnitude at the ceiling:
  this establishes that integration survives **one** further turn of burial depth (2 vs the
  rung-(ii) 1), **not** that it survives arbitrary depth, larger grids, or many turns. The "more
  turns" caveat is **bounded one step further**, not eliminated. Deeper burial (≥4 turns), larger
  grids, and **partially-conflicting** refinements (the other two horns of the rung-(ii) caveat)
  remain untested.
- **Not stronger evidence of *spontaneous* composition than rung (ii).** DIRECT is again at ceiling
  (1.000), so conjoining three compatible constraints is *easy* in this instrument; by the same
  argument rung (ii) made about itself, a ceiling on the spontaneous (no-instruction) arm is
  **weaker** evidence of genuinely spontaneous composition than a mid-range result would be. What
  this result adds over rung (ii) is **robustness to depth**, not a strengthening of the spontaneity
  reading. The informativeness rests entirely on the pre-registered gap between INTEG (1.000) and the
  0.50 RECENT-TWO ceiling: a clean "shed the oldest" behaviour was genuinely available and was not
  taken.
- **Not order-SENSITIVE integration.** The three constraints are *compatible* and symmetric, so a
  **commutative** three-way conjunction ("DAX is red AND striped AND a triangle") passes this test
  exactly as a genuinely order-sensitive composition would. The headline measures whether the buried
  earliest turn **survives** under depth, not whether the composition is non-commutative.
  "Order-sensitive integration" in the strong sense stays a further, untested refinement.
- **Not rich constitution.** Per [`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md),
  this is still on the **thin / single-reader-recoverable** side of the thin/rich criterion: a single
  reader handed the record can intersect the three stated constraints. It is **not** path-dependence
  (rung iii — see the ratified decision [`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md))
  and **not** between-agent constitution (rung iv). This result does not move the claim toward those
  rungs.
- **Not a human comparison** (`anchor: internal-contrast-only`). No in-repo resource grounds human
  integration-under-load at this grain; none is owed because no human contrast is asserted.

## Honesty box

- **Ceiling effect, two independent models, n=48/model INTEG.** Wilson LB 0.926, RECENT-TWO rate
  exactly 0.000, position at chance, DIRECT at ceiling, 0 NA. As clean as a behavioural contrast
  gets — but **saturated**: 48/48 establishes *direction* (integration survives depth 2), not a
  finer estimate of the depth at which it would fail.
- **One operationalization, one step deeper.** Shape-always-earliest / pattern-middle /
  color-latest, three-round histories, trivially discriminable figures. This adds **one** depth step
  to rung (ii); it does not vary which attribute is buried, go beyond three turns, enlarge the grid,
  or test partial conflict. Generality on those axes is untested.
- **Strengthens, does not trigger.** Like the implicit-reassignment control before it, this is a
  *strengthening* of an existing positive (the rung-(ii) "more turns" caveat is bounded one step),
  **not** a new rung and **not** a trigger firing. The rich upper ladder (rungs iii–iv) is unbuilt;
  the rung-(iii) operationalization was surfaced and has since been resolved (see l.160 of this
  page — the ratified decision
  [`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md)).
  *[Pointer, s183: the rung-iii Option-C line then ran —
  [`result/relational-order-composition-c`](relational-order-composition-c.md) (2026-06-18).]*
- **Spend.** 160 finding-bearing calls + 2 liveness = **$0.12892 billed** (`usage.cost`-summed,
  0 missing), inside the $0.50 per-run hard stop and the $5.00/day cap (day total ≈ $0.35).
