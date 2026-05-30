---
type: source
id: barsalou-1999-perceptual-symbol-systems
title: "Perceptual Symbol Systems"
authors:
  - Barsalou, Lawrence W.
year: 1999
venue: "Behavioral and Brain Sciences"
volume: 22
pages: 577–660
doi: "10.1017/S0140525X99002149"
url: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/perceptual-symbol-systems/C2D720D63C1CE3D7153F6BA473F9DD87
access: paywalled (Cambridge University Press); author's copy at https://barsaloulab.org/Online_Articles/1999-Barsalou-BBS-perceptual_symbol_systems.pdf
meaning-senses:
  - grounded
  - grounded.perceptual
  - grounded.causal
status: received
created: 2026-05-30
updated: 2026-05-30
pdf-pages: 84
links:
  - rel: supports
    target: concept/embodied-cognition
  - rel: supports
    target: concept/symbol-grounding-problem
---

# Barsalou 1999 — Perceptual Symbol Systems

## What it is

Target article with peer commentary in *Behavioral and Brain Sciences* 22 (1999) 577–660. The canonical cognitive-science statement that human conceptual knowledge is grounded in modal (perceptual/sensorimotor) representations, not in amodal abstract symbols. Introduces the *perceptual symbol system* framework: concepts are implemented as *simulators* — organized memories of perceptual components, reactivated top-down in sensory-motor cortex — rather than as discrete amodal tokens. The paper is the primary cognitive-science backbone for the project's `grounded.perceptual` sub-tag and provides the theoretical machinery for the "embodied cognition" position: concepts are not separate from perception and action but constituted by them.

Note on page range: Cambridge Core lists pp. 577–660; this includes the peer commentary section. The target article alone runs approximately pp. 577–609. The distinction matters for locating quotes.

**Provenance.** The Cambridge Core abstract was fetched and confirmed verbatim 2026-05-30. The author-lab PDF (barsaloulab.org) yielded no extractable text via automated tools. Key body passages were cross-checked against multiple citing sources (Jim Davies summary, Omar Meriwani summary, Cambridge Core abstract) and are noted below with their provenance level. Tom has library access and should verify body page numbers against the published text.

## Summary

Barsalou's argument has four moves:

1. **Against amodal theories.** Twentieth-century cognitive science inherited from formal logic and AI the view that concepts are amodal — abstract symbols whose form is arbitrary and disconnected from perception. Barsalou argues this view is empirically unsupported and theoretically deficient.

2. **Perceptual symbols.** During perception, *association areas* in the brain capture the bottom-up patterns of activation in sensory-motor areas. These captured patterns, stored as memory traces, are *perceptual symbols*: records of the neural states underlying perception, not arbitrary tokens. They are *modal* — they remain in the same systems that process perception and action.

3. **Simulators.** Repeated perceptions of a category's members cause the stored perceptual symbols to be organized around a *simulator*: an attractor-like system that can generate indefinitely many *simulations* of the category. A simulation is a partial re-enactment of sensory-motor experience. Simulators implement concepts: to have the concept CAR is (in part) to have a simulator that can produce varied simulations of car-like entities.

4. **Full conceptual system.** Barsalou argues that simulators are powerful enough to support productivity (by combining and nesting), propositions (by binding simulators to perceived individuals), and abstract concepts (grounded in simulations of combined physical and introspective events). The system therefore does what amodal theories do — without requiring an amodal symbolic layer.

## Key passages

All quotes from the abstract are verbatim from Cambridge Core abstract field (fetched 2026-05-30). Body quotes at specific page numbers are marked with their provenance level.

**p. 577 (abstract) — full abstract (verbatim from Cambridge Core):**

> "Prior to the twentieth century, theories of knowledge were inherently perceptual. Since then, developments in logic, statistics, and programming languages have inspired amodal theories that rest on principles fundamentally different from those underlying perception. In addition, perceptual approaches have become widely viewed as untenable because they are assumed to implement recording systems, not conceptual systems. A perceptual theory of knowledge is developed here in the context of current cognitive science and neuroscience. During perceptual experience, association areas in the brain capture bottom-up patterns of activation in sensory-motor areas. Later, in a top-down manner, association areas partially reactivate sensory-motor areas to implement perceptual symbols. The storage and reactivation of perceptual symbols operates at the level of perceptual components – not at the level of holistic perceptual experiences. Through the use of selective attention, schematic representations of perceptual components are extracted from experience and stored in memory (e.g., individual memories of green, purr, hot). As memories of the same component become organized around a common frame, they implement a simulator that produces limitless simulations of the component (e.g., simulations of purr). Not only do such simulators develop for aspects of sensory experience, they also develop for aspects of proprioception (e.g., lift, run) and introspection (e.g., compare, memory, happy, hungry). Once established, these simulators implement a basic conceptual system that represents types, supports categorization, and produces categorical inferences. These simulators further support productivity, propositions, and abstract concepts, thereby implementing a fully functional conceptual system. Productivity results from integrating simulators combinatorially and recursively to produce complex simulations. Propositions result from binding simulators to perceived individuals to represent type-token relations. Abstract concepts are grounded in complex simulations of combined physical and introspective events. Thus, a perceptual theory of knowledge can implement a fully functional conceptual system while avoiding problems associated with amodal symbol systems. Implications for cognition, neuroscience, evolution, development, and artificial intelligence are explored."

**Body — perceptual symbols as neural records (verified via Jim Davies summary citing the paper):**

> "Perceptual symbols are records of the neural states that underlie perception."

*Provenance: cited in Jim Davies (2003) summary of Barsalou 1999; cross-checked against abstract language "association areas … capture bottom-up patterns." Page number not independently confirmed — Tom should check against published text (likely §1, p. 577–579).*

**Body — sensory-motor grounding of concepts (verified via Jim Davies summary):**

> "Although mechanisms outside sensory-motor systems enter into conceptual knowledge, perceptual symbols always remain grounded in these systems."

*Provenance: cited in Jim Davies (2003) summary. Page number not confirmed; likely §2 or §3.*

**Body — simulator definition (approximately verbatim from Jim Davies summary):**

> "an integrated system of perceptual symbols that is used to construct specific simulations of a category."

*Provenance: Jim Davies (2003) summary; consistent with abstract language "implement a simulator." Treat as approximately verbatim.*

**Body — working memory as simulation engine (Jim Davies summary):**

> "working memory is the system that runs perceptual simulations."

*Provenance: Jim Davies (2003) summary. Page number not confirmed.*

## What it can ground

- [`concept/embodied-cognition`](../concepts/embodied-cognition.md) — this is the primary cognitive-science source for the perceptual-simulation theory of meaning.
- [`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md) — Barsalou's simulator theory is the positive proposal that fills the gap Harnad 1990 identified: how sensorimotor grounding actually works at the level of representations.
- The `grounded.perceptual` sub-tag in [`meaning-senses.md`](../../meaning-senses.md) — the strongest theoretical anchor for the claim that concepts are constituted by modal simulation, not amodal symbol manipulation.
- Any finding page that argues an LLM's text-only training leaves it without a perceptual simulator — this paper sets the theoretical benchmark against which text-only systems fall short.
- The `grounded.causal` sub-tag (indirectly): Barsalou's simulators are causally responsive to the world via their origins in perceptual experience; causal contact flows through the perceptual grounding chain.

## What it cannot ground

- Claims about LLM behavior on specific linguistic constructions — the paper is a cognitive theory, not a probing study.
- Claims about degree of grounding in LLMs — Barsalou's theory is about humans and does not evaluate LLMs. For a graded LLM grounding account, cite Lyre 2024.
- The `grounded.social` tag — Barsalou's theory is about individual-level perceptual simulation, not joint action or social embedding.
- Any claim that multimodal models (VLMs) are "perceptual symbol systems" in Barsalou's sense: his theory requires that the perceptual records be in the *same* sensory-motor systems as perception, a claim that does not straightforwardly translate to a neural network trained on pixel tensors.

## Known limits

- Long, complex target article (84 pages including commentary): body quote extraction was limited to what secondary sources corroborate. The four body quotes above carry provenance caveats; Tom should verify against the published text.
- The paper is primarily about human cognition and is agnostic about AI in the body; the AI implications section (mentioned in the abstract as one of the "implications … explored") should be checked for its specific claims before citing it as a source for LLM-specific conclusions.
- The peer commentary (pp. 609+) includes critical responses, some contesting the modal/amodal distinction. These are not extracted here; any citation of Barsalou 1999 as a settled consensus should acknowledge that the peer commentary was divided.
- Pages 577–609 is the target article range; pages beyond 609 are commentary. Distinguish in citations.

## Status

Received (2026-05-30): abstract verbatim from Cambridge Core; body quotes from Jim Davies (2003) secondary summary with provenance caveats noted. Tom should verify body page numbers against the published text via library access.
