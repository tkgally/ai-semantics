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

- `base/concepts/distributional-meaning.md` — distributional view; the null hypothesis for constructional-meaning claims. Grounded in Bender & Koller, Piantadosi & Hill, Weissweiler. (filled 2026-05-29)
- `base/concepts/referential-meaning.md` — stub
- `base/concepts/inferential-meaning.md` — stub
- `base/concepts/grounding.md` — stub
- `base/concepts/formal-vs-functional-competence.md` — Mahowald et al. 2024 distinction; structural knowledge vs. language-in-the-world. (filled 2026-05-29)
- `base/concepts/constructional-meaning.md` — CxG form–meaning pairing; underwrites the `constructional` tag. Grounded in Weissweiler 2023. (filled 2026-05-29)

### Base — sources

- `base/sources/bender-koller-2020-climbing.md` — Bender & Koller 2020, ACL; form-vs-meaning argument, octopus thought experiment; grounds `grounded` tag. **status: received** (page-level quotes extracted 2026-05-28).
- `base/sources/lyre-2024-semantic-grounding.md` — Lyre 2024, arXiv 2402.10992; grounding-as-gradual, three-dimensional typology (functional/social/causal); grounds `grounded` sub-tags. **status: received** (page-level quotes extracted 2026-05-28).
- `base/sources/piantadosi-hill-2022-meaning-without-reference.md` — Piantadosi & Hill 2022, arXiv 2208.02957; conceptual-role semantics, meaning without reference; grounds `inferential` tag. **status: received** (section-level quotes extracted 2026-05-28).
- `base/sources/weissweiler-2023-cxg-insight.md` — Weissweiler et al. 2023, GURT; CxG-probing methodology, form–meaning pairing as test criterion; grounds `constructional` tag. **status: received** (section-level quotes extracted 2026-05-28).
- `base/sources/mahowald-2024-dissociating.md` — Mahowald et al. 2024, TiCS 28(6); formal-vs-functional competence distinction, neuroscience grounding; primary reference for `functional-vs-formal` tag. **status: received** (section-level quotes extracted 2026-05-28).

### Base — resources

- `base/resources/index.md` — catalog of human-anchored empirical resources.
- `base/resources/mahowald-2023-aann-stimuli.md` — Mahowald 2023 EACL AANN stimulus suite + MTurk acceptability ratings (status: external-only); anchor for `conjecture/aann-construction`.

### Base — wants

- `base/wanted.md` — prioritized fetch list for Tom.

### Findings — conjectures

- `findings/conjectures/dative-alternation-information-structure.md`
- `findings/conjectures/aann-construction.md` — status: designed (2026-05-28)
- `findings/conjectures/way-construction.md` — status: designed (2026-05-28); path-traversal (self-motion) inference
- `findings/conjectures/function-word-substitutability.md`
- `findings/conjectures/caused-motion-construction.md` — status: proposed (2026-05-29); transitive causation-of-motion from non-motion verbs; anchor pending (`caused-motion-anchor`)
- `findings/conjectures/conative-construction.md` — status: proposed (2026-05-29); cancellation of the completed-contact entailment (verb held constant); anchor pending (`conative-anchor`)

### Findings — claims / results / theory / open-questions

- `findings/claims/formal-competence-aann-ceiling.md` — status: proposed (2026-05-28); AANN acceptability ceiling is evidence of formal, not functional, linguistic competence. Grounded by Mahowald 2024 formal/functional distinction; anchored to `resource/mahowald-2023-aann-stimuli`.
- `findings/claims/cxg-probing-surprisal-validity.md` — status: proposed (2026-05-29); surprisal contrast on form–meaning minimal pairs is a valid (but bounded) operationalization of constructional-meaning *sensitivity*. Methodological counterpart to the AANN-ceiling claim. `anchor: pending`, contingent on `cxg-probing-anchor`.
- `findings/theory/constructional-meaning-in-llms.md` — status: draft (2026-05-29); the project's first theory page. A five-tier evidence ladder (form-acceptability < surprisal-contrast < gradient semantic tracking < generalization < inference-licensing) placing each existing claim/conjecture; brackets the grounding axis; flags the relational axis as future work.

### Experiments — designs

(Not part of the wiki tree, but indexed here for navigability.)

- `experiments/designs/aann-construction-v1.md` — provisional; contingent on `aann-stimulus-source` and `aann-operationalization`.
- `experiments/designs/way-construction-v1.md` — provisional; anchor pending `way-construction-anchor` decision.

### Open questions

- `findings/open-questions/relational-meaning-pilot.md` — what minimal two-agent setup constitutes evidence that meaning is being constituted *between* agents rather than computed inside each?
- `findings/open-questions/constructional-vs-frequency-confound.md` — status: open (2026-05-29); how to separate constructional-meaning sensitivity from an n-gram/frequency confound in surprisal-contrast probes (form-level).
- `findings/open-questions/distributional-vs-inferential-constructional.md` — status: open (2026-05-29); granting constructional sensitivity, what minimal evidence shows it is inferential-role tracking vs. a distributional shadow (meaning-level; downstream of the frequency question).

## How to extend this file

When you add a typed page, add a one-line entry here in the right section. When you retire one, leave the line and append `— retired YYYY-MM-DD`. Do not delete entries; the audit trail matters.
