---
type: source
id: guo-2026-statistical-preemption
title: "Do Language Models Know What Not to Say? Causal Evidence for Statistical Preemption in LLMs"
authors:
  - Guo, Dongxin
  - Wu, Jikun
  - Yiu, Siu Ming
year: 2026
venue: "CoNLL 2026 (accepted; per arXiv comments). Preprint arXiv 2605.23039 (cs.CL)"
arxiv: "2605.23039"
doi: 10.48550/arXiv.2605.23039
url: https://arxiv.org/abs/2605.23039
access: open-access
meaning-senses:
  - constructional
  - distributional
  - inferential
status: received
created: 2026-07-17
updated: 2026-07-17
links:
  - rel: refines
    target: concept/constructional-meaning
  - rel: supports
    target: concept/distributional-meaning
---

# Guo, Wu & Yiu 2026 — Do Language Models Know What Not to Say? Causal Evidence for Statistical Preemption in LLMs

## What it is

A three-author computational-linguistics paper (arXiv 2605.23039; cs.CL; accepted at CoNLL 2026 per the arXiv comments) that asks whether language models acquire **negative** constructional knowledge — knowing that a form like *\*She explained him the problem* is not conventional — through **statistical preemption**, the indirect-negative-evidence mechanism Construction Grammar posits for human learners (see [`source/goldberg-2006-constructions-at-work`](goldberg-2006-constructions-at-work.md)). It runs four experiments across argument-structure alternations (dative, causative, locative): (1) LLM surprisal differentials vs human acceptability; (2) a regression separating a corpus-derived **preemption** score from raw **entrenchment** (verb frequency); (3–4) a **causal fine-tuning** intervention that manipulates competing-form frequency and observes the shift in the model's constructional preference. Its headline is that models capture "the distributional signature of statistical preemption," and that fine-tuning on the competing-form variable causally shifts the behavior.

This is a **behavioral + causal-intervention** study on **non-project open-weight models** (14 models across GPT-2, Pythia, LLaMA-2, OLMo). Like [`source/diera-2026-encode-semantic-relations`](diera-2026-encode-semantic-relations.md), it is catalogued as a **map and external-evidence counterpoint** to the project's own behavioral panel work — **not** a method the project uses, **not** evidence about the project's frontier panel, and **not** a human anchor (see "What it cannot ground"). Its specific value here is that it **externally instantiates the "preemption-vs-productivity probe" that [`theory/statistical-preemption-and-constructional-productivity`](../../findings/theory/statistical-preemption-and-constructional-productivity.md) named as owed but "not designed,"** and that its own read of the result independently reproduces that theory page's load-bearing bound.

## Provenance

Title, full author list, subject category (cs.CL), the "accepted at CoNLL 2026" comment, and the abstract were fetched from the arXiv abs page (https://arxiv.org/abs/2605.23039) on 2026-07-16 and verified. Body quotes (experiment structure, the r-value, the regression coefficients, the fine-tuning effect, the mechanism and non-adjudication sentences, the Limitations caveat) were extracted from the arXiv HTML full text (https://arxiv.org/html/2605.23039v1) on the same date. The two load-bearing sentences — the Abstract's "distributional competition" conclusion and the §8.2 non-adjudication passage — were re-fetched and confirmed character-for-character. **No published-proceedings page numbers** (the CoNLL 2026 camera-ready is not yet in the ACL Anthology), so locators below are **section numbers from the arXiv HTML**, not pages.

## Abstract highlight and the design

**The mechanism conclusion (Abstract, verbatim):**

> "These results provide converging evidence that neural language models acquire negative linguistic knowledge through distributional competition, the core mechanism posited by Construction Grammar."

**The stimulus set (§3.1, verbatim):**

> "120 verb–construction items organized along two dimensions: preemption strength (strong, weak, none) and construction type (dative, causative, locative)"

(Per the paper's breakdown: 80 dative, 20 causative, 20 locative items.)

**The models (§3.3, verbatim):**

> "14 models from four families: GPT-2 (124M, 355M, 774M, 1.5B), Pythia (160M, 410M, 1B, 2.8B, 6.9B, 12B), LLaMA-2 (7B, 13B, 70B), and OLMo (7B)"

**What preemption is, in the authors' framing (§1, verbatim):**

> "Preemption requires exposure to a specific competing form with the same communicative function"

## Key findings (verbatim; section locators from the HTML)

**(1) Surprisal tracks human acceptability (§4.3):**

> "LLaMA-2 7B achieves r=0.79 [0.69, 0.86] (p<.001, n=80 verbs)"

(Per-verb surprisal differentials correlated against DAIS human acceptability ratings; the paper reports validation against three independent human datasets — DAIS, Robenalt & Goldberg, Tachihara & Goldberg — not a fresh human-annotation instrument.)

**(2) Competing-form frequency, not raw verb frequency, is the driver (§5.3–§5.4):**

> "The preemption score is the dominant predictor (β=3.41, SE=0.31, t=11.0, p<.001), while entrenchment contributes modestly (β=0.19, SE=0.06, t=3.17, p=.003)."

> "Controlling for Entrench(v), corpus-derived Preempt(v) predicts DAIS human ratings with r_partial=0.58 [0.42, 0.71] (p<.001)"

**(3) The causal fine-tuning intervention (§7.2):**

> "The Amplified condition increases ΔS by 0.73 ± 0.07 bits (all 5 seeds positive, range [+0.66, +0.84])"

The authors summarize the causal claim (§8.1, verbatim):

> "Our central finding, that LLMs trained on English text capture the distributional signature of statistical preemption, and that manipulating the relevant distributional variable in fine-tuning data shifts behavior in the predicted direction"

## The authors' own bound — the load-bearing passage for this project

The paper explicitly declines to read its result as settling *how* the model got the behavior (§8.2, verbatim):

> "we do not read our results as adjudicating between usage-based and formal accounts: that LLMs trained on distributional input reproduce the empirical signature of preemption is compatible with both a usage-based reading (distributional learning over constructional alternatives directly drives the effect) and a structured-regularities reading (the model internalizes abstract verb-class generalizations correlated with preemption strength)."

And, on the causal experiment specifically (Limitations, verbatim):

> "Fine-tuning does not reconstruct developmental learning. Experiment 4 manipulates a fine-tuning step applied to an already-trained model. This is causal evidence that LLM constructional preferences are continuously sensitive to relative competing-form frequency, but it does not recreate the developmental trajectory by which preemption preferences are originally acquired."

## What this bears on in-repo

- **[`theory/statistical-preemption-and-constructional-productivity`](../../findings/theory/statistical-preemption-and-constructional-productivity.md) — the primary bearing.** That page maps Goldberg's two learning levers (productivity, preemption) onto the project's results, finds the record has **no isolated preemption test** (only *preconditions* — cancellability and form-keying), and names a "preemption-vs-productivity probe" as a **framing for a future probe, not designed**, whose whole difficulty is engineering a frequency control that lets a *meaning-conditioned* blocking be distinguished from a *frequency-conditioned* one. Guo, Wu & Yiu run essentially that isolated preemption test on a non-project model set, and land on the **frequency-conditioned side**: their operationalization of preemption, `Preempt(v)`, is a **corpus-derived competing-form-frequency score**; their causal handle is on that distributional variable. And their §8.2 non-adjudication sentence is **the theory page's own sharp bound, reached independently** — reproducing preemption's empirical signature is "compatible with both" a usage-based and a structured-regularities mechanism. So the paper is external corroboration of the theory page's guardrail (a preemption match is not evidence of a particular learning mechanism), not a defeater of it.
- **[`concept/constructional-meaning`](../concepts/constructional-meaning.md) — `refines`.** A concrete, causal, multi-model measurement of the *constraint* side of constructional productivity (negative knowledge / blocking), complementing the project's productivity-side (held-out-generalization) hooks.
- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md) — `supports`.** Evidence that a specifically **distributional** variable (competing-form frequency) causally carries the preemption signature — a data point on the concept's live question of how much constructional behavior reduces to co-occurrence structure.
- **The argument-structure alternation battery** ([`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md), [`claim/genitive-alternation-animacy`](../../findings/claims/genitive-alternation-animacy.md), [`claim/particle-placement-givenness`](../../findings/claims/particle-placement-givenness.md)). The project probes the *positive/gradient* direction of the dative (and genitive, particle) alternations (which alternant is preferred under an information-structural manipulation); this paper probes the *negative* direction of the dative/causative/locative alternations (which alternant is dispreferred as non-conventional). The two are companion faces of the same alternations; the paper is a distributional-mechanism counterpoint, not a replication of any project result.

## What it can ground

- A citation that, across 14 open-weight models (GPT-2, Pythia, LLaMA-2, OLMo), LLM surprisal differentials on dative/causative/locative items **correlate with human acceptability** (LLaMA-2 7B r=0.79 [0.69, 0.86], n=80 dative verbs), that a **corpus-derived competing-form preemption score dominates raw verb entrenchment** as a predictor, and that a **fine-tuning intervention on competing-form frequency causally shifts** the model's constructional preference (Amplified +0.73 bits ΔS) — all verbatim as above.
- A citation for the authors' framing that models capture "the distributional signature of statistical preemption" via "distributional competition, the core mechanism posited by Construction Grammar" (Abstract + §8.1).
- A citation for an **external, independent statement of the project's own bound**: that reproducing the behavioral signature of preemption "is compatible with both a usage-based reading … and a structured-regularities reading" (§8.2) — usable wherever the project needs to show its meaning-vs-mechanism caution is not idiosyncratic.

## What it cannot ground

- **Any claim about the project's frontier panel.** The models here (GPT-2 through LLaMA-2-70B / OLMo-7B) are open-weight models chosen for surprisal access and fine-tuning tractability, **not** the project's panel in [`config/models.md`](../../../config/models.md). No transfer to claude/gemini/gpt is established; the project's own preemption bet stays un-run on its panel.
- **A human anchor.** The paper *validates against* existing human datasets (DAIS, Robenalt & Goldberg, Tachihara & Goldberg) but is itself a model-behavior/intervention study, not a standalone human-labeled asset licensed and ingested as a project resource. It is **not a human anchor** and must not be cited as one; the dative line's human anchor remains the project's own corpus-production resources.
- **That any model "learned like a human."** The authors themselves decline this (§8.2, Limitations): the causal result shows sensitivity to *competing-form frequency*, a distributional variable, and does "not recreate the developmental trajectory by which preemption preferences are originally acquired." Do not cite the paper as evidence that the meaning-conditioned mechanism Goldberg posits for children is what a model runs.
- **A mechanistic (representational) bridging law.** The fine-tuning intervention is on *training data frequency*, not on an internal verbalizable representation; the paper does not fire the project's mechanistic-behavioral-firewall trigger (which requires a mechanistic-representation intervention predicting a behavioral residual out-of-sample). It is a data-side causal result, not a mechanism-side one.

## Known limits

- **Peer-review / provenance status:** accepted at CoNLL 2026 per the arXiv comments; the camera-ready proceedings were not consulted, so all locators are **section numbers from the arXiv HTML**, not published pages. Quotes were HTML-extracted 2026-07-16; the two load-bearing sentences were re-verified.
- **Non-project models only.** Nothing here speaks to the project's panel; cross-model transfer to frontier models is unverified.
- **Preemption operationalized as competing-form frequency.** `Preempt(v)` is a corpus co-occurrence statistic, not a direct measure of the *meaning-conditioning* Goldberg's account turns on; the paper's own §8.2 flags that the behavioral signature underdetermines the mechanism. Cite the causal frequency result, not a meaning-conditioned-learning conclusion the paper explicitly declines.
- **Causal ≠ developmental.** Experiment 4 fine-tunes an already-trained model; it is causal evidence of continuous sensitivity to competing-form frequency, not a reconstruction of acquisition (authors' Limitations).

## Status in wanted.md

Not previously listed by id. Catalogued 2026-07-17 (session 240) as external empirical/causal evidence on the statistical-preemption question — the outside-run instance of the preemption-vs-productivity probe the project's theory page named as owed-but-undesigned. The orchestrating session records it in [`wanted.md`](../wanted.md)/[`index.md`](../../index.md) as RECEIVED.
