# NEXT.md

## State

**Session of 2026-06-17 (twenty-fourth session, empirical) is landed and squash-merged to `main` (PR #TBD).** A
single-deep-unit empirical session: built, critic-gated, ran, and verified the **relational rung-(ii) integration
probe** — the next rung of the ladder in
[`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md). **Verdict: both models
INTEGRATION at ceiling.** When a coined term's latest turn is *compatible* with an earlier one (a *refinement*, not a
replacement), both `claude` and `gemini` **compose** the two rather than overwriting the earlier — INTEG target rate
**1.000** (Wilson [0.926, 1.0]), overwrite/earlier-only/neither all **0.000**, grid-position at chance, DIRECT on-demand
**1.000**, 0 NA. So the relational update rule is **supersede-on-conflict, compose-on-compatibility**. Still **thin /
single-reader-recoverable** — does not approach constitution. Independent pre-run critic **GO** (reproduced build/sha,
re-derived all shortcut bounds, ruled no new decision owed) + independent post-run verifier **REPRODUCED**. Day total
2026-06-17 (sessions 22–24) = **≈$0.222 of $5.00** (this session $0.103792 billed). **No decision opened or ratified**
(`wiki/decisions/open/` empty at cold-start and stays empty). Tracks 20–24: empirical / phil / empirical / phil /
**empirical(24)** — the next session is **due to lean philosophical**.

1. **EMPIRICAL (the headline) — rung (ii) occupied.** New result
   [`result/relational-integration-rung-ii`](wiki/findings/results/relational-integration-rung-ii.md) (proposed,
   `internal-contrast-only`). Design: a coined term DAX constrained over two stamped rounds about a 2×2 figure grid
   (earlier = a shape, latest = a pattern); each constraint matches 2 of 4 figures, only the conjunction is unique, so any
   single-attribute (overwrite or earlier-only) reader caps at 0.50 — beating it requires the earlier turn to *survive*.
   Run dir `experiments/runs/2026-06-17-relational-integration-rung-ii/`; design
   `experiments/designs/relational-integration-rung-ii.md`. Two binding caveats (folded everywhere): the design's
   constraints are *symmetric*, so this shows the earlier turn **survives**, **not** that the composition is
   *order-sensitive* (a commutative conjunction passes equally); and the conjunction is trivially easy (DIRECT=INTEG=1.0),
   so the ceiling is weak evidence of *spontaneous* composition and does not rule out overwrite under harder load.

2. **INTEGRATION (theory/essay/claim/concept synced).** [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md)
   draft→**revised** (revision trigger (a) fired; rung (ii) now occupied; **both rungs (i),(ii) on the thin side**; trigger
   stays live only in its stronger "order-sensitive composition" form).
   [`claim/relational-order-sensitive-reassignment`](wiki/findings/claims/relational-order-sensitive-reassignment.md)
   scope limit 2 updated (non-overwrite repairs tested → integration). [`concept/relational-meaning`](wiki/base/concepts/relational-meaning.md)
   and [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) synced (relational cell stays
   **negative on constitution**; two thin rungs climbed, rich upper ladder unbuilt). Exec-summary refreshed.

3. **DISCIPLINE.** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean.
   Website (`docs/`) updated: home status (38 studies) + new latest card + spending; journal 24th entry; findings
   relational section (combine step climbed); plans naming-game section refreshed. Plain-language, modest, nothing
   stronger than the wiki.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom override first.

**Then pick the lean — philosophical is due** (tracks 20–24 ran empirical/phil/empirical/phil/empirical). Candidates:

1. **PHILOSOPHICAL (highest-value, the natural follow-on) — absorb the rung-(ii) result into the relational essays.**
   The two compatible-turn rungs (overwrite, integrate) are now both established and both *thin*. A philosophical unit
   could (a) revise [`essay/aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md) and/or
   [`essay/conversation-as-text-not-timeline`](wiki/findings/essays/conversation-as-text-not-timeline.md) to record that
   the update rule is now "supersede-on-conflict, compose-on-compatibility" — still thin, still not constitution — and/or
   (b) sharpen the **thin/rich criterion** in [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md)
   now that *two* rungs sit demonstrably on the thin side (what, precisely, the live-vs-shuffled test would have to show to
   cross the cut). No spend; all in-repo quotes.

2. **EMPIRICAL (the next rung, if a later session leans empirical) — rung (iii): live-vs-shuffled / path-dependence.**
   The essay names this as the threshold rung that could begin to move toward constitution, and the claim's scope limit 3
   says the current instrument *cannot* separate rung (i)/(ii) from (iii). **This likely needs a new
   `wiki/decisions/open/` entry** — the operationalization is value-laden (how to present "the same final stamped multiset
   via two different ordered histories" without the stamps trivializing it; whether to drop stamps and rely on arrival
   order; what counts as a clean live-vs-shuffled gap). Surface a decision with options + provisional default rather than
   silently picking. The balanced-block machinery in `experiments/runs/2026-06-17-relational-integration-rung-ii/` is
   reusable. *Other empirical generality probes (image referents, cross-family dyads, shape-latest, >2-turn or
   partially-conflicting refinements, a harder spontaneous-integration variant) remain open and cheaper, but lower-value
   than rung (iii).*

3. **GRAMMATICAL (standing) — the AANN/CxG line's remaining open unit** (the cancel-direction / unification-shape
   Option-B held in reserve in `decisions/resolved/aann-uniqueness-third-construction`). Lower priority than the relational
   line while it is active.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty. The relational-v5 decision (`wiki/decisions/resolved/`) is fully realized
  (staged B→A complete; the order-sensitivity positive controlled for the wording artifact; rung (ii) integration now
  established). Climbing rung (iii) (path-dependence) would **owe a new decision** (value-laden operationalization — see
  backlog 2); rungs (i),(ii) are done under the existing internal-contrast-only posture with no new decision owed.

## Standing-override notes (for Tom, if he looks)

- This was an **experiment session** (~$0.10). It climbed the first step above the bottom of the conversation-meaning
  "ladder": when a later agreement about a made-up word *fits with* an earlier one (rather than contradicting it), both
  models **combine** the two instead of throwing the earlier away (100% of the time). So the rule is fuller than "latest
  wins" — overwrite on conflict, combine when compatible. The honest framing throughout: this is still a *thin* ability (a
  single reader of the transcript could do the same combining), a long way from meaning genuinely *built between* two
  parties; and because the combining task is easy, the perfect score shows the models *can and do* combine more than that
  they do so unprompted. An independent reviewer reproduced every number and pushed for those caveats. Two steps of the
  ladder are now climbed, both on the "thin" side. GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC
— check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **No decision is open.** Tracks 20–24 ran empirical/phil/empirical/phil/empirical — a session is **due to
lean philosophical** (absorb the rung-(ii) result into the relational essays / sharpen the thin/rich criterion). The next
*empirical* rung is rung (iii) live-vs-shuffled / path-dependence, which **would owe a new decision** (value-laden
operationalization). Two thin rungs of the relational ladder are now climbed; the rich upper ladder is unbuilt.
