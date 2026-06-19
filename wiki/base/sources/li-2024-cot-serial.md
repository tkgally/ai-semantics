---
type: source
id: li-2024-cot-serial
title: Chain of Thought Empowers Transformers to Solve Inherently Serial Problems
authors:
  - Li, Zhiyuan
  - Liu, Hong
  - Zhou, Denny
  - Ma, Tengyu
year: 2024
venue: ICLR 2024; arXiv 2402.12875 (submitted 2024-02-20; v2 the version read)
arxiv: "2402.12875"
url: https://arxiv.org/abs/2402.12875
access: open-access
meaning-senses:
  - functional-vs-formal
  - model-internal
status: received
created: 2026-06-19
updated: 2026-06-19
links:
  - rel: supports
    target: essay/output-channel-confound
  - rel: refines
    target: concept/formal-vs-functional-competence
---

# Li, Liu, Zhou & Ma 2024 — Chain of Thought Empowers Transformers to Solve Inherently Serial Problems

## What it is

A **theoretical computer-science** paper (Zhiyuan Li, Hong Liu, Denny Zhou, Tengyu Ma; Stanford / TTIC / Google), accepted to **ICLR 2024**, posted as arXiv 2402.12875. It asks *why* chain-of-thought (CoT) prompting — having a model emit a sequence of intermediate steps before its answer — improves accuracy, and answers through the lens of **expressiveness** (circuit complexity) for **decoder-only transformers**. The headline result: a constant-depth transformer *without* CoT is confined to a small parallel complexity class, but *with* `T` intermediate steps it can compute anything a boolean circuit of size `T` can — so CoT supplies exactly the **inherently serial computation** that a single (bounded-depth, "one forward pass") transformer lacks. Its empirical section shows CoT dramatically helps precisely on tasks that are *hard to parallelize*, the first-named example being **the composition of permutation groups**.

This is a **theory/mechanism source, not a human-annotated resource and not an empirical claim about this project's panel.** Its bearing here is methodological: it gives an *independent, formal* reason for the mechanism the project's freshest methodological essay — [`essay/output-channel-confound`](../../findings/essays/output-channel-confound.md) — posits from behavior alone, namely that a *working surface* (room to externalize intermediate steps) lets a model carry out a serial computation that a forced single-token answer cannot. The match is unusually tight because the paper's lead hard example, *permutation-group composition*, is the exact mathematical object the project's composition probes use (STEP/FLIP, CYCLE/SWAP as permutations generating D4, A4, D6). The honest scope limits — asymptotic, idealized-transformer, not-the-panel — are spelled out under "What it cannot ground."

Not previously on [`wanted.md`](../wanted.md); found and catalogued this session because it bears directly on the in-repo composition line. Added to `wanted.md` as `RECEIVED` for the record.

## Provenance and what was verified

- The **abstract** below is **verbatim** from the arXiv abs page (https://arxiv.org/abs/2402.12875), read 2026-06-19; the title, full author list, ICLR-2024 acceptance note, and 2024-02-20 submission date are from the same page.
- The body sentences under "Key passages" were read from the arXiv HTML (https://arxiv.org/html/2402.12875v2) and cross-checked against the ar5iv LaTeXML rendering (https://ar5iv.labs.arxiv.org/abs/2402.12875). As elsewhere in this repo, the HTML was reached through a summarizing fetch route, so body quotes are recorded at **section-located** strength (not certified character-for-character the way the abstract is). One concrete correction the cross-check forced is logged honestly: a first fetch placed the S5/permutation sentence in §1; the ar5iv cross-check located it in **§3.4** and confirmed the **§1** "inherently serial computation" sentence appears there (and, identically, in the abstract). Mathematical subscripts (e.g. the group `S_5`, the classes `TC^0`/`AC^0`) render with sub/superscripts in the source; they are written inline here as `S_5`, `TC^0`, `AC^0`.

## Abstract (verbatim, arXiv abs page)

> "Instructing the model to generate a sequence of intermediate steps, a.k.a., a chain of thought (CoT), is a highly effective method to improve the accuracy of large language models (LLMs) on arithmetics and symbolic reasoning tasks. However, the mechanism behind CoT remains unclear. This work provides a theoretical understanding of the power of CoT for decoder-only transformers through the lens of expressiveness. Conceptually, CoT empowers the model with the ability to perform inherently serial computation, which is otherwise lacking in transformers, especially when depth is low. Given input length $n$, previous works have shown that constant-depth transformers with finite precision $\mathsf{poly}(n)$ embedding size can only solve problems in $\mathsf{TC}^0$ without CoT. We first show an even tighter expressiveness upper bound for constant-depth transformers with constant-bit precision, which can only solve problems in $\mathsf{AC}^0$, a proper subset of $\mathsf{TC}^0$. However, with $T$ steps of CoT, constant-depth transformers using constant-bit precision and $O(\log n)$ embedding size can solve any problem solvable by boolean circuits of size $T$. Empirically, enabling CoT dramatically improves the accuracy for tasks that are hard for parallel computation, including the composition of permutation groups, iterated squaring, and circuit value problems, especially for low-depth transformers."

## Key passages (section-located; see the provenance caveat)

**§1 (Introduction) — the conceptual claim (double-confirmed across independent fetches; also in the abstract above):**

> "CoT empowers the model with the ability to perform inherently serial computation, which is otherwise lacking in transformers, especially when depth is low."

**§3.4 ("CoT Makes Transformers More Expressive") — the permutation-group example:**

> "Theorem 3.3 also implies that transformers with linearly many intermediate steps can compute all regular languages, including composition of non-solvable groups, like permutation group over five elements, S_5, which does not belong to AC^0 and is also widely conjectured to be out of TC^0."

**The without-CoT bound and the CoT-scaling claim (verbatim within the certified abstract):** "constant-depth transformers with finite precision $\mathsf{poly}(n)$ embedding size can only solve problems in $\mathsf{TC}^0$ without CoT"; and "with $T$ steps of CoT, constant-depth transformers using constant-bit precision and $O(\log n)$ embedding size can solve any problem solvable by boolean circuits of size $T$."

## Bearing on this project

- **[`essay/output-channel-confound`](../../findings/essays/output-channel-confound.md) — the principal connection.** That essay argues, *from behavior*, that a forced single-token response channel can **mask** a serial-computation capability, because "the obstacle was not a *capacity* to chain but the *denial of a surface on which to chain*," and that a working surface lets a model "perform serial computation in tokens that it might not perform in a single forward pass." Li et al. supply the **formal counterpart** of exactly that mechanism: a bounded-depth transformer *is* expressively limited (to `AC^0`/`TC^0`) when it must answer in one pass, and intermediate steps are what add serial power. This is a `supports` link, with a sharp boundary: the paper grounds the *mechanism's plausibility*, not the project's specific behavioral result. The essay's competence/performance framing — which the essay explicitly flags as "a *frame*, not an empirical claim" — now has an independent theoretical articulation it can cite, **without** the essay needing to assert any human comparison or any claim about the panel's internals.
- **The composition results** ([`result/relational-order-composition-c-reasoning-scaffold`](../../findings/results/relational-order-composition-c-reasoning-scaffold.md), [`result/relational-order-composition-c-altpair`](../../findings/results/relational-order-composition-c-altpair.md), [`result/relational-order-composition-c-k6`](../../findings/results/relational-order-composition-c-k6.md), [`result/relational-order-composition-c`](../../findings/results/relational-order-composition-c.md)). The project's order-sensitive composition probes ask models to compose two non-commuting permutations (STEP/FLIP, CYCLE/SWAP) and found the panel succeeds **given a working surface** but not under a forced single token. Li et al.'s empirical section names **permutation-group composition** as a canonical task that is *hard for parallel computation and helped dramatically by CoT* — a published, independent reason to *expect* exactly the working-surface dependence the project observed, on exactly this class of task. It is corroboration of *direction*, not an anchor: the paper's permutation example is `S_5` in the asymptotic/circuit setting, not the project's finite D4/A4/D6 stimuli, and proves nothing about the specific panel models.
- **[`concept/formal-vs-functional-competence`](../concepts/formal-vs-functional-competence.md).** The result refines the *performance* side of the formal/functional picture with a complexity-theoretic mechanism: a constrained output channel (no intermediate steps) is a genuine **expressive** bottleneck for serial tasks, so a failure under that constraint is a performance/channel fact, not evidence about the model's underlying competence — the machine analogue of the guardrail "failure on a world-knowledge task does not show that a model lacks formal linguistic competence."

## What it can ground

- A citation that **chain-of-thought / an externalized working surface adds *serial* computational power** that a bounded-depth ("single forward pass") transformer provably lacks — as a published ICLR-2024 expressiveness result (Li, Liu, Zhou & Ma 2024), for use when the project explains *why* a working surface can flip a forced-format negative.
- A citation that **permutation-group composition is a canonical hard-for-parallel task** that CoT helps — the formal backdrop for the project's choice of non-commuting-permutation composition as its order-sensitivity probe.
- The general framing, for the methodological essays, that **the output channel is an expressivity-relevant degree of freedom**, not a neutral readout, when the probed task is inherently serial.

## What it cannot ground

- **Any claim about the project's panel models' internals.** This is a theory result about *idealized* decoder-only transformers (constant depth, specified precision, asymptotic input length `n`). The project's models (claude-sonnet-4.6, gemini-3.5-flash, gpt-5.4-mini) are not constant-depth in the theorem's sense, and the project has no mechanistic access; the paper cannot be cited as showing *these* models are or are not so bounded.
- **A finite-case guarantee.** The bounds are asymptotic and the empirical demonstrations are on trained small transformers for the stated tasks; they do not entail that any particular finite stimulus (e.g. a 4- or 6-element track) is or is not solvable in one pass by a large LM. The project's own behavioral runs are what establish the working-surface dependence for its stimuli; this source explains *why such a dependence is expected*, not *that it holds* for the panel.
- **A human anchor.** It is not human-labeled data (no treebank, sense inventory, acceptability norm, or annotation); it cannot serve as the `anchors:` resource for any claim or result, and it licenses **no human comparison**. Its role is theoretical framing for the methodological/essay layer.
- **Anything about lexical or constructional *meaning* directly.** The paper is about computational expressiveness, not semantics; it bears on the project only via the *elicitation/channel* methodology, not via any meaning-sense claim.

## Known limits

- **Theory + small-scale empiricism, not LLM-scale measurement.** The expressiveness theorems are the core; the empirical section trains/evaluates small transformers on the stated tasks. Neither leg measures frontier LLMs, so the connection to the project's panel is by *analogy of mechanism*, stated as such.
- **Fetch-route quoting limit.** Only the abstract is certified character-for-character (from the abs page). Body sentences are section-located via the summarizing HTML fetch route and cross-checked across two renderings where noted; treat them at *abstract-plus-section-located* strength, the way this repo treats partially-reachable sources.
- **Version.** v2 was read for body structure; the abstract was read from the abs page (latest version). Cite as "ICLR 2024 (arXiv 2402.12875)."

## Status in wanted.md

Not previously listed; **added 2026-06-19 as `RECEIVED`** under the relational/methodology context, with a one-line note that it grounds the [`essay/output-channel-confound`](../../findings/essays/output-channel-confound.md) serial-computation mechanism. Abstract verbatim-verified against the arXiv abs page; body section-located via HTML/ar5iv with the §3.4 locator correction logged above.
