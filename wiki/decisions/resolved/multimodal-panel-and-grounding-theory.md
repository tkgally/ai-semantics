---
id: multimodal-panel-and-grounding-theory
title: For the new multimodal axis — which model panel, and which grounding theory to privilege?
status: resolved
opened: 2026-05-30
opened-by: orchestrator
resolved: 2026-05-31
resolved-by: tom
resolution: "Q1=A, Q2=A, Q3=B (GO)"
contingent-artifacts:
  - conjecture/multimodal-lexical-grounding-divergence
  - result/lexical-perceptual-grounding-moderation-v1
---

## RESOLUTION (2026-05-31, Tom)

Tom's ruling this round (verbatim intent): "IMAGE EXPERIMENT — APPROVED. … Treat decision
multimodal-panel-and-grounding-theory as: **Q3 → B is GO**; keep the existing image-capable
3-family panel (**Q1 default A**) and the Lyre gradual-grounding framing (**Q2 default A**)
as working defaults unless you find a principled reason to surface a change."

- **Q1 → A:** keep the existing 3-family image-capable panel (`claude-sonnet-4.6` /
  `gpt-5.4-mini` / `gemini-3.5-flash`), image toggled on/off within-family.
- **Q2 → A:** Lyre gradual-grounding framing + `grounded.perceptual`; Harnad/Barsalou as foils.
- **Q3 → B (GO):** **open the genuine image-input probe** (predictions 2–3 of
  [`conjecture/multimodal-lexical-grounding-divergence`](../../findings/conjectures/multimodal-lexical-grounding-divergence.md)).
  Q3-A (the $0 Lancaster text-side moderator) was already done last session → a null
  ([`result/lexical-perceptual-grounding-moderation-v1`](../../findings/results/lexical-perceptual-grounding-moderation-v1.md));
  that null lowered the prior but did not settle the image bet, so the image probe is GO.

**Consequence (applied this round):** the prediction-1 result has its
`contingent-on: multimodal-panel-and-grounding-theory` removed (it stands on its Lancaster +
DWUG anchors). The conjecture is no longer contingent on *this* decision; the **image
probe's human-anchor choice** (WiC-binary-keyed image set vs. a genuinely-multimodal
alternative) is a *new, narrower* surfaced question carried by
[`decisions/open/multimodal-image-anchor`](../open/multimodal-image-anchor.md) — opened this
round, proceeding under Tom's standing delegation with the choice surfaced, not fabricated.
The image probe design is [`design/multimodal-grounding-image-v1`](../../../experiments/designs/multimodal-grounding-image-v1.md).

---

## (original surfacing, for the record)

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

## Q3 — Which anchor class does the first multimodal unit privilege?

The anchor scouting ([`base/resources/multimodal-anchor-scouting.md`](../../base/resources/multimodal-anchor-scouting.md))
surfaced two structurally different first units, which differ in cost and in how much
they actually exercise *multimodality*:

- **A (provisional default) — Lancaster Sensorimotor Norms as a text-side grounding
  moderator on the EXISTING DWUG lexical result (\$0, no new probe).** Join the 40 DWUG EN
  lemmas to their perceptual-strength ratings (CC BY 4.0) and ask whether the established
  monotonicity ([`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md), Spearman 0.60–0.83) is *stronger for
  perceptually grounded words*. This directly **joins the lexical program to the grounded
  axis** (the integration goal) and is a read-only re-analysis in the project's proven $0
  mode — but it tests `grounded.perceptual` as a *property of words*, not via image input.
- **B — THINGS-data triplet judgments as an image-grounded perceptual anchor (new probe,
  new spend).** Compare a VLM (image input) vs a text-only model on human object-similarity
  judgments (CC0, 4.7M triplets). The genuinely *multimodal* first probe — exercises image
  input — but needs a new design + budget.
- **C — hold the multimodal axis and spend the next unit on the text lexical v3**
  (homonymy-enriched anchor) that [`result/lexical-polysemy-homonymy-v2`](../../findings/results/lexical-polysemy-homonymy-v2.md)'s null already
  points to. Keeps focus on the open lexical clause (b).

A and B are *sequenceable* (A first as the cheap bridge, B if warranted). The provisional
default is **A** because it is $0, exercises the integration goal, and reuses an already-
collected result — but whether to open the image-input probe (B) now, or hold for the
text lexical v3 (C), is the direction-setting call for Tom.

## Provisional defaults

**Q1 → A** (existing 3-family panel, image first), **Q2 → A** (Lyre gradual framing +
`grounded.perceptual`, Harnad/Barsalou as foils), **Q3 → A** (Lancaster text-side $0
moderator on the existing DWUG result as the first multimodal-adjacent unit). All three
are the choices the un-gated prep already assumed, so a "defaults stand" keeps everything
as built; a different call re-points the first multimodal unit. Tom: a one-liner per
question is enough. **Not blocking** — the conjecture and base layer stand either way;
this governs the first unit's panel, interpretive frame, and anchor class.
