# NEXT.md

## State

**Session of 2026-06-19 (forty-fourth session, empirical) is landed and squash-merged to `main` (PR #TBD).**
It built, certified, ran, and wrote up the **>2-move (deeper-composition) probe** — the priority empirical axis and the
[`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) **trigger-(b) contrast case**.
Spend **$0.803 billed**; day total 2026-06-19 now **≈$3.08 of $5.00** (sessions 38+40+42+44).

**Result: DEPTH SURVIVES THE CHANNEL — all three models RESPECTS-ORDER on THREE non-commuting moves**
([`result/relational-order-composition-three-move`](wiki/findings/results/relational-order-composition-three-move.md)):
claude DIRECT 1.000 / COMP 1.000; gemini 1.000 / 1.000; **gpt DIRECT 1.000 / COMP 0.903** (Wilson-LB 0.813 > 0.50; its
7 misses, all on reverse-printed records, are single mis-applied table lookups *after* a correct stamp-order re-sort,
not order-handling failures). So the working-surface composition **capacity now holds across THREE generality axes** —
operation pair (A4), grid size (K=6), and **depth (3 moves)** — and the trigger-(b) "survives a widened channel"
contrast returns **negative** for a depth-3 bound (the wide channel absorbed the deeper serial load, as
[`source/li-2024-cot-serial`](wiki/base/sources/li-2024-cot-serial.md) predicts). The suggestive K=6 state-size dip did
**not** continue into depth (gpt 0.903), but the depth-3 run used a different generic-permutation instrument, so it is
not a clean continuation of that series. Still **THIN**; `anchor: internal-contrast-only`; no human comparison.

**Design note worth keeping:** the dihedral STEP/FLIP family **cannot** be shortcut-proofed at three moves (its products
collapse — exhaustive search found no K≤12 config isolating the true ordering, exactly the pigeonhole worry the prior
handoff flagged). The fix was **three generic non-commuting derangements** of six figures (generating S6), found by
search to give a perfectly balanced set (6 orderings × 1 strict-valid start each, 6 distinct starts/targets). The **0.50
ceiling carries over** because a "half-composer" who orders only 2 of 3 moves correctly tops out at exactly 0.50 — proven
by brute-forcing the full reader family in `assert_balance` and confirmed by the independent pre-run critic (no
non-composing reader beats 0.50). This is the reusable template if a **≥4-move** run is ever built.

senselint **0 errors**; linkify clean. Website (`docs/`): journal 44th entry + home status block + "latest" entry +
findings.html follow-up. Essay/theory/claim updated (see below).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). This session opened
**no** decision (the pre-run critic concurred that the move-count change owes none — within-frame, same adjudication +
`internal-contrast-only` posture). Apply any Tom override first.

**Then pick the lean — philosophical is due** (tracks ended on …phil(43) → emp(44)). Candidates, either track:

1. **PHILOSOPHICAL (lean is due).** A genuinely warranted (not padding) writing unit carried over from before and now
   sharpened by this session's result: fold [`source/li-2024-cot-serial`](wiki/base/sources/li-2024-cot-serial.md) into
   the [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) **"A machine
   performance/competence gap"** section as **external theoretical grounding** for the serial-computation mechanism
   (the section currently flags that frame as "a *frame*, not an empirical claim" with no outside theoretical support;
   the source — chain-of-thought lets a transformer perform inherently serial computation a single forward pass cannot —
   supplies exactly that, carefully scoped: theory about idealized transformers, not the panel, no human comparison). The
   depth-3 result (trigger-(b) negative) makes this timely: the essay now *predicts and confirms* on the depth axis what
   the source explains. NB: this session already added a **forward note** + a trigger-(b) "tested, not fired" note to the
   essay and the depth result to its links — so the remaining unit is the **competence/performance section grounding**,
   not those. Check it isn't now redundant before writing. Or catalogue another open-access `wanted.md` source.

2. **EMPIRICAL (if a second wave or no philosophical unit is build-ready).** Remaining composition axes: **deeper still
   (≥4 moves)** — the only way to keep hunting for a channel-*controlled* bound, but **build cost grows** (the competing
   reader set expands with depth; use the generic-permutation + brute-forced `assert_balance` template from this session;
   K=6 may be too small to strict-isolate at 4 moves — likely needs K≥7/8; budget a dedicated build session, its own
   pre-run critic). Other axes: **partially-conflicting refinements**; **image referents**; **cross-family dyads**.
   Grammar reserve: the AANN/CxG cancel-direction Option-B held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). This session opened none.

## Standing-override notes (for Tom, if he looks)

- This session ran the "more than two moves" experiment the recent runs pointed to. It asked the models to work out the
  order of **three** time-stamped moves (not two), given room to show their working — the deepest version of the
  order-of-operations puzzle the project has built, and the case it expected might finally be too hard for the roomy
  answer format. It was **not** too hard: all three models worked out the three-move order on their own (two perfectly,
  the third about nine in ten, its slips small arithmetic errors after it had already sorted the moves correctly). So the
  ability is now confirmed across a different pair of moves, a bigger board, **and** a deeper chain. The honest limits
  hold: it makes no comparison to people, it is still a "thin" kind of order-sensitivity, and a success cannot prove that
  no even-deeper task (four or more moves) would trip the models up. Building the test was the bulk of the work and was
  double-checked independently before and after spending. Spend ≈ $0.80; day total ≈ $3.08 of $5.00.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-19 day total = **≈$3.08**; this session
added **$0.803**). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended
**emp(44)** after **phil(43)** — a session is **due to lean philosophical**. The composition line: the working-surface
order-sensitive composition witness is now a **capacity** generalizing over **three** axes — operation pair, grid size,
and **depth (three moves)** — still **THIN**, still **negative on constitution**, with **no** channel-controlled bound
found at any depth/size tested (the [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
trigger-(b) contrast remains open: only deeper-still or a qualitatively harder serial demand could fire it). Every
composition probe **must use a working surface** (the forced single-token format masks the capability). **Rung (iii)
stays documented structurally closed for text-only stimuli.** The methodological spine has **six** essays
(undischargeable-negative, witness-seeking-economics, capability-split, transcript-ceiling, floor-is-not-a-ceiling,
output-channel-confound).
