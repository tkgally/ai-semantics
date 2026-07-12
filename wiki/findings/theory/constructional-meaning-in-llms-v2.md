---
type: theory
id: constructional-meaning-in-llms-v2
title: What would count as evidence that an LLM has internalized a construction's meaning, not only its form — second edition, restated around the promoted claims layer
meaning-senses:
  - constructional
  - functional-vs-formal
  - distributional
  - inferential
  - human-comparison
status: draft
contingent-on: []
created: 2026-07-04
updated: 2026-07-13
links:
  - rel: supersedes
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: claim/output-channel-working-surface
  - rel: depends-on
    target: claim/comparative-correlative-covariation
  - rel: depends-on
    target: claim/dative-information-structure-givenness
  - rel: depends-on
    target: claim/aann-behavioral-gradient
  - rel: depends-on
    target: claim/lexical-sense-gradience
  - rel: refines
    target: claim/formal-competence-aann-ceiling
  - rel: depends-on
    target: claim/constructional-divergent-form-generalization-gap
  - rel: depends-on
    target: claim/preference-commitment-dissociation-aann-specific
  - rel: depends-on
    target: result/comparative-correlative-covariation-powered
  - rel: depends-on
    target: result/comparative-correlative-german-v1
  - rel: depends-on
    target: result/comparative-correlative-japanese-v1
  - rel: depends-on
    target: result/dative-information-structure-powered
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
  - rel: depends-on
    target: result/scivetti-let-alone-working-surface-v1
  - rel: depends-on
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: result/function-word-modal-second-instrument
  - rel: depends-on
    target: result/cxnli-distinction-divergence-v1
  - rel: depends-on
    target: result/aann-behavioral-gradient-rep2
  - rel: depends-on
    target: result/lexical-sense-gradience-rep2
  - rel: depends-on
    target: theory/shadow-depth-table-v1
  - rel: depends-on
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: theory/relational-meaning-in-llms
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: essay/output-channel-confound
  - rel: depends-on
    target: essay/concordant-verdict-hides-spread
  - rel: depends-on
    target: essay/function-words-not-one-category
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: depends-on
    target: source/weissweiler-2023-cxg-insight
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/lyre-2024-semantic-grounding
---

# Theory (second edition): evidence for constructional meaning in LLMs

> **Update (2026-07-05, session 183 — wiki-coherence pass).** Two single-run flags this edition
> carries were discharged after it was written, one by a replication this page's own trigger
> named: **(i)** the AANN gradient's cross-date replication landed s178
> ([`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md): 408
> fresh disjoint items on the byte-frozen instrument, gradient replicates 3/3, cell ρ
> 0.692/0.702/0.735 — the "second-date AANN gradient replication" trigger below **fired**, so the
> Tier-2 section's single-run flag is dropped; the noun-class dependence and gpt's Tier-0 18/24
> wobble are carried on the claim); **(ii)** the lexical sense-gradience single-run flag was
> discharged s181 ([`result/lexical-sense-gradience-rep2`](../results/lexical-sense-gradience-rep2.md):
> replicates 3/3, pair-disjoint — direction/agreement core only). Inline "single-run" phrasings
> below are bracket-annotated where they occur; the position itself is unchanged.

## The theoretical object

This is the clean second edition of the project's first synthesis page, forced by the
theory-edition rule ([`PROTOCOL.md`](../../../PROTOCOL.md) §3): the first edition had accreted far
more than three update boxes and had become a changelog rather than a position. This edition
**supersedes** [`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md), which
is kept visible as history.

The page answers one question, sharply: **what would count as evidence that an LLM has
internalized a construction's form–meaning pairing (`constructional` sense) — as opposed to merely
its form?** It is not "do LLMs understand language" (too coarse) and not "are LLMs grounded" (a
separate axis, bracketed below). A construction, in the Construction Grammar sense the project
adopts ([`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md)), is a
form–meaning pairing at some level of abstraction; Weissweiler et al. 2023
([`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md))
states the unit directly:

> "According to CxG, meaning is encoded in abstract constellations of linguistic units of different sizes."

The difficulty — and the interest — is that form-tracking and meaning-tracking can come apart: a
fluent model can have the first without the second. The page's core instrument for keeping them
apart is the evidence ladder below, unchanged in structure from the first edition because it has
held up. What has changed is the evidence standing on it.

## History — what changed between editions

The first edition ran 2026-05-28 → 2026-06-21. It was written before any probe of the project's
own design had run, and it grew by accretion as roughly two dozen results landed. Three things now
exist that did not exist in June, and this edition is organized around them:

1. **A claims layer.** Five results lines have been promoted, by cross-session adversarial review,
   to typed `claim` pages: [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md),
   [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md),
   [`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md), (at the lexical
   grain) [`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md), and — same
   session as this edition, methodological rather than a beater —
   [`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md). The
   ladder's rungs are now occupied by claims, not only by single results. *("Four" → "Five"
   corrected s183; the fifth was promoted the session this edition was written.)*
2. **Powered magnitudes with intervals.** The A2a powered re-runs attached what the founding-N
   runs could not: the CC construction-isolation gap of ≈87 pp (136 fresh items, s169) and the
   dative's per-model shifts at N=100 (3/3 CONFIRM with a ~9× spread, s175).
3. **The flagship table.** [`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md) arranges the
   four promoted beater lines and the two saturated corners as one measured object along the
   shadow-depth axis. Cross-row detail lives there; this page keeps the ladder reading.

Everything the first edition established that still binds — the wedge, the sense discipline, the
grounding bracket, the add/cancel asymmetry, the instrument-sensitivity theme, the output-channel
discovery, the relational pointer — is restated cleanly below, at current evidence.

## The wedge: formal vs. meaning

The cut that organizes the theory is the formal-vs-functional competence distinction of Mahowald
et al. 2024 ([`source/mahowald-2024-dissociating`](../../base/sources/mahowald-2024-dissociating.md)):

> "we evaluate LLMs using a distinction between formal linguistic competence—knowledge of linguistic rules and patterns—and functional linguistic competence—understanding and using language in the world."

Formal competence is operationally getting the form right:

> "Broadly, being formally competent means getting the form of language right: knowing which strings could be valid words of a language (e.g., bnick cannot be a word in English but blick can)."

And the paper's central asymmetry:

> "Although LLMs are surprisingly good at formal competence, their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules."

The load-bearing methodological corollary: success on a structural-acceptability task is evidence
of *formal* competence and does not, by itself, warrant a conclusion about meaning-tracking.
[`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) commits the
project to this at Tier 0, and this page **refines** that claim by generalizing it: for *any*
construction, the form-acceptability result is the floor of evidence, not the proof.

Two caveats travel with the wedge. First, Mahowald's formal/functional cut is not identical to the
constructional form/meaning cut — the source page warns that its "formal semantics" overlaps with
but is not the same as `constructional` meaning ("Citing it for construction probing requires
care," per the source page's limits). The project uses formal/functional as a *frame* for sorting
evidence, not as a substitute for a construction-specific meaning theory. Second, formal/functional
is orthogonal to grounded/ungrounded (the source page: a model can be formally competent but not
grounded); conflating them is a defect this page forbids.

## What "meaning" is, on this page

The project refuses the unqualified word ([`wiki/meaning-senses.md`](../../meaning-senses.md)).
Three senses are in play and kept separate:

- **Distributional** — meaning as co-occurrence structure; the implicit theory of the next-token
  objective, and the *null hypothesis* every rung must beat: a fluent model has distributional
  structure for free. The project's operational name for this null is the **distributional
  shadow** ([`theory/shadow-depth-table-v1`](shadow-depth-table-v1.md)); a claim earns a rung only
  with a named control that strips the shadow.
- **Inferential** — meaning as inferential role: a construction means what it licenses you to
  infer. Piantadosi & Hill 2022
  ([`source/piantadosi-hill-2022-meaning-without-reference`](../../base/sources/piantadosi-hill-2022-meaning-without-reference.md))
  supply the framing under which inference-preservation counts as genuinely semantic: LLMs work
  in a way that approximates a compelling account of human cognition "in which meaning arises
  from conceptual role," where
  "conceptual role is defined by the relationships between internal representational states"
  (abstract, verbatim). The top of the ladder is inferential for exactly this reason.
- **Constructional** — the form–meaning pairing itself, the thing the probe is for.

The distributional/inferential boundary did not collapse under testing, but it turned out to be a
**gradient secured per model, not a clean line**: the sister page
[`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md) closes the founding
distributional-vs-inferential question with a worked sufficiency criterion (cross-instrument
convergence) that is currently met by one of three panel models on the AANN line. This edition
inherits that closure rather than restating it.

### The grounding bracket (unchanged, and still binding)

Two poles bound the grounding debate the project sits inside. Bender & Koller 2020
([`source/bender-koller-2020-climbing`](../../base/sources/bender-koller-2020-climbing.md)) is the
form-only denial:

> "we argue that a system trained only on form has a priori no way to learn meaning"

— where meaning is defined as "the relation M ⊆ E × I which contains pairs (e, i) of natural
language expressions e and the communicative intents i they can be used to evoke." On this
definition no text-only behavior, however systematic, counts as meaning. Lyre 2024
([`source/lyre-2024-semantic-grounding`](../../base/sources/lyre-2024-semantic-grounding.md))
supplies the framing the project adopts methodologically — grounding as graded (p. 10):

> "semantic grounding isn't a yes-no matter, but rather a matter of degree. Intelligent or cognitive agents and systems can be more or less semantically grounded"

with the verdict that LLMs are "neither stochastic parrots nor semantic zombies, but already
understand the language they generate, at least in an elementary sense" (p. 1, abstract). The page
takes the Lyre stance as method: the question is how far up the evidence ladder behavior reaches,
not whether meaning is present full stop. Bender & Koller mark the position that even the top rung
of a text-only ladder does not reach grounded communicative meaning; that position is recorded,
not refuted. The ladder is deliberately silent on grounding — that silence is the honest scope of
a text-only probe program.

## The evidence ladder — current state of each rung

Tier ordering, weakest to strongest; each rung subsumes those below, and each upward step narrows
the space of distributional-only explanations. **Form-acceptability < surprisal-contrast <
gradient semantic tracking < generalization < inference-licensing.** Only the top rungs are
evidence for constructional *meaning* rather than constructional *form*.

**Tier 0 — form-acceptability.** The model distinguishes well-formed from minimally ill-formed
instances. This is formal competence in Mahowald's exact sense, and it is the floor.
[`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) lives here
by design: an AANN acceptability ceiling, even matching human raters, is "a necessary but not
sufficient test" for meaning. In current practice Tier 0 serves as the *manipulation check* of the
graded probes (e.g. the AANN behavioral run's 23–24/24 licit-vs-degenerate gate), a precondition
rather than a finding.

**Tier 1 — surprisal-contrast sensitivity.** Graded continuation likelihoods separating licit from
illicit instantiations, net of unigram frequency. This rung's original logprob instrument was
retired unexecutable (the ratified panel exposes no token logprobs), and the project's instruments
are now prompted/behavioral throughout; Tier 1 survives as the *shadow-control discipline* inside
the higher rungs rather than as a rung probed for its own sake. Weissweiler's memorization confound
bites hardest here — minimal-pair probing "currently does not tell us anything about if the model
has identified the extent of the construction correctly"
([`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md)) —
which is why Tier 3 exists.

**Tier 2 — gradient semantic tracking.** Behavior tracks a *meaning* gradient internal to the
construction, in the human-attested direction, with the distributional shadow controlled. Two
promoted claims now occupy this rung:

- *Dative information structure* —
  [`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md).
  Across three runs on disjoint item sets, the panel shifts its double-object vs.
  prepositional-dative production preference in the human direction (given recipient → DOC, given
  theme → PD), on a within-item design whose two scored phrasings are byte-identical across the
  item's two contexts — so length/position/order shortcuts yield shift = 0 *by construction* — and
  the effect survives the end-weight dissociation control. The s175 powered re-run
  ([`result/dative-information-structure-powered`](../results/dative-information-structure-powered.md),
  100 fresh items) attaches the magnitudes: claude **+0.316 [0.298, 0.334]**, gemini **+0.524
  [0.506, 0.542]**, gpt **+0.056 [0.039, 0.074]** — **3/3 CONFIRM at power**, with the load-bearing
  qualifiers that the spread is **~9×** (stable across v1 and the powered run) and gpt's effect is
  tiny and item-noise-sensitive (63/100 items positive; it flickered WEAK at v2's founding N). The
  human anchor ([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md),
  Bresnan et al. 2007 production corpus) grounds the *direction only*, never a size.
- *AANN acceptability gradient* —
  [`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md). On a single powered,
  pre-registered run, all three models' prompted acceptability rank-tracks the human Exp-2 MTurk
  gradient at cell grain (ρ 0.68–0.75, CIs excluding 0), and the tracking survives the two
  shadow controls — a Zipf word-frequency partial (partial ρ 0.66–0.74) and a noun-class marginal
  guard. This is the rung's discipline made concrete: a Tier-2 gradient is evidence only *if*
  frequency is controlled; here it does not collapse. The claim is deliberately **single-run
  scoped** — no cross-date replication of the overall positive exists. *(Since discharged for the
  graded gradient: rep2, s178 — see the update box at the head of this page.)*

Tier 2 is where Lyre's graded framing does real work: the prediction is monotonic correspondence
with a human gradient, not a hard flip.

**Tier 3 — generalization to held-out material.** The Tier-2 effect holds for lexical items the
model is unlikely to have seen in the construction — Goldberg's productivity criterion and the
main defense against memorization. Current state, honestly scoped: the AANN class gradient
replicates on frequency-matched held-out adjectives **at the overall grain** (held-out class-cell ρ
0.75–0.83) **but noun-class-dependently — the temporal stratum is uniformly negative** at every
grain for all three models (v2b, a powered second date). "Generalizes to novel adjectives,"
unqualified, is exactly the over-read the claim refuses; read it as *object/distance yes, temporal
no*. On the CC side, the powered run's atypical-pair arm (absurd scale pairs whose covariation
direction can come only from the construction) shows no collapse (typical − atypical ≤ 5 pp), the
n-gram/memorization control at this rung.

**Tier 4 — inference-licensing.** The model treats the construction as licensing its
characteristic inference, where the inference is contributed by the construction and not by any
lexical part ([`concept/coercion`](../../base/concepts/coercion.md) is the paradigm phenomenon).
This is the strongest text-internal rung and the one that earns the `inferential` tag in
Piantadosi & Hill's sense. Current state, by line:

- *Comparative correlative* — the most robust positive, now a promoted claim
  ([`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md)).
  The panel treats *the more X, the more/less Y* as licensing the covariation inference because of
  the construction, not the scalar words: the powered re-run
  ([`result/comparative-correlative-covariation-powered`](../results/comparative-correlative-covariation-powered.md),
  136 fresh disjoint items, s169) fixes the construction-isolation assertion gap at **≈87 pp**
  (86.8 / 88.2 / 86.8; 95% CI lower bounds ≈78 pp, 3/3 models; matched same-word controls still
  assert ≈12%, so the contrast is genuinely off-ceiling). Direction-flip on inverse CCs is 97–100%;
  earlier runs showed the reading survives conflicting world knowledge, composes two-step chains
  (including negative×negative→positive), and — for 2/3 models — survives sentential negation and
  epistemic hedging. The standing cautions travel: the per-item rates are at or near ceiling, so
  the magnitude is precise but licenses no depth-of-processing verdict; the powered legs are
  `internal-contrast-only`; the single human-comparison leg (v1's 30 Scivetti CC items, answer-key
  agreement 93–100% vs the ≈0.90 native baseline) is narrow and single-run. *(Strengthened s213/s214:
  the construction-isolation contrast now replicates **cross-linguistically** — a frozen German port to
  `je…desto/umso` reproduces the isolation gap +92.6/+88.2/+88.2 pp, the inverse-flip 100/97/97%, and
  the absurd-pair robustness 95–100%, and does not track UD-German-GSD frequency/co-occurrence
  ([`result/comparative-correlative-german-v1`](../results/comparative-correlative-german-v1.md)). So the
  Tier-4 CC reading is "keyed to the construction, not the scalar words" **and** not merely
  English-`the…the`-n-gram matching — a **partial** discharge of the n-gram worry, German being a modest
  typologically-close lever. `internal-contrast-only`: no human comparison, no German-competence claim;
  the claim's formal scope stays English. Does not change the Tier-4 placement — it hardens it. **Further
  strengthened s215/s216:** the same instrument ported to **Japanese** `〜ば〜ほど`
  ([`result/comparative-correlative-japanese-v1`](../results/comparative-correlative-japanese-v1.md))
  reproduces the isolation gap +94.1/+83.8/+95.6 pp (CI lb ≥ +75), inverse-flip 100/100/97%, and
  absurd-pair robustness 100/95/95%, not tracking UD-Japanese-GSD frequency/co-occurrence — on a
  construction with **no overt comparative morpheme at all** (SOV, agglutinative; the "more" carried by the
  ば…ほど frame + predicate repetition). So the reading is not even Germanic-template matching, since it
  holds where there is no comparative word — a **stronger-but-still-partial** discharge (two non-English
  languages ≠ all; within-model; `internal-contrast-only`, no Japanese-competence claim; formal scope stays
  English).)*
- *Add-direction coercion* — caused-motion and *way* draw their construction-contributed
  entailments onto non-motion verbs at or near ceiling, and the near-miss form control
  ([`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md)) shows the
  affirmation is construction-keyed, not a "displacement happened → the verb caused it" heuristic
  (62.5–100 pp gap over content-matched non-constructional frames).
- *Cancel-direction* — suppressing a lexically-default entailment (the conative's completed
  contact) is harder and more fragile: at matched task structure, suppression-no-cue is off-ceiling
  and variable across models and instruments
  ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)). See the
  add/cancel asymmetry below.
- *AANN inferential line* — **PARTIAL**, and this scope is load-bearing. With a
  headroom-bearing distributive-default control, the construction shifts paraphrase selection
  toward the unified-stretch reading panel-wide, replicated powered on fresh held-out adjectives
  ([`result/aann-inferential-v6`](../results/aann-inferential-v6.md): Δ² +0.875 / +0.575 / +0.90,
  all CI-clear) — but the **cross-instrument convergence** (paraphrase + NLI + the grammaticalized
  agreement reflex) that the ratified operationalization treats as the sufficiency criterion for
  reading a result as inferential-specific holds **in one model only** (gpt-5.4-mini). For the
  other two, the shift is read as a paraphrase *preference*, not inference. All
  `internal-contrast-only`. The preference/commitment dissociation this produced is itself
  AANN-specific so far ([`claim/preference-commitment-dissociation-aann-specific`](../claims/preference-commitment-dissociation-aann-specific.md)).
- *Function words* — the most abstract constructional bet reached this rung
  ([`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md)): swapping a
  function word flips a 3-way NLI label vastly more often than swapping a frequency+length-matched
  content word (contrast claude +0.340 / gpt +0.825 / gemini +0.859, content-swap flips near zero), strong support
  for the constructional reading over the matched-frequency distributional null. But the load is
  **type-specific, not uniform across closed-class items** — subordinator and
  existential→universal swaps flip near-totally, the future→conditional modal was null under NLI,
  the paucal→multal quantifier split the panel — the conceptual correction of
  [`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md). A
  second instrument then relocated the modal nulls to the *instrument*
  ([`result/function-word-modal-second-instrument`](../results/function-word-modal-second-instrument.md)):
  a forced-choice modal-force probe registers `will`→`would` in all three models where NLI flipped
  0/0/3. Which swaps reach this rung is co-determined by the inferential instrument's calibration,
  not by part-of-speech class.

**The lexical grain.** The same skeleton — does a meaning gradient beat the distributional
shadow? — runs at the word grain, where the promoted
[`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md) is the lexical
shadow-beater: on 200 DWUG pairs the panel's graded sense-relatedness rating rank-tracks the human
DURel median (ρ 0.60–0.83, in/above the human inter-annotator range ≈0.69) and survives partialling
the model's own topic-similarity rating (partial ρ 0.50–0.75) — single-run, direction/agreement
scope *(single-run flag since discharged, s181 rep2 — see the update box at the head of this page)*. It bears on *this* page only as the demonstration that the shadow-beating test is not
construction-specific: the cline has a measured beater at both grains. Depth, the hard-direction
nulls (polysemy/homonymy discreteness), and the coercion bridge live on
[`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md).

## Structural findings the ladder now carries

Three cross-cutting regularities emerged from the first edition's accretion and have survived
every subsequent test. They are part of the theory's content now, not commentary.

**1. The add/cancel asymmetry.** Current decoders more readily *license* a
construction-contributed inference (caused-motion, *way*, CC — all at or near ceiling) than
*suppress* a lexically-default one (the conative's completed contact — off-ceiling, variable,
instrument-fragile, even at matched task structure, so the asymmetry is about direction, not
ceiling). Abstracted as the project's own
[`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md):
additive-easy, defeasance-hard — a signature compatible with a distributional prior. The related
disposition observed across the conflicting-cue runs — take the construction's stated content at
face value and do not override it with world knowledge — is correct where the construction asserts
(CC) and questionable where physics objects (the impossible caused-motion, which only an explicit
in-premise denial flips): a property, not a competence verdict.

**2. Instrument sensitivity, with two identified sources.** The same model can carry a
constructional inference under one elicitation and lose it under another; a single-instrument
Tier-4 reading therefore under-determines competence. The evidence separates two distinct sources:
a **model-specific** one (gpt-5.4-mini's localized logical slips — the excluded-middle
over-inference under negated CCs, the conative NLI failure) and a **general pragmatics/entailment**
one, uniform across models (NLI admits a Gricean post-hoc causal reading that strict-entailment
forced-choice withholds — [`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md);
NLI is by construction blind to non-at-issue content, which *predicted* the function-word type
pattern a priori). The collected question lives at
[`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md).

**3. The output channel is an instrument.** A forced single-token response format can mask a
capability whose computation is serial: the `let-alone` near-chance negative largely dissolved
under a working surface (step-by-step + `FINAL:` tag, format-only change) — claude 0.542 → 0.792,
gemini 0.667 → 0.917 on the same items, control preserved
([`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md)) —
so what looked like a scalar-phrasal competence boundary was substantially a channel artifact
(gpt-5.4-mini declined the offered surface — channel non-uptake; with uptake forced it lifted
partially but a below-baseline channel-controlled residual survived in five of five repeated
runs — the full line, with its boundary control, is consolidated in
[`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md)). The general discipline — every behavioral
capability-negative owes a channel control — is argued in
[`essay/output-channel-confound`](../essays/output-channel-confound.md).

A fourth discipline governs how the ladder is *read*: **concordant panel verdicts hide spread**
([`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)). The
dative is the sharpest instance: a 3/3 CONFIRM at powered N still hides a ~9× magnitude spread and
a member that flickered below detection at founding N. Panel labels are existence statements, never
uniformity statements.

## The hard direction

The positives above are concentrated in what the first edition called the **easy direction**:
an unambiguous construction's core inference, or a well-described soft constraint tracked in the
human direction. The **hard direction** — mapping the *same surface form* to a divergent
constructional meaning — remains negative:
[`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md)
records Scivetti et al.'s >40% divergent-form drop against a ≈0.90 native-speaker baseline, and the
project's own probe reproduced the gap on its panel (mean ≈39 pp base→distinction drop, 3/3 models,
[`result/cxnli-distinction-divergence-v1`](../results/cxnli-distinction-divergence-v1.md)). The
live hypothesis is unchanged from June: current decoders handle the easy direction of the upper
ladder at or near ceiling and fail the hard direction. The one apparent extension of the hard
direction — a scalar-phrasal axis — collapsed into the channel-sensitivity theme above; the
divergent-form gap did not.

## The relational axis

Every rung above is `model-internal` or `human-comparison`. The charter's distinctive second axis
— meaning constituted *between* agents — has its own synthesis page,
[`theory/relational-meaning-in-llms`](relational-meaning-in-llms.md), carrying the whole arc
(the reference-game null, the coined-term order-sensitivity positive, the composition series).
This page claims nothing on that axis; its scope is single-model constructional meaning.

## What the theory predicts and forbids

**Predicts.** For a well-described construction, genuine constructional meaning should show a
*coherent climb*: Tier-2 gradient tracking that survives frequency control, Tier-3 generalization
to held-out items, and — for inference-bearing constructions — Tier-4 inference-licensing the
lexical items cannot explain. Two amendments, both forced by evidence since the first edition:
(i) the prediction is **per-construction and per-type** — "function word" is the wrong unit; the
Tier-4 signal is type-specific, and a pooled magnitude across a class is not a capability measure;
(ii) the climb is **per-model and per-instrument** — competence can be present yet
elicitation-dependent, so a coherent climb must be checked with the instrument held fixed, and a
cross-instrument disagreement is a finding about the instrument pair, not automatically about the
model. The AANN line is the current test case: Tier 2–3 panel-wide (temporal stratum excepted),
Tier 4 convergent in one model — a *partial* climb the theory expects to either complete
(convergence spreading across the panel on some line) or stay model-specific (which would support
the thin, per-model reading of inferential role the continuum page argues).

**Forbids.** Four inferences:

- From Tier 0 to constructional meaning (the AANN-ceiling block, generalized).
- From a frequency-uncontrolled gradient (Tier 1 dressed as Tier 2) to semantic tracking.
- From any text-internal tier to grounded communicative meaning in Bender & Koller's sense, absent
  a separate grounding argument.
- From a single-instrument, single-channel negative to a competence absence — the negative owes a
  channel/instrument control first (the `let-alone` lesson).

It also forbids stating a promoted claim above its scoped strength: the dative's 3/3 is not
uniformity (~9× spread); the AANN gradient positive is single-run *(flag since discharged, s178
rep2)* and its held-out generalization
noun-class-dependent (temporal negative — never "generalizes to novel adjectives" unqualified;
this caveat stands after the replication);
the AANN Tier-4 is convergent in one model; the CC's ceiling caution travels with its ≈87 pp.

## Open tensions

1. **Distributional null vs. constructional signal.** Every rung is read against the shadow; a
   pass without a named shadow control collapses a rung downward. Managed, not solved: the matched
   controls rule out same-surface probability, not every sufficiently rich latent interpolation
   (the bounded caveat carried on each result).
2. **Inferential evidence vs. grounding.** Piantadosi & Hill would count Tier-4 as genuine
   meaning; Bender & Koller would say it is still form. The theory does not adjudicate; Tier 4 is
   the ceiling of text-internal evidence and the grounding question lies beyond it.
3. **Memorization at every tier.** Managed by Tier 3, never retired — and Tier 3 itself is now
   known to be stratum-dependent (the AANN temporal hole), so a held-out pass is scoped to its
   strata.
4. **Instrument sensitivity as a measurement-noise floor.** With two identified sources, the open
   question is whether any Tier-4 reading can be stated instrument-independently, or whether the
   honest unit is always construction × model × instrument.

## Status and revision hook

`status: draft`. `contingent-on: []` — the page introduces no new empirical claim and no new
measurement; every number above is quoted from its claim or result page at that page's stated
strength, and the four promoted claims it leans on are each `contingent-on: []` with ratified
operationalizations. The predicts/forbids section restates and amends the first edition's standing
bet; it registers no new falsifiable bet of its own.

**Revision triggers for this edition (named, per the theory-edition rule):**

- **The edition rule itself:** more than ~3 update boxes accrete here → write the third edition;
  evidence rewrites this page, it does not accrete onto it.
- **The partial climb resolves:** AANN Tier-4 cross-instrument convergence spreads beyond
  gpt-5.4-mini (or is shown model-specific on a second construction with headroom) → the
  predicts section's test case is decided and the page is rewritten around it.
- **A hard-direction positive:** any panel model closes a divergent-form gap at power → the
  easy/hard hypothesis, the page's central structural reading, needs rewriting.
- **A beater fails:** a replication pushes claude's or gemini's dative shift toward zero, or the
  CC isolation gap fails on a fresh powered set → the corresponding rung placement is withdrawn
  (the shadow-depth table names the same trigger).
- **A second-date AANN gradient replication** lands (the scoped claim's named strengthening) →
  the Tier-2 section drops its single-run flag. **→ FIRED s178**
  ([`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md));
  discharged via the s183 update box at the head of this page.

The first edition's genuinely-open triggers that this edition retires as *discharged*: the AANN
logprob blocker (resolved by the ratified behavioral instrument, run and promoted), the lexical
probe (run; folded into the continuum page), and the relational pilot (run; re-homed to its own
synthesis page).
