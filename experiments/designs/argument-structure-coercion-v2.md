---
type: design
id: argument-structure-coercion-v2
title: argument-structure coercion probe v2 — escaping the v1 ceiling on the two "add-direction" positives (caused-motion + way), with conflicting-cue / coercion-resisting / graded-difficulty arms, and a de-confounding test of the add/cancel asymmetry
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: provisional
anchor: pending
contingent-on: []
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: operationalizes
    target: conjecture/way-construction
  - rel: operationalizes
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v2 — argument-structure coercion, harder (caused-motion + way)

**Why a v2.** Two of the project's own-design argument-structure probes returned *ceiling* positives in the same "add-direction" — the construction **adds** a construction-contributed entailment onto a verb that does not lexicalize it:

- [`result/caused-motion-minimal-pair-divergence-v1`](../../wiki/findings/results/caused-motion-minimal-pair-divergence-v1.md) — caused-motion adds a causation-of-motion entailment (*Maria sneezed the napkin off the table* ⊨ the napkin moved and her sneezing caused it); panel at **ceiling** (90–100%, gap 70–100 pp, 3/3 models).
- [`result/way-construction-traversal-v1`](../../wiki/findings/results/way-construction-traversal-v1.md) — the way-construction adds a self-motion / path-traversal entailment onto non-motion verbs (*Mia whistled her way down the hall* ⊨ Mia moved down the hall); panel **above the ratified bar, at/near ceiling** (77.8–100%, gap 77.7–100 pp, 3/3 models).

Both results carry the same lead caveat, stated verbatim in each page: **ceiling on relatively easy controls is weak evidence for any strong "deep processing" reading.** A saturated task cannot tell apart two hypotheses that v1 leaves wide open:

- (H-deep) the decoder genuinely **computes the construction's contributed inference** — given the form, it derives the added entailment and would withhold it when a resolving cue blocks it; versus
- (H-default) the decoder **defaults to "yes" on a well-formed coercion** — it has learned that this surface frame answers the path/causation question affirmatively, without computing anything that a conflicting cue could override.

On the v1 instruments these two predict the *same* near-ceiling affirm rate. **v2's job is to find the breaking point and, in doing so, to test whether the project's tentative "add easy / cancel hard" asymmetry survives off ceiling** (see [`theory/constructional-meaning-in-llms`](../../wiki/findings/theory/constructional-meaning-in-llms.md), which now carries that asymmetry as a *tentative* generalization — and which explicitly flags that all three add-direction positives are "ceiling / near-ceiling results on relatively easy controls").

This page is a **design**. It does **not** run here. The operationalization gate below is now **ratified** (2026-05-29); what remains before a run is the build+freeze of the item set.

## 1. Gate: the difficulty operationalization is RATIFIED (decision resolved 2026-05-29)

This v2 was gated on `cc-v2-difficulty-operationalization` — the difficulty-operationalization decision ([`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md)). **Tom ratified it 2026-05-29: UNIFY + adopt the provisional default.** The decision's scope is now broadened from CC-only to govern all off-ceiling argument-structure v2 designs (CC + caused-motion + way + the companion harder-conative), and its provisional default is adopted as the **fixed** operationalization. So the four choices below are no longer open — they are **settled, and frozen before any probe**:

1. **Difficulty axes** (§3 below): conflicting-cue (primary) + multi-step/coercion-resisting + near-miss controls + a graded ladder (embedded-CC deferred to v3).
2. **Conflicting-cue reading rule**: report the follow-construction-against-the-cue rate; "≥70% in ≥2/3 models = robust, ~chance/cue-following = informative partial-null" (report-the-rate, not a manufactured pass bar).
3. **Degradation-shape criterion**: monotone with slope < a fixed pp-drop-per-difficulty-step = graceful, else brittle cliff; the slope threshold is frozen *with* the item set.
4. **Human-anchor scope**: harder arms run internal-contrast-only with the human clause "pending" (§5); queue a human-rated harder anchor in `wanted.md` rather than blocking.

`contingent-on: []` — the yardstick is fixed. What remains before a run is purely the build+freeze of the item set (and `anchor: pending` stands for the hard arms, which is a data-availability matter, not an open decision). No v2 *result* is promoted to settled until the probe runs and is reviewed.

## 2. What v1 could not distinguish (per construction)

v1 for both constructions used controls that *removed* the construction (caused-motion: ctrl-loc = object stated to stay put, ctrl-sep = object moved by another cause; way: ctrl-loc = plain locative of the same scene, idiomatic = bleached *way*). Those controls cleanly rule out the surface-string and "any-motion" heuristics — but every *positive* item is a **well-formed, canonical-or-marked-but-interpretable coercion with no cue pulling against the added inference**. So v1 cannot separate H-deep from H-default. Specifically, v1 leaves open:

- Whether the added inference **survives a conflicting cue** — a later clause or world-knowledge fact that *resists* the coerced entailment (v1's controls were absent-construction, never anti-cued *within* the construction).
- Whether it survives **coercion-resisting verbs** — verbs that strongly resist the argument-structure coercion (v1's verbs were chosen to host the coercion, even the "atypical"/"anti-motion" arms).
- Whether the ceiling reflects **graceful, stressable computation** (monotone decline as difficulty rises) or a **brittle template default** (flat-at-ceiling then a cliff).
- Whether the ~ceiling affirm rate is the construction-contributed inference or a learned "this frame → yes" response that a resolving context should be able to cancel.

## 3. Harder manipulations (each isolates a v1 blind spot)

For each manipulation, **1–2 illustrative item sketches per construction** are given. These are **ILLUSTRATIVE drafts, NOT frozen stimuli** — the frozen `items.csv` is built and hashed by `build_items.py` only at build time, against the now-ratified difficulty operationalization (the canonical retuning-trap guard: the difficulty measures were fixed by the decision *before* this build step, since building difficulty after seeing v1's ceiling is exactly the §8 failure mode). Each sketch is written so that a model genuinely *computing* the added inference and a model *defaulting* to "yes" make **different** predictions.

### (a) Conflicting-cue items — the key manipulation

A later clause (or a hard world-knowledge fact) **resists** the coerced inference, forcing a genuine choice between the construction's contributed entailment and the cue. Note these items are genuinely **harder for humans too**: when a coercion frame collides with a resolving cue, the "correct" reading is contestable — which is why the human-anchor clause is pending (§5) and the indicator is **report-the-rate**, not pass/fail.

- **Caused-motion (object immovable / bolted down).** "*Maria sneezed the bolted-down statue off its pedestal.*" / "*Tom coughed the anvil across the floor, though it was far too heavy to move.*" The construction contributes "X caused the object to move"; the cue (bolted down / far too heavy) makes that physically resisted. H-deep should register the tension (lower/withheld affirm, or CANT_TELL); H-default affirms regardless. A milder graded version states the resistance only *after*: "*Maria sneezed the napkin off the table. The napkin, however, never left the table.*"
- **Way (goal reached without the subject moving / subject stated to stay put).** "*Felix waited his way to the front of the queue without ever leaving his seat.*" / "*Mia whistled her way down the hall, though she never moved from the doorway.*" The construction contributes self-motion/traversal; the cue denies displacement. H-deep registers the contradiction; H-default affirms traversal anyway. (Builds directly on the way result's flagged follow-up: "verbs that *contradict* motion in a fully resolved context.")

### (b) Coercion-resisting verbs

Verbs that **strongly resist** the argument-structure coercion, so the frame is marked-to-unacceptable. The diagnostic: does the model still mechanically affirm the added inference (H-default: surface frame → yes) or does it flag the resistance (H-deep / a graceful "this is anomalous")?

- **Caused-motion** — verbs whose semantics resist transitive causation-of-motion: stative/perception/cognition verbs ("*Maria knew the napkin off the table*", "*Tom believed the cup across the room*"). These are far past the v1 "atypical" arm (which kept genuinely coercible verbs).
- **Way** — verbs whose semantics resist self-motion even with a spatial path-PP, beyond the v1 anti-motion arm: pure stative/cognition ("*Felix knew his way to the answer*" is idiomatic-abstract, not spatial; the spatial stress is "*Felix slept his way down the corridor*" where displacement during the activity is anomalous).

### (c) Graded difficulty ladder

A **monotone series per construction**, canonical → marked → near-ungrammatical, with an a-priori difficulty score frozen with the item set. Reporting the affirm rate as a function of difficulty makes the **shape** the result: graceful (monotone, shallow slope) ⇒ the model is computing something stressable; brittle (flat-at-ceiling then cliff) ⇒ a template default. Example rungs:

- **Caused-motion:** canonical inanimate-propulsion (*sneezed the napkin off*) → animate self-mover (*laughed the toddler out of the room*) → coercion-resisting verb (*knew the napkin off*) → conflicting-cue (*sneezed the bolted-down statue off*).
- **Way:** canonical manner host (*whistled her way down the hall*) → anti-motion posture (*waited his way up the queue*) → coercion-resisting verb (*slept his way down the corridor*) → conflicting-cue (*whistled her way down the hall, though she never moved*).

### (d) Near-miss form controls (tighten the construction floor)

Controls **closer** to the construction than v1's absent-construction controls, to test whether the panel keys on the precise argument-structure form or on a looser shape:

- **Caused-motion** — the same verb + object + path-PP but in a **resultative-without-motion** or coordinated frame that does not assert caused motion ("*Maria sneezed, and the napkin was off the table*" — sequence, not construction-licensed causation).
- **Way** — a **bare directional** that is ungrammatical without the construction (*\*Mia whistled down the hall*) presented as a control, and a *POSS-way*-without-spatial-path near-miss, to bound the "is it just the *way* string?" worry the v1 result already flagged in its Limits.

## 4. Indicator and thresholds — OPERATIONALIZATION GATE (charter §8)

**No pass/fail thresholds are pre-committed in this design.** The v1 confirm bars (way ≥70% / gap ≥30 pp; caused-motion cm ≥70% / gap ≥30 pp) were calibrated to a near-ceiling regime and are **uninformative** once v2 is built to push off ceiling. Choosing v2's difficulty axes, conflicting-cue bar, degradation-shape criterion, or human-anchor scope **after** seeing v1's ceiling is the **canonical retuning trap** (charter §8; [`PROTOCOL.md`](../../PROTOCOL.md) §8-failure-modes: "Quietly tuning the operationalization until a null becomes positive … that is an operationalization gate. Queue it.").

Therefore all four are **fixed by the ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) decision (2026-05-29) and frozen with the item set before any probe.** The framing is **report-the-rate**, not a manufactured pass bar:

- **Conflicting-cue follow-construction rate** — the fraction following the *constructional* added inference against the resolving cue. Reported per construction, per model, per instrument. The honest expectation is that this is where the panel finally drops below ceiling; a near-chance or cue-following pattern is the **informative partial-null** (charter §2.6 / §6: write the null first-class), not a failure to be tuned away.
- **Coercion-resistance behavior** — affirm rate on coercion-resisting verbs vs. canonical hosts; the *drop* is the quantity, with a model that flags anomaly (rather than mechanically affirming) read as evidence against H-default.
- **Degradation-shape** — affirm rate as a function of the frozen difficulty score; the pre-committed operational definition of "graceful (monotone, shallow slope)" vs. "brittle cliff" (a fixed pp-drop-per-difficulty-step) is set with the item set, not after.
- **Instrument** — keep **both** NLI (0/1/2) + forced-choice (YES/NO/CANT_TELL), as v1 ratified; instrument-fragility is itself a first-class datum (the conative showed gpt-5.4-mini carries an inference under FC and loses it under NLI). No scored free-generation metric is added (it would be an un-anchored indicator); a short free-text justification arm may run only as a **qualitative side-channel**.

The provisional reading rule (in force only once ratified, mirroring the cc-v2 default): conflicting-cue items reported as a rate with "follows-construction vs. follows-cue vs. CANT_TELL" three-way; degradation read as graceful/brittle against the frozen slope threshold; the human clause pending. **A cliff, or a cue-following pattern, would qualify the v1 ceilings as task-easiness rather than robust constructional computation — and that null is the informative outcome, not a result to be retuned around.**

## 5. The asymmetry test — what v2 actually de-confounds

The project currently carries a **tentative** generalization (see [`theory/constructional-meaning-in-llms`](../../wiki/findings/theory/constructional-meaning-in-llms.md)): current decoders more readily **license** a construction's *added* inference (caused-motion, way — at/near ceiling) than **suppress** a *lexically-default* one (the conative's completed-contact — harder, instrument-fragile; gpt-5.4-mini failed it under NLI). See [`result/conative-minimal-pair-divergence-v1`](../../wiki/findings/results/conative-minimal-pair-divergence-v1.md).

**The asymmetry is currently confounded with ceiling.** The add-direction probes ran at ceiling; the cancel-direction probe (conative) ran off ceiling (it was the one that *discriminated*). So "add is easier than cancel" might just be "the add tasks were easier (saturated), the cancel task was harder." We cannot tell whether the asymmetry is about *direction* (add vs. cancel) or about *difficulty* (easy vs. hard instrument) — they vary together in the v1 set.

**v2 de-confounds it.** Running this off-ceiling add-direction v2 (conflicting-cue + coercion-resisting caused-motion/way) **alongside** an off-ceiling **cancel-direction** probe (a harder conative — e.g. conflicting-cue conative where a later clause asserts contact *did* occur, or coercion-resisting non-alternating verbs) puts both directions at *comparable* difficulty. Then:

- If **add stays robust off ceiling while cancel degrades more** → the asymmetry is about *direction* (a genuine "license-easier-than-suppress" property), and survives the de-confounding. This would *strengthen* the theory's tentative generalization.
- If **both degrade similarly off ceiling** → the v1 asymmetry was an artifact of ceiling/difficulty, and the generalization should be **retired or down-graded** to "the v1 add tasks were easier," not "adding is easier than cancelling." This is the first-class null.
- If **add degrades more than cancel** → the asymmetry reverses, a strong surprise worth a dedicated write-up.

This is the scientific payoff that justifies v2 beyond "harder for its own sake": only a matched off-ceiling add/cancel pair can tell whether the add/cancel asymmetry is real or a ceiling artifact. The harder-conative cancel arm is noted here as the **companion** v2 the asymmetry test requires; it is not built by this design (disjoint-writes discipline) — it is a separate design page, gated on the same (now ratified) difficulty decision.

## 6. Human anchor — honest scope (pending; internal-contrast-only)

The [`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md) CxNLI subsets that anchored v1 (caused-motion, way-manner; answer-key + ≈0.90/0.83 aggregate native baseline) **do not contain conflicting-cue or coercion-resisting items** — those are the project's own off-ceiling constructions, with no human norm in the repo. Per the cc-v2 decision's **Option-4 logic** (run harder arms as internal-contrast-only, human clause marked "pending"), this design's front-matter carries `anchor: pending`:

- The **canonical / near-miss arms** that overlap Scivetti's style retain the v1 phenomenon-level anchor (the construction is real and learnable, with the published native baseline).
- The **conflicting-cue, coercion-resisting, and graded-ladder arms have NO in-repo human baseline.** Their human-comparison clause is **"no human baseline; pending."** **Do not** state a "below/at/above human level" claim for those arms without a fetched, human-rated anchor. No human label is invented here. If v2 is pursued and a human comparison on the hard arms is wanted, queue a human-rated conflicting-cue/coercion-resisting anchor in `wanted.md` rather than fabricating one — and note these items' "correct" reading is itself contestable (a conflicting-cue coercion is a genuinely hard judgment for humans), which is *why* the rate is reported rather than scored against a manufactured gold.

This `anchor: pending` + the gating `contingent-on: cc-v2-difficulty-operationalization` entry together satisfy the anchor-discipline rule for an empirical design with no settled human norm on its load-bearing arms.

## 7. Harness and budget — reuses v1 verbatim

v2 reuses the v1 harness with no new machinery:

- **`build_items.py` → freeze (`items.csv` + sha256) → `probe.py` (NLI + forced-choice) → `analyze.py`**, exactly the [`experiments/runs/2026-05-29-way-construction-probe-v1/`](../../experiments/runs/2026-05-29-way-construction-probe-v1/README.md) build→freeze→probe pipeline (temperature 0; logprob-free greedy-parse instrument; v1 confirmed 0 NA across all calls).
- **Panel** unchanged ([`config/models.md`](../../config/models.md)): claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash, as subjects.
- **Run layout** mirrors v1 under `experiments/runs/<date>-argument-structure-coercion-probe-v2/`.

**Back-of-envelope pre-flight cost.** The v1 add-direction probes cost **$0.044** (caused-motion, 180 calls) and **$0.072** (way, 360 calls). A v2 of comparable size (the new arms × 2 constructions × 2 instruments × 3 models, on the order of ~120–200 items) is expected to land in the same **~$0.05–0.15** range — well under the $5 single-run flag in [`config/budget.md`](../../config/budget.md). Pre-flight per the budget page before running. The difficulty decision is **ratified**; what gates a run now is only the build+freeze of the item set (charter §8; PROTOCOL §5).

## 8. What v2 does not do

- Does not revisit v1's settled contrasts (the absent-construction controls; the causal-attribution ctrl-sep; the idiomatic over-generalization guard) — those passed; v2 only adds harder, anti-cued layers.
- Does not introduce a scored free-generation metric (no un-anchored indicator).
- Does not pre-commit any pass/fail threshold (§4) — the difficulty axes, conflicting-cue bar, degradation-shape criterion, and human-anchor scope are all fixed by the ratified decision and frozen with the item set before the run.
- Does not state any human-level claim on the conflicting-cue / coercion-resisting arms (§6).
- Does not build the companion harder-conative cancel arm itself (§5) — that is a separate design, same gate.

## 9. Handoff hooks

1. **DONE 2026-05-29** — Tom ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md): UNIFY (covers CC + caused-motion + way + the companion harder conative) + adopt the provisional default. The difficulty yardstick is fixed.
2. After ratification: build + freeze a v2 `items.csv` (conflicting-cue, coercion-resisting, graded ladder, near-miss controls, difficulty score) via `build_items.py` **before** any probe call.
3. Author the companion harder-conative cancel-direction design so the add/cancel asymmetry test (§5) can run as a matched off-ceiling pair.
4. If a human comparison on the hard arms is wanted, queue a human-rated conflicting-cue/coercion-resisting anchor in `wanted.md` first; never invent one.
5. Mirror the v1 run structure under `experiments/runs/<date>-argument-structure-coercion-probe-v2/`.
