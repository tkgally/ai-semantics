---
type: conjecture
id: decoupling-lexical-hierarchy-pos-generality
title: "The cue-strength–recovery decoupling is a lexical-hierarchy effect: it reappears in any POS that has an IS-A-like taxonomic backbone and vanishes in any POS that lacks one (verbs are the decisive test)"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: proposed
contingent-on: []
created: 2026-07-09
updated: 2026-07-09
links:
  - rel: refines
    target: essay/cue-strength-recovery-decoupling
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/adjective-antonymy-replication-v1
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Conjecture: the cue-strength–recovery decoupling is a lexical-hierarchy effect

## Where this comes from

The [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md) established, on
nouns, that the relation the corpus cues most is **not** the relation the frontier panel recovers best:
across the six WordNet noun relations, raw contrastive-frame co-occurrence cue-strength and recovery come
apart (across-relation Spearman ρ_cue ≈ **−0.086** at s186, replicated at ρ_cue ≈ **+0.09** on a fresh
corpus family at s193). Two probes then bracketed the phenomenon from opposite structural ends:

- **Nouns (decoupling present; hierarchy present).**
  [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)
  (s186) and [`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)
  (s193) both find the decoupling, and s193 diagnoses *why*: the decoupling is carried by **hypernymy** — a
  *low*-cue-strength but taxonomically central relation being the *best*-recovered, which scrambles the
  recovery rank against cue-strength. A pre-registered IS-A path-depth proxy out-predicts cue-strength on
  2/3 models (ρ_depth −0.20 / −0.37 / −0.37) — the taxonomic backbone, not co-occurrence density, tracks the
  recovery ordering.
- **Adjectives (decoupling absent; hierarchy absent).**
  [`result/adjective-antonymy-replication-v1`](../results/adjective-antonymy-replication-v1.md) (s196) ran
  the same instrument over four WordNet adjective relations and the clean decoupling **did not replicate**
  (ρ_cue +0.4 / +0.8 / +0.4; powered item-level ρ ≈ +0.25, all three) — cue-strength partially *regains* its
  predictive traction. The diagnosed reason is structural: **adjectives have no IS-A taxonomy** (WordNet
  adjective `min_depth()` is a degenerate constant 0 for every synset — verified: all 18,156 adjective
  synsets share `min_depth` = 0, and `happy.a.01` has no hypernyms), so there is no low-cue-strength
  taxonomically-central relation to scramble the ordering, and the most-cued adjective relation (antonymy) is
  *also* the best-recovered.

So the s196 result named the mechanism explicitly: the decoupling **is** the signature of a lexical
hierarchy scrambling the recovery rank against cue-strength. This conjecture promotes that mechanism from a
two-POS diagnosis to a general, falsifiable **POS-structural law**.

## Statement

> The across-relation cue-strength–recovery decoupling is not a fact about frontier lexical recovery in
> general; it is the signature of a **lexical hierarchy** (an IS-A-like taxonomic backbone) in the relation
> inventory of a part of speech. **The decoupling reappears — recovery rank goes near-zero or negatively
> correlated with contrastive-frame cue-strength — in any POS whose relation inventory contains a
> hierarchical, low-cue-strength-but-taxonomically-central relation, and it vanishes — cue-strength regains
> rank-predictive power over recovery — in any POS whose relation inventory lacks one.** Equivalently, the
> presence of the decoupling co-varies with the presence of a non-degenerate taxonomic depth structure over
> the POS's relations, POS by POS.

The **mechanism** is taxonomic-centrality-carries-the-scramble: a relation that is cheaply cued (high
contrastive-frame cue-strength) need not be best-recovered, and a relation that is expensively cued (low
cue-strength) but taxonomically central (shallow/superordinate in the IS-A tree, densely connected) can be
best-recovered; wherever such a relation exists, the recovery ordering is pulled out of alignment with the
cue-strength ordering, and cue-strength stops predicting recovery. Where no such relation exists — where the
relations are all "closeness/opposition" relations at a single flat level, as for adjectives — the most-cued
relation is also the best-recovered and cue-strength re-predicts recovery.

## The decisive test bed: verbs (troponymy + entailment)

Adjectives and nouns are the two *bracketing* points, and they differ on **both** axes at once (nouns:
hierarchy + decoupling; adjectives: no hierarchy + no decoupling), so they cannot on their own separate "has
a hierarchy" from every other noun/adjective difference. **Verbs are the decisive third point**, because
WordNet verbs *have* a hierarchy — unlike adjectives — but are a different POS from nouns:

- **Troponymy** is the verb IS-A-like manner hierarchy ("to *whisper* is to *talk* in some manner"):
  `whisper.v.01` has hypernym `talk.v.02`, itself under further hypernyms — a genuine tree.
- **Entailment** is a second verb-specific hierarchical relation (`snore.v.01` entails `sleep.v.01`;
  `buy.v.01` entails `choose.v.01` and `pay.v.01`; `breathe.v.01` entails `exhale.v.01` / `inhale.v.02`).

The bet therefore predicts, on a fresh verb-relation recovery probe: (H-verb-1) the across-relation
decoupling **re-appears** (ρ_cue near-zero or negative, ≥2/3 models), because troponymy supplies the
low-cue-strength-but-central relation nouns' hypernymy did; and (H-verb-2) a **troponymy-depth taxonomic
proxy out-predicts contrastive-frame cue-strength** for recovery rank — the H2 analog, now *testable* on
verbs where it was untestable on adjectives (adjective `min_depth` being degenerate). This is the natural
next empirical unit after s196.

### WordNet-verb structural facts (verified this session vs. left to design time)

Verified directly (`nltk` WordNet, this session):

- **Adjectives are genuinely flat.** All 18,156 adjective synsets have `min_depth()` = 0 (the only distinct
  value); `happy.a.01`.hypernyms() = [] — confirming the s196 "degenerate constant 0" claim and the "no IS-A
  taxonomy" premise.
- **Verbs have a real hierarchy.** 13,767 verb synsets; `min_depth()` ranges **0–12** (mean ≈ 2.53, 13
  distinct values) — a non-degenerate depth distribution, unlike adjectives. `whisper.v.01`.min_depth() = 4,
  `talk.v.02`.min_depth() = 3.
- **Troponymy/hypernymy is dense; entailment is sparse.** 13,208 / 13,767 verb synsets (≈96%) have a
  hypernym; 3,315 / 13,767 (≈24%) have troponyms (`hyponyms()`); **390 / 13,767 (≈3%) have an entailment**.
  So a troponymy-depth proxy is well-populated (the H-verb-2 vehicle), while entailment is a genuine but
  *sparse* relation — usable as one probe relation, not as the depth backbone.

Left to design time (do **not** pre-assert): the exact **per-relation, cue-level (lemma-level)** feasibility
counts after frequency-matching on [`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md)
and excluding prior cue sets — i.e. how many frequency-matched verb cues each of troponymy, hypernymy,
entailment (and any also-see/verb-group analog) can supply at the ~120-cue powered band, and whether
entailment's ≈3% synset coverage survives frequency-matching at usable N. These are to be measured at design
freeze, exactly as the noun and adjective runs measured theirs.

## What would confirm

Read orderings, not coefficients (n = 3 models). On a fresh, pre-registered verb-relation relatum-recovery
probe (fresh cues disjoint from the s186/s193/s196 sets; the same byte-frozen contrastive-frame G² control;
a troponymy-depth proxy pre-registered before recovery is observed):

1. **Decoupling reappears (H-verb-1).** The across-relation Spearman ρ_cue (recovery vs contrastive-frame
   cue-strength) is **near-zero or negative — ρ_cue ≤ +0.30 on ≥2/3 models** (the s186/s193 noun band),
   *not* the adjective band (+0.4 to +0.8). Ideally the powered item-level arm agrees (a cue's own
   cue-strength does *not* positively predict its own recovery, ρ ≈ 0, unlike adjectives' ρ ≈ +0.25).
2. **Troponymy depth out-predicts cue-strength (H-verb-2, the H2 analog).** A pre-registered troponymy-depth
   proxy (e.g. mean `min_depth` over the cue's first verb synset, predicted sign negative — shallower/more
   superordinate cue sets recover better, mirroring the noun IS-A-depth result) out-predicts contrastive-frame
   cue-strength on recovery rank, clearing a pre-registered margin (e.g. |ρ_depth| − |ρ_cue| ≥ 0.20) on
   **≥2/3 models**, in its predicted direction.

Confirmation of (1) alone re-scopes the decoupling from "noun phenomenon" to "any-hierarchical-POS
phenomenon" — the load-bearing generalization. (2) additionally confirms that the *same* taxonomic mechanism
(hierarchical depth, not cue density) carries it in a second POS, turning the noun H2 (currently 2/3,
single-run) into a two-POS pattern.

## What would falsify

1. **Decoupling fails to reappear on verbs.** If ρ_cue is clearly positive on ≥2/3 models (the adjective
   band, ρ_cue ≥ +0.50, or an item-level ρ clearly > 0), then a POS that *has* a hierarchy still shows
   cue-strength predicting recovery — the "hierarchy ⇒ decoupling" half of the law is wrong, and the noun
   decoupling would need some non-hierarchy explanation (POS-idiosyncratic, or specific to hypernymy rather
   than to hierarchy-in-general).
2. **Troponymy depth does not out-predict cue-strength.** If no troponymy-depth proxy clears the margin over
   cue-strength on ≥2/3 models (or cue-strength out-predicts every depth proxy), the H2 analog is
   fired-against on verbs: the decoupling (if it reappeared) is carried by something other than the
   taxonomic-depth mechanism the noun run named — reopening "what carries the scramble" with hierarchical
   depth ruled out for verbs.
3. **The pattern inverts the bracket.** If the decoupling *vanishes* on verbs (cue-strength predicts) despite
   the verified verb hierarchy, that is the sharpest falsifier of all: it would show the noun/adjective
   contrast is not about hierarchy-presence but about some other noun-vs-non-noun difference, and the
   conjecture's central identification (decoupling ⇔ lexical hierarchy) collapses.

A non-falsifying null worth pre-naming: ρ_cue could land **ambiguously** in the +0.3 to +0.5 gap on verbs
(as it did on adjectives at the across-relation grain), in which case the powered item-level arm breaks the
tie — the s196 precedent for reading a boundary from converging under-powered + powered arms.

## Scope and honesty caps (read before citing)

- **Two bracketing points, not a demonstrated law.** The current evidence is exactly **two points** — nouns
  (decoupling + hierarchy) and adjectives (no decoupling + no hierarchy) — plus a *mechanistic* reading that
  ties them together. A 2-point pattern with a named mechanism is **suggestive, not established**: the verb
  test is precisely what would turn the bracket into a supported generalization (or break it). Do not cite
  this conjecture as if the law held; cite it as the registered bet.
- **The noun H2 is itself only 2/3, single-run, between-relation.** The taxonomic-depth-out-predicts-cue-strength
  result it leans on ([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md))
  fired at 2/3 (not 3/3 — hypernymy being both deep and best-recovered caps one model's depth correlation),
  is between-relation not within-cue (item-level ρ ≈ 0), and its corpus Hearst-frame arm *lost*. The verb H2
  analog inherits all those caveats and must not be pre-sold as robust.
- **Within-distributional only; no human comparison.** Like the parent essay, this bet pits one form-internal
  statistic (taxonomic-depth structure — itself a WordNet-derived structural measure with a dense corpus
  footprint) against another form-internal statistic (contrastive-frame cue-strength). It makes **no** human
  comparison and **no** claim that recovery is non-distributional: if troponymy depth wins on verbs, that is
  *a different form-internal statistic out-ranking co-occurrence density*, never recovery escaping
  distribution ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)'s caveat —
  distribution is "by itself, silent on reference and on truth" — is untouched). The lexical relations at
  stake are inferential-role structure in the [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)
  sense (knowing *to whisper is to talk in a manner* licenses inferences), scored by same-task relatum
  production. The eventual verb probe would be **`internal-contrast-only`** in spirit — recovery scored
  against WordNet, a shared target that cancels in the head-to-head; the predictors are corpus/lexicon
  statistics — so it would need no human-resource anchor (it makes no human-comparison claim). A conjecture
  page carries no `anchors` link; this note records that the terminal declaration the eventual result should
  seek is `internal-contrast-only`, not a pending human anchor.
- **Not run, not queued as an immediate move.** This records a bet and names verbs as the natural next unit;
  it opens no `decisions/open/` entry (it makes no value-laden methodological choice — the design gates,
  including the cue-level feasibility counts and the depth-proxy specification, are chosen at design freeze).
