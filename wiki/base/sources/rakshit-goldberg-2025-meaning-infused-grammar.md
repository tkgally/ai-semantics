---
type: source
id: rakshit-goldberg-2025-meaning-infused-grammar
title: "Meaning-infused grammar: Gradient Acceptability Shapes the Geometric Representations of Constructions in LLMs"
authors:
  - Rakshit, Supantho
  - Goldberg, Adele E.
year: 2025
venue: "Second International Workshop on Construction Grammars and NLP @ IWCS 2025 (accepted; peer-review status as stated on arXiv). Preprint arXiv 2507.22286 (cs.CL; cs.AI); v1 2025-07-29, v2 2025-09-08"
arxiv: "2507.22286"
doi: 10.48550/arXiv.2507.22286
url: https://arxiv.org/abs/2507.22286
access: open-access
license: CC BY 4.0
meaning-senses:
  - constructional
  - distributional
  - model-internal
status: received
created: 2026-07-17
updated: 2026-07-17
links:
  - rel: refines
    target: concept/constructional-meaning
  - rel: supports
    target: concept/distributional-meaning
---

# Rakshit & Goldberg 2025 — Meaning-infused grammar: Gradient Acceptability Shapes the Geometric Representations of Constructions in LLMs

## What it is

A two-author **representational / model-internal** study (arXiv 2507.22286; cs.CL, cs.AI; accepted at the Second International Workshop on Construction Grammars and NLP at IWCS 2025) that asks whether the **internal activation geometry** of a language model reflects the **graded, function-infused** character that usage-based Construction Grammar attributes to constructions. It analyzes the English **Double Object (DO)** and **Prepositional Object (PO)** dative constructions in **Pythia-1.4B**, over 5,000 sentence pairs drawn from the **DAIS** dataset (Hawkins et al. 2020), each pair carrying a **human-rated preference strength** for DO or PO. Using two geometric separability measures (**energy distance** and **Jensen–Shannon divergence**) over the clouds of sentence representations, it finds that **separability between the two constructions is systematically modulated by gradient human preference strength**: more prototypical exemplars occupy more distinct regions of activation space, near-alternating exemplars less distinct — an ordering that holds at nearly every layer and replicates across the Pythia scale suite.

This is the **inside-the-model** genre — the same class as the in-repo interpretability sources [`source/diera-2026-encode-semantic-relations`](diera-2026-encode-semantic-relations.md), [`source/beckmann-queloz-2025-mechanistic-indicators`](beckmann-queloz-2025-mechanistic-indicators.md), and [`source/gurnee-2026-verbalizable-workspace`](gurnee-2026-verbalizable-workspace.md). The project's own dative evidence is strictly **behavioral** (stated production preference on the frontier panel — [`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md)) and repeatedly disclaims representational reach; this page is therefore catalogued as a **representational-side map and counterpoint** to that behavioral wedge — **not** a method the project uses, **not** evidence about the project's behavioral findings, and **not** a human anchor (see "What it cannot ground"). It is the **Diera-2026 pattern** applied to the constructional (grammatical) pole, where Diera & Scherp applied it to the lexical-relation pole.

## Provenance

Title, full author list (Supantho Rakshit, Adele Goldberg), subject categories (cs.CL, cs.AI), version dates (v1 2025-07-29; v2 2025-09-08), venue (IWCS 2025 CxG&NLP workshop), and license (**CC BY 4.0**) were fetched from the arXiv abs page (https://arxiv.org/abs/2507.22286) on 2026-07-17 and the abstract verified character-for-character. Body quotes and the bibliography entries below were extracted from the arXiv HTML full text (https://arxiv.org/html/2507.22286v2) on the same date via local extraction (regex over the `ltx_para`/`ltx_bibitem` blocks; MathML spans dropped, so numeric fragments embedded in math — e.g. "1.4B", PCA variance percentages — were read from the abstract or reconstructed and are flagged, never quoted from a math-stripped span). **No published-proceedings page numbers** (the IWCS 2025 camera-ready was not consulted), so locators below are **section names from the HTML**, not pages. Two in-paper typographical slips in the abstract ("have equally well have occured", "occured") are reproduced verbatim as the authors wrote them.

## Abstract (verbatim, from the arXiv abs page)

> "The usage-based constructionist (UCx) approach to language posits that language comprises a network of learned form-meaning pairings (constructions) whose use is largely determined by their meanings or functions, requiring them to be graded and probabilistic. This study investigates whether the internal representations in Large Language Models (LLMs) reflect the proposed function-infused gradience. We analyze representations of the English Double Object (DO) and Prepositional Object (PO) constructions in Pythia-1.4B, using a dataset of 5000 sentence pairs systematically varied by human-rated preference strength for DO or PO. Geometric analyses show that the separability between the two constructions' representations, as measured by energy distance or Jensen-Shannon divergence, is systematically modulated by gradient preference strength, which depends on lexical and functional properties of sentences. That is, more prototypical exemplars of each construction occupy more distinct regions in activation space, compared to sentences that could have equally well have occured in either construction. These results provide evidence that LLMs learn rich, meaning-infused, graded representations of constructions and offer support for geometric measures for representations in LLMs."

## Section structure (from the HTML)

1. Introduction
2. Methods
3. Results
4. Discussion
5. Conclusion and future directions

## The dataset (DAIS) and the model (Pythia-1.4B)

- **Dataset — DAIS (Hawkins et al. 2020).** Per §2 (Methods): "Stimuli sentences come from the DAIS (Dative Alternation and Information Structure) dataset, which includes English pairs of DO and PO sentences Hawkins et al. (2020)." And: "the DAIS dataset includes 5000 pairs of sentences, one in the DO and one in the PO, while systematically varying the length and definiteness each postverbal argument across pairs. Two hundred main verbs also vary across pairs, including verbs standardly treated as both 'alternating' and 'non-alternating' Levin (1993). Importantly, DAIS also includes human ratings of how strongly they prefer one construction over the other, for each combination of verb and arguments. Participants used a slider to indicate a preference for the DO (one end) or PO (other end) or neither (midpoint) Hawkins et al. (2020)." The full DAIS reference the paper cites is **Robert D. Hawkins, Ngan Nguyen, Adele E. Goldberg, Michael C. Frank & Noah D. Goodman. 2020. "Investigating representations of verb bias in neural language models." EMNLP 2020, pp. 4707–4718** (from the paper's reference list).
- **Preference binning.** Per §2: "We use these human preference ratings to partition sentences into five tiers based on the mean preference strength. We combined sentences from both ends of the scale to create 5 bins, ranging from: (1) the top of sentences with the strongest preference for one or the other construction, to (5) those sentences judged to be in the middle of the scale (equally non-biased toward either construction)." Both DO and PO sentences are binned symmetrically (strongly-biased → equi-biased).
- **Model.** Pythia-1.4B (Biderman et al. 2023). Per §2: "we extracted mean-pooled and normalized state representations for each sentence. We analyzed representations from all 24 layers, reducing them to principal components … We normalized the activations so that they all exist on a unit hypersphere." (PCA to a 150-dimensional space is used for the JSD analysis, per §2.)

## Methods — two geometric separability measures (§2)

- **Energy distance** (Rizzo & Székely 2016): used together with JSD "to measure the separability of entire clouds of representations, at different layers" of the model.
- **Jensen–Shannon divergence (JSD)** (Fuglede & Topsoe 2004): "A more sensitive measure of distributions is Jensen-Shannon Divergence (JSD), which measures the relationship between distributions in high-dimensional space." Estimated in the 150-dimensional PCA space by an anchor-vector Voronoi partition of the hypersphere (following Conklin 2025) yielding two discrete distributions whose JSD is then computed.
- The two measures are treated as **complementary, not interchangeable**: "because the two metrics are based on quite different calculations, so we do not attempt to compare them directly."

## Key findings (verbatim; section locators from the HTML)

**The core result — separability is modulated by graded human preference (§3, Results):**

> "the model assigns representations that are more distinct when the constructions are more clearly differentiated, when instances are more strongly biased toward the construction used. This is the case for both energy distance and JSD, as each shows a clear and consistent stratification by the tiers of preference strength (Figure 2 and 3). At nearly every layer, the Top 10 strongest preference tier exhibits the greatest geometric distance, followed in order by the other tiers, down to the ambiguous baseline."

**Robustness across the Pythia scale suite (§3):**

> "Results confirm that our central findings are robust across model scales. We consistently observe the geometric stratification by degree of bias so that preference strength remains a significant predictor of representational distance."

**Metric complementarity, not artifact (§3):** the two measures trace different layer-wise trajectories (energy distance convex/dipping mid-layers then rising; JSD rising sharply and staying high) yet agree on the bias-stratification, "which we take to indicate that the finding is robust and not an artifact of a single metric."

**Theory connection (§4, Discussion):**

> "LLMs develop representations whose geometric properties are highly consistent with the probabilistic, usage-based categories posited by the UCx approach."

> "This extends previous work that has focused on the model's ability to classify constructions categorically Huang (2025); Bonial and Tayyar Madabushi (2024) by showing more fine-grained, graded geometric structure, dependent on lexical and functional factors."

**Stated next step (§5, Conclusion and future directions):**

> "we are currently using these geometric insights to guide an investigation aimed at isolating the specific computational circuit(s) within the model that are responsible for encoding verb bias in the dative alternation, using tools like causal mediation analysis from Mechanistic Interpretability."

## What this bears on in-repo

- **[`concept/constructional-meaning`](../concepts/constructional-meaning.md) — `refines`.** That concept's "live tension" is exactly *where form ends and constructional meaning begins* — whether a model tracks a construction's graded, function-infused constraint structure or only its distributional surface. This paper is a **representational probe of that gradience**: it reports that the *internal geometry* of the DO/PO alternation is stratified by human preference strength (prototypical exemplars more separable, alternating ones less), i.e. the model's activation space encodes the construction's gradience rather than a flat categorical form. It sharpens the concept by adding an inside-the-model datum to the outside-the-model behavioral wedge — from the interpretability side, not as a method the project uses.
- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md) — `supports`.** The paper's framing question is whether "massive distributional learning can give rise to representations that reflect principles of the UCx approach"; its answer is that a next-token-trained model's geometry is "highly consistent with the probabilistic, usage-based categories" — a representational-side datum that distributional learning yields graded constructional structure, supporting (from inside the model) the concept page's live question about what distributional training encodes beyond formal recurrence.
- **[`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md) and the dative line — counterpoint, NOT support of the same proposition.** The project's dative finding is **behavioral** (frontier-panel stated *production preference* shifts in the human-attested givenness direction over a shortcut-immune within-item manipulation, anchored to the Bresnan et al. 2007 `languageR::dative` *production* corpus). Rakshit & Goldberg is **representational** (Pythia-1.4B internal *geometric separability* modulated by DAIS *acceptability/preference* strength). Both say "gradience infuses the dative construction," but at **different levels, on different models, against different human data** — do **not** conflate representational separability with behavioral production preference, and do **not** transfer this to the frontier panel (see "What it cannot ground"). Its value is as the *geometry-side companion* the flagship behavioral alternation battery lacked.
- **The shadow-depth line ([`theory/shadow-depth-table-v4`](../../findings/theory/shadow-depth-table-v4.md)) — map, NOT a new row.** The table's dative row is a *behavioral residual over a distributional control*. This paper reports representational gradience with **no shadow-stripping control** and on a non-panel model, so it contributes **no row** and no residual; it is a representational-side resonance with the table's "gradience is real" reading, held strictly separate from the measured beater rows.
- **[`source/diera-2026-encode-semantic-relations`](diera-2026-encode-semantic-relations.md), [`source/beckmann-queloz-2025-mechanistic-indicators`](beckmann-queloz-2025-mechanistic-indicators.md), [`source/gurnee-2026-verbalizable-workspace`](gurnee-2026-verbalizable-workspace.md).** Same "the project's evidence is behavioral; these read the inside" genre. This page joins them as a representational-side counterpoint — the *constructional/grammatical-pole* instance, where Diera & Scherp is the *lexical-relation-pole* instance.

## What it can ground

- A citation that, in **Pythia-1.4B** (and across the Pythia scale suite), the internal activation geometry of the English DO/PO dative alternation is **stratified by graded human preference strength** (DAIS): more prototypical exemplars occupy more separable regions, near-alternating exemplars less, on both energy distance and JSD, at nearly every layer (verbatim Abstract + §3).
- A citation that a next-token-trained decoder's **representations are consistent with usage-based Construction Grammar's graded, function-infused categories** — the representational-side statement of "meaning-infused grammar" (verbatim §4).
- A representational-side **counterpoint** to the project's behavioral dative/alternation findings when an essay or theory page wants to mark the inside/outside distinction (cf. the framing of the Diera 2026 and Beckmann & Queloz sources).
- A pointer to **DAIS (Hawkins et al. 2020)** as a *candidate* graded human DO/PO preference resource the dative line's acceptability/size leg currently lacks — flagged in [`wanted.md`](../wanted.md) as license-unverified, adopt only after a firsthand license check (the Cao `ProbeResponses` precedent).

## What it cannot ground

- **Any behavioral or human-comparison claim about the project's findings.** This is a representational/interpretability study. Its human data (DAIS preference ratings) grounds *the paper's own* geometry analysis on Pythia-1.4B; it is **not** adopted here as a project anchor, and the paper is **not a human anchor** for any project claim/result and must not be cited as one.
- **Transfer to the project's frontier panel.** The model is **Pythia-1.4B** (and smaller Pythia models), chosen for interpretability tractability — **not** the project's panel in [`config/models.md`](../../../config/models.md). No transfer of these representational results to `claude-sonnet-4.6` / `gpt-5.4-mini` / `gemini-3.5-flash` is established.
- **The project's behavioral dative givenness effect.** **Do not conflate** this paper's *representational geometric separability modulated by DO/PO acceptability preference* with the project's *behavioral production-preference shift in the givenness direction*. They are different phenomena at different levels (internal activation geometry vs. stated output preference), on different models, against different human datasets (DAIS graded acceptability vs. Bresnan et al. production corpus). At most there is a surface resonance — *both find the dative alternation's gradience is tracked* — and that resonance is a **characterization only, explicitly not an identity and not a finding**. Any page mentioning both must keep them clearly separate.
- **A use as an `anchors:` resource.** As a model-representation study (not a standalone human-labeled asset catalogued as a project `resource`), it cannot satisfy the human-anchor obligation for any claim/result. (DAIS *itself*, catalogued and license-cleared, could be a candidate — that is a separate future scout + decision, not this page.)

## Known limits

- **Peer-review status as stated on arXiv:** accepted at the IWCS 2025 CxG&NLP workshop per the arXiv listing; the workshop camera-ready was not consulted, so all body locators are **section names from the HTML**, not published page numbers. Three anonymous reviewers are acknowledged.
- **Pythia models only; single construction pair.** The strongest evidence is Pythia-1.4B with a scale-suite robustness check; only the DO/PO dative alternation is analyzed. Nothing here speaks to frontier-scale models or to other constructions directly.
- **Representational geometry, no behavioral or causal claim in the main result.** The core finding is a correlation between human preference strength and geometric separability; the paper is explicit that a causal (circuit-level) follow-up is *future work* ("we are currently using these geometric insights to guide an investigation …"), not established here.
- **DAIS is acceptability/preference, not production.** The human ratings are graded DO/PO *preference* judgments (slider), a different instrument from the project's Bresnan et al. *production* corpus anchor — a reason the two dative datapoints are complementary, not substitutable.

## Status in wanted.md

Listed there as a P2 want ("verified to exist firsthand s240", ingest as a representational/counterpoint source, not a human anchor). Catalogued **RECEIVED (2026-07-17, session 243)** as the constructional-pole representational counterpoint to the project's behavioral dative/alternation line, the Diera-2026 pattern applied to the grammatical pole. The DAIS dataset it uses is added to `wanted.md` as a license-unverified candidate graded-acceptability resource for the dative line.
