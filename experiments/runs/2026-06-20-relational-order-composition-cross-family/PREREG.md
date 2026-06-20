# PREREG — CROSS-FAMILY (heterogeneous-operation) order-sensitive composition, POSITION-ANCHORED (Option-C generality axis)

**Run:** `2026-06-20-relational-order-composition-cross-family`
**Frozen stimuli:** `stimuli.json`
**rstrip-sha256 = `7ea7222ef915cb60f6483659b46a1d2c0c888aa11f4cdff1032b2d05180c83f9`**
(the `probe.py full` gate refuses to run unless this exact sha is recorded here)

> **Status at freeze: design complete, balance + fixtures certified, awaiting independent pre-run
> critic GO on this (position-anchored, second) design.** No finding-bearing call may run before the
> critic returns GO.
>
> **Design history (disclosed).** A first, **object-anchored** design (readout = "what color is the
> moved token DAX?") was correctly **NO-GO'd by the independent pre-run critic (2026-06-20)**: a
> stamp-using but non-composing reader, `apply-only-the-earlier-op`, scored COMP **0.75** (Wilson-LB
> 0.639 > 0.50) and would have falsely earned RESPECTS-ORDER, because anchoring the readout to the
> *moved* token makes the spatial op a follow-the-token relabeling under which the attribute op is
> inert in most cells. An independent structural-verification pass then **refuted** the tempting
> conclusion that cross-family composition is unbuildable, and supplied the fix: **anchor the readout
> to a FIXED spot** (this design). At a fixed spot both ops are live in every order-discriminating
> cell, so every single-op and stamp-using-partial reader caps at 0.50. This PREREG's certification
> brute-forces those partial readers **explicitly**.

## The question (precise)

Every prior Option-C run composed operations of the **same family**: position permutations rendered
as opaque figure→figure tables (STEP/FLIP = D4, CYCLE/SWAP = A4, generic S6). The working-surface run
found a **witness** and the alt-pair / K=6 / three-move runs replicated a composition **capacity**
across the operation-pair, grid-size, and depth axes — all panel-concordant RESPECTS-ORDER. But to
the model those were all the *same task*: compose two opaque permutations of one ground set.
[`claim/relational-order-sensitive-reassignment`] scope limit 2 names the still-untested generality
axis verbatim — *"generality (image referents, cross-family dyads) is untested."*

**This probe varies the KIND of the two operations: it composes two TRANSPARENTLY HETEROGENEOUS,
non-commuting operations — one SPATIAL (a swap), one ATTRIBUTE (a recolor) — and asks: does the
working-surface composition capacity extend to binding two updates of *different kinds* in stamp
order?** This is the relational axis's core (composing heterogeneous updates).

## The two heterogeneous operations + the position-anchored readout (the single manipulated variable: operation KIND)

A row of `K=4` spots, each holding a colored token. One spot, `s`, is nicknamed the **"DAX spot"** —
the readout. Two kinds of move, both stated transparently (no opaque tables):

- **SWAP** (a SPATIAL move): names two spots; their tokens exchange places (color travels with the
  token). Acts on POSITION.
- **RECOLOR** (an ATTRIBUTE move): names one spot and a color; that spot's token is repainted. Acts
  on COLOR.

The DAX spot `s` is one of the two SWAP spots, and the RECOLOR targets one of the two SWAP spots, so
**both ops are live at the readout** and they **do not commute** on the color at `s`: SWAP changes
*which* token sits at `s`; RECOLOR changes a token's color; the order decides the final color at `s`.

Each record stamps the two ops with two distinct rounds (higher = more recent); the true composition
applies them in **stamp order**. The two op-lines are shown in a **display order decoupled from stamp
order** (COMP arm). 

- **COMP (headline, spontaneous):** op-lines shown (display decoupled), query asks only the color on
  the DAX spot — does **not** state the order. The working surface does not make COMP non-spontaneous.
- **DIRECT (on-demand gate):** same trials; query states the order ("first … and then …"). Gate
  `direct_acc ≥ 0.80`. If it fails, COMP is UNINTERPRETABLE.

## Why the 0.50 ceiling, and why position-anchored is shortcut-clean

The four geometry **cells** = readout_type {`SAME` = the DAX spot is the recolor target; `DIFF` = the
DAX spot is the non-recolored swap spot} × stamp_first {SWAP, RECOLOR}. The DAX spot's own initial
color is always overwritten (swapped out or recolored), so it is **never** the answer; the answer is
always one of {`Cr` (recolor color), `C_oth` (the other swap spot's initial color)}:

| cell | color at the DAX spot, in stamp order | answer |
|---|---|---|
| SAME, SWAP-first | swap brings C_oth to s, then recolor s → Cr | **Cr** |
| SAME, RECOLOR-first | recolor s → Cr, then swap brings C_oth to s | **C_oth** |
| DIFF, SWAP-first | swap brings C_oth to s, recolor hits the other spot | **C_oth** |
| DIFF, RECOLOR-first | recolor the other spot, then swap brings it to s → Cr | **Cr** |

So the answer is fixed by **neither order alone nor geometry alone — only by both.** With the four
cells equally frequent the answer is `Cr` half the time and `C_oth` half, so **every non-composing
reader caps at exactly 0.50** (brute-forced over the actual 72 COMP records in
`assert_balance`, including the partial readers that broke the object-anchored design):

| reader | COMP rate |
|---|---|
| genuine per-trial **stamp-order composer** | **1.0000** |
| `apply-only-the-EARLIER-op` (the object-anchored killer) | **0.2500** |
| `apply-only-the-LATER-op` | 0.5000 |
| `apply-only-PRINT-FIRST` / `PRINT-SECOND` | 0.3750 |
| `swap-only` | 0.5000 · `recolor-only` 0.2500 |
| `reverse-stamp` | 0.0000 |
| `print-order` · `fixed-SWAP-first` · `fixed-RECOLOR-first` | 0.5000 |
| `report-Cr` · `report-C_oth` | 0.5000 |
| `init@s` | 0.0000 · every fixed-spot initial/fixed-order-final & const | ≤ 0.50 |

Only the per-trial stamp-order composer clears 0.50. Beating it (COMP target Wilson-95 LB > 0.50) is
**cross-family order-sensitive composition**.

## Design parameters (frozen)

- `K = 4` spots; answer space = **6 colors**; const-color = 1/6. Recolor color disjoint from every
  spot's initial color.
- COMP: 4 cells × 3 (a,b) geometries = 12 blocks × 6 colors = **72 records/model**.
- DIRECT: 4 cells × 3 geometries = 12 blocks × 3 colors = **36 records/model**.
- Total **108 records/model × 3 models = 324 finding-bearing calls.**
- Balance (proven at build): answer color uniform over 6 (const = 1/6); 4 cells / stamp_first /
  readout_type / readout-spot `s` (uniform over the 4 spots) / display order all balanced; every
  record is order-discriminating (`target ≠ reverse`).
- Working-surface elicitation **held identical** to the prior Option-C working-surface runs (`FINAL:`
  tag, `MAX_TOKENS = 1024`, gemini `effort: minimal` held constant, length-truncation never parsed,
  target-blind parser).
- Panel: claude = positive control; gemini + gpt = the cross-family targets.
- Pre-flight cost: depth-2 task, short CoT; estimate **≈ $0.5–0.8**; pre-registered **hard stop
  $1.50** on projected billed total.

## Frozen verdict map (identical to every prior Option-C run)

- `UNINTERPRETABLE` : `direct_acc < 0.80`.
- `RESPECTS-ORDER` : DIRECT gate passed AND COMP target-rate Wilson-95 LB > 0.50.
- `ORDER-BLIND-OR-WEAKER` : DIRECT gate passed AND COMP target-rate Wilson-95 LB ≤ 0.50.

## ADJUDICATION (binding, decided BEFORE the run, biased AGAINST the rich reading)

Per [`decisions/resolved/relational-rung-iii-path-dependence`]: an operation-order gap here is
**THIN**. The stamped operation list, the spots, and the colors are **in the record**;
single-reader-recoverable. RESPECTS-ORDER is reported as a thin **"respects operation order" /
cross-family-composition** finding — **never** rung (iii). The rich-side rung (iii) program is
documented **structurally closed for text-only stimuli**. `anchor: internal-contrast-only`; **no
human-comparison claim.**

## No new decision is owed (surfaced for the critic to gate)

The ratified Option-C decision adopted **"non-commuting operation semantics"** *agnostic to which
operations realize them* (it explicitly contemplated "rotate/move" edits) and **did not freeze the
operation kind**. Like the alt-pair (D4→A4), grid size (K=4→K=6), and move count (2→3) — none of
which owed a new decision — the operation-KIND change (homogeneous permutation pair → heterogeneous
spatial+attribute pair, answer now a color) is the same class of within-frame variation. The design
states **no new `wiki/decisions/open/` entry is owed**; the independent pre-run critic gates this.

## Certifications run at freeze (no API)

- `python3 build_trials.py` → `assert_balance` PASS: 72 COMP + 36 DIRECT; **composer = 1.000**; every
  non-composing reader in the brute-forced family (including `apply-only-EARLIER` = 0.25) ≤ 0.50
  (worst = 0.5000); all balance checks pass; every record order-discriminating. Frozen sha above.
- `python3 fixtures/make_fixtures.py` → ALL FIXTURE ASSERTS PASS: only a genuine stamp-order composer
  → RESPECTS-ORDER (1.0); report-Cr / fixed-order / print-order → 0.50; earlier-only → 0.25; all
  ORDER-BLIND-OR-WEAKER; const-color / direct-fail → UNINTERPRETABLE.

## Anchor

`internal-contrast-only`, carried forward and ratified for the Option-C program. Within-model contrast
over balanced/order-permuted content; no human comparison asserted or owed.
