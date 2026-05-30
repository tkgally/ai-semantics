---
type: design
id: lexical-polysemy-homonymy-v2
title: lexical-sense-gradience v2 — does the panel treat polysemy (graded, intermediate) differently from homonymy (discrete, floored)? A re-analysis of the v1 ratings under a frozen etymological stratification (no new API)
meaning-senses:
  - referential
  - distributional
  - human-comparison
status: ready
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: operationalizes
    target: conjecture/lexical-sense-gradience
  - rel: refines
    target: design/lexical-sense-gradience-v1
  - rel: depends-on
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Experiment design v2 — polysemy vs homonymy (the lexical wedge's distinctive bet)

> **Status: ready.** This is the **clause-(b) / prediction-2** arm that [`design/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md) deliberately deferred (gate [`decisions/resolved/lexical-sense-gradience-operationalization`](../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md) Q2: "polysemy/homonymy stratification run as a **separate later probe (v2)**, *not* bundled into v1, so the contestable layer never touches the clean monotonicity test"). It **re-uses the already-collected v1 model ratings** ([`result/lexical-sense-gradience-v1`](../../wiki/findings/results/lexical-sense-gradience-v1.md)) — **no new API spend** — split by a frozen etymological stratification of the 43 DWUG EN lemmas.

## 1. What clause (b) predicts

[`conjecture/lexical-sense-gradience`](../../wiki/findings/conjectures/lexical-sense-gradience.md) prediction 2 — the conjecture's *distinctive* still-untested bet:

> "there is an **intermediate regime for related-but-distinct (polysemous) usages** that is **absent for homonyms** (homonym pairs sit at the 'different' floor with little intermediate mass); the distributions for the two regimes are separable — polysemy is *not* treated as just-another-homonym."

The v1 result established graded monotonicity (clauses a + c). v2 asks the sharper question: when the lemma's low-relatedness pairs are *genuinely unrelated* (homonymy — two etymologically distinct words sharing a spelling) vs *distantly-but-genuinely related* (polysemy — one root, senses shaded apart), does the model **treat them differently** — more discretely/floored for homonymy, with more intermediate mass for polysemy?

## 2. Why this needs no new model calls

DWUG rates usage pairs of the **same target lemma**; the v1 probe already collected each panel model's graded relatedness rating (`durel` 1–4 and `cont` 0–100) for all 200 pairs across 43 lemmas. The only thing v1 lacked was the **polysemy/homonymy label per lemma** (DWUG does not carry it; it is a design-added layer — see [`resource/dwug-usage-graphs`](../../wiki/base/resources/dwug-usage-graphs.md) "What it cannot ground"). v2 adds exactly that layer and re-reads the existing ratings split by it.

## 3. The stratification (gate Q2 method, instantiated for the no-WordNet/no-compute constraint)

The ratified gate fixed the **method** as a "WordNet lexicographer-file + hypernym + etymology rule; ambiguous lemmas excluded." **WordNet (nltk) is not installed offline and no ML libraries are available** (the session's hard constraint). The gate explicitly authorized the fallback already in its text — "a dictionary/Wiktionary etymology" cross-check — and Tom's standing delegation covers fixing this rigorously and recording it. So v2 uses a **pre-registered etymology-grounded rule** over two standard references (**Etymonline** and **English Wiktionary**), applied **blind to the per-pair model ratings**:

- **HOMONYM** — the lemma has **≥2 distinct etymological origins** (separate Etymonline headwords, e.g. *ball (n.1)* vs *ball (n.2)*; or separate Wiktionary "Etymology N" sections with unrelated roots) **whose senses are BOTH common/general in modern American English prose** — so the corpus (CCOHA) plausibly contains genuine cross-etymon usage pairs. (e.g. *ball*: round-object/Germanic vs dance/Romance.)
- **POLYSEMY** — the lemma has **exactly one** etymological origin (all senses share a root, related by metaphor/metonymy/specialization), **OR** has a rare/archaic/narrowly-technical second origin that is not part of general prose (functionally single-origin in the register the corpus samples — e.g. *ounce* weight vs the rare snow-leopard sense; *bar* rod/counter vs the technical pressure unit).
- **EXCLUDED (AMBIGUOUS)** — references genuinely disagree on shared-vs-distinct origin, or it is a true borderline call. **Dropped, not force-labelled** (the gate's "genuinely ambiguous lemmas are flagged and EXCLUDED" rule). Excluded lemmas are recorded with their reason so the exclusion set is auditable.

Each HOMONYM/AMBIGUOUS call is backed by a **quoted etymological statement** (root + origin language) in the run README, so the stratification is checkable and demonstrably etymology-driven, not result-driven. The stratification is committed as `stratification.csv` and **sha256-frozen before the analysis is run**. It is stored **separate from the DWUG files** (CC BY-ND — no modified-dataset redistribution).

## 4. Indicators (frozen before computing; report-the-number, no pass bar)

For each model × framing (`durel`, `cont`), `analyze.py` computes:

- **(b1) within-stratum monotonicity** — Spearman(model rating, human DURel) **separately** for homonym-lemma and polysemy-lemma pairs. A decomposition/sanity of the v1 positive: does the gradience hold in both regimes?
- **(b2) the clause-(b) contrast — discreteness/floor concentration**, matched on the human signal so a raw "homonyms are simply more unrelated" difference is not mistaken for discreteness:
  - mean model rating per (stratum × human-level) cell, and the **homonym − polysemy gap within each human level** (a **negative** gap = homonyms rated lower at *matched* human relatedness = the predicted discreteness/floor);
  - among **low-human pairs** (human_median ≤ 2.0), the **%-at-model-floor** and mean rating by stratum (homonym predicted lower mean / more floor mass).
- **(b3) intermediate-mass precondition (model-free)** — the human DURel distribution by stratum: clause (b) presupposes homonym lemmas are more **bimodal** (mass at 1 and 4, thin middle) than polysemy lemmas. Reported as each stratum's share of pairs in the intermediate human band (2..3) vs the extremes.
- **Uncertainty** on the headline (b2) gap: a **label-permutation test** that shuffles the stratum labels across **whole lemmas** (preserving the per-lemma cluster structure), giving a null for the matched-human gap.

No threshold is tuned after computing. **A clean null — no separable regime, polysemy treated as just-another-homonym — is a first-class result** (charter §2.6 / the conjecture's "discrete-sense collapse" branch), and given the small per-stratum N it is a live and unembarrassing outcome.

## 5. Honest limits (carried into the result)

- **This is a re-analysis, not a fresh pre-registration.** The v1 ratings were already seen (the v1 result is written). The no-retuning discipline here is: the **stratification is etymology-driven and frozen before this pass**, and the **statistics are fixed before computing**; the stratification was built without consulting the per-pair model ratings. An adversarial pre-run critic checks the stratification is not result-driven.
- **Small N per stratum**, especially homonym pairs (homonymy is concentrated in a handful of lemmas at the low human end). Direction-of-effect only; wide uncertainty; the permutation p is the honest yardstick.
- **The contrast lives at the low end.** Homonymy in DWUG appears as genuinely-unrelated cross-etymon pairs (human ≈ 1), which v1 already flagged ("low end mixes homonymy"). v2 is partly a *clean-up* of that v1 caveat: it labels which low pairs are homonymy.
- **Etymology ≠ synchronic relatedness.** Etymological distinctness is the operational stand-in for "homonymy"; a few etymological homonyms may feel related to modern speakers (and vice versa). Disclosed; the AMBIGUOUS-exclusion rule absorbs the worst cases.
- **Behavioral, not representational** (inherits every v1 caveat): a rank/level contrast, not evidence about sense representations.

## 6. Harness / scope

- `stratification.csv` — committed, sha256-frozen; lemma → stratum + n_etymons + key_roots + source note.
- `analyze.py` — pure-Python; joins the frozen stratification to the v1 manifest + v1 raw preds; emits `raw/results.json`. Deterministic (fixed permutation seed). **No API.**
- Does not modify/redistribute DWUG; does not run the panel again; asserts no reference/extension claim.
