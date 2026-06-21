# PREREG — function-word-vs-content-word swap probe (BUILD-v2, session 69, 2026-06-21)

**Frozen before any model output.** This pre-registration freezes the stimulus set, the
indicator, and the analysis for the probe of
[`conjecture/function-word-substitutability`](../../../wiki/findings/conjectures/function-word-substitutability.md),
under the ratified yardstick
[`decisions/resolved/function-word-anchor-design`](../../../wiki/decisions/resolved/function-word-anchor-design.md)
and the build-v2 resolution
[`decisions/resolved/function-word-count-vs-matching`](../../../wiki/decisions/resolved/function-word-count-vs-matching.md).

## Frozen stimulus set

- `stimuli.json` **file sha256** (probe.py freeze-guard checks this):
  `4763740e3da17e9f781d8d4c63b3522fb4789b1d14acc39e63964d095216f7d3`
- `stimuli.json` **canonical payload sha256** (build.py / certification.json `stimuli_sha256`,
  computed over the sorted payload before the `sha256` key is added):
  `1cfb287e62b82746c97fcc93439fc0f7f35a5dcf9935514a6aed3588b4a2f70c`
- **206 matched items** across **4 content semantic classes** (adj, noun_person, noun_thing, verb)
  + 10 `det_char` (the→a function-only characterizing arm, excluded from the primary matched contrast).
- Four function-word arms: `because`→`although` (subordinator, n=32), `some`→`every`
  (quantifier, singular, n=28), `will`→`would` (modal, n=20), `few`→`many` (quantifier, plural,
  the build-v2 inventory-widening pair, n=126). `many`→`every` was rejected (breaks number
  agreement: "many guards"→"every guards" is ungrammatical).
- `certification.json` `"ok": true`, 0 fails. Freq-only-reader and length-only-reader max
  POSITIVE threshold asymmetry both **0.0** (every content pair's |ΔLg10WF| gap ≥ its arm's
  function gap, so no surface-only reader can reproduce the function>content asymmetry); monotone
  pooled (func_gap−content_gap) = −0.047 (content-favoring, conservative).

## Indicator (sole confirm/weak/falsify-bearing test)

3-way NLI entailment-flip rate (instrument REUSED VERBATIM from the CxNLI / conative-cancel line;
0=entailment, 1=neutral, 2=contradiction; single-digit output). Per matched item, 3 finding-bearing
calls per model: (premise_base, hyp_base) → base label; (premise_fn, hyp_base) → flip_fn; (premise_ct,
hyp_ct) → flip_ct. PRIMARY (per model) = mean(flip_fn) − mean(flip_ct), bootstrap 95% CI over items
(seed 20260621). CONFIRM: contrast>0 AND bootstrap LB>0. WEAK: contrast>0, CI includes 0. FALSIFY:
contrast≤0 (content swap flips at least as much — a clean positive for the distributional camp).
Panel CONFIRM iff ≥2/3 models CONFIRM (count gate ≥200 / ≥4-class MET). Manipulation check: base-label
agreement with pred_base. The per-function-arm and per-class breakdowns are reported and must be read
(prediction 3: not driven by a few categories) — the `few` arm is 126/206 (61%), so the pooled
contrast must be checked against the per-arm contrasts.

## Panel

A = anthropic/claude-sonnet-4.6, B = openai/gpt-5.4-mini, C = google/gemini-3.5-flash
(gemini `reasoning:{effort:"minimal"}`).

## Pre-flight budget

206 matched × 3 + 10 det_char × 2 = 638 calls/model × 3 = 1,914 finding-bearing NLI calls + 3
liveness. Single-digit NLI outputs are cheap (cf. Scivetti CxNLI 1,170 calls = $0.33 billed).
Estimate **~$0.35–0.55 billed**. ABORT_USD single-run flag = $1.00 (probe.py). Well under the
$2.50 single-run prudence flag and today's UTC-2026-06-21 headroom ($5.00 − $1.964 already spent
= ~$3.04). Record actual billed `usage.cost` after.

## Falsify arm (binding)

`analyze.py`'s `FALSIFY: contrast ≤ 0` verdict is live (content flip rate ≥ function flip rate =
a positive for the distributional camp). The content swap is applied CONSISTENTLY in premise AND
hypothesis (biases toward the null). No item is added or dropped after the first probe call.

## PRE-RUN CRITIC: GO

Two independent fresh-agent pre-run critics reviewed this line. The FIRST returned **NO-GO** on the
first v2 freeze with two BLOCKERs: (1) certify.py's freq-only-reader θ grid was too coarse and
stepped over a +0.136 asymmetry peak at θ≈0.07; (2) the `few` arm reintroduced the v1 defect
(content pairs with |ΔLg10WF| gap below the arm's function gap). Both were fixed (grid rebuilt from
the actual gap values; every content pair's gap forced ≥ its arm's function gap — `some:man→guys`
dropped, `few:noun_thing` re-matched to `number/chance→problem`, `sit→play`→`sit→hold`), producing
this re-frozen set.

A SECOND, fully independent fresh-agent pre-run critic then reviewed the re-frozen set and returned
**VERDICT: GO** (2026-06-21). It reproduced the build byte-for-byte (internal sha
`1cfb287e…` matched), independently swept θ ∈ [0,1.6] at step 0.0005 plus just-below all 30 distinct
gap values and found freq-only-reader **max POSITIVE asymmetry = 0.000000** (≤0 at every θ, well
under the 0.12 yardstick), confirmed the structural guarantee (min content gap ≥ func gap in every
arm: because 1.4565≥1.4062, some 0.5107≥0.4976, will 0.1310≥0.0797, few 0.0766≥0.0758), confirmed
certify.py's gap-derived grid cannot step over a peak, verified len-only asymmetry 0.0, walked all
nine build-v2 conditions + parent (a)–(i) as PASS, and found minimal-pair integrity mechanically
perfect (0 fn-defects, 0 ct-defects, 0 hypothesis leaks). NITs (non-blocking, to weigh in the
result): the `few` arm is 126/206 (61%); six (function×class) cells rest on a single out-word
(because:*, some:noun_person, some:verb, will:verb), honestly reported in `matching-report.json`;
a few `few`-verb carriers are semantically thin — all neutralized as validity threats by the
consistent-content-swap design and made auditable by the per-arm breakdown.
