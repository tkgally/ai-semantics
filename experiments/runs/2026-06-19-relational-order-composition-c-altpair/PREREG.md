# PREREG — ALT-PAIR GENERALITY order-sensitive composition probe (a DIFFERENT non-commuting pair)

## What this is (a generality test of the working-surface composition WITNESS over the operation pair)

The execution-format (working-surface) run
([`2026-06-19-relational-order-composition-c-reasoning-scaffold`](../2026-06-19-relational-order-composition-c-reasoning-scaffold/),
[`result/relational-order-composition-c-reasoning-scaffold`](../../../wiki/findings/results/relational-order-composition-c-reasoning-scaffold.md))
found a **WITNESS**: on the byte-identical figure-to-figure trials, opening a **working surface**
(step-by-step output permitted, `FINAL:`-tag parsed; reasoning-effort knob held constant) flipped
**both** gemini (DIRECT 0.656→1.000) and gpt (0.250→0.969) from UNINTERPRETABLE (forced single-token)
to **RESPECTS-ORDER** at/near ceiling, so all three panel models compose the two non-commuting moves
given a place to externalize the execution. [`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)
draws the general lesson (the output channel is an instrument axis, a capability-masker) and claims the
dissolution reflects a composition **capacity**, not an artifact of the one STEP/FLIP instrument.

**That generalization is the open question this probe tests, on a single substantive change: the
operation pair.** Every prior Option-C run — including the witness run — used the **dihedral** pair
STEP (the 4-cycle `p→(p+1)%4`) and FLIP (the reflection `p→3−p`), which generate **D4**. This run
swaps that pair for a **genuinely different** non-commuting pair:

- **CYCLE** : the 3-cycle `(1 2 3)` on the 4 track positions (0 fixed; 1→2, 2→3, 3→1).
- **SWAP**  : the double transposition `(0 1)(2 3)` (positions 0↔1 and 2↔3).

CYCLE and SWAP generate **A4** (the alternating group), **not** the dihedral D4 — a different group, a
different cycle structure (a 3-cycle + a double transposition vs. a 4-cycle + a reflection). They **do
not commute** (verified at all 4 starts: CS-end ≠ SC-end for every start). So this is a generality
test over the operation pair, **not** a relabeling of the same pair.

**Everything else is held identical to the witness run:** K=4, the figure-to-figure rendering, the
working-surface elicitation (`FINAL:`-tag parser, `MAX_TOKENS=1024`, gemini `effort: minimal` held
constant), the two arms (COMP + DIRECT), `SHAPES`, `TERM`, `ROUND_PAIRS`, the thresholds, the symmetric
verdict map, and the thin adjudication. Only the two permutations (with honest model-facing labels
CYCLE/SWAP) and the balanced `VALID_CONFIGS` differ; the stimuli are **freshly built** (a new sha256).

## Reading the outcome (per model; the DIRECT gate is the empirical arbiter of composability)

- **REPLICATES** (all three clear DIRECT ≥ 0.80 and RESPECTS-ORDER on the alt pair): the working-
  surface composition witness **generalizes beyond** the specific STEP/FLIP pair — strengthens
  [`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)'s
  "capacity, not one-instrument artifact" reading and the
  [`essay/floor-is-not-a-ceiling`](../../../wiki/findings/essays/floor-is-not-a-ceiling.md) trigger-(b)
  generalization.
- **DOES NOT REPLICATE** (a model that cleared DIRECT on STEP/FLIP fails it here): the witness is
  **pair-specific** — a working surface does not by itself confer composition on an arbitrary non-
  commuting pair; **bounds** the generalization (still **undischargeable**, per
  [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md) — a
  behavioral negative is never a capacity verdict).
- **claude = positive control**: should still clear DIRECT (ideally RESPECTS-ORDER); a claude failure
  would mean the alt pair broke the instrument, not that the others are limited.

The **DIRECT gate is the empirical arbiter of composability on THIS pair** — the easiness/difficulty of
the alt pair is **measured** (DIRECT acc), not assumed; the instrument self-calibrates difficulty.

## Frozen stimuli

- `stimuli.json` rstrip-sha256 = **`f21f0cfbd1154cb09461c2e32e4c200a62d65ba416e4309d80daaade8c5222bb`**
  (`probe._require_frozen` hashes the rstrip'd bytes). **Differs** from the STEP/FLIP runs (different
  operation pair).
- Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. **96 unique records** (64 COMP + 32
  DIRECT), each served to **3 models → 288 finding-bearing calls**.

## Design (DIFFERENT non-commuting operation pair; figure-to-figure rendering, working-surface format)

K=4 distinct figures. "DAX" starts on a stated figure; two stamped moves from {CYCLE, SWAP}
(non-commuting), each rendered as a figure→figure lookup table (no positions). The 4 valid base configs
`VALID_CONFIGS = [(3,"CS"),(2,"SC"),(0,"SC"),(1,"CS")]` fall one each on the 4 target track positions,
order balanced 2 CS / 2 SC. COMP = 4 configs × 4 reps × K = 64; DIRECT = 4 configs × 2 reps × K = 32.

- **COMP (headline):** "Which figure does DAX sit on now?" — order not stated. Score `target_rate =
  P(pick == stamp-order end figure)`. Diagnostics: `swapped` (reversed-order), `start`, `cycle1`
  (CYCLE-only), `swap1` (SWAP-only).
- **DIRECT (gate):** order stated explicitly ("first … then …"). Score `direct_acc`.

## Pre-registered thresholds (frozen, identical to the witness run)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.25` (figure-identity chance).

## Verdict map (frozen, per model — identical to the witness run)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution.

## Shortcut-proofing (re-certified pre-run for the CYCLE/SWAP pair)

`build_trials.assert_balance` (PASS): target figure uniform (= 1/K); target track position uniform
(picker ≤ 1/K); print-order & both canonical-order (always-CS, always-SC) readers = exactly 0.50;
start / single-move (CYCLE-only, SWAP-only) / reversed-order readers = 0; frequency flat.
`fixtures/make_fixtures.py` (**ALL FIXTURE ASSERTS PASS**): only genuine stamp-order composition yields
RESPECTS-ORDER; every print/canonical reader 0.50; every position/identity reader 1/K; any reader
failing on-demand → UNINTERPRETABLE. The fixtures test `analyze.py`'s logic, which is rendering- and
format-invariant. The `FINAL:`-tag parser is inherited byte-identical from the witness run (already
unit-tested; target-blind).

## Spend (frozen)

Working-surface format, same scale as the witness run ($0.735 billed). Pre-flight ≈ **$0.8–1.0 billed**
(288 calls; claude CoT the driver; gemini held at `effort: minimal`). `HARD_STOP_USD = 1.50` on
projected total. Record actual `usage.cost` after. Day total before this run = **$0.735 of $5.00**
(2026-06-19); this run keeps the day well under cap.

## Anti-cheat

The verdict map is symmetric and pre-registered: a replication and a non-replication are **both**
fully reportable; neither is "the win", and **neither reaches rung (iii)** (adjudicated thin before the
run). No threshold may be retuned after seeing data. The instrument changes from the witness run
**only by the non-commuting pair** (CYCLE/SWAP for STEP/FLIP) and the balanced configs; the rendering,
format, parser, thresholds, and verdict map are unchanged. `anchor: internal-contrast-only`; **no
human-comparison claim.** **Governance (provisional):** a within-frame generality variation of the
already-ratified Option-C instrument under
[`decisions/resolved/relational-rung-iii-path-dependence`](../../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
and the ratified `internal-contrast-only` posture — the same kind of within-frame variation as the K=4
scale, the figure rendering, the worked-example scaffold, the gpt third-model extension, and the
working-surface easing, none of which owed a new decision; the operation pair is not a parameter that
decision froze. **No new `wiki/decisions/open/` entry owed** — but the independent pre-run critic gates
this judgement and may flag otherwise.

## Independent pre-run critic

*(to be filled by the fresh independent agent before any finding-bearing call)*
