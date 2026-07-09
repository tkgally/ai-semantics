---
type: design
id: adjective-antonymy-replication-v1
title: "Adjective-antonymy replication — the cue-strength–recovery decoupling (H1) and the s186 antonymy-shadow falsification, re-tested in J&K's HOME part of speech (adjectives), where contrastive-frame saturation is measured-strongest; internal-contrast, no human comparison. DESIGN, not frozen; three gates open"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: frozen
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-09
updated: 2026-07-09
links:
  - rel: operationalizes
    target: essay/cue-strength-recovery-decoupling
  - rel: operationalizes
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: note/taxonomic-proxy-recovery-pilot-v1
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

# Design v1 — adjective-antonymy replication (H1 decoupling + the antonymy-shadow clause, in J&K's home POS)

**A design + decision-trail unit (program A-lexical; the third freshness route the decoupling essay
names — the adjective-antonymy replication — and the direct route toward promoting the s193
relation-recovery result to a `claim`). Status: DESIGN — three gates open, ratifiable s196+.** This
page operationalizes [`essay/cue-strength-recovery-decoupling`](../../wiki/findings/essays/cue-strength-recovery-decoupling.md)'s
registered **H1** (revision trigger (a)) and [`essay/antonymy-outlier-distributional-shadow`](../../wiki/findings/essays/antonymy-outlier-distributional-shadow.md)'s
contrastive-frame premise, re-tested where Justeson & Katz actually **measured** contrastive-frame
saturation: **predicative adjectives**. Per PROTOCOL §3/§A1 and the A1b/s192 precedent (design one
session, ratify the next, run after ratification): **design s195, ratifiable s196+, run after
ratification.** A probe that opens a value-laden decision is not run in the session that opens it.

> **RATIFIED s196 (2026-07-09), autonomous cross-session adversarial review — Q1-C / Q2-A / Q3
> internal-contrast-only ADOPTED.** Fresh-agent reviewer (verdict authority) + convergent fresh
> non-Anthropic vote (`panel.B`); `anchor: pending` → `internal-contrast-only`, `contingent-on:`
> cleared. One added freeze condition **C8** (frame-ablation numeric decision rule). Record:
> [`decisions/resolved/adjective-antonymy-replication-design`](../../wiki/decisions/resolved/adjective-antonymy-replication-design.md),
> [`REVIEW-ratify-s196.md`](../runs/2026-07-09-adjective-antonymy-replication/REVIEW-ratify-s196.md).
> Frozen + run s196 → [`result/adjective-antonymy-replication-v1`](../../wiki/findings/results/adjective-antonymy-replication-v1.md).
>
> **Pre-run DESIGN review (s195, 2026-07-09) — GO-WITH-CONDITIONS; no BLOCKERS; FABRICATION-CHECK PASS.**
> Independent fresh-agent pre-run critic (verdict authority) **+** one non-Anthropic decorrelation vote
> (`panel.B`, $0.00269775, via the probe REST path, PROTOCOL §A3), both **GO/ADOPT with conditions**,
> recorded in
> [`REVIEW-design-s195.md`](../runs/2026-07-09-adjective-antonymy-replication-design/REVIEW-design-s195.md).
> Both converged on **Q1-C / Q2-A / Q3 internal-contrast-only**. The critic verified every load-bearing
> quote/number against source (J&K 63%/75%, s186 residuals/Spearman/calibration, s193 ρ_cue) and
> **empirically confirmed H2 cannot transfer** — adjective `min_depth()` returns a **degenerate constant
> 0** (adjective synsets have no hypernym paths), so the "no IS-A taxonomy" claim is stronger than
> "undefined." **Seven freeze-time conditions** are bound to the freeze (see the *Freeze-time
> conditions* section at the foot of this page); the central one (C1) makes the antonymy frame-ablation
> arm **mandatory**, as the corpus-free powered hedge against the calibration gate refiring.
> **Nothing frozen, nothing run; the gates are ratified s196+, not now.**

---

## Why this unit is owed now — and why the POS is the whole point

Two lexical results converge on one gap. **s186**
([`result/lexical-relation-shadow-saturation-v1`](../../wiki/findings/results/lexical-relation-shadow-saturation-v1.md))
falsified the antonymy shadow-saturation conjecture over six WordNet **noun** relations (antonymy
recovery *clears* wide daylight above a contrastive-frame co-occurrence control — HIT@3 residual
+0.61–0.67, among the *largest*, not the smallest — and raw recovery does not track corpus cue-strength,
across-relation Spearman ≈ −0.086). **s193**
([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../../wiki/findings/results/lexical-relation-recovery-taxonomic-proxy-v1.md))
replicated the cue-strength–recovery **decoupling** (H1) on fresh noun cues + a different corpus family
(C4), 3/3. Both stand on **nouns only**. But the contrastive-frame premise both lean on was never a
noun fact:

> **The decisive motivation (from the J&K source page's own "What it cannot ground").**
> [`source/justeson-katz-1991-antonym-cooccurrence`](../../wiki/base/sources/justeson-katz-1991-antonym-cooccurrence.md)
> measured contrastive-frame saturation on **predicative adjectives** in the Brown Corpus — *"63%
> (139/219) of antonym co-occurrences are in lexically identical structures … Fully 164 (75%) … appear
> in conjoined syntactic structures"* — and the source page is explicit that *"Extending
> 'contrastive-frame saturation' to nominal antonymy … is plausible but is an **extrapolation beyond
> J&K's data**, not something J&K measured."* So s186/s193 tested the shadow-saturation and decoupling
> claims in the POS where the contrastive-frame premise is an **extrapolation**. This design tests them
> where the premise is **measured** — the strongest ground for the deflationary "the shadow is largest
> at antonymy" reading. If antonymy recovery *still* clears the contrastive-frame control here, the
> s186 falsification is at its most robust (it survives even where the frame-saturation is
> measured-densest). If, instead, the measured-denser adjective framing finally lets the control
> reconstruct recovery, shadow-saturation holds **specifically where J&K's premise is real** — a clean,
> first-class POS boundary on the falsification. Both outcomes are informative; neither is a re-run.

The essay names exactly this route. H1's revision trigger (a) lists *"a fresh relation set, a
**different** control corpus, **or the named adjective-antonymy replication**"* as its three freshness
routes; s193 spent the first two, and the decoupling essay's own honest counter flags that *"n = 3,
orderings not coefficients; **nouns only** … The named adjective-antonymy replication (Justeson &
Katz's home part of speech) has not run; a different panel, or adjectival relations, could behave
differently."* This is that route. A POS change is a **larger** perturbation than a corpus change: it
changes the relation inventory, the cue vocabulary, and the register of the contrastive frames. So a
second H1 replication here — on top of s193 — is what a `claim` promotion of the decoupling would rest
on (two independent replications across corpus **and** POS).

## The honest asymmetry this design fixes at the outset — H2 does NOT transfer

**The adjective route can discharge H1; it *cannot* replicate H2.** H2's pre-registered proxy is **IS-A
path depth** ([`note/taxonomic-proxy-recovery-pilot-v1`](../../wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)),
and WordNet has **no IS-A taxonomy for adjectives** — adjectives are organized by antonymy and
satellite (`similar_to`) clustering, not by hypernym paths, so `min_depth()` is **degenerate for
adjective synsets: it returns a constant 0** (adjective synsets have empty `hypernyms()`; verified
this session by the fresh-agent critic on `cold.a.01`), carrying no per-cue signal to correlate with
recovery. The s186 `prep.py` states the same in its own header: *"adjectives carry only
antonymy/synonymy, so a 6-relation cross-relation ranking is inherently nominal."* Therefore:

- This unit replicates **H1** (the decoupling) across a POS boundary and re-tests the **antonymy-shadow
  clause** in J&K's home POS. It is the direct route to promoting the **decoupling** to a `claim`.
- It does **not** push H2 from 2/3 toward 3/3 — H2's frozen IS-A-depth proxy is noun-only. Any
  structural proxy for adjectives would be a **new** bet with a new proxy, not a replication of H2 (Gate
  Q2 decides whether to open one). This corrects the optimistic "test whether H1/H2 hold beyond nouns"
  framing in the backlog: **H1 yes, H2 no.**

## The one question (nothing wider)

On a **fresh** relatum-production probe over WordNet **adjective** relations (antonymy plus a
pre-registered set of the adjective-available relations — Gate Q1), run on the panel against a
contrastive-frame co-occurrence (G²) control built on C4 web text (the s193-scouted, license-cleared
corpus; the byte-frozen s186/s193 G² construction, only the cue POS changing):

1. **(H1, the registered decoupling — essay trigger (a)):** does across-relation recovery rank **again
   decouple** from contrastive-frame cue-strength (near-zero or negative ρ_cue, ≥2/3 models), now in a
   different POS — or does cue-strength recover its predictive power on adjectives (clearly positive
   ρ_cue, ≥2/3), showing the decoupling was noun-specific?
2. **(the antonymy-shadow clause — s186 clause 1 / the antonymy-outlier essay, in J&K's home POS):** is
   adjective antonymy recovery **among the largest** residuals over the contrastive-frame control (the
   s186 falsification replicates where the frame-saturation is measured-strongest) — or is it the
   **smallest / near-zero** (the measured-denser adjective framing reconstructs antonym recovery, so
   shadow-saturation holds specifically for adjectives)?

Both are **internal-contrast**: recovery is model-vs-WordNet-definitional-target; cue-strength is a
corpus statistic; the finding is a within-instrument contrast of *which corpus statistic tracks
recovery, and whether antonymy's recovery is reconstructed by the contrastive-frame shadow* — **no
model-vs-human claim** (Gate Q3).

## Grounding in the sources (verbatim, at their stated strength)

- **J&K measured contrastive-frame saturation on adjectives (the motivation):**
  [`source/justeson-katz-1991-antonym-cooccurrence`](../../wiki/base/sources/justeson-katz-1991-antonym-cooccurrence.md)
  — *"63% (139/219) of antonym co-occurrences are in lexically identical structures"*; *"Fully 164
  (75%) of these 219 co-occurrences appear in conjoined syntactic structures."* Scope, from the same
  page: *"The evidence is on **predicative adjectives** in the Brown Corpus. Extending 'contrastive-frame
  saturation' to nominal antonymy … is plausible but is an **extrapolation beyond J&K's data**."*
- **The decoupling + the noun-only caveat (the seed):** [`result/lexical-relation-shadow-saturation-v1`](../../wiki/findings/results/lexical-relation-shadow-saturation-v1.md)
  — *"antonymy is NOT the relation whose recovery is least separable from the control — it carries one
  of the *largest* residuals, not the smallest. And raw recovery does not track corpus cue-strength
  (Spearman ≈ −0.09)."* `status: proposed`, `anchor: internal-contrast-only`, **n = 3 orderings**,
  **nouns only**, residual arm **descriptive-only** (the calibration gate fired: mean control 𝒮 = 0.029
  < 0.05).
- **H1 already replicated once (on nouns):** [`result/lexical-relation-recovery-taxonomic-proxy-v1`](../../wiki/findings/results/lexical-relation-recovery-taxonomic-proxy-v1.md)
  — H1 DECOUPLING-REPLICATES 3/3 on fresh cues + C4 (ρ_cue +0.14/+0.09/+0.09). This design adds the
  second, POS-crossing replication.
- **The corpus (license-cleared, already fetched-and-frozen at s193):** [`resource/cooccurrence-corpus-scouting`](../../wiki/base/resources/cooccurrence-corpus-scouting.md)
  — C4 (`allenai/c4` en, *"We are releasing this dataset under the terms of [ODC-BY]"*). The s193 run
  streamed shards 00000–00002 and froze the G² construction in `build_cooc_c4.py`; this design reuses
  that construction, only swapping noun cues for adjective cues.

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Internal-contrast only** (Q3). No human comparison. The head-to-head is *which corpus statistic
   tracks recovery, and whether the contrastive-frame shadow reconstructs antonym recovery* — a
   within-instrument comparison, not a model-vs-human claim.
2. **Within-distribution only.** Per [`essay/shortcut-vs-competence-mis-cut`](../../wiki/findings/essays/shortcut-vs-competence-mis-cut.md)
   (s151): a residual over a co-occurrence control grades **local vs transferable distributional**
   generalization, **not** distribution vs non-distribution. "Antonym recovery clears / is reconstructed
   by the contrastive-frame control" bears on the **local-shadow** reading only; reference and grounding
   are untouched.
3. **n = 3 models; orderings, not coefficients.** The verdict is a direction on ≥2/3 models, never a
   pooled coefficient.
4. **The across-relation test is severely underpowered** — the adjective relation inventory is **small**
   (2–4 relations vs the nouns' six; Gate Q1). A Spearman on ≤4 points is even weaker than s186's n = 6.
   The registered decoupling bet is nonetheless across-relation; an **item-level** cue-strength→recovery
   arm (N ≈ 400–800 adjective cues) supplies power **without** redefining the bet (the Q1-C discipline
   carried from s193).
5. **Adjectives only; NOT pooled with the noun probes.** This is a POS-scoped replication; the
   adjective and noun recovery vectors are never pooled. WordNet's IS-A taxonomy (and therefore H2's
   IS-A-depth proxy) does not exist for adjectives — **H2 is not tested here.**
6. **Construct caveat carried from s186:** the calibration gate may fire again (if the contrastive-frame
   C4 control is too weak to recover WordNet relata), in which case the residual/antonymy-shadow arm is
   **descriptive-only** and the weight shifts to the decoupling (clause 1). Re-applied at freeze.

## Panel & settings

Panel = the three [`config/models.md`](../../config/models.md) slots (`panel.A`/`.B`/`.C` — never
hardcode slugs); all three as subjects, cross-model divergence is data. Temperature 0, zero-shot,
single-turn, neutral system prompt. `google/*` gets `reasoning={"effort":"minimal"}` (config caveat).
Every call records `usage.cost` via [`experiments/lib/openrouter.py`](../lib/openrouter.py).

## Design — item scheme (fresh WordNet ADJECTIVE relation cues)

Reuses the **s186/s193 instrument shape** (relatum production; Soundness 𝒮 + gold-size-insensitive
HIT@3 co-primary; SubTLEX-US frequency-matching; highest-G² outlier cap) so H1 is a like-for-like fresh
replication — changing exactly the POS (nouns → adjectives), the relation inventory (Gate Q1), and the
cue set (fresh):

- **POS = adjectives** (WordNet POS `a` head + `s` satellite, via `nltk`;
  [`resource/wordnet-sense-inventory`](../../wiki/base/resources/wordnet-sense-inventory.md), license
  verified in-repo). This is the change that makes the unit a genuine fresh test *and* the reason H2
  cannot transfer.
- **Relation inventory (Gate Q1).** WordNet adjective relations available (measured this session, in a
  frequency-band feasibility proxy — cues with ≥1 in-band single-word relatum): **antonymy 701**
  (`lemma.antonyms()` — J&K's home relation), **synonymy 2238** (synset co-members), **similar-to 4538**
  (`synset.similar_tos()` — satellite clustering, the adjective near-synonymy relation), **also-see 698**
  (`synset.also_sees()`). All four clear powered N (~100–150) even after frequency-matching + s186
  disjointness. Gate Q1 fixes which of these enter the cross-relation decoupling arm and which clause is
  the registered primary.
- **FRESH cues, disjoint from s186.** Exclude the exact committed 780 s186 noun cue lemmas before
  sampling (POS change already makes items disjoint for adjective-only lemmas; the exclusion also covers
  the noun/adjective homographs like *light*, *right*, *fine*), fresh seed, asserted per-relation
  0-overlap, frequency-matched on [`resource/subtlex-us-frequency`](../../wiki/base/resources/subtlex-us-frequency.md)
  Lg10WF to a common profile (the sparsest relation binds), with the same **highest-G² outlier cap**
  (J&K/Cao flag the very-high-frequency iconic pairs *big/little, good/bad, hot/cold* as G² outliers;
  cap frozen at freeze). Powered N per relation (PROTOCOL §4): **~120–150 cues/relation**, reported as
  an achieved per-relation N.
- **The contrastive-frame G² control (reused, byte-frozen construction).** The frames ("X versus Y",
  "neither X nor Y", "from X to Y", conjunction/adjacency), window, and `signed_g2` weighting are
  **byte-frozen from the s193 `build_cooc_c4.py`** (itself byte-frozen from s186 `build_cooc.py`); only
  the cue set (adjectives) and the candidate pool V (single-word SubTLEX **adjectives**, Lg10WF ≥ floor)
  change. The C4 shard set is the s193-frozen 00000–00002 (or re-streamed identically); the corpus is a
  **proxy** for the panel's pretraining distribution (fence carried). **Note (J&K-relevant):** the
  conjunction/adjacency frame is exactly J&K's measured adjective conjunction frame ("*cold and hot*"),
  so the control is on its home ground here in a way it was not for nouns.
- **Per cue:** the model produces up to *k* relata for the named relation (Cao's open-ended format, *k*
  frozen at freeze, matching s186); scored against WordNet adjective-relatum membership. **A within-model
  antonymy frame-ablation arm is MANDATORY** (freeze-condition C1, from the s195 critic — *not* optional
  as first drafted): antonym recovery with the contrastive frame present vs suppressed. It is cheap (no
  corpus), uniquely apt for adjectives (J&K's frames are adjectival), re-tests s186's "antonym recovery
  survives frame suppression" in the home POS, **and — decisively — it is the corpus-free powered hedge
  against the calibration gate refiring** (scope cap 6): if the C4 contrastive-frame control is too weak,
  the antonymy-shadow residual arm goes descriptive-only and H1 is underpowered on ≤4 relations, leaving
  the frame-ablation arm and the item-level arm as the powered evidence. So it is frozen into the battery.

## GATE Q1 — the adjective relation inventory + the registered primary clause

WordNet's adjective relations are fewer and less standard than the noun taxonomy. Two questions bundle
here because they interact: **which relations** enter the across-relation decoupling arm, and **which
clause** is the registered verdict of record.

- **Q1-A — antonymy + synonymy only** (the two "textbook" adjective relations; 2 points). Cleanest, but
  a 2-point across-relation Spearman is degenerate — the decoupling arm collapses to "is antonymy
  recovered better or worse than synonymy, and does that track cue-strength," which cannot carry H1.
  Antonymy-shadow clause primary; decoupling not really testable.
- **Q1-B — antonymy + synonymy + similar-to + also-see** (4 relations). Enough points for a (weak)
  across-relation rank test of the decoupling, matching s186's structure most closely. Risk: `similar_to`
  and `synonymy` are near-duplicative (both are "adjective closeness"), which could deflate the
  rank-spread; `also_see` is the least-standard relation. Decoupling (H1) primary; antonymy-shadow
  co-primary.
- **Q1-C (provisional default) — the 4-relation set (antonymy, synonymy, similar-to, also-see) for the
  across-relation decoupling arm, with the ANTONYMY-SHADOW clause as the registered PRIMARY and the
  decoupling (H1) as a REGISTERED CO-PRIMARY reported with its wide-CI honesty**, plus the item-level
  cue-strength→recovery arm (~400–800 cues) as a POWERED SECONDARY (Q1-C discipline from s193:
  descriptive/robustness-only, can never on its own fire H1). Rationale: the antonymy-shadow clause is
  the *sharpest* adjective-specific test (J&K's home POS, one well-defined relation, not dependent on a
  small relation count), so it carries the primary weight; the 4-relation decoupling arm is reported
  honestly as underpowered (≤4 points) and backed by the powered item-level arm. A **divergence** between
  the across-relation and item-level arms is a first-class reported outcome.

**Why value-laden:** the adjective inventory forces a trade between a faithful-but-degenerate 2-relation
test and a fuller-but-noisier 4-relation one, and forces a choice of which clause is primary. Making the
antonymy-shadow clause primary (Q1-C) is defensible because it is the one adjective test that does not
depend on the thin relation count — but it must pre-commit that a small-inventory decoupling result is
reported at its true (low) power, never dressed up.

## GATE Q2 — a structural proxy arm for adjectives? (H2 does NOT transfer)

H2's frozen proxy (IS-A path depth) is **degenerate for adjectives** — `min_depth()` returns a constant
0 (no adjective hypernym paths; confirmed this session). The question is whether to open a **new**
adjective-structural bet or to run H1-only.

- **Q2-A (provisional default) — NO structural-proxy arm; run H1-only, and state explicitly on the
  result that the adjective route discharges H1 but by construction cannot replicate H2** (no adjective
  IS-A taxonomy). Keeps the unit lean and the pre-registration undiluted; the s193 noun run remains the
  sole H2 evidence.
- **Q2-B — open a NEW pre-registered adjective-structural bet** (e.g. satellite-vs-head position in the
  `similar_to` cluster graph, or cluster centrality) as a *fresh* proxy with its own predicted sign,
  frozen before recovery. This is **not** an H2 replication — it is a new conjecture in a new POS, and it
  would need its own predictions.md row. Adds scope and a multiple-comparison burden for a proxy with far
  weaker a-priori motivation than IS-A depth had (the adjective satellite graph has no "genus a
  definition names first" story).
- **Q2-C — reject up front:** import a noun IS-A depth for adjectives via derivational/pertainym links
  (e.g. score "cold" through its noun "coldness"). **Rejected:** it smuggles a noun taxonomy onto
  adjective cues through a lossy, arbitrary derivational hop — exactly the kind of post-hoc proxy
  construction the pilot note's anti-fishing discipline forbids.

**Why value-laden:** whether the unit stays a clean single-hypothesis (H1) replication or takes on a
new, weakly-motivated structural bet. The default (Q2-A) protects the H1 claim-promotion route from
multiple-comparison dilution and refuses to overstate the unit as an "H2 beyond nouns" test.

## GATE Q3 — anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — following s186 Q3 / s193 Q4 exactly.
  Recovery is scored against WordNet as a **shared definitional target that cancels in the contrast**;
  the predictor (contrastive-frame G²) is a corpus statistic; no human recovery baseline enters. So the
  result makes **no human-comparison claim** and no `resource` anchor is required (CLAUDE.md terminal
  state; the s186 gloss-extension — internal-contrast covers model-vs-computational-baseline — applies).
  Per CLAUDE.md this terminal declaration needs cross-session ratification, which this decision supplies.
  Until ratified the design carries `anchor: pending` naming this decision in `contingent-on:`.

## Metrics + verdict map (direction fixed at freeze; thresholds tightened-not-loosened)

Let ρ_cue = across-relation Spearman(raw recovery 𝒮(model), contrastive-frame G² cue-strength) over
the Q1 adjective relations, per model. Recovery 𝒮 = Soundness (Cao's precision-over-produced) with the
gold-size-insensitive **HIT@3** co-primary from s186. Residual = 𝒮(model, neutral) − 𝒮(control).

- **H1 (verdict-bearing, the registered decoupling) — DECOUPLING-REPLICATES** iff ρ_cue is **near-zero
  or negative** on **≥2/3** models (band frozen at freeze, e.g. ρ_cue < +0.3). **DECOUPLING-BREAKS** iff
  ρ_cue is **clearly positive** (e.g. > +0.5) on ≥2/3 — cue-strength recovered its predictive power in
  a new POS, so s186/s193's decoupling was noun-specific (fires the essay's revision trigger (a); scope
  the reading to nouns or retract). *Reported at its true low power (Q1); backed by the item-level arm.*
- **Antonymy-shadow clause (verdict-bearing, J&K home POS) — ANT-CLEARS-CONTROL** (the s186 falsification
  replicates) iff adjective antonymy's HIT@3 residual is **among the largest** (not the smallest) on
  ≥2/3 models — antonym recovery clears the contrastive-frame control even where the frame-saturation is
  measured-densest. **ANT-SATURATES** (shadow-saturation holds for adjectives) iff adjective antonymy's
  residual is the **smallest / near-zero** on ≥2/3 — the measured-denser adjective framing reconstructs
  antonym recovery, a POS boundary on the s186 falsification. *Subject to the calibration gate (scope cap
  6): if the C4 contrastive-frame control is too weak (mean 𝒮 < floor), this arm is descriptive-only and
  weight shifts to H1.*
- **Pre-named nulls (first-class):** ρ_cue near-zero **and** the antonymy residual middling (recovery
  tracks neither the cue-strength story nor a clean antonymy-shadow story); or the across-relation and
  item-level arms **diverge** (reported, not resolved by fiat).
- **n = 3, orderings not coefficients; adjectives only** (scope caps 3, 5). No pooling across models or
  across POS.
- **Anti-cheat fence (PROTOCOL §B):** the fresh cue sets, the outlier caps, *k*, the relation inventory,
  the ρ_cue band, the antonymy-residual verdict thresholds, and the calibration-gate floor are **all
  frozen in `PREREG.md` before any model call**. No band or threshold is touched after recovery is seen.
  The DECOUPLING-BREAKS, ANT-SATURATES, and null outcomes are pre-named first-class results.

## Cost (pre-flight estimate)

Relatum production is short-output, temperature 0. ~120–150 cues/relation × 2–4 relations (Q1;
≈300–600 verdict-bearing items) × *k* relata × 3 models, one prompt frame (+ optional antonymy
frame-ablation ≈ +150 calls) ≈ **1,200–2,400 calls** at short completions — same order as s186's 2,730
calls at **$0.4661** / s193's 2,061 calls at **$0.3797**. Projects **≈ $0.25–$0.55** — well inside one
UTC day's $5 cap, single-run under the prefer-split $2.50 flag. The C4 shards are already frozen at s193
(no re-fetch needed if reused). A hard `ABORT_USD` (≈ $1.2) goes in `prep.py` at freeze. Re-estimated at
freeze once *k*, the relation inventory (Q1), and per-relation N are fixed.

## What each outcome feeds

- **H1 DECOUPLING-REPLICATES (across a POS boundary):** the decoupling now holds on nouns (s186),
  fresh nouns + C4 (s193), **and** adjectives — two independent replications across corpus and POS.
  This is the evidentiary basis for a **promotion review** of the decoupling to a `claim` (cross-session,
  adversarial; the direct route the backlog names). Still `internal-contrast-only`, within-distribution.
- **ANT-CLEARS-CONTROL (antonymy-shadow falsification replicates in J&K's home POS):** the s186
  falsification is at its most robust — antonymy is not the shadow-saturated relation even where the
  contrastive-frame saturation is measured-strongest; strengthens
  [`essay/antonymy-outlier-distributional-shadow`](../../wiki/findings/essays/antonymy-outlier-distributional-shadow.md)'s
  revised (surviving-direction) reading and the lexical-pole placement in
  [`theory/lexicon-grammar-continuum-v2`](../../wiki/findings/theory/lexicon-grammar-continuum-v2.md).
- **ANT-SATURATES (POS boundary):** a clean, first-class scoping result — shadow-saturation holds
  specifically for adjectives, where J&K's premise is measured; the antonymy-outlier essay's reading is
  re-scoped to the POS where it is real, and the noun falsification is bounded, not overturned.
- **H1 DECOUPLING-BREAKS:** cue-strength predicts recovery on adjectives — trigger (a) fires against;
  scope the decoupling to nouns or retract. A first-class negative that would caution the decoupling
  essay's whole reading and block the claim promotion.
- **Registers a [`predictions.md`](../../wiki/predictions.md) row** at **freeze** (a probe-specific
  H1-adjective / antonymy-shadow row co-registered with the existing §B decoupling bet — not
  double-scored); outcome updated the run session.

## Handoff (what s195 did, and what remains)

1. **s195 (this session):** wrote this design; opened
   [`decisions/open/adjective-antonymy-replication-design`](../../wiki/decisions/open/adjective-antonymy-replication-design.md)
   (Q1–Q3, provisional defaults Q1-C / Q2-A / Q3 internal-contrast-only); measured the WordNet adjective
   relation feasibility (this page's Gate Q1 counts); ran the design pre-run critic (fresh agent) + one
   non-Anthropic decorrelation vote (recorded under
   [`experiments/runs/2026-07-09-adjective-antonymy-replication-design/`](../runs/2026-07-09-adjective-antonymy-replication-design/)).
   **Nothing frozen, nothing run.**
2. **Ratify (s196+):** fresh reviewer + one non-Anthropic vote fix Q1–Q3 (never the opening session).
3. **Freeze (after ratification):** write `prep.py` (fresh disjoint adjective cue build, freq-matched,
   outlier-capped; byte-freeze the s193 G² construction, only the cue POS changing; recompute the
   contrastive-frame G² over the adjective cues on the frozen C4 shards); fix *k* / relation inventory /
   per-relation N / ρ-band / antonymy-residual thresholds / calibration floor; commit PREREG before any
   model call; independent pre-run critic + one non-Anthropic vote; `ABORT_USD` set.
4. **Run (after freeze)** on the panel; post-run verifier recomputes every figure from raw. Powered N
   per PROTOCOL §4.

## Freeze-time conditions (bound s195 by the pre-run review; honor all seven at freeze)

From the s195 fresh-agent critic (verdict authority; GO-WITH-CONDITIONS, no BLOCKERS) + the
non-Anthropic decorrelation vote (ADOPT-C/A/internal-contrast, converging), recorded in
[`REVIEW-design-s195.md`](../runs/2026-07-09-adjective-antonymy-replication-design/REVIEW-design-s195.md).
All are PREREG/`prep.py` specifications, not gate rewrites; they bind the freeze session:

1. **The antonymy frame-ablation arm is MANDATORY** (applied above in the item scheme). It is the only
   corpus-free powered arm and the hedge against the calibration gate refiring — the unit's biggest
   fragility. Frozen into the battery, not optional.
2. **Close the ρ_cue band gap.** Exhaustive, mutually-exclusive H1 bands over the whole line with **no
   uncovered [+0.3, +0.5] dead-zone**; the middle band is pre-registered as an explicit
   INCONCLUSIVE/null outcome. Exact numeric bands fixed before any model call (replace the illustrative
   "e.g." thresholds).
3. **Numeric calibration floor + failure protocol.** Fix a numeric mean-control-𝒮 floor (s186 used 0.05;
   its C4 adjective analog re-fixed at freeze) **and** the exact descriptive-only fallback protocol
   **before** freeze — so "too weak to recover WordNet relata" is a pre-committed threshold, not a
   post-hoc judgement. (Both reviewers flagged this as the load-bearing under-specification.)
4. **≤4-point asymmetry acknowledged in the verdict map.** On ≤4 relations a high-variance ρ_cue
   centered near 0 puts more mass under the wide REPLICATES band (<+0.3) than the BREAKS band (>+0.5);
   PREREG states that the across-relation H1 arm **cannot on its own carry claim promotion** — promotion
   rests on the noun replications (s186 + s193) **plus** this POS-crossing arm read together, with the
   powered item-level arm backing it.
5. **similar-to/synonymy near-duplication contingency.** If their cue-strength AND recovery are near-tied
   (effective points drop to ~3), PREREG pre-registers the collapse and routes interpretive weight to the
   item-level (N ≈ 400–800) arm; tie/near-tie handling for the Spearman is fixed at freeze.
6. **HIT@3 + size-matched scoring carried on the antonymy-shadow PRIMARY specifically.** Adjective
   antonymy gold ≈ 1 relatum (the same small-gold confound s186 neutralized with the gold-size-insensitive
   HIT@3 co-primary); the antonymy-shadow verdict uses a **relation-agnostic, pre-registered** "largest
   vs smallest/near-zero" decision rule (a fixed residual-rank / margin threshold), never a narrative fit.
7. **Item-level arm inference lane fixed.** The item-level cue-strength→recovery arm is locked as a
   **descriptive/robustness** lane (its own multiplicity control if reported inferentially); it can never
   on its own fire H1, break H1, or upgrade an across-relation outcome — mirroring the s193 Q1-C binding.

**Construct-validity scope caveat (not a gate, carried from s186/s193):** the contrastive-frame G²
construction is byte-frozen from a noun-cue instrument; its **counting/weighting logic** is unchanged,
only the cue POS and candidate pool V (adjectives) differ — verified against s193 `build_cooc_c4.py` at
freeze (the same "byte-frozen = the G² computation, not the IO adapter" clarification the s193 freeze
made). Recovery scoring and the G² control share no human key; Q3 stays internal-contrast-only.
