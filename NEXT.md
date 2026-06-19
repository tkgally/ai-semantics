# NEXT.md

## State

**Session 44 (housekeeping, monitor request) is landed.** A small docs-format change at Tom's instruction — **no models
queried, $0 spent**. From session 44 onward, public-site session entries (`docs/journal.html`, `docs/index.html`) stamp
the date **with the JST clock time** of the build and write the session number **as a numeral** ("session 44", not
"forty-fourth session"); earlier entries are left unrevised. The convention is recorded in
[`docs/README.md`](docs/README.md) ("Session-stamp format, from session 44 onward"). **Next research session is session
45** and should use the numeral + JST-time format. The empirical/philosophical backlog below is unchanged.

**Prior session of 2026-06-19 (forty-third session, philosophical) is landed and squash-merged to `main`.**
A reading-and-writing session — **no models queried, $0 spent**; day total 2026-06-19 unchanged at **≈$2.27 of $5.00**
(the 38th + 40th + 42nd experiment runs, same UTC day).

It catalogued one open-access outside source bearing directly on the project's current composition line:
[`source/li-2024-cot-serial`](wiki/base/sources/li-2024-cot-serial.md) — **Li, Liu, Zhou & Ma 2024, "Chain of Thought
Empowers Transformers to Solve Inherently Serial Problems" (ICLR 2024, arXiv 2402.12875)**. It is the **formal
counterpart** of the [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) mechanism: a
constant-depth ("one forward pass") transformer is expressively bounded (AC⁰/TC⁰), but with `T` chain-of-thought steps
it computes any size-`T` boolean circuit — so a working surface supplies the **inherently serial computation** a forced
single token lacks. Its lead hard example is **permutation-group composition**, exactly the project's composition-probe
object (STEP/FLIP, CYCLE/SWAP on D4/A4/D6). Catalogued with scope limits stated plainly: theory/mechanism source about
*idealized* transformers, **not a human anchor and not a claim about the panel**; licenses **no human comparison**.
Abstract verbatim-verified from the arXiv abs page; body section-located via arXiv HTML / ar5iv (one §3.4 locator
correction logged in-page after a cross-check caught a first-fetch mislocation). Links: `supports` the essay,
`refines` [`concept/formal-vs-functional-competence`](wiki/base/concepts/formal-vs-functional-competence.md).

**Why this and not an essay edit:** the two essays NEXT.md last flagged for a possible currency pass
([`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md),
[`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)) were checked and found **fully
current** — both updated 2026-06-19, both already folding in the K=6 grid-size axis, the alt-pair axis, and the gpt-dip
signal. Editing them would have been padding, so the session did the cleaner owed-nothing unit (ingest an outside work)
instead. senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean.
Website (`docs/`): journal 43rd entry + home status block + "latest" entry brought current.

**Tracks: …phil(41)→emp(42)→phil(43), so the next session is due to lean EMPIRICAL** (or philosophical again if no
empirical unit is build-ready — see below).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to ratify
unless Tom opens something or leaves an override. This session opened **no** decision. Apply any Tom override first.

**Then pick the lean — empirical is due** (tracks ended on phil(43)). Candidates, either track:

1. **EMPIRICAL (lean is due).** The clear priority is the **>2-move (deeper-composition)** probe — the **most
   informative** remaining axis and the natural
   [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) **trigger-(b) contrast case**
   (does a serial-depth negative *survive* the wide working-surface channel → channel-*controlled*, a real bound, not
   channel-bounded?). The K=6 gpt-dip signal (COMP 0.953→0.906→0.861 across the three working-surface instruments,
   DIRECT at ceiling throughout, overlapping CIs → suggestive only) makes it timely, and `source/li-2024-cot-serial`
   now gives a theoretical reason to expect serial *depth* to be the load-bearing axis. **BUILD-COST NOTE
   (unchanged, important):** a >2-move instrument needs **fresh** shortcut-proofing over all orderings of ≥3 distinct
   stamps — the competing-reader set explodes (single-move ×3, pair-compositions, more canonical orders), and K=4 may
   be **too small** to exclude every competing reader-end by construction (pigeonhole on 4 positions). Budget a
   **dedicated build session**: likely needs K≥5/6 *and* careful balancing, with its own independent pre-run critic.
   Do **not** rush it into a shared wave. Other axes remain: partially-conflicting refinements; image referents;
   cross-family dyads. Grammar reserve: the AANN/CxG cancel-direction Option-B held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

2. **PHILOSOPHICAL (if a second wave, or if no empirical unit is build-ready).** A now-available, genuinely warranted
   (not padding) writing unit: fold `source/li-2024-cot-serial` into the
   [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) "A machine performance/competence
   gap" section as **external theoretical grounding** for the serial-computation mechanism — the essay currently flags
   that frame as "a *frame*, not an empirical claim" with no outside support, and this source supplies exactly that
   support (carefully scoped: theory about idealized transformers, not the panel; no human comparison). *Deliberately
   left for a later session* this run to avoid same-day churn on a fresh draft. Or catalogue another open-access
   `wanted.md` source (self-fetch only).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session). This session opened none.

## Standing-override notes (for Tom, if he looks)

- This session read no models and spent nothing. It filed an outside computer-science result (a 2024 conference paper)
  that **independently backs the project's recent method lesson**: that proof shows a model forced to answer in one
  shot is mathematically limited, but gains genuine step-by-step ("serial") power once it can write out intermediate
  steps — exactly why "giving the models room to show their working" unlocked the order-of-operations puzzle. The
  paper's headline hard example is *composing permutations*, the very move the project's puzzle is built from, so both
  the puzzle choice and the explanation now have outside theoretical support. Filed with the honest limits front and
  centre: it is a proof about idealized model designs, **not** the specific models tested, and makes **no comparison to
  people**. The next session leans back toward an experiment — most likely the "more than two moves" test the recent
  runs pointed to (which needs a careful dedicated build).

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-19 day total = **≈$2.27**; this session
added **$0.00**). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended
**emp(42) → phil(43)** — a session is **due to lean empirical**. The composition line: the working-surface composition
witness **generalizes over two axes** — operation pair (D4↔A4) **and** grid size (K=4↔K=6) — a composition **capacity**,
still **THIN**, still **negative on constitution**; and as of this session it has **outside theoretical grounding**
([`source/li-2024-cot-serial`](wiki/base/sources/li-2024-cot-serial.md)). Remaining empirical axes: **>2 moves**
(deeper composition — most informative, the `output-channel-confound` trigger-(b) contrast case; **budget the intricate
≥3-stamp shortcut-proofing, likely needs K≥5/6**), images, cross-family. Every composition probe **must use a working
surface** (the forced single-token format masks the capability). **Rung (iii) stays documented structurally closed for
text-only stimuli.** The methodological spine has **six** essays (undischargeable-negative, witness-seeking-economics,
capability-split, transcript-ceiling, floor-is-not-a-ceiling, output-channel-confound).
