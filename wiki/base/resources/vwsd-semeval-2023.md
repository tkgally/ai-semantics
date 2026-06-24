---
type: resource
id: vwsd-semeval-2023
title: Visual Word Sense Disambiguation (VWSD) — SemEval-2023 Task 1 (Raganato et al. 2023)
status: catalogued
url: https://raganato.github.io/vwsd/
url-note: "Official task website https://raganato.github.io/vwsd/ carries the download links (Google Drive + OneDrive) and the only license statement. Code/citation repo: https://github.com/raganato/vwsd (README only — 1011 bytes; contains no data, no images, no LICENSE file; GitHub `license` field is null). Paper PDF: https://aclanthology.org/2023.semeval-1.308.pdf (pages 2227–2234)."
paper: "Raganato, A., Calixto, I., Ushio, A., Camacho-Collados, J., & Pilehvar, M. T. (2023). SemEval-2023 Task 1: Visual Word Sense Disambiguation. In Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023), pages 2227–2234. Association for Computational Linguistics."
venue: "Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023), pp. 2227–2234"
license: "CC-BY-NC 4.0 — stated ONLY on the task website (verbatim: 'The dataset is released under the CC-BY-NC 4.0 license'). Scope (images vs. annotations) NOT specified by the source; the paper body states no license at all; images derive from third-party sources (Wikidata/OmegaWiki/BabelPic), so image-redistribution terms are NOT settled by this CC-BY-NC line. See License & redistribution."
local-path: "NOT FETCHED — no data committed in-repo. Test images (~10.4GB original / 572MB resized) + queries are external Google-Drive/OneDrive downloads; not retrieved this session."
meaning-senses:
  - grounded.perceptual
  - referential.sense
  - human-comparison
contingent-on: []
created: 2026-06-24
updated: 2026-06-24
links:
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/symbol-grounding-problem
---

# Visual Word Sense Disambiguation (VWSD) — SemEval-2023 Task 1 (Raganato et al. 2023)

> **STATUS: scouted 2026-06-24 — catalogued as a typed resource, but with two material caveats that bound what it can anchor (read before citing).**
> 1. **License scope is under-specified and image redistribution is not cleared.** The *only* license statement is the task-website line "The dataset is released under the CC-BY-NC 4.0 license"; it does **not** say whether CC-BY-NC covers the *images*, the *annotations*, or both, and the paper body states no license at all. The images are sourced from third parties (Wikidata, OmegaWiki, BabelPic/BabelNet), whose own terms are not addressed by that one line. **Do not assume the images are freely redistributable.** The project's own annotation overlay (trigger words + gold index) is the part that is safely usable; bulk image redistribution is **unconfirmed** and should not be done without resolving it.
> 2. **Only the *test* and *trial* gold is human-made; the *training* split is silver (automatic).** The 12,869 English training instances are auto-derived from BabelNet structure ("intended for silver data only"). The **human-anchored** signal is the **463 EN + 200 FA + 305 IT gold *test*** instances (plus 16 EN trial), where human annotators chose the trigger words and selected the nine negative images. Anchor only to the gold test/trial split, never to the silver training split.
>
> Subject to those two caveats, license + human-provenance + availability are honestly verifiable, so this is written as a full `resource` page rather than a blocked scouting note. Nothing here was fetched into the repo; the data lives behind external Drive/OneDrive links (see Fetchability).

This page catalogs **VWSD (SemEval-2023 Task 1)** — named on `wanted.md` (P3) and in [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md) as the **image-native** sense-selection anchor: the regime where sense selection *requires* the image rather than treating the image as an add-on. It is the natural instrument for that conjecture's "under-determined" stratum (prediction 1, headroom gating). The companion scouting catalog [`base/resources/multimodal-anchor-scouting.md`](multimodal-anchor-scouting.md) covers the broader VLM-anchor landscape; this page is the focused VWSD scout.

## What it is

VWSD is a **fine-grained, image-native word-sense disambiguation** task. From the paper (Abstract, p. 2227): *"The objective of Visual-WSD is to identify among a set of ten images the one that corresponds to the intended meaning of a given ambiguous word which is accompanied with minimal context."* It is multilingual: *"The task provides datasets for three different languages: English, Italian, and Farsi."*

- **Task format** (§Task formulation, p. 2227): *"Given a target ambiguous word (e.g., coach) and a limited context (e.g. passenger) along with ten images, the Visual-WSD task consists of identifying the most appropriate image for the intended meaning of the ambiguous word."* Each instance is **one ambiguous target word + one or two trigger/context words + 10 candidate images, of which exactly one is gold.**
- **Why image-native, not image-as-add-on** (§Introduction, p. 2227): the context is deliberately minimal — *"minimal context (one or two words) is provided for the target word to increase the disambiguation difficulty"* — and the alternative framing is that *"Visual-WSD is a novel disambiguation task where the sense distinctions are given in the visual modality rather than the conventional textual definitions obtained from lexical sense inventories."* The trigger words are chosen *"so as not to give away the meaning of the image in isolation (i.e., the target word is generally necessary to understand the full context)."* This is exactly the **text-under-determined regime** the grounding-headroom conjecture targets: the image is required to pick the sense.
- **Negative-image design** (§Construction, p. 2228): the nine distractors are not random — they include *"images that correspond to words other than the target that belong to the same domain"* (via BabelDomains), making the choice fine-grained rather than coarse object recognition.

### Sizes (Table 1, p. 2228 — verbatim counts)

| Split | English | Farsi | Italian |
|---|---|---|---|
| **Trial** | 16 | – | – |
| **Training** (silver) | 12,869 | – | – |
| **Test** (gold) | 463 | 200 | 305 |

Each instance carries 10 candidate images. The paper does not report a count of unique images. English is the only language with training/trial data; Farsi and Italian are **gold test only**.

## Human-label provenance (load-bearing)

This is the section that decides what VWSD can anchor for the project (charter rule: cite a resource by the *feature* that bears). The construction is described (§2.2 Construction procedure) as a **"semi-automatic process"** and splits cleanly by split:

**Training (English, 12,869) — SILVER / automatic, not human gold.** The paper is explicit: *"We provide silver training data in English by leveraging BabelNet semantic network structure."* The gold image is the BabelNet-associated picture and the context is auto-derived from the hypernym: *"we first collect a list of senses... together with their associated picture provided by BabelNet. Context words are provided based on each concept hypernym (e.g., chef cook as the context for the word chef)."* It closes: *"This training data is intended for silver data only."* **The project must not treat the training split as a human anchor.**

**Test (463 EN + 200 FA + 305 IT) and Trial (16 EN) — HUMAN-annotated gold.** The paper: *"We provide gold testing data in English, Farsi and Italian."* Human involvement is at two steps:
1. **Trigger-word authoring.** *"for each word sense, we ask an annotator to provide one or two trigger words (the context) that are enough to identify the intended meaning of the word sense when considering the association between definition and image."* Annotators were qualified speakers: *"In the case of English, annotators were proficient English speakers, including the authors of this paper, while in the case of Farsi and Italian, native speakers performed the task."*
2. **Negative-image selection.** *"for each previously validated instance, a human annotator selects nine images from the extension set of candidate images, fulfilling the criteria of selecting related images but different from the target one."*
3. **Validation.** Trial likewise: *"Similarly to the test set, trial instances were validated by annotators."*

**Provenance verdict.** The candidate *target word↔sense↔gold-image* seed comes from BabelNet (automatic), but the **gold test/trial labels carry genuine human signal**: a human chose the disambiguating context and a human curated the nine distractors per item. This is stronger than a purely auto-derived link (contrast SNLI-VE's auto-construction in [`base/resources/multimodal-anchor-scouting.md`](multimodal-anchor-scouting.md)), but weaker than a per-item *graded human relatedness* judgment: VWSD gold is **binary correct-image**, and the authors being among the English annotators is a (disclosed) limit on annotator independence. No inter-annotator agreement statistic is reported in the paper.

## License & redistribution

**Verified license statement (task website, the only one that exists):** *"The dataset is released under the CC-BY-NC 4.0 license."* CC-BY-NC permits non-commercial use, sharing, and adaptation **with attribution** — research use is in scope, commercial use is not.

Three honest qualifications, each verified:

- **Scope is unspecified.** The website line says "the dataset" without distinguishing *images* from *annotations*. It does **not** verbatim state that CC-BY-NC covers the images. (An automated read earlier inferred "images and annotations"; that inference is **not** in the source text and is not asserted here.)
- **The paper body states no license at all.** A full-text search of the PDF found no "license", "CC-BY", "Creative Commons", "copyright", "non-commercial", or "redistribute" — the license claim rests entirely on the task website.
- **Images are third-party-sourced** (§2.1 Data sources, p. 2227–2228): *"The data for this task is mostly obtained from Wikidata, OmegaWiki, and BabelPic"*, with *"BabelNet as a bridge to link the three resources."* Encyclopedic/web-sourced images typically carry their own per-image terms. The single CC-BY-NC line cannot by itself clear bulk **image redistribution**; treat image redistribution as **unconfirmed**.

**Practical consequence for the project:** the **annotation overlay** (the human-authored trigger words and the gold image index per test item) is the part safely usable under CC-BY-NC for non-commercial research with attribution. **Redistributing the images in-repo is not cleared** by what is verifiable; if a probe needs the images, fetch them at run time from the official Drive/OneDrive links and do not re-host them, pending an explicit resolution of image terms.

## Fetchability

**Downloadable now, no registration or form, but via external file-hosts (not in the GitHub repo).** The GitHub repo `raganato/vwsd` contains only a 1011-byte README (no data, no images, no LICENSE file; GitHub `license` field null). All data is on the task website as Google-Drive/OneDrive links (verbatim entries, with the website's stated sizes):

- **[TRAIN+TRIAL]** combined train+trial data, ~17GB (Google Drive + OneDrive); includes gold keys.
- **[TRIAL]** trial-only data (Google Drive); includes gold keys.
- **[TEST]** test images, original size, ~10.4GB (Google Drive + OneDrive).
- **[TEST]** test images, **resized, 572MB** (Google Drive + OneDrive) — the practical option for a probe.
- **[TEST]** test queries in English, Farsi, Italian (Google Drive); includes gold keys.

**Fair-data-usage policy (verbatim, task website):** *"We require users participating in our shared task to adhere to a fair data usage policy. All users agree that they will not attempt to search the trial/training/test data using any search engine on the web, to reverse engineer the data generation process, or to tamper with the data beyond the goals of the task."* This is a behavioral-use constraint on how the data is used in the shared-task setting, distinct from the copyright license.

**Not fetched this session** — no checksum, no in-repo copy. Fetchability is "downloadable now via Drive/OneDrive without authentication," not "fetched + pinned" (contrast the checksummed [`base/resources/lancaster-sensorimotor-norms.md`](lancaster-sensorimotor-norms.md)). A future ingest unit should download the 572MB resized test set + the gold test queries, checksum them, and keep images out of git per the redistribution caveat above.

## What it can ground / known limits

**Fit to the grounding-headroom conjecture (good — this is the point of scouting it).** VWSD instantiates the **text-under-determined regime** by construction: minimal context, with trigger words deliberately chosen so the image is *necessary* to fix the sense. That is precisely the cell [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md) predicts a positive grounding effect Δ > 0 (prediction 1, "headroom gating"), in contrast to the saturated clear-homonym set where the image was redundant ([`result/multimodal-grounding-image-v1`](../../findings/results/multimodal-grounding-image-v1.md)). It is **image-native** — sense selection *requires* the image — rather than image-as-add-on, which is the structural property the conjecture's residual prediction needs.

It can ground:

- `grounded.perceptual` × `referential.sense` × `human-comparison`: whether a model selects the human-gold image for an ambiguous word's intended sense given minimal text — a behavioral test of sense selection that *cannot* be solved from the text alone, against a human-curated gold. The relevant senses are Fregean `Sinn` at the polysemy grain ([`concept/polysemy`](../concepts/polysemy.md)) realized perceptually, within the gradual-grounding framing ([`concept/grounding`](../concepts/grounding.md)); Harnad's symbol-grounding problem ([`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md)) is the conceptual backdrop.

**Known limits — sharp, state them:**

- **Binary gold, not a graded relatedness signal.** VWSD gold is "which one image is correct," not a per-pair human *gradient*. It therefore **cannot** replace the project's DURel/DWUG-style graded sense-relatedness instrument ([`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md)); it tests *selection accuracy*, not *graded similarity*. The grounding-headroom conjecture's instrument is a graded relatedness rating — VWSD supplies a **different** (selection) signal, complementary but not a drop-in for the conjecture's existing DV. Using it requires either adopting accuracy-against-human-gold as the DV or building a graded layer VWSD does not provide.
- **No per-item human gradient / no released human relatedness distribution.** Unlike THINGS triplets or DURel medians, there is no continuous human judgment per item — just the curated gold index. No inter-annotator agreement is reported.
- **Annotator independence is limited.** The English annotators *"includ[ed] the authors of this paper"*; the seed sense↔image link is BabelNet-automatic. The human signal is curatorial/confirmatory over an automatic seed, not an independent crowd judgment.
- **Training split is silver — not an anchor.** Only the 463 EN / 200 FA / 305 IT gold test (and 16 EN trial) instances carry human signal; the 12,869 training instances do not.
- **Image redistribution unconfirmed (see License).** The annotations are usable under CC-BY-NC for non-commercial research; image re-hosting is not cleared.
- **Not a constructional or reference-fixing anchor.** It bears on perceptual disambiguation of *lexical sense*; it does **not** touch `referential.externalist` (Putnam/Evans — still un-anchored in-repo). A model picking the gold image shows behavior *sensitive to* perceptual input in the under-determined residual; it is **not** evidence of a perceptual symbol system or of reference-fixing. Keep "selected the human-gold image" separate from "is perceptually grounded."

## Provenance (quotes + locators)

All quotes are from the paper PDF (Raganato et al. 2023, *Proc. SemEval-2023*, pp. 2227–2234) unless marked "task website."

| Claim | Verbatim quote | Locator |
|---|---|---|
| Task = pick 1 of 10 images for the intended sense, minimal context, 3 languages | "The objective of Visual-WSD is to identify among a set of ten images the one that corresponds to the intended meaning of a given ambiguous word which is accompanied with minimal context. The task provides datasets for three different languages: English, Italian, and Farsi." | Abstract, p. 2227 |
| Task formulation (word + context + 10 images) | "Given a target ambiguous word (e.g., coach) and a limited context (e.g. passenger) along with ten images, the Visual-WSD task consists of identifying the most appropriate image for the intended meaning of the ambiguous word." | §Task formulation, p. 2227 |
| Sense distinctions are in the visual modality (image-native) | "Visual-WSD is a novel disambiguation task where the sense distinctions are given in the visual modality rather than the conventional textual definitions obtained from lexical sense inventories" | §Introduction, p. 2227 |
| Minimal context by design | "minimal context (one or two words) is provided for the target word to increase the disambiguation difficulty" | §Introduction (objectives), p. 2227 |
| Image sources (third-party) | "The data for this task is mostly obtained from Wikidata, OmegaWiki, and BabelPic" ... "We use BabelNet as a bridge to link the three resources" | §2.1 Data sources, p. 2227–2228 |
| Construction is semi-automatic | "In the following section we describe the semi-automatic process to construct the Visual-WSD dataset." | §2.1, p. 2228 |
| Training is silver/automatic via BabelNet | "We provide silver training data in English by leveraging BabelNet semantic network structure." ... "This training data is intended for silver data only." | §2.2 (Training data), p. 2228 |
| Test gold is human; annotators authored triggers | "We provide gold testing data in English, Farsi and Italian." ... "we ask an annotator to provide one or two trigger words (the context) that are enough to identify the intended meaning" | §2.2 (Testing data), p. 2228 |
| Who the annotators were | "In the case of English, annotators were proficient English speakers, including the authors of this paper, while in the case of Farsi and Italian, native speakers performed the task." | §2.2, p. 2228 |
| Humans selected the nine negatives | "for each previously validated instance, a human annotator selects nine images from the extension set of candidate images, fulfilling the criteria of selecting related images but different from the target one." | §2.2, p. 2228 |
| Trial validated by annotators | "Similarly to the test set, trial instances were validated by annotators." | §2.3 Statistics, p. 2228 |
| Counts | Table 1: Trial EN 16; Training EN 12869; Test EN 463 / FA 200 / IT 305 | Table 1, p. 2228 |
| License (website only) | "The dataset is released under the CC-BY-NC 4.0 license." | task website https://raganato.github.io/vwsd/ |
| Fair-data-usage policy | "We require users participating in our shared task to adhere to a fair data usage policy. All users agree that they will not attempt to search the trial/training/test data using any search engine on the web, to reverse engineer the data generation process, or to tamper with the data beyond the goals of the task." | task website https://raganato.github.io/vwsd/ |
| No license in paper body | Full-text search of the PDF found no occurrence of "license", "CC-BY", "Creative Commons", "copyright", "non-commercial", or "redistribute". | PDF, all 8 pages (negative result) |
| Repo carries no data/images/LICENSE | github.com/raganato/vwsd contents: only [`README.md`](../../../README.md) (1011 bytes); GitHub `license` field = null; default branch `main`. | GitHub API `repos/raganato/vwsd` + `/contents/` |

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| Citation (Raganato, Calixto, Ushio, Camacho-Collados, Pilehvar 2023; SemEval-2023; pp. 2227–2234) | **VERIFIED** | Paper header |
| Task = 1-of-10 image selection, ambiguous word + 1–2 context words | **VERIFIED** | Abstract + §Task formulation |
| 3 languages (EN, IT, FA) | **VERIFIED** | Abstract |
| Counts: trial EN 16; train EN 12869; test EN 463 / FA 200 / IT 305; 10 images/instance | **VERIFIED** | Table 1 + §Construction |
| Training split = silver (automatic, BabelNet) | **VERIFIED** | §2.2 |
| Test/trial gold = human-annotated (trigger words + negative selection + validation) | **VERIFIED** | §2.2, §2.3 |
| Image sources = Wikidata / OmegaWiki / BabelPic (BabelNet bridge) | **VERIFIED** | §2.1 |
| License = CC-BY-NC 4.0 | **VERIFIED (website only)** | task website |
| License scope: does CC-BY-NC cover the images? | **NOT SPECIFIED by source** | website line says only "the dataset"; paper silent |
| Image redistribution rights | **UNCONFIRMED** | third-party image sources; no per-image terms addressed |
| Inter-annotator agreement statistic | **NOT REPORTED** | paper (negative result) |
| Number of unique images | **NOT REPORTED** | paper (negative result) |
| Data fetchable now without registration | **VERIFIED** | task website Drive/OneDrive links (not fetched this session) |
| Per-item graded human relatedness signal | **NOT PROVIDED** | gold is binary correct-image |

## Pointer for next visit

1. **If a grounding-headroom probe is greenlit**, this is the image-native instrument for the under-determined stratum. Fetch the **572MB resized test set + the gold test queries** (EN at minimum), checksum them, keep images out of git per the redistribution caveat, and write a PREREG fixing the DV *before* any model call (charter §8). Note that VWSD's native DV is **selection accuracy vs. human gold**, not the DURel-style graded relatedness the conjecture's existing instrument uses — decide and freeze which DV before running.
2. **Resolve the image-license question** before any redistribution: confirm from the organizers / per-image source terms whether the images (not just annotations) may be re-hosted. Until then, fetch-at-runtime only.
3. **Anchor only to the gold test/trial split.** The 12,869 training instances are silver and carry no human signal.
4. **Treat a positive image effect carefully.** Per the conjecture's distraction caveat, a model can score above chance by surface image dissimilarity alone; any sense claim needs the same-referent distraction control the prior image probe built.
