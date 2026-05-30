---
type: design
id: conative-cancel-v2
title: conative cancel-direction v2 — the matched off-ceiling cancel arm that de-confounds the add/cancel asymmetry from ceiling
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: provisional
anchor: pending
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: operationalizes
    target: conjecture/conative-construction
  - rel: refines
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: design/argument-structure-coercion-v2
  - rel: depends-on
    target: result/argument-structure-coercion-v2
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v2 — conative, cancel-direction (the companion off-ceiling arm)

> **Status: provisional.** This is the **companion harder-conative cancel-direction probe** that [`design/argument-structure-coercion-v2`](argument-structure-coercion-v2.md) §5 + hook 3 call for. It is governed by the **same ratified gate** ([`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md), whose 2026-05-29 UNIFY ruling explicitly scopes "the companion harder-conative cancel-direction probe") — so **no new decision** is opened; the difficulty yardstick is already fixed. `contingent-on: []`.

## Why this exists — de-confound the add/cancel asymmetry from ceiling

The project carries a **tentative** generalization ([`theory/constructional-meaning-in-llms`](../../wiki/findings/theory/constructional-meaning-in-llms.md)): current decoders more readily **license** a construction's *added* inference (caused-motion, way — v1 at/near ceiling) than **suppress** a *lexically-default* one (the conative's completed-contact — v1 off-ceiling, instrument-fragile; [`result/conative-minimal-pair-divergence-v1`](../../wiki/findings/results/conative-minimal-pair-divergence-v1.md)).

**The asymmetry is confounded with ceiling.** The add-direction probes ran at ceiling; the cancel-direction (conative) ran off ceiling. So "add is easier than cancel" might just be "the add tasks were saturated and the cancel task was harder." The off-ceiling add-direction v2 ([`result/argument-structure-coercion-v2`](../../wiki/findings/results/argument-structure-coercion-v2.md)) showed the add ceilings are **cue-sensitive** (drop to floor under an explicit denial — H-deep). This design puts the **cancel** direction in the **same conflicting-cue paradigm**, so the two directions are compared at matched task structure. Only a matched off-ceiling add/cancel pair can tell whether the asymmetry is about *direction* or about *difficulty*.

## Conditions (verb + object held constant; Levin conative-class verbs)

Hypothesis throughout: *"&lt;subj&gt; made contact with &lt;obj&gt;."* The conative ("kicked **at** the ball") cancels the contact entailment the transitive ("kicked the ball") carries.

| condition | difficulty | example | affirm-contact gold | role |
|---|---|---|---|---|
| `transitive` | 1 | Maria kicked the ball. | YES (entailed) | lexical default — the ceiling anchor (what is being suppressed) |
| `conative` | 2 | Maria kicked at the ball. | NO / CANT_TELL (construction suppresses) | **the off-ceiling suppression** — v1's fragile quantity |
| `cue` | 3 | Maria kicked at the ball, **and the ball sailed across the field.** | YES (an explicit consequence re-asserts contact) | conflicting cue — mirror of the add-direction's denial cue |

Plus a **resist** arm (mirror of the add-direction's coercion-resisting verb): non-alternating contact verbs (touch-/break-class, which do *not* take the conative in Levin 1993) forced into the conative frame (*touched at the wall*) — anomalous, gold NA, report the affirm rate only.

The cue is the cancel-direction mirror of the add-direction's cue: there an explicit clause *denied* the added inference (a model computing it should withhold → affirm drops to floor); here an explicit consequence *re-asserts* the suppressed inference (a model computing it should affirm → contact re-licensed). The per-verb consequence clauses (e.g. *the rope split in two*; *the pad shuddered from the blow*) entail contact occurred **without echoing the hypothesis** "made contact" — so the cue is a real-world consequence, not a restatement of the gold.

## Indicator, derived measures, reading rule (frozen with the item set; report-the-rate)

Indicator (same as v1 + the add-direction v2): affirm-contact rate (FC YES / NLI entailment), temperature 0, logprob-free, both instruments. Derived, matched to the add direction:

- **suppression-no-cue** = 100 − conative_affirm (construction-following with no cue) — compare to add-direction **canonical affirm** (licensing-no-cue).
- **cue-following** = cue_affirm (does the model update toward contact under the explicit cue?) — compare to add-direction cue-following = 100 − cue_affirm (withholding the denied inference).
- **conative→cue shift** = cue_affirm − conative_affirm.

**Reading rule (ratified report-the-rate, no manufactured pass bar):** the headline is the **cross-direction comparison** against the committed add-direction v2 numbers (`2026-05-29-argument-structure-coercion-probe-v2/raw/results.json`), not a threshold. If suppression-no-cue stays **lower** than add's licensing-no-cue *even with the cue arm present*, the asymmetry is about **direction** (real; strengthens the tentative generalization). If both directions follow the cue comparably and only the no-cue canonical differs, the v1 asymmetry was **canonical difficulty** → down-grade the generalization to "the v1 add tasks were easier." If cancel handles the cue *better* than add, the asymmetry reverses (a surprise). Each reading is first-class; no threshold is tuned after the run.

## Human anchor — pending / internal-contrast-only

Per the ratified Option-4 logic (same as the add-direction v2): the `transitive` vs `conative` **minimal pair** retains the v1 phenomenon-level conative anchor ([`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md) conative subset, ratified). The **cue arm has no in-repo human baseline** — Scivetti has no conflicting-cue items, and the contact-cued conative's "correct" reading is contestable for humans → **no human-level claim** is asserted on it. No human label invented. `anchor: pending`.

## Harness / freeze / budget

Reuses the add-direction v2 harness verbatim (`build_items.py` → freeze → `probe.py` NLI+FC → `analyze.py`). Items frozen + committed before any probe call (`items.csv` sha256[:16] `431945d4e1fa7a99` after the pre-run critique fixes; 44 items = 12 conative-class verbs × {transitive, conative, cue} + 4 control verbs × {transitive, resist}). 44 × 2 instruments × 3 models = 264 calls; expected ≈ $0.05–0.08 (cf. v1 conative $0.071), well under the budget flag. Pre-flight per [`config/budget.md`](../../config/budget.md).
