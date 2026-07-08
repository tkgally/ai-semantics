---
type: theory
id: lexicon-grammar-continuum-v2
title: One continuum, one test — lexical sense and constructional meaning as a single form–meaning cline, probed by the same "beat the distributional shadow" skeleton (second edition, restated around the promoted claims layer, the powered magnitudes, and the corner that moved)
meaning-senses:
  - constructional
  - referential
  - distributional
  - inferential
  - grounded
  - human-comparison
status: draft
contingent-on: []
created: 2026-07-08
updated: 2026-07-08
links:
  - rel: supersedes
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: claim/comparative-correlative-covariation
  - rel: depends-on
    target: claim/lexical-sense-gradience
  - rel: depends-on
    target: claim/lexical-graded-scale-ungraded-commitment
  - rel: depends-on
    target: claim/dative-information-structure-givenness
  - rel: depends-on
    target: claim/aann-behavioral-gradient
  - rel: depends-on
    target: claim/output-channel-working-surface
  - rel: depends-on
    target: theory/shadow-depth-table-v1
  - rel: depends-on
    target: theory/constructional-meaning-in-llms-v2
  - rel: depends-on
    target: theory/situating-llm-meaning-v2
  - rel: depends-on
    target: theory/relational-meaning-in-llms
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: result/lexical-sense-gradience-rep2
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: result/presupposition-doppelganger-control-v1
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v3
  - rel: depends-on
    target: result/coercion-sense-modulation-v2
  - rel: depends-on
    target: result/aann-inferential-v4
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v1
  - rel: depends-on
    target: note/cross-axis-lexical-constructional-ordering-v1
  - rel: depends-on
    target: essay/shadow-depth-cross-cuts-grain
  - rel: depends-on
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: essay/shortcut-vs-competence-mis-cut
  - rel: depends-on
    target: essay/under-licensed-middle
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: supports
    target: open-question/lexical-polysemy-gradience
  - rel: depends-on
    target: source/cao-2025-semantic-relation-knowledge
  - rel: depends-on
    target: source/diera-2026-encode-semantic-relations
  - rel: depends-on
    target: source/justeson-katz-1991-antonym-cooccurrence
---

# Theory (second edition): the lexicon–grammar continuum, and the single test that spans it

> **This is the clean second edition**, forced by the theory-edition rule
> ([`PROTOCOL.md`](../../../PROTOCOL.md) §3: more than ~3 update boxes force a rewrite). The first edition
> ([`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md), kept visible as history — cite it
> for the June/early-July record) had accreted more than three dated update boxes (chiefly the s147
> relation-type axis, s165 shadow-depth axis, s183 single-run discharge, and s188 antonymy falsification,
> over an earlier per-model-ordering box) and two of its body sections
> asserted a placement that a later box **reversed**. This edition restates the position cleanly around
> what now exists that did not exist when the first edition was drafted: a **promoted claims layer** (six
> typed `claim` pages, two poles carrying powered magnitudes with intervals), the flagship **shadow-depth
> table** ([`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md)), and — the one substantive
> change of *content*, not just of consolidation — **the lexical pole's shadow-saturated corner did not
> sit where the first edition placed it**: the panel bet that antonymy is the shadow-saturated relation
> **ran and was falsified** ([`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)).
> The continuum thesis and its two-axis structure are unchanged; the specific corner is corrected in the
> body, not carried as a contradicting box. Nothing measured on the first edition changed; the readings
> laid over the measurements did.

## Why this page exists

The project runs on two tracks that once looked separate: a **grammatical** wedge (constructional meaning
— does a model track a construction's contributed inference?) and a **lexical** wedge (sense gradience —
does a model track graded word-sense relatedness?). This page argues they are **not two tracks but one**,
and that the project has — without having named it at the outset — been applying a **single evidential
test** on both: *does a meaning gradient beat the distributional shadow?* It is a synthesis page (a
framework and a bridge), claiming a structure, not new data; the data are on the result and claim pages
it leans on.

## The continuum thesis (established in CxG, not novel here)

Construction Grammar's foundational move is that the lexicon and the grammar are **not different kinds of
thing**. [`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md) states it
directly: constructions "range from morphemes and closed-class items through idioms and argument-structure
templates to large-scale discourse patterns" — a single inventory (a *constructicon*) along a cline of
**specificity** and **schematicity**. A word is, on this view, a maximally specific construction (a
form–meaning pairing with fully fixed form); an argument-structure template is a maximally schematic one.
There is no principled seam between "lexical meaning" and "grammatical meaning"; there is one form–meaning
space at different grains. (CxG canon — Goldberg 1995/2006, Langacker, Croft 2001 — is referenced in
`constructional-meaning` as not-in-repo; the continuum claim rests on that concept page's in-repo statement
of it, not on fabricated quotation.)

If that is right, the project's two wedges are the **two ends of one cline**:

| | grain | the "meaning" tracked | the project's anchor | the distributional **shadow** (null) |
|---|---|---|---|---|
| **Lexical wedge** | maximally specific (a word) | graded **sense relatedness** of a word across uses ([`concept/polysemy`](../../base/concepts/polysemy.md)) | DWUG graded DURel judgments | **context/topic similarity** of the two sentences |
| **Grammatical wedge** | maximally schematic (a construction) | a construction's **contributed inference** ([`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md)) | Scivetti CxNLI / own minimal pairs | **n-gram frequency / surface form** |

## The single test: "does a meaning gradient beat the distributional shadow?"

Read across that table, the two wedges run the **same experiment**. In both, a fluent model has a
*distributional structure for free* — co-occurrence neighbourhoods for words, surface-form regularities for
constructions — and the live question is whether the model tracks a **meaning gradient not reducible to that
distributional structure**. This is the null-hypothesis discipline
[`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) imposes, and it is the
spine of both the constructional evidence ladder
([`theory/constructional-meaning-in-llms-v2`](constructional-meaning-in-llms-v2.md)) and the lexical
conjecture's load-bearing clause: the meaning signal must survive a matched distributional control.

## Two ordering axes: grain, and shadow-depth (orthogonal to grain)

The continuum has **two** orthogonal ordering axes, and keeping them apart is what the first edition's
update boxes were groping toward. This edition states both up front.

1. **Grain** — the CxG axis: specific word ↔ schematic construction. This is the lexicon–grammar cline
   itself.
2. **Shadow-depth** — how much of a phenomenon is already written into surface co-occurrence, argued in
   [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md). Run the single test
   across the whole cline and phenomena sort **not by grain but by shadow-depth**: a demonstrated
   **shadow-beater** (a residual survives a matched control) at one end, a **shadow-saturated corner** (the
   phenomenon is reconstructable from co-occurrence, so "looking good" is uninformative) at the other. This
   axis **cross-cuts** grain: each pole holds *both* a beater and a saturated corner.

The consequence for the headline is a calibration the rest of this page keeps: "beats the distributional
null at both grains" is true of the **beaters** at both grains, but **neither pole is uniformly** a
shadow-beater. Shadow-depth is a property of the **phenomenon**, silent on which model tracks which — it
does not touch the cross-axis competence dissociation recorded below.

## The state of the evidence, unified — the beaters, now on the claims layer

The project can state its central finding as a **cline-spanning** one rather than a grammar-only one:
*current decoders track a graded form–meaning signal that beats the distributional null at both the word
grain and the construction grain*. Both poles are now cross-date replicated on fresh items and promoted to
the compounding **claims layer**:

- **Grammatical beaters.** The comparative correlative deploys its covariation inference above matched
  controls that **reuse the same scalar words**, survives conflicting world knowledge and operator
  embedding, and composes — a construction-isolation gap of **≈87 pp** (95% CI lower bound ≈78 pp),
  replicated on **136 fresh disjoint items, 3/3 models**, verifier-reproduced
  ([`result/comparative-correlative-covariation-powered`](../results/comparative-correlative-covariation-powered.md)),
  promoted to [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md).
  Two further grammatical-pole beaters carry their own claim pages: dative alternation tracks
  information-structure (givenness) direction, powered 3/3 at N=100 with an ≈9× cross-model magnitude spread
  ([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md),
  scoped 2/3 for gpt at founding N but 3/3 at power), and the AANN construction shows a graded acceptability
  gradient that tracks the Mahowald human ordering, cross-date replicated 3/3
  ([`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md), scoped Tier-2 gradient
  tracking — distinct from the Tier-0 form ceiling and the thin Tier-4 inferential line).
- **Lexical beater.** The panel's graded sense-relatedness rating tracks the human DURel median (Spearman
  ≈0.60–0.83, in/above the human inter-annotator range) and **survives partialling out the model's own
  topic-similarity**, replicated on **200 fresh pair-disjoint DWUG pairs, 3/3**
  ([`result/lexical-sense-gradience-rep2`](../results/lexical-sense-gradience-rep2.md)), promoted to
  [`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md). Its single-run flag is
  **discharged for the direction/agreement core** (not for usage-independence, and not as a twice-powered
  independent magnitude). One scope note the word "gradience" forces, kept from the first edition: v1
  established a graded *scale* (a **cross-item** property — the model rank-orders many usage pairs the way
  humans do) and only that. Whether the model also shows graded *commitment* (a **within-item** property —
  intermediate behavior on a single bridging use) is logically independent, and the bridging probe found
  **graded scale, ungraded commitment: a clean null 3/3** ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md),
  promoted with the ungraded-commitment half to
  [`claim/lexical-graded-scale-ungraded-commitment`](../claims/lexical-graded-scale-ungraded-commitment.md)).
  Models place a bridging pair at an intermediate *position* (inside a frozen [40,60] band) yet meet it at
  clear-item confidence and almost never take the "UNCLEAR" decline. The honest asymmetry: the position/scale
  half is the **bound-but-weak** half (it partly tracks the model's own topic-similarity, the same shadow v1
  carried), while the ungraded-commitment half is the **robust** half, corroborated by three independent
  commitment instruments.

The same caveats bind both poles: behavioral not representational; modest N; single-run flags now
discharged at both poles by cross-date replication; and the hard *negatives* stay honest — divergent-form
generalization on grammar, and on the lexical side the **polysemy/homonymy discreteness split**, tested on a
homonymy-enriched WiC anchor and returning a **powered null**
([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md): no separate discrete
regime over plain graded distance). So the *graded* signal stands at both poles; the *discrete-regime* bet
does not.

## The corner that moved: the lexical pole's shadow-saturated end is not antonymy

The first edition placed the lexical pole's **shadow-saturated corner** at **antonymy**, on a convergence of
two open-access prior-art sources: behaviorally, [`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md)
reports "**Antonymy is the outlier relation where all models perform reasonably well**" (Abstract; antonymy
soundness 𝒮=0.57 vs ~0.30 for other relations, §8), and representationally,
[`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md)
finds "**Difficulty is consistent across models (antonymy easiest, synonymy hardest)**" (Abstract). Read
through this page's own test, that convergence looked **deflationary**: antonym pairs recur in tight
near-symmetric *contrastive frames* — a characterization with a primary corpus anchor (Justeson & Katz 1991
on the Brown Corpus: antonyms co-occur far above chance, "**63% (139/219) … in lexically identical
structures**", "**Fully 164 (75%) … in conjoined syntactic structures**",
[`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md),
§3, pp. 11–12) — so antonymy is **maximally Harris-recoverable** and the residual a competence claim must
show is smallest there. The prediction: on the panel, antonymy would be the relation whose recovery is
**least separable** from a contrastive-frame control.

**That panel bet ran (session 186) and was falsified**
([`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)). On
a same-task relatum-production probe over six WordNet noun relations, against a contrastive-frame
co-occurrence (G²) control, **antonymy is not the shadow-saturated relation**: it carries one of the
*largest* control-adjusted residuals (HIT@3 **+0.61–0.67**), with **meronymy** the *smallest* — the reverse
of the "antonymy smallest / meronymy & hyponymy larger" ordering the first edition predicted. Raw recovery
does **not** track corpus cue-strength (across-relation Spearman **≈ −0.09**; **hypernymy**, not antonymy, is
best-recovered), and antonym recovery **survives frame suppression**. Both of the conjecture's confirmation
clauses fail. `anchor: internal-contrast-only` (ratified s185): the force is a within-instrument
model-vs-baseline contrast, no human comparison.

Two things this correction does **not** license, per
[`essay/shortcut-vs-competence-mis-cut`](../essays/shortcut-vs-competence-mis-cut.md). It falsifies the
**local-shadow-saturation reading** (antonymy is *not* the relation where the shadow is deepest on the
panel), **not** "antonymy competence beyond distribution" — an internal-contrast control cannot license the
positive competence claim any more than it licensed the deflationary one. And the prior-art (Cao, Diera,
non-panel models) still stands as literature; what lost is the *panel bet* that the prior-art ordering would
reproduce on the project's own instrument. So the lexical pole still has a shadow-depth gradient across
relations — but the project does **not** currently know which relation sits at its saturated end, and the
one it confidently named turned out to be near the beater end. The corner moved.

## The grammatical pole's shadow-saturated corner: presupposition, and the under-licensed middle

At the grammatical pole the shadow-saturated corner is **presupposition** — environment-gated in both
signatures, cue-strength-graded ([`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md)).
Here the project ran the matched control the antonymy corner lacked, and the result is instructive about the
*instrument*, not just the phenomenon. The doppelgänger control
([`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md))
returned **BEATS-DOPPELGANGER** (pooled residual +0.78/+0.47/+0.94) — so the clean flat null the design
named as the "cleanly shadow-saturated" prize did **not** obtain — **but BEATS is the under-licensed
outcome**: the powered controls vary the **trigger word-form** (`realize`→`suspect`), whose distributions
differ, so a verb-sensitive surface-cue follower reconstructs the residual. The decisive disanalogy with the
comparative-correlative beater: the CC clears controls that reuse the **same words** and vary only the
construction; these controls vary the word. So the honest reading is a **third state** the project now names
explicitly ([`essay/under-licensed-middle`](../essays/under-licensed-middle.md)): a word-varying matched
control can only ever reach {saturated, under-licensed}, never a clean beater — "beater" and "under-licensed
middle" are outputs of two different instruments. Presupposition's corner did **not** move to the beater
side, and the essay's first revision trigger (a residual a surface-cue account *cannot* reconstruct, stable
across frames and contexts) did **not** fire.

So the two poles' shadow-saturated corners now stand asymmetrically evidenced: presupposition (grammatical)
carries a run matched control that lands in the under-licensed middle; the lexical pole's corner is
**unplaced** after the antonymy bet lost. This is a sharpening of the first edition's tidy "antonymy marks
the lexical end just as presupposition marks the grammatical end" — the structural move (each pole has a
saturated corner) survives; the specific lexical placement does not.

## The empirical bridge: coercion is where the two grains touch

The cleanest place the cline becomes a single phenomenon is **coercion**
([`concept/coercion`](../../base/concepts/coercion.md)) — a construction overriding a word. When the
caused-motion construction makes *sneeze* in *she sneezed the napkin off the table* contribute
causation-of-motion it does not lexically have, that **is** a shift in the word's sense *induced by the
grammar*: constructional coercion (grammar end) and contextual sense modulation (lexicon end) are the **same
event** from two ends of the cline. The bridge is directly testable with the instrument the lexical probe
built: ask, with the DWUG-style relatedness rating, how related a verb's sense is between its neutral and
its coerced frame, against non-coercing controls.

That probe ran, and its de-confounding v2 with it. v1 found the predicted direction (all models rate a
coerced use as less sense-related to its bare use than a length-matched non-coercing elaboration), and the
structure-matched v2 ([`result/coercion-sense-modulation-v2`](../results/coercion-sense-modulation-v2.md))
**partially de-confounds** it: a small, **fine-scale-only, fragile** sense-specific residual survives a
conventional-transitive control (isolation gap cont +13.6/+6.1/+1.9, ≈0 on the coarse 4-point scale, carried
by only 3–4 of 8 verbs) **alongside a real surface component**. So the two wedges genuinely touch — more
weakly than v1's raw gap implied (v1's drop was a *mix* of sense and surface, mostly sense for claude, mostly
surface for gemini). A second, unforced finding: the model strongest at pure lexical gradience (gemini) is
the *least* coercion-sensitive — the first hint of the cross-axis dissociation below.

## The prospective third axis: multimodal / perceptual grounding

A **third** scope axis runs orthogonal to grain: it varies the **modality of the form** — does adding
perceptual input change a model's meaning behavior beyond what the text distribution already supplies? Same
beat-the-shadow skeleton, a *different* null: not "context similarity" or "n-gram/surface form" but
**"the text already gave it away" (perceptual redundancy)**. The axis is designed to *join* the continuum
(it reuses the same DURel-style instrument and toggles one factor, modality — exactly how coercion bridged
the two text wedges), and the integration is deliberately conditional: a perceptual-redundancy null is a
first-class negative, not a failure to integrate.

As of the grounding runs the axis stands at **two bounded clear-homonym negatives plus one inconclusive
image-native selection run**. A $0 Lancaster-norms moderation found a word's perceptual groundedness does
**not** predict how well a text-only model tracks its graded senses (bounded null, underpowered). The first
image-input probe found showing the depicting picture does **not** improve same- vs different-synset
separation — because the **text-only panel already separates clear homonyms perfectly** (AUC = 1.000 in
every cell), the predicted redundancy null in strong form
([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)). The honest bound:
the test is **least sensitive exactly where it looks cleanest** — clear homonyms maximize both visual
distinctness and text separability, so text saturates and the image has nothing to add. The cell where an
image could still matter — **fine polysemy / abstract senses where text does not saturate** — is exactly the
cell neither probe contains, and stays open. The third outcome, an image-native VWSD run of the gating shape
([`result/vwsd-grounding-headroom-v1`](../results/vwsd-grounding-headroom-v1.md)), is **inconclusive, not a
clean negative**: the caption baseline saturated, the under-determined stratum fell below the pre-registered
floor, and real images gave no broad lift — a caption-leakage-confounded, underpowered reappearance of the
redundancy null, consistent with the conjecture's posture but not a test of its gating interaction.

## What this page predicts and forbids

**Predicts.** If the continuum thesis holds for these models, the two wedges should not dissociate sharply:
a model that tracks the gradient at one grain should tend to at the other, and coercion should register *in
the lexical instrument* as a sense shift (the bridge bet — confirmed, weakly). **The per-model-ordering
watch is tested, and partly disconfirmed** ([`note/cross-axis-lexical-constructional-ordering-v1`](../notes/cross-axis-lexical-constructional-ordering-v1.md)):
the lexical order (gemini > claude > gpt) transfers **only at the bottom** — gpt-5.4-mini is weakest
lexically *and* most fragile constructionally — but **not at the top** (gemini's lexical supremacy does not
make it uniquely strongest constructionally), and on the same-instrument coercion bridge the order
**inverts** (claude > gpt > gemini). So the grain-to-grain link holds for *failure* but not *strength*, and
the most comparable cross-axis measure inverts. The wedges are unified as **targets** (one form–meaning
cline) but the underlying model **competences are separable** — a concrete dissociation where the first
edition had only an open guess (caveat: n=3 models — read the orderings, not a coefficient).

**Forbids.** It forbids treating a lexical null and a grammatical null as unrelated: a context-similarity
shadow (lexicon) and a frequency shadow (grammar) are the *same* deflationary hypothesis at two grains, and
a finding that the gradient is "just distributional" at one end should lower the prior that it is genuine at
the other. It also forbids over-reading the unification: the continuum is a claim about the *targets*
(form–meaning pairings at different grains), **not** that the model uses one mechanism for both — an open
representational question this behavioral evidence cannot settle.

## The two founding open-questions, closed (session 170) and carried forward

Two open-questions written 2026-05-28 as the constructional wedge's method spine are **closed as founding
questions**, their residual threads narrowed and re-homed rather than left loop-spawning.

- **Q1 — the frequency confound** ([`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md),
  `answered`): answered by the **matched-same-material control + measured residual** — the "beat the
  distributional shadow" test this whole page is built on (the frequency confound and the distributional
  shadow are one deflation named twice). Worked exemplar: the comparative correlative's ≈87 pp
  construction-isolation gap, threshold frozen where it cannot be relaxed after a null
  ([`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md)),
  now a citable claim. It closes the *methodological* question; the irreducible bound (a rich latent n-gram
  interpolation might reconstruct the residual) is carried as a known caveat on each result, not an
  unanswered founding question.
- **Q2 — distributional vs inferential** ([`open-question/distributional-vs-inferential-constructional`](../open-questions/distributional-vs-inferential-constructional.md),
  `answered`): answered **thinly**. The discriminating design ran on AANN
  ([`result/aann-inferential-v4`](../results/aann-inferential-v4.md), escaping the v3 wall with a
  distributive-default control; Δ² +0.78/+0.70/+0.96 net of a lexical cue). The settled position:
  **distributional and inferential do not collapse — but the boundary is a shadow-depth gradient, not a
  clean line, and the inferential-specific signal is securable only model-by-model.** The cross-instrument
  convergence test (paraphrase + NLI + grammaticalized-agreement reflex agreeing) is the project's worked
  sufficiency criterion for *concluding* inferential role; on the current panel it is met by 1/3 models, not
  the panel. Distinct from the `inferential` front-matter *tag*, applied liberally to any probe that
  *targets* inferential role.

Reading the two closures together tightens the headline: the test is **real and passable** (Q1 — a residual
over the shadow exists and is measurable), while *how inferential* that residual is remains **thin,
model-specific, shadow-depth-graded** (Q2). The founding positives are left **intact but calibrated**.

## Theoretical situating

The "beat the distributional shadow" test sits inside a recognizable philosophical frame, mapped on
[`theory/situating-llm-meaning-v2`](situating-llm-meaning-v2.md): the graded sense signal it vindicates is a
**use / prototype** picture of word meaning rather than a discrete truth-conditional inventory; the
conceptual-role upgrade it implies inherits the **holism** objection, which the cross-axis dissociation
mildly strains; the relational axis has its own floor-and-no-positive-bottom-rung synthesis
([`theory/relational-meaning-in-llms`](relational-meaning-in-llms.md)); and the grounding axis's negatives
are generalized into the project's grounding-headroom conjecture — perceptual input can act only in the
residual the text distribution under-determines. Whether any of this amounts to "meaning" is the
eliminativist↔deflationary↔descriptivist question, left to the concept layer.

## Status and revision hook

`status: draft`; `contingent-on: []`. This edition reorganizes existing results under one frame; the probes
and re-analyses the first edition pointed to have run. Live revision triggers:

- **The lexical pole's shadow-saturated corner is unplaced.** The antonymy bet lost; the project does not
  currently know which lexical relation (if any) sits at the saturated end on its panel. A future
  relation-recovery probe with a fresh test (H2 in the decoupling essay's bets, the IS-A-depth proxy of
  [`note/taxonomic-proxy-recovery-pilot-v1`](../notes/taxonomic-proxy-recovery-pilot-v1.md)) would re-place
  it — **fires a revision** here if it finds a relation whose residual is reliably smallest.
- **The adjective-antonymy replication** (J&K's home POS, a fresh design) could revive or bury the prior-art
  reading on the panel; a positive there would re-open the corner question.
- **Grounding's open cell** — fine polysemy / abstract senses where text does not saturate — stays the one
  place perceptual input could still move the lexical pole; an external graded-image sense set would test it.
- **The cross-axis dissociation** is n=3; a within-family size ladder (A4b) or a panel refresh could firm or
  overturn "failure transfers, strength does not."

The net for the continuum thesis, restated for this edition: it is right that the two wedges are **one target
cline** — a positive that beats the distributional shadow on both ends, now promoted at both poles — but
wrong if read as **one competence**: the model orderings dissociate. The saturated corners are the honest
counterweight: presupposition's (grammatical) lands in the under-licensed middle under a run control, and the
lexical pole's is **unplaced** after the one confident placement was falsified. The continuum is a claim
about targets, calibrated by shadow-depth, and held apart from any claim about mechanism.
