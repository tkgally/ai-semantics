# Run record — lexical v2: polysemy vs homonymy (clause b), a re-analysis (2026-05-30)

**Date:** 2026-05-30
**Type:** re-analysis of the lexical-v1 ratings under a frozen etymological stratification — **NO new API spend** ($0.00).
**Design (frozen):** [`design/lexical-polysemy-homonymy-v2`](../../designs/lexical-polysemy-homonymy-v2.md)
**Governing gate:** [`decisions/resolved/lexical-sense-gradience-operationalization`](../../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md) Q2
**Conjecture probed:** [`conjecture/lexical-sense-gradience`](../../../wiki/findings/conjectures/lexical-sense-gradience.md) clause (b) / prediction 2
**Anchor:** [`resource/dwug-usage-graphs`](../../../wiki/base/resources/dwug-usage-graphs.md) (human DURel gold reused from v1)
**Result page:** [`result/lexical-polysemy-homonymy-v2`](../../../wiki/findings/results/lexical-polysemy-homonymy-v2.md)

## Outcome: a NULL / not-established

Clause (b) — that homonymy is treated as a discrete floor while polysemy keeps an intermediate regime — is **not established**. DWUG EN holds only **3 clean general-English homonym lemmas**; the matched-human gap is tiny/mixed-sign, every permutation p is non-significant (0.29–1.0), and the b3 bimodality precondition fails. See the result page for the full reading. The durable contribution is methodological (this anchor can't test clause b; a homonymy-enriched v3 is needed) plus cleaning up the v1 "low end mixes homonymy" caveat.

## What ran

Re-uses the already-collected v1 model ratings (`durel`, `cont`) for all 200 DWUG pairs across 43 lemmas (run [`2026-05-30-lexical-sense-gradience-probe-v1`](../2026-05-30-lexical-sense-gradience-probe-v1/README.md)), split by a frozen etymological stratification of the 43 lemmas.

## The frozen stratification (gate Q2, etymology fallback)

WordNet (nltk) is not installed offline and no ML libs are available (session hard constraint). The gate's Q2 method explicitly authorized a **dictionary/Wiktionary etymology** cross-check as the rule; Tom's standing delegation covers fixing it rigorously. The stratification is a pre-registered rule over **Etymonline + English Wiktionary** (retrieved 2026-05-30), applied **blind to the per-pair model ratings**, **uniformly**, with the gate's "genuinely ambiguous lemmas EXCLUDED, not force-labelled" discipline:

- **HOMONYM** — ≥2 distinct etymological origins (separate Etymonline headwords / unrelated Wiktionary "Etymology N" sections) whose senses are **both common in general modern English**.
- **POLYSEMY** — one etymological origin, OR a 2nd origin that is rare/archaic/narrowly-technical (functionally single-origin in general prose).
- **EXCLUDED (AMBIGUOUS)** — references disagree on shared-vs-distinct origin, a true borderline, **or a DWUG data-conflation** (one lemma id covering two unrelated words).

`stratification.csv` (committed; **sha256 below**, frozen before the final `analyze.py` run; kept separate from the DWUG files per CC BY-ND), per the corrected uniform rule:

- **HOMONYM = 3 lemmas** — `ball` (ON *bollr* round vs LL *ballare* dance), `plane` (L *planus* flat-surface/tool/aircraft vs Gk *platanos* tree), `prop` (MDu *proppe* support vs *property*-clip stage-prop). 16 pairs.
- **POLYSEMY = 35 lemmas** / 154 pairs.
- **AMBIGUOUS / EXCLUDED = 5** — `graft`, `heel`, `rally`, `tip` (disputed/hedged origins) and **`lass`** (the v1 S4 `lass`/`lassi` DWUG conflation — *not* an etymological homonym; `lass`=girl is single-origin, `lassi` is a different word lumped under the lemma — so excluded, not allowed to pad either stratum).

Per-lemma key roots + a source note (Etymonline / Wiktionary) are in `stratification.csv`.

### Correction history (adversarial pre-write critique)

An independent read-only critic reviewed the stratification + analysis before this page was finalized and forced four fixes — all applied:
1. **`lass` mis-filed HOMONYM → EXCLUDED.** `lass` (girl) is single-origin; `lassi` is a different word DWUG conflates under the lemma. Including it padded the homonym floor with 4 clean floor pairs — *helping* the hypothesis on a wrong label. Removed.
2. **`prop` mis-filed POLYSEMY → HOMONYM.** Support (`proppe`) vs stage-prop (`property`-clip) are genuinely distinct origins, both general — a true homonym by the gate rule. Adding it (pairs mostly human≥3) *weakened* the floor effect — the honest, rule-consistent direction.
3. **b3 precondition fails / floor circularity** → the result now leads with the null and treats the ordinal floor hint as confounded (scale-floor + circularity), not as support.
4. **source notes were placeholder "test"** → replaced with real per-lemma etymology + reference.

The net effect of the corrections was to *weaken* the apparent effect (remove `lass` floor pairs, add `prop` high pairs), which is why the result is a clean null rather than the "directionally supported" overclaim the first draft made.

### Decisive etymological evidence for the HOMONYM calls (quoted)

- **ball** — Etymonline `ball (n.1)` "round object … from cognate Old Norse *bollr* 'ball,' from Proto-Germanic *\*balluz*" (PIE *\*bhel-* 'to swell') vs `ball (n.2)` "dancing party … from Old French *baller* 'to dance,' from Late Latin *ballare* … from Greek *ballizein*" (PIE *\*gwele-* 'to throw').
- **plane** — flat-surface/tool/aircraft from Latin *planum*/*planus* vs **plane-tree** "from Latin *platanus*, from Ancient Greek *πλάτανος*."
- **prop** — Etymonline `prop (n.1)` "a support … probably from Middle Dutch *proppe*" vs `prop (n.2)` "object used in a play, 1898 … shortened form of *properties* … see *property*" (← Latin *proprius*).

A comprehensive dual-source (Etymonline + Wiktionary) classification of all 43 lemmas (independent research pass) confirmed the same confident HOMONYM set {ball, plane, prop} (flagging `bit` — computing-bit coined 1948 from "binary digit" — as a borderline 4th, excluded here as both anachronistic for the 1810–2010 CCOHA register and "the weakest of the homonyms").

## Pre-registration / no-retuning

- This is a **re-analysis**: the v1 ratings were already seen. Discipline: the **stratification is etymology-driven, applied blind to the model ratings, and frozen before the final analysis**; the **statistics are fixed in `analyze.py` before computing** (floor thresholds `durel`==1 / `cont`<=20, `LOW_CUT`=2.0, intermediate band [2,3], permutation seed + N=5000). The stratification correction was driven by the etymology rule + the critic, **not** by which labelling produced a stronger effect (the correction weakened it).

## Files

- `stratification.csv` — committed, sha256-frozen; lemma → stratum + n_general_etymons + key_roots + source note.
- `analyze.py` — pure-Python (no numpy); joins the frozen stratification to the v1 manifest + v1 raw preds; b1 within-stratum Spearman, b2 matched-human gap + low-end floor mass + whole-lemma label-permutation p, b3 model-free human-structure precondition; emits `raw/results.json`. **No API.**
- `raw/results.json` — computed statistics (corrected stratification).

## Headline numbers (corrected stratification; see result page for interpretation)

HOMONYM 3 lemmas / 16 pairs, POLYSEMY 35 lemmas / 154 pairs (170 of 200 pairs used; 30 in excluded lemmas).

- **b3 (model-free):** homonyms are **not** more bimodal than polysemy (homonym low/mid/high 0.50/0.25/0.31 vs polysemy 0.43/0.46/0.25; mean human 2.31 vs 2.49) — the discreteness precondition fails.
- **b1:** the v1 monotonicity holds within **both** strata (cont ρ: claude H 0.77 / P 0.67; gpt H 0.71 / P 0.62; gemini H 0.83 / P 0.79).
- **b2 (the clause-b contrast): not established.** Matched-human gap tiny/mixed-sign (cont −1.9 / −2.2 / −3.8; durel −0.02 / +0.67 / 0.0); **all** whole-lemma permutation p non-significant (0.29–1.0). Residual: ordinal low-end floor-fraction higher for homonyms (0.63–0.88 vs 0.23–0.27, n=8) but confounded with scale-floor + circularity, and gone on the continuous scale.

## Freeze hash

`stratification.csv` sha256: **`3169ff3a1b1e825d653e7eba33d4c1a8a4ab1de6b30c9c9c1c8c81fc14eef21f`** — the committed file is the corrected uniform-rule version (HOMONYM = ball/plane/prop; lass excluded). Re-running `analyze.py` against it reproduces `raw/results.json`.

## Post-run verification

Independent read-only number-verification recomputed every headline figure from `raw/*.json` + `manifest.csv` + `stratification.csv` with its own from-scratch Spearman → **CLEAN** (run on the pre-correction stratification; the correction only weakened the effect, consistent with the null). The adversarial pre-write critique (above) is the load-bearing check for this page.
