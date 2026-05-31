---
type: resource
id: wic-word-in-context
title: WiC — the Word-in-Context Dataset (Pilehvar & Camacho-Collados 2019), binary same/different-sense judgments
status: verified
url: https://pilehvar.github.io/wic/
url-note: "WiC project page https://pilehvar.github.io/wic/ returned HTTP 200 (23,490 bytes) on 2026-05-31. The full dataset package https://pilehvar.github.io/wic/package/WiC_dataset.zip returned HTTP 200 (275,984 bytes; this page's copy sha256 f1a2fb67d903c5b9b1180f1035d4228f7c0254e8f5f868d556235457046bd4b2) — and, unlike the SuperGLUE distribution, THIS package ships gold labels for the test split too. The dataset is also redistributed inside SuperGLUE (https://dl.fbaipublicfiles.com/glue/superglue/data/v2/WiC.zip, HTTP 200) where the test labels are HIDDEN behind the leaderboard."
paper: "NAACL 2019 (short) https://aclanthology.org/N19-1128/ ; arXiv https://arxiv.org/abs/1808.09121 ; HTML mirror https://ar5iv.labs.arxiv.org/html/1808.09121"
venue: "NAACL 2019 (short); also a SuperGLUE task (https://super.gluebenchmark.com/tasks) and the IJCAI-2019 SemDeep-5 challenge"
license: "Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) — https://creativecommons.org/licenses/by-nc/4.0/legalcode (stated verbatim on https://pilehvar.github.io/wic/, fetched 2026-05-31)"
meaning-senses:
  - distributional
  - referential
  - human-comparison
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: anchors
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# WiC — the Word-in-Context Dataset (binary same/different-sense)

> **Verification status (2026-05-31): VERIFIED from the actual released package + the paper.** The data file was fetched and inspected directly (HTTP 200; split line-counts, POS distribution, label balance, and unique-target counts read off the files themselves), and the construction method + license were confirmed verbatim from the project page and the NAACL-2019 paper (ar5iv HTML mirror). This page is written to serve **any** probe that needs a binary same/different-sense human contrast — both the text lexical-v3 polysemy-vs-homonymy discreteness test ([`design/lexical-polysemy-homonymy-v3`](../../../experiments/designs/lexical-polysemy-homonymy-v3.md)) and a multimodal image probe against the same anchor — so the "what it can / cannot ground" sections are kept general.

WiC was already named, but not catalogued as its own page, as the **binary cross-check** for [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) (the prior catalog entry [`resource/wic-graded-usage-similarity`](wic-graded-usage-similarity.md) describes WiC only in passing). The ratified anchor decision [`decisions/resolved/lexical-sense-gradience-anchor`](../../decisions/resolved/lexical-sense-gradience-anchor.md) calls WiC "the binary cross-check." This page is the verified, standalone WiC catalog.

The **load-bearing property** — the reason WiC is catalogued separately from the graded DWUG/Usim sets — is the *opposite* of theirs: WiC carries **binary** (not graded) human same/different-sense labels over **two contexts of the same target word**, and its negatives are **enriched for clearly-distinct (more homonym-like) sense pairs** by an explicit construction rule (see *Sense inventory & construction*). That makes it the natural anchor for a **discreteness** contrast — exactly what the graded DWUG anchor could not supply (the [`result/lexical-polysemy-homonymy-v2`](../../findings/results/lexical-polysemy-homonymy-v2.md) null was a *design gap*: too few clean homonyms in DWUG EN). It is **not** an anchor for a graded monotonicity claim; that scope limit is stated plainly below.

## What it is

**WiC (Word-in-Context).** Each instance gives a target word *w* — a noun or a verb — in **two** sentence contexts, and the task is a **binary** judgment. From the project page (https://pilehvar.github.io/wic/, fetched 2026-05-31, verbatim):

> "The task is to identify if the occurrences of w in the two contexts correspond to the same meaning or not."

Labels are **T** (True — same meaning) / **F** (False — different meaning). From the paper (NAACL 2019, ar5iv HTML mirror, verbatim):

> "Each instance in WiC has a target word w, either a verb or a noun, for which two contexts are provided. Each of these contexts triggers a specific meaning of w. The task is to identify if the occurrences of w in the two contexts correspond to the same meaning or not."

It was introduced in Mohammad Taher Pilehvar & Jose Camacho-Collados, *WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations*, NAACL 2019 (short) (https://aclanthology.org/N19-1128/; arXiv 1808.09121).

### The human signal — how the labels were produced

WiC labels are **not** crowd same/different votes. They are derived from **expert lexicographers' sense assignments** in standard sense inventories: two contexts get label **T** if the inventory lists them under the *same* sense of *w*, **F** if under *different* senses. From the paper (ar5iv, verbatim):

> "An instance can be either positive or negative, depending on whether the corresponding c₁ and c₂ are listed for the same sense of w in the target resource."

> "Lexicographer examples constitute a reliable base for the construction of the dataset, as they are curated in a way to be clearly distinguishable across different senses of a word."

So the "human" in WiC is **lexicographer sense-inventory structure**, not a per-item rating panel — a `human-comparison` signal of the same family as a sense-annotated corpus, but binary and inventory-derived. (The paper reports the dataset is "based on annotations curated by experts"; the per-instance label is the expert sense split, not a graded judgment.)

### Sense inventory & construction (this is what makes WiC homonymy-enriched)

Contexts are real lexicographer **example usages** drawn from three inventories. From the paper (ar5iv, verbatim):

> "Contextual sentences in WiC were extracted from example usages provided for words in three lexical resources: (1) WordNet Fellbaum (1998), the standard English lexicographic resource; (2) VerbNet Kipper-Schuler (2005), the largest domain-independent verb-based resource; and (3) Wiktionary, a large collaborative-constructed online dictionary. We used WordNet as our core resource, exploiting BabelNet's mappings Navigli and Ponzetto (2012) as a bridge between Wiktionary and VerbNet to WordNet."

The paper reports the initial example pool sizes (per the WebSearch summary of the paper body, secondary to the verbatim quotes above): "The total number of initial examples extracted from all resources were 23,949, 10,564 and 636 for WordNet, Wiktionary and VerbNet, respectively." (Recorded as a count, not a verbatim quote — flagged in *Provenance gaps*.)

**The construction rule that biases the negatives toward clearer (more homonym-like) distinctions** (paper, ar5iv, verbatim):

> "We removed all pairs whose senses were first degree connections in the WordNet semantic graph, including sister senses, and those which belonged to the same supersense."

This matters for any discreteness test: WiC's **F** (different-sense) pairs deliberately **exclude** the *closest* polyseme pairs (first-degree WordNet neighbours, sister senses, same supersense), so the negatives skew toward more clearly-separated senses. WiC is therefore **rich in clear different-sense (often homonym-like) contrasts** — its strength as a discreteness anchor — but it is **not** a clean source of *fine* polyseme-vs-homonym gradation, because the hardest near-polyseme negatives were pruned out. (See *What it cannot ground*.)

### Counts (VERIFIED directly from the released package, 2026-05-31)

Read off the actual files in `WiC_dataset.zip` (each `.data.txt` and matching `.gold.txt` have equal line counts; one line = one instance):

| Split | Instances | Label balance (F / T) | POS (N / V) | Unique target words |
|---|---|---|---|---|
| train | **5,428** | 2,714 / 2,714 (exactly balanced) | 2,794 / 2,634 | 1,265 |
| dev   | **638**   | 319 / 319 (exactly balanced)     | 395 / 243   | 599   |
| test  | **1,400** | 700 / 700 (exactly balanced)     | 831 / 569   | 1,184 |
| **total** | **7,466** | 3,733 / 3,733 | 4,020 / 3,446 | 2,345 (distinct across all splits) |

The split sizes 5,428 / 638 / 1,400 and the test "1,184 unique target words" figure match the paper's reported statistics (ar5iv). Every split is **exactly 50/50** T/F — a balanced binary benchmark.

### Data format (VERIFIED from the package README)

Each `.data.txt` is a tab-separated file; README.txt verbatim:

> "target_word <tab> PoS <tab> index1-index2 <tab> example_1 <tab> example_2"
> ... "PoS": ... (either "N": noun or "V": verb). ... "index1-index2": indicates the index of target_word in example_1 and example_2, respectively. ... In this version all examples are tokenized.

and the gold file:

> "(dev/train/test).gold.txt: This file contain the gold labels, which can be "T" (True) or "F" (False) depending on whether the intended sense of the target word is the same in both examples or not."

So each item carries: **target word**, **POS (N/V)**, **whitespace-token indices** of the target in each of the two **tokenized** contexts, the two contexts, and a binary gold label. Example line (train, verbatim from the file): `carry⟶V⟶2-1⟶You must carry your camping gear .⟶Sound carries well over water .` (gold `F`).

## License

From the project page (https://pilehvar.github.io/wic/, fetched 2026-05-31, **verbatim**):

> "This dataset is licensed under a Creative Commons Attribution-NonCommercial 4.0 License"

License URL: https://creativecommons.org/licenses/by-nc/4.0/legalcode.

**Practical implication (CC BY-NC 4.0):** non-commercial research use and analysis are permitted with attribution; redistribution is permitted for non-commercial purposes with attribution; building/redistributing a *derivative* (e.g. a re-annotated subset) is allowed under BY-NC as long as use stays non-commercial and attribution is preserved (BY-NC has **no** ND clause — unlike DWUG's CC BY-ND). For this project's purposes (research analysis, non-commercial), the practical posture mirrors DWUG: **do not commit the corpus example sentences to the public wiki**; commit only the reproducible recipe (download URL + sha256) + an item manifest of identifiers + gold labels + any derived stratification layer. This is conservative; CC BY-NC would likely permit more, but the recipe-not-corpus posture keeps the wiki license-clean regardless.

## What it can ground — and the specific feature that bears

(Charter rule: cite a resource by the *feature* that bears, not by existence.)

- **A binary same/different-sense human contrast over two contexts of the same word.** WiC's **T/F** labels are exactly a *discrete* per-item human (lexicographer-inventory) judgment of whether two usages of *w* are the same sense — the load-bearing signal for the conjecture's **prediction 5** (binary cross-check) and, more sharply, for a **discreteness / separability** test ([`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) clause b). A model's same/different-sense calls (or a continuous relatedness rating thresholded) can be scored against WiC's binary gold via agreement / AUC / a same-minus-different gap.
- **A homonymy-enriched different-sense pool.** Because the closest polyseme negatives were pruned (the "first-degree connections … sister senses … same supersense" rule), WiC's **F** items concentrate on clearer sense splits, so it supplies the *clearly-distinct* end of the contrast that DWUG EN lacked enough of. This is precisely the gap the v2 null identified.
- **A large, balanced, POS-typed item base** (7,466 items, 50/50, nouns and verbs, 2,345 distinct targets) — far larger than the graded sets (Usim 1,530 pairs / DWUG EN ~hundreds of within-period pairs), so a subset can be drawn to balance whatever stratification a design needs.
- **`human-comparison` × `referential.sense`:** the same-meaning judgment is a Fregean *Sinn* (mode-of-presentation) signal; the conjecture's null is that LLM behaviour reduces to context similarity (`distributional`). WiC supplies the human discrete-sense axis against which that is tested.

## What it cannot ground

- **Graded monotonicity / a DURel-style correlation.** This is the trap the seed open-question warns about and the reason WiC is *not* the gradience anchor: WiC is **binary by design**. It cannot ground "the model's signal is *monotonic* in human-rated relatedness," because it has no graded human relatedness axis. Any model rating run on WiC items can be correlated **only** against the **binary** label (a same/different separation, e.g. AUC or a mean-gap), **never** against a graded human median. A probe that uses WiC must scope its human-comparison claim to **binary same/different**, not to graded relatedness. (The graded claims stay anchored to [`resource/dwug-usage-graphs`](dwug-usage-graphs.md).)
- **A clean fine-grained polyseme-vs-homonym gradation out of the box.** WiC labels same/different sense but does **not** tag *which* different-sense pairs are homonymy (etymologically unrelated) vs distant polysemy. Worse for the gradient, its construction **pruned the closest polyseme negatives**, so the *near*-polyseme middle that a gradience study most wants is under-represented among the negatives. A polysemy/homonymy split must be **added** (e.g. by WordNet sense-relatedness or an etymological rule, as in the v2 stratification) and frozen with the item set — it is work-to-be-done, not a property of the released labels.
- **Reference / extension.** Like every in-repo resource, WiC carries no human-agreed *extension*; it bears on `referential.sense`, not `referential.reference` (see [`concept/referential-meaning`](../concepts/referential-meaning.md)).
- **Over-/under-splitting against a full sense inventory.** WiC is pairwise binary, not a sense-tagged corpus; the granularity-vs-WordNet question needs SemCor/OntoNotes, not WiC.
- **A perceptual / multimodal grounding signal by itself.** WiC is text-only (lexicographer example sentences). A multimodal image probe that uses WiC as its *sense* anchor supplies the images from elsewhere; WiC contributes only the binary same/different-sense human label over the two **text** contexts. State the image source's own provenance separately.

## Known limits / scope

- **Binary, not graded** (restated — it is the central scope limit; see *What it cannot ground*).
- **Negatives pruned of the closest polyseme pairs.** The "removed all pairs whose senses were first degree connections … sister senses … same supersense" rule makes WiC's different-sense pool *easier* / more clearly-separated than an unpruned sample would be. This is a feature for a discreteness anchor and a limitation for a fine-gradience anchor.
- **Sense-inventory labels, not per-item human ratings.** The T/F gold reflects expert sense-inventory structure (WordNet/VerbNet/Wiktionary, bridged via BabelNet). It is a curated expert signal but not an inter-annotator graded rating with a published agreement coefficient the way DWUG (ρ≈.69) or Usim (3 raters) are; the paper reports the curation as expert-based. Treat WiC agreement claims as "agreement with the lexicographer sense split," not "agreement with a rating panel."
- **Two WiC distributions differ on test labels.** The **pilehvar.github.io** package inspected here **includes** test gold labels (`test/test.gold.txt`, 1,400 lines, balanced). The **SuperGLUE** distribution of WiC withholds test labels (scored on the leaderboard). A probe should use the pilehvar package (test labels present) and cite which distribution it used.
- **English only** (the multilingual extension XL-WiC, Pilehvar et al. EMNLP 2020, is a separate resource not catalogued here).
- **Tokenized contexts.** Examples are whitespace-tokenized ("In this version all examples are tokenized"), and the target index is a whitespace-token index — a probe that re-presents the sentence to a model should account for the tokenization (e.g. de-tokenize lightly, or mark the target by its given index).

## Where it lives — download

- **Project page + dataset:** https://pilehvar.github.io/wic/ (HTTP 200, 2026-05-31). Full package (incl. test gold): https://pilehvar.github.io/wic/package/WiC_dataset.zip (HTTP 200, 275,984 bytes, sha256 `f1a2fb67d903c5b9b1180f1035d4228f7c0254e8f5f868d556235457046bd4b2` for the copy fetched 2026-05-31).
- **SuperGLUE copy (test labels hidden):** https://dl.fbaipublicfiles.com/glue/superglue/data/v2/WiC.zip (HTTP 200).
- **Paper:** https://aclanthology.org/N19-1128/ · arXiv https://arxiv.org/abs/1808.09121 · HTML https://ar5iv.labs.arxiv.org/html/1808.09121.

If/when mirrored: place at `experiments/data/wic/` (NOT in the wiki). Commit the recipe (URL + sha256) + an identifier/gold manifest, not the corpus example sentences (conservative posture; see License).

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| License: CC BY-NC 4.0 | **VERIFIED verbatim** | https://pilehvar.github.io/wic/ , fetched 2026-05-31 |
| Task = binary same/different sense (T/F) | **VERIFIED verbatim** | project page + paper (ar5iv) + package README |
| Split sizes 5,428 / 638 / 1,400 | **VERIFIED (direct file line-count + paper)** | unzipped package, 2026-05-31; matches ar5iv |
| Exact 50/50 T/F balance per split | **VERIFIED (direct)** | `sort | uniq -c` on the gold files |
| POS N/V counts; 2,345 distinct targets (1,184 test) | **VERIFIED (direct)** | `cut`/`sort -u` on the data files; test figure matches paper |
| Format: target / PoS / index1-index2 / two tokenized contexts | **VERIFIED verbatim** | package README.txt |
| This package ships test gold labels | **VERIFIED (direct)** | `test/test.gold.txt` present, 1,400 labels |
| Sense inventories WordNet + VerbNet + Wiktionary (WordNet core, BabelNet bridge) | **VERIFIED verbatim** | paper (ar5iv HTML) |
| Positive/negative = same/different sense in the inventory | **VERIFIED verbatim** | paper (ar5iv) |
| Closest-polyseme negatives pruned (first-degree / sister / same supersense) | **VERIFIED verbatim** | paper (ar5iv) |
| Initial example pool 23,949 / 10,564 / 636 (WordNet/Wiktionary/VerbNet) | **RECORDED, secondary** | WebSearch summary of paper body — NOT re-confirmed verbatim from the PDF (PDF text-extraction unavailable this session; see note) |

## Provenance gaps (honest)

- **The NAACL-2019 PDF could not be text-extracted in this environment** (the `cryptography` Python module is broken, so `pypdf`/`pdfminer` failed; `pdftotext` absent). All paper quotes above are taken from the **ar5iv HTML mirror** (https://ar5iv.labs.arxiv.org/html/1808.09121) of the arXiv version, cross-checked against the ACL Anthology landing page. The construction-method quotes are from that HTML mirror, which is a faithful rendering of the arXiv source but is a *mirror*, not the camera-ready PDF — flagged for the next visit to re-confirm against the PDF if a discrepancy ever matters.
- **The initial example-pool counts (23,949 / 10,564 / 636)** come from a WebSearch summary of the paper body, **not** a verbatim fetch — recorded as approximate provenance, not load-bearing for any probe.
- Everything that bears on a probe (license, task, format, counts, the pruning rule) is **either** verified directly from the released files **or** quoted verbatim from the HTML mirror.

## Pointer for next visit

1. If a discreteness result is promoted, re-confirm the "first degree connections … same supersense" pruning quote against the camera-ready PDF (https://aclanthology.org/N19-1128.pdf) once PDF extraction works locally.
2. To add the polysemy/homonymy split WiC lacks, reuse the v2 etymological-fallback rule (or WordNet sense-relatedness if local compute returns) and freeze it with the WiC item subset — see [`design/lexical-polysemy-homonymy-v3`](../../../experiments/designs/lexical-polysemy-homonymy-v3.md).
3. For a multimodal probe, pair WiC's binary sense label with an image source whose own provenance is catalogued separately; keep this page text-neutral.
