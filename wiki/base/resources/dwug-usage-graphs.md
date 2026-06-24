---
type: resource
id: dwug-usage-graphs
title: DWUG — Diachronic Word Usage Graphs (Schlechtweg et al. 2021)
status: partial
url: https://zenodo.org/records/14028531
url-note: "DWUG EN latest version (v3.0.0) confirmed HTTP 200 on 2026-05-30; download URL https://zenodo.org/records/14028531/files/dwug_en.zip?download=1 returned HTTP 200, ~17 MB. DOI 10.5281/zenodo.14028531. License: CC BY-ND 4.0 (see License below — NOT plain CC BY as previously noted in wanted.md and the anchor decision). Data not mirrored in-repo."
paper: "Schlechtweg, D., Tahmasebi, N., Hengchen, S., Dubossarsky, H. & McGillivray, B. (2021). DWUG: A large Resource of Diachronic Word Usage Graphs in Four Languages. EMNLP 2021, pp. 7079–7091. https://aclanthology.org/2021.emnlp-main.567/ (arXiv preprint: https://arxiv.org/abs/2104.08540)"
venue: "EMNLP 2021"
license: "Creative Commons Attribution No Derivatives 4.0 International — https://creativecommons.org/licenses/by-nd/4.0/legalcode (confirmed on Zenodo records for DWUG EN, DE, ES, SV 2026-05-30; see License section for implications)"
meaning-senses:
  - distributional
  - referential
  - human-comparison
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: anchors
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# DWUG — Diachronic Word Usage Graphs (Schlechtweg et al. 2021)

> **Verification status (2026-05-30):** License VERIFIED (CC BY-ND 4.0, not plain CC BY — a correction to `wanted.md`/anchor-decision wording). DURel annotation scale VERIFIED verbatim. Total-judgment count VERIFIED from primary source. DWUG EN download URL fetchable (HTTP 200). Per-lemma (40), per-usage-pair (29k), and agreement (ρ .69 / α .61) counts for DWUG EN VERIFIED from the primary Table 3 (independent pass 2026-05-30); annotator count VERIFIED = **9 for EN** (the "4" was only the starting count — a correction to the earlier draft). See the Verified / Unverified / Open breakdown at the end of this page. **Anchor status: carries `anchors:` link contingent on Tom's ratification of the license assessment and the diachronic-vs-synchronic fit note below** — the intellectual fit is established (graded human usage-similarity signal, same DURel tradition as Usim, 4-point graded scale) but the ND license restriction and the diachronic design are both open questions the orchestrator should surface to Tom before promoting any result.

This page catalogs the DWUG (Diachronic Word Usage Graphs) resource — the Option-B candidate anchor ratified by Tom on 2026-05-29 for [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md). The anchor decision [`decisions/resolved/lexical-sense-gradience-anchor`](../../decisions/resolved/lexical-sense-gradience-anchor.md) identified DWUG as the leading candidate; this page records what was actually confirmed on 2026-05-30.

**Critical correction:** `wanted.md` and the anchor-decision text described DWUG as "CC BY." The actual license on all DWUG language versions inspected — EN, DE, ES, SV, and the latest version of DWUG SV — is **CC BY-ND 4.0** (Attribution-NoDerivatives), not plain CC BY. Only DWUG LA (Latin) uses CC BY 4.0. This matters for mirroring; see the License section.

## What it is

DWUG (Diachronic Word Usage Graphs) is the largest resource of graded, contextualized, diachronic word meaning annotation in four languages — English (EN), German (DE), Swedish (SV), Latin (LA) — distributed as per-language archives on Zenodo. The abstract of Schlechtweg et al. 2021 (EMNLP; retrieved via Semantic Scholar API, 2026-05-30) states verbatim:

> "Word meaning is notoriously difficult to capture, both synchronically and diachronically. In this paper, we describe the creation of the largest resource of graded contextualized, diachronic word meaning annotation in four different languages, based on 100,000 human semantic proximity judgments."

The full cross-language resource contains 168 Diachronic Word Usage Graphs (DWUGs) across the four languages. Each graph is associated with a target word; nodes are corpus usage-instances of that word (from two time periods); edges are weighted by the **human-rated semantic proximity** of each usage pair, using the DURel annotation framework.

### Annotation scale

The DURel 4-point annotation scale, **verified verbatim** from the DURel Annotation Tool paper (Schlechtweg et al.; https://arxiv.org/html/2311.12664v2, fetched 2026-05-30):

> "4: Identical, 3: Closely Related, 2: Distantly Related, 1: Unrelated"

Annotators could additionally respond **"Cannot decide"** (same source). The scale is ordinal, human-assigned per usage-pair. This is the same DURel tradition as Usim but a 4-point rather than 5-point scale (Usim's scale: 1 – completely different … 5 – identical).

The paper describes the procedure: annotators "judge usage pairs on a semantic proximity scale avoiding the a priori definition of word senses" (from blog.junge-sprachwissenschaft.de/2021/08/01/Schlechtweg-DURel-Annotation-Tool.html, fetched 2026-05-30).

### DWUG EN — counts (verified from primary, Table 3)

These figures were **verified from the primary source** — the EMNLP 2021 paper's Table 3 (EN row), read directly from the PDF by an independent verification pass on 2026-05-30 (the earlier "partially verified, secondary citation" status is superseded):

- **Target words (lemmas):** **40** (for English; 168 DWUGs total across all four languages). **VERIFIED** (Table 3, EN row).
- **Judged usage pairs:** **29,000** (for English; "total no. of judged usage pairs", JUD column). **VERIFIED** (Table 3). **Version caveat:** this is the count in the 2021 paper. The v3.0.0 archive under audit (Zenodo 14028531) "extends previous versions with one more annotation round", and the WUGsite now lists DWUG EN at **~69k** judgments — so the released v3.0.0 is larger than the 29k reported in the paper. State the version when citing a count.
- **Annotators:** **9 total for English** (Table 3, AN column = 9). The "four annotators per language" figure is only the *starting* count: the paper states verbatim (§4.1) "We started out with four annotators per language. Following high annotation loads and dropouts, additional annotators were hired, resulting in 9/8/5 total annotators for EN/DE/SV, respectively." (Correction 2026-05-30: a prior draft said "~4 per language" — that understates the EN count by more than half.)
- **Total judgments (all languages):** ~100,000 ("based on 100,000 human semantic proximity judgments", EMNLP 2021 abstract, verbatim from Semantic Scholar API fetch 2026-05-30; the paper body §6 adds "In total, roughly 100,000 judgments were made by annotators").
- **Source corpus:** Clean Corpus of Historical American English (CCOHA); two time periods (1810–1860 and 1960–2010).
- **Annotator agreement:** Spearman ρ = 0.69 (SPR column), Krippendorff's α = 0.61 (KRI column) for English. **VERIFIED** (Table 3).

The paper further notes that "annotators make frequent use of the intermediate levels of the scale ('2','3') and thus assign graded distinctions of word meaning" — direct support for the conjecture's intermediate-regime prediction.

## License

**Verified license (2026-05-30):** All DWUG language-specific archives checked — DWUG EN (Zenodo records 14028531, 5796878, 7387261), DWUG DE (records 7441645, 14028509), DWUG ES (record 6433667), DWUG SV (records 7389506, 14028906) — carry the license:

> "Creative Commons Attribution No Derivatives 4.0 International"

License URL: https://creativecommons.org/licenses/by-nd/4.0/legalcode

The Zenodo description for DWUG EN v2.0.0 adds: **"Republication and redistribution is prohibited."** (quoted directly from the Zenodo record).

**Exception:** DWUG LA (Latin; Zenodo record 5255228) uses **CC BY 4.0**, not CC BY-ND. The Latin dataset is not relevant to the English-focused lexical-sense-gradience conjecture.

**What CC BY-ND 4.0 permits and restricts (per Creative Commons, https://creativecommons.org/licenses/by-nd/4.0/, fetched 2026-05-30):**

> "Share — copy and redistribute the material in any medium or format for any purpose, even commercially."
> "If you remix, transform, or build upon the material, you may not distribute the modified material."

The CC license FAQ (per web search result, 2026-05-30) further clarifies: "A company may annotate a work under an ND license for internal purposes and circulate it internally, and even if the annotated version is considered an adaptation, this does not violate version 4.0 of the ND licenses so long as the annotated copy is not shared outside the company."

**Practical implication for this project:**
- **Permitted:** Mirroring the verbatim DWUG EN archive to `experiments/data/dwug/` (verbatim redistribution, no modification).
- **Permitted:** Running experiments on the data (reading usage pairs and human-rated proximities); this is analysis, not distribution of a derivative.
- **Prohibited:** Distributing a modified version of the dataset publicly (e.g., a re-annotated or augmented version; adding columns and releasing the result externally).
- **Grey area:** Adding a polysemy/homonymy stratification column to the data files and committing that augmented file to a public repo. This may constitute a derivative; to be safe, keep the stratification layer separate from the raw DWUG files. The orchestrator should surface this to Tom before any augmented version is distributed.

**Correction notice:** The project's `wanted.md` (current entry for DWUG) and the [`decisions/resolved/lexical-sense-gradience-anchor`](../../decisions/resolved/lexical-sense-gradience-anchor.md) description both describe DWUG as "CC BY." This is incorrect — the actual license on all DWUG language releases inspected (EN, DE, ES, SV) is **CC BY-ND 4.0**. The orchestrator should update those entries when integrating this page.

## What it can ground

This is the key section (charter rule: cite a resource by the *feature* that actually bears).

**DWUG can ground the gradience (monotonicity) prediction (conjecture/lexical-sense-gradience, prediction 1).** Because DWUG carries **graded, multi-rater, 4-point human judgments of semantic proximity between usage pairs of the same target word**, it supplies exactly the graded signal the conjecture's monotonicity clause needs: one can ask whether an LLM's same/different-sense signal is monotonic in human-rated usage proximity across the range 1–4. This is the property no binary set (WiC) has.

The paper states synchronic uses are possible — "diachronic and synchronic uses for this dataset" (EMNLP 2021 abstract, secondary citation via web search 2026-05-30) — so within-time usage pairs can be extracted for a static gradience anchor even though the corpus design is diachronic.

The DURel scale ("4: Identical … 1: Unrelated") is conceptually equivalent to Usim's 5-point gradience scale and carries the same load-bearing property: a continuous-ish graded signal over usage pairs of the same lemma.

**More specifically, DWUG grounds:**
- `distributional` × `human-comparison`: the human proximity signal is drawn from contextualized usage pairs, grounding a claim about whether an LLM's distributional-similarity signal tracks this human gradation.
- `referential.sense` probing: usage proximity in the DURel tradition is an operational stand-in for sense relatedness — two usages rated 4 (Identical) are effectively same-sense; two rated 1 (Unrelated) are effectively different-sense; intermediate ratings (2–3) mark the graded middle that lexicographic gradience predicts should be a distinct regime for polysemy but absent for homonymy.

## What it cannot ground

- **Polysemy vs. homonymy contrast out of the box.** DWUG does not tag pairs as polysemy vs. homonymy; prediction 2 of [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) still needs a stratification step (e.g., from a dictionary or from WordNet sense-relatedness) added on top of the DWUG pairs — this is work-to-be-done, not a property of the released ratings. See the `lexical-sense-gradience` conjecture's *Notes* for this caveat.
- **Reference / extension.** Like every in-repo resource, DWUG carries no human-agreed extension (reference, not sense). It bears on `referential.sense`, not `referential.reference`.
- **Over-/under-splitting against a full sense inventory.** DWUG deliberately avoids committing to a discrete sense inventory; it cannot ground a claim about model sense granularity vs. WordNet. That comparison needs SemCor/OntoNotes.
- **Static synchronic polysemy without diachronic selection.** The English source corpus (CCOHA) spans 1810–2010 in two time periods; the DWUG EN usage-pair graph may contain cross-period pairs (old vs. modern usages of a word that has changed meaning) in addition to within-period pairs. A probe using DWUG for a static gradience anchor should filter or account for the diachronic structure — use within-period pairs only, or consider whether cross-period pairs introduce confounds for a synchronic gradience claim. This is a methodological note, not a disqualifier, but it should be resolved before running.

## Fit assessment: DWUG vs CoSimLex

Both were identified as candidates in the anchor decision. The 2026-05-30 verification produces a clear recommendation:

**DWUG EN — recommended (with caveats).**
- License: CC BY-ND 4.0. Permits analysis and verbatim mirroring; prohibits distributing modified versions. Adequate for the intended use with the caveat noted above.
- Scale: 4-point DURel (1=Unrelated … 4=Identical), human, multi-rater, **9 annotators for EN** (Table 3). Graded signal over usage pairs of the same target word.
- Design fit: measures human semantic proximity between two usages of the **same target word** — exactly the signal [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) needs for the monotonicity clause. The diachronic design is a complication (requires filtering within-period pairs) but is acknowledged as a solvable methodological step, not a disqualification.
- Fetchable: YES, confirmed HTTP 200.

**CoSimLex — not recommended for this conjecture.**
- License: **NOT stated in the CoSimLex paper** (no license or download URL in the text). The CC BY 4.0 on Zenodo record 3989788 is the **distinct SemEval-2020 Task 3 artifact**, not the CoSimLex release proper — a conflation corrected 2026-06-24 once the paper was read firsthand; see [`source/armendariz-2020-cosimlex`](../sources/armendariz-2020-cosimlex.md). The license of the CoSimLex release itself is unverified.
- Design mismatch: CoSimLex measures similarity between **pairs of different words** (from SimLex-999) rated in two different contexts — confirmed from the primary (each word pair presented in two Wikipedia-sourced three-sentence contexts; [`source/armendariz-2020-cosimlex`](../sources/armendariz-2020-cosimlex.md), §4.1). The lexical-sense-gradience conjecture requires graded similarity between **two usages of the same target lemma** (as in Usim / DWUG). CoSimLex cannot ground the conjecture's monotonicity clause; it addresses a different task (contextual word-pair similarity, not same-word usage-pair proximity).
- Annotation scale: **0 to 6** (verbatim, §4.2 of arXiv 1912.05320 — confirmed via [`source/armendariz-2020-cosimlex`](../sources/armendariz-2020-cosimlex.md); the earlier "0–10" here was an unverified HuggingFace-value inference and is **wrong**).
- English coverage: **333 pairs (§3) / 341 entries as built (§5)** — paper-reported figures now read firsthand (the earlier "~333–340 from secondary sources" is superseded; released-data counts still to be confirmed against the files).
- Fetchable: YES, HTTP 200.

**Summary:** CoSimLex fails on design fit, not license. DWUG EN fits on design (graded usage-pair proximity for the same word), has a confirmed fetchable archive, a known scale, and adequate license for analysis — but the CC BY-ND label needs to be surfaced to Tom as a correction to the prior description ("CC BY"), and the diachronic-vs-synchronic extraction plan should be documented before running any probe.

## Where it lives — download

- **Latest DWUG EN:** https://zenodo.org/records/14028531 (Zenodo DOI 10.5281/zenodo.14028531)
  - Direct download: https://zenodo.org/records/14028531/files/dwug_en.zip?download=1 — confirmed HTTP 200, ~17.0 MB, 2026-05-30.
  - Version: 3.0.0 ("extends previous versions with one more annotation round and new clusterings").
- **Previous DWUG EN versions:** Zenodo records 5796878 (v2.0.0, 2021-12-15), 7387261 (v2.0.1, 2022-11-30). All carry CC BY-ND 4.0.
- **All languages and full dataset description:** https://www.ims.uni-stuttgart.de/data/wugs (WUGsite).
- **GitHub (code + dataset pointer):** https://github.com/Garrafao/WUGs

If/when mirrored: place at `experiments/data/dwug/dwug_en.zip` (NOT in the wiki). Do not modify the archive contents before mirroring.

## Known limits / scope

- **CC BY-ND 4.0, not CC BY.** The `wanted.md` entry and the anchor decision text both say "CC BY." This is incorrect. The license on DWUG EN is CC BY-ND 4.0. The practical difference is that a modified/augmented version of the dataset may not be distributed publicly. Analysis use and verbatim mirroring are permitted. Tom should be aware of this before any stratification layer is distributed.
- **Diachronic design.** DWUG pairs span two time periods; within-time pairs must be selected explicitly for a synchronic gradience anchor. The paper notes "diachronic and synchronic uses" — this is a methodological step, not a blocker, but it requires freezing the within-period pair selection before any probe (charter §8 re: instrument-before-results).
- **Per-lemma/pair counts for EN: VERIFIED (2026-05-30).** "40 target words, 29k judged usage pairs" were read directly from the paper's Table 3 (EN row) by an independent pass. Version caveat: the released v3.0.0 archive (Zenodo 14028531) is larger (~69k judgments per the WUGsite) after later annotation rounds.
- **Annotator count: VERIFIED = 9 for EN (2026-05-30).** Table 3 (AN column) gives 9 total annotators for English; "four per language" was only the starting count before dropouts/hires (paper §4.1, verbatim quoted above). A prior draft's "~4" is corrected.
- **Data not mirrored or inspected in-repo** (`status: partial`). The Zenodo record and download URL are verified; the archive contents, file format, and exact within-time pair extraction procedure are not yet confirmed.

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| License: CC BY-ND 4.0 on DWUG EN (all versions checked) | **VERIFIED** | Zenodo records 14028531, 5796878, 7387261, 7441645 (DE), 14028509 (DE), 6433667 (ES), 14028906 (SV); all consistent; fetched 2026-05-30 |
| License URL https://creativecommons.org/licenses/by-nd/4.0/legalcode | **VERIFIED** | Zenodo records above |
| DURel scale "4: Identical, 3: Closely Related, 2: Distantly Related, 1: Unrelated" | **VERIFIED verbatim** | arxiv.org/html/2311.12664v2 (DURel Annotation Tool paper), fetched 2026-05-30 |
| "Cannot decide" option available | **VERIFIED** | Same source |
| Total judgments ~100,000 across all languages | **VERIFIED verbatim** | EMNLP 2021 abstract via Semantic Scholar API, 2026-05-30 |
| DWUG EN download URL fetchable (HTTP 200, ~17 MB) | **VERIFIED** | curl HEAD 2026-05-30 |
| DWUG EN 40 target words | **VERIFIED** | Primary paper Table 3 (EN row), read directly 2026-05-30 |
| DWUG EN 29k judged usage pairs (2021 paper; v3.0.0 archive ~69k) | **VERIFIED** | Primary paper Table 3 (JUD); v3.0.0 size per WUGsite |
| Annotators = **9 for EN** (started from 4) | **VERIFIED / PRIOR DRAFT CORRECTED** | Table 3 (AN=9) + §4.1 "9/8/5 total annotators for EN/DE/SV"; earlier "~4" was the starting count only |
| Agreement ρ .69 / α .61 (EN) | **VERIFIED** | Primary paper Table 3 (SPR/KRI) |
| Within-time (synchronic) pair subset is extractable | **PARTIALLY VERIFIED** | EMNLP abstract mentions "diachronic and synchronic uses"; corpus spans two periods; details not inspected |
| Data format (file structure inside dwug_en.zip) | **UNVERIFIED** | Archive not downloaded or inspected |
| CoSimLex scale = **0 to 6** (earlier "0–10" CORRECTED) | **VERIFIED verbatim** | §4.2 of arXiv 1912.05320, primary read 2026-06-24 via source/armendariz-2020-cosimlex |
| Prior claim that DWUG is "CC BY" | **CORRECTED** | All DWUG EN/DE/ES/SV records carry CC BY-ND 4.0, not CC BY |

## Pointer for next visit

1. **Surface the CC BY-ND license correction to Tom** (not plain CC BY as stated in `wanted.md` and the anchor decision). Confirm the intended use (analysis + verbatim mirror) is acceptable under CC BY-ND. The orchestrator integrates `wanted.md` and the anchor-decision text; correction belongs there.
2. **Confirm per-language statistics** by reading the EMNLP 2021 paper statistics table (available as EMNLP PDF, or via arXiv if HTML is restored). The key figures: EN lemma count, usage-pair count per language, annotator count.
3. **Mirror and inspect:** Download `dwug_en.zip` into `experiments/data/dwug/` (verbatim, no modification — CC BY-ND permits). Inspect the file structure, confirm the judgment-level TSV format (usage-pair × annotator × rating), and identify within-period pairs (both usages from the same time period) for the synchronic gradience anchor.
4. **Freeze the synchronic pair selection** before running any probe (charter §8: instrument-before-results). Document the selection rule (e.g., "retain only pairs where both usages are from the same time period and the same lemma") in a design page under `experiments/designs/`.
5. **Add polysemy/homonymy stratification** as a separate annotation layer (not modifying the DWUG files) using a dictionary or WordNet sense-relatedness measure. This stratification is needed for conjecture prediction 2 and is work-to-be-done, not given by DWUG itself.
6. **Upgrade `status:`** from `partial` to `catalogued` (or `verified`) once the archive is mirrored and the file format is confirmed.
