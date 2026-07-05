---
type: essay
id: compositionality-asymptote-not-wall
title: Compositionality is an asymptote, reference is a wall — two different ways the behavioral method falls short of its philosophical target
meaning-senses:
  - constructional
  - distributional
  - inferential
  - referential
status: draft
contingent-on: []
created: 2026-06-27
updated: 2026-07-05
links:
  - rel: depends-on
    target: source/janssen-zimmermann-montague-semantics-sep
  - rel: depends-on
    target: concept/compositionality
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: result/comparative-correlative-covariation-v2
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: refines
    target: concept/compositionality
  - rel: depends-on
    target: essay/reference-as-premise-bound
  - rel: depends-on
    target: essay/two-distributional-hypotheses
  - rel: depends-on
    target: essay/undischargeable-negative
---

# Essay: compositionality is an asymptote, reference is a wall

> **Status: draft (2026-06-27). A philosophical-track essay arguing in the project's own voice.** It introduces **no new empirical claim**: every empirical or textual assertion cites the in-repo page that carries it, and the original part is the argument — a diagnosis of *how* the project's behavioral method falls short of two of its philosophical targets, and why the two shortfalls have **different shapes**. It builds on the new (s124) Montague source [`source/janssen-zimmermann-montague-semantics-sep`](../../base/sources/janssen-zimmermann-montague-semantics-sep.md), which makes the compositionality target precise enough to state the shortfall sharply. It takes **no side** on whether LLMs "really" compose; it locates where the behavioral method can and cannot reach, and disciplines how a compositional positive may be cited.

## The position

The project owns one essay that names a place its behavioral method is **constitutively silent**: [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) shows that the in-repo dispute over whether an LLM's words *refer* is "premise-bound, not evidence-bound" — it "turns entirely on a single metasemantic premise no behavioral probe the project can run can settle," so the method is silent there and the silence is "a principled limit, not a gap more probes can close." That essay's diagnosis is about the **word-to-world** axis (`referential`).

This essay argues the **part-to-whole** axis (`constructional`/compositional) is *also* a place the method falls short of its philosophical target — Montague's homomorphism — **but in a different way, and the difference matters.** Reference is a **wall**: no behavioral probe moves the dispute at all, because the deciding fact is fixed off-board. Compositionality is an **asymptote**: every well-built generalization probe moves the question, narrowing the deflationary alternative arbitrarily far, yet none completes the last step to "the model *realizes the homomorphism*," because that is a claim about the *form of the map* and finite behavior fixes only its *graph*. The two cells of the meaning map fail the behavioral method for structurally different reasons, and the difference explains a fact about the project's own history: the compositionality program keeps buying evidence run after run, while the reference program is saturated after one round of conceptual analysis.

That contrast — wall versus asymptote, the same method failing two targets in two shapes — is the essay's original contribution.

## Montague makes the target precise

Until this session the project leaned on "compositionality" as common knowledge. The Montague survey now in-repo states the target in its sharpest form. The plain principle (SEP §1.2):

> "The meaning of a compound expression is a function of the meanings of its parts and of the way they are syntactically combined." ([`source/janssen-zimmermann-montague-semantics-sep`](../../base/sources/janssen-zimmermann-montague-semantics-sep.md), §1.2)

and its algebraic statement (SEP §3.2):

> "Syntax is an algebra, semantics is an algebra, and meaning is a homomorphism between them" ([`source/janssen-zimmermann-montague-semantics-sep`](../../base/sources/janssen-zimmermann-montague-semantics-sep.md), §3.2)

with the rule-to-rule pairing that makes it run (SEP §1.2):

> "each syntactic rule must be accompanied by a semantic rule which says how the meaning of the compound is obtained." ([`source/janssen-zimmermann-montague-semantics-sep`](../../base/sources/janssen-zimmermann-montague-semantics-sep.md), §1.2)

The load-bearing word is **homomorphism**. A homomorphism is not merely a function from wholes to meanings; it is a *structure-preserving* map: the way the parts combine syntactically is mirrored, step for step, by the way their meanings combine semantically. The derivation's structure *is* the meaning's structure. That is a far stronger claim than "the model gets composite cases right." Getting cases right is a fact about the function's **graph** — its input–output pairs. Being a homomorphism is a fact about the function's **form** — how it is computed. This gap between graph and form is where the whole essay lives.

The Montague source itself flags the project's question as open and declines to settle it. Its "What it cannot ground" section names, among what the survey cannot supply, a verdict on whether LLM behavior is "compositional" in Montague's sense, and states the residue directly:

> "whether a model's behavior realizes a homomorphism rather than a distributional shortcut is the project's own open question" ([`source/janssen-zimmermann-montague-semantics-sep`](../../base/sources/janssen-zimmermann-montague-semantics-sep.md), §"What it cannot ground"; pointing to [`concept/compositionality`](../../base/concepts/compositionality.md) §4).

This essay does not close that question. It sharpens *what kind* of open it is.

## What behavior can show: the systematicity signature

The homomorphism is too strong to read off behavior directly, but its weaker, **extensional** consequences are exactly what the project measures — and the project has measured them. The cleanest case is the comparative-correlative composition probe. [`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md) ran two-step covariation chains including a diagnostic double-negative item:

> "a model reading only one clause would answer *decrease*. All three models answer *increase* (100%) — evidence of actual two-step composition, not last-clause matching." ([`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md))

This is the *systematicity* datum the compositionality principle predicts: the value of the whole is computed from the signs of the parts under their mode of combination (negative × negative = positive), not read off the last clause. A model that ignored combination — an order-blind, sign-blind bag-of-words — would get this case *wrong*. So the result **beats the simplest distributional null**: the kind of distributional competence that tracks neighbourhood co-occurrence but is blind to how the pieces combine (the `distributional` reading whose caveat is that "by itself, distributional structure is silent on reference and on truth" — [`meaning-senses.md`](../../meaning-senses.md), §`distributional`; combination-blindness is the present essay's gloss on what the *simplest* such competence omits, not a quoted phrase). The double-negative item is built precisely to make that part-blind null fail.

The coercion results add the complementary extensional signature. [`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md) and [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md) show the panel drawing an inference *the verb cannot supply* (caused-motion affirmed 90–100 %, path-traversal 77.8–100 %, with large gaps over matched controls), which is where, in the [`concept/compositionality`](../../base/concepts/compositionality.md) §2 framing, "strict **lexical** compositionality under-predicts." Read in Montague's terms, the coerced sentence is still compositional once the construction is admitted as a *part*: its meaning is a function of (verb-meaning) combined with (construction-meaning). The behavior is consistent with a map that has the construction in its domain.

So the behavioral record reaches the homomorphism's **extensional shadow**: the model's input–output behavior on composite cases patterns as a structure-respecting map would pattern, and specifically *unlike* the simplest part-blind distributional competence. This is real evidence and it is not nothing. It is the *graph* of the function coming out homomorphism-shaped on the tested cases.

## Why it is an asymptote, not a wall

The extensional shadow is not the homomorphism. Here is the gap, stated carefully.

**Any finite probe set is consistent with infinitely many functions.** The double-negative item, the held-out coercion verbs, the minimal-pair controls — together they rule out *some* functions (the order-blind bag-of-words, the verb-only lexical map, the memorized-instance lookup). They do not rule out *all* non-homomorphic functions. A system that has internalized enough of the combinatory regularities to reproduce the tested outputs — a sufficiently rich distributional structure — agrees with a genuine homomorphism on exactly those cases while not *being* one. The [`concept/compositionality`](../../base/concepts/compositionality.md) §4 statement of the project's two defenses is explicit about the residue:

> "These narrow the distributional-only explanation; they do not eliminate it" ([`concept/compositionality`](../../base/concepts/compositionality.md), §4).

That word **narrow** is the whole point of "asymptote." Each new probe — a fresh held-out item set, a deeper composition chain, a new coercion construction — excludes a further band of non-homomorphic alternatives. The deflationary "richer distributional shortcut" is pushed into an ever-smaller corner. The project's evidence ladder ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)) is built to climb exactly this gradient: its Tier-3 generalization rung is "the project's main defense against memorization," and each rung is "harder to fake with distributional structure alone." *(Superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) — cited here as the edition this essay engaged.)* This is monotone approach. It is also genuine progress: a run is *worth doing* because it moves the question.

**But the approach never arrives, for two compounding reasons.** First, the finite-probe underdetermination above never empties: there is always a next non-homomorphic function that agrees on everything tested so far, so no finite ladder reaches "is a homomorphism" with certainty — only "has survived every distributional alternative we could build." Second, and deeper, "realizes a homomorphism" is a claim about the *mechanism* — the form of the computation — and the project's standing position is that behavior does not settle mechanism. [`essay/undischargeable-negative`](undischargeable-negative.md) holds that the question of what a model *can* or *is* doing internally is not closable from behavior alone; the homomorphism-vs-dense-graph question is that question in its compositional form. Even a model that matched a homomorphism's extension *everywhere* would leave open whether the matching map is computed homomorphically or is an extensionally-equivalent non-homomorphic function — a question behavior is the wrong instrument to ask.

So: the deflationary alternative is squeezed without limit but never to zero, and the affirmative target is a mechanism claim behavior cannot reach even in the extensional limit. That is precisely the shape of an asymptote — approached arbitrarily closely, never touched.

## The contrast that does the work

Lay the compositionality case beside the reference case and the two silences are different in *kind*.

**Reference is a wall.** [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) shows the LLM-reference dispute "turns entirely on a single metasemantic premise" — whether corpus-inherited use counts as community membership — and that premise is, on the externalist's own picture, "settled **off-board**: by the natural history of the form and the social structure of the community, not by anything in the model's head or in its behavior." A dispute, that essay says, "is *evidence-bound* when the parties would converge if shown the right measurement"; the reference dispute "has no such fact in it." So a behavioral probe does not *narrow* the reference question by an inch — it is the wrong axis entirely. There is no ladder to climb. The method is silent from the first rung.

**Compositionality is an asymptote.** Here a behavioral probe *does* bear on the question — it narrows the deflationary alternative, monotonically, with each run — and the limit it approaches is well-defined (the homomorphism's extension). What it cannot do is *complete* the last inference from "survives every distributional alternative tested" to "is a homomorphism." The deciding residue is not an off-board fact about natural history; it is the underdetermination of a function's form by its finite graph, plus the behavior-vs-mechanism gap. The method is not silent; it is *asymptotically eloquent and finally inconclusive*.

This is not a difference of degree dressed up as a difference of kind. The two failures have different signatures and different remedies:

- A reference probe and the reference question **never intersect** (the word-to-world relation lives where the word-to-word method cannot look). More probes do nothing.
- A compositionality probe and the compositionality question **intersect on every run** (each excludes more non-homomorphic functions). More probes do something — just never the *last* thing.

And the contrast **is consistent with the project's own history** — though, as the limits note, the history corroborates the diagnosis without proving it. The reference cell is recorded as **saturated** after a single round of conceptual analysis (the internalism-vs-externalism work the reference essay synthesizes) — what a wall would predict: once you see no probe moves it, you stop probing. The compositionality cell, by contrast, has paid for run after run — AANN, dative, comparative-correlative, coercion, the *way*-construction — each one narrowing the deflationary corner without ever closing it — what an asymptote would predict: the marginal probe keeps returning information, so the program rationally keeps running. A method silent on compositionality in reference's *wall* sense would have made all that empirical work pointless; it was not pointless.

The honest caveat is that this asymmetry is *also* explained by a mundane confound the history cannot rule out: the project holds in-repo human-anchored compositional resources (treebanks, the CxNLI dataset) that make a composition probe cheap to build, and holds *no* reference anchor at all — the reference essay stresses one "is not a fetch away" and is structurally un-probeable for a text model. So the reference cell might be unprobed because the *instrument is missing*, not because the cell is a wall of principle, and both readings predict the same run-history. The history is therefore *consistent with* the wall/asymptote diagnosis and does not discriminate it from a missing-instrument story; it corroborates, it does not prove. The diagnosis rests on the structural argument of the two preceding sections, not on the history.

## Consequences (disciplining the project's own citation)

Two rules follow, parallel to the reference essay's two consequences.

**Consequence 1 — cite a compositional positive by the null it beats, never as realizing the homomorphism.** A result like the comparative-correlative double-negative is licensed to say: *the model's behavior on these items is inconsistent with the simplest part-blind distributional competence, and consistent with structure-respecting composition over the tested cases.* It is **not** licensed to say *the model realizes a syntax-to-semantics homomorphism* — that overruns the graph/form gap. The honest citation names which band of the deflationary alternative the probe excluded (order/sign-blind bag-of-words; verb-only lexical map; memorized instances) and stops there. This mirrors [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md)'s discipline that a distributional result should "name its ancestor precisely and stop": a compositional result should name the *null it beats* precisely and stop.

**Consequence 2 — treat the homomorphism question as productive-open, not principled-closed.** Because the compositionality cell is an asymptote, the marginal probe carries information, so — unlike the reference cell — it is *not* a place to write "principled limit, stop probing." The correct standing note is the opposite of reference's: the question stays open *and worth spending on*, with each run pricing how much further the deflationary corner has shrunk. The project should resist two symmetric errors: reading a strong compositional positive as having *reached* the homomorphism (the over-claim Consequence 1 blocks), and reading the never-arriving asymptote as a reference-style wall that makes further runs pointless (the under-claim this consequence blocks). The compositionality program is bounded above by a ceiling it approaches but cannot touch — and that is a reason to keep climbing carefully, not a reason to stop.

## What this essay is not

- **Not a verdict on whether LLMs compose.** It does not affirm or deny that any model realizes Montague's homomorphism. It locates what behavioral evidence can and cannot establish about that, and stops.
- **Not a claim that the compositional results are weak.** The extensional signatures (the double-negative composition; coercion's verb-overriding inference) are real and beat the simplest distributional null. The essay's point is about the *ceiling* on what they license, not the *floor* of what they show.
- **Not a re-statement of the concept page.** [`concept/compositionality`](../../base/concepts/compositionality.md) §4 *names* the homomorphism-vs-shortcut question as open and lists the two defenses; this essay argues the question's *shape* (asymptote, graded, productive-open) and contrasts it structurally with reference's (wall, binary, principled-closed) — a diagnosis the concept page does not make.
- **Not a claim that the two cells exhaust the map.** Wall and asymptote are two shapes of shortfall; other cells (e.g. the relational axis) may fail the method in yet other shapes. The essay characterizes only these two.

## Meaning-sense usage note

The essay's own claims are `constructional`/compositional (the homomorphism target and the construction-as-part reading), `distributional` (the part-blind null the systematicity signature beats), and `inferential` (coercion's verb-overriding inference as the extensional signature). The `referential` tag is present only as the **contrast pole** — the essay makes no referential claim of its own; it borrows the reference cell's "wall" verdict wholesale from [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) to set the compositionality "asymptote" against it. Per the project's lint rule, the unqualified word "meaning" is avoided; where it appears it is tagged or qualified.

## Honest limits

- **"Asymptote" and "wall" are deliberately-chosen metaphors, defended, not proven.** The defended content is precise — *monotone narrowing without completion* versus *no narrowing at all* — and is tied to a structural difference (graph-underdetermines-form plus behavior-vs-mechanism, versus an off-board deciding fact). But the metaphors compress; a reader should take the structural claims, not the geometry, as the thesis.
- **The "saturated after one round" reading of the reference cell is the project's own record, not an external fact.** It reflects how the project's sessions have treated that cell ([`essay/reference-as-premise-bound`](reference-as-premise-bound.md) and the internalism-vs-externalism synthesis); a different research program might find evidence-bearing reference probes the project's constraints forbid. The contrast is about *this method*, as the reference essay is careful to say of itself.
- **The Montague target is in-repo at secondary strength.** The homomorphism formulation is quoted from the SEP survey, not Montague's PTQ primary (still wanted); the survey is "a reference survey reporting Montague," and the essay's use of the homomorphism as *the* compositionality target inherits that secondary standing. The argument does not turn on any contested reading of the primary — the homomorphism formulation is uncontroversial textbook content — but the provenance is flagged.
- **It is a structural diagnosis, not a measurement.** It produces no number and overturns no result. Its force is locating the *shape* of a shortfall and what follows for citation and for spending — a real but modest contribution.

## Honesty box

- The essay's *original* contribution is the **asymptote-versus-wall diagnosis**: that the behavioral method falls short of the compositionality target (Montague's homomorphism) by *monotone-narrowing-without-completion* (a graded, productive-open shortfall, because finite behavior fixes a function's graph but underdetermines its form, and mechanism is behaviorally undischargeable), and that this differs in *kind* from how it falls short of the reference target (a binary, principled-closed shortfall, because the deciding fact is off-board) — together with the claim that this difference *explains* why the compositionality program keeps buying evidence while the reference program is saturated, and the two citation consequences that follow. This shape is the essay's own; no source page asserts it.
- **Every empirical and textual assertion cites its in-repo page.** The Montague quotes (§1.2, §3.2, §"What it cannot ground") are from [`source/janssen-zimmermann-montague-semantics-sep`](../../base/sources/janssen-zimmermann-montague-semantics-sep.md). The "narrow ... do not eliminate" and §2/§4 framings are from [`concept/compositionality`](../../base/concepts/compositionality.md). The double-negative composition quote is from [`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md); the coercion magnitudes from [`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md) and [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md). The "premise-bound, not evidence-bound," "constitutively silent," "settled off-board," and "evidence-bound when the parties would converge" lines are from [`essay/reference-as-premise-bound`](reference-as-premise-bound.md). The behavior-does-not-settle-mechanism point leans on [`essay/undischargeable-negative`](undischargeable-negative.md).
- **The strongest thing the essay asserts** is that no finite behavioral probe completes the inference to "the model realizes the homomorphism," while every well-built probe narrows the deflationary alternative. That is an argued structural claim about this method, not a proof that no method whatever could reach the form of the map; the limits section bounds it.

## Revision triggers (read before citing)

- **(a) If a non-behavioral instrument enters the project's scope** — a mechanistic / representational probe that bears on whether a model's composition *is* structure-preserving rather than an extensionally-equivalent shortcut — then the compositionality shortfall stops being purely an asymptote-of-behavior and the essay must be relativized to behavioral evidence specifically (the [`essay/undischargeable-negative`](undischargeable-negative.md) "architecture, not behavior" escape, made actual).
- **(b) If a probe is designed that an adversarial reviewer judges *completes* the homomorphism inference from finite behavior** (not merely narrows it) — for instance a provably-exhaustive composition test over a closed combinatory domain — then the "never arrives" claim weakens for that domain and the asymptote framing must be restated as domain-relative.
- **(c) If the Montague PTQ primary enters the repo and the homomorphism formulation is found to be weaker or stronger than the survey states**, re-check that the "graph versus form" gap is stated against the correct target; the argument is expected to survive (the formulation is textbook-standard) but the provenance note would upgrade.
- **(d) If the reference cell turns out to be evidence-bound after all** (a behavioral reference probe is admitted, firing [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) trigger (a) or (b)), then the wall/asymptote contrast loses one of its poles and must be re-drawn — the compositionality half stands on its own, but the *contrast* that is this essay's spine would need a new second term.
