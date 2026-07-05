---
type: result
id: scivetti-let-alone-repeated-runs-v1
title: Five repeated temp-0 runs pin the let-alone jitter — gpt's below-baseline residual is robust to run-to-run noise (every draw < 0.90), the swing is ~±0.12 for gpt but ceiling-protected and model-specific, and "gemini is deterministic" softens to "gemini is most stable"
meaning-senses:
  - model-internal
  - constructional
  - inferential
  - human-comparison
status: proposed
contingent-on: []
created: 2026-06-21
updated: 2026-07-05
links:
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: refines
    target: result/scivetti-let-alone-powered-rerun-v1
  - rel: supports
    target: essay/point-estimate-is-a-draw
  - rel: supports
    target: essay/output-channel-confound
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: supports
    target: claim/output-channel-working-surface
---

# Result: repeated-run temp-0 jitter measurement (let-alone forced-decomposition)

The **repeated-run measurement** that
[`result/scivetti-let-alone-powered-rerun-v1`](scivetti-let-alone-powered-rerun-v1.md)
(session 62) named as the trigger-(g) redirect and that
[`essay/point-estimate-is-a-draw`](../essays/point-estimate-is-a-draw.md) revision trigger (a)
prescribed: session 62 surfaced **temp-0 run-to-run label stochasticity** as the new binding
limit on the let-alone construction, but inferred "~12% per run" from a **single** cross-session
run-pair (s60 → s62; claude 3/24 flips all adverse, gpt 3/24 net 0, gemini 0). This run **pins
the jitter** by scoring the **byte-identical** forced-decomposition instrument **K = 5** times at
temperature 0 over the **same frozen 63-item set** (24 let-alone test + 9 let-alone train + 30
comparative-correlative ceiling control), and tests the essay's trigger (a): *does jitter shrink
at the easier ceiling and concentrate at the hard near-chance let-alone?* It is a licit
same-instrument re-run because it **measures the noise floor**, not because it re-scores the
residual (the [`essay/undischargeable-negative`](../essays/undischargeable-negative.md) threaded
needle: re-running to measure the floor buys the floor; re-running to "firm a null" buys nothing).

## One-line finding

Across five same-session runs the comparative-correlative ceiling control **never jittered**
(range 0.000 for claude/gemini; 0.033 — one item once — for gpt) while the hard near-chance
let-alone jittered materially (**gpt range 0.121**, claude 0.061, gemini 0.030) — so
[`essay/point-estimate-is-a-draw`](../essays/point-estimate-is-a-draw.md) **trigger (a) FIRES**
(jitter is near-chance-concentrated and **ceiling-protected**; the essay narrows from "single-run
point estimates are draws" to "…**on hard, near-chance, functional instruments** are draws"). The
~±0.12 the source result estimated lands **exactly** for gpt (range 0.121) but is **model-specific**
(claude ~0.06, gemini ~0.03). Most consequentially, **gpt's below-baseline residual is robust to
the jitter**: every one of the 5 runs reads **< 0.90** (band [0.545, 0.667], max 0.667), the
de-noised majority-vote accuracy is **0.606** (Wilson hi **0.753 < 0.90**), so session 62's
CONFIRMS-RESIDUAL was **not** a low draw. Two honest refinements: session 62's *"gemini is
deterministic"* softens to **"gemini is the most stable"** (it churns 2/33 over five runs, not
zero), and the **same-session spread is a lower bound** — claude's single cross-session s60→s62
test-cell swing (0.125) **exceeds** its within-session 5-run test-cell range (0.042), and claude's
s62 0.708 was itself a low draw (within-session test cell [0.750, 0.792]).

## What ran

- **Design: same instrument, same items, K = 5 repeats.** The ONLY change vs session 62 is that
  each item is scored five times instead of once. `NLI_SYS_DECOMP` is **byte-identical** to
  sessions 60/62 (programmatically diff-checked; the evaluated payload is identical — the PREREG's
  "len 910" counts the escaped source literal, 809 chars evaluated, same string either way). Same
  panel, temperature 0, gemini `effort: minimal` held constant. Every one of the 945 calls
  (5 × 3 × 63) is an independent HTTP request; nothing cached or deduped.
- **Provenance re-asserted** (all byte-identical to s62): frozen 63-item sha `1b87dc871e4ec8dd`,
  full-set `1c5cffb18c5ef78e`, s60-subset `9be31a8fea8d7f16`, train-LA `6b0c8d82536f25e6`.
- **Integrity.** 5 runs × 3 models × 63 items, **0 missing**, **945/945 parsed via the `FINAL:`
  tag** (0 fallbacks), **0 missing `usage.cost`**. All three models **worked 33/33** let-alone
  items on **every** run (uptake induced throughout). All five runs **clean** (uptake induced +
  control preserved + 0 missing) for all three models.
- **Cost** (billed `usage.cost`): **$1.9642** (claude $1.1785 / gemini $0.5615 / gpt $0.2242;
  per-model summed across the five runs). On pre-flight ($1.96 = 5 × session-62's measured
  $0.392). Under the $2.40 abort and the $2.50 single-run flag; **UTC-day 2026-06-21 total =
  $1.964 of $5.00**.
- **Governance.** A same-instrument, same-item, repeat-count-only re-run under the
  already-ratified Scivetti answer-key anchor (ratified 2026-05-29) + the ratified
  `constructional-divergence-operationalization`. It changes nothing about *what* is scored
  against the human gold — only how many times. **No new decision owed** (independent pre-run
  critic GO, fresh agent; `wiki/decisions/open/` empty). Its force is a within-model **measurement
  of instrument jitter**; it makes **no new human-comparison claim** beyond pinning the magnitude
  of the already-reported (descriptive) let-alone residual. Independent post-run verifier (fresh
  agent) **REPRODUCED** every number from raw.

## Results

Human reference (fixed, not retuned): Scivetti Exp-1 native-speaker accuracy ≈ 0.90; 3-way chance
≈ 0.33. comparative-correlative carries the **ratified anchor**; let-alone is **descriptive** from
the same human-annotated release (not individually anchored), exactly as sessions 57/58/60/62.

### let-alone combined (n = 33) — five repeated draws

| model | per-run accuracy (5 runs) | range | SD | churn | majority-vote (Wilson) | mean pairwise agree |
|---|---|---:|---:|---:|---:|---:|
| claude-sonnet-4.6 | 0.818 / 0.758 / 0.758 / 0.788 / 0.758 | **0.061** | 0.027 | 7/33 (0.21) | 0.788 [0.622, 0.893] | 0.897 |
| gpt-5.4-mini | 0.636 / 0.667 / 0.545 / 0.606 / 0.545 | **0.121** | 0.054 | 10/33 (0.30) | **0.606 [0.437, 0.753]** | 0.873 |
| gemini-3.5-flash | 0.879 / 0.879 / 0.879 / 0.909 / 0.909 | **0.030** | 0.017 | 2/33 (0.06) | 0.909 [0.764, 0.969] | 0.970 |

*churn = fraction of items whose label is not constant across the 5 runs; majority-vote = accuracy
of the per-item modal label vs gold (the de-noised estimate); mean pairwise agree = mean label
agreement over the C(5,2)=10 run-pairs.*

### comparative-correlative (n = 30) — ceiling control (the trigger-(a) contrast)

| model | per-run accuracy (5 runs) | range | churn |
|---|---|---:|---:|
| claude-sonnet-4.6 | 1.000 ×5 | **0.000** | 0/30 |
| gpt-5.4-mini | 0.967 / 1.000 / 0.967 / 1.000 / 1.000 | **0.033** | 2/30 |
| gemini-3.5-flash | 1.000 ×5 | **0.000** | 0/30 |

### gpt let-alone residual — pinned below baseline

Every one of the 5 same-session runs reads **below 0.90** (band **[0.545, 0.667]**, max 0.667).
Adding the s62 cross-session draw (0.636) → **6 draws all in [0.545, 0.667]**. The de-noised
majority-vote accuracy is **0.606**, Wilson **[0.437, 0.753]**, **hi 0.753 < 0.90**. Even allowing
gpt its single best draw (0.667), it stays a fifth below the human baseline. The session-62
CONFIRMS-RESIDUAL is therefore **robust to the run-to-run jitter it surfaced**, not an artifact of
a favorable draw.

### Cross-session vs within-session (Q6 — the lower-bound check)

| model | s60 test (24) | s62 test (24) | within-session test band (5 runs) | within-session test range | single s60→s62 swing |
|---|---:|---:|---|---:|---:|
| claude | 0.833 | 0.708 | [0.750, 0.792] | 0.042 | **0.125** |
| gpt | 0.583 | 0.583 | [0.542, 0.667] | 0.125 | 0.000 |
| gemini | 0.875 | 0.875 | [0.833, 0.875] | 0.042 | 0.000 |

claude's single cross-session swing (0.125) **exceeds** its within-session 5-run range (0.042),
and its s62 0.708 sits **below** the within-session band — i.e. s62 caught claude at a low draw,
and the same-session K-run spread is a **lower bound** on true run-to-run jitter, exactly as the
PREREG flagged. (gpt's and gemini's cross-session draws fell inside their within-session bands.)

## Interpretation (modest)

1. **Trigger (a) fires: the jitter is near-chance-concentrated and ceiling-protected.** On the
   *same* runs, the comp-correlative ceiling control was rock-steady (range 0.000 for two models;
   one model dropped one item on one run, range 0.033) while the hard near-chance let-alone swung
   up to 0.121. This is the cleanest possible form of
   [`essay/point-estimate-is-a-draw`](../essays/point-estimate-is-a-draw.md) trigger (a): jitter is
   *negligible at the ceiling and large near chance*, so the essay **narrows** its scope from "all
   single-run point estimates are draws" to "single-run point estimates **on hard, near-chance,
   functional instruments** are draws." The discipline (ask whether a gap clears the jitter) is
   unchanged; only the claimed *prevalence* of large jitter sharpens — to the small-and-functional
   cell where it was measured, leaving ceilings and clean separations untouched.
2. **The ~±0.12 estimate is confirmed for gpt — and shown to be model-specific.** gpt's let-alone
   accuracy range is **0.121** across five runs (0.125 on the 24-item test cell), landing on the
   source result's "~±0.12 spread" estimate. But the jitter is **not** a panel constant: claude's
   range is 0.061 and gemini's 0.030. So the "~12%" is **gpt's** number on this instrument; the
   discipline reads "ask whether the gap clears the jitter *for this model on this instrument*,"
   not "subtract 0.12 everywhere" (essay trigger (b), a transferable constant, is **not** licensed).
3. **gpt's residual is robust to the jitter — the central session-62 finding holds.** Because every
   one of the five runs (and the s62 draw) reads below 0.90 with a de-noised majority-vote 0.606
   (Wilson hi 0.753 < 0.90), the run-to-run noise that *could* have explained gpt's 0.636 as a low
   draw demonstrably does **not**: gpt's residual survives being measured five more times. This is
   the [`essay/output-channel-confound`](../essays/output-channel-confound.md) trigger-(b)
   residual, now with its magnitude **pinned** (de-noised ~0.61, not a single jittery 0.636) and its
   robustness to noise established. (As always: a *below-baseline residual* with uptake forced, not
   a near-chance absence and **not** "gpt cannot do let-alone" — undischargeable-negative still
   binds.)
4. **Two honest refinements of the source result.** (i) Session 62's *"gemini reproduced
   deterministically (0 flips)"* was a small-sample artifact of the single 24-item run-pair: over
   five runs on 33 items gemini churns **2 items** (range 0.030, pairwise agreement 0.970) — so the
   accurate statement is *"gemini is the **most stable** of the three,"* not strictly deterministic.
   (ii) claude's s62 let-alone test accuracy (0.708) was itself a **low draw**: its de-noised test
   accuracy is ~0.75–0.79 (majority-vote 0.750), so claude remains a baseline-region matcher
   (combined majority-vote 0.788) well above gpt's ~0.61 — the *gap* the source result called the
   robust signal is preserved and de-noised.

## What this does and does not license

**Does license:** a project-owned, revisable measurement statement that, on this hard near-chance
let-alone NLI instrument under forced decomposition at temperature 0, **single-run accuracies jitter
run-to-run by ~±0.12 for gpt, ~±0.06 for claude, and ~±0.03 for gemini, while the comp-correlative
ceiling control does not jitter at all** — so the jitter is **near-chance-concentrated and
ceiling-protected** (essay/point-estimate-is-a-draw trigger (a), fired). And that **gpt's
below-baseline let-alone residual is robust to this jitter** (de-noised majority-vote 0.606, Wilson
hi 0.753 < 0.90; every one of five runs < 0.90), pinning the magnitude the source result left at
~±0.12.

**Does NOT license:**
- **A transferable jitter constant.** The ~±0.12 is gpt's number on *this* instrument; claude and
  gemini differ by 2–4×, and the ceiling control is jitter-free. essay trigger (b) stays unlicensed.
- **A precise single-number let-alone accuracy.** Even de-noised, the right object is the *band*
  (gpt [0.437, 0.753] Wilson on the modal labels), not a third decimal place.
- **"gpt cannot do let-alone."** Forbidden (undischargeable-negative). gpt is well above the 0.33
  floor and externalizes the inference; the claim is a below-baseline residual.
- **A claim about the *mechanism* of temp-0 nondeterminism.** This run measures *that* the labels
  jitter and *where* (near chance, not at ceiling); *why* (FP non-associativity / batching / routing)
  is unsourced in-repo and not asserted (essay trigger (c); queued in [`base/wanted.md`](../../base/wanted.md)).
- **A revision of any large, concordant, or ceiling result.** The ceiling control's 0.000 jitter is
  positive evidence that those results are jitter-robust; the discipline targets the
  small-and-functional cell only.

## Limits

- **Same-session lower bound.** The five runs were collected sequentially within one session;
  cross-session/cross-hardware jitter can be larger (claude's single s60→s62 swing of 0.125 exceeded
  its within-session range of 0.061). The within-session figures are a **floor**, reported as such.
- **Item ceiling unchanged.** 33 is still the max human-annotated let-alone N; this run buys
  measurement precision (the jitter floor and the de-noised estimate), not new items.
- **One instrument, one construction, one date.** The jitter magnitudes are this instrument's; the
  transferability question is explicitly left open (essay trigger (b)).
- **Contamination (inherited).** Public items; a *match* cannot distinguish learned
  construction-meaning from memory. The robust signals are the within-model jitter contrast (ceiling
  vs near-chance) and the de-noised gpt-vs-others gap; the absolute 0.90 comparison inherits the
  contamination caveat from session 57.
- **Majority vote over 5 is itself an estimate.** With K=5 the modal label is a low-K majority; the
  de-noised accuracies carry their own (smaller) uncertainty, reported as Wilson intervals on the
  modal labels.

## Provenance

- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (CxNLI Exp-1 gold + ≈0.90 native-speaker baseline; ratified 2026-05-29).
  Source: [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md).
- Operationalization (NLI answer-key) governed by the ratified
  [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md);
  the repeated-run measurement is an extension under it (no new decision owed; independent pre-run
  critic GO, fresh agent).
- Refines [`result/scivetti-let-alone-powered-rerun-v1`](scivetti-let-alone-powered-rerun-v1.md)
  (pins its ~±0.12 estimate, confirms the residual robust to noise, refines its "gemini
  deterministic" to "gemini most stable").
- No license upstream → read in place, **not mirrored**; the working-surface CoT (which restates
  source text) is **gitignored** under `raw/cot/`; the committed artifact is
  `raw/run{k}-{slot}-labels.json` (run index + item_id + cxn + split + gold + label + parse_mode +
  uptake + content sha256 + usage, **NO text**). Numbers reproducible from the committed `raw/` +
  `analyze.py` against a local Scivetti clone. Independent post-run verifier (fresh agent)
  **REPRODUCED** every per-run accuracy, range/SD, churn, mean pairwise agreement, majority-vote
  accuracy + Wilson CI, the trigger-(a) reading, the uptake/ceiling guard, the cross-session
  comparison, the billed cost, parse integrity, and confirmed no gold-leak path.

## Status

`status: proposed`, `contingent-on: []` (the governing operationalization decision and the Scivetti
anchor are both ratified). What is `proposed` is the project's reading. Promotion past `proposed`
awaits Tom's review. *(Governance note, s183: since the autonomous-era amendment of 2026-06-12 —
[`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous cross-session adversarial
review; Tom holds a standing override. The promotion in fact landed:
[`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md), s177.)*
This result **discharges** the trigger-(g) / trigger-(a) repeated-run redirect:
the jitter is pinned (near-chance-concentrated, ceiling-protected, model-specific), and gpt's
residual is established robust to it. No further repeated-run power is owed on this construction.
