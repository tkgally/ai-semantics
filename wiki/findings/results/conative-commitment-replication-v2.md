---
type: result
id: conative-commitment-replication-v2
title: claude's COMMITMENT-ONLY conative anomaly does NOT replicate on a fresh verb set — the v1 +0.46 was verb-set-specific, not a stable single-model property
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
  - rel: depends-on
    target: design/conative-commitment-replication-v2
  - rel: depends-on
    target: result/conative-preference-commitment-v1
  - rel: refines
    target: result/conative-preference-commitment-v1
  - rel: refines
    target: essay/preference-without-commitment
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: supports
    target: claim/preference-commitment-dissociation-aann-specific
---

# Result: conative COMMITMENT-ONLY direct replication v2

A **clean direct replication** of the one positive effect in
[`result/conative-preference-commitment-v1`](conative-preference-commitment-v1.md): claude-sonnet-4.6's
**COMMITMENT-ONLY** double contrast — Δ²_commit = **+0.46**, 95% CI [0.08, 0.79], a commitment shift
*without* a preference shift, the mirror of the AANN dissociation. That effect rested on one model,
one item set, a wide CI; v1's *Honest limits* flagged it as "an anomaly worth a future look, not a
finding." This run put the **identical instrument, scoring, thresholds, bootstrap, and panel** to a
**fresh, disjoint** verb set (12 new conative verbs + 8 new resist verbs; `analyze.py` byte-identical
to v1, `probe.py` differing only in its docstring) to ask the one question a replication answers: is
the effect **stable** or **one-item-set noise**? Frozen design:
[`design/conative-commitment-replication-v2`](../../../experiments/designs/conative-commitment-replication-v2.md);
run record: [`experiments/runs/2026-06-15-conative-commitment-replication-v2/`](../../../experiments/runs/2026-06-15-conative-commitment-replication-v2/README.md).
Runs under the ratified [`decisions/resolved/fresh-construction-inferential-generalization`](../../decisions/resolved/fresh-construction-inferential-generalization.md)
(Option A — the conative); **no new decision**.

## Headline — the effect did NOT replicate (claude FAILS the pre-registered replication criterion)

claude's COMMITMENT-ONLY effect **vanished** on the fresh verbs. Its Δ²_commit fell from **+0.46 →
+0.04** (95% CI [−0.29, 0.33], not positive), and its category flipped from COMMITMENT-ONLY to
**LEXICAL-CUE ARTIFACT** — the same category the other two models occupied in v1. The driver is
transparent: claude withheld the contact entailment for the licensed conative **58% of the time in
v1** but only **17% (2 of 12 verbs) on the fresh set**. The pre-registered replication criterion
(REPLICATES iff claude's Δ²_commit ≥ 0.20 with bootstrap CI-lower > 0, Δ²_pref not positive) is
**not met**. **VERDICT: FAILS TO REPLICATE.** The v1 +0.46 is best read as **verb-set-specific
(plausibly one-item-set noise)**, not a stable single-model property.

## The numbers (per model; independently verified — see Verification)

Headroom precondition (transitive contact default must read at ceiling): **all three PASS at 1.00 /
1.00** — so this is not a ceiling artifact; there was full room for a construction effect and none
appeared.

| model | headroom | Δ²_pref (cancel-pref: conative − resist) | pref CI | Δ²_commit (withhold: conative − resist) | commit CI | category |
|---|---|---|---|---|---|---|
| **A** claude-sonnet-4.6 | PASS (1.00 / 1.00) | −0.2917 (0.333 − 0.625) | [−0.71, 0.13] | **+0.0417** (0.167 − 0.125) | **[−0.29, 0.33]** | **LEXICAL-CUE ARTIFACT** |
| **B** gpt-5.4-mini | PASS (1.00 / 1.00) | +0.25 (0.25 − 0.00) | [0.00, 0.50] | −0.125 (0.00 − 0.125) | [−0.375, 0.00] | **LEXICAL-CUE ARTIFACT** |
| **C** gemini-3.5-flash | PASS (1.00 / 1.00) | −0.4167 (0.333 − 0.75) | [−0.79, 0.00] | −0.125 (0.00 − 0.125) | [−0.375, 0.00] | **LEXICAL-CUE ARTIFACT** |

τ = 0.20 (inclusive); "positive" requires Δ² ≥ τ **and** bootstrap 95% CI lower bound **> 0** (strict;
10,000 resamples, seed 20260615; two-sample item-level bootstrap). **No model is positive on either
arm.** Panel verdict **INCONCLUSIVE** (no CONVERGENT-POSITIVE + PARAPHRASE-ONLY pair; not unanimously
convergent or null).

- **The v1→v2 collapse for the target effect.** claude Δ²_commit: v1 **+0.458** (withhold 0.583 vs
  0.125) → v2 **+0.042** (withhold 0.167 vs 0.125). The entire effect lived in claude withholding the
  contact entailment for *those particular* v1 conative verbs (kick/hit/punch/…); on a fresh,
  equally-licensed conative sample (slap/smack/pound/…) it overwhelmingly affirms contact.
- **gpt's +0.25 paraphrase Δ² is not positive** (CI lower bound exactly 0, excluded by the strict
  rule), and its negative Δ²_commit is again its known conative NLI fragility (withhold|conative =
  0%), **not** retrofitted as evidence (the carried-over pre-registered scoring rule).

## Robustness — the critic's flagged verbs behaved as predicted (conservatively)

The fresh-verb pre-run critic flagged two pro-effect risks and one conservative risk; the raw data
confirm none manufactured an effect:

- **strike / beat (figurative-inflation risk):** both returned NLI = entailment for claude (no
  withhold) — i.e. they did **not** inflate Δ²_commit. The concern is moot; the only two conative
  verbs claude withheld on were **slap** and **smack**.
- **squash (marginal-resist risk):** squash was the one resist verb claude withheld on (raising
  P(withhold|resist) to 0.125) — exactly the **conservative** direction (it *shrinks* Δ²_commit), and
  with Δ²_commit already ≈ 0 it changes nothing. Dropping squash would only move claude's Δ²_commit
  *up* toward 0.17, still far below τ and with a CI spanning 0.

## What this means

### For claude's v1 anomaly — retired as non-robust

The single genuine construction effect v1 surfaced — claude's commitment-without-preference, the lone
counter-signal to "the AANN dissociation is AANN-specific" — **does not survive a fresh lexical
sample**. It was a property of the v1 conative verbs, not of the conative construction in claude. The
honest status: **the COMMITMENT-ONLY anomaly is not replicable on independent items**; it should not
be carried forward as evidence that claude "licenses the conative inference."

### For the generality question — the AANN-specific reading is strengthened

[`result/conative-preference-commitment-v1`](conative-preference-commitment-v1.md) already found the
AANN preference-without-commitment shape did **not** generalize to the conative. The one wrinkle was
claude's mirror effect. With that wrinkle now shown non-robust, the conative test yields a **cleaner
negative on both arms across the whole panel**: net of the bare-*at* lexical cue, the licensed
conative moves neither the paraphrase preference nor the NLI commitment in any model, on two
independent verb samples. The most defensible present reading is unchanged and slightly firmer: **the
preference-without-commitment dissociation is, so far, AANN-specific** — it does not appear on the
conative under this instrument, and the apparent single-model exception was sampling noise. (Still one
construction; this does not prove AANN-uniqueness — see Honest limits.)

### For the essay and theory page

[`essay/preference-without-commitment`](../essays/preference-without-commitment.md): the scope-limiting
datum from v1 is reinforced — the conceptual "two constructs" point stands, but the conative provides
no positive instance of the dissociation in *either* direction once the v1 anomaly is retired (logged
as a revision-log entry, no trigger fired — the essay's triggers are AANN-internal). For
[`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
*(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
— cited here as the edition this page engaged.)*: the
instrument-sensitivity story stays construction-particular, and the conative now reads as a clean
"no-dissociation" construction for all three models on both instruments.

## Anchor discipline (identical split to v1)

- **NLI commitment arm, conative items — human-anchored** via
  [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (conative subset, ratified 2026-05-29). The CxNLI conative gold for a "V-at-NP → made contact"
  hypothesis is **non-entailment** (the catalogued triple *"I sipped at the Heineken."* / *"The
  Heineken was not the target of my sipping."* is **Contradiction**, Table 9; Exp-1 native baseline
  ≈ 0.90) — an **answer-key comparison + aggregate baseline, NOT a per-item human gradient**. Against
  that key, on the fresh verbs **no model reliably withholds for the licensed conative** (claude 17%,
  gpt 0%, gemini 0%): all three commit to contact for most conatives — further from the
  human-adjudicated non-entailment key than v1's claude was.
- **Paraphrase forced-choice arm and resist/LCC arm — `internal-contrast-only`.** No in-repo human
  paraphrase-preference norm exists; the anomalous at-string has no human reading key. The
  expert-stipulated conative-correct paraphrase reading (cancel) is labelled expert-stipulated. **No
  anchor invented.**

## Honest limits

- **A non-replication, not proof of absence.** Failing to reproduce a wide-CI single-model effect on
  one fresh sample is strong evidence it was noise, but it does not *prove* claude never shows a
  conative commitment effect; it shows the v1 magnitude is not robust to verb choice.
- **Still one construction.** Two conative verb samples both failing to reproduce the AANN shape
  strengthens "AANN-specific so far" but cannot establish AANN-uniqueness; that needs a genuinely
  different construction with engineered headroom (the ratified decision's named fallback).
- **The verb-class confound is inherited and disclosed.** The double contrast is
  *licensed-conative-vs-anomalous-at-string*, not a perfect lexical minimal pair (only non-alternating
  verbs are non-conative); the headroom gate is on the conative-verb transitives (the correct anchor).
- **`results.json` carries inherited v1 label strings.** Because `analyze.py` is byte-for-byte from
  v1 (the replication-fidelity requirement), `results.json` records `"run"`/`"design"` as the **v1**
  identifiers and its printed header says "v1". This is a cosmetic inheritance, **not** a yardstick
  change (verified by the post-run verifier); the numbers are this run's, computed from this run's
  `raw/`.

## Verification

- **Pre-run:** a fresh independent critic returned **GO** (no blocker): `analyze.py` byte-identical to
  v1, `probe.py` differing only in docstring, stimuli sha256[:16] `84e2e0d6afb4b5b6`, all 12 conative
  verbs genuinely alternate with transitive contact-entailment, all 8 resist verbs non-alternating
  with **no idiomatic "at" reading** (LCC purity clean), contaminant direction conservative. (PREREG §8.)
- **Freeze discipline:** stimuli + `probe.py` + `analyze.py` + `PREREG.md` committed (freeze commit
  `5affa9b`) before any model call; the post-run verifier confirmed `git diff` on those is empty since
  the freeze.
- **Post-run:** independent verifier returned **REPRODUCED-CLEAN** — every per-model P, Δ², CI, and
  the panel verdict recomputed independently (not via `analyze.py`) and matched; parsing clean (0
  unparsed of 240 rows); withhold = NLI ≠ 0 pooled correctly (no v4-style aggregation bug); cost
  summed independently to ≈ $0.0502, 0 calls missing `usage.cost`; the non-replication is the honest
  outcome and gpt fragility was not retrofitted.
- **Spend:** 240 calls, **$0.05 billed** ($0.0502); day total 2026-06-15 = $0.05 (v1) + $0.05 (this
  run) = **$0.10 of $5.00**.
