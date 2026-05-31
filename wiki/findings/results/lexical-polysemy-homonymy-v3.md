---
type: result
id: lexical-polysemy-homonymy-v3
title: The clause-(b) discreteness test on a homonymy-enriched WiC noun subset — the headline separation test is a NULL, the one positive (homonym different-senses floored more) cannot be distinguished from plain graded distance
meaning-senses:
  - referential
  - distributional
  - human-comparison
status: proposed
anchor: resource/wic-word-in-context
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: anchors
    target: resource/wic-word-in-context
  - rel: operationalizes
    target: conjecture/lexical-sense-gradience
  - rel: refines
    target: result/lexical-polysemy-homonymy-v2
  - rel: refines
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: clause (b) on a homonymy-enriched WiC anchor — a (better-powered) NULL on the discreteness test

> **Status: proposed (2026-05-31).** The clean clause-(b) re-run the [`result/lexical-polysemy-homonymy-v2`](lexical-polysemy-homonymy-v2.md)
> null pointed to. Design [`design/lexical-polysemy-homonymy-v3`](../../../experiments/designs/lexical-polysemy-homonymy-v3.md);
> anchor [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md) (WiC **binary** same/different-sense,
> CC BY-NC 4.0; Tom decision 3a). Run record + freeze hashes:
> [`experiments/runs/2026-05-31-lexical-polysemy-homonymy-v3/`](../../../experiments/runs/2026-05-31-lexical-polysemy-homonymy-v3/README.md).
> **966 calls, $1.430 billed, 0 NA.** Independent pre-run stratification critic (no blockers; the
> etymology calls verified) + independent post-run number-verifier (every figure reproduced exactly
> from raw; the one positive stress-tested to attrition). **Claims scoped to WiC's binary
> same/different signal — never a graded correlation.**

## The one-line finding

On a homonymy-enriched WiC **noun** subset (11 etymology-distinct homonym lemmas vs 11 single-origin
polyseme lemmas, 161 items), the **headline discreteness test is a null**: the panel's graded
relatedness rating does **not** separate WiC same/different-sense pairs any *better* for homonyms than
for polysemes (AUC_homonym − AUC_polyseme ≈ 0 in all 6 model×framing cells, every permutation p
0.73–0.96). The **only** positive — homonym different-sense (F) pairs pile at the "unrelated" rating
floor more than polyseme-F pairs (gemini, claude) — **cannot be distinguished from the models simply
tracking graded relatedness** (homonym senses *are* more unrelated; v1 already established the panel
tracks that gradient), is **half-driven by a single lemma** (`case`), is **partly a gemini
scale-use quirk**, and its **clustering-honest CIs all cross zero**. So the conjecture's distinctive
bet — that polysemy is treated as a **separate discrete regime** from homonymy, *over and above*
graded distance — **remains unestablished** (clause b), now via an adequately-powered test that
diagnoses *why*, not just "untestable at this anchor" (the v2 verdict).

## What clause (b) predicted, and how v3 tested it

[`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) prediction 2: an
**intermediate regime for polysemous different-senses that is absent for homonyms** (homonym pairs at
the "different" floor; the two distributions *separable* — polysemy not treated as just-another-homonym).
[`result/lexical-polysemy-homonymy-v2`](lexical-polysemy-homonymy-v2.md) could not test this (DWUG EN
held only 3 clean homonym lemmas). v3 uses WiC's **binary** human same(T)/different(F)-sense label as
the anchor and the **same v1 ratified graded panel** (gate Q1: DURel 4-point + 0–100), and asks two
frozen questions (full pre-registration in the run README):

- **(P-b-ii)** Does the model rating separate **T vs F better for homonyms** than polysemes? — **AUC**
  of *r* against the binary label, within each stratum. Predicted positive.
- **(P-b-i)** Do **homonym-F items sit at the floor** (a separable low mode) while polyseme-F items
  keep intermediate mass? — floor-fraction and mean *r* among F items, by stratum. Predicted positive.

Both nulls (N1 no low mode; N2 equal separation) were declared first-class. The instrument, strata,
floor band (durel=1 / cont≤10), permutation/bootstrap, and matched control were all frozen (sha256)
**before any model call**.

## Numbers (every figure independently reproduced from raw — post-run verifier)

Panel: claude-sonnet-4.6 (A) / gpt-5.4-mini (B) / gemini-3.5-flash (C). 161 items: HOMONYM 21T/39F
(11 lemmas), POLYSEME 36T/65F (11 lemmas).

### P-b-ii — same/different separation by stratum: **NULL** (N2 holds)

| model × framing | AUC_homonym | AUC_polyseme | **AUC diff (H−P)** | perm p | cluster-boot 95% |
|---|---|---|---|---|---|
| claude · durel | 0.882 | 0.879 | **+0.003** | 0.96 | [−0.11, +0.10] |
| claude · cont | 0.882 | 0.900 | **−0.019** | 0.73 | [−0.12, +0.07] |
| gpt · durel | 0.775 | 0.799 | **−0.024** | 0.85 | [−0.23, +0.15] |
| gpt · cont | 0.830 | 0.852 | **−0.022** | 0.83 | [−0.21, +0.12] |
| gemini · durel | 0.894 | 0.878 | **+0.016** | 0.76 | [−0.09, +0.09] |
| gemini · cont | 0.907 | 0.904 | **+0.003** | 0.96 | [−0.11, +0.07] |

The rating **separates WiC's binary classes well in *both* strata** (AUC 0.78–0.91 — itself a clean
replication that the panel tracks the human sense split, cf. v1) — but **homonyms are not separated
better than polysemes**. Every AUC diff is within ±0.024 of zero; no permutation approaches
significance. This is the discreteness-specific prediction, and it is **null**.

### P-b-i — floor-piling among different-sense (F) items: a positive that does not survive scrutiny

| model × framing | floorfrac homonym-F | floorfrac polyseme-F | **floor diff** | perm p | meanF_H < meanF_P? |
|---|---|---|---|---|---|
| claude · durel | 0.436 | 0.185 | **+0.251** | 0.024 | 2.00 < 2.23 ✓ |
| claude · cont | 0.564 | 0.308 | **+0.256** | 0.066 | 30.9 < 37.1 ✓ |
| gpt · durel | 0.282 | 0.154 | +0.128 | 0.13 | 2.10 ≈ 2.12 |
| gpt · cont | 0.179 | 0.200 | −0.021 | 0.81 | 38.9 > 31.9 ✗ |
| gemini · durel | 0.410 | 0.000 | **+0.410** | ~0.00 | 1.92 < 2.42 ✓ |
| gemini · cont | 0.487 | 0.031 | **+0.456** | ~0.00 | 33.1 < 45.5 ✓ |

Surface read: gemini and claude floor homonym-F items more than polyseme-F items (gpt null). But the
post-run verifier stress-tested this to attrition — **four reasons it is not evidence for a discrete
regime:**

1. **It is exactly what plain graded tracking predicts (the load-bearing confound).** Homonym
   different-sense pairs are *etymologically unrelated*, so they sit further out on the **same single
   relatedness gradient** v1 already showed the panel tracks. A model with **one continuous
   relatedness axis and no discrete sense regime** floors them more *purely because they are more
   unrelated*. Nothing in the data separates "a separable low mode / discrete sense boundary" from
   "monotone graded distance, homonyms further out." The AUC-diff null (P-b-ii) confirms the
   *rank-ordering quality is identical across strata* — no extra separability where a discrete regime
   would live. A genuine discreteness test needs bimodality *within* a stratum, or a contrast holding
   graded distance constant — neither is available here (the overlap covariate is ≈0 for all cells,
   so it cannot adjust for distance either). **The floor effect is consistent with the conjecture but
   gives no evidence for it over the simpler v1 graded-distance account.**
2. **Half of it is one lemma.** `case` supplies 8 of the ~16–17 floored homonym-F items. Removing
   `case`, the floor diff drops gemini 0.410→0.308 and claude 0.251→0.162 — survives but materially
   attenuated, resting on ~9 floored items spread thinly across few lemmas.
3. **Gemini's is partly a scale-use quirk.** All 16 of gemini's durel "1" ratings (of 161) are
   homonym-F; gemini *never* rates a polyseme-F pair (or any T pair) at the floor, so polyseme-F floor
   is structurally pinned at 0, mechanically inflating the diff.
4. **Clustering-honest CIs cross zero.** The whole-lemma cluster bootstrap on the AUC diff straddles 0
   everywhere; the floor diff rests on thin, clustered counts. The permutation p (gemini ≈0, claude
   durel 0.024) is the most favorable framing; under honest clustering even the floor diff is not
   robustly nonzero.

So **N1 (no separable homonym low mode) is not cleanly rejected**: the apparent low mode is
confound-laden, lemma-concentrated, scale-quirk-amplified, and CI-fragile. Read together with the
clean N2 (AUC) null, **clause (b) is not established.**

## Honest limits (carried from the design + both adversarial passes)

- **Binary anchor, binary claim.** WiC grounds only a same/different separation; **no graded-relatedness
  claim** is made against WiC (it has no graded human axis). The graded-monotonicity positive stays
  anchored to DWUG via [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md). v3 scores a
  graded model rating against a *binary* human label, by stratum.
- **The discreteness/graded-distance confound is intrinsic to this design** (verifier's headline; reason
  1 above). v3 cannot, even in principle, separate a discrete homonymy regime from graded distance with
  a lemma-level homonym/polyseme contrast. A cleaner test would need pair-level senses (to hold human
  graded distance constant across strata) — which WiC does not expose.
- **Lemma-level, not pair-level.** WiC does not release per-item sense ids, so the homonym/polyseme
  label is applied at the lemma level. Many homonym-F items are within-etymon polysemy splits (e.g.
  `case` = instance-vs-legal-case, both *casus*; `school`-F is mostly education-vs-education; `rock`'s
  music sense never appears) — a dilution that biases *toward* the null (conservative for P-b-ii, and it
  blunts P-b-i). Stated pre-run.
- **The lexical-overlap matched control is vacuous here.** 159/161 items have overlap = 0 (WiC's short
  lexicographer sentences share almost no content words), so the "low-overlap subset" is the whole
  sample — it controls nothing. Disclosed (not "a passed control").
- **WiC negatives are pruned of the closest polyseme pairs** (resource page, verbatim rule), so the
  polyseme-F stratum is the *clearer* negatives, mildly stacking the deck *toward* finding a
  homonym/polyseme difference — which makes the P-b-ii **null** a *conservative* (strong) outcome.
- **Thin homonym pool / few lemmas.** The homonym AUC effectively rests on `ball`/`case`/`date`/`school`
  (4 of 11 lemmas carry the T mass; `bank`/`pitch`/`pitcher`/`seal` have 0 T items). Far better than
  v2's 3 lemmas, but the homonym stratum is the binding, noisy side (wide CIs) — unavoidable given
  WiC's clean-homonym supply.
- **Behavioral, single temp-0 run, logprob-free, English, n=161/3 models.** Inherits every v1 caveat;
  the representation lane stays deferred on local compute.

## Methodological by-product (recorded for the op-gate)

Tom's steer this round was to *prefer the WordNet lexicographer-file rule over the etymological
fallback* (gate Q2) now that nltk WordNet is installable. Evaluating it (`explore.py`) produced a
durable finding: **the bare WordNet lexicographer-file + hypernym rule over-calls homonymy ~6:1** —
of 2,585 WiC (lemma,pos) keys it labels 1,487 HOMONYM, flagging textbook *polysemes* like
*make/break/take/head/work/play* as homonyms (WordNet's fine sense granularity scatters *related*
senses across lexnames with shallow common hypernyms; for verbs it is useless). Even for the noun
*light* it returns a false homonym (2 noun clusters, but the noun is single-origin; the etymologically
distinct *not-heavy* root is adjective/verb). So the gate's **etymology AND-condition is load-bearing**
exactly as written; v3 used the **etymology-grounded** classifier (nouns only), each HOMONYM call
backed by a quoted distinct-origin statement in `stratification.csv`, with `grave`/`key`/`light`
excluded as ambiguous/cross-POS. (The WordNet structural signal is recorded only as a supporting cue.)

## Relation to other findings

- **Refines** [`result/lexical-polysemy-homonymy-v2`](lexical-polysemy-homonymy-v2.md): v2 closed clause
  (b) as *untestable at the DWUG anchor* (3 homonyms); v3 closes the **discreteness-separation** prediction
  (P-b-ii) as a *powered null* on a purpose-built, homonymy-enriched, human-rated (binary) anchor, and
  shows the only floor signal is confounded with graded distance.
- **Refines** [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md): the high within-stratum
  AUCs (0.78–0.91) re-confirm the panel tracks the human sense split; the new result is that this
  tracking is **graded, with no evidence of a *separate* discrete homonymy regime** beyond it. The
  gemini > claude > gpt ordering on the (confounded) floor signal mirrors the v1 lexical-tracking order.
- **Operationalizes** [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md)
  clause (b): the distinctive bet stays **not established** (now powered). Clauses (a)+(c) remain
  supported by v1.

Anchored to [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md). `contingent-on: []`.
Cost **$1.430 billed** (gemini $1.227 — reasoning-token dominated, as on every multi-call run).
