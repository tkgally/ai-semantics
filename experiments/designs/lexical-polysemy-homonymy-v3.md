---
type: design
id: lexical-polysemy-homonymy-v3
title: lexical-sense-gradience v3 — the polysemy-vs-homonymy DISCRETENESS test on a homonymy-enriched WiC subset, with WiC's binary same/different label as the human anchor (the clean clause-(b) test the DWUG null pointed to)
meaning-senses:
  - referential
  - distributional
  - human-comparison
status: ready
anchor: resource/wic-word-in-context
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: operationalizes
    target: conjecture/lexical-sense-gradience
  - rel: refines
    target: design/lexical-polysemy-homonymy-v2
  - rel: depends-on
    target: resource/wic-word-in-context
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Experiment design v3 — polysemy vs homonymy discreteness, on a homonymy-enriched WiC subset

> **Status: ready (pending the binary-anchor sub-decision flagged in §8).** This is the **clean re-run of clause (b)** that [`result/lexical-polysemy-homonymy-v2`](../../wiki/findings/results/lexical-polysemy-homonymy-v2.md) showed DWUG EN cannot carry: the v2 null was a **design gap**, not a falsification — DWUG EN held only **3 clean general-English homonym lemmas / 16 pairs**, no separable discreteness regime could exist, and every test was non-significant (p 0.29–1.0). Tom's steer this round (decision 3a): *finish the lexical open question, clause (b), with "a homonymy-enriched, human-rated contrast (e.g. WiC's binary same/different sense labels as the cross-check …). Reuse existing human resources only."* v3 does exactly that: it runs the **same ratified graded-relatedness instrument** (gate Q1) on a **homonymy-enriched WiC subset** and uses **WiC's binary same/different label** ([`resource/wic-word-in-context`](../../wiki/base/resources/wic-word-in-context.md), CC BY-NC 4.0) as the human anchor.

## 1. What clause (b) predicts, and why WiC fixes the v2 gap

[`conjecture/lexical-sense-gradience`](../../wiki/findings/conjectures/lexical-sense-gradience.md) prediction 2 — the conjecture's *distinctive* still-open bet (clause a+c are supported by v1; clause b is "not established", a null at the DWUG anchor):

> "there is an **intermediate regime for related-but-distinct (polysemous) usages** that is **absent for homonyms** (homonym pairs sit at the 'different' floor with little intermediate mass); the distributions for the two regimes are separable — polysemy is *not* treated as just-another-homonym."

The v2 null diagnosed the precise obstruction (b3 precondition failed): DWUG EN's homonym lemmas were too few and were **not** more bimodal than its polysemy lemmas, so there was no separable distribution to detect. WiC removes both obstructions:

- It is **large and homonymy-enriched.** 7,466 items, 2,345 distinct target words, **exactly 50/50** same/different (T/F) per split — and its different-sense (**F**) negatives are deliberately pruned of the *closest* polyseme pairs ("removed all pairs whose senses were first degree connections … sister senses … same supersense", WiC paper, verbatim in the resource page). So WiC's **F** pool concentrates on clearly-distinct sense splits — exactly the clear-homonym contrast DWUG lacked.
- It supplies a **per-item binary human sense label** (T = same sense, F = different sense), inventory-derived from WordNet/VerbNet/Wiktionary. That is the human anchor.

**The instrument is the v1/v2 graded panel; the anchor is WiC binary.** We run the ratified DURel-style graded-relatedness panel (§3) on WiC's two contexts per item, then ask whether the *model's graded relatedness rating* separates WiC's binary classes **better for homonyms than for polysemes** — the discreteness fingerprint.

## 2. The discreteness prediction, made precise (frozen before any model call)

Clause (b) becomes two pre-registered predictions over the model's graded relatedness rating *r* (per model × framing):

- **(P-b-i) A separable low mode for homonyms.** Among **different-sense (F)** items, **homonym** pairs (etymologically unrelated senses) sit at/near the model's "unrelated" floor — a **low mode** — while **polyseme** different-sense pairs spread **graded** above the floor. Operationally: the distribution of *r* over homonym-F items is more concentrated at the floor (lower mean, higher floor-fraction, more bimodal against the same-sense T items of the same words) than over polyseme-F items. This is the **bimodality/separation DWUG lacked** (v2 b3).
- **(P-b-ii) Larger same/different separation for homonyms.** The model rating separates WiC **T vs F** *better for homonyms than for polysemes*: a larger AUC (and a larger mean T−F gap) of *r* against the binary label within the homonym stratum than within the polyseme stratum. Intuition: homonym different-sense pairs are unrelated and easy to floor; polyseme different-sense pairs are distantly-related and harder to push to the floor, compressing the T−F gap.

**Nulls (first-class, charter §2.6 / the conjecture's "discrete-sense collapse" branch):**

- **(N1) No separable homonym mode.** Homonym-F items are *not* more floored/bimodal than polyseme-F items — the model treats homonymy as just-another-different-sense. (This is the discrete-collapse-absent reading; equally informative.)
- **(N2) Equal same/different separation.** AUC(T,F) and the mean T−F gap are statistically indistinguishable between the homonym and polyseme strata — the model's binary sense discrimination does not depend on the polysemy/homonymy distinction.

A clean N1+N2 is a publishable **null** that *closes* clause (b) with adequate power (unlike v2, which closed it only as untestable-at-this-anchor). That is the point of v3: give clause (b) a fair, powered test.

## 3. Instrument — the SAME ratified graded panel (gate Q1, reused verbatim)

This reuses the operationalization gate already ratified ([`decisions/resolved/lexical-sense-gradience-operationalization`](../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md), Q1) — **no new instrument decision.** Each panel model ([`config/models.md`](../../config/models.md): claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash), at **temperature 0, logprob-free**, rates each WiC item's **two contexts** for the relatedness of the target word's meaning, under the **same pre-registered framings** v1 used:

- **`durel`** — the verbatim 4-point DURel scale (4 Identical / 3 Closely Related / 2 Distantly Related / 1 Unrelated), the primary graded signal;
- **`cont`** — a 0–100 continuous relatedness rating (instrument robustness).

(v1's third framing `topic` — the context-similarity control — is **optional** in v3: clause (c) is already supported by v1, and the discreteness test of §2 is about how the rating separates the *binary* classes, not about a context shadow. To keep cost down and scope tight, v3 runs `durel` + `cont` only; a `topic` arm may be added later if a context-shadow concern is raised for the WiC items specifically. This is a scope choice within the ratified gate, not a new gate.)

The target word is marked in each context by its WiC-supplied token index (the resource page notes WiC contexts are whitespace-tokenized and the index is a token index; the builder marks the target by index with «guillemets», matching the v1 marking convention, and de-tokenizes lightly for readability). The prompt is the v1 DURel-annotator prompt, **unchanged** except for substituting the WiC contexts.

## 4. Item selection — the homonymy-enriched, frozen WiC subset

The build (`build_items.py`) is **fully reproducible** (download URL + sha256 pinned; deterministic seed) and emits a **frozen item table** that is sha256'd **before any model call** (the orchestrator runs the probe later — see §7).

1. **Source.** Download `WiC_dataset.zip` from https://pilehvar.github.io/wic/package/WiC_dataset.zip (this distribution ships test gold labels; sha256 `f1a2fb67d903c5b9b1180f1035d4228f7c0254e8f5f868d556235457046bd4b2` pinned). Use **train + dev + test** (all carry gold here). CC BY-NC 4.0; commit only the recipe + an id/gold/stratum manifest, **not** the corpus example sentences (the resource page's conservative posture).
2. **Polysemy/homonymy stratification per target word** — the layer WiC does not carry (resource page "What it cannot ground"). **Reuse the v2 etymological-fallback rule verbatim** (gate Q2 authorized this fallback under the no-WordNet constraint; the rule and its `stratification.csv` format already exist at `experiments/runs/2026-05-30-lexical-polysemy-homonymy-v2/stratification.csv`):
   - **HOMONYM** — the target has **≥2 distinct etymological origins both common/general in modern English** (separate Etymonline headwords / unrelated Wiktionary "Etymology N" sections), so genuine cross-etymon different-sense pairs exist (e.g. *ball*, *plane*, *bat*, *bank*, *crane*, *pitch*, *spring*, *bar*, *bow*…).
   - **POLYSEME** — exactly one general-register origin (all senses one root, related by metaphor/metonymy/specialization), or a second origin that is rare/archaic/narrowly-technical in general prose.
   - **AMBIGUOUS → EXCLUDED**, not force-labelled (references disagree on shared-vs-distinct origin, or the lemma conflates a distinct-POS homograph). Recorded with reason, auditable.
   - Each HOMONYM/AMBIGUOUS call is backed by a **quoted etymological statement** in the run README, so the stratification is demonstrably etymology-driven, **applied blind to the model ratings**. *(If local compute returns and WordNet/nltk becomes available, the gate's preferred WordNet lexicographer-file + hypernym rule may replace the etymological fallback — but that is the same gate Q2 method, not a new decision; freeze whichever is used.)*
   - **Crucially, in v3 the homonym judgment can be applied at the WiC PAIR level, not just the lemma level** — because WiC gives a per-pair same/different label and (via WordNet/BabelNet provenance) two specific senses. A pair is a **homonym different-sense pair** only if it is labelled **F** *and* its two senses fall in the target word's distinct etymological strata; a **polyseme different-sense pair** is **F** with both senses in one etymological origin. (This pair-level labelling is the cleaner design v2 said DWUG could not supply — "a pair-level (not lemma-level) homonymy label would be the cleaner design.") Where the WiC release does not expose the underlying sense ids, fall back to the lemma-level label and record that the homonym stratum is lemma-level; **state which granularity was achievable** in the result.
3. **Enrichment + balance.** Select all clean HOMONYM target words with ≥1 F item and ≥1 T item, plus a matched POLYSEME sample, balancing on **POS (N/V)** and on **WiC label (T/F)** within each stratum, so neither stratum is confounded with POS or with base rate. Target a frozen subset of roughly **N ≈ 600 items** (see §6 for the count + cost rationale): ~150 homonym-F + ~150 homonym-T + ~150 polyseme-F + ~150 polyseme-T, drawn to maximize distinct homonym target words (the binding scarce resource, as in v2). The exact N is whatever the homonym pool supports after the etymological filter — recorded at freeze, not tuned to a result.
4. **Controls (ratified, reused).** (i) **content-token lexical overlap** between the two contexts minus the target (Jaccard / token-F1), computed independently of any model — the surface control from gate Q3; reported per stratum so a "homonyms simply share fewer words" confound is visible. (ii) the model's own **topic similarity** is the deeper control but is **deferred** (see §3); clause (c) is already supported by v1 and is not what v3 tests.
5. **Freeze.** `build_items.py` emits `manifest.csv` (WiC id + target + POS + token indices + binary gold + stratum + overlap covariate; **no corpus sentences in the wiki**) and `stratification.csv` (target → stratum + n_etymons + key_roots + quoted source). **sha256 both, recorded in the run README, BEFORE any probe call.** The full context text lives only in a gitignored local extraction during the run.

## 5. Indicators & reading rules (frozen before computing; report-the-number, NO pass bar, NO post-hoc threshold)

For each model × framing (`durel`, `cont`), `analyze.py` computes:

- **(b-i) separable-low-mode statistics** over **F (different-sense)** items: mean *r* and **floor-fraction** (share at the bottom rating: `durel`=1, or `cont` ≤ a pre-registered floor band fixed *before* the run, e.g. ≤10) by stratum; and a **bimodality / separation** read — the homonym-F vs homonym-T separation against the polyseme-F vs polyseme-T separation (does homonymy carve a cleaner two-mode structure?). The homonym−polyseme **floor-fraction gap** among F items is the headline for P-b-i.
- **(b-ii) same/different separation by stratum:** **AUC** of *r* against the binary WiC label (T vs F), computed **separately** within the homonym stratum and the polyseme stratum, plus the mean **T−F gap** in each. The headline for P-b-ii is **AUC_homonym − AUC_polyseme** (and the gap difference). Predicted **positive**.
- **Matched control:** the same AUC/gap difference re-computed on the **lexical-overlap-matched** subset (strata matched on overlap quantiles), so the separation difference is not a surface-overlap artifact.
- **Uncertainty:** a **label-permutation test** that shuffles the polysemy/homonymy stratum labels across **whole target words** (preserving per-word clustering), giving a null distribution for both headline differences (the floor-fraction gap and the AUC difference). The permutation p is the honest yardstick (as in v2). Bootstrap CIs on AUC.
- **Within-stratum sanity:** AUC and mean T−F gap reported for each stratum on its own, so "homonyms separate better" is not read off a single noisy stratum.

**No threshold is tuned after seeing the model ratings.** The `cont` floor band, the AUC/permutation machinery, the strata definitions, and the matched-overlap control are **all fixed at freeze**. The discreteness claim is supported only if **AUC_homonym − AUC_polyseme > 0 with permutation p below the pre-registered level AND a separable homonym-F low mode**, both surviving the overlap match. N1/N2 (no difference) is a first-class null.

## 6. Sample size + pre-flight cost estimate

- **Items:** target **N ≈ 600** WiC items (the homonym pool after the etymological filter is the binding constraint; v2 found ~3 clean homonyms in DWUG's 40 lemmas, but WiC's 2,345 distinct targets contain far more — classic homographs like *ball/bat/bank/bar/bow/crane/pitch/plane/pole/spring/seal/bass/club/date/light/match/mole/palm/pitcher/sole* are common in WordNet/VerbNet and survive the etymological rule). If the clean homonym pool yields fewer F+T items than ~300, **reduce N proportionally and record it at freeze** rather than padding with AMBIGUOUS lemmas.
- **Calls:** N items × **2 framings** (`durel`, `cont`) × **3 models** = **600 × 2 × 3 = 3,600 calls**.
- **Cost estimate (via [`experiments/lib/openrouter.py`](../lib/openrouter.py), billed `usage.cost`):** v1 ran **1,800 calls for $3.134 billed** (3 framings × 200 items × 3 models), dominated by gemini reasoning tokens (~$2.6 of it). v3 at 3,600 calls but **2 framings** is ≈ (3,600/1,800)×(2/3) = **1.33× the v1 per-call-count work** → a point estimate of **≈ $4.2 billed** (claude ≈ $0.6, gpt ≈ $0.15, gemini ≈ $3.5). **This is under the $5 single-run flag but close to it** ([`config/budget.md`](../../config/budget.md)); the gemini reasoning-token cost is the swing factor. **Pre-flight mitigations to keep it clean:** (a) cap N at the homonym pool (likely < 600, lowering cost); (b) if a billed pre-flight on a 30-item slice projects > $5, drop to **1 framing (`durel` only)** — still a valid discreteness test — and record the reduction. **Flag in NEXT.md before running if the 30-item pre-flight projects > $5.**
- **Re-use note:** v3 needs **new** model calls (WiC items were never rated), unlike v2 which re-analyzed v1 ratings at $0. So v3 carries real spend; budget accordingly.

## 7. Freeze / run protocol (orchestrator runs the probe later)

1. `build_items.py` downloads WiC (gitignored), applies the etymological stratification + enrichment/balance, emits `manifest.csv` + `stratification.csv`, prints both sha256s. **Freeze = both sha256s recorded in the run README before any model call.**
2. **Adversarial pre-run pass** (independent, read-only) on the stratification (is any homonym/polyseme call result-driven? are the etymology quotes real? is the AMBIGUOUS-exclusion applied uniformly?) and the prompts/analysis — the same gate the v2 design used, which caught the `lass`/`prop` mislabels there.
3. Pre-flight cost on a 30-item slice (billed); if > $5 projected, reduce framings/N and re-record; flag in NEXT.md if still > $5.
4. Run the panel (temp 0, logprob-free); commit model outputs + gold + stratum only (no corpus sentences).
5. `analyze.py` (pure-Python, deterministic seed) computes §5; write the result page, **leading with the null if N1/N2 hold**.

## 8. Human anchor scope + the binary-anchor sub-decision (RECOMMENDED, not created here)

- **The anchor is WiC's BINARY same/different label** ([`resource/wic-word-in-context`](../../wiki/base/resources/wic-word-in-context.md)). **Scope the human-comparison claim to a binary same/different separation** (AUC, T−F gap) — **NOT** a graded DURel-median correlation. WiC has no graded human axis (resource page "What it cannot ground"); v3 must never claim "the model is monotonic in human-rated relatedness" against WiC. The graded-monotonicity claim stays anchored to DWUG ([`resource/dwug-usage-graphs`](../../wiki/base/resources/dwug-usage-graphs.md)) via v1. v3's model rating is graded; the *human* signal it is scored against is binary; the discreteness test lives in how the graded model rating separates the binary human classes by stratum.
- **The polysemy/homonymy stratification is a design-added layer**, not a WiC annotation (resource page); the result must label it as such.
- **Does this reuse the ratified gate, or need a new sub-decision?** The **instrument (Q1), the stratification method (Q2), and the lexical-overlap control (Q3)** are reused **verbatim** from the resolved operationalization gate — **no new decision** on those. **But the gate was written for a GRADED anchor (DWUG) and a graded-median comparison.** v3 introduces a **binary** human anchor and a **binary-separation** comparison statistic (AUC against T/F) that the gate did not contemplate. That is a small but real new operationalization choice — *which human comparison statistic binds the result*. **Ratified this round by Tom's decision 3a** (2026-05-31): clause (b) "needs a homonymy-enriched, human-rated contrast (e.g. **WiC's binary same/different sense labels** as the cross-check …). Reuse existing human resources only." So the **binary WiC anchor is endorsed** and the human-comparison claim is **scoped to a binary same/different separation** (AUC / T−F gap by stratum, with whole-word permutation), explicitly **not** a graded-relatedness correlation; the homonym/polyseme stratification reuses the ratified Q2 method (etymological fallback, pair-level where WiC sense ids permit). **No separate open decision needed** — Tom's 3a covers the binary scope; the resolved operationalization gate covers the instrument + controls. (Recorded for the audit trail; promotion of a v3 *result* still goes through the normal pre/post-run adversarial passes.)

## 9. Honest limits (carried into the result)

- **Binary anchor, binary claim.** WiC grounds only a same/different separation; no graded-relatedness claim against WiC. (Restated — the central scope limit.)
- **WiC negatives are pruned of the closest polyseme pairs** (resource page, verbatim construction rule). This *helps* the homonym contrast but means the polyseme-F stratum is the *harder, more-separated* polyseme negatives, not the near-bridging cases — so a *null* (N1/N2) is a conservative outcome (the deck is mildly stacked toward finding a homonym/polyseme difference, since polyseme-F is already pruned toward clarity; a null is therefore strong). Disclosed.
- **Etymology ≠ synchronic relatedness; pair-level vs lemma-level.** Same caveat as v2; v3 improves on it where WiC exposes sense ids (pair-level homonymy), else falls back to lemma-level and says so.
- **Sense-inventory labels, not a rating panel.** WiC's T/F is lexicographer-inventory-derived, not an inter-annotator graded rating; "agreement with WiC" = agreement with the sense split.
- **Behavioral, not representational** (inherits every v1 caveat: single temp-0 run per model; logprob-free; English; the small-model representation lane stays deferred on local compute).
- **Real spend** (≈$4 billed, gemini-dominated), unlike the $0 v2 re-analysis.

## 10. Harness / scope

- `build_items.py` — downloads WiC (gitignored), applies stratification + enrichment/balance, emits `manifest.csv` + `stratification.csv`, prints sha256s. Reuses the v2 stratification format (`experiments/runs/2026-05-30-lexical-polysemy-homonymy-v2/stratification.csv`).
- `probe.py` — runner (`durel` + `cont` × 3 models); imports [`experiments/lib/openrouter.py`](../lib/openrouter.py) (billed `usage.cost`); reads the gitignored full text; commits model outputs + gold + stratum only.
- `analyze.py` — pure-Python: per-stratum AUC + T−F gap + floor-fraction + bimodality, overlap-matched re-computation, whole-word label-permutation null, bootstrap CIs. Deterministic (fixed seed). 
- Does not modify/redistribute WiC corpus text; asserts no reference/extension claim; does not build the small-model lane.
