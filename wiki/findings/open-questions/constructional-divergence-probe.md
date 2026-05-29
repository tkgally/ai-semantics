---
type: open-question
id: constructional-divergence-probe
title: What minimal project-run probe would turn the external constructional-divergence gap into a project result?
meaning-senses:
  - constructional
  - functional-vs-formal
  - human-comparison
status: open
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: depends-on
    target: claim/constructional-divergent-form-generalization-gap
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
  - rel: depends-on
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: conjecture/conative-construction
  - rel: depends-on
    target: conjecture/way-construction
---

# Open question: from an external divergence gap to a project-run result

## The question

[`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md) records, with in-repo human-comparison bearing, that current LLMs drop >40% (GPT-o1) on syntactically-identical / semantically-divergent constructional forms relative to a native-speaker baseline (≈0.90 / ≈0.83). But that claim is about an **external** paper's published aggregate result; the project has run **no probe of its own design** at the upper rungs of the evidence ladder (see [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), whose revision trigger names exactly this gap). 

What is the **smallest probe of the project's own design** — runnable read-only against the panel in [`config/models.md`](../../../config/models.md) under the budget cap — that would convert this external negative into a project `result` at the Tier 3→4 boundary: a replication and/or extension of the divergent-form contrast, against an in-repo human anchor, that the project itself produces and can revise?

## Why it matters

The theory page is currently honest that it claims "a *structure* (the ladder, the placements) plus one externally-grounded negative data point … and not yet any *result* of the project's own." This open question is the concrete path off that plateau. It is also where the project's distinctive assets bite: a lexicographer's fine sense-distinctions (which divergent-meaning pairs are genuinely minimal), and the **panel-as-subjects** design (cross-model divergence in the gap is itself data about whether the divergence-failure is model-specific or convergent — charter §6).

## What is already external, and what a project result needs

- **Already external (the claim):** Scivetti et al. 2025's aggregate cross-construction >40% drop with a native-speaker baseline.
- **What a project result adds, minimally:**
  1. The **panel's own** behavior on the syntactically-identical / semantically-divergent contrast, recorded under `experiments/` (prompts, models, date), so the finding is the project's to revise — not a citation of someone else's table.
  2. A **human anchor in-repo**: the Scivetti CxNLI-Distinction data ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)) — now the **ratified** anchor (2026-05-29) for the four CxG conjectures; the repo was de-anonymized and inspected (`status: partial`: per-item construction labels + a single gold answer per item). A per-construction result can compare panel labels to the per-item gold answers plus the aggregate ≈0.90/≈0.83 baseline; note the anchor is an answer key, not a graded per-item human distribution (single gold label only).
  3. A **memorization control**, reusing Scivetti's own lever: pragmatically atypical lexical fillers "unlikely to appear in pre-training data" — tying this probe to the method spine in [`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md).

## What a serious answer would look like

A minimal design that:

1. **Fixes the contrast.** A set of surface-identical sentence frames each readable under two constructions with divergent meaning (the Scivetti Experiment-2 logic), with the inference that distinguishes them. The three per-construction conjectures supply ready instances: caused-motion vs. its non-caused reading, conative vs. transitive ([`conjecture/conative-construction`](../conjectures/conative-construction.md) — the *sip at* / target-directedness contrast), way-manner vs. literal-path.
2. **Picks an instrument.** Either (a) the NLI/entailment format Scivetti uses (apples-to-apples with the external baseline, panel run as subjects), or (b) a surprisal/continuation contrast in the small-model lane (graded, but a different measure — and then the human anchor comparison must be re-derived). The choice is an **operationalization gate** (below).
3. **Defines the gap and a threshold** *before* seeing results: what magnitude of panel drop on the divergent condition, relative to the base condition and relative to the human baseline, counts as reproducing the effect — and what counts as a null (a first-class negative, charter §2.6).
4. **Exploits cross-model divergence.** Report per-model gaps; treat convergence as QA and divergence as signal about whether the failure is architectural or idiosyncratic.

## The operationalization gate (queue, do not auto-resolve)

Per charter §8 and [`CLAUDE.md`](../../../CLAUDE.md) rule 5, the choices in steps 2–3 are exactly where an autonomous loop would quietly cheat by retuning the threshold after seeing a null. They must be written into a decision page **before** the probe runs, not settled here:

- [`decisions/resolved/constructional-divergence-operationalization.md`](../../decisions/resolved/constructional-divergence-operationalization.md) (**ratified 2026-05-29**) — fixed the instrument (both NLI + forced-choice), the gap/threshold definitions (30 / 70 / within-15 pp), the human-baseline comparison, and the memorization-control requirement. The comparative-correlative design ([`design/comparative-correlative-v1`](../../../experiments/designs/comparative-correlative-v1.md)) is its first client.

This open-question only **names** the design space; it does not resolve it.

## Relation to the existing wedge

- It is the **upper-ladder counterpart** of [`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md): that question is the method spine for *surprisal* (Tier 1–2) probes; this one is for *inference-licensing / generalization* (Tier 3–4) probes. They share the memorization-control concern.
- It is the experimental cash-out of [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md): the claim reads an external negative; this question asks what project-run probe would let the project assert (or refute) it on its own evidence.
- Its per-construction instances are the three anchor-pending conjectures; resolving the relevant anchor decision is what lets a per-construction version of this probe produce a promotable result.

## Pointers for the next visit

- The Scivetti release repo is reachable (de-anonymized at github.com/melissatorgbi/beyond-memorization; inspected 2026-05-29). A future run can mirror it (license-check first) for the per-construction probe; the per-item gold answers are the anchor.
- Confirm which panel models expose token-level log-probs (needed for the surprisal-lane variant) vs. only API-level outputs (needed for the NLI-lane variant).
- Open the operationalization decision page **before** running, not after.
