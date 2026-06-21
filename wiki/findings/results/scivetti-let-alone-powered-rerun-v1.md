---
type: result
id: scivetti-let-alone-powered-rerun-v1
title: The powered re-run confirms gpt's below-baseline let-alone residual at higher N (and reproduces it exactly) — a cleaner channel-controlled residual — but exposes ~12% temp-0 label stochasticity as the new binding limit, not item count
meaning-senses:
  - constructional
  - inferential
  - human-comparison
  - model-internal
status: proposed
contingent-on: []
created: 2026-06-20
updated: 2026-06-20
links:
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: refines
    target: result/scivetti-let-alone-forced-decomposition-v1
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: essay/witness-seeking-economics
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Result: POWERED let-alone forced-decomposition re-run (trigger-(g))

The **powered re-run** that
[`result/scivetti-let-alone-forced-decomposition-v1`](scivetti-let-alone-forced-decomposition-v1.md)
(session 60) and
[`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md) §"The partial
witness" (revision trigger (g)) prescribed for session 60's **partial witness**: gpt-5.4-mini's
directional-but-underpowered +0.21 let-alone lift under forced uptake (0.583 on n = 24,
sign-test p = 0.090, below the ≈0.90 human baseline). The continuation is a **powered re-run
of the same forced-decomposition axis** with **more let-alone items** — explicitly exempt
from the "more of the same probe cannot" caution because session 60 left a directional
*signal*, not a null. The forced-decomposition instrument is held **byte-identical** to
session 60; the let-alone target is enlarged **24 → 33** with the only additional
human-annotated let-alone items in the upstream release (the **9 disjoint** train-split
items; the 1-example train split is a strict subset, so **33 is the ceiling** of available
human-anchored let-alone N).

## One-line finding

With the let-alone set enlarged to the maximum available 33 items, **gpt's below-baseline
residual HOLDS at higher power** (combined 0.636, Wilson CI **[0.466, 0.778]**, hi < 0.90 →
pre-registered verdict **CONFIRMS-RESIDUAL**) — and **gpt's session-60 test-item *accuracy*
reproduced exactly** (0.583 → 0.583, via 3 offsetting label flips — see below) while the
**fresh disjoint** train items independently came in below baseline (7/9 = 0.778). Uptake stayed induced (33/33
worked, median 125 completion tokens) and the comp-correlative ceiling control is
**PRESERVED** (1.000) for all three, so this is the **cleanest channel-controlled let-alone
residual the record has** — the [`essay/output-channel-confound`](../essays/output-channel-confound.md)
**trigger-(b)** contrast case, sharpened from session 60's *candidate* toward a *fired*
reading (still descriptive + contamination-caveated, **never** "cannot"). **But the run's
most important new lesson cuts the other way:** claude — the manipulation-check control that
matches baseline (s60 0.833) — **fell to 0.708 on the *identical* 24 test items this run**
(3 labels flipped, *all* adverse), revealing **~12% run-to-run label stochasticity at
temperature 0** (claude *and* gpt each flip 3/24 between two identical runs), a swing
**comparable to the residual gap**. So the binding limit going forward is **measurement
noise, not item count** — the trigger-(g) "design/measurement, not count, limits power →
redirect axis" outcome. gemini reproduced **deterministically** (0 flips) and stays at
baseline (0.909).

## What ran

- **Design: same instrument, enlarged item set.** The ONLY change vs session 60 is the
  let-alone item *count* (24 test → 33 = 24 test + 9 **disjoint** train). The
  forced-decomposition response format (`NLI_SYS_DECOMP`) is **byte-identical** to session
  60 (programmatically diff-checked, both 909 chars); same 0/1/2 label definitions, same
  gold (not shown), same panel, temperature 0, gemini `effort: minimal` held constant.
- **The 9 train items are DISJOINT** (0 shared premise/hypothesis pairs, 0 shared premises —
  3 distinct source sentences), balanced 3/3/3, from the **same** human-annotated release /
  construction / anchor. Provenance re-asserted: full-set sha `1c5cffb18c5ef78e` (== sessions
  57/58/60), s60-subset sha `9be31a8fea8d7f16`, frozen-63 sha `1b87dc871e4ec8dd`.
- **Cells.** let-alone combined n = 33 (the target, balanced 11/11/11); comp-correlative
  n = 30 (the ceiling control, byte-identical to s57/58/60).
- **Integrity.** 63 rows/model, **0 missing**, **189/189 parsed via the `FINAL:` tag** (0
  fallbacks), **0 missing `usage.cost`**. All three models **worked 33/33** let-alone items.
- **Cost** (billed `usage.cost`): **$0.3921** (claude $0.235 / gpt $0.045 / gemini $0.112).
  On pre-flight ($0.39). Under the $0.80 abort and the $2.50 single-run flag; UTC-day
  2026-06-20 total after this run ≈ $4.52, under the $5 cap.
- **Governance.** A same-instrument **power extension** under the already-ratified Scivetti
  answer-key anchor (ratified 2026-05-29) + `constructional-divergence-operationalization`;
  it does **not** change *what* is scored against the human gold (same labels, same gold) —
  only the item count. No demonstration items. **No new decision owed** (independent pre-run
  critic GO, fresh agent). Independent post-run verifier (fresh agent) **REPRODUCED** every
  number from raw.

## Results

Human reference (fixed, not retuned): Scivetti Exp-1 native-speaker accuracy ≈ 0.90; 3-way
chance ≈ 0.33. comparative-correlative carries the **ratified anchor**; let-alone is
**descriptive** from the same human-annotated release (not individually anchored), exactly
as sessions 57/58/60.

### let-alone (combined n = 33) — the powered target

| model | s60 test (24) | **this: combined (33)** | test (24) | train (9, disjoint) | vs human 0.90 | verdict |
|---|---:|---:|---:|---:|---|---|
| claude-sonnet-4.6 | 0.833 | **0.727** [0.558, 0.849] | 0.708 | 0.778 | CI hi < 0.90 | (control — see below) |
| gpt-5.4-mini | 0.583 | **0.636** [0.466, 0.778] | 0.583 | 0.778 | **CI hi 0.778 < 0.90** | **CONFIRMS-RESIDUAL** |
| gemini-3.5-flash | 0.875 | **0.909** [0.764, 0.969] | 0.875 | 1.000 | CI covers 0.90 | DISSOLVES (at baseline) |

### Run-to-run label stability (the identical 24 test items, session 60 → this run)

| model | s60 test acc | this test acc | label agreement | flips | direction of flips |
|---|---:|---:|---:|---:|---|
| claude-sonnet-4.6 | 0.833 | 0.708 | 21/24 (0.875) | 3 | **all adverse** (✓→✗: items #10, #18, #31) |
| gpt-5.4-mini | 0.583 | 0.583 | 21/24 (0.875) | 3 | **mixed, net 0** (1 ✓→✗ #15, 1 ✗→✓ #26, 1 ✗→✗ #27) |
| gemini-3.5-flash | 0.875 | 0.875 | 24/24 (1.000) | 0 | **deterministic** |

### comparative-correlative (n = 30) — ceiling control

| model | this run | control guard |
|---|---:|---|
| claude-sonnet-4.6 | 1.000 [0.886, 1.000] | **PRESERVED** |
| gpt-5.4-mini | 1.000 [0.886, 1.000] | **PRESERVED** |
| gemini-3.5-flash | 1.000 [0.886, 1.000] | **PRESERVED** |

### Uptake (let-alone, all 33) — the precondition for the channel reading

All three models **worked 33/33** (≥ 40 pre-`FINAL` chars + ≥ 2 numbered steps); median
completion tokens claude 211 / gpt 125 / gemini 170. The wide channel was **genuinely
exercised** by every model, so the residual is read off a channel actually used.

## Interpretation (modest)

1. **gpt's below-baseline let-alone residual is confirmed at higher power — and reproduces
   at the accuracy level.** Two independent strands agree: (i) gpt's session-60 24-item
   *accuracy* reproduced **exactly** (0.583 → 0.583 — though via 3 *offsetting* temp-0 label
   flips, not zero churn: gpt is subject to the same ~12% label stochasticity as claude, its
   net effect just cancelled this draw), and (ii) the **9 fresh disjoint** train items came
   in at 0.778, also below the 0.90 baseline. The combined 33-item Wilson CI hi is **0.778 <
   0.90**, a tighter and still-below-baseline interval than session 60's [0.388, 0.755]. With uptake forced (33/33 worked) and the control preserved,
   this is the **cleanest channel-controlled residual** in the record:
   [`essay/output-channel-confound`](../essays/output-channel-confound.md) **trigger (b)**
   ("a serial-computation negative that *survives* a genuinely-widened channel") moves from
   session 60's *candidate* toward a *fired* reading — gpt externalizes the inference and
   **still** falls below the human level. (As session 60 stressed: "survives" means a
   **below-baseline** residual, not *near-chance persistence* — gpt at 0.636 is well above
   the 0.33 floor.)
2. **But the run's headline lesson is a measurement one: temp-0 labels are not
   deterministic, and the run-to-run swing rivals the effect.** claude — a baseline-matcher
   (s60 0.833) and the run's manipulation-check control — read **0.708** on the *same* 24
   items this run, because 3 of its labels flipped and **all 3 went the wrong way**. gpt
   likewise flipped 3/24 (its flips happened to cancel); only gemini was deterministic. A
   **~12% per-run label swing** on this hard, small construction is **comparable to the gpt
   residual gap** (0.636 vs 0.90). So a single run's accuracy is a *draw*, and the Wilson CI
   (which assumes a fixed per-item Bernoulli rate) **understates** the true across-run
   uncertainty. This is exactly the [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md)
   trigger-(g) contingency: a re-run can reveal that **the design/measurement, not the item
   count, limits power**, redirecting the next spend to a *different* axis — here **repeated
   runs / within-run multi-sampling to average out label noise**, not yet-more items (33 is
   already the item ceiling).
3. **Why claude's swing does not dissolve the gpt conclusion — but does cap its strength.**
   The data actively *defends* gpt: the model that swung directionally (claude, 3 adverse
   flips) is the manipulation-check control, **not** the trigger subject; the trigger
   subject (gpt) held its *accuracy* still (its flips cancelled). So the "gpt's 0.636 is just
   a low draw" worry is *weakened*, not strengthened, by the contrast. And the residual is
   robust to a claude-sized swing: even allowing gpt a +0.12 favorable draw, its upper
   plausible accuracy (~0.76) stays **below 0.90**. The honest force is therefore: the
   residual is **real and reproduces at the accuracy level**, but its **exact magnitude**
   carries an unquantified per-run stochastic component (~±0.12) — the robust signal is the
   *gap* between gpt (~0.6) and the baseline-matchers (~0.83–0.88), not gpt's precise 0.636.
4. **gemini is the clean manipulation check; claude's drop is noise, not a broken
   instrument.** gemini reproduced deterministically and sits at baseline (0.909); the
   comp-correlative ceiling control is **PRESERVED at 1.000 for all three** — so the larger
   item set did **not** break the instrument. claude's let-alone drop is traced entirely to
   run-to-run flips on the *test* items (its *train* leg, 0.778, is higher than its test leg,
   0.708), i.e. measurement noise, not a degraded scaffold.

## What this does and does not license

**Does license:** a project-owned, revisable statement that, with uptake forced and the
let-alone set at its human-anchored ceiling (33), **gpt-5.4-mini's let-alone accuracy stays
below the ≈0.90 human baseline** (combined 0.636, CI hi 0.778 < 0.90), reproducing the
session-60 test result exactly and extending to fresh disjoint items — the cleanest
channel-controlled residual in the record (output-channel-confound trigger (b), now *fired*
with a magnitude caveat). And a methodological statement that **the binding precision limit
on this construction is now temp-0 label stochasticity (~12% per run), not item count.**

**Does NOT license:**
- **"gpt cannot do let-alone."** Forbidden (undischargeable-negative). gpt is well above
  chance and externalizes the inference; the claim is a *below-baseline residual*, not an
  absence.
- **A precise residual magnitude.** claude's 0.833→0.708 swing on identical items shows
  per-run point estimates carry ~±0.12 noise; the robust signal is the *gap* between gpt and
  the baseline-matchers, not gpt's exact 0.636.
- **A clean within-model paired-lift verdict.** The session-60 vs-offered paired sign-test
  (+0.21, p = 0.090) is **NOT** powered by this run — the 9 new items have no offered-surface
  arm — so the "did forcing uptake raise gpt" question stays at its session-60 strength. This
  run powers the **vs-baseline residual**, which is what trigger (b) needs.
- **A "models have scalar-construction meaning" verdict.** let-alone items are public →
  answer-key match cannot distinguish learned construction-meaning from memory (session 57
  *Limits*). The robust signals are the uptake jump and the within-model contrasts; the
  absolute 0.90 comparison inherits the contamination caveat.

## Limits

- **The decisive new limit: temp-0 label stochasticity.** ~3/24 labels flip between two
  byte-identical runs for both claude and gpt (gemini deterministic). Single-run accuracies
  on this construction are draws with ~±0.12 spread; CIs that assume fixed per-item rates
  understate across-run uncertainty. The right next move is **repeated runs / multi-sample**,
  not more items. **→ Done (session 64):**
  [`result/scivetti-let-alone-repeated-runs-v1`](scivetti-let-alone-repeated-runs-v1.md) ran the
  byte-identical instrument **K = 5** times and **pins** this — the swing is **gpt ~±0.12 / claude
  ~0.06 / gemini ~0.03** (model-specific, *not* a constant), it is **ceiling-protected** (the
  comp-corr control did not jitter), gemini is **most-stable not strictly deterministic** (2/33 over
  five runs), and **gpt's below-baseline residual survives** the jitter (de-noised majority-vote
  0.606; every one of five runs < 0.90). The "~12%" / "gemini deterministic" phrasings on this page
  are the **single-run-pair** read; the K = 5 measurement supersedes their magnitude/determinism
  detail (the finding — gpt's residual — is unchanged and strengthened).
- **Item ceiling reached.** 33 is the maximum human-annotated let-alone N in the upstream
  release (the 1-example train split ⊆ the 9 used). No further power is available from this
  resource without new human annotation (out of scope: no human subjects).
- **Small train leg.** The disjoint generalization rests on 9 items (7/9); directionally
  below baseline, but wide.
- **Contamination (inherited).** Public items; a *match* cannot distinguish learned
  construction-meaning from memory.
- **Shared priors (charter §2.5).** The human baseline (Scivetti, aggregate) is the
  independent bearing for the accuracy leg; the format/uptake contrast is model-internal.

## Provenance

- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (CxNLI Exp-1 gold + ≈0.90 native-speaker baseline; ratified 2026-05-29).
  Source: [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md).
- Operationalization (NLI answer-key) governed by the already-ratified
  [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md);
  the forced-decomposition format + the same-instrument power extension are extensions under
  it (no new decision owed; independent pre-run critic GO, fresh agent).
- Refines [`result/scivetti-let-alone-forced-decomposition-v1`](scivetti-let-alone-forced-decomposition-v1.md)
  (the partial witness this run powers).
- No license upstream → read in place, **not mirrored**; the working-surface CoT (which
  restates source text) is **gitignored** under `raw/cot/`; the committed artifact is
  `raw/{slot}-labels.json` (item_id + cxn + split + gold + label + parse_mode + uptake +
  content sha256 + usage, NO text). Numbers reproducible from the committed `raw/` +
  `analyze.py` + the session-60 `raw/` against a local Scivetti clone. Independent post-run
  verifier (fresh agent) **REPRODUCED** every accuracy, Wilson CI, the run-to-run flip counts
  and directions, the internal replication, the uptake check, the billed cost, parse
  integrity, the `content_sha256`↔CoT binding, CoT genuineness, and confirmed no gold-leak
  path.

## Status

`status: proposed`, `contingent-on: []` (the governing operationalization decision and the
Scivetti anchor are both ratified). What is `proposed` is the project's reading. Promotion
past `proposed` awaits Tom's review. The natural next probe is **not** more items (the
ceiling is reached) but a **repeated-run / multi-sample** design to characterize the temp-0
label distribution and pin the residual magnitude — recorded as the trigger-(g) redirect.
