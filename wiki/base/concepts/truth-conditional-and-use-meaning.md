---
type: concept
id: truth-conditional-and-use-meaning
title: Truth-conditional meaning vs. meaning-as-use (the Wittgensteinian pole)
meaning-senses:
  - referential
  - inferential
  - distributional
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v3
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
---

# Truth-conditional meaning vs. meaning-as-use

This page owns one axis of the meaning-theory debate: **truth-conditions ↔ use**. It is the oldest fault line under the project's lexical and grammatical wedges, and it is the one that decides what an LLM's behavior could even *be evidence for*. Compositionality, prototype/frame category structure, semantic holism, and the deflationary/eliminativist positioning each have their own sibling page and are linked, not developed, here.

## The two poles

**(a) Truth-conditional / model-theoretic semantics.** On this view, to know the meaning of a (declarative) sentence is to know the conditions under which it would be true; meaning bottoms out in *reference* (what words pick out) and *truth-in-a-model* (how the picked-out things make sentences true or false). The lineage is, in its standard textbook telling (the primary texts are **not in-repo; characterization**): Frege's distinction between sense and reference (`Über Sinn und Bedeutung`, 1892) gave the referential side its modern shape, with `Bedeutung` as the truth-relevant semantic value of an expression; Tarski's recursive definition of truth for a formalized language (1933/1944) made "is true" a precise, compositional notion via satisfaction; Davidson (1967) proposed that a Tarski-style truth theory could serve as a theory of *meaning* for a natural language — in the standard slogan-form of his proposal, to give a sentence's meaning is, in effect, to state its truth-conditions; and Montague (PTQ, 1973) showed a fragment of English could be handled with the model-theoretic machinery of intensional logic, treating natural language as a formal language with a denotational semantics. The unifying commitment: meaning is, at its core, a *world-relation* — a function from expressions to truth-conditions or denotations — and the semantics of a complex expression is built up systematically from the denotations of its parts. (The systematicity half of that commitment is exactly [`compositionality.md`](compositionality.md)'s lane; the world-relation half is [`concept/referential-meaning`](referential-meaning.md)'s.)

**(b) Meaning-as-use / the Wittgensteinian pole.** Against fixing meaning to a determinate truth-condition, the later Wittgenstein (*Philosophical Investigations*, 1953; **not in-repo; characterization**) urged that the meaning of an expression is the *role it plays* in the practices — the "language-games" — embedded in a "form of life." The slogan reading is "don't look for the meaning, look for the use." Two further moves matter for this project. First, **family resemblance**: many of our general words (the standing example is *game*) are held together not by a shared set of necessary-and-sufficient conditions but by a network of overlapping, criss-crossing similarities — there need be no definitional core. Second, the rejection of a fixed, fully-determinate hidden sense behind ordinary words: what an expression means is exhausted by how it is used in practice, not by a private object or a sharp boundary the use is answerable to. On this pole, a meaning theory describes regularities of use; it does not reduce them to a denotation.

The two poles are not strictly contradictory about every word — a truth-conditional semanticist can grant that *use* is the evidence we have, and a use theorist can grant that some sentences have clear truth-conditions. They come apart on **where meaning ultimately lives**: in a relation to the world (pole a) or in patterns of practice (pole b). That is the choice this page is about.

## Where the project sits — a methodological reading (not a metaphysical verdict)

This section is an **interpretation of the project's method, flagged as such** — a working commitment, not a proven claim about what meaning *is*.

The project's primary instrument is behavioral API probing: it reads a model's "meaning" off **patterns of use** — same/different-sense ratings, graded relatedness judgments, acceptability, inference behavior under minimal pairs. That is methodologically a *use*-side stance by construction. Crucially, the project has **no verified truth-condition or world-relation for any LLM**: as [`concept/referential-meaning`](referential-meaning.md) records, "there is **no comparable in-repo resource that anchors reference**: no dataset that pins a human-agreed extension or reference relation an LLM could be tested against" (§"Live tension"). So the truth-conditional pole is not refuted here — it is *un-probed*, and un-probeable with the resources in hand.

The charter's "describe, don't litigate" posture and the project's recurring **distributional null** (apparent meaning-tracking must be shown to beat a context-similarity / form shadow before it counts) both sit closer to the use pole than to the truth-conditional one: they treat the regularity of use as the thing to characterize, and stay agnostic about an underlying denotational fact. **This is a bet the method makes**, and it should be stated plainly rather than smuggled in: probing use does not *show* that meaning is use; it shows that use is what this instrument can see. A truth-conditional theorist could agree with every measured number and still hold that the world-relation — the thing the instrument cannot reach — is where meaning really resides.

## Map to the lexical findings

- **[`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md) — SUPPORTS the use pole over a discrete sense inventory.** Across 200 DWUG EN within-period usage pairs, every panel model's graded sense-relatedness rating is strongly rank-correlated with the human DURel median: Spearman **0.68 / 0.60 / 0.80** (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash) on the 4-point DURel framing and **0.70 / 0.68 / 0.83** on the 0–100 framing — in or above the human inter-annotator range (DWUG EN human–human ρ ≈ 0.69) — and the monotonicity *survives* partialling out the model's own topic-similarity rating (gemini 0.80→0.73). The signal is **graded usage-relatedness**, not a near-binary same/different collapse onto a fixed inventory of senses. That is a *family-resemblance / meaning-as-use* picture of word sense: relatedness is scalar and read off use, not a step function over discrete denotations. The human-side echo is the Erk/McCarthy/Gaylord finding quotable via [`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md): "We find that the graded responses correlate with annotations from previous datasets, but sense assignments are used in a way that weakens the case for clear cut sense boundaries." (citing Erk, McCarthy & Gaylord, ACL 2009, https://aclanthology.org/P09-1002.pdf). *Honest bound:* this is a behavioral rank correlation, not evidence of graded sense *representations*, and the topic control is model-internal (see the result's own caveats); it supports the use pole's picture of sense, it does not prove the truth-conditional picture false.

- **[`result/lexical-polysemy-homonymy-v3`](../../findings/results/lexical-polysemy-homonymy-v3.md) — STRAINS the classical truth-conditional picture; SILENT on its strongest form.** The classical truth-conditional/lexicographic expectation is *discrete senses with a sharp polysemy/homonymy switch* — homonyms are two entries, polysemes one, and a competent system should treat them as different *kinds*. v3 is a **powered null** on exactly that switch: the panel's graded rating does **not** separate WiC same/different-sense pairs any better for homonyms than for polysemes (AUC_homonym − AUC_polyseme ≈ 0 in all 6 model×framing cells; permutation p 0.73–0.96), which strains the "discrete switch" expectation and is consistent with a single graded-use axis (homonyms simply sitting further out on it). The one positive — homonym different-sense pairs piling at the "unrelated" floor more than polyseme-F pairs — **cannot be separated from plain graded distance** (homonyms *are* more unrelated; it is half-driven by one lemma `case`, partly a gemini scale-use quirk, and its clustering-honest CIs cross zero). *Be scrupulous:* the result page states its design **cannot distinguish a discrete sense boundary from monotone graded distance** at all. So on the *strongest* truth-conditional claim — that a sharp discrete regime exists underneath — v3 is **SILENT, not decisive**; it removes a positive sign that a discreteness advocate would have wanted, nothing more. A null is "no detectable effect, or underpowered-for-the-discrete-reading," never "discreteness proven absent."

- **The truth-conditional pole is the SILENT cell for LLMs here.** No in-repo resource anchors *truth-conditions* or a *world-relation* for any model (the gap [`concept/referential-meaning`](referential-meaning.md) flags). Truth-conditional LLM meaning is un-probed **by construction** — the project measures use, and has no yardstick for the world-relation. Every "support for the use pole" above is therefore *relative*: it is support for the use picture over a *discrete-sense* construal, not a measured defeat of a truth-conditional one.

## Tensions and where they are developed

These are flagged links, not arguments to be made here:

- Truth-conditional semantics is the home of **systematic composition** ([`compositionality.md`](compositionality.md)) and tends to be **classical about categories** (necessary-and-sufficient definition) — whereas the category-structure evidence the project touches leans graded/usage-based, which is [`frame-and-prototype-semantics.md`](frame-and-prototype-semantics.md)'s lane.
- A strong use stance shades into **semantic holism** — if meaning is role-in-a-practice, an expression's meaning may depend on indefinitely much of the rest of the language; that consequence is [`semantic-holism.md`](semantic-holism.md)'s to develop.
- The use pole connects naturally to **inferential role** ([`concept/inferential-meaning`](inferential-meaning.md)): "what an expression licenses you to infer" is one disciplined way to make "use" precise, and Piantadosi & Hill's "meaning without reference" line is the in-repo statement that meaning need not bottom out in extra-linguistic reference — "there are many terms that are meaningful to us but have no discernible referent at all, such as abstract words like 'justice' and 'wit.'" ([`source/piantadosi-hill-2022-meaning-without-reference`](../sources/piantadosi-hill-2022-meaning-without-reference.md), §"Meaning and reference"). The hard truth-conditional rejoinder in-repo is Bender & Koller's: meaning is "the relation M ⊆ E × I which contains pairs (e, i) of natural language expressions e and the communicative intents i they can be used to evoke" ([`source/bender-koller-2020-climbing`](../sources/bender-koller-2020-climbing.md), p. 5187), and form-only training "will not learn meaning" because there is "not sufficient signal to learn the relation M between that form and the non-linguistic intent of human language users" (p. 5187) — a world/intent-relation requirement the use pole denies is constitutive.
- Whether *any* of this should be read as the model having meaning at all, or merely as a useful redescription of token statistics, is the **deflationary/eliminativist** question ([`deflationary-and-eliminativist-llm-meaning.md`](deflationary-and-eliminativist-llm-meaning.md)) — the pole this page's "use" reading is most easily mistaken for, and which that page keeps distinct.

## Honest gaps

The truth-conditional lineage (Frege 1892; Tarski 1933/1944; Davidson 1967; Montague PTQ 1973) and the use pole's founding text (Wittgenstein, *Philosophical Investigations*, 1953) are **not in-repo**; every characterization of them above is in this page's own words, with no quote or page locator, and all five are added to the returned `wanted.md` proposals. Until a `source/` page with page-level provenance exists for each, references to "the truth-conditional tradition" and "meaning-as-use" rest on standard common knowledge in the field, not on a citable in-repo source. The only verbatim quotes on this page are the three in-repo ones (Bender & Koller p. 5187; Piantadosi & Hill §"Meaning and reference"; Erk/McCarthy/Gaylord via the WiC-graded resource page). The project's stance toward the two poles is a **methodological commitment**, not an established metaphysics, as §"Where the project sits" states.
