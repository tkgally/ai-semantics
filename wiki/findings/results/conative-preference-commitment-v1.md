---
type: result
id: conative-preference-commitment-v1
title: The AANN "preference without commitment" dissociation does NOT generalize to the conative — a fresh divergent-default construction returns INCONCLUSIVE, with the preference component absorbed by the bare lexical cue
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: supported
contingent-on: []
created: 2026-06-15
updated: 2026-07-05
links:
  - rel: contradicts
    target: conjecture/preference-commitment-generality
  - rel: depends-on
    target: design/conative-preference-commitment-v1
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: refines
    target: essay/preference-without-commitment
  - rel: refines
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: refines
    target: result/conative-commitment-replication-v2
---

# Result: conative preference/commitment double contrast v1

The project's test of whether its sharpest cross-instrument dissociation — the AANN
**preference without commitment** ([`result/aann-inferential-v6`](aann-inferential-v6.md),
replicating [`result/aann-inferential-v4`](aann-inferential-v4.md); a forced-choice paraphrase
preference shifts in all three panel models while the NLI entailment commitment carries in only one)
— is **AANN-specific or general**. The forward bet was
[`conjecture/preference-commitment-generality`](../conjectures/preference-commitment-generality.md):
that the dissociation is a general property of constructions whose licensed inference diverges from
their distributional default. It was tested on the **conative** ("Maria kicked **at** the ball" →
contact not guaranteed), a cancel-direction construction supplying the inference/default divergence
"for free." Frozen design: [`design/conative-preference-commitment-v1`](../../../experiments/designs/conative-preference-commitment-v1.md);
run record: [`experiments/runs/2026-06-15-conative-preference-commitment-v1/`](../../../experiments/runs/2026-06-15-conative-preference-commitment-v1/README.md).
Governed by the ratified [`decisions/resolved/fresh-construction-inferential-generalization`](../../decisions/resolved/fresh-construction-inferential-generalization.md)
(Option A — the conative; ratified 2026-06-15).

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The single-model COMMITMENT-ONLY
> anomaly reported below (claude Δ²_commit = +0.46) was put to a same-day fresh-verb-set
> replication and **failed to replicate** —
> [`result/conative-commitment-replication-v2`](conative-commitment-replication-v2.md): "VERDICT:
> FAILS TO REPLICATE"; the effect is read as verb-set noise and is not carried forward. The
> AANN-specific scope of the dissociation is what survives, promoted as
> [`claim/preference-commitment-dissociation-aann-specific`](../claims/preference-commitment-dissociation-aann-specific.md).
> *(Back-annotation: this page's numbers and INCONCLUSIVE verdict stand unchanged.)*

## Headline — VERDICT: INCONCLUSIVE; the dissociation did not generalize

**The AANN preference-without-commitment shape did not reproduce on the conative.** The two
instruments do not split the way they did for AANN; the panel matches neither the confirm shape
(≥1 CONVERGENT-POSITIVE **and** ≥1 PARAPHRASE-ONLY), nor full convergence, nor a full null. Two
facts carry the reading:

1. **The "preference" component — broad in AANN — is here a bare lexical-cue effect.** The
   paraphrase double contrast **Δ²_pref = P(cancel-pref | conative) − P(cancel-pref | resist/LCC)** is
   **non-positive in all three models** (claude −0.21, gpt 0.00, gemini −0.04). The licensed conative
   does **not** move the paraphrase preference *more than the matched anomalous "at"-string moves it*:
   both the conative and the bare-*at* control shift the reading toward "did not necessarily make
   contact" together. So the broad, cross-model paraphrase shift that defined the AANN dissociation
   has **no construction-specific analogue** on the conative once the lexical cue is netted out.
2. **The only construction effect is a single model's *commitment* shift — the mirror of AANN.**
   claude-sonnet-4.6 shows a positive **Δ²_commit = +0.46** (95% CI [0.08, 0.79]): it withholds the
   contact entailment for the licensed conative more than for the anomalous at-string — a
   **COMMITMENT-ONLY** effect (commitment *without* preference), the inverse of the AANN
   preference-without-commitment. The other two models show no positive double contrast on either arm
   (both **LEXICAL-CUE ARTIFACT**).

## The numbers (per model; verified independently — see Verification)

Headroom precondition (the conative-translated gate, per the ratification condition): the transitive
contact default must read at ceiling so there is room for the conative to suppress it.

| model | headroom | Δ²_pref (cancel-pref: conative − resist) | pref CI | Δ²_commit (withhold: conative − resist) | commit CI | category |
|---|---|---|---|---|---|---|
| **A** claude-sonnet-4.6 | PASS (1.00 / 1.00) | **−0.2083** (0.667 − 0.875) | [−0.58, 0.17] | **+0.4583** (0.583 − 0.125) | **[0.08, 0.79]** | **COMMITMENT-ONLY** (anomaly) |
| **B** gpt-5.4-mini | PASS (0.92 / 1.00) | 0.0000 (0.25 − 0.25) | [−0.42, 0.38] | −0.2500 (0.00 − 0.25) | [−0.63, 0.00] | **LEXICAL-CUE ARTIFACT** |
| **C** gemini-3.5-flash | PASS (1.00 / 1.00) | −0.0417 (0.833 − 0.875) | [−0.33, 0.29] | +0.2500 (0.25 − 0.00) | [0.00, 0.50] | **LEXICAL-CUE ARTIFACT** |

τ = 0.20 (inclusive); "positive" requires Δ² ≥ τ **and** bootstrap 95% CI lower bound **> 0** (strict;
10,000 resamples, seed 20260615; two-sample item-level bootstrap over the disjoint conative/resist
verb pools). **Headroom: all three PASS** — so the INCONCLUSIVE is not a ceiling artifact; there was
room for a construction effect and it did not appear on the paraphrase arm.

- **gemini's near-miss is correctly not positive:** Δ²_commit = +0.25 but its CI lower bound is
  **exactly 0**, and the strict `> 0` rule (frozen pre-run) excludes it. Reported, not rounded away.
- **gpt's negative Δ²_commit is its known fragility, not new evidence:** gpt withholds the contact
  entailment for the conative **0%** of the time (it commits to contact under NLI), exactly the
  conative NLI fragility seen in [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md)
  and [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md). Per the
  pre-registered scoring rule, this pre-existing single-model divergence is **not** retrofitted as
  confirmation; the converger (had there been one) had to be read from this run, and there was none.

## Robustness — A's effect survives the marginal LCC verbs

The independent pre-run critic flagged two resist verbs (smash, crush) as carrying *weak* idiomatic
"V at NP" readings (the strong contaminant, "snap," was swapped out pre-run for "bump"). The design
pre-registered a with/without robustness report. **claude's COMMITMENT-ONLY effect is robust:**
dropping smash and crush from the resist pool moves Δ²_commit only from **+0.458 → +0.417** (claude in
fact withheld on only **one** resist verb — `split` — not on smash or crush). The marginal verbs did
not manufacture the effect. (gpt −0.25 → −0.167; gemini +0.25 → +0.25, unchanged.) The effect is still
a **single-model, within-model directional contrast with a wide CI (n = 12 conative vs 8 resist
stems)** — not a precise estimate, and reported as such.

## What this means

### For the conjecture — not confirmed (contradicted as stated)

[`conjecture/preference-commitment-generality`](../conjectures/preference-commitment-generality.md)
bet that a fresh divergent-default construction would **reproduce the qualitative AANN shape** (broad
paraphrase shift, narrow commitment, ≥1 model converging and ≥1 preferring-without-committing). The
conative did not. The conjecture's own confirm criterion is not met, and the pattern that did appear
(no net paraphrase shift anywhere; one model's commitment-only effect) is, if anything, the *mirror*
of the AANN dissociation. The most defensible present reading: **the preference-without-commitment
dissociation is, so far, AANN-specific — it does not generalize to the conative under this
instrument.** This is one fresh construction, so it cannot establish "the dissociation is unique to
AANN"; it establishes that the **first** generalization attempt **failed to reproduce it**, which is a
genuine, informative negative against the forward bet.

A live alternative the result raises (not claimed, flagged for a future turn): the AANN paraphrase
shift may have been *partly* a lexical-cue effect too — the conative result shows that a paraphrase
forced choice can move with a bare lexical cue alone. The AANN design controlled for this with its own
LCC and the AANN paraphrase double contrast *was* positive net of the cue; but the contrast between
"AANN paraphrase Δ² positive" and "conative paraphrase Δ² non-positive" is itself the sharpest datum
here, and is what makes the dissociation look construction-particular rather than general.

### For the essay — scope-limiting, no trigger fired

[`essay/preference-without-commitment`](../essays/preference-without-commitment.md) argued the
*type* distinction (a paraphrase preference and an entailment commitment are evidence for two
different constructs) on the AANN instance, and was explicit that its worked instance is AANN and that
"the general distinction … would survive as a conceptual point" even if an instance failed. This
result **bounds the essay's instanced scope to AANN**: the *direction* of the dissociation is not even
stable across constructions (AANN = preference-without-commitment; conative = a single model's
commitment-without-preference). The essay's two pre-registered triggers are both AANN-internal
replication triggers and neither is fired by a *different* construction; this result is logged on the
essay as a scope-limiting datum (the conceptual "two constructs" point stands; the claim that the
*preference-without-commitment ordering* is general does **not**, and the essay never made it).

### For the theory page

[`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md) *(superseded
s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) —
cited here as the edition this result fed)*: the
instrument-sensitivity story is now construction-particular. The two instruments *can* dissociate
(AANN), but the *way* they dissociate does not transfer to the conative, and on the conative the
weaker paraphrase instrument is the one that fails to show a construction-specific signal at all.

## Anchor discipline (honest split)

- **NLI commitment arm, conative items — human-anchored** via
  [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (conative subset, ratified 2026-05-29). The CxNLI conative gold for a "V-at-NP → made contact"
  hypothesis is **non-entailment** (the catalogued triple *"I sipped at the Heineken."* / *"The
  Heineken was not the target of my sipping."* is **Contradiction**, Table 9; Exp-1 native baseline
  ≈ 0.90). So the answer-key conative-correct response is **withhold** — an **answer-key comparison +
  aggregate baseline, NOT a per-item human gradient** (the release gives a single adjudicated gold
  label per item). Against that key, only claude reliably withholds for the licensed conative; gpt
  systematically does not; gemini partly.
- **Paraphrase forced-choice arm and resist/LCC arm — `internal-contrast-only`.** No in-repo human
  paraphrase-preference norm exists, and the anomalous at-string has no human reading key. The
  expert-stipulated conative-correct paraphrase reading (cancel) is labelled expert-stipulated. No
  human label was invented.

## Honest limits

- **One construction, one panel, one date.** A single fresh construction failing to reproduce the
  shape is a non-confirmation, **not** proof the dissociation is unique to AANN. The conjecture's
  general form remains open to a *third* construction (the ratified decision named the way/caused-motion
  near-miss variant as the fallback host, though those run at ceiling).
- **The verb-class confound is real and disclosed.** The double contrast is
  *licensed-conative-vs-anomalous-at-string*, not a perfect lexical minimal pair (only non-alternating
  verbs are non-conative). The headroom gate is based on the conative-verb transitives, the correct
  anchor; the result leans on Δ² net of the cue, with the robustness check above.
- **A's COMMITMENT-ONLY is an anomaly, held modestly.** Single model, wide CI, directional within-model
  contrast under a part-internal-contrast-only anchor — it is reported as an anomaly worth a future
  look, not as a finding that the conative "licenses the inference for claude."
- **No magnitude or human-comparison claim on the paraphrase arm.** The headline is the *shape*
  comparison to AANN, anchored on the NLI arm only.

## Verification

- **Pre-run:** independent critic returned **GO-WITH-FIXES**; the one SHOULD-FIX (resist verb
  `snap`→`bump`) was applied pre-run and the stimuli refrozen (sha256[:16] `3ca3a1d50069f0cd`);
  `analyze.py --selftest` re-passed (30 checks).
- **Freeze discipline:** stimuli + `probe.py` + `analyze.py` + `PREREG.md` committed (freeze commit)
  before any model call; the post-run verifier confirmed `git diff` on those is empty since the freeze.
- **Post-run:** independent verifier returned **REPRODUCED-CLEAN** — every per-model P, Δ², CI, and
  the panel verdict recomputed bit-identically from the raw outputs; parsing clean (0 unparsed of 240
  rows); the strict CI rule correctly excludes gemini's CI-lower = 0; **no NLI-aggregation bug** (the
  class caught in the v4 line does not recur); cost summed independently to **$0.049986 → $0.05**,
  **0 calls missing `usage.cost`**.
- **Spend:** 240 calls, **$0.05 billed**; day total 2026-06-15 = $0.05 of $5.00.
