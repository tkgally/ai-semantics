---
id: relational-fetchable-anchor
title: May the Hawkins tangrams corpus be committed as the in-repo human convergence baseline for the relational pilot?
status: resolved
opened: 2026-05-31
opened-by: orchestrator
resolved: 2026-05-31
resolved-by: Tom (ratified, this round)
contingent-artifacts:
  - open-question/relational-meaning-pilot
---

# Decision: a web-fetchable human anchor for the relational pilot

## Resolution (2026-05-31, Tom)

**Ratified — Option A.** Tom (this round, decision 2): *"relational-fetchable-anchor — Option A:
catalog the Hawkins tangrams corpus under the DWUG/Lancaster recipe-not-corpus posture (commit
recipe + derived/aggregate tables only, gitignore raw). Move to resolved; it unblocks an
entrainment baseline for the relational pilot when you get to it."* So the Hawkins/Stanford
tangrams corpus (`hawkrobe/tangrams`, `data/tangrams.csv`) **may** be catalogued as a typed
`resource` under the conservative recipe-not-corpus posture (download recipe + sha256 + derived
aggregate entrainment tables committed; raw corpus gitignored, **not** redistributed), and a
relational *result* may later anchor its human convergence/entrainment baseline to it. **Brennan &
Clark 1996** ("Conceptual pacts") is added to [`base/wanted.md`](../../base/wanted.md) alongside
Clark & Wilkes-Gibbs 1986 (the ratified theoretical anchor, still unfetched). This unblocks the
relational entrainment baseline; the live-vs-shuffled trajectory-dependence measure (novel to the
LLM probe) is still not anchored by Hawkins, and "Decision 9" (the two-AI experiment) is still
untaken — so the pilot remains queued, now with a fetchable human baseline available.

---

# Decision: a web-fetchable human anchor for the relational pilot (original framing, retained)

## Why this exists (the ratified anchor is unfetchable; a fetchable substitute was found)

The relational pilot's ratified empirical anchor — Clark & Wilkes-Gibbs 1986
([`decisions/resolved/relational-anchor-shortlist`](relational-anchor-shortlist.md)) —
is **not in the repo** and Tom can't fetch it for a few days (decision 4). Tom asked (decision 3c) to
scout **web-fetchable** alternative human anchors so the relational groundwork is not blocked. The
scouting ([`experiments/notes/relational-axis-literature.md`](../../../experiments/notes/relational-axis-literature.md))
found a strong fetchable candidate but with a **license gap**, so the use-it-or-not call is surfaced.

## Finding (verified by direct repo inspection, 2026-05-31)

- **Hawkins/Stanford tangrams (`hawkrobe/tangrams`) — STRONGEST fit.** `data/tangrams.csv` confirmed
  **HTTP 200, 3.13 MB**, carrying ordered per-dyad referring-expression histories
  (`gameid, repetitionNum, role, contents, correct, numRawWords`) — exactly the entrainment-curve /
  trajectory-dependent convergence signal the pilot's bottom rung (live-vs-shuffled history) needs.
  **License gap:** GitHub `license: null`, no LICENSE file; only the paper's "We release an open
  corpus" statement. (Hawkins, Frank & Goodman 2020; arXiv abstract verbatim in the note.)
- **PhotoBook (Haber 2019) — STRONG, visually grounded**, public unrestricted downloads, 2,500
  dialogues / 164,615 utterances; same `license: null` gap; complementary (larger N, touches
  `grounded.perceptual`), looser fit for a *minimal* pilot.

## The question

May the project commit the Hawkins tangrams corpus as a typed `resource` (the in-repo human
convergence baseline) given it has no SPDX license, only the authors' published "open corpus"
release statement — supplementing the ratified-but-unfetchable C&W-G 1986?

## Options

- **A (provisional default) — Yes, under the DWUG/Lancaster posture.** Catalog it as a typed
  `resource` for read/compare under academic-research norms + the published release statement; **do
  not redistribute the raw data** (gitignore it; commit only the recipe + derived/aggregate
  entrainment tables, exactly as done for DWUG and the Lancaster norms). Unblocks the entrainment
  baseline now; license posture is conservative (no redistribution).
- **B — Hold for explicit author license confirmation** (email) before committing anything.
- **C — Wait for the ratified C&W-G 1986 fetch** and keep the relational axis fully blocked.

## Provisional default

**Option A** — the recipe-not-corpus posture keeps the wiki license-clean regardless, and an "open
corpus" release statement + non-redistribution is the same standard the project already applies to
CC BY-ND DWUG. **Non-blocking for design work** (the pilot design proceeds either way); this gates
only whether a *result* may later anchor to Hawkins. Secondary: add **Brennan & Clark 1996**
("Conceptual pacts") to [`base/wanted.md`](../../base/wanted.md) alongside C&W-G. Tom: a one-liner is
enough.
