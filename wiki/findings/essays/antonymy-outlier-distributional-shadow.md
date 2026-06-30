---
type: essay
id: antonymy-outlier-distributional-shadow
title: The antonymy outlier is the distributional shadow showing through
meaning-senses:
  - distributional
  - inferential
  - human-comparison
status: draft
contingent-on: []
created: 2026-06-29
updated: 2026-06-30
links:
  - rel: depends-on
    target: source/cao-2025-semantic-relation-knowledge
  - rel: depends-on
    target: source/cao-2025-distinctive-cooccurrence-antonymy
  - rel: depends-on
    target: source/diera-2026-encode-semantic-relations
  - rel: depends-on
    target: source/justeson-katz-1991-antonym-cooccurrence
  - rel: depends-on
    target: source/harris-1954-distributional-structure
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: essay/two-distributional-hypotheses
  - rel: depends-on
    target: essay/cross-level-convergence-ladder
  - rel: supports
    target: conjecture/lexical-relation-shadow-saturation
---

# Essay: the antonymy outlier is the distributional shadow showing through

> **Status: draft (2026-06-29). A philosophical-track essay arguing in the project's own voice.**
> It introduces **no new empirical claim** and makes **no human comparison of its own**: every
> empirical assertion inside it cites the in-repo `source` page that carries it, at that page's
> stated strength. The original contribution is the **argument** — a reading of *why* antonymy is
> the lexical-semantic relation models recover best, and what that recovery does and does not show.
> The two empirical inputs are **prior-art on older/smaller models** (Cao et al. 2025 on
> BERT/RoBERTa/Llama-3; Diera & Scherp 2026 on Pythia-70M/GPT-2/Llama-3.1-8B), **not** the project's
> own frontier panel; the essay makes no claim about the panel. **Revision trigger (headline):** if a
> frontier-panel relatum probe with a contrastive-frame distributional control shows antonymy
> competence *surviving* the control, revise the deflationary reading for that case (see the triggers
> at the end).
>
> **Revision (session 148, 2026-06-29).** Trigger (d) fired in the *confirming* direction: the primary
> corpus study of antonym co-occurrence,
> [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
> (Justeson & Katz 1991, Brown Corpus, predicative adjectives), was ingested. It *measures* the
> contrastive-frame characterization the essay had grounded only in Harris — so that characterization
> now carries a primary anchor (below), and one phrase was sharpened (J&K, with Charles & Miller, deny
> *free* substitutability; the substitution is *within* co-occurrence sentences). No empirical claim
> about the panel changed; the deflationary reading is unchanged and now better-grounded.
>
> **Revision (session 149, 2026-06-30).** Trigger (d) fired a *second* time, on the further primary
> source it was left live for: [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md)
> (Cao, Yamada & Tokunaga 2025, \*SEM; COCA, a cross-relation/cross-PoS co-occurrence study by the
> same group as Cao et al. 2025a). It bears on the essay's flagged **adjectival→nominal extrapolation**
> in the *confirming* direction on the **co-occurrence-strength leg** (antonym pairs co-occur
> distinctively for **nouns/verbs/adverbs**, not only adjectives) and supplies the **cross-relation
> comparison J&K lacked** (antonymy is the relation with the *highest* co-occurrence strength, the only
> consistent order preference, and the shortest span, distinctively above synonymy/hypernymy/holonymy).
> One residual is preserved, not closed: this source measures strength/order/distance only and
> *explicitly cannot say* "in which lexical and dependency constructions two words … occur", so the
> specific **parallel-contrastive-frame mechanism for nouns stays inferential** (J&K measured it for
> adjectives; this paper only *speculates* it for the rest). No empirical claim about the panel changed;
> the deflationary reading is unchanged and better-grounded across parts of speech.

## The convergence

Two independent in-repo sources, with two different methods, find the **same** thing about the
lexical-semantic relations: **antonymy is the relation models recover best.**

The first is behavioral. Cao et al. 2025 build a same-task human-vs-model prompt-based probe over
six nominal relations (hypernymy, hyponymy, holonymy, meronymy, antonymy, synonymy) and report,
verbatim, that "**Antonymy is the outlier relation where all models perform reasonably well**"
([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md),
Abstract). The §8 soundness numbers put a figure on the outlier: "**All models perform relatively
well for antonymy, where the best model Llama-8B (L1) achieves 𝒮=0.57, whereas for other relations,
best values typically lie around 𝒮=0.30**"
([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md),
§8). All of this sits inside the paper's headline gap — "**The results reveal a significant
knowledge gap between humans and models for all semantic relations**"
([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md),
Abstract): antonymy is the *positive* outlier *within* a generally human-subceiling picture, not a
relation at which models reach the human ceiling.

The second is representational. Diera & Scherp 2026 probe where four lexical relations (synonymy,
antonymy, hypernymy, hyponymy) live inside decoder activations, using linear probing plus sparse
autoencoders and activation patching, and report a difficulty ordering that holds across three
models: "**Difficulty is consistent across models (antonymy easiest, synonymy hardest)**"
([`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md),
Abstract). The body sharpens it: "**a consistent difficulty ordering across models, with antonymy
easiest, followed by hyponymy, then hypernymy, and synonymy hardest … antonymy approaches ceiling on
Llama**" ([`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md),
§4.1).

So a behavioral relatum-production probe and an internal-representation probe agree on the same
relation. The question this essay asks is what that agreement is *evidence for*. (The competence at
issue is, in the [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) sense, an
inferential one — a semantic relation like antonymy is inferential-role structure, since knowing *X is
the opposite of Y* licenses inferences to and from it — and the essay's question is how much of that
inferential-relation signal reduces to the `distributional` shadow.)

## The thesis: this is the distributional shadow at its largest, not relational competence over and above it

The project's lexical wedge runs on a single test, stated at
[`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md): a lexical-meaning claim
must show the model tracks sense/relation structure **over and above** surface co-occurrence — it must
*beat the distributional shadow*. The Cao source page's own note to the continuum already reads the result this way, calling
antonymy "the relation most strongly cued by symmetric contrastive co-occurrence … the one models
recover best, which is exactly what a distributional-shadow story predicts"
([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md),
§"What this bears on in-repo", the `refines` note to the continuum). This essay takes that one-line
observation and makes it the argument.

The claim is this. **Antonymy is the relation where the distributional shadow is largest, so it is the
relation where the "over and above" residual that a genuine competence claim must show is smallest.**
Antonym pairs do not merely co-occur; they recur in tight, near-symmetric *contrastive frames* —
conjoined "X and Y" and repeated phrases with one antonym substituted for the other (illustratively,
"X not Y", "neither X nor Y", "from X to Y", "X versus Y") — and *when they co-occur* they
substitute for one another in otherwise near-identical environments. This is not just an intuition
read off Harris: it is a measured corpus fact. The primary corpus-linguistic study of antonym
co-occurrence,
[`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
(Justeson & Katz 1991, on the Brown Corpus), confirms "**antonymous adjectives do co-occur within the
same sentence much more often than is expected by chance**" (p. 3) and that they do so in highly
regular contrastive frames — "**we find a strong trend for the antonyms to occur in syntactically
parallel and usually lexically identical structures**" (§3, p. 11), with "**63% (139/219) of antonym
co-occurrences … in lexically identical structures**" and "**Fully 164 (75%) … in conjoined syntactic
structures**" (§3, pp. 11-12); in their summary, "**antonyms co-occur sententially mainly by
substituting for one another in otherwise identical or near-identical phrases**" (p. 13). (Two
honesty caveats J&K force: the substitution is *within co-occurrence sentences*, not free global
interchangeability — J&K, following Charles & Miller, deny that antonyms are generally substitutable
in single-member contexts; and their evidence is on **predicative adjectives in one corpus**, so its
extension to nominal antonymy is the essay's plausible extrapolation, not a J&K measurement.) That
extrapolation's **co-occurrence-strength leg** now carries its own primary measurement:
[`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md)
(Cao, Yamada & Tokunaga 2025, on COCA) finds antonym pairs "**co-occur with high strength, in a
preferred linear order, and within short spans**" (Abstract) **across nouns, verbs, adjectives and
adverbs**, and — the cross-relation comparison J&K could not make — "**consistently distinctive from
all other relations across all metrics used**" (§6) — antonymy pairs "**consistently yield both the
highest G² scores … and the largest percentage … of significant co-occurring pairs across all PoS**"
(§4). So antonymy is not merely co-occurrence-dense in absolute terms but *distinctively the
most* co-occurrence-dense relation, for nouns as for adjectives — which is exactly the corpus fact the
shadow-is-largest reading needs. The residual the extrapolation still carries is narrower than before:
Cao et al. measure strength/order/distance only and state they "**can not answer in which lexical and
dependency constructions two words … occur**" (Limitations), so the specific *parallel-contrastive-
frame* mechanism remains a J&K measurement for adjectives and the authors' (and this essay's)
*conjecture* for nouns — they note only that the strong lexical pairing "**might enhance their
suitability for parallel constructions**" (§5). On
Harris's form-internal contrast measure, "**difference of meaning correlates with difference of
distribution**"
([`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md),
p. 156), antonymy is then the relation where the relational structure is *most fully written into the
distribution itself*: producing the antonym of a cue is, to a first approximation, completing a
contrastive frame the *corpus* is measurably saturated with — a Brown-Corpus fact (J&K), which the
essay reads forward to a model's training distribution as its own flagged extrapolation, not a J&K
measurement of any model's training data. So "antonymy is the one relation models do
well" is not, on its face, a triumph of relational competence over distribution — it is the lexical
wedge's **distributional shadow cast most fully**, the one relation where the deflationary null is
hardest to reject because there is least daylight between the relation and its distributional trace.

This re-describes a strong-looking positive as the *weakest* place to mount a competence claim. The
relation at which models look best is precisely the relation at which "looking good" is least
informative about anything over and above co-occurrence.

## Which ancestor antonymy names: maximally Harris-recoverable

The sorting in [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md) makes the
point sharper. That essay argues the next-token objective instantiates the **Harris** (form-internal)
distributional hypothesis and not the **Firth** (situated) one, so that a distributional success
"names the Harris ancestor precisely and leaves the Firth (situated) and … world-relation questions
exactly where they were." Antonymy is the extreme case of a maximally **Harris-recoverable** relation:
its structure is a within-language contrast over linguistic environments, and the contrast measure
Harris defines — read forward as "the vector-space neighborhood / substitution-similarity measure the
project uses as a distributional indicator"
([`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md),
§"Bearing on this project") — is *exactly* the measure under which paired antonyms come out tightly
related. Antonymy is what the form-internal contrast measure was almost built to recover.

That has a deflationary corollary the two-hypotheses essay already licenses. If antonymy's strong
recovery names the Harris ancestor, then it "names its ancestor precisely and leaves the situated and
world-relation questions untouched" — it tells us *nothing new* about anything situated, referential,
or grounded. The antonymy outlier is a maximally clean instance of a Harris-shaped success: it shows
the form-internal contrast measure doing exactly what it does, and it carries none of the further
reach. A relation recovered *because* it is maximally written into the form is the last place to read
a recovery as evidence of competence beyond the form.

## The sharpest point: cross-method convergence does not screen off the distributional cause

The most tempting misreading is that two *different* methods agreeing — behavioral relatum-production
(Cao) and internal-representation probing (Diera & Scherp) — makes the antonymy result *more* than a
distributional artifact: surely two independent witnesses pointing at the same relation triangulate a
real underlying competence. This essay's central rigor point is that **the convergence does the
opposite — it supports the deflationary reading.**

[`essay/cross-level-convergence-ladder`](cross-level-convergence-ladder.md) imports, from the
philosophy of common-cause inference, the **screening-off** condition: agreement between two
measurements is evidence for a *shared cause* only if the measurements are conditionally independent
given that cause — only if the cause "screens" one off from the other, rather than the two co-varying
through a shared route. The ladder's whole R1→R2 step is built to enforce this: agreement under two
instruments that are *confounded with a common factor* "could flow through the shared method rather
than a shared cause," and you have to *equalize* or remove the shared route before agreement counts.

Apply that condition here — and note carefully that this is **not a move the convergence ladder makes**.
The ladder is written for cross-*level* pattern claims; this is a cross-*method* case (two probes of
*one* relation), so what follows is an *application of the ladder's screening-off concept*, not a claim
the ladder asserts. With that flagged, the application is clean and decisive in the deflationary
direction:

- A behavioral relatum-production probe and a representational probe are **both downstream of the same
  training-time co-occurrence structure.** The behavioral probe reads off what the model *produces*
  when completing a relation prompt; the representational probe reads off what is *encoded* in the
  activations. Both quantities were *fixed by the same training distribution* — the contrastive-frame
  co-occurrence that makes antonymy distributionally salient.
- So the shared distributional ancestor does **not** screen the two methods off from each other. They
  are not conditionally independent given "genuine relational competence"; they **co-vary through the
  shared distributional cause.** The behavioral antonymy-soundness and the representational
  antonymy-easiness are two readings of one upstream fact (antonymy is the most contrastively-framed
  relation in the corpus), not two independent witnesses to a competence over and above it.
- Therefore the cross-method agreement **raises the prior on the distributional-shadow reading rather
  than rebutting it.** It is exactly the kind of convergence the screening-off condition warns against
  treating as triangulation: two methods that share an uncontrolled common cause will agree *because*
  of that cause, and their agreement is evidence *for* the common cause, not against its sufficiency.

This is the essay's strongest claim, and it is a *deflationary* one: the very fact that makes the
antonymy result look robust across methods is the fact that makes it least able to discriminate
competence from distribution.

## The antonym/synonym distributional paradox — and why it strengthens, not weakens, the thesis

There is a well-known wrinkle that must be handled honestly, because at first glance it looks like a
counterexample. Antonyms and synonyms have notoriously *similar* overall distributions: both
substitute into similar frames (*hot* and *cold* both fill "the X water"; so do *hot* and *warm*),
which is precisely why *telling antonymy apart from synonymy* is hard. Both sources register this from
their opposite ends. Cao et al. introduce a dedicated metric for exactly this difficulty —
"**Distinguishability evaluates agents' ability to distinguish relations from each other**"
([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md),
§5) — and Diera & Scherp find the mirror image at the representational level: **synonymy hardest**
([`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md),
Abstract).

The resolution is to keep two things apart that the word "antonymy" runs together:

1. **Relatum production / recovery** — *given* a cue and the relation "antonym", produce or encode an
   appropriate opposite. This is strongly contrastive-frame-cued: the corpus is full of "X and its
   opposite Y" patterns, so the antonym of a cue is a near-deterministic frame completion. This is the
   axis on which **antonymy is easy**.
2. **Antonym-vs-synonym discrimination** — *given* a pair, decide whether it is an opposite or a
   near-equivalent. This is exactly what the shared distribution *fails* to disambiguate, because
   antonyms and synonyms occupy the same frames. This is the axis on which **synonymy is hard** and
   distinguishability is a problem.

The essay's thesis is about axis (1), not axis (2). And the paradox, once split this way, **strengthens
the thesis rather than threatening it**: it is *the same distributional fact* — the dense
contrastive-frame co-occurrence of antonym pairs — that makes antonym *production* easy and antonym-vs-
synonym *discrimination* hard. A relation whose distributional trace is strong enough to drive its
relatum-production almost deterministically is, for the very same reason, a relation whose distributional
trace cannot by itself separate "opposite" from "near-equivalent." Both halves of the pattern are
distributional-shadow effects of one cause. That the two papers find easy production *and* hard
discrimination is not two facts but one, read from two sides — which is precisely what the deflationary
reading predicts.

## The honest counter

The deflationary reading is **consistent with** the convergence; it is not *proven* by it, and the
essay does not claim it is.

- **An over-and-above component could still exist.** Nothing in either paper isolates the residual.
  Neither Cao's relatum-production probe nor Diera & Scherp's probing/patching run includes a
  *contrastive-frame distributional control* — a baseline that supplies the antonym-cuing frame
  statistics without any relational competence — against which antonymy competence would have to clear
  daylight. So neither paper has measured the over-and-above residual to zero; they have shown antonymy
  is the relation recovered best, which is what the shadow predicts but does not *establish* as the
  whole story.
- **The project cannot run the discriminating control on its own panel.** Both papers test
  older/smaller models — BERT/RoBERTa/Llama-3 (Cao); Pythia-70M/GPT-2/Llama-3.1-8B (Diera & Scherp) —
  not the frontier decoders in the project's panel, and the project's own panel probe for this is
  **blocked** (see the conjecture below). So the project cannot, today, run the contrastive-frame
  control that would separate antonymy competence from its distributional shadow on its own models.

What the essay claims, then, is bounded: the convergent antonymy-outlier is **predicted by** the
distributional-shadow null, is **consistent with** the pure-shadow reading, and **raises the prior**
on it — sharply, because the cross-method agreement is itself a screening-off-failure that points at
the shared distributional cause. It does **not** claim to have measured the residual to zero, nor that
antonymy involves *no* competence over and above distribution. It claims only that antonymy is the
relation where the shadow is largest and the deflationary null hardest to reject, and that the
much-cited convergence is reason to *raise* the prior on deflation, not to lower it.

## The testable bet

The discriminating control the two papers lack is a probe this project could in principle run on its
own panel, and the bet is registered as
[`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md):
that, on the project's panel, antonymy is the relation where relatum competence is **least separable**
from a contrastive-frame distributional control — i.e. where adding such a control most fully erases
the apparent competence, relative to the other lexical relations. This essay supplies the *reading*;
the conjecture states the *bet* and (when unblocked) names the probe that would test it. A panel
relatum probe with a contrastive-frame control that showed antonymy competence *surviving* would be
the clean falsifier of the pure-shadow reading.

## What this essay is not

- **Not a human comparison.** The essay makes no claim about how the project's panel — or any model —
  compares to humans. It cites Cao's human-vs-model gap (the "significant knowledge gap … for all
  semantic relations", with antonymy the positive outlier *within* that gap) as a **cited fact from
  prior-art at Cao's stated strength** — on Cao's older/smaller models — and nothing stronger. The
  `human-comparison` tag is carried only because that cited gap is structural to the argument (antonymy
  is the positive outlier *inside* a human-subceiling picture); the essay imports no human result of
  its own.
- **Not a claim about the project's panel.** Both empirical inputs are prior-art on non-panel models;
  no transfer to claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash is asserted or implied. The panel
  bet lives in the conjecture, marked blocked.
- **Not a claim that antonymy involves no over-and-above component.** The essay claims only that the
  distributional shadow is *largest* there, that the residual is therefore *smallest* and hardest to
  detect, and that the cross-method convergence *raises the prior* on the deflationary reading. An
  over-and-above component may exist; neither paper isolates it, and the essay does not deny it.
- **The contrastive-frame claim now rests on a primary corpus source, read at its stated scope.** As
  of session 148 the claim that antonym pairs recur in tight contrastive frames is anchored to
  [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
  (Justeson & Katz 1991), a primary Brown-Corpus study of **predicative adjectives** whose purpose was
  a psycholinguistic *acquisition* theory, not an LLM result. The essay uses it only for the corpus
  fact (above-chance co-occurrence in parallel/conjoined/repeated-substituted frames); the *deflationary
  reading* of what that fact implies for models remains the essay's own argument, not J&K's. The
  extension from adjectival to nominal antonymy, and the read-forward to a model's training
  distribution, are the essay's plausible interpretive moves, flagged as such — not J&K measurements.
- **Not a cross-level convergence claim.** The convergence-ladder logic is *applied* here to a
  cross-*method* case as a screening-off argument; the ladder itself is about cross-*level* claims and
  makes no assertion about this case (see the explicit flag in the screening-off section).

## Revision triggers (read before citing)

- **(a) A frontier-panel relatum probe with a contrastive-frame control shows antonymy competence
  surviving the control.** This is the clean falsifier. If
  [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)'s
  probe (or any equivalent) runs and antonymy competence clears daylight above a contrastive-frame
  distributional baseline, the pure-shadow reading is wrong for that case — revise the deflationary
  reading to "shadow plus a measured residual," scoped to the panel tested. *Interpretation caveat
  (companion essay, s150):* [`essay/shortcut-vs-competence-mis-cut`](shortcut-vs-competence-mis-cut.md)
  argues this "surviving residual ⇒ over-and-above distribution" gloss over-reads a co-occurrence
  control — a residual over such a control grades *local* versus **transferable** distributional
  generalization (still distributional), so a survivor falsifies *local*-shadow-saturation but does
  not establish competence beyond distribution. A relabeling flagged for cross-session ratification
  ([`PROJECT.md`](../../../PROJECT.md) §12.3), not yet applied to this trigger's wording.
- **(b) A method genuinely independent of the training distribution agrees on the antonymy outlier.**
  The screening-off argument turns on both Cao's and Diera & Scherp's methods being downstream of the
  same training-time co-occurrence. If a method that is *not* downstream of that distribution (a clean
  causal/interventional manipulation; a controlled-corpus training study) independently recovered the
  antonymy outlier, the convergence would no longer be a screening-off failure and the deflationary
  weight of the convergence argument would have to be re-stated.
- **(c) The in-repo sources are re-read at greater strength and the antonymy ordering changes.** Both
  source pages flag version/locator caveats (Cao: v1-vs-v5 divergence, section-level locators; Diera &
  Scherp: HTML section locators, camera-ready not consulted). If a closer reading overturns "antonymy
  best / synonymy hardest", the empirical premise of the essay changes and the reading must be revised.
- **(d) A primary antonymy-distribution literature is ingested that bears on the contrastive-frame
  claim. — FIRED twice (s148, s149), both confirming.**
  *Session 148:* [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
  was catalogued and *confirms* the characterization, which now carries a primary corpus anchor rather
  than resting on Harris alone; the substitutability phrasing was sharpened to match J&K's
  *within-co-occurrence* (not free) substitution.
  *Session 149:* the further primary source the trigger was left live for —
  [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md)
  (Cao, Yamada & Tokunaga 2025, COCA) — was catalogued. It *confirms* the adjectival→nominal
  extrapolation on the **co-occurrence-strength leg** (antonym co-occurrence is distinctive across
  nouns/verbs/adverbs, not only adjectives) and adds the **cross-relation** measurement that antonymy
  is the *distinctively most* co-occurrence-dense relation; the thesis paragraph and Honesty box were
  updated. It does **not** complicate the reading; it leaves one **narrower residual still inferential**
  (the *parallel-contrastive-frame* mechanism for nouns — measured by J&K for adjectives, only
  *speculated* by Cao et al. for other PoS). The trigger now stays live only for a source that would
  *genuinely complicate*: a construction-type corpus study showing nominal (or some-class) antonym
  co-occurrences are **not** concentrated in parallel/contrastive frames (Cao et al. did not measure
  construction type), or any primary source overturning antonymy's cross-relation co-occurrence
  distinctiveness — either would force a revision of the now-better-grounded extrapolation.

## Honesty box

- The essay's **original** contribution is the **reading**: (i) that the convergent antonymy-outlier
  is what the distributional-shadow null predicts because antonymy is the relation most fully written
  into contrastive-frame co-occurrence and hence maximally Harris-recoverable; (ii) the screening-off
  argument that the *cross-method* convergence (behavioral + representational) **supports** the
  deflationary reading because both methods are downstream of the same training distribution and so do
  not screen off the shared cause; and (iii) the production-vs-discrimination split that makes the
  antonym/synonym distributional paradox *strengthen* rather than threaten the thesis. The
  screening-off concept is borrowed, with an explicit "not a claim the ladder makes" flag, from
  [`essay/cross-level-convergence-ladder`](cross-level-convergence-ladder.md); the Harris-recoverable
  sorting is borrowed from [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md);
  the beat-the-shadow frame is from
  [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md).
- **No empirical claim here is new, original, or reported.** The empirical facts leaned on are all
  cited at their source pages' stated strength: from
  [`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md)
  — "Antonymy is the outlier relation where all models perform reasonably well" (Abstract); "All models
  perform relatively well for antonymy, where the best model Llama-8B (L1) achieves 𝒮=0.57, whereas for
  other relations, best values typically lie around 𝒮=0.30" (§8); "The results reveal a significant
  knowledge gap between humans and models for all semantic relations" (Abstract); "Distinguishability
  evaluates agents' ability to distinguish relations from each other" (§5). From
  [`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md)
  — "Difficulty is consistent across models (antonymy easiest, synonymy hardest)" (Abstract); "a
  consistent difficulty ordering across models, with antonymy easiest, followed by hyponymy, then
  hypernymy, and synonymy hardest … antonymy approaches ceiling on Llama" (§4.1). From
  [`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md)
  — "difference of meaning correlates with difference of distribution" (p. 156). From
  [`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)
  — "antonymous adjectives do co-occur within the same sentence much more often than is expected by
  chance" (p. 3); "we find a strong trend for the antonyms to occur in syntactically parallel and
  usually lexically identical structures" (§3, p. 11); "antonyms co-occur sententially mainly by
  substituting for one another in otherwise identical or near-identical phrases" (p. 13) — a 1991
  Brown-Corpus study of predicative adjectives, **not** an LLM result. From
  [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md)
  — "We find that antonymy is distinctive in three respects: antonym pairs co-occur with high strength,
  in a preferred linear order, and within short spans" (Abstract); "antonymy is consistently distinctive
  from all other relations across all metrics used" (§6); and the construction caveat, "We … can not
  answer in which lexical and dependency constructions two words are likely to occur" (Limitations) — a
  2025 COCA corpus study at lemma+PoS level, **not** an LLM result and **not** a construction-type
  measurement. All on older/smaller/non-panel models or pre-LLM/corpus work.
- The strongest thing the essay asserts is that the convergent antonymy-outlier **is predicted by, is
  consistent with, and raises the prior on** the distributional-shadow null — and that the cross-method
  convergence supports rather than rebuts it. It explicitly does **not** assert the residual is zero, a
  panel result, a human comparison of its own, or that antonymy involves no competence over and above
  distribution. Nothing here outruns that.
