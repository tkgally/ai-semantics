---
type: result
id: relational-order-composition-c-worked-example
title: Worked-example-scaffold witness-seeking re-run of order-sensitive composition — explicitly demonstrating the chaining mechanic did NOT let gemini or gpt clear the on-demand composition gate; the single-move-reader signature persists (gpt's intensifies) even when shown a worked chain and told the order, further localizing the difficulty to chaining execution itself; claude still RESPECTS-ORDER at ceiling
meaning-senses:
  - relational
  - model-internal
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-18
updated: 2026-06-18
links:
  - rel: refines
    target: result/relational-order-composition-c-figure-to-figure
  - rel: refines
    target: result/relational-order-composition-c-easier-k4
  - rel: refines
    target: result/relational-order-composition-c
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: supports
    target: essay/witness-seeking-economics
  - rel: supports
    target: essay/undischargeable-negative
  - rel: supports
    target: essay/capability-split
  - rel: refines
    target: concept/relational-meaning
---

# Result: worked-example-scaffold witness-seeking re-run — no witness; an explicit demonstration of chaining did not suppress the single-move-reader signature

> **Status: proposed (2026-06-18).** The **worked-example-scaffold** witness-seeking re-run of the
> Option-C order-sensitive composition split — the **first easing of the chaining axis** the
> figure-to-figure run ([`result/relational-order-composition-c-figure-to-figure`](relational-order-composition-c-figure-to-figure.md))
> localized. The witness search to date: claude RESPECTS-ORDER; **both** gemini and gpt UNINTERPRETABLE
> across K=6 positional, K=4 positional (state-space easing, off-signature, no witness), and K=4
> figure-maps (read-off easing, on-signature, no witness). The fig run's decisive detail — even **told
> the order** on the DIRECT arm, gpt applied only one of the two moves 65.6% of the time — localized
> the residual difficulty to **chaining itself** (holding two operations and applying *both* in
> sequence), not the per-move read-off. This probe eases **that** axis, exactly as
> [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md) trigger (a) and
> [`essay/capability-split`](../essays/capability-split.md) trigger (b) name it: a **worked-example
> scaffold** demonstrating that both stamped moves must be applied. The single manipulated variable is
> one **worked example** added to the **byte-identical** figure-to-figure trials (same `stimuli.json`
> sha `975e31bc…88ba`); it demonstrates the chaining mechanic (apply move 1 to the start, then move 2
> to the *result*) using a **disjoint** illustrative item/move set and an **explicit** order — so it
> eases chaining **without** teaching stamp-resolution (the COMP spontaneity arm stays uncontaminated).
> `analyze.py`, thresholds, and the verdict map are unchanged.
>
> **Outcome: NO WITNESS — the scaffold did not help.** With both moves' chaining demonstrated outright
> and the order stated, neither model cleared the on-demand gate: **gemini DIRECT 0.625** (< 0.80; CI
> [0.453, 0.771]) and **gpt DIRECT 0.156** (< 0.80; CI [0.069, 0.318]) → **both still UNINTERPRETABLE**.
> **claude still RESPECTS-ORDER at ceiling** (DIRECT 1.000; COMP 64/64) — the scaffolded instrument is a
> valid non-commuting composition. The load-bearing detail: the **single-move-reader signature persists
> and, for gpt, intensifies** — on the DIRECT arm, where the order is stated *and* a worked chain has
> just been shown, **gpt applies only one of the two moves 84.4% of the time** (up from the fig run's
> 65.6%; gemini 21.9%, ~unchanged; claude 0%). So the difficulty is **not** a task-comprehension or
> demonstration gap: shown exactly how to chain two moves and told their order, gpt still does only one.
> Per [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md), this on-signature
> non-witness **further localizes** the difficulty and updates the witness-search suspension note
> (below); per [`essay/undischargeable-negative`](../essays/undischargeable-negative.md) it **does not**
> prove gemini or gpt "cannot compose" — the negative stays **undischargeable, not closed**.
> `anchor: internal-contrast-only`; **no human-comparison claim.**

## The question (precise)

Witness-seeking asks: is the Option-C UNINTERPRETABLE verdict for gemini and gpt driven by an axis of
difficulty an *easier* elicitation removes — a *witness* flipping the negative — or robust to easing?
Three easings had already failed (state-space K=4, off-signature; read-off figure-maps, on-signature;
plus the third-model extension). The figure-to-figure run localized the residual difficulty to
**chaining** — the models read only one of the two stamped moves even when each move is a trivial
lookup. This probe tests the hypothesis that the single-move reading is a **chaining-demonstration
gap**: that the models fail because nothing has shown them they must apply *both* moves in sequence.
The single manipulated variable is the addition of one **worked example** that demonstrates exactly
that, on the byte-identical fig trials.

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

The byte-identical K=4 / figure-to-figure trials (non-commuting STEP/FLIP, dihedral generators of a
4-ring; each move rendered as an explicit figure→figure lookup table, no positions shown), with one
**worked example** inserted between the move tables and the record. The worked example:

- demonstrates the **chaining mechanic** — "apply the FIRST move to the start … then apply the SECOND
  move to that result … BOTH moves are applied, one after the other";
- uses a **disjoint** illustrative set (three colored lights; example moves PUSH/TURN) so **no trial
  figure, trial map, or trial answer leaks**;
- gives the example's order **explicitly** ("first PUSH, then TURN") and contains **no round numbers /
  stamps / recency words** — so it eases the **chaining** axis **without** teaching stamp-resolution
  (the COMP spontaneity question — *which* move is first, read off the round stamps — stays untaught).

- **COMP (headline, spontaneous):** order *not* stated; a reader who applies the moves in print or a
  fixed canonical order scores exactly **0.50**; only ordering by the round stamps (Wilson-95 LB > 0.50)
  clears the bar.
- **DIRECT (on-demand gate):** order stated ("first … then …"). Gate: `direct_acc ≥ 0.80`. If it fails,
  COMP is UNINTERPRETABLE (cannot tell spontaneous order-blindness from inability-to-compose).

**Adjudicated THIN before the run** (carried over unchanged, biased *against* the rich reading): the
stamped move-list and the maps are in the record, so an order gap is single-reader-recoverable —
"respects operation order", **never** rung (iii) / constitution; the rich side is documented
structurally closed for text-only stimuli. An **independent pre-run critic** returned **GO**: it
reproduced the freeze (sha byte-identical to the fig/K=4 trials; `build_trials.py`/`analyze.py`/
fixtures byte-identical), recomputed the geometry from scratch (0 mismatches; STEP/FLIP non-commuting
at all 4 starts; 32/32 DIRECT solvable), traced the rendering from text (0 position leaks across 96
prompts), and — the key new check — verified the worked example **(a)** leaks no trial figure/map/answer
(disjoint items/moves), **(b)** teaches **no** stamp-resolution (order explicit; no digits/round/stamp/
recency words), **(c)** is arithmetically correct and self-consistent, and **(d)** is the *only*
functional prompt change vs. the fig run (single variable). It ruled **no new decision owed** (a
scaffold easing within the ratified Option-C / `internal-contrast-only` frame).

## Results (3 models, 96 records/model, 0 NA, 0 length-truncation, 0 retried; independently reproduced)

An **independent post-run verifier** recomputed every number from raw with its own Wilson
implementation: **REPRODUCED, no mismatches** (0 missing-cost calls; sha confirmed).

| model | DIRECT on-demand acc (gate 0.80) | COMP target rate (bar: Wilson-LB > 0.50) | verdict |
|---|---|---|---|
| **claude-sonnet-4.6** | **1.000** [0.893, 1.000] PASS | **1.000** [0.943, 1.000] → sig | **RESPECTS-ORDER** |
| **gemini-3.5-flash** | **0.625** [0.453, 0.771] FAIL | 0.562 [0.441, 0.677] → not sig | **UNINTERPRETABLE** |
| **gpt-5.4-mini** | **0.156** [0.069, 0.318] FAIL | 0.297 [0.199, 0.418] → not sig | **UNINTERPRETABLE** |

**The failure signature, on the DIRECT (order-stated, *worked-example-shown*) arm** — the load-bearing detail:

| model | DIRECT target | step-only | flip-only | **single-move sum** | swapped | start |
|---|---|---|---|---|---|---|
| claude | 1.000 | 0.000 | 0.000 | **0.000** | 0.000 | 0.000 |
| gemini | 0.625 | 0.094 | 0.125 | **0.219** | 0.031 | 0.031 |
| gpt | 0.156 | 0.312 | 0.531 | **0.844** | 0.125 | 0.125 |

Shown a worked chain *and* told the order, gpt still applies only one of the two moves in **84.4%** of
DIRECT trials (up from 65.6% under figure-maps alone); gemini in ~one-fifth (unchanged). Demonstrating
the chaining mechanic did **not** dissolve — and for gpt did not even reduce — the single-move signature.

**DIRECT on-demand accuracy across the four instruments** (the witness search to date):

| model | K=6 positional | K=4 positional (state-space) | K=4 figure-maps (read-off) | **K=4 figure-maps + worked example (chaining, this run)** |
|---|---|---|---|---|
| gemini | 0.583 | 0.594 | 0.656 | **0.625** (no improvement; still sub-gate) |
| gpt | 0.194 | 0.438 | 0.250 | **0.156** (no improvement; still sub-gate) |
| claude | 0.861 | 0.906 | 1.000 | **1.000** (positive control, ceiling) |

Neither failing model improved under the scaffold. gpt's DIRECT (0.156, CI [0.069, 0.318]) **overlaps**
the fig run's 0.250 (CI [0.133, 0.421]) — read as "**no improvement / no witness**", **not** as "got
worse" (single instrument, overlapping intervals; and a worked example unavoidably also lengthens the
prompt, a confound that forbids reading the numeric drop as the scaffold *hurting*). gemini's 0.625
likewise overlaps its prior 0.656. Both verdicts remain UNINTERPRETABLE.

## Reading (honest, bounded)

1. **claude — positive control holds.** RESPECTS-ORDER at ceiling under the scaffold (DIRECT 1.000,
   COMP 64/64) confirms the scaffolded instrument is a valid non-commuting composition; the others'
   failure is not an artifact of a broken instrument.
2. **No witness, on the chaining axis.** Demonstrating the chaining mechanic explicitly did not let
   either model clear the on-demand gate. By [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md)
   this is an **on-signature** non-witness on a **newly-eased axis** (the three prior runs never eased
   chaining) — so it carries real information rather than the diminished value of re-easing an
   exhausted axis.
3. **What it localizes (the diagnostic dividend, persist branch).** The worked example tested the
   sub-hypothesis that the single-move reading is a **demonstration / comprehension gap** — that the
   models fail only because nothing showed them both moves must be applied. The signature **persisted**
   (gpt's intensified to 0.844), so that sub-hypothesis is **disfavored**: shown a worked chain and
   told the order, the models still read one move. The residual difficulty is therefore **not** that
   the procedure is undemonstrated; it is the **execution** of holding and applying two operations in
   sequence in this instrument. The implicated-axis map is redrawn again: the worked-example axis is
   now eased-and-discharged.
4. **Undischargeable, not closed** ([`essay/undischargeable-negative`](../essays/undischargeable-negative.md)).
   This is a **kind-2 instrument-uninterpretable** verdict for both models, not a capability-absence.
   It now survives **four** instruments (K=6 positional, K=4 positional, K=4 figure-maps, K=4
   figure-maps + worked example), two of them on-signature — without converting into "cannot compose."

## Witness-search suspension note (updated; per [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md))

A second on-signature easing has now been tried, so the suspension record is updated (a **spending**
decision; **not** a closure — the negative stays undischargeable):

- **(i) Axes eased and the verdict on each:** **state-space** (K=6→K=4) → no witness (off-signature);
  **per-move read-off** (positional arithmetic → figure→figure table) → no witness (on-signature);
  **chaining demonstration** (a worked example of applying both moves in sequence, this run) → **no
  witness** (on-signature; the signature persisted/intensified).
- **(ii) Implicated-but-un-eased axes:** **fewer chaining steps.** With the read-off and the
  demonstration gaps both discharged, the residual implicated axis is the bare *execution* of chaining
  two moves. **A caveat now bears on the search's reach:** an order-sensitive *composition* requires
  **≥ 2** moves by construction, so "fewer chaining steps" cannot go below two and remain a composition
  — this axis is near its natural floor on the byte-identical line. Further easing would change the
  instrument (a different/easier operation pair) or move off the byte-identical comparison.
- **(iii) Structural bound on the remaining search:** **none of the available type exists** (updated
  2026-06-19; was "none yet" — a later session supplied the argument). Unlike the rich-side rung (iii),
  which has the [`essay/transcript-ceiling`](../essays/transcript-ceiling.md) closure, this thin-side
  composition capability has **no kind-3 reach-closure**: [`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md)
  examined the only candidate — the **≥2-move floor** plus the chaining-execution localization — and
  showed it is a **task-parameter floor**, not a **medium-level exclusion**, so it caps one easing axis
  (step count) while the elicitation space stays open along others (a different operation pair, an
  execution-format scaffold, many-shot), and the step that would close it ("the difficulty *is* the
  irreducible core") is an undischargeable behavioral universal (the kind-4 box). So the search stays
  **suspended on budget, never structurally closed** — a *reasoned* null, not merely an absent bound. The
  ≥2-move floor still narrows what a "fewer-steps" easing could be, but a floor is not a ceiling.
- **(iv) Reopen condition:** a cheap, well-targeted probe on the remaining implicated axis (a genuinely
  easier *execution* of two-move chaining, or a different/easier non-commuting operation pair) would
  reopen the search; until one is run, the search is **suspended, not closed**.

## Honesty box

- **What this shows:** the on-demand composition gap for gemini and gpt survives a **second
  on-signature** easing — an explicit worked demonstration of the chaining mechanic; the single-move
  signature persists (gpt's intensifies to 0.844 with the order stated), so the difficulty is not a
  demonstration/comprehension gap but chaining execution. claude composes at ceiling.
- **What it does NOT show:** that gemini or gpt **cannot** compose two non-commuting moves. The
  negative is **undischargeable** ([`essay/undischargeable-negative`](../essays/undischargeable-negative.md)):
  a fewer-steps or alternative-operation easing might still find a witness. Both verdicts are **kind-2
  instrument-uninterpretable**, not capability-absence. The numeric DIRECT drops (gpt 0.250→0.156,
  gemini 0.656→0.625) are **within overlapping CIs** and read as "no witness", **not** "the scaffold
  hurt" (a confound: the worked example also lengthens the prompt).
- **SPLIT, not panel** ([`essay/capability-split`](../essays/capability-split.md)): a one-model
  existential (claude) plus two per-model instrument-bounded negatives; **never** averaged. No "claude
  is the stronger model" claim — these four runs are the **same** capability eased four ways (one task,
  four renderings), not several distinct probes (the explicit non-firing of `capability-split` trigger
  (c)).
- **Thin, not rich.** RESPECTS-ORDER is "respects operation order" (single-reader-recoverable), **not**
  rung (iii) / relational constitution; the rich side is documented structurally closed for text.
- **Limits:** one operationalization (STEP/FLIP, two moves), text-only, three-model panel, single run.
- **No human comparison** made or owed: `anchor: internal-contrast-only` (a within-model contrast over
  balanced, order-permuted content).
- **Spend:** **$0.372384 billed** (`usage.cost`-summed, 0 missing; liveness $0.00358 + claude $0.23749
  + gemini $0.08506 + gpt $0.04625). Pre-flight ≈ $0.40; came in just under. $0.60 hard stop never
  approached. **Day total 2026-06-18 ≈ $1.358 of $5.00.**
