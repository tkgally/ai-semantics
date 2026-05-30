---
type: result
id: lexical-polysemy-homonymy-v2
title: Lexical v2 — polysemy vs homonymy (the conjecture's distinctive bet) — homonym pairs are rated more floored than polysemy pairs at matched human relatedness (the predicted discreteness direction) in all 3 models, but the effect is non-significant on 3 homonym lemmas — a directional, not established, partial confirmation of clause (b)
meaning-senses:
  - referential
  - distributional
  - human-comparison
status: proposed
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: supports
    target: conjecture/lexical-sense-gradience
  - rel: refines
    target: result/lexical-sense-gradience-v1
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Result: lexical v2 — polysemy vs homonymy (clause b)

**One-line:** re-analyzing the **already-collected** lexical-v1 ratings (no new API spend) under a frozen etymological polysemy/homonymy stratification of the 43 DWUG EN lemmas, all three models rate **homonym** pairs (distinct unrelated roots — *ball*, *plane*, *prop*) as **less related than polysemy pairs at the *same* human relatedness level** (matched-human gap negative for every model/framing; low-end floor-fraction 0.8–1.0 for homonyms vs 0.5–0.74 for polysemy) — the **direction clause (b) predicts** (homonymy treated more discretely than polysemy). **But the effect is not significant** — only 3 homonym lemmas / 13 pairs, whole-lemma permutation p 0.23–0.86 — so this is a **directional, not established, partial confirmation**. The conjecture's *distinctive* bet gets a first, honest, **weak-positive** test; the clean version needs more homonym lemmas.

Run record: [`experiments/runs/2026-05-30-lexical-polysemy-homonymy-v2/`](../../../experiments/runs/2026-05-30-lexical-polysemy-homonymy-v2/README.md). Design: [`design/lexical-polysemy-homonymy-v2`](../../../experiments/designs/lexical-polysemy-homonymy-v2.md). Gate: [`decisions/resolved/lexical-sense-gradience-operationalization`](../../decisions/resolved/lexical-sense-gradience-operationalization.md) Q2 (stratification staged to a separate v2). Anchor: [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md). Cost **$0.00** (re-analysis).

## What was tested (conjecture clause b / prediction 2)

[`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) prediction 2 — the still-untested *distinctive* bet, deliberately kept out of the clean v1 monotonicity result:

> "there is an **intermediate regime for related-but-distinct (polysemous) usages** that is **absent for homonyms** (homonym pairs sit at the 'different' floor with little intermediate mass); the distributions for the two regimes are separable — polysemy is *not* treated as just-another-homonym."

v1 established graded monotonicity (clauses a + c). v2 asks the sharper question: when a lemma's low-relatedness pairs are *genuinely unrelated* (homonymy) vs *distantly-but-genuinely related* (polysemy), does the model treat them **differently** — more floored/discrete for homonymy?

- **Stratification (frozen pre-analysis; etymology fallback for the no-WordNet constraint):** an Etymonline + Wiktionary rule, blind to the model ratings, with genuinely ambiguous lemmas **excluded** not force-labelled (gate Q2). **HOMONYM = 3 lemmas** (`ball` Germanic-round vs Romance-dance; `plane` Latin-*planus* vs Greek-*platanos* tree; `prop` Dutch-support vs *property*-clip) / 13 pairs; **POLYSEMY = 36 lemmas** / 158 pairs; 4 excluded (`graft`/`heel`/`rally`/`tip`-class). sha256 `afbf4cc6…`. Etymology quotes in the run README; an independent dual-source pass over all 43 lemmas confirmed the same confident homonym set.
- **Reuses** each model's v1 `durel` (1–4) and `cont` (0–100) rating for the 171 in-stratum pairs.
- **Reading rule (frozen pre-computation; report-the-number, no pass bar):** b1 within-stratum Spearman; b2 the **matched-human** homonym−polysemy gap (averaged over shared human levels, so a raw "homonyms are simply more unrelated" difference is *not* mistaken for discreteness) + low-end floor mass; b3 the model-free human-DURel structure by stratum (the bimodality precondition); a **whole-lemma label-permutation** null for the matched gap.

## Result (independently re-verified from raw JSON — CLEAN)

**b3 — precondition (model-free human gold).** Homonym pairs are concentrated at the human floor; polysemy pairs carry the intermediate mass:

| stratum | n pairs | mean human | frac ≤2 | frac intermediate (2–3) | frac ≥3.5 |
|---|---|---|---|---|---|
| HOMONYM | 13 | 1.5 | 0.77 | 0.08 | 0.15 |
| POLYSEMY | 158 | 2.54 | 0.42 | 0.46 | 0.27 |

**b1 — within-stratum monotonicity holds in *both* strata** (the v1 positive is not an artifact of one regime). cont ρ(model, human): claude H 0.75 / P 0.69; gpt H 0.64 / P 0.64; gemini H 1.00 / P 0.81. (Homonym ρ is high but rests on only 3 distinct human levels in 13 pairs — not load-bearing.)

**b2 — the clause-(b) contrast: right direction, not significant.**

| model | framing | matched-human gap (H−P) | low-end homonym (mean, floor-frac) | low-end polysemy (mean, floor-frac) | perm p |
|---|---|---|---|---|---|
| claude | cont | **−5.6** | 7.4, **1.00** | 23.7, 0.74 | 0.58 |
| gpt-5.4-mini | cont | **−12.0** | 11.3, 0.80 | 31.9, 0.61 | 0.24 |
| gemini | cont | **−9.4** | 0.0, **1.00** | 28.9, 0.50 | 0.23 |
| claude | durel | +0.05 | 1.3, 0.70 | 1.9, 0.23 | 0.86 |
| gpt-5.4-mini | durel | −0.35 | 1.2, 0.80 | 1.9, 0.27 | 0.23 |
| gemini | durel | −0.23 | 1.0, **1.00** | 2.0, 0.26 | 0.28 |

**Three readings:**

1. **The predicted direction appears, consistently — clause (b) is weakly, directionally supported.** On the continuous framing, homonym pairs are rated **lower than polysemy pairs at matched human relatedness** for all three models (gap −5.6 / −12.0 / −9.4), and the **low-end floor-fraction is higher for homonyms** in every cell (0.8–1.0 vs 0.5–0.74; gemini floors **100%** of low homonym pairs to ~0 on cont). So where humans rate two usages "unrelated," the models treat the *genuinely-cross-etymon* (homonym) cases as **more emphatically unrelated** than the *distantly-related* (polysemy) cases — the discreteness clause (b) predicts. Polysemy is **not** treated as just-another-homonym in the direction of the means.
2. **But it is not statistically established — this is a first-class weak result, not a confirmation.** The whole-lemma label-permutation p is **non-significant in every cell** (0.23–0.86), because the homonym stratum is only **3 lemmas / 13 pairs** (DWUG's EN lemma set simply contains few clean general-English homonyms). The durel (ordinal) framing barely separates the strata at all (gaps −0.35 to +0.05). The honest summary: **the means point the predicted way; the sample cannot rule out chance.**
3. **A circularity bound keeps it modest.** Homonym pairs are low *because* they are cross-etymon, and humans already rated them low (b3) — so part of "models floor homonyms" is just models tracking the human gold v1 already showed they track. The **matched-human** gap is the guard against this (it compares strata *at the same human level*), and it stays negative — modest evidence the model adds floor-concentration *beyond* the human signal — but with 1–2 homonym pairs per matched level, that guard is thin. The cleanest reading: v2 **cleans up the v1 "low end mixes homonymy" caveat** (it labels which low pairs are homonymy and shows they sit lowest) more than it establishes a new regime.

## Caveats (lead with these)

- **Underpowered: 3 homonym lemmas.** This is the binding limit. The effect is directional in 5/6 cells but significant in 0/6. Do not report clause (b) as confirmed; report it as *directionally supported, awaiting more homonym lemmas* (a larger graded set, e.g. more DWUG languages or a homonymy-enriched item set, is the v3).
- **Etymology ≠ synchronic relatedness.** Etymological distinctness is the operational stand-in for homonymy; frozen from Etymonline+Wiktionary because WordNet is unavailable offline (gate-authorized fallback). A few etymological homonyms may feel related to modern speakers. The AMBIGUOUS-exclusion rule absorbs the worst cases; the 3 retained homonyms are unambiguous.
- **`lass_nn` conflation works *against* the hypothesis.** DWUG's `lass_nn` lemma conflates *lass* (girl) and *lassi* (drink) — a data-level homonymy — yet it is labelled POLYSEMY (single etymological origin for *lass*). This injects homonym-like floor pairs into the *polysemy* stratum, **shrinking** the H−P gap, so the stratification is conservative on this point (the true effect, if any, is at least as large as measured).
- **Re-analysis, not fresh pre-registration.** The v1 ratings were already seen; the discipline is the etymology-frozen stratification + pre-fixed statistics (run README). Inherits all v1 caveats (behavioral not representational; single run; 43 CCOHA lemmas; English).
- **`durel` vs `cont` disagree on resolution.** The contrast is visible on the continuous framing and nearly flat on the ordinal one — the lexical echo of the project's standing instrument-sensitivity theme.

## Where it sits

- **Supports** [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) clause (b) **weakly/directionally** — the conjecture's central bet (a+c) was supported in v1; its *distinctive* bet (b) now has a first directional positive, not yet an established one. The conjecture stays `tested` with (b) "directionally supported, underpowered."
- **Refines** [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md): cleans up its S4 "low end mixes homonymy" caveat by labelling the cross-etymon pairs and showing they sit lowest, and decomposes the v1 monotonicity as holding within both strata.
- Anchored to [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (human DURel gold, reused). `contingent-on: []`.
