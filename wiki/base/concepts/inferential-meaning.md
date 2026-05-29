---
type: concept
id: inferential-meaning
title: Inferential / conceptual-role meaning
meaning-senses:
  - inferential
  - distributional
created: 2026-05-28
updated: 2026-05-29
links:
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: refines
    target: concept/distributional-meaning
  - rel: contradicts
    target: concept/grounding
---

# Inferential meaning

The inferential view holds that a linguistic expression's meaning is constituted by its **inferential role**: a word or construction means what it licenses you to infer to and from. Brandom's inferentialism (1994/2000; not in-repo) is the systematic philosophical statement — content is fixed by an expression's position in a web of material inferences and incompatibilities, not by any prior relation to objects. Conceptual-role semantics in philosophy of mind is the broader family: the content of a representational state is its causal-functional role among other states. On either telling, to grasp a concept is to be disposed to make the inferences it underwrites, and the unit of analysis is the relational structure, not the isolated symbol.

For this project the `inferential` tag marks findings whose force is that an LLM tracks the inferences a word or construction licenses — that it preserves or breaks the right entailments, not merely that it reproduces a characteristic distribution. The contrast with the `distributional` tag is deliberate. Distributional structure is co-occurrence; inferential structure is what follows from what. The two are entangled in an LLM — next-token prediction is implicitly inferential, and [`meaning-senses.md`](../../meaning-senses.md) flags the open question of whether the two senses should collapse — but they are not definitionally the same, which is why this page `refines` rather than restates [`concept/distributional-meaning`](distributional-meaning.md). A finding earns the `inferential` tag when the indicator is inference-preservation, not similarity or surprisal alone.

## Piantadosi & Hill's "meaning without reference"

The strongest pro-LLM-meaning position in the current literature is Piantadosi & Hill (2022), who argue from conceptual-role semantics that meaning constituted through inferential relationships among a system's internal states is genuine meaning, and that LLMs plausibly achieve it. The central thesis is explicit:

> "Contrary to claims that LLMs possess no meaning whatsoever, we argue that they likely capture important aspects of meaning, and moreover work in a way that approximates a compelling account of human cognition in which meaning arises from conceptual role. Because conceptual role is defined by the relationships between internal representational states, meaning cannot be determined from a model's architecture, training data, or objective function, but only by examination of how its internal states relate to each other." ([`source/piantadosi-hill-2022-meaning-without-reference`](../sources/piantadosi-hill-2022-meaning-without-reference.md), §Abstract)

Two moves do the work. First, meaning is relational rather than referential — it "comes from the way concepts relate to each other" (§"Conceptual role theory"). Second, reference is therefore not necessary: "there are many terms that are meaningful to us but have no discernible referent at all, such as abstract words like 'justice' and 'wit.'" (§"Meaning and reference"). The illustrative case is logical vocabulary: "A symbol like AND only means logical conjunction if it interacts (composes) with others symbols like TRUE and FALSE in the appropriate way—i.e. when it has the right conceptual role" (§"Discovering conceptual role"). The upshot for LLMs is a positive claim stronger than mere distributional competence — that an LLM whose internal states stand in the right relations already "share[s] the foundation of how our own concepts get their meaning" (§"Conclusion").

This is the direct counter to the grounding requirement, which is why this page `contradicts` [`concept/grounding`](grounding.md). Bender & Koller (2020) hold that form-only training cannot yield meaning because meaning is a relation to communicative intent and the world that distributional form does not supply ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md)). Piantadosi & Hill deny the premise: if inferential role is sufficient for meaning, then the absence of extra-linguistic grounding is not a disqualification.

## How the project operationalizes the tag

The `inferential` indicator is inference behavior, not distribution. Concretely: entailment / NLI behavior (does the model accept what its premises entail and reject what they exclude?); acceptability and behavior under inference-licensing constructions (constructions co-tagged `constructional` because constructions license characteristic inferences); and **systematic substitution that preserves or breaks inferential role** — swapping a term for an inferential equivalent should leave licensed inferences intact, while swapping for a non-equivalent should break them. A model that passes the first and fails the second is exhibiting inferential structure rather than surface mimicry. Piantadosi & Hill supply the philosophical backing for treating such a result as semantically significant, but they do not supply the evidence: the source page is explicit that it "cannot ground … empirical claims about whether specific models actually exhibit the right inferential role structure" — that requires a human-anchored resource on the finding page itself.

**Live tension for this project.** The genuine open question is whether systematic inferential-role structure produced by distributional training actually *constitutes* meaning. Piantadosi & Hill say yes; Bender & Koller's grounding requirement says form-only training never yields meaning regardless of how systematic its inferential structure looks. This project does not adjudicate that dispute — it sets up findings so the contrast is visible, and a page that pits "model tracks the inferential role" against "model is form-only" must cite both sides. Two honest caveats temper any triumphalism. First, the source page's "Known limits" warns that the conceptual-role account advocated there "is not the only version of inferentialism; it should not be conflated with Brandom-style normative inferentialism or with NLI-task performance alone" — so a strong NLI score is not by itself the philosophical conclusion. Second, all Piantadosi & Hill quotes here are section-level, not page-level (the ar5iv HTML rendering has no pagination); this is expected for this source and noted on its page, but it means citations locate by heading, not page number.
