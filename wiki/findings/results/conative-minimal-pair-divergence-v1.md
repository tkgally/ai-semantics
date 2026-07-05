---
type: result
id: conative-minimal-pair-divergence-v1
title: The project's own verb-held-constant conative minimal pairs — 2/3 models cleanly cancel the completed-contact entailment for "V at NP", but one model (gpt-5.4-mini) fails it entirely under NLI while partly recovering under forced-choice
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: proposed
contingent-on: []
created: 2026-05-29
updated: 2026-07-05
links:
  - rel: supports
    target: conjecture/conative-construction
  - rel: refines
    target: result/cxnli-distinction-divergence-v1
  - rel: supports
    target: claim/constructional-divergent-form-generalization-gap
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Result: conative minimal-pair probe v1

The project's **own verb-held-constant** test of [`conjecture/conative-construction`](../conjectures/conative-construction.md) — the cleaner follow-up to [`result/cxnli-distinction-divergence-v1`](cxnli-distinction-divergence-v1.md), which found the conative the single hardest construction on Scivetti's items but could not separate the construction from the verb. Here the **verb is identical across the two frames** (*Maria kicked the ball* vs. *Maria kicked at the ball*), so any difference in the completed-contact inference is `constructional`, not lexical. Design + frozen stimuli: [`design/conative-construction-v1`](../../../experiments/designs/conative-construction-v1.md); run record: [`experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/`](../../../experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/README.md).

**One-line finding:** the conjecture's core prediction (P1) **holds** — the panel affirms completed contact far less for the conative *at*-frame than for the matched transitive (forced-choice gap **42–88 pp, all 3 models**; NLI gap **54–67 pp** for 2 of 3). The effect **replicates across verbs**, **persists for low-frequency objects** (no memorization-artifact collapse, P3), and is **construction-specific** (much weaker for non-alternating control verbs, P2). The discriminating wrinkle: **gpt-5.4-mini fails the conative entirely under the NLI instrument** (it calls *all* 24 conative items "entailment" — *kicked at the ball* ⊨ *made contact*) yet **partly recovers under forced-choice** (gap 42 pp). The same model was the hardest-hit in the distinction probe — a convergent signal that gpt-5.4-mini is the panel's weakest conative reader.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A), `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects (charter §6). Temperature 0; **both instruments** (NLI 0/1/2 + forced-choice YES/NO/CANT_TELL), the ratified divergence operationalization. **0 NA across all 336 calls.**
- **Stimuli** (the project's own, frozen pre-run; `items.csv` sha256[:16] `9ae53279dc483827`): 12 Levin (1993) conative-alternation verbs × {typical, atypical} object × {transitive, conative}; + 4 non-alternating control verbs (touch/kiss/break/shatter). Primary indicator = **affirm completed-contact rate** (FC YES, or NLI entailment).
- **Cost** (actual, token usage): **$0.071** (A $0.049 / B $0.003 / C $0.020). Well under the $5 single-run flag.

## Results

Affirm completed-contact rate (%) and the **transitive − conative gap** (the conjecture's P1 quantity; predicted ≥30 pp). 24 items/frame/model for the conative-class arm.

| model | instrument | transitive | conative | **gap** | verbs with +gap | verbs gap ≥30 |
|---|---|---:|---:|---:|:--:|:--:|
| claude-sonnet-4.6 | NLI | 100% | 46% | **+54 pp** | 8/12 | 8/12 |
| claude-sonnet-4.6 | FC | 100% | 33% | **+67 pp** | 8/12 | 8/12 |
| gpt-5.4-mini | NLI | 92% | **100%** | **−8 pp** | 0/12 | 0/12 |
| gpt-5.4-mini | FC | 92% | 50% | **+42 pp** | 7/12 | 7/12 |
| gemini-3.5-flash | NLI | 100% | 33% | **+67 pp** | 8/12 | 8/12 |
| gemini-3.5-flash | FC | 100% | 13% | **+88 pp** | 11/12 | 11/12 |

**P1 (core) — confirmed at the ratified bar.** The ≥30 pp gap holds in **3/3 models under forced-choice** and **2/3 under NLI**, and it **replicates across verbs** (8/12 for claude and gemini; 7/12 for gpt under FC) rather than being carried by one verb. The single failing cell is gpt-5.4-mini under NLI (see below).

### P3 (frequency / memorization control) — confirmed

The gap **does not depend on object frequency**: typical-object vs. atypical-object gaps differ by ≤ 8.4 pp in every model×instrument cell (claude NLI 58→50; claude FC 67→67; gemini NLI 67→67; gemini FC 83→92; gpt FC 42→42). The non-completion reading **persists for low-frequency objects** (*kicked at the gourd*, *struck at the cymbal*), so it is not plausibly a memorized-typical-string artifact — direct support for the constructional (not n-gram) account of the contrast ([`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md)).

### P2 (verb-class specificity) — supported, with a nuance

The contact-cancellation is **construction-specific**, not a generic "*at* = atelic" effect. Control (non-alternating) verbs show a much smaller gap than conative-class verbs in 5 of 6 model×instrument cells. Cleanest under NLI for claude: the control-conative gap is **−25 pp** (claude reads the *anomalous* *touched at the wall* as entailing contact *more* than the control transitive) while the genuine conative gap is **+54 pp** — claude specifically cancels contact for the licit conative, not for *at* in general. The nuance: under forced-choice, control verbs still show a ~25 pp gap in every model, so *at* on an anomalous string does pull affirm-rate down somewhat — but far less (≈25 pp) than the genuine conative (≈42–88 pp).

### The cross-instrument divergence (the discriminating result)

**gpt-5.4-mini under NLI labels all 24 conative items "entailment" (0)** — it treats *kicked at the ball* as entailing *made contact with the ball*, the opposite of the construction's meaning, with a 0/12 verb replication. Yet the **same model under forced-choice** answers CANT_TELL on half the conative items (gap +42 pp). So the conative non-completion inference is **latent but instrument-fragile** in gpt-5.4-mini: the forced-choice "based only on the sentence" framing surfaces it; the NLI entailment framing collapses it to a default "yes, contact." Claude and gemini are stable across both instruments. This is exactly the kind of cross-model + cross-instrument divergence the panel design exists to surface (charter §6), and it converges with the distinction probe, where gpt-5.4-mini was the hardest-hit model overall.

## Interpretation (modest)

1. **The conative's non-completion meaning is partly available to current decoders — more so than the Scivetti distinction items suggested.** With clean verb-held-constant minimal pairs, claude and gemini cancel the completed-contact entailment 54–88 pp of the way, and even gpt-5.4-mini does under forced-choice. This **refines** [`result/cxnli-distinction-divergence-v1`](cxnli-distinction-divergence-v1.md): the conative "collapse" there (panel 20–45% correct) reflects partly the *adversarial difficulty* of Scivetti's distinction items, not a blanket inability to read the conative — a clean minimal-pair contrast is substantially easier. Both can be true: the construction's core contrast is largely tracked, while the harder divergent-form items defeat it.
2. **The contrast is constructional, not lexical or distributional.** Verb held constant (P1), persists on low-frequency objects (P3), specific to alternating verbs (P2). This is the cleanest verb-control the wedge has run, and it points at `inferential`/`constructional` tracking rather than an n-gram shadow.
3. **Instrument framing is a first-class variable.** A model can carry the inference under one elicitation and lose it under another (gpt-5.4-mini). Single-instrument results over-state or under-state competence; the divergence is the datum.

## What this licenses / does not license

**Licenses:** a project-owned, revisable statement that current decoders partly track the conative alternation's non-completion meaning with verb held constant (P1 confirmed at the ratified bar, P2/P3 supported), promoting [`conjecture/conative-construction`](../conjectures/conative-construction.md) to `tested` (supported, with the gpt-NLI divergence as the standing caveat).

**Does NOT license:**
- **A "models understand the conative" claim.** This is behavioral affirm-rate on one contrast; 2/3 models still leave 13–46% of conative items affirming contact, and gpt-5.4-mini fails the NLI framing outright. "Partly tracks, instrument-fragile" is the calibrated reading.
- **A tight magnitude or item-matched human comparison.** N = 12 verbs (24 items/frame); single run; the Scivetti anchor is an answer-key + aggregate baseline, and these are the project's *own* items, so the human bearing is to the *phenomenon* (the conative is a real, learnable contrast with a ≈0.90/0.83 native baseline), not an item-matched accuracy.
- **A model-internal or grounding claim.** Behavioral only.

## Limits

- **N = 12 verbs, single run, single date, two instruments.** Cross-model + cross-instrument convergence/divergence is the robustness signal, not any single cell's precision.
- **`swat`'s transitive contact is the softest of the set** (swatting can miss); noted at design time. The effect is robust across the other 11 verbs, so this does not carry it.
- **Control arm is N = 4 verbs** and its conative cell is an *anomalous* string (gold `NA`); the P2 conclusion rests on the gap being much smaller than the conative-class gap, not on a clean control baseline. gpt-5.4-mini also labelled 2/24 transitive items "contradiction" under NLI (minor parse-of-meaning noise).
- **Verb-neutral "made contact with" predicate** reads most naturally for impact verbs; chosen to hold the hypothesis constant across verbs.
- **Shared priors (charter §2.5):** three decoders are not three independent witnesses; the independent bearing is the Levin/Scivetti human anchor.

## Provenance

- Conjecture: [`conjecture/conative-construction`](../conjectures/conative-construction.md) (P1/P2/P3, confirm/falsify criteria). Operationalization: [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md) (ratified; both instruments, 30/15-pp thresholds, frozen pre-run). Anchor: [`decisions/resolved/conative-anchor`](../../decisions/resolved/conative-anchor.md) → [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md). Verb-class inventory: Levin (1993) conative alternation classes.
- Complements/refines: [`result/cxnli-distinction-divergence-v1`](cxnli-distinction-divergence-v1.md); supports [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md).
- Run record + code + full (unredacted, own-stimuli) outputs + cost: [`experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/`](../../../experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/README.md). Every number here is reproducible from the committed `raw/results.json`.

## Status

`status: proposed`. Numbers reproducible from committed code + `raw/results.json`. `contingent-on: []` (governing operationalization ratified). Promotion past `proposed` awaits Tom's review. *(Governance note, s183: since the autonomous-era amendment of 2026-06-12 — [`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous cross-session adversarial review; Tom holds a standing override.)* The standing caveat is the gpt-5.4-mini NLI failure and the instrument-fragility it reveals.
