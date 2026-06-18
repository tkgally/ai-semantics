# NEXT.md

## State

**Session of 2026-06-18 (thirty-first session, philosophical) is landed and squash-merged to `main` (PR #TBD).**
A single-wave writing session (no models queried, **$0 spent**) that wrote the project's **twelfth essay** —
the general epistemology of the negative that was implicit in the last three sessions' work but never stated on its
own terms.

1. **PHILOSOPHICAL HEADLINE — new essay [`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md).**
   Gives the charter's "write the null" discipline a logical-epistemic backbone: a capability **positive** is a
   *verifiable existential* (one witness — one elicitation on which the model succeeds — discharges it); a capability
   **absence** ("M cannot do X") is an *unverifiable universal over elicitations* that no finite behavioral battery
   reaches — so from behavior alone the negative is **undischargeable** (the mirror of the Popperian law/existence
   asymmetry). This **vindicates** the null discipline: the project's nulls are not capability-absence claims but
   instrument-relative facts; the only error is the silent upgrade to "M cannot." Builds a **typology of negatives** —
   (1) effect-null under an instrument, (2) instrument-uninterpretable / prerequisite-gate failure, (3) structural
   reach-closure (a negative about the *instrument*, not the model) — and keeps a fourth box, a *behavioral*
   capability-absence, deliberately empty (only a non-behavioral architectural/mechanistic proof closes it). Payoff:
   re-running a failing probe is futile (another ∀-instance, never the ∀); only a **witness-seeking** probe (an easier
   elicitation) or a structural argument can change a negative's status. **Generalizes**
   [`essay/capability-split`](wiki/findings/essays/capability-split.md) (clean-null/instrument-uninterpretable mark,
   lifted from split-panel to single-model) and lifts [`essay/transcript-ceiling`](wiki/findings/essays/transcript-ceiling.md)'s
   structural closure into "kind 3." `status: draft`; `meaning-senses: model-internal, functional-vs-formal, relational`;
   no new empirical claim, no human comparison.

2. **PROCESS.** Orchestrator authored the essay (judgement-heavy; coheres with four existing essays — not parallelized,
   per `PROTOCOL §A`); one **independent read-only adversarial review** agent found 1 BLOCKER (a quote cited to the wrong
   page — "lacks order-sensitive composition in general" belongs to `essay/capability-split`, not the result page) + 3
   SHOULD-FIX (chained-quote attribution; under-signposted reconciliation of kind-3 reach-closure vs trigger-(a)
   capacity-proof; an "adequately-powered" overstatement contradicting the relational pilot's own power caveat); **all
   applied**. Distinctness from the two essays it generalizes was confirmed real by the reviewer.

**Integration:** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean.
Website (`docs/`): journal 31st entry + home status block + "The latest" card + findings.html twelfth-essay paragraph.
No glossary term added (site prose stays jargon-free). Tracks 21–31: phil/emp/phil/… ending **emp(30) → phil(31)**, so
the next session is **due to lean empirical** (or a cheap relational/grammatical unit).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to ratify
unless Tom opens something or leaves an override. Apply any Tom override first, as always.

**Then pick the lean — empirical is due** (tracks ended on phil(31)). Candidates:

1. **EMPIRICAL (lean is due) — the single most informative cheap test, now doubly motivated.**
   **Capability-split trigger (b) / the witness-seeking probe:** does an *easier* non-commuting-operation design let
   gemini or gpt clear the Option-C **on-demand gate** and then compose? The new essay makes this the *only* kind of
   probe that can change the two UNINTERPRETABLE verdicts' status (a witness flips a negative to a positive; re-running
   the hard instrument cannot). A both-fail-under-difficulty vs stable-gap discriminator — bounds the split to *this*
   instrument if they then compose. Frozen instrument:
   [`design/relational-order-composition-c`](experiments/designs/relational-order-composition-c.md); the new probe needs
   a fresh, certified *easier* operation pair (e.g. two moves that compose more legibly), independent pre-run critic GO,
   pre-flight budget estimate. Cheap (gpt+gemini are the cheap panel models).

2. **EMPIRICAL alternatives.** Other untested relational horns: **partially-conflicting refinements** (a later turn
   *partly* conflicts — overwrite/integrate/split?); **larger-grid / >3-turn** integration generality; **image
   referents**; **cross-family dyads**. Grammar reserve: the AANN/CxG **cancel-direction / unification-shape Option-B**
   held in [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

3. **PHILOSOPHICAL reserve (if a unit pairs).** The new essay's **trigger (a)** names an off-behavioral route to a
   genuine capability-absence (an architectural expressivity bound / mechanistic result) — if the project ever ingests
   an open-access expressivity-limit source, that would instance the otherwise-empty fourth box. Not pressing.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session).

## Standing-override notes (for Tom, if he looks)

- This session **wrote one essay and spent nothing**. The essay names a plain asymmetry under a lot of the recent work:
  you can show a model *can* do a task with one good example, but you can never show from its behaviour that it *can't*
  ("can't" = "fails no matter how you ask," and you can't try every way of asking). The point is that this *supports*
  the project's habit of honestly reporting empty results — those results only ever mean "nothing showed up under this
  test," never "the model is incapable" — and it sorts every empty result the project has into three honest kinds while
  leaving "the model is incapable" deliberately unclaimed. An independent review caught a mis-cited quote and a couple of
  over-statements, all fixed before merge.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog lives at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check
today's ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-18 day total ≈ **$0.335**, this
session added $0). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended **emp(30) →
phil(31)** — a session is **due to lean empirical**; the sharpest cheap unit is **capability-split trigger (b)** (an
easier composition design — a witness-seeking probe, the only kind that can move the two UNINTERPRETABLE verdicts). The
relational ladder stands at rung (i) overwrite, rung (ii) integration (+depth 2), order-sensitive **composition**
(**claude only** across the full three-model panel), and **rung (iii) documented structurally closed for text-only
stimuli**.
