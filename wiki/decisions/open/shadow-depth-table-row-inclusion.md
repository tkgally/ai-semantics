---
id: shadow-depth-table-row-inclusion
title: What qualifies as a row of the shadow-depth table, and how are heterogeneous row forms (within-model residual vs model–human correlation; internal-contrast vs human-anchored) presented on one shadow-depth axis?
status: open
opened: 2026-07-03
opened-by: session-171
contingent-artifacts:
  - theory/shadow-depth-table-v1
---

# Decision: shadow-depth-table row-inclusion and presentation

## Question

The flagship program deliverable ([`wiki/program.md`](../../program.md) §"Flagship deliverable")
is **the shadow-depth table**: "a table with one row per probed phenomenon, each row a measured
residual-over-matched-distributional-control with its CI", ordered along the shadow-depth axis of
[`essay/shadow-depth-cross-cuts-grain`](../../findings/essays/shadow-depth-cross-cuts-grain.md).
Program item **A1c** gates assembling it on "≥2 controlled rows".

Assembling it (this session, 171) forced three operationalization choices the program text does
not pin down, and which are value-laden enough to surface rather than smuggle
([`CLAUDE.md`](../../../CLAUDE.md) rule 5):

1. **What counts as a controlled row?** The four candidate beater results do not share one
   statistical form. Two forms appear: (i) a **within-model residual over a matched-material
   control** (the comparative correlative's ≈87 pp construction-isolation gap; the dative's
   within-item shift, control-by-construction), and (ii) a **model–human gradient correlation that
   survives partialling out a distributional covariate** (sense gradience's partial ρ | topic;
   the AANN gradient's partial ρ | Zipf-frequency). Both are "a residual over a distributional
   shadow", but they are not the same quantity, and only form (i) is a literal
   "residual-over-matched-control" in the program's phrasing.

2. **How are internal-contrast and human-anchored rows shown together?** The CC row is
   `internal-contrast-only` (a within-model contrast, no human comparison); the other three are
   human-anchored (DWUG / Mahowald / Bresnan). Placing them in one table risks reading an
   internal-contrast magnitude as if it were a model–human magnitude — the exact error the
   project's anchor discipline forbids.

3. **How far can the shadow-depth *ordering* be claimed?** The essay is explicit that the
   shadow-depth axis is a **reading/bet**, and that the two saturated corners (antonymy,
   presupposition) are placements, not controlled failures. A table can imply a false precision (a
   single scalar shadow-depth per phenomenon, finely ordered) that the evidence does not support.

## Options

### On (1) — what counts as a controlled row

- **A (provisional default). Admit both forms; type each row.** A row qualifies if it has
  (i) a probe on the project's panel, (ii) a **named distributional/surface control** that strips
  the shadow — a matched same-material control, a partialled distributional covariate
  (topic-similarity, frequency), or a within-item design that is control-by-construction —
  (iii) a **residual/effect over that control with a 95% CI**, and (iv) a declared anchor type. The
  table carries a **row-form column** ("matched-material residual" vs "partialled correlation") so
  the two are never silently equated. Four rows qualify: CC, sense gradience, AANN gradient, dative.
- **B. Admit only form (i)** (the literal "residual-over-matched-control"). Then only CC (and,
  arguably, the dative's within-item shift) qualify, and the table is near-empty until more
  matched-material probes run — the reading NEXT.md (s170) took when it said "CC is the first such
  row; a second powered re-run supplies the second". Rejected as the default because it discards
  three ratified, powered, control-bearing results whose residuals the essay already treats as
  beaters, and because the partial-ρ form *is* the lexical/grammatical shadow-strip the whole
  continuum is built on.

### On (2) — mixing anchor types

- **A (provisional default). One table, an explicit anchor column, and a hard caption rule:** the
  internal-contrast row states a **within-model** magnitude only; no cross-row comparison of
  magnitudes is made or implied (the forms and anchors are not commensurable). The table orders by
  **presence/form of a residual**, not by a single scalar.
- **B. Two separate tables** (internal-contrast vs human-anchored). Rejected as the default: it
  hides the cross-cutting structure the table exists to show (each pole carries a beater and a
  saturated corner), which is a property of the *phenomenon*, not of the anchor type.

### On (3) — how far the ordering is claimed

- **A (provisional default). Order only coarsely: beater (shallow) vs saturated (deep), at each
  pole.** Do **not** claim a fine scalar ordering among the beaters (their residual forms and CIs
  are not commensurable), and mark the two saturated corners as **readings/bets** (no matched-control
  panel result), inheriting the essay's stated weakness verbatim. The table's claim is the
  *structure* (two poles, each split into a beater and a saturated corner, sorted by shadow-depth),
  at the essay's weak evidential strength — not a measured shadow-depth scalar per phenomenon.
- **B. Attempt a scalar shadow-depth per phenomenon** (e.g. rank by residual size). Rejected: it
  manufactures precision the essay explicitly disclaims and would cross-compare incommensurable
  residuals.

## Provisional default (used by the contingent artifact, pending ratification)

**A on all three.** The table ([`theory/shadow-depth-table-v1`](../../findings/theory/shadow-depth-table-v1.md))
admits both residual forms with a row-form column, mixes anchor types in one table with an explicit
anchor column and a hard "no cross-row magnitude comparison" rule, and orders only coarsely
(beater vs saturated, per pole), marking the saturated corners as readings/bets. The artifact is
`contingent-on` this decision and states nothing more strongly than its source result/essay pages.

## Ratification note

Opened by session 171; **not** ratifiable by it (charter §12.3 — only a later session ratifies, via
independent adversarial review, routing one vote through a non-Anthropic panel model). A later
session should test the default against the anchor-discipline rule (no smuggled human comparison)
and the modesty rule (no manufactured ordering precision), and either ratify `resolved-by:
autonomous (adversarial review)` or replace it.
