---
type: result
id: relational-order-composition-three-move
title: Three-move (deeper-composition) extension of order-sensitive composition — the working-surface composition witness SURVIVES a deeper serial load; all three models RESPECTS-ORDER on THREE non-commuting moves; the output-channel-confound trigger-(b) contrast returns negative for a depth-3 bound
meaning-senses:
  - relational
  - model-internal
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-19
updated: 2026-06-19
links:
  - rel: refines
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: supports
    target: result/relational-order-composition-c-k6
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: essay/undischargeable-negative
  - rel: depends-on
    target: source/li-2024-cot-serial
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: refines
    target: concept/relational-meaning
---

# Result: three-move (deeper-composition) extension — the working-surface composition witness SURVIVES a deeper serial load

> **Status: proposed (2026-06-19).** A **depth** test of the execution-format **witness**
> ([`result/relational-order-composition-c-reasoning-scaffold`](relational-order-composition-c-reasoning-scaffold.md)),
> varying the one axis the witness, alt-pair, and K=6 runs all left fixed: the **number of moves
> (2 → 3)**. Every prior Option-C run composed exactly two non-commuting moves. This run composes
> **three**, on a working surface — the [`essay/output-channel-confound`](../essays/output-channel-confound.md)
> **trigger-(b) contrast case** (does a serial-*depth* gap **survive** the wide channel, which would be
> a channel-*controlled* bound, or does the channel absorb the deeper load too?), and the natural
> sharpening that essay's forward note and the K=6 result both named. The dihedral STEP/FLIP family
> cannot be shortcut-proofed at three moves (its products collapse — exhaustive search finds no K≤12
> config that isolates the true ordering), so it is replaced by **three generic non-commuting
> derangements** of six figures; everything else (figure→figure rendering, working-surface elicitation,
> the **0.50** ceiling, the symmetric verdict map, the thin adjudication) is held identical. Stimuli
> freshly built (rstrip-sha `eae2a2ab…0b6d774a`); an independent pre-run critic recomputed the geometry
> and the three-move shortcut-proofing from scratch and returned **GO**.
>
> **Outcome: DEPTH SURVIVES THE CHANNEL — all three models RESPECTS-ORDER on three moves.** Given a
> working surface, **claude** (DIRECT 1.000 / COMP 1.000), **gemini** (DIRECT 1.000 / COMP 1.000), and
> **gpt** (DIRECT 1.000 / COMP 0.903, Wilson-LB **0.813 > 0.50**) all clear the on-demand gate **and**
> spontaneously order **three** non-commuting moves by their round stamps. So the working-surface
> composition capacity is **not** specific to two-move depth: it extends to depth three. This is the
> [`essay/output-channel-confound`](../essays/output-channel-confound.md) **trigger-(b) contrast coming
> back negative for a depth-3 bound** — the deeper serial load did **not** produce a negative that
> survives the wide channel; the channel absorbed it. 324/324 replies parsed via the target-blind
> `FINAL:` tag; **0 NA, 0 retried, 0 length-truncation**; independently reproduced. **Still THIN**
> ("respects operation order", **not** rung (iii) / constitution; rich side stays documented
> structurally closed for text); `anchor: internal-contrast-only`; **no human-comparison claim.**

## The question (precise)

The execution-format witness found that opening a **working surface** (step-by-step output permitted,
`FINAL:`-tag parsed; reasoning-effort held constant) flipped both gemini and gpt from UNINTERPRETABLE to
RESPECTS-ORDER on two-move composition; the **alt-pair** (A4) and **K=6** (D6) runs replicated a two-move
composition **capacity** over the operation-pair and grid-size axes.
[`essay/output-channel-confound`](../essays/output-channel-confound.md) reads the witness as a capacity,
and its **trigger (b)** asks the sharper question: is there *any* serial-computation negative that
**survives** a widened channel (channel-*controlled*, a real bound) rather than dissolving
(channel-*bounded*)? The K=6 run logged a *suggestive* gpt COMP dip with **state** size (0.953 → 0.906
→ 0.861) and flagged the **deeper-composition (>2-move)** probe as the way to test whether a bigger
**serial-depth** demand (rather than a bigger *state*) yields such a survival negative.
[`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md) supplies the theoretical reason
to expect depth to be load-bearing: a constant-depth transformer is expressively bounded, but `T`
chain-of-thought steps let it compute any size-`T` serial circuit — so a working surface should supply
exactly the serial computation a deeper composition needs. **This probe varies the depth (2 → 3 moves)
and asks: does the working-surface composition survive a deeper serial load, or does depth defeat the
channel?**

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

The **single substantive change** vs. the witness run is the **number of moves (2 → 3)**. As a **forced
consequence**, the dihedral STEP/FLIP pair is replaced by **three generic non-commuting permutations**
of the six figures: `FLIP=[1,5,4,2,0,3]`, `SLIDE=[4,2,5,0,3,1]`, `TWIST=[3,0,1,5,2,4]` (position→position),
each a **derangement** (no figure maps to itself), pairwise non-commuting, together generating the full
**S6** (order 720). The dihedral group could not be used: at three moves its products collapse so that
no K≤12 configuration isolates the true ordering from the competing readers (verified by exhaustive
search) — the generic permutations are the shortcut-proofable choice. Each move is rendered as an opaque
figure→figure lookup table (the model never sees positions or any group structure). The **6 strict-valid
configs** (one start per stamp-ordering; targets falling one each on the six track positions) are chosen
so that for each config the true-stamp-order endpoint is hit by **no other sub-path** among all 16
(start, the 3 single moves, the 6 ordered pairs, the 5 other full orderings). Everything else is held
identical to the witness run: figure→figure rendering, the working-surface elicitation (`FINAL:`-tag
parser, `MAX_TOKENS` 1024, gemini `effort: minimal` **held constant**), the two arms, `TERM`, the
thresholds, the symmetric verdict map, and the **THIN** adjudication.

**Why the 0.50 ceiling carries over.** With three moves there are 3!=6 orderings. A reader that fails to
order **all three** moves by their stamps can pin at most one move's slot from the stamps and must fill
the remaining two-move sub-order from the print/display order (decoupled from stamps) — producing the
true ordering exactly **half** the time. So every such **half-composer** scores exactly **0.50**; every
fixed canonical order and the print-order reader score **1/6**; every start / single-move / ordered-pair
/ reversed-order reader scores **0**; every figure / position picker scores **1/K = 1/6**. Beating 0.50
(Wilson-95 LB > 0.50) requires ordering all three moves by their stamps — the same bar as the two-move
runs, on a strictly deeper task. (`build_trials.assert_balance` brute-forces the full reader family;
`fixtures/make_fixtures.py` tests the verdict logic end-to-end, the half-composer fixture landing at
exactly 0.50 and reading as a null.)

- **COMP (headline, spontaneous):** the three stamped move-lines are shown (display order decoupled) and
  the query does **not** state the order; only ordering all three by the round stamps clears 0.50. A
  working surface does not make COMP non-spontaneous — the query still does not state the order.
- **DIRECT (on-demand gate):** order stated ("first … then … and then …"). Gate `direct_acc ≥ 0.80` —
  the **empirical arbiter** of whether three moves are composable at all in this instrument (it
  self-calibrates the depth-3 difficulty; a model that fails DIRECT yields an UNINTERPRETABLE COMP).

An **independent pre-run critic** (fresh agent) returned **GO**: it recomputed the three permutations
(each a derangement, pairwise non-commuting, generating S6), independently enumerated all 16 sub-paths
per config and confirmed all 6 configs **strict-isolated** with six distinct targets, recomputed the
full reader family over the 72 COMP records (stamp-order composer = 1.000; every canonical and the
print-order reader = 0.1667; every half-composer = 0.5000; start/single-move/ordered-pair/reversed = 0;
figure/position pickers = 0.1667), and — adversarially — **could not construct any non-composing reader
beating 0.50** (pinning two of three slots from the stamps forces the third, i.e. becomes a full
composer; the only oracle keyed on genuinely non-composing cues hit 0.597 with Wilson-LB 0.4818 ≤ 0.50,
not clearing the bar). It confirmed the parser is target-blind, the frozen sha matches, and — concurring
with the design — ruled **no new decision owed** (the ratified
[`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md)
adopted non-commuting-operation semantics agnostic to which group realizes them and did not freeze the
move count; the generic-permutation switch is the same class of within-frame variation as the alt-pair
D4→A4 change).

## Results (3 models, 108 records/model, 0 NA, 0 retried, 0 length-truncation; independently reproduced)

An **independent post-run verifier** (fresh agent) recomputed every number from raw with its own Wilson,
re-derived the three-move geometry from `track`+`start_idx`+`stamp_moves` with its own permutation code,
and re-parsed every reply with an independent `FINAL:`-tag extractor: **REPRODUCED** — 108/108
geometry fields matched (target / reversed / single-move ends), **324/324 picks matched** the stored
picks, 0 NA / 0 retried / 0 length-truncation, and the billed total $0.80303 confirmed with 0
missing-cost fields. Its own Wilson gave the same verdicts (claude/gemini COMP 72/72 LB 0.9493; gpt
COMP 65/72 LB 0.8126 > 0.50).

| model | DIRECT on-demand acc (gate 0.80) | COMP target rate (bar: Wilson-LB > 0.50) | verdict |
|---|---|---|---|
| **claude-sonnet-4.6** | **1.000** [0.904, 1.000] PASS | **1.000** (72/72) [0.949, 1.000] → sig | **RESPECTS-ORDER** |
| **gemini-3.5-flash** | **1.000** [0.904, 1.000] PASS | **1.000** (72/72) [0.949, 1.000] → sig | **RESPECTS-ORDER** |
| **gpt-5.4-mini** | **1.000** [0.904, 1.000] PASS | **0.903** (65/72) [0.813, 0.952] → sig | **RESPECTS-ORDER** |

**Composition across depth** — the on-demand gate (DIRECT) and spontaneous composition (COMP), across
the now-tested axes (all working-surface; gpt is the only model not at ceiling, so the trend shows on
it):

| model | depth-2, K=4 STEP/FLIP (witness) | depth-2, K=4 CYCLE/SWAP (alt-pair) | depth-2, K=6 STEP/FLIP | **depth-3, K=6 generic (this run)** |
|---|---|---|---|---|
| claude | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 1.000 | **1.000 / 1.000** |
| gemini | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 1.000 | **1.000 / 1.000** |
| gpt | 0.969 / 0.953 | 1.000 / 0.906 | 1.000 / 0.861 | **1.000 / 0.903** |
(DIRECT / COMP)

**COMP failure breakdown** (spontaneous arm): claude and gemini perfect (72/72; all diagnostic
non-target rates 0.000). **gpt's 7 misses** (65/72 = 0.903) all fall on **reverse-printed** records
(display order ≠ stamp order — exactly where the ordering decision bites); none is a clean single-move
read on a stamp-printed record. The post-run verifier characterized them by reading gpt's working: they
are predominantly **single mis-applied table lookups / move-label slips** — gpt **re-sorts the moves to
stamp order correctly** but then mis-reads one figure→figure transition, or lets a display-order move
intrude into one slot — with **one** clear reversed-order slip (rid 2). So they are **not** a systematic
reader (no single-move-reading signature, no consistent reversed/print-order strategy); each wrong
figure coincides with one or more diagnostic ends only because with six figures a single mistaken
endpoint often lands on several competing readers at once. gpt's DIRECT (order stated) stays at
**ceiling (36/36)**, so it composes three moves reliably on demand; it spontaneously picks the correct
three-move order 90.3% of the time.

### CoT genuineness (decisive)

On the **decoupled** COMP records (display order ≠ stamp order — where a print-order reader lands OFF
target), the post-run verifier read the visible working and found genuine three-move stamp-order
composition: **claude 60/60, gemini 60/60, gpt 53/60 on-target**, with the ceiling models explicitly
re-sorting the three moves by round number before applying them. Verbatim (verifier-confirmed):

- **claude rid 0** (display SLIDE,TWIST,FLIP; rounds 2,5,9): *"The moves should be applied in
  chronological order (lowest round number first): Round 2: FLIP / Round 5: SLIDE / Round 9: TWIST"* —
  then traces diamond→star→square→triangle (target).
- **gemini rid 2** (display FLIP,TWIST,SLIDE; rounds 3,6,10): *"track its moves in chronological order
  based on the round numbers (from lowest to highest). The chronological order of the rounds is:
  1. Round 3: FLIP, 2. Round 6: SLIDE, 3. Round 10: TWIST"* — then circle→triangle→heart→square (target).
- **gpt rid 0**: *"Apply the moves in round order from earliest to latest: Round 2: FLIP… Round 5:
  SLIDE… Round 9: TWIST…"* — correct three-move stamp-order composition.

So the COMP signal is genuine stamp-order composition of all **three** moves, not a print-order
coincidence or a two-move shortcut. A representative gpt **miss** (rid 9, target star, pick circle): gpt
correctly sorts to the FLIP,TWIST,SLIDE stamp order but then **mis-labels/mis-applies** the transitions
(applying the moves' tables in the wrong correspondence), yielding the wrong figure — a table-lookup
slip, not a parse artifact and not a single-move read.

## Reading (honest, bounded)

1. **The witness survives a deeper serial load — depth does not defeat the channel.** With a working
   surface, all three models compose **three** non-commuting moves in stamp order, not just two. So the
   working-surface composition capacity is not a two-step artifact: it extends to depth three. Combined
   with the alt-pair (operation pair) and K=6 (grid size) runs, the capacity now holds across **three**
   generality axes — pair, grid size, and **depth**. This is the **further support**
   [`essay/output-channel-confound`](../essays/output-channel-confound.md)'s "capacity, not artifact"
   reading needed, on the axis [`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md)
   predicted would be load-bearing.
2. **The output-channel-confound trigger-(b) contrast returns NEGATIVE for a depth-3 bound.** Trigger
   (b) asked for a serial-computation negative that **survives** the wide channel (a channel-controlled
   bound). Depth three did not produce one: the wide channel absorbed the deeper load, exactly as
   [`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md)'s serial-computation account
   predicts a scratchpad should. So the line still has **no** channel-controlled composition bound — the
   working surface remains sufficient at every depth and size tested. (This does not *foreclose* such a
   bound; deeper still, or other instruments, may yet find one. A behavioral positive is not a ceiling
   any more than a negative is — per [`essay/undischargeable-negative`](../essays/undischargeable-negative.md).)
3. **The suggestive state-size dip did not continue into depth.** The K=6 run flagged a monotone gpt
   COMP dip with state size (0.953 → 0.906 → 0.861). At depth three (a different, generic-permutation
   instrument), gpt COMP is **0.903** — on par with the two-move alt-pair/K=6 instruments, not lower. So
   a deeper *serial load* did **not** erode gpt's spontaneous ordering further on this instrument. Read
   cautiously: the depth-3 run uses a different operation set (generic S6 permutations, not the dihedral
   family), so it is **not** a clean continuation of the same dip series — it is a different instrument
   that happens to sit in the same 0.86–0.95 band. The honest summary is that gpt's spontaneous-ordering
   reliability stays in that band across all four working-surface instruments, with on-demand
   composition at ceiling throughout.
4. **Still THIN; still no capability split; still no human comparison.** The verdict remains "respects
   operation order" (single-reader-recoverable; the stamped three-move list and the maps are in the
   record), **not** rung (iii). The panel is concordant at depth three. `anchor: internal-contrast-only`;
   no claim about people.

## What this adds to the witness-search record

- **(i) Axes now tested for generality of the witness:** operation pair (STEP/FLIP → CYCLE/SWAP) →
  replicates; grid size (K=4 → K=6) → replicates; **composition depth (2 → 3 moves) → survives** (this
  run). Still untested: still deeper composition (≥4 moves), partially-conflicting refinements, image
  referents, cross-family dyads.
- **(ii) Bound on the capacity reading:** the working-surface composition now holds on two non-commuting
  pairs (D4, A4), two grid sizes (K=4, K=6), and **two depths (2, 3 moves)**. It remains one
  operationalization family (figure→figure lookup tables, text-only, three-model panel, single run per
  cell).
- **(iii) The thin/rich gap is untouched:** rung (iii) stays documented structurally closed for
  text-only stimuli; this result is on the thin side by construction (adjudicated before the run).
- **(iv) The trigger-(b) hunt continues:** no channel-controlled composition bound has been found at any
  depth/size tested. If one is wanted, the next move is **deeper still** (≥4 moves) or a qualitatively
  harder serial demand — but note each deeper instrument needs fresh shortcut-proofing (the competing
  reader set grows with depth).

## Honesty box

- **What this shows:** with a step-by-step working surface, **all three** panel models perform
  order-sensitive composition of **three** non-commuting moves at/near ceiling (claude/gemini 1.000; gpt
  DIRECT 1.000 / COMP 0.903), spontaneously ordering by round stamps. The working-surface composition
  witness **survives a deeper serial load**; the output-channel-confound trigger-(b) contrast (a negative
  that survives the wide channel) returns **negative** for a depth-3 bound.
- **What it does NOT show:** rung (iii) / constitution (the verdict is **THIN**, single-reader-
  recoverable). It does not show composition *without* a working surface. It does not establish that no
  depth ever defeats the channel — only that depth three does not (a positive is not a ceiling). It does
  not extend to non-figure referents or cross-family dyads. It makes **no** claim that one model is
  stronger than another (panel concordant). gpt's COMP is 0.903, not ceiling; its 7 misses (all on
  reverse-printed records) are predominantly single mis-applied table lookups after a correct
  stamp-order re-sort, not failures to chain or to order (DIRECT at ceiling 36/36).
- **Genuine, not parsing:** 324/324 replies parsed via the target-blind `FINAL:` tag; 0 NA, 0 retried,
  0 length-truncation; the COMP signal survives the reverse-printed records (the visible working
  explicitly re-sorts the three moves by round stamp — see CoT section, verifier-confirmed).
- **No human comparison** made or owed: `anchor: internal-contrast-only` (a within-model contrast over
  balanced, order-permuted content).
- **Spend:** **$0.80303 billed** (`usage.cost`-summed, 0 missing; liveness $0.00554 + claude $0.38889 +
  gemini $0.33902 + gpt $0.06958). Pre-flight ≈ $1.0–1.4; came in under (claude/gemini CoT the drivers).
  $1.80 hard stop never approached. **Day total 2026-06-19 ≈ $3.07 of $5.00** (this run $0.80 + the
  witness $0.74 + alt-pair $0.74 + K=6 $0.80 earlier the same UTC day).
