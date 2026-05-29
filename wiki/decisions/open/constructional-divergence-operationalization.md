---
id: constructional-divergence-operationalization
title: How is the constructional-divergence / meaning-use probe operationalized (instrument, thresholds, frequency-matching)?
status: open
opened: 2026-05-29
opened-by: orchestrator
contingent-artifacts:
  - open-question/constructional-divergence-probe
  - design/comparative-correlative-v1
---

# Decision: constructional-divergence probe operationalization

## Question

The open question [`open-question/constructional-divergence-probe`](../../findings/open-questions/constructional-divergence-probe.md) and the first design that instantiates it, [`design/comparative-correlative-v1`](../../../experiments/designs/comparative-correlative-v1.md), turn on operationalization choices that — per the charter's operationalization gate ([`PROJECT.md`](../../../PROJECT.md) §8, [`CLAUDE.md`](../../../CLAUDE.md) rule 5) — must be fixed **before** any probe runs, not retuned after seeing a null. This is the gate class where an autonomous loop quietly cheats by adjusting the indicator until a result turns positive. The decision locks three things for the upper-ladder (Tier 3→4 / inference-licensing) constructional probes:

1. **Instrument.** NLI / entailment framing (Scivetti-style) vs. forced-choice covariation/inference-direction question vs. both — and, if both, which instrument grounds which indicator.
2. **Gap / threshold definitions.** What construction-vs-control gap, direction-sensitivity rate, and generalization-persistence margin count as confirmation, and the rule for the "below human baseline" comparison.
3. **Frequency-matching procedure.** How typical vs. atypical / held-out lexical fillers are selected and frozen so a positive result is not an n-gram artifact (shared concern with [`open-question/constructional-vs-frequency-confound`](../../findings/open-questions/constructional-vs-frequency-confound.md)).

This decision is the upper-ladder counterpart of `aann-operationalization` (which governs the Tier 0–1 acceptability/surprisal probe). It is generic to the divergence-probe family; the comparative-correlative design is its first client, and the caused-motion / conative / way designs would reuse it.

## Options / the live choices

### Instrument

- **A. NLI / entailment only.** Apples-to-apples with the candidate human anchor (the Scivetti CxNLI subsets, 3-way NLI with a native-speaker accuracy baseline). Downside: not the instrument Weissweiler et al. 2022 used (masked/cloze semantic-application), so the encoder-PLM baseline is not interchangeable.
- **B. Forced-choice direction/inference question only.** Closer to Weissweiler's semantic-application framing and the cleanest read on direction-sensitivity; downside: no apples-to-apples human baseline.
- **C. Both, each grounding the indicator it fits (provisional default).** NLI grounds the human-comparison arm (against Scivetti); forced-choice grounds the direction-sensitivity indicator and the generational comparison to Weissweiler. **Hard rule:** never cross-compare an NLI number against the Weissweiler encoder semantic-application baseline as if interchangeable.

### Thresholds (provisional defaults, from the CC design — to be ratified or replaced, then frozen)

- Construction-vs-control gap **≥ 30 pp** in ≥ 2 of 3 panel models (matches the way-construction design's convention).
- Direction-sensitivity (e.g. inverse-CC flip) rate **≥ 70%** in ≥ 2 of 3 models.
- Generalization persistence: atypical/held-out rate **within 15 pp** of the typical rate (no collapse) in ≥ 2 of 3 models.
- "Below human baseline" rule: the panel's NLI accuracy on the construction subset is reported against Scivetti's native-speaker baseline; "narrows but does not close" requires clearing the encoder-PLM chance baseline (comparable framing) while sitting measurably below the human baseline.

### Frequency-matching

- Pick the proxy for "atypical / unlikely-to-be-memorised" fillers (the Scivetti atypical-filler lever vs. a proxy-corpus frequency floor), and freeze the typical/atypical split with the item list **before** the run. Resolve jointly with [`open-question/constructional-vs-frequency-confound`](../../findings/open-questions/constructional-vs-frequency-confound.md) so the family of probes uses one frequency-control spine.

## Provisional default (in force until Tom ratifies)

Instrument **C** (both, each grounding its own indicator, with the no-cross-comparison rule); the thresholds and frequency-matching as listed above, **frozen at item-commit time**. Any design contingent on this decision (currently the CC design) stays `provisional` and may not promote a human-comparison finding to settled until Tom ratifies.

Rationale: (i) running both instruments is cheap (well under the budget cap) and lets each indicator use the framing that grounds it; (ii) the thresholds reuse the project's existing 30 pp / 70% conventions so they are not bespoke-tuned per probe; (iii) freezing before the run is the whole point of the gate.

## What would change the default

- Tom prefers a single instrument (collapse to A or B), or sets different thresholds, or names a specific frequency-control proxy.
- The Scivetti repo inspection (gated separately, see the resource page) reveals the CC/other subsets cannot ground an NLI human baseline, pushing toward B + a wanted request.

## Notes for the resolver

Tom: a one-line ratification is enough — "C + those thresholds, frozen", "NLI only", or set your own numbers. This decision governs the *family* of upper-ladder divergence probes; ratifying it once lets the comparative-correlative (and later caused-motion / conative / way) designs run without re-litigating the instrument each time. It is paired with `comparative-correlative-anchor` (which fixes the human anchor) and with the Scivetti repo-inspection gate noted on [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md).
