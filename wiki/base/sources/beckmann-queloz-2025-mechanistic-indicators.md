---
type: source
id: beckmann-queloz-2025-mechanistic-indicators
title: Mechanistic Indicators of Understanding in Large Language Models
authors:
  - Beckmann, Pierre
  - Queloz, Matthieu
year: 2025
venue: arXiv 2507.08017 (preprint, v1 2025-07-07; last revised v5 2026-02-25; no journal reference listed on arXiv at fetch time)
arxiv: "2507.08017"
url: https://arxiv.org/abs/2507.08017
access: open-access
meaning-senses:
  - functional-vs-formal
  - model-internal
  - inferential
status: received
created: 2026-06-14
updated: 2026-06-14
links:
  - rel: refines
    target: concept/deflationary-and-eliminativist-llm-meaning
  - rel: refines
    target: concept/formal-vs-functional-competence
---

# Beckmann & Queloz 2025 — Mechanistic Indicators of Understanding in Large Language Models

## What it is

Two-author philosophy-of-AI article (Pierre Beckmann; Matthieu Queloz, Bern), posted to arXiv as 2507.08017 (cs.CL; cs.AI), v1 2025-07-07, last revised v5 2026-02-25. Its project is to fuse **mechanistic interpretability** (MI) — the empirical program that probes the inner workings of LLMs — with a **philosophical theory of understanding**, and to use that fusion to argue that the deflationary "merely imitating linguistic patterns without genuine understanding" picture is "increasingly untenable" once MI findings are read through a theory of what understanding is. The paper proposes a **tiered framework** with three hierarchical varieties of understanding, each tied to a level of computational organization: **conceptual understanding** (a model forming "features" as directions in latent space), **state-of-the-world understanding** (learning contingent factual connections between features and tracking changes in the world), and **principled understanding** (ceasing to rely on memorized facts and discovering a compact "circuit" connecting them). Its closing methodological claim is the one most directly relevant to this project: MI plus theory lets us **transcend binary debates over whether AI understands**, replacing them with a "comparative, mechanistically grounded epistemology" of how AI understanding aligns with and diverges from our own — including the point that LLM internal organizations "diverge from human cognition in their parallel exploitation of heterogeneous mechanisms."

This is a **philosophical map and an interpretability-side counterpoint, not a human-annotated resource.** Its evidence base is *mechanistic* (interpretability of model internals); this project's own evidence base is *behavioral* (black-box probing). That boundary is load-bearing and is stated plainly under "What it cannot ground." Catalogued from [`wanted.md`](../wanted.md), where it was at P3, surfaced 2026-06-12 with only the title and arXiv id seen and the authors unknown.

Provenance and what was verified: title, both authors, abstract, subject categories, and submission/revision history were fetched from the arXiv abs page (https://arxiv.org/abs/2507.08017) on 2026-06-14; the abstract below is **verbatim** from that page and matched the cross-check text character-for-character (including the `--` em-dash renderings). The section structure was read from the arXiv-native HTML (https://arxiv.org/html/2507.08017v5) and cross-checked against the ar5iv LaTeXML rendering (https://ar5iv.labs.arxiv.org/html/2507.08017). **Both HTML renderings truncate before the end of the paper** (the readable text cuts off inside §4, "Principled Understanding"), so Sections 5 and 6 could not be read in full, and the two renderings even returned **conflicting titles for §5** ("A Motley Mix of Mechanisms" vs "Strange Minds: The Phenomenon of Parallel Mechanisms") — see "Known limits." Accordingly, the only passage verified as a long verbatim block is the **abstract** (plus three short, cross-fetch-confirmed §1 tier-label openings); the short body items below are tier-label openings and the section list that came back **identically across independent fetches**, and are flagged as such. Longer body sentences could not be certified verbatim through the available fetch route and are deliberately **not** quoted. Status: **received** (abstract verbatim-verified against the arXiv abs page 2026-06-14; body catalogued at abstract-plus-structure level only, with the §5/§6 limitation stated honestly).

## Abstract (verbatim, arXiv abs page)

> "Large language models (LLMs) are often portrayed as merely imitating linguistic patterns without genuine understanding. We argue that recent findings in mechanistic interpretability (MI), the emerging field probing the inner workings of LLMs, render this picture increasingly untenable--but only once those findings are integrated within a theoretical account of understanding. We propose a tiered framework for thinking about understanding in LLMs and use it to synthesize the most relevant findings to date. The framework distinguishes three hierarchical varieties of understanding, each tied to a corresponding level of computational organization: conceptual understanding emerges when a model forms \"features\" as directions in latent space, learning connections between diverse manifestations of a single entity or property; state-of-the-world understanding emerges when a model learns contingent factual connections between features and dynamically tracks changes in the world; principled understanding emerges when a model ceases to rely on memorized facts and discovers a compact \"circuit\" connecting these facts. Across these tiers, MI uncovers internal organizations that can underwrite understanding-like unification. However, these also diverge from human cognition in their parallel exploitation of heterogeneous mechanisms. Fusing philosophical theory with mechanistic evidence thus allows us to transcend binary debates over whether AI understands, paving the way for a comparative, mechanistically grounded epistemology that explores how AI understanding aligns with--and diverges from--our own."

(The abstract renders its dashes as `--`, as shown; the curly quotes around "features" and "circuit" are escaped here but appear as straight or typographic quotes on the abs page.)

## Section structure (verbatim headings, from the arXiv HTML / ar5iv renderings)

The two renderings agree on the headings through §4 and on the existence of a §5; they **disagree on the §5 title** (recorded honestly here):

1. Introduction
2. Conceptual Understanding — 2.1 The Emergence of Features; 2.2 The Linear Representation Hypothesis: Features as Directions; 2.3 Superposition: Accommodating a World of Features; 2.4 The Transformer Architecture: Deepening Conceptual Understanding
3. State-of-the-World Understanding — 3.1 Learning Factual Connections; 3.2 Internal Models of External States: The Othello-GPT Findings
4. Principled Understanding — 4.1 A Simple Circuit: The Induction Head; 4.2 A Deeper Principle: The Fourier Algorithm for Modular Addition; 4.3 Circuits in the Wild; 4.4 Crystallized vs. Fluid Understanding of Principles
5. **[title unverified]** — returned as "A Motley Mix of Mechanisms" by one rendering and "Strange Minds: The Phenomenon of Parallel Mechanisms" by another; the two could not be reconciled because both renderings truncate before this section's body
6. Conclusion (present in the arXiv HTML listing; not reachable as readable text in either rendering)

## Key passages (verbatim where certifiable; see the caveat)

The abstract above is the **only long verbatim block** this catalogue certifies. The items below are **short** tier-label openings from §1's framework list that came back identically across independent fetches; they are quoted conservatively, and the surrounding sentences (which the fetch route truncated at ~125 characters) are paraphrased in "What it is" rather than quoted, to avoid over-quoting unverified text.

**§1 Introduction — the three tiers, as named and opened in the framework list:**

> "Conceptual Understanding: This foundational form involves the model developing internal representations (\"features\") that are functionally analogous to human concepts."

> "State-of-the-World Understanding: Building upon conceptual understanding, this involves forming an internal representation of the state of the world by grasping contingent empirical connections between features."

> "Principled Understanding: At the apex of this hierarchy lies the ability to grasp the underlying principles or rules that unify a diverse array of facts."

(The "transcend binary debates … comparative, mechanistically grounded epistemology" stance and the "parallel exploitation of heterogeneous mechanisms" divergence claim are both stated **in the abstract, verbatim above**; the corresponding §5/§6 *body* sentences could not be reached through the truncated renderings and are therefore not quoted from the body. Do not cite a §5 or §6 sentence from this page — only the abstract carries these two claims in verified form here.)

## Bearing on this project

- **[`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md) — the principal connection, and it cuts two ways.** The paper's explicit target is the deflationary/eliminativist "merely imitating linguistic patterns without genuine understanding" reading, and it argues MI findings make that picture "increasingly untenable" — so it is a published *push against strict eliminativism*, from the mechanistic side, complementing the project's own behavioral findings that strain the slogan-parrot reading (that concept page's §2 second list). The link is `refines` (it sharpens that map), but the agreement is only partial, and the divergence is worth stating: the project's stance on that page is **descriptivist — "describe, don't litigate"** — and Beckmann & Queloz, while they likewise reject the binary, go further than the project does: they argue that MI evidence *underwrites understanding-like unification*, a (modestly) positive verdict, where the project stops at describing structure. The honest relation is therefore: **strong agreement on transcending the yes/no binary; partial divergence on whether the evidence licenses a positive "understanding" attribution.** Crucially, their warrant is mechanistic (internal features, circuits), and the project's deflationary-page argument turns on a *behavioral* in-principle gap (Bender & Koller: form-only training cannot fix meaning, and behavioral evidence cannot refute that). Their MI evidence does not, on this project's own terms, *close* that gap — it changes the *kind* of evidence in play. So this page is an **interpretability-side ally** for the anti-binary stance, not a behavioral anchor that settles the existence question.
- **[`concept/formal-vs-functional-competence`](../concepts/formal-vs-functional-competence.md).** The tiered framework is, in effect, a *graded* refinement on the functional side of the Mahowald et al. formal/functional line: conceptual → state-of-the-world → principled understanding is a hierarchy of increasingly world- and reasoning-involving organization, exactly the territory "functional competence" names. Where Mahowald et al. draw a behavioral/neural dissociation, Beckmann & Queloz offer a *mechanistic* story for how the functional varieties could be realized internally (features, factual connections, compact circuits). The project can cite this as a published, mechanistically grounded gradation of "functional competence," with the standing caveat that the gradation is a philosophical framing over interpretability case studies, not a measured dissociation.
- **[`source/milliere-buckner-2024-philosophical-intro-i`](milliere-buckner-2024-philosophical-intro-i.md) and Part II (arXiv 2405.03207).** This is another survey-style philosophical map of the LLM-understanding question, and it slots beside the Millière & Buckner two-parter — but with a sharper editorial line. Where Part I argues most disputes are *empirically underdetermined* and Part II turns to mechanistic methods with a "broadly negative (with qualifications)" verdict, Beckmann & Queloz take the *same* mechanistic-interpretability evidence base (including the Othello-GPT world-model case the Millière–Buckner survey also features) and read it more affirmatively, toward "understanding-like unification." Read together, the three give the project a spread of in-repo philosophical verdicts over a shared MI evidence base — useful precisely as a *range of framings*, not a settled result.
- **The "parallel exploitation of heterogeneous mechanisms" point (abstract).** The claim that LLM internal organization diverges from human cognition by running many heterogeneous mechanisms in parallel is a mechanistic-side statement of *human-divergence* that resonates with the project's recurring finding that model behavior can match a human signal while not being human-like in its underlying route (e.g. convergence-without-human-like-compression on the relational axis). It is a *hypothesis about internals*, stated in the abstract; the project cannot adopt it as its own claim (it has no mechanistic access), but it can cite it as the published interpretability-side articulation of why "matches the human signal" need not mean "by the human mechanism."

## What it can ground

- Citations for the **tiered framework** itself — conceptual / state-of-the-world / principled understanding as three varieties tied to levels of computational organization — as a published philosophical proposal (Beckmann & Queloz 2025), not as an empirical result this project has reproduced.
- The framing that one can **transcend the binary "does AI understand?" debate** in favor of a comparative, mechanistically grounded epistemology — a published statement of a stance closely allied to this project's "describe, don't litigate," and a useful citation when the project explains why it refuses the yes/no.
- The interpretability-side observation that LLM internal organization may **diverge from human cognition through parallel/heterogeneous mechanisms** — as the authors' framing of the human-divergence question, to be cited as their claim about internals.

## What it cannot ground

- **Any mechanistic claim as this project's own.** The project's evidence is *behavioral* black-box probing; this paper's is *mechanistic interpretability*. The project cannot adopt "the model has a feature for X," "a circuit implements Y," or "principled understanding is present" as anchored findings — these belong to the MI primary literature the paper synthesizes (e.g. the Othello-GPT and modular-addition case studies), each of which would need its own source page before any finding leaned on it. This is the boundary that makes the page a *map and counterpoint*, not a resource.
- **A settled verdict that LLMs understand.** The paper argues the deflationary picture is "increasingly untenable" and that MI uncovers "understanding-like unification," but it explicitly reframes the question as comparative rather than resolving a yes/no; its positive language is hedged with the human-divergence point. Do not cite it as establishing that LLMs understand in the full human sense.
- **Any human-anchor for an empirical claim.** It is not a human-labeled resource (no treebank, sense inventory, acceptability norm, or annotation): it cannot serve as the `anchors:` resource for a claim or result. Its role is philosophical framing and interpretability-side context.
- **Anything about lexical gradience or Construction Grammar specifically.** The framework is general (features, factual connections, circuits); it does not treat graded word sense, constructional form–meaning pairing, or acceptability methodology, which are the project's own probe-level questions.

## Known limits

- **Renderings truncate; §5 and §6 are not certifiable.** Both the arXiv-native HTML and the ar5iv LaTeXML rendering cut off inside §4 in the available fetch route, so the body of §5 (the heterogeneous-mechanisms discussion) and §6 (Conclusion) could not be read or quoted verbatim. The two renderings additionally returned **conflicting titles for §5**, which this page records rather than resolves. The two headline claims that live in those sections — "transcend binary debates" and "parallel exploitation of heterogeneous mechanisms" — are quoted here **only from the abstract**, where they appear verbatim; their body statements are not quoted.
- **Fetch-route quoting limit.** The summarizing fetch truncated long sentences (~125 characters) and was inconsistent across calls on whether a given body sentence was present, so longer §1 sentences (including the "understanding as apprehending relational structure" framing one fetch returned and another could not confirm) are **not** quoted; only short, repeatedly-confirmed tier-label openings are. Treat the body coverage here as *abstract-plus-structure*, the way this repo treats PDF-only and partially-reachable sources.
- **Preprint, multiply revised.** v1 2025-07-07, last revised v5 2026-02-25; no journal reference on arXiv at fetch. The version read for structure was v5; the abstract was read from the abs page (which reflects the latest version). Cite as "preprint, v5."
- **Philosophical synthesis over secondary evidence.** Every mechanistic finding it reports (features-as-directions, superposition, induction heads, the Fourier modular-addition algorithm, Othello-GPT) is the property of the cited MI primary work; this paper is a *framing of* that evidence, and its tiered reading is the authors' proposal, not a consensus taxonomy.

## Status in wanted.md

Listed in [`wanted.md`](../wanted.md) at P3 ("candidate bridge between interpretability evidence and the understanding/meaning question," surfaced 2026-06-12 with only the arXiv id and title seen and authors unknown). Catalogued 2026-06-14 with authors now verified (Pierre Beckmann; Matthieu Queloz); the wanted.md entry should be flipped to `RECEIVED` in the same wave (replacement status line proposed to the orchestrator).
