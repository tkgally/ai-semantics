---
id: caused-motion-anchor
title: Which human-anchored resource should ground the caused-motion construction probe?
status: resolved
resolved: 2026-05-29
resolution: "Adopt the Scivetti CxNLI dataset as the human anchor (Scivetti bundle, with conative / way / comparative-correlative). De-anonymized repo (github.com/melissatorgbi/beyond-memorization) inspected 2026-05-29: per-item CxN-Type labels + a single gold relation per item confirmed; aggregate human baseline only (no multi-rater gradient). Anchor only — the conjecture stays untested. Ratified by Tom."
opened: 2026-05-28
opened-by: subagent
contingent-artifacts:
  - conjecture/caused-motion-construction
---

# Decision: caused-motion construction anchor

## Question

The caused-motion conjecture ([`wiki/findings/conjectures/caused-motion-construction.md`](../../findings/conjectures/caused-motion-construction.md)) needs a human anchor — an item-level acceptability- or entailment-rated stimulus set for the English caused-motion construction (`Subj V Obj Obl(path/goal)`, *She sneezed the napkin off the table*) — to compare against panel-model behavior. No such resource is currently in-repo. We need to decide which human-anchored resource grounds the probe, and what to do if no item-rated caused-motion set is publicly available.

Critically, the conjecture's discriminating manipulation is the use of **non-motion, non-transitive verbs** (*sneeze*, *laugh*, *yawn*) in a frame that requires an object and an oblique path. The anchor must support, at minimum, distinguishing verbs that lexically license `V NP PP` from verbs that do not.

## Options

### A. A rated caused-motion acceptability set, if one exists (preferred if confirmable)

- **What would qualify:** a published stimulus set giving item-level human acceptability or naturalness ratings for caused-motion sentences, ideally crossing verb type (motion / contact / sound-emission / non-motion) with path/goal PPs.
- **Status:** not yet confirmed to exist in inspectable, public form. Goldberg (1995, ch. 7) provides the canonical descriptive inventory but **no item-level human ratings**; it grounds the construction's existence and example set, not a gradient anchor.
- **Action if pursued:** a future run searches for a rated caused-motion set (psycholinguistic norming, or an argument-structure-construction corpus study with caused-motion as a condition) and, if found and public, catalogs it as a `resource` page with `status: external-only` until mirrored.

### B. Verb-frame resource as a partial anchor (provisional default)

- **What:** use an existing verb-lexicon resource — **VerbNet** and/or **PropBank** — to ground the *verb-side* contrast rather than the construction's acceptability. These document, per verb, the licensed syntactic frames and argument structure.
- **What it grounds:** the claim that *sneeze*, *laugh*, *yawn* do **not** lexically license a direct object + oblique path. That is exactly the premise the conjecture leans on: if the verb's frame inventory excludes `NP PP`, then a caused-motion entailment from such a sentence cannot be projected from the verb. This anchors the *coercion* premise empirically.
- **What it does not give:** human acceptability ratings on the caused-motion sentences themselves. The construction's gradient must then come from the model's own contrast, with VerbNet/PropBank only certifying the non-licensing premise.
- **Why provisional default:** VerbNet/PropBank are well-documented, public, and directly certify the load-bearing premise (verb does not license the frame). It is a weaker anchor than (A) but a real, inspectable one — enough to run a first-pass probe without inventing a resource.

### C. Defer and queue a wanted-resource request

- If neither a rated caused-motion set (A) nor the VerbNet/PropBank framing (B) is judged sufficient, hold the conjecture at `proposed` and add a request to [`wiki/base/wanted.md`](../../base/wanted.md) for an item-rated caused-motion stimulus set (or for Goldberg-derived stimuli with fresh acceptability collection — noting the project's **no-human-subjects** rule, this means *existing* released ratings only, not new collection).

### D. Scivetti et al. 2025 CxNLI dataset as an inference-rate anchor (surfaced 2026-05-29 — candidate, not yet adopted)

- **What:** the public dataset catalogued at [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md). `Caused-Motion` is one of its 8 constructions, with human-annotated NLI triples and a native-speaker accuracy baseline (≈0.90).
- **Why it bears on this decision:** unlike Option B (which only certifies the *verb-side non-licensing premise* and leaves the construction's gradient to the model), Scivetti supplies **human-licensed inference labels on caused-motion sentences themselves** — the inference-licensing level the conjecture actually targets — plus an aggregate human baseline for direct LLM-vs-human comparison on the same items. Its verified caused-motion example item (premise *"I threw the stone across the river."*, hypothesis *"I caused the stone to move across the river by throwing it."*, label Entailment) is exactly the caused-motion entailment the conjecture probes.
- **Limits to weigh:** small N per construction (≈435 triples / 8 constructions); the human bearing verified so far is an *aggregate* accuracy, not per-item graded ratings; the data repository was not inspectable this run (whether per-item human labels are released is unconfirmed); the items use ordinary motion-licensing verbs (e.g. *throw*), so whether the set includes the conjecture's discriminating **non-motion** verbs (*sneeze*, *laugh*) must be confirmed by inspecting the data.
- **Status:** a candidate only — surfaced for Tom's consideration, not adopted. Adoption needs (a) Tom's ratification and (b) item-level inspection of the repo (see the resource page's "Pointer for next visit").

## Provisional default (in force until Tom ratifies)

**Option B** remains the provisional default (a new candidate, Option D, was surfaced 2026-05-29 but is not adopted): anchor the *non-licensing premise* on VerbNet/PropBank verb-frame inventories, certifying that the chosen non-motion verbs do not lexically license `V NP PP`, while a future run searches for an Option-A rated set. The conjecture carries `anchor: pending` until either (A) lands or Tom ratifies B as sufficient.

Rationale: (i) the conjecture's force comes precisely from verbs that *cannot* project the frame, and a verb-frame resource certifies that directly; (ii) VerbNet/PropBank are public and inspectable now, unlike any presumed rated caused-motion set; (iii) it avoids fabricating a human-rated resource that may not exist.

## What would change the default

- If item-level inspection of the Scivetti repo confirms human-licensed caused-motion inference labels (Option D), that is a stronger anchor for the *inference* the conjecture targets than Option B's verb-frame premise — promote to D (or D-as-supplement-to-B).
- If a public, item-rated caused-motion acceptability set is found and inspected, promote to Option A (it gives a gradient anchor, which B cannot).
- If VerbNet/PropBank turn out not to cleanly mark the non-motion verbs as excluding `V NP PP` (e.g., they list a coerced frame), the premise weakens and we fall back to Option C plus a wanted-resource request.

## Notes for the resolver

Tom: a one-line ratification is enough — "B stands", "search for A first", or "name a specific rated set". If you know of an existing rated caused-motion stimulus set, naming the paper precisely lets the resource page be created directly. Reminder: no new human-subject collection — existing released ratings only.
