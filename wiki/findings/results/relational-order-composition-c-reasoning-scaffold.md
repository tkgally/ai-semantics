---
type: result
id: relational-order-composition-c-reasoning-scaffold
title: Execution-format (working-surface) witness-seeking re-run of order-sensitive composition — a WITNESS — permitting step-by-step working flips BOTH gemini and gpt from UNINTERPRETABLE (four prior forced-format instruments) to RESPECTS-ORDER at/near ceiling; the four-instrument split was an artifact of denying a working surface, not a composition-capacity limit
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
    target: result/relational-order-composition-c-worked-example
  - rel: refines
    target: result/relational-order-composition-c-figure-to-figure
  - rel: refines
    target: result/relational-order-composition-c
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: supports
    target: essay/floor-is-not-a-ceiling
  - rel: supports
    target: essay/undischargeable-negative
  - rel: supports
    target: essay/witness-seeking-economics
  - rel: supports
    target: essay/capability-split
  - rel: refines
    target: concept/relational-meaning
---

# Result: execution-format witness-seeking re-run — a WITNESS; a working surface flips gemini and gpt to RESPECTS-ORDER

> **Status: proposed (2026-06-19).** The **execution-format (working-surface)** witness-seeking
> re-run of the Option-C order-sensitive composition split — the **fifth easing**, and the **first
> to find a witness**. The witness search to date had run four easings without one: claude
> RESPECTS-ORDER throughout; **both** gemini and gpt UNINTERPRETABLE across K=6 positional, K=4
> positional, K=4 figure-maps, and K=4 figure-maps + worked example
> ([`result/relational-order-composition-c-worked-example`](relational-order-composition-c-worked-example.md)).
> Every one of those four runs **forbade the model a working surface**: the system prompt demanded
> "EXACTLY ONE figure name and NOTHING ELSE — no explanation, no reasoning", and gemini ran at
> reasoning `effort: minimal`. [`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md)
> objection **(B)** named **execution-format scaffolding** as an explicit, **un-eased** axis the
> ≥2-move floor does not touch. This probe eases exactly that: on the **byte-identical**
> figure-to-figure trials (same `stimuli.json` rstrip-sha `975e31bc…88ba`), the **only** manipulated
> variable is the response format — the prompt now **permits step-by-step working** and parses a
> `FINAL: <figure>` tag; the reasoning-effort knob is **held constant** (gemini stays at `effort:
> minimal`; the working surface is opened only in the visible output channel).
>
> **Outcome: WITNESS — all three models now RESPECTS-ORDER.** Given room to write out the two-step
> execution, **gemini flips DIRECT 0.656 → 1.000** and **gpt flips DIRECT 0.250 → 0.969** (both now
> clear the 0.80 gate), and both spontaneously order the two moves by their round stamps on COMP
> (gemini target **1.000**, gpt target **0.953**, Wilson-LB > 0.50). claude stays at ceiling (DIRECT
> 1.000, COMP 1.000). 96/96 replies parsed via the `FINAL:` tag; **0 NA, 0 retried, 0 length-
> truncation**. So the four-instrument gemini/gpt negative was an artifact of the **forced single-
> token format** (no working surface), **not** a composition-capacity limit. This is the witness
> [`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md) revision-trigger (b) predicted
> would **confirm objection (B)** — the elicitation space was open along an axis the floor did not
> touch — and exactly the [`essay/undischargeable-negative`](../essays/undischargeable-negative.md)
> vindication: the negative was never "M cannot compose", and a witness discharged it. **Still THIN**
> (single-reader-recoverable; "respects operation order", **not** rung (iii) / constitution; the
> rich side stays documented structurally closed for text). `anchor: internal-contrast-only`; **no
> human-comparison claim.**

## The question (precise)

Across four eased instruments, gemini and gpt failed the on-demand DIRECT gate; their error signature
was **single-move reading** (applying only one of the two stamped moves), even when **told the order**
on DIRECT, which the figure-to-figure and worked-example runs read as localizing the difficulty to
"chaining execution." But every one of those runs **denied the model a working surface** — the system
prompt forced one figure name with reasoning forbidden, and gemini ran at `effort: minimal`. A model
that cannot externalize a two-step computation may apply only one move **for that reason**.
[`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md) objection (B) names this
verbatim:

> The on-demand DIRECT gate *states* the order but does not scaffold the *execution* into externalized
> steps. An elicitation that decomposes the execution itself (an explicit step-by-step working
> surface) eases the localized difficulty directly, and is un-eased.

This probe eases that single axis and asks: is the four-instrument negative robust to giving the
models a scratchpad, or is it a witness — a flip to RESPECTS-ORDER?

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

The **byte-identical** figure-to-figure K=4 trials (non-commuting STEP/FLIP, each move an explicit
figure→figure lookup table, no positions shown; 64 COMP + 32 DIRECT records/model). The **only**
manipulated variable vs. the figure-to-figure run is the response format:

- **Before:** "Reply with EXACTLY ONE figure name … no explanation, no reasoning." Parser: the whole
  reply must be one figure.
- **Now:** "You MAY think step by step and show your working … write your final answer on the LAST
  line in EXACTLY this form: `FINAL: <figure>`." Parser (`common.parse_forced`): read the **last
  `FINAL:` tag** whose figure is present — **target-blind** (keyed on reply position, never on which
  figure is correct); a `finish_reason == "length"` reply is never parsed.

The reasoning-effort knob is **held constant** (gemini stays at `effort: minimal`, exactly as in the
four prior runs). The max-token cap was raised (512 → 1024) and the parser changed to read the tag;
both are necessary consequences of permitting working, not independent manipulations. Geometry,
scoring (`analyze.py`), thresholds, and the verdict map are byte-identical to the four prior runs.

- **COMP (headline, spontaneous):** order *not* stated; a reader who applies the moves in print or a
  fixed canonical order scores exactly **0.50**; only ordering by the round stamps (Wilson-95 LB >
  0.50) clears the bar. **Permitting a working surface does not make COMP non-spontaneous** — the
  query still does not state the order, so the model must still **decide** to order by the stamps; the
  scratchpad only lets it externalize whatever ordering it chooses.
- **DIRECT (on-demand gate):** order stated ("first … then …"). Gate: `direct_acc ≥ 0.80`.

**Adjudicated THIN before the run** (carried over unchanged, biased *against* the rich reading): the
stamped move-list and the maps are in the record, so an order gap is single-reader-recoverable —
"respects operation order", **never** rung (iii) / constitution; the rich side is documented
structurally closed for text-only stimuli. An **independent pre-run critic** returned **GO**: it
recomputed the geometry (STEP/FLIP non-commuting at all 4 starts; all 96 records' target/swapped/
single-move ends re-derived, 0 mismatches), confirmed `stimuli.json` byte-identical to the fig run
(rstrip-sha `975e31bc…88ba`) and `build_trials.py`/`analyze.py`/fixtures byte-identical, diffed
`common.py` to confirm the **only** functional changes are format (SYS, STERN, final instruction,
the `FINAL:`-tag parser, `MAX_TOKENS`, `HARD_STOP`) with `REASONING` **unchanged**, verified the
parser is **target-blind** (12/12 cases incl. last-tag-wins, length-truncation → never parsed), and
ruled **no new decision owed** (an elicitation-format easing within the ratified Option-C /
`internal-contrast-only` frame, the same kind as the K=4, fig, worked-example, and gpt-extension
easings).

## Results (3 models, 96 records/model, 0 NA, 0 retried, 0 length-truncation; independently reproduced)

An **independent post-run verifier** recomputed every number from raw with its own Wilson
implementation, re-derived the geometry from `track`+`start_idx`+`order` (0 mismatches on all stored
target/swapped/single-move fields), and re-parsed every reply with an independent `FINAL:`-tag
extractor: **REPRODUCED — its 288 picks matched the stored picks 288/288** (a target-biased parser
ruled out: gpt's 4 errors were parsed to the *wrong* figure gpt actually wrote). It confirmed the
print-order ceiling holds (a print-order reader scores exactly 0.500; the rev/stamp split is balanced
32/32), 0 NA / 0 retried / 0 length-truncation / 0 duplicate rids / full coverage, and the billed cost
$0.735346 with 0 missing-cost fields. **CoT-genuineness, decisive check:** on every reverse-printed
COMP record picked as target (32 each for gemini and gpt), the working **explicitly re-sorts the two
moves by round stamp** before applying them, overriding the printed order — genuine stamp-order
composition, not a print-order coincidence.

| model | DIRECT on-demand acc (gate 0.80) | COMP target rate (bar: Wilson-LB > 0.50) | verdict |
|---|---|---|---|
| **claude-sonnet-4.6** | **1.000** [0.893, 1.000] PASS | **1.000** [0.943, 1.000] → sig | **RESPECTS-ORDER** |
| **gemini-3.5-flash** | **1.000** [0.893, 1.000] PASS | **1.000** [0.943, 1.000] → sig | **RESPECTS-ORDER** |
| **gpt-5.4-mini** | **0.969** [0.843, 0.995] PASS | **0.953** [0.871, 0.984] → sig | **RESPECTS-ORDER** |

**The DIRECT on-demand accuracy across all five instruments** (the witness search):

| model | K=6 pos. | K=4 pos. | K=4 fig-maps | K=4 fig + worked-ex | **K=4 fig + working surface (this run)** |
|---|---|---|---|---|---|
| gemini | 0.583 | 0.594 | 0.656 | 0.625 | **1.000** ← WITNESS (gate cleared) |
| gpt | 0.194 | 0.438 | 0.250 | 0.156 | **0.969** ← WITNESS (gate cleared) |
| claude | 0.861 | 0.906 | 1.000 | 1.000 | **1.000** (positive control, ceiling) |

The single-move-reader signature that persisted (and for gpt intensified to 84.4%) across four
forced-format instruments **vanishes** the moment a working surface is allowed: on the DIRECT arm,
gpt's single-move sum drops to ~0 and gemini's to 0; both apply *both* moves in sequence.

**COMP failure breakdown** (spontaneous arm): claude swapped/start/single-move all 0.000; gemini all
0.000; gpt swapped 0.047, start 0.047, single-move 0.000 — i.e. gpt's few misses are ordinary slips
(occasionally the reversed order or the start figure), not single-move reads and not a parsing
artifact.

## Reading (honest, bounded)

1. **A witness — the four-instrument negative is discharged.** Permitting step-by-step working flips
   **both** previously-UNINTERPRETABLE models to RESPECTS-ORDER at/near ceiling, on the byte-identical
   trials. By [`essay/undischargeable-negative`](../essays/undischargeable-negative.md), a single
   witness (one easier elicitation on which the model succeeds) discharges a behavioral capability-
   negative — and here the witness lands for both models at once. The project was right never to close
   the negative; it was a **kind-2 instrument-uninterpretable** verdict, and the responsible instrument
   was the **forced single-token format**.
2. **The difficulty was the execution FORMAT, not chaining-execution capacity.** The figure-to-figure
   and worked-example runs localized the difficulty to "chaining execution"; this run refines that:
   the obstacle was not a *capacity* to chain but the *denial of a surface on which to chain*. When the
   models may write "STEP: star → square; FLIP: square → triangle", they chain correctly. The
   single-move signature was the shape of a two-step computation forced through a one-token channel.
3. **Spontaneous composition, genuine (not print-order).** On COMP the order is not stated, and half
   the records print the two moves in *reversed* round order, so a print-order reader would land on the
   `swapped` figure (≈0.50). gemini's and gpt's CoT on those records explicitly re-sorts by round
   stamp ("apply the moves in chronological order based on the round numbers, from lowest to highest")
   and lands on the **stamp-order** target — genuine order-sensitive composition, not a print-order
   coincidence. The verifier confirmed this on reverse-printed records.
4. **Confirms [`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md) objection (B).**
   The essay argued the ≥2-move floor closed only the "fewer steps" axis and left the elicitation space
   open along others — naming **execution-format scaffolding** as one. A witness on that axis is exactly
   its revision-trigger (b): "the elicitation space was open along an axis the floor did not touch, so
   the floor was never a closure. The central claim is strongly corroborated and the specific suspension
   is reopened-and-resolved-positive." The composition witness-search is **reopened and resolved
   positive**; the budget-based suspension is **lifted** for the question "can these models compose two
   non-commuting moves?" (yes — given a working surface).
5. **The split was format-relative, not a capability split** ([`essay/capability-split`](../essays/capability-split.md)).
   The earlier one-model (claude-only) RESPECTS-ORDER reading held only under the forced format. With a
   working surface the panel is **concordant**: all three compose. This is why the result `contradicts`
   capability-split as applied to *this* split — it bounds that essay's "claude > gemini/gpt on
   composition" watch-item to the forced-format elicitation (capability-split was always careful never
   to promote it to a finding; this is the witness it flagged could arrive).

## Witness-search suspension note (updated → reopened-resolved-positive)

Per [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md), the suspension record
is updated. **The suspension is lifted: a witness was found.**

- **(i) Axes eased and the verdict on each:** state-space (K=6→K=4) → no witness; per-move read-off
  (figure-maps) → no witness; chaining demonstration (worked example) → no witness; **execution format
  (a working surface, this run) → WITNESS** (both failing models clear the gate at/near ceiling).
- **(ii) What the witness localizes:** the four-instrument difficulty was the **denial of a working
  surface**, not a chaining-execution capacity. The "ease the implicated axis" heuristic succeeded —
  the truly implicated axis was the elicitation format, and easing it found the witness in one cheap
  probe, exactly as the economics predicts a well-targeted probe can.
- **(iii) Structural bound:** moot — the search is resolved positive, not suspended. (The
  [`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md) verdict that no kind-3
  reach-closure of the available type existed is **confirmed in the strongest way**: there was a
  witness all along; a structural closure would have been wrong.)
- **(iv) What remains open:** the THIN→rich gap is untouched (rung (iii) stays structurally closed for
  text); generality across operation pairs, larger grids, >2 moves, and the many-shot/different-pair
  axes is still untested; this is one operationalization, one run, three-model panel.

## Honesty box

- **What this shows:** with a step-by-step working surface, **all three** panel models perform
  order-sensitive composition of two non-commuting moves at/near ceiling and spontaneously order by
  round stamps — flipping the four-instrument gemini/gpt UNINTERPRETABLE negatives. The negatives were
  relative to the **forced single-token format**, not a composition-capacity limit.
- **What it does NOT show:** rung (iii) / constitution (the verdict is **THIN**, single-reader-
  recoverable — "respects operation order"; the rich side stays documented structurally closed for
  text). It does **not** show the models compose *without* a working surface (they do not, robustly,
  across four instruments) — the finding is precisely that the **format** gates the behavior. It makes
  **no** claim that one model is stronger than another (the panel is now concordant).
- **Genuine, not parsing:** 96/96 replies parsed via the target-blind `FINAL:` tag; 0 NA, 0 retried,
  0 length-truncation; the COMP signal survives the reverse-printed records (genuine stamp-order
  re-sort in the CoT, not print order).
- **Limits:** one operationalization (STEP/FLIP, two moves, figure-maps), text-only, three-model
  panel, single run, one shot. A working surface raises output tokens (cost), not just accuracy — the
  comparison is format-vs-format on byte-identical trials, the legitimate single variable.
- **No human comparison** made or owed: `anchor: internal-contrast-only` (a within-model contrast over
  balanced, order-permuted content).
- **Spend:** **$0.73535 billed** (`usage.cost`-summed, 0 missing; liveness $0.00454 + claude $0.46178
  + gemini $0.21713 + gpt $0.05189). Pre-flight ≈ $0.95; came in under (claude CoT the driver). $1.50
  hard stop never approached. **Day total 2026-06-19 ≈ $0.74 of $5.00.**
