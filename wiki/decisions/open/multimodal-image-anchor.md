---
id: multimodal-image-anchor
title: For the image probe — which human anchor keys it (WiC-binary-keyed constructed image set vs. an existing genuinely-multimodal resource)?
status: open
opened: 2026-05-31
opened-by: orchestrator
contingent-artifacts:
  - conjecture/multimodal-lexical-grounding-divergence
  - design/multimodal-grounding-image-v1
---

# Decision: the image probe's human anchor

## Why this exists (surfaced, proceeding under standing delegation)

Tom **approved** the genuine image experiment this round (decision 2; the panel/theory/anchor-class
gate [`decisions/resolved/multimodal-panel-and-grounding-theory`](../resolved/multimodal-panel-and-grounding-theory.md)
is ratified Q3=B GO). Tom **delegated the anchor choice** to the orchestrator but was explicit:
"Choose the image experiment's human anchor rigorously … (either an imperfect-but-real existing
human resource with the claim scoped accordingly, or an image-paired stimulus set keyed to an
EXISTING human sense inventory — no new human subjects); **surface the anchor choice, don't
fabricate one**." This page is that surfacing. It is **non-blocking**: the design proceeds on the
provisional default under the standing delegation; Tom can redirect a one-liner asynchronously.

## REALIZED ANCHOR (2026-05-31) — Option A-variant, surfaced

On building, **WiC's actual sentence items badly under-covered clean visually-distinct homonyms**
(bat/crane/mouse are absent as WiC nouns; most WiC noun-F items use abstract/non-prototypical senses),
which would have left the prediction-3 "visually-distinct" stratum weak. So the **realized** v1 anchor
is the *other* arm of Tom's authorization — **a constructed minimal-pair set keyed to an EXISTING human
sense inventory: Princeton WordNet** ([`resource/wordnet-sense-inventory`](../../base/resources/wordnet-sense-inventory.md),
the same inventory WiC is built from). Each item's same/different gold = same vs different WordNet noun
**synset** (verified via NLTK WordNet; synset ids in the run's `items.csv`). **Honesty note (forced by
the independent pre-run critic):** *no per-item human annotator judged these constructed pairs* — the
human-anchored part is the WordNet **sense inventory** (these are genuinely distinct vs identical
synsets); the **mapping of each constructed sentence to a synset is the author's**, weaker than WiC's
released per-item labels, and the result states this. **WiC remains the anchor for the text-only
lexical-v3** ([`design/lexical-polysemy-homonymy-v3`](../../../experiments/designs/lexical-polysemy-homonymy-v3.md)),
where its actual items suffice. Result: [`result/multimodal-grounding-image-v1`](../../findings/results/multimodal-grounding-image-v1.md).
Tom: a one-liner ("WordNet-keyed constructed set is fine" / "redo with WiC/VWSD") is enough; **not blocking**.

## The question

Which independent human anchor keys the image probe's graded-relatedness DV, and how is the image
set built — without new human subjects?

## Options

- **A (provisional default, in force) — WiC binary same/different labels + a constructed
  image-paired set keyed to them.** Use [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md)
  (CC BY-NC 4.0; binary lexicographer same/different-sense labels) as the independent human anchor;
  for a subset of WiC noun items with concrete, visually-distinct referents (incl. genuine
  homonyms: bat, crane, bank, seal, pitcher, mouse…), source one small CC0/PD image per context
  depicting that context's referent (Wikimedia Commons API, verified reachable + downscaled +
  sha256-frozen). The image is a **designed manipulation**; the human signal stays WiC's binary
  label; every claim is scoped to a **binary same/different separation** (not a graded correlation).
  This is exactly Tom's "image-paired stimulus set keyed to an existing human sense inventory," and
  it **reuses the same anchor as the text-only lexical-v3** so the two axes integrate. Governs
  [`design/multimodal-grounding-image-v1`](../../../experiments/designs/multimodal-grounding-image-v1.md).
- **B — a genuinely-multimodal existing human resource (VWSD / SemEval-2023 Task 1).** Images +
  human gold already paired. Rejected for v1 in the design because its gold is a *retrieval* answer
  key (discriminative — the bag-of-words gap the conjecture warns against), it does not slot into the
  DURel-style relatedness instrument without redesign, and its images are a license patchwork.
  Reconsider for a v2.
- **C — THINGS-data triplet judgments (CC0).** Object-concept similarity, not word-sense relatedness
  — a *related* claim, not this one; weaker fit to the lexical program's instrument.

## Provisional default

**Option A** — WiC-binary-keyed constructed image set, all claims binary-scoped, images sourced
PD/CC0 and frozen (sha256) before any model call. Proceeding under the standing delegation with the
choice surfaced here. Tom: a one-liner ("A stands" / "use B/C" / "hold") is enough; **not blocking**.
