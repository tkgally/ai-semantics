---
type: design
id: lexical-relation-recovery-verb-decoupling-v1
title: "Verb-relation recovery vs a pre-registered troponymy-depth proxy — the DECISIVE third point of the lexical-hierarchy conjecture: does the cue-strength–recovery decoupling (H1) re-appear on VERBS (which HAVE a hierarchy, unlike adjectives) and does a troponymy-depth proxy out-predict contrastive-frame cue-strength (H2, now testable)? Internal-contrast, no human comparison. DESIGN, not frozen; three gates open"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: draft
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-09
updated: 2026-07-09
links:
  - rel: operationalizes
    target: conjecture/decoupling-lexical-hierarchy-pos-generality
  - rel: operationalizes
    target: essay/cue-strength-recovery-decoupling
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/adjective-antonymy-replication-v1
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: claim/lexical-relation-recovery-cue-strength-decoupling
  - rel: depends-on
    target: note/taxonomic-proxy-recovery-pilot-v1
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
---

# Design v1 — verb-relation recovery vs a troponymy-depth proxy (the decisive third point)

**A design + decision-trail unit (program A-lexical; the s197 conjecture's *decisive test* and the
route to strengthening the noun decoupling claim toward a mechanism-bearing form). Status: DESIGN —
one bundled decision (three gates) open, ratifiable s199+.** This page operationalizes
[`conjecture/decoupling-lexical-hierarchy-pos-generality`](../../wiki/findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md)
(registered s197) and, through it, [`essay/cue-strength-recovery-decoupling`](../../wiki/findings/essays/cue-strength-recovery-decoupling.md).
Per PROTOCOL §3/§A1 and the s192/s195 precedent (design one session, ratify the next, run after
ratification): **design s198, ratifiable s199+, run after ratification.** A probe that opens a
value-laden decision is not run in the session that opens it.

> **RATIFIED s199 (2026-07-09), autonomous cross-session adversarial review + one non-Anthropic
> decorrelation vote → RATIFY-WITH-BINDING-CONDITIONS (Q1-C / Q2-A / Q3 internal-contrast-only).**
> [`decisions/resolved/verb-relation-decoupling-design`](../../wiki/decisions/resolved/verb-relation-decoupling-design.md).
> Three new binding conditions on top of the seven below: **B1** a single committed *numeric*
> depth-spread degeneracy bound frozen in PREREG on the frozen sample before any model call; **B2**
> applied symmetrically (below the bound a DEPTH-OUT-PREDICTS is *also* flagged under-powered, never
> banked as noun-equivalent); **B3** the "decisive → third-point" softening propagates to the run
> artifacts (a single verb confirmation is one point in a 3-point pattern, never the established law).
> Fabrication spot-check PASS (verb `min_depth` 0–12/13 distinct; adjective `a`+`s` all `{0}`/28,849;
> 13,767 verb synsets — reproduced firsthand). Frozen + run this same session (s199).

> **Pre-run DESIGN review (s198, 2026-07-09) — GO-WITH-CONDITIONS; no BLOCKER; FABRICATION-CHECK PASS.**
> Independent fresh-agent pre-run critic (verdict authority) **+** one non-Anthropic decorrelation vote
> (`panel.B`, $0.0028815, via the probe REST path, PROTOCOL §A3), both **GO/ADOPT** on **Q1-C / Q2-A /
> Q3 internal-contrast-only**, recorded in
> [`REVIEW-design-s198.md`](../runs/2026-07-09-verb-relation-decoupling-design/REVIEW-design-s198.md).
> The critic re-measured every feasibility figure from scratch (all reproduced **exactly**; adjective
> degeneracy confirmed *stronger* — all 28,849 `a`+`s` synsets share `min_depth` 0) and caught one
> substantive issue the first draft did not surface: **the between-relation depth spread H2 rides on is
> near-degenerate on verbs** (four of the five relations' mean depths within 0.23; antonymy the lone
> shallow outlier, and antonymy's depth is *confounded* with its cue-strength) — so a `DEPTH-FAILS` must
> be pre-registered as **under-powered/uninformative, not a clean falsifier**. H1 (the decoupling
> headline) is unaffected. **Seven freeze-time conditions** bind the freeze (recorded at foot); the H2
> under-power guard + antonymy confound are also folded into the scope caps and verdict map below, and
> the "decisive" framing is softened this session (read: *the registered next / third-point test*, not
> *isolating*). **Nothing frozen, nothing run; the gates are ratified s199+, not now.**

---

## Why this unit is the decisive one — verbs separate "has a hierarchy" from everything else

Three lexical results now bracket the cue-strength–recovery decoupling from opposite structural ends,
and the s197 conjecture ties them into a falsifiable **POS-structural law**:

- **Nouns — decoupling PRESENT, hierarchy PRESENT.** s186
  ([`result/lexical-relation-shadow-saturation-v1`](../../wiki/findings/results/lexical-relation-shadow-saturation-v1.md))
  and s193 ([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../../wiki/findings/results/lexical-relation-recovery-taxonomic-proxy-v1.md))
  both find that raw contrastive-frame cue-strength does not rank-predict which noun relation the panel
  recovers best (across-relation ρ_cue ≈ −0.086 at s186, +0.09 at s193; **twice-replicated**, now the
  nouns-only [`claim/lexical-relation-recovery-cue-strength-decoupling`](../../wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)),
  and s193 diagnoses *why*: **hypernymy** — a low-cue-strength but taxonomically central relation — is the
  best-recovered, scrambling the recovery rank against cue-strength. A pre-registered IS-A path-depth proxy
  out-predicts cue-strength on 2/3 models (the H2 arm).
- **Adjectives — decoupling ABSENT, hierarchy ABSENT.** s196
  ([`result/adjective-antonymy-replication-v1`](../../wiki/findings/results/adjective-antonymy-replication-v1.md))
  ran the same instrument over four WordNet adjective relations and the clean decoupling **did not
  replicate** (ρ_cue +0.4/+0.8/+0.4; item-level ρ ≈ +0.25) — cue-strength partially regains predictive
  traction. The diagnosed reason is structural: **adjectives have no IS-A taxonomy** (`min_depth()` a
  degenerate constant 0 for all 18,156 adjective synsets), so there is no low-cue-strength
  taxonomically-central relation to scramble the ordering, and H2 was *uncomputable*.

**The two bracketing points differ on BOTH axes at once** (nouns: hierarchy + decoupling; adjectives:
no hierarchy + no decoupling), so they cannot on their own separate "has a hierarchy" from every other
noun/adjective difference. **Verbs are the decisive third point:** WordNet verbs *have* a real hierarchy
(troponymy — "to *whisper* is to *talk* in some manner") but are a different POS from nouns. If the
decoupling re-appears on verbs, "hierarchy ⇒ decoupling" gains its first out-of-noun confirmation and
H2 becomes a two-POS pattern; if it vanishes despite the verified verb hierarchy, the conjecture's central
identification (decoupling ⇔ lexical hierarchy) collapses. Either outcome is first-class.

## Verb structural facts — verified this session (design-time feasibility, not frozen)

Measured directly (`nltk` WordNet 3.0 + SubTLEX-US Lg10WF, the s186/s193 cue band [2.0, 4.5], excluding
all 1,740 prior cue lemmas [s186 nouns + s193 fresh nouns + s196 adjectives] as a homograph guard;
[`feasibility.py`](../runs/2026-07-09-verb-relation-decoupling-design/feasibility.py) +
[`feasibility.txt`](../runs/2026-07-09-verb-relation-decoupling-design/feasibility.txt)):

| WordNet verb relation | in-band cues | fresh (excl. 1,740 prior) | median gold | note |
|---|---|---|---|---|
| **hypernymy** (whisper→talk; the more-general verb) | 2,580 | **2,006** | 9 | the troponymy backbone, "up" |
| **synonymy** (synset co-members) | 1,874 | **1,448** | 3 | |
| **troponymy** (talk→whisper; more specific manner) | 1,479 | **1,136** | 6 | the IS-A backbone, "down" |
| **verbgroup** (`verb_groups()`) | 553 | **429** | 2 | near-synonymy — deflates rank-spread |
| **entailment** (snore→sleep) | 320 | **242** | 2 | sparse but clears powered N |
| **antonymy** (rise→fall) | 200 | **140** | 1 | J&K-style; small gold |
| **cause** (`causes()`) | 173 | **126** | 2 | borderline after freq-matching |
| **alsosee** (`also_sees()`) | 1 | **0** | 0 | **unusable** — verbs lack it |

- **The verb hierarchy is genuinely non-degenerate** (unlike adjectives). `min_depth()` over the cue's
  first verb synset ranges **0–11** on the fresh troponymy pool (n=1,136, mean 2.24, **12 distinct
  values**) and identically on hypernymy (n=2,006, mean 2.47, 12 distinct) — a well-populated depth
  distribution, so the **H2 troponymy-depth proxy is computable and carries per-cue signal**, exactly
  where the adjective route could not.
- **Five relations comfortably clear powered N (~120–150) even after frequency-matching + homograph
  exclusion**: hypernymy, synonymy, troponymy, entailment, antonymy. `verbgroup` (429) is well-populated
  but near-duplicative with synonymy (the `similar_to`/synonymy near-dup problem s196 flagged for
  adjectives); `cause` (126) is a semantically distinct sixth relation but **binds at the floor** — after
  matching to a common Lg10WF profile it may drop below 120. `alsosee` is unusable.

Left to freeze (do **not** pre-assert): the exact **frequency-matched** per-relation cue counts after
matching all chosen relations to a common Lg10WF profile (the sparsest chosen relation binds), and
whether `cause` survives matching at usable N. Measured at freeze, exactly as s186/s193/s196 measured
theirs.

## The one question (nothing wider)

On a **fresh** relatum-production probe over WordNet **verb** relations (Gate Q1), run on the
[`config/models.md`](../../config/models.md) panel against a contrastive-frame co-occurrence (G²) control
byte-frozen from the s193 `build_cooc_c4.py` (only the cue POS and candidate pool V changing to verbs),
with a **pre-registered troponymy-depth proxy** frozen before recovery is observed (Gate Q2):

1. **(H-verb-1, the registered decoupling — the conjecture's decisive test):** does across-relation
   recovery rank **decouple** from contrastive-frame cue-strength on verbs (near-zero or negative ρ_cue,
   ≥2/3 models — the noun band, *not* the adjective band) — confirming "hierarchy ⇒ decoupling" out of
   nouns — or does cue-strength recover its predictive power on verbs (clearly positive ρ_cue, ≥2/3),
   **falsifying** the conjecture's central identification despite the verified verb hierarchy?
2. **(H-verb-2, the troponymy-depth mechanism — the H2 analog, now testable):** does a pre-registered
   troponymy-depth proxy (min_depth over the cue's first verb synset; predicted sign **negative** —
   shallower/more-superordinate cue sets recover better, mirroring the noun IS-A-depth result)
   **out-predict** contrastive-frame cue-strength on recovery rank, clearing a pre-registered margin on
   ≥2/3 models — turning the noun H2 (2/3, single-run) into a two-POS pattern?

Both are **internal-contrast**: recovery is model-vs-WordNet-definitional-target; cue-strength and
troponymy-depth are corpus/lexicon statistics; the finding is a within-instrument contrast of *which
form-internal statistic tracks recovery* — **no model-vs-human claim** (Gate Q3).

## Grounding in the sources (verbatim, at their stated strength)

- **The conjecture names verbs as the decisive test and pre-registers the bands:**
  [`conjecture/decoupling-lexical-hierarchy-pos-generality`](../../wiki/findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md)
  — *"Verbs are the decisive third point, because WordNet verbs *have* a hierarchy — unlike adjectives —
  but are a different POS from nouns"*; confirm band *"ρ_cue ≤ +0.30 on ≥2/3 models"*, falsify *"ρ_cue
  is clearly positive on ≥2/3 models (the adjective band, ρ_cue ≥ +0.50)."* The conjecture's own verified
  structural facts (13,767 verb synsets; `min_depth` 0–12; troponyms 24%, hypernym 96%, **entailment ≈3%
  — sparse**) match this session's independent re-measurement.
- **The decoupling + its noun-only scope (the claim this strengthens):**
  [`claim/lexical-relation-recovery-cue-strength-decoupling`](../../wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)
  — `supported`, **nouns-only, H1-only, internal-contrast, no magnitude**; the **cross-POS claim stays
  blocked** (s196 POS boundary). A verb replication of H1 is the named route toward a mechanism-bearing,
  cross-POS-aware form; a verb replication of H2 turns the single-run noun H2 into a two-POS pattern.
- **H2's frozen proxy spec (byte-analogous):** [`note/taxonomic-proxy-recovery-pilot-v1`](../../wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)
  and the s193 `prep.py` `is_a_depth()` — *"min_depth of the cue's FIRST noun synset … Predicted sign
  NEGATIVE."* The verb analog swaps `pos="n"` → `pos="v"`; the min_depth computation and predicted sign
  are unchanged.
- **The corpus (license-cleared, frozen at s193):** [`resource/cooccurrence-corpus-scouting`](../../wiki/base/resources/cooccurrence-corpus-scouting.md)
  — C4 (`allenai/c4` en, *"We are releasing this dataset under the terms of [ODC-BY]"*). The s193 run
  streamed shards 00000–00002 and froze the G² construction in `build_cooc_c4.py`; this design reuses
  that construction, only swapping noun cues for verb cues and V for single-word SubTLEX verbs.

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Internal-contrast only** (Q3). No human comparison. The head-to-head is *which form-internal
   statistic (contrastive-frame cue-strength vs troponymy-depth) tracks recovery* — a within-instrument
   comparison, not a model-vs-human claim.
2. **Within-distribution only.** Per [`essay/shortcut-vs-competence-mis-cut`](../../wiki/findings/essays/shortcut-vs-competence-mis-cut.md):
   troponymy-depth out-predicting cue-strength is *a different form-internal statistic out-ranking
   co-occurrence density*, **never** recovery escaping distribution
   ([`concept/distributional-meaning`](../../wiki/base/concepts/distributional-meaning.md)'s "silent on
   reference and truth" caveat untouched).
3. **n = 3 models; orderings, not coefficients.** The verdict is a direction on ≥2/3 models, never a
   pooled coefficient. The across-relation Spearman is on 5 (or 6) points — weak; the powered item-level
   arm (N ≈ 120/relation × 5 ≈ 600 cues) supplies power **without** redefining the bet.
4. **Verbs only; NOT pooled with the noun or adjective probes.** POS-scoped; the recovery vectors are
   never pooled across POS. This unit's job is the *third bracketing point*, read alongside the noun and
   adjective points — not merged with them.
5. **The verb H2 is STRICTLY WEAKER than the noun H2 — and near-degenerate (s198 critic catch).** The
   noun H2 is already 2/3, single-run, between-relation (item-level ρ ≈ 0), corpus-Hearst-arm-lost. On
   verbs it is weaker still: only 5 rank points (vs 6), and — measured this session — the between-relation
   mean depths cluster **near-degenerately** (hypernymy 2.469, synonymy 2.313, troponymy 2.239,
   entailment 2.236, antonymy 1.564: four relations within 0.23, antonymy the lone shallow outlier). So a
   5-point ρ_depth is effectively decided by antonymy's rank, and **antonymy's depth is confounded with
   its cue-strength** (antonymy is both shallowest-depth → predicts recovers-well, and highest
   contrastive-frame cue-strength → its frames *are* antonym frames), so on verbs ρ_depth-negative and
   ρ_cue-positive are **aligned**, the reverse of the noun case. Consequence, bound at freeze
   (conditions 1–2): a verb **DEPTH-OUT-PREDICTS** is genuinely informative, but a verb **DEPTH-FAILS**
   is reported as **UNDER-POWERED/uninformative, NOT a clean fire-against of the conjecture's
   falsifier 2**, and no verb H2 win/loss is read as mechanistically equivalent to the noun H2. **H1
   stands entirely on its own and is unaffected** — this scopes H2, it does not block the probe.
6. **Hypernymy gold-size confound (carried from s186/s193).** Hypernymy median gold ≈ 9 vs antonymy's ≈ 1;
   Soundness (precision-over-produced) and even HIT@3 can be easier at large gold, so hypernymy's recovery
   advantage — the putative scramble-carrier — is partly a gold-size artifact. Mitigated by the
   gold-size-insensitive HIT@3 co-primary, disclosed, not eliminated.
7. **Construct caveat carried from s186/s193:** the calibration gate may fire (mean control 𝒮 below a
   pre-registered floor), in which case the residual arm goes descriptive-only and weight shifts to the
   decoupling (H1) and the depth (H2) arms, both of which are corpus-control-independent for their rank
   tests. Re-applied at freeze.

## Panel & settings

Panel = the three [`config/models.md`](../../config/models.md) slots (`panel.A`/`.B`/`.C` — never
hardcode slugs); all three as subjects, cross-model divergence is data. Temperature 0, zero-shot,
single-turn, neutral system prompt. `google/*` gets `reasoning={"effort":"minimal"}` (config caveat).
Every call records `usage.cost` via [`experiments/lib/openrouter.py`](../lib/openrouter.py).

## Design — item scheme (fresh WordNet VERB relation cues)

Reuses the **s186/s193 instrument shape** (relatum production; Soundness 𝒮 + gold-size-insensitive
HIT@3 co-primary; SubTLEX-US frequency-matching; highest-G² outlier cap) so H1/H2 are a like-for-like
fresh test — changing exactly the POS (nouns → verbs), the relation inventory (Gate Q1), the depth proxy
POS (Gate Q2), and the cue set (fresh):

- **POS = verbs** (WordNet POS `v`, via `nltk`; [`resource/wordnet-sense-inventory`](../../wiki/base/resources/wordnet-sense-inventory.md),
  license verified in-repo). This is the change that makes the unit the *decisive* test — a POS that has
  a hierarchy but is not nouns — and the reason H2 **can** transfer (unlike adjectives).
- **Relation inventory (Gate Q1).** Default: the **5-relation** set **{hypernymy, troponymy, synonymy,
  entailment, antonymy}** (all clear powered N fresh; the hypernymy/troponymy taxonomic pair is the H2
  backbone). Gate Q1 fixes the set and whether `cause` is added as a sixth (contingent on surviving
  frequency-matching).
- **FRESH cues, disjoint from all prior probes.** Exclude the 1,740 committed prior cue lemmas (s186
  nouns + s193 fresh nouns + s196 adjectives) before sampling — POS change already makes most items
  disjoint, but the exclusion also covers noun/verb and adjective/verb homographs (e.g. *run, walk,
  fall, light*). Fresh seed, asserted per-relation 0-overlap, frequency-matched on
  [`resource/subtlex-us-frequency`](../../wiki/base/resources/subtlex-us-frequency.md) Lg10WF to a common
  profile (the sparsest chosen relation binds), with the same **highest-G² outlier cap** (the iconic
  high-frequency pairs *come/go, rise/fall, live/die* are the verb analogs J&K/Cao flag; cap frozen at
  freeze). Powered N per relation (PROTOCOL §4): **~120–150 cues/relation**, reported as an achieved
  per-relation N.
- **The contrastive-frame G² control (reused, byte-frozen construction).** The frames ("X versus Y",
  "neither X nor Y", "from X to Y", conjunction/adjacency), window, and `signed_g2` weighting are
  **byte-frozen from the s193 `build_cooc_c4.py`**; only the cue set (verbs) and the candidate pool V
  (single-word SubTLEX **verbs**, Lg10WF ≥ floor) change. The C4 shard set is the s193-frozen
  00000–00002 (re-streamed identically if needed); the corpus is a **proxy** for the panel's pretraining
  distribution (fence carried). Verb antonym/opposite pairs occur in the same conjunction frames
  (*"come and go", "rise and fall"*), so the control is on comparable ground to nouns.
- **The troponymy-depth proxy (Gate Q2).** Default: **min_depth over the cue's first verb synset**
  (byte-analogous to the noun `is_a_depth`, `pos="v"`), frozen in `prep.py` before any model call,
  predicted sign **negative**. Gold-independent (a property of the cue, not the answer set).
- **Per cue:** the model produces up to *k* relata for the named relation (Cao's open-ended format, *k*
  frozen at freeze, matching s186); scored against WordNet verb-relatum membership. As with s196, a
  **within-model frame-ablation arm** on the opposition relation (antonymy) is retained as the
  corpus-free powered hedge against the calibration gate refiring (freeze-condition, below).

## GATE Q1 — the verb relation inventory + the registered primary clause

Unlike the adjective probe (where J&K's home-POS antonymy-shadow clause was primary because the relation
inventory was thin and the decoupling arm near-degenerate), **for verbs the decoupling (H1) IS the
headline** — the conjecture's decisive test — and the inventory is adequate (5 relations, richer than
adjectives' 4). Two coupled questions: **which relations** enter the across-relation arm, and (settled by
the conjecture) that **H1 is the registered primary + H2 the registered co-primary**.

- **Q1-A — 4-relation taxonomic core {hypernymy, troponymy, synonymy, antonymy}.** Cleanest, centers the
  taxonomic pair, but drops entailment (a genuine verb-specific hierarchical relation the conjecture
  names) and gives only 4 rank points.
- **Q1-B — 6-relation {hypernymy, troponymy, synonymy, entailment, antonymy, cause}.** Maximal rank
  spread (matches the noun 6-point structure), but `cause` binds at the floor (126 fresh) and may drop
  below powered N after frequency-matching, and `cause` is semantically the least central verb relation.
- **Q1-C (provisional default) — the 5-relation set {hypernymy, troponymy, synonymy, entailment,
  antonymy}** for the across-relation decoupling arm, with **H1 (decoupling) the registered PRIMARY and
  H2 (troponymy-depth) the registered CO-PRIMARY**, plus the item-level cue-strength→recovery arm
  (~600 cues) as a POWERED SECONDARY (the s193/s196 Q1-C discipline: descriptive/robustness-only, can
  never on its own fire H1). `cause` is added as a **sixth relation only if it survives frequency-matching
  at ≥100 cues** (decided mechanically at freeze, pre-registered either way); if it drops out, the arm is
  5-point and this is reported, not patched. Rationale: 5 relations is enough for a real rank test (more
  than adjectives), all five clear powered N fresh, and the taxonomic pair (hypernymy/troponymy) that
  carries H2 is centered.

**Why value-laden:** the inventory forces a trade between a clean-but-thin 4-relation test, a
maximal-but-fragile 6-relation one, and the choice of whether a floor-binding relation (`cause`) enters
conditionally. Making H1 primary (Q1-C) is warranted here — unlike adjectives — because verbs are the
POS the conjecture pre-registered as decisive, and the inventory is adequate; but Q1-C must pre-commit
that a 5-point across-relation ρ_cue is reported at its true (low) power, never dressed up, with the
powered item-level arm backing it.

## GATE Q2 — the troponymy-depth proxy specification (H2 DOES transfer here)

Unlike adjectives (where H2 was uncomputable), verbs have a non-degenerate depth structure (verified:
min_depth 0–11, 12 distinct). The question is **which** depth proxy is frozen as the H2 primary.

- **Q2-A (provisional default) — min_depth over the cue's FIRST verb synset** (byte-analogous to the
  noun `is_a_depth`; `pos="v"`), predicted sign negative, a single frozen proxy. Cleanest, byte-parallel
  to the noun run, minimal multiple-comparison surface. The s193 noun H2 used exactly this on `pos="n"`.
- **Q2-B — a richer depth proxy** (mean min_depth over all the cue's verb senses, or a troponym-branching
  centrality measure). Potentially more faithful to "taxonomic centrality," but opens multiple depth
  bets → multiple-comparison burden, and diverges from the noun H2 spec (breaking the like-for-like
  parallel that makes a verb confirmation a genuine *replication* of the mechanism).
- **Q2-C — reject up front: a corpus troponymy-frame ("Hearst") arm** analogous to the s193 nominal
  Hearst-pattern second arm. **Rejected:** verb troponymy has no clean lexico-syntactic frame analogous
  to nominal "X such as Y" (the s193 nominal Hearst arm *lost* even where it was well-motivated); building
  a verb-troponymy corpus frame would be a weakly-motivated fishing surface. The structural
  (WordNet-derived) troponymy-depth proxy is the single frozen H2 vehicle.

**Why value-laden:** whether the verb H2 stays a byte-parallel *replication* of the noun mechanism
(Q2-A) or becomes a new, multi-proxy bet (Q2-B) that would dilute the two-POS-pattern reading and add a
multiple-comparison burden. The default (Q2-A) protects the "same taxonomic mechanism, second POS"
inference the conjecture is testing.

## GATE Q3 — anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — following s186 Q3 / s193 Q4 / s196 Q3
  exactly. Recovery is scored against WordNet as a **shared definitional target that cancels in the
  contrast**; the predictors (contrastive-frame G², troponymy-depth) are corpus/lexicon statistics; no
  human recovery baseline enters. So the result makes **no human-comparison claim** and no `resource`
  anchor is required (CLAUDE.md terminal state; the s186 model-vs-computational-baseline gloss-extension
  applies). Per CLAUDE.md this terminal declaration needs cross-session ratification, which this decision
  supplies. Until ratified the design carries `anchor: internal-contrast-only` provisionally, naming this
  decision in `contingent-on:`.

## Metrics + verdict map (direction fixed at freeze; thresholds tightened-not-loosened)

Let ρ_cue = across-relation Spearman(raw recovery 𝒮(model), contrastive-frame G² cue-strength) over the
Q1 verb relations, per model. Recovery 𝒮 = Soundness (Cao's precision-over-produced) with the
gold-size-insensitive **HIT@3** co-primary from s186. ρ_depth = across-relation Spearman(recovery,
mean troponymy-depth), predicted negative. Residual = 𝒮(model, neutral) − 𝒮(control).

- **H-verb-1 (verdict-bearing, the registered decoupling) — DECOUPLING-REAPPEARS** iff ρ_cue is
  **near-zero or negative on ≥2/3 models** (the noun band, exact cut frozen at freeze, e.g. ρ_cue ≤
  +0.30). **DECOUPLING-BREAKS** iff ρ_cue is **clearly positive** on ≥2/3 (the adjective band, e.g.
  ρ_cue ≥ +0.50) — a POS that *has* a hierarchy still shows cue-strength predicting recovery, falsifying
  the conjecture's central identification (fires the conjecture's falsifier 1). The **[+0.30, +0.50] gap
  is pre-registered as an explicit INCONCLUSIVE band** (the s196 adjective precedent), broken by the
  powered item-level arm.
- **H-verb-2 (verdict-bearing, the troponymy-depth mechanism) — DEPTH-OUT-PREDICTS** iff a
  troponymy-depth proxy out-predicts cue-strength on recovery rank (|ρ_depth| − |ρ_cue| ≥ a pre-registered
  margin, e.g. 0.20) **in its predicted (negative) direction** on ≥2/3 models — the noun H2 becomes a
  two-POS pattern. **DEPTH-FAILS** iff no depth proxy clears the margin on ≥2/3 (or cue-strength
  out-predicts depth). **BUT (s198 critic condition 1) — DEPTH-FAILS is read as UNDER-POWERED, NOT a
  clean fire-against conjecture-falsifier 2**, whenever the achieved between-relation depth spread is
  near-degenerate (eligible-pool means: hypernymy 2.469 / synonymy 2.313 / troponymy 2.239 / entailment
  2.236 / antonymy 1.564 — four within 0.23, antonymy the lone outlier and confounded with cue-strength,
  scope cap 5). The achieved per-relation mean depths are re-measured on the frozen sample and a degeneracy
  threshold is pre-registered; only a **non-degenerate** depth spread lets DEPTH-FAILS fire as a
  falsifier. A DEPTH-OUT-PREDICTS stays genuinely informative either way.
- **Pre-named nulls (first-class):** ρ_cue in the INCONCLUSIVE band with the item-level arm also
  ambiguous; or DECOUPLING-REAPPEARS but DEPTH-FAILS (decoupling without the named mechanism — reopens
  "what carries the scramble"); or the across-relation and item-level arms **diverge** (reported, not
  resolved by fiat).
- **n = 3, orderings not coefficients; verbs only** (scope caps 3, 4). No pooling across models or POS.
- **Anti-cheat fence (PROTOCOL §B):** the fresh cue sets, the outlier caps, *k*, the relation inventory
  (incl. the mechanical `cause`-inclusion rule), the depth-proxy spec, the ρ_cue bands, the ρ_depth
  margin, and the calibration-gate floor are **all frozen in `PREREG.md` before any model call**. No
  band or threshold is touched after recovery is seen. DECOUPLING-BREAKS, DEPTH-FAILS, and the null
  outcomes are pre-named first-class results.

## Cost (pre-flight estimate)

Relatum production is short-output, temperature 0. ~120–150 cues/relation × 5–6 relations (Q1;
≈600–900 verdict-bearing items) × *k* relata × 3 models, one prompt frame (+ antonymy frame-ablation
≈ +150 calls) ≈ **2,000–3,000 calls** at short completions — same order as s186's 2,730 calls at
**$0.4661** / s193's 2,061 calls at **$0.3797** / s196's run. Projects **≈ $0.35–$0.60** — well inside
one UTC day's $5 cap, single-run under the prefer-split $2.50 flag. The C4 shards are already frozen at
s193 (no re-fetch if reused). A hard `ABORT_USD` (≈ $1.3) goes in `prep.py` at freeze. Re-estimated at
freeze once *k*, the relation inventory (Q1), and per-relation N are fixed.

## What each outcome feeds

- **DECOUPLING-REAPPEARS (H-verb-1 confirmed):** "hierarchy ⇒ decoupling" gains its first out-of-noun
  confirmation — the conjecture moves from a two-point bracket to a three-point pattern. This is the
  evidentiary basis a future review would weigh for **broadening the noun decoupling claim toward a
  cross-POS / mechanism-bearing form** (the s197 REFUSE-dissenter's named strengthening path: a
  replicated positive paired to the repeated absence). Still `internal-contrast-only`, within-distribution.
- **DEPTH-OUT-PREDICTS (H-verb-2 confirmed):** the noun H2 (2/3, single-run) becomes a **two-POS
  pattern** — the same taxonomic-depth mechanism carries the scramble in a second POS. Feeds a possible
  H2 promotion review and the [`theory/shadow-depth-table-v2`](../../wiki/findings/theory/shadow-depth-table-v2.md)
  lexical corner.
- **DECOUPLING-BREAKS (H-verb-1 falsified):** the sharpest possible result — a POS that *has* a hierarchy
  still shows cue-strength predicting recovery; the conjecture's central identification collapses, the
  noun decoupling needs a non-hierarchy explanation, and the essay's whole reading is cautioned. A
  first-class negative.
- **DEPTH-FAILS with H1 reappearing:** reopens "what carries the scramble" with hierarchical depth ruled
  out for verbs — a mechanism-level puzzle, not a null.
- **Registers a [`predictions.md`](../../wiki/predictions.md) probe-specific row** at **freeze**
  (co-registered with the existing s197 conjecture bet — not double-scored); outcome updated the run
  session.

## Handoff (what s198 did, and what remains)

1. **s198 (this session):** wrote this design; opened
   [`decisions/open/verb-relation-decoupling-design`](../../wiki/decisions/open/verb-relation-decoupling-design.md)
   (Q1–Q3, provisional defaults Q1-C / Q2-A / Q3 internal-contrast-only); measured the WordNet verb
   relation feasibility (this page's table + the run dir's `feasibility.py`/`.txt`); ran the design
   pre-run critic (fresh agent) + one non-Anthropic decorrelation vote (recorded under
   [`experiments/runs/2026-07-09-verb-relation-decoupling-design/`](../runs/2026-07-09-verb-relation-decoupling-design/)).
   **Nothing frozen, nothing run.**
2. **Ratify (s199+):** fresh reviewer + one non-Anthropic vote fix Q1–Q3 (never the opening session).
3. **Freeze (after ratification):** write `prep.py` (fresh disjoint verb cue build, freq-matched,
   outlier-capped, with the mechanical `cause`-inclusion rule; byte-freeze the s193 G² construction, only
   the cue POS changing; freeze the troponymy-depth proxy `pos="v"`); fix *k* / relation inventory /
   per-relation N / ρ_cue-bands / ρ_depth-margin / calibration floor; commit PREREG before any model
   call; independent pre-run critic + one non-Anthropic vote; `ABORT_USD` set.
4. **Run (after freeze)** on the panel; post-run verifier recomputes every figure from raw. Powered N
   per PROTOCOL §4.

## Freeze-time conditions (bound s198 by the pre-run review; honor all seven at freeze)

From the s198 fresh-agent critic (verdict authority; GO-WITH-CONDITIONS, no BLOCKER, FABRICATION-CHECK
PASS) + the non-Anthropic decorrelation vote (ADOPT-C/A/internal-contrast), recorded in
[`REVIEW-design-s198.md`](../runs/2026-07-09-verb-relation-decoupling-design/REVIEW-design-s198.md). All
are PREREG/`prep.py` specifications, not gate rewrites; they bind the freeze session:

1. **H2 near-degenerate-depth guard (the critic's primary catch).** Compute + freeze the achieved
   per-relation mean depths in the actual frozen sample; pre-register that if the non-antonymy spread is
   degenerate (heavy ties / range below a stated threshold), H2 is reported **UNDER-POWERED/uninformative,
   not a clean DEPTH-FAILS falsifier** (folded into scope cap 5 + the verdict map above).
2. **Antonymy depth×cue-strength confound.** Pre-register as a stated construct caveat that on verbs the
   depth-carrying relation (antonymy) aligns ρ_depth-negative with ρ_cue-positive (reverse of the noun
   case); no verb H2 win/loss is read as mechanistically equivalent to the noun H2.
3. **Thin-relation fallback for the CORE set (not only `cause`).** Fix the binding profile explicitly
   (antonymy's fresh profile). Any core relation dropping below powered N after frequency-matching is
   reported at achieved N and **never silently dropped or reweighted**; set a hard floor (e.g. <80) and
   pre-commit both branches (drop → reported 4-point arm, or keep-and-flag), decided mechanically.
4. **Exact fresh-in-band cue definition.** A cue is *fresh* iff its surface lemma ∉ the 1,740 prior cue
   lemmas (**POS-agnostic surface match**, the stricter guard the code implements, covering homographs
   like *run/fall/light*); *in-band* iff single-word, `isalpha`, Lg10WF ∈ [2.0, 4.5]; gold aggregated
   across **all** verb senses; relatum single-word Lg10WF ≥ 1.5. Disclose the carried caveat: gold is
   all-sense while the depth proxy is **first-synset** (byte-identical to the noun run).
5. **Lock the `cause`-inclusion rule before any inspection.** ≥100 cues *after frequency-matching to the
   binding profile* (define the matched-N computation), decided mechanically at freeze, both branches
   pre-registered; `cause` never enters or exits after recovery is seen.
6. **Byte-freeze integrity.** Byte-identity applies to the G²/co-occurrence computation (frames, window,
   K, `signed_g2`) verified unchanged vs the s193 `build_cooc_c4.py`; only the cue POS (→verbs) and
   candidate pool V (→single-word SubTLEX verbs) change; C4 shards = the s193-frozen 00000–00002. Assert
   in PREREG.
7. **Close the band arithmetic + inherit the calibration gate.** Exhaustive mutually-exclusive ρ_cue
   bands (reappears ≤ +0.30 / inconclusive (+0.30, +0.50) / breaks ≥ +0.50) + a numeric H2 margin
   (|ρ_depth| − |ρ_cue| ≥ 0.20, negative direction), fixed before any model call. Carry the s186/s193
   calibration-gate floor (residual arm descriptive-only if mean control 𝒮 < floor; weight shifts to the
   corpus-control-independent H1/H2 rank tests). Set `ABORT_USD`; register the `predictions.md` row at
   freeze (co-registered with the s197 bet, not double-scored); assert per-relation 0-overlap with the
   1,740 prior lemmas.

**Framing note (s198 critic, applied):** "decisive" throughout this page means **the registered
next / third-point test**, not a crucial experiment that *isolates* hierarchy — verbs confound POS with
hierarchy exactly as nouns do (they carry their own aspect/argument-structure differences), so a verb
DECOUPLING-REAPPEARS is confirmatory third-point evidence and DECOUPLING-BREAKS is the clean falsifier;
neither identifies hierarchy as the sole cause. Scope caps 4–5 carry this.
