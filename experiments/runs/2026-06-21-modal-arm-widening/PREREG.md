# PREREG — modal-arm-widening probe (session 71, 2026-06-21)

**Frozen before any model output.** Freezes the stimulus set, the indicator, and the analysis for
the modal-arm-widening follow-up to
[`result/function-word-swap-run-v2`](../../../wiki/findings/results/function-word-swap-run-v2.md),
firing revision trigger (a) of
[`essay/function-words-not-one-category`](../../../wiki/findings/essays/function-words-not-one-category.md).
Design rationale + arm table: `README.md`. Reuses the ratified instrument + matching discipline
([`decisions/resolved/function-word-anchor-design`](../../../wiki/decisions/resolved/function-word-anchor-design.md))
and the ratified inventory-widening method
([`decisions/resolved/function-word-count-vs-matching`](../../../wiki/decisions/resolved/function-word-count-vs-matching.md)).
**No new operationalization decision is owed** (confirmed by the independent pre-run critic, below).

## Frozen stimulus set

- `stimuli.json` **file sha256** (probe.py freeze-guard checks this):
  `cccac581b39b14c394565bc85efec5774073a5079f6b58a75598645ee8b67960`
- `stimuli.json` **canonical payload sha256** (build.py / certification.json `stimuli_sha256`):
  `fb605ed9863bcd877778e6b4a9cd8b39df551e64272aa67ef37fd7915fb7c28a`
- **118 matched items**, 4 content semantic classes (adj, noun_person, noun_thing, verb), 5 arms:
  - **Modal sweep:** `will`→`would` (future→conditional, n=20, REUSE run-v2 — replication of the
    null), `shall`→`should` (deontic obligation→advisory, n=18, NEW), `must`→`might` (deontic
    necessity→epistemic possibility, n=20, NEW).
  - **In-run positive controls:** `some`→`every` (existential→universal, n=28, REUSE),
    `because`→`although` (causal→concessive, n=32, REUSE — also supplies the adj class).
- `certification.json` `"ok": true`, 0 fails. Freq-only and length-only shortcut-reader
  max-positive threshold asymmetry both **0.0**; monotone pooled (func_gap−content_gap) = −0.0527
  (content-favoring, conservative). Every content pair's |ΔLg10WF| gap ≥ its arm's function gap.
- The NEW modal arms use an **"is required to {verb}"** hypothesis: `shall`/`must` ≈ required (base
  ENT=0), `should` (advisory) / `might` (possibility) ≠ required (fn NEU=1). `will`→`would` uses
  run-v2's "is going to {verb}" hypothesis (base ENT=0, fn NEU=1).

## Indicator (sole confirm/weak/falsify-bearing test)

3-way NLI entailment-flip rate (instrument REUSED VERBATIM from the CxNLI / conative-cancel line;
0=ent, 1=neu, 2=con; single-digit output). Per matched item, 3 calls per model: (premise_base,
hyp_base)→base; (premise_fn, hyp_base)→flip_fn; (premise_ct, hyp_ct)→flip_ct. **`flip_fn` is
direction-agnostic** (any label change vs base); the predicted labels feed only the diagnostic
manipulation checks, never the flip rate. PRIMARY readout = the **per-arm `flip_fn`** for the three
MODAL arms vs the two positive-control arms (`analyze.py` `per_function_type`, `modal_arm_flip_fn`,
`control_arm_flip_fn`). The pooled contrast/verdict are SECONDARY (this is a per-arm
characterization, not a conjecture re-test). Bootstrap 95% CI seed 20260621.

**The question (essay trigger a):** does the `will`→`would` modal null GENERALIZE across modal
types? If `shall`→`should` and `must`→`might` are ALSO near-null while the positive controls flip,
the essay's "modals are NLI-invisible" reading **strengthens** to a type-level fact. If some modal
arm flips strongly, the reading **narrows** (will→would was idiosyncratic).

## Panel

A = anthropic/claude-sonnet-4.6, B = openai/gpt-5.4-mini, C = google/gemini-3.5-flash
(gemini `reasoning:{effort:"minimal"}`), temperature 0.

## Pre-flight budget

118 matched × 3 × 3 = 1,062 finding-bearing NLI calls + 3 liveness. Estimate **~$0.28–0.40 billed**
(run-v2: 1,914 calls = $0.502). `ABORT_USD` = $1.00. Under the $2.50 single-run flag; UTC-2026-06-21
headroom at session start $5.00 − $2.467 = **$2.533**. Record actual billed `usage.cost` after.

## Falsify arm (binding)

`analyze.py`'s `FALSIFY: contrast ≤ 0` stays live per arm (content flip ≥ function flip = a positive
for the distributional camp). The content swap is applied CONSISTENTLY in premise AND hypothesis
(biases toward the null). No item added or dropped after the first probe call (`probe.py
require_frozen()`).

## PRE-RUN CRITIC: GO

An independent fresh-agent pre-run critic (2026-06-21) reproduced the build byte-for-byte (canonical
sha `fb605ed9…` matched; file sha `cccac581…`), ran its own **9001-point fine-θ shortcut-reader
sweep** over [−0.2, 1.6] and found **freq-only and len-only max-positive asymmetry = 0.00000** (0 gap
violations / 118, 0 length violations / 118), confirmed minimal-pair integrity (0/118 failures, no
modal leak into any hypothesis), spot-checked all 18 `shall` + all 20 `must` predicted labels as
sound/defensible, confirmed **no new decision is owed** and `internal-contrast-only` is correct, and
confirmed the design is not gerrymanderable (the headline `flip_fn` is direction-agnostic, so the
predicted labels cannot corrupt the primary number). **VERDICT: GO.**

**NITs the result write-up + post-run verifier MUST disclose:**

1. **Per-arm base-label agreement (with teeth).** The pooled `manip_base_label_agreement` could mask
   a `shall`-specific base collapse (`shall` read as plain future, not deontic → "shall buy →
   required to buy" becomes NEU not ENT). `analyze.py` now emits `base_label_agreement` **per arm**
   (added pre-run, post-GO, in response to this NIT — diagnostic only, stimuli sha unchanged). The
   verifier must report `shall`/`must` per-arm base agreement from raw; if `shall` base agreement is
   low, its flip is **uninterpretable** and must be reported as such, NOT as evidence the null
   generalizes.
2. **`shall` modal-reading caveat.** The `shall`→`should` ENT depends on a deontic (legal) reading of
   `shall`; a future reading weakens it (gated on NIT 1).
3. **`shall` single-content-pair thinness.** All 18 `shall` items rest on one content pair
   (`buy`→`give`); `must` carries three (`find`/`call`→`leave`, `put`→`move`); `will` two. Same
   Option-A supply ceiling run-v2's arms carried (`matching-report.json` `single_out_word_classes`).
4. **`must` flavor cross.** `must`→`might` crosses deontic→epistemic (necessity→possibility): a
   strength contrast *with* a flavor cross, not a pure-strength manipulation.
