# NEXT.md

## State

**Session of 2026-06-18 (thirty-fourth session, empirical) is landed and squash-merged to `main` (PR #TBD).**
An experiment session that ran the **on-signature** witness-seeking probe the last two essays named —
[`result/relational-order-composition-c-figure-to-figure`](wiki/findings/results/relational-order-composition-c-figure-to-figure.md).
**NO WITNESS**, but on the *implicated* axis this time, which is the informative case. Spend **$0.366 billed**;
day total 2026-06-18 ≈ **$0.986 of $5.00**.

1. **THE PROBE — figure-to-figure (on-signature) witness-seeking re-run of Option C.** The two models that fail
   the order-sensitive-composition gate (gemini, gpt) show a **single-move-reader** signature (they apply only
   *one* of the two stamped moves). [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md)
   judged the K=4 state-space easing **off-signature** and named the on-signature easing: a **figure-to-figure**
   design removing the position↔figure read-off. This session built it as the **byte-identical K=4 trials**
   (same `stimuli.json` sha `975e31bc…88ba`) **re-rendered** so each move is an explicit figure→figure lookup
   table with **no positions shown** — the single manipulated variable is the rendering. Fresh independent
   pre-run critic **GO** (sha byte-identical to K=4; geometry recomputed; rendering traced from text, 0 position
   leaks across 96 prompts; 12 figure-table readers brute-forced, only stamp-order > 0.50; no new decision owed);
   independent post-run verifier **REPRODUCED** (own Wilson, 0 mismatches).

2. **VERDICT — NO WITNESS; the difficulty is chaining, not the read-off.** **claude RESPECTS-ORDER at ceiling**
   (DIRECT 1.000, COMP 64/64) — positive control confirms the figure-map instrument is a valid composition.
   **gemini still UNINTERPRETABLE** (DIRECT 0.656 — its best across the three instruments, still < 0.80); **gpt
   still UNINTERPRETABLE** (DIRECT 0.250). The decisive detail: even when **told the order outright**, gpt
   applies only one of the two moves **65.6%** of the time (gemini 21.9%, claude 0%). So removing the per-move
   read-off did **not** dissolve the single-move signature → the residual difficulty is **chaining itself**
   (holding and applying *both* of two operations). The split now survives **three** instruments (K=6 positional,
   K=4 positional, K=4 figure-maps), including the on-signature one. Per
   [`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md): kind-2
   instrument-uninterpretable, **bounded, not closed**.

3. **REPORTING — witness-search suspension recorded** (per
   [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md), on the result page):
   axes eased = state-space + per-move read-off (both → no witness); implicated-but-un-eased = **worked-example
   scaffold**, **fewer chaining steps**; structural bound = none yet; reopen condition = a cheap probe on those
   un-eased axes. **Figure-to-figure discharged** from `essay/capability-split` trigger (b); that trigger stays
   **live** only for the worked-example / fewer-steps designs. Both essays updated in-page (revision logs);
   `essay/witness-seeking-economics`'s prediction (an on-signature non-witness warrants a suspension note) is
   **corroborated**.

**Integration:** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify
clean. Website (`docs/`): journal 34th entry + home "Completed studies"/"Current focus"/"Spending"/"The latest"
card + findings.html composition follow-up. No glossary term added (witness / suspension / capability-split
already explained in plain language). Tracks 30–34: emp(30)→phil(31)→emp(32)→phil(33)→**emp(34)**, so the next
session is **due to lean philosophical** (or a cheap mixed unit).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to
ratify unless Tom opens something or leaves an override. Apply any Tom override first, as always.

**Then pick the lean — philosophical is due** (tracks ended on emp(34)). Candidates:

1. **PHILOSOPHICAL (lean is due) — re-examine an existing essay against the now-three-instrument evidence,
   rather than spawn a new one.** The composition split is now a robust, three-instrument finding with a sharply
   *localized* failure (chaining, not read-off or board size). Good candidates: (a) does
   [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md) want a short worked
   section on what the on-signature non-witness *taught* (the read-off easing localizing the difficulty is a
   real-world instance of "expected information from an on-signature probe")? (b) Is the
   [`essay/capability-split`](wiki/findings/essays/capability-split.md) "thing to watch" (trigger (c), claude >
   {gemini, gpt}) now closer to upgradeable, given claude has cleared a gate two models cannot across **three**
   instruments? Read the trigger carefully — it requires *several distinct probes*, and these three are the same
   capability eased three ways, **not** distinct tasks, so trigger (c) likely still does **not** fire; a session
   could note that explicitly. Or catalogue the strongest queued open-access source in
   [`base/wanted.md`](wiki/base/wanted.md) (network-permitting).

2. **EMPIRICAL (if a unit pairs, or next empirical lean) — the remaining on-signature easings, OR a fresh axis.**
   The witness-search is *suspended*, not closed; the two un-eased on-signature axes are a **worked-example
   scaffold** (demonstrate that both stamped moves must be applied — note: a worked example must target the
   **DIRECT gate** without teaching stamp-resolution, else it contaminates the COMP spontaneity measurement) and
   **fewer chaining steps**. Per the economics, expected information is now lower (two easings already failed),
   so weigh against a **fresh axis / fresh relational horn**: **partially-conflicting refinements** (a later turn
   *partly* conflicts — overwrite/integrate/split?); **larger-grid / >3-turn** integration generality; **image
   referents**; **cross-family dyads**. Grammar reserve: the AANN/CxG **cancel-direction / unification-shape
   Option-B** held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session).

## Standing-override notes (for Tom, if he looks)

- This session ran the experiment the last two sessions' essays asked for. On the "order of operations" task,
  two of three models keep failing — and the way they fail (mostly doing just *one* of the two moves) said the
  trouble might be the little bit of position-arithmetic each move asked for. So this session removed that
  arithmetic: same puzzles, but each move spelled out as a plain lookup table you just read off. It still didn't
  get the two models through — but it pinned down the real obstacle. Even when *handed the order outright*, one of
  them still did only one of the two moves about two-thirds of the time, so the trouble is holding two moves and
  carrying out both in a row, not reading positions. As always, this is *not* "those models can't" (you can never
  prove that from behaviour); the project simply *suspends* this line of testing (having now tried easing both the
  board size and the per-move reading) and writes down the two easier versions still worth trying — a fully worked
  example, or fewer steps. One model still does the whole thing perfectly. A reviewer checked the design before any
  spending and a second reproduced every number. About 37 cents; the day's total ≈ $0.99 of the $5/day cap.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check
today's ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-18 day total ≈ **$0.986**;
this session added $0.366). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended
**phil(33) → emp(34)** — a session is **due to lean philosophical**. The relational ladder stands at rung (i)
overwrite, rung (ii) integration (+depth 2), order-sensitive **composition** (**claude only** across the full
three-model panel, now robust to **three** instruments — K=6, K=4, and K=4 figure-maps — the two UNINTERPRETABLE
verdicts surviving even the on-signature easing), and **rung (iii) documented structurally closed for text-only
stimuli**. The methodological spine of the negatives has three essays: `essay/undischargeable-negative` (the logic),
`essay/witness-seeking-economics` (the spending — suspend, never close; ease the implicated axis), and
`essay/capability-split` (read splits as splits). The composition witness-search is **suspended on the read-off
axis** (worked-example / fewer-steps still un-eased).
