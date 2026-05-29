---
type: conjecture
id: conative-construction
title: LLMs track the non-completion / attempted-contact meaning of the conative alternation
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
contingent-on:
  - conative-anchor
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
---

# Conjecture: LLMs track the conative alternation's non-completion meaning

## Statement

The English **conative construction** is the *at*-marked oblique variant of certain transitive verbs of contact and motion-toward-contact: *Maria kicked **at** the ball* vs. the direct-object transitive *Maria kicked the ball*; *He bit **at** the apple* vs. *He bit the apple*; *She slashed **at** the rope* vs. *She slashed the rope*. The alternation is a classic Levin (1993) diagnostic and a Construction-Grammar form–meaning pairing: the conative `Subj V at Obl` frame carries an **"attempted / directed-at but not necessarily completed contact (or effect)"** semantics, while the transitive `Subj V Obj` frame entails completed contact and (often) an effect on the object.

The discriminating inference: from *She kicked at the ball* it does **not** follow that the ball was contacted or moved; from *She kicked the ball* it does. The semantic difference is carried by the construction (presence/absence of *at* + oblique vs. direct object), not by the verb, which is held constant across the pair.

The conjecture: current LLMs draw the **non-completion / attempted-contact** inference from conative `V at NP` instances and the **completed-contact** inference from the matched transitive `V NP` instances, at a rate that separates the alternation from minimally different controls — i.e. they treat the *at*-frame as a meaning-bearing construction, not as a stylistic paraphrase of the transitive.

This is distinct from the other argument-structure conjectures in the wedge. [`conjecture/caused-motion-construction`](caused-motion-construction.md) and [`conjecture/way-construction`](way-construction.md) test whether the construction *adds* an entailment the verb cannot license (motion/causation from non-motion verbs). The conative tests the converse: whether the construction *removes* / *weakens* an entailment (completed contact) that the bare transitive carries, with the **same verb** in both frames. It probes whether the model reads telicity / affectedness off the argument-structure construction rather than off the verb's lexical aspect.

## Why this is interesting

- The verb is held **constant** across the minimal pair; only the construction (direct object vs. *at*-oblique) varies. So a difference in the completion entailment cannot come from the verb's lexical entry — it must be `constructional`. This is a cleaner verb-control than caused-motion (where the verb also changes valence).
- It bites the `inferential` side precisely: confirmation requires the model to treat the conative as *cancelling* the completed-contact entailment (an inference about telicity/affectedness), not merely as producing fluent text or assigning a likelihood gap.
- It exposes the `constructional`-vs-`distributional` tension (see [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md)) with an unusually favorable design: because the two frames share the verb and most lexical material, raw unigram frequency is nearly matched, and the surviving signal is more plausibly the construction's contribution. The *at*-frame is also markedly **lower-frequency** than the transitive, which lets a frequency-only account make a falsifiable wrong prediction (see Predictions 3).

## Predictions

1. Given an inferential probe ("After 'She kicked at the ball', did the ball move / was it contacted? Y/N"), conative items yield a substantially **lower** completed-contact "yes" rate than the matched transitive items (*She kicked the ball*), with the verb held constant.
2. The contrast is **graded by verb class**: it is sharpest for verbs that license the conative on a contact-by-motion semantics (*kick*, *hit*, *slash*, *bite*) and weak/absent for verbs that do not enter the conative at all (*touch*, *break* — *#bite at* vs. *touch* contrasts), tracking the Levin alternation-class inventory rather than applying uniformly.
3. **Frequency-orthogonal check:** despite the *at*-conative being the lower-frequency surface string, the model still assigns it the non-completion reading. A purely distributional/n-gram account predicts the higher-frequency transitive reading to leak in (over-reporting completed contact for conative items); a constructional account predicts the model holds the non-completion reading for the *at*-frame regardless.
4. Panel divergence: the non-completion inference is recovered more cleanly in models that also handle the caused-motion and `way`-construction inferences, suggesting a shared argument-structure-construction competence rather than item-specific memorization.

## What would confirm / falsify

- **Confirm:** completed-contact "yes" rate for conative `V at NP` items is >=30pp **below** the matched transitive `V NP` items, holding with the verb constant and replicating across the Levin conative-class verbs (not a single verb), in >=2 of 3 panel models, against a human-anchored conative-class inventory (anchor pending; see below).
- **Weak:** a gap exists but tracks the *at*-oblique's lexical association with non-completion (the model is reading *at* as a generic atelic marker) rather than the verb-specific conative alternation — or the effect holds only for canonical high-frequency items (*kick at the ball*) and collapses on held-out verbs/objects.
- **Falsify:** flat completed-contact rate across conative and transitive frames (model treats *at* as a stylistic variant); or a rate that tracks the unigram/bigram frequency of the surface string alone, with no residual once frequency is matched. A clean null here is a positive result for the `distributional` position and must be written as such (charter §8).

## Human anchor (pending)

No in-repo resource currently covers the conative alternation with item-level human acceptability or entailment ratings. The canonical *inventory* is Levin (1993, §1.3 / the "Conative Alternation" class) — a descriptive verb-class list, **not** rated stimuli; it certifies *which verbs* enter the conative, which is the load-bearing premise for Prediction 2, but gives no gradient acceptability or entailment norms. Until a usable empirical anchor is in-repo and inspected, this conjecture carries `anchor: pending`.

→ Open decision queued: [`decisions/open/conative-anchor`](../../../decisions/open/conative-anchor.md) — which human-anchored resource grounds the probe (a rated conative/telicity-completion stimulus set if one is public; else VerbNet/Levin verb-class membership as a partial anchor for the verb-class premise; else defer + queue a wanted-resource request).

## Notes / caveats

- *at* is polysemous (locative, temporal, conative). Control by holding the verb in a contact-by-motion semantic class so the only available *at*-reading is conative; exclude locative-*at* readings (*looked at*) from the stimulus set.
- The completed-contact entailment is itself defeasible in the transitive for some verbs (you can *hit at* and *hit*; *hit the wall* strongly entails contact). Anchor the confirmation criterion on verbs where the transitive's completion entailment is robust.
- Probe phrasing matters; trial multiple phrasings **before** seeing results, then commit (charter §8 operationalization gate).
- Frequency is handled jointly with [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md); lock the frequency-matching and the verb-class membership list **before** running.
