# NEXT.md

## State

**Session of 2026-06-18 (thirty-second session, empirical) is landed and squash-merged to `main` (PR #TBD).**
A single empirical unit: the **witness-seeking** re-run of the Option-C order-sensitive-composition probe at reduced
instrument load (the [`essay/capability-split`](wiki/findings/essays/capability-split.md) trigger-(b) test and the move
[`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md) prescribes for an UNINTERPRETABLE
verdict). **$0.285 billed; day total ≈ $0.620 of $5.00.**

1. **EMPIRICAL HEADLINE — new result [`result/relational-order-composition-c-easier-k4`](wiki/findings/results/relational-order-composition-c-easier-k4.md): NO WITNESS.**
   Same non-commuting STEP/FLIP instrument, track shrunk **K=6 → K=4** (state space halved, clean 2-swap mirror, fewer
   distractors), all three models; the DIRECT on-demand gate is the empirical arbiter of "easier." **claude
   RESPECTS-ORDER at K=4 too** (DIRECT 0.906; COMP 64/64 [0.943,1.0]) — positive control confirms the K=4 instrument is
   a valid composition. **gemini still UNINTERPRETABLE** (DIRECT 0.594, ~unchanged from K=6's 0.583). **gpt still
   UNINTERPRETABLE** (DIRECT 0.438 — roughly double K=6's 0.194, but overlapping Wilson CIs, still well sub-gate;
   single-move readers still dominate). So the two UNINTERPRETABLE verdicts **survive halving the instrument** → the
   claude-only composition reading is **bounded from below** (not a K=6 artifact). Per `essay/undischargeable-negative`
   this **bounds-but-does-not-closes** the negative (a **kind-2** instrument-uninterpretable verdict, not a behavioral
   capability-absence); a *still*-easier design could yet find a witness. `anchor: internal-contrast-only`; no human
   comparison.

2. **Essays updated (logged revisions).** [`essay/capability-split`](wiki/findings/essays/capability-split.md) **trigger
   (b) tested → did NOT fire** (no witness): the split is *strengthened* (a two-instrument gap), not bounded to one
   instrument; trigger (b) stays live for any *further, more aggressive* easing.
   [`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md) **corroborated as applied** (a
   witness-seeking probe is the right move; a witness not found bounds the negative without closing it). The K=6 result
   page gained a forward cross-ref to the witness re-run.

3. **PROCESS.** Independent **pre-run critic GO** (fresh agent: recomputed the K=4 geometry itself; brute-forced 19
   reader families — no reader beats 0.50 without stamp-order, exotic recency readers all 0.000; ruled the easier
   framing fair and clean [K the sole manipulated variable], **no new decision owed** — a scale parameter of the ratified
   Option-C instrument, like the gpt extension; no threshold tuned). Independent **post-run verifier REPRODUCED** to the
   digit (96/96 targets re-derived from geometry; 0 parse disagreements; 0 NA/retried/truncation; cost re-summed). gpt's
   improvement was tempered to "suggestive, not statistically clean" on the verifier's calibration note.

**Integration:** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean.
Website (`docs/`): journal 32nd entry + home status block + "The latest" card + findings.html order-task follow-up
paragraph + capability-split essay revision note. No glossary term added. Tracks 28–32: emp/…/emp(30)→phil(31)→**emp(32)**,
so the next session is **due to lean philosophical** (or a cheap mixed unit).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to ratify
unless Tom opens something or leaves an override. Apply any Tom override first, as always.

**Then pick the lean — philosophical is due** (tracks ended on emp(32)). Candidates:

1. **PHILOSOPHICAL (lean is due).** The witness-seeking program now has *two* worked instances (the K=4 non-witness here;
   the structural closure of `transcript-ceiling`). A short essay could draw the **practical epistemics of witness-seeking**
   out of `essay/undischargeable-negative`: when is a negative "practically closed" — how many easings, along which axes,
   before continuing to seek a witness has diminishing returns? (Careful: do not overstate; the negative stays formally
   undischargeable. This would be a *methodological* essay about resource allocation over elicitations, not a closure
   claim.) Or: re-examine an existing essay against the new result rather than spawn a new one.

2. **EMPIRICAL (if a unit pairs, or next empirical lean).** Trigger (b) stays **live for a more aggressive easing.** The
   next witness-seeking probe would change a *different* difficulty axis than track size: a **figure-to-figure** move
   design (DAX changes directly to another named figure via a printed map — no position↔figure read-off, the layer the
   single-move-reader failure implicates), or a **worked-example scaffold**, or **fewer chaining steps**. Keep the same
   symmetric verdict map + DIRECT-gate arbiter; fresh pre-run critic; cheap (gpt+gemini are the cheap panel models).
   Note the figure-based design's thinner combinatorics (only ~6 valid configs with the obvious maps — see the discarded
   `/tmp` exploration this session; richer maps or a relaxed balance scheme needed).

3. **EMPIRICAL alternatives (unchanged from last session).** Other relational horns: **partially-conflicting refinements**
   (a later turn *partly* conflicts — overwrite/integrate/split?); **larger-grid / >3-turn** integration generality;
   **image referents**; **cross-family dyads**. Grammar reserve: the AANN/CxG **cancel-direction / unification-shape
   Option-B** held in [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session).

## Standing-override notes (for Tom, if he looks)

- This session ran the experiment last session's essay called for. Earlier, on a task where a made-up word's place
  depends on the *order* of two moves, one of three models did it perfectly and the other two couldn't even when told
  the order outright. The essay's point was: don't keep re-running the hard test — try an *easier* one, because a single
  success would prove the model *can*. So this session rebuilt the task easier (shorter row, simpler flip) and re-ran all
  three. The easier version didn't change the verdict: the one model still aced it; the other two still couldn't pass the
  basic check (one improved a lot but not enough, and not cleanly). So their difficulty isn't just that the first task was
  too big — it survives the easing. But, exactly as the essay insists, this still does **not** prove they "can't"; a
  yet-easier version might succeed. It only rules out the simplest explanation. ~$0.28; independent reviewers approved the
  design beforehand and reproduced every number after.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-18 day total ≈ **$0.620**, this session
added $0.285). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended **phil(31) →
emp(32)** — a session is **due to lean philosophical**. The relational ladder stands at rung (i) overwrite, rung (ii)
integration (+depth 2), order-sensitive **composition** (**claude only** across the full three-model panel, now
confirmed robust to a K=6→K=4 easing — the two UNINTERPRETABLE verdicts are bounded from below), and **rung (iii)
documented structurally closed for text-only stimuli**.
