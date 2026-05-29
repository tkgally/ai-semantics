---
id: cc-v2-difficulty-operationalization
title: How is the harder comparative-correlative v2 probe operationalized (difficulty axes, conflicting-cue bar, degradation-shape criterion)?
status: open
opened: 2026-05-29
opened-by: orchestrator
contingent-artifacts:
  - design/comparative-correlative-v2
---

# Decision: comparative-correlative v2 difficulty operationalization

## Why this exists

[`result/comparative-correlative-covariation-v1`](../../findings/results/comparative-correlative-covariation-v1.md) returned a *ceiling* positive; its lead caveat is that ceiling on an easy instrument is weak evidence for the strong reading. [`design/comparative-correlative-v2`](../../../experiments/designs/comparative-correlative-v2.md) proposes harder manipulations to find the breaking point. But the v1 thresholds were calibrated to a near-ceiling regime, and **choosing the v2 difficulty measures after seeing v1's ceiling is the canonical retuning trap** (charter §8). This gate fixes the v2 measures *before* any v2 probe runs. No v2 probe runs until this is ratified.

## The live choices (see design §3)

1. **Difficulty axes to include.** Conflicting-cue CC (world knowledge vs. stated direction — the key discriminator), multi-step/composed covariation, distractor/embedded CC (negation/modal/counterfactual), near-miss form controls, and a graded difficulty ladder. Which subset is in scope for v2, and how each is built and frozen.
2. **Conflicting-cue bar.** The confirm threshold for "follows the construction against world knowledge" — the number v1 could not test. Provisional: report the rate; do not pre-commit a pass bar so high it manufactures a null, nor so low it manufactures a pass. Candidate: ≥ 70% follow-construction in ≥ 2/3 models = "robust"; near 50% or world-knowledge-following = informative partial-null.
3. **Degradation-shape criterion.** What counts as "graceful degradation" (monotone, shallow slope on the difficulty ladder = computing something stressable) vs. "brittle cliff" (= shallow pattern). Pre-commit the operational definition.
4. **Human-anchor scope.** The Scivetti CC subset does not contain conflicting-cue/multi-step items, so those arms have no in-repo human norm. Decide: run them as internal-contrast-only (human clause = "pending"), or gate v2 on first fetching a human-rated harder-CC anchor (queue in `wanted.md`).

## Provisional default (in force until Tom ratifies — NOT acted on; v2 stays unrun)

Include conflicting-cue (primary) + multi-step + near-miss controls + the graded ladder; defer embedded-CC to a v3. Report conflicting-cue rate with "≥70% in ≥2/3 = robust, ~chance/world-following = partial-null" as the reading rule; degradation "monotone with slope < cliff-threshold = graceful" (cliff-threshold to be a fixed pp-drop-per-difficulty-step, frozen with the item set). Run harder arms as internal-contrast-only with the human clause marked pending; queue a human-rated harder-CC anchor in `wanted.md` rather than blocking on it. Keep both NLI + forced-choice instruments; free-text justification is a qualitative side-channel only, never a scored indicator.

## Scope-broadening proposed 2026-05-29 (surfacing — your call)

Since this gate was opened, the project has run **two more own-design Tier-4 positives that are also at/near ceiling** — [`result/caused-motion-minimal-pair-divergence-v1`](../../findings/results/caused-motion-minimal-pair-divergence-v1.md) (ceiling) and [`result/way-construction-traversal-v1`](../../findings/results/way-construction-traversal-v1.md) (above bar / near ceiling). All three "add-direction" positives carry the **same** lead caveat (ceiling on easy controls is weak evidence for deep processing), and a new unified off-ceiling design [`design/argument-structure-coercion-v2`](../../../experiments/designs/argument-structure-coercion-v2.md) now references **this** decision rather than spawning a parallel one. So the difficulty-operationalization question (axes, conflicting-cue confirm bar, degradation-shape criterion, human-anchor scope) is really **one** question shared across CC + caused-motion + way v2 designs.

**Proposed (not acted on):** broaden this decision's scope from "comparative-correlative v2" to **"argument-structure coercion v2 (CC + caused-motion + way)"**, so a single ratification fixes the off-ceiling difficulty measures for all of them at once. The provisional default above (conflicting-cue primary + multi-step/coercion-resisting + near-miss controls + graded ladder; report-the-rate, no manufactured pass bar; harder arms internal-contrast-only with human clause pending) carries over unchanged to the broadened scope. The new design also flags a **companion harder-conative (cancel-direction) probe** that, run as a matched off-ceiling pair with the add-direction v2, would *de-confound the add/cancel asymmetry from ceiling* — worth folding into the same gate. If you prefer to keep CC-v2 separate, say so and the new design will get its own gate. **Still open; this is surfacing, not a resolution.** Running ANY v2 stays blocked until this is ratified.

## Notes for the resolver

Tom: a one-line ratification or amendment is enough. The point of this gate is only to stop the next run from tuning v2's difficulty to whatever makes v1's ceiling look either robust or brittle. This is *not* urgent — v2 is a follow-up; the v1 results stand on their own (as ceiling positives with their caveat). If you'd rather not pursue a v2 at all, say so and this decision + the v2 designs can be retired. A one-liner on the scope question above ("unify" vs "keep CC-v2 separate") is also enough.
