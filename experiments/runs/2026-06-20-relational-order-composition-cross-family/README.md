# Cross-family (heterogeneous-operation) order-sensitive composition — BUILT, NOT RUN (witness-search suspension)

**Status: NOT RUN. $0 spent. Suspended before any finding-bearing call**, on
[`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md) grounds
(build cost demonstrably high + low prior of a new finding), exactly parallel to the depth-4 suspension
recorded on [`result/relational-order-composition-three-move`](../../../wiki/findings/results/relational-order-composition-three-move.md).
The frozen stimuli (`stimuli.json`, rstrip-sha `d33aa8e8…`) and the whole toolchain are kept for the
record and for a future session that wants to reopen with a cleaner design. `probe.py full` refuses to
run (`PREREG.md` renamed to `PREREG-NOTRUN.md`).

## What this was

The backlog's priority empirical step was a **different-kind** composition probe (not one more move of
the same kind): the **cross-family** axis named verbatim in
[`claim/relational-order-sensitive-reassignment`](../../../wiki/findings/claims/relational-order-sensitive-reassignment.md)
scope limit 2. The design composes two **transparently heterogeneous, non-commuting** operations — a
SPATIAL **SWAP** (two spots' tokens exchange) and an ATTRIBUTE **RECOLOR** (one spot's token repainted)
— on the working surface, asking whether the working-surface composition capacity (panel-concordant
RESPECTS-ORDER across operation pair, grid size, and depth 3) extends to binding two updates of
*different kinds* in stamp order. Verdict map, working-surface format, 0.50 ceiling, THIN adjudication,
and `internal-contrast-only` anchor all carried over from the Option-C runs; the ratified Option-C
decision is agnostic to which operations realize the non-commuting semantics, so no new decision was
owed (independently confirmed by the pre-run critic).

## Why it was suspended: five distinct shortcut-leak classes at the pre-run gate

The independent pre-run critic NO-GO'd the instrument **five** times, each for a real, distinct way a
**non-composing reader** could clear the 0.50 bar without reading+comparing the two round stamps. Each
was fixed; each fix exposed the next. This is the value of the gate — none of these reached a paid run.

1. **Object-anchored readout** ("what color is the moved token DAX?"): a stamp-using one-op reader
   `apply-only-the-earlier-op` scored **0.75**, because following the *moved* token makes the spatial
   op a relabeling under which the attribute op is inert in most cells. → Fixed by **position-anchored**
   readout ("what color is on the fixed DAX *spot*?").
2. *(structural-verification pass — refuted a tempting "cross-family is unbuildable" closure and
   supplied fix #1's idea.)*
3. **Geometry × cell confound**: the visible swap-pair geometry was correlated with the order (12:6),
   and since SWAP names its spots, a geometry-keyed reader scored up to **0.83**. → Fixed by the
   **MATCHED-PAIR construction**: each unit fixes the entire visible scene and emits *both* stamp
   orders, differing only in which op carries the earlier round number (opposite answers), so stamp
   order is independent of all visible geometry (geometry-oracle = 0.5000).
4. **Round-magnitude (marginal)**: round values were disjoint earlier/later (1–4 vs 5–9), so one
   op-line's round against a fixed cutoff recovered the order (**1.0**). → Fixed with **overlapping
   consecutive round pairs** `(k,k+1)`; best marginal single-round reader Wilson-LB **0.44**.
5. **Round-magnitude (geometry-conditional)**: `gcd(16,12)=4` correlated geometry with the round pair,
   so *within* each geometry the round values were disjoint by order — a geometry+one-round reader
   scored **1.0**. → Fixed by crossing **each geometry with all 12 round pairs** (4 geometries),
   collapsing the conditional reader to the marginal (Wilson-LB 0.44).

After all five fixes the instrument is clean against every **generalizable / causal** non-composing
reader (the round magnitude itself; the salient geometry and readout_type, each independent of the
round pair): geometry-oracle = **0.5000**, every brute-forced family reader ≤ 0.50, every
marginal/geometry/readout_type-conditional single-round reader Wilson-LB ≤ **0.44**, the genuine
composer at Wilson-LB **0.9615** — a decisive separation. `build_trials.py` + `fixtures/make_fixtures.py`
certify all of this mechanically.

## The residual gap (documented, not hidden) and why it tips to suspension

A **content-conditional** reader — keyed on the exact recolor color *and* one round line — retains a
small in-sample correlation (best ≈ 0.656, Wilson-LB ≈ 0.557) because, with a **single-bit answer**
({Cr, C_oth}) over two near-orthogonal operations and per-unit-varying colors, any visible content
feature keeps enough finite-count correlation with the round pair to overfit the 96-record set. This is
an **overfitting artifact of the frozen set, not a strategy a model could apply to a fresh prompt** (the
recolor color is causally irrelevant to the order; a model is not trained on these stimuli). Erasing
even that residual is combinatorially hard in a small frozen set.

The decisive point is **allocation, not certifiability** ([`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md)):
- **Low prior of a new finding.** The working-surface composition capacity is panel-concordant
  RESPECTS-ORDER on *every* axis tested (operation pair, grid size, depth 3), with zero strain. The
  expected outcome here is one more ceiling — modest information, the same diminishing-returns case that
  suspended depth-4.
- **High and rising build cost.** The cost term in the economics is usually the API spend; this probe
  surfaces a second cost dimension the essay's depth discussion already anticipates — **shortcut-proofing
  cost** — and shows it grows not only with *depth* but with *operation heterogeneity*: a single-bit
  answer over two heterogeneous ops is unusually leak-prone (five redesigns to defeat the structural
  leaks, with a residual content-conditional gap remaining).

So the project **suspends** the cross-family witness-search on these grounds — a spending decision, not
a closure, asserting **nothing** about the models. It is reopened by: a cleaner cross-family design that
certifies against content-conditional readers too (e.g. a larger/non-binary answer space so no single
visible feature pins the order); a cheaper route; or any sign that the capacity is *not* uniform (which
would raise the prior). The other "different-kind" candidates — **partially-conflicting refinements**
and **image referents** (multimodal) — remain the higher-value next steps and are not touched by this.

## Files

`common.py` (ops + working-surface elicitation), `build_trials.py` (frozen stimuli + the full
shortcut-certification suite, including the geometry-oracle and the marginal/conditional single-round
readers), `analyze.py` (the verdict map), `probe.py` (liveness + freeze-gated full run; refuses to run),
`fixtures/make_fixtures.py` (idealized-reader fixtures), `PREREG-NOTRUN.md` (the freeze doc, renamed so
`probe.py` refuses), `stimuli.json` (frozen, rstrip-sha `d33aa8e8…`).
