# Run record — lexical-sense-gradience probe v1 (the project's first LEXICAL probe)

**Date:** 2026-05-30
**Design (frozen):** [`design/lexical-sense-gradience-v1`](../../designs/lexical-sense-gradience-v1.md)
**Governing decision (RESOLVED under Tom's delegation):** [`decisions/resolved/lexical-sense-gradience-operationalization`](../../../wiki/decisions/resolved/lexical-sense-gradience-operationalization.md)
**Conjecture probed:** [`conjecture/lexical-sense-gradience`](../../../wiki/findings/conjectures/lexical-sense-gradience.md)
**Anchor:** [`resource/dwug-usage-graphs`](../../../wiki/base/resources/dwug-usage-graphs.md) (DWUG EN v3.0.0, Zenodo 14028531, CC BY-ND 4.0)
**Result page:** [`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md)

## What ran (v1 scope = P1 monotonicity + P3 context-similarity control)

The project's **first lexical (non-grammatical) probe**. It tests whether an LLM's same/different-sense signal is **monotonic in human-rated usage similarity** (DWUG's graded DURel judgments) and whether that monotonicity **survives a context-similarity control** (clause c of the conjecture — the lexical analogue of the constructional `distributional`/frequency shadow). The polysemy-vs-homonymy arm (prediction 2) is **deferred to v2** with a frozen WordNet-grounded stratification, so the contestable layer never touches this clean monotonicity test.

- **Anchor / items:** DWUG EN graded human DURel judgments (4 Identical / 3 Closely Related / 2 Distantly Related / 1 Unrelated) over pairs of usages of the **same target word**. 200 pairs, balanced 50 per rounded DURel level (1–4), across **43 lemmas**, **within-period only** (Q4 synchronic filter), each pair with **≥2 annotator judgments** (median = human gold). Frozen pre-run; manifest sha256 `7b4ad11f25e8734c52f2f87da338aebd9056f764e2130bf36e32aaead6109fd2`; DWUG archive sha256 `64eef477154b82cb27925ab4ea8c030a8e23840b538dd06b6464aa1e55af2dbf`.
- **Instrument (Q1, behavioral panel):** each model rates each pair under **three pre-registered framings** — `durel` (the verbatim 4-point DURel scale; the primary graded signal, rank-comparable to the human median), `cont` (0–100 continuous sense-relatedness; instrument robustness), `topic` (0–100 topic/situation similarity *ignoring* the target word; the Q3 semantic context control). Temperature 0, logprob-free → the 3-family panel ([`config/models.md`](../../../config/models.md)). Target word marked with «guillemets».
- **Controls (Q3):** (i) content-token **lexical overlap** (independent, surface) — **near-zero across all DURel levels in this sample** (mean Jaccard 0.001–0.015; Spearman with human level 0.18), so a surface-lexical shadow is ruled out almost by construction but has little variance to partial; (ii) the model-rated **topic similarity** (semantic, model-internal) — added pre-run to meet the deeper shadow. Both partials reported.
- **Reading rule (report-the-correlation; no pass bar):** Spearman ρ(model sense, human DURel) per model per framing, with bootstrap 95% CI; partial ρ controlling for overlap and for model topic-similarity; per-human-level mean ratings (the monotonic table); ρ(sense, topic) = sense/topic conflation. No threshold tuned after the run.

## Data / licence handling

DWUG EN is **CC BY-ND 4.0** over copyrighted **CCOHA** corpus text. To be conservative the project does **not** commit the raw archive or the corpus sentences: `experiments/data/dwug/` is gitignored; `build_items.py` re-downloads DWUG from Zenodo (URL + archive sha256 pinned) and regenerates the identical item set from a fixed seed + frozen filters. Committed: the **recipe** (`build_items.py`), a **manifest** of selected pairs by DWUG identifier + the human DURel gold + the derived lexical-overlap covariate (pointers + the specific rating values used as gold — research-analysis use, not dataset/corpus redistribution), and raw JSON of model outputs + gold (**no corpus sentences**).

## Pre-registration / no-retuning

- The within-period filter, ≥2-judgment requirement, 50/level balance, per-(lemma,level) diversity cap, sampling seed, all three framings, and both controls were fixed **before any model call** (the topic-similarity control was added after the *build-time* overlap finding but **before any sense-probe result** — strengthening the control, not tuning toward a result).
- Manifest frozen + committed before any probe call (sha256 above).
- **Adversarial pre-run pass:** independent read-only subagent (see below).

## Files

- `build_items.py` — downloads DWUG (gitignored), applies the frozen filters/sampling, emits the gitignored full-text file + the committed `manifest.csv`; prints the freeze sha256.
- `manifest.csv` — committed item manifest (ids + human gold + overlap covariate; **no corpus text**).
- `probe.py` — runner (durel + cont + topic × 3 models); imports `experiments/lib/openrouter.py` (billed `usage.cost`); reads the gitignored full text; commits model outputs only.
- `analyze.py` — pure-Python Spearman + partial Spearman (both controls) + bootstrap CI + per-level means; emits `raw/results.json`.
- `raw/` — `{durel,cont,topic}_{A,B,C}.json`, `results.json`, `run_summary.json` (no corpus text).

## Pre-run critique

An **independent read-only adversarial methods critic** reviewed the build, prompts, analysis, and spot-checked the human gold. **One BLOCKER, fixed before the run + re-frozen:**

- **B1 (fixed) — ~7/200 items had mis-extracted target spans.** DWUG's `indexes_target_token` offsets are **+1 misaligned for items whose `context` has a leading space** (verified: e.g. `h«eels »` instead of `«heels»`, `r«isk »`, `t«ipped »`), clustering in the high-relatedness cells that drive the signal. **Fix:** `build_items.py` now **anchor-expands** each offset to the maximal alphabetic run and **validates** it against the lemma root (recovering the off-by-ones rather than dropping data; genuinely unrecoverable uses are dropped). **B2:** a span-sanity `assert` now gates the freeze (every selected surface must validate). Re-built + re-frozen; manifest hash `f2a09ecc…` → **`7b4ad11f…`**; all 400 target surfaces are now clean words (0 non-alpha), the critic's flagged items verified corrected.

**Framing fixes (SHOULD-FIX, applied in the result's interpretation — not blockers):**
- **S1 — the lexical-overlap control is near-degenerate** (only 30/200 items have any overlap; mean Jaccard ~0.003–0.015). So overlap is ruled out **a priori** (the sentences barely share content words), **not** by partialling — a surviving `partial|overlap` licenses little. The result frames it this way and does not headline it.
- **S2 — the topic-similarity control is model-internal.** A *surviving* `partial|topic` is modest support that the sense signal isn't merely the model echoing context similarity; a *collapsing* one is **ambiguous** (sense and topic are genuinely correlated across items) and must **not** be read as "no sense-tracking." Stated in the result.
- **S3 — 151/200 pairs rest on only 2 annotators** *(erratum 2026-07-05 s183: manifest recompute gives 152/200 two-annotator, 48/200 n>=3)* (the half-integer gold levels are 2-rater disagreements). `analyze.py` now also reports ρ on the **n≥3** subset; the writeup won't treat half-integer levels as reliable gold.
- **S4 — some level-1 "unrelated" pairs are homonyms** (e.g. `lass` girl vs `lassi` drink under one DWUG lemma), so the low end mixes homonymy with the polysemy gradience — noted in the result.
- **Strongest supportable claim (per the critic):** "model X's DURel-framed rating is rank-correlated with the human DURel median (ρ, CI), not accounted for by surface lexical overlap; relation to model topic-similarity [survives/collapses]." It must **not** claim graded sense *representations*, isolation of sense from context, or generalization beyond these 43 CCOHA lemmas / the DURel framing.

VERDICT after fixes: sound to run.

## Results / cost

1800 calls, **0 NA**. Cost **$3.134 billed** (A $0.423 / B $0.105 / C **$2.606**) — gemini billed ~14.5× its rate-card estimate ($2.61 vs $0.18) over 600 reasoning-heavy calls; the priciest single run to date but under the $5 single-run flag and far under the $20/mo cap (reasoning-token cost on multi-call gemini probes is now a known budget driver).

**Headline: a clean POSITIVE — the panel's graded sense-relatedness rating is strongly rank-correlated with the human DURel median, and the correlation survives the context-similarity control.** Spearman ρ(model sense, human DURel), n=200, bootstrap 95% CI:

| model | durel ρ (CI) | cont ρ (CI) | partial \| overlap | partial \| topic | ρ(sense,topic) |
|---|---|---|---|---|---|
| claude-sonnet-4.6 | 0.679 (0.59–0.75) | 0.696 (0.61–0.78) | 0.67 / 0.69 | 0.52 / 0.54 | 0.64 / 0.68 |
| gpt-5.4-mini | 0.601 (0.49–0.69) | 0.675 (0.58–0.75) | 0.59 / 0.66 | 0.50 / 0.58 | 0.46 / 0.52 |
| gemini-3.5-flash | **0.804 (0.75–0.85)** | **0.825 (0.76–0.87)** | 0.80 / 0.82 | 0.73 / 0.75 | 0.56 / 0.59 |

- **P1 monotonicity holds for all 3 models, both framings.** Per-human-level mean ratings are cleanly monotonic (e.g. claude `cont`: 18→21→32→36→50→76→80 across human levels 1.0→4.0). For reference, DWUG EN's *human* inter-annotator Spearman is **0.69** — so the panel's agreement with the human median is in (claude) or **above** (gemini 0.80) the human–human range (a reference point, not an identical comparison: model-vs-median is more stable than annotator-vs-annotator).
- **P3 / clause (c): the monotonicity is not a context shadow.** Partialling out lexical overlap barely moves ρ (overlap is near-degenerate here, so this rules out a *surface* shadow a priori, not by partialling — S1). Partialling out the model's **own topic-similarity** rating **substantially survives** (e.g. gemini 0.80→0.73, claude 0.68→0.52) — the sense signal adds rank information beyond the model's perception of how similar the two contexts/topics are. (Model-internal control — a surviving partial is modest positive support; a collapse would have been ambiguous — S2.)
- **Instrument/model note:** gpt-5.4-mini is again the noisier model under the *ordinal* DURel framing (ρ 0.60; its mid-level means non-monotonic) but cleaner under the *continuous* framing (ρ 0.68) — a lexical echo of the project's instrument-sensitivity theme. gemini is the strongest sense-tracker; claude in between.

Reproducible from `raw/results.json`. **Post-run verification:** all 24 ρ/partial figures + the 1800-record/0-NA counts + the monotonic per-level means were independently recomputed from `raw/*.json` + `manifest.csv` by a read-only adversarial subagent → **CLEAN — all figures verified**.
