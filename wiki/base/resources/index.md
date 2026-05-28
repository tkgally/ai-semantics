# Human-anchored resources — catalog

This is the project's reservoir of independent human bearing on empirical claims about LLM meaning (charter §2.5). Every empirical claim about LLM meaning must `anchors:` a resource catalogued here.

A resource page belongs here when the artifact:

1. Was produced by humans, with human judgment in the loop (treebank, sense-annotated corpus, acceptability norming, dictionary, construction inventory, etc.).
2. Has a documented method and a stable identifier.
3. Can be inspected (in repo or via a stable URL) by a later run.

Format per page (under `base/resources/<id>.md`):

```yaml
---
type: resource
id: universal-dependencies
title: Universal Dependencies
status: catalogued | partial | external-only
url: https://universaldependencies.org/
local-path: data/ud/   # if mirrored locally
license: ...
---
```

Plus a short prose description of:

- What the resource is and how it was made.
- **What kinds of claims it can ground** (be specific — UD can ground claims about dependency structure across languages; it cannot ground claims about word sense disambiguation).
- Known limits.
- Pointer to the specific feature(s) most likely to be cited by claims.

## Catalogued

- `mahowald-2023-aann-stimuli.md` — Mahowald 2023 EACL AANN stimulus suite (templates + slot fillers) plus MTurk acceptability ratings, released at `github.com/mahowak/aann-public`. Status: `external-only`. Grounds: `conjecture/aann-construction` and `experiments/designs/aann-construction-v1.md`.

## Shortlist to catalogue when a finding first cites them

These are the resources the founding conjectures point to. They become full pages in this directory when first cited.

- **Universal Dependencies (UD)** — multi-lingual dependency treebanks; for any claim about argument structure across languages.
- **PropBank / FrameNet / VerbNet** — predicate-argument and frame-semantic annotation; for argument-structure constructions and verb-class semantics.
- **CoNLL acceptability / BLiMP / SyntaxGym** — minimal-pair acceptability sets; canonical anchors for behavioral semantics/syntax probes.
- **WordNet / OntoNotes / SemCor** — sense inventories and sense-tagged corpora; for any claim about lexical sense.
- **CxG construction inventories** — e.g., the *Berkeley Construction Inventory*, ConstructiCon (Russian, English etc.); for any constructional claim.
- **Norming / rating studies** — concreteness, age-of-acquisition, semantic feature norms (McRae et al.; Brysbaert) — when a claim turns on a graded human judgment about a lexical item.

When a run first cites one of these, write the resource page (the catalogue entry), check the specific feature actually bears on the claim, and `anchors:` to it. Do not pre-write empty resource pages.
