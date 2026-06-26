---
type: essay
id: gradient-from-overlap
title: Gradient from overlap — declining to read an LLM's sense-gradience as a stored prototype repeats the prototype tradition's own discipline, not a machine-specific deflation
meaning-senses:
  - distributional
  - referential
status: draft
contingent-on: []
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: depends-on
    target: source/rosch-mervis-1975-family-resemblances
  - rel: depends-on
    target: source/rosch-1975-cognitive-representations
  - rel: depends-on
    target: source/wittgenstein-1953-philosophical-investigations
  - rel: depends-on
    target: concept/frame-and-prototype-semantics
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: concept/distributional-meaning
---

# Essay: gradient from overlap

> **Status: draft (2026-06-26). A philosophical-track essay arguing in the project's own voice.** It introduces **no new empirical claim**: every empirical assertion cites the in-repo page that carries it, and the original part is the argument — a sorting of what a typicality/relatedness *gradient* ever licenses about a *representation*, in people as in models. The load-bearing historical premise (that Rosch & Mervis founded the prototype result by deriving graded typicality from attribute **overlap**, and explicitly declined to offer a model of how a prototype is *learned or formed* — from which this essay *infers* that the paper posits no stored prototype the gradient is evidence for) is **primary-direct** in-repo: it rests on quotations verified character-for-character on [`source/rosch-mervis-1975-family-resemblances`](../../base/sources/rosch-mervis-1975-family-resemblances.md). The Rosch 1975b graded-typicality findings it leans on more lightly are in-repo at **secondary strength** ([`source/rosch-1975-cognitive-representations`](../../base/sources/rosch-1975-cognitive-representations.md)), and the essay marks where it relies on them. **Revision triggers** are listed at the end; chief among them, a representation-level probe that actually adjudicates the underdetermination this essay says the gradient leaves open.

## The position

The project's lexical centrepiece — [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md) — carries a standing worry, foregrounded on its own concept page: a model's graded sense-relatedness signal "may be nothing more than **graded distributional similarity** … with no 'prototype representation' distinct from context-similarity at all" ([`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md), §"The standing distributional question"). The worry is usually heard as a *deflation aimed at the machine*: the model only *looks* prototype-like; underneath there is merely distribution, so the prototype reading is the generous one and the distributional one the debunking one.

This essay argues that framing mis-locates the asymmetry. The bounded thesis: a typicality/relatedness **gradient underdetermines whether anything prototype-shaped is stored** — and this is not a fact peculiar to LLMs but the discipline the prototype tradition imposed on *itself* at its founding. Rosch & Mervis 1975 *derived* graded typicality from attribute **overlap** among category members, and stated in as many words that they were **not** offering a model of how a prototype is *learned or formed* — leaving (on this essay's reading) no stored prototype that the gradient is evidence *for*. So when the project refuses to read the model's graded behaviour as evidence of a stored prototype — "monotonicity, not representation" — it is not flinching from a claim it could otherwise make about a machine. It is repeating, for a model, exactly the inference-barrier the founders drew for people. The "prototype reading" and the "merely distributional reading" are therefore **not two rival hypotheses one of which the project hopes to confirm**: an overlap-derived gradient with no representational verdict attached just *is* what the prototype tradition's own evidence ever amounted to. What stays genuinely open — and is the whole of what the worry should name — is narrower, and stated at the end.

## What Rosch & Mervis actually built: a gradient out of overlap

The founding prototype result is not a posited central representation from which typicality is read off. It runs the other way: typicality is the *output*, and **attribute overlap** is the input that predicts it. Rosch & Mervis state the basic hypothesis as overlap, in their own words:

> "In the present research, we viewed natural semantic categories as networks of overlapping attributes; the basic hypothesis was that members of a category come to be viewed as prototypical of the category as a whole in proportion to the extent to which they bear a family resemblance to (have attributes which overlap those of) other members of the category." ([`source/rosch-mervis-1975-family-resemblances`](../../base/sources/rosch-mervis-1975-family-resemblances.md), p. 575)

The "family resemblance" that does the explaining is operationalized as a per-item **overlap score** — "the sum of the weighted raw scores of each of the attributes listed for the item" ([`source/rosch-mervis-1975-family-resemblances`](../../base/sources/rosch-mervis-1975-family-resemblances.md), pp. 581–582) — and the result is that this overlap score is strongly rank-correlated with rated typicality across all six categories (Spearman 0.84–0.94, all p < .001; [`source/rosch-mervis-1975-family-resemblances`](../../base/sources/rosch-mervis-1975-family-resemblances.md), p. 582). The complementary demonstration is the same point from the other side: the five most-typical members of a category share many attributes among themselves while the five least-typical share almost none (Table 2, p. 582) — there is no feature common to all, only overlap that thins toward the periphery.

The crucial move for this essay is what the authors *declined* to add on top of that. The same source page records their own disclaimer, verbatim:

> "the present research was not intended to provide a processing model of the learning of categories or formation of prototypes" ([`source/rosch-mervis-1975-family-resemblances`](../../base/sources/rosch-mervis-1975-family-resemblances.md), p. 574, quoted on the source page under "What it cannot ground")

So the founding result is a **structural** finding — overlap predicts typicality — and, by the authors' explicit disclaimer, **not** a model of how a prototype is formed; nor, this essay reads, a claim about a stored prototype the gradient is evidence *for*. The "prototype" in "prototype theory" is, on Rosch & Mervis's own measure, the point of maximal overlap in a network, characterized *behaviourally* by the typicality gradient; it is not, in this paper, posited as a represented object the gradient is evidence *for*. The gradient is what overlap produces; the founders left the formation/processing question explicitly unaddressed, and — this essay's inference from that, not a sentence they wrote — the representation question with it. (The disclaimer's verbatim scope is a *learning/formation* model; that the paper thereby posits no stored prototype the gradient is evidence *for* is the reading this essay draws from the result's structure, not a claim Rosch & Mervis stated.)

This is reinforced by the priming side of the program, carried in-repo at secondary strength: typicality judgments are "reliable even under changes of instructions and items," and degree of typicality governs "whether advance information about the category name facilitates or inhibits responses in a matching task" ([`source/rosch-1975-cognitive-representations`](../../base/sources/rosch-1975-cognitive-representations.md), §§1, 3, carried via Rosch's 1978 retrospective). Processing *tracks* the gradient — but, again, that a process is sensitive to typicality does not say the typicality is stored as a prototype rather than computed from overlap each time. The early prototype literature is careful about exactly this gap; the project did not invent the caution.

## The same barrier, twice

Set the two cases side by side and the barrier is one barrier, drawn in the same place.

**For people.** A typicality gradient (robins are better birds than penguins; furniture grades from chair to telephone) is what you observe. Rosch & Mervis explain it by overlap and decline to say whether the underlying representation is a stored abstract central tendency or something computed from remembered exemplars — a question that stayed live for decades after, between prototype and exemplar models, *both of them representational*. Even within psychology, the gradient did not settle the representation; the founders said as much.

**For the model.** A graded sense-relatedness signal is what [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md) observes: every panel model's rating is "strongly rank-correlated with the human DURel median," with cleanly monotone per-level means, and the result page leads with the matching disclaimer — "**Monotonicity, not representation** … it is **not** evidence of graded sense *representations*" ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)). The concept page draws the same line: the lexical line "**asserts prototype-consistent behavior, not prototype representation**" ([`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md)).

The shape is identical: **a gradient does not entail a stored representation of the thing the gradient is graded in.** It holds for Rosch's human typicality data and it holds for the model's relatedness data, and it holds for the same reason — overlap (of attributes, of contexts) is sufficient to produce the gradient, so the gradient cannot by itself reach past overlap to a representation. The project's "monotonicity, not representation" is therefore not a machine-specific austerity. It is the prototype tradition's own discipline, applied to a new gradient. Reading the model's gradient as a stored prototype would over-read it in precisely the way Rosch & Mervis warned against over-reading *theirs*.

## Why "prototype-consistent" and "merely distributional" are not rivals

The usual framing pits a *prototype* reading against a *distributional* reading as competitors — the first the meaningful one, the second the debunking one. On the overlap analysis, that contest dissolves at the level the gradient operates on.

Rosch & Mervis's family-resemblance score *is* an overlap measure: typicality rises "in proportion to the extent to which" a member's attributes "overlap those of" the other members of the category (p. 575; the parenthetical-clause wording quoted in full at the top of the previous section). The source page itself names this the "cognitive-psychology ancestor of the project's standing 'graded behavior may be nothing more than graded distributional similarity' worry" ([`source/rosch-mervis-1975-family-resemblances`](../../base/sources/rosch-mervis-1975-family-resemblances.md), §"Bearing on this project"). So a graded category, *as the founders operationalized it*, is already an overlap-derived gradient. A model that produces a relatedness gradient by tracking how much two usages' contexts overlap is not failing to be prototype-like and merely simulating it from distribution; it is reproducing the very kind of signal — overlap-derived gradedness — that the prototype result consists in. "Prototype-consistent behaviour" and "an overlap-derived gradient" name the same behavioural fact, not two stories about what underlies it.

What this does **not** do is collapse the project's distributional worry into nothing. It relocates it. The worry is no longer "is the model's gradient prototype-shaped or merely distributional?" — for that question, on the overlap reading, the two are the same shape. The worry that survives is sharper and is the next section.

## The disanalogy that survives — and is the real open question

There is one place the two cases come apart, and keeping it visible is what stops this essay from over-claiming a clean identity.

Rosch & Mervis's overlap is over **human-listed attributes**: their per-item score sums "the attributes listed for the item" — features elicited *from people* asked what category members have. The overlap lives in a space of articulated semantic attributes. The model's relatedness gradient, on the deflationary reading, is overlap over **distributional context** — token co-occurrence geometry, not articulated attributes. Both are overlap; the **space the overlap lives in differs**. And whether distributional-context overlap is a faithful proxy for human-attribute overlap — whether the two feature spaces coincide closely enough that the model's gradient is *the same gradient* a human attribute-overlap account would draw, rather than a coincidentally-similar ordering — is exactly the standing question [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) tracks, and it is **not** settled here.

The project's one piece of leverage on it is the v1 topic-similarity control: partialling out the model's own topic-similarity rating, the relatedness signal "**substantially survives**" (gemini 0.80→0.73; [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)), which is modest evidence that the gradient carries rank information beyond the model's *perception of context similarity*. But the result page flags that control as "model-internal" and "not a fully independent control," so it bounds the worry without dissolving it. The honest residue is therefore this: an overlap-derived gradient with no representational verdict is common ground between the prototype tradition and the distributional reading; what remains genuinely contested is **which overlap space the model's gradient is computed in**, and whether that space is the human-attribute one the prototype result was built from. That is the question worth the project's anxiety — not the dissolved "prototype vs distributional" contest, and not a stored-representation claim the gradient was never going to license on either side.

## Sibling note

This essay backstops the "behaviour, not representation" discipline that [`graded-scale-ungraded-commitment`](graded-scale-ungraded-commitment.md) treats as a load-bearing rule. That essay holds the line ("'Ungraded commitment' would be a fact about the model's stated stance, not a peek inside it"); this one gives the line its *rationale* — the prototype tradition's founding evidence was itself a gradient its authors declined to read representationally, so the discipline is fidelity to that tradition, not caution specific to machines. The two are complementary: that essay sorts *kinds* of gradience (scale vs commitment) and what each would license; this one sorts what *any* such gradient licenses about representation, in people and models alike.

## What this essay is not

- **Not a primary-reading dispute about Rosch.** The Rosch & Mervis premises are primary-direct in-repo (verified quotations with journal pagination); the Rosch 1975b graded-typicality and priming findings are secondary-only (carried via her 1978 retrospective) and used only for the lighter "processing tracks the gradient" point, flagged as such.
- **Not a new empirical claim.** It re-sorts existing in-repo material and measures nothing. The one empirical fact it leans on (v1's cross-item monotonicity, and the topic-control survival) is cited at the result page's stated strength; the essay does not restate v1's specific correlation magnitudes as findings of its own.
- **Not a claim that the model has — or lacks — a prototype representation.** The whole argument is that the gradient is silent on that, symmetrically for people and models. It declines the representation question; it does not answer it either way.
- **Not a dissolution of the distributional worry.** It dissolves only the *mis-stated* version (prototype vs distributional as rival readings of the gradient) and re-states the surviving version (which overlap space the gradient lives in), explicitly leaving that open.
- **Not a human-anchor claim.** None of Rosch & Mervis, Rosch 1975b, or Wittgenstein is a human anchor (each grounds the *theory*, never a model result); the only human yardstick the v1 result is scored against is its DURel/Usim resource, and this essay adds no comparison beyond what that result already states.

## Honesty box

- The essay's **original** contribution is the **sorting**: that a typicality/relatedness gradient underdetermines a stored representation; that Rosch & Mervis founded the prototype result by deriving the gradient from attribute overlap and *explicitly declined* a learning/formation processing model (from which this essay infers — it is not their stated words — that no stored prototype is posited for the gradient to be evidence of); that the project's "monotonicity, not representation" therefore repeats the prototype tradition's own discipline rather than deflating the machine; and that "prototype-consistent" and "merely distributional" are not rival readings of the gradient but the same overlap-derived shape — with the genuinely open question re-stated as *which overlap space* the model's gradient is computed in.
- The strongest thing the essay asserts is that **the gradient does not license a stored-prototype reading on either side, and the surviving distributional question is about the overlap space, not about prototype-vs-distribution.** It does not assert that the model's distributional-context overlap *is* (or is not) the human-attribute overlap space; that is named as open.
- Every quotation is verified on its in-repo source page; the Rosch & Mervis lines are primary-direct, the Rosch 1975b lines secondary-only, both flagged in place. No quotation is reconstructed from memory.
