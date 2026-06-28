---
type: result
id: monotonicity-within-verbal-battery-v1
title: "Within-verbal matched add-vs-cancel battery — CONFIRMS the monotonicity asymmetry on a within-verbal (domain-matched, not surface-form-matched) contrast (both arms verbal): add licenses at uniform ceiling, the progressive suppresses only partially; asymmetry ≥0.20 in 3/3 models, leave-one-out robust at the verdict level, M2 domain mismatch DISCHARGED"
meaning-senses:
  - constructional
  - inferential
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: supports
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: result/monotonicity-causative-progressive-cancel-v1
  - rel: depends-on
    target: result/monotonicity-verbal-cancel-survey-v1
  - rel: refines
    target: result/monotonicity-c2-battery-v1
  - rel: depends-on
    target: concept/coercion
---

# Result: within-verbal matched add-vs-cancel monotonicity battery — a clean confirm, M2 discharged

> **The decisive within-verbal test, `internal-contrast-only`.** Pairs the frozen s135
> resultative **ADD** arm (verbatim, sha `80bd4b60b55a3e60`) with the s140 causative-inchoative
> progressive **CANCEL** arm — **both verbal** — in the matched conflicting-cue paradigm, read by
> the **frozen s134 thresholds** (ratified
> [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../decisions/resolved/constructional-monotonicity-generalization-operationalization.md);
> no new decision, no threshold tuned). Because both arms are verbal, a positive asymmetry here is
> the **clean within-verbal confirm that discharges the M2 verbal-add / nominal-cancel domain
> mismatch** the weak C2 confirm carried. Makes **no** human-comparison claim. Pre-registration,
> frozen items, every number:
> [`experiments/runs/2026-06-28-monotonicity-within-verbal-battery/`](../../../experiments/runs/2026-06-28-monotonicity-within-verbal-battery/README.md).

## Why this is the clean test

The s137 C2 battery ([`result/monotonicity-c2-battery-v1`](monotonicity-c2-battery-v1.md)) advanced
[`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
to `tested`, but only on a **weak** confirm bought across the **M2** mismatch (verbal resultative
ADD vs *nominal* taxonomic CANCEL), marginal in 2/3 models and leave-one-out-fragile (it fell to
1/3 if either borderline privative was dropped). Sessions 139–140 removed the compromise: s139
B2-confirmed a **verbal** held default (causative-inchoative result, NLI 1.00 3/3,
[`result/monotonicity-verbal-cancel-survey-v1`](monotonicity-verbal-cancel-survey-v1.md)) and s140
showed the **progressive** genuinely suppresses it
([`result/monotonicity-causative-progressive-cancel-v1`](monotonicity-causative-progressive-cancel-v1.md)).
This battery puts the two **verbal** arms in one paradigm.

## What was measured

Frozen set (items.csv sha256[:16] **`2c0d4f70f28bb1c4`**): **48 items = 30 add (verbatim s135) +
18 cancel** (6 causative-inchoative verbs × default/construction/cue). Matched conflicting-cue
paradigm: ADD control "Maria beat the cream." / construction "…the cream stiff." (`add_no_cue`) /
cue "…stiff, but the cream did not become stiff." (DENIAL); CANCEL default "Sam broke the vase."
(B2 anchor) / construction "Sam was breaking the vase." (`cancel_no_cue` = 1 − affirm) / cue "…the
vase, and the pieces scattered across the floor." (RE-ASSERTION). NLI primary + FC, temperature 0,
the ratified panel. 48 × 2 × 3 = **288 calls**. An independent fresh-agent **pre-run critic** GO
(verbatim ADD reuse diff-checked; thresholds un-tuned; falsification arms verified live by a
dry-run); an independent fresh-agent **post-run verifier** reproduced every cell + ran the
leave-one-out (exact match; 288/288 priced, 0 errors, 0 parse failures, cost matched).

## One-line finding

**The asymmetry CONFIRMS on a clean within-verbal contrast, in all three models: the ADD arm
licenses the constructional inference at a uniform ceiling (add_no_cue 1.00, 3/3) while the
progressive CANCEL arm suppresses the held result entailment only partially (cancel_no_cue
0.50 / 0.67 / 0.33), giving a positive add-minus-cancel asymmetry of +0.50 / +0.33 / +0.67 —
≥ 0.20 in 3/3 models (confirm 3, symmetric 0, reversal 0).** The B2 gate is GO (add construction
1.00 / control 0.00, cancel default 1.00, all 3/3), the instrument-fragility leg confirms 3/3
(cancel more NLI-vs-FC fragile than add), the cue re-licenses robustly (add and cancel cue-follow
both 3/3), and the verdict is **leave-one-out robust** (survives dropping any single cancel verb,
worst case 2/3). Because both arms are verbal, **the M2 domain mismatch is discharged** — this is
the clean within-verbal confirm the conjecture's generalization criterion demanded, and it is
materially stronger than the weak, domain-mismatched, LOO-fragile C2 confirm.

## Numbers (verified)

NLI primary; rates in [0,1]; n = 10 add verbs / 6 cancel verbs per condition per model.
Independently recomputed by the post-run verifier — exact match to `raw/results.json`.

| model | add_no_cue | add_control | cancel_default | cancel_no_cue | **asymmetry** | cue: add / cancel |
|---|---|---|---|---|---|---|
| A claude-sonnet-4.6 | 1.00 | 0.20 | 1.00 | 0.50 | **+0.50** | 1.00 / 0.83 |
| B gpt-5.4-mini | 1.00 | 0.10 | 1.00 | 0.67 | **+0.33** | 1.00 / 1.00 |
| C gemini-3.5-flash | 1.00 | 0.00 | 1.00 | 0.33 | **+0.67** | 1.00 / 0.83 |
| **verdict** | | | | | **CONFIRMS 3/3** | robust 3/3 & 3/3 |

- **B2 GATE: GO** — add construction 1.00, add control 0.00, cancel default 1.00 (calib subset, all
  3/3). M1: the cancel default-at-ceiling pass licenses reading the suppression shortfall as
  **defeasance** (the result is a held model entailment, not a never-held one — the s135 confound is
  closed).
- **Asymmetry (leg 1): CONFIRMS 3/3** (≥ 0.20 each; the threshold needs only ≥ 2/3).
- **Instrument-fragility (leg 2): CONFIRMS 3/3** (cancel NLI-vs-FC disagreement exceeds add's by
  ≥ 0.10 in every model — A +0.50, B +0.167, C +0.167).
- **Cue robust:** add cue-follow (withholds the denied inference) 1.00/1.00/1.00; cancel cue-follow
  (re-affirms under the explicit consequence) 0.83/1.00/0.83 — both ≥ 0.70 in 3/3.

## Leave-one-out (the robustness the C2 confirm lacked)

Dropping each cancel verb in turn and recomputing the per-model asymmetry, the **CONFIRMS verdict
(≥ 2/3) survives every single-verb drop** — worst case **2/3** (dropping `vase` or `window` pushes
gpt-5.4-mini to exactly 0.20, but claude and gemini carry it). This is sharply better than the C2
battery, which collapsed to 1/3 if either borderline privative was removed. The confirm does **not**
rest on any one verb.

## Per-verb cancel suppression (carried, not averaged away)

The partial suppression is uneven across verbs, reproducing the s140 finding (verifier-confirmed):

- **`vase` (break) and `tablet` (dissolve) suppress cleanly** (cancel-construction affirm 0 in most
  models).
- **`window` (shatter) resists in all three models under NLI** (the progressive read as
  already-culminated — a punctual achievement), and `snowman`/`page` resist in some.

So the asymmetry is carried by the ADD arm's *uniform ceiling* against the cancel arm's *partial,
verb-dependent* suppression — which is exactly the conjecture's content (constructional *addition*
is licensed uniformly; *defeasance* is partial and patchy). The model ordering is the honest
sharp edge: **gpt-5.4-mini sits nearest the 0.20 bar (asymmetry +0.33) precisely because it
suppresses the *most*** (4/6 cancel verbs; cancel_no_cue 0.667, the highest suppression of the
three), so its add-vs-cancel gap is the smallest — the best defeasance gives the smallest
asymmetry, as the conjecture predicts. **gemini suppresses the *least*** (2/6 verbs; cancel_no_cue
0.333) and so shows the largest asymmetry (+0.67); claude is in between (3/6; +0.50). Every model's
ADD arm is at 1.00, so the spread is driven entirely by how much each model defeases.

## What this does and does not license

- **Does:** deliver the **clean within-verbal confirm** of
  [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
  — both arms verbal, asymmetry ≥ 0.20 in 3/3, fragility 3/3, cue robust, leave-one-out robust at
  the verdict level. It **discharges the M2 domain-mismatch caveat**: the conjecture's `tested`
  status no longer rests only on a verbal-add / nominal-cancel contrast.
- **Does not** make a human comparison (`internal-contrast-only`) nor tune any threshold (frozen
  ratified s134 set; ADD arm byte-for-byte verbatim).
- **Carries honest caveats:** (1) suppression is **partial and verb-uneven** (`window` resists;
  gpt at the margin) — the cancel arm is a *defeasance shortfall*, not a clean cancel; (2) the add
  and cancel hypotheses are **domain-matched but not form-identical** — add predicates a copular
  result-state ("became stiff"), cancel an inchoative result ("the vase broke"); both predicate the
  affected object reaching its caused result, so the contrast is fair, but it is *verbal-domain*
  matched, not *surface-form* matched (a strictly weaker mismatch than the nominal/adjectival M2 it
  replaces); (3) small N, single run, three-model panel, `internal-contrast-only` (no human
  baseline) — the asymmetry is a within-model direction-of-effect, not a claim about people.

## What this means for the conjecture

The conjecture stays `tested`, but its support is now materially firmer: the generalization
criterion ("the asymmetry generalizes to a *new* add-vs-cancel pair at matched difficulty and
ceiling") is met by a **genuinely new verbal cancel construction** (the progressive, beyond the
original caused-motion / way / conative) on a **clean within-verbal contrast**, leave-one-out
robust. The standing M2 headline caveat is discharged. The falsification arms (symmetric / reversal)
were live and did **not** fire. What remains open is not the within-verbal generalization but the
deeper questions the conjecture always carried: human comparison (un-anchored by design here) and
whether the partial, verb-uneven suppression reflects defeasance *competence* or strict-NLI
*labeling* — the per-verb unevenness (punctual progressives read as culminated) is a live thread.

## Provenance

- Every figure is reproduced verbatim from `raw/results.json` and independently recomputed from the
  per-call `raw/*.json` by a read-only post-run verifier (exact match; 288/288 priced, 0 missing,
  0 parse failures; leave-one-out reproduced).
- The ADD arm is the s135 frozen resultative arm reused **byte-for-byte** (source sha
  `80bd4b60b55a3e60`, asserted at build); the CANCEL arm is the s140 frozen calibration strings
  (sha `5ba8a996fa70cf55`). The frozen s134 thresholds and the matched paradigm are the ratified
  yardstick ([`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md) template).
- Spend: **$0.06882 billed** (UTC 2026-06-28).
