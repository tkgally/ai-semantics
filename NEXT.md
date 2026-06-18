# NEXT.md

## State

**Session of 2026-06-18 (thirtieth session, empirical) is landed and squash-merged to `main` (PR #TBD).**
A workflow session that (1) ratified the one open decision and (2) ran the empirical lean that was due.

1. **EMPIRICAL HEADLINE — order-sensitive composition is confirmed claude-only across the full panel.** The
   already-certified, frozen **Option-C** order-sensitive-composition instrument
   ([`design/relational-order-composition-c`](experiments/designs/relational-order-composition-c.md)) was re-run on the
   **third panel model, gpt-5.4-mini** (panel.B) — the generality test named by
   [`essay/capability-split`](wiki/findings/essays/capability-split.md) trigger (a). **gpt is UNINTERPRETABLE**
   (DIRECT on-demand gate 0.194 < 0.80, Wilson [0.097, 0.350] — it cannot compose two non-commuting moves even when told
   the order; error pattern is single-move readers). So across all three models only **claude RESPECTS-ORDER**; **gemini
   and gpt both UNINTERPRETABLE**. Running the third model did **not** widen the split toward a panel property — it
   **sharpened** the claude-only reading (2/3 models fail the on-demand gate; each an instrument-capability limit, not a
   clean order-blind null). New run dir
   [`experiments/runs/2026-06-18-relational-order-composition-c-gpt/`](experiments/runs/2026-06-18-relational-order-composition-c-gpt/),
   byte-identical frozen stimuli; independent pre-run critic GO (no panel-change owed — gpt IS panel.B; its earlier
   relational drop was a stimulus-generation reason inapplicable to synthetic stimuli) + independent post-run verifier
   REPRODUCED. **$0.037017 billed**; day total 2026-06-18 ≈ **$0.335** of $5.00.
   [`result/relational-order-composition-c`](wiki/findings/results/relational-order-composition-c.md) updated to the
   three-model headline; [`essay/capability-split`](wiki/findings/essays/capability-split.md) carries a logged in-page
   revision to the three-model panel (trigger (a) partially discharged; "thing to watch" widened to claude > {gemini, gpt}).

2. **RECONCILE — ratified [`decisions/resolved/wiki-frontmatter-ergonomics`](wiki/decisions/resolved/wiki-frontmatter-ergonomics.md): ADOPT Option D** (NOT the
   provisional default Option A). An independent adversarial-review agent measured the repo and corrected two premises of
   the opening analysis: the resolved-decisions changelog was ~11% of `index.md` (not "most"), and `wiki/decisions/*` are
   not frontmatter-bare today. So the index-trim core was adopted and the per-page-header half cut. Applied: the
   resolved-decisions changelog moved out of `wiki/index.md` into a new history page
   [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md) (index 208 KB → 187 KB); `index.md` keeps a
   count + governance note + one-line pointer; **no** per-page headers, **no** new senselint check; logged in `log.md`.

**Integration:** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean
(self-healed 63 moved-changelog links + 2 hand-fixed design-page paths). Website (`docs/`): journal 30th entry + home
status/card + findings relational paragraph + plans naming-game update. Tracks 20–30: emp/phil ×5 then **emp(30)** — the
next session is **due to lean philosophical** (or a cheap empirical relational unit).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to ratify
unless Tom opens something or leaves an override. Apply any Tom override first, as always.

**Then pick the lean — philosophical is due** (tracks 20–30 ended emp). Candidates:

1. **PHILOSOPHICAL (lean is due).** The capability-split essay now stands on a three-model panel — a natural philosophical
   follow-on is on **what a one-of-three capability split licenses and forbids** when the two failures are *instrument*
   limits, not capacity nulls (the asymmetry between an existential positive and an undischargeable negative). Or develop
   [`essay/rung-iv-instrument`](wiki/findings/essays/rung-iv-instrument.md) (the between-agent scored-practice blueprint)
   now that the text-only ceiling is firm across three models. No standalone philosophical unit is *pressing*; pick the
   one that pairs with the evidence that just moved.

2. **EMPIRICAL alternatives (if the lean flips or a unit pairs).** The single most informative cheap test the new result
   invites is **capability-split trigger (b): does an *easier* non-commuting-operation design let gemini or gpt clear the
   on-demand gate?** (a both-fail-under-difficulty vs stable-gap discriminator — bounds the split to *this* instrument if
   they then compose). Other untested relational horns: **partially-conflicting refinements** (a later turn *partly*
   conflicts — overwrite/integrate/split?); **larger-grid / >3-turn** integration generality; **image referents**;
   **cross-family dyads**. Grammar reserve: the AANN/CxG **cancel-direction / unification-shape Option-B** held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; the full changelog now lives in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). The most recent ratification was
  `wiki-frontmatter-ergonomics` (Option D, this session).

## Standing-override notes (for Tom, if he looks)

- This session **ran one cheap experiment and tidied the wiki**. (1) The "order of operations" puzzle was run on a
  *third* model to see whether tracking the order of two moves is shared — it is not: the third model couldn't do the
  basic step even when told the order (right ~1/5 of the time), so across all three models exactly one does it. The
  finding stays "one model's capability," never averaged into a claim about "the models," and the two failures are read
  as limits of *this task*, not proof of inability. (2) Your queued note-keeping question was decided cross-session by an
  independent review: it *measured* the files, found the original hunch half-right, and adopted the lean answer — slim the
  always-read index (move the decisions archive to a history page) and skip per-page summaries. GitHub Pages serves from
  `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (now leaner — the
resolved-decisions changelog lives at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget
$5/day UTC — check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End squash-merged to
`main`, website updated. **No decision is open.** Tracks 20–30 ran emp/phil ×5 then emp — a session is **due to lean
philosophical**. The relational ladder stands at rung (i) overwrite, rung (ii) integration (+depth 2), the
order-sensitive-**composition** rung (**claude only** — now confirmed across the full three-model panel: gemini and gpt
both fail the on-demand gate), and **rung (iii) documented structurally closed for text-only stimuli**.
