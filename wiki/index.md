# wiki/index.md — catalog

Read this before loading any individual page. Load pages selectively.

The wiki is split into two strata:

- `base/` — **stratum 0**: prior knowledge and human-anchored resources. Source of truth about human semantics.
- `findings/` — **strata above**: this project's own typed work.

`meaning-senses.md` is the controlled vocabulary every findings page must tag against.

## Pages

### Controlled vocabulary

- `meaning-senses.md` — typology of senses of "meaning". Mechanically required by `senselint`.

### Base — concepts

- `base/concepts/distributional-meaning.md` — stub
- `base/concepts/referential-meaning.md` — stub
- `base/concepts/inferential-meaning.md` — stub
- `base/concepts/grounding.md` — stub
- `base/concepts/formal-vs-functional-competence.md` — stub
- `base/concepts/constructional-meaning.md` — stub

### Base — sources

(none ingested yet — see `base/wanted.md`)

### Base — resources

- `base/resources/index.md` — catalog of human-anchored empirical resources.
- `base/resources/mahowald-2023-aann-stimuli.md` — Mahowald 2023 EACL AANN stimulus suite + MTurk acceptability ratings (status: external-only); anchor for `conjecture/aann-construction`.

### Base — wants

- `base/wanted.md` — prioritized fetch list for Tom.

### Findings — conjectures

- `findings/conjectures/dative-alternation-information-structure.md`
- `findings/conjectures/aann-construction.md` — status: designed (2026-05-28)
- `findings/conjectures/way-construction.md`
- `findings/conjectures/function-word-substitutability.md`

### Findings — claims / results / theory / open-questions

(none yet)

### Experiments — designs

(Not part of the wiki tree, but indexed here for navigability.)

- `experiments/designs/aann-construction-v1.md` — provisional; contingent on `aann-stimulus-source` and `aann-operationalization`.

### Open questions

- `findings/open-questions/relational-meaning-pilot.md` — what minimal two-agent setup constitutes evidence that meaning is being constituted *between* agents rather than computed inside each?

## How to extend this file

When you add a typed page, add a one-line entry here in the right section. When you retire one, leave the line and append `— retired YYYY-MM-DD`. Do not delete entries; the audit trail matters.
