---
type: source
id: barrie-tornberg-2025-data-leakage
title: "Emergent LLM behaviors are observationally equivalent to data leakage (with the Ashery et al. reply)"
authors:
  - Barrie, Christopher
  - Törnberg, Petter
reply-authors:
  - Flint Ashery, Ariel
  - Aiello, Luca Maria
  - Baronchelli, Andrea
year: 2025
venue: arXiv preprint (cs.CL), critique + authors' reply
arxiv: "2505.23796"
reply-arxiv: "2506.18600"
url: https://arxiv.org/abs/2505.23796
reply-url: https://arxiv.org/abs/2506.18600
access: open-access
meaning-senses:
  - relational
  - distributional
  - model-internal
status: received
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: contradicts
    target: source/ashery-2025-llm-conventions
---

# Barrie & Törnberg 2025 — Emergent LLM behaviors are observationally equivalent to data leakage (with the Ashery et al. reply)

## What it is

A two-sided open-access exchange on arXiv (both cs.CL) about whether the convention-formation dynamics in [`source/ashery-2025-llm-conventions`](ashery-2025-llm-conventions.md) are *genuinely emergent* or an artifact of training-data memorization. This page catalogues **both** the critique and the authors' reply, because the project's relational-axis caveat (see [`wanted.md`](../wanted.md)) requires reading both before any in-repo finding leans on the *emergence* — rather than the mere *occurrence* — of LLM conventions.

1. **The critique.** Barrie, C. & Törnberg, P., "Emergent LLM behaviors are observationally equivalent to data leakage," arXiv 2505.23796v1 (submitted 2025-05-26). Authors: Christopher Barrie, Petter Törnberg.
2. **The reply.** Flint Ashery, A., Aiello, L.M. & Baronchelli, A., "Reply to 'Emergent LLM behaviors are observationally equivalent to data leakage,'" arXiv 2506.18600v1 (submitted 2025-06-23). Authors: Ariel Flint Ashery, Luca Maria Aiello, Andrea Baronchelli (the same three authors as the original *Science Advances* result).

Provenance: both abstracts verified character-for-character against their arXiv abstract pages (`https://arxiv.org/abs/2505.23796` and `https://arxiv.org/abs/2506.18600`, fetched 2026-06-13). Body quotes verified verbatim against the arXiv HTML full text (`https://arxiv.org/html/2505.23796v1` and `https://arxiv.org/html/2506.18600v1`, fetched 2026-06-13), with section locators where the HTML supplies them.

## Summary — the critique (Barrie & Törnberg)

The critique accepts the *observation* (LLM populations in a naming game converge on shared labels) but rejects the *explanation* (spontaneous emergence). Its claim is one of **observational equivalence**: the reported dynamics are indistinguishable from the models reproducing coordination-game conventions they already saw in pre-training. The argument runs through direct probing of the models out of the multi-agent loop: when queried, the LLMs can name the game type, state the optimal (matching) move, and anticipate convergence — so the multi-agent "emergence" may be the models *recalling* the structure and outcome of a known game rather than *self-organizing* one.

This is a `distributional`/`model-internal` deflation of a `relational` claim: it relocates the explanatory work from between-agent interaction dynamics back into each model's pre-training distribution and single-model behavior.

## Summary — the reply (Flint Ashery, Aiello & Baronchelli)

The reply concedes that data contamination is a real and important concern that "may hinder certain experiments," but argues it "does not preclude the study of genuinely emergent dynamics." Its structure: *recognizing* a game's structure is not the same as *producing* its population-level dynamics. Three population-level signatures — symmetry breaking, collective bias, and critical-mass tipping — are held to depend on history-dependent, decentralized interaction, not on any globally optimal solution a single model could recall. The reply leans especially on **collective bias**: a population-level skew that appears even when individual agents are unbiased in isolation, and that is model-dependent (present in Llama-3.1, not uniform across models) — features the authors argue a memorization account does not predict.

## Key passages — critique (arXiv 2505.23796v1)

**Abstract (verbatim, arXiv abs page):**

> "Ashery et al. recently argue that large language models (LLMs), when paired to play a classic "naming game," spontaneously develop linguistic conventions reminiscent of human social norms. Here, we show that their results are better explained by data leakage: the models simply reproduce conventions they already encountered during pre-training. Despite the authors' mitigation measures, we provide multiple analyses demonstrating that the LLMs recognize the structure of the coordination game and recall its outcomes, rather than exhibit "emergent" conventions. Consequently, the observed behaviors are indistinguishable from memorization of the training corpus. We conclude by pointing to potential alternative strategies and reflecting more generally on the place of LLMs for social science models."

**Body — the leakage thesis (HTML full text, main body):**

> "Rather than offering a novel research finding, the model may hence be simply regurgitating the results of existing research findings from its training data."

**Body — the probing evidence (HTML full text, main body):**

> "It is clear from these experiments that the model knows both what type of game it is as well as likely optimal moves after success and ultimate convergence."

**Body — the deflationary conclusion (HTML full text, main body; the quoted sentence opens "As a result, …"):**

> "As a result, what we observe in the interaction of LLM agents may not be the "spontaneous" development of conventions as argued by the authors but the more prosaic mirroring of model training data."

## Key passages — reply (arXiv 2506.18600v1)

**Abstract (verbatim, arXiv abs page):**

> "A potential concern when simulating populations of large language models (LLMs) is data contamination, i.e. the possibility that training data may shape outcomes in unintended ways. While this concern is important and may hinder certain experiments with multi-agent models, it does not preclude the study of genuinely emergent dynamics in LLM populations. The recent critique by Barrie and Törnberg [1] of the results of Flint Ashery et al. [2] offers an opportunity to clarify that self-organisation and model-dependent emergent dynamics can be studied in LLM populations, highlighting how such dynamics have been empirically observed in the specific case of social conventions."

**Body — recognition is not production (HTML, section "Data Leakage and Prior Knowledge"):**

> "even if an LLM recognises the game structure, the observed population-level dynamics (symmetry breaking, collective bias, critical mass) depend on history-dependent, decentralised interactions, not on a globally optimal solution."

**Body — collective bias as the load-bearing rebuttal (HTML, section "Further insights from collective bias"):**

> "even when individual agents are tested to be unbiased in isolation, collective bias emerges as a population-level effect, driven by the dynamics of interaction and memory accumulation."

**Body — model-dependence against simple memorization (HTML, section "Data Leakage and Prior Knowledge"):**

> "Moreover, this behaviour, stemming from the collective bias phenomenon, is model-dependent: it is observed in Llama-3.1 but not uniformly across models."

## What this exchange means for the relational axis

The in-repo Ashery source is the relational axis's load-bearing **LLM-side prior art, explicitly flagged as a *foil*** (coordination shown, constitution untested) in [`source/ashery-2025-llm-conventions`](ashery-2025-llm-conventions.md) and [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md). This exchange is precisely the "fetch both before any in-repo finding leans on the *emergence* (rather than the mere *occurrence*) of LLM conventions" caveat that [`wanted.md`](../wanted.md) records — now satisfied.

What the quotes actually support, and no more:

- The critique is a live, credible challenge to the **emergence** reading specifically. It does **not** dispute that convergence *occurs*; it disputes that convergence is *self-organized* rather than recalled. So it bears on the *explanation*, not the *phenomenon*.
- The reply does not refute the contamination concern outright — it concedes contamination "may hinder certain experiments" — and instead argues that population-level signatures (collective bias, model-dependence, critical mass) are the part a leakage account does not obviously cover. That is an argument, not a settled result; the exchange is unadjudicated here.
- **Calibration, not undermining, of the project's own work.** The project's relational pilot and perturbation results ([`result/relational-reference-game-v1`](../../findings/results/relational-reference-game-v1.md)) are read as a *foil* and do **not** rest on an emergence claim — their force is coordination phenomena as a floor, with the constitution test deliberately separated out. Because the project makes no "spontaneous emergence" claim about its own LLM conventions, this exchange **calibrates** the strength of any future emergence language rather than threatening existing findings. Any in-repo page that would assert genuine *emergence* (not mere occurrence) of LLM conventions must now cite *both* sides of this exchange and treat the question as open.

## What it can ground

- The methodological caveat that reported "emergent" LLM-population behaviors can be observationally equivalent to training-data leakage — with a named, datable critique to cite.
- The distinction, useful across the relational axis, between a model *recognizing* a coordination structure (single-model, distributional) and a population *producing* history-dependent dynamics (relational) — both sides of the exchange agree this distinction is where the disagreement lives.
- The point that any strong **emergence** claim about LLM conventions is currently *contested in the literature*, not settled.

## What it cannot ground

- Any verdict on *who is right*. This page records an unresolved exchange; it does not adjudicate it, and the project should not cite either side as having "won."
- Any meaning-constitution claim — like the original, neither the critique nor the reply poses the constitution question; the conventions remain payoff-defined arbitrary labels.
- Any human-comparison claim — there is no human baseline in either document.
- The internal experiments in the critique (direct probing of the models) are reported here only via the authors' own verbatim characterizations; this page has not re-run or independently verified those probes.

## Known limits

- Both items are **arXiv preprints (v1)** as fetched; neither the critique nor the reply was confirmed peer-reviewed at catalogue time. The original Ashery result, by contrast, is peer-reviewed (*Science Advances*).
- Body section headings are taken from the arXiv HTML rendering; the critique's HTML supplies several quotes without a clear section heading (recorded as "main body"). The reply's section headings ("Data Leakage and Prior Knowledge," "Further insights from collective bias") are as rendered.
- The exchange is one round (critique + reply); no further-reply or third-party adjudication was located as of 2026-06-13.
- Quotes preserve the source's straight/curly quotation marks as rendered; in-text citation markers in the reply abstract ("[1]", "[2]") are reproduced as shown.

## Status in wanted.md

[`wanted.md`](../wanted.md) records this exchange as the caveat to fetch before any in-repo finding leans on the *emergence* of LLM conventions. As of 2026-06-13 both sides are catalogued here; that wanted.md entry should move to `received` (locator: this page, `source/barrie-tornberg-2025-data-leakage`).
