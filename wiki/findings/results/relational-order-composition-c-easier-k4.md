---
type: result
id: relational-order-composition-c-easier-k4
title: Easier (K=4) witness-seeking re-run of order-sensitive composition — halving the instrument did NOT let gemini or gpt clear the on-demand composition gate (both still UNINTERPRETABLE); claude still RESPECTS-ORDER at ceiling, so the claude-only composition reading is bounded from below (it is not an artifact of K=6 difficulty)
meaning-senses:
  - relational
  - model-internal
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-18
updated: 2026-06-18
links:
  - rel: refines
    target: result/relational-order-composition-c
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: supports
    target: essay/undischargeable-negative
  - rel: supports
    target: essay/capability-split
  - rel: refines
    target: concept/relational-meaning
---

# Result: easier (K=4) witness-seeking re-run — no witness; the two UNINTERPRETABLE verdicts survive halving the instrument

> **Status: proposed (2026-06-18).** A **witness-seeking** re-run of the Option-C order-sensitive
> composition probe ([`result/relational-order-composition-c`](relational-order-composition-c.md)) at
> **reduced instrument load** (the same non-commuting STEP/FLIP pair, track shrunk **K=6 → K=4**). The
> Option-C run found a split: `claude-sonnet-4.6` RESPECTS-ORDER, but **both** `gemini-3.5-flash`
> (DIRECT 0.583) and `gpt-5.4-mini` (DIRECT 0.194) **failed the on-demand DIRECT gate** → UNINTERPRETABLE.
> [`essay/undischargeable-negative`](../essays/undischargeable-negative.md) gives the rationale: re-running
> the *same* hard instrument cannot move an UNINTERPRETABLE verdict; only an **easier elicitation** (a
> witness-seeking probe) can. This is that probe — [`essay/capability-split`](../essays/capability-split.md)
> **revision trigger (b)**, the single most informative cheap test named in [`NEXT.md`](../../../NEXT.md).
>
> **Outcome: NO WITNESS.** Halving the track (state space halved, a clean 2-swap mirror instead of
> 3-swap, fewer distractors) did **not** let either model clear the on-demand composition gate:
> **gemini DIRECT 0.594** (< 0.80, essentially unchanged from K=6's 0.583) and **gpt DIRECT 0.438**
> (< 0.80 — *substantially improved* from K=6's 0.194, but still below the gate) → **both still
> UNINTERPRETABLE**. **claude still RESPECTS-ORDER at ceiling** (DIRECT 0.906; COMP 64/64). So the
> claude-only composition reading is **bounded from below**: it is not merely an artifact of K=6
> difficulty — the inability survives a substantial easing. Per [`essay/undischargeable-negative`](../essays/undischargeable-negative.md) this
> does **not** prove gemini or gpt "cannot compose" (the behavioral negative stays undischargeable; a
> *still*-easier instrument might yet find a witness); it **bounds** the negative to survive *this*
> easing. `anchor: internal-contrast-only`; **no human-comparison claim.**

## The question (precise)

A witness-seeking probe asks one thing: is the Option-C UNINTERPRETABLE verdict (gemini, gpt cannot
compose two non-commuting moves on demand) driven by **instrument load** — in which case an easier
non-commuting-composition instrument would let them clear the on-demand gate (a *witness*, flipping
the negative) — or is it **robust** to easing (no witness, sharpening the claude-only reading)? The
single manipulated variable is the track size **K**: 6 → 4. Everything else is byte-identical in
logic (same STEP/FLIP pair, same two arms, same scoring, same thresholds, `analyze.py` unchanged);
the **DIRECT on-demand gate is the empirical arbiter of "easier."**

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

Run dir: [`experiments/runs/2026-06-18-relational-order-composition-c-k4/`](../../../experiments/runs/2026-06-18-relational-order-composition-c-k4/).
Design: [`relational-order-composition-c-easier-k4`](../../../experiments/designs/relational-order-composition-c-easier-k4.md).

- **Same non-commuting STEP/FLIP semantics, smaller.** K=4 figures on a stated track; DAX starts on a
  stated figure; two stamped moves from {STEP `p→(p+1)%4`, FLIP `p→3−p` (mirror 1↔4, 2↔3 — a clean
  2-swap derangement, no fixed point)}. STEP and FLIP do not commute, so stamp order vs reversed order
  reach different figures. The two move-lines are printed in stamp order in half the records and
  reversed in the other half (print order decoupled from stamp order).
- **Two arms.** **COMP** (headline, 64/model): *"Which figure does DAX sit on now?"* — order not
  stated. **DIRECT** (on-demand gate, 32/model): order stated explicitly (*"first … then …"*). If
  `direct_acc < 0.80`, COMP is UNINTERPRETABLE.
- **Shortcut-proof by construction.** The 4 valid base configs fall one each on the 4 target
  positions, order balanced 2 SF / 2 FS. Proven at build, separately per arm: every figure-identity
  picker and every track-position picker scores **1/K = 0.25**; the **print-order reader and both
  canonical fixed-order readers score exactly 0.50**; the **start / single-move / reversed-order
  readers score 0**. So **only ordering the two moves by their stamps can clear the 0.50 bar.** Six
  idealized-reader fixtures certify the verdict map.
- **Same binding adjudication (THIN).** An operation-order gap here is single-reader-recoverable —
  *"respects operation order,"* **not** rung (iii). The rich-side rung (iii) stays documented
  **structurally closed** for text-only stimuli ([`essay/transcript-ceiling`](../essays/transcript-ceiling.md)).
- **Independent pre-run critic GO** (fresh agent): recomputed the geometry itself (STEP/FLIP do not
  commute at all 4 starts; exactly 4 valid configs; sha matches), brute-forced **19 reader families**
  and confirmed **no reader beats 0.50 without stamp-order** (the exotic recency readers all 0.000),
  ruled the easier framing fair and clean (K the sole manipulated variable; smaller answer space
  *raises* the floor to 0.25 but the bar stays 0.50), and confirmed **no new decision owed** (a scale
  parameter of the ratified Option-C instrument) and no threshold tuned to a result.
- Forced single-figure elicitation; one stern retry then NA; `HARD_STOP_USD = 0.60`.

## The headline (verified — numbers not altered)

| model | DIRECT on-demand acc | COMP target (stamp-order) | Wilson 95% | swapped | start | step-only | flip-only | NA | verdict | K=6 DIRECT |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **0.906** (29/32) | **1.000** (64/64) | [0.943, 1.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0 | **RESPECTS-ORDER** | 0.861 |
| gemini-3.5-flash | **0.594** (19/32) | 0.484 | [0.366, 0.604] | 0.000 | 0.000 | 0.109 | 0.328 | 0 | **UNINTERPRETABLE** | 0.583 |
| gpt-5.4-mini | **0.438** (14/32) | 0.344 | [0.239, 0.466] | 0.094 | 0.094 | 0.234 | 0.344 | 0 | **UNINTERPRETABLE** | 0.194 |

- **claude — RESPECTS-ORDER (positive control holds).** DIRECT 0.906 (> 0.80) and COMP recovers the
  stamp-order figure **every time** (64/64, Wilson LB 0.943 — far above the 0.50 print/canonical
  ceiling); swapped / start / single-move readings taken **zero** times. So claude spontaneously orders
  the two non-commuting moves by their stamps at K=4 too — confirming the **K=4 instrument is a valid
  non-commuting composition** (had claude failed, the instrument would be indicted, not the others).
- **gemini — UNINTERPRETABLE (no witness).** DIRECT **0.594** still fails the 0.80 gate — essentially
  unchanged from K=6 (0.583). Halving the instrument did **not** let gemini compose the two moves on
  demand; its COMP (0.484) is therefore uninterpretable. Its COMP errors are dominated by **flip-only**
  (0.328) — it frequently applies only one of the two moves.
- **gpt — UNINTERPRETABLE (no witness; a suggestive but not clean improvement).** DIRECT **0.438**
  still fails the 0.80 gate, but roughly **doubled** from K=6's 0.194 (K=6 [0.097, 0.350] → K=4
  [0.282, 0.607]). The two Wilson intervals **overlap** (0.350 vs 0.282) and n is only 32, so the rise
  is **directional/suggestive, not statistically clean** — and it stays far below the gate, so the
  verdict is unchanged. Read it as "DIRECT roughly doubled but remained sub-gate," not as a confirmed
  effect. As at K=6, gpt's COMP errors are dominated by **single-move readers** (step-only 0.234,
  flip-only 0.344): it still applies only **one** of the two stamped moves.
- **Clean record:** 288/288 answered across the three models, **0 NA, 0 retried, 0 length-truncation**.

**Discipline.** Independent pre-run critic GO (geometry recomputed; 19 reader families enumerated; no
sub-0.50 leak; no new decision owed; anti-cheat PASS). Independent **post-run verifier** re-derived
every stamp-order target from the K=4 geometry by its own route, re-parsed all 288 records with its
own parser, recomputed every rate, and audited claude's last-line extraction — **REPRODUCED** (see
provenance below).

## What this shows — and what it does NOT (binding scope)

**Shows (within-model, internal-contrast-only):**

1. **No witness: the composition failure survives halving the instrument.** The most likely way the
   capability-split reading could over-read — that gemini/gpt simply found the K=6 instrument too hard
   — was tested directly by the easiest defensible same-pair instrument, and it did **not** flip:
   neither model clears the on-demand gate at K=4. So the Option-C split is **not** an artifact of K=6
   difficulty alone; the claude-only composition reading is **bounded from below**.
2. **A suggestive (not clean) easing effect for gpt; none for gemini.** gpt's on-demand DIRECT
   roughly doubled (0.194 → 0.438) while gemini's barely moved (0.583 → 0.594). gpt's rise is
   **directional but not statistically clean** (overlapping Wilson intervals, n=32) and stays
   sub-gate, so it does not change the verdict; it is a *hint* that gpt's composition is
   load-sensitive, reported as a hint, not a finding. Either way K=4 is not easy enough to make a
   composer of either model.
3. **claude's composition is robust to scale.** RESPECTS-ORDER at both K=6 and K=4, at ceiling, with
   the same transparent reasoning — a within-model confirmation that the positive is not a K=6-specific
   fluke.

**Does NOT show:**

- **Does NOT prove gemini or gpt "cannot compose."** Per
  [`essay/undischargeable-negative`](../essays/undischargeable-negative.md), a behavioral
  capability-absence is an undischargeable universal over elicitations: this probe is **one more
  (easier) instrument**, and a witness it failed to find is not a proof of absence. A *still*-easier
  non-commuting-composition design (figure-to-figure moves, worked-example scaffolds, fewer chaining
  steps) could yet find a witness. What is established is the **instrument-relative** fact: no witness
  *under this K=6→K=4 easing*. This is exactly the typology the essay prescribes — an **effect-null /
  prerequisite-gate failure** (kind 2: the on-demand composition prerequisite is not met), not a
  closed capability-absence (kind 4, which only a non-behavioral argument could reach).
- **Not rich constitution, not rung (iii).** Adjudicated THIN before the run; the rich side stays
  structurally closed for text-only stimuli.
- **Not a human comparison** (`anchor: internal-contrast-only`).

## Effect on the two essays it instances

- [`essay/capability-split`](../essays/capability-split.md) **revision trigger (b)** ("gemini or gpt
  composing under an easier operationalization") is **tested and did NOT fire in the witness
  direction**: easing the instrument (K halved) did not let either model compose on demand. The
  "capability split" reading is therefore **not** weakened toward "this-(K=6)-instrument split" — it is
  **strengthened**: the split survives the most direct easing, so it is at least a *two-instrument*
  (K=6 and K=4) capability gap for gemini and gpt, not a K=6 artifact. (The trigger stays live for any
  *further*, more aggressive easing.)
- [`essay/undischargeable-negative`](../essays/undischargeable-negative.md) is **corroborated as
  applied**: a witness-seeking probe is the right move on an UNINTERPRETABLE verdict, and a witness not
  found bounds-but-does-not-closes the negative — precisely the essay's discipline. The negative is
  filed as **kind 2** (instrument-uninterpretable / prerequisite-gate failure), the box the essay keeps
  distinct from kind 4 (behavioral capability-absence, deliberately empty).

## Honesty box

- **No witness; non-witness verdict.** gemini DIRECT 0.594, gpt DIRECT 0.438 — both still below the
  0.80 on-demand gate at K=4 → both UNINTERPRETABLE. claude RESPECTS-ORDER (DIRECT 0.906, COMP 64/64).
- **gpt's improvement is reported but not over-read.** K=6 0.194 → K=4 0.438 (CIs [0.097,0.350] →
  [0.282,0.607]). The intervals **overlap** and n=32, so this is a **suggestive directional** rise,
  not a confirmed effect; it stays well below the gate and does not change the verdict. Reported
  honestly as "roughly doubled but still sub-gate," a hint of load-sensitivity, not a finding.
- **gemini barely moved** (0.583 → 0.594) — for gemini, halving the instrument made essentially no
  difference to on-demand composition.
- **The negative is undischargeable, not closed.** This bounds the Option-C negative to survive a
  K=6→K=4 easing; it does not prove incapability. A still-easier instrument is the live next probe.
- **claude emitted CoT despite the forced format**, as at K=6 — the post-run verifier confirmed the
  last-line extraction is the genuine final answer and matches the independently-derived target; the
  RESPECTS-ORDER verdict rests on transparent reasoned ordering, not a black-box token.
- **One easing axis.** K=6→K=4 only (same STEP/FLIP pair). Other easings (figure-based moves, fewer
  chaining steps, worked examples) untested.
- **Spend.** 288 finding-bearing calls + 3 liveness = **$0.28451 billed** (`usage.cost`-summed, 0
  missing; claude $0.19916, gemini $0.05203, gpt $0.03011, liveness $0.00321). Inside the $0.60 hard
  stop; day total 2026-06-18 ≈ **$0.620** of the $5.00/day cap.

## Provenance — independent post-run verifier

A fresh independent verifier re-derived every result from raw by its own route — **REPRODUCED**:

- **Stimuli sha256** `975e31bc…3ef88ba` reproduced exactly on the newline-stripped blob (the frozen
  form, matching `probe.py._require_frozen`).
- **Geometry recomputed independently** (its own `apply_order` over K=4 STEP/FLIP, mapped through each
  record's `track`): **96/96** stored `target_shape` reproduced; `swapped`/`step1`/`flip1` 96/96 each.
- **Re-parsed all 288 replies** with its own parser: **0 parse disagreements**, **0 NA, 0 retried, 0
  length-truncation**.
- **Verdicts match to the digit:** claude DIRECT 29/32 = 0.9062 [0.758, 0.968], COMP 64/64 = 1.000
  [0.943, 1.0] → RESPECTS-ORDER; gemini DIRECT 19/32 = 0.5938 [0.423, 0.745] → UNINTERPRETABLE (COMP
  0.484; step-only 7, flip-only 21); gpt DIRECT 14/32 = 0.4375 [0.282, 0.607] → UNINTERPRETABLE (COMP
  0.344; swapped 6, start 6, step-only 15, flip-only 22).
- **claude CoT audit:** 6 strict / 90 non-strict parses; for all 64/64 COMP and 29/32 DIRECT the
  last-line pick equals the independently-derived target; the 3 DIRECT misses are genuine wrong final
  figures, not parser artifacts. The RESPECTS-ORDER verdict depends on the (verified-faithful)
  last-line extraction branch.
- **Failure-mode:** gemini/gpt DIRECT errors are genuine single-figure wrong answers (0 NA, 0
  truncation); single-move readers dominate (gemini's 13 DIRECT errors: step-only 6, flip-only 7;
  gpt's 18: step-only 10, flip-only 5, swapped 2, other 1) — a real composition-ability limit, the
  identical failure signature to K=6.
- **Cost:** `usage.cost` summed over 288 finding records = $0.281306 (0 missing) + liveness $0.003207
  = **$0.284513**, matching the ledger.
- **Verifier's calibration note (incorporated above):** gpt's K=6→K=4 DIRECT rise is real-directional
  but the Wilson intervals overlap, so it is "suggestive, not statistically clean"; the non-witness
  headline holds cleanly.
