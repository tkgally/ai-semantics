---
type: result
id: lexical-sense-gradience-v1
title: Lexical sense gradience v1 — the panel's graded sense-relatedness rating tracks the human DURel median (Spearman 0.60–0.83, in/above the human inter-annotator range) and survives a context-similarity control; the project's first lexical result and first own-design result with a real human anchor
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: proposed
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-05-30
updated: 2026-07-05
links:
  - rel: supports
    target: conjecture/lexical-sense-gradience
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: open-question/lexical-polysemy-gradience
  - rel: supports
    target: claim/lexical-sense-gradience
---

# Result: lexical sense gradience v1 (the project's first LEXICAL probe)

**One-line:** across 200 DWUG EN within-period usage pairs, every panel model's graded sense-relatedness rating for the target word is **strongly rank-correlated with the human DURel median** — Spearman **0.68 / 0.60 / 0.80** (claude / gpt-5.4-mini / gemini) on the 4-point framing, **0.70 / 0.68 / 0.83** on a 0–100 framing — and this monotonicity **survives partialling out the model's own topic-similarity rating** (e.g. gemini 0.80→0.73). The panel's agreement with the human median is **in or above the human inter-annotator range** (DWUG EN human–human Spearman = 0.69). This is the project's **first lexical (non-grammatical) result**, the **first own-design result anchored to a real human signal** (not internal-contrast-only), and a **positive for [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md)** clauses (a) + (c).

Run record: [`experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/`](../../../experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/README.md). Design: [`design/lexical-sense-gradience-v1`](../../../experiments/designs/lexical-sense-gradience-v1.md). Gate: [`decisions/resolved/lexical-sense-gradience-operationalization`](../../decisions/resolved/lexical-sense-gradience-operationalization.md) (ratified under Tom's delegation). Anchor: [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (DWUG EN v3.0.0). Cost **$3.134 billed**.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** This line compounded: clauses
> (a)+(c) were promoted s176 →
> [`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md) (`supported`,
> direction/agreement scope), and the cross-date re-run landed s181 →
> [`result/lexical-sense-gradience-rep2`](lexical-sense-gradience-rep2.md) (200 fresh
> pair-disjoint DWUG pairs on the byte-frozen instrument; **replicates 3/3** — every rep2 ρ within
> this page's 95% CIs; the topic-partial shadow-beater survives both framings; the claim's
> single-run flag is **discharged** for the direction/agreement core). gpt remains the weakest and
> most elicitation-sensitive corner (rep2 durel ρ 0.528, partial|topic 0.392 — down from v1, still
> positive and non-collapsing). *(Back-annotation: this page's numbers stand as the v1 record.)*

## What was tested (v1 scope: P1 monotonicity + P3 context control)

Does an LLM's same/different-sense behavior reproduce the **graded** usage-similarity lexicographers (and DWUG's annotators) document, or collapse to discreteness — and is any gradience separable from a **context-similarity shadow** (clause c, the lexical analogue of the constructional `distributional`/frequency null that runs through this repo)? The polysemy-vs-homonymy intermediate-regime arm (conjecture prediction 2) is **deferred to v2** with a frozen WordNet-grounded stratification, so the contestable layer never touches this clean monotonicity test.

- **Anchor / items:** DWUG EN graded human DURel judgments (4 Identical / 3 Closely Related / 2 Distantly Related / 1 Unrelated) over pairs of usages of the **same target word**. 200 pairs, balanced 50 per rounded DURel level (1–4), 43 lemmas, **within-period only** (synchronic), ≥2 annotator judgments per pair (median = human gold). Frozen pre-run (manifest sha256 `7b4ad11f…`); a pre-run critic's target-span BLOCKER was fixed + re-frozen before any model call (run README).
- **Instrument (behavioral panel, no logprobs):** each model rated each pair under three pre-registered framings — `durel` (verbatim 4-point DURel scale, the primary graded signal rank-comparable to the human median), `cont` (0–100 continuous, instrument robustness), `topic` (0–100 topic/situation similarity *ignoring* the target word, the semantic context control). Temperature 0 → the 3-family panel.
- **Reading rule (report-the-correlation; no pass bar):** Spearman ρ(model sense, human DURel) per model per framing with bootstrap 95% CI; partial ρ controlling for lexical overlap and for model topic-similarity; per-human-level mean ratings.

## Result (independently re-verified from raw JSON — CLEAN)

| model | `durel` ρ (95% CI) | `cont` ρ (95% CI) | partial ρ \| overlap | partial ρ \| topic | ρ(sense,topic) |
|---|---|---|---|---|---|
| claude-sonnet-4.6 | 0.679 (0.59–0.75) | 0.696 (0.61–0.78) | 0.67 / 0.69 | 0.52 / 0.54 | 0.64 / 0.68 |
| gpt-5.4-mini | 0.601 (0.49–0.69) | 0.675 (0.58–0.75) | 0.59 / 0.66 | 0.50 / 0.58 | 0.46 / 0.52 |
| gemini-3.5-flash | **0.804 (0.75–0.85)** | **0.825 (0.76–0.87)** | 0.80 / 0.82 | 0.73 / 0.75 | 0.56 / 0.59 |

1800 calls, 0 NA. Per-human-level mean ratings are cleanly **monotonic** (e.g. claude `cont`: 18.2 → 21.1 → 31.6 → 36.0 → 50.1 → 76.1 → 80.3 across human levels 1.0→4.0).

**Three readings:**

1. **Graded-sense tracking holds (clause a).** All three models order usage pairs by sense-relatedness much as DWUG's annotators do — not a near-binary same/different collapse but a graded monotone signal, consistent across an ordinal and a continuous framing. The CIs are well clear of zero (lowest bound 0.49). gemini (0.80–0.83) is the strongest, claude (0.68–0.70) ≈ the human–human agreement (0.69), gpt-5.4-mini (0.60–0.68) the weakest.
2. **It is not just a context shadow (clause c).** Lexical overlap is near-degenerate in this sample (DWUG's same-lemma usage sentences barely share content words), so a *surface* shadow is ruled out a priori — partialling it changes ρ by ≤0.02. The stronger test, partialling out the model's **own** topic-similarity rating, **substantially survives** (gemini 0.80→0.73; claude 0.68→0.52; gpt 0.60→0.50): the sense signal carries rank information about human sense-relatedness *beyond* the model's perception of how similar the two contexts are.
3. **Instrument/model echo of the project's standing theme.** gpt-5.4-mini is the noisier model under the *ordinal* DURel framing (ρ 0.60, mid-level means non-monotonic) but cleaner under the *continuous* framing (ρ 0.68) — the lexical reappearance of the instrument-sensitivity pattern that [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md) tracks on the grammatical side; here, again, gpt-5.4-mini is the model whose reading depends most on the elicitation format.

## The lexicon–grammar connection (why this matters beyond the lexical axis)

This result and the constructional findings share **one evidential skeleton**, which is the project's emerging unifying frame (developed on the theory page): *does the model track a meaning gradient that beats a distributional shadow?* On the **grammatical** axis the meaning is a construction's contributed inference and the shadow is n-gram/frequency or surface form; on the **lexical** axis the meaning is graded sense-relatedness and the shadow is context/topic similarity. Construction Grammar treats the two axes as a single continuum — words are maximally specific constructions, grammar and lexicon a `constructicon` — so the parallel is not a loose analogy but the same form–meaning question at two grains. The constructional centerpiece (the comparative correlative) survived its shadow + harder stress tests; this lexical centerpiece survives its context-similarity shadow. **Both axes now have a positive that beats the distributional null** — the first time the project can state the lexicon–grammar parallel with evidence on *both* sides rather than one. (A dedicated theory page works this continuum out — since written: [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) — and this result is its lexical anchor.)

## Caveats (lead with these)

- **Monotonicity, not representation.** This is a *behavioral* rank correlation (the model rates pairs much as humans do); it is **not** evidence of graded sense *representations* — that is the deferred small-model representation lane, blocked on local compute. Do not over-read.
- **The topic control is model-internal.** A surviving `partial|topic` is *modest* positive support that the sense signal isn't merely echoed context similarity; it is not a fully independent control, and a collapse would have been ambiguous (sense and topic are genuinely correlated across items). The lexical-overlap control is near-degenerate and rules out only the surface shadow.
- **Gold reliability.** 152/200 pairs rest on only 2 annotators *(corrected s183 by recompute from `manifest.csv` — the page originally said 151; the n≥3 subset is 48/200, matching the rep2 record)*; the half-integer levels are 2-rater disagreements; the n≥3 subset ρ is reported in `raw/results.json` as a robustness check, and the half-integer levels are not treated as reliable graded gold.
- **Low end mixes homonymy.** Some DWUG lemmas conflate homonyms (e.g. `lass` girl vs `lassi` drink), so the "Unrelated" floor is partly homonymy, not graded polysemy; the clean polysemy-vs-homonymy contrast is the deferred v2.
- **Scope.** 200 pairs, 43 CCOHA lemmas, single temp-0 run per model, DURel framing, English. Direction-of-effect, not a coverage benchmark; no claim beyond these lemmas/register/framing.
- **Human-comparison scope.** DWUG's DURel median is a genuine human signal (this is the project's first own-design result with a real `anchors` resource), but the "in/above human inter-annotator range" comparison references the published EN agreement (ρ 0.69); model-vs-median and annotator-vs-annotator are related but not identical quantities.
