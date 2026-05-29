---
type: concept
id: constructional-meaning
title: Constructional meaning (form–meaning pairings)
meaning-senses:
  - constructional
  - inferential
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: source/weissweiler-2023-cxg-insight
  - rel: refines
    target: concept/distributional-meaning
  - rel: refines
    target: concept/formal-vs-functional-competence
---

# Constructional meaning (form–meaning pairings)

Construction Grammar (CxG; Goldberg 1995, 2006; Croft 2001; Fillmore et al.; not in-repo) holds that the basic unit of grammatical knowledge is the **construction**: a conventionalized pairing of form and meaning that is not fully predictable from its parts. Constructions range from morphemes and closed-class items through idioms and argument-structure templates to large-scale discourse patterns. What makes a construction a construction — and what makes constructional meaning a distinct sense in this project's vocabulary — is that the meaning is carried by the pairing itself, not by the individual lexical items slotted into it. The ditransitive (*she gave him the book*), the *way*-construction (*they elbowed their way through*), and the AANN pattern (*a beautiful three days*) all carry semantic content — agency-and-transfer, effortful traversal, scalar-evaluative unitization — that is not derivable from the parts' independent distributional meaning.

Weissweiler et al. (2023) provide the methodological statement for CxG-based probing of neural language models: "According to CxG, meaning is encoded in abstract constellations of linguistic units of different sizes" (source/weissweiler-2023-cxg-insight, §2.1). The paper's central argument is that probing for construction knowledge tests whether a model encodes the **form–meaning unity**, not merely a distributional surface pattern or a semantic plausibility preference in isolation — making CxG probes a sharper test of meaning-tracking than either pure acceptability tasks or pure semantic similarity tasks. The confound to guard against is memorization of collocational patterns, which can produce the right surface behavior without encoding the construction's constraint structure (source/weissweiler-2023-cxg-insight, §3.1).

For this project, constructional meaning is the main empirical wedge. Constructions have three features that make them tractable: (1) they license probing by minimal pairs across licit and illicit instantiations; (2) they license inferential probes — the construction's meaning entails specific consequences (the AANN entails a unified scalar frame; the *way*-construction entails effortful self-propelled motion); (3) they provide gradient measures through slot constraints (adjective type, noun type, verb telicity) that distinguish pure form-tracking from partial meaning-tracking. The `constructional` tag should typically be co-tagged with `inferential` when the finding turns on whether the construction's inference-licensing is tracked, and co-tagged with `distributional` when the finding is that only the distributional surface environment has been learned.

**Live tension for this project.** The hardest question is where form ends and constructional meaning begins. The AANN form — *a* + evaluative-adj + numeral + plural-noun — has a characteristic distributional environment that a language model can track without encoding the construction's unification-and-evaluation meaning. Structural acceptability tasks probe the form side; inferential probes (does the model treat *a beautiful three days* as presenting the stretch as a coherent, evaluatively-loaded unit?) probe the meaning side. The claim `formal-competence-aann-ceiling` encodes exactly this gap: acceptability-ceiling is evidence of formal competence, not constructional meaning-tracking (findings/claims/formal-competence-aann-ceiling.md). Resolving this tension requires probes that go beyond form-acceptability to gradient semantic constraints and inference-licensing — the open design question for the AANN, *way*, and dative-alternation conjecture lines.
