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

**What it is.** Winoground (Thrush, Jiang, Bartolo, Roberts, Bhatt, Bhatt, Singh, Cohan, Roth, Diab 2022, CVPR) is a 400-item benchmark for evaluating whether vision-and-language models can correctly match two images and two captions where the captions share identical words but differ only in word order (and therefore in meaning). Example: *"there is a mug in some grass"* vs. *"there is some grass in a mug"* — same words, opposite meanings. The dataset was hand-curated by expert annotators, who also applied rich fine-grained tags for error analysis. Images come from Getty Images.

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
