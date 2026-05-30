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
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `d799ef279f589db9`): 44 items — 12 Levin conative-class verbs × {transitive, conative, cue} + 4 non-alternating control verbs × {transitive, resist}.

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

(to be filled from the independent adversarial pass; any item fixes re-freeze the hash.)

## Results / cost

(to be filled after the run.)
