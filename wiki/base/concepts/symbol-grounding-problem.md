---
type: concept
id: symbol-grounding-problem
title: Symbol Grounding Problem
meaning-senses:
  - grounded
  - grounded.perceptual
  - grounded.causal
created: 2026-05-30
updated: 2026-07-06
links:
  - rel: depends-on
    target: source/harnad-1990-symbol-grounding
  - rel: depends-on
    target: source/barsalou-1999-perceptual-symbol-systems
  - rel: refines
    target: concept/grounding
---

# Symbol Grounding Problem

The symbol grounding problem, stated by Harnad (1990), asks: how can the semantic interpretation of a formal symbol system be made *intrinsic* to the system rather than *parasitic* on meanings in the head of an external interpreter? The question bites on any system — biological or artificial — whose cognition is described in terms of symbolic manipulation: if the symbols have meaning only because we assign them meaning from the outside, the system itself is not really a semantic system at all, merely a syntactic engine with an semantic veneer borrowed from its users.

This page is about the *mechanism* of grounding — the *symbol→sensorimotor anchoring* question — and should be read as distinct from [`concept/grounding`](grounding.md), which is about the *binary-vs-gradual debate* (Bender & Koller vs. Lyre). The two pages cross-reference each other but cover different ground: `grounding` is about whether and how much; this page is about *what grounding requires at the level of representations*.

## The problem stated

A symbol system consists of tokens manipulated by rules that operate purely on the tokens' shapes (their syntactic form), not on what they represent. The manipulation is semantically interpretable — one can assign meanings to the tokens — but the meaning assignment comes from outside the system. Harnad draws the crucial consequence:

> "How can the semantic interpretation of a formal symbol system be made intrinsic to the system, rather than just parasitic on the meanings in our heads?" ([`source/harnad-1990-symbol-grounding`](../sources/harnad-1990-symbol-grounding.md), p. 335)

> "How can the meanings of the meaningless symbol tokens, manipulated solely on the basis of their (arbitrary) shapes, be grounded in anything but other meaningless symbols?" ([`source/harnad-1990-symbol-grounding`](../sources/harnad-1990-symbol-grounding.md), p. 335)

The regress is made vivid by the Chinese/Chinese dictionary scenario. Trying to learn Chinese by consulting only a Chinese/Chinese dictionary produces an endless "merry-go-round, passing endlessly from one meaningless symbol or symbol-string (the definientes) to another (the definienda), never coming to a halt on what anything meant." ([`source/harnad-1990-symbol-grounding`](../sources/harnad-1990-symbol-grounding.md), body — arXiv cs/9906002, verbatim). The merry-go-round is a regress of the same kind that afflicts purely symbolic AI: every symbol is defined by other symbols, none of which has its meaning grounded in anything non-symbolic.

## Harnad's proposed solution

Harnad proposes a *hybrid* architecture that breaks the regress at the bottom:

> "A candidate solution is sketched: Symbolic representations must be grounded bottom-up in nonsymbolic representations of two kinds: (1) iconic representations, which are analogs of the proximal sensory projections of distal objects and events, and (2) categorical representations, which are learned and innate feature-detectors that pick out the invariant features of object and event categories from their sensory projections." ([`source/harnad-1990-symbol-grounding`](../sources/harnad-1990-symbol-grounding.md), p. 335)

The elementary symbols in the hybrid system — category names — are not purely formal tokens: they are connected to nonsymbolic representations of what category members look like (iconically) and what distinguishes members from non-members (categorically). Higher-order symbol strings composed from these grounded names inherit their grounding by composition; the regress terminates at the sensorimotor level.

The theory is therefore a *grounding-by-contact* story: symbols acquire intrinsic meaning by being causally connected to the sensory-motor world that produces the categorical and iconic representations. The contact is the grounding.

## Relation to Barsalou's perceptual symbol systems

Barsalou (1999) provides the positive cognitive theory that fills the explanatory role Harnad's architecture requires. Where Harnad asks *what kind of representation* grounds symbols, Barsalou answers: *perceptual symbols* — records of the neural states underlying perception, stored in the association areas of sensory-motor cortex and reactivated top-down as *simulations*. The perceptual symbol system is, in effect, the neuroscientifically grounded implementation of Harnad's iconic and categorical representations.

See [`concept/embodied-cognition`](embodied-cognition.md) for the broader theoretical context and for the specific question of what this means for model behavior.

## Relation to Bender & Koller (2020)

Bender & Koller's form-vs.-meaning argument (see [`concept/grounding`](grounding.md)) is structurally identical to Harnad's symbol grounding problem, updated for neural LLMs trained on text. Where Harnad focuses on purely symbolic AI, Bender & Koller note that text corpora are still form only: the communicative intents that constitute meaning are not in the training signal. Both arguments conclude that training on form alone cannot yield intrinsic semantic content. Harnad 1990 predates the neural turn by decades but anticipates the argument precisely.

The key structural continuity: Harnad's "symbol/symbol merry-go-round" — all symbols interpreted only by other symbols — maps directly onto the distributional training regime. A model trained on text-to-text prediction has, on its face, only text to interpret text with. Whether that amounts to the same regress depends on whether one thinks distributional structure encodes something more than co-occurrence patterns — this is the live debate that the project's wedge is designed to probe.

## Relevance to text-only vs. multimodal models

The symbol grounding problem provides the theoretical frame for the most pointed version of the text-vs.-multimodal split:

- A *text-only* model's representations are (arguably) stuck in the symbol/symbol loop: its "categorical representations" are distributional clusters, not sensorimotor feature-detectors. On Harnad's account, this is precisely the regress that lacks intrinsic grounding.
- A *multimodal* (vision-language) model has, in addition, exposure to image (and potentially audio, video) signals during training. Whether this constitutes the "iconic and categorical representations" Harnad requires is a substantive empirical question — not trivially yes. A VLM's image encoder produces a representation of a visual scene, but whether that representation is *causally responsive* to distal objects in the way Harnad's account requires, or whether it is merely a different kind of formal token (pixel statistics rather than word co-occurrences), is not settled.

The project's `grounded.perceptual` sub-tag is designed to track findings that bear on this question. Any finding tagged `grounded.perceptual` should be read in the context of this question: is the model's behavior evidence of sensorimotor anchoring (in Harnad's sense), or merely of richer statistical structure?

## What in-repo evidence bears

The project's grounding probes bear on this page's question only **obliquely**, and it is worth being precise about how. They test whether adding a *perceptual channel* (an image of a usage) or a word's *perceptual groundedness* moves a model's lexical-sense behavior — a tractable proxy for "does sensorimotor contact add anything measurable here." Every result so far is a **null that lands where text already saturates**, so none of them touches the *in-principle* symbol-grounding question this page owns (whether a text- or image-trained model's representations are intrinsically grounded in Harnad's sense); they bound only the *easy cases*, and they do so modestly.

- **The image-redundancy null.** [`result/multimodal-grounding-image-v1`](../../findings/results/multimodal-grounding-image-v1.md) (the project's first image-input probe) showed that attaching a **depicting picture** of each usage does **not** improve the panel's same-sense / different-sense separation for clear homonyms — because the **text-only** panel already separates them perfectly (AUC = 1.000 in every cell). Where text saturates, the image has nothing measurable to add. This is a *redundancy* null on 12 clear-homonym pairs, n=3 models, single run — not evidence that grounding is impossible, and its own caveat reads even the one small positive cell as behavior *sensitive to* image input on a continuous scale, **not** a Harnad-style perceptual symbol system.
- **The text-side moderation null.** [`result/lexical-perceptual-grounding-moderation-v1`](../../findings/results/lexical-perceptual-grounding-moderation-v1.md) (the project's first `grounded`-tagged result, a $0 re-analysis) found that a word's static **perceptual groundedness** (Lancaster Sensorimotor Norms) does **not** predict how well a text-only model tracks its graded senses — if anything a weak *opposite* tilt (Δρ −0.05 / −0.27 / −0.04), the one bootstrap CI excluding zero running the wrong way. It is **underpowered** (≈21 lemmas/side, compressed moderator range), so it reads as "no detectable moderation *or* an effect this design cannot resolve," not as evidence against grounding.
- **The standing bet on *where* perception could act.** [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md) (`tested` — gating shape only) turns those two nulls into a forward hypothesis: perceptual input can move lexical-sense behavior **only in the residue the text distribution under-determines** (the *headroom*), and for concrete depictable senses that residue is **empirically narrow** — a self-concealing headroom, because the fluent models worth probing have already extracted the sense-relevant distinction from text for exactly the clear, depictable cases where a picture "should" obviously help. The gating *shape* has first confirming-direction evidence on a binary VWSD selection task (3/3 models in direction, distraction-controlled); the *magnitude* bet stays untested.
- **The instrument gap.** [`open-question/grounding-magnitude-instrument`](../../findings/open-questions/grounding-magnitude-instrument.md) records why the magnitude bet is stuck: no in-repo resource jointly satisfies the four requirements a valid magnitude instrument needs (a certified-competent text channel on the specific items, a graded human signal, image-native fine-polysemy material, and no de-referencing trap). On current open resources the magnitude is **un-instrumentable in-repo** — an externally-released graded-image fine-polysemy set is the only route the project can see.

The honest summary: adding the external perceptual channel changes nothing measurable **exactly where the text distribution already determines the sense**, and the project cannot yet instrument the one cell (fine polysemy; perceptually-subtle senses) where Harnad's sensorimotor contact might still earn its keep. That leaves the *symbol→sensorimotor-anchoring* mechanism this page owns **open** — the evidence trims a hope about the easy cases, not the mechanism.

## What this page is not

This page covers the *symbol→sensorimotor mechanism* question. It does not re-argue the binary-vs.-gradual debate (that is [`concept/grounding`](grounding.md)) or the externalist reference question (that is [`concept/referential-meaning`](referential-meaning.md)). The three overlap — externalist reference-fixing is one species of causal contact with the world, and Lyre's gradual grounding is in part a response to Harnad-style requirements — but they are tracked separately in this wiki.
