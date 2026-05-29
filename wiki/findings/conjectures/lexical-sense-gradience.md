---
type: conjecture
id: lexical-sense-gradience
title: LLM same/different-sense behavior is monotonic in human-rated usage similarity, with an intermediate regime for polysemy absent for homonymy — separable from a context-similarity shadow
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: proposed
contingent-on:
  - lexical-sense-gradience-anchor
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: refines
    target: open-question/lexical-polysemy-gradience
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
  - rel: anchors
    target: resource/wic-graded-usage-similarity
---

# Conjecture: graded sense-relatedness tracking in LLMs (the lexical wedge)

> **Status: proposed, untested.** This is the project's first **lexical** (non-grammatical) conjecture, sharpening the seed [`open-question/lexical-polysemy-gradience`](../open-questions/lexical-polysemy-gradience.md). Its human anchor is a **candidate, not ratified**: the graded usage-similarity resource it points to ([`resource/wic-graded-usage-similarity`](../../base/resources/wic-graded-usage-similarity.md)) is `external-only` (not yet mirrored or inspected in-repo), and an anchor decision (`lexical-sense-gradience-anchor`) should be queued before any result is promoted. All claims here are provisional.

## Statement

Lexicographers treat word sense as **graded**: the senses of a polysemous word (*paper*: material / newspaper / academic article; *run* across dozens of related uses) shade into one another with intermediate, bridging cases, **unlike** homonymy (*bank*: riverside / financial), where the two senses are discrete and unrelated. The seed open-question fixed three hypotheses for how an LLM might behave against this picture: **graded-sense tracking**, **discrete-sense collapse**, and **distributional shadow**.

This conjecture stakes out the **graded-sense-tracking** hypothesis as a falsifiable directional claim:

> An LLM's same-sense / different-sense behavior for a target word across two contexts is **monotonic in the human-rated usage similarity** of those two usages — graded, not near-binary. Concretely: (a) the model's same-sense signal decreases monotonically as human-rated usage similarity decreases; (b) there is an **intermediate regime for related-but-distinct (polysemous) usages** that is **absent for homonyms** (homonym pairs sit at the "different" floor with little intermediate mass); and (c) this graded behavior is **not reducible to context similarity** — it survives when the overall lexical/contextual overlap of the two sentences is held roughly constant, so it is not merely the lexical analogue of the constructional `distributional` shadow that runs through this repo.

Clause (c) is the load-bearing one: it is what separates graded-sense tracking (hypothesis 1) from the distributional-shadow null (hypothesis 3). Without the context-similarity control, any apparent gradience could be the model tracking how similar the two *sentences* are, not how related the two *senses* are.

## Why this is interesting

- It opens the project's **lexical** axis, which has been empty — every prior finding is constructional/grammatical. It does so on exactly the asset the charter names as under-used: "a lexicographer's tolerance for fine-grained polysemy … the gradiness is the point" ([`PROJECT.md`](../../../PROJECT.md) §1, via the seed [`open-question/lexical-polysemy-gradience`](../open-questions/lexical-polysemy-gradience.md)).
- It is a clean `distributional`-vs-`referential.sense` test ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), [`concept/referential-meaning`](../../base/concepts/referential-meaning.md)). On a deflationary reading, distributional structure plausibly captures sense-as-mode-of-presentation — but whether it carries the *graded relatedness* a lexicographer documents, rather than just same/different discrimination, is the contested fine-grain question. A clean intermediate-regime result would be modest positive evidence that distributional training recovers graded `referential.sense`; a collapse result would bound how fine that recovery goes.
- Most LLM word-sense work uses **discrete** WordNet synsets and reports classification accuracy. The lexicographically interesting question — graded relatedness and bridging contexts — is comparatively under-probed, so a careful null or positive here is genuinely informative rather than redundant.
- The polysemy-vs-homonymy split gives the conjecture a built-in internal contrast: the *same* model on two regimes that human lexicography treats differently. That contrast is harder to explain away as an artifact than a single monotonicity correlation.

## Predictions

1. **Monotonicity (hypothesis 1).** Across usage pairs of a target word, the model's same-sense signal — prompted same/different-sense judgment with confidence, or a representational-similarity score in the small-model lane — rises monotonically with human-rated usage similarity (e.g., Spearman correlation reliably positive, not a step function).
2. **Intermediate regime for polysemy, floor for homonymy.** Related-but-distinct polysemous usage pairs occupy an **intermediate** band of the model's signal; homonym pairs cluster near the "different" floor. The distributions for the two regimes are separable — polysemy is *not* treated as just-another-homonym (which would be discrete-collapse, hypothesis 2).
3. **Context-similarity control (the discriminating prediction).** When usage pairs are matched so that overall sentence/context overlap is roughly constant across high- and low-relatedness pairs, the monotonic relation to *human sense relatedness* **persists**. If instead the signal tracks context overlap and goes flat once context overlap is controlled, that is the distributional shadow (hypothesis 3).
4. **Bridging contexts.** Deliberately sense-ambiguous (bridging) contexts, engineered so two senses are co-present, yield **intermediate, less-confident** model behavior rather than a forced discrete pick — the behavioral fingerprint of gradience.
5. **Binary cross-check.** On a binary same/different set (WiC), the model's same-sense judgments agree with human binary labels at a baseline rate; the *graded* set (Usim) is where the monotonicity claim is actually tested. Agreement on the binary task without gradience on the graded task would be evidence for discrete-collapse.

## What would confirm / falsify

- **Confirm (graded-sense tracking):** monotonic relation between model same-sense signal and human-rated usage similarity (prediction 1), with a **separable intermediate regime for polysemy vs. a floor for homonymy** (prediction 2), that **survives the context-similarity control** (prediction 3). This is the conjecture's central bet — and it must clear clause (c) to count.
- **Discrete-sense collapse (an interesting alternative, partial falsification of clause b):** model behavior is near-binary — polysemous-but-related pairs are treated as sharply same or different, with no intermediate band distinguishing them from homonyms — even though the binary same/different baseline (prediction 5) is met. A clean collapse result is a **first-class negative** (charter §2.6): it would say the model discriminates senses but does not reproduce lexicographic gradience.
- **Distributional shadow (falsification of clause c):** any apparent gradience disappears once context similarity is held constant (prediction 3 fails). The monotonic relation was to sentence overlap, not sense relatedness. This is the lexical analogue of the constructional `distributional` null and would be the most deflationary outcome.
- **Falsify outright:** no monotonic relation to human usage similarity at all, and no binary agreement either — the model's same/different behavior is unrelated to the human sense signal. (Least likely given how well distributional models do on same/different sense tasks, but the cleanest null.)

The **context-similarity control is the design's spine**: confirming clauses (a)+(b) while *failing* (c) reads as distributional shadow, not as graded-sense tracking. The conjecture is only supported if all three clauses hold.

## Human anchor

Candidate (not ratified): the **Usim graded usage-similarity ratings** of Erk, McCarthy & Gaylord, catalogued at [`resource/wic-graded-usage-similarity`](../../base/resources/wic-graded-usage-similarity.md). Usim is the load-bearing anchor because its **graded 5-point human usage-similarity judgments** are what predictions 1–3 require — a binary set cannot ground monotonicity. **WiC** (binary same/different-sense, Pilehvar & Camacho-Collados 2019) is the cross-check for prediction 5 and the discrete contrast, but is explicitly *insufficient* for the gradience claim (the seed's warning).

Anchor caveats, stated plainly:
- The resource is **`external-only`**: not yet mirrored or inspected in-repo. Its license, exact scale wording, and item counts were **not verified from a primary source** this run (see the resource page's *Known limits*). So this anchor is a *candidate*, and the conjecture's `contingent-on` carries `lexical-sense-gradience-anchor`.
- Usim rates usage similarity but does **not** itself tag pairs as polysemy vs. homonymy; prediction 2 needs a polysemy/homonymy **stratification** added on top (e.g., from a dictionary or WordNet sense-relatedness). That stratification is work-to-be-done, not a property of the released ratings.
- The over-/under-splitting arm of the seed (model sense inventory vs. a human inventory) is **not** carried by this conjecture; it would need WordNet + SemCor/OntoNotes and is left to a later, separate finding.

→ An **anchor decision should be queued** (`wiki/decisions/open/lexical-sense-gradience-anchor`): adopt Usim (graded) as the ratified gradience anchor with WiC as the binary cross-check, vs. an alternative graded set. **This page does not open that decision** (per house rules, surfacing is the job, not auto-resolving); it is flagged for the orchestrator.

## Notes / caveats

- **Instrument is an operationalization gate.** Two loci are possible: behavioral (prompted same/different-sense + confidence on the panel) or the small-model lane (representation-similarity / probe for a graded signal). They are different instruments and may disagree; pick and **freeze the instrument before seeing results** (charter §8) — do not tune it until the collapse becomes gradience or vice versa. Queue this gate before running.
- **Context-similarity must be measured, not assumed.** Clause (c) needs an explicit context-overlap measure (lexical overlap, sentence-embedding similarity, or both) computed independently of the model's sense signal, so the control is real and not circular.
- **Small N.** Usim is on the order of hundreds of items over ~11 lemmas (provisional, unverified count); per-lemma claims will carry wide uncertainty. Treat this as a gradience-signal probe, not a coverage benchmark.
- **Sense relatedness is itself graded and contested.** "Human-rated usage similarity" is the operational stand-in for "sense relatedness"; they are close but not identical, and the conjecture should not silently equate them. Usim measures usage similarity; the lexicographic gradience claim is about sense relatedness — keep the two labelled distinctly in any result.
- **Relation to the constructional wedge.** This is the lexical counterpart of [`open-question/constructional-vs-frequency-confound`](../open-questions/constructional-vs-frequency-confound.md) / [`open-question/distributional-vs-inferential-constructional`](../open-questions/distributional-vs-inferential-constructional.md): there the null is n-gram frequency; here it is context similarity. Both ask whether a `distributional` shadow explains apparent meaning-tracking. It does **not** touch the relational axis.
