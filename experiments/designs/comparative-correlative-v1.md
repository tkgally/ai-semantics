---
type: design
id: comparative-correlative-v1
title: comparative-correlative covariation-inference probe v1 — CC vs non-CC controls, direction-flip on inverse CC, atypical-pair generalization
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
  - human-comparison
status: provisional
anchor: pending
contingent-on:
  - comparative-correlative-anchor
  - constructional-divergence-operationalization
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: operationalizes
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/formal-vs-functional-competence
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/weissweiler-2022-comparative-correlative
---

# Experiment design v1 — comparative correlative

**Status**: provisional. The human-comparison component is contingent on [`decisions/open/comparative-correlative-anchor`](../../wiki/decisions/open/comparative-correlative-anchor.md) (`anchor: pending`), and the operationalization choices (instrument, gap definition, frequency-matching) are contingent on a `constructional-divergence-operationalization` decision the orchestrator should open before any run (see §8). Nothing claiming a human-comparison finding may be promoted to settled until both are ratified. Marked provisional in exactly the way [`aann-construction-v1`](aann-construction-v1.md) and [`way-construction-v1`](way-construction-v1.md) are marked contingent on their decisions.

## 1. Construct

The English **comparative correlative** (CC) — the two-clause `the X-er …, the Y-er …` template (*the more you practice, the better you get*) — as a Construction Grammar form–meaning pairing: form = the paired-`the` two-clause template; constructional meaning = a **proportional / covariational dependency** between two scales (as the first scale changes, the second changes in a fixed direction). The covariation semantics is non-compositional — no lexical item in either clause carries the "as X, so Y" relation; the construction supplies it (see [`source/weissweiler-2022-comparative-correlative`](../../wiki/base/sources/weissweiler-2022-comparative-correlative.md)).

The construct of interest: whether a panel model **uses** the CC's covariation meaning — draws the inference that a change along the first scale entails a corresponding directional change along the second — rather than merely **recognising** the CC's form. This is the recognise-vs-use distinction Weissweiler et al. 2022 operationalised for encoder PLMs (form recognised by a syntactic probe; meaning at chance on a semantic-application task). It is a direct operationalization of the `constructional` and `inferential` meaning-senses, landing on the `functional-vs-formal` wedge ([`concept/formal-vs-functional-competence`](../../wiki/base/concepts/formal-vs-functional-competence.md)).

## 2. Indicator

(Per provisional default in the `constructional-divergence-operationalization` decision to be opened — see §8. Instrument choice is locked there *before* the probe runs.)

The construct maps to a **covariation-inference rate** with three derived contrasts, all committed and frozen before any probe call:

- **CC covariation-inference rate** — fraction of CC items on which the model gives the correct covariation answer (entailment under NLI framing / correct direction under forced-choice framing). Predicted high.
- **CC-vs-control gap (primary indicator)** — CC covariation-inference rate minus the rate on matched non-CC controls that reuse the same scalar lexical material in non-CC syntax. This is the number that isolates the *construction*, not the words, as the source of the inference. **Threshold T1: gap ≥ 30 percentage points** in ≥ 2 of 3 panel models. (Same magnitude convention as the way-construction design's construction-vs-control gap, chosen before results; if the orchestrator's operationalization decision sets a different threshold, that decision governs and this number is updated there, not retuned here.)
- **Direction-flip rate on inverse-CC items (the discriminating indicator)** — fraction of inverse-CC items (*the more …, the less …*) on which the model's covariation answer flips to the inverse direction relative to the matched positive-CC item. A model *using* the meaning tracks direction; a model only recognising the template does not reliably flip. **Threshold T2: direction-flip rate ≥ 70%** in ≥ 2 of 3 panel models.
- **Atypical-pair persistence (generalization indicator)** — CC covariation-inference rate on low-frequency / pragmatically atypical scale pairings, reported separately from the typical-pair rate. **Threshold T3: atypical-pair rate within 15 pp of typical-pair rate** (no collapse) in ≥ 2 of 3 panel models. A large drop here is the n-gram/frequency signature, not constructional use (ties to [`open-question/constructional-vs-frequency-confound`](../../wiki/findings/open-questions/constructional-vs-frequency-confound.md)).

**Logprob/answer handling.** Under the NLI framing, record the model's 3-way label (entailment / neutral / contradiction) and, where exposed, first-answer-token logprobs; under the forced-choice framing, record the chosen direction and its logprob. If a model does not expose logprobs, fall back to temperature = 0 greedy completion and parse the label/direction string (unparseable → NA, excluded from rates and reported separately; NA rate > 10% is flagged a model-level failure mode). The fallback is recorded per model in the run record and not switched after seeing first-batch outputs.

## 3. Method

A behavioral API probe over the panel ([`config/models.md`](../../config/models.md)), zero-shot, read-only.

### 3.1 Probe format — the instrument choice (operationalization gate)

Two candidate instruments, with a real trade-off that the operationalization decision must fix **before** running (charter §8):

- **(a) NLI / entailment framing (Scivetti-style).** Present premise + hypothesis, ask for entailment / neutral / contradiction. Example: premise *"The more the committee delayed, the angrier the investors grew."*, hypothesis *"If the committee delayed more, the investors grew angrier."* → entailment; an inverse-direction hypothesis on an inverse-CC item → contradiction. **Upside:** apples-to-apples with the candidate human anchor, the Scivetti CxNLI CC subset ([`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)), which is 3-way NLI with a native-speaker accuracy baseline — so the human-comparison arm can be run on the *same instrument*. **Downside:** it is a *different* instrument from Weissweiler 2022's masked/cloze **semantic-application** task, so the encoder-PLM "meaning at chance" baseline is **not directly interchangeable** with NLI accuracy.
- **(b) Forced-choice covariation-direction question.** Ask directly: *"Does increased delay go with increased anger, or decreased anger?"* (or Y/N "Does increased delay go with increased anger?"). **Upside:** closer in spirit to Weissweiler's semantic-application framing (use the meaning to answer a covariation question), and the cleanest read on the direction-flip indicator. **Downside:** not apples-to-apples with the Scivetti NLI human baseline; the human-comparison arm would then need a re-derived baseline.

**Recommendation (provisional default for the decision):** run **both** framings on a shared item set — NLI as the primary instrument for the human-comparison arm (against Scivetti), forced-choice as the primary instrument for the direction-flip indicator and as the closer analogue to Weissweiler's semantic task. Report each indicator against the instrument that grounds it, and **never** cross-compare an NLI number against the Weissweiler encoder baseline as if interchangeable (conjecture caveat; charter §8). Cost permits both (see §6). The decision page locks which instrument grounds which indicator before the run.

### 3.2 Item set

Target: **~120 base scale-pair items**, each instantiated in CC form and matched non-CC control form, run under both framings (§3.1). Order of magnitude is deliberately small — the construct is carried by the contrasts, not by N — and stays far under the budget cap (§6).

CC frames × scale pairs:

- **Scale pairs (~30)** — each a pair of gradable dimensions (delay/anger, practice/skill, altitude/cold, price/demand, distance/cost, …). Two subsets:
  - *Typical pairs* (~20): covariation is plausible but **not world-knowledge-obvious** to the point that plausibility alone gives the answer (conjecture caveat: avoid causally telegraphing verbs so the inference must come from the construction).
  - *Atypical / low-frequency pairs* (~10): pragmatically odd or unlikely-to-be-memorised pairings (the Scivetti atypical-filler lever), for the generalization arm (T3).
- **Direction conditions**: each scale pair built in a **positive-CC** (*the more …, the more …*) and an **inverse-CC** (*the more …, the less …*) variant, matched, for the direction-flip indicator (T2).
- **Matched non-CC controls**: each CC item paired with a control that **reuses the same scalar lexical material** in non-CC syntax — (i) two independent declarative clauses, and (ii) a single comparative clause — so the words are held constant and only the construction is removed. These ground the CC-vs-control gap (T1).

Full item list (scale pair, dimension words, direction, item-type {cc-positive / cc-inverse / control-two-clause / control-single-comparative}, typicality, source) is committed to `experiments/data/comparative-correlative/items.csv` **before** the probe runs, lexically frozen at that commit. Multiple probe phrasings (per framing) are pre-committed before seeing any results (conjecture caveat; charter §8).

### 3.3 Panel

Per [`config/models.md`](../../config/models.md):

- `panel.A` — `anthropic/claude-sonnet-4.6`
- `panel.B` — `openai/gpt-5.4-mini`
- `panel.C` — `google/gemini-3.5-flash` (reasoning-token mitigation per calibration caveats)

### 3.4 Probe protocol

For each panel model:

1. **Dry run** — confirm label parsing and logprob availability via a 3-item dry run (one per item-type) before any full call. If logprobs unavailable, switch to greedy-string parsing for that model; record the flip.
2. **Full run** — for each item × framing: submit the frozen prompt, record full prompt, label/direction, first-answer-token logprobs (or greedy string), latency, usage tokens.
3. **Persist** raw JSON to `experiments/data/comparative-correlative/runs/<run-date>/<panel-slot>/`.

Temperature = 0 throughout. Reasoning-token mitigation for `panel.C`: set `reasoning: {"enabled": false}` if supported, else `max_tokens` ≥ 1024. Document per-model settings in the run record; do not adjust after first-batch outputs.

### 3.5 Analysis

For each panel model: compute the CC covariation-inference rate, the CC-vs-control gap (apply T1), the inverse-CC direction-flip rate (apply T2), and the typical-vs-atypical rates (apply T3), each against the framing that grounds it (§3.1). Report all numbers for all three models in one table, with NA rates and fallback notes. Cross-model divergence is itself a result (charter §6). No item-level cherry-picking; no post-hoc threshold adjustment.

## 4. Human anchor

**Candidate anchor**: the Scivetti et al. 2025 CxNLI **comparative-correlative subset** ([`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)) — human-annotated NLI triples for the CC (one of its 8 constructions) with a native-speaker accuracy baseline (≈ 0.90 Exp 1 / ≈ 0.83 Exp 2). This is the only in-repo candidate pairing CC inference items with a human baseline, and it shares the NLI framing of instrument (a).

**`anchor: pending`.** The resource is `external-only` / uninspected: the release repo was unreachable when catalogued, so the CC subset's per-item structure, count, and whether **per-item** human labels (vs. aggregate accuracy) are released are unverified. The human-comparison arm of this design is therefore contingent on **(a)** item-level inspection of the Scivetti repo and **(b)** Tom's ratification of [`decisions/open/comparative-correlative-anchor`](../../wiki/decisions/open/comparative-correlative-anchor.md) (provisional default: Option A pending inspection; fall back to Option B — Weissweiler-2022 stimulus seed with the human arm pending — if inspection shows no usable per-item data).

**Model-side comparison (available now, no anchor ratification needed)**: the Weissweiler 2022 encoder-PLM baseline — BERT/RoBERTa/DeBERTa recognise the CC's form but score **at chance** on its meaning ([`source/weissweiler-2022-comparative-correlative`](../../wiki/base/sources/weissweiler-2022-comparative-correlative.md)). Caveat (carried from the conjecture): that baseline is a masked/cloze semantic-application result, not NLI, so it grounds the **generational narrowing** comparison only against a comparable framing — do not equate it with an NLI accuracy number. An aggregate panel-vs-encoder narrowing claim can be made without ratifying the anchor; the panel-vs-human "below human level" clause cannot, until the anchor lands.

## 5. Predictions (from [`conjecture/comparative-correlative-construction`](../../wiki/findings/conjectures/comparative-correlative-construction.md))

1. **High CC covariation-inference rate** — CC items yield a high correct-covariation rate in ≥ 2 of 3 panel models.
2. **Large CC-vs-control gap** — gap ≥ 30 pp (T1) in ≥ 2 of 3 panel models: the construction, not the shared scalar words, drives the inference.
3. **Direction flip on inverse CC** — inverse-CC items flip the covariation answer; direction-flip rate ≥ 70% (T2) in ≥ 2 of 3 panel models. The discriminating prediction: a form-only recogniser would not reliably flip.
4. **Persistence on atypical pairs** — atypical/low-frequency scale pairs hold the inference (T3) in ≥ 2 of 3 panel models, distinguishing constructional use from an n-gram effect.
5. **Narrows-but-below-human vs the two baselines** — decoder LLMs clear the encoder-PLM chance-level semantic baseline (the gap narrows from Weissweiler 2022) yet remain measurably below the Scivetti native-speaker baseline. This is the conjecture's central directional bet.

## 6. Pre-flight cost check ([`config/budget.md`](../../config/budget.md) §Pre-flight)

~120 base items × 2 control forms ≈ 240 items, × 2 framings ≈ 480 prompt evaluations per model. (Inverse/positive direction conditions are part of the item count, not an extra multiplier.) Single-token-ish answers.

| Model | Tokens in / call | Tokens out / call | Pricing (in / out per MT) | Est. cost |
|-------|-----------------:|------------------:|---------------------------|----------:|
| `panel.A` claude-sonnet-4.6 | ~120 | ~5 | $3 / $15 | ≈ $0.18 |
| `panel.B` gpt-5.4-mini | ~120 | ~5 | $0.20 / $0.60 | < $0.02 |
| `panel.C` gemini-3.5-flash | ~120 | ~5 + reasoning tokens | $0.15 / $0.60 | < $0.02 + reasoning overage |

Total: well under $1 even with the Gemini reasoning-token caveat (the visible output is short, so reasoning tokens are the main variable cost; cap `max_tokens` and accept the overhead). **No pre-flight budget escalation required** (cap is $5 single-run / $20 monthly soft).

## 7. Falsification criteria

The conjecture (re-stated): current decoder LLMs **use** the CC's proportional-covariation meaning, narrowing but not closing the 2022 form-vs-meaning dissociation.

- **Confirm (narrows-but-not-closes)**: T1, T2, T3 met in ≥ 2 of 3 models AND the panel clears the encoder-PLM chance baseline yet sits below the Scivetti human baseline. The central bet.
- **Stronger (closes)**: panel reaches human-level covariation inference including inverse and atypical items — would *refine* the conjecture's "not closing" clause toward retirement (gap is construction-/generation-specific).
- **Weak / dissociation persists**: inference tracks the surface template — positive-CC handled, inverse-CC direction-flip fails (T2 missed), or atypical fillers collapse (T3 missed). Form recognised, meaning still not used — the 2022 dissociation essentially unchanged.
- **Frequency-only explanation**: the CC-vs-control gap is present on typical pairs but vanishes on atypical pairs (T3 fails while T1 passes on typical only) — the effect is an n-gram artifact, not constructional use ([`open-question/constructional-vs-frequency-confound`](../../wiki/findings/open-questions/constructional-vs-frequency-confound.md)).
- **Falsify (of "narrows")**: panel at chance on covariation just as encoder PLMs were — no narrowing. A clean null here is a **first-class negative** (charter §2.6): the form/meaning dissociation is durable across model generations. Write it.

## 8. Operationalization gate (charter §8)

The following choices are exactly where an autonomous loop would quietly cheat by retuning after seeing a null; they must be fixed in a decision page **before** the probe runs, not after:

- **Instrument** — NLI vs forced-choice vs both (§3.1), and which instrument grounds which indicator (the NLI/Weissweiler non-interchangeability is the live risk).
- **Gap / threshold definitions** — T1 (CC-vs-control ≥ 30 pp), T2 (direction-flip ≥ 70%), T3 (atypical within 15 pp), and the "below-human" comparison rule.
- **Frequency-matching procedure** — how typical vs atypical scale pairs are selected and frozen (shared concern with [`open-question/constructional-vs-frequency-confound`](../../wiki/findings/open-questions/constructional-vs-frequency-confound.md)).

**Note to the orchestrator (a new decision needs opening).** [`open-question/constructional-divergence-probe`](../../wiki/findings/open-questions/constructional-divergence-probe.md) already names a `constructional-divergence-operationalization` decision to be opened when this design space is picked up. The orchestrator should open that decision (or a CC-specific `comparative-correlative-operationalization` decision) covering the three bullets above, with the §3.1 recommendation as the provisional default. This design is marked **provisional / contingent** on it and on `comparative-correlative-anchor`, mirroring how [`aann-construction-v1`](aann-construction-v1.md) is contingent on `aann-operationalization` and [`way-construction-v1`](way-construction-v1.md) on `way-construction-anchor`.

## 9. What this design does not do

- Does not assume the Scivetti CC subset is usable as a per-item anchor; until the repo is inspected and Tom ratifies the anchor decision, the human-comparison arm reports "pending."
- Does not cross-compare an NLI accuracy number against the Weissweiler 2022 encoder semantic-application baseline as if the two instruments were interchangeable.
- Does not test the model's *productive generation* of novel CC instances — a different indicator, queued for a v2.
- Does not cross-link to the AANN, way, caused-motion, or conative designs as a shared run; independent loop turn.
- Does not require Weissweiler's or Scivetti's theoretical analyses to be correct — only that the CC items are genuine CC tokens and that the cited baselines are as the source pages quote them.

## 10. Handoff hooks

When a future run executes the probe:

1. Confirm [`decisions/open/comparative-correlative-anchor`](../../wiki/decisions/open/comparative-correlative-anchor.md) status and the (to-be-opened) operationalization decision; do not promote anything to settled while either is open.
2. If the Scivetti repo is reachable, mirror `https://anonymous.4open.science/r/beyond-memorization-B82B` into `experiments/data/comparative-correlative/scivetti/` (license-check first), inspect the CC subset item-level, and confirm whether per-item human labels are released; update the resource page's `status:` accordingly.
3. Commit the full item list to `experiments/data/comparative-correlative/items.csv` (columns per §3.2), lexically frozen, before the probe runs.
4. Run the 3-item dry run per panel model to confirm label parsing / logprob availability.
5. Write the probe code under `experiments/runs/<date>-comparative-correlative-probe-v1/` mirroring the calibration probe at `experiments/runs/2026-05-28-panel-calibration/probe.py`.
