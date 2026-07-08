# PREREG — FRESH relation-recovery / taxonomic-proxy probe (H1 + H2)

**Frozen s193, 2026-07-08, BEFORE any model call.** Design:
[`design/lexical-relation-recovery-taxonomic-proxy-v1`](../../designs/lexical-relation-recovery-taxonomic-proxy-v1.md).
Gates RATIFIED s193:
[`decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design`](../../../wiki/decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design.md)
— **Q1-C / Q2-B (C4 primary) / Q3-A / Q4 internal-contrast-only.** This file freezes the item set, the
control, both proxies (specs + predicted signs), the corpus, the verdict map with numeric thresholds,
and the anti-cheat fence. Nothing below may be touched after recovery is observed.

## The question (nothing wider)

On a **fresh** relatum-production probe over the six WordNet noun relations, run on the panel against a
**different** contrastive-frame G² control corpus (C4 web text, not s186's Simple English Wikipedia),
with **IS-A path depth pre-registered before recovery is observed**: **(H1)** does recovery rank
**again** decouple from contrastive-frame cue-strength, and **(H2)** does IS-A path depth (or the
pre-registered corpus Hearst-frame proxy) **out-predict** cue-strength for relation-wise recovery, in
the pilot-registered **negative** direction (depth) / theory-set **positive** direction (Hearst),
≥2/3 models? **Internal-contrast only** (Q4): recovery is scored against WordNet, a shared target that
cancels in the head-to-head; both predictors are corpus/lexicon statistics; no human baseline enters.

## Frozen artifacts (built + committed BEFORE any model call)

- **`items.json`** (`prep.py`, SEED 20260708): FRESH cue nouns per relation, DISJOINT from the 707
  committed s186 cue lemmas (asserted 0 overlap, 6/6 relations — freeze-condition 6). Each cue carries
  its gold relatum set (relata() byte-identical to s186) **and** its `is_a_depth`
  (`wn.synsets(cue,'n')[0].min_depth()`). Frequency band Lg10WF ∈ [2.0, 4.5], matched to antonymy's
  fresh per-bin profile. **ACHIEVED per-relation N (freeze finding, condition 6):**

  | relation | N | Lg10WF median | mean IS-A depth |
  |---|---|---|---|
  | antonymy | **87** | 3.028 | 6.126 |
  | synonymy | 120 | 3.002 | 6.950 |
  | hypernymy | 120 | 3.012 | 7.008 |
  | hyponymy | 120 | 3.015 | 6.375 |
  | holonymy | 120 | 2.976 | 7.200 |
  | meronymy | 120 | 2.969 | 6.867 |

  **687 verdict-bearing cues.** Antonymy is capped at **87** (WordNet nominal antonym sparsity after
  excluding the 130 s186 antonymy cues — the fresh eligible pool was 87), reported at its achieved N,
  not padded (condition 6 / rider 1). IS-A depth resolved 100% (687/687).

- **`control.json` / `counts.json`** (`build_cooc_c4.py`): the contrastive-frame G² control on **C4**.
  **Freeze-condition 4:** `signed_g2` + `compute_control` produce **byte-identical output** to the s186
  `build_cooc.py` (verified by assertion — a battery of inputs + a synthetic `compute_control` case; K,
  FRAME_WIN, CONNECTIVES identical); only the sentence-streaming IO adapter changed (gzipped C4 JSONL
  vs Simple-Wikipedia bz2 XML). **Corpus (Q2-B + rider 1):** C4 (`allenai/c4` en) shards
  **00000–00002** streamed and discarded. **Achieved volume: 22,329,495 sentences / 388,243,981 tokens
  ≥ s186's 21.3M sentences / ~320M tokens** (asserted before writing — rider 1). ODC-BY (+ Common-Crawl
  terms — travels to the result provenance, rider 3).

- **`hearst.json`** (same pass): the Q3-A **second** proxy — corpus Hearst-frame definitional-density
  per cue. Triggers frozen (`and other` / `or other` / `such as` / `and any other` / `or any other`;
  unigrams `including` / `especially`), window ±3. **Predicted sign POSITIVE** (theory-set, frozen
  before counting — condition 5: cues appearing more in genus-naming/definitional frames are more
  definitionally central, and the essay predicts definitionally-central relations recover better).

## Frozen predictor vectors (pre-recovery — legitimate to state; NO model data existed when computed)

| relation | cue-strength (frame-G²) | IS-A depth | Hearst density |
|---|---|---|---|
| antonymy | 0.1494 | 6.126 | 0.0137 |
| synonymy | 0.0056 | 6.950 | 0.0126 |
| hypernymy | 0.0083 | 7.008 | 0.0123 |
| hyponymy | 0.0361 | 6.375 | 0.0147 |
| holonymy | 0.0308 | 7.200 | 0.0142 |
| meronymy | 0.0194 | 6.867 | 0.0146 |

Control non-degenerate (top-3 produced for ~every cue; mean control-frame soundness 0.036). Note two
things the fresh corpus already changed vs s186/the pilot, which make H2 a genuine risk (not a
foregone win): on C4 the second-most-cued relation is **hyponymy** (not meronymy), and **hypernymy is
one of the DEEPEST** relations by IS-A depth (7.008) — so if recovery again tops at hypernymy (as s186
found), ρ_depth is pushed toward zero/positive and H2 (depth) can lose cleanly.

## Panel & elicitation (byte-identical to s186 neutral arm)

Panel = [`config/models.md`](../../../config/models.md) `panel.A/.B/.C` (never hardcode slugs).
Temperature 0, zero-shot, single-turn, neutral system prompt; `google/*` gets
`reasoning={"effort":"minimal"}`. NEUTRAL prompt + `parse_words` byte-identical to s186 `probe.py`.
ONE arm (neutral, all 6 relations); the s186 antonymy frame-ablation arm is DROPPED (bears on the
local-shadow reading, not H1/H2). `ABORT_USD = 1.50`. Every call records `usage.cost`.

## Metrics

- **Recovery 𝒮** (per relation) = mean raw **Soundness** (Cao precision-over-produced) over the
  relation's cues — the essay/pilot's clause-2 quantity (the −0.086 pipeline). **HIT@3** = gold-size-
  insensitive co-primary (a hit is a hit regardless of over-production), carried from s186.
- **Cue-strength** (per relation) = mean 𝒮(control top-3, frame variant) — the s186 clause-2 quantity.
- **ρ_cue / ρ_depth / ρ_hearst** = across-relation Spearman (n=6, **tie-naive** — the authoritative
  s186 pipeline; the pilot notes tie-corrected gives a slightly larger |ρ|) of recovery against each
  predictor, **per model**.

## Verdict map (FROZEN; direction fixed; condition 1 + 2)

**Verdict of record = the ACROSS-RELATION (n=6) result** (Q1-C / condition 1). The item-level
cue-depth regression is **descriptive/robustness-only, NON-DECISIVE** — it can never fire H2 or
upgrade an across-relation H2-loss; a level-divergence is a pre-named first-class reported outcome.

**H1 (safer) — exhaustive, mutually-exclusive bands (condition 2), on primary (soundness) ρ_cue:**
- **DECOUPLING-REPLICATES** iff ρ_cue **≤ +0.30** on **≥2/3** models (near-zero or negative).
- **DECOUPLING-BREAKS** iff ρ_cue **> +0.50** on **≥2/3** models (cue-strength clearly recovers its
  predictive power on the fresh corpus — s186's decoupling was corpus/set-specific; fires essay
  trigger (a)).
- **H1-PARTIAL/AMBIGUOUS** otherwise (any model in (+0.30, +0.50], or no ≥2/3 majority either way) —
  pre-named first-class (cue-strength partially recovers).

**H2 (riskier) — numeric margin (condition 2); IS-A depth PRIMARY, Hearst SECONDARY (condition 5):**
- A proxy **wins** for a model iff **|ρ_proxy| − |ρ_cue| ≥ 0.20** AND ρ_proxy is in its pre-registered
  direction (depth **negative**; Hearst **positive**).
- **TAXONOMIC-PROXY-WINS** iff **IS-A depth** wins on **≥2/3** models (the primary, full-status result).
- **TAXONOMIC-PROXY-WINS-QUALIFIED** iff IS-A depth does **not** win on ≥2/3 but the **Hearst** proxy
  does — reported as a **weaker/qualified** H2 result, never equal-status (condition 5).
- **TAXONOMIC-PROXY-LOSES** otherwise (no pre-registered proxy out-predicts cue-strength, or
  cue-strength out-predicts every proxy — the decoupling is real but taxonomic structure is not the
  filler; the "what predicts recovery" question reopens with taxonomic structure ruled out).

**Pre-named nulls (first-class):** ρ_cue and ρ_depth both near-zero (recovery tracks neither corpus
statistic — an honest "we don't yet know what predicts recovery"); or an across-vs-item-level
divergence (reported, not resolved by fiat).

**n = 3 models; orderings, not coefficients; nouns only. No pooling across models.**

## What each outcome feeds

- **H1 REPLICATES + H2 WINS (IS-A depth ≥2/3):** essay trigger (b) fires **for**; the lexical pole's
  **unplaced** shadow-saturated corner in
  [`theory/lexicon-grammar-continuum-v2`](../../../wiki/findings/theory/lexicon-grammar-continuum-v2.md)
  gains a *measured* re-placement candidate. Still internal-contrast, still within-distribution.
- **H1 REPLICATES + H2 LOSES:** the decoupling is robust but taxonomic structure is not the filler —
  trigger (b) fired-against; a clean honest partial (the risky half loses, the safe half wins).
- **H1 BREAKS:** cue-strength recovers on a fresh corpus — trigger (a); scope s186's decoupling to its
  Simple-Wikipedia/noun setting or retract.
- **A [`predictions.md`](../../../wiki/predictions.md) row** is registered at freeze (co-registered with
  the existing §B decoupling bet, not double-scored); outcome updated the run session.

## Anti-cheat fence (PROTOCOL §B; the six conditions + three riders)

The fresh disjoint cue sets, the outlier cap (band [2.0,4.5], frozen), k=3, both proxy specs and their
predicted signs, the ρ_cue / ρ_depth / ρ_hearst bands, and the H1/H2 numeric thresholds are **all
frozen here BEFORE any model call**. No proxy, band, or threshold is touched after recovery is seen.
The H1-break, H2-lose, and both-null outcomes are pre-named first-class. The pilot's refusal of the
gloss-length exploratory maximum (ρ=−0.83) is respected — gloss length is **not** a proxy here; the
Hearst arm is the pilot-*licensed* corpus construct.

**Construct-validity scope caveat (carried to the result, not a gate):** IS-A depth and the
recovery-scoring key share a source (WordNet); mitigated by the gold-independent cue-first-synset depth
(a property of the cue, not the answer set). Q4 stays internal-contrast-only.
