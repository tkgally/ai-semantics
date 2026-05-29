---
type: resource
id: scivetti-2025-cxnli-dataset
title: Scivetti et al. 2025 CxNLI / CxNLI-Distinction constructional NLI dataset
status: external-only
url: https://anonymous.4open.science/r/beyond-memorization-B82B
paper: https://arxiv.org/abs/2501.04661 (ACL Anthology https://aclanthology.org/2025.ijcnlp-long.65/)
venue: IJCNLP-AACL 2025, pp. 1184–1201
meaning-senses:
  - constructional
  - inferential
  - human-comparison
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
---

# Scivetti et al. 2025 — CxNLI and CxNLI-Distinction constructional NLI dataset

This page catalogs the **public dataset** released with Scivetti et al. 2025. The argument summary of the paper lives on the source page [`source/scivetti-2025-beyond-memorization`](../sources/scivetti-2025-beyond-memorization.md); this page is the *dataset catalog* — a distinct role. It documents the data only at the level the paper itself documents, because the release repository is **not reachable from this environment** this run (see Known limits), so item-level inspection is pending.

## What it is

The natural language inference (NLI) evaluation dataset accompanying Scivetti et al. 2025, *Beyond Memorization: Assessing Semantic Generalization in Large Language Models Using Phrasal Constructions* (IJCNLP-AACL 2025). The authors build NLI triples (premise + hypothesis → inference label) over a set of English phrasal / argument-structure constructions drawn from Construction Grammar (CxG), then compare LLM behavior against a native-speaker baseline. The constructions are sourced from a construction inventory the paper calls CoGS:

> "We construct our datasets with 8 of the 10 Cxns in CoGS, shown in Table 3." (arXiv 2501.04661 v2 HTML, §4.1)

The items are human-annotated by the paper's authors:

> "All datasets are annotated by co-authors of this paper." (arXiv 2501.04661 v2 HTML, Appendix C)

The annotation process iterated to agreement:

> "Once the dataset was created, a second and sometimes third author annotated the relations and hypotheses were amended until achieving an Inter-Annotator Agreement (IAA) of 90%." (arXiv 2501.04661 v2 HTML, §4.1)

The public release is stated in the abstract:

> "We make our novel dataset and associated experimental data, including prompts and model responses, publicly available." (ACL Anthology 2025.ijcnlp-long.65, abstract; arXiv v2 HTML)

with the repository at footnote 1:

> "https://anonymous.4open.science/r/beyond-memorization-B82B" (arXiv 2501.04661 v2 HTML, footnote 1 to the abstract)

## Dataset structure (as documented by the paper)

There are two sub-datasets, one per experiment.

- **Experiment 1 — "CxNLI"**, 8 constructions:
  > "The final Exp 1 'CxNLI' dataset totals 435 triples." (arXiv 2501.04661 v2 HTML, §4.1)
- **Experiment 2 — "CxNLI-Distinction"**, a subset of 5 of those 8 constructions, with added surface-identical / meaning-divergent variants:
  > "The final Exp 2 'CxNLI-Distinction' dataset totals 99 NLI triples." (arXiv 2501.04661 v2 HTML, §5.1)
  > "Thus, for the 5 argument structure Cxns of our 8 Cxns, we add test instances which share a surface syntax with our Cxns, but convey a different meaning." (arXiv 2501.04661 v2 HTML, §5.1)

The Experiment-1 construction set (8) was selected for balance across two CxG types:

> "We select 8 Cxns that are roughly balanced across two types: argument structure Cxns with no fixed words but clear syntactic slots (e.g., caused-motion in Table 3) and phrasal Cxns with two or more fixed words that clearly identify the Cxn (e.g., let-alone in Table 3)." (arXiv 2501.04661 v2 HTML, §3)

**The 8 constructions (Table 3), verbatim as printed:** Causative-With, Caused-Motion, Comparative-Correlative, Conative, Intransitive Motion, Let-Alone, Resultative, Way-Manner.

**Task and label scheme.** The task is 3-way NLI:

> "NLI is the task of determining the inference relation between two (short, ordered) texts: entailment, contradiction, or neutral" (arXiv 2501.04661 v2 HTML, Appendix H, Annotation Guidelines)

with the label definitions:

> "0 – entailment – The hypothesis must be true given the premise." (arXiv 2501.04661 v2 HTML, Appendix H)
> "1 – neutral – The hypothesis may or may not be true given the premise." (arXiv 2501.04661 v2 HTML, Appendix H)
> "2 – contradiction – The hypothesis must not be true given the premise." (arXiv 2501.04661 v2 HTML, Appendix H)

**Human baseline / agreement.**

- Experiment 1: native-speaker accuracy ≈ 0.90.
  > "Thus, if we take the original author's assigned relation to be the gold standard, then native speaker accuracy on the NLI task is 90%." (arXiv 2501.04661 v2 HTML, §4.1)
- Experiment 1 inter-annotator agreement was also 90% (annotation process figure; see the IAA quote under *What it is*). Note: the IAA figure and the native-speaker-accuracy figure are *both* 90% but are reported as two different sentences (process vs. baseline); do not double-count them.
- Experiment 2: ≈ 0.83.
  > "achieving an IAA of 83% with the original judgments." (arXiv 2501.04661 v2 HTML, §5.1)
  Caveat: the verified Exp-2 sentence is phrased as an **IAA** ("83% with the original judgments"); the source page and task brief gloss this as the Exp-2 human-baseline accuracy. The 0.83 number is verified; whether it is best read as IAA or as a native-speaker-accuracy baseline should be re-checked against Table 1 on the next visit. (A WebFetch read of Table 1 reported "Human performance = 0.90 (Exp 1) and 0.83 (Exp 2)", but the table values were not independently verified character-for-character this run.)

**Models evaluated** (not part of the released *human* data, but the experimental-data release includes prompts + model responses):

> "GPT-4o-2024-05-13 and GPT-3.5-turbo-0125, as well as o1-preview-2024-09-12. We also test two Llama models: Llama-3-8B-instruct and Llama-3-70B-instruct." (arXiv 2501.04661 v2 HTML, §4.3)

**Example items (Table 9), verbatim** — one per task-brief-requested construction:

- Caused-Motion — premise *"I threw the stone across the river."*, hypothesis *"I caused the stone to move across the river by throwing it."*, relation Entailment. (arXiv 2501.04661 v2 HTML, Table 9)
- Conative — premise *"I sipped at the Heineken."*, hypothesis *"The Heineken was not the target of my sipping."*, relation Contradiction. (arXiv 2501.04661 v2 HTML, Table 9)
- Way-Manner — premise *"I yawned my way back to the Narrow Neck."*, hypothesis *"I traveled back to Narrow Neck without yawning."*, relation Contradiction. (arXiv 2501.04661 v2 HTML, Table 9)

These three examples were read via WebFetch from the v2 HTML rendering of Table 9; they are reported here as the table's verbatim cell text, but a future run with direct repo/PDF access should re-confirm them character-for-character before any are quoted in a claim/result page.

## What it can ground

This is the key section. The dataset is a **candidate human inference-rate anchor** (the project's Tier-4 "inference-licensing" level of evidence) for exactly three of the project's open conjectures, because it contains human-annotated NLI triples for precisely those constructions *plus* a native-speaker accuracy baseline:

- **caused-motion** — `Caused-Motion` is one of the 8 constructions, with human-annotated triples and the 0.90 baseline.
- **conative** — `Conative` is one of the 8.
- **way-manner / way-construction** — `Way-Manner` is one of the 8.

Concretely, it **could** serve as the human anchor that the three open decisions `caused-motion-anchor`, `conative-anchor`, and `way-construction-anchor` are seeking — an alternative to (or supplement to) their current provisional VerbNet/Levin/Goldberg default. The bearing is real: human-licensed inference labels over those exact constructions, with an aggregate accuracy baseline against which model NLI accuracy can be compared on the *same items*.

**This is a CANDIDATE only.** It is *not* asserted to be the anchor. Those three decisions are open with a different provisional default, so this page intentionally adds **no `anchors:` links** — doing so would pre-resolve an open decision. Adoption is pending (a) Tom's ratification of the decision and (b) item-level inspection of the currently unreachable data repository (see Pointer for next visit). The orchestrator will surface this candidate in the relevant decision pages.

More generally the dataset can ground:

- `constructional` × `inferential` probes that test argument-structure / phrasal constructions via NLI rather than acceptability.
- `human-comparison` contrasts: LLM NLI accuracy vs. native-speaker accuracy on identical constructional items.

## What it cannot ground

- **AANN.** The Article + Adjective + Numeral + Noun construction is **not** among the 8 constructions. Do not cite this dataset for AANN.
- **Model-internal / representational claims.** The evaluation is behavioral NLI accuracy only; it says nothing about internal representations, so it cannot ground `model-internal` claims.
- **Exact per-item human ratings.** Only aggregate native-speaker accuracy / IAA (0.90, 0.83) are verified. Whether the public repo releases *per-item* human labels (and in what schema) has **not** been inspected this run; per-item human-rating claims cannot be grounded until the repo is inspected.

## Known limits

- **Aggregate baseline, not gradient ratings.** The human bearing is an aggregate accuracy/agreement figure, not per-item graded human inference ratings. It supports an accuracy-comparison anchor, not a graded-inference-strength anchor, on the evidence verified so far.
- **Small N per construction.** ≈435 triples / 8 constructions in Exp 1 and ≈99 triples / 5 constructions in Exp 2 — so only on the order of tens of items per construction. Any per-construction claim carries wide uncertainty.
- **Repo not inspectable from this environment.** `https://anonymous.4open.science/r/beyond-memorization-B82B` is not reachable here (proxied away / 403), so item-level file structure, file names, column layouts, and per-construction counts are **not** verified. This page deliberately catalogs only what the paper documents; `status: external-only`.
- **Exp-2 0.83 figure is phrased as IAA, not unambiguously as accuracy.** See the caveat in *Dataset structure* above.
- **Version / title drift.** arXiv v1 (8 Jan 2025) was titled "Assessing Language Comprehension in Large Language Models Using Construction Grammar"; v2 (13 Aug 2025) and the published ACL version are "Beyond Memorization: … Using Phrasal Constructions." Quotes on this page are from the **arXiv v2 HTML** (`https://arxiv.org/html/2501.04661v2`) and the **published ACL Anthology** abstract, both fetched 2026-05-29. The source page records the same drift.

## Pointer for next visit

A future run that can reach the repository should:

1. Mirror `https://anonymous.4open.science/r/beyond-memorization-B82B` into `experiments/data/` (NOT the wiki).
2. Inspect the item-level structure: file names, formats, columns; confirm the per-construction triple counts; and determine **whether per-item human labels (not just aggregate accuracy) are released**.
3. Re-confirm the Table 9 example items and the Table 1 human-performance values character-for-character against the PDF/repo.
4. Upgrade `status:` from `external-only` to `catalogued` (or `partial`) accordingly.
5. Only after Tom ratifies the relevant decision(s), add the appropriate `anchors:` link(s) to the [`conjecture/caused-motion-construction`](../../findings/conjectures/caused-motion-construction.md), [`conjecture/conative-construction`](../../findings/conjectures/conative-construction.md), and/or [`conjecture/way-construction`](../../findings/conjectures/way-construction.md) pages (note the full conjecture ids — the first two are `…-construction`).
