---
type: open-question
id: constructional-vs-frequency-confound
title: How do we separate constructional-meaning sensitivity from an n-gram/frequency confound in surprisal-contrast probes?
meaning-senses:
  - constructional
  - distributional
  - inferential
status: answered
created: 2026-05-28
updated: 2026-07-02
links:
  - rel: depends-on
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: conjecture/aann-construction
  - rel: depends-on
    target: conjecture/function-word-substitutability
---

# Open question: constructional meaning vs. the frequency confound

> **Answered (closed as a founding question) 2026-07-02, session 170 — see the closure argued in
> [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) § "Closing the two founding
> open-questions".** The deliverable this page demanded — *name the discriminating move the project treats as
> load-bearing, and write it where it cannot be quietly relaxed* — is met by the continuum's **shadow-control
> apparatus**. Because the panel is closed-weight, the project could not adopt move (1) as literally written
> (proxy-corpus frequency residualization) and instead committed to the **behavioral analogue of moves (4)+(1)**:
> a **matched control that reuses the construction's own surface material** (so a frequency-only account predicts
> no gap), against which a **residual is measured with an interval**. Worked exemplar: the comparative correlative
> — CC items assert covariation ~100%, matched non-CC controls reusing the *same scalar words* ~12%, a
> construction-isolation gap **≈87 pp [95% CI lb ≈78]**, 136 fresh disjoint items, 3/3 models, verifier-reproduced
> ([`result/comparative-correlative-covariation-powered`](../results/comparative-correlative-covariation-powered.md);
> promoted to [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md)).
> The **residual live bound** the question named (a rich latent n-gram interpolation could still reconstruct the
> residual; the control is behavioral-same-material, not a proxy-corpus frequency model) is now a **known caveat
> carried on each result**, not an unanswered founding question. Body kept below unchanged.

## The question

Every surprisal-contrast probe in this project's constructional wedge ([`conjecture/aann-construction`](../conjectures/aann-construction.md), [`conjecture/way-construction`](../conjectures/way-construction.md), [`conjecture/caused-motion-construction`](../conjectures/caused-motion-construction.md), [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md)) shares one threat: when a model assigns lower surprisal to a licit construction than to an illicit minimal-pair variant, that gap is consistent with **two** explanations that the probe does not, by itself, distinguish:

1. The model has acquired the **form–meaning pairing** — it tracks the construction as a `constructional` unit with characteristic semantics (the project's claim).
2. The model is tracking **surface co-occurrence statistics** — the licit string is simply more probable n-gram-by-n-gram in the training distribution (the `distributional` deflation of the claim).

What is the minimal additional evidence that licenses concluding (1) rather than (2)? Concretely: what design move turns a surprisal gap from "consistent with constructional sensitivity" into "not explainable by frequency alone"?

## Why it matters

This is the load-bearing methodological question for the entire constructional program. If it is not answered, every confirmed conjecture in the wedge is vulnerable to the one-line objection "you measured n-gram frequency, not meaning," and no `result` can be promoted past `weak` (see the "Weak" branches across the project's constructional conjectures, which are exactly this confound). The charter's `distributional`-vs-`constructional` boundary ([`meaning-senses.md`](../../meaning-senses.md)) is contested precisely here. Resolving the question is what lets a result discriminate between the two camps instead of being claimed by both.

## Why it is hard

- **Frequency is not directly observable for closed LLMs.** We cannot inspect the training distribution of most panel models, so "matched frequency" must be estimated from a proxy corpus (COCA/BNC/UD/an open-pretraining-corpus n-gram model). The proxy may diverge from the model's actual distribution, so a "frequency-matched" pair may still differ in the model's true statistics.
- **Generalization and frequency are entangled.** The standard defense — show the effect on **held-out / novel lexical items** (held-out adjectives for AANN, novel non-motion verbs for caused-motion) — weakens the confound but does not eliminate it: a sufficiently rich n-gram/skip-gram model can interpolate to unseen items via partial overlap, so "novel" is a matter of degree, not a clean separation.
- **The constructional account predicts frequency.** Goldbergian CxG expects productive constructions to *be* frequent and to *shape* the distribution. So frequency and constructional meaning are not rival causes at the same level; the confound is about whether the model represents the pairing or only its statistical shadow. A naive "regress out frequency" can therefore regress out the very signal of interest.
- **Surprisal conflates levels.** A single surprisal number bundles lexical, syntactic, and constructional contributions; isolating the construction's contribution requires a contrast design that holds the other levels fixed, which is exactly what is hard to guarantee.

## What a serious answer would look like

A discriminating design would do at least one of the following, and ideally several converging:

1. **Frequency-residualized contrast.** Fit the construction-vs-control surprisal gap as a function of a proxy-corpus frequency estimate (n-gram model, or the construction skeleton's corpus count), and test whether a **residual** gap survives once the frequency predictor is partialled out. A surviving residual is evidence for (1). Pre-register the proxy and the frequency model **before** seeing results.
2. **Novel-element generalization with a frequency floor.** Use lexical items whose proxy-corpus frequency in the construction is at or near zero (genuinely novel verb/adjective in the slot), and show the entailment/acceptability gap persists. The closer to a true frequency floor, the harder the n-gram explanation.
3. **Meaning-side dissociation, not just form-side.** The strongest move: show the model tracks an inference that frequency cannot encode. E.g., for caused-motion, the **causation** entailment ("her sneezing caused it") does not follow from the `V NP PP` n-gram skeleton at all; an inferential probe that isolates causation from mere co-occurrence is frequency-orthogonal by construction. This is why several conjectures co-tag `inferential` — the inferential probe is the escape from the frequency confound.
4. **Adversarial frequency-matched illicit controls.** Construct illicit variants that are *more* frequent as raw strings than the licit construction (e.g., a high-frequency but non-constructional reordering), so that a frequency-only model predicts the *wrong* sign. If the model still prefers the licit construction, frequency is ruled out as the sole driver.
5. **Cross-model decorrelation.** If the gap tracked raw frequency, models trained on overlapping web text should converge tightly on it. Systematic cross-model *divergence* that does not track training-corpus overlap is weak evidence that something beyond shared n-gram statistics is being computed (this is the "decorrelation" angle already noted in the conjectures).

A satisfying answer names which of these the project will treat as **necessary** for promoting a constructional `result` past `weak`, and writes that threshold into a decision page so it cannot be quietly relaxed after seeing a null.

## Relation to the existing wedge

This question generalizes the "Weak" / memorization branches already written into the project's constructional conjectures (aann, way, function-word, caused-motion, conative, comparative-correlative) and the operationalization-gate notes in [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) and [`conjecture/caused-motion-construction`](../conjectures/caused-motion-construction.md). It is the natural **method spine** that a future loop turn should resolve once, then reuse across probes — rather than re-litigating the confound per conjecture.

## Pointers for the next visit

- `decisions/open/constructional-frequency-control.md` (to be opened when this is picked up) — pick the proxy corpus + frequency model, and fix which of moves (1)–(5) is the project's promotion criterion.
- Check whether any panel model exposes log-probs at the token level (needed for clean surprisal contrasts) vs. only API-level likelihoods.
- Read the SyntaxGym / BLiMP methodology notes on frequency controls; they have partial machinery for matched minimal pairs that may be reusable rather than rebuilt.
