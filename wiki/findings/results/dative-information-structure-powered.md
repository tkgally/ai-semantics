---
type: result
id: dative-information-structure-powered
title: Dative information-structure, powered re-run — the magnitude+interval owed the claim, on 100 fresh disjoint main items; PANEL CONFIRM 3/3, and gpt's v2 WEAK does NOT hold at power (its shift clears zero at +0.056 [0.039, 0.074], recovering its v1 value), while the order-of-magnitude effect-size spread reproduces (~9×, like v1)
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-04
updated: 2026-07-05
links:
  - rel: depends-on
    target: conjecture/dative-alternation-information-structure
  - rel: anchors
    target: resource/languageR-dative-corpus
  - rel: refines
    target: result/dative-information-structure-v2
  - rel: supports
    target: claim/dative-information-structure-givenness
  - rel: supports
    target: essay/concordant-verdict-hides-spread
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/constructional-meaning-in-llms
---

# Result: the dative alternation tracks information structure — POWERED re-run (100 main items)

> **Status: proposed (2026-07-04, session 175).** The **owed A2a powered re-run**
> ([`PROTOCOL.md §4`](../../../PROTOCOL.md); program A2a "dative information-structure `[ ]`") of the
> dative **givenness** information-structure line. It re-runs the byte-frozen v1/v2 instrument on a
> **fresh, disjoint, powered item set** — 100 newly authored main items + 12 new control items, 0
> shared `(subject, recipient, theme)` items and **0 shared context sentences** with v1 or v2 —
> under the *same* ratified operationalization
> ([`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md),
> ADOPT MODIFIED). No new decision owed. Its purpose is to **attach a magnitude+interval** to
> [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)
> (promoted direction-only at s174, magnitude deferred here), exactly as
> [`result/comparative-correlative-covariation-powered`](comparative-correlative-covariation-powered.md)
> (s169, 136 items) did for the CC claim. **Panel verdict: CONFIRM — 3/3 at powered N.** The headline
> surprise: **gpt's v2 WEAK does not hold at power** — on 100 fresh items gpt's shift is **+0.056
> [0.039, 0.074]**, clearing zero and **recovering its v1 value (+0.056)**, so v2's dip to +0.018
> reads as founding-N item noise, not a stable gpt insensitivity. At the same time the
> **order-of-magnitude effect-size spread reproduces** (gemini +0.524 ≫ claude +0.316 ≫ gpt +0.056; a
> gemini-to-gpt ratio of **≈9.3×**, matching v1's ≈9× — **not** v2's inflated ≈27×), so a *3/3
> concordant* label at powered N **still hides a ~9× magnitude spread and a member (gpt) that flickered
> below detection at founding N** — a sharper, not weaker, vindication of
> [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md). **Human-anchored**
> to the same Bresnan et al. (2007) `languageR::dative` production surface.

## What was run, and why

The claim was promoted at s174 on a **direction-only** scope, scoped **2/3** (claude + gemini robust;
gpt's v1 CONFIRM (+0.056) had not replicated in v2, falling to +0.018 with a bootstrap CI that
included zero → WEAK). Two things were explicitly **owed**: (1) a **powered magnitude+interval**
([`PROTOCOL.md §4`](../../../PROTOCOL.md): ~100–150 items), which the founding N (32 main) could not
supply; and (2) a fresh-item re-test of the **2/3 pattern** — was gpt's WEAK a stable fact or a
small-N artifact? This run answers both at **N = 100 main items** (~3× founding, ~10× the founding-era
micro-N).

The instrument is **byte-for-byte** the v1/v2 design: a discourse context establishes whether the
recipient or the theme is discourse-**given**; the model distributes 100 points by naturalness between
the double-object (DOC) and prepositional-dative (PD) phrasings of the *same* proposition; the two
phrasings are **identical across an item's two contexts**, so the within-item shift
`shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)` is immune to any
length-only / position-only / order-only / always-DOC / always-PD / shorter-first / longer-first reader
**by construction**. Certification PASS (all eight enumerated shortcut readers → max |shift| = 0); an
**independent fresh-agent pre-run critic** re-derived shortcut-proofness with **seven** of its own
surface readers (all 0), verified every binding condition, full item- and context-disjointness from
v1/v2, the analysis's bias against a free positive, and the budget gate, and returned **GO**. A
non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`) **dissented NO-GO and was weighed and
rebutted** (its GO-condition — a frozen model roster and a fixed panel rule that cannot be altered post
hoc — is already satisfied by the standing ratified panel and the byte-identical frozen verdict map;
see `PREREG.md`).

Frozen `stimuli.json` sha256 **`6df9a7df94236495e3551589697364326df1557f1875640e4c32b879aaf65aa1`**
(112 items = 100 main + 12 control; 648 trials/model; 1944 calls). The human anchor — the firsthand
`languageR::dative` logistic fit (`corpus_inspection.json`, in-sample accuracy 0.887, all five
canonical directions reproduced) — is the same corpus as v1/v2; only the synthetic stimuli are new.

## Results

**Panel verdict: CONFIRM (3/3 models CONFIRM).** Recomputed from the raw jsonl by a fresh post-run
verifier (own bootstrap; doc-pref reconstructed from `a_points`/`b_points`/`doc_is_a` rather than
trusting the recorded field; all 1944 rechecked): **VERIFIER: REPRODUCED — no material discrepancy.**

Main within-item shift `shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)`,
per model, with a 10 000-resample bootstrap 95% CI over the **100 main items** and a one-sided sign
test (verdict map fixed before any call: CONFIRM iff mean shift > 0 **and** bootstrap lower bound > 0):

| Model | main shift | 95% CI | items + | sign-p | rec-given / thm-given DOC-pref | neutral | control shift | ctrl + | corpus-ρ (secondary) | verdict | v1 / v2 verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gemini-3.5-flash | **+0.524** | [0.506, 0.542] | 100/100 | <1e-9 | 0.785 / 0.261 | 0.577 | +0.443 | 10/12 | 0.85 | CONFIRM | CONFIRM / CONFIRM |
| claude-sonnet-4.6 | **+0.316** | [0.298, 0.334] | 100/100 | <1e-9 | 0.705 / 0.389 | 0.593 | +0.338 | 12/12 | 0.85 | CONFIRM | CONFIRM / CONFIRM |
| gpt-5.4-mini | **+0.056** | **[0.039, 0.074]** | 63/100 | 0.006 | 0.652 / 0.596 | 0.637 | +0.113 | 10/12 | 0.36 | **CONFIRM** | CONFIRM / **WEAK** |

Data quality: **0 NA, 0 stern-retries on gemini/gpt (3 on claude, all re-parsed cleanly), 0
length-truncations** across all 1944 trials — every reply parsed its graded `FINAL:` line (matching
v1/v2's clean data).

### What the numbers say

1. **The two strong members replicate for the third time at near-identical magnitude, now at power.**
   claude's main shift is **+0.316** (v1 +0.327, v2 +0.325) and gemini's is **+0.524** (v1 +0.524, v2
   +0.500) — all within a few thousandths of their prior values, both **100/100** items positive, both
   clearing their bootstrap lower bound by a wide margin, both surviving the end-weight dissociation
   control (claude 12/12, gemini 10/12). The powered CI is **~1.9× tighter** than the founding-N CI
   (claude [0.298, 0.334], width 0.036, vs v2's width 0.076). For these two models the dative
   information-structure capacity is a **thrice-observed, powered, human-direction-anchored Tier-2
   positive** with a magnitude and interval.
2. **gpt's v2 WEAK does NOT hold at power — its effect clears zero and recovers its v1 value.** On 100
   fresh items gpt's main-arm shift is **+0.056** with a bootstrap 95% CI of **[0.039, 0.074] that
   excludes zero** → **CONFIRM** under the pre-registered gate. This is **the same +0.056 gpt returned
   in v1**, so v2's dip to +0.018 (CI included zero) reads as **founding-N item-set noise on a genuinely
   tiny effect**, not a stable gpt insensitivity. gpt is only **63/100** items positive (vs claude/gemini
   100/100) and its sign-test p is 0.006 — a real but *weak and item-noisy* effect that a 32-item set can
   miss (v2) and a 100-item set detects (v1 caught it too, at the same size). The honest revision: **gpt's
   dative givenness effect is real but ~9× smaller than gemini's and small enough to flicker below
   detection at founding N.**
3. **The order-of-magnitude spread reproduces and does NOT compress.** The main-arm shift again spans an
   order of magnitude — gemini +0.524 ≫ claude +0.316 ≫ gpt +0.056 — a gemini-to-gpt ratio of **≈9.3×**.
   Crucially this **matches v1's ≈9×**, so v2's inflated ≈27× was itself the small-N artifact (driven by
   gpt's v2 dip), and the true spread is stable at ~9×. This is the essay's sharpest demonstration yet:
   even a **3/3 concordant CONFIRM at powered N** hides a ~9× magnitude spread and a member whose effect
   flickered WEAK at founding N. Reading the per-model magnitudes (as
   [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md) prescribes),
   not the panel label, is exactly what keeps this honest — the concordant 3/3 label alone would have
   erased both the spread and gpt's fragility.
4. **The effect is bidirectional around the neutral baseline, at power, for the strong members.** The
   shift moves preference in *both* directions off the model's own neutral both-new default — claude
   given-rec/given-theme 0.705 / 0.389 against neutral 0.593; gemini 0.785 / 0.261 against 0.577 — a
   genuine bidirectional context shift, not a one-sided ceiling artifact. gpt's cells (0.652 / 0.596
   against 0.637) barely separate, consistent with its tiny magnitude.
5. **The control arm survives the end-weight dissociation at power.** On the 12 dissociating control
   items (the given constituent made the *longer* one, so information structure predicts the longer-first
   order, *opposing* end-weight) the shift stays positive for all three (claude +0.338 12/12, gemini
   +0.443 10/12, gpt +0.113 10/12). The main effect is not a short-before-long heuristic. (The control
   arm is reported, not decision-bearing; it may not rescue a failed primary — none failed.)
6. **The secondary corpus gradient tracks the primary, same ranking as v1/v2.** Each model's per-cell
   DOC-preference correlates with the firsthand `languageR::dative` predicted P(NP=DOC) (Spearman ρ 0.85
   / 0.85 / 0.36 for gemini / claude / gpt), the same ordering as before (gpt far below). Non-decisive by
   pre-registration; it points the same way.

## Reading on the evidence ladder

This **refines** v1/v2's Tier-2 (gradient semantic tracking) positive on
[`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)'s ladder
*(Superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
— cited here as the edition this page engaged.)*, and it
**tightens the panel reading rather than narrowing it**: v2 had narrowed "all three track it" to "two of
three robustly," but the powered re-run shows the third member's effect **is** real (clears zero at N=100,
matching v1) — just an order of magnitude smaller. So the accurate statement is *"all three panel models
shift in the human-attested direction, but the magnitudes decorrelate by ~9× and the smallest (gpt) is
small enough to flicker below detection at founding N."* This is the project's recurrent **add/easy-direction**
pattern — a soft, well-described constraint handled cleanly by the more capable decoders and *weakly but
really* by the third — now measured with intervals. It does **not** reach Tier 4 (inference-licensing): the
effect is a gradient *preference*, not the licensing of a construction-contributed entailment.

## Caveats (binding)

- **Still single-lab, single-date-per-version, single-run-per-version.** Powered N (100 main) is a real
  strengthening — a magnitude with a tight interval on fresh items — but this is not a multi-date time
  series, and the panel is three specific model versions. Three decoders converging is weak evidence on
  its own; the human corpus direction is what gives the result independent bearing.
- **gpt's CONFIRM is a *tiny* effect that clears zero, not a strong one.** +0.056 [0.039, 0.074], 63/100
  items positive. The honest statement is that gpt's information-structure shift is **real but an order of
  magnitude below gemini's and item-noise-sensitive at small N** — it CONFIRMs at N=100 and at v1's N=32,
  and missed at v2's N=32. It is *not* claimed to be robust in the sense claude and gemini are.
- **Production preference, not acceptability rating; elicited with a working surface.** As in v1/v2: the
  corpus anchors the human *production* direction (the right anchor for a production-preference indicator),
  not a per-item human acceptability rating; the graded forced-choice measures *stated* naturalness
  preference, not logprob/surprisal (none available under pure autonomy).
- **The secondary corpus-gradient ρ codes six institutional recipients as inanimate** (conservative), a
  value-laden choice feeding **only** the non-decisive ρ, never the primary verdict — unchanged from
  v1/v2.
- **The UTC budget day straddled midnight.** The finding-bearing calls began ~2026-07-03T21:55 UTC and the
  billing rows landed 2026-07-04T00:06–00:40 UTC; the spend books to the 2026-07-04 UTC ledger (a fresh
  day), with only the $0.005 liveness on 2026-07-03. Both UTC days stay far under the $5/day cap.

## Provenance & cost

- Run dir: [`experiments/runs/2026-07-03-dative-information-structure-powered/`](../../../experiments/runs/2026-07-03-dative-information-structure-powered/)
  — `PREREG.md` (frozen sha + verdict map + pre-run critic GO rationale + non-Anthropic dissent-and-rebuttal),
  `build_trials.py` + `certification.json` (the fresh stimuli and their shortcut-proof certification),
  `analysis.json`, `raw/probe-{claude,gemini,gpt}.jsonl` (1944 finding-bearing records),
  `corpus_inspection.json` (the firsthand corpus fit, shared with v1/v2).
- **Billed: $4.32373** finding-bearing (claude $2.784, gemini $1.255, gpt $0.285), all `usage.cost`-summed,
  **0 missing** — under the pre-registered **$4.65 hard stop** and under the ~$4.22 pre-flight's ceiling
  (per-call ran ~$0.00222). Plus $0.00495 liveness (2026-07-03). Day total 2026-07-04 UTC = **$4.324 of
  $5.00** (the day's only spend); 2026-07-03 UTC carried $0.1142 prior + $0.005 liveness = $0.1192.
