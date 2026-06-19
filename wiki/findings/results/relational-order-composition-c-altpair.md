---
type: result
id: relational-order-composition-c-altpair
title: Alt-pair generality re-run of order-sensitive composition — the working-surface witness REPLICATES on a genuinely different non-commuting pair (CYCLE/SWAP, A4) — all three models RESPECTS-ORDER; the dissolution of the split is a composition capacity, not an artifact of the one STEP/FLIP instrument
meaning-senses:
  - relational
  - model-internal
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-19
updated: 2026-06-19
links:
  - rel: refines
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: essay/undischargeable-negative
  - rel: supports
    target: essay/floor-is-not-a-ceiling
  - rel: supports
    target: essay/capability-split
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: refines
    target: concept/relational-meaning
---

# Result: alt-pair generality re-run — the working-surface witness REPLICATES on a different non-commuting pair

> **Status: proposed (2026-06-19).** A **generality** test of the execution-format **witness**
> ([`result/relational-order-composition-c-reasoning-scaffold`](relational-order-composition-c-reasoning-scaffold.md)),
> varying the **single** axis the witness run left untested: the **operation pair**. Every prior
> Option-C run — including the witness — used the **dihedral** pair STEP (the 4-cycle `p→(p+1)%4`) and
> FLIP (the reflection `p→3−p`), which generate **D4**. This run swaps that for a **genuinely
> different** non-commuting pair — **CYCLE** (the 3-cycle `(1 2 3)` on the track) and **SWAP** (the
> double transposition `(0 1)(2 3)`), which generate **A4**, a different group with a different cycle
> structure — holding everything else identical (K=4, figure→figure rendering, working-surface
> elicitation, thresholds, verdict map, thin adjudication). The stimuli are freshly built (rstrip-sha
> `f21f0cfb…22bb`); an independent pre-run critic recomputed the A4-vs-D4 distinction and the shortcut-
> proofing and returned **GO**.
>
> **Outcome: REPLICATES — all three models RESPECTS-ORDER on the alt pair.** Given a working surface,
> **claude** (DIRECT 1.000 / COMP 1.000), **gemini** (DIRECT 1.000 / COMP 1.000), and **gpt** (DIRECT
> 1.000 / COMP 0.906, Wilson-LB **0.810 > 0.50**) all clear the on-demand gate **and** spontaneously
> order the two non-commuting moves by their round stamps. So the witness — the dissolution of the
> four-instrument forced-format split into panel-concordance — is **not specific to the STEP/FLIP
> instrument**: it generalizes to a different non-commuting operation pair. This **strengthens**
> [`essay/output-channel-confound`](../essays/output-channel-confound.md)'s reading that the witness
> reflects a composition **capacity** (given a working surface), not a one-instrument artifact, and
> answers the witness result's open-question (iv) ("generality across operation pairs… still untested")
> in the **positive**. 288/288 replies parsed via the target-blind `FINAL:` tag; **0 NA, 0 retried, 0
> length-truncation**; independently reproduced. **Still THIN** ("respects operation order", **not**
> rung (iii) / constitution; rich side stays documented structurally closed for text); `anchor:
> internal-contrast-only`; **no human-comparison claim.**

## The question (precise)

The execution-format witness found that opening a **working surface** (step-by-step output permitted,
`FINAL:`-tag parsed; reasoning-effort held constant) flipped **both** gemini (DIRECT 0.656→1.000) and
gpt (0.250→0.969) from UNINTERPRETABLE to RESPECTS-ORDER on the byte-identical figure-to-figure trials,
so all three panel models compose two non-commuting moves given room to externalize the execution.
[`essay/output-channel-confound`](../essays/output-channel-confound.md) draws the general lesson and
claims the dissolution reflects a composition **capacity**, not an artifact of the one STEP/FLIP
instrument. But the witness was measured on a **single** non-commuting pair (STEP/FLIP, the dihedral
generators of D4). Its own honesty box flagged the gap: "generality across operation pairs, larger
grids, >2 moves… is still untested." A capacity claim that holds for exactly one operation pair is
under-tested. **This probe varies that one axis and asks: does the working-surface composition
generalize to a genuinely different non-commuting pair, or was it pair-specific?**

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

The **single manipulated variable** vs. the witness run is the **operation pair**. CYCLE and SWAP are a
genuinely different pair, not a relabeling: ⟨CYCLE, SWAP⟩ = **A4** (order 12, all even permutations)
versus ⟨STEP, FLIP⟩ = **D4** (order 8); a 3-cycle + a double transposition versus a 4-cycle + a
reflection. They do not commute (CS-ends `[1,3,2,0]` ≠ SC-ends `[2,0,1,3]` at every start). Each move
is rendered as an opaque figure→figure lookup table (the model never sees positions or operation
names' semantics — only the table), so swapping the pair changes the tables the model must compose
**without** changing the surface presentation format. Everything else is held identical to the witness
run: K=4, figure→figure rendering, the working-surface elicitation (`FINAL:`-tag parser, `MAX_TOKENS`
1024, gemini `effort: minimal` **held constant**), the two arms, `SHAPES`/`TERM`/`ROUND_PAIRS`, the
thresholds, the symmetric verdict map, and the **THIN** adjudication. The stimuli are freshly built
(64 COMP + 32 DIRECT records/model; rstrip-sha `f21f0cfb…22bb`, differing from the STEP/FLIP runs).

- **COMP (headline, spontaneous):** order *not* stated; a reader who applies the moves in print or a
  fixed canonical order scores exactly **0.50**; only ordering by the round stamps (Wilson-95 LB >
  0.50) clears the bar. A working surface does not make COMP non-spontaneous — the query still does not
  state the order, so the model must still **decide** to order by the stamps.
- **DIRECT (on-demand gate):** order stated ("first … then …"). Gate `direct_acc ≥ 0.80` — the
  **empirical arbiter** of whether the alt pair is composable at all (it self-calibrates the pair's
  difficulty; a model that fails DIRECT yields an UNINTERPRETABLE COMP, exactly as on STEP/FLIP).

An **independent pre-run critic** (fresh agent) returned **GO**: it recomputed CYCLE/SWAP from scratch,
confirmed A4 ≠ D4 (a genuinely different pair, not a relabeling), re-derived every record's
target/swapped/single-move ends (**0 mismatches**), computed every idealized shortcut reader
(constant-figure and fixed-position = 1/K; print-order and both canonical-order readers = **exactly
0.50**; start / single-move / reversed-order = **0.00**; only a genuine stamp-order composer > 0.50),
confirmed the frozen sha, verified the parser is target-blind, diffed against the witness run to
confirm **only** the operation pair (and the balanced configs / honest labels) changed, and ruled **no
new decision owed** (a within-frame generality variation of the ratified Option-C instrument; the
operation pair is not a parameter [`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md)
froze).

## Results (3 models, 96 records/model, 0 NA, 0 retried, 0 length-truncation; independently reproduced)

An **independent post-run verifier** (fresh agent) recomputed every number from raw with its own
Wilson, re-derived the geometry from `track`+`start_idx`+`order` with its own CYCLE/SWAP (0 mismatches
on all stored fields), and re-parsed every reply with an independent `FINAL:`-tag extractor:
**REPRODUCED — its 288 picks matched the stored picks 288/288** (a target-biased parser ruled out:
gpt's 6 COMP errors were parsed to the **wrong** figure gpt actually wrote — all to the reversed-order
`swapped` figure). It confirmed the print-order ceiling (a print-order reader scores exactly 0.500; the
rev/stamp display split is balanced 32/32), target figure uniform (16/16/16/16), full coverage / 0
duplicate rids / 0 NA / 0 retried / 0 length-truncation, and the billed cost $0.73911 with 0
missing-cost fields.

| model | DIRECT on-demand acc (gate 0.80) | COMP target rate (bar: Wilson-LB > 0.50) | verdict |
|---|---|---|---|
| **claude-sonnet-4.6** | **1.000** [0.893, 1.000] PASS | **1.000** [0.943, 1.000] → sig | **RESPECTS-ORDER** |
| **gemini-3.5-flash** | **1.000** [0.893, 1.000] PASS | **1.000** [0.943, 1.000] → sig | **RESPECTS-ORDER** |
| **gpt-5.4-mini** | **1.000** [0.893, 1.000] PASS | **0.906** [0.810, 0.956] → sig | **RESPECTS-ORDER** |

**Generality across the operation pair** — the on-demand composition gate, STEP/FLIP (witness run) vs.
CYCLE/SWAP (this run):

| model | STEP/FLIP DIRECT (witness) | STEP/FLIP COMP | **CYCLE/SWAP DIRECT (this run)** | **CYCLE/SWAP COMP** |
|---|---|---|---|---|
| claude | 1.000 | 1.000 | **1.000** | **1.000** |
| gemini | 1.000 | 1.000 | **1.000** | **1.000** |
| gpt | 0.969 | 0.953 | **1.000** | **0.906** |

**COMP failure breakdown** (spontaneous arm): claude and gemini swapped/start/single-move all 0.000;
**gpt** swapped (reversed-order) **0.094** (6/64), start 0.062 (4/64), single-move (cycle-only 0.000,
swap-only 0.031). So gpt's few misses are **reversed-order slips** (it occasionally applies the two
moves in the wrong order) and a couple of start/single-move slips — **not** the single-move-reading
signature that defined its forced-format failure (cycle-only 0.000). gpt composes *both* moves; it
just spontaneously picks the right order 90.6% of the time rather than at ceiling.

**CoT genuineness (decisive).** On the 32 reverse-printed COMP records (the higher-round move printed
*first*, so a print-order reader lands on `swapped`), all three models picked target **32/32** and the
visible working explicitly **re-sorts the two moves by round stamp** (lower round first) before
applying them. Verbatim (verifier-confirmed): claude — *"Round 6 is more recent than Round 1, so Round
1's move happened first… 1. First move (Round 1): CYCLE … 2. Second move (Round 6): SWAP"*; gemini —
*"track its moves in chronological order based on the round numbers (from lowest to highest)… Round 3
(First Move): CYCLE … Round 8 (Second Move): SWAP"*; gpt — *"Round 3: CYCLE → circle becomes star -
Round 8: SWAP → star becomes triangle"* (applies Round 3 before Round 8 despite SWAP@8 printed first).
So the COMP signal is genuine stamp-order composition, not a print-order coincidence.

## Reading (honest, bounded)

1. **The witness generalizes across the operation pair.** On a genuinely different non-commuting pair
   (A4, not the witness's D4), all three panel models again compose given a working surface. The
   dissolution of the four-instrument forced-format split was therefore **not** an artifact of the one
   STEP/FLIP instrument — it reflects a composition **capacity** that survives changing the pair. This
   is the direct support [`essay/output-channel-confound`](../essays/output-channel-confound.md)'s
   "capacity, not one-instrument artifact" reading needed, and it answers the witness result's
   open-question (iv) (generality across operation pairs) in the **positive**.
2. **The DIRECT gate self-calibrated the new pair, and it cleared.** A real risk for a generality test
   is that the alt pair is intrinsically harder (or easier), confounding "does it generalize?" with
   "is this pair different difficulty?". The on-demand DIRECT gate controls for exactly this: it is the
   measured arbiter of whether the pair is composable when the order is *given*. Here **all three clear
   DIRECT at ceiling (1.000)** — so the alt pair is fully composable on demand, and the COMP arm is
   interpretable for every model. The instrument did not break (claude, the positive control, stays at
   ceiling), so the alt pair is a valid test, not a degenerate one.
3. **gpt: composes, with a slightly noisier spontaneous order.** gpt's COMP target on the alt pair is
   0.906 (vs 0.953 on STEP/FLIP) — a touch off ceiling — but its DIRECT is **1.000** (vs 0.969), and
   its misses are **reversed-order** slips, not single-move reads. So the residual is in *which order it
   spontaneously chooses*, not in *whether it can chain both moves*; the single-move signature that
   defined the forced-format negative is gone (cycle-only 0.000). This is the honest nuance: the
   capacity replicates cleanly; the spontaneous-ordering reliability is marginally lower for gpt on this
   pair, well clear of the 0.50 bar.
4. **Still THIN; still no capability split; still no human comparison.** The verdict remains "respects
   operation order" (single-reader-recoverable; the stamped move-list and maps are in the record),
   **not** rung (iii). The panel is concordant on the alt pair too, so this again `supports` the
   concordant reading [`essay/capability-split`](../essays/capability-split.md) flagged (the forced-
   format "claude is the stronger composer" split was elicitation-relative, and a second instrument
   confirms it). `anchor: internal-contrast-only`; no claim about people.

## What this adds to the witness-search record

- **(i) Axes now tested for generality of the witness:** operation pair (STEP/FLIP → CYCLE/SWAP) →
  **replicates** (all three RESPECTS-ORDER given a working surface). Still untested: larger grids (K>4),
  deeper composition (>2 moves), partially-conflicting refinements, image referents, cross-family
  dyads.
- **(ii) Bound on the capacity reading:** the working-surface composition is now shown on **two**
  distinct non-commuting pairs of different group structure (D4, A4), so it is not a property of a
  single pair's particular geometry. It remains one operationalization family (figure→figure lookup
  tables, two moves, K=4, text-only, three-model panel, single run per pair).
- **(iii) The thin/rich gap is untouched:** rung (iii) stays documented structurally closed for
  text-only stimuli; this result is on the thin side by construction (adjudicated before the run).

## Honesty box

- **What this shows:** with a step-by-step working surface, **all three** panel models perform
  order-sensitive composition of two non-commuting moves at/near ceiling on a **genuinely different**
  non-commuting pair (CYCLE/SWAP, A4) than the one the witness was found on (STEP/FLIP, D4), and
  spontaneously order by round stamps. The witness — the dissolution of the forced-format split — is a
  composition **capacity** that generalizes over the operation pair, not an artifact of one instrument.
- **What it does NOT show:** rung (iii) / constitution (the verdict is **THIN**, single-reader-
  recoverable). It does not show composition *without* a working surface (untested here; the witness run
  showed the forced format gates it). It does not extend generality to larger grids, deeper
  composition, or non-figure referents. It makes **no** claim that one model is stronger than another
  (panel concordant). gpt's COMP is 0.906, not ceiling — the spontaneous-ordering reliability is
  marginally lower for gpt on this pair (its misses are reversed-order, not failure to chain).
- **Genuine, not parsing:** 288/288 replies parsed via the target-blind `FINAL:` tag; 0 NA, 0 retried,
  0 length-truncation; the COMP signal survives the 32 reverse-printed records (genuine stamp-order
  re-sort in the CoT for all three models, verbatim-confirmed).
- **No human comparison** made or owed: `anchor: internal-contrast-only` (a within-model contrast over
  balanced, order-permuted content).
- **Spend:** **$0.73911 billed** (`usage.cost`-summed, 0 missing; liveness $0.00486 + claude $0.46459 +
  gemini $0.21683 + gpt $0.05283). Pre-flight ≈ $0.8–1.0; came in mid-range (claude CoT the driver).
  $1.50 hard stop never approached. **Day total 2026-06-19 ≈ $1.47 of $5.00** (this run $0.74 + the
  witness run $0.74 earlier the same UTC day).
