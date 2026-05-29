---
type: design
id: way-construction-v1
title: way-construction inference probe v1 — path-traversal inference contrast with non-motion verbs
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: provisional
anchor: resource/scivetti-2025-cxnli-dataset
contingent-on: []
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: operationalizes
    target: conjecture/way-construction
  - rel: depends-on
    target: concept/constructional-meaning
---

# Experiment design v1 — way-construction

**Status**: the `decisions/resolved/way-construction-anchor.md` decision was **ratified 2026-05-29** — the **Scivetti CxNLI dataset** (its way-manner subset) is the human anchor. The operationalization itself is self-standing and not behind a separate gate. That fixes the yardstick, but the design is **unrun**: nothing claiming a human-comparison finding may be promoted to settled until the probe actually runs.

## 1. Construct

The ***way*-construction** (Goldberg 1995, ch. 9; Jackendoff 1990) as a construction in the Goldberg CxG sense: form = NP *way* PP, embedded in a clause with a verb in any semantic class; constructional meaning = the subject traverses a path while/by performing the action described by the verb. The verb is not required to be a motion verb; the path-traversal inference arises from the **construction**, not from the verb.

The construct of interest: whether a panel model draws the path-traversal inference from way-construction instances where the verb is non-motion — and whether it fails to draw that inference from minimally-different control items that lack the construction. This is a direct operationalization of the `constructional` and `inferential` meaning senses: if the inference arises from the constructional form rather than from the verb's lexical semantics, that is evidence the model is tracking the form–meaning pairing at the construction level.

## 2. Indicator

**Primary indicator**: binary forced-choice inference probe. For each item (a way-construction sentence or a matched control), the panel model is asked to answer whether the subject moved along a path, and the model's token-level log-probability is recorded for "yes" vs. "no" on the first answer token.

Probe template (exact; committed and frozen before probe runs):

```
Sentence: {sentence}
Question: After reading this sentence, is it true that the subject moved along a path?
Answer (yes or no):
```

Three derived numbers per panel model:

- **Construction inference rate** — fraction of way-construction items where p("yes") > p("no"). Predicted: ≥ 70%.
- **Control inference rate (Type-1)** — same, on matched control items that lack the way-construction. Predicted: substantially lower.
- **Construction-vs-control gap** — construction inference rate minus control inference rate. Predicted: ≥ 30 percentage points.

**Logprob fallback**: if a model does not expose logprobs for the answer token, fall back to temperature = 0 greedy completion and take the output string as binary (case-insensitive "yes" → 1, "no" → 0, other → NA). Record the fallback per model in the run record. NA responses are excluded from rate calculations and reported separately (if NA rate > 10%, flag as a model-level failure mode).

## 3. Method

### 3.1 Item set

Target: ~140 items total.

**Way-construction items (60)**:

Verb categories (20 items each):

- *Non-motion manner* (20): verbs whose primary meaning is manner of sound, expression, or bodily motion that does not entail displacement — *whistle, laugh, sneeze, cough, hum, mutter, sob, grumble, sing, clap, stomp, dance, twirl, gesture, wave, nod, shrug, blink, sigh, yawn*.
- *Non-motion activity* (20): verbs whose primary meaning is a sustained activity or process with no motion implication — *eat, drink, read, write, knit, paint, work, type, scroll, think, dream, worry, fret, scheme, plot, muse, chat, gossip, argue, debate*.
- *Anti-motion / stative* (20): verbs that actively implicate non-motion or a stationary state — *sit, stand, wait, pause, rest, linger, stay, remain, lurk, crouch, kneel, lie, sleep, doze, freeze, idle, halt, stall, dawdle, loiter*.

Path PPs (10, rotated across items to avoid telegraphing motion from the PP alone):
*down the hall, through the crowd, across the room, into the building, along the street, up the stairs, past the guards, around the obstacle, out of the office, into the lobby*.

Example items (illustrative; full list committed to `experiments/data/way-construction/items.csv` before probe):
- "She laughed her way through the crowd." (non-motion manner)
- "He read his way across the room." (non-motion activity)
- "They loitered their way down the hall." (anti-motion)

**Type-1 controls (60)** — same verb + same path PP, way-construction absent:

Two control subtypes (30 each):
- **Subtype 1a** — path PP with no motion implication ("He whistled *in* the hall"; "She read *beside* the room"): the PP denotes location, not traversal. Systematic: replace "*POSS way* PATH-PP" with "*LOCATION-PREP* PATH-NP".
- **Subtype 1b** — explicit motion verb + adverbial ("He whistled *as he walked* down the hall"): the path-traversal inference is now carried by *walk*, not by the construction. Tests whether the model's inference tracks construction presence, not mere path-PP presence.

Use 1a as the primary control; 1b as a secondary check on 30 items (one per way-construction item in the non-motion-manner and non-motion-activity categories).

**Type-2 controls (20)** — way-construction surface without path inference:

- **Idiomatic/metaphorical** (10): "She found *her way* around the problem"; "He lost *his way*"; "They made *their way* in the world" — surface *way* tokens where path-traversal inference is absent or metaphorical.
- **No path PP** (10): Way-construction without a path argument ("He hummed *his way*" — grammatically marginal but tests whether the model tracks PP presence as the inference trigger).

Type-2 items test over-generalization: if the model scores high on idiomatic *way* tokens, it is detecting surface strings rather than the constructional form–meaning pairing.

All items are seeded from Goldberg's (1995, ch. 9) canonical examples and extended by systematic slot-filling. The full item list (sentence, verb, verb category, control type, path PP, source) is committed to `experiments/data/way-construction/items.csv` *before* the probe runs, with the verb lists lexically frozen at that commit.

### 3.2 Panel

Per `config/models.md`:

- `panel.A` — `anthropic/claude-sonnet-4.6`
- `panel.B` — `openai/gpt-5.4-mini`
- `panel.C` — `google/gemini-3.5-flash` (reasoning-token mitigation per panel calibration caveats)

### 3.3 Probe protocol

For each panel model:

1. **Dry run** — confirm logprob availability for the answer token via a 3-item dry run (one item per way-construction verb category). If logprobs unavailable, switch to greedy-string mode; record the fallback.
2. **Full run** — for each of the ~140 items:
   - Submit the probe template with the sentence inserted.
   - Record: full prompt, first-token logprobs for "yes" and "no" (or greedy string if fallback), latency, usage tokens.
3. **Persist** raw JSON to `experiments/data/way-construction/runs/<run-date>/<panel-slot>/`.

Temperature = 0 throughout. Reasoning-token mitigation for `panel.C`: set `reasoning: {"enabled": false}` if supported; otherwise `max_tokens` ≥ 512. Document the per-model setting in the run record. Do not adjust the setting after seeing first-batch outputs.

### 3.4 Analysis

For each panel model:

1. Compute **construction inference rate** across all 60 way-construction items, reported overall and broken down by verb category.
2. Compute **Type-1 control inference rate** overall and by subtype (1a, 1b).
3. Compute **construction-vs-control gap** (overall construction rate minus overall 1a rate) and apply the T1 threshold (≥ 30pp).
4. Compute **Type-2 check rate** (expected substantially below 70%).
5. Check **verb-category monotonicity**: if the construction inference rate is substantially higher for non-motion-manner than for anti-motion items, flag as a potential verb-reading confound (see §7).

Report all rates for all three models in a single table, including NA rates and any fallback notes. Cross-model divergence is itself a result (charter §6, `config/models.md`).

No item-level cherry-picking. No post-hoc threshold adjustment.

## 4. Human anchor

**Ratified anchor (2026-05-29)**: the **Scivetti CxNLI dataset** ([`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)) — its **way-manner subset** — is the human anchor for this design (`decisions/resolved/way-construction-anchor.md`). Goldberg (1995, ch. 9) remains the **descriptive seed** for the item set: its canonical examples certify that way-construction items are genuine tokens of the construction. A resource page for the Goldberg seed (`wiki/base/resources/goldberg-1995-way-stimuli.md`) is created at probe-prep time.

**What the Scivetti anchor delivers (caveat)**: the release repo was inspected (de-anonymized at github.com/melissatorgbi/beyond-memorization) and provides a **single gold-standard label per item plus an aggregate ~0.90/0.83 human baseline — an "answer key," NOT a per-item multi-rater gradient.** So the human-comparison arm is an answer-key comparison (model label vs. gold label, model rate vs. the aggregate human baseline), not a regression against a graded human-judgment distribution. Treat the path-traversal inference as near-ceiling for human readers of canonical items only where the Scivetti gold label confirms it.

## 5. Predictions (from `conjecture/way-construction`)

1. **Construction inference rate** ≥ 70% across all 60 way-construction items, in ≥ 2 of 3 panel models.
2. **Construction-vs-control gap** ≥ 30pp (construction minus Type-1a control), in ≥ 2 of 3 panel models.
3. **Verb-category robustness**: the construction inference rate is substantially above 50% even for anti-motion verbs, in ≥ 2 of 3 panel models. (If it collapses for anti-motion, the model is reading the verb; if it collapses for the activity category, the model may be reading for manner-of-motion cues. Both are diagnostically interesting failure modes.)
4. **Type-2 check**: inference rate on idiomatic/metaphorical controls < 40%, in ≥ 2 of 3 panel models (the model is not over-generalizing from surface *way*).

## 6. Pre-flight cost check

Back-of-envelope: ~140 items × 1 prompt per item × 3 models.

| Model | Tokens in / call | Tokens out / call | Pricing (in / out per MT) | Est. cost |
|-------|-----------------:|------------------:|---------------------------|----------:|
| `panel.A` claude-sonnet-4.6 | ~80 | ~2 | $3 / $15 | ≈ $0.04 |
| `panel.B` gpt-5.4-mini | ~80 | ~2 | $0.20 / $0.60 | < $0.01 |
| `panel.C` gemini-3.5-flash | ~80 | ~2 + reasoning tokens | $0.15 / $0.60 | < $0.01 + caveat |

Total: well under $1. No pre-flight budget escalation required. Reasoning-token overage for `panel.C` is bounded — the output is a single token, so reasoning tokens are the main variable cost; set `max_tokens` ≥ 512 and accept the overhead.

## 7. Falsification criteria

- **Confirm**: construction inference rate ≥ 70% AND gap ≥ 30pp in ≥ 2 of 3 models. Direct evidence for `constructional` meaning-sense computation.
- **Verb-reading failure**: construction inference rate tracks verb motion-relatedness (collapses for anti-motion verbs relative to manner verbs). The model is reading the verb lexically, not the construction. Informative partial falsification — citable as a `distributional` finding.
- **PP-reading failure**: construction and Type-1b control (explicit-motion-verb control) both score high while Type-1a (location-PP control) scores low. The model is tracking the path PP, not the *way*-construction specifically. Diagnosis: ablation without path PP (Type-2 no-PP items) should then show low rates. Interpretable failure mode.
- **Flat rates**: construction and Type-1a controls not separable (< 10pp gap across all three models). The model treats *way*-construction surface as semantically inert.
- **Over-generalization**: Type-2 idiomatic controls score high (≥ 70%), matching construction rate. The model is detecting surface *way* tokens, not the constructional form–meaning pairing.

All outcomes above are claim-worthy results; none is a non-finding (charter §2.6).

## 8. What this design does not do

- Does not address benefactive *way*-construction (*She found him a way through*) or possessive *way* (*He made his way home* in the non-caused-motion reading). Scope is the canonical caused-motion reading.
- Does not test productive generation (can the model extend the construction to novel verbs in a generation task). That requires a different indicator and is queued as a v2 design.
- Does not cross-link to the AANN, dative-alternation, or function-word-substitutability designs. Independent constructions, independent loop turns.
- Does not require Goldberg's theoretical analysis to be correct — only that her examples are genuine way-construction tokens, which is uncontroversial in the CxG literature.

## 9. Handoff hooks

When the next run executes the probe:

1. Create `wiki/base/resources/goldberg-1995-way-stimuli.md` with provenance (Goldberg 1995 ch. 9, note page numbers of sourced examples).
2. Commit the full item list to `experiments/data/way-construction/items.csv` with columns: `item_id`, `sentence`, `verb`, `verb_category`, `path_pp`, `item_type` (way-construction / type1a / type1b / type2-idiomatic / type2-nopp), `source`.
3. Run the 3-item dry run per panel model to confirm logprob availability before committing to the full run.
4. `decisions/resolved/way-construction-anchor.md` is ratified (2026-05-29, Scivetti CxNLI way-manner subset); when the Scivetti repo is mirrored in, align §4/§5 with the actual per-item gold labels and aggregate human baseline before running.
5. Write the probe code under `experiments/runs/<date>-way-construction-probe-v1/` mirroring the calibration probe structure at `experiments/runs/2026-05-28-panel-calibration/probe.py`.
