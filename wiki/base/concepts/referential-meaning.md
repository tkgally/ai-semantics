---
type: concept
id: referential-meaning
title: Referential meaning (sense and reference; externalism)
meaning-senses:
  - referential
  - grounded
created: 2026-05-28
updated: 2026-05-29
links:
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: refines
    target: concept/grounding
  - rel: contradicts
    target: concept/distributional-meaning
---

# Referential meaning

The referential view holds that a linguistic expression's meaning is, at least in part, its relation to something outside the linguistic system — an object, a property, a set in a world or model. This is the tradition that runs from Frege's `Bedeutung` through the twentieth-century externalists (Putnam, Burge, Evans). It is the natural foil to [`concept/distributional-meaning`](distributional-meaning.md): distributional structure characterizes an expression by the company it keeps inside the text, whereas referential meaning characterizes it by what it reaches out to *beyond* the text. The two need not be rivals about every word, but they come apart precisely on the question this project most cares about — whether tracking linguistic context amounts to tracking the world — which is why this page links `contradicts` to the distributional page rather than `refines`.

For the project's purposes three sub-positions must be kept separate; the controlled vocabulary in [`meaning-senses.md`](../../meaning-senses.md) (§`referential`) carries them as distinct sub-tags, and a finding that turns on the LLM case should tag the ones it actually bears on.

- **Sense** (`referential.sense`) — Frege's `Sinn`: the *mode of presentation*, the way a referent is given. "The morning star" and "the evening star" share a referent (Venus) but differ in sense. Sense is the sub-position closest to what distributional structure plausibly captures: a mode-of-presentation is, roughly, a way of being embedded in a web of descriptive and inferential associations, and that web is exactly what co-occurrence statistics encode. An LLM that distinguishes the contexts of "morning star" from "evening star" is, on a deflationary reading, tracking something sense-like.
- **Reference** (`referential.reference`) — what the expression actually picks out: the object, the extension, the truth-condition. Reference is not recoverable from sense alone in any mechanical way, and on most accounts it requires a relation to the world that linguistic context, however rich, does not by itself constitute. This is the contested sub-position for LLMs.
- **Externalist reference-fixing** (`referential.externalist`) — the thesis that what an expression refers to is fixed *partly outside the head*, by causal-historical chains and social facts rather than by any description the speaker can produce. Putnam's Twin Earth argument (that two physically identical speakers can mean different things by "water" because their environments differ) and his *division of linguistic labor* (that the reference of "elm" or "gold" is fixed by experts and a community, not by each speaker's private grasp), together with Evans's causal theory of names (that a name refers via a causal chain back to a baptismal event, not via a cluster of descriptions), are the canonical statements. These are uncited common-knowledge background here: **the primary sources — `Putnam 1975, "The Meaning of 'Meaning'"` and `Evans 1973, "The Causal Theory of Names"` — are not yet in-repo** (both are listed in [`wiki/base/wanted.md`](../wanted.md)), so no quote or page locator is given for them, and the externalist sub-tag has no in-repo primary-source anchor until they are ingested.

## Why the hardest LLM-meaning cases live here

The referential axis is where the LLM-meaning debate stops being a matter of degree and becomes a matter of kind. The three sub-positions sort an LLM very differently:

- On **sense**, an LLM has a plausible, almost trivial, claim: distributional training produces fine-grained discriminations between modes of presentation, and "sense as position in an inferential/associative web" is close to what next-token prediction optimizes for. A sense-only construal of meaning is roughly the inferentialist escape hatch (see [`concept/inferential-meaning`](inferential-meaning.md)).
- On **reference**, the claim is contested. Tracking the distribution of "water" is not obviously the same as referring to H₂O; the distributional signal is, by construction, silent on the extension.
- On **externalist reference-fixing**, the case is at its weakest, and this is exactly where Bender & Koller's form-only critique bites hardest. Their argument is that a system exposed only to *form* has no access to the relation that connects form to anything beyond it. They give that relation a formal shape:

> "We take meaning to be the relation M ⊆ E × I which contains pairs (e, i) of natural language expressions e and the communicative intents i they can be used to evoke." ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5187)

and then argue that form-only training cannot recover it:

> "We argue that a model of natural language that is trained purely on form will not learn meaning: if the training data is only form, there is not sufficient signal to learn the relation M between that form and the non-linguistic intent of human language users, nor C between form and the standing meaning the linguistic system assigns to each form." ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5187)

Bender & Koller frame the missing relation as one to *communicative intent* rather than to extra-linguistic *referents* specifically, but the structural point transfers directly: reference and externalist reference-fixing are relations between form and something the corpus does not contain (a causal-historical chain, a community of experts, a world the speaker is embedded in). If form-only training cannot recover the intent relation, the burden is on any account that says it nonetheless recovers the reference relation. This is the same architectural objection that the [`concept/grounding`](grounding.md) page develops as the `grounded` requirement — referential meaning is, on the externalist construal, a *grounded* relation, which is why this page co-tags `grounded` and links `refines` to the grounding concept. (Note that Bender & Koller's own use of "meaning" is not sorted against this sub-typology; their source page flags that citing them "requires specifying which sense the citation is intended to invoke" — here the intended sense is the form-to-world/intent relation that referential and grounded share.)

## Live tension

The genuine open question for this project is whether an LLM that demonstrably tracks distributional, sense-like structure is thereby tracking **reference** at all — or whether sense-tracking and reference-fixing are different in kind, such that no quantity of the former adds up to the latter. A deflationist (and the inferentialist line behind [`concept/inferential-meaning`](inferential-meaning.md)) says sense-tracking is enough to count as meaning; an externalist says reference is constitutively a relation to a world and a community that text does not contain, and Bender & Koller's form-only argument is the sharpest version of that "no" on the table in-repo.

There is also a methodological tension specific to how this project verifies things, and it should be stated bluntly. The project has an in-repo, human-anchored resource for **form** — the AANN acceptability stimuli ([`resource/mahowald-2023-aann-stimuli`](../resources/mahowald-2023-aann-stimuli.md)) let a formal-competence claim be checked against human acceptability judgements. There is **no comparable in-repo resource that anchors reference**: no dataset that pins a human-agreed extension or reference relation an LLM could be tested against. So referential claims about LLMs currently cannot be empirically grounded the way formal claims can; they remain conceptual until a reference-bearing resource is found or built. Compounding this, the primary philosophical sources for the externalist sub-tag (`Putnam 1975`, `Evans 1973`) are still in `wiki/base/wanted.md` and not yet ingested, so even the *conceptual* grounding of `referential.externalist` is provisional pending those ingestions. Any finding tagged `referential.reference` or `referential.externalist` should carry this gap explicitly rather than borrow the apparent solidity of a form-side result.
