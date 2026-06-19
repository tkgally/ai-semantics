# PREREG — THREE-MOVE (deeper-composition) order-sensitive composition probe

## What this is (the >2-move DEPTH axis: does the working-surface composition WITNESS survive a deeper serial load?)

Every prior Option-C run composed exactly **two** non-commuting moves. The working-surface run
([`2026-06-19-relational-order-composition-c-reasoning-scaffold`](../2026-06-19-relational-order-composition-c-reasoning-scaffold/),
[`result/relational-order-composition-c-reasoning-scaffold`](../../../wiki/findings/results/relational-order-composition-c-reasoning-scaffold.md))
found a **WITNESS**: opening a **working surface** (step-by-step output permitted, `FINAL:`-tag parsed;
reasoning-effort knob held constant) flipped **both** gemini (DIRECT 0.656→1.000) and gpt (0.250→0.969)
from UNINTERPRETABLE to **RESPECTS-ORDER** on the two-move task. The **alt-pair** (A4) and **larger-grid**
(K=6) runs then **replicated** a two-move composition **capacity** over the operation-pair and grid-size
axes. [`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md) draws the
general lesson (the output channel is a capability-masker) and — grounded by
[`source/li-2024-cot-serial`](../../../wiki/base/sources/li-2024-cot-serial.md) (chain-of-thought lets a
transformer perform inherently **serial** computation a forced single token cannot) — predicts the
load-bearing axis is serial **depth**. The honest signal from the K=6 run: gpt COMP **dipped**
(0.953→0.906→0.861) across the three working-surface two-move instruments (DIRECT at ceiling throughout;
overlapping CIs → suggestive only).

**This probe adds the DEPTH axis directly: THREE stamped non-commuting moves instead of two.** It is the
[`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md) **trigger-(b)
contrast case** — does a serial-depth gap **survive** the wide working-surface channel (a
**channel-controlled** bound, a real limit) or does the working surface absorb the deeper load too
(composition capacity extends to depth 3)?

**The single manipulated variable vs the working-surface witness run is the NUMBER OF MOVES (2 → 3).** As a
**forced consequence**, the dihedral STEP/FLIP pair is replaced by **three generic non-commuting
permutations** of the six figures (the dihedral group is too structured to shortcut-proof at three moves:
its products collapse, so no K≤12 config isolates the true ordering — verified by exhaustive search). The
working-surface elicitation (`FINAL:`-tag parser, `MAX_TOKENS=1024`, gemini `effort: minimal` held
constant), the two arms (COMP + DIRECT), `TERM`, the figure→figure rendering, the `PRINT_CEILING = 0.50`
bar, the symmetric verdict map, and the THIN adjudication are **all held identical**.

### Why the 0.50 ceiling carries over from the two-move instrument

With three moves there are 3! = 6 orderings. A reader that fails to order **all three** moves by their
stamps can pin at most **one** move's slot from the stamps and must fill the remaining two-move sub-order
from the print/display order (decoupled from stamps). It produces the true ordering only when that
remaining sub-order happens to match — exactly **half** the time. So every such **half-composer** scores
**exactly 0.50**; every fixed canonical order and the print-order reader score **1/6**; every start /
single-move / ordered-pair / reversed-order reader scores **0**; every figure / position picker scores
**1/K = 1/6**. **Only ordering all three moves by their stamps clears 0.50** (a genuine stamp-order composer
scores 1.0). This is the same 0.50 bar as the two-move runs, with the same interpretive force — but beating
it now requires composing **three** moves, not two.

## Reading the outcome (per model; the DIRECT gate is the empirical arbiter of THREE-move composability)

- **DEPTH SURVIVES THE CHANNEL** (all three clear DIRECT ≥ 0.80 and RESPECTS-ORDER at depth 3): the
  working-surface composition capacity **extends to three moves** — strengthens
  [`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)'s "capacity,
  not artifact" reading on the **depth** axis; the trigger-(b) contrast comes back **negative** for a
  depth-3 bound.
- **DEPTH DEFEATS THE CHANNEL** (a model that cleared DIRECT at depth 2 fails it at depth 3): a serial-depth
  gap that **survives the wide working-surface channel** — the **first channel-controlled** composition
  bound the line has found, exactly the
  [`essay/floor-is-not-a-ceiling`](../../../wiki/findings/essays/floor-is-not-a-ceiling.md) objection (B) /
  [`essay/capability-split`](../../../wiki/findings/essays/capability-split.md) trigger-(b) contrast case,
  and consistent with [`source/li-2024-cot-serial`](../../../wiki/base/sources/li-2024-cot-serial.md)'s
  serial-depth prediction. Still **undischargeable** (per
  [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md) — a
  behavioral negative is never a capacity verdict) and still **thin**.
- **claude = positive control**: should still clear DIRECT (ideally RESPECTS-ORDER); a claude failure would
  mean the deeper instrument broke, not that the others are limited.

The **DIRECT gate is the empirical arbiter** — the difficulty of the deeper load is **measured** (DIRECT
acc), not assumed; the instrument self-calibrates difficulty.

## Frozen stimuli

- `stimuli.json` rstrip-sha256 = **`eae2a2ab11d8d54092c23e8a9adc9b7da596a068032c0baca2254e2d0b6d774a`**
  (`probe._require_frozen` hashes the rstrip'd bytes).
- Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. **108 unique records** (72 COMP + 36
  DIRECT), each served to **3 models → 324 finding-bearing calls**.

## Design (three generic non-commuting permutations on a SIX-figure track; figure-to-figure, working-surface)

K=6 distinct figures (triangle, circle, square, star, diamond, heart). "DAX" starts on a stated figure;
**three** stamped moves from {FLIP, SLIDE, TWIST}, each a permutation of the six positions rendered as a
figure→figure lookup table (no positions shown). The three moves carry **no inherent order**; the order
comes only from the round stamps.

- **Move permutations (position → position, 0-indexed):** `FLIP=[1,5,4,2,0,3]`, `SLIDE=[4,2,5,0,3,1]`,
  `TWIST=[3,0,1,5,2,4]`. Each a **derangement** (no figure maps to itself); **pairwise non-commuting**;
  ⟨FLIP,SLIDE,TWIST⟩ acts so that the six orderings spread.
- **The 6 strict-valid base configs** `CONFIGS = [(3,FLIP·SLIDE·TWIST), (1,FLIP·TWIST·SLIDE),
  (4,SLIDE·FLIP·TWIST), (2,SLIDE·TWIST·FLIP), (0,TWIST·FLIP·SLIDE), (5,TWIST·SLIDE·FLIP)]` — **exactly one
  start per ordering**, targets falling one each on track positions {4,3,1,0,5,2} (all six, balanced). For
  each config the true-stamp-order endpoint is hit by **NO other sub-path** among all 16 (start + 3 singles
  + 6 ordered pairs + 5 other full orderings) — re-proven at build by `strict_isolated`.
- COMP = 6 configs × 2 reps × K = **72**; DIRECT = 6 configs × 1 rep × K = **36**. Each block cycles the
  target **figure** through all 6 shapes once (figure uniform) and cycles all 6 **display permutations** of
  the move-lines once (display order decoupled from stamp order).

- **COMP (headline):** "Which figure does DAX sit on now?" — order **not** stated. Score `target_rate =
  P(pick == stamp-order end figure)`. Diagnostics: `rev` (reversed order), `print` (display order), `start`,
  single-move (×3).
- **DIRECT (gate):** order stated explicitly ("first … then … and then …"). Score `direct_acc`.

## Pre-registered thresholds (frozen, identical to the working-surface runs)

- `PRINT_CEILING = 0.50` — every half-composer / canonical / print reader caps at or below this (proven at
  build); the **half-composer hits exactly 0.50**.
- `DIRECT_FLOOR = 0.80` — on-demand THREE-move composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.1667` (figure-identity chance).

## Verdict map (frozen, per model — identical to the working-surface runs)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (deeper, 3-move composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution.

## Shortcut-proofing (certified pre-run)

`build_trials.assert_balance` (PASS): per-record integrity (track a permutation, rounds strictly
increasing, config strict-isolated); target figure uniform (= 1/6); target track position balanced (picker
≤ 1/6); true stamp-order balanced (each of 6 orderings equally frequent); display order balanced (each of 6
perms equally frequent); start / each single-move / **each of the 6 ordered-pair** / reversed-order readers
= **0**; **each of the 6 canonical full-order readers and the print-order reader = 1/6**; **each
half-composer (3 display-fill + 18 canon-fill) ≤ 0.50, the display-fill half-composers exactly 0.50**;
genuine stamp-order composer = **1.0**; the max non-composition reader = exactly `PRINT_CEILING` 0.50.
`fixtures/make_fixtures.py` (**ALL FIXTURE ASSERTS PASS**): only genuine three-move stamp-order composition
yields RESPECTS-ORDER; the strongest non-composer (half-composer) scores exactly 0.50 and reads as a null;
canonical/print = 1/6; position/identity = 1/K; any reader failing on-demand → UNINTERPRETABLE. The
`FINAL:`-tag parser is target-blind.

## Spend (frozen)

Working-surface format, a third move lengthens the chain-of-thought. Pre-flight ≈ **$1.0–1.4 billed** (the
K=6 two-move run billed $0.80 for the same 324 calls; deeper CoT raises output tokens; gemini held at
`effort: minimal`). `HARD_STOP_USD = 1.80` on projected total. Record actual `usage.cost` after. Day total
before this run = **≈$2.27 of $5.00** (2026-06-19); a ~$1.2 run keeps the day total ≈$3.5, under cap.

## Anti-cheat

The verdict map is symmetric and pre-registered: depth-survives and depth-defeats are **both** fully
reportable; neither is "the win", and **neither reaches rung (iii)** (adjudicated thin before the run). No
threshold may be retuned after seeing data. The instrument changes from the working-surface run **only by
the number of moves (2 → 3)** and the forced switch to a shortcut-proofable generic permutation set; the
rendering, format, parser, thresholds, and verdict map are unchanged. `anchor: internal-contrast-only`;
**no human-comparison claim.**

**Governance (surfaced for the critic).** This is a within-frame **depth** variation of the already-ratified
Option-C instrument under
[`decisions/resolved/relational-rung-iii-path-dependence`](../../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
and the ratified `internal-contrast-only` posture — the stamp-order = composition semantics, the
figure→figure rendering, the working-surface format, the 0.50 ceiling, the symmetric verdict map, and the
THIN adjudication are all preserved. Like the K=4 scale, the figure rendering, the worked-example scaffold,
the gpt third-model extension, the working-surface easing, the alt-pair operation pair, and the K=6 grid
size — none of which owed a new decision — the **move count** is not a parameter that decision froze. The
number-of-moves change is **surfaced** here; the design's judgement is **no new `wiki/decisions/open/`
entry is owed**. The independent pre-run critic gates this judgement and may rule otherwise — **if it judges
a decision is owed, open one and mark the result `contingent`.**

## Independent pre-run critic

**GO** (fresh independent agent, 2026-06-19, before any finding-bearing call; recomputed all geometry,
the reader family, Wilson, prompt rendering, and the sha from scratch — did NOT import the run's
`apply_seq`/`op`/`PERMS`). Independently confirmed: FLIP/SLIDE/TWIST are each bijections of {0..5},
each a **derangement**, **pairwise non-commuting**, and ⟨FLIP,SLIDE,TWIST⟩ generates the **full S6
(order 720)** — orderings spread maximally. All 16 sub-paths enumerated per config: all **6 configs
strict-isolated** (true-stamp-order endpoint hit by none of the other 15 paths, and ≠ start); targets
= {0,1,2,3,4,5} (6 distinct positions); the 6 orderings cover S3 exactly once. Over the 72 COMP records
(endpoints recomputed independently): genuine stamp-order composer = **1.0000**; all 6 canonical
full-order readers = **0.1667**; print/display reader = **0.1667**; the 3 display-fill half-composers =
**0.5000**, max over all 18 canon-fill half-composers = **0.5000**; start / each single-move / max
ordered-pair / reversed-order = **0.0000**; max constant-figure and max track-position pickers =
**0.1667**. **Could not construct ANY non-composing reader beating 0.50:** an adversarial brute force
over ordering-rules keyed on round-rank patterns confirmed that pinning 2 of 3 slots from the stamps
forces the 3rd (only one move remains) ⇒ a full composer (1.0), so there is **no systematic
non-composing strategy strictly between 0.50 and 1.0**; an apparent "0.833 non-composer" was a *partial*
composer (orders by stamps on 5/6 round-rank patterns, deviates on 1 — genuine composition the bar is
meant to credit); the only oracle keyed on genuinely non-composing cues, `(start_shape, display-order)`,
hit 0.597 with **Wilson-LB 0.4818 ≤ 0.50** — does not clear the bar. **The 0.50 ceiling is clean.**
Rendering: figure→figure tables match an independent derivation from each record's `track`+PERMS (0
mismatches over 108×3×6); no position/index/slot words leak; COMP omits the order; DIRECT states the
order matching each record's stamp order; FINAL-tag instruction present; `parse_forced` **target-blind**
(10 hand cases + length-truncation: last-tag-wins, last-line fallback, non-present tags ignored,
ambiguous last line → None, `finish_reason=="length"` never parsed). rstrip-sha256 =
`eae2a2ab…0b6d774a`, matching PREREG and `probe._require_frozen`. DIRECT (n=36): target 1.0, start 0,
reversed 0; COMP figure/position/order/display balanced. `build_trials.py` + `fixtures/make_fixtures.py`
re-run clean (matching sha, all balance asserts pass, ALL FIXTURE ASSERTS PASS). Diffed vs the K=6
two-move run: substantive changes are exactly (a) move count 2→3 and (b) the **forced** operation-set
switch (dihedral STEP/FLIP → three generic permutations, since the dihedral group's products collapse
at three moves and cannot be shortcut-proofed — confirmed), plus the half-composer machinery and
`HARD_STOP_USD` 1.50→1.80; `parse_forced` byte-identical in code, MAX_TOKENS / DIRECT_FLOOR /
PRINT_CEILING / POS_CHANCE / REASONING (gemini effort minimal) held constant. **Governance: no new
`wiki/decisions/open/` entry owed** — concurs with the design: the ratified
`decisions/resolved/relational-rung-iii-path-dependence` adopted Option C (non-commuting operation
semantics, agnostic to which group realizes them), froze the THIN adjudication and `internal-contrast-only`
anchor (preserved verbatim here), and did not freeze the move count; the generic-permutation switch is
the same class of within-frame variation as the alt-pair (D4→A4) operation-pair change, and the depth
change introduces no new value-laden choice (the deeper load is *measured* by the DIRECT gate, not
assumed). Spend sane and within budget (`HARD_STOP_USD=1.80` is on the run's projected total; even at
the cap the day total ≈$4.07 < $5.00). **No BLOCKER, no SHOULD-FIX**; one NIT (this critic-section
placeholder — now filled).
