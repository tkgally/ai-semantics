# Run record — conative cancel-direction probe v2 (off-ceiling, de-confounding arm)

**Date:** 2026-05-30
**Design (frozen, pre-registered):** [`design/conative-cancel-v2`](../../designs/conative-cancel-v2.md)
**Governing decision (ratified):** [`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (UNIFY + adopt default, 2026-05-29 — explicitly scopes "the companion harder-conative cancel-direction probe"). **No new decision.**
**Conjecture probed:** [`conjecture/conative-construction`](../../../wiki/findings/conjectures/conative-construction.md)
**Companion to:** [`experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/`](../2026-05-29-argument-structure-coercion-probe-v2/README.md) (the off-ceiling ADD-direction v2)
**Result page:** [`result/conative-cancel-direction-v2`](../../../wiki/findings/results/conative-cancel-direction-v2.md)

## What ran

The **cancel-direction** mirror of the off-ceiling add-direction v2, built to **de-confound the project's tentative "add easier than cancel" asymmetry from ceiling** (design §"Why this exists"). The conative ("kicked **at** the ball") cancels the completed-contact entailment the transitive carries; this probe puts that suppression in the **same conflicting-cue paradigm** the add-direction v2 used, so the two directions are compared at matched task structure.

- **Indicator:** affirm-contact rate (FC YES / NLI entailment) on "&lt;subj&gt; made contact with &lt;obj&gt;"; temperature 0, no logprobs → the existing 3-family behavioral panel.
- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C).
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `431945d4e1fa7a99`, after the pre-run critique fixes below): 44 items — 12 Levin conative-class verbs × {transitive, conative, cue} + 4 non-alternating control verbs × {transitive, resist}.

## Conditions

| condition | difficulty | example | affirm-contact gold |
|---|---|---|---|
| `transitive` | 1 | Maria kicked the ball. | YES (lexical default; ceiling anchor) |
| `conative` | 2 | Maria kicked at the ball. | NO / CANT_TELL (construction suppresses) |
| `cue` | 3 | Maria kicked at the ball, and the ball sailed across the field. | YES (explicit consequence re-asserts contact) |
| `resist` | 2 | Hana touched at the wall. | NA (anomalous; non-alternating verb; report rate) |

**Key arms.** *suppression-no-cue* = 100 − conative_affirm (compare to add-direction canonical affirm = licensing-no-cue). *cue-following* = cue_affirm (compare to add-direction cue-following = 100 − cue_affirm). The headline is the **cross-direction comparison** against the committed add-direction v2 `raw/results.json`, not a pass bar (ratified report-the-rate).

## Human anchor

**Pending / internal-contrast-only** (ratified Option-4 logic, same as the add-direction v2). The `transitive`–`conative` minimal pair keeps the v1 phenomenon-level conative anchor (Scivetti conative subset); the `cue` arm has **no in-repo human baseline** (Scivetti has no conflicting-cue items; the contact-cued conative's "correct" reading is contestable for humans) → **no human-level claim** on it. No human label invented.

## Pre-registration / no-retuning

- The difficulty axes, conflicting-cue reading rule, degradation criterion, and human-anchor scope were **fixed by the ratified `cc-v2-difficulty-operationalization` decision BEFORE this build** (the same gate that governs the add-direction v2). Building the cancel arm to mirror the already-run add arm is the §5 de-confounding design, not a retune.
- Items frozen + committed **before any probe call** (sha256[:16] `d799ef279f589db9`).
- **Adversarial pre-run pass:** an independent read-only subagent critiqued the frozen stimuli before the run (see "Pre-run critique" below).
- `analyze.py` reports raw affirm rates per condition + the derived de-confounding quantities; no threshold tuned after the run.

## Files

- `build_items.py` — emits + freezes `experiments/data/conative-cancel-v2/items.csv`.
- `probe.py` — runner (NLI + FC × 3 models), copied verbatim from the add-direction v2.
- `analyze.py` — affirm rate per condition; suppression-no-cue; cue-following; conative→cue shift; cross-model summary; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Pre-run critique

An **independent read-only adversarial subagent** critiqued the frozen stimuli before the run (anti-retuning §8 — stimulus fixes precede seeing any result). **No BLOCKERs**; gold logic internally consistent across all 44 rows. Applied its SHOULD-FIX items (re-froze `d799ef279f589db9` → `431945d4e1fa7a99`):

- **swat/cushion → swat/balloon** (+ cue "shot across the room"): "swatted at the cushion" (stationary) is marginal and "tumbled off the sofa" under-determined contact; the balloon variant cleanly entails contact under the cue.
- **strike/bell → whack/melon** (+ cue "the melon split open"): "strike at" has a dominant idiomatic *aim/attack* reading so "struck at the bell" is a marginal physical conative, and "rang out" weakly entailed *this* subject's contact; whack is a clean Levin hit-class conative.
- **kiss → embrace** (resist arm): "kiss at" alternates (air-kissing), so it did not anomalize crisply; "embraced at the child" is robustly anomalous.
- **jab cue "shuddered from the blow" → "jolted backward"**: "from the blow" presupposed a landed strike (near-circular with the contact hypothesis).
- **Kept, flagged:** scratch/claw are weaker-contrast surface verbs (the "at" frame implies grazing contact); reported with that caveat rather than dropped.

The kick/hit/punch/slash/stab/chop/hack core + touch/break/shatter resist arm were judged sound as-is.

## Results / cost

264 calls, **0 NA**, cost **$0.059** (A $0.039 / B $0.002 / C $0.017). **Headline: the add/cancel asymmetry survives de-confounding from ceiling.** The transitive lexical default is at ceiling (affirm-contact 91.7–100%), but **suppression-no-cue** (`100 − conative_affirm`) is off-ceiling and model/instrument-dependent — NLI [58.3, 0.0, 66.7] pp, FC [66.7, 33.3, 83.3] pp — vs the add-direction's matched **licensing-no-cue** ~ceiling (claude/gemini 100%, gpt-5.4-mini 70–80%). gpt-5.4-mini **fails suppression entirely under NLI** (conative affirm 100%) but recovers under FC; gemini **over-suppresses under FC** (cue-following 25% — won't re-license contact even against an explicit contact consequence). Full write-up + every number at [`result/conative-cancel-direction-v2`](../../../wiki/findings/results/conative-cancel-direction-v2.md); reproducible from `raw/results.json`.

**NOTE — path bug caught + fixed:** the `probe.py` copied from the add-direction v2 carried a hardcoded `ITEMS` path to `argument-structure-coercion-v2/items.csv`. The first run (pre-fix) therefore re-ran the OLD coercion-v2 stimuli (~$0.09 wasted, no result contaminated — nothing was written up from it). The path was corrected to `conative-cancel-v2/items.csv` and the probe re-run on the correct frozen items; the numbers above are from the corrected run.

**Post-run verification:** every figure was independently recomputed from the per-record `raw/*.json` by a read-only adversarial subagent (separate from `analyze.py`).
