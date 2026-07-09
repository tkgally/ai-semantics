---
type: result
id: adjective-antonymy-replication-v1
title: "Adjective-antonymy replication — in J&K's home POS the antonymy-shadow falsification REPLICATES and strengthens (antonymy clears a genuinely-strong contrastive-frame control, verdict-bearing 3/3), but the across-relation cue-strength–recovery DECOUPLING does NOT cleanly replicate (H1-PARTIAL): a POS boundary"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-09
updated: 2026-07-09
links:
  - rel: operationalizes
    target: essay/antonymy-outlier-distributional-shadow
  - rel: operationalizes
    target: essay/cue-strength-recovery-decoupling
  - rel: operationalizes
    target: design/adjective-antonymy-replication-v1
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
  - rel: depends-on
    target: source/justeson-katz-1991-antonym-cooccurrence
  - rel: depends-on
    target: source/cao-2025-distinctive-cooccurrence-antonymy
---

# Result — adjective-antonymy replication (H1 decoupling + the antonymy-shadow clause, in J&K's home POS)

> **Status: proposed · `anchor: internal-contrast-only` · adjectives only · n = 3 models, orderings not
> coefficients.** A **split verdict**, ratified + frozen + run this session (s196; design
> [`design/adjective-antonymy-replication-v1`](../../../experiments/designs/adjective-antonymy-replication-v1.md),
> gates ratified [`decisions/resolved/adjective-antonymy-replication-design`](../../decisions/resolved/adjective-antonymy-replication-design.md),
> PREREG frozen before any model call, post-run verifier recomputed from raw):
> 1. **The antonymy-shadow clause (registered PRIMARY) — ANT-CLEARS-CONTROL 3/3, and here it is
>    VERDICT-BEARING, not descriptive-only.** In J&K's *measured* home POS (predicative adjectives),
>    antonym recovery clears **wide daylight** above the contrastive-frame control (HIT@3 residual
>    **+0.52/+0.52/+0.54**, the *largest* of the four relations on all three models) — even though the
>    control is genuinely *strong* on adjective antonymy (control HIT@3 0.364, ≈3× the other relations).
>    The s186 falsification **replicates and strengthens** where the frame-saturation premise is
>    measured, not extrapolated.
> 2. **The frame-ablation arm — SURVIVES-SUPPRESSION 3/3.** Antonym recovery does not collapse when the
>    contrastive frame is removed (neutral HIT@3 0.88/0.88/0.89 ≥ frame-present) — a corpus-free
>    confirmation, in the home POS, of s186's "antonym recovery survives frame suppression."
> 3. **The across-relation cue-strength–recovery decoupling (registered CO-PRIMARY, H1) — DOES NOT
>    cleanly replicate: H1-PARTIAL/AMBIGUOUS.** ρ_cue = **+0.4/+0.8/+0.4** (soundness; one BREAKS, two
>    PARTIAL — neither a clean replicate at ≤+0.30 nor a clean 2/3 break at >+0.50), and the powered
>    item-level arm agrees (ρ ≈ **+0.25/+0.27/+0.24**, all 3). On **adjectives**, cue-strength partially
>    *recovers* its predictive power — a **POS boundary** on the clean noun decoupling (s186/s193).
>
> **No human comparison** (Q3): recovery is scored against WordNet, a shared target that cancels in the
> contrast; the predictor is a corpus statistic. **Within-distributional only.** **H2 is not tested** —
> WordNet has no adjective IS-A taxonomy (`min_depth()` is a degenerate constant 0), so the noun run's
> taxonomic-depth proxy cannot transfer (Q2-A). **The split blocks the decoupling→`claim` promotion the
> design aimed at:** a claim needs the decoupling to replicate across POS, and it did not.

## What ran

A **fresh** relatum-production probe (SEED 20260709) over **four WordNet adjective relations** —
antonymy, synonymy, similar-to (`similar_tos`), also-see (`also_sees`) — **130 fresh cues each** (520
total), disjoint from the 707 committed s186 noun cues (0 overlap asserted, 4/4), frequency-matched on
[`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md) Lg10WF band [2.0, 4.5]
to antonymy's profile. The panel ([`config/models.md`](../../../config/models.md) A/B/C) produced up to
3 relata per cued relation (neutral / frame-suppressed prompt), plus a mandatory antonymy **frame-present**
arm. Scored by **Soundness** (precision-over-produced) and the gold-size-insensitive **HIT@3** co-primary,
against WordNet adjective-relatum membership. The control is a contrastive-frame **G² co-occurrence**
statistic on **C4 web text** (`allenai/c4` en, shards 00000–00002, 22.3M sentences; ODC-BY) — the G²
computation **byte-frozen** from the s186/s193 instrument (verified by assertion), only the cue POS +
candidate pool changing. 1,950 calls, **$0.366**, 1 empty production (A-synonymy), post-run verifier
recomputed from raw.

**Why the POS is the whole point.** [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
*measured* contrastive-frame saturation on **predicative adjectives** — *"63% (139/219) of antonym
co-occurrences are in lexically identical structures … Fully 164 (75%) … appear in conjoined syntactic
structures"* — and the source page flags that extending it to nouns is *"an extrapolation beyond J&K's
data."* s186 and s193 tested the antonymy-shadow and decoupling claims on **nouns** (the extrapolation);
this tests them on **adjectives** (the measured ground). Two facts the POS change fixed *before any model
call*, both frozen in [`PREREG.md`](../../../experiments/runs/2026-07-09-adjective-antonymy-replication/PREREG.md):

- **The adjective contrastive-frame control is genuinely strong on antonymy.** Frozen frame-G²
  cue-strength: antonymy **0.1214** (HIT@3 0.364) vs synonymy 0.0465 / similar 0.0462 / also-see 0.0615
  (HIT@3 0.115–0.185). The control recovers antonym relata ≈3× better than any other relation's — J&K's
  measured adjective frame-saturation, made concrete. So a large *model* residual over it is a real
  clearance, not a floor artifact.
- **The calibration gate CLEARS.** Mean control-frame soundness = **0.0689 ≥ 0.05** (vs s186's noun-run
  0.029, which fired the gate and forced the residual arm to descriptive-only). So on adjectives the
  antonymy-shadow **RESIDUAL arm is verdict-bearing** — the confirmatory line the noun run could not run.

## The three arms (confirmatory vs descriptive, separated per the freeze review)

### 1. Antonymy-shadow clause (CONFIRMATORY — calibration cleared) — ANT-CLEARS-CONTROL 3/3

Per-cue HIT@3 residual = recovery(model, neutral) − control(frame), bootstrap 95% CI (B=2000):

| model | **antonymy** residual [95% CI] | synonymy | similar | also-see | verdict |
|---|---|---|---|---|---|
| A (claude) | **+0.519** [+0.419, +0.620] | +0.320 | +0.369 | +0.285 | CLEARS |
| B (gpt) | **+0.519** [+0.419, +0.620] | +0.341 | +0.323 | +0.323 | CLEARS |
| C (gemini) | **+0.535** [+0.434, +0.636] | +0.318 | +0.339 | +0.239 | CLEARS |

Antonymy carries the **largest** residual on all three models (its 95% lower bound, ≈+0.42, sits above
every other relation's point estimate), and it clears a control that is itself strongest on antonymy.
By the frozen relation-agnostic RANK+MARGIN rule (residual ≥ 0.10 **and** ≥ the 4-relation median →
CLEARS), the verdict is **ANT-CLEARS-CONTROL 3/3**. Model antonym recovery HIT@3 is 0.88/0.88/0.89 vs
the control's 0.364. **The s186 falsification is at its most robust: antonymy is not the shadow-saturated
relation even where its contrastive-frame saturation is measured-densest and the control is genuinely
strong.**

### 2. Frame-ablation (CONFIRMATORY, corpus-free) — SURVIVES-SUPPRESSION 3/3

Antonym recovery HIT@3, frame-suppressed (neutral) vs the J&K contrastive scaffold ("*X* versus ___",
"neither *X* nor ___", "from *X* to ___"): A 0.877 vs 0.785 · B 0.885 vs 0.777 · C 0.892 vs 0.892.
Neutral ≥ frame-present − 0.15 on all three (indeed neutral is *higher* for A and B — the frame slightly
*lowers* HIT, as s186 found for nouns). Removing the contrastive frame does **not** collapse antonym
recovery: the panel is not leaning on the frame to produce antonyms. Independent of the corpus control,
this re-confirms s186's frame-ablation finding in the home POS.

### 3. Across-relation cue-strength–recovery decoupling (CO-PRIMARY, at true low power ≤4 relations) — H1-PARTIAL/AMBIGUOUS

Recovery soundness per relation (neutral): antonymy tops every model (A 0.309 / B 0.317 / C 0.321),
then synonymy ≈ similar ≈ also-see (0.16–0.22, near-tied). Since antonymy is **both** the highest
cue-strength relation **and** the best-recovered, the rank-scramble that defined the noun decoupling does
not obtain: ρ_cue (tie-naive Spearman, recovery vs cue-strength, 4 relations) = **+0.4 / +0.8 / +0.4**
(soundness) — none ≤ +0.30 (no clean replicate), only one > +0.50 (no clean 2/3 break) → **H1-PARTIAL/
AMBIGUOUS**. The HIT@3 framing is similar (+0.4/+1.0/+0.2). **The powered item-level arm converges:**
pooled over all 520 cues, each cue's own contrastive-frame cue-strength positively (weakly) predicts its
own recovery, ρ = **+0.268/+0.272/+0.241** (all 3) — against the noun run's item-level ρ ≈ 0. Both the
under-powered across-relation arm and the powered item-level arm point the same way: **on adjectives,
contrastive-frame cue-strength partially predicts recovery**, so the clean noun decoupling is
**POS-specific**.

*(Descriptive, not verdict-bearing on its own: the across-relation arm is a 4-point Spearman [C4 caveat]
and cannot carry claim promotion; the item-level arm is locked descriptive/robustness-only [C7]. But
they agree, which is why the H1-PARTIAL reading is a genuine boundary, not a tie artifact.)*

## Why the decoupling is POS-bounded (the reading)

On **nouns** the decoupling was driven by **hypernymy** — a *low*-cue-strength but taxonomically central
relation — being the *best*-recovered, scrambling the recovery rank against cue-strength (s186 ρ ≈
−0.086; s193 ρ_cue ≈ +0.09). **Adjectives have no hypernymy** (no IS-A taxonomy — the same fact that
makes H2 untestable). The four adjective relations are all "closeness/opposition" relations, and the
most-cued one, **antonymy**, is also the sharpest and best-recovered — so nothing scrambles the rank, and
cue-strength regains weak predictive traction. The decoupling was never a claim about antonymy's own
recovery (which *clears* its control in both POS); it was a claim about the *cross-relation ordering*,
and that ordering is carried, on nouns, by a taxonomic relation adjectives lack. **This is consistent,
not contradictory:** antonymy clears its control (large residual) *and* cue-strength tracks the recovery
ordering (because antonymy tops both) can both hold at once.

## What this feeds

- **[`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md)
  — strengthened.** Its trigger (a) fired s186 in the *surviving* direction on nouns (residual
  descriptive-only, calibration gate fired). Here the same falsifier fires again in J&K's home POS **and
  is verdict-bearing** (calibration cleared): antonym recovery clears a strong contrastive-frame control
  by +0.52 HIT@3. The local-shadow reading is revised in-page (still *transferable-distributional*, not
  competence-beyond-distribution — the s151 relabeling holds).
- **[`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md)
  — scoped to nouns.** Its trigger (a) named the adjective-antonymy replication as a freshness route.
  The clean across-relation decoupling **did not cross the POS boundary** (H1-PARTIAL; item-level ρ ≈
  +0.25). The essay's thesis is re-scoped: the decoupling is a **noun** phenomenon, carried by the
  taxonomic relations adjectives lack; on adjectives cue-strength partially predicts recovery. Revised
  in-page.
- **NO claim promotion.** The design's stated aim — a second/third replication of the decoupling across
  corpus **and** POS as the route to promoting the s193 result to a `claim` — is **not** discharged: the
  decoupling did not cleanly replicate on adjectives. The s193 decoupling result stays a `result`; the
  decoupling `claim` is **blocked** pending a within-family or same-POS replication that holds.
- **[`predictions.md`](../../predictions.md)** — the decoupling essay's trigger (a) row updated (adjective
  route: did-not-replicate-cleanly, POS-bounded); the antonymy-shadow row updated (falsification
  replicates + strengthens in the home POS).

## Scope caps (LOAD-BEARING — read before citing)

1. **Internal-contrast only** (Q3): no human comparison. J&K's 63%/75% figures and Cao's human-vs-model
   gaps are **motivation only** — this result never asserts the panel reproduces or differs from J&K's
   measured saturation; its force is a within-instrument contrast (model recovery vs a corpus-statistic
   control on a shared WordNet target).
2. **Within-distribution only.** A residual over a co-occurrence control grades **local vs transferable
   distributional** generalization, not distribution vs non-distribution
   ([`essay/shortcut-vs-competence-mis-cut`](../essays/shortcut-vs-competence-mis-cut.md)).
   "Antonym recovery clears the contrastive-frame control" bears on the **local-shadow** reading only.
3. **n = 3 models; orderings, not coefficients; adjectives only. Never pooled with the noun probes.**
4. **H2 NOT tested** — adjective `min_depth()` degenerate constant 0; the noun taxonomic-depth proxy does
   not transfer (Q2-A). This result discharges H1 (in the POS-boundary direction) and re-tests the
   antonymy-shadow clause; it says nothing about H2.
5. **The across-relation H1 arm is ≤4 relations** (a coarse Spearman) and **cannot alone carry claim
   promotion** (C4); the H1-PARTIAL reading rests on the across-relation arm **and** the powered
   item-level arm agreeing.
6. **Calibration divergence from s186 noted:** the calibration gate is the single-condition form
   (`mean < 0.05`), pre-registered in C3, and the *stricter* direction; on adjectives it CLEARS (0.069),
   so unlike the noun run the residual arm is verdict-bearing here. This is a POS difference, not
   instrument drift.

## Provenance (verbatim, at stated strength)

- **J&K measured the frame saturation on adjectives (the motivation):** [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
  — *"63% (139/219) of antonym co-occurrences are in lexically identical structures"*; *"Fully 164 (75%)
  … appear in conjoined syntactic structures"*; scope — *"The evidence is on **predicative adjectives** in
  the Brown Corpus. Extending 'contrastive-frame saturation' to nominal antonymy … is … an **extrapolation
  beyond J&K's data**."*
- **The noun antonymy-shadow falsification (replicated + strengthened here):** [`result/lexical-relation-shadow-saturation-v1`](lexical-relation-shadow-saturation-v1.md)
  — antonymy carries *"one of the *largest* residuals, not the smallest"* (HIT@3 +0.61–0.67), residual arm
  **descriptive-only** (calibration gate fired, mean control 𝒮 0.029). Here the same clearance obtains
  **verdict-bearing** (gate cleared) in J&K's home POS.
- **The noun decoupling (POS-bounded here):** [`result/lexical-relation-recovery-taxonomic-proxy-v1`](lexical-relation-recovery-taxonomic-proxy-v1.md)
  — H1 DECOUPLING-REPLICATES 3/3 on fresh nouns + C4 (ρ_cue +0.14/+0.09/+0.09). The adjective route gives
  ρ_cue +0.4/+0.8/+0.4 → H1-PARTIAL, the boundary.
- **The corpus (license-cleared, s193-frozen):** [`resource/cooccurrence-corpus-scouting`](../../base/resources/cooccurrence-corpus-scouting.md)
  — C4 (`allenai/c4` en, *"released … under the terms of [ODC-BY]"*); 22.3M sentences streamed + discarded.
- **Cross-relation antonymy co-occurrence distinctiveness (adjacent support):** [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md).

## Reproduce

`experiments/runs/2026-07-09-adjective-antonymy-replication/`: `prep.py` (items), `build_cooc_c4.py`
(control), `probe.py` (panel), `analyze.py` (verdict) — all recompute from committed inputs (control.json
+ raw/ committed; counts.json re-derivable). `PREREG.md` frozen before any model call;
`REVIEW-ratify-s196.md` / `REVIEW-freeze-s196.md` carry the ratification + freeze reviews. **A fresh-agent
post-run verifier ([`REVIEW-verify-s196.md`](../../../experiments/runs/2026-07-09-adjective-antonymy-replication/REVIEW-verify-s196.md))
recomputed every headline number with an independent second implementation → REPRODUCED, 0 discrepancies,
max diff 0.0000** (antonymy residual n=129 traced to one control-null cue, not a model empty).
