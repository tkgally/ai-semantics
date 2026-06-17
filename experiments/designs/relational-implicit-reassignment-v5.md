# Design — relational implicit-reassignment control (of Option A)

**Run dir:** `experiments/runs/2026-06-17-relational-implicit-reassignment/`
**Controls:** `wiki/findings/results/relational-spontaneous-recency-a` (Option A) and the claim it
supports, `wiki/findings/claims/relational-order-sensitive-reassignment`.
**Decision lineage:** `wiki/decisions/resolved/relational-v5-text-position-neutralization`
(anchor `internal-contrast-only`; the staged B→A line is complete — this is a follow-on control of
the Option-A positive, not a new staged arm).

## The question this control isolates

Option A established that both panel models recover a **reassigned** coined term by its
**most-recent binding**, spontaneously (SPONT latest-binding 1.000, position at chance, DIRECT
on-demand 1.000) → `claim/relational-order-sensitive-reassignment`. The claim's sharpest open
caveat (scope limit 4 / revision trigger 2): "spontaneous" there means *query-not-directed, not
cue-free* — Option A's INTRO told the model the term *"was reassigned … in different rounds you
agreed it referred to different figures."* This control removes **exactly that sentence** and
re-measures the SPONT latest-binding rate, to test whether latest-binding-wins is a **surface
artifact** of the explicit reassignment wording.

## The sole manipulation (single-factor control)

The INTRO drops Option A's explicit reassignment flag; it keeps the stamp semantics ("a higher
round number means it was said more recently") and the not-in-round-order note (the framing Option B
proved both models read on demand, required for the stamp to be interpretable and the DIRECT gate to
be meaningful). The model must itself notice the term picks out different figures across rounds.

**Everything else is held identical to Option A**, and the frozen `stimuli.json` roster is
**byte-identical** (same sha256 `432cb57d4aeefea62f382923fbc98019a184bd1e62879956edcd0e3dd944ff71`;
the INTRO text lives in `common.py`'s renderer, not the roster): figures, non-contiguous round
quadruples, balanced-block geometry (position/lexical/frequency all pinned to 1/K), `TERM = "DAX"`,
`SEED0`, the two query conditions (SPONT headline 48/model + DIRECT manipulation check 32/model),
forced single-label elicitation, parse, scoring, and the verdict map.

## Verdict map and pre-registered claim reading

Carried verbatim from Option A (see the run's `PREREG.md`): `SPONTANEOUS-RECENCY` /
`SPONTANEOUS-ANTI-RECENCY` / `ORDER-SENSITIVE-MIXED` = order-sensitive (non-commutative);
`COMMUTATIVE-HERE` = order-insensitive without the explicit flag; `UNINTERPRETABLE` = DIRECT gate
failed for that model.

- Both `SPONTANEOUS-RECENCY` → latest-binding-wins is **not** a wording artifact; **strengthens** the
  claim and bounds revision trigger 2; scope limit 4 tightened (spontaneous = also flag-not-directed).
- Both `COMMUTATIVE-HERE` → revision trigger 2 **fires**; the claim **narrows** to the
  explicit-reassignment frame; the Option-A positive is preserved but scoped.
- Split/mixed/uninterpretable → report per model; narrow to the surviving regime.

## Discipline

Independent pre-run critic GO (re-derive shortcut bounds; run fixtures; rule on whether dropping the
explicit flag changes what is tested in a way needing re-surfacing) **before** freeze; independent
post-run verifier after. Anti-retuning: the verdict map, DIRECT floor (0.80), SPONT bar (Wilson-95
LB > 0.25), and roster are frozen before any call; a collapse is as reportable as a persistence.

## Anchor & spend

`anchor: internal-contrast-only` (no human-comparison claim). 160 finding-bearing calls; pre-flight
≈ $0.10–0.13 (Option A billed $0.124444 for the identical call count); $0.50 per-run hard stop;
well inside the $5/day cap.
