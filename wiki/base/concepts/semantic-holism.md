---
type: concept
id: semantic-holism
title: Semantic holism, molecularism, and atomism
meaning-senses:
  - inferential
  - distributional
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: result/cross-axis-lexical-constructional-ordering-v1
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/quine-1951-two-dogmas
  - rel: depends-on
    target: source/davidson-1967-truth-and-meaning
---

# Semantic holism, molecularism, and atomism

How *much* of a language do you need to fix the meaning of one expression in it? The answers fall on an axis. At one end, **atomism**: an expression's meaning is independent of every other — you could in principle know what `dog` means while knowing nothing else. At the other, **holism**: the meaning of any expression is fixed by its place in the whole web of the language (or the whole theory, or the whole web of belief), so that nothing has a meaning *except* against everything else. **Molecularism** sits between: meaning is fixed by a privileged, bounded *subset* of an expression's connections — enough to be more than atomism, little enough to avoid holism's vertigo.

This axis matters to the project for one sharp reason. The strongest pro-LLM-meaning position in the repo — conceptual-role / inferential semantics ([`concept/inferential-meaning`](inferential-meaning.md)) — is **holist by its own statement**, and distributional models ([`concept/distributional-meaning`](distributional-meaning.md)) are **holist by construction**. So the classical objection to holism is, transposed, an objection to the cleanest case for LLM meaning. This page owns that axis and that objection. It does **not** develop the threat-to-compositionality argument — that is its own sibling, [`compositionality.md`](compositionality.md) — nor the truth-conditional/use, frame/prototype, or deflationary framings, each with their own sibling. It hands those off and develops the holism question itself.

## The spectrum (characterization)

The three positions are best drawn through their canonical (and almost entirely **not-in-repo**) statements, characterized rather than quoted:

- **Atomism.** Fodor's later view (e.g. Fodor & Lepore, *Holism: A Shopper's Guide*, 1992; not in-repo; characterization) is the limit case: the meaning of a primitive term is its (informational/nomic) relation to what it is about, fixed one term at a time, with inferential connections *not* constitutive of content. Atomism's payoff is exactly what holism struggles to deliver — two people, or two systems, can share a concept without sharing anything else — but it buys that by severing meaning from inferential role, which is the move inferentialism refuses.

- **Molecularism.** Dummett ("What is a Theory of Meaning?", 1975/76; not in-repo; characterization) is the usual reference point: a theory of meaning should be *molecular*, assigning each expression a content graspable from a bounded body of knowledge, so that meaning is learnable piecemeal and a speaker can fully understand some sentences without understanding the whole language. Molecularism is the position that *wants* the benefits of inferential-role meaning without paying holism's price; the open problem it inherits is principled — which inferences are the meaning-constitutive subset, and which are merely collateral belief.

- **Holism.** Quine's confirmation holism ("Two Dogmas of Empiricism", 1951; **now in-repo** at primary strength, [`source/quine-1951-two-dogmas`](../sources/quine-1951-two-dogmas.md); *Word and Object*, 1960, remains not in-repo) is the headwater: "our statements about the external world face the tribunal of sense experience not individually but only as a corporate body" (§V–§VI), so "The unit of empirical significance is the whole of science" (§VI) — there is no fact of the matter about the meaning of one sentence in isolation, and the analytic/synthetic distinction — the line between what a word *means* and what we merely *believe* using it — cannot be cleanly drawn, because "synonymy" is "no less in need of clarification than analyticity itself" (§I) and the attempt to define one through the other closes a circle: "So we are back at the problem of analyticity" (§IV). Davidson carries this into the theory of meaning: already in "Truth and Meaning" (1967; **now in-repo**, [`source/davidson-1967-truth-and-meaning`](../sources/davidson-1967-truth-and-meaning.md)) he holds that "only in the context of the language does a sentence (and therefore a word) have meaning" (p. 308) — the meanings of sentences are fixed together, by their place in the whole truth-theory for the language; the fuller radical-interpretation development (belief and meaning fixed together by interpreting a whole pattern of assent, *Inquiries into Truth and Interpretation*, 1984) remains not in-repo; characterization. On both, meaning lives in the web, not the node.

Conceptual-role / inferential semantics tends **holist** by its own logic: if what a term means is the inferences it licenses to and from *other* terms ([`concept/inferential-meaning`](inferential-meaning.md)), then its content is its position in the inferential web, and a different web is a different position. Brandom's inferentialism (1994/2000; in [`base/wanted.md`](../wanted.md), not in-repo) is the systematic version cited there; whether it must be *fully* holist or admits a molecularist discipline is itself contested, and is the seam molecularism tries to hold open.

## The holism objection

The classical objection — sharpest in Fodor & Lepore (1992; not in-repo; characterization) — runs: *if* meaning is holistic, *then* any difference in the web changes the content of every expression in it. From which several unwelcome consequences are alleged to follow:

1. **No two systems ever share a content exactly.** Since no two speakers' (or models') webs are identical, strict holism implies they never mean exactly the same thing by any word — and so, on a strong reading, never disagree, agree, or translate, because there is no shared content to do it with.
2. **No two time-slices of one system share content.** Learning anything changes the web, hence (on strong holism) changes every meaning — so a system's terms shift content with every update, threatening the *stability* of meaning over time.
3. **The threat to communication.** If shared content is unobtainable, the ordinary picture of communication as the transfer of a shared content is undermined.
4. **The threat to compositionality.** Holism is in tension with the compositional picture on which the meaning of a complex expression is built from stable, independently-specifiable meanings of its parts. This is a real and much-argued line, but it is **[`compositionality.md`](compositionality.md)'s** to develop; here it is noted as one head of the objection and handed off.

The dialectic is not one-sided — holists reply that *exact* content-identity is the wrong requirement, and that *similarity* of inferential role is enough for communication and comparison (a Quinean/Davidsonian move toward "close enough" rather than "identical"). The project does not adjudicate this. What matters here is that the objection is the **central worry for conceptual-role semantics**, and that it transposes directly onto LLMs.

## Why it bites hard for LLMs

LLMs are holistic *by construction*, which is what makes this more than a philosophy-of-mind quarrel for this project.

**Distributional models are holist by construction.** A token's representation just *is* its position in the whole co-occurrence web — its meaning, on the distributional view, is constituted by patterns of co-occurrence across the entire training distribution ([`concept/distributional-meaning`](distributional-meaning.md)). There is no atom; the vector for a word is defined relationally against every other. So an artefact built on the distributional hypothesis inherits holism's structure whether or not its builders wanted the philosophical commitment.

**The strongest pro-LLM-meaning position is *explicitly* holist.** Piantadosi & Hill's conceptual-role account ([`concept/inferential-meaning`](inferential-meaning.md)) states the holism outright:

> "Because conceptual role is defined by the relationships between internal representational states, meaning cannot be determined from a model's architecture, training data, or objective function, but only by examination of how its internal states relate to each other." ([`source/piantadosi-hill-2022-meaning-without-reference`](../sources/piantadosi-hill-2022-meaning-without-reference.md), §Abstract)

Read against the spectrum, "*only* by examination of how its internal states relate to each other" is a holist thesis: meaning is in the web of internal relations, with the architecture, data, and objective explicitly *insufficient* to fix it. This is the **key tension** the page surfaces: the most affirmative position on LLM meaning in the repo is the position that most fully *inherits the holism objection*. If meaning is constituted only by internal-state-to-internal-state relations, then Fodor & Lepore's worry applies with full force — two models with different relational geometries would, strictly, share no content; one model before and after a fine-tune would share none with itself. (Bender & Koller, from the other side, deny the antecedent: a "system trained only on form has a priori no way to learn meaning" at all ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5185) — so for them the holism objection is moot, the relations are not meaning to begin with. The holism objection is the *internal* problem for the pro-meaning side; the grounding objection is the *external* one.)

### What the project's own findings say about it

Two in-repo results bear on strong holism's "one entangled content store" picture. Both are read cautiously, and the direction of bearing is stated explicitly.

**A mild *strain* on strong holism — competences dissociate (n=3, orderings only).** [`result/cross-axis-lexical-constructional-ordering-v1`](../../findings/results/cross-axis-lexical-constructional-ordering-v1.md) asks whether a model's *lexical* sense-gradience strength predicts its *grammatical/constructional* performance. The lexical order (gemini 0.80 > claude 0.68 > gpt-5.4-mini 0.60) transfers only **at the bottom** — gpt-5.4-mini is weakest lexically *and* the most fragile constructionally — but **not at the top** (gemini's lexical lead does not make it uniquely strongest constructionally), and on the one same-instrument coercion bridge the order **inverts** (claude 31.4 > gpt 20.5 > gemini 8.3). So the lexical and grammatical competences **dissociate** at the model level. On a *very* strong holism in which all of a system's content is one entangled store, one might have expected competence to move together across grains; that the strongest pure lexical tracker is the *least* coercion-sensitive is a small piece of friction against that expectation. The honest reading is narrow: **behavioral competences are at least partly separable**, not "the content store is modular." The binding caveat is loud — **n = 3 models is an ordering, not a coefficient**; only a handful of rank-orders exist and none is significance-testable. This *strains* a strong-holism reading; it does not refute holism, which is a thesis about content-constitution, not about behavioral skill profiles. (INTERPRETATION, not a holism test: the result was built to probe the lexicon–grammar continuum — [`theory/lexicon-grammar-continuum`](../../findings/theory/lexicon-grammar-continuum.md) — not holism, and is `anchor: internal-contrast-only` — a within-model contrast making no human-comparison claim.)

**Relevant to holism-vs-shared-meaning — cross-model convergence (INTERPRETATION).** [`result/relational-reference-game-v1`](../../findings/results/relational-reference-game-v1.md) had three independently-run models from different makers coin opaque conventions in a reference game; a fresh matcher then recovered each convention from the shared content of prior turns (the convention proved **order-insensitive** — recovered from the *set* of turns, not their ordered trajectory). That different "webs" — three separately-trained systems — still **converge on a usable convention recovered from shared content** is *relevant* to the holism-vs-shared-meaning question: it is the kind of cross-system commonality strong holism predicts should be unavailable. But this is marked clearly as **INTERPRETATION, not a holism test**. The result was designed to probe relational meaning-constitution, and its own headline is a *deflationary* null (convergence is *coordination*, explained by the overlapping distributional content two next-token predictors condition on, not *constitution*). The deflationary reading actually fits holism comfortably: shared distributional substrate → overlapping webs → convergence, no shared *content* in the strict atomist sense required. So this result is **suggestive, not decisive**, on the holism axis, and its force points toward the deflationary sibling, not toward settling holism.

## The methodological bet

There is a bet under the whole project that this page must flag honestly. The project's central *method* — comparing models against each other, and against human resources (treebanks, sense inventories, acceptability norms) — **presupposes enough shared content to make the comparison meaningful**. When [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md) reports that a model's graded sense ratings rank-correlate with the human DURel median, that *assumes* the model's "relatedness" and the annotators' "relatedness" are commensurable enough to correlate. Strong holism is exactly the position that would question this: if each system's web fixes its own content with no shared remainder, cross-system and human-vs-model comparison have nothing stable to range over.

This is not a fatal objection — the holist's own "similarity is enough" reply is available, and the project's comparisons are statistical-behavioral, not claims of content-identity — but it is a **load-bearing assumption worth naming rather than hiding**. It is the same assumption flagged on [`meaning-senses.md`](../../meaning-senses.md), whose open issue *"Should `distributional` and `inferential` collapse, given that next-token prediction is implicitly inferential?"* is downstream of exactly this axis: if the inferential web and the distributional web are the same holistic object, the two tags track one thing; if molecularism is right, there is a principled subset that pulls them apart. The project's working stance is the modest one — treat the comparisons as tracking *similarity* of role, not identity of content — and to let the deflationary upshot (that the convergence may be mere coordination over a shared substrate) be developed where it belongs, in [`deflationary-and-eliminativist-llm-meaning.md`](deflationary-and-eliminativist-llm-meaning.md).

## What this page supports, strains, and is silent on

- **Supports** (sets up the tension for): the holist reading of [`concept/inferential-meaning`](inferential-meaning.md) and [`concept/distributional-meaning`](distributional-meaning.md) — naming the objection their strongest form inherits.
- **Strains** (mildly, n=3, orderings only): a *strong* "one entangled content store" holism, via the cross-axis competence dissociation ([`result/cross-axis-lexical-constructional-ordering-v1`](../../findings/results/cross-axis-lexical-constructional-ordering-v1.md)). Not a refutation of holism as a content-constitution thesis.
- **Silent on**: whether holism is *true*; whether the holism objection is *decisive* (the "similarity is enough" reply is live); the threat-to-compositionality argument (handed to [`compositionality.md`](compositionality.md)); the deflationary verdict (handed to [`deflationary-and-eliminativist-llm-meaning.md`](deflationary-and-eliminativist-llm-meaning.md)); and any human-comparison claim about LLM content (this is a concept page — no resource anchor, and the results it cites are internal-contrast-only or deflationary nulls).
