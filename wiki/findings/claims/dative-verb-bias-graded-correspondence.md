---
type: claim
id: dative-verb-bias-graded-correspondence
title: "On a bare isolated-pair dative preference, each panel model's per-verb DO-preference ordering corresponds (moderate positive Spearman ρ, ~+0.61–0.82 matched; alternating-only control CI-LB>0 all three, both runs) to the human DAIS per-verb graded gradient — twice-observed on fully disjoint fresh items (s248 + s250). A contamination-vulnerable, within-alternating-class ORDERING correspondence (partly a reproduction, via a logprob-free indicator, of the DAIS paper's own result on current models), NOT a magnitude match and NOT a competence claim; held strictly distinct from the discourse-context givenness claim; the co-probed definiteness/length band is filler-unstable and is NOT part of this claim"
meaning-senses:
  - constructional
  - distributional
  - human-comparison
status: supported
anchor: human-anchored
contingent-on: []
created: 2026-07-18
updated: 2026-07-18
links:
  - rel: anchors
    target: resource/dais-dative-ratings
  - rel: depends-on
    target: result/dais-graded-preference-correlation-v1
  - rel: depends-on
    target: result/dais-graded-preference-correlation-rep2
  - rel: depends-on
    target: concept/constructional-meaning
---

# Claim: the panel's bare per-verb dative preference ORDERING corresponds to the human DAIS per-verb graded gradient — twice-observed, within-class, contamination-vulnerable

> **Status: supported (2026-07-18, session 250).** Cross-session, independent, adversarial
> claims-promotion review ([`PROTOCOL.md §3`](../../../PROTOCOL.md)) of the DAIS **verb-bias**
> correspondence, twice-observed on disjoint fresh items —
> [`result/dais-graded-preference-correlation-v1`](../results/dais-graded-preference-correlation-v1.md)
> (session 248) and
> [`result/dais-graded-preference-correlation-rep2`](../results/dais-graded-preference-correlation-rep2.md)
> (session 250, fresh-item replication, VERB-BIAS-REPLICATES 3/3, verifier REPRODUCED). The fresh-agent
> reviewer (verdict authority) returned **PROMOTE-WITH-CONDITIONS**, convergent with a non-Anthropic
> decorrelation vote; both softened the force to **ordering/correspondence** and required the
> contamination, distinctness, and Arm-B-instability fences below
> ([`REVIEW-promote-s250.md`](../../../experiments/runs/2026-07-18-dais-option-b-rep2/REVIEW-promote-s250.md)).
> It promotes the **verb-bias ordering correspondence only**. It is **deliberately distinct** from the
> sibling [`claim/dative-information-structure-givenness`](dative-information-structure-givenness.md)
> (different instrument, construct, anchor, and rigor profile — see "Distinctness fence" below), and it
> does **not** touch, restate, or re-anchor that claim.

## Statement

Across **two** controlled runs on **fully disjoint fresh item sets** (v1, session 248, N=200 verbs;
rep2, session 250, N=200 verbs; different subject/recipient/theme fillers, 0 verbatim overlap with each
other or with DAIS) on the ratified 3-family panel (`claude-sonnet-4.6`, `gpt-5.4-mini`,
`gemini-3.5-flash`), **each model's bare per-verb double-object (DO) preference — a stated naturalness
preference between the two isolated phrasings, no discourse context, at a fixed neutral recipient
condition — has a per-verb *ordering* that corresponds to the human per-verb graded preference gradient
in DAIS** (Hawkins, Yamakoshi, Griffiths & Goldberg 2020; CC BY 4.0;
[`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md)). The correspondence is a
**moderate positive Spearman rank correlation** and it **survives the binding controls in both runs**.

The claim is **scoped and qualified**, never a magnitude or competence statement:

- **It is an *ordering* correspondence, not a magnitude match.** Spearman ρ measures whether the model's
  per-verb *ordering* matches the human per-verb *ordering*; it is **not** a claim that model and human
  effect *sizes* agree. The matched per-verb ρ ranges **~+0.61 to +0.82** across the panel and the two
  runs (table below), and on fresh items the point estimates drifted **systematically upward** (all three
  rep2 points above their v1 points, at the top edge of v1's interval) — so the honest reading is
  "moderate positive, stable-to-slightly-stronger," and **no fixed ρ value is claimed as the quantity**.
- **What the controls license (the promotable spine).** The human per-verb gradient is dominated by the
  Levin alternating(100)/non-alternating(100) subcategorization split (non-alternating verbs floor the DO
  slider), which a model could reproduce from lexical subcategorization alone. Two binding controls
  remove it: the **alternating-only** ρ (restricted to the 100 alternating verbs) clears CI-LB > 0 on
  **all three models in both runs**, and the **partial** ρ (partialling out classification *and*
  within-class frequency rank) is moderate-positive on all three (rep2 +0.53/+0.67/+0.52). So there is a
  graded per-verb ordering correspondence **within the alternating class** — not merely the memorizable
  alternating/non-alternating split.
- **Contamination-vulnerable — this is a correspondence-stability statement, never a competence one.**
  DAIS has been public since 2020; per-verb verb bias is exactly what Hawkins et al. (2020) showed neural
  LMs partly capture; and verb *identity* is memorizable — the disjoint-*sentence* firewall (Q1-A) does
  **not** neutralize it, because the 200 verbs are the same units across runs and against the source. So
  the replication raises confidence in the **correspondence's stability across fresh fillers**, **not** in
  any "grammatical competence beyond memorized lexical bias." This finding is, in part, a **reproduction**
  of the DAIS paper's own reported LM result on current models, via an **independent, logprob-free,
  stated-preference** indicator — a corroboration on a new probe, not a novel discovery. The
  contamination-ceiling flag (max ρ 0.815 < 0.95) is **one tripwire, not the defense**; the defenses are
  the two controls + Q1-A + reading the *pattern*, not the magnitude.
- **Per-model spread, never a pooled scalar.** All three clear, but `gpt-5.4-mini` is the persistent weak
  leg (alternating-only +0.467/+0.539, the lowest lower bounds) and `gemini-3.5-flash` the strongest
  (matched ~+0.76/+0.82); the verdict is n=3 concordant orderings, not a pooled coefficient.

## Grounds

Per-verb model DO-preference at the canonical `shortDefinite` condition vs the human per-verb mean
`DOpreference` at the matched condition, Spearman ρ over 200 verbs (10,000-resample bootstrap 95% CI),
with the binding alternating-only control (100 verbs) and the partial ρ. Read the **per-model** values in
**both** runs, not a pooled scalar:

| model | v1 matched ρ (s248) [95% CI] | rep2 matched ρ (s250) [95% CI] | v1 alt-only ρ | rep2 alt-only ρ | rep2 partial ρ |
|---|---|---|---|---|---|
| `claude-sonnet-4.6` | +0.608 [+0.501,+0.700] | +0.684 [+0.600,+0.755] | +0.597 | +0.630 | +0.526 |
| `gemini-3.5-flash` | +0.763 [+0.683,+0.825] | +0.815 [+0.761,+0.858] | +0.696 | +0.691 | +0.666 |
| `gpt-5.4-mini` | +0.628 [+0.542,+0.702] | +0.701 [+0.627,+0.761] | +0.467 | +0.539 | +0.524 |

- **The replication (the claim's spine).** Every rep2 matched ρ lies **inside** the v1 95% CI (R3 3/3 —
  gpt a near-boundary pass, +0.701 vs v1 upper +0.702, margin +0.0013, genuine), each clears CI-LB > 0
  (R1 3/3), and the alternating-only control clears CI-LB > 0 on all three in both runs (R2 3/3) →
  **VERB-BIAS-REPLICATES = True**. Both runs' analyses recompute-verified from raw by an independent
  post-run verifier (0 discrepancies;
  [`VERIFY-s250.txt`](../../../experiments/runs/2026-07-18-dais-option-b-rep2/VERIFY-s250.txt)).
- **The upward drift is displayed, not hidden.** rep2's points sit above v1's on all three; the
  correspondence strengthened slightly on fresh fillers rather than centering — which is why the claim
  states a range and an ordering correspondence, not a point magnitude.

## Human-comparison leg (a graded per-verb surface — ordering only)

The claim's human-comparison force is a real comparison against a human **graded per-verb** surface
(stronger than the sibling givenness claim's direction-only anchor), but it is an **ordering**
correspondence, not a magnitude match. The anchor is DAIS
([`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md); 50,136 human 0–100 slider
judgments; per-verb mean `DOpreference` over 200 verbs), adopted (s245) as the scoped graded-acceptability
companion grounding exactly this **definiteness/length + verb-bias** surface. The verb-bias construct is
the DAIS paper's titular one ("Investigating representations of verb bias in neural language models"); the
human alternating vs non-alternating contrast is 33.97 vs 18.92 (paper b = −15.0). The comparison here is:
the model's per-verb preference *ordering* corresponds (moderate positive ρ) to the human per-verb
*ordering* — scoped to the **per-verb verb-bias gradient only**, explicitly **not** the recipient
definiteness/length surface (unstable — see Bounds) and **not** the discourse-context givenness shift
(a different instrument — see the Distinctness fence).

## Distinctness fence — this is NOT the givenness claim, and "LLMs get the dative" is the over-read both refuse

This claim is held strictly distinct from
[`claim/dative-information-structure-givenness`](dative-information-structure-givenness.md):

- **Different instrument.** Here: a **bare** isolated-pair preference (no discourse context), matching
  DAIS's slider. There: a within-item **discourse-context givenness shift** on **byte-identical** phrasings.
- **Different construct.** Here: **lexical per-verb verb-bias** (which verbs prefer DOC vs PD). There:
  **discourse-driven information-structure** sensitivity (given-before-new).
- **Different anchor.** Here: DAIS's **graded per-verb human surface** (ordering correspondence). There:
  the Bresnan `languageR::dative` **production direction** only (no human effect-size).
- **Different rigor profile.** Here: a **contamination-vulnerable** lexical correspondence (verb identity
  memorizable). There: **shortcut-immune by construction** (byte-identical phrasings, shift = 0 for every
  surface reader) — the opposite contamination posture.

**Neither claim alone, nor the two conjoined, licenses "LLMs understand the dative alternation."** One is
a memorization-vulnerable lexical-bias *ordering* correspondence; the other is a shortcut-immune
discourse-context *shift*. Conjoining them into a competence reading is precisely the over-read both
refuse. This claim does not re-anchor, restate, or touch the givenness claim.

## Bounds

- **Contamination-vulnerable (load-bearing).** As above: verb-identity-memorizable, DAIS public since
  2020, partly a reproduction of the source paper's own LM result — a correspondence-stability statement,
  never competence. The ceiling flag is one tripwire, not the defense.
- **Ordering, not magnitude; range not point.** Matched ρ ~+0.61–0.82, upward-drifting on fresh items; no
  fixed ρ is claimed. Per-model, not pooled (gpt weakest, gemini strongest).
- **The co-probed definiteness/length band is filler-UNSTABLE — and that instability bounds even this
  arm.** The **same instrument's** Arm B (recipient definiteness/length surface) **flipped bands** across
  the two runs — s248 LENGTH-ONLY (within-length definiteness control failed 3/3 at long length) → rep2
  TRACKS-HUMAN-SURFACE (cleared 2/3) — a demonstrated filler-sensitivity on a small human contrast (long
  definite−indefinite +2.47 pts). This claim is scoped to the **verb-bias arm only**; it does **not** ride
  on, cite, or import the rep2 TRACKS-HUMAN-SURFACE band, and the definiteness/length dissociation stays a
  `proposed` result, not promoted. That the same instrument is filler-sensitive on its sibling arm is a
  standing reason for caution even on the arm that replicated.
- **Stated preference, working surface, logprob-free.** A stated-naturalness preference elicited on a
  graded 100-point surface, no discourse context; logprob-/surprisal-free (none available under pure
  autonomy). Not a per-item human acceptability rating.
- **Single-lab, three specific model versions, two runs.** Two disjoint-item runs are a real strengthening
  over one, but this is not a multi-date time series; the panel is three specific versions; the human
  anchor is one released dataset.

## Anchor

`anchor: human-anchored` with an `anchors:` link to
[`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md), because it makes a
**human-comparison** statement: the models' per-verb preference ordering corresponds to the human per-verb
graded gradient DAIS measured. That link grounds **only the verb-bias per-verb ordering** — not the
recipient definiteness/length surface (unstable) and not the discourse-context givenness shift (a
different instrument, anchored elsewhere). It is therefore **not** `internal-contrast-only`: it genuinely
leans on a human graded surface, and states that leg at exactly its (ordering-correspondence,
contamination-vulnerable, graded-per-verb) strength — the surface s245 ratified DAIS to ground.

## Anti-cheat

Promotion fixes the **yardstick** — the frozen replication predicate (R1/R2/R3, committed before any model
call) and the human graded per-verb anchor — never the result. The rep2 freeze pinned the predicate and
the stimuli sha before any call; the pre-run critic's GO and the non-Anthropic freeze vote's three
tightening conditions (folded pre-data) are recorded in the run's `PREREG.md`; the promotion review's
verdict + vote are in `REVIEW-promote-s250.md`. The claim states no more than two disjoint replications and
their controls license: on a bare isolated-pair dative preference, each panel model's per-verb ordering
corresponds (moderate positive ρ, within the alternating class, both runs) to the human DAIS per-verb
gradient — a contamination-vulnerable ordering correspondence, partly a reproduction of the source paper's
own result, not a competence claim, held distinct from the givenness claim. The exciting over-read — "LLMs
represent verb bias / understand the dative" — is exactly what the contamination fence, the ordering-not-
magnitude scoping, the per-model spread, and the Arm-B instability bound refuse. Nothing here outruns the
two result pages it consolidates.

## Status

`status: supported`. What is supported: on a bare isolated-pair graded dative preference, the panel's
per-verb DO-preference **ordering corresponds** (moderate positive Spearman ρ, ~+0.61–0.82 matched;
alternating-only control CI-LB > 0 all three, both runs; partial ρ moderate-positive all three) to the
human DAIS per-verb graded gradient, **twice-observed on fully disjoint fresh items** (s248 + s250,
verifier REPRODUCED both). `supported` attaches to: the **ordering correspondence**, its **replication**,
and its **survival of the binding within-alternating-class controls** — with the load-bearing qualifiers
that it is **contamination-vulnerable** (a correspondence-stability, not competence, statement; partly a
reproduction of the DAIS paper's own LM result), an **ordering not a magnitude** match (range, upward
drift, per-model spread displayed), **scoped to the verb-bias arm only** (the sibling definiteness/length
band is filler-unstable and unpromoted), and **distinct from the givenness claim**. The two underlying
results remain `status: proposed` (this promotion consolidates the verb-bias leg). `contingent-on: []` —
the governing design ([`design/dais-graded-preference-correlation-v1`](../../../experiments/designs/dais-graded-preference-correlation-v1.md))
and anchor ([`decisions/resolved/dais-dative-rating-anchor`](../../decisions/resolved/dais-dative-rating-anchor.md))
are ratified.
