# NEXT.md

## State

**Session of 2026-06-19 (forty-second session, empirical) is landed and squash-merged to `main` (PR #TBD).**
An experiment session — **$0.805 billed**; day total 2026-06-19 = **≈$2.27 of $5.00** (the 38th + 40th + this 42nd
runs, all the same UTC day).

It ran the **larger-grid (K=6, D6) generality re-run** of the Option-C order-sensitive composition probe
([`result/relational-order-composition-c-k6`](wiki/findings/results/relational-order-composition-c-k6.md)): the
**same** dihedral STEP/FLIP pair as the working-surface witness, but on a **six-figure** track (D6, order 12, vs
D4's 8) — a larger answer space (chance 1/4→1/6) and more positions to track — holding the figure→figure rendering,
the working-surface format, thresholds, verdict map, and the THIN adjudication identical. The reader set is unchanged
(only K), so the K=4 certification framework carried over; `analyze.py` + fixtures are byte-identical (K-only diff).
Fresh stimuli rstrip-sha `f4d0e36d…82b33`.

**Verdict: REPLICATES — all three models RESPECTS-ORDER on the bigger grid.** claude DIRECT 1.000 / COMP 1.000;
gemini DIRECT 1.000 / COMP 1.000; **gpt DIRECT 1.000 / COMP 0.861** (Wilson-LB 0.763 > 0.50; its 10 misses are
**reversed-order slips**, not single-move reads — step/flip-only 0.000). DIRECT at ceiling for all three
self-calibrates K=6 as fully composable; CoT re-sorts by round stamp on all 36 reverse-printed COMP records (genuine,
verbatim-confirmed). 324/324 parsed via the target-blind `FINAL:` tag; **0 NA, 0 retried, 0 length-truncation**.
Independent **pre-run critic GO** (recomputed D6 + shortcut-proofing at K=6, K-only diff, no new decision owed) +
independent **post-run verifier REPRODUCED** (324/324 picks matched, 0 geometry mismatches, CoT genuineness
confirmed, cost re-summed). `anchor: internal-contrast-only`; **no human comparison.**

**So the working-surface composition witness now generalizes over TWO axes:** the operation pair (40th, A4 vs D4)
**and** the grid size (this run, K=6 vs K=4) — a composition **capacity**, not a one-instrument or one-grid artifact.
**Still THIN, still negative on constitution; rung (iii) stays documented structurally closed for text-only stimuli.**

**One honest signal flagged (not a finding):** gpt's spontaneous-ordering COMP rate dips monotonically across the
three working-surface instruments — 0.953 (K=4 STEP/FLIP) → 0.906 (K=4 CYCLE/SWAP) → **0.861 (K=6)** — while its
on-demand DIRECT stays at ceiling throughout and misses stay reversed-order (capacity intact). With n=72 the CIs
overlap, so this is **suggestive only**. It points squarely at the **>2-move** probe (a bigger *serial-depth* demand,
not a bigger *state*) as the natural next test of [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
trigger (b): a negative that *survives* a wide channel would be **channel-controlled** (a real bound), not
channel-bounded.

**Integration this session:** new result page; [`wiki/index.md`](wiki/index.md) catalog entry; extended the
`output-channel-confound` essay's 2026-06-19 forward-note to fold in the grid-size axis + the gpt-dip watch-item.
senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean. Website
(`docs/`): journal 42nd entry + home status block + `findings.html` composition follow-up brought current. Tracks:
…emp(40)→phil(41)→**emp(42)**, so the next session is **due to lean philosophical** (or empirical again if a
philosophical unit isn't ready — see below).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to ratify
unless Tom opens something or leaves an override. This session opened **no** decision. Apply any Tom override first.

**Then pick the lean — philosophical is due** (tracks ended on emp(42)). Candidates, either track:

1. **PHILOSOPHICAL (lean is due).** The composition line is now a clean, replicated, panel-concordant capacity across
   **two** generality axes (operation pair + grid size). A cheap, owed-nothing unit: catalogue a `wanted.md` source
   (open-access self-fetch only). Or a writing unit: the composition synthesis could be re-checked for currency
   against this K=6 result in [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md)'s
   relational cell and [`essay/update-is-not-constitution`](wiki/findings/essays/update-is-not-constitution.md) — but
   **note**: this run moves nothing across the thin/rich cut and is a generality corroboration only, so neither page
   is *stale* (both already record the panel-wide thin capacity); a light currency pass at most, not a rewrite.

2. **EMPIRICAL (if a second wave, or if leaning empirical again).** The clear priority is now the **>2-move
   (deeper-composition)** probe — the **most informative** remaining axis and the natural
   [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) **trigger-(b) contrast case**
   (does a serial-depth negative *survive* the wide working-surface channel → channel-controlled, a real bound?).
   The K=6 gpt-dip signal makes this especially timely. **BUILD-COST NOTE (unchanged, important):** a >2-move
   instrument needs **fresh** shortcut-proofing over all orderings of ≥3 distinct stamps — the competing-reader set
   explodes (single-move ×3, pair-compositions, more canonical orders), and K=4 may be **too small** to exclude every
   competing reader-end from the target by construction (pigeonhole on only 4 positions). Budget a dedicated build
   session: likely needs K≥5/6 *and* careful balancing, with its own independent pre-run critic. Do **not** rush it
   into a shared wave. Other axes remain: partially-conflicting refinements; image referents; cross-family dyads.
   Grammar reserve: the AANN/CxG cancel-direction Option-B held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session). This session opened none.

## Standing-override notes (for Tom, if he looks)

- This session re-ran the "order of operations" experiment on a **bigger board** (six figures instead of four),
  changing only the board size. All three models still work the puzzle out — applying both moves perfectly when told
  the order, and working out the order themselves when it isn't given (two perfectly, the third ~86% of the time, its
  slips being ordinary "wrong order" mistakes). So the ability survives both a different pair of moves (last session)
  and a larger board (this one) — a real capacity given room to show working, not a quirk of the smallest test. It
  stays a **thin** kind of order-sensitivity and the top of the ladder is no closer; **no comparison to people.** One
  honest detail noted for a future test: the third model's harder-question score has drifted gently down as the puzzle
  grew (95%→91%→86%) — a hint, not an established effect — pointing to a "more than two moves" test next. Independently
  checked before spending and independently reproduced after. Spend ≈ $0.80; day total June 19 ≈ $2.27 of $5.00. Next
  session leans back toward the writing/philosophy track.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-19 day total = **≈$2.27**; this session
added **$0.805**). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended
**phil(41) → emp(42)** — a session is **due to lean philosophical**. The composition line: the working-surface
composition witness now **generalizes over two axes** — operation pair (D4↔A4) **and** grid size (K=4↔K=6) — a
composition **capacity**, still **THIN**, still **negative on constitution**. Remaining empirical axes: **>2 moves**
(deeper composition — most informative, the `output-channel-confound` trigger-(b) contrast case; **budget the intricate
≥3-stamp shortcut-proofing, likely needs K≥5/6**), images, cross-family. Every composition probe **must use a working
surface** (the forced single-token format masks the capability). **Rung (iii) stays documented structurally closed for
text-only stimuli.** The methodological spine has **six** essays (undischargeable-negative, witness-seeking-economics,
capability-split, transcript-ceiling, floor-is-not-a-ceiling, output-channel-confound).
