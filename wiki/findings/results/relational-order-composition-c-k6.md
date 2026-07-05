---
type: result
id: relational-order-composition-c-k6
title: Larger-grid (K=6, D6) generality re-run of order-sensitive composition — the working-surface witness REPLICATES on a bigger grid; all three models RESPECTS-ORDER; gpt's spontaneous-ordering reliability dips slightly with grid size but its on-demand composition stays at ceiling
meaning-senses:
  - relational
  - model-internal
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-19
updated: 2026-07-05
links:
  - rel: refines
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: supports
    target: result/relational-order-composition-c-altpair
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: essay/undischargeable-negative
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: refines
    target: concept/relational-meaning
  - rel: supports
    target: claim/output-channel-working-surface
---

# Result: larger-grid (K=6) generality re-run — the working-surface witness REPLICATES on a bigger grid

> **Status: proposed (2026-06-19).** A **generality** test of the execution-format **witness**
> ([`result/relational-order-composition-c-reasoning-scaffold`](relational-order-composition-c-reasoning-scaffold.md)),
> varying one further axis the witness and the alt-pair runs left fixed: the **grid size K**. Every
> prior Option-C run used a K=4 track (the dihedral group **D4**). This run keeps the **same** dihedral
> pair STEP (the K-cycle `p→(p+1)%K`) and FLIP (the reflection `p→(K-1)−p`) but on a **six-figure
> track**, so they generate **D6** (order 12 vs D4's 8): a larger answer space (figure-identity chance
> 1/4 → 1/6) and more positions to track. Everything else is held identical (figure→figure rendering,
> working-surface elicitation, thresholds, verdict map, thin adjudication). Stimuli freshly built
> (rstrip-sha `f4d0e36d…82b33`); an independent pre-run critic recomputed the D6 geometry and the
> shortcut-proofing at K=6 and returned **GO**.
>
> **Outcome: REPLICATES — all three models RESPECTS-ORDER on the larger grid.** Given a working
> surface, **claude** (DIRECT 1.000 / COMP 1.000), **gemini** (DIRECT 1.000 / COMP 1.000), and **gpt**
> (DIRECT 1.000 / COMP 0.861, Wilson-LB **0.763 > 0.50**) all clear the on-demand gate **and**
> spontaneously order the two non-commuting moves by their round stamps. So the witness — the
> dissolution of the four-instrument forced-format split into panel-concordance — is **not specific to
> the K=4 grid**: it generalizes to a larger one. This **strengthens**
> [`essay/output-channel-confound`](../essays/output-channel-confound.md)'s reading that the witness
> reflects a composition **capacity** (given a working surface), now shown across the grid-size axis as
> well as the operation-pair axis ([`result/relational-order-composition-c-altpair`](relational-order-composition-c-altpair.md)).
> 324/324 replies parsed via the target-blind `FINAL:` tag; **0 NA, 0 retried, 0 length-truncation**;
> independently reproduced (324/324 picks matched). **Still THIN** ("respects operation order", **not**
> rung (iii) / constitution; rich side stays documented structurally closed for text); `anchor:
> internal-contrast-only`; **no human-comparison claim.**

## The question (precise)

The execution-format witness found that opening a **working surface** (step-by-step output permitted,
`FINAL:`-tag parsed; reasoning-effort held constant) flipped **both** gemini (DIRECT 0.656→1.000) and
gpt (0.250→0.969) from UNINTERPRETABLE to RESPECTS-ORDER, so all three panel models compose two
non-commuting moves given room to externalize the execution. The **alt-pair** run
([`result/relational-order-composition-c-altpair`](relational-order-composition-c-altpair.md)) then
showed this is not specific to the one STEP/FLIP **operation pair** — it replicates on a genuinely
different non-commuting pair (CYCLE/SWAP, A4). [`essay/output-channel-confound`](../essays/output-channel-confound.md)
reads the witness as a composition **capacity**, not an artifact of one instrument. Both witness runs
ran at **K=4** (a four-figure track, the smallest grid on which two non-commuting moves are
distinguishable). The witness result's own honesty box flagged the gap: "larger grids (K>4)… still
untested." A capacity that holds only on the smallest grid is under-tested — a larger answer/position
space is a harder serial-tracking demand. **This probe varies that one axis and asks: does the
working-surface composition generalize to a larger grid, or was the witness grid-size-bounded?**

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

The **single substantive change** vs. the witness run is the **grid size K (4 → 6)**. STEP and FLIP are
K-general functions, so at K=6 they are the dihedral generators of **D6** (STEP a fixed-point-free
6-cycle, FLIP a fixed-point-free involution); they do not commute (SF-ends `[4,3,2,1,0,5]` ≠ FS-ends
`[0,5,4,3,2,1]`). Each move is rendered as an opaque figure→figure lookup table (the model never sees
positions). The balanced **VALID_CONFIGS** were re-enumerated for K=6 — one valid config per target
track position 0..5, order balanced 3 SF / 3 FS — where a config is valid iff its stamp-order target
differs from the start, both single-move ends, and the reversed-order end. Everything else is held
identical to the witness run: figure→figure rendering, the working-surface elicitation (`FINAL:`-tag
parser, `MAX_TOKENS` 1024, gemini `effort: minimal` **held constant**), the two arms, `TERM`/`ROUND_PAIRS`,
the thresholds, the symmetric verdict map, and the **THIN** adjudication. The stimuli are freshly built
(72 COMP + 36 DIRECT records/model; rstrip-sha `f4d0e36d…82b33`, differing from every K=4 run). The
reader **set** is unchanged from K=4 (only two moves: 2 canonical orders + print-order + 2 single-move
+ reversed) — only K changes — so the certification framework carries over.

- **COMP (headline, spontaneous):** order *not* stated; a reader who applies the moves in print or a
  fixed canonical order scores exactly **0.50**; only ordering by the round stamps (Wilson-95 LB >
  0.50) clears the bar. A working surface does not make COMP non-spontaneous — the query still does not
  state the order, so the model must still **decide** to order by the stamps.
- **DIRECT (on-demand gate):** order stated ("first … then …"). Gate `direct_acc ≥ 0.80` — the
  **empirical arbiter** of whether the larger grid is composable at all (it self-calibrates K=6's
  difficulty; a model that fails DIRECT yields an UNINTERPRETABLE COMP).

An **independent pre-run critic** (fresh agent) returned **GO**: it recomputed STEP/FLIP at K=6 from
scratch, confirmed D6 (order 12) and non-commutativity, independently enumerated the valid configs and
matched the frozen set, re-derived every record's target/swapped/single-move ends (**0 mismatches**
across 108 records), computed every idealized shortcut reader (constant-figure and fixed-position =
1/6; print-order and both canonical-order readers = **exactly 0.50**; start / single-move / reversed =
**0**), confirmed the frozen sha, verified the parser is target-blind, diffed against the witness run to
confirm the change is **K-only** (`analyze.py` and the fixtures byte-identical), and ruled **no new
decision owed** (K is not a parameter [`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md)
froze — indeed the original Option-C ran at K=6 before narrowing to K=4 for the witness search).

## Results (3 models, 108 records/model, 0 NA, 0 retried, 0 length-truncation; independently reproduced)

An **independent post-run verifier** (fresh agent) recomputed every number from raw with its own
Wilson, re-derived the K=6 geometry from `track`+`start_idx`+`order` with its own STEP/FLIP (0 mismatches
on all stored fields), and re-parsed every reply with an independent `FINAL:`-tag extractor:
**REPRODUCED — its 324 picks matched the stored picks 324/324** (a target-biased parser ruled out:
gpt's 10 COMP errors were parsed to the **wrong** figure gpt actually wrote — the reversed-order
`swapped` figure). It confirmed the build-time ceilings hold at K=6 (print-order = canonical-SF =
canonical-FS = exactly 0.50; start/single-move/reversed readers = 0), target figure uniform (12 each of
6 shapes), order balanced (36 SF / 36 FS), display balanced (36 stamp / 36 rev), full coverage / 0
duplicate rids / 0 NA / 0 retried / 0 length-truncation, and the billed cost $0.80455 with 0
missing-cost fields.

| model | DIRECT on-demand acc (gate 0.80) | COMP target rate (bar: Wilson-LB > 0.50) | verdict |
|---|---|---|---|
| **claude-sonnet-4.6** | **1.000** [0.904, 1.000] PASS | **1.000** [0.949, 1.000] → sig | **RESPECTS-ORDER** |
| **gemini-3.5-flash** | **1.000** [0.904, 1.000] PASS | **1.000** [0.949, 1.000] → sig | **RESPECTS-ORDER** |
| **gpt-5.4-mini** | **1.000** [0.904, 1.000] PASS | **0.861** [0.763, 0.923] → sig | **RESPECTS-ORDER** |

**Generality across grid size** — the on-demand gate (DIRECT) and spontaneous composition (COMP),
across the now-tested axes (all working-surface; gpt is the only model not already at ceiling, so the
trend shows on it):

| model | K=4 STEP/FLIP (witness) DIRECT / COMP | K=4 CYCLE/SWAP (alt-pair) DIRECT / COMP | **K=6 STEP/FLIP (this run) DIRECT / COMP** |
|---|---|---|---|
| claude | 1.000 / 1.000 | 1.000 / 1.000 | **1.000 / 1.000** |
| gemini | 1.000 / 1.000 | 1.000 / 1.000 | **1.000 / 1.000** |
| gpt | 0.969 / 0.953 | 1.000 / 0.906 | **1.000 / 0.861** |

**COMP failure breakdown** (spontaneous arm): claude and gemini swapped/start/single-move all 0.000;
**gpt** swapped (reversed-order) **0.139** (10/72), start 0.014 (1/72, a coincidence where the swapped
figure equals the start figure — the same miss double-counted), single-move (step-only 0.000, flip-only
0.000). So gpt's misses are **reversed-order slips** (it applies *both* moves but occasionally in the
wrong order) — **not** the single-move-reading signature that defined its forced-format failure. All 10
misses fall on `order=FS, display=stamp` records (the true order is FLIP-then-STEP, but the moves are
printed in round order); gpt composes both moves, just spontaneously picks the right order 86.1% of the
time at K=6.

**CoT genuineness (decisive).** On the 36 reverse-printed COMP records per model (the higher-round move
printed *first*, so a print-order reader lands on `swapped`), the visible working explicitly **re-sorts
the two moves by round stamp** (lower round first) before applying them. Verbatim (verifier-confirmed),
all on rid 0 (FLIP@8 printed first, STEP@3 second; target = triangle): claude — *"Round 8 was agreed
more recently than Round 3… determine the actual sequence"* (works out chronological order, lands on
target); gemini — *"First, we must order the moves by their round numbers, from earliest to most recent:
1. Round 3: STEP, 2. Round 8: FLIP"* then applies STEP then FLIP; gpt — *"Apply the two moves in round
order (older first, since higher round number means more recent): Round 3: STEP from diamond → square;
Round 8: FLIP from square → triangle"*. So the COMP signal is genuine stamp-order composition, not a
print-order coincidence. A representative gpt **miss** (rid 31): gpt correctly *printed* "Round 7: STEP…
Round 2: FLIP" but then applied them in listed order (7 before 2) rather than round order (2 before 7),
yielding the swapped figure — a genuine order-reversal error, not a parse artifact and not a single-move
read.

## Reading (honest, bounded)

1. **The witness generalizes across grid size.** On a larger grid (K=6, D6 — a bigger answer space and
   more positions to track than the K=4 the witness was found on), all three panel models again compose
   given a working surface. So the dissolution of the forced-format split is **not** an artifact of the
   small K=4 grid either — combined with the alt-pair run it now holds across **two generality axes**
   (operation pair and grid size). This is the further support
   [`essay/output-channel-confound`](../essays/output-channel-confound.md)'s "capacity, not
   one-instrument artifact" reading needed, and answers the witness result's open-question on larger
   grids in the **positive**.
2. **The DIRECT gate self-calibrated the larger grid, and it cleared at ceiling for all three.** The
   risk for a grid-size generality test is that K=6 is intrinsically harder, confounding "does it
   generalize?" with "is the bigger grid just harder?". The on-demand DIRECT gate controls for exactly
   this: it measures whether the grid is composable when the order is *given*. Here **all three clear
   DIRECT at ceiling (1.000)** — so K=6 is fully composable on demand for every model, and the COMP arm
   is interpretable. The instrument did not break (claude, the positive control, stays at ceiling), so
   K=6 is a valid test, not a degenerate one.
3. **gpt: a mild, monotone grid-size dip in spontaneous-ordering reliability — but composition capacity
   is untouched.** gpt's COMP target rate declines gently across the now-tested instruments — 0.953
   (K=4 STEP/FLIP) → 0.906 (K=4 CYCLE/SWAP) → **0.861 (K=6)** — while its **DIRECT stays at ceiling**
   (0.969 → 1.000 → 1.000) and its misses remain **reversed-order** slips (single-move reads 0.000
   throughout). So a larger grid makes gpt's *spontaneous choice of which order to apply* a little
   noisier, but does **not** erode its ability to chain both moves when told the order. The honest
   nuance: the capacity replicates cleanly on the larger grid; the spontaneous-ordering reliability for
   gpt is marginally lower as K grows, still comfortably clear of the 0.50 bar (Wilson-LB 0.763). With
   n=72 the three instruments' gpt CIs overlap, so the monotone dip is *suggestive*, not established.
4. **Still THIN; still no capability split; still no human comparison.** The verdict remains "respects
   operation order" (single-reader-recoverable; the stamped move-list and maps are in the record),
   **not** rung (iii). The panel is concordant on the larger grid too. `anchor: internal-contrast-only`;
   no claim about people.

## What this adds to the witness-search record

- **(i) Axes now tested for generality of the witness:** operation pair (STEP/FLIP → CYCLE/SWAP) →
  **replicates**; **grid size (K=4 → K=6) → replicates** (this run). Still untested: deeper composition
  (>2 moves), partially-conflicting refinements, image referents, cross-family dyads.
- **(ii) Bound on the capacity reading:** the working-surface composition is now shown on **two**
  distinct non-commuting pairs (D4, A4) and **two** grid sizes (K=4, K=6), so it is not a property of a
  single pair's geometry or a single grid's size. It remains one operationalization family (figure→figure
  lookup tables, **two** moves, text-only, three-model panel, single run per cell).
- **(iii) The thin/rich gap is untouched:** rung (iii) stays documented structurally closed for
  text-only stimuli; this result is on the thin side by construction (adjudicated before the run).
- **(iv) A measured grid-size signal worth a follow-up:** gpt's monotone COMP dip (0.953 → 0.906 →
  0.861, DIRECT at ceiling throughout) is the kind of pattern the **>2-move** (deeper-composition)
  probe — the natural [`essay/output-channel-confound`](../essays/output-channel-confound.md) trigger
  contrast case — would sharpen: does a bigger *serial-depth* demand (rather than a bigger *state*)
  produce a negative that survives the working surface? *[Pointer, s183: that probe ran —
  [`result/relational-order-composition-three-move`](relational-order-composition-three-move.md):
  the witness survives depth 3, all three models RESPECTS-ORDER.]*

## Honesty box

- **What this shows:** with a step-by-step working surface, **all three** panel models perform
  order-sensitive composition of two non-commuting moves at/near ceiling on a **larger grid** (K=6, D6)
  than the one the witness was found on (K=4, D4), and spontaneously order by round stamps. The witness
  — the dissolution of the forced-format split — is a composition **capacity** that generalizes over the
  grid size as well as the operation pair, not an artifact of one instrument.
- **What it does NOT show:** rung (iii) / constitution (the verdict is **THIN**, single-reader-
  recoverable). It does not show composition *without* a working surface (the witness run showed the
  forced format gates it). It does not extend generality to deeper composition (>2 moves), non-figure
  referents, or cross-family dyads. It makes **no** claim that one model is stronger than another (panel
  concordant). gpt's COMP is 0.861, not ceiling — the spontaneous-ordering reliability is marginally
  lower for gpt at this grid size (misses are reversed-order, not failure to chain), and with n=72 the
  apparent monotone dip across instruments is suggestive only (overlapping CIs).
- **Genuine, not parsing:** 324/324 replies parsed via the target-blind `FINAL:` tag; 0 NA, 0 retried,
  0 length-truncation; the COMP signal survives the 36 reverse-printed records (genuine stamp-order
  re-sort in the CoT for all three models, verbatim-confirmed).
- **No human comparison** made or owed: `anchor: internal-contrast-only` (a within-model contrast over
  balanced, order-permuted content).
- **Spend:** **$0.80455 billed** (`usage.cost`-summed, 0 missing; liveness $0.00528 + claude $0.48526 +
  gemini $0.25337 + gpt $0.06065). Pre-flight ≈ $0.83; came in just under. $1.50 hard stop never
  approached. **Day total 2026-06-19 ≈ $2.27 of $5.00** (this run $0.80 + the witness run $0.74 + the
  alt-pair run $0.74 earlier the same UTC day).
