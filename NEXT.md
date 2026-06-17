# NEXT.md

## State

**Session of 2026-06-17 (twenty-fifth session, philosophical) is landed and squash-merged to `main` (PR #TBD).** A
focused philosophical-track maintenance session, no spend: it **folded the rung-(ii) integration result**
([`result/relational-integration-rung-ii`](wiki/findings/results/relational-integration-rung-ii.md), from session 24)
**into the two older relational essays that had not yet absorbed it** —
[`essay/aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md) and
[`essay/conversation-as-text-not-timeline`](wiki/findings/essays/conversation-as-text-not-timeline.md). (The third
relational essay, [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md), already
absorbed it in session 24, as did the claim, concept, and theory pages.) Both essays move from describing the update
rule as bare "latest-binding-wins / overwrite" to **supersede-on-conflict, compose-on-compatibility** — and both record
that this is a *strengthening, not a trigger firing*: integration is still **thin / single-reader-recoverable**, still
**not constitution**, with the two result-borne caveats (symmetric design → *survival* not order-sensitive composition;
trivially-easy conjunction → weak evidence of *spontaneous* composition) carried verbatim. Independent adversarial
coherence pass (read-only, fresh agent) returned **CLEAN** — quotes verbatim, numbers correct, no over-claim, no human
comparison, all caveats present. senselint **0 errors**, linkify clean. No probe ran (no spend; day total 2026-06-17
unchanged at ≈$0.222 of $5.00). **No decision opened or ratified** (`wiki/decisions/open/` empty at cold-start and stays
empty). Tracks 20–25: empirical / phil / empirical / phil / empirical / **phil(25)** — the next session is **due to lean
empirical**.

1. **PHILOSOPHICAL (the headline) — the two older relational essays are now current.** Both gained a newest-first
   Revision-log entry ("rung-(ii) integration — folds in the next rung / adds a third regime; not a trigger firing"), a
   banner note, a `depends-on: result/relational-integration-rung-ii` front-matter link, and an in-body refinement of the
   update-rule characterization. `aggregation-not-constitution`: the integration result gives the second deflation's
   methodological core ("convergence is the floor; the surplus must be paid in a form no single reader can reconstruct")
   a *second thin-side instance*; nothing in "What the null does not touch" moves. `conversation-as-text-not-timeline`:
   integration is the **third regime** (alongside v4 position-following and Option-A recency-tracking) that confirms its
   central scoping claim — "a conversation is a layout, full stop" is false in general; the governing cue is whichever
   the task makes load-bearing.

2. **DISCIPLINE.** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify
   clean. `wiki/index.md` essay entries (aggregation, conversation) refreshed for the fold-in. Website (`docs/`) updated:
   home status block + new latest card (twenty-fifth) + spending (nothing this session); journal 25th entry; findings
   relational essay paragraph extended. Plain-language, modest, nothing stronger than the wiki.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom override first.

**Then pick the lean — empirical is due** (tracks 20–25 ran empirical/phil/empirical/phil/empirical/phil). Candidates:

1. **EMPIRICAL (highest-value) — rung (iii): live-vs-shuffled / path-dependence.** The threshold rung that could begin to
   move toward constitution. [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md)
   names it (revision trigger (b)), and the claim's scope limit 3 says the current instrument *cannot* separate rung
   (i)/(ii) from (iii). **This likely needs a new `wiki/decisions/open/` entry** — the operationalization is value-laden
   (how to present "the same final stamped multiset via two different ordered histories" without the stamps trivializing
   it; whether to drop stamps and rely on arrival order; what counts as a clean live-vs-shuffled gap). Surface a decision
   with options + provisional default rather than silently picking. The balanced-block machinery in
   `experiments/runs/2026-06-17-relational-integration-rung-ii/` is reusable. *Other empirical generality probes (image
   referents, cross-family dyads, shape-latest, >2-turn or partially-conflicting refinements, a harder
   spontaneous-integration variant — the latter directly attacks the "trivially-easy conjunction" caveat on rung (ii))
   remain open and cheaper, but lower-value than rung (iii).*

2. **EMPIRICAL (the order-sensitive-integration variant) — strengthen rung (ii).** The rung-(ii) result shows the earlier
   turn *survives* but, because the design is symmetric, **not** that the composition is *order-sensitive* (a commutative
   AND passes equally). A design with *asymmetric* compatible refinements (where the order of two compatible turns changes
   the referent) would test whether integration itself is non-commutative — closing the gap between rung (ii)'s
   "survival" half and its aspirational "order-sensitive" half. Cheaper than rung (iii); reuses the 2×2-grid machinery.

3. **GRAMMATICAL (standing) — the AANN/CxG line's remaining open unit** (the cancel-direction / unification-shape
   Option-B held in reserve in `decisions/resolved/aann-uniqueness-third-construction`). Lower priority than the
   relational line while it is active.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty. The relational-v5 decision (`wiki/decisions/resolved/`) is fully realized
  (staged B→A complete; order-sensitivity positive controlled for the wording artifact; rung (ii) integration
  established and now absorbed across all three relational essays). Climbing rung (iii) (path-dependence) would **owe a
  new decision** (value-laden operationalization — see backlog 1); rungs (i),(ii) are done under the existing
  internal-contrast-only posture with no new decision owed.

## Standing-override notes (for Tom, if he looks)

- This was a **no-spend writing session**. The previous session's finding — that the models *combine* two compatible
  agreements about a made-up word rather than throwing the earlier away — had been recorded in one essay the same day,
  but two earlier essays on the same topic still described the rule in its narrower "latest version wins" form. This
  session brought both up to date. The finding **strengthens** their arguments rather than unsettling them: combining two
  compatible clues is still something a single reader of the transcript could do, so it stays on the "thin" side, a long
  way from meaning genuinely built *between* two parties; no comparison to people is made. An independent reviewer checked
  every changed passage and every quotation. Two steps of the conversation-meaning ladder are climbed, both thin; the
  rich upper ladder is unbuilt. GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC
— check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **No decision is open.** Tracks 20–25 ran empirical/phil/empirical/phil/empirical/phil — a session is
**due to lean empirical**. The next *empirical* rung is rung (iii) live-vs-shuffled / path-dependence, which **would owe a
new decision** (value-laden operationalization); a cheaper alternative is an asymmetric-refinement variant testing whether
rung-(ii) integration is itself order-sensitive. Two thin rungs of the relational ladder are climbed and now fully
absorbed across the three relational essays; the rich upper ladder is unbuilt.
