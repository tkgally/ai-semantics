---
id: multimodal-panel-and-grounding-theory
title: For the new multimodal axis — which model panel, and which grounding theory to privilege?
status: open
opened: 2026-05-30
opened-by: orchestrator
contingent-artifacts:
  - conjecture/multimodal-lexical-grounding-divergence
---

# Decision: the multimodal axis's panel and its privileged grounding theory

## Why this exists (direction-setting — surfaced, not self-resolved)

This session opened the project's third scope axis — **multimodal / physical-AI
meaning** (alongside grammatical and lexical) — at Tom's headline steer. Most of the
session's un-gated prep (the base-layer literature, the conjecture, the anchor and
panel-capability scouting) was done under the standing delegation. But the steer was
explicit that *a new modality + a new model family + a new anchor class* is exactly the
kind of scope expansion whose **value-laden, direction-setting** choices should be
surfaced to Tom rather than auto-resolved — "especially the choice of which multimodal
model panel and which grounding theory to privilege." This page surfaces those two.
Neither is blocking: the un-gated prep (concepts, conjecture, feasibility, anchor
scouting) proceeded; this gate governs which way the *first multimodal probe* is pointed.

## Q1 — Which multimodal model panel?

**Feasibility fact (un-gated, settled):** the existing three-lab decorrelated panel is
already image-capable — `anthropic/claude-sonnet-4.6`, `openai/gpt-5.4-mini`,
`google/gemini-3.5-flash` all accept image input (verified 2026-05-30 against the
OpenRouter `/models` catalog; gemini also accepts audio+video). See
[`experiments/notes/multimodal-panel-feasibility.md`](../../../experiments/notes/multimodal-panel-feasibility.md).
So unlike the AANN logprob blocker, there is **no capability gap** forcing a swap. The
open question is a *design* choice, not a capability one:

- **A (provisional default) — keep the existing 3-family panel, image only.** Preserves
  family decorrelation (charter §6) across the text-vs-VLM contrast: the *same* three
  model families, with the image toggled on/off, is the cleanest way to isolate "does
  grounding change meaning behaviour" from "does this model differ." Audio/video stay
  out of the headline (only gemini carries them → not decorrelated). Cheapest, most
  comparable to the existing text corpus.
- **B — add or swap in a VLM-specialist family** (e.g. a dedicated open vision-language
  model) for breadth, accepting that it widens the family set beyond the text panel and
  weakens the text↔multimodal within-family comparison.
- **C — add a single audio/video arm via gemini** for an early "beyond image" probe,
  explicitly single-model / not-decorrelated (lower evidential weight, flagged as such).

## Q2 — Which grounding theory does the axis privilege?

The base layer this session catalogs three framings that bear on multimodal meaning, and
a finding's interpretation depends on which one frames it:

- **Harnad 1990 (symbol grounding).** Meaning requires symbols connected to sensorimotor
  categories; the sharpest "form alone is not enough" ancestor. Privileging it frames the
  axis as *testing whether image grounding repairs a symbol-grounding deficit*.
- **Barsalou 1999 (perceptual symbol systems / embodied simulation).** Concepts are modal
  perceptual simulations. Privileging it frames the axis around *perceptual* sense
  structure (the `grounded.perceptual` tag) and graded perceptual similarity.
- **Lyre 2024 (grounding-as-gradual, 3-dimensional).** The project's existing working
  stance ([`concept/grounding`](../../base/concepts/grounding.md)); already adopted for the text axis. Privileging it keeps
  the multimodal axis continuous with the rest of the repo: *image input adds degrees of
  `grounded.perceptual`*, measured, not a presence/absence verdict.

- **A (provisional default) — Lyre's gradual framing, extended with `grounded.perceptual`.**
  It is already the repo's adopted stance, it is the only one that lets *degrees-of-
  grounding* findings be stated, and it makes the multimodal axis continuous with the
  text lexical↔grammatical continuum (the integration goal). Harnad + Barsalou are
  carried as the *conceptual ancestors / sharper foils*, cited but not the headline
  yardstick. (Caveat already on [`concept/grounding`](../../base/concepts/grounding.md): Lyre is a non-peer-reviewed preprint
  whose 3-D typology is his own framing, not consensus — cite with attribution.)

## Provisional defaults

**Q1 → A** (existing 3-family panel, image first) and **Q2 → A** (Lyre gradual framing +
`grounded.perceptual`, Harnad/Barsalou as foils). Both are the choices the un-gated prep
already assumed, so a "defaults stand" keeps everything as built; a different call
re-points the first multimodal probe. Tom: a one-liner per question is enough. **Not
blocking** — the conjecture and base layer stand either way; this governs the first
probe's panel + interpretive frame.
