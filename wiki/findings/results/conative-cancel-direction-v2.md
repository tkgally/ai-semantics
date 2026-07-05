---
type: result
id: conative-cancel-direction-v2
title: Cancel-direction conative v2 — the add/cancel asymmetry survives de-confounding from ceiling; at matched conflicting-cue task structure, decoders suppress a lexically-default inference far less reliably than they license an added one
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-30
updated: 2026-07-05
links:
  - rel: supports
    target: conjecture/conative-construction
  - rel: refines
    target: result/conative-minimal-pair-divergence-v1
  - rel: refines
    target: result/argument-structure-coercion-v2
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/coercion
---

# Result: cancel-direction conative probe v2 (off-ceiling, de-confounding arm)

The **companion** off-ceiling probe to the add-direction v2 ([`result/argument-structure-coercion-v2`](argument-structure-coercion-v2.md)), built to **de-confound the project's tentative "add easier than cancel" asymmetry from ceiling**. Design + frozen stimuli: [`design/conative-cancel-v2`](../../../experiments/designs/conative-cancel-v2.md); governing operationalization (ratified): [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md) (which explicitly scopes "the companion harder-conative cancel-direction probe"); run record: [`experiments/runs/2026-05-30-conative-cancel-probe-v2/`](../../../experiments/runs/2026-05-30-conative-cancel-probe-v2/README.md).

## The confound it targets

The project carried a **tentative** generalization ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md) *(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) — cited here as the edition this page engaged.)*): decoders more readily **license** a construction's *added* inference (caused-motion, way — v1 ceiling) than **suppress** a *lexically-default* one (the conative's completed-contact — v1 off-ceiling, instrument-fragile; [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md)). But the add probes ran at ceiling and the cancel probe off ceiling, so "add easier than cancel" was **confounded with difficulty**. This probe puts the cancel direction in the **same conflicting-cue paradigm** the add-direction v2 used, so the two are compared at matched task structure.

The conative ("kicked **at** the ball") cancels the completed-contact entailment the transitive ("kicked the ball") carries. Indicator: affirm-contact rate on "&lt;subj&gt; made contact with &lt;obj&gt;" (FC YES / NLI entailment), temperature 0, both instruments, the ratified 3-family panel.

## One-line finding

**The asymmetry survives de-confounding: at matched conflicting-cue task structure, the panel suppresses the lexical default far less reliably — and far less uniformly — than it licenses an added inference.** The transitive lexical default is at ceiling (affirm-contact 91.7–100%), but **suppression with no cue** (the conative; `100 − conative_affirm`) is off-ceiling and model/instrument-dependent — NLI **[58.3, 0.0, 66.7] pp**, FC **[66.7, 33.3, 83.3] pp** — where the *add*-direction's matched **licensing-no-cue** (canonical affirm) was ~ceiling (claude/gemini 100%, gpt-5.4-mini 70–80%). gpt-5.4-mini **fails conative suppression entirely under NLI** (conative affirm 100% — it calls *kicked at the ball* an entailment of contact), replicating the v1 conative wrinkle and the [`result/instrument-disagreement-reanalysis-v1`](instrument-disagreement-reanalysis-v1.md) finding.

This is the design's **"add stays robust off ceiling while cancel degrades more"** outcome → the asymmetry is about **direction**, not a ceiling artifact, and the theory's tentative generalization is **strengthened** (modestly — see caveats).

## Numbers

Affirm-contact rate (%), conative-class verbs (12 verbs × {transitive, conative, cue}), 0 NA / 264 calls:

| model | instr | transitive (default) | conative (suppress→low) | cue (re-license) | suppression-no-cue | cue-following |
|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | NLI | 100.0 | 41.7 | 100.0 | 58.3 | 100.0 |
| claude-sonnet-4.6 | FC | 100.0 | 33.3 | 75.0 | 66.7 | 75.0 |
| gpt-5.4-mini | NLI | 91.7 | **100.0** | 100.0 | **0.0** | 100.0 |
| gpt-5.4-mini | FC | 100.0 | 66.7 | 91.7 | 33.3 | 91.7 |
| gemini-3.5-flash | NLI | 100.0 | 33.3 | 100.0 | 66.7 | 100.0 |
| gemini-3.5-flash | FC | 100.0 | 16.7 | **25.0** | 83.3 | **25.0** |

- **suppression-no-cue** = `100 − conative_affirm` (construction-following with no cue) — the matched analogue of the add-direction's **canonical/licensing-no-cue** (~70–100%, mostly ceiling). Cancel is uniformly lower and far more variable.
- **cue-following** = cue_affirm (does an explicit contact consequence — *…and the ball sailed across the field* — re-license contact?). NLI: all re-license (100%). FC: claude/gpt re-license (75/91.7%) but **gemini over-suppresses (25%)** — it will not affirm contact even when the cue states a contact consequence.

## Two distinct off-ceiling failures (instrument-fragility, first-class)

The cancel direction exposes **more** instrument/model fragility than the add direction did:
1. **gpt-5.4-mini under NLI does not suppress at all** (conative = 100% affirm) but recovers under FC (66.7%) — the same NLI-fails/FC-recovers signature as the v1 conative. Cf. [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md).
2. **gemini-3.5-flash under FC over-suppresses** — a *sticky* conative: cue-following only 25%, so it withholds contact even against an explicit contact consequence. The opposite error from gpt-mini.

No single model is clean on both suppression and re-licensing across both instruments — unlike the add direction, where all three floored cleanly under the explicit denial.

## Cross-direction comparison (the de-confounding payoff)

| quantity | add direction (v2, committed) | cancel direction (this) |
|---|---|---|
| construction reading, **no cue** | canonical affirm ~ceiling (claude/gemini 100; gpt 70–80) | suppression-no-cue **0–83**, gpt-mini 0 (NLI) |
| explicit conflicting cue respected | cue affirm floored 0–20 (cue-following 80–100) | cue-following 25–100 (gemini FC 25) |

At matched task structure the **no-cue** construction reading is the discriminating cell: licensing an added inference is near-ceiling and uniform; suppressing a lexical default is partial, model-dependent, and (for gpt-mini under NLI) absent. The asymmetry is **about direction**.

## Caveats (lead first)

- **Small N, panel-as-subjects.** 12 verbs × 3 conditions × 3 models; rates carry wide per-cell uncertainty. Read as a direction-of-effect signal, not a precise magnitude.
- **Internal-contrast-only; no human baseline on the cue arm.** The `transitive`–`conative` minimal pair keeps the v1 phenomenon-level conative anchor ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) conative subset); the **cue arm has no in-repo human norm** and the contact-cued conative's "correct" reading is contestable for humans → **no human-level claim** on it (`anchor: internal-contrast-only`, [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). No human label invented.
- **Weak-contrast verbs flagged.** scratch/claw are surface-contact verbs whose "at" frame still implies grazing contact (pre-run critique); they may inflate conative_affirm slightly, *strengthening* (not weakening) the "suppression is hard" reading.
- **Control arm wrinkle.** The non-alternating control verbs (touch/embrace/break/shatter) show gemini under-affirming even the *transitive* contact (ctrl-transitive 50%), so its control floor is noisy; the headline rests on the conative-class verbs, not the small control arm.
- **"Strengthened," not "established."** The generalization is a modest direction-of-effect claim across three models on the project's own stimuli; it is not a human-anchored or large-N result.

## Bearing

Refines [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md) (adds the cue arm + the matched cross-direction comparison) and the add-direction [`result/argument-structure-coercion-v2`](argument-structure-coercion-v2.md) (supplies its missing cancel companion). Feeds [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md): the "license-easier-than-suppress" asymmetry is no longer flagged as confounded-with-ceiling. Internal-contrast-only by ratified decision ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md), 2026-05-31). Cost **$0.30 billed** (the probe's token-estimate of $0.059 undercounts ~5× — the harness's rate card is stale; see [`config/budget.md`](../../../config/budget.md)); 0 NA / 264 calls.
