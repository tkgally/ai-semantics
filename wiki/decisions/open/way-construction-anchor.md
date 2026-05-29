---
id: way-construction-anchor
title: Which human-anchored stimulus set should ground the way-construction inference probe?
status: open
opened: 2026-05-28
opened-by: lead-agent
contingent-artifacts:
  - conjecture/way-construction
  - design/way-construction-v1
---

# Decision: way-construction human anchor

## Question

The way-construction experiment design ([`experiments/designs/way-construction-v1.md`](../../../experiments/designs/way-construction-v1.md)) requires a human-anchored stimulus resource to ground the inference probe. Unlike the AANN probe, which compares model acceptability behavior against human acceptability ratings, the way-construction probe is an **inference probe** — it asks whether the model draws a path-traversal inference. The anchor therefore needs to supply human inference rates (or at minimum a stimulus list that linguistically-trained experts certify as genuine way-construction tokens with unambiguous path-traversal entailments).

No such rated dataset is currently in-repo. Goldberg (1995, ch. 9) is the canonical reference for the *way*-construction, but it is a theoretical monograph with expert-curated examples and no rating distribution. This decision gate identifies options and records the provisional default.

## Options

### Option A — Goldberg (1995) examples as seed only, anchor: pending (provisional default)

Use Goldberg's (1995, ch. 9) canonical examples and the item-generation logic in the design (verb list × path PP list) to build the stimulus set. Acknowledge there is no in-repo rated anchor for the *inference* probe itself. Mark the design `anchor: pending`. The probe still runs and produces model inference rates; the human-comparison component reports "no human norm in-repo — pending."

A placeholder resource page `wiki/base/resources/goldberg-1995-way-stimuli.md` is created at probe-prep time to document which examples are drawn from which pages of Goldberg (1995).

**Upside:** tractable now; the probe results are still interpretable (we learn the model's inference rate and the construction-vs-control gap). **Risk:** the human-comparison arm of the finding is weak (theoretical rather than empirically rated).

### Option B — corpus-derived instances annotated by Tom

Generate 50–100 *way*-construction tokens from COCA, BNC, or another English corpus, plus matched controls. Tom annotates each for path-traversal inference (yes/no, with a confidence score). This gives a human inference rate on a matched set.

**Upside:** an empirically-rated human anchor, defensible as a single-expert pilot annotation with documented limits. **Risk:** requires Tom's annotation time; corpus search is not in scope for this design session. Adds a session before the probe can run.

### Option C — published psycholinguistic data (if discoverable)

Search for existing judgment or priming data on the way-construction's path-traversal inference. Candidate sources: Boas & Sag (2012), Perek (2015 corpus study), recent CxG-probing work in the Weissweiler / Tayyar Madabushi line. None are confirmed to contain rated inference-probe data.

**Upside:** independent external anchor with potentially larger N. **Risk:** may not exist in the form needed; fetching and confirming takes a session.

## Provisional default

**Option A.** Rationale: (i) the design's primary result is the model construction-vs-control gap, which does not require a rated human norm; (ii) Goldberg's expert-curated examples are sufficient to verify that items are genuine way-construction tokens; (iii) proceeding now keeps the probe on track without waiting for annotation or literature search; (iv) if the gap result is strong, the anchor question becomes a refinement, not a blocker.

The design marks `anchor: pending` and records the limitation in the human-anchor section.

## What would change the default

- If Tom is willing to annotate 60–100 items before the probe runs, switch to Option B and update the design to add a human-rate column to the results table.
- If a published inference-rated dataset surfaces in the literature search (Option C), adopt it instead.

## Notes for the resolver

Tom: "Option A stands" is sufficient to ratify. If switching to Option B, please indicate a timeline for annotation and whether you want the item list committed for review first.
