---
type: concept
id: embodied-cognition
title: Embodied Cognition and Sensorimotor Theories of Meaning
meaning-senses:
  - grounded
  - grounded.perceptual
  - grounded.causal
created: 2026-05-30
updated: 2026-07-05
links:
  - rel: depends-on
    target: source/barsalou-1999-perceptual-symbol-systems
  - rel: depends-on
    target: source/harnad-1990-symbol-grounding
  - rel: refines
    target: concept/grounding
  - rel: depends-on
    target: concept/symbol-grounding-problem
---

# Embodied Cognition and Sensorimotor Theories of Meaning

Embodied cognition is the family of theories in cognitive science and philosophy of mind that hold that meaning, thought, and conceptual structure are constituted — at least in part — by the body's sensorimotor capacities, not only by abstract amodal symbols. The core claim, in its strongest form, is that cognizing *chair* involves (partially) simulating what it would be like to perceive and interact with a chair — not merely activating an arbitrary internal token. The primary in-repo source is [`source/barsalou-1999-perceptual-symbol-systems`](../sources/barsalou-1999-perceptual-symbol-systems.md); the in-repo philosophical ancestor is [`source/harnad-1990-symbol-grounding`](../sources/harnad-1990-symbol-grounding.md). See also [`concept/symbol-grounding-problem`](symbol-grounding-problem.md) for the mechanism-level question.

## The Barsalou perceptual symbol system theory

Barsalou's (1999) perceptual symbol system theory is the most fully developed cognitive-science framework in this tradition. Three ideas are central:

**Perceptual symbols as modal records.** During perception, association areas in the brain capture bottom-up patterns of activation in sensory-motor areas. The resulting memory traces — *perceptual symbols* — remain in the same modal systems that processed the original perception. They are not translations into an amodal format; they are partial re-recordings of the perceptual state itself. As Barsalou states in the abstract:

> "association areas in the brain capture bottom-up patterns of activation in sensory-motor areas. Later, in a top-down manner, association areas partially reactivate sensory-motor areas to implement perceptual symbols." ([`source/barsalou-1999-perceptual-symbol-systems`](../sources/barsalou-1999-perceptual-symbol-systems.md), p. 577)

**Simulators as concepts.** Through repeated perceptual encounters with a category's members, organized perceptual symbols coalesce into a *simulator*: a system capable of producing indefinitely many *simulations* of the category. Simulations are partial, schematic re-enactments of sensory-motor experience — not replays of specific memories but productive reconstructions. A concept, on this account, *is* (in large part) a simulator: the concept CAR is the system that generates varied simulations of car-relevant experience. Simulators develop not only for sensory experience but for proprioception (e.g., *lift, run*) and introspection (e.g., *compare, remember, happy*), giving the theory scope over abstract as well as concrete concepts.

**Full conceptual system from perceptual grounding.** Barsalou argues that simulators, through composition and recursion, support a full conceptual system: productivity (by combining simulators), propositions (by binding simulators to perceived individuals), and abstract concepts (grounded in simulations of combined physical and introspective events). The abstract states the conclusion:

> "a perceptual theory of knowledge can implement a fully functional conceptual system while avoiding problems associated with amodal symbol systems." ([`source/barsalou-1999-perceptual-symbol-systems`](../sources/barsalou-1999-perceptual-symbol-systems.md), p. 577)

## Connection to sensorimotor grounding and Harnad

Barsalou fills in the explanatory gap that [`concept/symbol-grounding-problem`](symbol-grounding-problem.md) identifies. Harnad (1990) asked what *kind* of representations could break the symbol/symbol merry-go-round; Barsalou's answer is: modal records in sensory-motor cortex, organized as simulators. The two theories are not the same — Harnad's "iconic and categorical representations" are more abstractly characterized, while Barsalou's "perceptual symbols" are specified at the neuroscience level — but they belong to the same theoretical family.

Both theories share the key structural commitment: meaning is constituted by causal contact with the world through the sensorimotor system. The causal chain runs from distal object → sensory projection → perceptual record → simulator → conceptual content. This is what the project's `grounded.causal` sub-tag is tracking when it applies to embodiment claims.

## Where embodiment claims make testable contact with model behavior

Most of the embodied cognition literature concerns humans (and sometimes robots with sensorimotor loops). The translation to language models requires care, and the honest statement is that **most embodiment predictions are not directly testable on a text-only model** — and many remain poorly specified even for multimodal models.

Here is a taxonomy of what is and is not testable with current model architectures:

### Testable on a vision-language model (VLM)

- **Perceptual consistency across modalities.** If a VLM has genuine perceptual grounding, its language representations of a concept should be consistent with its visual representations of it. If it says "a lemon is bright yellow" but its vision encoder does not distinguish yellow from grey lemons, the grounding claim is weakened. This is in principle probeable on a VLM with access to both modalities. Whether our project will run this is a separate question.
- **Affordance tracking.** Barsalou's theory predicts that concepts carry action-relevant structure (affordances in the Gibson sense). A grounded VLM might be expected to reason about object manipulability, reachability, or use in ways that track real-world affordance constraints. Whether current VLMs do this, and whether they do it via simulation or via statistical regularity in the training data, is not settled.
- **Simulation-based inference blocking.** If concepts are simulators, blocking the simulation should impair inference. Dual-task paradigms in humans (occupy working memory during conceptual processing → impair simulation → impair inference) have no obvious analogue in model probing, so this prediction is not testable in the standard way.

### Not testable on a text-only model (and only indirectly on a VLM)

- **Modal reactivation of sensory-motor cortex.** The neuroscience core of Barsalou's theory — that the same cortical areas active in perception are reactivated during conceptual processing — is by definition not testable on a language model. It is a claim about biological neural architectures.
- **Grounding in proprioception.** Concepts of action (lift, run) are grounded in proprioceptive records in Barsalou's theory. A text model has no proprioception; a VLM has no proprioception either. This part of the theory is simply inapplicable.
- **The intrinsic/extrinsic distinction.** Harnad's strongest claim is that without sensorimotor grounding, all symbol interpretations remain extrinsic (supplied by the interpreter). Whether a model's representations are intrinsically or extrinsically meaningful is not directly observable from the model's behavior — the question "is this intrinsic or parasitic?" is philosophical, not probeable via prompting.

### The calibration warning

Any finding tagged `grounded.perceptual` in this project should carry an explicit acknowledgement that demonstrating good performance on a perceptual task (e.g., visual question answering, affordance queries) is **not the same as** demonstrating that the model has Barsalou-style modal simulators. Statistical regularity in training data can support good behavior on many perceptual probes without grounding in the theoretical sense. The distinction between "the model gets the right answer" and "the model has a perceptual symbol system" is exactly the Harnad regress re-stated for model behavior: the right answer could be correct for purely distributional reasons.

## The externalist gap

The project's `referential.externalist` sub-tag (Putnam/Evans) is no longer characterization-only — the externalist primaries are now substantially in-repo: [`source/putnam-1975-meaning-of-meaning`](../sources/putnam-1975-meaning-of-meaning.md) (session 110), [`source/evans-1973-causal-theory-of-names`](../sources/evans-1973-causal-theory-of-names.md) and [`source/burge-1979-individualism-and-the-mental`](../sources/burge-1979-individualism-and-the-mental.md) (both session 111; the session-111 correction on [`concept/referential-meaning`](referential-meaning.md) records that Evans *rejects* the pure baptism-chain picture — reference tracks the dominant causal source of a community's body of information). Only **Kripke**, the baptism-chain pole Evans criticizes, remains not-in-repo (queued in [`wiki/base/wanted.md`](../wanted.md)); these are theory sources, not human anchors, so the missing reference-*resource* gap stands. Embodiment and externalism are related but distinct: the externalist holds that reference is fixed by causal-historical chains and social facts *external to the individual*; the embodied cognition theorist holds that concepts are constituted by *individual* sensorimotor states. Harnad's account is closer to the externalist — the grounding is by causal contact with the world — but Barsalou's focus is on individual simulation, making it more internalist (the records are in the individual brain).

The practical import for this project: the `grounded.causal` sub-tag can be used for both Harnad-style causal-contact stories and Lyre-style world-model stories, but the `referential.externalist` question (Twin Earth, division of linguistic labor) is a separate axis that embodiment does not close. A model that has sensorimotor grounding in some sense might still fail the externalist criterion — its "water" might refer to H₂O in its training data without the model being in the causal-social chain that fixes what "water" refers to in human linguistic practice. These are the **empirical cousin** and the **un-anchored philosophical question** respectively, and they should not be conflated.

This wiki records that embodiment/grounding is the empirical cousin of the externalist question — the two overlap (both require something beyond distributional form) but neither subsumes the other. The Putnam and Evans (and Burge) sources are now ingested (sessions 110–111, above), and the relationship is made precise on [`concept/referential-meaning`](referential-meaning.md) (its internalism/externalism section and the grounding-nulls reading).

## Summary of sub-tag assignments

| Claim type | Tag |
|---|---|
| Concepts constituted by modal simulation (Barsalou) | `grounded.perceptual` |
| Causal contact with world via sensorimotor loop (Harnad) | `grounded.causal` |
| Multimodal model's perceptual representations (VLM probing) | `grounded.perceptual` |
| Reference fixed by causal-historical chain (Putnam/Evans) | `referential.externalist` (primaries in-repo, sessions 110–111; still no reference-*resource* anchor) |
| Joint action, shared norms, social grounding (not covered here) | `grounded.social` |
