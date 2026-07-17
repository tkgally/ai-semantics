---
type: source
id: mosolova-2025-wsi-unsolved
title: "In the LLM era, Word Sense Induction remains unsolved"
authors:
  - Mosolova, Anna
  - Candito, Marie
  - Ramisch, Carlos
year: 2025
venue: "Findings of the Association for Computational Linguistics: ACL 2025, pp. 17161–17178 (ACL Anthology 2025.findings-acl.882)"
doi: 10.18653/v1/2025.findings-acl.882
url: https://aclanthology.org/2025.findings-acl.882/
access: open-access
meaning-senses:
  - distributional
  - referential
status: received
created: 2026-07-17
updated: 2026-07-17
links:
  - rel: refines
    target: concept/polysemy
---

# Mosolova, Candito & Ramisch 2025 — In the LLM era, Word Sense Induction remains unsolved

## What it is

A three-author computational-linguistics paper (Findings of ACL 2025) on **word sense induction (WSI)** — the *unsupervised* task of clustering a lemma's corpus occurrences into discrete senses, without a predefined sense inventory. The paper's contribution is partly methodological (it argues that the standard SemEval WSI datasets over-represent polysemy and use metrics that hinder comparability) and partly empirical: it builds a **SemCor-derived evaluation** that "respect[s] the original corpus polysemy and frequency distributions," and on it evaluates pre-trained embeddings + clustering, prior SOTA systems, and an **LLM-based WSI method** the authors propose (prompting Llama-3.1-8B-Instruct and Llama-3.3-70B-Instruct). Its headline is that **no fully unsupervised method — theirs or previous — beats the trivial "one cluster per lemma" (1cpl) baseline** (i.e. do not split a lemma's senses at all) once the dataset follows a natural sense distribution; LLMs in particular "have troubles performing this task." Semi-supervision using Wiktionary (data augmentation, must-link constraints, fine-tuning) *does* help, surpassing the previous SOTA on their test set by 3.3%.

This is a **model-behavior + methodology** study on **non-project models** (BERT-family PLMs, PolyLM, and Llama-3.1/3.3-Instruct — **not** the project's frontier panel). Like [`source/diera-2026-encode-semantic-relations`](diera-2026-encode-semantic-relations.md), it is catalogued as a **map and counterweight**, not a method the project uses and **not a human anchor** (see "What it cannot ground"). Its value here is as a **sobering trivial-baseline counterweight** on the *lexical-sense* side — a "beat the trivial baseline?" test structurally akin to the project's "beat the distributional shadow?" tests — bearing on the discreteness clause of the project's sense-gradience line ([`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md), [`claim/lexical-sense-gradience`](../../findings/claims/lexical-sense-gradience.md)).

## Provenance

Title, full author list, venue (Findings of ACL 2025, Vienna, July 2025), page range (17161–17178), and the **abstract** were fetched and verified firsthand against the ACL Anthology landing page (https://aclanthology.org/2025.findings-acl.882/) on 2026-07-17; the page declares the standard ACL license, **CC BY 4.0** ("Materials published in or after 2016 are licensed under the Creative Commons Attribution 4.0 International License"). Body quotes were extracted from the ACL Anthology PDF (https://aclanthology.org/2025.findings-acl.882.pdf) locally with PyMuPDF and verified; **line-break hyphenation was rejoined** (e.g. "distribu-tion" → "distribution"), flagged here. Page numbers are the published Anthology pagination (17161–17178); section numbers are the paper's own (§1, §4.2–4.3, §5, Conclusion).

## Abstract (verbatim)

> "In the absence of sense-annotated data, word sense induction (WSI) is a compelling alternative to word sense disambiguation, particularly in low-resource or domain-specific settings. In this paper, we emphasize methodological problems in current WSI evaluation. We propose an evaluation on a SemCor-derived dataset, respecting the original corpus polysemy and frequency distributions. We assess pre-trained embeddings and clustering algorithms across parts of speech, and propose and evaluate an LLM-based WSI method for English. We evaluate data augmentation sources (LLM-generated, corpus and lexicon), and semi-supervised scenarios using Wiktionary for data augmentation, must-link constraints, number of clusters per lemma. We find that no unsupervised method (whether ours or previous) surpasses the strong \"one cluster per lemma\" heuristic (1cpl). We also show that (i) results and best systems may vary across POS, (ii) LLMs have troubles performing this task, (iii) data augmentation is beneficial and (iv) capitalizing on Wiktionary does help. It surpasses previous SOTA system on our test set by 3.3%. WSI is not solved, and calls for a better articulation of lexicons and LLMs' lexical semantics capabilities."

## The task and the baseline (verbatim)

**What WSI is, in the authors' framing (§1, p. 17160):**

> "The word sense induction task (WSI) does away with the need for a predefined sense inventory and sense-labeled data (except for evaluation), albeit at the expense of quality. In addition, one of the standard techniques in WSI is to cluster vector representations of a lemma's occurrences."

**The 1cpl baseline (§4.2, p. 17164):**

> "For each dataset, we provide two simple baselines: one cluster per lemma (1cpl) and one cluster per example (1cpex)."

(1cpl = assign *every* occurrence of a lemma to a single cluster — i.e. never distinguish senses; 1cpex = one cluster per occurrence — i.e. every occurrence a distinct sense.)

## Key findings (verbatim; section/page locators)

**No model beats 1cpl on the natural-distribution dataset (§4.3, p. 17165):**

> "None of the models surpasses the high 1cpl baseline in F-B3 on SemCor-WSI, a result likely to hold for full-corpus scenario on other corpora."

**LLMs lag (§4.3, p. 17165):**

> "Performance of LLMs is globally much lower (except on verbs, see Table 17 in Appendix), with sometimes huge variance."

**The methodological reading (§5, p. 17165):**

> "We reported earlier that the top-performing systems do not surpass the 1cpl baseline when switching to a more naturally distributed dataset. This suggests that over-representation of polysemy in earlier datasets may have influenced the systems' design."

**The conclusion (Conclusion, p. 17169):**

> "Our striking conclusion is that, when considering a dataset following a more natural sense distribution and polysemy level, none of the fully unsupervised systems we tested surpass the simple baseline of clustering all instances of the same lemma into a single cluster (considering a dataset with an average polysemy close to 2, cf. Table 11)."

> "The LLM prompting technique we proposed lays far behind, calling for better leveraging the lexical semantics knowledge of LLMs."

## What this bears on in-repo

- **[`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) clause (b) — the primary bearing.** The conjecture's *distinctive* bet, clause (b), is that a model treats polysemy as a **discrete regime beyond graded distance**; the project found this an **adequately-powered null** ([`result/lexical-polysemy-homonymy-v3`](../../findings/results/lexical-polysemy-homonymy-v3.md) — the panel does not separate polysemy from graded distance) and reads the sense signal as **graded, not discrete**. Mosolova et al. supply **external, cross-method corroboration of the difficulty of discrete sense individuation**: on a natural-distribution corpus, *no* unsupervised induction method beats the no-split baseline, so a discrete sense inventory is not cleanly recoverable — consistent with the project's clause-(b) null and with a gradience-over-discreteness reading. It is corroboration of a *difficulty already recorded*, not a new positive result.
- **[`claim/lexical-sense-gradience`](../../findings/claims/lexical-sense-gradience.md) — a modesty counterweight, NOT a challenge.** The promoted claim (clauses a+c) is that the **frontier panel's graded pairwise sense-relatedness rating rank-tracks the human DURel median** and survives a topic-similarity partial — a *direction/agreement* statement over usage *pairs*. Mosolova evaluates a **different task** (full-corpus clustering into sense inventories), a **different grain** (whole-corpus induction, not pairwise relatedness), on **different models** (BERT/PolyLM/Llama, not claude/gemini/gpt), by **different metrics** (F-B3/NMI). So it does **not** test, confirm, or contradict the claim; its force here is a general caution against over-reading LLM lexical-sense competence — reinforcing the claim's existing "behavioral, single-lab, cross-model shared priors" and "not beyond the tested surface" fences.
- **[`concept/polysemy`](../concepts/polysemy.md) — `refines`.** A data point on the graded-vs-discrete tension the concept page carries: discrete sense inventories resist unsupervised induction from natural text, which sits more comfortably with the lexicographic gradience picture than with a discrete-sense ontology — though (see below) the paper diagnoses a *methodology*, it does not settle the ontology.

## What it can ground

- A citation that, on a **SemCor-derived dataset respecting natural corpus polysemy and frequency distributions**, **no fully unsupervised WSI method — the authors' own, prior SOTA, or an LLM-prompting method — surpasses the trivial "one cluster per lemma" (1cpl) no-split baseline** (F-B3 on SemCor-WSI), and "LLMs have troubles performing this task," while **Wiktionary-based semi-supervision surpasses previous SOTA by 3.3%** — all verbatim as above.
- A citation for the **"beat the trivial baseline"** framing on the lexical-sense-**induction** side: a counterweight cautioning that recovering a *discrete* sense structure from distributional evidence is not solved, useful wherever the project states its sense findings modestly.

## What it cannot ground

- **A human anchor.** This is a model-behavior/method study; its SemCor sense labels are used **only for evaluation**, it is a *discrete-induction* task (not the graded DURel usage-similarity signal the project's sense claim anchors on — [`resource/dwug-usage-graphs`](../resources/dwug-usage-graphs.md)), and no licensed graded human asset is adopted from it. It is **NOT a human anchor** and must not be cited as one.
- **Any claim about the project's frontier panel.** The models are BERT-family PLMs, PolyLM, and Llama-3.1/3.3-Instruct — **not** the project's panel in [`config/models.md`](../../../config/models.md). No transfer to claude/gemini/gpt is established.
- **A challenge to [`claim/lexical-sense-gradience`](../../findings/claims/lexical-sense-gradience.md).** A "1cpl wins" result on unsupervised full-corpus clustering says nothing about whether a frontier model's *graded pairwise rating* rank-tracks human *graded* judgments — a different task and grain. Do **not** cite this paper as weakening the panel's graded direction/agreement finding.
- **Positive evidence for the gradience thesis.** "1cpl wins" is compatible with several readings (senses genuinely continuous; or the task/metric/dataset mismatched); the paper diagnoses WSI *methodology and evaluation*, it does not settle the graded-vs-discrete ontology. Cite it as corroboration of a *difficulty*, not as proof that senses are continuous.

## Known limits

- **Peer-reviewed** (Findings of ACL 2025); the **abstract** was verified firsthand against the ACL Anthology landing page, **body quotes** PDF-extracted locally (PyMuPDF) with line-break hyphenation rejoined (flagged). Locators are Anthology pages + the paper's own section numbers.
- **Scope (authors' own Limitations):** the study "evaluates only three large language models and four pre-trained language models in combination with two clustering algorithms" — a bounded system set, English only.
- **Task and metric.** A *clustering/induction* study scored by clustering metrics (F-B3/NMI), **not** a graded-relatedness measure and **not** the pairwise DURel instrument the project's sense claim uses; the two are companion questions about lexical sense, not the same measurement.

## Status in wanted.md

Firsthand-verified to exist at s240 (abstract char-checked; ACL Anthology landing page confirmed); listed `wanted` (P2) there. Catalogued 2026-07-17 (session 241) as a **methodology/counterweight source** bearing on the discreteness clause of the sense-gradience line — the orchestrating session records it in [`wanted.md`](../wanted.md)/[`index.md`](../../index.md) as **RECEIVED**.
