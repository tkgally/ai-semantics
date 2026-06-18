# PREREG — EASIER (K=4) WITNESS-SEEKING order-sensitive composition probe

## What this is (witness-seeking, not a re-run of the hard instrument)

The K=6 Option-C run ([`2026-06-18-relational-order-composition-c`](../2026-06-18-relational-order-composition-c/))
found a **split**: claude RESPECTS-ORDER at ceiling, but **both** gemini (DIRECT 0.583) and gpt
(DIRECT 0.194) **failed the on-demand DIRECT gate** (< 0.80) → UNINTERPRETABLE for each.
[`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md): re-running
the *same* hard instrument cannot move an UNINTERPRETABLE verdict; only a **witness-seeking probe** (an
**easier** elicitation of the same capability) can flip a negative. This is that probe
([`essay/capability-split`](../../../wiki/findings/essays/capability-split.md) trigger (b); NEXT.md's
single most informative cheap test).

**Single manipulated variable = instrument load (K).** The track shrinks **K=6 → K=4** — the *same*
non-commuting STEP/FLIP pair (dihedral generators of a ring), only smaller: a clean 2-swap mirror
(1↔4, 2↔3; no fixed point), halved state space, fewer distractors. Everything else is unchanged
(prompt skeleton, two arms, shortcut-proofing, symmetric verdict map). The **DIRECT gate is the
empirical arbiter of "easier"** — the easiness claim is *measured*, not assumed.

- **Witness** (gemini/gpt clear DIRECT ≥ 0.80 at K=4): attributes the K=6 failure to instrument load,
  re-opens the COMP order-sensitivity question for them.
- **Non-witness** (DIRECT still fails at K=4): the composition inability is robust to halving the
  instrument; **sharpens** the claude-only reading.
- **claude = positive control**: should still clear DIRECT (and ideally RESPECTS-ORDER); a claude
  failure would mean the instrument is broken, not the others limited.

**Same ratified frame.** A scale parameter (K) of the already-ratified Option-C instrument under
[`decisions/resolved/relational-rung-iii-path-dependence`](../../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
and the already-ratified `internal-contrast-only` posture — exactly as the gpt third-model extension
was the same instrument with a different panel. **No new `wiki/decisions/open/` entry owed**; the
in-session independent pre-run critic gates instrument validity, as for every relational probe.

## Frozen stimuli

- `stimuli.json` sha256 = **`975e31bc4f13aff0e220a44cd709a62821f5a0a6a1cc03883a212debf3ef88ba`**
- Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. 96 records/model (64 COMP + 32
  DIRECT), **3 models → 288 finding-bearing calls**.

## The binding adjudication (carried over unchanged, biased AGAINST the rich reading)

An operation-order gap here is **THIN** (the stamped operation list is in the record;
single-reader-recoverable). A RESPECTS-ORDER positive is a thin **"respects operation order"**
finding — **NOT** rung (iii) / constitution. The rich-side rung (iii) is documented **structurally
closed** for text-only stimuli (a transcript IS a final content+stamps record). Both verdicts thin.

## Design (frozen)

K=4 figures on a stated track; DAX starts on a stated figure; two stamped moves from {STEP:
`p→(p+1)%4`, FLIP: `p→3−p`} (non-commuting). Move-lines displayed in stamp order in half the
records, reversed in half. All 4 shapes present every record (answer space). The 4 valid base
configs fall one each on the 4 target track positions, order balanced 2 SF / 2 FS; COMP = 4 configs
× 4 reps (16 blocks × 4 = 64), DIRECT = 4 configs × 2 reps (8 × 4 = 32).

- **COMP (headline):** "Which figure does DAX sit on now?" — order not stated. Score `target_rate =
  P(pick == stamp-order end figure)`. Diagnostics: `swapped` (reversed-order), `start`, `step-only`,
  `flip-only`.
- **DIRECT (gate):** order stated explicitly ("first … then …"). Score `direct_acc`.

## Pre-registered thresholds (frozen)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.25` (figure-identity / track-position chance).

## Verdict map (frozen, per model)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution. Rich-side
rung (iii) is documented closed regardless.

## Shortcut-proofing (certified pre-run)

`build_trials.assert_balance` (PASS): target figure uniform (identity picker = 1/K = 0.25); target
track position uniform (position picker ≤ 1/K); print-order & both canonical-order readers = exactly
0.50; start / single-move / reversed-order readers = 0; frequency flat.
`fixtures/make_fixtures.py` (**ALL FIXTURE ASSERTS PASS**): only genuine stamp-order composition
yields RESPECTS-ORDER; every print/canonical reader scores 0.50 on COMP; every position/identity
reader 1/K; any reader failing on-demand → UNINTERPRETABLE.

## Spend (frozen)

Pre-flight ≈ **$0.30 billed** (288 calls; K=6 per-call ≈ claude $0.00215 / gemini $0.00059 / gpt
$0.00034 — likely less at K=4). `HARD_STOP_USD = 0.60` on projected total. Record actual
`usage.cost` after. Day total before this run ≈ $0.335 of $5.00.

## Anti-cheat

The verdict map is symmetric and pre-registered: a non-witness (DIRECT still fails) **sharpens** the
claude-only reading and is fully reportable; a witness re-opens the COMP question; neither is "the
win," and **neither reaches rung (iii)** (adjudicated thin before the run). No threshold may be
retuned after seeing data. The instrument changes *only* by scale (K=6→K=4) from the ratified
Option-C design. `anchor: internal-contrast-only`.

## Independent pre-run critic

> _GO / NO-GO recorded here after the fresh pre-run-critic pass, before any finding-bearing call._
