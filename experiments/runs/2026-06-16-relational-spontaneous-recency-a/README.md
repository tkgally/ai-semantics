# 2026-06-16 — relational spontaneous-recency arm (Option A)

The **Option A** arm of the ratified relational-v5 decision
(`decisions/resolved/relational-v5-text-position-neutralization`, adopt-default: B then A,
staged; C the binding fallback). Both panel models passed the Option-B stamp-comprehension gate
(`result/relational-stamp-comprehension-b`), so A is warranted.

**Question.** When a coined term (`DAX`) is **reassigned** to different figures across stamped,
non-contiguous rounds — with physical line-position neutralized by balanced rotation — does a
model **spontaneously** weight the round stamp (treat the most-recent agreement as operative: a
*path-dependent / non-commutative* convention) when asked which figure the term refers to,
*without the query mentioning recency*? Or does it treat the history as an order-insensitive
content-set (*commutative*)? This is the decisive test
`conjecture/commutative-convention` names, with v4's text-position confound removed.

**Design in one line.** Two balanced-block rosters per model — **SPONT** (48 records; headline; no
recency in the query) and **DIRECT** (32 records; B-style explicit-recency manipulation check) —
built so that every position strategy, every figure-preference ordering, and the frequency
heuristic all score **exactly 1/K = 0.25** (proven at build and on idealized-reader fixtures), so
only spontaneously reading the stamp can clear the SPONT order-sensitivity bar (Wilson-95 LB >
0.25) or the DIRECT floor (0.80). `anchor: internal-contrast-only`.

**Verdict map** (frozen; see PREREG): `SPONTANEOUS-RECENCY` / `SPONTANEOUS-ANTI-RECENCY` /
`ORDER-SENSITIVE-MIXED` = order-sensitive (non-commutative); `COMMUTATIVE-HERE` = the narrow
A-null ("comprehends recency on demand but does not spontaneously weight it here");
`UNINTERPRETABLE` = the DIRECT manipulation check failed for that model.

## Files
- `common.py` — instrument, panel, elicitation, cost ledger + hard stop (adapted from the B run).
- `build_trials.py` — the two balanced-block rosters + the at-build shortcut proofs (no API).
- `fixtures/make_fixtures.py` — idealized-reader fixtures certifying the verdict map + shortcut
  bounds before any model is queried (no API; the v4 GO-discipline).
- `probe.py` — `liveness` / `full` (freeze-gated on `PREREG.md` + frozen sha256).
- `analyze.py` — the pre-registered verdict (no API).
- `PREREG-draft.md` → `PREREG.md` — frozen only **after** an independent pre-run critic GO.
- `raw/` — JSONL per model + cost ledger + analysis.json.

## Status
Built; idealized-reader fixtures pass; **awaiting independent pre-run critic GO** before freeze
and any finding-bearing call. If the task cannot be certified shortcut-proof, route to Option C
(do not weaken the task).
