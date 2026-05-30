# Run record — lexical v2: polysemy vs homonymy (clause b), a re-analysis (2026-05-30)

**Date:** 2026-05-30
**Type:** re-analysis of the lexical-v1 ratings under a frozen etymological stratification — **NO new API spend** ($0.00).
**Design (frozen):** [`design/lexical-polysemy-homonymy-v2`](../../designs/lexical-polysemy-homonymy-v2.md)
**Governing gate:** [`decisions/resolved/lexical-sense-gradience-operationalization`](../../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md) Q2 (polysemy/homonymy stratification, staged to a separate v2)
**Conjecture probed:** [`conjecture/lexical-sense-gradience`](../../../wiki/findings/conjectures/lexical-sense-gradience.md) clause (b) / prediction 2
**Anchor:** [`resource/dwug-usage-graphs`](../../../wiki/base/resources/dwug-usage-graphs.md) (DWUG EN; human DURel gold reused from v1)
**Result page:** [`result/lexical-polysemy-homonymy-v2`](../../../wiki/findings/results/lexical-polysemy-homonymy-v2.md)

## What ran

The clause-(b) arm v1 deferred: does the panel treat **polysemy** (one etymological root, related senses) with an **intermediate** regime but **homonymy** (distinct unrelated roots sharing a spelling) as **discrete / floored**? It re-uses the already-collected v1 model ratings (`durel`, `cont`) for all 200 DWUG pairs across 43 lemmas (run [`2026-05-30-lexical-sense-gradience-probe-v1`](../2026-05-30-lexical-sense-gradience-probe-v1/README.md)), split by a frozen etymological stratification of the 43 lemmas.

## The frozen stratification (gate Q2, etymology fallback)

WordNet (nltk) is not installed offline and no ML libs are available (session hard constraint). The gate's Q2 method explicitly authorized a **dictionary/Wiktionary etymology** cross-check as the rule; Tom's standing delegation covers fixing it rigorously. So the stratification is a pre-registered etymology rule over **Etymonline + English Wiktionary** (retrieved 2026-05-30), applied **blind to the per-pair model ratings**, with the gate's "genuinely ambiguous lemmas EXCLUDED, not force-labelled" discipline:

- **HOMONYM** — ≥2 distinct etymological origins (separate Etymonline headwords / unrelated Wiktionary "Etymology N" sections) whose senses are **both common in general modern English**.
- **POLYSEMY** — one etymological origin, OR a 2nd origin that is rare/archaic/narrowly-technical (functionally single-origin in general prose).
- **EXCLUDED (AMBIGUOUS)** — references disagree on shared-vs-distinct origin, or a true borderline.

`stratification.csv` (committed; **sha256 `afbf4cc683f9a7d9d6a4ffbb50742a2b461129dc682d9a45d45c99d482fddfa4`**, frozen before `analyze.py` was run; kept separate from the DWUG files per CC BY-ND): **HOMONYM = 3** (`ball`, `plane`, `prop`), **POLYSEMY = 36**, **AMBIGUOUS/excluded = 4** (`graft`, `heel`, `ounce`, `rally`, `tip` were evaluated; the committed file marks `graft/heel/rally/tip`-class borderlines AMBIGUOUS and demotes the rare-2nd-origin cases to POLYSEMY per the rule — see the file for each call + its key roots).

### Decisive etymological evidence for the HOMONYM calls (quoted)

- **ball** — Etymonline `ball (n.1)` "round object … from cognate Old Norse *bollr* 'ball,' from Proto-Germanic *\*balluz*" (PIE *\*bhel-* 'to swell') vs `ball (n.2)` "dancing party … from French, from Old French *baller* 'to dance,' from Late Latin *ballare* … from Greek *ballizein*" (PIE *\*gwele-* 'to throw'). Two unrelated roots; both everyday.
- **plane** — Etymonline/Wiktionary: flat-surface/tool/aircraft from Latin *planum*/*planus* vs **plane-tree** "from Old French *plane*, from Latin *platanus*, from Ancient Greek *πλάτανος*." Latin *planus* family vs Greek *platanos* — distinct origins, both in general prose.
- **prop** — Etymonline `prop (n.1)` "a support … probably from Middle Dutch *proppe* 'vine prop, support'" vs `prop (n.2)` "object used in a play, 1898 … shortened form of *properties* … see *property*" (← Latin *proprius*). Support vs stage-prop: unrelated origins, both general.

A comprehensive dual-source (Etymonline + Wiktionary) classification of all 43 lemmas was produced by an independent research pass; it confirms the same confident HOMONYM set {ball, plane, prop} (flagging `bit` — computing-bit coined 1948 from "binary digit" — as a borderline 4th, deliberately excluded here as both anachronistic for the 1810–2010 CCOHA corpus register and "the weakest of the homonyms" per the classifier).

## Pre-registration / no-retuning

- This is a **re-analysis**, not a fresh pre-registration: the v1 ratings were already seen. The discipline (stated in the design + result): the **stratification is etymology-driven and frozen before this pass** (built without consulting the per-pair model ratings), and the **analysis statistics are fixed before computing**. An independent adversarial pre-run critic reviewed the stratification for result-driven labelling.
- Floor thresholds (`durel`==1, `cont`<=20), `LOW_CUT`=2.0, intermediate band [2,3], permutation seed and N=5000 are all in `analyze.py` constants, fixed before the run.

## Files

- `stratification.csv` — committed, sha256-frozen; lemma → stratum + n_general_etymons + key_roots + source note.
- `analyze.py` — pure-Python (no numpy); joins the frozen stratification to the v1 manifest + v1 raw preds; b1 within-stratum Spearman, b2 matched-human gap + low-end floor mass + whole-lemma label-permutation p, b3 model-free human-structure precondition; emits `raw/results.json`. **No API.**
- `raw/results.json` — computed statistics.

## Headline numbers (see result page for interpretation)

Stratification: HOMONYM 3 lemmas / 13 pairs, POLYSEMY 36 lemmas / 158 pairs (171 of 200 pairs used; 29 in excluded/ambiguous lemmas).

- **b3 precondition (model-free):** homonym pairs are concentrated at the human floor (mean human 1.5; 77% at level ≤2, only 8% intermediate) vs polysemy (mean 2.54; 42% low, 46% intermediate). The homonym sample *is* more floored in the **human** gold — the precondition holds but is partly built into which DWUG pairs are cross-etymon.
- **b1 within-stratum monotonicity:** the v1 gradience holds in **both** strata (e.g. cont: claude H 0.75 / P 0.69; gemini H 1.00 / P 0.81) — no stratum is non-monotone.
- **b2 the clause-(b) contrast — directional but not significant.** Matched on the human level, homonym pairs are rated **lower** than polysemy pairs at the same human relatedness (cont matched-gap: claude −5.6, gpt −12.0, gemini −9.4; all negative = homonyms more floored). Low-end (human ≤2): homonym mean **0–11** with floor-fraction **0.8–1.0**, vs polysemy mean **24–32** with floor-fraction **0.5–0.74**. **But** the whole-lemma label-permutation test is **non-significant** (two-sided p 0.23–0.86; only 3 homonym lemmas), so the contrast is a **direction-of-effect, not an established separable regime**.

## Post-run verification

Independent read-only number-verification agent recomputed every headline figure (within-stratum ρ, matched-human gap + per-level gaps, low-end mean + floor-fraction, b3 structure) from `raw/*.json` + `manifest.csv` + `stratification.csv` with its own from-scratch Spearman → **CLEAN — all figures reproduce within rounding.** It independently flagged that the largest-magnitude matched gap is **gpt-5.4-mini's**, not gemini's (consistent with results.json; corrects any "gemini largest" narrative).
