---
type: source
id: armendariz-2020-cosimlex
title: "CoSimLex: A Resource for Evaluating Graded Word Similarity in Context"
authors:
  - Armendariz, Carlos Santos
  - Purver, Matthew
  - Ulčar, Matej
  - Pollak, Senja
  - Ljubešić, Nikola
  - Granroth-Wilding, Mark
year: 2020
venue: "Proceedings of the Twelfth Language Resources and Evaluation Conference (LREC 2020), pp. 5878–5886, European Language Resources Association; arXiv 1912.05320"
arxiv: "1912.05320"
url: https://aclanthology.org/2020.lrec-1.720/
access: open-access
meaning-senses:
  - distributional
  - human-comparison
status: received
created: 2026-06-24
updated: 2026-06-24
links:
  - rel: refines
    target: concept/distributional-meaning
---

# Armendariz et al. 2020 — CoSimLex: A Resource for Evaluating Graded Word Similarity in Context

## What it is

A multi-author **resource paper** describing the construction of **CoSimLex**, a dataset of human ratings of **graded word similarity in context**: pairs of words (drawn from SimLex-999) each rated for similarity within two different short text contexts, so that the *change* in rated similarity between the two contexts can be measured. Published at LREC 2020 (European Language Resources Association, pp. 5878–5886; ACL Anthology id `2020.lrec-1.720`); preprint arXiv 1912.05320 (v1 submitted 2019-12-11; last revised v3 2020-10-29; subject category cs.CL). CoSimLex is the gold-standard dataset for **SemEval-2020 Task 3, "Graded Word Similarity in Context" (GWSC)** — a *related but distinct* shared task (the paper here describes the *dataset*; the SemEval task is the competition that uses it; see "On the SemEval-2020 Task 3 relationship" below).

This page is the project's first catalogue of CoSimLex, the **alternative graded anchor to DWUG** that the lexical-sense-gradience anchor decision ([`decisions/resolved/lexical-sense-gradience-anchor`](../../decisions/resolved/lexical-sense-gradience-anchor.md), Option B) flagged as a fallback if DWUG does not fit. It is catalogued here as a `source` (paper summary) only; see "What it cannot ground" for why it is **not** yet an anchor.

Provenance: title, author list, venue, page range, and abstract were fetched from the ACL Anthology landing page (https://aclanthology.org/2020.lrec-1.720/) and its BibTeX (https://aclanthology.org/2020.lrec-1.720.bib), and cross-checked against the arXiv abs page (https://arxiv.org/abs/1912.05320), all on 2026-06-24. The abstract below is verbatim, identical on both the ACL Anthology page and the arXiv abs page. All body quotes with section locators were verified character-for-character against the ar5iv full-text rendering of arXiv 1912.05320 (https://ar5iv.labs.arxiv.org/abs/1912.05320, fetched 2026-06-24); section numbers are from that rendering's structure.

**Author-list note (recorded, not resolved):** the **published LREC version** (ACL Anthology landing page and BibTeX, 2026-06-24) lists **six** authors, in this order: Carlos Santos Armendariz, Matthew Purver, Matej Ulčar, Senja Pollak, Nikola Ljubešić, Mark Granroth-Wilding. The **arXiv 1912.05320 abs page** (v3) additionally lists Marko Robnik-Šikonja and Kristiina Vaik (eight authors total). The front-matter above uses the **published LREC six-author list** as canonical; the arXiv preprint's two extra names are noted here for honesty and should not be cited as the LREC author list. (The prompt that requested this ingest recalled the author list as including "Mark Granroth-Wilding" but not the two arXiv-only names; the published list was taken from the primary anthology record, not from recollection.)

## Abstract (verbatim)

> "State of the art natural language processing tools are built on context-dependent word embeddings, but no direct method for evaluating these representations currently exists. Standard tasks and datasets for intrinsic evaluation of embeddings are based on judgements of similarity, but ignore context; standard tasks for word sense disambiguation take account of context but do not provide continuous measures of meaning similarity. This paper describes an effort to build a new dataset, CoSimLex, intended to fill this gap. Building on the standard pairwise similarity task of SimLex-999, it provides context-dependent similarity measures; covers not only discrete differences in word sense but more subtle, graded changes in meaning; and covers not only a well-resourced language (English) but a number of less-resourced languages. We define the task and evaluation metrics, outline the dataset collection methodology, and describe the status of the dataset so far."

## Summary

1. **The gap.** Intrinsic word-embedding evaluation rests on similarity judgements that **ignore context**; word-sense disambiguation uses context but yields **discrete**, not **continuous**, meaning distinctions. CoSimLex aims to fill the gap with a **graded, in-context** similarity signal.
2. **Design.** Each item is a **pair of words** (from SimLex-999) presented inside **two different short contexts**; annotators rate the similarity of the pair within each context. The dataset thus supports two things: an absolute graded similarity per context, and the **change** in similarity across the two contexts of a pair.
3. **Collection.** English ratings were crowd-sourced on Amazon Mechanical Turk following SimLex-999's process, with a **0-to-6 scoring scale** and **27 annotators per pair-and-context**; the other languages used directly-recruited annotators (**12** each). The aggregated score is the **average** of annotators' scores.
4. **Coverage.** English plus three less-resourced languages (Croatian, Slovene, Finnish). Counts are reported at two stages of the paper (see Key passages); the later count is **341 (English), 113 (Croatian), 112 (Slovene), 25 (Finnish)**.
5. **Use.** CoSimLex is the gold standard for **SemEval-2020 Task 3 (GWSC)**; the paper states the dataset was made available for that task's evaluation stage and would be made public after the competition.

## Key passages (verbatim, section locators from the ar5iv rendering of arXiv 1912.05320)

**§1 — the gap CoSimLex fills (this is also the abstract's middle sentence):**

> "Standard tasks and datasets for intrinsic evaluation of embeddings are based on judgements of similarity, but ignore context; standard tasks for word sense disambiguation take account of context but do not provide continuous measures of meaning similarity."

**§3 — base task (SimLex-999) and the SemEval-2020 Task 3 relationship:**

> "It is to be used as the gold standard for evaluation of a task at SemEval2020: Task 3, Graded Word Similarity in Context."

**§4.1 — how the two contexts per pair were sourced:**

> "For each word pair we need to find two suitable contexts. These contexts are extracted from each language's Wikipedia."

> "They are made of three consecutive sentences and they need to contain the pair of words, appearing only once each."

**§4.2 — scoring scale and crowd-sourcing (English):**

> "For English we adopted a modified version of their crowd-sourcing process: we use Amazon Mechanical Turk, with the same scoring scale (0 to 6), the same post-processing and cleaning of the data (a necessary step when working with this kind of crowd-sourcing platform), and achieve similarly good inter-annotator agreement."

**§4.2 — annotator counts (English vs. the other languages):**

> "In English, given the resources available, we follow SimLex-999 closely: we will use Amazon Mechanical Turk to get 27 annotators per pair and context."

> "For Croatian, Finnish and Slovene we recruit annotators directly: this means we have less of them (12 vs 27) but we expect the quality of the annotation to be better"

**§4.2 — aggregation (the human gold score is an average):**

> "We do the same with the average of the scores produced by the human annotators."

**§3 — pair counts (initial statement):**

> "The English dataset consists of 333 pairs; the Croatian, Finnish and Slovene datasets of 111 pairs each."

**§5 — pair counts (later statement, the as-built numbers):**

> "The dataset contains 341 entries in English, 113 in Croatian, 112 in Slovene and 25 in Finnish."

**§6 — availability:**

> "The full dataset was provided for the evaluation stage of SemEval 2020 at the beginning of February 2020, and will be made public when the competition is over"

## On the SemEval-2020 Task 3 relationship (keep these distinct)

- **This paper / this dataset = CoSimLex** (Armendariz, Purver, Ulčar, Pollak, Ljubešić, Granroth-Wilding 2020, LREC): the *resource*. The graded human ratings live here.
- **SemEval-2020 Task 3 = "Graded Word Similarity in Context" (GWSC)**: the *shared task* that uses CoSimLex as its gold standard. Its overview/data record (Zenodo record 3989788, "SemEval-2020 Task 3: Graded Word Similarity in Context", authors Armendariz, Purver, Pollak, Ljubešić, Ulčar, Vulić, Pilehvar; CC BY 4.0, v3, 2020-07-31; confirmed 2026-06-24) is a **different artifact** with a partly different author list. Do not cite the SemEval task overview as "the CoSimLex paper," and do not cite this LREC paper as "the SemEval task." The §3 quote above is the in-paper statement of the dependency.

## Bearing on this project

- **Alternative graded-in-context anchor to DWUG (the Option-B fallback).** [`decisions/resolved/lexical-sense-gradience-anchor`](../../decisions/resolved/lexical-sense-gradience-anchor.md) ratified Option B — anchor [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) on a graded, released, licensed usage/sense-similarity set, and named **DWUG** as the recommended candidate with **CoSimLex** as the flagged alternative. This page is the first in-repo summary of that alternative.
- **Construct distinction from DWUG — related but not the same signal.** [`resource/dwug-usage-graphs`](../resources/dwug-usage-graphs.md) carries graded human **usage-similarity** between **two usages of the *same* target lemma** (DURel tradition, diachronic design, 4-point scale). CoSimLex carries graded human **word-pair similarity** between **two *different* words**, each rated **in two contexts** (0-to-6 scale, synchronic). Both are "graded similarity in context," but the unit differs: DWUG = same-word usage pairs; CoSimLex = different-word pairs across contexts. The DWUG page's own "Fit assessment" section recorded exactly this mismatch as the reason it preferred DWUG for the monotonicity clause of the lexical-sense-gradience conjecture, which needs same-lemma usage proximity. This page does not overturn that assessment; it documents the alternative honestly so a future session can re-weigh it firsthand.
- **`distributional` × `human-comparison`.** The dataset is a human-anchored, graded distributional-similarity signal sensitive to context — the home territory of the `distributional` tag (similarity/substitution behavior) crossed with `human-comparison` (force comes from contrast with a human-rated resource). It [`refines`](../concepts/distributional-meaning.md) `concept/distributional-meaning` by adding a context-conditioned, graded similarity operationalization.

## What it can ground

- Citations for the existence and design of a **graded, in-context, human-rated word-similarity** resource built on SimLex-999, with two contexts per pair — as a published LREC 2020 resource description.
- The framing that intrinsic similarity evaluation has historically **ignored context** while WSD gives only **discrete** distinctions, with CoSimLex positioned to provide a **continuous, context-sensitive** signal (abstract / §1, both verbatim above).
- The stated scale (0 to 6), per-language annotator counts (27 English MTurk; 12 for each of Croatian/Finnish/Slovene), averaging aggregation, Wikipedia-sourced three-sentence contexts, and the as-reported pair counts — **as the paper reports them** (locators above).
- The CoSimLex ↔ SemEval-2020 Task 3 dependency relationship, kept distinct (the two are different artifacts).

## What it cannot ground

- **It is a `source` page, not a `resource` page, and by itself it is NOT an anchor.** No empirical claim about any LLM may cite this page as a human anchor. Before CoSimLex can anchor any result, a future session must **firsthand verify** (i) the **license** of the actual released CoSimLex data files, (ii) **fetchability** of those files, and (iii) the **counts and scale** as found in the released data (not only as described in the paper) — exactly the resource-page discipline applied to DWUG. The paper here only says the data "will be made public when the competition is over"; it states **no license and no download URL** in the text. (A separate Zenodo record, 3989788, is the *SemEval-2020 Task 3* data under CC BY 4.0 — a related but distinct artifact; whether the CoSimLex release proper carries the same license must be checked against the CoSimLex release itself, not assumed from the task record.)
- **The lexical-sense-gradience monotonicity clause out of the box.** That clause needs graded similarity between **two usages of the same target lemma**; CoSimLex rates **different-word pairs**. Using CoSimLex for that conjecture would require re-deriving a same-lemma signal it does not directly provide — which is why the anchor decision and the DWUG page both preferred DWUG. A different clause (context-driven *change* in word-pair similarity) is the natural CoSimLex fit, and would need its own operationalization.
- **Any number "as released."** The paper gives two different pair-count statements (§3: 333 English / 111 each; §5: 341 / 113 / 112 / 25). These are paper-stage figures; the released-dataset counts must be confirmed against the data before being used as resource counts.
- **Reference / extension or truth.** Like every distributional-similarity resource, CoSimLex carries no human-agreed extension; it bears on similarity/sense relatedness, not on reference or truth.

## Known limits

- **Resource paper, status-report framing.** The paper itself describes "the status of the dataset so far" (abstract); some figures are stated as the build was in progress (the two differing pair-count statements), so the paper is not a frozen data-card. Treat its numbers as paper-reported, not as verified released counts.
- **Author-list discrepancy** between the published LREC version (6 authors) and the arXiv preprint (8 authors), recorded above; the published list is treated as canonical.
- **Only the ar5iv rendering of the arXiv preprint and the ACL Anthology landing page/BibTeX were read** for this page; the LREC proceedings PDF and the actual CoSimLex data release were **not** inspected. Section locators are from the ar5iv structure of arXiv 1912.05320.
- **Less-resourced-language coverage is small** (Finnish in particular: 25 entries per §5), and per-language annotator pools differ (12 vs. 27), which would matter for any cross-language comparison built on the data.
- **No license/download URL in the paper text.** Availability is asserted as "will be made public," not licensed in the paper — the standing blocker before any anchor use.
