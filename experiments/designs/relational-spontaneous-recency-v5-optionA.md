# Design — relational v5, Option A: spontaneous recency-weighting under mid-trajectory reassignment

**Run dir:** `experiments/runs/2026-06-16-relational-spontaneous-recency-a/`
**Decision:** `wiki/decisions/resolved/relational-v5-text-position-neutralization` (adopt-default,
B then A staged; C the binding fallback; anchor `internal-contrast-only`).
**Conjecture under test:** `wiki/findings/conjectures/commutative-convention`.
**Gate passed:** `wiki/findings/results/relational-stamp-comprehension-b` (Option B; both models
read the stamp on demand → both earn this Option-A arm).

## The question this arm isolates

v4 found both panel models follow physical text-position, not stamped chronology, in a
convention-recovery task; its binding caveat was *"position-following here is indistinguishable
from stamp-blindness."* Option B removed the stamp-blindness horn (both models read the round
stamp as a recency value **on demand**, 1.000). What remains open — and is the decisive
relational question — is **spontaneous** weighting: when the operative convention depends on
*which agreement is most recent*, but the query does **not** direct attention to recency, does a
model treat the most-recent agreement as operative (a **path-dependent, non-commutative**
convention) or treat the reassignment history as an order-insensitive content-set
(**commutative**)? This is exactly the conjecture's named falsification test ("reassign a coined
term mid-trajectory … test whether interpretation tracks *where* in the sequence the change
landed"), now with text-position neutralized by **balanced rotation** so chronology-following is
separable from text-position-following (binding carry-forward of the v4 confound).

## Instrument

A reference game: a grid of **K=4 clearly-distinct figures** (label + one-line description), and a
stamped history in which the coined term **`DAX`** is **reassigned** to the 4 figures across 4
**non-contiguous** rounds (drawn from frozen quadruples like `{2,4,7,9}`), **once each** so
frequency is flat. The history references a figure by its *description*; the answer space is the
figure *label* (matcher maps description→label via the grid — the v4 instrument class).

Two query conditions, each its **own** balanced-block roster:

- **SPONT (headline, 48 records/model).** *"Which of your figures does the term \"DAX\" refer
  to?"* — **no recency mention.** Latest-governs answer = max-round figure (`latest_rate`);
  min-round figure tracked as the anti-recency diagnostic (`first_rate`).
- **DIRECT (manipulation check, 32 records/model; 16 latest + 16 earliest).** B-style explicit
  recency query. Confirms on-demand comprehension survives in *this* instrument; gates whether a
  SPONT null is interpretable.

The INTRO framing is held **constant** across SPONT and DIRECT (the same neutral framing B used
and B proved both models read — it states stamp semantics and that the term was reassigned, but
never instructs the model to weight recency or to treat the latest agreement as operative). The
entire SPONT/DIRECT contrast lives in the **question**.

### Sample SPONT prompt (rid 0; latest-governs answer F3 @ round 9; min-round F8 @ round 2)

```
Your figures:
- F3: a crescent moon
- F4: a stack of three cubes
- F5: a single teardrop shape
- F8: a spiral seashell

Here is a record of how you and your partner used the term "DAX" for these figures over several
rounds. The term was reassigned: in different rounds you agreed it referred to different figures.
Each line is stamped with the round it was said in (a higher round number means it was said more
recently). The lines are NOT necessarily listed in round order:
- Round 9: we agreed "DAX" referred to a crescent moon.
- Round 4: we agreed "DAX" referred to a single teardrop shape.
- Round 2: we agreed "DAX" referred to a spiral seashell.
- Round 7: we agreed "DAX" referred to a stack of three cubes.

Question: Which of your figures does the term "DAX" refer to?
Reply with exactly one label (F3, F4, F5, F8) and nothing else.
```

## Shortcut-proofing (binding carry-forward 3)

Reuses the Option-B balanced-block construction over figures. Proven **at build** and on
**idealized-reader fixtures**, separately per subset: every constant-physical-history-slot
strategy scores **exactly 1/K**; every fixed figure-preference ordering (incl. grid order) scores
**exactly 1/K**; each figure appears exactly once per record (frequency flat). The fixtures
further certify the **verdict map**: only a genuine stamp-recency reader yields a `SPONTANEOUS-*`
verdict; every position/lexical/frequency reader is `COMMUTATIVE-HERE` (if it passes the on-demand
gate) or `UNINTERPRETABLE` (if not) — and a reader that *looks* spontaneous on SPONT but fails the
on-demand gate is held `UNINTERPRETABLE`, blocking a false positive.

## Deliberate, surfaced deviation: distinct figures, not v4 near-twins

The decision's Option-A *sketch* suggested keeping the v4 near-twin harvest class. This arm uses
**clearly-distinct** figures and **no** harvest, because near-twins would **confound** a recency
failure with a *discrimination* failure. Option A isolates spontaneous recency-weighting, so the
only hard step must be reading the stamp; shortcut-proofing comes from the balanced-block
construction, not near-twin difficulty (Option B was likewise ratified without near-twins). This
deviation is **flagged for the independent pre-run critic to rule on**; if dropping near-twins is
judged to change what Option A tests in a way needing re-surfacing, route accordingly rather than
weakening the task.

## Verdict map and conjecture reading

See `PREREG-draft.md`. `SPONTANEOUS-*` / `ORDER-SENSITIVE-MIXED` = order-sensitive ⇒ evidence
**against** commutativity (would move the conjecture toward falsification in the chronology
direction). `COMMUTATIVE-HERE` = the ratified narrow A-null ("comprehends recency on demand but
does not spontaneously weight it here") — never inflated; does not by itself certify the
commutative null; keeps the conjecture `proposed` with its inconclusiveness located.

## Anchor & spend

`anchor: internal-contrast-only` (no human-comparison claim). 160 finding-bearing calls; pre-flight
≈ $0.05–0.10; $0.50 per-run hard stop; well inside the $5/day cap.
