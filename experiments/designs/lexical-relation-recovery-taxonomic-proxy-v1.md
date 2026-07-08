---
type: design
id: lexical-relation-recovery-taxonomic-proxy-v1
title: "lexical-relation recovery vs a pre-registered taxonomic proxy — a FRESH test of the cue-strength–recovery decoupling (H1) and whether IS-A depth out-predicts contrastive-frame cue-strength for relation-wise recovery (H2); internal-contrast, no human comparison. DESIGN, not frozen; four gates open"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: draft
anchor: pending
contingent-on:
  - lexical-relation-recovery-taxonomic-proxy-design
created: 2026-07-08
links:
  - rel: operationalizes
    target: essay/cue-strength-recovery-decoupling
  - rel: depends-on
    target: note/taxonomic-proxy-recovery-pilot-v1
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
---

# Design v1 — lexical-relation recovery vs a pre-registered taxonomic proxy (H1 + H2)

**A design + decision-trail unit (program A-lexical; the empirical discharge of the decoupling essay's
bets). Status: DESIGN, NOT FROZEN (s192, 2026-07-08).** Four value-laden gates are routed to
[`decisions/open/lexical-relation-recovery-taxonomic-proxy-design`](../../wiki/decisions/open/lexical-relation-recovery-taxonomic-proxy-design.md):
**Q1** (level of analysis for H2 — the anti-goalpost-moving gate), **Q2** (the fresh control corpus),
**Q3** (the second pre-registered proxy arm), **Q4** (the `anchor: internal-contrast-only` declaration).
Nothing here is frozen; no `prep.py` exists yet. This page operationalizes
[`essay/cue-strength-recovery-decoupling`](../../wiki/findings/essays/cue-strength-recovery-decoupling.md)
(the registered H1/H2 bet, [`predictions.md`](../../wiki/predictions.md) §B) and carries forward the
frozen proxy specification from [`note/taxonomic-proxy-recovery-pilot-v1`](../../wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md).

Per PROTOCOL §3/§A1 and the A1b precedent (design s184 → ratified s185 → run s186): **design s192,
ratifiable s193+, run after ratification.** The design opens a decision; a probe that opens a
value-laden decision is not run in the session that opens it.

> **Pre-run DESIGN review (s192, 2026-07-08) — GO-WITH-CONDITIONS; no BLOCKERS; FABRICATION-CHECK PASS.**
> Independent fresh-agent pre-run critic (verdict authority) **+** one non-Anthropic decorrelation vote
> (`openai/gpt-5.4-mini`, $0.0035265), both **GO-WITH-CONDITIONS**, recorded in
> [`REVIEW-design-s192.md`](../runs/2026-07-08-relation-recovery-taxonomic-proxy-design/REVIEW-design-s192.md).
> Faithfulness + anti-cheat PASS; every load-bearing quote/number verified against source. **Six
> freeze-time conditions bound to the freeze** (see the *Freeze-time conditions* section at the foot of
> this page). One live **Q2 divergence carried to the s193 ratifier**: the non-Anthropic vote picks
> **Q2-B (C4 primary)** over the design's default Q2-C (Wikipedia primary + C4 sensitivity), and the
> critic binds a Wikipedia-only scope-cap with C4 strongly preferred — the ratifier weighs whether C4
> becomes primary/co-primary. **Nothing frozen, nothing run; the gates are ratified s193+, not now.**

---

## Why this unit is owed now (and why it is doubly-motivated)

The s186 antonymy probe ([`result/lexical-relation-shadow-saturation-v1`](../../wiki/findings/results/lexical-relation-shadow-saturation-v1.md))
falsified the shadow-saturation conjecture and, in passing, logged a new observation the result page
deliberately did **not** develop: the **cue-strength–recovery decoupling** — across the six WordNet
noun relations, raw contrastive-frame co-occurrence cue-strength and panel recovery come apart
(across-relation Spearman ≈ **−0.086**, 3/3). The essay
[`essay/cue-strength-recovery-decoupling`](../../wiki/findings/essays/cue-strength-recovery-decoupling.md)
(s187) turned that seed into a two-part falsifiable bet:

- **H1 (safer) — the decoupling replicates.** On a fresh test (fresh relation set, a *different*
  control corpus, or the adjective-antonymy replication), recovery rank again decouples from raw
  contrastive-frame co-occurrence cue-strength — near-zero-or-negative across-relation rank
  correlation, ≥2/3 models. **Falsified** if cue-strength recovers its predictive power on a fresh
  set (a clearly positive rank correlation, ≥2/3) — i.e. s186's decoupling was corpus- or set-specific.
- **H2 (sharper, riskier) — taxonomic structure is the missing predictor.** On that same fresh test,
  recovery rank tracks a **pre-registered taxonomic/definitional-structure proxy** (*not* bare gold
  fan-out, which s186 already breaks) **better** than it tracks contrastive-frame cue-strength.
  **Falsified** if no pre-registered taxonomic proxy out-predicts cue-strength, or cue-strength
  out-predicts every proxy.

This design is that fresh test. It is **doubly-motivated**:

1. The theory second edition [`theory/lexicon-grammar-continuum-v2`](../../wiki/findings/theory/lexicon-grammar-continuum-v2.md)
   (s191) leaves the **lexical pole's shadow-saturated corner explicitly *unplaced*** after the
   antonymy bet lost, and names *"a fresh relation-recovery probe … the IS-A-depth proxy of
   [`note/taxonomic-proxy-recovery-pilot-v1`]"* as the trigger that would **re-place** it. This is
   that named trigger.
2. The proxy is already **provisionally pre-registered**. The taxonomic-proxy pilot note (s188) did the
   design due-diligence in a **$0, deliberately non-circular** way — it computed WordNet structural
   proxies over the s186 cue sets, confirmed bare gold fan-out fails, and pre-registered **IS-A path
   depth** (`min_depth`) as the default proxy **on principle, explicitly refusing the exploratory
   maximum** (gloss length, ρ = −0.83, was the top correlate and was **rejected** precisely because
   picking the strongest correlate on the hypothesis-generating data is the fishing move). This design
   carries that frozen specification into a real test.

## The one question (nothing wider)

On a **fresh** relatum-production probe over the six WordNet noun relations, run on the panel against a
**different** contrastive-frame co-occurrence (G²) control corpus, with **IS-A path depth pre-registered
before recovery is observed**: (H1) does recovery rank **again** decouple from contrastive-frame
cue-strength, and (H2) does IS-A path depth **out-predict** cue-strength for relation-wise recovery, in
the pilot-registered **negative** direction (more-superordinate/shallower cue sets recover better),
≥2/3 models?

This is the essay's bet in its internal-contrast form. It makes **no human comparison** (Q4): recovery
is model-vs-WordNet-definitional-target; cue-strength and IS-A depth are both **corpus/lexicon
structure statistics**; the finding is a within-instrument contrast of *which corpus/structure
statistic tracks recovery*, not a model-vs-human competence claim.

## Grounding in the sources (verbatim, at their stated strength)

- **The decoupling (the seed):** [`result/lexical-relation-shadow-saturation-v1`](../../wiki/findings/results/lexical-relation-shadow-saturation-v1.md)
  — *"The across-relation Spearman between raw recovery and corpus cue-strength is **−0.086** on every
  model. Antonymy **is** top of corpus cue-strength … but it is **not** top of recovery: **hypernymy**
  is best recovered … while meronymy — the *second*-most-cued relation — is *worst* recovered."*
  (`status: proposed`, `anchor: internal-contrast-only`, **n = 3 orderings not coefficients**, **nouns
  only**, residual arm **descriptive-only** because the calibration gate fired.)
- **The pre-registered proxy (frozen spec):** [`note/taxonomic-proxy-recovery-pilot-v1`](../../wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)
  — *"**IS-A path depth.** For each relation's cue set, take each cue's first WordNet noun synset
  (`wn.synsets(cue, pos='n')[0]`), compute its `min_depth()` … and average over the cues → the
  relation's **mean IS-A depth**. … **Predicted sign: negative** — more-superordinate (shallower) cue
  sets recover better — with **H2 winning only if |ρ(depth, recovery)| is clearly greater than
  |ρ(cue-strength, recovery)|** and in the predicted direction, ≥2/3 models."* The note is explicit
  the pilot **cannot** fire H2 (circular, n = 6, same corpus) and that IS-A depth was chosen *on
  principle, not because it topped* (it did not — gloss length did, and was refused).
- **The corpus (license-cleared):** [`resource/cooccurrence-corpus-scouting`](../../wiki/base/resources/cooccurrence-corpus-scouting.md)
  (s185) verified firsthand that **English Wikipedia** (Wikimedia dumps, *"licensed under the GNU Free
  Documentation License (GFDL) and the Creative Commons Attribution-Share-Alike 4.0 License"*) and
  **C4** (`allenai/c4`, *"We are releasing this dataset under the terms of [ODC-BY]"*) both clear the
  license bar — both **different** from s186's Simple English Wikipedia, so either satisfies H1's
  "different control corpus" freshness route.

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Internal-contrast only** (Q4). No human comparison. The head-to-head is *which corpus/structure
   statistic (contrastive-frame G² vs IS-A depth) better rank-predicts recovery* — a within-instrument
   comparison of predictors, not a model-vs-human claim.
2. **Within-distribution only.** Per the ratified [`essay/shortcut-vs-competence-mis-cut`](../../wiki/findings/essays/shortcut-vs-competence-mis-cut.md)
   discipline (s151) and the decoupling essay's own §"Why this is not 'recovery is non-distributional'":
   **IS-A path depth is itself a distributional/structural statistic** (WordNet's taxonomy has a dense
   Hearst-frame corpus footprint). If H2 wins, it wins as *a different form-internal statistic
   out-ranking contrastive-frame co-occurrence* — **never** as evidence that recovery escapes
   distribution. Reference and grounding are untouched.
3. **n = 3 models; orderings, not coefficients.** The verdict is a direction on ≥2/3 models, never a
   pooled coefficient.
4. **The across-relation test is n = 6 relations** — severely underpowered as a Spearman (this is
   exactly what Gate Q1 confronts). The registered bet is nonetheless across-relation; the item-level
   arm (Q1) supplies power **without** redefining the bet.
5. **Nouns only.** WordNet's taxonomic relations (and `min_depth`) exist for nouns; the
   adjective-antonymy replication (H1's third freshness route) is a **separate** unit, not this one.

## Panel & settings

Panel = the three [`config/models.md`](../../config/models.md) slots (`panel.A`/`.B`/`.C` — never
hardcode slugs); all three as subjects, cross-model divergence is data. Temperature 0, zero-shot,
single-turn, neutral system prompt. `google/*` gets `reasoning={"effort":"minimal"}` (config caveat).
Every call records `usage.cost` via [`experiments/lib/openrouter.py`](../lib/openrouter.py).

## Design — item scheme (fresh WordNet noun relation cues, disjoint from s186)

Reuses the **s186 instrument shape** ([`design/lexical-relation-shadow-saturation-v1`](lexical-relation-shadow-saturation-v1.md);
ratified gates in [`decisions/resolved/antonymy-internal-contrast-scoring`](../../wiki/decisions/resolved/antonymy-internal-contrast-scoring.md))
so H1 is a like-for-like fresh replication — same six relations, same relatum-production task, same
Soundness / HIT@3 scoring, same frequency-matching + outlier-capping — changing exactly three things to
make it a genuine **fresh** test:

- **Six relations (unchanged):** antonymy, synonymy, hypernymy, hyponymy, holonymy, meronymy
  (WordNet 3.0 via `nltk`; [`resource/wordnet-sense-inventory`](../../wiki/base/resources/wordnet-sense-inventory.md),
  BSD-style license verified in-repo). Nouns only.
- **FRESH cues, disjoint from s186 (change 1).** s186 sampled **130 nouns/relation, seed 20260706, freq
  band Lg10WF ∈ [2.0, 4.5]** (`items.json`: antonymy *absence, acceptance, advance, …*; etc.). This
  design **excludes all 780 s186 cues before sampling** a fresh set (new seed, asserted + re-verified
  0-overlap per relation, exactly the disjointness discipline of the s181/s178/s175 powered re-runs),
  frequency-matched on [`resource/subtlex-us-frequency`](../../wiki/base/resources/subtlex-us-frequency.md)
  Lg10WF, with the same **highest-G² outlier cap** (Cao's *man/woman, parent/child* nominal-antonymy
  inflation hazard) frozen at freeze. Powered N per relation (PROTOCOL §4): **~120–150 cues/relation**
  where WordNet supplies enough fresh pairs, antonymy capped lower by WordNet nominal sparsity and
  **reported as such** — a per-relation N, not a pooled N.
- **A DIFFERENT control corpus (change 2, Q2).** s186 built the contrastive-frame G² control from
  **Simple English Wikipedia**. This design uses a **different** license-cleared corpus (Q2) so a
  positive H1 outcome cannot be a same-corpus artifact — the essay's own counter says *"a cue-strength
  measured on a corpus closer to the panel's training mix could rank the relations differently, and the
  decoupling is only as good as that proxy."* The contrastive-frame G² construction itself
  (frames: "X versus Y", "neither X nor Y", "from X to Y", conjunction/adjacency; window; weighting) is
  **byte-frozen from the s186 `build_cooc.py`** so only the corpus changes, not the instrument.
- **A pre-registered taxonomic proxy (change 3, the H2 arm).** IS-A path depth (Q3 primary), frozen
  from the pilot spec, computed over the **fresh** cue sets **before** recovery is observed.
- **Per cue:** the model produces up to *k* relata for the named relation (Cao's open-ended format,
  k frozen at freeze, matching s186); scored against WordNet relatum membership. The **frame-ablation
  arm is dropped** here (s186 already ran it; it bears on the local-shadow reading, not on H1/H2) —
  keeping the probe lean and the spend on the fresh recovery measurement that H1/H2 need.

## GATE Q1 — level of analysis for H2 (the anti-goalpost-moving gate)

The essay registered H2 as an **across-relation rank** hypothesis: recovery rank vs proxy rank, over
the six relations, head-to-head against cue-strength rank. But **n = 6 relations is severely
underpowered** — a Spearman on 6 points cannot be significant, and the pilot note flags this explicitly.
There is a far more powerful test latent in the same data (IS-A depth is a **per-cue** property, so
recovery can be regressed on a cue's own depth at the **item** level, N ≈ 700–900). Choosing the
item-level test *alone*, however, would be **moving the goalposts** — it tests a related-but-distinct
within-relation hypothesis, not the essay's registered across-relation bet. Options:

- **Q1-A — across-relation rank only** (6 points). Faithful to the exact registered bet; underpowered.
- **Q1-B — item-level cue-depth regression only** (~700–900 items; powered). Tests whether a cue's own
  IS-A depth predicts *its* recovery. Powered, but a **different** hypothesis than the registered
  across-relation one — adopting it alone silently redefines H2 after the fact.
- **Q1-C (provisional default) — across-relation rank as the PRIMARY, registered, verdict-bearing test
  (n = 6, reported honestly with its wide CI), PLUS the item-level analysis as a POWERED SECONDARY**,
  reported side-by-side. The head-to-head of record stays |ρ(depth, recovery)| vs |ρ(cue-strength,
  recovery)| across relations, ≥2/3 models (the essay's exact bet); the item-level arm adds power and
  guards against an n=6 fluke **without** changing what H2 was registered to predict. A **divergence**
  between the two levels (e.g. across-relation favours depth but item-level does not, or vice versa) is
  itself a first-class reported outcome, not smoothed over.

**Why value-laden:** the choice is *what counts as testing H2*. Q1-B alone would answer an easier,
better-powered, but **different** question; Q1-A alone accepts near-zero power on the registered bet.
Q1-C keeps the registered bet primary and buys power honestly — but it must pre-commit that the
across-relation result is the verdict of record even if the item-level arm looks stronger.

## GATE Q2 — the fresh control corpus

H1's falsifier requires a **fresh** test; a "different control corpus" is one of its three named routes,
and the cleanest one for a noun-relation replication (the adjective route is a separate unit; a "fresh
relation set" over WordNet's six noun relations is just fresh cues, already change 1). Both candidates
below cleared the s185 license scout firsthand. Options:

- **Q2-A — full English Wikipedia** (Wikimedia dumps, CC BY-SA 4.0 + GFDL). Cleanest license, best
  proxy for the panel's pretraining mix (heavily represented in LLM training), billions of words. **But
  it is the same *source family* as s186's Simple English Wikipedia** (encyclopedic register, larger
  vocabulary/complexity) — a real change (≈100× larger, un-simplified register) but the *weakest*
  register-decorrelation of the options.
- **Q2-B — C4** (`allenai/c4` en, ODC-BY). Web register, genuinely **different** from encyclopedic
  Simple Wikipedia — the strongest test of H1's "corpus closer to the training mix could rank
  relations differently" counter. Heavier to fetch (~305 GB, but streamable; only the fixed fresh cue
  set need be counted), Common-Crawl-terms caveat recorded.
- **Q2-C (provisional default) — full English Wikipedia as PRIMARY (cleanest license + best pretraining
  proxy + decisively larger/different-register than *Simple* Wikipedia) + C4 as a labelled
  register-decorrelation SENSITIVITY arm** iff the fetch/compute is tractable within the day's budget
  and effort; if only one is tractable, **Wikipedia is primary and the C4 arm is deferred and named**
  (an honest scope note, not a silent drop). The cue-strength G² ranking used for the H1/H2 head-to-head
  is Wikipedia's; the C4 arm, if run, tests whether the decoupling and the depth-vs-cue-strength verdict
  survive a register change.

**Why value-laden:** how "different" the corpus must be *is* how strong a fresh test H1 gets. Full
Wikipedia is the cheap, clean, defensible choice but the least register-decorrelated; C4 is the
strongest fresh test but the heaviest lift. The decision fixes whether register-decorrelation is
required for the primary verdict or is a sensitivity check.

## GATE Q3 — the second pre-registered proxy arm (definitional-frame)

The pilot pre-registered **IS-A path depth** as the single default proxy, but flagged that the essay's
*actual* named "definitional-frame statistic" means **corpus Hearst-style hypernym frames** ("X such as
Y", "Y and other X", genus-naming templates) — a corpus statistic WordNet gloss-length only cheaply
echoes, and which the pilot deliberately **did not** freeze. Since the control corpus is fetched anyway
(Q2), a corpus definitional-frame proxy is nearly free to compute and tests the essay's own "it would
still be a distributional story" framing head-on. Options:

- **Q3-A (provisional default) — IS-A path depth PRIMARY (the pilot's frozen spec) + a corpus
  Hearst-frame definitional-density proxy as a SECOND pre-registered arm.** Per the essay, H2 is
  satisfied if *any* pre-registered taxonomic/definitional proxy out-predicts cue-strength (≥2/3); both
  proxies frozen — spec, frames, and predicted sign — **before** recovery is seen. The Hearst proxy's
  construction is frozen in `prep.py` under the same anti-cheat discipline as the G² control and cited
  as the project's own synthesis (as with the s186 contrastive-frame G²).
- **Q3-B — IS-A path depth only** (simplest; faithful to the pilot's single pre-registered proxy; but
  leaves the essay's actual definitional-frame candidate untested and forgoes a nearly-free arm).
- **Q3-C — add the ill-behaved candidates** (subtree connectivity, polysemy). **Rejected up front**:
  the pilot showed subtree connectivity is indistinguishable from the fan-out baseline and gloss length
  is a fishing hazard; adding them dilutes the pre-registration.

**Why value-laden:** whether H2's "taxonomic/definitional-structure proxy" is operationalized narrowly
(one structural primitive) or as the essay wrote it (structural **or** definitional-frame) changes what
can fire H2 — and adding a second arm raises the multiple-comparison bar, which the freeze must handle
(a pre-registered rule: H2 fires-for only if a **named** proxy wins in its **pre-registered** direction).

## GATE Q4 — anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — following the s186 Q3 ratification
  exactly. Recovery is scored against WordNet as a **shared definitional target that cancels in the
  head-to-head** (both the depth story and the cue-strength story predict the *same* recovery vector);
  the predictors are corpus/lexicon **statistics**; no human recovery baseline enters. So the result
  makes **no human-comparison claim** and no `resource` anchor is required (CLAUDE.md terminal state;
  the s186 gloss-extension — internal-contrast covers model-vs-computational-baseline — applies here
  too). Per CLAUDE.md this terminal declaration itself needs cross-session ratification, which this
  decision supplies. Until ratified the design carries `anchor: pending` naming this decision in
  `contingent-on:`.

## Metrics + verdict map (direction fixed at freeze; thresholds tightened-not-loosened)

Let ρ_cue = across-relation Spearman(raw recovery 𝒮(model), contrastive-frame G² cue-strength) and
ρ_depth = across-relation Spearman(raw recovery, mean IS-A depth), both over the six relations, per
model. Recovery 𝒮 = Soundness (Cao's precision-over-produced) with the gold-size-insensitive **HIT@3**
co-primary carried from s186.

- **H1 (verdict-bearing, safer) — DECOUPLING-REPLICATES** iff ρ_cue is **near-zero or negative** on
  **≥2/3** models (pre-registered band fixed at freeze, e.g. ρ_cue < +0.3). **DECOUPLING-BREAKS**
  (H1 falsified) iff ρ_cue is **clearly positive** (e.g. > +0.5) on ≥2/3 — cue-strength recovered its
  predictive power on a fresh corpus/set, so s186's decoupling was corpus- or set-specific (fires the
  essay's revision trigger (a); scope the reading to s186's setting or retract).
- **H2 (verdict-bearing, riskier) — TAXONOMIC-PROXY-WINS** iff a **pre-registered** proxy (IS-A depth,
  or the Q3 Hearst arm) satisfies **|ρ_proxy| > |ρ_cue|** in its **pre-registered direction** (depth:
  **negative**) on **≥2/3** models (Q1-C: across-relation primary; item-level powered secondary
  reported alongside). **TAXONOMIC-PROXY-LOSES** (H2 fired-against) iff no pre-registered proxy
  out-predicts cue-strength, or cue-strength out-predicts every proxy — the decoupling is real but
  taxonomic structure is not the filler; the "what predicts recovery" question reopens with taxonomic
  structure ruled out.
- **Pre-named nulls (first-class):** ρ_cue and ρ_depth both near-zero (recovery tracks *neither* corpus
  statistic — an honest "we don't yet know what predicts recovery"); or the across-relation and
  item-level arms **diverge** (reported, not resolved by fiat).
- **n = 3, orderings not coefficients; nouns only** (scope caps 3, 5). No pooling across models.
- **Anti-cheat fence (PROTOCOL §B):** the fresh cue sets, the outlier caps, k, both proxy specs and
  their predicted signs, the ρ_cue / ρ_depth bands, and the H1/H2 verdict thresholds are **all frozen
  in `PREREG.md` before any model call**. No proxy, band, or threshold is touched after recovery is
  seen. The nulls and the H1-break / H2-lose outcomes are pre-named first-class results, not failures.

## Cost (pre-flight estimate)

Relatum production is short-output, temperature 0. ~120–150 cues/relation × 6 relations
(≈720–900 verdict-bearing items, antonymy capped lower) × k relata × 3 models, one prompt frame
(frame-ablation dropped) ≈ **2,200–2,800 calls** at short completions — the same order as s186's 2,730
calls at **$0.4661**. Projects **≈ $0.35–$0.65** — well inside one UTC day's $5 cap, single-run under
the prefer-split $2.50 flag. The corpus fetch is $0 (bandwidth) but is the effort-gating sub-step
(Wikipedia dump is the lighter fetch; C4 heavier — Q2). A hard `ABORT_USD` (≈ $1.5) goes in `prep.py`
at freeze. Re-estimated at freeze once k and per-relation N are fixed.

## What each outcome feeds

- **H1 REPLICATES + H2 WINS (IS-A depth out-predicts cue-strength, negative, ≥2/3):** fires the essay's
  revision trigger (b) **for**; the "what predicts recovery" question gains a promotable answer; the
  lexical pole's **unplaced** shadow-saturated corner in
  [`theory/lexicon-grammar-continuum-v2`](../../wiki/findings/theory/lexicon-grammar-continuum-v2.md)
  gains a *measured* re-placement candidate (taxonomic-central relations carry the shallowest shadow) —
  still `internal-contrast-only`, still within-distribution.
- **H1 REPLICATES + H2 LOSES:** the decoupling is robust but taxonomic structure is not the filler —
  trigger (b) fired-against; a clean, honest partial (the risky half loses while the safe half wins,
  exactly as the essay pre-named).
- **H1 BREAKS:** cue-strength recovers on a fresh corpus — trigger (a); scope s186's decoupling to its
  Simple-Wikipedia/noun setting or retract. A first-class negative that would also caution the
  decoupling essay's whole reading.
- **Registers a [`predictions.md`](../../wiki/predictions.md) row** at **freeze** (a probe-specific
  H1/H2 row co-registered with the existing §B decoupling bet — not double-scored); outcome updated the
  run session.

## Handoff (what s192 did, and what remains)

1. **s192 (this session):** wrote this design; opened
   [`decisions/open/lexical-relation-recovery-taxonomic-proxy-design`](../../wiki/decisions/open/lexical-relation-recovery-taxonomic-proxy-design.md)
   (Q1–Q4, provisional defaults Q1-C / Q2-C / Q3-A / Q4 internal-contrast-only); ran the design pre-run
   critic (fresh agent) + one non-Anthropic decorrelation vote (recorded under
   [`experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy-design/`](../runs/2026-07-08-relation-recovery-taxonomic-proxy-design/)).
   **Nothing frozen, nothing run.**
2. **Ratify (s193+):** fresh reviewer + one non-Anthropic vote fix Q1–Q4 (never the opening session).
3. **Freeze (after ratification):** fetch the Q2 corpus (own resource page + verified license already
   scouted); write `prep.py` (fresh disjoint cue build, freq-matched, outlier-capped; byte-freeze the
   s186 G² construction, only the corpus changing; compute + freeze IS-A depth and any Q3 proxy over the
   fresh cues); fix k / per-relation N / ρ-bands / thresholds; commit PREREG before any model call;
   independent pre-run critic + one non-Anthropic vote; `ABORT_USD` set.
4. **Run (after freeze)** on the panel; post-run verifier recomputes every figure from raw. Powered N
   per PROTOCOL §4.

## Freeze-time conditions (bound s192 by the pre-run review; honor all six at freeze)

From the s192 fresh-agent critic (verdict authority) + non-Anthropic vote
([`REVIEW-design-s192.md`](../runs/2026-07-08-relation-recovery-taxonomic-proxy-design/REVIEW-design-s192.md)).
All are PREREG/`prep.py` specifications, not gate rewrites; they bind the freeze session:

1. **Q1 verdict-of-record binding.** PREREG states as a hard commitment that the **across-relation (n=6)
   result is the sole verdict of record for H1 and H2**; the item-level cue-depth arm is
   **descriptive/robustness-only** and can never on its own fire H2 or upgrade an across-relation
   H2-loss to a win. A level-divergence is a pre-named first-class outcome.
2. **Close the ρ_cue band gap.** Exhaustive, mutually-exclusive H1 bands over the whole line (no
   uncovered [+0.3, +0.5] middle), and a **numeric** H2 margin for "|ρ_proxy| clearly greater than
   |ρ_cue|," fixed before any model call (replace the illustrative "e.g." thresholds above).
3. **Q2 register scope-cap + C4.** A Wikipedia-only H1-REPLICATES reading carries an explicit
   same-source-family / register-decorrelation-untested scope note and does not claim to fully discharge
   H1's "different corpus" route; **C4 strongly preferred as co-primary, or run whenever tractable**,
   reason documented if deferred. *(The non-Anthropic vote dissented toward Q2-B, C4-primary — the s193
   ratifier weighs this.)*
4. **Clarify "byte-frozen."** Byte-identity applies to the **G²/co-occurrence computation** (`FRAME_WIN`,
   connective set, K, weighting, `signed_g2`) — verified unchanged against s186 `build_cooc.py`; the
   per-corpus sentence-streaming/IO adapter necessarily changes but must not touch any counting/weighting
   logic.
5. **Q3 multiple-comparison rule + Hearst sign.** IS-A depth primary, Hearst-frame proxy secondary;
   freeze the Hearst construction **and its theory-set predicted sign** before any corpus counting on the
   fresh cues; a Hearst-only H2 win (IS-A depth loses) is reported as a **qualified/weaker** result, not
   an equal-status H2-WINS.
6. **Disjointness + fresh-N reporting.** Exclude the exact committed 780 s186 cue lemmas with asserted
   per-relation 0-overlap; report the achieved fresh per-relation N (antonymy expected ~100, capped by
   WordNet nominal sparsity).

**Construct-validity scope caveat (not a gate):** IS-A depth and the recovery-scoring key share a source
(WordNet); mitigated by the pilot's gold-independent cue-first-synset depth ("a property of the cue, not
a restatement of the answer set"). Carry as a scope caveat on the eventual result; Q4 stays
internal-contrast-only.
