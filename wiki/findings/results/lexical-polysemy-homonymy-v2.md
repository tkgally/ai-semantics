---
type: result
id: lexical-polysemy-homonymy-v2
title: Lexical v2 — polysemy vs homonymy (the conjecture's distinctive bet) — NOT ESTABLISHED — DWUG EN holds too few clean homonyms (3 lemmas) to test clause (b); the predicted discreteness regime is not separable from monotonicity-plus-selection, and every test is non-significant
meaning-senses:
  - referential
  - distributional
  - human-comparison
status: proposed
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-05-30
updated: 2026-07-05
links:
  - rel: refines
    target: result/lexical-sense-gradience-v1
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Result: lexical v2 — polysemy vs homonymy (clause b) — a NULL / not-established

**One-line (write the null first):** re-analyzing the **already-collected** lexical-v1 ratings (no new API spend) under a frozen etymological polysemy/homonymy stratification of the 43 DWUG EN lemmas, the conjecture's *distinctive* bet — clause (b), that homonymy is treated as a **discrete floor** while polysemy keeps an **intermediate** regime — is **not established**. DWUG EN contains only **3 clean general-English homonym lemmas** (`ball`, `plane`, `prop`; 16 pairs); the matched-human homonym−polysemy gap is tiny and mixed-sign (−3.8 to +0.7), **every** whole-lemma permutation test is non-significant (p 0.29–1.0), and the b3 **precondition fails** (homonym lemmas are *not* more bimodal than polysemy lemmas in the human gold). A residual weak hint survives only at the ordinal floor (homonym pairs sit at the model floor somewhat more than polysemy at human ≤2) but is confounded with scale-floor and circularity. **The honest finding is methodological: this anchor cannot test clause (b); a homonymy-enriched set is required (lexical v3).** *[Pointer, s183: the homonymy-enriched v3 ran 2026-05-31 — [`result/lexical-polysemy-homonymy-v3`](lexical-polysemy-homonymy-v3.md), a better-powered null on the discreteness test.]* The clean monotonicity of v1 (clause a) does decompose cleanly into *both* strata.

Run record: [`experiments/runs/2026-05-30-lexical-polysemy-homonymy-v2/`](../../../experiments/runs/2026-05-30-lexical-polysemy-homonymy-v2/README.md). Design: [`design/lexical-polysemy-homonymy-v2`](../../../experiments/designs/lexical-polysemy-homonymy-v2.md). Gate: [`decisions/resolved/lexical-sense-gradience-operationalization`](../../decisions/resolved/lexical-sense-gradience-operationalization.md) Q2. Anchor: [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md). Cost **$0.00** (re-analysis). An independent adversarial pre-write critic forced this null framing (see Provenance).

## What was tested (conjecture clause b / prediction 2)

[`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) prediction 2 — the still-untested *distinctive* bet, deliberately kept out of the clean v1 monotonicity result:

> "there is an **intermediate regime for related-but-distinct (polysemous) usages** that is **absent for homonyms** (homonym pairs sit at the 'different' floor with little intermediate mass); the distributions for the two regimes are separable — polysemy is *not* treated as just-another-homonym."

v1 established graded monotonicity (clauses a + c). v2 asks: when a lemma's low-relatedness pairs are *genuinely unrelated* (homonymy) vs *distantly-but-genuinely related* (polysemy), does the model treat them **differently** — a separable discrete regime for homonymy?

- **Stratification (frozen pre-analysis; etymology fallback for the no-WordNet constraint; gate Q2).** An Etymonline + Wiktionary rule, applied **blind to the model ratings**, with genuinely ambiguous lemmas **excluded** not force-labelled, and applied **uniformly** (per the pre-write critic): a lemma is HOMONYM only if it has ≥2 distinct etymological origins **both common in general modern English**. **HOMONYM = 3 lemmas** — `ball` (Germanic round vs Romance dance), `plane` (Latin *planus* vs Greek *platanos* tree), `prop` (Middle Dutch *proppe* support vs *property*-clip stage-prop) / **16 pairs**; **POLYSEMY = 35 lemmas / 154 pairs**; **EXCLUDED (AMBIGUOUS) = 5** — `graft`/`heel`/`rally`/`tip` (disputed/hedged origins) and **`lass`** (the v1 S4 `lass`/`lassi` case — a DWUG *data-conflation*, **not** an etymological homonym, so excluded rather than allowed to pad a stratum). sha256-frozen; per-lemma etymology + source in `stratification.csv` and the run README.
- **Reuses** each model's v1 `durel` (1–4) and `cont` (0–100) rating for the 170 in-stratum pairs.
- **Reading rule (frozen pre-computation; report-the-number).** b1 within-stratum Spearman; b2 the **matched-human** homonym−polysemy gap (averaged over shared human levels, so a raw "homonyms are just more unrelated" difference is not mistaken for discreteness) + low-end floor mass; b3 the model-free human-DURel structure by stratum (the bimodality precondition); a **whole-lemma label-permutation** null for the matched gap.

## Result (independently re-verified from raw JSON — CLEAN; numbers below are the corrected-stratification re-run)

**b3 — the precondition FAILS.** Clause (b) presupposes homonym lemmas are more **bimodal** (mass at the extremes, thin middle) than polysemy. They are not:

| stratum | n pairs | mean human | frac ≤2 | frac intermediate (2–3) | frac ≥3.5 |
|---|---|---|---|---|---|
| HOMONYM | 16 | 2.31 | 0.50 | 0.25 | 0.31 |
| POLYSEMY | 154 | 2.49 | 0.43 | 0.46 | 0.25 |

The homonym lemmas carry substantial intermediate **and** high human mass (mostly `prop` and `plane`, whose cross-period usage pairs humans often rated *related*), so there is no "homonyms pile at the floor, polysemy fills the middle" structure to detect. The test below sits on a precondition the data do not meet.

**b1 — within-stratum monotonicity holds in *both* strata** (the v1 clause-(a) positive decomposes cleanly, the one solid sub-finding): cont ρ(model, human) claude H 0.77 / P 0.67; gpt H 0.71 / P 0.62; gemini H 0.83 / P 0.79. (Homonym ρ rests on 16 pairs / 3 lemmas — not load-bearing.)

**b2 — the clause-(b) contrast: NOT established.**

| model | framing | matched-human gap (H−P) | perm p | low-end homonym (mean, floor-frac, n) | low-end polysemy (mean, floor-frac, n) |
|---|---|---|---|---|---|
| claude | cont | −1.9 | 0.98 | 15.0, 0.75, 8 | 23.7, 0.74, 66 |
| gpt-5.4-mini | cont | −2.2 | 0.88 | 10.6, 0.88, 8 | 31.9, 0.61, 66 |
| gemini | cont | −3.8 | 0.79 | 8.8, 0.88, 8 | 28.9, 0.50, 66 |
| claude | durel | −0.02 | 1.0 | 1.62, 0.63, 8 | 1.91, 0.23, 66 |
| gpt-5.4-mini | durel | +0.67 | 0.29 | 1.25, 0.75, 8 | 1.85, 0.27, 66 |
| gemini | durel | 0.0 | 1.0 | 1.38, 0.88, 8 | 1.95, 0.26, 66 |

**Three readings:**

1. **Clause (b) is not established — write the null.** The matched-human gap (the de-confounded statistic that compares strata *at the same human relatedness*) is tiny and mixed-sign (−3.8 to +0.7 across cells), and **no** whole-lemma permutation test approaches significance (p 0.29–1.0). With only **3 homonym lemmas**, the test has almost no power and **cannot reject** the null that the panel treats homonymy and polysemy the same way once the human signal is matched. The conjecture's "separable regime" prediction is not detectable here.
2. **The one residual hint is at the ordinal floor — and is confounded.** On the `durel` scale, the low-end (human ≤2) **floor-fraction** is higher for homonyms (0.63–0.88) than polysemy (0.23–0.27): where humans call usages unrelated, models put the *cross-etymon* ones at the bare floor (rating 1) more often. But this is **(a)** n=8 homonym pairs, **(b)** a scale-floor artifact (a 4-point scale cannot go below 1, so "more discrete" and "more floored" are the same notch), and **(c)** partly **circular** — these pairs were *selected into* human=1 by DURel annotators, so the model agreeing is already-shown clause-(a) monotonicity, not a new homonymy regime. On the continuous (`cont`) scale, where the floor artifact is weaker, the homonym/polysemy floor-fractions converge (0.75–0.88 vs 0.50–0.74). The hint does not survive as a regime.
3. **The real finding is methodological.** DWUG EN — built for *diachronic* change, not synchronic homonymy — contains too few clean general-English homonym lemmas to test clause (b). A proper test needs a **homonymy-enriched** graded set (the lexical v3): a resource where homonym and polysemy pairs are matched on human relatedness across the *full* range, not concentrated at the floor. v2's durable contribution is to **clean up the v1 "low end mixes homonymy" caveat** — it labels which low pairs are cross-etymon (3 lemmas) and shows they do not form a separable regime — and to retire the idea that v1's anchor could carry clause (b).

## Caveats (lead with these)

- **Underpowered to the point of untestable: 3 homonym lemmas / 16 pairs.** This is the binding limit. Report clause (b) as **not established** (a null at this N), not as "directionally supported." Earlier framing to that effect was corrected after an adversarial pre-write critique.
- **b3 precondition unmet.** The homonym lemmas are not bimodal; the discreteness test has no separable distribution to find.
- **Floor circularity + scale-floor.** The only residual signal is at human=1 where model-agrees-with-human is clause (a), not a homonymy regime, and the ordinal scale floors out.
- **Etymology ≠ synchronic relatedness; and the in-corpus sense may be single.** `plane`/`prop` pairs are often the *same* sense within a pair (so the lemma is etymologically a homonym but the pair is not a cross-sense pair) — another reason the homonym stratum does not behave as clause (b) imagines. A pair-level (not lemma-level) homonymy label would be the cleaner design, and DWUG does not supply it.
- **Re-analysis, not fresh pre-registration** (inherits all v1 caveats: behavioral not representational; single run; 43 CCOHA lemmas; English).

## Where it sits

- **Refines** [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md): cleans up its S4 "low end mixes homonymy" caveat (labels the cross-etymon lemmas; shows no separable regime) and decomposes the v1 monotonicity as holding within both strata (b1).
- **Bears on** [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) clause (b): **not established** — the conjecture's central bet (a+c) stands from v1; its *distinctive* bet (b) remains **open**, now with a concrete reason (DWUG EN too few clean homonyms) and a defined next step (homonymy-enriched v3).
- Anchored to [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md). `contingent-on: []`.

## Provenance

- Data: the committed v1 raw preds + manifest; the frozen `stratification.csv` (sha256 in run README). Script: `analyze.py` (stdlib only; deterministic seed).
- **Adversarial pre-write critique (independent, read-only):** flagged that (i) the homonym floor signal is circular and scale-floored, (ii) the b3 precondition fails, (iii) `lass` was a DWUG conflation mislabelled as a homonym, and (iv) `prop` was a genuine homonym mis-filed as polysemy. All four were applied: the stratification was corrected to the uniform rule (`lass` excluded, `prop`→HOMONYM), the analysis re-run, and this page rewritten from "directionally supported" to **not established**. The critique is the reason this is a clean null rather than an overclaim.
- **Post-run number-verification (independent, read-only):** recomputed every headline figure from raw JSON with an independent Spearman → CLEAN (on the pre-correction stratification; the correction only *weakened* the effect, consistent with the null).
