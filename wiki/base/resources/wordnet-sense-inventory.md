---
type: resource
id: wordnet-sense-inventory
title: Princeton WordNet — expert sense inventory (synsets) for English
status: verified
url: https://wordnet.princeton.edu/
paper: "Miller 1995, CACM 38(11):39–41; Fellbaum (ed.) 1998, WordNet: An Electronic Lexical Database, MIT Press"
license: "WordNet 3.0 License (permissive, BSD-style) — verbatim below; verified 2026-05-31 from the LICENSE file shipped in the NLTK `wordnet` corpus zip"
meaning-senses:
  - referential
  - human-comparison
  - distributional
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: anchors
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Princeton WordNet — expert sense inventory

> **Verification (2026-05-31):** the WordNet 3.0 data was inspected directly via the NLTK
> `wordnet` corpus (`from nltk.corpus import wordnet`): **117,659 synsets** total, **82,115 noun
> synsets** (WordNet 3.0). The license text below is **verbatim** from the `LICENSE` file shipped
> inside the NLTK `wordnet.zip` (`WordNet Release 3.0`, dated 2006-11-14). The Princeton web page
> (https://wordnet.princeton.edu/license-and-commercial-use) was Cloudflare-gated this session and
> could not be fetched directly; the shipped LICENSE is the authoritative copy used here.

## What it is

**WordNet** (Princeton) is the standard English lexical database: nouns, verbs, adjectives and
adverbs are grouped into **synsets** (synonym sets), each a distinct lexicalized **sense** ("concept"),
with definitions (glosses), example sentences, and semantic relations (hypernymy, meronymy, antonymy,
…). A polysemous word maps to *multiple* synsets, one per sense; two synsets of the same word that are
etymologically/semantically unrelated are the standard operationalization of **homonymy** vs the
related-sense **polysemy** within one word. Introduced in Miller 1995 (CACM) and documented in
Fellbaum (ed.) 1998.

## The human signal — what bears, and its grain

WordNet's synsets are an **expert-lexicographer sense partition**: which uses of a word count as "the
same sense" is fixed by trained lexicographers, not by a per-item rating panel. This is the **same
family of signal** that WiC ([`resource/wic-word-in-context`](wic-word-in-context.md)) is built from
(WiC's same/different labels are derived from WordNet/Wiktionary/VerbNet sense structure). So WordNet
is a legitimate **independent human sense inventory** — but it is a *categorical lexicographic
partition*, **not**:

- a *graded* human relatedness rating (that is DURel / [`resource/dwug-usage-graphs`](dwug-usage-graphs.md));
- a *per-item* human judgment on a specific sentence pair (that is WiC's released labels, or a
  sense-annotated corpus like SemCor).

**Honest scope for a constructed probe.** When a study *constructs* its own sentence pairs and assigns
each pair a same/different gold **by which WordNet synset the author judges each context to instantiate**
(as in [`result/multimodal-grounding-image-v1`](../../findings/results/multimodal-grounding-image-v1.md)),
the human-anchored part is the **synset inventory** (that these are genuinely distinct vs identical
senses in WordNet — verifiable, e.g. `bat.n.01` mammal vs `bat.n.05` club). The **mapping of a
constructed sentence to a synset is the author's**, not an independent annotator's. That makes the gold
*weaker* than a released per-item human label (WiC/SemCor) and it must be stated as such: the claim is
anchored to "WordNet says these senses are distinct," not to "a human judged these two sentences
different." Verify the synsets; do not over-state the gold as a per-item human judgment.

## What it can / cannot ground

- **Can:** a categorical same-sense / different-sense (and polysemy-vs-homonymy) distinction for English
  content words, with verifiable synset ids; the sense-inventory backbone the operationalization gate's
  Q2 stratification names ([`decisions/resolved/lexical-sense-gradience-operationalization`](../../decisions/resolved/lexical-sense-gradience-operationalization.md))
  and the v2/v3 polysemy/homonymy split assume.
- **Cannot:** a graded relatedness magnitude (use DWUG); a per-item behavioral human label on a specific
  context pair (use WiC / SemCor); reference/extension (`referential.sense`, not `referential.reference`).

## License (verbatim, WordNet 3.0)

> "Permission to use, copy, modify and distribute this software and database and its documentation for
> any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the
> following copyright notice and statements, including the disclaimer, and that the same appear on ALL
> copies … WordNet 3.0 Copyright 2006 by Princeton University. All rights reserved."

A permissive, BSD-style license (the "WordNet License"): unrestricted use including modification and
redistribution (commercial included), provided the copyright notice + disclaimer travel with copies,
and Princeton's name is not used in advertising. One of the most permissive resources in the repo.

## Where it lives

- Princeton WordNet: https://wordnet.princeton.edu/ (download + browser). Paper: Miller 1995 (CACM
  38(11):39–41); Fellbaum (ed.) 1998 (MIT Press).
- Accessed in-repo via the **NLTK `wordnet` corpus** (`nltk.download('wordnet')`), WordNet 3.0
  (117,659 synsets / 82,115 noun synsets, verified 2026-05-31). Synset ids cited by a probe (e.g.
  `crane.n.05`) are reproducible from this corpus.
