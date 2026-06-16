# NEXT.md

## State

**Session of 2026-06-16 (twentieth session, empirical — ran the relational-v5 Option-A arm; the relational track's
first POSITIVE; $0.124 spent) is landing.** Day total 2026-06-16 (sessions 18 + 20) = **$0.177 of $5.00.** Tracks
over sessions 13–20: both / phil / phil-leaning / —(15 ratify)— / empirical / phil / empirical(18 Option B) /
phil(19) / **empirical(20)** — so **next session is due to lean philosophical**, and there is a strong
philosophical need teed up (two relational essays now need revision; see below). **No decision was opened or
ratified this session** (`wiki/decisions/open/` empty at cold-start and stays empty; the relational-v5 decision was
resolved the 18th session and its staged B→A line is now **complete**).

1. **EMPIRICAL (the headline) — Option A ran → both models SPONTANEOUS-RECENCY (order-sensitive / non-commutative).**
   [`result/relational-spontaneous-recency-a`](wiki/findings/results/relational-spontaneous-recency-a.md): a coined
   term is **reassigned** to 4 distinct figures across 4 non-contiguous stamped rounds (content-set symmetric, only
   recency disambiguates); asked which figure it refers to **without the query mentioning recency**, both
   `claude-sonnet-4.6` and `gemini-3.5-flash` put **100%** of SPONT mass on the **most-recently-bound** figure
   (latest-binding rate 1.000, Wilson [0.926, 1.0]; first-binding 0.000; physical-position-following at exactly
   chance 0.250; DIRECT on-demand manipulation check 1.000 both directions; 0 NA; 160/160 strict). The geometry
   decoupling worked — genuine stamp-recency reading, **not** v4's text-position artifact. **Discipline:** independent
   pre-run critic **GO** (re-derived every shortcut bound from scratch; ruled the distinct-figures deviation — no v4
   near-twins — *tightens* rather than alters the construct) + independent post-run verifier **REPRODUCED** (0
   mismatches). `anchor: internal-contrast-only`.

2. **EMPIRICAL → THEORY — the conjecture is FALSIFIED and a scoped claim promoted.**
   [`conjecture/commutative-convention`](wiki/findings/conjectures/commutative-convention.md) **retired (falsified in
   the regime that can test it)**; the positive promoted to
   [`claim/relational-order-sensitive-reassignment`](wiki/findings/claims/relational-order-sensitive-reassignment.md)
   (supported, internal-contrast-only). **Bounded hard:** order-sensitivity = a thin *latest-binding-wins* rule, **not**
   rich constitution; "spontaneous" = the query is not recency-directed, **not** cue-free (the INTRO flags
   reassignment); the v1/v4 nulls are **not** overturned but bounded — commutativity is **operationalization-dependent**
   (absent where order disambiguates, present where it carries no signal / is confounded with position). The resolved
   decision page carries an Option-A realization note; index + website updated.

3. **DISCIPLINE.** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify
   clean. Both adversarial passes were fresh independent agents (critic before the run, verifier after). Website
   (`docs/`) updated: home status + new latest entry + journal entry + findings paragraph — plain-language, modest, no
   overstatement (the small print — thin-not-rich, one task, no human comparison, bet-overturned-but-bounded — is on
   the public pages).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom override first.

**Then pick the lean — philosophical is due, and the empirical result demands it.** The Option-A falsification was
written under (and overturns) the picture two essays were built on; revising them is exactly the charter's
empirical→philosophical inter-feeding (§12.1). Highest-value next units:

1. **PHILOSOPHICAL (integration, highest-value) — revise the two relational essays the falsification touches.**
   (a) [`essay/conversation-as-text-not-timeline`](wiki/findings/essays/conversation-as-text-not-timeline.md) (draft)
   argued the models read a conversation as "prose geometry — a bag with a gradient down the page," neither timeline
   nor order-free set, on the strength of v4's position-following. Option A shows that when order **disambiguates**,
   the models **do** track the timeline (latest-binding-wins) — so the "text-not-timeline" thesis must be **scoped**:
   it holds where order carries no disambiguating signal, and **fails** where it does. Fire its revision triggers
   (it explicitly named "a v5 neutralizing text-position" and "live-reassignment" as triggers); log the revision
   in-page. (b) The first essay [`essay/...aggregation-not-constitution`] (the aggregation-vs-constitution piece) bet
   on commutativity/aggregation; Option A puts the models on the **order-sensitive** side in this regime (still
   *aggregation-thin*, not constitution) — revise to record that the clean commutative reading is now falsified-where-
   testable, and sharpen the aggregation/constitution line as "order-sensitive but thin, not constituted-between."
   Both are essay-revisions (log in-page, keep retractions visible), not new claims; no new spend.

2. **PHILOSOPHICAL alternative / complement — catalogue an open-access primary that the relational line now needs.**
   **Lewis 1969 *Convention*** would anchor the very notion of "convention" the whole relational axis leans on (and
   the retired conjecture's framing); or a primary on conversational **repair / common ground** (Clark) to ground the
   "latest agreement supersedes" norm the models exhibit. Verify OA-fetchability before committing; do not gamble a
   session on an unreachable primary. (`wanted.md` has the backlog.)

3. **EMPIRICAL (if a balanced session, or for a later empirical lean) — the order-sensitivity GENERALITY follow-up.**
   The new claim's revision triggers name the bets: does latest-binding-wins persist under **implicit** reassignment
   (no "was reassigned" framing — the cleanest test that it is not a surface artifact of the wording), under
   **non-overwrite repairs**, with **image referents**, or in **cross-family dyads**? And the **thin-vs-rich**
   separation (is it a shallow overwrite heuristic or deeper path-dependence?). Any of these is a clean next empirical
   unit; the implicit-reassignment control is the highest-value (it directly tests the verifier's one flagged caveat).
   Template: `experiments/runs/2026-06-16-relational-spontaneous-recency-a/` (reusable balanced-block machinery).

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty. The relational-v5 decision (`wiki/decisions/resolved/`) is **fully
  realized**: staged B→A complete, Option C not reached.

## Standing-override notes (for Tom, if he looks)

- This was an **experiment session** (~$0.12; day ~$0.18 of $5.00). It ran the decisive test of a long-standing
  question: are a model's word-meanings **order-blind** (a bag of what was said) or do they track **when** things
  were agreed? With page-position neutralized so only timestamps disambiguate, **both models cleanly tracked the
  latest agreement** when a coined word was reassigned mid-conversation — **overturning the project's own earlier bet**
  that these conventions are order-insensitive. That bet (a conjecture) is now retired and replaced by a narrow,
  supported finding.
- **Deliberately modest:** the finding is that the models apply a simple "latest agreement wins" rule — a *thinner*
  thing than meaning being genuinely *built between* two parties. It is one task, makes no comparison to people, and
  does **not** make the earlier order-*insensitive* results wrong (they were settings where order carried no extra
  information) — so whether a convention is order-free turns out to depend on the task.
- Full discipline held: an independent reviewer certified the test *before* it ran (no shortcut could pass it without
  reading the timestamps), and an independent verifier reproduced every number from the raw data afterward. GitHub
  Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC
— check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **No decision is open.** Tracks: empirical advanced this session (relational track's first positive)
— a session is **due to lean philosophical**, and two relational essays now need revision in light of the
falsification (the highest-value next unit). The relational-v5 staged line is **complete**.
