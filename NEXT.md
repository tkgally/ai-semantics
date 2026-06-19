# NEXT.md

## State

**Session of 2026-06-19 (fortieth session, empirical) is landed and squash-merged to `main` (PR #TBD).**
A single experiment session — **288 finding-bearing calls, $0.739 billed**; day total 2026-06-19 = **$1.47 of $5.00**
(witness run $0.735 earlier the same UTC day + this $0.739).

It ran the **alt-pair generality re-run** of the Option-C order-sensitive composition probe,
[`result/relational-order-composition-c-altpair`](wiki/findings/results/relational-order-composition-c-altpair.md):
a generality test of the 38th-session **working-surface witness** over the **one axis the witness left fixed — the
operation pair**. The witness was found on the dihedral STEP/FLIP pair (generating **D4**); this run swapped it for a
**genuinely different** non-commuting pair — **CYCLE** (the 3-cycle `(1 2 3)`) + **SWAP** (the double transposition
`(0 1)(2 3)`), generating **A4** (a different group, not a relabeling) — holding everything else identical (K=4,
figure→figure rendering, working-surface format, thresholds, verdict map, THIN adjudication; fresh stimuli, rstrip-sha
`f21f0cfb…22bb`). **Outcome: REPLICATES — all three models RESPECTS-ORDER** (claude DIRECT 1.000 / COMP 1.000; gemini
1.000 / 1.000; **gpt DIRECT 1.000 / COMP 0.906**, Wilson-LB 0.810 > 0.50 — gpt's 6 misses are reversed-order slips, NOT
single-move reads). DIRECT at ceiling for all three self-calibrates the alt pair as fully composable; CoT re-sorts by
round stamp on all 32 reverse-printed COMP records (genuine composition). So the dissolution of the four-instrument
forced-format split is a composition **capacity**, not an artifact of the one STEP/FLIP instrument — **strengthening**
[`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)'s "capacity, not one-instrument
artifact" reading and answering the witness result's open-question (iv) (generality across operation pairs) **positive**.
**Still THIN** ("respects operation order", not rung iii); `anchor: internal-contrast-only`; **no human comparison.**

**Integration:** independent **pre-run critic GO** (fresh agent recomputed CYCLE/SWAP from scratch, confirmed A4 ≠ D4
a genuinely different pair, 0 geometry mismatches, all shortcut readers exactly at bounds, sha match, parser
target-blind, only the operation pair changed vs the witness run, no new decision owed) + independent **post-run
verifier REPRODUCED** (288/288 picks matched, 0 geometry mismatches, CoT genuineness confirmed with verbatim quotes for
all three models, cost re-summed $0.739, 0 missing). Updated, by judgement (orchestrator): the new result page;
forward-pointer notes to the **witness result** (open-question iv answered positive) and to
[`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) (capacity reading corroborated over
the operation pair); [`wiki/index.md`](wiki/index.md) +1 result entry; senselint **0 errors** (2 expected WARNs:
`wanted.md`, `multimodal-anchor-scouting.md`); linkify clean. Website (`docs/`): journal 40th entry + home status block
(Completed studies 45→46, Current focus rewritten, Spending updated) + new "The latest" card + findings generality
follow-up paragraph. Tracks: …emp(38)→phil(39)→**emp(40)**, so the next session is **due to lean philosophical**.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to
ratify unless Tom opens something or leaves an override. This session opened **no** decision (the alt-pair run owed
none, per the pre-run critic). Apply any Tom override first, as always.

**Then pick the lean — philosophical is due** (tracks ended on emp(40)). Candidates:

1. **PHILOSOPHICAL (lean is due).** The composition line now has a clean empirical shape worth synthesizing:
   - **Re-examine [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md)** (the
     relational ladder) now that order-sensitive **composition** is **panel-concordant AND generalizes across the
     operation pair** (thin, under a working surface) — is composition a stable rung, and where does it sit relative to
     rungs (i)–(ii)? Or
   - **A short synthesis / theory-page touch** recording that the working-surface composition capacity is now
     corroborated on two distinct non-commuting pairs (D4, A4) — what the capacity reading does and does not license
     (still THIN, still one operationalization family). Could update
     [`findings/theory/situating-llm-meaning.md`](wiki/findings/theory/situating-llm-meaning.md)'s relational cell.
   - Or **catalogue a `wanted.md` source** (philosophical-track reading) if a cheap mixed unit is preferred.

2. **EMPIRICAL (if a philosophical anchor is not ready, or as a second wave).** Generality axes still untested for the
   working-surface composition capacity (all need a working-surface elicitation — the forced format is known to mask):
   (a) **larger grids** (K>4); (b) **deeper composition** (>2 moves) — the most informative, and a candidate
   **contrast case** for [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) trigger (b)
   (a serial-computation negative that *survives* a widened channel → channel-controlled, not channel-bounded);
   (c) partially-conflicting refinements; (d) image referents; (e) cross-family dyads. **NOTE on build cost:** a >2-move
   instrument needs fresh shortcut-proofing over all orderings of 3 distinct stamps (intricate certification — budget
   the build time); the alt-pair build here was cheap because it reused the K=4 machinery.
   - Grammar reserve: the AANN/CxG cancel-direction Option-B held in
     [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
     (needs a fresh human anchor first).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session).

## Standing-override notes (for Tom, if he looks)

- Last session found that two models which had "failed" a two-step order-of-operations puzzle could actually do it
  once given room to show their working — but only on one specific pair of moves. This session checked whether that
  was a fluke of the one pair: it rebuilt the puzzle with a **genuinely different pair of moves** (a three-way rotation
  and a swap-in-pairs, which combine differently) and re-ran all three models, changing only the pair. **It
  replicated cleanly** — all three again apply both moves correctly on demand and work out the order on their own when
  it isn't given (two perfectly, the third ~91%), with their working re-sorting the moves into time order even when
  printed in reverse. So the ability is a **real capacity** to carry out an order of operations (given room to show
  the working), not a quirk of the one test. It stays modest: a thin kind of order-sensitivity, no comparison to
  people, one family of puzzle (bigger boards, more moves, and picture versions untested). An independent reviewer
  approved the materials before any spending and a second reproduced every number. ≈ 74 cents; day total ≈ $1.47. The
  next session leans back to the writing/philosophy track.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-19 day total so far = **$1.47**; this
session added **$0.739**). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended
**phil(39) → emp(40)** — a session is **due to lean philosophical**. The composition line: the working-surface
**witness** (all three models compose two non-commuting moves given a working surface) now **generalizes across the
operation pair** (replicated on a second, A4, pair) — a composition **capacity**, not a one-instrument artifact;
remaining empirical generality axes are larger grids, >2 moves (deeper composition; also the natural
`essay/output-channel-confound` trigger-(b) contrast case), images, cross-family. Every composition probe **must use a
working surface** (the forced single-token format masks the capability). **Rung (iii) stays documented structurally
closed for text-only stimuli.** The methodological spine has **six** essays (undischargeable-negative,
witness-seeking-economics, capability-split, transcript-ceiling, floor-is-not-a-ceiling, output-channel-confound).
