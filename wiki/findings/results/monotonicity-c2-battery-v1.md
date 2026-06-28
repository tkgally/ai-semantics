---
type: result
id: monotonicity-c2-battery-v1
title: C2 matched add-vs-cancel monotonicity battery — a WEAK CONFIRM of the monotonicity asymmetry across a verbal-add/nominal-cancel domain difference; add licensing is at uniform ceiling, cancel (privative) suppression is partial and item/model-dependent
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
  - rel: refines
    target: result/monotonicity-c2-privative-calibration-v1
  - rel: refines
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: concept/coercion
---

# Result: C2 matched add-vs-cancel monotonicity battery — a weak, heavily-caveated confirm

> **The conjecture's decisive matched-difficulty test, finally run — `internal-contrast-only`.**
> STEP 2 of the ratified cancel-arm re-design. Reusing the s135 frozen resultative **ADD** arm
> verbatim and pairing it with the **C2 privative CANCEL** arm (B2-passing, STEP 1b), this is the
> first matched, ceiling-controlled battery the [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
> has had since its for-durative arm failed. Per the frozen reading rule it is a **CONFIRMS**
> (asymmetry ≥ 20 pp in 2/3 models; cancel more instrument-fragile in 2/3) — so the conjecture
> advances to **`tested`**. But the confirm is **weak and heavily caveated**: it spans a
> deliberate **verbal-add / nominal-cancel domain difference** (M2), it is marginal in 2 of 3
> models, and a leave-one-out shows it is **sensitive to single pre-flagged borderline items**.
> Pre-registration, run record, every number:
> [`experiments/runs/2026-06-28-monotonicity-c2-battery/`](../../../experiments/runs/2026-06-28-monotonicity-c2-battery/README.md).

## Why this ran, and what makes it fair (M1)

Three cancel-side defaults were B2-calibrated before this battery could be built: single-occurrence
(s135, floored 0.00), completion (C1, 0/3 at ceiling), and **category membership (C2, 1.00 in
3/3)**. Only C2 supplied a default the panel holds as a **categorical entailment at ceiling** —
the precondition the B2 gate exists to certify. **M1 (binding):** because the cancel default
("Sam bought a gun" ⊨ "Sam bought a weapon") cleared B2 at 1.00 in 3/3, a *failure to suppress* it
under a privative modifier can legitimately be read as **defeasance failure** — there is a real
held entailment to cancel, closing the s135 "the inference was never an entailment" confound. This
is exactly the discipline [`essay/nothing-to-cancel`](../essays/nothing-to-cancel.md) argued for.

## What was measured

Frozen battery (items.csv sha256[:16] **`4b823d3d48422eaf`**, committed before any probe):
**54 items** = 30 **ADD** (s135 resultative arm, reused **verbatim** — byte-for-byte, sha-checked
`80bd4b60b55a3e60`) + 24 **CANCEL** (C2 privative: 8 noun→category pairs × default/construction/cue).
Matched conflicting-cue paradigm; NLI primary + forced-choice; temperature 0; panel
claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash. The B2 gate was **re-run on the frozen
combined set = GO** (add construction 1.00 / control 0.00; cancel default 1.00; 3/3) before the
main run; an independent fresh-agent **pre-run critic** returned GO (and flagged `toy violin` as
the weakest-suppression item in advance); an independent **post-run verifier** recomputed every
cell and ran a leave-one-out.

Key cells (NLI primary): `add_no_cue` = add construction affirm (license); `cancel_no_cue` =
1 − cancel construction affirm (suppression). Asymmetry = `add_no_cue − cancel_no_cue`.

## One-line finding

**Add licensing is at uniform perfect ceiling (1.00 in 3/3 models); privative cancellation
(suppression) is partial and item/model-dependent (cancel_no_cue 0.75 / 0.625 / 0.875). The
asymmetry is positive in 3/3 models and clears the pre-registered 20 pp bar in 2/3 → CONFIRMS by
the frozen rule. But it is a weak confirm: it is marginal in claude and does not clear the bar in
gemini, and removing either of the two pre-flagged borderline privatives (toy violin, plastic
apple) drops it to 1/3. It holds across a verbal-add/nominal-cancel domain difference (M2), not a
clean within-verbal contrast.**

## Numbers (verified)

Affirm rates, NLI primary; independently recomputed by the post-run verifier (exact match to
`raw/results.json`; 324/324 priced, 0 missing, 0 parse failures, 0 errors).

| model | add_no_cue | add_control | cancel_default | cancel_no_cue | asymmetry | ≥ 0.20? |
|---|---|---|---|---|---|---|
| A — claude | 1.00 | 0.20 | 1.00 | 0.750 | **+0.250** | ✓ (marginal) |
| B — gpt-mini | 1.00 | 0.10 | 1.00 | 0.625 | **+0.375** | ✓ |
| C — gemini | 1.00 | 0.00 | 1.00 | 0.875 | **+0.125** | ✗ (symmetric) |
| | | | | | **2/3 confirm** | **CONFIRMS** |

- **Asymmetry (leg 1): CONFIRMS** — ≥ 0.20 in 2/3 (claude, gpt); gemini is below at +0.125. The
  direction is positive in **3/3** (add ≥ cancel always), but the magnitude bar is met in 2/3.
- **Instrument-fragility (leg 2): CONFIRMS** — cancel NLI-vs-FC rate disagreement exceeds the add
  arm's by ≥ 0.10 in 2/3 (gpt 0.25, gemini 0.125; claude 0.00). The add arm is instrument-stable
  (NLI = FC = 1.00 everywhere); only the cancel arm moves between instruments.
- **Cue arms:** follow-cue = 1.00 in 3/3 for both add (denial → withhold) and cancel (re-assertion
  → affirm) — both arms follow an explicit in-sentence cue perfectly. (Secondary, as pre-registered.)

### Per-item suppression map (cancel construction, NLI; suppressed = label 1/2, FAILED = label 0)

| noun (privative) | A | B | C | suppresses? |
|---|---|---|---|---|
| gun (fake), diamond (fake), rose (artificial), pearl (imitation), sword (toy) | 1/2 | 1 | 1/2 | **clean, 3/3** |
| tiger (toy) | 2 | **0** | 1 | mixed (gpt fails) |
| apple (plastic) | **0** | **0** | 1 | weak (claude+gpt fail) |
| violin (toy) | **0** | **0** | **0** | **fails 3/3** (weakest) |

The five clean privatives suppress in all three models; the asymmetry's strength is concentrated
there. The two items the pre-run critic flagged (`toy violin`, and `plastic apple`) fail to
suppress — a toy violin is arguably still a playable musical instrument, a plastic apple borderline.

## Robustness: the confirm is fragile (leave-one-out)

The post-run verifier recomputed the verdict with each cancel noun removed in turn (a **diagnostic**,
not a re-binning — the frozen verdict stands):

- Removing **violin**: asymmetry → claude 0.143, gpt 0.286, gemini 0.000 → **1/3 confirm**.
- Removing **apple**: → claude 0.143, gpt 0.286, gemini 0.143 → **1/3 confirm**.
- Removing any of the five clean privatives: still **2/3 confirm**.

So the 2/3 confirm rests on the two weakest-suppression items being counted as genuine
suppression-failures. This is the danger direction the pre-run critic named in advance (a weak
privative → high construction affirm → low cancel_no_cue → larger asymmetry). The honest reading:
**the qualitative asymmetry is real and consistent in direction (3/3 models: add at ceiling, cancel
below it), but its magnitude clears the pre-registered bar only because of borderline items, and is
marginal.** Under-claim accordingly.

## What this does and does not license

- **Does (per the frozen rule):** advance [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
  to **`tested`**, **supported on this leg** — a matched, ceiling-controlled battery shows add
  licensing uniformly at ceiling and privative cancellation reliably below it, in the predicted
  direction in 3/3 models, clearing 20 pp in 2/3 and the fragility bar in 2/3. With M1, the
  suppression shortfall is legitimately a *defeasance* shortfall (the default was a held entailment).
- **Heavily caveats that support:**
  1. **M2 domain mismatch (headline).** ADD is a *verbal* argument-structure construction; CANCEL
     is a *nominal/adjectival* privative. The asymmetry is across a **domain difference**, a
     broadened (weaker) version of the original verbal-only bet. It is **not** a clean within-verbal
     add-vs-cancel contrast; some of the gap could be verbal-vs-nominal, not add-vs-cancel.
  2. **Fragile / borderline-item-sensitive** (leave-one-out above); marginal in 2/3 models.
  3. **Small N, single run, panel-as-subjects, `internal-contrast-only`** — no human baseline; a
     direction-of-effect signal, not a magnitude or a human comparison.
- **Does not** falsify (no symmetric/reversal verdict), and the principled-limit closure (M3) is
  **not** triggered (it fires only on a B2 NO-GO, which did not occur at C2). Does not make any
  human-level claim, nor re-tune any threshold (all frozen s134 values untouched).

## How this sits with the prior evidence

It is consistent with — and weaker than — the existing internal-contrast legs the conjecture
abstracts over. The add direction is again at perfect ceiling (matching caused-motion / way /
resultative); the cancel direction is again off-ceiling and instrument-fragile (matching the
conative-cancel-v2 cue arm). The new contribution is a *fourth* construction pair showing the same
shape, now with a B2-certified categorical default — but bought at the cost of a verbal/nominal
domain mismatch. The conjecture's mechanism (LABELED speculation: accumulation aligns with the
predictive objective, retraction works against a strong prior) is untouched; this result neither
confirms nor refutes it.

## Provenance

- Every figure is reproduced verbatim from [`raw/results.json`](../../../experiments/runs/2026-06-28-monotonicity-c2-battery/README.md)
  and independently recomputed from the per-call `raw/*.json` by a read-only post-run verifier
  (exact match; 324/324 priced, 0 missing, 0 parse failures; leave-one-out diagnostic run).
- The ADD arm is the s135 frozen resultative arm reused byte-for-byte (sha `80bd4b60b55a3e60`); the
  C2 default ceiling (1.00, 3/3) is from [`result/monotonicity-c2-privative-calibration-v1`](monotonicity-c2-privative-calibration-v1.md);
  the matched conflicting-cue paradigm and the off-ceiling/fragile cancel pattern are from
  [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md). M1/M2 are the ratified
  decision's own modifications.
- Spend: **$0.09324 billed** (UTC 2026-06-28) = B2 calib $0.01675 + full battery $0.07649.
