---
type: result
id: lexical-relation-recovery-taxonomic-proxy-v1
title: "Cue-strength–recovery decoupling REPLICATES on a fresh corpus + a pre-registered taxonomic proxy (IS-A depth) WINS (2/3): both halves of the decoupling essay's bet fire, with the depth effect between-relation not within-cue, and the Hearst arm losing (internal-contrast)"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-08
updated: 2026-07-08
links:
  - rel: operationalizes
    target: design/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: operationalizes
    target: essay/cue-strength-recovery-decoupling
  - rel: supports
    target: essay/cue-strength-recovery-decoupling
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: note/taxonomic-proxy-recovery-pilot-v1
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
---

# Result — fresh relation-recovery / taxonomic-proxy probe (H1 + H2)

> **Status: proposed (reading-bearing result; s193, 2026-07-08). VERDICT: both halves of the
> [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md) bet fire
> FOR — with honest caveats.**
> **H1 — DECOUPLING-REPLICATES (3/3).** On a genuinely fresh test (fresh cues disjoint from s186; a
> *different* corpus family — C4 web text, not s186's Simple English Wikipedia), across-relation
> recovery rank again decouples from contrastive-frame co-occurrence cue-strength: ρ_cue = **+0.14 /
> +0.09 / +0.09** (all ≤ +0.30, near-zero). s186's decoupling was **not** a corpus- or set-specific
> artifact. Essay trigger (a) does **not** fire.
> **H2 — TAXONOMIC-PROXY-WINS on IS-A depth (2/3).** The pre-registered **primary** proxy — mean IS-A
> path depth (`min_depth`), predicted sign **negative** (shallower/more-superordinate cue sets recover
> better) — out-predicts cue-strength on 2/3 models: ρ_depth = **−0.20 / −0.37 / −0.37**, clearing the
> pre-registered 0.20 margin on B and C (not A). Essay trigger (b) fires **for**.
> **Two load-bearing caveats.** (i) The depth effect is **between-relation, not within-cue**: the
> item-level regression (a cue's own depth → its own recovery, n≈687) is **near-zero** (ρ ≈ +0.06 /
> +0.01 / +0.04) — the depth story holds at the *relation* grain only. (ii) The **Hearst-frame
> definitional-density** second arm **loses**: it correlates with recovery in the sign *opposite* its
> pre-registered positive prediction (ρ_hearst = −0.54 / −0.49 / −0.49), so H2 is carried by IS-A depth
> alone, not by the corpus definitional-frame proxy.
> `anchor: internal-contrast-only` (ratified s193): the force is a within-instrument comparison of
> *which corpus/lexicon statistic best rank-predicts recovery* — **no human comparison**. Post-run
> verifier **REPRODUCED** every figure from raw (0.000 max ρ discrepancy).

Design [`design/lexical-relation-recovery-taxonomic-proxy-v1`](../../../experiments/designs/lexical-relation-recovery-taxonomic-proxy-v1.md);
gates ratified s193 ([`decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design`](../../decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design.md):
**Q1-C / Q2-B (C4 primary) / Q3-A / Q4 internal-contrast-only**). Frozen `PREREG.md` + a freeze-stage
pre-run critic (GO) + non-Anthropic vote + an independent post-run verifier (REPRODUCED) under
[`experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/`](../../../experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/).
This is the empirical discharge of the decoupling essay's registered H1/H2 bets
([`predictions.md`](../../predictions.md) §B).

## The question

On a **fresh** relatum-production probe over the six WordNet noun relations, run on the panel against a
**different** contrastive-frame G² control corpus (C4), with **IS-A path depth pre-registered before
recovery is observed**: (H1) does recovery rank **again** decouple from contrastive-frame cue-strength,
and (H2) does a pre-registered taxonomic proxy **out-predict** cue-strength for relation-wise recovery,
in its pre-registered direction, ≥2/3 models? Internal-contrast: recovery is scored against WordNet, a
shared target that **cancels in the head-to-head**; the predictors (contrastive-frame G², IS-A depth,
Hearst density) are all corpus/lexicon **statistics** — the contrast is *which statistic tracks
recovery*, never a model-vs-human claim.

## What was run (frozen before any model call)

- **Items** ([`prep.py`], SEED 20260708): fresh cue nouns per relation, **DISJOINT from the 707
  committed s186 cue lemmas** (verifier-confirmed 0 overlap, 6/6). Achieved per-relation N: antonymy
  **87** (WordNet nominal antonym sparsity after excluding the s186 antonymy cues — the fresh eligible
  pool was 87, reported not padded), the other five **120** each — **687 verdict-bearing cues**.
  Frequency-matched on SubTLEX-US Lg10WF ∈ [2.0, 4.5]. (The design/condition-6 wording says "780 s186
  cue lemmas"; the correct exclusion is the **707 unique** lemmas — 780 = 6×130 cue *slots*, and a noun
  serving multiple relations collapses the union to 707. `prep.py` excludes the union.)
- **Control** ([`build_cooc_c4.py`]): contrastive-frame G² on **C4** (`allenai/c4` en, shards
  00000–00002; **22,329,495 sentences / 388,243,981 tokens ≥ s186's 21.3M sentences / ~320M tokens**).
  The G²/co-occurrence computation (`signed_g2`, `compute_control`, FRAME_WIN=4, connectives, K=3) is
  **byte-identical to the s186 `build_cooc.py`** (verifier-confirmed); only the sentence-streaming IO
  adapter changed (gzipped C4 JSONL vs Simple-Wikipedia bz2 XML). C4 is a **different source family**
  from s186's Simple English Wikipedia, so a positive H1 outcome cannot be a same-corpus artifact.
- **Proxies** (pre-recovery): IS-A path depth per cue (`wn.synsets(cue,'n')[0].min_depth()`, the pilot
  spec, predicted sign **negative**); a corpus Hearst-frame definitional-density per cue (predicted
  sign **positive**, theory-set, frozen before counting).
- **Panel**: `panel.A/.B/.C`, temperature 0, zero-shot, neutral prompt (byte-identical to the s186
  neutral arm). One arm (frame-ablation dropped). 2,061 calls, **$0.3797 billed** (A $0.224 / B $0.064
  / C $0.092), 0 errors, 4 empties (all A: 2 synonymy, 1 hypernymy, 1 meronymy).

## The numbers (post-run verifier REPRODUCED, 0.000 max ρ discrepancy)

**Recovery (mean raw Soundness, per model per relation), ordered by mean recovery:**

| relation | A | B | C | IS-A depth | cue-strength (frame-G²) | Hearst density |
|---|---|---|---|---|---|---|
| hypernymy | 0.378 | 0.365 | 0.403 | 7.008 (deep) | 0.008 | 0.0123 |
| antonymy | 0.324 | 0.331 | 0.370 | **6.126 (shallowest)** | **0.149** | 0.0137 |
| hyponymy | 0.240 | 0.236 | 0.233 | 6.375 | 0.036 | 0.0147 |
| synonymy | 0.212 | 0.193 | 0.214 | 6.950 | 0.006 | 0.0126 |
| meronymy | 0.120 | 0.146 | 0.172 | 6.867 | 0.019 | 0.0146 |
| holonymy | 0.131 | 0.096 | 0.164 | 7.200 (deepest) | 0.031 | 0.0142 |

Recovery ordering (hypernymy > antonymy > hyponymy > synonymy > meronymy ≈ holonymy) holds 3/3 and
reproduces s186's shape (hypernymy best, part-whole worst, antonymy second) on **fresh cues + a fresh
corpus**. HIT@3 (gold-size-insensitive co-primary) gives the same recovery ordering.

**Across-relation Spearman (n=6, tie-naive — the s186 pipeline), per model — the SOLE verdict of record:**

| | A | B | C | pre-registered direction | verdict |
|---|---|---|---|---|---|
| ρ_cue (recovery vs cue-strength) | +0.143 | +0.086 | +0.086 | — | all ≤ +0.30 → **H1 REPLICATES 3/3** |
| ρ_depth (recovery vs IS-A depth) | −0.200 | −0.371 | −0.371 | negative | margin cleared **B,C (2/3)** → **H2 WINS** |
| ρ_hearst (recovery vs Hearst density) | −0.543 | −0.486 | −0.486 | positive | wrong sign → **loses 0/3** |

H2 margin rule (|ρ_proxy|−|ρ_cue| ≥ 0.20, predicted direction): depth clears on B (0.285) and C
(0.285), not A (0.057 — hypernymy being both deep *and* best-recovered caps A's depth correlation).
So IS-A depth, the pre-registered **primary** proxy, out-predicts cue-strength on **2/3** models, in
the predicted negative direction — **H2 fired-for**.

**Item-level secondary (DESCRIPTIVE/NON-DECISIVE per Q1-C):** within-cue ρ(own depth, own recovery),
n ≈ 687 pooled = **+0.055 / +0.008 / +0.042** — near-zero. This is a genuine, pre-named
**level-divergence**: the depth→recovery relationship is a **between-relation** fact (relation-mean
depth tracks relation-mean recovery) and is **absent at the cue level**. It cannot (per condition 1)
fire, upgrade, or downgrade the across-relation H2 verdict, but it materially scopes the reading: the
taxonomic-depth story is about **relation categories**, not about individual cues.

## Reading (what the result licenses, and what it does not)

1. **The cue-strength–recovery decoupling is robust (H1).** It survives a change of corpus family
   (encyclopedic Simple Wikipedia → C4 web text) and a change of cue set — the two strongest freshness
   moves short of a POS change. The essay's safer bet is confirmed on a fair fresh test; the
   decoupling was not a Simple-Wikipedia artifact. This is the load-bearing, 3/3 half.
2. **Taxonomic depth out-predicts cue-strength — at the relation grain, on 2/3 (H2).** Among the
   essay's candidate replacements, the pre-registered IS-A-depth proxy wins where raw contrastive-frame
   cue-strength failed: relations whose cues sit *higher/more superordinate* in the WordNet hierarchy
   are better recovered. This is the riskier half, and it fired **for** — but at 2/3, not 3/3, and
   between-relation only.
3. **It remains a WITHIN-DISTRIBUTIONAL result (the misreading the essay forbids).** IS-A depth is
   itself a form-internal structural statistic (WordNet's taxonomy has a dense corpus footprint). H2
   winning means *a different form-internal statistic out-ranks contrastive-frame co-occurrence* —
   **never** that recovery escapes distribution. Reference and grounding are untouched.
4. **The Hearst arm losing is informative, not just a null.** The corpus definitional-frame proxy
   correlated *negatively* with recovery (opposite its theory-set prediction), so the "definitional-frame
   density" operationalization of the essay's construct fails here while the structural (IS-A depth)
   operationalization succeeds. The taxonomic story that survives is **hierarchical position**, not
   **corpus genus-naming frequency**.

## Scope caps (LOAD-BEARING — read before citing)

- **Internal-contrast only** (Q4, ratified s193). No human comparison. The head-to-head cancels the
  shared WordNet target; the contrast is between corpus/lexicon predictors.
- **n = 3 models; orderings, not coefficients.** H1 is 3/3; H2 is **2/3** (A does not clear the depth
  margin). No pooling across models.
- **The verdict of record is across-relation (n = 6), and n = 6 is a wide-CI Spearman.** The item-level
  arm is powered (~687) but **descriptive/non-decisive** and shows the effect is **between-relation
  only** — a real limit on how far the depth reading generalizes.
- **Nouns only.** WordNet's taxonomic relations and `min_depth` are noun-scoped. The adjective-antonymy
  replication (H1's third freshness route) is a separate unit.
- **Construct-validity caveat.** IS-A depth and the recovery-scoring key share a source (WordNet);
  mitigated by the gold-independent cue-first-synset depth (a property of the cue, not the answer set).
- **HIT@3 is a co-primary, not verdict-bearing** — the frozen H1/H2 bands run on Soundness ρ_cue; HIT
  reproduces the H1 ordering and is reported for robustness, not as the decisive metric.
- **Provenance note.** C4 is ODC-BY **plus** Common-Crawl terms
  ([`resource/cooccurrence-corpus-scouting`](../../base/resources/cooccurrence-corpus-scouting.md)).

## What this feeds

- Fires [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md)
  trigger (b) **for** (a pre-registered taxonomic proxy out-predicts cue-strength); trigger (a) does
  **not** fire (H1 replicated, did not break). [`predictions.md`](../../predictions.md) §B row updated.
- Gives the lexical pole's **unplaced** shadow-saturated corner in
  [`theory/lexicon-grammar-continuum-v2`](../theory/lexicon-grammar-continuum-v2.md) a **measured
  re-placement candidate** (taxonomically-central/shallower relations carry the shallowest shadow) —
  scoped between-relation, 2/3, internal-contrast, within-distribution.
- A candidate future promotion review (adjective replication or a within-family ladder would strengthen
  the 2/3 H2); a `claim` is **not** written from this single run.
