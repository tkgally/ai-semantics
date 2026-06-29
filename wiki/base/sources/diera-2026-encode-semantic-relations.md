---
type: source
id: diera-2026-encode-semantic-relations
title: "Do Language Models Encode Semantic Relations? Probing and Sparse Feature Analysis"
authors:
  - Diera, Andor
  - Scherp, Ansgar
year: 2026
venue: "LREC 2026 (accepted; peer-review status as stated on arXiv). Preprint arXiv 2603.17624 (cs.CL); v1 2026-03-18, v2 2026-03-31"
arxiv: "2603.17624"
doi: 10.48550/arXiv.2603.17624
url: https://arxiv.org/abs/2603.17624
access: open-access
meaning-senses:
  - distributional
  - model-internal
status: received
created: 2026-06-29
updated: 2026-06-29
links:
  - rel: refines
    target: concept/distributional-meaning
  - rel: supports
    target: concept/polysemy
---

# Diera & Scherp 2026 — Do Language Models Encode Semantic Relations? Probing and Sparse Feature Analysis

## What it is

A two-author interpretability paper (arXiv 2603.17624; cs.CL; accepted at LREC 2026) that asks **where and how reliably four lexical-semantic relations live inside the internal representations of decoder-only language models** — synonymy, antonymy, hypernymy, hyponymy. It combines **linear probing** (classifiers trained on per-layer activation streams) with **mechanistic-interpretability** tools — **sparse autoencoders (SAE)** and **activation patching** — across three models of increasing scale (Pythia-70M, GPT-2, Llama 3.1 8B). Its headline is a **directional asymmetry within the hierarchical relations**: hypernymy is encoded redundantly and resists suppression, whereas hyponymy relies on compact features that ablation disrupts more easily.

This is a **representational / model-internal** study, the same genre as the in-repo mechanistic-interpretability sources ([`source/beckmann-queloz-2025-mechanistic-indicators`](beckmann-queloz-2025-mechanistic-indicators.md), [`source/milliere-buckner-2024-philosophical-intro-ii`](milliere-buckner-2024-philosophical-intro-ii.md) on the Othello-GPT world-model case). The project's own evidence is strictly **behavioral** and repeatedly disclaims representational/mechanistic reach; this page is therefore catalogued as a **map and interpretability-side counterpoint** to that method, **not** as a method the project uses, **not** as evidence about the project's behavioral findings, and **not** as a human anchor (see "What it cannot ground").

## Provenance

Title, full author list, version dates (v1 2026-03-18; v2 2026-03-31), subject category (cs.CL), and the abstract were fetched from the arXiv abs page (https://arxiv.org/abs/2603.17624) on 2026-06-29 and the abstract verified character-for-character. Body quotes (section structure, models, datasets, methods, the directional-asymmetry and difficulty-ordering sentences) were extracted from the arXiv HTML full text (https://arxiv.org/html/2603.17624v1) on the same date. **No published-proceedings page numbers** (the LREC 2026 camera-ready was not consulted), so locators below are **section names/numbers from the HTML**, not pages. The two load-bearing finding sentences (the §4.3.2 sufficiency/necessity sentence and the Conclusion reversal sentence) were re-fetched and confirmed. Where a sentence is reproduced from the abstract that also recurs in the body, it is flagged as abstract-sourced.

## Abstract (verbatim, from the arXiv abs page)

> "Understanding whether large language models (LLMs) capture structured meaning requires examining how they represent concept relationships. In this work, we study three models of increasing scale: Pythia-70M, GPT-2, and Llama 3.1 8B, focusing on four semantic relations: synonymy, antonymy, hypernymy, and hyponymy. We combine linear probing with mechanistic interpretability techniques, including sparse autoencoders (SAE) and activation patching, to identify where these relations are encoded and how specific features contribute to their representation. Our results reveal a directional asymmetry in hierarchical relations: hypernymy is encoded redundantly and resists suppression, while hyponymy relies on compact features that are more easily disrupted by ablation. More broadly, relation signals are diffuse but exhibit stable profiles: they peak in the mid-layers and are stronger in post-residual/MLP pathways than in attention. Difficulty is consistent across models (antonymy easiest, synonymy hardest). Probe-level causality is capacity-dependent: on Llama 3.1, SAE-guided patching reliably shifts these signals, whereas on smaller models the shifts are weak or unstable. Our results clarify where and how reliably semantic relations are represented inside LLMs, and provide a reproducible framework for relating sparse features to probe-level causal evidence."

## Section structure (from the HTML)

1. Introduction
2. Related Work (2.1 Concept-based Interpretability; 2.2 Mechanistic Interpretability; 2.3 Semantic Relationships in LLMs)
3. Procedure (3.1 Models; 3.2 Datasets; 3.3 Probing; 3.4 Activation Patching)
4. Results (4.1 Probing Results; 4.2 Relation-specific Analysis; 4.3 SAE Analysis, incl. 4.3.2 Activation Patching)
5. Conclusion
6. Ethical Considerations and Limitations

## The four relations and the three models

- **Relations.** Synonymy, antonymy, hypernymy, hyponymy (Abstract, verbatim). The dataset is built from WordNet 3.0 via NLTK: per §3.2 (Datasets), "From WordNet synsets, we randomly extracted 1,000 pairs for each semantic relation: hypernyms, hyponyms, synonyms, antonyms, along with 1,000 random word pairs that were verified to share no semantic relationship." (§3.2; the random-pair control gives a no-relation baseline.)
- **Models.** Three decoder-only transformers of increasing scale (§3.1): **Pythia-70M** ("a 6-layer open-weight model developed by EleutherAI to support mechanistic interpretability research"), **GPT-2** ("a 12-layer model with 124M parameters that has become a standard reference point in interpretability work"), and **Llama 3.1 8B** ("a 32-layer model from a recent family of open-weight LLMs"). All §3.1, verbatim fragments.

## Methods (locators from §3.3–§3.4)

- **Linear probing.** Per §3.3: "We probe the internal representations of each model to assess how well concept relationships are captured across layers. From every transformer block, we extract three activation streams: the attention output, the MLP output, and the post-residual stream." (So the unit of analysis is a per-layer, per-stream probe.)
- **Sparse autoencoders (SAE).** Per §3.4, features are ranked and selected against held-out data: "For each model/layer, we train the probe on the training split, rank features by the absolute coefficient magnitude, and choose k on a held-out validation set."
- **Activation patching.** Per §3.4: "To examine whether relation-specific SAE features causally affect a linear probe's decision over the post-residual stream, we use activation patching Meng et al. (2022), a targeted intervention technique that replaces or removes internal activations to test their effect on output logits."

## Key findings (verbatim; section locators from the HTML)

**The headline directional asymmetry (Abstract):**

> "Our results reveal a directional asymmetry in hierarchical relations: hypernymy is encoded redundantly and resists suppression, while hyponymy relies on compact features that are more easily disrupted by ablation."

**§4.3.2 (Activation Patching) — the sufficiency/necessity evidence behind that asymmetry:**

> "Hypernymy shows high sufficiency but low necessity (i.e., (ΔFR=0.69) vs DR=0.35 in Llama 3.1), suggesting diffuse or redundant coding. Hyponymy is more consistently high on both, indicating reliance on compact, targeted features."

**Conclusion — the reversal restatement:**

> "Hyponymy weakens under reversal, while hypernymy remains stable."

**Layer/stream localization (Abstract):**

> "More broadly, relation signals are diffuse but exhibit stable profiles: they peak in the mid-layers and are stronger in post-residual/MLP pathways than in attention."

**Difficulty ordering and scale (Abstract + §4.1):**

> "Difficulty is consistent across models (antonymy easiest, synonymy hardest)." (Abstract.)

> "The table highlights a clear scale effect and a consistent difficulty ordering across models, with antonymy easiest, followed by hyponymy, then hypernymy, and synonymy hardest. Accuracies rise from Pythia to GPT-2 to Llama 3.1 in both means and peak accuracies; antonymy approaches ceiling on Llama, while synonymy remains the hardest even at scale." (§4.1, Probing Results.)

**Capacity-dependence of causal effects (Abstract):**

> "Probe-level causality is capacity-dependent: on Llama 3.1, SAE-guided patching reliably shifts these signals, whereas on smaller models the shifts are weak or unstable."

## What this bears on in-repo

- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md) — `refines`.** The concept's live question is whether the structure a next-token-trained model tracks is "only its formal recurrence" or also encodes relational/inferential structure. This paper is a **representational probe of exactly that question**: it asks whether structured lexical-relational information (synonymy/antonymy/hypernymy/hyponymy) is *recoverable from and causally present in* the model's internal activations, beyond raw co-occurrence. It sharpens the concept by reporting *where* (mid-layers, post-residual/MLP over attention) and *how reliably* (capacity-dependent causal effects) such relational signal is found — and by flagging in its Conclusion that **"cosine similarity obscures relational distinctions"** (Conclusion; a caution that plain embedding-distance under-reads relation structure). It does this from the **interpretability side**; the concept page itself frames the project's behavioral wedge from the outside, so this is a counterpoint method, not a substitute for the project's own probes.
- **[`concept/polysemy`](../concepts/polysemy.md) and the lexical end of `theory/lexicon-grammar-continuum` — `supports`.** The relations probed (synonymy, antonymy, hypernymy, hyponymy) are the lexicographer's **sense-relation vocabulary** the polysemy page invokes ("hyponymy, meronymy, antonymy, troponymy"). This paper is evidence that those relation types are differentially represented and differentially recoverable inside models — relevant to the lexical wedge as a representational-side companion to the project's behavioral graded-sense work. The support is to the *lexical-relation framing*, not to any specific polysemy-gradience claim, which this paper does not test.
- **[`source/beckmann-queloz-2025-mechanistic-indicators`](beckmann-queloz-2025-mechanistic-indicators.md) and [`source/milliere-buckner-2024-philosophical-intro-ii`](milliere-buckner-2024-philosophical-intro-ii.md).** Same interpretability genre (SAE/activation-patching mechanistic analysis). This page joins them as **map/counterpoint sources from the representational side**: where Beckmann & Queloz argue a philosophical tiered framework over mechanisms and Millière & Buckner survey the mechanistic-interpretability program (Othello-GPT world models), Diera & Scherp supply a concrete, narrow, reproducible mechanistic measurement of lexical-relation encoding. All three are "the project's evidence is behavioral; these read the inside" entries.

## What it can ground

- A citation that, in three decoder-only models (Pythia-70M, GPT-2, Llama 3.1 8B), the four WordNet lexical relations are **differentially represented**, with a **directional asymmetry in the hierarchical pair**: hypernymy redundantly/diffusely coded and suppression-resistant, hyponymy carried by compact features more disruptable by ablation (verbatim Abstract + §4.3.2 + Conclusion).
- A citation for **where** relation signal concentrates (mid-layers; post-residual/MLP over attention) and a **difficulty ordering** (antonymy easiest → hyponymy → hypernymy → synonymy hardest), with a clear scale effect Pythia→GPT-2→Llama 3.1 (verbatim Abstract + §4.1).
- A citation that **probe-level causal effects are capacity-dependent** — robust SAE-guided patching only on Llama 3.1, weak/unstable on the smaller models (verbatim Abstract).
- A representational-side **counterpoint** to the project's behavioral method when an essay or theory page wants to mark the inside/outside distinction (cf. the framing of the Beckmann & Queloz source).

## What it cannot ground

- **Any behavioral or human-comparison claim about the project's findings.** This is a representational/interpretability study with **no human-judgment resource** (the labels are WordNet relation types, a lexical-database schema, not a fresh human-annotation instrument bearing on a project claim). It is **not a human anchor** and must not be cited as one. It speaks to model internals, not to the project's behavioral probes or their human anchors.
- **Transfer to the project's frontier panel.** The models here (Pythia-70M, GPT-2, Llama 3.1 8B) are small-to-mid open-weight models chosen for interpretability tractability, **not** the project's panel in [`config/models.md`](../../../config/models.md). No transfer of these representational results to the panel is established; cross-model generalization beyond the three tested is unverified (and the paper itself finds causal effects emerge only at the Llama-8B scale).
- **The project's add-vs-cancel monotonicity asymmetry.** **Do not conflate** this paper's *representational* hypernymy-vs-hyponymy directional asymmetry with the project's own *constructional, behavioral* ADD-vs-CANCEL monotonicity asymmetry (about adding vs cancelling a contributed inference). They are different phenomena at different levels: one is about which lexical direction is more redundantly encoded inside the weights; the other is about how a construction's contributed inference behaves under addition vs cancellation in observed output. At most there is a surface resonance — *both involve a directionality between two paired operations* — and that resonance is a **characterization only, explicitly not an identity and not a finding**. Any page that mentions both must keep them clearly separate.
- **A use as an `anchors:` resource.** As a model-behavior/representation study, not a standalone human-labeled asset, it cannot satisfy the human-anchor obligation for any claim/result.

## Known limits

- **Peer-review status as stated on arXiv:** accepted at LREC 2026 per the arXiv listing; the camera-ready proceedings version was not consulted, so all body locators are **section names/numbers from the HTML**, not published page numbers.
- **Three small/mid models only.** The causal (activation-patching) results are largely a Llama-3.1-8B phenomenon; on GPT-2 and Pythia-70M the interventions are "weak or unstable," so the strongest causal claims do not generalize down in scale, and nothing here speaks to frontier-scale models.
- **WordNet-schema relations, not graded human judgments.** Relations are WordNet 3.0 categories (discrete relation types), not a graded usage-similarity or acceptability instrument; the paper does not address sense gradience.
- **Metric caveat from the authors.** Their own Conclusion flags that "cosine similarity obscures relational distinctions" — a reminder that embedding-distance summaries under-read the structure their probes recover; cite the probe/patching evidence, not a cosine reduction.

## Status in wanted.md

Not previously listed by id. Catalogued 2026-06-29 as a representational/interpretability counterpoint source on the lexical-relation-encoding question (the inside-the-model companion to the project's behavioral lexical wedge). The orchestrating session should record it in `wanted.md`/[`index.md`](../../index.md) as RECEIVED.
