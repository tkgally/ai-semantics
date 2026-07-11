# PREREG — BLiMP R1 frequency control, covariate arm (C8 promotion-prep, program A3b), s208

**Frozen before `F(p)` is computed and before it meets the paradigm→H mapping (G1′).** Ratified gates
(s208, [`decisions/resolved/blimp-profile-frequency-control-design`](../../../wiki/decisions/resolved/blimp-profile-frequency-control-design.md)):
**Q1-C / Q2-A (surface-scoped) / Q3-A; G8 BINDING; G9 NEW.** This PREREG covers the **covariate arm only**
(the $0 arm run this session). Per **G8** the covariate arm earns a **ROBUSTNESS / CORROBORATION** result,
never a promotion; the **swap arm** (Q1-C, required for a promotion) is a later session and is NOT
pre-registered here.

## The question

Does R1 PROFILE-ALIGNED — the per-model Spearman across the 40 frozen paradigms of order-averaged
forced-choice accuracy vs BLiMP per-paradigm human agreement `H(p)` (ρ_prof **+0.606 / +0.543 / +0.628**,
n=40, all CIs > 0) — survive controlling a per-paradigm **surface-string corpus-frequency** proxy `F(p)`?

## §F — the frequency proxy F(p) (Q2-A, zero post-freeze latitude — G7 sharpening)

`build_freq.py` implements exactly this; `analyze_partial.py` consumes `freq.json`. Both are committed
before `F(p)` is computed. **No parameter below is resolvable after seeing any accuracy or `H` value.**

1. **Corpus items:** the 40 frozen s205 paradigms,
   `experiments/runs/2026-07-10-blimp-forced-choice-sweep/items.json → items[uid]` (30 pairs each). Use the
   **`good`** sentence of each pair only.
2. **Tokenizer (frozen, reused from `build_cooc_c4.py`, import-pinned — G1′):** lowercase, then
   `_nonword.sub(" ", s).split()` where `_nonword = [^a-z\s]+`. Applied **identically** to item sentences
   and to C4.
3. **Content words:** tokens NOT in the frozen `STOPWORDS` set (an explicit ~200-item English
   function-word list, verbatim in `build_freq.py`; includes the contraction fragments `s t re ve ll d m`
   the a-z-only tokenizer produces).
4. **Target n-grams of a good sentence:** every **adjacent-token bigram and trigram** whose tokens are
   **all content words**. (A surface-material familiarity proxy — "how frequent is this paradigm's actual
   surface material in C4".)
5. **C4 count `c(g)`:** occurrences of n-gram `g` as **consecutive tokens** across the streamed C4 set
   (shards `c4-train.00000/00001/00002-of-01024.json.gz`, the s193-frozen 22,329,495-sentence set; ODC-BY
   + Common-Crawl terms carried to provenance). A volume-floor assertion (`Nsent ≥ 21.3M`) guards a short
   stream. **`F(p)` is computed blind to accuracy and `H` — `build_freq.py` reads neither.**
6. **Sentence score:** mean over the sentence's content-word n-grams of `log(1 + c(g))`. A good sentence
   with **zero** content-word n-grams is **dropped and logged** (`dropped_sentences`), never repaired.
7. **F(p) PRIMARY** = mean sentence score over the paradigm's 30 good sentences, **bigrams + trigrams**.
   **F(p) SENSITIVITY** = the single pre-specified variant (G7), **bigrams only**.
8. **G7 proxy-validity audit inputs** (computed blind, in the same C4 pass): per-paradigm mean content-word
   **unigram** log-frequency and mean content-word **length**.

## §V — the verdict (frozen bands; direction fixed; thresholds tighten-not-loosen)

`analyze_partial.py` computes, per model m: raw ρ_prof(m) = Spearman(acc, H); **partial** ρ_prof·F(m) =
Spearman partial correlation of acc vs H controlling F (on ranks); bootstrap 95% CI (BOOT = 5000, seed
**20260711**, resample paradigms).

- **corr(F,H) collinearity branch (G6) — decided FIRST:** report `corr(F,H)` = Spearman(F, H).
  - `|corr(F,H)| < 0.20` → **CORROBORATED-NO-CONFOUND**: the C8-posited frequency structure is absent, so
    it cannot have inflated ρ_prof (partial ≈ raw). A first-class sub-outcome.
  - `|corr(F,H)| > 0.70` → **INCONCLUSIVE-OVER-CONTROL-SUSPECT**: strong collinearity; the partial has
    inflated variance and (insofar as F tracks depth) partialling strips shared structure. Distinct from
    SURVIVES/BREAKS.
  - `0.20 ≤ |corr(F,H)| ≤ 0.70` → the interpretable regime; read the partial:
- **SURVIVES-COVARIATE** iff the partial ρ_prof·F(m) bootstrap CI **excludes 0** (and is positive) on
  **≥ 2/3** models. **BREAKS-COVARIATE** iff the CI includes 0 on ≥ 2/3. (At df = 37, CI-exclusion already
  requires partial |ρ| ≈ 0.325; the `+0.30` figure in the design is a **non-binding floor**, not a second
  gate — the CI-exclusion is the binding criterion, G4′.)
- **Power (G4′):** stated as P(bootstrap CI excludes 0) per model at the observed partial magnitude
  (`p_boot_pos` reported per model), NOT a point-threshold. The weaker model's wide n=40 CI makes an
  INCONCLUSIVE landing a realistic outcome even on a true partial ≈ +0.35.
- **Two negative controls (G1′, necessary-not-sufficient, pre-registered):**
  - **NC1 scramble-H** (shuffle the paradigm→H mapping): raw and partial ρ → ~0 expected (a real-signal
    check; a scramble collapses ρ regardless of F).
  - **NC2 scramble-F** (shuffle F across paradigms): partial ≈ raw ρ_prof expected (a random covariate
    controls nothing — a partialling-machinery check).
- **Sensitivity:** the bi-only F partial is reported alongside; a divergence between primary and
  sensitivity is flagged, not silently averaged.

## §G7 — proxy-validity audit (read BEFORE the partial verdict; predictions frozen here)

Frozen predictions, checked before the partial is interpreted (a failure downgrades F to descriptive):
- Spearman(F, per-paradigm mean content-word **unigram log-freq**) — predicted **strongly positive** (the
  n-gram proxy must track lexical frequency).
- Spearman(F, per-paradigm mean content-word **length**) — predicted **negative** (Zipf: frequent words
  are shorter). An independent (item-derived, not C4-count) sanity direction.

## §S — scope caveats carried into any statement (G3′, G9)

1. **Controls R1 only** (not R2 DEPTH-GRADED / R2h TRACKS-DIP).
2. **Q2-A controls SURFACE-LEXICAL familiarity, NOT construction frequency** (C8's literal confound). The
   covariate arm's honest reach is "over-and-above lexical/surface exposure."
3. **C4 is a PROXY** for the panel's unknown pretraining distribution: a SURVIVES reads "against a
   **C4-frequency proxy**," never "against actual training frequency."
4. **G8/G9:** the covariate arm alone is a **ROBUSTNESS / CORROBORATION** result. **C8's promotion gate is
   NOT satisfied by this arm.** The Q1-C **swap arm** (exact-string memorization, fresh items + calls) is
   the outstanding requirement for a promotion, and this result must **not** advance the shadow-depth
   table's form-(iv) row toward a claim.
5. Reuses the frozen s205 order-averaged per-paradigm accuracies (`results.json → per_model[*].per_paradigm`,
   verifier-reproduced s205) and the committed human anchor — **no new grammatical measurement**; the force
   is entirely in the partialling.

## §P — prediction registered at freeze (`wiki/predictions.md`)

One row: **the covariate arm SURVIVES** (partial CI excludes 0 on ≥2/3 in the interpretable
collinearity regime). Rationale for the bet direction: R1's raw ρ_prof +0.54–0.63 sit well above the
CI-exclusion floor, and the human profile is non-monotonic in structural depth (so `F` — a surface-lexical
proxy — is unlikely to be so collinear with `H` as to explain the whole alignment). Registered as a bet,
resolved this session by the run. A BREAKS or an INCONCLUSIVE-OVER-CONTROL or a CORROBORATED-NO-CONFOUND
are all pre-named first-class outcomes.

## §A — anti-cheat fence (PROTOCOL §B; G1′, G7, G9)

`build_freq.py` (F(p)) and `analyze_partial.py` (partial, bands, audit, NCs) are **committed before
`F(p)` is computed**. A **fresh-agent verifier** independently reproduces the `F(p)` recipe from this
PREREG on a synthetic fixture (matching `build_freq.py` output on the fixture), certifies the **zero
post-freeze latitude** property, and confirms the audit + bands are frozen in the committed code —
**before `F(p)` touches the real paradigm→H mapping**. The `F(p)` code reuses only the C4 streaming
adapter + tokenization from `build_cooc_c4.py` (import-pinned to those, not the G² kernel); the n-gram
extraction + aggregation are **new code with genuine DoF**, authored with the s205 accuracies already
known — which is exactly why G8 caps this arm at robustness/corroboration. A post-run verifier recomputes
every figure from `freq.json` + the frozen s205 inputs.
