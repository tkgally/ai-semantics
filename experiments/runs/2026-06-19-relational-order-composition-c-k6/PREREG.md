# PREREG — LARGER-GRID (K=6) GENERALITY order-sensitive composition probe (same dihedral pair, bigger grid)

## What this is (a generality test of the working-surface composition WITNESS over the GRID SIZE K)

The execution-format (working-surface) run
([`2026-06-19-relational-order-composition-c-reasoning-scaffold`](../2026-06-19-relational-order-composition-c-reasoning-scaffold/),
[`result/relational-order-composition-c-reasoning-scaffold`](../../../wiki/findings/results/relational-order-composition-c-reasoning-scaffold.md))
found a **WITNESS**: on the figure-to-figure trials, opening a **working surface** (step-by-step output
permitted, `FINAL:`-tag parsed; reasoning-effort knob held constant) flipped **both** gemini (DIRECT
0.656→1.000) and gpt (0.250→0.969) from UNINTERPRETABLE (forced single-token) to **RESPECTS-ORDER** at
near ceiling, so all three panel models compose the two non-commuting moves given a place to externalize
the execution. The **alt-pair** run
([`result/relational-order-composition-c-altpair`](../../../wiki/findings/results/relational-order-composition-c-altpair.md))
then **replicated** that on a genuinely different non-commuting operation pair (A4 vs D4).
[`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md) draws the
general lesson (the output channel is an instrument axis, a capability-masker) and claims the dissolution
reflects a composition **capacity** — not an artifact of the one STEP/FLIP instrument and not of K=4. The
operation-pair axis is discharged; the **grid-size axis** is the next generality question, and is the one
this probe tests.

**The single substantive change vs the witness run is the grid size K (4 → 6).** Every prior Option-C
run used a K=4 track (the dihedral group **D4**). This run keeps the **same dihedral pair** STEP (the
K-cycle `p→(p+1)%K`) and FLIP (the reflection `p→(K-1)−p`) — the very pair the witness run used — but on a
**six-figure track**, so STEP and FLIP now generate **D6** (order 12 vs D4's 8): a larger answer space
(figure-identity chance drops 1/4 → 1/6) and a larger position space to track. STEP and FLIP are K-general
functions (`op_step`/`op_flip` read `C.K`), so the only substantive changes are `K=6`, the six-figure
`SHAPES`, and the re-enumerated balanced `VALID_CONFIGS`. The stimuli are **freshly built** (a new sha256).

**Everything else is held identical to the witness run:** the figure-to-figure rendering, the working-
surface elicitation (`FINAL:`-tag parser, `MAX_TOKENS=1024`, gemini `effort: minimal` held constant), the
two arms (COMP + DIRECT), `TERM`, `ROUND_PAIRS`, the thresholds, the symmetric verdict map, and the thin
adjudication. **The reader SET is unchanged** (still only two moves: 2 canonical orders + print-order + 2
single-move + reversed-order) — only K changes — so the certification framework carries over unchanged.

## Reading the outcome (per model; the DIRECT gate is the empirical arbiter of composability at K=6)

- **REPLICATES** (all three clear DIRECT ≥ 0.80 and RESPECTS-ORDER at K=6): the working-surface
  composition witness **generalizes beyond K=4** to a larger grid — strengthens
  [`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)'s
  "capacity, not one-instrument artifact" reading on the grid-size axis.
- **DOES NOT REPLICATE** (a model that cleared DIRECT at K=4 fails it here): the working surface's
  sufficiency is **grid-size-bounded** — a larger answer/position space defeats on-demand composition even
  with a scratchpad; **bounds** the generalization (still **undischargeable**, per
  [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md) — a
  behavioral negative is never a capacity verdict).
- **claude = positive control**: should still clear DIRECT (ideally RESPECTS-ORDER); a claude failure
  would mean the larger grid broke the instrument, not that the others are limited.

The **DIRECT gate is the empirical arbiter of composability at K=6** — the difficulty of the larger grid
is **measured** (DIRECT acc), not assumed; the instrument self-calibrates difficulty.

## Frozen stimuli

- `stimuli.json` rstrip-sha256 = **`f4d0e36d70a0815a1b6d1a92f337d0220e97de9a0defed464f17be180ae82b33`**
  (`probe._require_frozen` hashes the rstrip'd bytes). **Differs** from every K=4 run (different K).
- Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. **108 unique records** (72 COMP + 36
  DIRECT), each served to **3 models → 324 finding-bearing calls**.

## Design (dihedral STEP/FLIP on a SIX-figure track; figure-to-figure rendering, working-surface format)

K=6 distinct figures (triangle, circle, square, star, diamond, heart). "DAX" starts on a stated figure;
two stamped moves from {STEP, FLIP} (non-commuting), each rendered as a figure→figure lookup table (no
positions). The **6 valid base configs** `VALID_CONFIGS = [(4,"SF"),(3,"SF"),(1,"SF"),(4,"FS"),(2,"FS"),
(1,"FS")]` fall one each on the 6 target track positions, order balanced 3 SF / 3 FS. COMP = 6 configs ×
2 reps × K = 72; DIRECT = 6 configs × 1 rep × K = 36.

- **COMP (headline):** "Which figure does DAX sit on now?" — order not stated. Score `target_rate =
  P(pick == stamp-order end figure)`. Diagnostics: `swapped` (reversed-order), `start`, `step1`
  (STEP-only), `flip1` (FLIP-only).
- **DIRECT (gate):** order stated explicitly ("first … then …"). Score `direct_acc`.

### Valid-config derivation (enumerated from the K-general ops at K=6)

With STEP=`p→(p+1)%6`, FLIP=`p→5−p`, a config `(start, order∈{SF,FS})` is *valid* iff its stamp-order
target differs from the start, both single-move ends (STEP-only, FLIP-only), and the reversed-order end.
Enumerating all 12 (start, order) pairs gives exactly these valid configs, grouped by target track
position:

| target pos | valid configs |
|---|---|
| 0 | (4,SF) |
| 1 | (3,SF), (5,FS) |
| 2 | (4,FS) |
| 3 | (1,SF) |
| 4 | (0,SF), (2,FS) |
| 5 | (1,FS) |

Positions 0,2,3,5 have a unique valid config (2 forced SF: pos 0,3; 2 forced FS: pos 2,5). Positions 1
and 4 each offer one SF and one FS; choosing `(3,SF)` for pos 1 and `(2,FS)` for pos 4 yields exactly one
config per target position with the order balanced **3 SF / 3 FS**. (The alternative choice `(5,FS)`/`(0,SF)`
is equally balanced; either is sound — the chosen set is frozen above.)

## Pre-registered thresholds (frozen, identical to the witness run)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.1667` (figure-identity chance — lower than K=4's 0.25).

## Verdict map (frozen, per model — identical to the witness run)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution.

## Shortcut-proofing (re-certified pre-run for K=6)

`build_trials.assert_balance` (PASS): target figure uniform (= 1/K = 1/6); target track position uniform
(picker = 1/K); print-order & both canonical-order (always-SF, always-FS) readers = exactly 0.50;
start / single-move (STEP-only, FLIP-only) / reversed-order readers = 0; frequency flat.
`fixtures/make_fixtures.py` (**ALL FIXTURE ASSERTS PASS**): only genuine stamp-order composition yields
RESPECTS-ORDER; every print/canonical reader 0.50; every position/identity reader 1/K; any reader failing
on-demand → UNINTERPRETABLE. The fixtures test `analyze.py`'s logic, which is rendering- and format-
invariant. The `FINAL:`-tag parser is inherited byte-identical from the witness run (target-blind).

## Spend (frozen)

Working-surface format, slightly larger than the witness run (324 vs 288 calls). Pre-flight ≈ **$0.83
billed** (the K=4 witness billed $0.735 for 288 calls; claude CoT the driver; gemini held at
`effort: minimal`). `HARD_STOP_USD = 1.50` on projected total. Record actual `usage.cost` after. Day total
before this run = **$1.47 of $5.00** (2026-06-19); this run keeps the day well under cap (~$2.3 projected).

## Anti-cheat

The verdict map is symmetric and pre-registered: a replication and a non-replication are **both** fully
reportable; neither is "the win", and **neither reaches rung (iii)** (adjudicated thin before the run). No
threshold may be retuned after seeing data. The instrument changes from the witness run **only by the grid
size K** (4 → 6) and the re-enumerated balanced configs; the operation pair, rendering, format, parser,
thresholds, and verdict map are unchanged. `anchor: internal-contrast-only`; **no human-comparison claim.**
**Governance (provisional):** a within-frame generality variation of the already-ratified Option-C
instrument under
[`decisions/resolved/relational-rung-iii-path-dependence`](../../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
and the ratified `internal-contrast-only` posture — the same kind of within-frame variation as the K=4
scale, the figure rendering, the worked-example scaffold, the gpt third-model extension, the working-
surface easing, and the alt-pair operation pair, none of which owed a new decision; K is not a parameter
that decision froze (indeed the original Option-C ran at K=6 before narrowing to K=4 for the witness
search). **No new `wiki/decisions/open/` entry owed** — but the independent pre-run critic gates this
judgement and may flag otherwise.

## Independent pre-run critic

_(pending — to be filled with the fresh independent agent's GO/flag verdict before any finding-bearing call)_
