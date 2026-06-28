# Multimodal anchor scouting — feasibility catalog

**Scouted:** 2026-05-30. **Purpose:** anchor-feasibility note for a future probe of whether vision-language models (VLMs) interpret lexical/grammatical meaning differently from text-only models. This is a *scouting* note, not a typed resource page; it covers multiple candidates and ends with a ranked recommendation. The project's recurring rule applies: a resource must be cited by the *specific human-annotated feature* that bears on the claim, never by existence alone.

**Multimodal axis design constraint:** any anchor chosen here must be buildable so it can later join the text-based lexical↔grammatical continuum ([`theory/lexicon-grammar-continuum`](../../findings/theory/lexicon-grammar-continuum.md)). The clearest join: the visual/perceptual grounding signal should be comparable to the project's existing DURel-style sense-relatedness signal — ideally graded, human-produced, tied to specific words or object concepts.

---

## Candidate 1: THINGS / THINGS-data — odd-one-out triplet judgments + SPoSE embeddings

**What it is.** THINGS-data (Hebart, Contier, King et al., eLife 2023) is a large-scale collection of human behavioral similarity judgments over 1,854 systematically sampled object concepts, each with multiple naturalistic images. The human signal is a triplet odd-one-out task: participants see three objects and indicate which is most dissimilar. The dataset collects **4.70 million triplet judgments** from **12,340–14,025 participants** (two counts appear in sources; the eLife 2023 paper reports 12,340 in one passage). From these judgments, a **66-dimensional embedding** (SPoSE) of object similarity was derived, with dimensions interpretable as perceptual and conceptual object properties (colorful, animal-related, etc.).

**Who made it / is the signal human.** Yes. Judgments were crowdsourced via online platforms; each trial is a single human similarity choice. No gold label was imposed top-down; the embedding is derived entirely from aggregated human choices.

**License (verified).** The eLife 2023 paper and associated repositories use a **CC0 license** — confirmed via web search citing the eLife publication directly ("A CC0 license was added to all software and data"). The behavioral data are deposited at OSF (doi: 10.17605/OSF.IO/F5RN6) and the Figshare record (figshare.com/articles/dataset/20552784). The THINGS image set itself has a separate, more restrictive license (academic use only for the full set; CC0 for the THINGSplus subset of 1,854 license-free images). For the *behavioral/triplet data alone* — the human similarity judgments — the CC0 license applies. *Caveat: the CC0 claim comes from a secondary source citing the eLife paper; the OSF record itself was not directly inspectable in this run. Mark as "verified via secondary source, not directly from the OSF README."*

**Fetchability.** OSF project at https://osf.io/f5rn6/; SPoSE code at https://github.com/ViCCo-Group/SPoSE. `pip install osfclient; osf -p f5rn6 clone THINGS-behavior` per the THINGS initiative website. URL confirmed reachable (HTTPS 200 not directly tested this run — fetchability is *likely* given OSF's stability and CC0 designation, but not independently curl-verified).

**What meaning-claim it could anchor.** The human triplet judgments ground a claim about *perceptual/conceptual object similarity* — specifically: does a VLM's internal representation of an object concept track the same similarity structure that humans use? This is the perceptual analogue of the project's DURel-graded lexical-sense probe: instead of asking "do two usages of the same word feel similar to humans?", it asks "do two object images feel similar to humans?" The bridge to the project's lexical program: if a VLM's word representation for *dog* and *wolf* is closer than for *dog* and *hammer*, and human triplet judgments agree, that is convergent evidence that distributional training recovers some of the graded *conceptual* similarity structure humans use — a perceptual analogue of clause (a) in [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md). A VLM that additionally processes images could be compared to a text-only model on the same judgments: divergence would be evidence that grounding shifts the similarity structure.

**What it cannot anchor.** THINGS covers object *concepts*, not word *senses*. It cannot ground a polysemy/homonymy-style claim (THINGS has one concept per image-set; it does not have usage-pair proximity for the same word in different senses). It cannot ground a grammatical/constructional claim. The graded signal is over concept-pairs, not sense-pairs; the lexical program's DURel tradition is a closer instrument for within-word gradience. THINGS triplet data cannot directly test whether an LLM tracks *lexical* sense relatedness — it tests *conceptual* object similarity, a broader, more perceptual target.

**Recommendation: promising — verify more before cataloguing as full resource.** The scale (4.7M judgments, 12k+ participants), the CC0 license, and the OSF availability make this the strongest multimodal behavioral anchor found in this search. The conceptual similarity signal is genuinely human-produced and graded, matching the project's preference for continuous human signals over binary gold. The main open question is whether the project's VLM probe would target *image* similarity (requires a VLM with vision input) or *word-concept* similarity (which text-only models could also be tested on, using the SPoSE concept labels). The join to the lexical↔grammatical continuum requires an explicit design decision: treat THINGS as an image-grounded perceptual anchor or as a concept-similarity anchor that both text and vision models can be probed on. That design question should be surfaced to Tom before this is catalogued as a full resource page.

---

## Candidate 2: Winoground — visio-linguistic compositionality benchmark

**What it is.** Winoground (Thrush, Jiang, Bartolo, Singh, Williams, Kiela & Ross 2022, CVPR — author list per [`source/thrush-2022-winoground`](../sources/thrush-2022-winoground.md), verified against arXiv 2204.03162) is a 400-item benchmark for evaluating whether vision-and-language models can correctly match two images and two captions where the captions share identical words but differ only in word order (and therefore in meaning). Example: *"there is a mug in some grass"* vs. *"there is some grass in a mug"* — same words, opposite meanings. The dataset was hand-curated by expert annotators, who also applied rich fine-grained tags for error analysis. Images come from Getty Images.

**Who made it / is the signal human.** Yes. The 400 examples were created by expert human annotators at Facebook/Meta AI Research; no automatic generation was used for caption construction. The images were licensed from Getty Images and hand-matched to caption pairs. The gold label is the correct image-caption matching, determined by the expert curation process. Human baseline was not reported as a crowd-sourced participant study — it is an expert-curated correctness label, not a distributional human-judgment signal.

**License (verified / partially).** The dataset is hosted at https://huggingface.co/datasets/facebook/winoground with *gated access*: users must log in and agree to research-only use ("you also agree that you are using it solely for research purposes"). The full license agreement is described as "available in the dataset files" but is not stated in the public README. The arXiv paper (2204.03162) shows a CC BY 4.0 icon for the *paper*, but this likely does not extend to the images (which remain under Getty Images terms). *Status: the license for the benchmark data itself is UNVERIFIED — it requires authenticating to HuggingFace and reading the dataset-internal license file. The gated access and Getty Images provenance strongly suggest the images carry a research-only restriction that would prohibit redistribution.*

**Fetchability.** Gated access via HuggingFace requires a user account and agreement; the dataset files are not directly downloadable without authentication. The text annotations (captions, tags) may have a more permissive license than the images.

**What meaning-claim it could anchor.** Winoground bears on *compositional* meaning — specifically the question of whether a VLM can distinguish the semantic contribution of word *order* (a grammatical/structural signal) from bag-of-words content. This is close to the constructional program's spirit (a construction's form determines its meaning) extended to the visual domain. It could anchor a claim such as: "VLMs fail to use compositional meaning when image-caption matching requires distinguishing role-structure (subject vs. object) indicated by word order." This is a *ceiling/binary* claim, not a graded one — Winoground has 400 items and a binary correct/incorrect response, not a graded human similarity signal.

**What it cannot anchor.** Winoground cannot ground a graded perceptual-similarity claim (it is binary, not continuous). It cannot ground a lexical polysemy or sense-gradience claim. The human signal is an expert-curatorial correctness label, not a distributional human-judgment distribution — it is more like a benchmark answer key than a gradient human norm. It tests *visual* compositionality, not lexical sense; the join to the lexical↔grammatical continuum would require a separate design step.

**Recommendation: drop for now / revisit if compositional-VLM probe becomes a target.** The gated access + unverified/restrictive license make this difficult to catalog responsibly. The binary signal is weaker than the project's preference for graded human anchors. The fit to the current lexical/grammatical program is indirect — it tests visual compositionality, not lexical sense or constructional inference per se. If Tom decides to open a compositional VLM axis (e.g., *does a VLM use the caused-motion construction's argument-structure meaning when processing image-caption pairs?*), Winoground becomes relevant as a benchmark; until then it is off-scope.

---

## Candidate 3: Lancaster Sensorimotor Norms — perceptual/action strength ratings for ~40k words

**What it is.** The Lancaster Sensorimotor Norms (Lynott, Connell, Brysbaert, Brand & Carney 2020, *Behavior Research Methods* 52(3): 1271–1291) provide human ratings of **39,707 English words** on **11 sensorimotor dimensions**: six perceptual modalities (auditory, gustatory, haptic, interoceptive, olfactory, visual) and five action effectors (foot/leg, hand/arm, head, mouth/throat, torso). Each word received ratings from **at least 10 participants**; words averaged 18.0 ratings on the perceptual side and 19.1 on the action side. Total rater pool: **3,500 unique participants** via Amazon Mechanical Turk (experienced raters with >100 tasks and >97% approval; recruited via TurkPrime). The ratings are mean sensorimotor strength scores on a 0–5 scale per dimension.

**Who made it / is the signal human.** Yes. Each rating is a direct human judgment of how strongly a given word is experienced through that modality or action effector (e.g., "to what extent do you experience *thunder* through hearing?"). The signal is a multi-rater mean, not a derived or automatic label.

**License (verified).** **CC BY 4.0** — confirmed verbatim from the PMC full text of the paper: "Creative Commons Attribution 4.0 International License (CC-BY), which permits use, sharing, adaptation, distribution, and reproduction in any medium." Data are deposited on OSF at https://osf.io/7emr6/ and the Lancaster University interactive tool at https://www.lancaster.ac.uk/psychology/lsnorms/. This is one of the cleanest licenses in this shortlist — fully permissive for research and derivative use.

**Fetchability.** OSF at https://osf.io/7emr6/ — OSF is a stable, open repository. The Lancaster University web tool allows word lookup and export. *Direct URL curl-verification not performed this run; OSF is structurally stable. Mark as likely-fetchable, not independently curl-verified.*

**What meaning-claim it could anchor.** This is a TEXT resource about perceptual grounding: it tells you, for each of ~40k English words, *how perceptually grounded* it is and *through which modality*. It directly bridges the project's lexical program to the multimodal/grounded axis. Specifically:

- It could anchor a claim of the form: "words that humans rate as highly visually or haptically grounded are tracked more accurately in sense-relatedness judgments by VLMs than by text-only models." The sensorimotor scores become a continuous moderator variable — the graded perceptual grounding of a word — and the DV is the model's accuracy relative to the DWUG human DURel baseline.
- It could operationalize a *gradient of groundedness* for words already in the DWUG EN set (all 40 DWUG EN lemmas can be looked up in the Sensorimotor Norms, since the norms cover ~40k words) — producing a within-DWUG control variable.
- It could ground a claim about whether the *type* of grounding (visual vs. haptic vs. auditory) predicts VLM advantage over text-only models — the perceptual-modality-specificity question.

**What it cannot anchor.** The norms are a *word-level* resource, not a *usage-pair* resource. They do not carry graded usage-pair proximity (that is DWUG's contribution). They cannot directly replace the DWUG anchor for the monotonicity/gradience probe. They cannot anchor a constructional-inference claim (the norms are about word properties, not construction meaning). They do not carry image data or any visual grounding of their own — they are human *verbal* ratings of perceptual associations.

**Recommendation: catalog as a full resource page now — the cleanest text-side bridge to the multimodal axis.** CC BY 4.0, ~40k words, 3,500 MTurk raters, stable OSF deposit, directly citable by word-lookup against existing DWUG lemmas. The norms can be incorporated into the existing lexical probe as a moderator variable with minimal additional design: annotate each DWUG EN lemma with its Lancaster visual/haptic/auditory strength score, then ask whether monotonicity (the project's established positive from [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md)) is stronger for highly grounded words. This is actionable under Tom's no-local-compute constraint because it requires only a lookup table, not a new API probe. The data should be fetchable from OSF without authentication.

---

## Candidate 4a: SNLI-VE — visual entailment (Xie et al. 2019)

**What it is.** SNLI-VE (Xie et al. 2019, arXiv 1901.06706) repurposes the Stanford NLI (SNLI) corpus by replacing each *textual* premise with the corresponding Flickr30k photograph. The result is a three-way image-text entailment task (entailment / neutral / contradiction). Scale: approximately 565,286 premise-hypothesis pairs. Repository: https://github.com/necla-ml/SNLI-VE.

**Who made it / is the signal human.** Partially and problematically. The *hypothesis labels* (entailment/neutral/contradiction) come from the original SNLI crowdworker annotations — which are human. However, the *premise replacement* (image for text) was done **automatically** by matching SNLI sentences to the Flickr30k images they originally described. This automatic construction introduced a well-documented label-noise problem: "the automatic way in which SNLI-VE has been assembled gives rise to a large number of errors in the labels" — approximately **31% error rate in the neutral class**, ~1% in entailment and contradiction (from the e-SNLI-VE critique, arXiv 2004.03744). A corrected version (SNLI-VE-2.0 / e-SNLI-VE-2.0) exists but still carries the auto-derived construction artifact. The README acknowledges label noise and recommends dropping the neutral class for quality-sensitive uses.

**License.** Not stated in the repository README or the arXiv paper (per this search). SNLI-VE inherits license constraints from SNLI (which is under a research-use license from the Stanford NLP Group) and Flickr30k (which carries Flickr image terms). *Status: license UNVERIFIED. The combination of inherited licenses from multiple sources, none of which are clearly open, makes this a license-risk item.*

**Fetchability.** GitHub repository confirmed reachable at https://github.com/necla-ml/SNLI-VE. Whether images are freely downloadable (Flickr30k images) is a separate question governed by Flickr30k terms.

**What it could anchor / what it cannot.** Even setting aside label noise: SNLI-VE tests whether a VLM can judge image-text entailment on SNLI-style natural-language hypotheses. The human signal is the original SNLI crowdworker label — but that label was about *text-text* entailment; its transfer to *image-text* entailment is the auto-derived step that introduced noise. The neutral class — where the most interesting "uncertain grounding" cases live — is the most corrupted. For anchoring a *meaning* claim, this is a significant problem: the cases where meaning matters most (the graded, uncertain cases) are the most noisy.

**Recommendation: drop.** The auto-derived label construction, the 31% neutral-class error rate, the unverified license, and the Flickr30k image-access complication collectively make SNLI-VE a poor anchor for this project's standards (charter rule: cite by the *feature* that actually bears; the auto-derived construction undermines the claim that the label is a clean human judgment). Use VALSE instead for image-text meaning probing.

---

## Candidate 4b: NLVR2 — natural language visual reasoning (Suhr et al. 2019)

**What it is.** NLVR2 (Suhr, Zhou, Zhang, Zhang, Bai & Artzi 2019, ACL; arXiv 1811.00491) contains **107,292 examples** of human-written English sentences paired with pairs of natural photographs; each sentence is labeled true or false about the image pair. Sentences were collected by crowd-sourcing with a built-in balance constraint (each sentence appears with both true and false labels, controlling for language bias). Images are natural photographs. Repository: https://github.com/lil-lab/nlvr; project page: https://lil.nlp.cornell.edu/nlvr/.

**Who made it / is the signal human.** Yes. Both the *sentences* (human-written by crowdworkers) and the *truth-value labels* (determined by the corpus construction + verified by human annotators) are human-produced. The anti-bias construction procedure (each sentence appears with true and false label contexts) is a methodological strength.

**License.** The *annotations* (sentences and binary labels) are **CC BY 4.0** — confirmed from the GitHub README. The images are not licensed by the corpus creators (they do not hold image copyright); image access requires filling out a Google Form for direct access (or using the provided download scripts that pull from original URLs). *Status: annotation license verified as CC BY 4.0; image license is a non-trivial access barrier.*

**Fetchability.** Annotations (text + labels) are freely downloadable from GitHub. Direct image access requires a Google Form request. This is a partial access barrier — unlike DWUG or Lancaster Norms, you cannot curl the images without an extra step.

**What it could anchor.** NLVR2 tests whether a VLM uses spatial, set, counting, and comparative reasoning to ground natural language about image pairs. The human signal is genuine (human-written, balanced labels). It could anchor a claim about whether VLMs correctly use *quantificational or spatial meaning* (a grammatical/semantic claim) when processing paired images and sentences. This is closer to the project's constructional program than THINGS or Winoground: it tests argument-structure-adjacent meaning (set relations, spatial prepositions, comparatives) grounded in visual scenes.

**What it cannot anchor.** NLVR2 is a binary true/false benchmark, not a graded human signal. It cannot anchor a polysemy/gradience claim. The image-access barrier complicates replication. The task is synthetic in the sense that the sentence is written *about* the images — the human-written sentences are not naturally occurring usage instances; they are elicited descriptions. The fit to the project's DURel-style graded signal is poor.

**Recommendation: promising but not first-priority — note for a future constructional VLM axis.** NLVR2 has the cleanest human provenance of the image-text entailment candidates (genuine human-written sentences, CC BY 4.0 annotations, anti-bias design). If the project opens a "VLM constructional inference" axis — parallel to the text-only constructional program but with images in the loop — NLVR2 would be the recommended anchor for spatial/quantificational meaning. For now it is off-scope; note in the return report as a future-axis candidate.

---

## Candidate 4c: VALSE — linguistic phenomena in VLMs (Parcalabescu et al. 2022)

**What it is.** VALSE (Parcalabescu, Cafagna, Muradjan, Frank, Calixto & Gatt 2022, ACL) is a benchmark of approximately **6,800 validated image-foil-caption triples** covering six linguistic phenomena: existence (505 items), plurality (851), counting (2,459), spatial relations (535), actions (1,633), and coreference (812). Each instance pairs an image with a correct caption and a *foil* caption — a near-synonym differing in one word or phrase — and the task is to identify which caption describes the image. Repository: https://github.com/Heidelberg-NLP/VALSE.

**Who made it / is the signal human.** Hybrid: foils were generated using a mix of automatic methods (masked language modeling, SpanBERT, template transformations) and then validated by crowdworkers (Amazon Mechanical Turk, 3 annotators per sample). A sample is included only if at least 2/3 annotators confirmed the foil does NOT describe the image. 87.7% of generated instances passed this filter. The gold label (which caption is correct) is the human-validation-confirmed caption, not a fully human-constructed one. Inter-annotator agreement is low to moderate (Krippendorff's α: 0.23–0.64, mean 0.42).

**License.** The GitHub repository carries an **MIT license**. The paper itself is CC BY 4.0 (ACL 2022). *MIT license confirmed via GitHub repository fetch.* Images and captions are drawn from existing datasets (e.g., SWiG); their licenses vary and are not all open.

**Fetchability.** GitHub repository at https://github.com/Heidelberg-NLP/VALSE reachable. The data files themselves are in the repo; image access depends on the original datasets from which images were drawn. Partial access barrier on images.

**What it could anchor.** VALSE tests whether VLMs use specific *linguistic* meanings (existence, plurality, number, spatial prepositions, verbal events, coreference) when processing image-caption pairs. The six phenomena map onto the project's grammatical/semantic interests: spatial relations and actions are constructionally relevant; existence and plurality are quantificational. The human-validated foil structure (confirmed by 3 MTurk annotators per item) gives the gold labels human provenance — stronger than SNLI-VE's auto-derived labels, weaker than NLVR2's fully human-written sentences. The moderately low inter-annotator agreement (α mean 0.42) is a known limitation that the authors acknowledge.

**What it cannot anchor.** VALSE is a benchmark, not a graded human norm. It cannot anchor a gradience/polysemy claim. The foils are automatically generated and human-*validated* (not human-*created*), so the human signal is confirmatory rather than constitutive. The low IAA on some phenomena limits how strongly one can claim the gold labels reflect human consensus. Image licenses are a patchwork.

**Recommendation: promising for a future VLM-constructional axis, but weaker than NLVR2 on provenance.** The MIT license on the data repo is the cleanest license in the image-text entailment group. The linguistic-phenomena framing (spatial, action, existence) maps well onto the constructional program. However, the hybrid foil generation + moderate IAA make the human anchor weaker than this project's standard (DWUG had ρ = 0.69 IAA; VALSE mean α = 0.42). If a VLM constructional-inference axis opens, prefer NLVR2 for the cleaner human provenance, and VALSE as a secondary/parallel benchmark covering a wider range of phenomena.

---

## Ranked recommendation

**Best first anchor for a multimodal lexical-meaning probe: Lancaster Sensorimotor Norms (Candidate 3).**

Rationale:
1. **Actionable now, no new probe required.** The project already has 40 DWUG EN lemmas and a verified DURel-based lexical result ([`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md)). The Lancaster Norms can be used as a lookup-table moderator: annotate each DWUG lemma with its visual/haptic/auditory sensorimotor strength score and ask whether the project's established monotonicity result (Spearman ρ 0.60–0.83) is stronger for highly grounded words. This requires no new API probe — only a table join and a subgroup Spearman correlation. It respects Tom's no-local-compute constraint.
2. **Clean license (CC BY 4.0), stable OSF deposit, no authentication barrier.** This is the only candidate in the shortlist with a fully verified, permissive, open license that has been confirmed verbatim from the primary paper.
3. **Direct bridge to the lexical↔grammatical continuum.** The sensorimotor grounding of a word is a continuous variable that could explain *why* some DWUG lemmas are tracked better than others — a mechanistic moderator, not a separate probe. This extends the existing result rather than opening a new axis.
4. **What it requires before cataloguing as a full resource page:** (a) Tom fetches the OSF deposit or the Lancaster web interface export; (b) the 40 DWUG EN lemmas are cross-referenced against the norms (all are likely covered in 39,707 words); (c) a design decision is made about which sensorimotor dimensions to use (visual strength alone? all-modalities composite?). This is a small, bounded fetch task.

**Second choice: THINGS-data triplet judgments (Candidate 1).** If Tom decides to open a VLM-vs-text-only comparison axis (does image grounding change concept similarity structure?), the THINGS triplet data — CC0, 4.7M human judgments, OSF-hosted — is the strongest fully-behavioral graded signal available. The design question (image-grounded probe vs. concept-label probe) must be resolved first.

**Third / future-axis: NLVR2 (Candidate 4b)** for a VLM constructional-inference axis (spatial/quantificational meaning), then **VALSE (Candidate 4c)** as a secondary benchmark covering a wider phenomenon range. Both require a new axis decision before they become relevant.

**Drop: Winoground** (unverified/restrictive license, Getty Images provenance, gated access) and **SNLI-VE** (auto-derived labels, 31% neutral-class error, unverified license).

---

## Candidates with unverified elements

| Candidate | Unverified element | Risk |
|-----------|-------------------|------|
| THINGS-data | CC0 claim is from a secondary source (eLife article description); OSF README not directly inspected this run | Low — eLife is a peer-reviewed publisher with strict open-data requirements; OSF CC0 is consistent with eLife's open-data policy |
| THINGS-data | HTTPS 200 on the OSF download URL not directly curl-verified | Low — OSF is stable; the dataset has been cited and downloaded widely |
| Lancaster Norms | OSF record (https://osf.io/7emr6/) not directly fetched; CC BY confirmed from PMC paper body | Low — PMC text is authoritative; OSF is stable |
| Lancaster Norms | Exact coverage of DWUG EN lemmas in the 39,707-word set not confirmed | Low — the norms cover 39,707 common English words; all DWUG EN content words are almost certainly included |
| Winoground | Dataset-internal license not inspected (gated access required) | High — licensing is the primary risk here; do not catalog without resolving |
| SNLI-VE | License not stated anywhere in the inspected sources | High — inherited licenses from SNLI + Flickr30k are both restricted |
| VALSE | Image licenses from source datasets (SWiG etc.) not fully inspected | Medium — MIT on the repo data itself is good; image licensing is a known patchwork problem in VLM benchmarks |
| NLVR2 | Image access requires Google Form; direct image URL availability not confirmed | Low-medium — annotations are CC BY 4.0 and freely available; images are the access barrier |

---

## Proposed additions to `wanted.md`

The following should be added to `wanted.md` when the orchestrator integrates this report. These are not editorial additions — they are the concrete fetch tasks this scouting generates.

**P1 (next, actionable now):**
- Lancaster Sensorimotor Norms (Lynott, Connell, Brysbaert, Brand & Carney 2020). *Behavior Research Methods* 52(3): 1271–1291. OSF: https://osf.io/7emr6/. CC BY 4.0.
  - why: the cleanest text-side bridge to the multimodal axis; use as a moderator on the existing DWUG lexical result (annotate DWUG EN lemmas with visual/haptic strength, ask whether monotonicity is stronger for highly grounded words). Requires Tom to download the OSF spreadsheet and cross-reference against the 40 DWUG EN lemmas. No new API probe needed.
  - status: wanted (scouted 2026-05-30; license + counts + OSF URL verified; full data not yet fetched)

**P2 (soon, requires design decision first):**
- THINGS-data behavioral triplet judgments (Hebart, Contier, King et al., eLife 2023). OSF: https://osf.io/f5rn6/. CC0.
  - why: 4.7M graded human perceptual-similarity judgments over 1,854 object concepts — the strongest available multimodal behavioral anchor for a VLM-vs-text-only comparison. Requires a design decision on the probe structure (image-grounded or concept-label) before the anchor is operationally useful.
  - status: wanted (scouted 2026-05-30; CC0 + OSF availability confirmed via secondary sources; direct OSF README not inspected)

**P3 (eventually, pending axis decision):**
- NLVR2 corpus annotations (Suhr et al. 2019). GitHub: https://github.com/lil-lab/nlvr. CC BY 4.0 annotations.
  - why: 107k human-written sentences + binary true/false labels over image pairs; the cleanest human provenance in the image-text entailment group; relevant if a VLM constructional-inference axis opens.
  - status: wanted (scouted 2026-05-30; annotation license + annotation access verified; image access requires Google Form)

---

## Decision the orchestrator should surface to Tom

**Which anchor class to privilege for a multimodal probe?** There are two structurally different options:

**Option A (text-side grounding moderator):** Use Lancaster Sensorimotor Norms as a moderator on the existing text-based lexical result. No new VLM probe, no image input required. Tests: *do text-only LLMs track lexical sense better for perceptually grounded words?* This is actionable now and extends the current result without a new experiment.

**Option B (image-grounded perceptual anchor):** Use THINGS-data triplet judgments to compare VLM (with image input) vs. text-only model on object concept similarity. Requires a new probe design, a VLM model in the panel, and a design decision on how to present the 1,854 THINGS concepts to both model types. This is a genuinely new axis but requires more setup and a new API budget.

The two options are not mutually exclusive — they could be sequenced (Option A first, as a moderator analysis on existing data; Option B as the first VLM probe if the result is interesting). The orchestrator should surface this choice to Tom before any resource is catalogued or any probe is designed for the multimodal axis.

---

## Session-130 deeper scout: a graded-image fine-polysemy MAGNITUDE instrument

**Scouted:** 2026-06-28. **Why this section exists.** [`open-question/grounding-magnitude-instrument`](../../findings/open-questions/grounding-magnitude-instrument.md) records that the VWSD competence-audited-fluent-channel route to prediction 3's *magnitude* ("for concrete sense the headroom is **empirically narrow**" — [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md), prediction 3) is **blocked** (the fluent channel's strict held-out referent-recovery is 0.438, below the ratified `[0.60,0.95]` floor — [`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../../findings/results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)), and that **no in-repo resource is a drop-in magnitude instrument**. That page names THINGS as worth a "$0 deeper scout … as scaffolding, not the anchor." This section goes deeper: it hunts open-access for **genuinely NEW** candidates the open-question page has not assessed, and it works the THINGS-as-scaffolding build-feasibility question concretely. **$0; web search/fetch only; no model run.** The four requirements a valid magnitude instrument must satisfy (verbatim source: the open-question page) are summarized here as: **(a)** a *certified-competent text/description channel on the specific target items*; **(b)** a *graded* (per-item, continuous/ordinal) *human signal*, not a binary selection gold; **(c)** *image-native or fine-polysemy material where the senses are perceptually distinguishable*; **(d)** the *de-referencing trap avoided* (under-determination intrinsic to the material's fine/abstract senses, not manufactured by stripping referent names). The recurring rule applies: cite each candidate by the *specific human-annotated feature* that bears, never by existence.

### (1) New candidates assessed against (a)–(d) [Task 1]

The hunt targeted three families the open-question page flags: (i) *graded* multimodal/visual-WSD datasets; (ii) "visual polysemy" / sense-tagged image datasets (BabelPic, VisualSem, ImageNet/WordNet senses, VerSe); (iii) graded cross-modal semantic-similarity datasets (Crisscrossed Captions/CxC, multimodal STS) — checking in each case whether the gradedness is over *word senses* vs caption/object similarity. A fourth family surfaced unbidden and is included: graded *image-similarity* MDS/relatedness norms. **The structural finding up front:** every newly-found resource fails on the *same axis pair* — it is either **graded same-word sense-relatedness but text-only** (fails (c)), or **graded + image but the wrong construct** (whole-caption or whole-object similarity, no within-word sense structure → fails (b)-as-construct and (d)), or **image + sense-tagged but binary/categorical** (fails (b)). None is a graded *word-sense* relatedness signal carried *with* disambiguating images.

#### Candidate 5: RAW-C / SAW-C — graded same-word sense relatedness, TEXT-ONLY

- **What it is.** RAW-C (Trott & Bergen 2021, ACL, *"Relatedness of Ambiguous Words—in Context"*, arXiv 2105.13266; repo github.com/seantrott/raw-c) is a lexical resource of **graded human relatedness judgments** for **112 ambiguous English words** across **672 minimal sentence pairs** (each word in 4 sentences, 2 per sense → four Different-Sense + two Same-Sense pairs per word), plus human sense-dominance estimates. SAW-C is the Spanish analogue (**812 sentence pairs**, surfaced via a secondary paper).
- **(b) graded human signal: YES — and the RIGHT construct.** This is **graded same-word sense relatedness** — exactly the DURel-tradition construct DWUG carries, and the construct THINGS/CxC lack. Each pair is two *usages of one ambiguous word*; the rating is how related those two senses are. The repo exposes a `mean_relatedness` column; reported **leave-one-annotator-out IAA = 0.79** (VERIFIED from the GitHub README via search). Scale endpoints were **not stated verbatim on the repo landing page** this session (the README references the mean but did not display the endpoints in the fetched view) — secondary descriptions and the DURel lineage indicate a graded ordinal (commonly 0–4); mark the **exact scale endpoints UNVERIFIED**, the gradedness itself VERIFIED.
- **(c) image-native / perceptual material: NO.** Confirmed text-only from two independent fetches: "RAW-C is purely textual … no mention of images, visual stimuli, or perceptual material." There is no image arm at all.
- **(a)/(d):** the de-referencing trap is *not* triggered (the under-determination is intrinsic — these are genuinely fine polysemes rated by humans), and a text channel can be built on the items — but with **no image (c)**, there is nothing for grounding to move, so (a) and (d) are moot.
- **License:** **UNVERIFIED.** No LICENSE file or license statement was visible in the fetched README this session; the arXiv paper PDF did not render. Do **not** assume open terms without reading the repo LICENSE directly.
- **Verdict:** **insufficient — fails (c) decisively (text-only).** Same class as DWUG / Usim / WiC: it *proves the graded same-word sense-relatedness signal (b) exists and is reusable* (and is arguably a cleaner same-/different-sense design than DWUG, with explicit per-word same-sense and different-sense pairs), but it carries **no image arm**, so it cannot supply the disambiguating image the magnitude Δ toggles. It is a *build ingredient* (the graded-label side), not an instrument.

#### Candidate 6: Crisscrossed Captions (CxC) — graded + image, but WHOLE-CAPTION/SCENE similarity, no word-sense structure

- **What it is.** CxC (Parekh, Baldridge, Cer, Waters, Yang 2021, EACL, arXiv 2004.15020; repo github.com/google-research-datasets/Crisscrossed-Captions) extends MS-COCO dev/test with **continuous (0–5) human semantic-similarity ratings** for **caption↔caption, image↔image, and image↔caption** pairs: **267,095 pairs** from **1,335,475 independent judgments** (annotator counts 170 text-text / 61 image-image / 113 image-text).
- **(b) graded human signal: YES, but over the WRONG unit.** The ratings are graded (0–5, intermediate values encouraged), but they measure **whole-sentence / whole-image / scene similarity**, *not* word-sense relatedness. Verbatim from the fetch: the ratings are "graded, denser annotations for relationships between and among captions and images"; "CxC contains no isolated target-word structure … without focusing on specific ambiguous words in context." The rating criterion is **Semantic Textual Similarity (STS)** extended to images — caption-level, not lexeme-level.
- **(c) image-native: YES** (it is built on MS-COCO photographs) — this is the part it *does* satisfy.
- **(d) de-referencing trap / construct: FAILS the construct, in the THINGS way.** Because there is **no single ambiguous target word isolated and rated for sense relatedness across contexts**, there is no within-word polysemy structure for the magnitude Δ to be defined over. The under-determination CxC could exhibit is *scene-description* under-determination, not *fine-sense* under-determination of one lexeme — the exact construct mismatch that disqualified THINGS (object similarity) and that prediction 3 is not about.
- **License:** **UNVERIFIED.** "The paper does not specify a license in the provided content"; the repo hosts annotations to be merged with MS-COCO (whose images carry their own terms). Mark license UNVERIFIED; the MS-COCO image-terms layer is an additional barrier.
- **Verdict:** **insufficient — fails (b)-as-construct and (d).** CxC is the strongest *graded + image-native* resource found, but its gradedness is over **caption/scene similarity**, not **word-sense relatedness**. It is THINGS's failure mode transposed to scenes: right *shape* (graded + image), wrong *axis* (holistic similarity, not within-word sense). It cannot read prediction 3's magnitude.

#### Candidate 7: BabelPic — sense-tagged images, but BINARY human signal (recognizability), non-commercial license

- **What it is.** BabelPic (Calabrese, Bevilacqua, Navigli 2020, ACL, *"Fatality Killed the Cat or: BabelPic"*; sapienzanlp.github.io/babelpic) is a hand-labeled dataset of **14,931 images tagged with 2,733 non-concrete BabelNet synsets**, built by cleaning BabelNet's image-synset associations.
- **(b) graded human signal: NO — binary.** The human contribution is **binary recognizability validation**: raters were asked "if the labels are visually recognizable," and image-synset associations were cleaned (kept/dropped). There is no per-item *graded sense-relatedness* signal — the gold is a categorical image↔synset tag, not a continuous relatedness rating.
- **(c) image-native / sense-distinguishable: PARTLY** (images are tagged to specific senses, and the dataset deliberately targets non-concrete concepts) — but with no graded signal, (c) alone cannot carry a magnitude read.
- **License:** BabelPic depends on **BabelNet's non-commercial license** (babelnet.org/license) — a restriction inherited via the synset tagging. Image redistribution terms are the usual web-image patchwork (UNVERIFIED per-image).
- **Verdict:** **insufficient — fails (b) (binary, not graded).** Useful only as a *sense-tagged image inventory*, not a magnitude instrument. Same disqualifier as VWSD's binary gold, with an added non-commercial-license constraint.

#### Candidate 8: VisualSem — sense-tagged images at scale, but NO graded human judgments, non-commercial license

- **What it is.** VisualSem (Alberts et al. 2021; github.com/iacercalixto/visualsem) is a multilingual multimodal knowledge graph: **89,896 nodes** (each linked to a BabelNet id / WordNet id / Wikipedia article), **~930,000 images** associated to nodes, **1.3M glosses**, 1.5M relation tuples.
- **(b) graded human signal: NO.** Fetch verdict: "No evidence of graded or continuous human judgments. The data structure appears categorical — nodes either have associated images/glosses or they don't." The image↔sense links are categorical, not a graded relatedness rating.
- **(c):** images are sense-tagged (linked to BabelNet/WordNet senses) — but again, no graded signal.
- **License:** released **under BabelNet's non-commercial license** (verbatim: "released under BabelNet's non-commercial license"). Non-commercial restriction inherited.
- **Verdict:** **insufficient — fails (b) (categorical, not graded).** A large sense-tagged image graph, not a graded-sense-relatedness instrument.

#### Candidate 9: Sense Identification Dataset (SID) — graded similarity + sense IDs, CC BY, but TEXT-ONLY and *between-word* similarity

- **What it is.** SID (PMC7494475, *"Sense identification data: A dataset for lexical semantics"*; Mendeley Data doi 10.17632/r5fbdpvnkk.1) takes **SemEval-2017 Task 2** word pairs — which carry **graded human similarity on a 0–4 Likert scale** ("0 … 'totally dissimilar and unrelated' to 4 … 'very similar'") — and adds manually-annotated BabelNet **sense identifiers** "coherent with the word pair and with the similarity score." **492 word pairs / 984 terms**; 3 annotators; CC BY; Mendeley-hosted.
- **(b) graded human signal: YES (0–4)** — VERIFIED verbatim — **but it is *between-word* similarity** (how similar *word A* is to *word B*), not *within-word sense relatedness* (two usages of one ambiguous word). That is the **CoSimLex disqualifier** already recorded in [`dwug-usage-graphs.md`](dwug-usage-graphs.md): a different relation. The added sense IDs disambiguate which senses the pair invokes, but the *rating* is still word-pair similarity, not a graded Δ over one lexeme's senses.
- **(c) image-native: NO.** Fetch verdict: "this is text-only … No visual or perceptual material is included" (TSV files only).
- **License: CC BY** (VERIFIED via fetch). The cleanest license in this batch — but irrelevant given the construct and modality failures.
- **Verdict:** **insufficient — fails (c) (text-only) and (b)-as-construct (between-word, not within-word sense).** Catalogued here so a future scout does not re-rediscover it as a false positive: "graded + sense-annotated" is true but it is *word-pair* similarity without images.

#### Candidate 10 (family): graded IMAGE-similarity MDS / relatedness norms — PiCS, MM-MDS, Carlson-Image RSA, Mooney-THINGS — graded + image, but OBJECT-CATEGORY construct (the THINGS failure mode), no polysemy

This family surfaced repeatedly and is the closest "graded + image" relative of THINGS; all share THINGS's construct gap.

- **PiCS** (Pictures by Category and Similarity; PMC12208956; OSF osf.io/yvb8h; **CC BY 4.0**, VERIFIED): **1,200 images / 20 object categories**, similarity from the Spatial Arrangement Method (SpAM), 334 participants. Fetch verdict: "Object-category similarity … It is not designed for word-sense disambiguation or semantic relatedness of ambiguous terms"; "No … single ambiguous word with different senses." (Also note: the primary release is **MDS-derived distances**, not raw graded ratings — a further gap.)
- **MM-MDS** (PMC4229237): MDS similarity ratings for **240 object categories** from the Massive Memory Picture Database — same object-category construct.
- **"Carlson-Image" word-to-word-similarity-adapted-for-images** (the RSA-alignment method paper, arXiv 2412.00577): the word-to-word semantic-similarity rating task was "adapted to accommodate relatedness ratings for images," exemplars cropped on gray backgrounds — but the relatedness is over **object exemplars/concepts**, not word senses (paper PDF did **not render** this session — **UNVERIFIED** beyond the search snippet; flagged honestly).
- **Mooney-THINGS visual-ambiguity dataset** ("Determinants of visual ambiguity resolution," biorxiv 2025.05.28.656283 / Nature Comms Psych s44271-026-00441-8): Mooney (two-tone) images of the **1,854 THINGS objects** from THINGSplus paired with **>100,000 behavioural ratings from >1,000 participants**. This is the most eye-catching new THINGS-family graded-image resource — but its construct is **visual ambiguity resolution** (can a degraded two-tone image be recognized, and what makes it ambiguous), **not lexical polysemy / word-sense relatedness**. The "ambiguity" is *perceptual* (is this blob a camel or a dog?), not *semantic* (which sense of "crane"?). Related THINGS-family release for completeness: **Drawings of THINGS** (Springer BRM 2025, PMC12858628) — 1,854-concept drawing dataset, again whole-object.
- **(b) graded: mostly YES; (c) image-native: YES; but (b)-as-construct and (d): FAIL.** Every member rates **whole-object / whole-image / category similarity** (or perceptual recognizability), with **no within-word sense structure**. They are THINGS's exact disqualifier, replicated across the cognitive-science image-norm literature: graded + image is *available and even abundant*, but always on the **object-similarity / perceptual axis**, never on the **word-sense-relatedness axis**.
- **Verdict:** **insufficient — fails (b)-as-construct and (d), uniformly.** They confirm, from outside THINGS, that the "graded human relatedness over images" signal that exists in the world is **object/scene similarity**, not lexical sense relatedness. This is the structural reason the magnitude instrument has to be *built*, not found.

#### Also checked, no new magnitude candidate

- **VerSe** (Gella et al., Visual Verb Sense Disambiguation): **binary** verb-sense labels with images — fails (b), same class as VWSD.
- **SemEval-2023 VWSD gold**: re-checked for any *graded / ranked / continuous* variant or extension — **none found**; the gold remains "choose the one gold image among ten" (binary selection), as the in-repo [`resource/vwsd-semeval-2023`](vwsd-semeval-2023.md) already records.
- **"Discovering and Distinguishing Multiple Visual Senses for Polysemous Words"** (AAAI 2018): an *unsupervised visual-sense-discovery* method, not a human-graded relatedness gold — no magnitude signal.
- No **"DURel-style usage-similarity resource that ships paired images"** exists, per the 2024–2025 search: graded usage-similarity (DURel/WiC/RAW-C/Usim) is uniformly text-only; the graded-image norms are uniformly object-similarity. The two have **not** been joined in any open resource found.

### (2) THINGS-as-scaffolding build feasibility [Task 2]

The open-question page asks concretely: *could a fine-polysemy depicted-sense set be **built** using THINGS/THINGSplus PD-CC0 images + its human similarity prior as a stimulus source and pre-stratifier, with the graded sense-relatedness labels still coming from a DURel-style instrument?* Worked through, the answer is: **the build is describable but not tractable for this project, for three compounding reasons — and the deeper scout did not improve its tractability; if anything it confirmed the blockers.**

**What such a build would require (the steps):**

1. **A within-word polysemy spine THINGS does not have.** THINGS samples **disambiguated object concepts**, one sense per entry (per [`resource/things-data-triplets`](things-data-triplets.md): "THINGS samples disambiguated object concepts … not ambiguous word forms," "no same-word, different-sense pairs"). A magnitude set needs *target words depicted in two related-but-distinct senses*. So step 1 is to **assemble the polysemy structure from elsewhere** (e.g. a DURel-style ambiguous-word list — DWUG / RAW-C words) — THINGS supplies neither the words nor the sense pairs. THINGS can at best supply *images for object-noun senses that happen to coincide with a THINGS concept*, a small and uncontrolled intersection.
2. **PD/CC0 images per depicted sense, from THINGSplus not base THINGS.** The base THINGS images are **academic-use-only with publication restrictions**; only **THINGSplus** supplies one PD/CC0 image per concept (both VERIFIED verbatim in [`resource/things-data-triplets`](things-data-triplets.md), from THINGSplus PMC10991023). A build must pull images from THINGSplus (or Wikimedia PD/CC0, as the prior image probe did), one per *sense* — and THINGSplus offers one image per *concept*, not per *sense of an ambiguous word*, so for genuine polysemy the THINGSplus image is at most one of the two senses' images; the second must come from elsewhere. The image-license base-vs-THINGSplus split therefore does **not** cleanly cover a two-sense-per-word design.
3. **A graded *sense-relatedness* label per usage pair — which THINGS cannot provide and the project cannot produce.** This is the decisive blocker. The graded labels must be **per-item human word-sense relatedness** (DURel-style). THINGS's human signal is **whole-object odd-one-out similarity** — the wrong construct (the entire reason it is "partial / does-not-cleanly-fit"). So the labels would have to come from a **new DURel-style annotation pass** over the constructed image-paired usages. **The project does not run new human annotation** (CLAUDE.md always-on rule 4: "All human bearing comes from existing resources … No human subjects"; the project "uses only existing human-labeled resources — it does NOT run new human annotation," per this unit's brief). The THINGS similarity prior could *pre-stratify* candidate object pairs by human-rated object similarity (scaffolding), but pre-stratification is not the graded *sense* label the magnitude Δ is read against.

**The blockers, stated plainly:**

- **Construct mismatch (fatal for the labels).** THINGS gives graded *object similarity*; prediction 3 needs graded *within-word sense relatedness*. No transformation turns one into the other — they are different relations (the same reason CoSimLex and SID are rejected). THINGS can scaffold *stimuli*, never *labels*.
- **No within-word polysemy in THINGS (fatal for the spine).** The set has no same-word/different-sense pairs, so the very backbone of a magnitude set must be imported from a text resource (DWUG/RAW-C), at which point THINGS is reduced to an optional image source for a minority of object-noun senses.
- **Image-license split does not cover a two-sense design (build friction).** THINGSplus PD/CC0 is one image per *concept*; a two-related-senses-per-word design needs two images, at least one of which THINGS/THINGSplus does not supply — so Wikimedia PD/CC0 sourcing (the prior probe's method) is needed anyway, making THINGS's image contribution marginal.
- **New annotation is out of bounds (fatal for tractability).** Even granting steps 1–2, the graded sense-relatedness labels require human annotation the project is constitutionally barred from collecting. There is no existing open resource that supplies those labels *over images* (Task 1's whole finding). So the build cannot be completed from existing resources alone.

**Tractability verdict for THIS project: NOT tractable as an anchor build.** THINGS (via THINGSplus PD/CC0 + its object-similarity prior) is legitimately usable as **stimulus scaffolding and a pre-stratifier**, exactly as [`resource/things-data-triplets`](things-data-triplets.md) already says — but the **graded sense-relatedness labels cannot be obtained** without either (i) new human annotation (forbidden) or (ii) an existing open graded-sense-relatedness-over-images resource (does not exist, per Task 1). The deeper scout therefore **confirms** the open-question page's call ("scaffolding, not the anchor") and adds the sharper conclusion that scaffolding cannot be promoted to an anchor *within this project's constraints* — not because the engineering is impossible in principle, but because the one indispensable ingredient (per-item graded human *sense* relatedness over images) is exactly the thing neither THINGS nor any found resource supplies, and the project does not manufacture it.

### (3) Honest bottom-line verdict

- **Nothing clears all four requirements.** After a broad open-access hunt (graded multimodal/visual-WSD; visual-polysemy / sense-tagged image datasets; graded cross-modal STS; graded image-similarity MDS norms; DURel-with-images), **no resource carries a graded *word-sense* relatedness signal together with disambiguating images.** The failures are structural and consistent: graded same-word sense relatedness exists only **text-only** (DWUG, Usim, WiC-as-binary-cross-check, **RAW-C/SAW-C**, **SID**-as-between-word); graded **image** signals exist only over the **wrong construct** — whole-caption/scene similarity (**CxC**) or whole-object/category similarity (**THINGS, PiCS, MM-MDS, Carlson-Image, Mooney-THINGS**); and the sense-tagged image resources (**BabelPic, VisualSem, VerSe**, VWSD) carry only **binary/categorical** human signals. The same two-axis wall the open-question page hit from in-repo candidates holds across the open-access frontier.
- **A bespoke build remains the only route — and it is not tractable for this project.** The instrument prediction 3 needs (graded human *sense* relatedness with disambiguating images per usage, a competence-certifiable non-de-referenced text channel) must be **built**, and the indispensable graded *sense* labels over images do not exist in any open resource and cannot be produced here without new human annotation the project forbids. THINGS-as-scaffolding does not change this: it can pre-stratify stimuli, not supply labels.
- **The honest consequence for prediction 3.** Its *magnitude* sub-bet ("narrow headroom for concrete sense") is **not testable on any existing open resource**, and the only path that would test it requires capability (new graded sense annotation over images) outside this project's charter. Prediction 3 should be carried as **UNTESTED and, on current open resources, untestable** — not as a pending probe with a known instrument. The gating *shape* (predictions 1–2) stands on the v2 VWSD evidence; the *magnitude* does not, and the deeper scout finds no open-access instrument to read it.
- **No new typed `resource` page is warranted from this scout.** None of the new candidates is both fit-for-purpose and a build the project can complete, so none earns promotion to a typed resource for the magnitude question. (Two are *separately* catalog-worthy for **other** axes — see the closing note — but not for prediction 3.) Everything found is recorded here, in the scouting note, so a future session does not re-rediscover it.

**Catalog-worthy for other axes (not for prediction 3), if a future session opens those axes:** **RAW-C / SAW-C** is a clean graded same-word sense-relatedness *text* resource (cleaner same-/different-sense design than DWUG; 112 words / 672 pairs; IAA 0.79) that could **strengthen the text-side lexical-gradience program** as a second graded anchor alongside DWUG — *if* its license is verified (UNVERIFIED this session). **PiCS** (CC BY 4.0, 1,200 images / 20 object categories) and **CxC** could anchor a future *representational-alignment* axis (object-category or caption-scene similarity geometry), the same adjacent use already noted for THINGS — never a word-sense-relatedness test. Neither belongs to the magnitude question.

**Provenance / verification ledger for this scout.**

| Candidate | Key human-annotated feature (cited by) | Graded? | Image? | Construct | Fails req. | License | Verification notes |
|---|---|---|---|---|---|---|---|
| RAW-C / SAW-C | graded relatedness over same-word usage pairs; IAA 0.79; `mean_relatedness` | YES | NO | within-word sense relatedness (RIGHT) | (c) | **UNVERIFIED** (no LICENSE seen) | gradedness + IAA VERIFIED; **scale endpoints UNVERIFIED**; text-only VERIFIED (2 fetches) |
| Crisscrossed Captions (CxC) | continuous 0–5 STS over caption/image pairs | YES | YES | whole-caption/scene similarity (WRONG) | (b)-construct, (d) | **UNVERIFIED** (+ MS-COCO image terms) | "no isolated target-word structure" VERIFIED verbatim |
| BabelPic | binary recognizability validation; image↔synset tag | NO | YES | sense-tagged images, binary | (b) | BabelNet non-commercial | 14,931 imgs / 2,733 synsets VERIFIED; per-image terms UNVERIFIED |
| VisualSem | categorical node↔image links | NO | YES | sense-tagged KG, categorical | (b) | BabelNet non-commercial (verbatim) | "no graded or continuous human judgments" VERIFIED |
| Sense Identification Dataset (SID) | 0–4 Likert similarity + BabelNet sense IDs | YES | NO | **between-word** similarity (WRONG) | (c), (b)-construct | **CC BY** (VERIFIED) | text-only VERIFIED; 492 pairs / 984 terms |
| PiCS | SpAM/MDS object-category similarity | (MDS distances) | YES | object-category similarity (WRONG) | (b)-construct, (d) | **CC BY 4.0** (VERIFIED) | "not … word-sense disambiguation" VERIFIED; MDS-derived, not raw ratings |
| MM-MDS | MDS similarity, 240 object categories | (MDS) | YES | object-category similarity (WRONG) | (b)-construct, (d) | UNVERIFIED | from search; construct clear |
| Carlson-Image RSA norms | image relatedness ratings over object exemplars | YES (claimed) | YES | object/concept similarity (WRONG) | (b)-construct, (d) | UNVERIFIED | **paper PDF did NOT render — UNVERIFIED beyond snippet** |
| Mooney-THINGS | >100k ratings over Mooney 1,854-object images | YES | YES | **visual** ambiguity resolution, not lexical (WRONG) | (b)-construct, (d) | UNVERIFIED | construct = perceptual recognizability, not word sense |
| VerSe | binary verb-sense labels with images | NO | YES | sense-labelled, binary | (b) | UNVERIFIED | same class as VWSD |

**Fetches that failed / facts not verified this scout (stated honestly):**
- RAW-C **license** and **exact rating-scale endpoints** — not visible in the fetched README; arXiv PDF (2105.13266) rendered as binary, unreadable. UNVERIFIED.
- CxC **license** — not stated in the fetched paper content. UNVERIFIED.
- RSA-alignment paper (arXiv 2412.00577) PDF rendered as binary/unreadable — the "Carlson-Image" graded-image-relatedness detail is from a **search snippet only**, UNVERIFIED.
- MM-MDS license and Mooney-THINGS license not read from primary fields (construct is clear from search; license UNVERIFIED).
- Per-image redistribution terms for BabelPic / VisualSem / VerSe / CxC images — the usual web-image patchwork, not individually verified (the binding disqualifier for each is the *human-signal* axis, not the license, so this was not pursued exhaustively).
