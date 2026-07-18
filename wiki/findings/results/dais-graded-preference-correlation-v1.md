---
type: result
id: dais-graded-preference-correlation-v1
title: "DAIS-anchored graded-preference correlation — the dative line's first human effect-SIZE comparison (scoped to the definiteness/length + verb-bias surface, NOT the givenness shift). VERDICT LENGTH-ONLY: the panel reproduces the human recipient gradient and tracks the human verb-bias magnitude (alternating-only control survives 3/3), and clears the SHORT-length definiteness contrast 3/3 — but the binding within-length definiteness control fails 3/3 at LONG length, so the recipient gradient is substantially end-weight-driven, not cleanly definiteness-tracking"
meaning-senses:
  - constructional
  - distributional
  - human-comparison
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-18
updated: 2026-07-18
links:
  - rel: operationalizes
    target: conjecture/dative-alternation-information-structure
  - rel: anchors
    target: resource/dais-dative-ratings
  - rel: depends-on
    target: design/dais-graded-preference-correlation-v1
  - rel: depends-on
    target: result/dative-information-structure-powered
  - rel: depends-on
    target: claim/dative-information-structure-givenness
---

# DAIS-anchored graded-preference correlation — VERDICT LENGTH-ONLY

> **Ran s248 (2026-07-18). Single run → `proposed`.** The frozen, cross-session-ratified DAIS Option-B
> instrument ([`design/dais-graded-preference-correlation-v1`](../../../experiments/designs/dais-graded-preference-correlation-v1.md),
> RATIFIED s247; freeze [`PREREG.md`](../../../experiments/runs/2026-07-18-dais-option-b/PREREG.md), sha
> `8e26f033…`, honoring B1–B3/S1–S3) correlated the three-model panel's **bare** graded double-object
> preference against the human graded gradient in DAIS (Hawkins, Yamakoshi, Griffiths & Goldberg 2020;
> CC BY 4.0; [`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md)). 1,200 calls,
> 0 NA, $1.82074; pre-run critic **GO-WITH-CONDITIONS** (C1 applied pre-data) + non-Anthropic vote
> **GO-WITH-CONDITIONS**; post-run verifier **REPRODUCED** (0 discrepancies).
>
> **SCOPE FENCE (load-bearing — read before citing this).** This is a human-effect-size comparison for
> the **definiteness/length + verb-bias preference surface only**, on a *bare* isolated-pair preference
> matching DAIS's slider task. It is **NOT** a human-effect-size comparison for the project's
> discourse-context **givenness shift** ([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)),
> which has no human effect-size anchor by design and is **untouched** here (its anchor stays
> `languageR::dative` production, direction-only). The DAIS anchor lands only on **this** result, scoped
> as above. "The dative line's first human effect-*size* comparison" is true **only** in this scoped
> sense — never for the givenness magnitudes.
>
> **VERDICT: LENGTH-ONLY** (frozen S3 decision-tree). The registered
> [`predictions.md`](../../predictions.md) §B bet (TRACKS-HUMAN-SURFACE) is a **LOSS** — an honest,
> informative negative on the calibration record.

## Headline — Arm B first (S2): the recipient definiteness/length surface

Within 40 alternating verbs, does the panel reproduce the human recipient gradient (pronoun >
shortDefinite > shortIndefinite > longDefinite > longIndefinite), and — the binding question — does it
do so by tracking **definiteness** or merely by **counting length**? The five DAIS recipient conditions
covary length with definiteness, so a pure end-weight reader reproduces the whole gradient with zero
definiteness sensitivity; the **within-length definiteness control** (definite − indefinite at each
length, length held fixed) is what separates the two.

| model | monotonicity rate (≥+0.5 ρₛ vs human dir; null p0=0.225) | beats chance? | short: `the girl`−`a girl` [95% CI] | long: `the girl from college`−`a girl from college` [95% CI] | within-length pass? |
|---|---|---|---|---|---|
| claude | 28/40 = 0.70 | **yes** (p<1e-4) | **+0.052 [+0.010, +0.092]** | +0.033 [CI incl. 0] | **no** |
| gemini | 29/40 = 0.725 | **yes** (p<1e-4) | **+0.071 [+0.024, +0.119]** | +0.021 [CI incl. 0] | **no** |
| gpt | 18/40 = 0.45 | **yes** (p=0.0013) | **+0.114 [+0.021, +0.210]** | +0.049 [CI incl. 0] | **no** |

- **The raw recipient gradient is reproduced 3/3** (monotonicity rate beats the pinned chance null on
  all three; needs ≥14/40, all clear). gpt is the weakest leg (0.45, still beats chance) — its
  persistent-shadow pattern across the dative/particle lines recurs.
- **The within-length definiteness control fails 3/3.** The **short**-length definiteness contrast
  (`the girl` vs `a girl`) clears on all three (CI-LB > 0) — a real, if small (≈5–11 points/100),
  definiteness sensitivity. But the **long**-length contrast (`the girl from college` vs `a girl from
  college`) has a CI including 0 on all three: at long recipient length the panel does **not** reliably
  raise DO-preference for the definite recipient. By the frozen rule (definiteness-tracking requires
  **both** within-length contrasts to clear, ≥2/3), the control **fails** → **LENGTH-ONLY**: the
  reproduced recipient gradient is substantially **end-weight-driven**, not cleanly a
  definiteness/information-structure surface.

**Reading:** the panel has *partial* definiteness sensitivity (present at short length, absent at long
length) riding on a dominant end-weight preference. This is the exact end-weight shortcut the flagship
givenness claim spent its rigor budget excluding by construction (byte-identical phrasings) — and it is
first-class evidence that on a *bare* definiteness/length surface, without the discourse-context
firewall, the panel's recipient gradient is more length-counting than definiteness-tracking.

## Companion — Arm A: the human verb-bias magnitude (an honest extension of the s245 scope)

Arm A is the s245-scope's **companion**, recorded as an explicit, honest extension to the DAIS paper's
headline **verb-bias** construct (never re-anchoring the givenness claim). Per-verb model DO-preference
at the canonical `shortDefinite` condition vs the human per-verb mean `DOpreference` at the matched
condition, Spearman ρ over 200 verbs, with the **binding** alternating-only frequency/classification
control (B2, a TRACKS conjunct):

| model | matched ρ (200 verbs) [95% CI] | alternating-only ρ (100 verbs) [95% CI-LB] | partial ρ (\|class+freq) | contamination ceiling (ρ≥0.95)? |
|---|---|---|---|---|
| claude | +0.608 [+0.501, +0.700] | +0.597 [LB > 0] | +0.480 | no |
| gemini | +0.763 [+0.683, +0.825] | +0.696 [LB > 0] | +0.631 | no |
| gpt | +0.628 [+0.542, +0.702] | +0.467 [LB > 0] | +0.542 | no |

- **The panel tracks the human verb-bias magnitude 3/3**, and — the binding B2 control — it survives
  restriction to the **alternating** verbs on all three (alternating-only ρ CI-LB > 0), so the
  correspondence is **not** merely the memorizable alternating/non-alternating lexical-subcategorization
  split: there is a graded per-verb verb-bias magnitude correspondence *within* the alternating class.
  This is the **dative line's first human effect-size correspondence** (scoped to the verb-bias surface).
- **No contamination ceiling** — the largest ρ is 0.763, far below the 0.95 memorization-upper-bound
  flag. **S1 standing caveat still binds:** DAIS verb bias is exactly what the source paper showed LMs
  partly capture, and per-verb bias is memorizable under the disjoint-stimulus construction (Q1-A), so
  even this clean, moderate ρ is contamination-vulnerable; the ceiling flag is one tripwire, not the
  defense (the defenses are the controls + Q1-A + reading the *pattern*, not the magnitude).

## The dissociation (the first-class result)

The panel **tracks the human verb-bias magnitude** (Arm A, controls survive) and **reproduces the raw
recipient gradient** (Arm B monotonicity), but its recipient gradient is **not cleanly a definiteness
surface** — it clears definiteness at short length only, and by the binding within-length control it is
substantially **end-weight-driven** (LENGTH-ONLY). So the two graded surfaces DAIS grounds come apart in
the panel: *lexical verb-bias magnitude* is tracked; the *graded definiteness/information-structure*
component of the recipient surface is only partially present, dominated by length. A model with a strong
verb-bias ρ and a length-driven recipient gradient has **lexical** knowledge and an **end-weight**
preference, not a clean graded definiteness surface — the honest deliverable the design named.

## Gates (frozen S3 decision-tree; per-model booleans, C2)

- `armA_full` (per-verb ρ CI-LB>0, ≥2/3): **True** (3/3).
- `armA_ctrl` (alternating-only ρ CI-LB>0, ≥2/3; B2 binding): **True** (3/3).
- `armB_mono` (monotonicity rate beats chance, ≥2/3; B1): **True** (3/3).
- `armB_within` (within-length definiteness, both lengths CI-LB>0, ≥2/3; binding): **False** (0/3).
- `armB_mono ∧ ¬armB_within` → **LENGTH-ONLY**. Contamination-ceiling flag: **False**.

Per-model transparency (C2): no single model drives a gate against the other two — Arm A clears on all
three, Arm B monotonicity clears on all three, the within-length control fails on all three. The verdict
is n=3 concordant orderings, not a pooled coefficient.

## What it feeds

- **The conjecture's secondary-confirm graded-acceptability clause** ([`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md)):
  filled with a **measured correlation**, but as a **partial/dissociated** result — the panel tracks the
  human graded *verb-bias* magnitude and the *raw* recipient gradient, but not the clean graded
  *definiteness* surface (end-weight-dominated at length). Secondary/non-decisive per the conjecture's
  confirm criterion; it neither converts nor rescues the primary givenness test, which it does not touch.
- **The predictions §B bet: a LOSS** (TRACKS did not obtain; LENGTH-ONLY). Recorded as an honest
  calibration negative.
- **Promotion:** not now. Single run → `proposed`. A scoped `claim` (a human-effect-size dative claim on
  the definiteness/length + verb-bias surface, held **distinct** from the givenness claim) would need a
  fresh-item replication + a cross-session promotion review; the verb-bias ρ is the promotable leg if it
  replicates, the definiteness surface is a **null-leaning** LENGTH-ONLY dissociation.

## Provenance + reproduction

- **Run:** [`experiments/runs/2026-07-18-dais-option-b/`](../../../experiments/runs/2026-07-18-dais-option-b/)
  — `build_trials.py` (project-constructed stimuli, B3 disjointness + fidelity audit), `common.py`
  (bare-preference indicator), `probe.py` (blind, per-arm hard stops), `analyze.py` (frozen stats + S3
  tree), `PREREG.md` (frozen bands + gate outcomes), `VERIFY-s248.txt` (post-run verifier). Raw model
  preferences in `raw/probe-{A,B}-<model>.jsonl`. No DAIS sentence rows or building-blocks in git (B3).
- **Human anchor:** [`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md)
  (`anchors:`, Q3-A), scoped to the definiteness/length + verb-bias surface only.
- **Verifier:** independent recomputation from raw (separate code path) reproduced every headline figure;
  `analyze.py` re-run byte-identical (seeded bootstrap). 0 discrepancies.
