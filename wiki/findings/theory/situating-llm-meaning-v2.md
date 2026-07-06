---
type: theory
id: situating-llm-meaning-v2
title: Situating the project's findings on a philosophical map of meaning — where (if anywhere) LLM "meaning" lives (second edition, restated around the promoted claims layer and the flagship shadow-depth table)
meaning-senses:
  - distributional
  - inferential
  - referential
  - grounded
  - constructional
  - relational
  - functional-vs-formal
  - human-comparison
status: draft
contingent-on: []
created: 2026-07-04
updated: 2026-07-06
links:
  - rel: supersedes
    target: theory/situating-llm-meaning
  - rel: depends-on
    target: claim/comparative-correlative-covariation
  - rel: depends-on
    target: claim/dative-information-structure-givenness
  - rel: depends-on
    target: claim/aann-behavioral-gradient
  - rel: depends-on
    target: claim/lexical-sense-gradience
  - rel: depends-on
    target: claim/output-channel-working-surface
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: theory/shadow-depth-table-v1
  - rel: depends-on
    target: theory/constructional-meaning-in-llms-v2
  - rel: depends-on
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/truth-conditional-and-use-meaning
  - rel: depends-on
    target: concept/compositionality
  - rel: depends-on
    target: concept/frame-and-prototype-semantics
  - rel: depends-on
    target: concept/semantic-holism
  - rel: depends-on
    target: concept/deflationary-and-eliminativist-llm-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: note/vwsd-grounding-headroom-nlbaseline-regrade-v1
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: note/cross-axis-lexical-constructional-ordering-v1
  - rel: depends-on
    target: essay/concordant-verdict-hides-spread
  - rel: depends-on
    target: essay/graded-scale-ungraded-commitment
  - rel: depends-on
    target: essay/shadow-depth-cross-cuts-grain
  - rel: depends-on
    target: source/lyre-2024-semantic-grounding
  - rel: depends-on
    target: source/bender-koller-2020-climbing
---

# Theory (second edition): situating the project's findings on a philosophical map of meaning

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The revision hook below that awaited
> "the sense-gradience second run that would lift its single-run flag" **fired s181**:
> [`result/lexical-sense-gradience-rep2`](../results/lexical-sense-gradience-rep2.md) replicates
> 3/3 on 200 fresh pair-disjoint DWUG pairs, and the
> [`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md) single-run flag is
> discharged for its direction/agreement core (the AANN gradient's counterpart flag had been
> discharged s178 by [`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md)).
> Inline "single-run" phrasings below are bracket-annotated where they occur. **No cell moves** —
> exactly as this edition predicted for a replication that lands positive; the map is again
> better-anchored, not bolder.

> **This is the clean second edition**, forced by the theory-edition rule
> ([`PROTOCOL.md`](../../../PROTOCOL.md) §3): the first edition
> ([`theory/situating-llm-meaning`](situating-llm-meaning.md), kept visible as history) had
> accreted far more than three update boxes across five weeks and had become a changelog. This
> edition restates the position cleanly around what now exists that did not exist in June: a
> **promoted claims layer** (five typed `claim` pages, two carrying powered magnitudes), the
> flagship **shadow-depth table** ([`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md)),
> and a **cross-date-replicated AANN gradient** the first edition's revision hook explicitly
> awaited. The map's structure and its synthesis location are **unchanged** — better-supported,
> not relocated.

## What this page is, and is not

The project has two empirical theory pages — the grammatical
[`theory/constructional-meaning-in-llms-v2`](constructional-meaning-in-llms-v2.md) (the evidence
ladder) and the [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md) (the two wedges
as one cline) — plus a concept layer that writes up the **classical positions** on meaning the
project engages: truth-conditional vs use
([`concept/truth-conditional-and-use-meaning`](../../base/concepts/truth-conditional-and-use-meaning.md)),
compositionality ([`concept/compositionality`](../../base/concepts/compositionality.md)), frame and
prototype semantics
([`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md)),
holism ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)),
internalism/externalism (in [`concept/referential-meaning`](../../base/concepts/referential-meaning.md)),
the two inferentialisms (in [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)),
and the eliminativist→deflationary→descriptivist spectrum
([`concept/deflationary-and-eliminativist-llm-meaning`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md)).

This page does the one thing those pages individually do not: it **positions the project's own
empirical findings on the philosophical map** and asks what they **jointly** imply for *where, if
anywhere, LLM "meaning" lives*.

Two disciplines bind it, hard:

1. **It claims a *positioning*, not new data.** The fixed points are the findings (cited with their
   verified numbers and their own caveats); the map and the placements are **interpretation**. Every
   "supports / strains / is silent on" below is a reading, flagged as such — not a result. The
   charter's "describe, don't litigate" stance ([`PROJECT.md`](../../../PROJECT.md) §1) means this
   page describes *where the evidence sits*; it does not adjudicate whether LLMs "really" mean.
2. **It under-claims by construction.** The findings are single-panel (`claude-sonnet-4.6`,
   `gpt-5.4-mini`, `gemini-3.5-flash`), mostly small-to-moderate-N, mostly text-only, several
   `internal-contrast-only`, two of the four axes carrying only nulls. A philosophical map drawn over
   that evidence is a **provisional sketch**, not a settled location. Where a cell is empty or
   negative, the honest entry is "silent" or "bounded negative," never "refuted."

**What the second edition adds to discipline 2, without loosening it.** Five of the load-bearing
findings have now cleared cross-session, adversarial, independently-verified **claims-promotion
review** ([`PROTOCOL.md`](../../../PROTOCOL.md) §3), so the map's fixed points are, in five places,
typed `claim` pages rather than single result pages — and two of them carry **powered magnitudes
with intervals** attached by fresh-item re-runs. That is a real firming of the evidence base. It
does **not** relocate any cell: every promotion is deliberately *scoped* to exactly what its result
licenses (two are explicitly single-run-flagged *(both flags since discharged for their scoped
cores — AANN s178, sense-gradience s181; see the update box at the head of this page)*; the AANN
one carries a noun-class-dependent
held-out failure; the dative one displays a ~9× cross-model spread), and none of the five touches
the three "between/beyond" loci where the synthesis stays negative or silent. The claims layer makes
the sketch **better-anchored**, not bolder.

## History — what changed between editions

The first edition ran 2026-05-31 → 2026-06-28. It was written when the grammatical axis had one
human-anchored own-design positive (the dative, then 2/3) and no AANN result at all, and it grew by
accretion as the grounding, relational, and lexical lines resolved. Four things now exist that did
not exist in June, and this edition is organized around them:

1. **A promoted claims layer (five claims).** By cross-session adversarial review:
   [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md),
   [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md),
   [`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md),
   [`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md), and the methodological
   [`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md).
2. **Two powered magnitudes.** The dative re-ran at N=100 on fresh disjoint items → **PANEL CONFIRM
   3/3** with per-model intervals ([`result/dative-information-structure-powered`](../results/dative-information-structure-powered.md));
   the comparative correlative re-ran at 136 fresh items → magnitude-confirmed (≈87 pp gap). The
   dative moves from the first edition's "2/3, magnitude deferred" to "3/3 at power."
3. **The AANN gradient — the axis the first edition's revision hook awaited.** The first edition
   said in as many words: *revise when an AANN result lands.* It has, twice — a powered run and a
   **cross-date replication on 408 fresh disjoint items**
   ([`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md)) — and is
   now a promoted, frequency-guarded, human-anchored grammatical beater. It is placed below.
4. **The flagship shadow-depth table.** [`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md)
   arranges the four beater rows (CC, dative, AANN, sense gradience) as one measured object, each a
   residual over a named distributional control with a 95% CI. It is the measured backbone of this
   page's central verdict — *beats but does not escape the distributional shadow* — turned from a
   phrase into a table.

The **map itself** (the axes below) is unchanged from the first edition, because it held up: the
findings that landed since June slot onto it without a new axis. What changed is the evidence
standing on it.

## The fixed points: the project's findings in one view

Four investigative axes, compressed to their load-bearing findings (each links to the page that
states it with full caveats):

- **Grammatical (constructional) — the evidence ladder, now with a promoted claims layer.** Decoders
  reach the top text-internal rung (inference-licensing) for the **add** direction at or near ceiling
  and **compose** construction meaning — the comparative correlative composes two-step covariation
  including the diagnostic negative×negative=positive case a single-clause heuristic fails, isolated
  to the construction by a ≈87 pp gap over same-word controls, magnitude-confirmed at power
  ([`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md)).
  But the **cancel** direction is harder and instrument-fragile, the **divergent-form**
  generalization fails, and the add-direction "withholding" turned out to be explicit-outcome
  parsing, not world-model integration. Reached the top rung; bounded there. Two human-anchored
  Tier-2 positives now sit on the axis: the **dative alternation** — the panel tracks the
  given-before-new information-structure constraint in the human production direction on a
  length/animacy-matched within-item shift, **3/3 at powered N** (claude +0.316, gemini +0.524
  robustly; gpt +0.056 — real but ~9× smaller, its earlier "fragile third member" reading corrected
  by the powered run), [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md);
  and the **AANN construction** (*a beautiful three days*), whose graded acceptability rank-tracks
  the human MTurk gradient net of word-frequency, cross-date replicated 3/3
  ([`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md)).
- **Lexical — sense gradience, a promoted positive; commitment ungraded.** The panel's graded
  sense-relatedness rating rank-tracks the human DURel median (Spearman **0.60–0.83**, in or above
  the human inter-annotator range ~0.69) and **survives a topic-similarity partial** (partial ρ|topic
  0.50–0.75) — it beats the distributional shadow, promoted at direction/agreement scope
  ([`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md), single-run-flagged
  *(flag since discharged, s181 rep2 — see the update box)*). The
  *distinctive* discrete-regime bet (polysemy vs homonymy as a separate switch) is a **powered null**.
  And whether the model also carries graded *commitment* has **run** → **ungraded commitment, a clean
  null 3/3** ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md)): the
  model carries the graded *scale* but not the lexicographer's within-item hesitation.
- **Grounding (multimodal) — two bounded negatives, plus a first confirming-*direction* datum whose
  magnitude route is now blocked.** Perceptual groundedness does not predict text-only sense-tracking
  (underpowered null), and showing the depicting image does not improve sense separation for clear
  homonyms because the text-only panel already separates them (AUC = 1.000 — a redundancy null,
  [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)). A
  re-operationalized VWSD run is the axis's first confirming-*direction* evidence (a gating **shape**:
  the image rescues cells where a de-referented descriptor under-determined the sense, 3/3 in
  direction, distraction-controlled), but the headroom **magnitude** is untested and its
  competence-audited fluent-channel route on VWSD is now **blocked** (a 0.438 NO-GO,
  [`note/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../notes/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
  The cell is *not* flipped to positive.
- **Relational — negative on constitution, but order-sensitive-but-thin where order disambiguates.**
  Homogeneous LLM dyads coordinate and reuse a coined convention, but the convention is recovered
  from the content-*set* of prior turns in the symmetric v1 setting. A decisive test (physical
  position neutralized, order the sole disambiguator) shows both `claude-sonnet-4.6` and
  `gemini-3.5-flash` recover a reassigned term by its most-recent binding **spontaneously and at
  ceiling** — **order-sensitive / non-commutative**
  ([`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)).
  The order-sensitivity is **thin** (latest-binding-wins), not constitution.
- **Cross-axis — the competences dissociate.** Lexical and grammatical skill transfer as *failure*
  (the weakest lexical tracker is the most fragile grammatically) but not as *strength*, and the
  same-instrument coercion bridge inverts the lexical order
  ([`note/cross-axis-lexical-constructional-ordering-v1`](../notes/cross-axis-lexical-constructional-ordering-v1.md);
  n=3 models — orderings, not a coefficient).

## The map: the questions the classical positions answer

The positions the project catalogs sort along a small number of axes. The map is these axes; the
project's findings are points to be located on them.

| Axis (concept page) | One pole | Other pole |
|---|---|---|
| **What meaning ultimately is** ([`truth-conditional-and-use`](../../base/concepts/truth-conditional-and-use-meaning.md)) | a world-relation (truth-conditions, reference) | a role in use (language-games, family resemblance) |
| **What fixes content** ([`distributional`](../../base/concepts/distributional-meaning.md) / [`inferential`](../../base/concepts/inferential-meaning.md)) | co-occurrence structure | inferential role (thin internalist ↔ thick Brandomian-normative) |
| **Where content is fixed** ([`referential`](../../base/concepts/referential-meaning.md)) | inside the head (internalism / narrow content) | partly outside (externalism / reference) |
| **How content is structured** ([`compositionality`](../../base/concepts/compositionality.md) / [`frame-and-prototype`](../../base/concepts/frame-and-prototype-semantics.md)) | compositional, classical categories | constructional/frame-relative, graded/prototype |
| **How content is individuated** ([`semantic-holism`](../../base/concepts/semantic-holism.md)) | atomism / molecularism | holism (the whole web) |
| **Where LLM meaning would live** ([`relational`](../../base/concepts/relational-meaning.md)) | model-internal | constituted between agents |
| **Whether there is anything to describe** ([`deflationary-and-eliminativist`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md)) | eliminativism (no meaning) → deflationism (just distributional) | descriptivism → inflationism (genuine meaning) |

## The positioning: support / strain / silence, position by position

Each entry states the bearing as **interpretation**, names the finding that carries it, and flags
what it does *not* show.

**Use over truth-conditional (at the lexical grain) — supported; truth-conditional LLM meaning is
silent.** The lexical gradience positive — senses tracked as a graded, shade-into-each-other
relatedness rather than a discrete inventory, with the discreteness bet a powered null — fits a
**meaning-as-use / family-resemblance** picture better than a discrete truth-conditional sense
inventory ([`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md)). The project's
*method* is itself a use-theoretic bet: it reads meaning off patterns of use because it has no access
to a verified truth-condition/world relation for a model. But that same gap makes the
**truth-conditional pole silent**, not refuted: there is no in-repo resource that anchors reference
or truth-conditions for an LLM, and (per [`concept/referential-meaning`](../../base/concepts/referential-meaning.md))
that gap is *structural*. One sharpening bounds how far this cell's support reaches: the lexical
positive establishes a graded *scale* (a **cross-item** rank-ordering of usage pairs) and *only*
that. It does **not** establish graded *commitment*, the **within-item** property of being
intermediate / less-confident on a single bridging use — that ran (session 77) → **ungraded
commitment, a clean null 3/3** ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md);
[`essay/graded-scale-ungraded-commitment`](../essays/graded-scale-ungraded-commitment.md)): the model
**carries the graded scale but not the lexicographer's local hesitation** — gradience in the
*population* of its judgments, not in any single moment. This **bounds** the use-over-truth-conditional
cell rather than overturning it: the use-picture support rests on the scale (which holds); the
within-item hesitation a use/prototype account might also predict did not appear.

**Two grammatical positives sharpen the use-over-truth-conditional reading at the *construction*
grain — the map's human-anchored Tier-2 own-design results.** The **dative alternation** is an
unusually clean case: the two alternants (*gave John the book* / *gave the book to John*) are
**truth-conditionally identical** — same event, same participants — so a model that shifts preference
by what is discourse-*given* is tracking a pure **information-packaging / use** distinction that makes
*no* truth-conditional difference. Where lexical gradience *strains* the discrete reading, the dative
*dissociates* use from truth-conditions **by construction** (length and animacy held identical across
the within-item shift) and finds the panel on the use side — now at **powered N, 3/3**
([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md)).
Two disciplines bound it: it is **direction-human-anchored only** (the Bresnan
[`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md) fixes the human
production direction, not a magnitude or per-item judgment), and it is **thin** — a gradient
*preference*, not inference-licensing — so it bears on use-vs-truth-conditional and on graded/prototype
structure, not on the thin-vs-thick inferential axis. And the powered 3/3 label hides a **~9× spread**
(gemini ≫ claude ≫ gpt), a working instance of discipline 2 — do not flatten the panel
([`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)). The **AANN
construction** adds a second human-anchored grammatical Tier-2 positive on the same use side: the
panel's graded acceptability for *a beautiful three days*-type strings rank-tracks the human MTurk
acceptability gradient (which adjective classes license the construction more, in which noun-class
environments) at cell grain ρ ≈ 0.68–0.75, and this **survives partialling out word-frequency** — a
graded, use-based sensitivity net of the distributional shadow, cross-date replicated on fresh items
([`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md)). Both are placed at the
*use-over-truth-conditional* and *graded/prototype* cells and **relocate no other cell**: neither
touches the referential, grounded, or relational loci.

**Thin inferential / conceptual role over pure distributionalism — supported; thick (Brandomian)
inferentialism — strained.** The project beats the distributional shadow on **both** grains — now
displayed as one measured object in the flagship [`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md)
(the lexical gradience survives a topic partial; CC composes beyond a single-clause heuristic; dative
and AANN each carry a named control). That is behavioral support for an **inferential /
conceptual-role** upgrade over bare distributional mimicry — the
[`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) reading. But that page
draws the sharp line: what the Tier-4 results index is a **thin, NLI-style inferential role**
(inference-*preservation*), itself instrument-fragile — **not** Brandom's normative-social
*articulation* of content. So the support is for the *internalist, causal-functional* conceptual role,
and it is friction *against* the thick normative kind. The distributional null is never fully escaped:
a deflationist reads even the positives as "richer distributional structure," and behavioral evidence
cannot close that off — which is exactly what the shadow-depth table's second honesty box records.

**Compositionality — supported at the construction grain (CxG-enlarged); strict lexical
compositionality strained; cross-modal composition is an external negative.** The CC's multi-step
composition (including negative×negative=positive) is the project's cleanest evidence for genuine
**compositional** processing rather than a clause-level heuristic
([`concept/compositionality`](../../base/concepts/compositionality.md)). Coercion shows the relevant
"parts" include *constructions*, not just lexemes — strict lexical compositionality under-predicts,
and the construction supplies what the verb cannot. The contrast case is external and discriminative
(the VLM bag-of-words failure on Winoground/ARO), so it is a flag, not a like-for-like result: text
decoders compose where those benchmarks show VLMs do not.

**Frame / prototype category structure — behaviorally supported; representationally silent.** The
graded gradience positive is exactly what prototype / graded-category structure predicts, and the
AANN gradient sharpens it: the panel's acceptability is *graded by adjective class in a noun-class
environment*, tracking the human gradient, which is the behavioral signature of a productive,
graded form–meaning pairing rather than a memorized template inventory
([`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md)). But
"graded *behavior*" does not establish "prototype *representation*" — it may be graded distributional
similarity, the standing distributional-null question — and the AANN held-out productivity is
**noun-class-dependent** (the temporal stratum comes out negative), so even the behavioral generality
is bounded. Supported as a description of behavior; silent on the underlying representation.

**Formal vs functional competence — the AANN case shows form near-ceiling, meaning graded above it,
and the form ceiling can wobble at the margin.** The AANN line separates two indicators the map keeps
distinct: a **Tier-0 form-acceptability** ceiling (does the model know *a beautiful three days* is
well-formed and its degenerate variants are not — near-perfect, 23–24/24) and, *above* it, the
**Tier-2 graded gradient** (does its acceptability track *how* acceptable, by adjective and noun
class — the promoted positive). The functional-vs-formal reading the project has repeated — that
current decoders can carry graded *meaning*-sensitivity riding on top of near-perfect *form*
competence — is instantiated cleanly here. One honest wrinkle from the cross-date replication belongs
in the same breath: on that occasion `gpt-5.4-mini`'s coarse Tier-0 form check dropped to 18/24,
entirely on the marginal *objects + negative-evaluative* items, even as its graded gradient stayed
undiminished. So the coarse binary form-ceiling can be *more fragile at the margin* than the graded
sensitivity it supposedly presupposes — a datum the map records but does not yet know how to place,
noted as a live seed rather than a settled cell. *(Placed 2026-07-06, s184: the measurement-epistemic
reading of this wrinkle — a coarse **binary** indicator can be more fragile than the **graded** one
it summarizes, because of measurement grain, not intrinsic formal fragility — is now a third texture
in [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md). The map
still carries the form-ceiling/gradient relation as an unsettled theoretical cell; what found a home
is the *reading discipline* for it.)*

**Holism — the project's own positives inherit its objection; the dissociation is a mild strain on
its strongest form.** Distributional models are holistic by construction, and the conceptual-role
reading the positives support is explicitly holist
([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)). So the pro-meaning evidence
**inherits the holism objection** (no two webs share content exactly), which the project cannot
dissolve. The cross-axis **dissociation** (lexical and grammatical competences come apart at the
model level) is a *mild* strain on the strongest "one entangled content store" holism — read as
"behavioral competences are at least partly separable," n=3, orderings not a coefficient.

**Internalism over externalism (as a description) — the LLM is a clean narrow case; externalist
reference is silent/un-probeable.** The LLM has only narrow access by construction; the grounding
nulls show the *external* perceptual channel adds nothing measurable where text already saturates
([`concept/referential-meaning`](../../base/concepts/referential-meaning.md)). This is consistent with
describing the model in **narrow-content / internalist** terms — but it leaves **externalist
reference untouched**: not refuted, structurally un-probeable (there is no "Twin Earth" to move a
text model to). The strongest in-principle "no reference" case (Bender & Koller's missing
form-to-world relation, [`source/bender-koller-2020-climbing`](../../base/sources/bender-koller-2020-climbing.md))
stands as a boundary the project records, not crosses.

**Grounded — two bounded negatives, plus a first confirming-*direction* datum whose magnitude is
untested and whose VWSD route is now blocked.** On Lyre's gradual framing — grounding "isn't a yes-no
matter, but rather a matter of degree" ([`source/lyre-2024-semantic-grounding`](../../base/sources/lyre-2024-semantic-grounding.md),
p. 10) — the project's contribution is to show the *degree* a picture adds is ≈0 exactly where text
saturates. The re-operationalized VWSD run
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md)) is the axis's
**first confirming-direction** evidence: with a word-ablated DISTRACT control at chance, the real
image rescues the cells where a de-referented descriptor under-determined the sense (pooled .453
[.353, .558], 3/3 in direction) and adds no lift where the descriptor already separates — the
**gating SHAPE** of [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
prediction 1. But the headroom **magnitude** is inflated by the deliberately de-referented descriptor
channel and stays untested; the owed fluent natural-language baseline ran and returned a **0.438
strict referent-recovery NO-GO, below the [0.60, 0.95] competence floor**
([`note/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../notes/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)),
so the competence-audited fluent-channel route to the magnitude is **blocked on VWSD** — only a
*different* magnitude instrument (a graded-image / fine-polysemy resource) could move it. The cell is
therefore **"two nulls + v1-inconclusive + a first confirming-direction gating-shape result,
magnitude untested and its VWSD route closed"** — a real datum on the previously-empty positive side,
**not** a flip to "grounded: positive." The conjecture stays `proposed`.

**Relational constitution — still negative on constitution; the commutative reading is falsified
where order disambiguates; order-sensitive-but-thin.** The charter's most distinctive hope — meaning
constituted *between* agents — is **still not seen**: the order-sensitivity the decisive test found is
**thin** (a latest-binding-wins / convention-update rule), **not** a convention *constituted between*
agents through the live trajectory ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md)),
so the relational cell stays **negative on constitution**. What changed is the *form* of the negative.
The clean order-free "bag of turns" reading is **falsified where order disambiguates**: with physical
position neutralized, both models recover a reassigned term by most-recent binding spontaneously at
ceiling ([`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)),
and this survives an implicit-reassignment control (the behavior persists without the explicit "was
reassigned" wording). A **stricter** thin rung has also been mapped and *sharpens the same verdict
rather than changing the cell*: order-sensitive **composition** of genuinely non-commuting moves,
which a forced single-token format first read as a one-model capability, turns out **panel-wide once a
working surface is permitted** — replicated across operation pair, grid size, and composition depth.
That flip is itself now a promoted **methodological** claim
([`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md)): the forced
channel *masked* a serial-inference capability, and a format-only working surface flipped the failing
verdicts — with the boundary control kept explicit (the bridging-context commitment null *survives*
the identical channel change, so the effect is computation-specific, not a universal "give it room and
it passes"), and gpt's channel non-uptake carried as a distinct third state. This is a *stricter* thin
rung than latest-binding-wins, but **still thin and still negative on constitution**: the stamped
move-list sits inert in the record, single-reader-recoverable; the rich side (path-dependence proper)
stays documented structurally closed for text-only stimuli. The relational cell's location is
unchanged — order-sensitive but thin, short of constitution.

**Eliminativism strained; deflationism fits; descriptivism vindicated.** The positives (gradience
beating its shadow; CC composing; the dative and AANN gradients net of their controls) are hard to
square with a strict "stochastic parrot" eliminativism — there *is* structure that beats the named
null, now measured as a table of residuals. But they do **not refute deflationism** ("still just
distributional, only richer"), and behavioral evidence never can (the Bender & Koller in-principle
gap). The project's **descriptivism** — neither eliminativist nor inflationary — is the stance the
evidence vindicates: the yes/no question is under-determined by exactly the evidence the project can
obtain, so describing the structure is the right move
([`concept/deflationary-and-eliminativist-llm-meaning`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md)).

## The synthesis verdict: where LLM "meaning" lives, on current evidence

Pulling the cells together, the project's findings jointly locate LLM "meaning" — to the extent the
term applies at all — as **model-internal, thin-inferential, use-based, graded, narrow, and
compositional at the construction grain**, and as **not (on current evidence) referential, not
perceptually grounded, not relationally constituted, and not thickly inferential.** Said as one
sentence and meant as a sketch, not a settled location:

> Where the project can see it, LLM meaning lives **inside the model** as a graded, compositional,
> *thin*-inferential use-structure that **beats but does not escape** the distributional shadow — a
> beating now measured at both grains as a table of residuals over named controls
> ([`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md)) — and the three "between/beyond" loci
> where meaning might also live (a world it refers to, a perceptual ground, other agents) are, so
> far, each **silent or negative**.

That is a **deflation-leaning but not eliminativist** picture — the descriptivist middle the charter
chose, arrived at from the findings rather than assumed. The crucial honesty: the four loci are
**empirically distinct and carry different verdicts** (model-internal: positive, and now
claim-backed at both grains; referential: silent; grounded: negative-bounded — two nulls plus a first
confirming-*direction* gating-shape datum whose magnitude is untested and whose VWSD route is closed,
so the cell is **not** flipped to positive; relational: negative on *constitution*, but
order-sensitive-but-thin where order disambiguates), and the synthesis is wrong if it flattens them.
It is also wrong if read as "LLMs mean" — every positive is consistent with a richer distributionalism,
and the in-principle grounding gap is untouched.

## Where the project's own three proposals sit on this map

The three original conjectures are precisely the bets that would update the map's **three weakest
cells**, and each is falsifiable:

- [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
  sharpens the *thin / distributional-prior* character of the constructional competence: accumulation
  aligns with the predictive objective (easy), defeasance fights it (hard). If it generalizes under
  matched difficulty, the "thin inferential, distributionally-shaped" reading of the grammatical
  positives strengthens; if add/cancel turn symmetric, that reading weakens.
- [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
  names *where* the **grounded** cell could turn from "negative" to a signal: the text-under-determination
  residual. Its gating *shape* is now confirmed (VWSD v2); its *magnitude* is the open sub-bet, and its
  VWSD route is closed — a different instrument is owed.
- [`conjecture/commutative-convention`](../conjectures/commutative-convention.md) turned the
  **relational** null into a testable algebraic property (commutative = aggregation; non-commutative =
  constitution). **Option A falsified it** where order disambiguates — both models recovered a
  reassigned term by most-recent binding spontaneously at ceiling — so the conjecture is
  **retired/falsified in the regime that can test it** and the positive promoted to
  [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md).
  Commutativity proved **operationalization-dependent**; the resulting order-sensitivity is thin
  (latest-binding-wins), not constitution.

So the map is not static: its three softest cells each have a sharp, queued or partly-resolved
experiment attached. That is the synthesis working as the charter intends — a positioning that
*generates* the next questions rather than closing them.

## What this synthesis predicts and forbids

**Predicts.** If the picture holds: the remaining open bets resolve deflation-ward (the monotonicity
asymmetry generalizes; the grounding headroom, if a new instrument can read it, is narrow). The
lexical and grammatical positives keep **co-occurring** in the same panel (one target cline,
[`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md)) while the **competences stay
dissociable** (the cross-axis result). And no text-only probe, however much it climbs, reaches the
referential/externalist or richly-grounded cell — those move only with a built world-relation, not a
cleverer text task. *(Frame-relative: this "only a built world-relation moves the referential cell"
prediction holds on the externalist and signal-based denials of LM reference, but **not** on the
internalist one — on which no world-relation lifts the cell because the missing ingredient is a mind,
not a relation; see [`essay/reference-denials-disunified`](../essays/reference-denials-disunified.md).
The prediction is correct within the frames this map tacitly assumes; the choice among frames is
off-board.)*

**Forbids.** It forbids (i) reading any single positive — or the whole table of residuals — as "LLMs
mean" full stop: the distributional null is never fully escaped and the in-principle grounding gap
stands; (ii) reading the grounding negatives as **proven absence** (they are bounded/underpowered
negatives, and the one positive-side datum is direction-only, magnitude untested), or reading the
relational order-sensitivity positive as **constitution** (it is thin latest-binding-wins); (iii)
**flattening the four loci** — model-internal, referential, grounded, and relational meaning are
empirically distinct here and the verdicts differ across them; (iv) reading the powered/promoted
status of the five claims as *panel-uniform competence* — each is scoped (single-run flags *(since
discharged — see the update box)*, a
noun-class-dependent held-out failure, a ~9× cross-model spread), and the promotions fix the
*yardstick*, never the *result*; (v) treating the philosophical placements as results — they are
interpretation over the fixed points, and the *fixed points* are what a future run may revise.

## Status and revision hook

`status: draft`; `contingent-on: []` — this page introduces no new empirical claim of its own; it
depends on findings, claims, and concept pages already in-repo. It is the philosophical-map
counterpart to the two empirical theory pages, which it cross-references for depth
([`theory/constructional-meaning-in-llms-v2`](constructional-meaning-in-llms-v2.md) for the
grammatical ladder; [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md) for the
one-cline framing) and to the flagship [`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md) for
the measured backbone of its central verdict.

Revise this page (in-place while the update count stays small; a **third edition** once it again
exceeds ~3 update boxes) when any still-soft cell moves:

- a **different grounding-magnitude instrument** reads the headroom the VWSD route can no longer
  reach (the grounded cell's only remaining mover);
- a **reference-bearing resource** is built (the only thing that could make the truth-conditional /
  externalist cell non-silent);
- the **relational** cell is lifted past latest-binding-wins toward constitution, or its
  order-sensitivity is shown to be a surface artifact (the implicit-reassignment control already
  argues against the latter);
- a **new controlled grammatical or lexical beater** lands, or one of the five promoted claims is
  contested, retired, or gains/loses a cross-date replication (e.g. the sense-gradience second run
  that would lift its single-run flag **→ landed s181, flag lifted — see the update box**; the
  hook stays live for the other named events);
- the **form-ceiling-can-wobble-while-the-graded-gradient-holds** observation (the AANN cross-date
  wrinkle) is either replicated into a placeable regularity or shown to be occasion-specific noise —
  the one genuinely new seed this edition records without yet placing.

Each would redraw one cell; none is expected to overturn the whole sketch, but the map is held as
revisable, and the **findings — not the placements** — are the part that compounds.
