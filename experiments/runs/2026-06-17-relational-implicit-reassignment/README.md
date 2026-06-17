# 2026-06-17 — relational IMPLICIT-reassignment control (of Option A)

The **implicit-reassignment control** of `result/relational-spontaneous-recency-a` (Option A).
Option A found both panel models recover a **reassigned** coined term (`DAX`) by its **most-recent
binding**, spontaneously → `claim/relational-order-sensitive-reassignment`. That claim's sharpest
open caveat (scope limit 4 / revision trigger 2) is that "spontaneous" meant *query-not-directed,
not cue-free*: Option A's INTRO told the model the term *"was reassigned … in different rounds you
agreed it referred to different figures."*

**Question.** When a coined term simply **is** used for different figures across stamped,
non-contiguous rounds — with **no sentence flagging a reassignment** — and the matcher is asked
which figure the term refers to (no recency mention), does the model **still** spontaneously recover
the **most-recent** binding, or does removing the explicit flag collapse latest-binding-wins?

**The sole manipulation.** This run drops exactly one sentence from Option A's INTRO (the "was
reassigned" flag). The **frozen stimuli roster is byte-identical to Option A** (same `stimuli.json`
sha256 `432cb57d…`; the INTRO text is in `common.py`'s renderer, not the roster). Everything else —
figures, rounds, balanced-block geometry, query text, panel, parse, scoring, verdict map, DIRECT
gate — is held identical. A clean single-factor control.

```
Your figures:
- F3: a crescent moon
- F4: a stack of three cubes
- F5: a single teardrop shape
- F8: a spiral seashell

Here is a record of how you and your partner used the term "DAX" for these figures over several
rounds. Each line is stamped with the round it was said in (a higher round number means it was said
more recently). The lines are NOT necessarily listed in round order:
- Round 9: we agreed "DAX" referred to a crescent moon.
- Round 4: we agreed "DAX" referred to a single teardrop shape.
- Round 2: we agreed "DAX" referred to a spiral seashell.
- Round 7: we agreed "DAX" referred to a stack of three cubes.

Question: Which of your figures does the term "DAX" refer to?
Reply with exactly one label (F3, F4, F5, F8) and nothing else.
```
*(The Option-A SPONT prompt for the same record was identical except for an extra sentence after the
first: "The term was reassigned: in different rounds you agreed it referred to different figures.")*

**Verdict map** (frozen; carried verbatim from Option A): `SPONTANEOUS-RECENCY` /
`SPONTANEOUS-ANTI-RECENCY` / `ORDER-SENSITIVE-MIXED` = order-sensitive (non-commutative);
`COMMUTATIVE-HERE` = order-insensitive without the explicit flag; `UNINTERPRETABLE` = the DIRECT
manipulation check failed for that model. Pre-registered claim reading: both `SPONTANEOUS-RECENCY` →
the latest-binding-wins behaviour is **not** a wording artifact (strengthens the claim, bounds
revision trigger 2); both `COMMUTATIVE-HERE` → the claim **narrows** to the explicit-reassignment
frame (revision trigger 2 fires). See `PREREG.md`.

## Files
- `common.py` — instrument, panel, elicitation, cost ledger + hard stop (adapted from Option A; the
  ONE change is the IMPLICIT INTRO that drops the reassignment flag).
- `build_trials.py` — the two balanced-block rosters + at-build shortcut proofs (no API; unchanged).
- `fixtures/make_fixtures.py` — idealized-reader fixtures certifying the verdict map + shortcut
  bounds (no API; prompt-text-agnostic, so unchanged).
- `probe.py` — `liveness` / `full` (freeze-gated on `PREREG.md` + frozen sha256).
- `analyze.py` — the pre-registered verdict (no API; unchanged).
- `PREREG-draft.md` → `PREREG.md` — frozen only **after** an independent pre-run critic GO.
- `raw/` — JSONL per model + cost ledger + analysis.json.

## Status
Built; stimuli sha256 matches Option A; idealized-reader fixtures pass; **awaiting independent
pre-run critic GO** before freeze and any finding-bearing call.
