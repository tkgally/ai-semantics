---
type: essay
id: mechanistic-behavioral-firewall
title: The mechanistic–behavioral firewall — why verbalizable-representation findings and distributional-shadow findings are mutually non-entailing about lexical and grammatical meaning
meaning-senses:
  - model-internal
  - distributional
  - inferential
  - measurement-epistemic
status: draft
contingent-on: []
created: 2026-07-10
updated: 2026-07-10
links:
  - rel: depends-on
    target: source/gurnee-2026-verbalizable-workspace
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: claim/output-channel-working-surface
  - rel: depends-on
    target: essay/output-channel-confound
  - rel: depends-on
    target: open-question/verbalizable-workspace-and-llm-meaning
  - rel: depends-on
    target: theory/situating-llm-meaning-v2
  - rel: supports
    target: essay/reference-as-premise-bound
  - rel: supports
    target: essay/undischargeable-negative
---

# Essay: the mechanistic–behavioral firewall

> **Status: draft (2026-07-10). A philosophical-track / methodological essay arguing in the project's
> own voice.** Its contribution is to **name and defend a positive epistemological thesis** the project
> has so far practised only as caution. The project already treats interpretability evidence as *a
> bearing, never an import* ([`open-question/verbalizable-workspace-and-llm-meaning`](../open-questions/verbalizable-workspace-and-llm-meaning.md)).
> This essay argues that reticence is not timidity but a **structural claim about constructs**: a
> behavioral **distributional-shadow** finding (a claim about what a model *does* against a
> human-anchored contrast) and a mechanistic **verbalizable-representation** finding (a claim about a
> model-internal representational object surfaced by an approximate method) stand in a relation of
> **mutual non-entailment** with respect to claims about **lexical and grammatical meaning**, because
> they operationalize **different constructs**. It is a **firewall, not a hierarchy** — and the
> non-entailment runs in **both** directions: a mechanistic "concept" vector does not beat a behavioral
> distributional shadow, and a behavioral null does not refute an internal representation. The essay
> introduces **no new empirical claim** and makes **no human comparison**; the paper it reads is
> **first-party, non-peer-reviewed, and not a human anchor**, and its "conscious access" framing is
> **not imported** — this project's subject is meaning, not consciousness. Read "What this essay does
> not claim" and the revision triggers before citing.

## The occasion

At the project owner's standing-override request, a 2026 Anthropic interpretability paper was
catalogued: [`source/gurnee-2026-verbalizable-workspace`](../../base/sources/gurnee-2026-verbalizable-workspace.md)
(Gurnee et al. 2026, *Verbalizable Representations Form a Global Workspace in Language Models*). It
reports a privileged, causally-load-bearing subset of a frontier model's internal representations —
the "J-space" — surfaced by a new "Jacobian lens," and characterizes it by five workspace-like
properties. The scoping page that received it,
[`open-question/verbalizable-workspace-and-llm-meaning`](../open-questions/verbalizable-workspace-and-llm-meaning.md),
records that the **most likely first move, if any, is philosophical** — "an essay weighing the
mechanistic-vs-behavioral relationship on one of topics 1–3." This is that essay. It does not restate
the open question; it argues a position the open question leaves under a provisional default ("orthogonal
until an essay argues otherwise").

The project has done this before, and its practice is already a firewall. Every interpretability ingest
in the repo is filed as *a map / representational counterpoint, NOT a human anchor and NOT behavioral
evidence about the project's findings*: so with [`source/beckmann-queloz-2025-mechanistic-indicators`](../../base/sources/beckmann-queloz-2025-mechanistic-indicators.md),
whose warrant "is mechanistic (internal features, circuits), and the project's deflationary-page
argument turns on a *behavioral* in-principle gap … Their MI evidence does not, on this project's own
terms, *close* that gap — it changes the *kind* of evidence in play," and so with
[`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md),
catalogued as an "interpretability-side counterpoint … **not** as evidence about the project's
behavioral findings." The discipline is settled at the level of individual sources. What has not been
stated is *why* it holds in general — whether it is a prudential firewall the project could in principle
lower once the interpretability evidence gets good enough, or a **constitutive** one that no quality of
mechanistic result could dissolve. This essay argues the latter, and derives the reading discipline the
Gurnee paper specifically owes.

## The firewall, stated as a positive thesis

The claim is not "interpretability evidence is unreliable" (the project takes no stand on the J-lens's
internal validity), nor "the project should ignore it" (it is a valuable map of the model-internal
locus). The claim is about **what two findings can license about each other**, and it has a precise
shape borrowed from measurement theory: two indicators bear on the same *thing* only if they
operationalize the same *construct*, and these two do not.

- A **behavioral distributional-shadow finding** operationalizes: *does a model's graded behavior on a
  construction track a meaning gradient over and above a matched co-occurrence control, against a
  human-anchored contrast?* Its unit is an **observed output** on frozen stimuli; its yardstick is a
  **human resource** or a **within-model matched control**; its verb is *does*. The project's flagship
  cases are exactly this: sense gradience surviving a topic-similarity partial, the comparative
  correlative isolated to the construction by a ≈87 pp gap over same-word controls
  ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), "What the
  project's findings say about the distributional null").
- A **verbalizable-representation finding** operationalizes: *is there a model-internal vector, surfaced
  by an approximate method on one model family, that is available for report, modulation, and internal
  reasoning?* Its unit is a **representational object**; its yardstick is an **intervention on model
  internals** (swap, ablate, inject); its verb is *is present*. Gurnee et al.'s content characterization
  is that these vectors "consist of a small, evolving set of unspoken words, neither pure echoes of the
  input nor predictions of the next token, naming the concepts the model is currently reasoning with"
  ([`source/gurnee-2026-verbalizable-workspace`](../../base/sources/gurnee-2026-verbalizable-workspace.md),
  Introduction).

These are different questions with different units, yardsticks, and verbs. Neither is a measurement of
the other's construct. So the entailments the two most tempt one to draw are **both blocked**, and the
symmetry is the heart of the thesis:

- **The forward smuggle** — "the paper shows the model *really has* concepts, therefore the
  distributional shadow is *beaten*" — is blocked. A verbalizable internal vector is not a behavioral
  residual over a matched control; establishing the former settles nothing about the latter, because the
  distributional-shadow question is a question about *behavior against a control*, which no intervention
  on internals answers. (And the project's own reading of a beaten shadow is already deflationary: per
  [`essay/output-channel-confound`](output-channel-confound.md)'s sibling discipline in
  [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), "beating the
  shadow" is graded *inside* form-internal distribution, not against a world-relation — so even a
  behavioral residual does not license "genuine concept," let alone a mechanistic vector standing in
  for one.)
- **The reverse smuggle** — "the behavioral probe found a null, therefore the internal representation is
  *absent*" — is blocked too, and this direction matters just as much. A behavioral effect-null under a
  frozen instrument is, per [`essay/undischargeable-negative`](undischargeable-negative.md), "direction
  and absence-of-large-effect," never "M cannot" and never "the representation is not there." An
  internal vector could be present and behaviorally silent under the instrument tried; a behavioral null
  cannot reach in and refute it.

Mutual non-entailment is the conjunction of these two blocks. It is *positive* because it does more than
counsel caution: it tells you the two findings are answering **different questions**, so their apparent
agreement or disagreement about "meaning" is, until a bridge is built (see the revision triggers), an
artifact of running two constructs together, not evidence about either. The firewall is the honest
default; a bridge is a thing one would have to *earn*.

## Topic 1: the distributional-vs-inferential seam, from the inside and from the outside

The seam the project cares about most is the one between
[`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) and
[`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md): is a model's success
co-occurrence structure, or does it also track inferential role? The Gurnee paper's content claim reads,
at first, like a representational-side verdict on exactly this: the workspace vectors are "neither pure
echoes of the input nor predictions of the next token" — that is, on its face, a layer of content
*beyond* next-token surface statistics, the inside-the-model companion to the project's behavioral
question of whether a meaning gradient beats a matched co-occurrence control.

The firewall says: it is a companion, not a settler. Set the two objects side by side.

- The project's object is a **behavioral residual over a named control** — e.g. lexical sense gradience
  that "survives partialling out the model's own topic-similarity rating" — a claim about what the model
  *does* on frozen items, scored against a human gradient. It is silent about *how* the model does it;
  the project has "no mechanistic access" and says so on every relevant page.
- Gurnee et al.'s object is a **model-internal vector** surfaced by "an imperfect tool, which we believe
  only approximately and incompletely captures the model’s underlying workspace structure" and which
  "only identifies vectors associated with concepts that correspond to single tokens"
  ([`source/gurnee-2026-verbalizable-workspace`](../../base/sources/gurnee-2026-verbalizable-workspace.md),
  What it cannot ground). It is silent about whether that vector *earns its keep behaviorally against a
  distributional control* — the paper runs no matched co-occurrence control and no human-gradient
  contrast, because that is not its question.

So neither settles the seam the other probes. A verbalizable "concept" vector that is "neither pure
echoes … nor predictions of the next token" is a claim about the *provenance and causal role of an
internal representation*; it does not show that the model's behavior beats a co-occurrence control,
because a representation with that description could still produce behavior a matched-control account
fully reconstructs. And conversely — the direction the project must guard just as hard — a behavioral
finding that a residual *does* beat the shadow does not tell you a verbalizable vector is what carries
it, and a behavioral finding that a residual *does not* survive its control (a shadow-saturated corner,
in the vocabulary of [`essay/shadow-depth-cross-cuts-grain`](shadow-depth-cross-cuts-grain.md)) does not
show the internal vector is absent. The two live on opposite sides of the inside/outside line, and the
line is the firewall. The paper's phrase is a genuinely interesting *representational-side statement
about the seam*; it is not a *behavioral verdict on it*, and reading it as one would be to let a
mechanistic description do a distributional control's job.

One further guard belongs here, because the paper's vocabulary invites a second, quieter smuggle. Its
"concepts the model is currently reasoning with" are **model-internal representations** — the sense
tagged `model-internal` in this project — and are at most `referential.sense`-adjacent. They are **not**
the reference-bearing concepts of the philosopher, and the paper makes no reference or world-grounding
claim. So the paper cannot be cited as bearing on the referential locus of the project's map
([`theory/situating-llm-meaning-v2`](../theory/situating-llm-meaning-v2.md)), which stays silent for
reasons [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) makes structural. "Concept"
here is a representational object, not a word-to-world relation; the firewall keeps the paper's noun
from importing a claim the paper does not make.

## Topic 2: representational corroboration of a premise buys motivation, not a verdict

The paper's **Internal reasoning** property is the place the firewall is most tempting to breach in the
project's *favour*, and so the place to be most careful. That property states that "Workspace vectors
can be used to represent the value of intermediate computations, when the model chains inferential steps
or composes plans, and intervening on them is sufficient to redirect the conclusion"
([`source/gurnee-2026-verbalizable-workspace`](../../base/sources/gurnee-2026-verbalizable-workspace.md),
the five workspace properties). This is a mechanistic picture of precisely the serial computation the
project's own methodological claim argues can proceed *beneath a forced output channel* — the premise of
[`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md) and
[`essay/output-channel-confound`](output-channel-confound.md) — the claim's finding that "a forced
single-token output channel masked a serial-inference capability" which "a format-only working surface …
flipped."

Say precisely what this corroboration buys. The output-channel line rests on a **premise** — that
current models perform multi-step, serial computation that a one-token channel can deny a surface to —
which the project has grounded in behavior (the flip) and in an idealized theory-of-computation result
([`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md)) that establishes the mechanism's
*plausibility*, "not the panel's internals." The Gurnee property is a **third, representational-side
corroboration of that same premise**: serial intermediate computation, now exhibited as intervenable
internal vectors rather than as a behavioral flip or a complexity theorem. That the source page already
carries a front-matter `supports` link to the claim is exactly this and no more. It **strengthens the
motivation** for treating the output channel as a mandatory control — three independent kinds of evidence
now point at the same premise — which is a real gain for a control the essay argues "should be tried
first, not fifth."

But corroboration-of-premise **discharges no behavioral verdict**, and the reasons are the firewall's.
First, the claim is **method-scoped and human-anchored to CxNLI** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)),
not to a mechanism: its supported content is a within-item format contrast and a let-alone lift to a
human baseline, and a mechanistic picture of serial computation cannot move a single one of those
numbers, which are facts about behavior on frozen items. Second, the paper's flagship model is Claude
Sonnet 4.5, "by a novel and self-described-imperfect method," and "nothing here licenses a behavioral
prediction on" the project's panel — the Internal-reasoning property is not even *about* the same
models. Third, and most important for the firewall's symmetry: were the paper's evidence to have come out
the *other* way — no intervenable serial-computation vectors found — that would **not** have refuted the
output-channel claim either, because the claim is established behaviorally and a mechanistic non-finding
is an undischargeable negative about internals (the [`essay/undischargeable-negative`](undischargeable-negative.md)
asymmetry, applied across the method boundary). A premise can be corroborated from three sides and the
verdict it motivates still rests entirely on the one side that measured behavior against a human anchor.
That is what a firewall between corroboration and verdict looks like: the motivation crosses; the
warrant does not.

## Topic 3: a mechanistic correlate for "verbal report" relocates the skepticism, it does not soften it

The paper's **Verbal report** property is that "When the model is asked what it is thinking about, it
names concepts represented in the workspace. Swapping one active workspace vector for another changes
its answer to match" — a mechanistic operationalization of a model naming its own internal contents,
with an intervention (the swap) that ties the report to the representation. The project's behavioral
method deliberately does **not** use self-report as evidence: its constitutive-silence disciplines
([`essay/undischargeable-negative`](undischargeable-negative.md),
[`essay/reference-as-premise-bound`](reference-as-premise-bound.md)) treat a model's own account of what
it is doing as behavior to be probed, never as a window that settles anything. Does a *claimed mechanistic
correlate* for self-report soften that skepticism?

It **relocates** it; it does not soften it. Grant, arguendo and without endorsing it, that the swap-changes-the-answer
result gives verbal report a mechanistic handle the project's black-box method lacks. Two things still
hold, and they are the firewall again. First, **a behavioral project cannot use the mechanism.** The
correlate lives on the far side of the inside/outside line; the project has no J-lens, runs no swaps,
and imports no interpretability result into its evidence base. A self-report the project would treat
skeptically on a frozen behavioral instrument remains exactly as skeptically-treated, because the thing
that would allegedly license trusting it is a measurement the project does not and will not make. The
skepticism moves from "we have no reason to trust the report" to "the reason that might exist lives
somewhere our method cannot reach" — a relocation, not a discharge.

Second, and this is where topic 3 is genuinely interesting rather than merely defensive: the relocation
tells you **what the two methods can and cannot say to each other**. They cannot *transfer verdicts* —
the firewall. But they can *pose each other questions*. The behavioral side can ask the mechanistic
side: is the "workspace" content that the swap surfaces the same content a behavioral probe would elicit
by asking, and where do they come apart? The mechanistic side can ask the behavioral side: on which
constructions does report-behavior track a human contrast, so that a swap-intervention has a behavioral
target worth predicting? Neither question is answered by importing the other's result; each is a
well-posed research question *because* the constructs are distinct. A firewall that let verdicts through
would collapse these into one muddled construct; a firewall that lets *questions* through is how two
methods stay honest neighbours. The paper does not soften the project's self-report skepticism — but it
sharpens the account of where that skepticism's escape hatch would have to be built, and it is not a
hatch a behavioral instrument can install.

## What this essay does not claim

- **Not that the J-lens is valid, or invalid.** The project takes no position on the paper's internal
  validity. The paper's authors call the method "an imperfect tool" that "only approximately and
  incompletely captures" the workspace and "only identifies vectors associated with concepts that
  correspond to single tokens"; the firewall does not depend on the method being good or bad, only on
  its measuring a *different construct*. A perfectly valid J-lens would still not settle a
  distributional-shadow question.
- **Not a consciousness claim, in either direction.** The paper's "conscious access" framing is
  explicitly bracketed by its authors — "we do not claim that language models reproduce the full
  architecture global workspace theory ascribes to the brain—specialized, encapsulated processors
  competing for entry to a workspace that broadcasts back to them through recurrent connections" — and
  its philosophical implications are flagged "unclear and likely controversial." This project's subject
  is lexical and grammatical **meaning**, not consciousness; the analogy is **not imported** as a meaning
  claim, and this essay makes no use of it.
- **Not that the paper is a human anchor.** It carries "no human-judgment resource"; it is first-party,
  non-peer-reviewed, on Anthropic's own model, and "must not be cited as" a human anchor "nor as
  behavioral evidence for or against any project result." Nothing in this essay anchors any claim to it.
- **Not evidence for or against any project finding.** The essay's entire point is that the paper
  neither confirms nor refutes the shadow-beater results, the output-channel claim, the grounding nulls,
  or the relational nulls. It corroborates *one premise* (topic 2) and discharges no verdict.
- **Not that "concept" (the paper's noun) is the philosopher's concept.** It is a `model-internal`
  representational object, at most `referential.sense`-adjacent, making no reference or world-grounding
  claim.
- **Not a human comparison, and not a new empirical result.** Every empirical assertion cites the in-repo
  page that carries it, at that page's stated strength; the essay's own contribution is a **structural
  diagnosis** of a construct relation, not a measurement.

## Revision triggers (read before citing)

- **(a) A bridging law — the firewall becomes a bridge for one construction (the essay's falsifiable
  bet).** The mutual-non-entailment thesis makes a scorable prediction: it forbids a tight,
  construction-specific link between the two constructs. **The bet:** *if a published study exhibits, for
  a single lexical or grammatical construction, a behavioral distributional-shadow residual whose
  per-item sign and rank are predicted out-of-sample by the magnitude of a mechanistic J-space (or
  equivalent verbalizable-representation) intervention on that same construction in a shared model —
  cross-validated, at a pre-registered threshold such as rank correlation ρ ≳ 0.5 or a monotone
  dose-response — then for that construction the two methods are answering, at least partly, the same
  question, and the firewall is downgraded to a **bridge**.* Such a result would **weaken** the thesis
  (one construct-pair partially fused) without retiring it, and the essay would be revised to carry the
  bridge as a scoped exception and to say what makes that construction special. Absent such a law, the
  firewall is the default. (Note the bet's asymmetry with the guard rails: a bridge must be *earned* by a
  demonstrated cross-method prediction; mere co-direction — both methods "find something" on the same
  construction — does **not** fire it, because co-direction is exactly what running two constructs
  together manufactures.)
- **(b) Retraction — a *systematic* bridging law across constructions.** If a bridging law of the kind in
  (a) were shown to hold **generally** — behavioral residuals reliably predictable from
  verbalizable-representation interventions across a *range* of lexical and grammatical constructions,
  not one — then mutual non-entailment fails systematically: the two indicators would be measuring one
  construct after all, the relation would have been a **hierarchy, not a firewall**, and this essay is
  **retracted** (kept visible, per the corpus convention, with the retraction dated and the superseding
  reading named). This is the essay's genuine falsification condition, distinct from the one-construction
  weakening in (a).
- **(c) A construct redefinition on either side.** If the project were to redefine its behavioral
  distributional-shadow construct to *include* a mechanistic component (importing interpretability
  evidence into its evidence base), or if the interpretability field converged on defining
  "verbalizable representation" *behaviorally*, the two constructs would no longer be disjoint by
  construction and the firewall's premise would need restating. This would not falsify the thesis so much
  as change the objects it is about; the essay would be re-scoped to whatever residue stayed distinct.
- **(d) The paper is peer-reviewed, replicated, or independently reproduced on other model families.**
  None of these would move the firewall (the thesis is about constructs, not the paper's strength), but
  each would remove a caveat the essay currently attaches to the paper's *standing*, and the source page
  should be re-pinned first (its provenance ceiling — no figure/section-number locators, no reference
  list — is recorded there).
- **(e) A fetched human resource bearing on the report/representation relation.** None is in-repo. One
  that let a *human* self-report be tested against an independent measure of internal content would, for
  the first time, let topic 3's skepticism be examined comparatively — currently forbidden by the
  no-human-comparison discipline this essay observes.

## Honesty box

- The essay's **original** contribution is to **name and defend the mechanistic–behavioral firewall as a
  positive epistemological thesis**: behavioral distributional-shadow findings and mechanistic
  verbalizable-representation findings are in **mutual non-entailment** about lexical and grammatical
  meaning because they operationalize different constructs (different units, yardsticks, and verbs), so
  neither the forward smuggle ("the model really has concepts, so the shadow is beaten") nor the reverse
  smuggle ("a behavioral null refutes an internal representation") is licensed — a firewall, not a
  hierarchy. It applies this to topics 1–3 and derives the reading discipline the Gurnee paper owes.
  **No empirical claim here is new, original, or reported.**
- **Every empirical and textual assertion cites its in-repo page.** The verbatim Gurnee quotes — the
  content characterization ("neither pure echoes of the input nor predictions of the next token, naming
  the concepts the model is currently reasoning with"), the **Internal reasoning** property ("Workspace
  vectors can be used to represent the value of intermediate computations … intervening on them is
  sufficient to redirect the conclusion"), the **Verbal report** property ("When the model is asked what
  it is thinking about, it names concepts represented in the workspace. Swapping one active workspace
  vector for another changes its answer to match"), the **Selectivity** phrase ("not involved in
  pervasive, routine processing like text parsing or grammatical fluency"), the consciousness bracket
  ("we do not claim that language models reproduce the full architecture global workspace theory ascribes
  to the brain—specialized, encapsulated processors …"; "unclear and likely controversial"), and the
  J-lens limits ("an imperfect tool, which we believe only approximately and incompletely captures the
  model’s underlying workspace structure"; "only identifies vectors associated with concepts that
  correspond to single tokens") — are all taken from
  [`source/gurnee-2026-verbalizable-workspace`](../../base/sources/gurnee-2026-verbalizable-workspace.md),
  which records that figure/section-number locators are **not** recoverable, so they are cited by named
  section/property only. The output-channel sentences are quoted from
  [`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md) (the confound is
  further developed in [`essay/output-channel-confound`](output-channel-confound.md)); the "bearing, never an import"
  discipline from [`open-question/verbalizable-workspace-and-llm-meaning`](../open-questions/verbalizable-workspace-and-llm-meaning.md)
  and the sibling firewall framings from
  [`source/beckmann-queloz-2025-mechanistic-indicators`](../../base/sources/beckmann-queloz-2025-mechanistic-indicators.md)
  and [`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md).
- **On the sense tags.** The essay carries `distributional` and `inferential` because its core is the
  seam between those two senses (topic 1), and `model-internal` because the paper's object and half the
  firewall live at that locus; `measurement-epistemic` is a legitimate **co-tag** here — not a
  substitute — because the essay's move is about *construct individuation and how the project measures*,
  and it sits alongside the apt sense tags rather than replacing them (per
  [`meaning-senses.md`](../../meaning-senses.md), "How to tag").
- **On the typed links.** It `supports` [`essay/reference-as-premise-bound`](reference-as-premise-bound.md)
  because it extends that essay's *constitutive-silence* diagnosis from the reference-premise boundary to
  the mechanistic-representation boundary — the same silence, now shown to hold across the method boundary
  too, making that essay's reading more robust rather than sharpening its content; it `supports` [`essay/undischargeable-negative`](undischargeable-negative.md)
  because its reverse-non-entailment direction (a behavioral null cannot refute an internal
  representation) is that essay's asymmetry applied across the method boundary, and reinforces its
  trigger (a) that a capacity-absence is dischargeable only off the behavioral axis.
- **The strongest thing the essay asserts** is that *no interpretability result of the Gurnee kind
  transfers a verdict to, or from, the project's behavioral findings about lexical and grammatical
  meaning* — an argued structural claim about constructs, bounded by revision triggers (a)/(b) to the
  condition that no bridging law is established. It is a **structural diagnosis, not a measurement**; it
  produces no number and overturns no result. Nothing here outruns that.
