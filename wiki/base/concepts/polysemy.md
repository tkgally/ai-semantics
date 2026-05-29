---
type: concept
id: polysemy
title: Polysemy, homonymy, and graded word sense
meaning-senses:
  - referential
  - distributional
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: refines
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: resource/wic-graded-usage-similarity
---

# Polysemy, homonymy, and graded word sense

**Polysemy** is the property of a single word having multiple related senses that shade into one another, with intermediate and bridging cases where two senses are co-present and judgements are genuinely indeterminate. The canonical examples are *paper* (material / newspaper / academic article) and *run* (a verb with dozens of related uses across locomotion, cooking, management, and time). **Homonymy** is the sharply different case: unrelated senses sharing a phonological and orthographic form by historical accident — *bank* (riverside / financial institution), *bat* (flying mammal / sports implement). The distinction is a lexicographer's baseline, and it is the core of the project's lexical wedge: the two cases are the built-in internal control for any probe of LLM sense behavior, because the same model, on the same surface form, faces a structurally different task in each regime.

The charter names this property directly as an under-used asset: "a lexicographer's tolerance for fine-grained polysemy and sense-distinction … the gradiness is the point" ([`PROJECT.md`](../../../PROJECT.md) §1, via [`open-question/lexical-polysemy-gradience`](../../findings/open-questions/lexical-polysemy-gradience.md)). This concept page is that asset's base-concept home — exactly parallel to the role [`concept/coercion`](coercion.md) plays for the constructional wedge.

## What polysemy is: sense as graded and relational

The defining property of polysemy is **gradience**. Between the "completely different" end (homonymy) and the "same sense" end, polysemous usages of a word occupy intermediate positions where relatedness is real but senses are genuinely distinct. A use of *paper* meaning newspaper and a use meaning academic article share a conceptual ancestor — something written and published — without being the same mode of presentation; a bridging context ("I read the paper") leaves the two co-present. These bridging contexts are not anomalies to be disambiguated away; they are the evidence that sense distinctions are scalar, not binary. The gradience is the point.

Homonymy, by contrast, is discrete. *Bank* (riverside) and *bank* (financial) share no semantic ancestor: they are two unrelated lexical entries that happen to converge on the same form. There is no bridging context where both senses are co-present in the way *paper* bridges article and newspaper; disambiguation is expected and clean.

The lexicographer's tradition handles this contrast through sense-relation vocabulary — hyponymy, meronymy, antonymy, troponymy — but for this project's purposes the operative distinction is simply: does varying usage regularly produce *graded* relatedness judgements (polysemy), or does it produce a step function with no meaningful intermediate (homonymy)? That is the question the lexical wedge puts to an LLM.

## How this refines referential meaning: sense at fine grain

Polysemy is a `referential.sense` phenomenon — Frege's `Sinn`, the mode of presentation, at fine grain. When someone uses *paper* to mean newspaper rather than academic article, the difference is not in reference (the denotation of "paper" in the abstract) but in which mode of presentation is operative: which cluster of descriptive and inferential associations the usage mobilizes. "Sense" in the Fregean tradition is the fine-grained vehicle; polysemy is what happens when one word carries multiple such vehicles that are related but not identical.

This page therefore `refines` [`concept/referential-meaning`](referential-meaning.md) in the same way [`concept/coercion`](coercion.md) refines [`concept/constructional-meaning`](constructional-meaning.md): it is a sharpening within the referential-sense sub-position, not a new kind of meaning. The referential-meaning page notes that "sense as position in an inferential/associative web is close to what co-occurrence statistics encode" ([`concept/referential-meaning`](referential-meaning.md), §"Why the hardest LLM-meaning cases live here"). Polysemy is the test of how *fine-grained* that tracking goes: whether distributional training recovers not just same/different discrimination (which is a coarse sense-presence test) but the graded relatedness a lexicographer would map — the difference between a 1-on-a-5-point-scale pair and a 3-on-a-5-point-scale pair.

Note that polysemy does not touch the `referential.reference` or `referential.externalist` sub-positions: sense distinctions between usages of *paper* do not turn on which object *paper* picks out in the world, and they do not require a causal-historical anchoring story. The wedge is cleanly within the `referential.sense` sub-tag.

## The distributional null: context-similarity as the shadow

[`concept/distributional-meaning`](distributional-meaning.md) gives sense-in-context for free. A word embedded in different sentences occupies different distributional neighborhoods, and those neighborhoods encode something sense-like. The deflationary reading of any apparent LLM sense-tracking is that the model is simply responding to the *similarity of the two sentence contexts* — how much the surrounding words overlap — rather than to the *relatedness of the two senses* as such.

This is the lexical analogue of the constructional distributional shadow that runs through the project's grammatical probes (where the null is that an LLM reproduces construction form because of co-occurrence patterns, not because it encodes the construction's meaning). Here the null is: the apparent gradience in the LLM's same/different-sense signal is monotonic in context-similarity, and once context-similarity is held constant the sense-relatedness signal goes flat.

The discriminating feature of the polysemy/homonymy contrast is precisely that it can break this null. Polysemous pairs and homonymous pairs can be matched for surface lexical overlap of their surrounding sentences while the human-rated sense relatedness differs sharply (related vs. unrelated). If the LLM's signal tracks the human relatedness distinction *within* that control, that is evidence for `referential.sense` tracking; if it goes flat, that is the distributional shadow. Without the control, any apparent gradience is underdetermined between the two. The context-similarity control is the design spine for the lexical wedge, as [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) states explicitly.

## What in-repo evidence bears

The one in-repo resource that directly operationalizes this concept is [`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md), which catalogs two datasets:

- **Usim** (Erk, McCarthy & Gaylord, ACL 2009 / Computational Linguistics 2013): human-rated graded usage-similarity on a 5-point scale ("1 — completely different … 5 — identical"), covering 34 lemmas and 1530 usage-pair comparisons (SPAIRs), each rated by 3 annotators. Usim does not require annotators to commit to a discrete sense label; it asks directly how similar two usages are. This is the instrument whose scale is calibrated to the gradience question. The resource page quotes the ACL 2009 abstract verbatim:

  > "We find that the graded responses correlate with annotations from previous datasets, but sense assignments are used in a way that weakens the case for clear cut sense boundaries." ([`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md), citing Erk, McCarthy & Gaylord, ACL 2009, https://aclanthology.org/P09-1002.pdf)

  That finding — that sense assignments weaken the case for clear-cut boundaries — is the empirical observation the gradience concept is built on. **However**: as the resource page records, Usim's data file is currently unfetchable (Box 404 / mirror 503 on 2026-05-29) and carries no explicit license; it has been retired as the conjecture's primary anchor pending identification of a graded, licensed, fetchable replacement (DWUG and CoSimLex are the leading candidates; see [`base/wanted.md`](../wanted.md)).

- **WiC** (Pilehvar & Camacho-Collados, NAACL 2019, CC BY-NC 4.0): binary same/different-sense judgments for a target word in two contexts. WiC grounds the discrete contrast and the same/different baseline, but is binary by design and cannot by itself ground the gradience (monotonicity) prediction.

Together, these two datasets map out the measurement space for the lexical wedge: the graded set (Usim, or its replacement) bears on the fine-grain gradience claim; WiC bears on the binary/discrete contrast.

## How polysemy sits in the project's vocabulary

This concept grounds the **lexical wedge** — the cluster consisting of [`open-question/lexical-polysemy-gradience`](../../findings/open-questions/lexical-polysemy-gradience.md) and [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md). Polysemy supplies the conceptual object the conjecture is about; the resource page supplies the empirical instrument; the open question frames the three hypotheses (graded-sense tracking, discrete-sense collapse, distributional shadow).

In the project's meaning-sense tagging, this concept sits at the intersection of `referential` (polysemy is about `referential.sense`, modes of presentation at fine grain) and `distributional` (the null is always a distributional-context-similarity reduction). When a finding on this wedge is written up, it should tag both senses and specify which is bearing the empirical weight — distributional context-similarity as the null to be beaten, referential.sense as the positive claim when the null is beaten. The concept does **not** touch the `relational` axis: the polysemy probe is `model-internal` (one model's sense behavior) plus `human-comparison` (against human-rated usage similarity or binary same/different labels). It also does not touch `referential.reference` or `referential.externalist` — sense distinctions between polysemous usages do not require a world-relation or causal-chain story.

The polysemy-vs-homonymy contrast is the wedge's built-in internal control. It does not need to be engineered separately: homonym pairs are the discreteness floor, polysemous pairs are the gradience case, and the same probe can be run across both. A model that shows an intermediate regime for polysemy but a floor for homonymy — and does so after the context-similarity control — is the signature the conjecture predicts.

## Honest gaps

The canonical lexical-semantics treatments of polysemy and sense-relation gradience — Cruse *Lexical Semantics* (1986), Murphy *Semantic Relations and the Lexicon* (2003), and Lyons *Semantics* (1977) — are on the wanted list ([`base/wanted.md`](../wanted.md)) and are **not yet in-repo**. No quote, page number, or finding from those works is attributed here, and none may be until a `source/` page with page-level provenance exists for them. The same applies to the Firth and Harris originals (the distributional-hypothesis sources) and the externalist tradition (Putnam, Evans), which are also in `wanted.md` and currently unverified.

The current grounding of this concept page is therefore limited to: the ACL 2009 Erk/McCarthy/Gaylord finding as quoted via [`resource/wic-graded-usage-similarity`](../resources/wic-graded-usage-similarity.md), the conceptual treatment of `referential.sense` in [`concept/referential-meaning`](referential-meaning.md), and the distributional-null framing in [`concept/distributional-meaning`](distributional-meaning.md). That grounding is sufficient for the wedge-concept role this page plays, but the lexicographic treatment of gradience, bridging, and sense-relation vocabulary is pending the Cruse and Murphy ingestions. Until those sources are in-repo, references to "the lexicographer's picture" rest on common knowledge in the field, not on a citable in-repo source.
