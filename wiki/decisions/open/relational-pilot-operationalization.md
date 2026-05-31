---
id: relational-pilot-operationalization
title: Are the relational-pilot v1 operationalization choices (text-grid referents; order-isolating ordered-vs-shuffled; monologue floor) the right yardstick?
status: open
opened: 2026-05-31
opened-by: orchestrator
contingent-artifacts:
  - result/relational-reference-game-v1
---

# Decision: relational pilot v1 operationalization

## Why this exists (surfaced, not auto-resolved)

`decisions/resolved/relational-pilot-go` ("Decision 9", GO) ratified **what** to run — the two-AI
iterated dyadic reference game, homogeneous dyads first, with the live-vs-shuffled trajectory
contrast as the load-bearing measure and Hawkins as the convergence anchor only. Building it forced
three **operationalization** calls that the GO decision did not fix. Per PROTOCOL §A/§5 and CLAUDE.md
always-on rule 5, these are surfaced here with a provisional default and the result
(`result/relational-reference-game-v1`) is
marked `contingent-on` this page; none is auto-promoted to settled until Tom ratifies the yardstick.
Ratifying fixes the *yardstick*, never the *result*.

## The three choices (provisional defaults taken; alternatives named)

### Q1 — Referent modality: text-grid vs image tangrams

- **Default taken (A):** 6 abstract referents rendered as 8×8 `#`/`.` text grids, generated
  deterministically (`build_figures.py`, frozen sha256 in PREREG), as 3 confusable near-twin pairs.
- **Why:** the shuffle control demands the prior turns be reorderable as **byte-identical** content,
  and this is the most call-heavy probe to date (every round = a fresh generation for both agents on a
  growing history) — text keeps the shuffle exact and the per-call token cost bounded. A director
  word-budget (≤12 words) blocks exhaustive cell-listing, forcing the holistic coined label the
  paradigm needs.
- **Alternative (B):** real image tangrams (the panel is image-capable). Higher ecological validity
  and a closer tie to `resource/hawkins-tangrams`, but multiplies image-token cost on every turn and
  complicates exact content-holding for the shuffle.
- **Known risk:** if text grids are too easy to describe literally within the budget, the live game
  runs at ceiling and the trajectory test loses sensitivity. The PREREG flags a ceiling outcome as
  **under-powered**, not as a relational result.

### Q2 — The load-bearing contrast: design-named "live vs shuffled" vs order-isolating "ordered-replay vs shuffled-replay"

- **Default taken (A):** report BOTH, but treat **ordered-replay vs shuffled-replay** (both arms a
  fresh one-shot matcher; only the order of an identical record differs) as the **headline**
  de-confounded number. The design's literal "live-B vs shuffled-fresh-B" contrast confounds *order*
  with *incremental self-generated exposure* (live-B built the convention online and produced the
  feedback), so it is reported but not headlined.
- **Why:** this is a sharpening *toward* a cleaner order isolation, not a retune toward a positive —
  it was fixed in the PREREG before any finding-bearing call, and it makes the deflationary null
  *easier* to obtain (a fresh ordered matcher has no online-exposure advantage), not harder.
- **Alternative (B):** take the design's literal live-vs-shuffled as the headline. Rejected as
  confounded, but kept in the record.

### Q3 — Bar (b) floor: single-agent-with-self as monologue

- **Default taken (A):** the open question's "single-agent-with-self baseline" is operationalized as a
  **no-partner, no-feedback monologue** (same model labels each figure over R passes), with the same
  ordered/shuffled probe re-run on the monologue records. A relational reading requires the **dyadic**
  ordered−shuffled gap to *exceed* this monologue gap.
- **Why:** in homogeneous dyads both roles are already the same model, so the meaningful floor is "how
  much order-dependence arises with no genuine interactive feedback loop at all." Monologue records
  lack feedback-driven repairs, so they carry less trajectory information by construction — the
  correct floor.
- **Alternative (B):** one agent literally plays both roles in a self-dialogue with self-generated
  feedback. Closer to the literal phrase but reintroduces the feedback loop the floor is meant to
  remove.

## Provisional default and contingency

Run v1 under A/A/A (above), freeze + report, and mark
`result/relational-reference-game-v1`
`contingent-on: relational-pilot-operationalization`. The **trajectory-dependence measure makes no
human-comparison claim** — it is the pilot's own within-model internal contrast (the open question and
the GO decision both state Hawkins anchors the *convergence* baseline only), so the result carries an
`anchors` link to `resource/hawkins-tangrams` for the entrainment curve and is otherwise an internal
contrast. A v1 positive would be held contingent (a candidate relational `conjecture`, not a settled
finding) until Tom ratifies this yardstick; a v1 null stands as a first-class negative regardless of
this decision (a null does not over-claim).

## Recommended resolution

**Default A on all three** (text grids; order-isolating headline; monologue floor) for the *pilot*,
with **Q1→B (image tangrams)** as the natural v2 upgrade if v1 shows headroom and a non-null signal,
and the **perturbation arm** (deferred in v1) as the sharper v2 trajectory test.
