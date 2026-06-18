---
type: result
id: relational-order-composition-c-figure-to-figure
title: Figure-to-figure (on-signature) witness-seeking re-run of order-sensitive composition — removing the position↔figure read-off did NOT let gemini or gpt clear the on-demand composition gate; the single-move-reader signature persists even when each move is a trivial lookup, localizing the difficulty to chaining itself; claude still RESPECTS-ORDER at ceiling
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

# Result: figure-to-figure (on-signature) witness-seeking re-run — no witness; the single-move-reader signature persists when each move is a trivial lookup

> **Status: proposed (2026-06-18).** The **on-signature** witness-seeking re-run of the Option-C
> order-sensitive composition split. The Option-C run ([`result/relational-order-composition-c`](relational-order-composition-c.md), K=6)
> found: `claude-sonnet-4.6` RESPECTS-ORDER, but **both** `gemini-3.5-flash` (DIRECT 0.583) and
> `gpt-5.4-mini` (DIRECT 0.194) **failed the on-demand DIRECT gate** → UNINTERPRETABLE. The first
> easing ([`result/relational-order-composition-c-easier-k4`](relational-order-composition-c-easier-k4.md))
> shrank the **state space** (K=6→K=4) and the split survived — but
> [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md) judged that easing
> **off-signature**: the failure signature is **single-move readers** (the model applies only *one* of
> the two stamped moves), which implicates the **chaining / per-move read-off** layer, not track size.
> This probe eases **that** layer — the exact "figure-to-figure" easing
> [`essay/capability-split`](../essays/capability-split.md) **revision trigger (b)** names — by
> re-rendering the **byte-identical K=4 trials** so each move is an explicit **figure → figure lookup
> table** with **no positions shown** (removing the position↔figure read-off). `analyze.py`,
> thresholds, and the verdict map are unchanged; the DIRECT gate is the measured arbiter of "easier."
>
> **Outcome: NO WITNESS — and this time on the implicated axis.** Removing the positional read-off did
> **not** let either model clear the on-demand gate: **gemini DIRECT 0.656** (< 0.80; CI [0.483, 0.796])
> and **gpt DIRECT 0.250** (< 0.80; CI [0.133, 0.421]) → **both still UNINTERPRETABLE**. **claude still
> RESPECTS-ORDER at ceiling** (DIRECT 1.000; COMP 64/64) — the figure-map instrument is a valid
> non-commuting composition. The decisive detail: the **single-move-reader signature persists** even
> though each move is now a one-step table lookup — on the DIRECT arm, where the order is *stated
> outright*, **gpt applies only one of the two moves 65.6% of the time** (gemini 21.9%, claude 0%). So
> the difficulty is **not** the per-move computation the figure-maps removed; it is **holding and
> applying two operations in sequence** (the chaining itself). Per
> [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md), an on-signature
> non-witness meaningfully lowers the posterior that a witness exists and warrants a **witness-search
> suspension note** (below) — but per [`essay/undischargeable-negative`](../essays/undischargeable-negative.md)
> it **does not** prove gemini or gpt "cannot compose": the behavioral negative stays
> **undischargeable, not closed**. `anchor: internal-contrast-only`; **no human-comparison claim.**

## The question (precise)

A witness-seeking probe asks one thing: is the Option-C UNINTERPRETABLE verdict (gemini, gpt cannot
compose two non-commuting moves on demand) driven by an axis of difficulty an *easier* elicitation
removes — a *witness* flipping the negative — or robust to easing? The K=4 easing already tested the
**state-space** axis (off-signature) and found no witness. This probe tests the **on-signature** axis
the failure implicates: the per-move **read-off / computation**. The single manipulated variable is
the **rendering** — the trials are byte-identical to the K=4 run (same `stimuli.json` sha
`975e31bc…88ba`), but each move is now given as an explicit figure→figure table rather than positional
arithmetic on a track, so composing the two moves is two table look-ups and the position↔figure
read-off is gone.

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

The K=4 non-commuting STEP/FLIP trials (dihedral generators of a 4-ring), re-rendered. The prompt
shows the four figures, then **two move tables** ("Move STEP: a triangle becomes a circle, a circle
becomes a square, …"; "Move FLIP: …") derived from each record's geometry and listed in a **fixed
canonical figure order** (no positions appear anywhere), then a stamped record of the two moves
("Round 3: DAX made move STEP"), displayed in round order in half the records and reversed in half.

- **COMP (headline, spontaneous):** "Which figure does DAX sit on now?" — order *not* stated. A reader
  who applies the moves in print order, or in a fixed canonical order, scores exactly **0.50**; only
  ordering the two moves **by their round stamps** (Wilson-95 LB > 0.50) clears the bar.
- **DIRECT (on-demand gate):** the order is stated ("first … then …"). Confirms the model *can*
  compose the two moves in this instrument. Gate: `direct_acc ≥ 0.80`. If it fails, COMP is
  UNINTERPRETABLE (cannot tell spontaneous order-blindness from inability-to-compose).

**Adjudicated THIN before the run** (carried over unchanged; biased *against* the rich reading): the
stamped move-list and the maps are in the record, so an order gap is single-reader-recoverable —
"respects operation order", **never** rung (iii) / constitution. The rich-side rung (iii) is
documented structurally closed for text-only stimuli. An **independent pre-run critic** returned
**GO**: it reproduced the freeze (sha byte-identical to K=4), recomputed the geometry from scratch (0
mismatches), parsed the move tables back out of the rendered text (0 position leaks across 96 prompts;
stamp-order composition → target in all 96; DIRECT solvable 32/32), brute-forced 12 figure-table-level
readers (only stamp-order beats 0.50; the track-position picker *vanishes*), and ruled **no new
decision owed** (a rendering-only, byte-identical-trial easing within the ratified Option-C frame).

## Results (3 models, 96 records/model, 0 NA, 0 length-truncation; independently reproduced)

An **independent post-run verifier** recomputed every number from raw with its own Wilson
implementation: **REPRODUCED, no mismatches**.

| model | DIRECT on-demand acc (gate 0.80) | COMP target rate (bar: Wilson-LB > 0.50) | verdict |
|---|---|---|---|
| **claude-sonnet-4.6** | **1.000** [0.893, 1.000] PASS | **1.000** [0.943, 1.000] → sig | **RESPECTS-ORDER** |
| **gemini-3.5-flash** | **0.656** [0.483, 0.796] FAIL | 0.484 [0.366, 0.604] → not sig | **UNINTERPRETABLE** |
| **gpt-5.4-mini** | **0.250** [0.133, 0.421] FAIL | 0.312 [0.212, 0.434] → not sig | **UNINTERPRETABLE** |

**The failure signature, on the DIRECT (order-stated) arm** — the load-bearing detail:

| model | DIRECT target | step-only | flip-only | **single-move sum** | swapped | start |
|---|---|---|---|---|---|---|
| claude | 1.000 | 0.000 | 0.000 | **0.000** | 0.000 | 0.000 |
| gemini | 0.656 | 0.094 | 0.125 | **0.219** | 0.031 | 0.031 |
| gpt | 0.250 | 0.188 | 0.469 | **0.656** | 0.156 | 0.156 |

Even when **told the order explicitly**, gpt applies only one of the two moves in **two-thirds** of
DIRECT trials; gemini in ~one-fifth. The COMP arm shows the same dominant error mode (gpt step-only
0.328 + flip-only 0.297; gemini 0.172 + 0.141). Removing the per-move computation the figure-maps
eased did **not** dissolve the single-move signature.

**DIRECT on-demand accuracy across the three easings** (the witness search to date):

| model | K=6 positional | K=4 positional (state-space easing) | **K=4 figure-maps (read-off easing, this run)** |
|---|---|---|---|
| gemini | 0.583 | 0.594 | **0.656** (rose; still sub-gate) |
| gpt | 0.194 | 0.438 | **0.250** (did not improve over K=4 positional) |
| claude | 0.861 | 0.906 | **1.000** (positive control, ceiling) |

gemini's DIRECT has risen monotonically across the eased instruments and the figure-map rendering
helped it most (0.594 → 0.656), bringing its upper CI (0.796) to just under the gate — but it has not
cleared it. gpt's DIRECT did **not** improve under figure-maps relative to the K=4 positional run
(0.438 → 0.250; overlapping Wilson intervals, single instrument — not over-read as "got worse", but
plainly **not a witness**); its single-move reading actually intensified. Both verdicts remain
UNINTERPRETABLE.

## Reading (honest, bounded)

1. **claude — positive control holds.** RESPECTS-ORDER at ceiling under figure-maps (DIRECT 1.000,
   COMP 64/64) confirms the eased instrument is a valid non-commuting composition; the others' failure
   is not an artifact of a broken instrument.
2. **No witness, on the implicated axis.** Neither gemini nor gpt cleared the on-demand gate when the
   position↔figure read-off was removed. By [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md),
   this is the **first on-signature** non-witness in the search (the K=4 easing was off-signature) — so
   it lowers the posterior that a witness exists more than the K=4 non-witness did.
3. **What it localizes.** The figure-maps removed per-move computation cost, and the single-move-reader
   signature **survived** (gpt 65.6% single-move on the order-stated arm). This is genuinely
   informative: the remaining difficulty is **not** the per-move read-off but the **chaining** —
   holding two operations and applying *both* in sequence. The next un-eased on-signature axes are a
   **worked-example scaffold** (demonstrating that both moves must be applied) and **fewer chaining
   steps**; figure-to-figure is now discharged.
4. **Undischargeable, not closed** ([`essay/undischargeable-negative`](../essays/undischargeable-negative.md)).
   This is a **kind-2 instrument-uninterpretable** verdict for both models, not a capability-absence. A
   still-different easing (worked example, fewer steps) might yet find a witness; this result *bounds*
   the negative — it now survives **three** instruments (K=6 positional, K=4 positional, K=4
   figure-maps) including the on-signature one — without converting it into "cannot compose."

## Witness-search suspension note (per [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md))

The on-signature easing has now been tried, so the reporting discipline calls for a suspension record
(a **spending** decision; **not** a closure — the negative stays undischargeable):

- **(i) Axes eased and the verdict on each:** **state-space** (K=6→K=4, [`…-easier-k4`](relational-order-composition-c-easier-k4.md)) → no witness; **per-move read-off / computation** (positional arithmetic → figure→figure lookup table, this run) → **no witness** (the on-signature easing).
- **(ii) Implicated-but-un-eased axes:** **chaining itself** — a **worked-example scaffold** (demonstrate that both stamped moves must be applied) and **fewer chaining steps**. The single-move signature surviving the read-off easing implicates *these* specifically.
- **(iii) Structural bound on the remaining search:** **none yet** for this thin-side composition capability (unlike the rich-side rung (iii), which has the [`essay/transcript-ceiling`](../essays/transcript-ceiling.md) closure). No argument yet shows a worked example or fewer-steps design *cannot* carry a witness.
- **(iv) Reopen condition:** a cheap, well-targeted probe on an un-eased implicated axis — a worked-example-scaffold or fewer-chaining-steps composition design. Such a probe would reopen the search; until one is run, the search is **suspended, not closed**.

## Honesty box

- **What this shows:** the on-demand composition gap for gemini and gpt survives an **on-signature**
  easing (removing the position↔figure read-off); the single-move-reader signature persists when each
  move is a trivial lookup, localizing the residual difficulty to chaining. claude composes at ceiling.
- **What it does NOT show:** that gemini or gpt **cannot** compose two non-commuting moves. The
  negative is **undischargeable** ([`essay/undischargeable-negative`](../essays/undischargeable-negative.md)):
  a worked-example or fewer-steps easing might still find a witness. Both verdicts are **kind-2
  instrument-uninterpretable**, not capability-absence.
- **SPLIT, not panel** ([`essay/capability-split`](../essays/capability-split.md)): a one-model
  existential (claude) plus two per-model instrument-bounded negatives; **never** averaged. No
  "claude is the stronger model" claim — one probe licenses no cross-task ranking.
- **Thin, not rich.** RESPECTS-ORDER is "respects operation order" (single-reader-recoverable), **not**
  rung (iii) / relational constitution; the rich side is documented structurally closed for text.
- **Limits:** one operationalization (STEP/FLIP, two moves), text-only, three-model panel, single run.
- **No human comparison** made or owed: `anchor: internal-contrast-only` (a within-model contrast over
  balanced, order-permuted content).
- **Spend:** **$0.366074 billed** (`usage.cost`-summed, 0 missing; liveness $0.00253 + claude $0.28262
  + gemini $0.05122 + gpt $0.02972). Pre-flight ≈ $0.30; came in just above (figure-map prompts longer).
  $0.60 hard stop never approached. **Day total 2026-06-18 ≈ $0.986 of $5.00.**
