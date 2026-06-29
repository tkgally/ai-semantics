---
type: source
id: cao-2025-semantic-relation-knowledge
title: A Comprehensive Evaluation of Semantic Relation Knowledge of Pretrained Language Models and Humans
authors:
  - Cao, Zhihan
  - Yamada, Hiroaki
  - Teufel, Simone
  - Tokunaga, Takenobu
year: 2025
venue: "Language Resources and Evaluation (2025); peer-reviewed. Preprint arXiv:2412.01131 (cs.CL), submitted 2024-12-02; HTML v5 used for body quotes."
arxiv: "2412.01131"
doi: 10.1007/s10579-025-09858-9
url: https://arxiv.org/abs/2412.01131
access: open-access
meaning-senses:
  - distributional
  - inferential
  - human-comparison
status: received
created: 2026-06-29
updated: 2026-06-29
links:
  - rel: supports
    target: concept/polysemy
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: refines
    target: theory/lexicon-grammar-continuum
---

# Cao et al. 2025 — A Comprehensive Evaluation of Semantic Relation Knowledge of Pretrained Language Models and Humans

## What it is

A peer-reviewed paper (*Language Resources and Evaluation*, 2025; DOI 10.1007/s10579-025-09858-9; arXiv:2412.01131) by Zhihan Cao, Hiroaki Yamada, Simone Teufel, and Takenobu Tokunaga that builds a **prompt-based probing framework** for six nominal lexical-semantic relations — **hypernymy, hyponymy, holonymy, meronymy, antonymy, and synonymy** — and runs it on **both pretrained language models and human participants on the same task**, so that human performance acts as a measurable ceiling rather than an assumed one. The headline is a **"significant knowledge gap between humans and models for all semantic relations,"** with **antonymy the lone outlier** where models do reasonably well, and the wrinkle that **causal LMs do not always beat masked LMs** despite being more fashionable.

This is the **first in-repo source giving an empirical, human-compared, multi-relation treatment of the lexical sense-relation vocabulary** (hypernymy/hyponymy/holonymy/meronymy/antonymy/synonymy) that the project's lexical wedge had so far touched only through [`source/cruse-1986-lexical-semantics`](cruse-1986-lexical-semantics.md) at **secondary-only strength**. It is **prior-art + methodology + a candidate human-comparison resource**, *not* a direct comparison to the project's own frontier-decoder panel — the models it tests (BERT, RoBERTa, Llama-3) are older/smaller masked + causal LMs, not [`config/models.md`](../../../config/models.md)'s claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash. See "What this bears on in-repo" for the precise mapping.

## Provenance

Title, full author list, submission date (2024-12-02), subject category (cs.CL), journal reference (*Language Resources & Evaluation* 2025), and DOI were fetched from the arXiv abs page (https://arxiv.org/abs/2412.01131) on 2026-06-29. **Version note (load-bearing):** the abs-page abstract reflects the *latest* arXiv version (v5), which differs materially from arXiv v1. The v1 HTML reports "**16 PLMs, eight masked and eight causal**" and "**six metrics**" (adding *asymmetry*) and concludes "masked language models perform significantly better than causal"; the **published v5** reports "**six PLMs, four masked and two causal**", "**five metrics**", and "causal language models … do not always perform significantly better than masked language models." **All body quotes below are taken from the v5 HTML full text (https://arxiv.org/html/2412.01131v5)**, fetched and stripped to text on 2026-06-29 and verified character-for-character; the abstract is the v5/abs-page abstract. Quote locators are **section names/numbers from the HTML** (no journal page numbers were available from the open HTML). Do not cite v1's "16 PLMs / asymmetry / MLMs win" figures as this paper's result — they were superseded.

## Abstract (verbatim, from the arXiv abs page / v5)

> "Recently, much work has concerned itself with the enigma of what exactly pretrained language models (PLMs) learn about different aspects of language, and how they learn it. One stream of this type of research investigates the knowledge that PLMs have about semantic relations. However, many aspects of semantic relations were left unexplored. Generally, only one relation has been considered, namely hypernymy. Furthermore, previous work did not measure humans' performance on the same task as that performed by the PLMs. This means that at this point in time, there is only an incomplete view of the extent of these models' semantic relation knowledge. To address this gap, we introduce a comprehensive evaluation framework covering five relations beyond hypernymy, namely hyponymy, holonymy, meronymy, antonymy, and synonymy. We use five metrics (two newly introduced here) for recently untreated aspects of semantic relation knowledge, namely soundness, completeness, symmetry, prototypicality, and distinguishability. Using these, we can fairly compare humans and models on the same task. Our extensive experiments involve six PLMs, four masked and two causal language models. The results reveal a significant knowledge gap between humans and models for all semantic relations. In general, causal language models, despite their wide use, do not always perform significantly better than masked language models. Antonymy is the outlier relation where all models perform reasonably well. The evaluation materials can be found at https://github.com/hancules/ProbeResponses ."

## Section structure (from the v5 HTML table of contents)

1. Introduction
2. Related Work (2.1 Hypernymy; 2.2 Relations beyond hypernymy; 2.3 Symmetry and Prototypicality)
3. Methodological Considerations
4. Data
5. Metrics (5.1 Soundness and Completeness; 5.2 Symmetry; 5.3 Prototypicality; 5.4 Distinguishability)
6. Human Experiment (6.1 Elicitation of Human Responses; 6.2 …)
7. Model Experiment (7.1 Target Models)
8. Results and Analyses (incl. 8.5 Prototypicality)
9. Limitations
10. Conclusion
+ Appendices

## The six relations and the five metrics

**Six nominal semantic relations** (Abstract, verbatim "five relations beyond hypernymy, namely hyponymy, holonymy, meronymy, antonymy, and synonymy" — hypernymy is the sixth, the baseline relation prior work had used):

- hypernymy, hyponymy, holonymy, meronymy, antonymy, synonymy.

**Five metrics, two of them new** (§5, verbatim):

> "The proposed evaluation framework consists of five metrics, two of which are novel. The novel metrics are called prototypicality and distinguishability. Prototypicality evaluates a property of semantic relations. Distinguishability evaluates agents' ability to distinguish relations from each other. Soundness and completeness measure the performance of relatum prediction under the multiple relata setting. Symmetry has been studied before, but only with factual relations."

Individual metric definitions (verbatim, §5.1 / §5.2):

> "Soundness, denoted by 𝒮(r;m), is the extent to which words predicted by m are valid relata for relation r." (§5.1)

> "Completeness 𝒞(r;m) measures the extent to which m can predict all relata for relation r." (§5.1)

> "We measure whether reciprocal elicitation happens for tuple (w,r,v) using metrics proposed by Mruthyunjaya et al [45] …" (§5.2 — symmetry; an established metric used in a new context.)

## The "same task" design (humans and models compared identically)

The paper's distinctive methodological move is that **the identical prompt-based probe is answered by both models and humans**, so the human result is a measured ceiling, not an assumption (§1, verbatim):

> "First, we compare models against humans on the same task, so that we can quantify the difference with the theoretically achievable ceiling."

> "We further provide a direct comparison between models and humans on the same task. Such a human ceiling will allow us to interpret the performance of models more meaningfully." (§3)

On the probing paradigm itself (§2.1, verbatim):

> "In prompt-based probing, responses from a model are elicited using a prompt, a textual string with slots, all of which are unfilled."

> "A probe is a prompt where the target word has been filled in." (§2.1)

The model and human responses are pooled into comparable distributions (§5, verbatim): *"This allows us to treat human responses and model responses in a comparable way."*

## The six PLMs (four masked + two causal)

§7.1 "Target Models" names them (verbatim):

> "We use BERT as one of the MLMs because it is widely used in previous work (we use the cased version). In addition to BERT, we also chose RoBERTa [36], as this allows us to quantify the effect of training objectives and architectures. For the CLMs, we chose Llama-3 [18] (from here on, referred to as Llama)."

The six variants tabulated (Table 4, from the HTML): **BERT-base, BERT-large, RoBERTa-base, RoBERTa-large** (the four MLMs) and **Llama-8B, Llama-70B** (the two CLMs). So the four masked LMs are two BERT and two RoBERTa sizes; the two causal LMs are two Llama-3 sizes. (In v1 the panel was larger — 16 models including ALBERT and OPT — and the headline favoured MLMs; the published v5 reduced and re-ran it. Cite only the v5 panel above.)

## Key findings (verbatim where possible; v5 HTML section locators)

**Abstract — the central gap and the antonymy outlier:**

> "The results reveal a significant knowledge gap between humans and models for all semantic relations."

> "In general, causal language models, despite their wide use, do not always perform significantly better than masked language models."

> "Antonymy is the outlier relation where all models perform reasonably well."

**§8 (soundness) — antonymy as the positive outlier, in numbers:**

> "All models perform relatively well for antonymy, where the best model Llama-8B (L1) achieves 𝒮=0.57, whereas for other relations, best values typically lie around 𝒮=0.30."

**§8 — models far below the human ceiling on relatum prediction:**

> "We conclude from the results for the OOR rate, soundness, and completeness that the models only acquire a limited ability to perform relata prediction, which is far below the human ceiling."

**§10 Conclusion — the main result and the size/type findings:**

> "Our main result is that PLMs fall short of achieving human-level performance on the extensive semantic relation tasks defined here."

> "We also found that a large model size does not always guarantee better performance in learning semantic relations. The type of PLMs also matters. MLMs consistently outperformed CLMs for hyponymy and meronymy. Therefore, the bidirectional context utilized by MLMs is a crucial factor in learning these two semantic relations."

**§10 Conclusion — prototypicality findings (the first human gold standard for it):**

> "We established the first human gold standard for prototypicality. For the other aspects, where we constructed gold standards from existing lexicographic data, we established the first human ceiling, which can be used in comparisons with automatic models."

> "We were able to confirm prototype effects for hypernymy and antonymy that have been experimentally studied in the literature. We also found a prototype effect for holonymy and synonymy that was not known before. One of our most important findings for prototypicality was that hyponymy and meronymy showed little prototypicality."

## The human experiment (verbatim, §6.1)

> "In order to collect responses to probes from human participants, we use the Amazon Mechanical Turk (MTurk) crowdsourcing platform."

> "In total, 48 qualified participants were recruited."

> "We split the 10,507 probes from Table 1 into 276 subsets of 38 probes on average, making sure that no subset contained more than one probe with the same relation and the same target word. … Four participants were assigned to each subset. Participants answered 22 subsets on average."

> "We asked participants to type up to five relata for each probe. We instructed them that they should use nouns, but no multi-word expressions."

So the human "ceiling" is an MTurk crowd of **48 Master-qualified annotators** (US/UK/Australia/Canada, >500 approvals, >95% approval rate) producing up to five **open-ended noun relata** per probe, four annotators per probe, with bogus-item screening. (Minor count discrepancy: the paper §6.1 states **10,507 probes**; the released GitHub README states **10,546** — see below. Cite the paper's number for the paper.)

## What this bears on in-repo

- **[`concept/polysemy`](../concepts/polysemy.md) — `supports`.** The polysemy page leans on the lexical-semantics *sense-relation vocabulary* (hypernymy, meronymy, antonymy, troponymy) and currently grounds it only through [`source/cruse-1986-lexical-semantics`](cruse-1986-lexical-semantics.md) at secondary strength, flagging in "Honest gaps" that the full sense-relation taxonomy is "still pending the Murphy ingestion and a primary-strength reach of Cruse." This paper **partially fills that gap with an empirical, human-compared treatment** of six of those relations — not the lexicographic theory of the taxonomy, but a measured demonstration of how *recoverable* each relation is from distributional training versus from humans. It does not touch polysemy's own *graded-sense* axis (Usim/WiC-style usage-similarity); it is about relation-*type* knowledge, a complementary corner of the same lexical wedge.
- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md) — `depends-on`.** The probe is a pure language-modeling/cloze task ("prompt-based probing is a language modeling task, it aligns well with the pretraining task of PLMs," §2.1), so what it measures is exactly **distributional competence at the lexical-relation level**. The "significant knowledge gap" is therefore a clean datum for the distributional-meaning page's central question — *how much* of human lexical-relation knowledge falls out of distribution alone — and its answer is "a lot, but well short of the human ceiling, and very unevenly across relations (antonymy recovers; meronymy/hyponymy lag)." Read with care: this is *older masked + causal* models, not the project's frontier decoders, so it bounds what the **distributional shadow** delivered for that model generation, not for the panel.
- **[`theory/lexicon-grammar-continuum`](../../findings/theory/lexicon-grammar-continuum.md) — `refines`.** The lexical end of the continuum is the "beat the distributional shadow" frame: a lexical-meaning claim must show the model tracks sense/relation structure *over and above* surface co-occurrence. This paper is a concrete instance of the shadow being only partly beaten — relations vary sharply in how far distributional training carries them, and **antonymy** (the relation most strongly cued by symmetric contrastive co-occurrence) is the one models recover best, which is exactly what a distributional-shadow story predicts. It sharpens the continuum's lexical pole with a six-relation, human-anchored gradient rather than a single binary.

Meaning-sense tags: `distributional` (the probe is a cloze/language-modeling task measuring co-occurrence-derived relation knowledge), `inferential` (semantic relations — hypernymy, antonymy, etc. — are inferential-role structure: knowing *X is a kind of Y* licenses inferences), and `human-comparison` (the paper's whole force is the same-task human ceiling). `referential` is **not** tagged: the task is word-form-level relatum prediction, and the authors explicitly note the evaluation "is performed at the word form level … and not the sense level" (§4 footnote), so it does not turn on reference or on `referential.sense` at fine grain.

## What it can ground

- A citation that, on a **same-task human-vs-model probing design**, current (BERT/RoBERTa/Llama-3-generation) PLMs show a **significant knowledge gap below the human ceiling across all six relations**, with **antonymy the positive outlier** and **causal LMs not reliably beating masked LMs** (verbatim Abstract + §8 + §10).
- A citation that **bidirectional (masked) context helps specifically for hyponymy and meronymy** (verbatim §10), and that **model size does not guarantee better relation knowledge** (verbatim §10) — a useful caution for any "bigger frontier model therefore better lexical semantics" assumption.
- A methodological template: a **cloze/prompt-based probe answered identically by humans and models**, with the human distribution pooled to a comparable gold — a design the project could adapt for a frontier-panel lexical-relation probe.

### Resource / anchor potential (honest assessment — NOT yet adopted)

The released materials (GitHub `hancules/ProbeResponses`, visited 2026-06-29) are **the human probe responses only** — `human_responses.json`, structured as `target word → relation → prompt → [annotator 1..4 responses]` (e.g. the probe *"a mother is a kind of a ___"*). Key facts for resource potential:

- **What it is:** 48 MTurk Master annotators' **open-ended word completions** (up to five noun relata per probe), four responses per probe, over the six relations; README statistics give per-relation target-word/prompt counts (Hypernymy 692×7, Hyponymy 310×4, Holonymy 186×7, Meronymy 144×6, Antonymy 91×9, Synonymy 211×7) and "We split 10,546 probes into 276 questionnaires" (README) — note the **10,546 vs. paper's 10,507** discrepancy.
- **Categorical vs. graded:** **Categorical / open-ended**, *not* a graded scalar rating. Responses are free-text relata, not similarity scores on a scale — so this is a *production* gold standard (what humans produce as the hypernym/antonym/etc. of a cue), unlike DWUG/DURel's graded usage-similarity. This makes it a candidate anchor for a **lexical-relation production/recovery** wedge, *complementary to* (not a substitute for) the project's existing graded word-sense-relatedness anchors.
- **License:** **No LICENSE file and no license statement** were present in the repo on 2026-06-29 (checked README + LICENSE on `main` and `master`; both 404). License status is therefore **unknown** — a blocker for adopting it as an anchor until clarified.
- **Verdict:** the human responses are a real, human-generated, same-task gold that **could** anchor a future lexical-relations wedge (especially an antonymy-vs-other-relations contrast, or a "does the frontier panel recover human-produced relata?" probe). **But adopting it as a `resource`/anchor is a separate, cross-session step** (PROJECT.md §12.3): it requires fetching and cataloguing `human_responses.json` as its own `resource` page, resolving the **missing license**, and reconciling the **10,507/10,546 count discrepancy**. This `source` page does **not** stand in for that and makes **no** human-anchor claim.

## What it cannot ground

- **Any claim about the project's panel.** The models are BERT/RoBERTa (masked) and Llama-3 8B/70B (causal) — older/smaller than [`config/models.md`](../../../config/models.md)'s frontier decoders. The gap-to-human result **does not transfer** to claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash without re-running the probe on them; treat it as prior-art bounding an earlier model generation.
- **A graded-polysemy / usage-similarity claim.** The task is relatum *production* at the word-form level, not graded usage-similarity; it does not bear on the Usim/WiC gradience question that [`concept/polysemy`](../concepts/polysemy.md)'s wedge runs on. The two are complementary corners of the lexical wedge, not the same measurement.
- **A `referential` claim.** Word-form-level, sense-agnostic by the authors' own statement; do not read it as evidence about reference or fine-grained Fregean sense.
- **Use as an `anchors:` resource as-is.** It is a `source` (a peer-reviewed experiment paper), not a catalogued human-labeled resource. Its released human responses have anchor *potential* (see above) but require a separate `resource` page, a resolved license, and the count reconciliation first.

## Known limits

- **Two materially different arXiv versions.** v1 (16 PLMs, six metrics incl. asymmetry, "MLMs win") vs. the published v5 (six PLMs, five metrics, "CLMs don't always win"). This page cites **v5 only**; anyone re-checking quotes must use the v5 HTML or the journal version, not v1.
- **No journal page locators** from the open HTML — all body locators are section names/numbers.
- **README/paper count mismatch** (10,546 vs 10,507 probes) — flagged; reconcile before any resource adoption.
- **Crowd-sourced human ceiling.** The "human" gold is 48 MTurk Master annotators producing open-ended relata, not an expert lexicographer panel; it is a strong but crowd-level ceiling, and for several aspects the gold was "constructed from existing lexicographic data" (§10) rather than freshly elicited — the freshly-elicited human gold is specifically for **prototypicality**.
- **Released data is human responses only** — model responses are not in the repo, so reproducing the model side requires re-running the probes.

## Status in wanted.md

Not previously listed by id. Ingested 2026-06-29 as the first in-repo empirical, human-compared, multi-relation treatment of the lexical sense-relation vocabulary (partially filling the gap flagged in [`concept/polysemy`](../concepts/polysemy.md) "Honest gaps"). The orchestrating session should record it in `wanted.md` / [`index.md`](../../index.md) as RECEIVED, and note the released `ProbeResponses` human data as a **candidate future `resource`** (pending license clarification and the count reconciliation), not an adopted anchor.
