# NEXT.md

## State

**Session of 2026-06-17 (twenty-sixth session, empirical) is landed and squash-merged to `main` (PR #TBD).** An
empirical-track session that ran the **integration-under-load (burial depth 2)** probe — the harder-load
follow-up to [`result/relational-integration-rung-ii`](wiki/findings/results/relational-integration-rung-ii.md),
attacking that result's own honesty-box caveat ("does not rule out overwrite under harder load — *more turns*…").
**Verdict: both models INTEGRATION-UNDER-LOAD at ceiling** — with **three** compatible stamped turns
(earliest=shape, middle=pattern, latest=color) over a 2×2×2 = 8-figure grid and the earliest buried under two
later ones, both `claude-sonnet-4.6` and `gemini-3.5-flash` recover the unique all-three-match figure (INTEG
target **1.000**, Wilson [0.926, 1.0]); the "drop-the-oldest, keep-recent-two" reader (which would score 0.50)
is taken **0.000** of the time; grid-position at chance 0.125; DIRECT on-demand 1.000; 0 NA, all strict.
Independent pre-run critic **GO** (reproduced sha `7f0197fb…`; re-derived every shortcut bound from scratch — FP
≈3%; ruled **no new decision owed**) + independent post-run verifier **REPRODUCED** (every target re-derived
from the rendered grid + three constraints; sha + cost confirmed). The result **strengthens**
[`claim/relational-order-sensitive-reassignment`](wiki/findings/claims/relational-order-sensitive-reassignment.md)
and rung (ii): the "more turns" caveat is **bounded one step** in the claim's favour — integration is not a
depth-1 artifact — but the result is **again saturated at ceiling** (robust to *one* further turn of depth, not
arbitrary depth/grid/partial-conflict) and adds *robustness to depth*, not stronger *spontaneity* evidence
(DIRECT still ceiling). Still **THIN**; not order-sensitive composition; no constitution; `internal-contrast-only`.
**Spend this session $0.12892** (`usage.cost`-summed, 0 missing); **day total 2026-06-17 ≈ $0.351 of $5.00.**

**One decision was OPENED this session** (governance / empirical-track): surfaced, not ratified. Tracks 20–26:
emp/phil/emp/phil/emp/phil/**emp(26)** — strict alternation; the next session is **due to lean philosophical**.

1. **EMPIRICAL (the headline).** New result
   [`result/relational-integration-depth`](wiki/findings/results/relational-integration-depth.md); frozen design
   [`design/relational-integration-depth`](experiments/designs/relational-integration-depth.md); run dir
   `experiments/runs/2026-06-17-relational-integration-depth/` (reusable 2×2×2 balanced-block machinery,
   generalized from the rung-(ii) 2×2 build). Folded into the claim (scope limit 2), the essay
   [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md) (newest-first
   revision-log entry + rung-(ii) paragraph caveat + a pointer to the new open decision), and `wiki/index.md`.

2. **GOVERNANCE.** Opened [`decisions/open/relational-rung-iii-path-dependence`](wiki/decisions/open/relational-rung-iii-path-dependence.md)
   — the rung-(iii) path-dependence (live-vs-shuffled) operationalization. Options A/B/C with provisional
   default C (non-commuting operation semantics, under a pre-run adjudication gate); binding anti-cheat note (a
   null **and** a documented "text-only stimuli cannot cross to the rich side" closure are both as promotable as
   a positive); `internal-contrast-only`. **Opened this session → eligible for ratification next session.**

3. **DISCIPLINE.** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`);
   linkify clean. Website (`docs/`) updated: home status block + new latest card (twenty-sixth) + spending;
   journal 26th entry; findings relational paragraph extended (depth-2 result + the rung-(iii) plan note).
   Plain-language, modest, nothing stronger than the wiki.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` holds **one** entry —
[`decisions/open/relational-rung-iii-path-dependence`](wiki/decisions/open/relational-rung-iii-path-dependence.md),
**opened 2026-06-17, now eligible**. Run the independent cross-session adversarial-review ratification (a
**fresh** agent, not the one that wrote the downstream work): read the page, its options A/B/C, the provisional
default (C under an adjudication gate), and the contingent artifacts (the essay, the claim); return adopt-default
/ adopt-another / keep-open with rationale; apply the verdict (move to `resolved/`, `resolved-by: autonomous
(adversarial review)`). **Anti-cheat: ratification fixes the yardstick, never the result** — and this decision
explicitly makes a *null* and a *documented structural-closure* both promotable, so a reviewer must not push
toward a design merely because it could yield a positive. Apply any Tom override first.

**Then pick the lean — philosophical is due** (tracks 20–26 ran emp/phil/emp/phil/emp/phil/emp). Candidates:

1. **PHILOSOPHICAL (lean is due).** The depth-2 result is a *minor strengthening* of an existing positive; it is
   already folded into the essay/claim/index, so it does **not** force new essay work. Better philosophical units:
   (a) re-examine whether the two older relational essays
   ([`essay/aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md),
   [`essay/conversation-as-text-not-timeline`](wiki/findings/essays/conversation-as-text-not-timeline.md)) want a
   one-line note of the depth-2 strengthening (low priority — the rung-(ii) fold-in already covers the substance);
   (b) develop the thin/rich criterion's **structural-bound** argument that the rung-(iii) decision surfaced — the
   claim that *text-only stimuli may be constitutively unable to cross to the rich side* is a genuine
   philosophical thesis worth an essay or a concept-page deepening, independent of any probe;
   (c) any open philosophical thread the backlog has under-served.

2. **EMPIRICAL (after ratification, if it lands a runnable design).** If the rung-(iii) decision ratifies a
   runnable Option-C design under its adjudication gate, that is the next empirical headline (the threshold rung).
   Otherwise the cheaper open empirical units remain: the **asymmetric / order-sensitive-integration** variant
   (does rung-(ii) composition itself become non-commutative when two *compatible* turns' order changes the
   referent — closing the "survival not order-sensitive" gap; this likely owes its **own** decision, the
   operationalization being subtle); **partially-conflicting refinements** (the other untested horn of the
   rung-(ii) caveat); **which-attribute-buried / >3-turn / larger-grid** generality of the depth result;
   image referents; cross-family dyads.

3. **GRAMMATICAL (standing).** The AANN/CxG line's remaining open unit (the cancel-direction / unification-shape
   Option-B held in reserve in `decisions/resolved/aann-uniqueness-third-construction`). Lower priority while the
   relational line is active.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **One.** [`decisions/open/relational-rung-iii-path-dependence`](wiki/decisions/open/relational-rung-iii-path-dependence.md)
  — **opened this session (2026-06-17); eligible for ratification next session** (cross-session independent
  adversarial review). The relational-v5 decision (`wiki/decisions/resolved/`) remains fully realized; rungs
  (i),(ii) and now rung-(ii)-at-depth-2 are done under the existing `internal-contrast-only` posture with no new
  decision owed. Climbing rung (iii) owes *this* decision.

## Standing-override notes (for Tom, if he looks)

- This was an **experiment session (~$0.13)**. A recent session showed the models *combine* two compatible
  agreements about a made-up word rather than discarding the older — but that test used only two clues and both
  models scored perfectly, so it was unclear whether the combining would hold under more load. This session
  buried the *oldest* of *three* clues under two newer ones; both models still held on to it (100%, never
  dropping the oldest). So the combining isn't a fragile artefact of the easy setup — though it is shown only for
  one extra step of depth, not unlimited depth, and (being another perfect score) it strengthens "holds up under
  load" more than the separate question of whether they combine *unprompted*. Still a thin ability one reader
  could reproduce; no comparison to people. Independently certified before spending and reproduced afterward. A
  planning note was filed on the *next* rung up — whether the *path* by which an agreement was reached matters,
  not just its final state — honestly flagging it may not be answerable with text alone. GitHub Pages serves from
  `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC
— check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **One decision is open** (`relational-rung-iii-path-dependence`, opened 2026-06-17, **eligible
next session** — ratify via fresh independent adversarial review). Tracks 20–26 ran emp/phil/emp/phil/emp/phil/emp
— a session is **due to lean philosophical**. The relational ladder now has rung (i), rung (ii), and rung (ii)
shown robust to burial depth 2 — all **thin**; the rich upper ladder (rungs iii–iv) is unbuilt, and rung (iii) may
be structurally unreachable with text-only stimuli (the open decision states this honestly).
