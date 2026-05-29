---
type: open-question
id: distributional-vs-inferential-constructional
title: What minimal evidence separates distributional from inferential constructional sensitivity?
meaning-senses:
  - constructional
  - distributional
  - inferential
status: open
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
  - rel: depends-on
    target: conjecture/conative-construction
  - rel: depends-on
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: conjecture/way-construction
---

# Open question: distributional vs. inferential constructional sensitivity

## The question

Suppose [`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md) is answered and we have established that a model's behavior on a construction is **not** reducible to raw n-gram frequency — the model is genuinely sensitive to the construction as a unit. A second, finer question remains, and it is *not* the same question.

Granting that a model is constructionally sensitive, that sensitivity could be either of two kinds:

1. **Distributional constructional sensitivity** — the model represents the construction as a *characteristic distribution*: which lexical items fill which slots, what typically precedes and follows, what continuations are likely. The form–meaning pairing is encoded as the pairing's distributional signature. The model "knows the construction" the way it knows a collocation: as a richly structured but ultimately *predictive* pattern.
2. **Inferential constructional sensitivity** — the model represents the construction as *licensing inferences*: from a caused-motion instance, that the object moved and the subject caused it; from a conative instance, that contact was *not* necessarily completed. The form–meaning pairing is encoded as a set of entailments the construction supports and cancels, in the Brandomian / conceptual-role sense ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), [`source/piantadosi-hill-2022-meaning-without-reference`](../../base/sources/piantadosi-hill-2022-meaning-without-reference.md)).

What is the minimal additional evidence that licenses concluding (2) rather than (1)? Concretely: what design move turns "the model tracks the construction's distribution" into "the model tracks the construction's inferential role"?

## Why it matters

The project's conjectures co-tag `constructional` with both `distributional` and `inferential`, and several (`way`, `caused-motion`, `conative`) carry an *inferential probe* as their confirmation criterion precisely to reach for sense (2). But an inferential probe ("did the napkin move? Y/N") does not by itself secure (2): a model could answer correctly because the *answer text* is distributionally likely given the prompt, not because it computes the entailment. So the inferential probe risks being a distributional probe wearing a meaning-shaped mask.

This is the wedge that bears on the charter's contested `distributional`/`inferential` boundary ([`meaning-senses.md`](../../meaning-senses.md) Open issue: "Should `distributional` and `inferential` collapse, given that next-token prediction is implicitly inferential? Probably no — but write the case explicitly when it next matters."). This question is where it next matters. An answer tells us whether the constructional wedge can ever produce evidence that bites *inferentialism specifically*, or whether it can only ever certify distributional structure under a different name.

## Why it is hard

- **Inference and likelihood are entangled by the objective.** A next-token model produces a "yes" because "yes" is the high-probability continuation. If correct entailments are also distributionally likely continuations (they usually are — true things are said more often), then correct inferential behavior and good distributional fit are observationally identical on a single probe. The two senses predict the *same* answer in the easy cases.
- **The distinguishing cases are the rare ones.** The senses diverge only where the inferentially-licensed answer is distributionally *dispreferred*, or vice versa — exactly the low-frequency, adversarial, or coercion items that are noisiest and where models are least reliable. So the discriminating evidence lives where measurement is worst.
- **"Inferential role" has no single ground truth in text.** Unlike acceptability (which has human norms) or frequency (which has a proxy corpus), the *set of inferences a construction licenses* is theory-laden. Goldbergian CxG, Brandomian inferentialism, and a truth-conditional account will not always agree on what follows. The anchor problem is therefore sharper here than for the frequency confound.
- **Behavioral probes underdetermine representation.** Even a model that answers every entailment probe correctly might do so via a shortcut that is distributional under the hood. Distinguishing (1) from (2) may require representational evidence (probing classifiers, causal interventions on internal states), which moves the question from `constructional`+behavioral to `model-internal` and brings its own validity problems.

## What a serious answer would look like

A discriminating design would do at least one of the following, ideally several converging:

1. **Inference under distributional pressure (the core move).** Construct items where the construction *licenses* an inference whose surface answer is the **dispreferred** continuation — e.g. a caused-motion sentence where "no, it did not move" is the locally fluent completion but the construction entails it did. If the model follows the construction against the local distributional gradient, that is evidence for (2). This is the inferential analogue of the "adversarial frequency-matched control" in [`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md), but at the entailment level rather than the form level.
2. **Inference transfer across surface forms.** Show the model draws the *same* entailment from the construction across paraphrases / surface realizations that share the construction but differ distributionally (active/passive, different fillers, embedded vs. matrix). A distributional account predicts the entailment behavior to vary with surface distribution; an inferential account predicts it to track the construction. Convergent entailment across divergent surface forms is the signature of inferential role.
3. **Inference cancellation / defeasibility sensitivity.** Inferential role includes knowing when an inference is *cancelled*. The conative's whole point ([`conjecture/conative-construction`](../conjectures/conative-construction.md)) is that the *at*-frame **cancels** the completed-contact entailment that the transitive carries. A model that tracks *when an entailment is withdrawn* — not just when it holds — is doing something a flat distributional similarity cannot easily mimic, because cancellation is a structural property of the construction, not a co-occurrence fact.
4. **Mutual-information / answer-symmetry test.** For a genuine entailment, the construction should shift the *answer distribution* asymmetrically (toward "moved") even when the question is phrased to make "did not move" the lexically primed answer. Compare the model's answer under entailment-consistent vs. entailment-inconsistent question phrasings; an inferential model is robust to phrasing, a distributional model swings with it.
5. **Representational corroboration (secondary, `model-internal`).** Where token log-probs or activations are available, test whether an entailment-predictive internal signal exists that is separable from a frequency/continuation-predictive one. Treat this as corroborating, not load-bearing, given the representation-underdetermination problem above.

A satisfying answer names which of these the project treats as **sufficient** to tag a `result` `inferential` (as opposed to `distributional`-only), and writes that criterion into a decision page so the inferential tag cannot be applied on the strength of a probe that any distributional model would also pass.

## Relation to the existing wedge

This question is **downstream** of [`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md), not a duplicate of it. That question asks whether a *form-level* surprisal gap is more than n-gram frequency (constructional vs. distributional at the level of *form*). This question assumes that is settled and asks whether the *meaning-level* behavior is genuine inferential-role tracking or distributional shadow (inferential vs. distributional at the level of *meaning*). The frequency confound is about whether the model sees the construction at all; this is about what *kind* of meaning it computes once it does. Both feed the promotion criterion for any constructional `result` that wants to claim the `inferential` tag rather than only `distributional`.

## Pointers for the next visit

- `decisions/open/inferential-tag-criterion.md` (to be opened when this is picked up) — fix which of moves (1)–(5) is necessary to apply the `inferential` meaning-sense to a constructional `result`, vs. `distributional`-only.
- The conative ([`conjecture/conative-construction`](../conjectures/conative-construction.md)) is the most favorable first testbed because its entailment is a **cancellation**, which move (3) targets directly and which is hardest for a distributional account to fake.
- Re-read [`source/piantadosi-hill-2022-meaning-without-reference`](../../base/sources/piantadosi-hill-2022-meaning-without-reference.md) for the conceptual-role / inferentialist framing of what "the inference a construction licenses" even means, and check whether it commits to a ground truth for inferential role that this project can borrow.
- Check whether any panel model exposes token-level log-probs (needed for moves 1 and 4) vs. only categorical Y/N outputs.
