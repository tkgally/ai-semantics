---
type: design
id: lexical-sense-gradience-v1
title: lexical-sense-gradience probe v1 — does an LLM's same/different-sense signal track graded human usage-similarity (DWUG), with an intermediate regime for polysemy absent for homonymy, separable from a context-similarity shadow?
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: ready
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: operationalizes
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Experiment design v1 — lexical sense gradience (the lexical wedge)

> **Status: ready. Operationalization gate RESOLVED 2026-05-30** ([`decisions/resolved/lexical-sense-gradience-operationalization`](../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md), ratified under Tom's standing delegation, within the no-local-compute constraint). The four measures are now **fixed before any probe**: **Q1** instrument = behavioral panel as a DURel annotator (verbatim 4-point scale) + a 0–100 continuous framing, both pre-registered (small-model lane deferred — needs compute); **Q2** polysemy/homonymy stratification = WordNet-grounded rule, run as a **separate later probe (v2)**, *not* bundled into v1 (so the contestable layer never touches the clean monotonicity test); **Q3** context-similarity control = content-token lexical overlap (frozen primary), embedding cosine secondary-if-available; **Q4** synchronic filter = within-period pairs only (verified amply feasible: 22,393 within-period pairs across all 4 DURel levels). **v1 scope = P1 (monotonicity) + P3 (context-similarity control).** DWUG was independently verified 2026-05-30 ([`resource/dwug-usage-graphs`](../../wiki/base/resources/dwug-usage-graphs.md), VERDICT: YES-WITH-CAVEATS); `dwug_en.zip` v3.0.0 was downloaded + inspected this session (format confirmed: per-lemma `uses.csv` [context + period + target offsets] + `judgments.csv` [per-annotator DURel 1–4]).
>
> **Data/licence (decided with the gate):** DWUG is CC BY-ND 4.0 over copyrighted CCOHA text; the project commits the reproducible **recipe** + an identifier/rating **manifest**, never the raw archive or the corpus sentences (gitignored, local-only during the run). See the resolved decision's "Data/licence handling".

This is the project's **first lexical (non-grammatical) probe design**. It operationalizes [`conjecture/lexical-sense-gradience`](../../wiki/findings/conjectures/lexical-sense-gradience.md) — that an LLM's same/different-sense behavior is *monotonic in human-rated usage similarity*, with an *intermediate regime for polysemy* absent for homonymy, *separable from a context-similarity shadow*. Every prior finding is constructional; this opens the lexical axis the charter names as under-used.

## 1. Anchor — what DWUG supplies (verified)

[`resource/dwug-usage-graphs`](../../wiki/base/resources/dwug-usage-graphs.md) (DWUG EN, Schlechtweg et al. 2021; Zenodo 14028531; CC BY-ND 4.0). The load-bearing feature, verified from the primary Table 3 on 2026-05-30:

- **Graded, multi-rater human usage-similarity judgments** on the 4-point DURel scale — verbatim "4: Identical, 3: Closely Related, 2: Distantly Related, 1: Unrelated" (plus "Cannot decide" = 0) — over pairs of usages of the **same target word**. 40 EN lemmas, ~29k judged pairs (2021 paper; v3.0.0 archive ~69k), 9 EN annotators, ρ≈.69 / α≈.61.
- The paper notes annotators "make frequent use of the intermediate levels of the scale ('2','3')" — exactly the graded middle the conjecture's intermediate-regime clause needs.

This is the property no binary set (WiC) has. CC BY-ND permits analysis + verbatim mirroring; it forbids distributing a *modified* version (so any polysemy/homonymy stratification layer is kept **separate** from the raw DWUG files — see §6).

**What DWUG does NOT supply (and the design must add):** (i) a polysemy-vs-homonymy tag per lemma/pair (prediction 2 needs a stratification step, §3); (ii) a synchronic-only pair subset (DWUG mixes two CCOHA periods 1810–1860 / 1960–2010, so within-period pairs must be filtered, §2); (iii) any reference/extension signal (it bears on `referential.sense`, not `referential.reference`).

## 2. Data preparation (frozen before any probe)

1. **Mirror** `dwug_en.zip` verbatim into `experiments/data/dwug/` (CC BY-ND permits; do not modify the archive). Record the sha256.
2. **Inspect** the judgment-level format (usage-pair × annotator × DURel rating) and the per-usage time-period metadata.
3. **Synchronic filter (gate Q4):** retain only usage pairs whose two usages are from the **same** time period (a within-period pair), so the gradience anchor is synchronic, not confounded by diachronic change. Freeze the filtered pair list (sha256) before any model call.
4. **Aggregate** each retained pair to a median (or mean) human DURel rating across annotators; keep the inter-annotator spread as a per-pair reliability weight.

## 3. Polysemy / homonymy stratification (gate Q2 — NOT yet fixed)

Prediction 2 (intermediate regime for polysemy, floor for homonymy) needs each retained lemma (or pair) labelled **polysemous** (related senses) vs **homonymous** (discrete unrelated senses). DWUG does not carry this. Candidate sources, to be fixed by the operationalization decision:

- **WordNet-based:** a lemma whose competing senses fall under unrelated coarse hypernym roots (or are flagged as distinct homographs/etymologies) → homonymy; a lemma whose senses share a near hypernym / are marked related → polysemy.
- **Dictionary-based:** a lexicographer's split into numbered senses (polysemy, one headword) vs separate headwords (homonymy).
- **Manual expert tag** of the 40 DWUG EN lemmas (small N; defensible but introduces a judgment the design must pre-register).

Whichever is chosen is **frozen with the item set**; the stratification layer is stored separately from the raw DWUG files (CC BY-ND, §6).

## 4. Instrument (gate Q1 — NOT yet fixed)

Two loci, as the conjecture's Notes flag — they are different instruments and may disagree:

- **Behavioral panel (provisional default).** Present the two usage sentences for a target word to the 3-family panel ([`config/models.md`](../../config/models.md)) and elicit a same-sense / different-sense judgment **with a graded confidence** (e.g. a 1–4 or 0–100 relatedness rating, or a calibrated same/different + confidence). Temperature 0; logprob-free → runs on the existing panel (no local compute). This mirrors every prior probe and is **not** blocked the way the AANN logprob/small-model lane is.
- **Small-model representation-similarity lane.** Cosine between the target word's contextual representations in the two sentences, as a continuous same-sense signal. This is the cleaner "distributional" instrument but **needs local compute** (the same blocker that holds AANN, [`decisions/open/aann-panel-logprob-blocker`](../../wiki/decisions/open/aann-panel-logprob-blocker.md)) — OpenRouter exposes no usable hidden states.

The gate must pick one (or commit to both as separate, pre-registered instruments). The provisional default is the **behavioral panel**, with the small-model lane deferred until local compute is available.

## 5. Context-similarity control (gate Q3 — the design's spine)

Clause (c) of the conjecture is load-bearing: apparent gradience must **not** reduce to the model tracking how similar the two *sentences* are. So context overlap is measured **independently** of the model's sense signal (gate Q3 fixes which measure): lexical overlap (Jaccard / token F1 of the two sentences minus the target word) and/or sentence-embedding cosine. Then:

- **Partial correlation:** Spearman of (model same-sense signal, human DURel rating) **controlling for** the context-similarity measure. If the relation to human sense-relatedness survives, that supports graded-sense tracking; if it goes flat once context similarity is partialled out, that is the distributional shadow (hypothesis 3).
- **Matched-context subset:** report the monotonicity within strata of roughly-constant context overlap.

## 6. Indicators and reading rules (frozen with the item set; no pass bar that manufactures a result)

- **P1 monotonicity:** Spearman ρ between the model same-sense signal and the median human DURel rating, per model. Report-the-correlation (with CI), not a pass/fail bar. A reliably positive, non-step ρ supports graded tracking; a step function (high then cliff at one DURel level) supports discrete-collapse.
- **P2 intermediate regime:** the distribution of the model signal for **polysemous related-but-distinct** pairs vs **homonym** pairs. Separability (the polysemy distribution sits in an intermediate band; homonyms cluster at the "different" floor) supports P2; polysemy treated as just-another-homonym is discrete-collapse.
- **P3 context-similarity control:** the partial correlation of §5. **This is the discriminating prediction** — P1+P2 holding while P3 fails reads as distributional shadow, not graded-sense tracking.
- **P5 binary cross-check:** agreement of the panel's same/different calls with **WiC** binary labels (Pilehvar & Camacho-Collados 2019, CC BY-NC 4.0; binary, the discrete cross-check named in the conjecture). Baseline agreement on WiC *without* gradience on DWUG = discrete-collapse.

No threshold is tuned after the run. A clean collapse or a vanished-under-control result is a **first-class null** (charter §2.6), not a failure to retune around.

## 7. Human anchor — scope

The **monotonicity / intermediate-regime** arms are anchored to DWUG's graded human DURel ratings ([`resource/dwug-usage-graphs`](../../wiki/base/resources/dwug-usage-graphs.md)) — a genuine human-comparison signal. The **polysemy/homonymy stratification** is a design-added layer (§3), not a DWUG annotation; the result must label it as such and not claim DWUG tags the split. The binary cross-check is anchored to WiC. No human label is invented.

## 8. Harness, budget, scope

- Reuses the behavioral build→freeze→probe→analyze pipeline (temperature 0, logprob-free greedy parse) of the argument-structure probes; new `build_items.py` emits the DWUG-derived within-period pair set + the frozen stratification layer; new `analyze.py` computes the Spearman / partial-correlation / separability statistics.
- **Pre-flight cost:** within-period DWUG EN pairs are on the order of a few thousand; sampling a balanced ~150–300 pairs (across DURel levels × polysemy/homonymy) × 1 graded-rating call × 3 models is well under the $5 single-run flag in [`config/budget.md`](../../config/budget.md). Pre-flight before running.
- Does **not** build the small-model lane (local compute), does **not** distribute a modified DWUG file (CC BY-ND), does **not** assert reference/extension claims.

## 9. Handoff hooks

1. **Ratify** [`decisions/open/lexical-sense-gradience-operationalization`](../../wiki/decisions/open/lexical-sense-gradience-operationalization.md) (instrument / stratification source / context-similarity measure / synchronic filter) — fixes the yardstick before any run.
2. Mirror + inspect `dwug_en.zip` (§2); confirm the judgment-level format and the period metadata; freeze the within-period pair list (sha256).
3. Build + freeze the stratification layer (§3) separately from the raw files.
4. Build + freeze `items.csv`; run; review; only then promote a result.
