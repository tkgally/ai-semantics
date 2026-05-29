---
id: conative-anchor
title: Which human-anchored resource should ground the conative alternation probe?
status: open
opened: 2026-05-28
opened-by: subagent
contingent-artifacts:
  - conjecture/conative-construction
---

# Decision: conative alternation anchor

## Question

The conative conjecture ([`wiki/findings/conjectures/conative-construction.md`](../../findings/conjectures/conative-construction.md)) needs a human anchor — ideally an item-level acceptability- or entailment-rated stimulus set for the English conative alternation (*She kicked at the ball* vs. *She kicked the ball*) — to compare against panel-model behavior. No such resource is currently in-repo. We need to decide which human-anchored resource grounds the probe, and what to do if no item-rated conative set is publicly available.

The conjecture's discriminating manipulation holds the **verb constant** and varies only the construction (direct object vs. *at*-oblique), testing whether the construction cancels the completed-contact entailment. Prediction 2 additionally leans on **verb-class membership**: only Levin conative-class verbs should show the effect. The anchor must therefore support at least one of: (a) item-level human judgments of the completion/contact entailment or acceptability, or (b) certification of which verbs lexically enter the conative alternation.

## Options

### A. A rated conative / telicity-completion stimulus set, if one exists (preferred if confirmable)

- **What would qualify:** a published stimulus set giving item-level human acceptability or entailment ratings for conative vs. transitive sentences, ideally crossing verb class with the completed-contact inference, or a psycholinguistic norming study on telicity/affectedness that includes the conative as a condition.
- **Status:** not yet confirmed to exist in inspectable, public form. Levin (1993) gives the canonical descriptive verb-class inventory but **no item-level human ratings**.
- **Action if pursued:** a future run searches for a rated set and, if found and public, catalogs it as a `resource` page with `status: external-only` until mirrored.

### B. Levin / VerbNet verb-class membership as a partial anchor (provisional default)

- **What:** use Levin (1993) "Conative Alternation" class membership and/or **VerbNet** class structure to ground the *verb-side* premise: which verbs lexically participate in the conative and which do not.
- **What it grounds:** Prediction 2's premise — that the effect should appear for conative-class verbs (*kick*, *hit*, *slash*, *bite*) and be absent for non-conative verbs (*touch*, *break*). This certifies the verb-class contrast empirically.
- **What it does not give:** human acceptability or entailment ratings on the conative sentences themselves. The completion-inference gradient must then come from the model's own contrast, with Levin/VerbNet only certifying class membership.
- **Why provisional default:** Levin's class list and VerbNet are well-documented, public, and directly certify the load-bearing verb-class premise. It is a weaker anchor than (A) — it does not provide a gradient on the entailment itself — but it is a real, inspectable resource, enough to run a first-pass probe without inventing a resource.

### C. Defer and queue a wanted-resource request

- If neither a rated conative set (A) nor the Levin/VerbNet framing (B) is judged sufficient, hold the conjecture at `proposed` and add a request to [`wiki/base/wanted.md`](../../base/wanted.md) for an item-rated conative/telicity stimulus set. Per the project's **no-human-subjects** rule, this means *existing* released ratings only — not new collection.

## Provisional default (in force until Tom ratifies)

**Option B**: anchor the *verb-class premise* on Levin (1993) / VerbNet conative-class membership, certifying that the chosen verbs do (and the controls do not) enter the conative, while a future run searches for an Option-A rated set. The conjecture carries `anchor: pending` until either (A) lands or Tom ratifies B as sufficient.

Rationale: (i) the conjecture's Prediction 2 turns precisely on verb-class membership, which a verb-lexicon resource certifies directly; (ii) Levin/VerbNet are public and inspectable now, unlike any presumed rated conative set; (iii) it avoids fabricating a human-rated resource that may not exist. Caveat: Option B alone does **not** anchor the completion-entailment gradient (Prediction 1), so a `result` built on B can be promoted no further than `weak` on that prediction until an Option-A gradient anchor lands — consistent with the promotion logic in [`open-question/constructional-vs-frequency-confound`](../../findings/open-questions/constructional-vs-frequency-confound.md).

## What would change the default

- If a public, item-rated conative or telicity-completion stimulus set is found and inspected, promote to Option A (it gives the gradient anchor that B cannot).
- If Levin/VerbNet turn out not to cleanly separate the chosen verbs by conative-class membership, the verb-class premise weakens and we fall back to Option C plus a wanted-resource request.

## Notes for the resolver

Tom: a one-line ratification is enough — "B stands", "search for A first", or "name a specific rated set". If you know of an existing rated conative or telicity stimulus set, naming the paper precisely lets the resource page be created directly. Reminder: no new human-subject collection — existing released ratings only.
