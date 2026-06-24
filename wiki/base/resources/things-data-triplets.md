---
type: resource
id: things-data-triplets
title: THINGS-data behavioral triplet odd-one-out similarity judgments (Hebart et al. 2023)
status: scouted
url: https://osf.io/f5rn6/
url-note: "Behavioral triplet odd-one-out data: OSF project https://osf.io/f5rn6/ ('THINGS-odd-one-out'). Also mirrored on Figshare+ as 'THINGS-data: Behavioral odd-one-out data and code' (https://plus.figshare.com/articles/dataset/THINGS-data_Behavioral_odd-one-out_data_and_code/20552784; part of collection DOI 10.25452/figshare.plus.c.6161151). The THINGS *images* themselves live in a separate OSF project (https://osf.io/jum2f/, Hebart et al. 2019 PLOS ONE) with DIFFERENT terms (academic-use-only — see License). Paper: eLife 12:e82580 (https://elifesciences.org/articles/82580). NOTHING FETCHED in-repo this session; routes verified from landing pages only."
paper: "Hebart, M. N., Contier, O., Teichmann, L., Rockter, A. H., Zheng, C. Y., Kidder, A., Corriveau, A., Vaziri-Pashkam, M., & Baker, C. I. (2023). THINGS-data, a multimodal collection of large-scale datasets for investigating object representations in human brain and behavior. eLife, 12, e82580. https://doi.org/10.7554/eLife.82580"
venue: "eLife 12:e82580 (2023)"
license: "Behavioral triplet data: stated CC0 (public domain dedication) in the paper / secondary sources — BUT the OSF node f5rn6 metadata returns node_license = null (no machine-readable license on the node itself); CC0 NOT confirmed verbatim from a primary licence field this session. THINGS *images* are a SEPARATE matter: the original THINGS image set (osf.io/jum2f) is academic/research-use only ('fair use in the United States', restrictions on visualizing images in publications); only THINGSplus (Stoinski et al. 2024, BRM) supplies one public-domain/CC0 image per concept for free reuse. Do NOT conflate the two."
local-path: "NOT FETCHED — no data committed in-repo. Behavioral data is downloadable from OSF/Figshare+; images are a separate, restricted download. Nothing retrieved or checksummed this session."
meaning-senses:
  - grounded.perceptual
  - human-comparison
contingent-on: []
created: 2026-06-24
updated: 2026-06-24
links:
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/embodied-cognition
---

# THINGS-data behavioral triplet odd-one-out similarity judgments (Hebart et al. 2023)

> **STATUS: scouted 2026-06-24 — catalogued as a typed `resource` (basics verifiable), but `status: scouted` not `catalogued` for two material reasons, read before citing.**
> 1. **The CC0 license is asserted by the *paper / secondary sources*, NOT confirmed from a primary machine-readable license field.** The OSF node `f5rn6` API metadata returns `node_license = null` — i.e. the node carries no embedded license. The "CC0" claim is real (it appears in the eLife data-availability discussion and is widely reported), but this session could not read a CC0 statement *verbatim from the OSF/Figshare licence field itself*; treat CC0 on the behavioral data as **stated-but-not-primary-verified**.
> 2. **The behavioral data and the images have DIFFERENT terms — the images are restricted.** The triplet judgments are the (reported-CC0) behavioral asset; the THINGS *object images* are a separate OSF project published under US "fair use" for research, with explicit restrictions on showing the images in publications. THINGSplus later added one public-domain/CC0 image per concept precisely to lift that restriction. **Any image-using probe must source images from THINGSplus (or PD/CC0), not assume the THINGS images are freely redistributable.**
>
> **Most important — the fit verdict (see "What it can ground / known limits"): THINGS triplets DO NOT cleanly anchor the grounding-headroom conjecture's graded prediction-1.** They supply graded human *whole-object similarity* (odd-one-out among three objects), which is a **different construct** from the conjecture's graded *word-sense relatedness with disambiguating images*. THINGS is a partial/adjacent fit at best, not a drop-in for the DURel-style graded sense-relatedness Δ. Reasons below.

This page scouts **THINGS-data behavioral triplet odd-one-out judgments** as a candidate *graded* multimodal human anchor for [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md) — specifically for prediction-1-as-written, which this session's ratification noted "remains open for a future **graded-image resource**." The companion image-native scout is [`base/resources/vwsd-semeval-2023.md`](vwsd-semeval-2023.md) (binary selection, no graded signal); the project's existing **graded lexical-sense** anchor is [`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md) (DURel-style 4-point usage-pair proximity). THINGS sits between them on the modality axis but, crucially, on a *different construct* axis.

## What it is

THINGS-data is the core behavioral release of the THINGS initiative: large-scale human **triplet odd-one-out** similarity judgments over the THINGS object concept/image set. From the eLife paper (Hebart et al. 2023):

- **Task (verbatim, Results):** *"In a triplet odd-one-out task, participants (N=12,340) were presented with three objects from the THINGS database and were asked to indicate which object is the most dissimilar."* The signal per trial is which of three objects is the odd one out; aggregated across the embedding it yields a graded object-similarity space.
- **Number of judgments:** **4.70 million** similarity judgments (Abstract). Methods give the exact figure **4,699,160 triplets**, of which **4,574,059** comprised the training and test data.
- **Concepts / images:** **1,854 object concepts** and **26,107 manually curated naturalistic object images** (THINGS set, Hebart et al. 2019 PLOS ONE). For the behavioral triplets the unit is the 1,854 concepts (one representative image per concept in the odd-one-out task).
- **Collection:** crowd-sourced (Amazon Mechanical Turk); the behavioral component is the input to the SPoSE / similarity-embedding model (github.com/ViCCo-Group/SPoSE).

The `~4.7M` figure the scouting brief flagged is **confirmed** (4,699,160 exactly; 4.70M as headline). The 1,854-concept / 26,107-image counts are **confirmed** against both the THINGS-data paper and the original THINGS PLOS ONE database.

## License

**Behavioral triplet data — reported CC0, but not primary-verified this session.**
- Reported by the eLife data-availability discussion and multiple secondary reads as released under the **Creative Commons CC0 public domain dedication** (behavioral odd-one-out dataset, OSF `f5rn6`).
- **However**, the OSF node API (`https://api.osf.io/v2/nodes/f5rn6/`, fetched 2026-06-24) returns `"node_license": null` — the node carries **no embedded license metadata**. Node title verbatim: *"THINGS-odd-one-out"*; description verbatim: *"4.7 million odd-one-out similarity judgments of 1854 natural objects"*; `public: true`, `registration: false`.
- The Figshare+ mirror ("THINGS-data: Behavioral odd-one-out data and code", part of collection DOI `10.25452/figshare.plus.c.6161151`) was **HTTP 403** to WebFetch this session; its licence field was not read verbatim.
- **Verdict:** CC0 on the behavioral data is **stated and plausible but not confirmed from a primary licence field**. A future ingest must read the licence directly off the OSF file/component or the Figshare+ item before relying on CC0.

**THINGS images — a SEPARATE, RESTRICTED matter (do not conflate).**
- The original THINGS object images (Hebart et al. 2019, OSF `jum2f`) are **academic/research-use** under US fair use, with restrictions on reproducing them in publications. From THINGSplus (Stoinski et al. 2024, BRM, PMC10991023, fetched 2026-06-24), verbatim: *"while mostly unlimited use of THINGS is possible for research purposes, there are still restrictions for visualizing THINGS images in publications."*
- **THINGSplus** added one freely-reusable image per concept to lift this: verbatim *"We only chose candidate images with a public domain or CC0 copyright license."* So a PD/CC0 image per concept exists, but it is the **THINGSplus** asset, not the base THINGS images.
- **Practical consequence:** the *behavioral judgments* may be reusable (reported CC0); the *base images* are not freely redistributable. An image-using probe must pull from THINGSplus / PD-CC0, exactly as the project's prior image probe sourced Wikimedia PD/CC0.

## Fetchability

- **Behavioral triplet data:** OSF project `https://osf.io/f5rn6/` (public, no registration to browse; `public: true` confirmed via API). Also mirrored on **Figshare+** ("THINGS-data: Behavioral odd-one-out data and code"; collection DOI `10.25452/figshare.plus.c.6161151`). Format not inspected this session (the brief said do not download the full set); the behavioral release is tabular triplet data + analysis code (SPoSE). **Route verified; format UNVERIFIED.**
- **Images:** separate OSF project `https://osf.io/jum2f/` (THINGS) and the THINGSplus norms/images (Springer BRM 2024). The base-THINGS image download is gated by the academic-use terms above.
- **Not fetched, not checksummed this session.** Contrast the checksum-pinned [`base/resources/lancaster-sensorimotor-norms.md`](lancaster-sensorimotor-norms.md); this is "route verified," not "fetched + pinned."

## What it can ground / known limits

**The load-bearing judgment: does THINGS anchor the grounding-headroom conjecture's *graded* prediction-1? Verdict: NO, not cleanly — it is a different construct. Partial/adjacent fit at best.**

The conjecture's prediction-1-as-written needs a **per-item graded human signal of word-sense relatedness** (Δ = image-induced movement toward that graded signal), reusing the **DURel-style graded relatedness instrument** the lexical program validated ([`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md): 4-point usage-pair proximity for **two usages of the same target word**). THINGS supplies something structurally different:

- **Construct mismatch (the decisive gap).** THINGS triplets measure **whole-object similarity** — "of these three *objects*, which is most dissimilar" — yielding a graded **between-concept** object-similarity space (e.g. how similar is *dog* to *wolf* vs *chair*). The conjecture needs graded **within-word sense relatedness** — how related are two *usages/senses of one ambiguous word*, with images disambiguating the sense. Object-similarity (resemblance between distinct object concepts) is **not** word-sense relatedness (Fregean `Sinn` distance between senses of one lexeme). A high THINGS similarity between *bat(animal)* and *bat(sports)* is not even defined in the odd-one-out frame — the two are different concepts/images, not two senses of one word probed for relatedness.
- **No polysemy / sense structure.** THINGS concepts are **disambiguated object concepts**, deliberately one-sense-per-entry (the database samples *object concepts*, not ambiguous word forms). It carries **no** same-word, different-sense pairs — the exact thing the conjecture's graded Δ is computed over, and the same gap DWUG has (no homonym pairs) but for a more basic reason: THINGS is not organized around lexical ambiguity at all.
- **Graded, multi-rater, human — that part fits.** Where THINGS *does* match is the property VWSD lacks: it is a **graded** (continuous embedding from millions of judgments), **multi-rater**, **human** similarity signal over **depicted objects** with **images attached**. That is genuinely a "graded-image resource." So on the *modality + gradedness* axes it is what the ratification asked for; it fails only on the *construct* (object-similarity vs sense-relatedness).

**What THINGS COULD legitimately anchor (adjacent, not the conjecture-1 Δ):**
- `grounded.perceptual` × `human-comparison`: whether a model's representational geometry over **object concepts** aligns with the human odd-one-out similarity embedding — i.e. a *representational-alignment* claim (this is exactly how it is used in the human-alignment literature, e.g. Muttenthaler et al.). That is a real, well-anchored use — but it is a **between-concept object-similarity** alignment test, not a within-word graded-sense-relatedness test, and so it answers a *different* question than the grounding-headroom conjecture poses.
- A **stimulus source / similarity prior** for *building* a future graded sense set: THINGS images (via THINGSplus PD/CC0) could supply depicted-object stimuli, and the THINGS similarity space could pre-stratify object pairs by human-rated similarity — useful scaffolding, but the graded *sense-relatedness* labels would still have to come from a DURel-style instrument, not from THINGS.

**What THINGS CANNOT ground:**
- The conjecture's **prediction-1-as-written graded Δ** — because there is no per-item graded *word-sense relatedness* signal and no within-word sense pairs (the construct gap above).
- Any **lexical polysemy / homonymy** contrast — THINGS has no ambiguous-word structure.
- **Reference / extension** (`referential.externalist`) — like every in-repo resource, it carries no human-agreed extension; even its object-similarity is `grounded.perceptual` × `human-comparison`, not reference-fixing.
- A **drop-in replacement** for DWUG's graded sense anchor — it measures a different relation (object resemblance, not same-word usage proximity), exactly as CoSimLex was rejected for measuring a different relation in [`base/resources/dwug-usage-graphs.md`](dwug-usage-graphs.md).

**Bottom line:** THINGS-data is a strong, large, graded, human, image-linked resource — but for the **wrong construct** relative to this conjecture. It is the right *shape* of signal (graded + image) on the wrong *axis* (object similarity, not word-sense relatedness). The "future graded-image resource" the ratification envisaged would need graded human **sense-relatedness with disambiguating images per usage**; THINGS supplies graded human **object similarity**. Record it as **partial / does-not-cleanly-fit**, not as the anchor.

## Provenance (quotes + locators)

| Claim | Verbatim quote | Locator |
|---|---|---|
| Odd-one-out task definition | "In a triplet odd-one-out task, participants (N=12,340) were presented with three objects from the THINGS database and were asked to indicate which object is the most dissimilar." | eLife 82580, Results |
| Judgment count | "4.70 million similarity judgments" (Abstract); "4,699,160 triplets", of which "4,574,059 triplets comprised the training and test data" (Methods) | eLife 82580, Abstract + Methods |
| Concepts / images | "1,854 object concepts" and "26,107 manually curated naturalistic object images" | eLife 82580, Results / THINGS PLOS ONE 2019 |
| OSF node = behavioral data, no license | node title "THINGS-odd-one-out"; description "4.7 million odd-one-out similarity judgments of 1854 natural objects"; `"node_license": null`; `public: true` | api.osf.io/v2/nodes/f5rn6/, fetched 2026-06-24 |
| Images academic-use-only / pub restriction | "while mostly unlimited use of THINGS is possible for research purposes, there are still restrictions for visualizing THINGS images in publications." | THINGSplus (PMC10991023), fetched 2026-06-24 |
| THINGSplus images are PD/CC0 | "We only chose candidate images with a public domain or CC0 copyright license." | THINGSplus (PMC10991023), fetched 2026-06-24 |
| Behavioral data reported CC0 | "The work is made available under the Creative Commons CC0 public domain dedication." (data-availability discussion / secondary reads — NOT confirmed from OSF/Figshare licence field) | eLife 82580 data-availability (secondary); contradicted by OSF node_license=null |

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| Citation (Hebart et al. 2023, eLife 12:e82580) | **VERIFIED** | eLife header + DOI |
| Task = triplet odd-one-out, choose most dissimilar of 3 objects | **VERIFIED verbatim** | eLife Results |
| 4,699,160 triplets (~4.70M); 4,574,059 train/test | **VERIFIED** | eLife Abstract + Methods |
| 1,854 concepts; 26,107 images | **VERIFIED** | eLife Results + THINGS PLOS ONE 2019 |
| Behavioral data hosted on OSF f5rn6 (+ Figshare+ mirror) | **VERIFIED (route)** | OSF API + Figshare+ search; format not inspected |
| Behavioral data licence = CC0 | **STATED, NOT PRIMARY-VERIFIED** | secondary/data-availability YES; OSF node_license = null; Figshare+ 403 this session |
| THINGS *images* academic-use-only, pub restrictions | **VERIFIED verbatim** | THINGSplus PMC10991023 |
| THINGSplus supplies one PD/CC0 image per concept | **VERIFIED verbatim** | THINGSplus PMC10991023 |
| File format of behavioral release | **UNVERIFIED** | not downloaded (per brief) |
| Per-item graded human *word-sense relatedness* signal | **NOT PROVIDED** | THINGS measures object similarity, not sense relatedness |
| Within-word / polysemy sense pairs | **NOT PROVIDED** | THINGS samples disambiguated object concepts |
| Fit to grounding-headroom prediction-1 graded Δ | **DOES NOT CLEANLY FIT (partial/adjacent)** | construct gap: object similarity ≠ word-sense relatedness |

## Pointer for next visit

1. **Do not promote THINGS as the conjecture-1 graded anchor.** It is the right shape (graded + image, human, multi-rater) on the wrong construct (object similarity, not word-sense relatedness). The "future graded-image resource" the ratification wants still needs **graded human sense-relatedness with disambiguating images per usage** — a resource THINGS does not provide.
2. **If used at all, use it for representational-alignment of object-concept geometry** — a distinct, legitimate question, anchored to the human odd-one-out embedding — and write that as its own claim, not as a grounding-headroom test.
3. **Before any reuse, confirm the behavioral-data licence from a primary field** (OSF file/component licence or Figshare+ item; the node metadata is null and the Figshare+ page 403'd this session). Do not assume CC0 without reading it.
4. **Never redistribute the base THINGS images.** Source depicted-object stimuli from THINGSplus (PD/CC0) or Wikimedia PD/CC0, downscaled + sha256-frozen before any model call, as the prior image probe did.
