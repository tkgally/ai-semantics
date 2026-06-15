---
type: source
id: zeng-2026-lvlms-ground-differently
title: LVLMs and Humans Ground Differently in Referential Communication
authors:
  - Zeng, Peter
  - Li, Weiling
  - Paige, Amie
  - Wang, Zhengxiang
  - Kaliosis, Panagiotis
  - Samaras, Dimitris
  - Zelinsky, Gregory
  - Brennan, Susan
  - Rambow, Owen
year: 2026
venue: "arXiv 2601.19792 (cs.CL; cs.AI; cs.HC); v1 2026-01-27, v3 2026-04-20"
arxiv: "2601.19792"
doi: 10.48550/arXiv.2601.19792
url: https://arxiv.org/abs/2601.19792
access: open-access
meaning-senses:
  - relational
  - distributional
  - grounded
  - human-comparison
status: received
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: refines
    target: concept/relational-meaning
  - rel: supports
    target: result/relational-reference-game-v1
---

# Zeng et al. 2026 — LVLMs and Humans Ground Differently in Referential Communication

## What it is

Nine-author empirical paper (arXiv 2601.19792; cs.CL/cs.AI/cs.HC), one of whose authors is **Susan Brennan** — co-author of the canonical conceptual-pacts study the project already catalogues ([`source/brennan-clark-1996-conceptual-pacts`](brennan-clark-1996-conceptual-pacts.md)). It runs a **referential-communication experiment with a 2×2 factorial of director–matcher pairs** — human-human (HH), human-AI (HA), AI-human (AH), and AI-AI (AA) — over **repeated rounds** of matching hard-to-name objects (baskets "not associated with any obvious lexicalized labels"), and asks whether large vision-language models (LVLMs) can interactively *generate and resolve* referring expressions the way humans do. The headline is negative: LVLMs do not build common ground interactively — they do not entrain on compact, reusable referring expressions (conceptual pacts), AI directors are strikingly verbose, and accuracy fails to improve (and in some conditions declines) across rounds.

This is the **closest in-design neighbor yet** to the project's own relational pilot ([`result/relational-reference-game-v1`](../../findings/results/relational-reference-game-v1.md)): an iterated dyadic reference game over non-lexicalized figures, evaluated for accuracy, efficiency, and lexical overlap, with an explicit conceptual-pacts/entrainment lens. Its **distinctive contribution over the two model-only dyad papers already in-repo** ([`source/imai-2025-vlm-common-ground`](imai-2025-vlm-common-ground.md), [`source/ashery-2025-llm-conventions`](ashery-2025-llm-conventions.md)) is the **mixed human-AI and AI-human conditions plus a human-human baseline collected in the same paradigm** — so the human convergence curve and the LLM failure are measured on the same task rather than borrowed from a separate corpus.

## Provenance

Title, full author list, submission dates (v1 2026-01-27; last revised v3 2026-04-20), subject categories, and the abstract were fetched from the arXiv abs page (https://arxiv.org/abs/2601.19792) on 2026-06-15. Body quotes and design details (section structure, task, conditions, models, metrics, results sentences) were extracted from the arXiv HTML full text (https://arxiv.org/html/2601.19792 / v3) on the same date; the load-bearing finding sentences were re-fetched and verified character-for-character against the HTML. **No journal/conference venue and no page numbers** were available, so locators below are **section names/numbers from the HTML**, not pages. Where I report a figure or section-level summary not anchored to a verbatim sentence, it is flagged as such below.

## Abstract (verbatim, from the arXiv abs page)

> "For generative AI agents to partner effectively with human users, the ability to accurately predict human intent is critical. But this ability to collaborate remains limited by a critical deficit: an inability to model common ground. We present a referential communication experiment with a factorial design involving director-matcher pairs (human-human, human-AI, AI-human, and AI-AI) that interact with multiple turns in repeated rounds to match pictures of objects not associated with any obvious lexicalized labels. We show that LVLMs cannot interactively generate and resolve referring expressions in a way that enables smooth communication, a crucial skill that underlies human language use. We release our corpus of 356 dialogues (89 pairs over 4 rounds each) along with the online pipeline for data collection and the tools for analyzing accuracy, efficiency, and lexical overlap."

## Section structure (from the HTML)

1. Introduction
2. Cognitive Science Background
3. Related Work in Human-AI Interaction
4. Experimental Design and Method (4.1 Task Description; 4.2 Human Participants; 4.3 AI Participants; 4.4 Resulting Corpus; 4.5 Evaluation Metrics)
5. Results
6. Follow-Up AI–AI Experiments
7. Conclusion

## Design (section-level summary; not all clauses are verbatim — see flag)

- **Task.** Director–matcher pairs identify/order baskets across 4 rounds via multi-turn text dialogue; the matcher chooses among the target set plus additional distractor baskets. The objects are "objects not associated with any obvious lexicalized labels" (Abstract, verbatim) — the analogue of tangram/abstract-figure referents.
- **Conditions.** A 2×2 factorial of director × matcher agent type: HH, HA, AH, AA.
- **Corpus.** 356 dialogues, 89 pairs over 4 rounds each (Abstract, verbatim). *Per-condition pair counts (≈32 HH / 22 HA / 17 AH / 18 AA) are reported at section level from the extraction and are NOT individually quoted verbatim — flagged.*
- **Models.** Primary AI participant is **GPT-5.2**; the follow-up AI–AI experiments (§6) also use **Gemini-3-Pro** and **Claude Opus-4.5**. *Model identities are from the extraction; the GPT-5.2 identity is corroborated by the verbatim Conclusion sentence below; Gemini/Claude as §6 follow-up models are section-level, not individually quoted — flagged.*
- **Metrics.** Accuracy, efficiency (words/turns), and lexical overlap (Abstract, verbatim "analyzing accuracy, efficiency, and lexical overlap").

## Key findings (verbatim; section locators from the HTML)

**Abstract — the central negative claim:**

> "We show that LVLMs cannot interactively generate and resolve referring expressions in a way that enables smooth communication, a crucial skill that underlies human language use."

**§7 Conclusion — the frontier-model verdict (names GPT-5.2):**

> "Even a frontier LVLM, GPT-5.2, showed no hint of any ability to build common ground."

**§7 Conclusion — the human contrast (conceptual pacts / entrainment):**

> "These trends are consistent with the ability of human-human pairs to rapidly establish common ground and entrain on compact, reusable referring expressions that reflect conceptual pacts."

**§7 Conclusion — AI directors verbose despite poor accuracy:**

> "Despite poor accuracy, pairs with AI directors were remarkably verbose, producing many more words than did pairs with human directors."

**§5 Results — human partners rated higher than AI partners on collaboration:**

> "Consistent with the performance gap, human partners were rated significantly higher than AI partners across all dimensions related to collaboration (all ps < .001)."

*Additional results reported at section level in the extraction but NOT individually verified character-for-character (so paraphrased, flagged): AI-AI accuracy decreased significantly across rounds while effort stayed flat (§7); in the AI-Human condition accuracy "declined precipitously" relative to other conditions (§5); AI-AI lexical overlap stayed high (≥60%) but did not vary across rounds (§5). Treat these as section-level summaries, not as verbatim quotes.*

## Methodology: discriminative AND generative

Both axes are exercised, which is what makes the paper an unusually complete relational probe:

- **Generative.** Directors (human or LVLM) *produce* referring expressions in free multi-turn text; the paper measures their length/verbosity and lexical reuse across rounds. The negative finding is about generation under interactive pressure — the model cannot coin and then compress a reusable label.
- **Discriminative.** Matchers (human or LVLM) *select/order* the target basket from a candidate set including distractors; accuracy is the matching score. Human matchers additionally repaired misunderstandings interactively (clarification turns).

So unlike a one-shot caption-matching benchmark, the discriminative and generative roles are *coupled across turns and rounds* — the same property the project's relational pilot relies on, and the property that lets the paper speak to entrainment rather than only to one-shot reference.

## What this bears on in-repo

- **[`concept/relational-meaning`](../concepts/relational-meaning.md) — `refines`.** The paper is a direct, on-paradigm instance of the concept's iterated-dyadic-reference setting, and it sharpens the concept's central caution: it finds coordination *failure* (not just absence of constitution), with a human baseline collected in the same task. Crucially, it operationalizes entrainment via **lexical overlap and verbosity over rounds** — exactly the *reuse/compression* family of measures the concept page flags as **order-insensitive by design** and therefore explicable by the deflationary distributional story. The paper does **not** run an order-scramble / shuffled-history control, so like Imai et al. and Ashery et al. it tests *whether* (and how well) models entrain, not *whether convention is constituted in the ordered trajectory* — the live-vs-shuffled discriminator remains the project's own wedge ([`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md)).
- **[`result/relational-reference-game-v1`](../../findings/results/relational-reference-game-v1.md) — `supports`.** The project's pilot reported "convergence WITHOUT human-like compression" for homogeneous LLM dyads (flat ~8.5–10.8-word REs vs the human compression curve). This paper finds the **same non-compression / verbosity pattern** for AI directors, plus the stronger AI-AI result that accuracy itself *fails to improve or declines* across rounds — and it adds the mixed-agent conditions the pilot deferred. The support is qualitative and cross-design (image-grid LLM games under a word budget vs this paper's basket task; different models and channel), so it corroborates the *pattern* (LLM dyads coordinate-or-fail without human-like conceptual-pact compression) rather than any specific number. Note the pilot's panel (claude-sonnet-4.6, gpt-5.4-mini, gemini-3.5-flash) and this paper's panel (GPT-5.2, Gemini-3-Pro, Claude Opus-4.5) are different models.
- **[`source/brennan-clark-1996-conceptual-pacts`](brennan-clark-1996-conceptual-pacts.md).** Susan Brennan is a co-author here; the paper's "conceptual pacts" framing is the same construct her 1996 paper established (historical, partner-specific lexical entrainment). This is a 2026 LLM-era application of that exact construct, with a co-author through-line — useful provenance for the conceptual-pacts measure.
- **[`source/imai-2025-vlm-common-ground`](imai-2025-vlm-common-ground.md) and [`source/ashery-2025-llm-conventions`](ashery-2025-llm-conventions.md).** This page is the third in-repo relational-axis empirical neighbor. Its advance over both: a **human-human baseline and mixed human-AI / AI-human conditions in one paradigm** (Imai is model-only self-play vs a separate human corpus; Ashery is population-scale model-only convention emergence). The three agree on the core empirical pattern — current models reach (or fail at) referential coordination without human-like conceptual-pact compression — from three different designs.
- **[`source/imai-2025-vlm-common-ground`](imai-2025-vlm-common-ground.md) note on "grounding".** As with Imai, "ground/grounding" here is **Clark-style conversational grounding** (building common ground in dialogue), *not* symbol grounding in the Harnad sense — do not conflate with [`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md) or [`concept/grounding`](../concepts/grounding.md). The `grounded` meaning-sense tag here points at the social/joint-action sub-sense closest to `relational`, not at perceptual grounding.

## What it can ground

- A citation that, in an iterated referential-communication game with a **human baseline collected in the same paradigm**, current LVLMs (including frontier GPT-5.2) **fail to build common ground interactively** and **do not entrain on compact reusable referring expressions / conceptual pacts** (verbatim Abstract + §7 quotes).
- A citation for **AI-director verbosity** despite poor accuracy (verbatim §7), corroborating the project pilot's non-compression finding from an independent design.
- A citation that, in the same paradigm, **human partners are rated significantly higher than AI partners on collaboration dimensions** (verbatim §5) — a human-perception contrast not present in the model-only dyad papers.
- Calibration for what **human conceptual-pact entrainment** looks like in this paradigm (the HH baseline), complementing [`resource/hawkins-tangrams`](../resources/hawkins-tangrams.md) and [`source/brennan-clark-1996-conceptual-pacts`](brennan-clark-1996-conceptual-pacts.md).

## What it cannot ground

- **Any meaning-constitution / trajectory-dependence claim.** The metrics (accuracy, verbosity, lexical overlap over rounds) are **reuse/efficiency measures, order-insensitive in design**; there is no live-vs-shuffled / order-scramble control. So the deflationary distributional reading of entrainment that the project insists any relational *positive* must beat is untouched by this paper. It sharpens *how* models fail to ground; it does not address whether convention is *constituted between* agents.
- **Claims about the project's own panel models.** The models tested (GPT-5.2, Gemini-3-Pro, Claude Opus-4.5) are not the panel in [`config/models.md`](../../../config/models.md); cross-model transfer of the result to the panel is plausible-by-pattern, not established.
- **Use as an `anchors:` resource for a claim/result.** It is an experiment paper (model behavior measured against human dyads), not a standalone human-labeled resource like a treebank or sense inventory. Its **human-human dialogues** are a released corpus and could in principle ground a future relational result — but only after that corpus is itself fetched and catalogued as a `resource` page; this `source` page does not stand in for that.
- **Strong claims beyond the basket/object referent type.** Referents are non-lexicalized physical objects in a text-channel matching game; effects may differ for other referent modalities or richer multimodal channels.

## Known limits

- **Preprint, not peer-reviewed at retrieval** (2026-06-15); no stated journal/conference venue. Standing is "arXiv preprint."
- **No page-level locators.** All quote locators are section names/numbers from the HTML; the abstract is from the abs page. Per-condition pair counts, the AI-AI accuracy-decline and AI-Human "declined precipitously" results, and the Gemini/Claude follow-up identities are **section-level summaries from the extraction, not character-verified verbatim** — flagged inline above.
- **Reasoning-mode detail.** The extraction noted GPT-5.2 was run with a "none" reasoning option; this is a configuration detail not character-verified here and should be checked against §4.3 before being cited.
- **Reuse/efficiency metrics only.** As above, the paper's strength (a same-paradigm human baseline and mixed conditions) does not extend to the constitution question; cite it for *coordination/grounding quality*, not for relational meaning-constitution.

## Status in wanted.md

Not previously listed by id. Flagged in [`NEXT.md`](../../../NEXT.md) as a confirmed-fetchable relational/referential-grounding source; catalogued 2026-06-15 as the third in-repo relational-axis empirical neighbor (the first with a same-paradigm human-human baseline and mixed human-AI conditions). The orchestrating session should record it in `wanted.md`/[`index.md`](../../index.md) as RECEIVED.
