---
id: comparative-correlative-anchor
title: Which human-anchored resource should ground the comparative-correlative inference probe?
status: resolved
resolved: 2026-05-29
resolution: "Option A — adopt the Scivetti CxNLI comparative-correlative subset as the human anchor (Scivetti bundle). De-anonymized repo inspected 2026-05-29: per-item CxN-Type labels (incl. Comparative-Correlative) + a single gold relation per item confirmed; aggregate human baseline only. Anchor only — the conjecture stays untested. Ratified by Tom."
opened: 2026-05-29
opened-by: orchestrator
contingent-artifacts:
  - conjecture/comparative-correlative-construction
---

# Decision: comparative-correlative construction anchor

## Question

The comparative-correlative conjecture ([`conjecture/comparative-correlative-construction`](../../findings/conjectures/comparative-correlative-construction.md)) needs a human anchor — ideally an item-level human-rated **inference** dataset for the English comparative correlative (CC), so the panel's covariation-inference behavior can be compared against human performance. The conjecture's discriminating manipulations are (a) CC vs. non-CC minimal-pair controls, (b) positive- vs. inverse-CC direction sensitivity, and (c) generalization to atypical scale pairs. The anchor must support at least an aggregate human baseline on CC inference.

Two in-repo sources bear on the CC but neither is a human-rated `resource`: [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) supplies an encoder-PLM baseline (form recognised, meaning at chance), not a human norm; and the CC subset of the Scivetti dataset is a candidate but uninspected.

## Options

### A. Scivetti et al. 2025 CxNLI comparative-correlative subset (provisional default)

- **What:** the CC items within [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) — human-annotated NLI triples for the comparative correlative (one of its 8 constructions), with a native-speaker accuracy baseline (≈0.90 Exp 1 / ≈0.83 Exp 2).
- **What it grounds:** a human inference baseline on CC NLI items, on the same task the panel would be run on (apples-to-apples with Scivetti's NLI framing).
- **Why provisional default:** it is the only in-repo candidate that pairs CC inference items with a human baseline, and the NLI framing matches a clean panel probe.
- **Limits:** the dataset is `external-only` — the release repo was not reachable when catalogued, so the CC subset's per-item structure, count, and whether per-item human labels (vs. aggregate accuracy) are released are **unverified**; small N per construction; the baseline verified so far is aggregate, not a per-item gradient; and the Exp-2 0.83 figure is phrased as IAA (see the resource page's caveat). Adoption requires item-level inspection (see the resource page's "Pointer for next visit").

### B. Weissweiler 2022 stimulus design as a seed, human-comparison arm pending

- **What:** reuse the Weissweiler et al. 2022 CC stimulus-construction logic (CFG-generated + corpus-based CC vs. non-CC items, and their semantic-application task design) to build the probe, with no human inference norm — the human-comparison arm reports "no human norm in-repo — pending," and the model-side comparison is to the 2022 encoder-PLM baseline.
- **Upside:** tractable now; gives a direct generational comparison to the 2022 encoders. **Risk:** no human inference baseline, so the conjecture's "below human level" clause cannot be evaluated; only the encoder-vs-decoder narrowing can.

### C. Defer and queue a wanted-resource request

- If neither (A) nor (B) is judged sufficient, hold the conjecture at `proposed` and add a [`wiki/base/wanted.md`](../../base/wanted.md) request for a human-rated CC inference/judgement dataset (existing released ratings only — no new human-subject collection, per charter §8).

## Provisional default (in force until Tom ratifies)

**Option A**, contingent on item-level inspection of the Scivetti CC subset (which has not happened — the repo was unreachable this run). Until inspected and ratified, the conjecture carries `anchor: pending`; if inspection shows the CC subset does not release usable per-item data, fall back to **Option B** (Weissweiler-2022 seed, human arm pending) plus a wanted request.

Rationale: (i) the Scivetti CC subset is the only in-repo candidate pairing CC inference with a human baseline; (ii) it shares the NLI framing a clean panel probe would use; (iii) it avoids inventing a human-rated resource. The dependency on inspection is real and is shared with the sibling decisions (`caused-motion-anchor`, `conative-anchor`, `way-construction-anchor`), for which the same dataset was surfaced as candidate Option D.

## What would change the default

- If item-level inspection shows the Scivetti CC subset releases per-item human labels, Option A is straightforwardly adoptable (pending Tom).
- If it does not, fall back to Option B and queue a wanted request for a human-rated CC dataset.

## Notes for the resolver

Tom: a one-line ratification is enough — "A pending inspection", "use B for now", or name a specific CC dataset. This decision is coupled to the broader item-level-inspection gate on the Scivetti repo noted on the resource page; ratifying the Scivetti dataset as an anchor for the four CxG conjectures (caused-motion, conative, way, comparative-correlative) could be done in one stroke if you prefer.
