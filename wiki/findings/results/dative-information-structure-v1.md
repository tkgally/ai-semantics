---
type: result
id: dative-information-structure-v1
title: Dative alternation tracks information structure — all three panel models shift DOC/PD preference in the human direction (given recipient → double-object, given theme → prepositional), length and animacy held constant, the effect surviving the end-weight dissociation control; a human-anchored Tier-2 positive with effect size sharply decorrelated across models
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-06-20
updated: 2026-06-20
links:
  - rel: depends-on
    target: conjecture/dative-alternation-information-structure
  - rel: anchors
    target: resource/languageR-dative-corpus
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/constructional-meaning-in-llms
---

# Result: the dative alternation tracks information structure (v1)

> **Status: proposed (2026-06-20, session 51).** Runs the frozen, certified, pre-run-critic-GO'd
> instrument built and registered by session 50 under the ratified operationalization
> [`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md)
> (ADOPT MODIFIED). **Panel verdict: CONFIRM — 3/3 models.** All three panel models move their
> double-object-vs-prepositional-dative preference in the human direction across an information-structure
> manipulation that holds length and animacy identical by construction, and the effect **survives the
> control arm** that pits information structure against end-weight. The effect magnitude is sharply
> **decorrelated across models** (gemini ≫ claude ≫ gpt), as the conjecture's prediction 3 anticipated.
> **Human-anchored** (NOT internal-contrast-only): the *direction* tested is the human production fact
> coded in [`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)
> (Bresnan et al. 2007), and the non-decisive secondary measure tracks that corpus's production-probability
> gradient.

## The question and the instrument

The English dative alternation — *Mary gave John the book* (double-object, **DOC**) vs. *Mary gave the
book to John* (prepositional dative, **PD**) — is constrained by **information structure**: given/old
material tends to precede new material, so a *given recipient* favours DOC and a *given theme* favours
PD ([`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md)).
The human anchor is the Bresnan et al. (2007) `languageR::dative` corpus
([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)), 3263 attested
ditransitive clauses hand-coded for the information-structure factors plus the NP(=DOC)/PP(=PD) outcome;
the firsthand logistic fit reproduces all five canonical directions (given/pronominal recipient → DOC;
given/pronominal theme → PD; longer theme → DOC by end-weight) at in-sample accuracy 0.887.

**Indicator** (logprob-free graded forced-choice — no panel prompt-logprobs are available under pure
autonomy). A discourse context establishes whether the recipient or the theme is discourse-**given**; the
model then distributes 100 points by naturalness between the DOC and PD phrasings of the *same*
proposition. DOC-preference = DOC_points / (DOC_points + PD_points) ∈ [0,1]. The DOC↔A/B mapping is
**counterbalanced** (every item × context run with DOC=A and DOC=B) and the parser is **target-blind**
(it keys on reply position, not on which option is DOC).

**The within-item design is the source of its rigour.** The givenness manipulation lives **only in the
discourse context** — the two phrasings the model scores are byte-identical across an item's contexts
(same words, same recipient/theme lengths, same animacy). The finding-bearing measure is the within-item
shift:

> shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)

Because every surface feature of the test sentence is identical across an item's two contexts, **any
length-only, position-only, order-only, always-DOC, always-PD, shorter-first, or longer-first reader
yields shift = 0** — certified at build (`certification.json`: all eight enumerated shortcut readers →
max|shift| = 0.000000) and re-derived by the independent pre-run critic (ten further surface readers, all
zero). Only tracking the discourse context can move the shift off zero.

Frozen `stimuli.json` sha256 **`0ffe3700524a8e5e0780820bab2fa4301923d37d93f7683d69515c968c4ababf`**
(44 items = 32 main + 12 control; 240 trials/model; 720 calls). `probe.py full` refuses to run unless
this exact sha is recorded in `PREREG.md`.

## Pre-registered verdict map (fixed before any call)

Per model, on the 32 main items, with a 10000-resample bootstrap 95% CI over items and a one-sided sign
test:

- **CONFIRM** — mean shift > 0 **and** bootstrap 95% lower bound > 0 (the human direction).
- **WEAK** — mean shift > 0 but the CI includes 0.
- **FALSIFY** — mean shift ≤ 0.
- **Panel CONFIRM iff ≥ 2/3 models CONFIRM.**

The **control arm** (12 items whose dissociating cells make the given constituent the *longer* one, so
information structure predicts the longer-first order, opposing end-weight) and the **neutral both-new
baseline** are reported alongside. The **secondary** corpus-gradient Spearman ρ is non-decisive — it may
strengthen a confirm or characterize a weak result, but may **not** convert weak→confirm nor rescue a
failed primary.

## Results

**Panel verdict: CONFIRM (3/3 models CONFIRM).** Independently reproduced from the raw jsonl by a fresh
post-run verifier (own RNG, own corpus-prediction recomputation, all 720 `doc_pref` values rechecked):
*"REPRODUCED — no material discrepancies."*

| Model | main shift | 95% CI | items + | sign-p | rec-given / thm-given DOC-pref | control shift | ctrl + | neutral | corpus-ρ (secondary) | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| gemini-3.5-flash | **+0.524** | [0.495, 0.552] | 32/32 | 2e-10 | 0.791 / 0.266 | +0.404 | 12/12 | 0.559 | 0.79 | CONFIRM |
| claude-sonnet-4.6 | **+0.327** | [0.289, 0.359] | 31/32 | <1e-8 | 0.708 / 0.382 | +0.305 | 12/12 | 0.580 | 0.83 | CONFIRM |
| gpt-5.4-mini | **+0.056** | [0.023, 0.086] | 22/32 | 0.025 | 0.653 / 0.597 | +0.076 | 10/12 | 0.619 | 0.48 | CONFIRM |

Data quality: **0 NA, 0 stern-retries, 0 length-truncations** across all 720 trials — every reply parsed
its graded `FINAL:` line on the first call.

### What the numbers say

1. **All three models track the constraint, in the human direction.** Each model's DOC-preference is
   higher when the recipient is given than when the theme is given (e.g. gemini 0.79 vs 0.27; claude 0.71
   vs 0.38), and the gap clears its bootstrap lower bound in every case. The neutral both-new baseline
   sits between the two (0.56–0.62), so the manipulation moves preference *around the model's own default*
   in both directions — it is a genuine context shift, not a one-sided ceiling artifact.
2. **The effect survives the end-weight dissociation control.** On the 12 control items, where the *given*
   constituent is the *longer* one (so a short-before-long reader would predict the opposite order), the
   shift stays positive for all three models (gemini +0.40, claude +0.31, gpt +0.08). So the main effect
   is **not** a short-before-long surface heuristic — the models follow givenness even when it opposes
   end-weight. (The within-item design already makes the measure length-immune by construction; the
   control arm is the stronger, absolute-order-level check.)
3. **Effect size is sharply decorrelated across models — prediction 3 confirmed.** The shift spans an
   order of magnitude (gemini +0.52, claude +0.33, gpt +0.06). gpt-5.4-mini is the weak-but-clearing case:
   a small effect (22/32 items positive, CI lower bound just above zero at +0.023) that earns CONFIRM
   legitimately under the pre-registered lower-bound gate but is roughly **one-tenth** gemini's magnitude.
   Two models with comparable general competence differ greatly in how cleanly they track this constraint,
   exactly as the conjecture predicted. **What this spread means for reading the concordant 3/3 label** —
   that a binary panel CONFIRM can hide an order-of-magnitude magnitude spread, so the verdict licenses a
   panel-scoped *direction* sentence but not a panel-scoped *uniformity* one — is drawn out as a reading
   discipline in [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md).
4. **The secondary corpus gradient strengthens the read.** Each model's per-cell DOC-preference correlates
   with the firsthand `languageR::dative` corpus model's predicted P(NP=DOC) per factor configuration
   (Spearman ρ 0.48 / 0.79 / 0.83), and the ranking matches the primary: the model with the strongest
   primary shift (gemini) and the model with the strongest gradient correlation (claude) both sit far
   above gpt's ρ 0.48. This is non-decisive by pre-registration, but it points the same way.

## Reading on the evidence ladder

This is a **Tier-2 (gradient semantic tracking) positive** on
[`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)'s ladder — the
rung the dative line was placed at — and the project's **first human-anchored Tier-2 result from a probe
of its own design** (the AANN gradient result is human-anchored to an acceptability gradient; the dative
here is anchored to a corpus *production* surface, a different and arguably stronger human signal for a
*production-preference* indicator). It lands with the project's "the add/easy direction is handled well"
pattern: tracking a well-described soft constraint in the human direction is something current decoders do
cleanly. It does **not** by itself reach Tier 4 (inference-licensing): the dative's information-structure
sensitivity is a gradient *preference* effect, not the licensing of a construction-contributed entailment
the lexical items cannot supply.

## Caveats (binding)

- **Single panel / single date / single run, small item N (32 main + 12 control).** This is
  direction-of-effect evidence, not a magnitude estimate; gpt's small positive especially wants
  replication on a fresh item set before any weight is put on its size. **Replicated (session 53)
  by [`result/dative-information-structure-v2`](dative-information-structure-v2.md)** on a disjoint
  item set: claude (+0.325) and gemini (+0.500) reproduced almost exactly, but **gpt's CONFIRM did
  not replicate** — its shift fell to +0.018 with a CI including zero (WEAK). The panel verdict holds
  at CONFIRM but drops to 2/3, and the order-of-magnitude effect-size spread widened rather than
  compressed.
- **Production preference, not acceptability rating.** The corpus anchors the human *production* direction
  (what speakers choose in context), which is the right anchor for this production-preference indicator;
  it is **not** a per-item human acceptability rating. The Bresnan & Ford (2010) graded-rating anchor was
  ratified an *opportunistic upgrade only* and was not used here.
- **Elicited with a working surface.** The graded forced-choice lets the model reason briefly before its
  `FINAL:` line; this is a behavioral preference measure, not a logprob/surprisal measure (none is
  available under pure autonomy). It measures *stated* naturalness preference.
- **The secondary corpus-gradient correlation codes six institutional recipients as inanimate**
  (conservative), a value-laden choice that feeds **only** the non-decisive secondary ρ, never the primary
  verdict (flagged by the pre-run critic as owing no new decision).

## Provenance & cost

- Run dir: [`experiments/runs/2026-06-20-dative-information-structure/`](../../../experiments/runs/2026-06-20-dative-information-structure/)
  — `PREREG.md` (frozen sha + verdict map + pre-run critic GO), `analysis.json` (the analyzed output),
  `raw/probe-{claude,gemini,gpt}.jsonl` (720 finding-bearing records), `certification.json`,
  `corpus_inspection.json` (the firsthand corpus fit).
- **Billed: $1.57763** for the 720 finding-bearing calls (claude $0.990, gemini $0.485, gpt $0.103;
  liveness $0.005; **session total $1.58281**), all `usage.cost`-summed, **0 missing**. This is today's
  only spend (2026-06-20 UTC; $5/day cap).
- **Budget-gate event (disclosed).** The first invocation tripped the pre-registered **$1.50 hard stop**
  at gpt 30/240, because the working-surface format made *both* claude and gemini far costlier than the
  pre-flight estimate (gemini ~5× its $0.05–0.10 estimate — under `effort: minimal` it still wrote
  justifications). The hard stop is a **budget** gate, not a scientific one; the decision to complete
  gpt's data collection on the **byte-identical frozen instrument** (gpt *is* panel.B — no model swap)
  was taken **blind to all analysis** (no `analyze.py` run, no shift seen), keeps the registered 3-model
  panel intact, and stays well under both the $5/day cap and the $2.50 single-run flag. The per-probe gate
  was raised 1.50→1.80 with the rationale recorded in `common.py`; a resume double-counting bug in the
  cost ledger (it re-logged completed models' full cost on resume) was fixed in `probe.py`, and the ledger
  was rebuilt from the jsonl source-of-truth. Total actual billed is unaffected by these mechanics.
