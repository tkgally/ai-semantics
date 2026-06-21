---
type: source
id: he-2025-defeating-nondeterminism
title: Defeating Nondeterminism in LLM Inference
authors:
  - He, Horace
  - Thinking Machines Lab
year: 2025
venue: "Thinking Machines Lab: Connectionism (research blog), September 10, 2025"
url: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
access: open-access
meaning-senses:
  - model-internal
status: received
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: supports
    target: essay/point-estimate-is-a-draw
---

# He & Thinking Machines Lab 2025 — Defeating Nondeterminism in LLM Inference

## What it is

An open-access engineering/systems write-up (Thinking Machines Lab's "Connectionism" research blog, 2025-09-10; lead author **Horace He**, with collaborators at the lab) that diagnoses **why large-language-model inference is not bit-reproducible even at temperature 0** (greedy decoding) and shows how to remove the nondeterminism. It is a *mechanism* source, not a meaning-theory or behavioral-science source: it explains the engineering reason a byte-identical prompt to the same model can return a different completion on a re-run.

It was fetched for one specific in-repo purpose: [`essay/point-estimate-is-a-draw`](../../findings/essays/point-estimate-is-a-draw.md) observes **behaviorally** (from the session-62 / session-64 *let-alone* re-runs) that temperature-0 labels are not reproducible run-to-run, but until now the essay carried **no in-repo citation for the mechanism** — *why* the jitter occurs — and explicitly refused to fabricate one (its revision **trigger (c)**). This source discharges exactly that trigger: it grounds the essay's empirical premise (*that* temp-0 decoding is not deterministic) with a documented account of *why*, without the essay having to assert the mechanism on its own authority.

## Provenance

Title, author attribution ("Horace He in collaboration with others at Thinking Machines Lab"), publication date (2025-09-10), venue ("Thinking Machines Lab: Connectionism"), and the blog's own suggested citation were read from the article page (https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) via the harness `WebFetch` tool on **2026-06-21**. The verbatim quotes in the next section were extracted via the same tool with an explicit request for exact, word-for-word wording.

**Provenance caveat (read before leaning on a quote).** `WebFetch` converts the page to markdown and answers a prompt against it through a small intermediary model; the quotes below were requested as exact wording and are reproduced as returned, but they were **not** hand-verified character-for-character against the raw HTML in this session (the project's higher provenance bar — cf. the character-verification done for [`source/zeng-2026-lvlms-ground-differently`](zeng-2026-lvlms-ground-differently.md)). The four quotes under "Core verbatim quotes" were each returned to a direct exact-wording request and are high-confidence; the "Supporting quotes" were returned inside a summary and are reproduced as close paraphrase-or-verbatim — treat them as **characterized**, not as character-verified, and re-verify against the page before quoting any of them as exact in a load-bearing artifact. No page numbers exist (it is a web article); the article is unsectioned-by-number, so no section locators are given. Emphasis markers (bold/italics) inside quotes reflect the source's own rendering as converted to markdown.

## Core verbatim quotes (returned to a direct exact-wording request)

**The empirical demonstration of nondeterminism** (sampling the same prompt many times at temperature 0):

> "we generate _80_ unique completions, with the most common of these occuring 78 times." [*sic* "occuring"]

**Against the common but incomplete "concurrency + floating point" explanation** — the individual kernels are themselves deterministic:

> "However, all the kernels used in a language model's forward pass are **deterministic**."

> "Although concurrent atomic adds **do** make a kernel nondeterministic, _atomic adds are not necessary for the vast majority of kernels._"

**The actual identified cause — variable batch size, not per-kernel randomness:**

> "the primary reason nearly all LLM inference endpoints are nondeterministic is that the load (and thus batch-size) nondeterministically varies!"

**What a fix requires (batch invariance):**

> "The requirement for batch invariance is that the **reduction order for each element must be fixed regardless of the batch-size of the kernel.**"

## Supporting quotes (characterized — re-verify before quoting as exact)

On floating-point non-associativity (the mechanism people usually *name*, which is necessary but not the full story):

> "with floating-point numbers: (a + b) + c ≠ a + (b + c)"

On why batch size is "nondeterministic" from the user's side:

> "when you make a query to an inference endpoint, the amount of load the server is under is effectively 'nondeterministic' from the user's perspective"

On the prescription:

> "if we'd like to avoid nondeterminism in our inference servers, we must achieve batch invariance in our kernels"

## The argument, in the project's words

1. **The phenomenon.** At temperature 0 (greedy, argmax-at-every-step decoding) an LLM API "should" be deterministic, yet in practice it is not: re-sampling the same prompt many times yields many distinct completions (the source reports 80 unique completions out of repeated sampling, the modal one occurring 78 times). The divergence is small per step but compounds, because one different token early reshapes everything after it.
2. **The usual explanation is incomplete.** The folk account blames GPU concurrency plus floating-point non-associativity — `(a+b)+c ≠ a+(b+c)`, so parallel reductions in a nondeterministic order give different rounding. The source agrees floating-point non-associativity is the *ultimate* source of the numeric differences but argues the *concurrency* half is largely a red herring: the kernels in a forward pass are run-to-run deterministic for a fixed input shape; atomic-add nondeterminism is avoidable and avoided in most kernels.
3. **The real cause is lack of batch invariance.** Inference servers batch many users' requests together, and the **batch size varies with server load**, which from any single user's perspective is effectively random. Several common kernels (RMSNorm, matmul, attention reductions) compute a numerically *different* result for the same input row depending on the **batch size** they were run in — because the reduction order changes with the batch shape. So the same prompt, run once in a batch of 4 and once in a batch of 32, can produce a slightly different logit, hence (after argmax) a different token. The randomness the user sees is inherited from the *batching*, not from the math being random.
4. **The fix.** Make the kernels **batch-invariant** — fix the reduction order so a given element's result does not depend on the batch size. With batch-invariant implementations of the few offending reductions, repeated temperature-0 sampling becomes bitwise identical.

## What this bears on in-repo

- **[`essay/point-estimate-is-a-draw`](../../findings/essays/point-estimate-is-a-draw.md) — `supports` (discharges trigger (c)).** The essay's central empirical premise is that "temperature-0 decoding is **not**, in practice, deterministic," established so far only from the project's own behavioral observation (claude reading 0.833 then 0.708 on byte-identical items; the K=5 jitter measurement). This source supplies the *mechanism* the essay explicitly flagged as un-sourced and refused to fabricate: temp-0 non-reproducibility is a real, documented property of production inference, driven by **load-dependent batch-size variation interacting with non-batch-invariant kernels** (floating-point non-associativity being the ultimate numeric cause). It grounds *why* the jitter occurs, not only *that* it does.
- **[`result/scivetti-let-alone-repeated-runs-v1`](../../findings/results/scivetti-let-alone-repeated-runs-v1.md) and [`result/scivetti-let-alone-powered-rerun-v1`](../../findings/results/scivetti-let-alone-powered-rerun-v1.md).** These results *measured* the project's panel's run-to-run label jitter at temperature 0; this source is the independent systems-level account of the general phenomenon they ran into. It corroborates that the observed jitter is an expected property of API inference, not an artifact of the project's harness or prompts.
- **The "most stable ≠ deterministic" correction (session 64).** The mechanism explains why a model can be *nearly* but not perfectly stable across runs (gemini churned 2/33): the jitter is governed by how often that model's requests land in differently-sized server batches that happen to flip a near-tie logit — load- and routing-dependent, not a fixed per-model constant. It does **not** license any in-repo claim about a *specific* panel model's batching.

## What it can ground

- A citation that **temperature-0 / greedy LLM inference is documented to be non-reproducible in practice**, with a named mechanism (load-dependent batch-size variation × non-batch-invariant kernels; floating-point non-associativity as the ultimate numeric cause), from an open-access systems write-up.
- A citation that the **common "concurrency + floating point" folk explanation is incomplete** — the individual forward-pass kernels are run-to-run deterministic; the leak is batching, not per-kernel randomness.
- A citation that the nondeterminism is **removable** in principle (batch-invariant kernels) — i.e. it is an engineering property of *served* inference, not an in-principle property of the model's function.

## What it cannot ground

- **Anything about meaning** — lexical, grammatical, distributional, or otherwise. It is a numerics/systems source; it has no bearing on any human-comparison, constructional, or inferential claim. Cite it only for the temp-0-jitter mechanism.
- **The magnitude of jitter on the project's instruments.** The source's "80 unique completions" is from *open-ended generation* (many tokens, divergence compounding), a very different quantity from the project's *single-label forced-choice* jitter (~±0.12 on one near-chance instrument for gpt; ~0.03–0.06 for the others). The source explains the *mechanism*; it does **not** predict how large the label-level jitter will be on any given classification probe — that stays an empirical, per-instrument measurement (the K=5 result).
- **Claims about the specific panel models' or OpenRouter's batching.** The project does not observe its providers' batch sizes or kernels; the source is a general account, and the project must not assert that claude/gpt/gemini *as served via OpenRouter* use (or lack) batch-invariant kernels. The honest in-repo statement is "consistent with a documented general mechanism," not "caused, in our case, by X."
- **A determinism guarantee.** The source shows nondeterminism is *fixable with control of the serving stack*; the project has **no** such control (it calls hosted APIs), so the mechanism is a reason to **expect** jitter and measure it, not a knob the project can turn off.
- **Use as an `anchors:` human resource.** It is an engineering source, not a human-labeled empirical asset; it anchors no claim/result in the human-comparison sense.

## Known limits

- **Not peer-reviewed.** A company research blog post, not a journal/conference paper. Standing is "open-access engineering write-up by practitioners," credible and widely cited in the community but not formally refereed. Treat it as the *mechanism characterization* the essay's trigger (c) asked for, at that standing.
- **Provenance is tool-extracted, not character-verified** (see Provenance caveat). The four core quotes are high-confidence exact; the supporting quotes are characterized.
- **Mechanism, not measurement, for this project.** Its empirical numbers are for an open-ended-generation setting on a specific open model; they do not transfer to the project's forced-choice label setting as quantities, only as qualitative confirmation that the phenomenon is real and expected.

## Status in wanted.md

Listed under the founding/ongoing backlog as the **temperature-0 nondeterminism mechanism** want ([`base/wanted.md`](../wanted.md), P2). Marked **received** 2026-06-21: fetched from the primary open-access source (Thinking Machines Lab blog), satisfying the want's "a current arXiv or engineering-blog treatment" criterion.
