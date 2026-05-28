# meaning-senses.md — controlled typology

This is the controlled vocabulary that every `wiki/findings/` page must tag with at least one entry under `meaning-senses:` (see `CLAUDE.md`). The point is not a finished taxonomy. The point is to refuse the unqualified word "meaning" in this project's prose. Where two senses are both relevant, list both — that is informative, not a defect.

This page is **revisable**. Propose changes via a `decisions/open/` entry; do not silently rename a tag that other pages already cite.

## Tags

### `distributional`
Meaning as patterns of co-occurrence in linguistic context. The Firth/Harris tradition; the implicit theory of word embeddings and the next-token objective. Operationalized through similarity, substitution behavior, neighborhood structure, and predictive surprisal in context.

- Anchors: corpus distributional measures, vector-space neighborhoods, surprisal under a language model.
- Caveat: by itself, distributional structure is silent on reference and on truth — this is exactly the contested boundary.

### `referential`
Meaning as the relation between an expression and something in the world (or in a model). Frege's `Bedeutung`; the externalist tradition (Putnam, Burge, Evans). Sub-distinctions worth carrying:

- `referential.sense` — Frege's `Sinn`: mode of presentation.
- `referential.reference` — what the expression picks out.
- `referential.externalist` — meaning fixed by causal/social embedding (Twin Earth, division of linguistic labor).

When a finding turns on whether an LLM tracks reference vs. only sense, tag both sub-distinctions.

### `inferential`
Meaning as inferential role: a word/construction means what it licenses you to infer to and from. Brandom's inferentialism; conceptual-role semantics. Includes Piantadosi & Hill's "meaning without reference" line — that a meaningful expression need not bottom out in extra-linguistic reference.

- Anchors: entailment datasets, NLI behavior, acceptability under inference-licensing constructions, behavior on systematic substitution that preserves/breaks inferential role.

### `grounded`
Meaning as anchored in non-linguistic experience — perception, action, body, social embedding. The form-vs-meaning distinction of Bender & Koller's "climbing toward NLU" is the strongest form; Lyre's grounding-as-gradual (functional, social, causal sub-grounds) is the most useful framing for a non-binary project like this one.

- Sub-distinctions to consider tagging:
  - `grounded.perceptual` — multimodal anchoring (text+image+audio+video).
  - `grounded.causal` — tracking of intervention/consequence structure.
  - `grounded.social` — uptake in joint action, normative status.
- The Bender-Koller "octopus" thought experiment is a stress test on `grounded.causal` and `grounded.social`, not on `distributional`.

### `functional-vs-formal`
The Mahowald / Ivanova / Fedorenko distinction between formal linguistic competence (knowing the patterns of a language) and functional competence (using language for reasoning, world-modeling, social action). Tag a finding here when its bite is precisely whether an LLM's behavior is on the formal or functional side of that line.

### `constructional`
Meaning as form–meaning pairing at any level of the grammar — morphemes, words, idioms, argument-structure constructions. Construction Grammar (Goldberg, Croft, Fillmore). The CxG-probing line (Weissweiler, Tayyar Madabushi, Scivetti) is the natural home for many of this project's experiments.

- Operationalizes a particularly tractable wedge: function words, inflection, argument structure, and idiomatic templates have meaning that is under-theorized at the meaning-theory level yet probeable through minimal pairs and acceptability.
- Often co-tag with `inferential` (constructions license inferences) or `distributional` (constructions have characteristic distributions).

### `model-internal`
Meaning located in a single model's behavior or representations — the first of the three candidate axes in §1 of the charter. Tag a finding here when the claim is about one model's internal structure, not about cross-model convergence or human-comparison.

### `relational`
Meaning constituted between a model and a person, or between models — the under-explored second axis from the charter. Treat this as the project's distinctive wedge: the multi-agent literature is about coordination, not meaning-constitution.

### `human-comparison`
Meaning understood by setting LLM behavior against existing human-generated evidence — the third axis. Tag here when the finding's force comes specifically from a contrast or alignment with a treebank, sense inventory, acceptability norm, or other human-anchored resource.

## How to tag (rules of thumb)

- A finding can carry multiple tags; do not force a single one.
- If you cannot decide between tags, the page probably needs sharpening first.
- If the sense you mean is not in this list, propose an addition in `decisions/open/` rather than inventing a tag inline.
- "Meaning" used without a clear tag in prose is a lint defect; reword.

## Open issues with the typology

These are not yet settled. They become decision pages as they bite.

- Is `grounded.social` a sub-tag of `grounded` or a separate top-level sense closer to `relational`? Plausibly the latter for this project.
- Should `distributional` and `inferential` collapse, given that next-token prediction is implicitly inferential? Probably no — but write the case explicitly when it next matters.
- Is `model-internal` a meaning-sense at all, or only a *locus*? If the latter, move it out of this vocabulary.
