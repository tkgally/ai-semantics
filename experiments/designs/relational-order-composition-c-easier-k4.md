# Design — EASIER (K=4) WITNESS order-sensitive composition probe

**Status:** frozen design (2026-06-18). Internal-contrast-only (the ratified relational posture; no
human comparison). A **scale parameter (K=6→K=4)** of the already-ratified Option-C instrument under
[`decisions/resolved/relational-rung-iii-path-dependence`](../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
— **no new decision owed** (as the gpt third-model extension owed none: same instrument, different
parameter). Run dir: `experiments/runs/2026-06-18-relational-order-composition-c-k4/`.

## The question

The K=6 Option-C run ([`result/relational-order-composition-c`](../../wiki/findings/results/relational-order-composition-c.md))
found a **split**: `claude-sonnet-4.6` RESPECTS-ORDER at ceiling, but **both** `gemini-3.5-flash`
(DIRECT 0.583) and `gpt-5.4-mini` (DIRECT 0.194) **failed the on-demand DIRECT gate** (< 0.80) — they
could not compose two non-commuting moves *even when told the order* — so their COMP was
UNINTERPRETABLE. [`essay/undischargeable-negative`](../../wiki/findings/essays/undischargeable-negative.md)
gives the methodological point: re-running the **same hard instrument** cannot move an UNINTERPRETABLE
verdict (it is one more instance of the same universal-over-elicitations). Only a **witness-seeking
probe** — an **easier** elicitation of the same capability — can flip a negative to a positive. This
is that probe ([`essay/capability-split`](../../wiki/findings/essays/capability-split.md) trigger (b);
the single most informative cheap test named in `NEXT.md`).

**Does an *easier* non-commuting-composition instrument let gemini or gpt clear the on-demand gate
and then compose by stamp order?**

## The single manipulated variable: instrument load (K)

The track shrinks **K=6 → K=4** — the *same* non-commuting STEP/FLIP pair (the dihedral generators of
a ring), only smaller:

- **STEP** — `p → (p+1)%4` (one position toward the back, wrapping back→front).
- **FLIP** — `p → 3−p` (mirror: position 1↔4, 2↔3) — a clean **2-swap derangement, no fixed point**.

Halved state space, a 2-swap mirror instead of 3-swap, fewer distractor figures. **Nothing else
changes**: identical prompt skeleton, identical two arms (COMP / DIRECT), identical shortcut-proofing,
identical symmetric verdict map. So the comparison to K=6 is clean — K is the only difference.

The **DIRECT gate is the empirical arbiter of "easier"**: the easiness claim is *measured*, not
assumed.

- **Witness** (gemini/gpt clear DIRECT ≥ 0.80 at K=4): attributes the K=6 failure to instrument load;
  re-opens the COMP order-sensitivity question for them.
- **Non-witness** (DIRECT still fails at K=4): the composition inability is robust to halving the
  instrument; **sharpens** the claude-only reading and bounds it.
- **claude = positive control**: it RESPECTS-ORDER at K=6, so it should still clear DIRECT (and
  ideally RESPECTS-ORDER) at K=4; a claude failure would mean the K=4 instrument is broken, not the
  others limited.

## Frozen parameters

- Panel: `claude-sonnet-4.6` (control) + `gemini-3.5-flash` + `gpt-5.4-mini` (the two witness targets).
  gemini `reasoning: {effort: minimal}`.
- `K = 4`; the 4 valid base configs fall one each on the 4 target positions, order balanced 2 SF / 2
  FS. `N_BLOCKS_COMP = 16` (4 configs × 4 reps) → 64 COMP records/model; `N_BLOCKS_DIRECT = 8` (×2) →
  32 DIRECT records/model. **96 records/model × 3 models = 288 finding-bearing calls.**
- `PRINT_CEILING = 0.50`; `DIRECT_FLOOR = 0.80`; composition bar = COMP target-rate Wilson-95 LB >
  0.50; `POS_CHANCE = 1/K = 0.25`.
- Forced single-figure format; `MAX_TOKENS = 512`; one stern retry then NA. `HARD_STOP_USD = 0.60`;
  pre-flight ≈ $0.30. `stimuli.json` sha256 frozen in `PREREG.md` before any finding-bearing call.

## Shortcut-proofing (certified at build + on idealized-reader fixtures)

`build_trials.assert_balance` (PASS) proves, per subset: target figure **uniform over the 4 shapes**
(identity picker = 1/4); target track position **uniform** (COMP: every fixed-position picker = 1/4);
**print-order and both canonical fixed-order readers = exactly 0.50**; the **start / single-move /
reversed-order readers = 0** on the target; frequency flat. `fixtures/make_fixtures.py` (**ALL
FIXTURE ASSERTS PASS**) certifies the verdict map on six idealized readers (`stamp_order` →
RESPECTS-ORDER 1.000; `print_order` / `canonical_sf` → ORDER-BLIND-OR-WEAKER 0.500; `figpref` /
`trackpos` → UNINTERPRETABLE 1/K; `direct_fail` → UNINTERPRETABLE). **Only ordering the two moves by
their stamps clears the 0.50 bar.**

## Verdict map (frozen, per model)

- **UNINTERPRETABLE** — `direct_acc < 0.80` (cannot compose the two moves on demand).
- **RESPECTS-ORDER** — DIRECT pass **and** COMP target-rate Wilson-95 LB **> 0.50** ⇒ order-sensitive
  composition (thin).
- **ORDER-BLIND-OR-WEAKER** — DIRECT pass **and** COMP target-rate Wilson-95 LB **≤ 0.50** ⇒ reads the
  moves in print/canonical order, not stamp order (thin).

## Scope & honesty (binding; carried over from Option-C)

1. **Internal-contrast-only.** A within-model contrast over balanced / order-permuted content; **no
   human claim.**
2. **Adjudicated THIN, not rung (iii).** Either verdict is single-reader-recoverable; a RESPECTS-ORDER
   positive is "respects operation order," never promoted to constitution. The rich-side rung (iii) is
   documented **structurally closed** for text-only stimuli.
3. **Witness-seeking interpretation only.** A witness flips an UNINTERPRETABLE verdict to interpretable
   *for the easier instrument*; it does not retroactively make the K=6 verdict a positive. A
   non-witness does not prove incapability (the negative stays undischargeable) — it bounds it to
   survive this easing.
4. **One easing axis.** K=6→K=4 only. Other easings (figure-based moves, fewer chaining steps,
   worked-example scaffolds) untested.

Gated by the independent pre-run critic before any spend (recorded in `PREREG.md`).
