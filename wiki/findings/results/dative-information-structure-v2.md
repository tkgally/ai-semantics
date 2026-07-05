---
type: result
id: dative-information-structure-v2
title: Dative alternation tracks information structure — fresh-item replication holds the panel CONFIRM (2/3) but qualifies it; the order-of-magnitude effect-size spread reproduces and does not compress, and one model's v1 CONFIRM (gpt, +0.056) does not replicate (drops to WEAK, +0.018, CI includes 0)
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-06-20
updated: 2026-07-05
links:
  - rel: depends-on
    target: conjecture/dative-alternation-information-structure
  - rel: anchors
    target: resource/languageR-dative-corpus
  - rel: refines
    target: result/dative-information-structure-v1
  - rel: supports
    target: essay/concordant-verdict-hides-spread
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/constructional-meaning-in-llms
  - rel: supports
    target: claim/dative-information-structure-givenness
---

# Result: the dative alternation tracks information structure — fresh-item replication (v2)

> **Status: proposed (2026-06-20, session 53).** A **direct replication** of
> [`result/dative-information-structure-v1`](dative-information-structure-v1.md) (session 51) on a
> **fresh, disjoint item set** — 32 newly authored main items + 12 new control items, 0 shared
> `(subject, recipient, theme)` items and 0 shared discourse contexts with v1 — under the *same*
> ratified operationalization
> ([`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md),
> ADOPT MODIFIED). No new decision owed. **Panel verdict: CONFIRM — but 2/3, not v1's 3/3.** claude
> and gemini reproduce their effect almost exactly; **gpt's v1 CONFIRM does not replicate** — its
> main-arm shift falls to +0.018 with a bootstrap CI that includes zero (WEAK). **The order-of-magnitude
> effect-size spread reproduces and, if anything, widens at the bottom** (gemini ≈ 27× gpt), so the
> concordant-verdict reading discipline of
> [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md) is vindicated,
> not weakened. **Human-anchored** to the same Bresnan et al. (2007) `languageR::dative` production
> surface as v1.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The powered re-run
> ([`result/dative-information-structure-powered`](dative-information-structure-powered.md), s175:
> 100 fresh disjoint items on the byte-frozen instrument) **reversed this page's headline
> qualification**: at N=100 the panel is **CONFIRM 3/3**, and gpt's WEAK did **not** hold — its
> main-arm shift recovers v1's +0.056 with a CI clear of zero (+0.056 [0.039, 0.074]); this page's
> +0.018 dip is best read as founding-N item noise. The order-of-magnitude spread **does**
> reproduce (~9.3×, v1's 9×, not this page's 27×). The line was promoted s174 →
> [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)
> (magnitudes+intervals attached s175). *(Back-annotation: nothing measured on this page changes —
> the v2 numbers stand as this run's record.)*

## What was replicated, and why

v1 returned a **3/3 panel CONFIRM** on the within-item information-structure shift, but with the effect
size **sharply decorrelated across models** (gemini +0.524 ≫ claude +0.327 ≫ gpt +0.056). Two of v1's
own binding caveats motivated this replication: *"single panel / single date / single run, small item
N … gpt's small positive especially wants replication on a fresh item set before any weight is put on
its size,"* and revision trigger (c) of
[`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md) — *a replication
that **compresses** the spread would weaken the essay's "in strongest form" claim*. v2 tests both on
entirely new lexical material.

The instrument is byte-for-byte the v1 design: a discourse context establishes whether the recipient or
the theme is discourse-**given**; the model distributes 100 points by naturalness between the
double-object (DOC) and prepositional-dative (PD) phrasings of the *same* proposition; the two phrasings
are **identical across an item's two contexts**, so the within-item shift
`shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)` is immune to any
length-only / position-only / order-only / always-DOC / always-PD / shorter-first / longer-first reader
by construction. Certification PASS (all eight enumerated shortcut readers → max|shift| = 0); an
**independent fresh-agent pre-run critic** re-derived shortcut-proofness with fourteen of its own surface
readers (all 0), verified every binding condition, full item- and context-disjointness from v1, the
analysis's bias against a free positive, and the budget gate, and returned **GO**.

Frozen `stimuli.json` sha256 **`32d3e6225b328920d3612cd418a62cb61f34445dc55ee7e1a2841d9b9cddbf9b`**
(44 items = 32 main + 12 control; 240 trials/model; 720 calls). The human anchor — the firsthand
`languageR::dative` logistic fit (`corpus_inspection.json`, in-sample accuracy 0.887, all five canonical
directions reproduced) — is the same corpus as v1; only the synthetic stimuli are new.

## Results

**Panel verdict: CONFIRM (2/3 models CONFIRM).** Independently reproduced from the raw jsonl by a fresh
post-run verifier (own bootstrap, doc-pref reconstructed from `a_points`/`b_points`/`doc_is_a` rather than
trusting the recorded field; 720/720 rechecked): *"The raw per-call data independently reproduces the
run's headline … No verdict-changing or materially different number was found."*

| Model | main shift | 95% CI | items + | sign-p | rec-given / thm-given DOC-pref | control shift | ctrl + | neutral | corpus-ρ (secondary) | verdict | v1 verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gemini-3.5-flash | **+0.500** | [0.458, 0.537] | 32/32 | <1e-9 | 0.778 / 0.278 | +0.461 | 12/12 | 0.558 | 0.84 | CONFIRM | CONFIRM (+0.524) |
| claude-sonnet-4.6 | **+0.325** | [0.286, 0.362] | 32/32 | <1e-9 | 0.714 / 0.389 | +0.335 | 12/12 | 0.607 | 0.81 | CONFIRM | CONFIRM (+0.327) |
| gpt-5.4-mini | **+0.018** | [−0.011, 0.047] | 15/32 | 0.70 | 0.631 / 0.613 | +0.144 | 12/12 | 0.641 | 0.37 | **WEAK** | CONFIRM (+0.056) |

Data quality: **0 NA, 0 stern-retries, 0 length-truncations** across all 720 trials — every reply parsed
its graded `FINAL:` line on the first call (matching v1's clean data).

### What the numbers say

1. **The two strong members replicate almost exactly.** claude's main shift is **+0.325** (v1 **+0.327**)
   and gemini's is **+0.500** (v1 **+0.524**) — both within a few thousandths of their v1 values, both
   32/32 items positive, both clearing their bootstrap lower bound by a wide margin, both surviving the
   end-weight dissociation control 12/12. For these two models the dative information-structure capacity
   is **robust** across an entirely fresh stimulus set: a genuinely reproduced Tier-2 positive.
2. **gpt's v1 CONFIRM does not replicate.** On fresh items gpt's main-arm shift is **+0.018** with a
   bootstrap 95% CI of **[−0.011, 0.047]** that **includes zero** (15/32 items positive — a coin flip;
   sign-p 0.70). Under the pre-registered lower-bound gate this is **WEAK**, not CONFIRM. v1's gpt
   value (+0.056, lower bound just above zero at +0.023) was the panel's weakest CONFIRM and was flagged
   in v1's own caveats as the one *"especially want[ing] replication … before any weight is put on its
   size."* The replication shows that caution was warranted: gpt's effect is at best tiny and does **not**
   robustly clear zero.
3. **The order-of-magnitude spread reproduces and does not compress.** The main-arm shift again spans an
   order of magnitude and then some — gemini +0.500 ≫ claude +0.325 ≫ gpt +0.018 — a gemini-to-gpt ratio
   of ≈ **27×** (v1's was ≈ 9×). So
   [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)'s revision
   trigger (c) fires in the **strengthening** direction: a fresh-item replication did **not** compress the
   spread, and the essay's "in strongest form" reading of prediction 3 stands. More pointedly, v2 supplies
   the essay's sharpest demonstration to date: v1's **concordant 3/3 label hid a fragile member** — the
   one model whose CONFIRM did not survive replication. Reading the per-model magnitudes (as the essay
   prescribes), rather than the panel label, is exactly what would have flagged gpt's CONFIRM as the one
   to distrust.
4. **A reported wrinkle on gpt (not used to change the verdict).** gpt's **control-arm** shift is
   **+0.144** (12/12 items positive) — larger than its near-zero main-arm shift. Because the within-item
   shift is length-immune by construction in *both* arms, this says gpt shows a little more givenness
   tracking on the control items (which have long NPs) than on the length-matched main items. It is a
   small, real signal that gpt is not *wholly* context-insensitive — but the pre-registered **primary**
   test is the main arm, and the control arm may **not** rescue a failed primary (pre-registration). gpt
   is WEAK. The wrinkle is reported, not retuned.
5. **The secondary corpus gradient tracks the primary, same ranking as v1.** Each model's per-cell
   DOC-preference correlates with the firsthand `languageR::dative` predicted P(NP=DOC) (Spearman ρ
   0.84 / 0.81 / 0.37 for gemini / claude / gpt), the same ordering as v1 (gpt far below). Non-decisive
   by pre-registration; it points the same way.

## Reading on the evidence ladder

This **refines** v1's Tier-2 (gradient semantic tracking) positive on
[`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)'s ladder
*(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) —
cited here as the edition this result fed)*. The
*panel* verdict survives replication (CONFIRM, 2/3), and for **claude and gemini** the effect is now
twice-observed at near-identical magnitude on disjoint items — about as solid as a single-lab,
single-decoder behavioral result can be without a third date or a logprob channel. But the replication
**narrows what can be claimed about the panel as a whole**: v1's "all three models track it" becomes
"two of three track it robustly; the third's effect does not clear zero on fresh items." This is the
project's recurrent pattern — the soft, well-described constraint is handled cleanly *by the more capable
decoders* — sharpened by the observation that membership in "handles it cleanly" is itself model-specific
and not guaranteed to replicate. It does **not** reach Tier 4 (inference-licensing): the effect is a
gradient *preference*, not the licensing of a construction-contributed entailment.

## Caveats (binding)

- **Still single-lab, single-date, single-run per version, small item N (32 main + 12 control).** v2 adds
  a second date and a fresh item set — a real strengthening for claude and gemini — but it is not a
  multi-date time series, and the panel is three specific model versions.
- **gpt's WEAK is "does not clear," not "confirmed null."** The CI is [−0.011, 0.047]; the point estimate
  is positive. The honest statement is that gpt's information-structure shift is **too small to
  distinguish from zero on this fresh item set**, and that its v1 CONFIRM did not replicate — not that gpt
  is proven insensitive.
- **Production preference, not acceptability rating; elicited with a working surface.** As in v1: the
  corpus anchors the human *production* direction (the right anchor for a production-preference
  indicator), not a per-item human acceptability rating; the graded forced-choice measures *stated*
  naturalness preference, not logprob/surprisal (none available under pure autonomy).
- **The secondary corpus-gradient ρ codes six institutional recipients as inanimate** (conservative), a
  value-laden choice feeding **only** the non-decisive ρ, never the primary verdict — flagged by v1's
  pre-run critic as owing no new decision, and unchanged here.

## Provenance & cost

- Run dir: [`experiments/runs/2026-06-20-dative-information-structure-v2/`](../../../experiments/runs/2026-06-20-dative-information-structure-v2/)
  — `PREREG.md` (frozen sha + verdict map + pre-run critic GO rationale), `build_trials.py` +
  `certification.json` (the fresh stimuli and their shortcut-proof certification), `analysis.json`,
  `raw/probe-{claude,gemini,gpt}.jsonl` (720 finding-bearing records), `corpus_inspection.json` (the
  firsthand corpus fit, shared with v1).
- **Billed: $1.56053** for the run (claude $0.979, gemini $0.471, gpt $0.105; liveness $0.005;
  finding-bearing $1.55541), all `usage.cost`-summed, **0 missing**. Pre-flighted from v1's measured
  $1.578 (not the rate card); the pre-registered **$2.00 hard stop was never approached**. Day total
  2026-06-20 UTC (sessions 49–53) = **$3.144 of $5.00**.
