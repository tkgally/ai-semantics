---
type: result
id: aann-temporal-heldout-v2b
title: AANN held-out productivity is noun-class-dependent — the widened temporal stratum does NOT replicate the human gradient (a powered confirmation of v2 caveat 2)
meaning-senses:
  - constructional
  - human-comparison
status: proposed
anchor: resource/mahowald-2023-aann-stimuli
contingent-on: []
created: 2026-06-13
updated: 2026-07-05
links:
  - rel: refines
    target: result/aann-behavioral-gradient-v2
  - rel: depends-on
    target: design/aann-temporal-heldout-v2b
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
  - rel: supports
    target: claim/aann-behavioral-gradient
---

# Result: the temporal held-out stratum (v2b) — a real hole in AANN productivity, not a small-n fluke

> **Status: proposed (2026-06-13).** The named follow-up to **caveat 2** of
> [`result/aann-behavioral-gradient-v2`](aann-behavioral-gradient-v2.md): v2's held-out
> adjective gradient replicated overall, but the **temporal noun-class stratum was ≈ −0.2 over
> only 4 thin cells** — too little to read. This run widens the temporal stratum **5×** (16 → 80
> items) under the **same ratified v2 instrument** (no new operationalization decision;
> [`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md))
> and re-reads it. **Verdict, pre-registered rule: STILL-TOO-THIN/MIXED — and, more pointedly,
> the temporal stratum is uniformly NEGATIVE at every grain for all three models.** The widened
> data confirm caveat 2 was a real signal: held-out AANN productivity is **noun-class-dependent**,
> and the temporal class is where it fails. **432 calls, $0.0793 billed, 0 missing.** Independent
> pre-run critic (5 blockers + 8 should-fixes applied before freeze) + independent post-run
> verifier (every figure re-derived from raw from scratch, **0 mismatches**). Run record:
> [`experiments/runs/2026-06-13-aann-temporal-heldout-v2b/`](../../../experiments/runs/2026-06-13-aann-temporal-heldout-v2b/README.md).

## What ran (under the ratified v2 instrument, three arms)

The temporal noun class admits only 4 adjective classes in Mahowald's Exp-2 validity matrix
(ambig / neg / pos / quant), so the **4 class-cells cannot be widened** — the widening is
*within* cells: **10 held-out adjectives per class** (6 new + 4 v2 carryovers), 2 items each,
all 5 Mahowald temporal nouns = **80 held-out temporal items**. Plus two arms the pre-run critic
required: a **fresh Tier-0** manipulation check (24 v2 forced-choice pairs × 3 models, gate ≥
20/24) and a **4-point framing-robustness subsample** (40 items, caveat-bearing, since v2's
framing-convergence evidence had **zero neg×temporal items**). Primary read unchanged from v2
caveat 2: per-model Spearman of the 4 held-out temporal class-cell means against the **human
anchored-half** temporal means (quant 8.45 > ambig 8.25 > pos 8.02 > neg 7.57). Secondary,
pre-registered before data: the finer **adjective-grain** Spearman (40 held-out adjective means
vs the class-assigned human mean) with a 10,000-resample bootstrap CI. Gate-bearing per the
governing decision's Conditions 2 + 4.

## The numbers (reproduced from raw by the post-run verifier, 0 mismatches)

| model | Tier-0 (gate ≥20/24) | 4-pt framing ρ (fragile?) | cell-grain ρ (n=4) | adjective-grain ρ [CI] | verdict (pre-registered) |
|-------|----------------------|---------------------------|--------------------|------------------------|--------------------------|
| claude-sonnet-4.6 | 23/24 ✓ | 0.939 (no) | **−0.20** | **−0.139 [−0.438, +0.172]** | FAILS-TO-REPLICATE |
| gpt-5.4-mini | 21/24 ✓ | 0.878 (no) | **−0.40** | −0.028 [−0.353, +0.305] | STILL-TOO-THIN |
| gemini-3.5-flash | 22/24 ✓ | 0.815 (no) | **−0.40** | −0.046 [−0.352, +0.265] | STILL-TOO-THIN |

**Stratum verdict: STILL-TOO-THIN/MIXED** (one FAILS, two too-thin; no model replicates). The
new-only subgroup (n=24, excluding carryovers) is also negative for all three (−0.151 / −0.151 /
−0.060), so the negative sign is **not** a carryover artifact.

## Reading it honestly

1. **No model positively tracks the human temporal gradient — at any grain.** Every cell-grain
   ρ, every adjective-grain ρ, the pooled item-grain figures, the partial-Zipf controls, and the
   new-only subgroup are **all ≤ 0**. This is not softened: where v2's overall held-out
   replication was a clean positive (0.75–0.83), the temporal slice of it is a clean *negative*,
   now with 5× the data behind it.
2. **It is a "fails / too-thin" split, not a clean falsification.** Only claude's adjective-grain
   CI is informative enough to read as FAILS-TO-REPLICATE (upper bound below the 0.20 band); gpt
   and gemini have CIs wide enough to straddle, so the frozen rule calls them STILL-TOO-THIN.
   Even at 80 items, a 4-class-cell stratum is intrinsically coarse — which is exactly why the
   adjective-grain secondary was pre-registered, and why the honest stratum verdict is
   "too-thin/mixed" rather than a categorical "the gradient is absent."
3. **What this does to v2.** It does **not** overturn v2's overall **SUPPORTED** verdict (which
   passed across all noun classes at the overall grain). It **sharpens caveat 2 into a finding**:
   AANN held-out productivity — generalizing the acceptability gradient to *novel* adjectives —
   is **noun-class-dependent**, strong for the object/distance classes that carried v2's positive
   and absent for the temporal class. The construction's gradient-tracking is real; its
   *productivity* is uneven across the noun classes the construction can take.
4. **The instrument is sound here.** Fresh Tier-0 passes for all three (the manipulation works —
   models do prefer well-formed AANNs), and 0–100↔4-point framing agreement is high (0.82–0.94,
   no fragility flag), so the negative temporal read is **not** an instrument artifact or a
   framing quirk — it is the models' actual graded behavior on held-out temporal AANNs.

## Caveats (all disclosed; the verifier's list)

1. **The "tourish"-typo template drives the verdict-category flips.** Mahowald's template 2
   carries an upstream typo ("The tourish stayed…") and its ratings run far below the other
   templates for every model (claude 15.4, gpt 4.8, gemini 51.5 vs ~70–90 for template 0).
   Excluding template-2 items (a pre-declared mandatory descriptive) **flips claude
   FAILS→too-thin and gemini too-thin→FAILS** — so the *category* labels are template-sensitive,
   while the overall picture (uniformly non-positive, non-replicating) is not. The mandatory
   caveat fires for claude and gemini, as pre-registered. (Held-out items make no item-level
   human comparison, so the typo carries no anchor risk; it is a within-model rating depressant.)
2. **Tier-0 gemini is parser-sensitive.** gemini answered three `ugly-three-desks` pairs as
   verbose `**A**`; the frozen `parse_ab_last` does not strip markdown bold, scoring it 22/24
   last-token (a markdown-stripping parser would give 24 first-token / 21 last-token). gemini
   passes the gate under every parser, so the verdict is unaffected — but the "22" rests on the
   frozen parser's markdown-blindness, disclosed.
3. **4 class-cells is the structural maximum** for the temporal stratum; the adjective-grain
   secondary does the real inferential work, and at n=4 the cell-grain Spearman is coarse
   (lattice {0, ±0.2, ±0.4, ±0.6, ±0.8, ±1}). This is a precision *widening* of an existing arm,
   not a new conjecture test.
4. **Held-out class membership is project-assigned** — no human validation is possible for
   held-out items by construction (same status as v2's held-out list, with 24 new assignments).
   The arm anchors to [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
   only **via the anchored-half human gradient it is asked to replicate**; it makes no
   independent human claim.

## Provenance / reproduction

Run dir [`experiments/runs/2026-06-13-aann-temporal-heldout-v2b/`](../../../experiments/runs/2026-06-13-aann-temporal-heldout-v2b/README.md):
frozen `PREREG.md`, `prep.py` (mirror-independent; reproduces every v2 Zipf value exactly),
`stimuli.json` (80 main items byte-identical to the pre-critic build; embedded freq audit +
human yardstick), `probe.py`, `analyze.py` (selftest 47 checks), raw JSONL per model ×
arm, `results.json`, and `VERIFIER-REPORT.md` (independent re-derivation, 0 mismatches).
Refines [`result/aann-behavioral-gradient-v2`](aann-behavioral-gradient-v2.md) (caveat 2);
anchored to [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md);
`contingent-on: []`.

*Pointer (s183): the "why" was later decomposed by the $0 re-analysis
[`result/aann-temporal-why-reanalysis`](aann-temporal-why-reanalysis.md) (H1 human-gradient
compression explains the low power; a localized H4 quant×temporal cell inversion carries the
negative sign), and the temporal hole is echoed for claude and gemini by the second-date held-out
arm of [`result/aann-behavioral-gradient-rep2`](aann-behavioral-gradient-rep2.md).*
