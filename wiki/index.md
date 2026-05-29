# wiki/index.md — catalog

Read this before loading any individual page. Load pages selectively.

The wiki is split into two strata:

- `base/` — **stratum 0**: prior knowledge and human-anchored resources. Source of truth about human semantics.
- `findings/` — **strata above**: this project's own typed work.

[`meaning-senses.md`](meaning-senses.md) is the controlled vocabulary every findings page must tag against.

This page is the **project entry point**: start here to read the project's status and decide what to do next. The dashboard immediately below is the decision-relevant view; the full typed-page catalog follows under [Pages](#pages).

---

## Status & next steps — start here

### What to do next
- [`NEXT.md`](../NEXT.md) — current state and the next concrete action / fan-out backlog.
- [`log.md`](../log.md) — dated history of every run.
- Current synthesis: [`findings/theory/constructional-meaning-in-llms.md`](findings/theory/constructional-meaning-in-llms.md) — the live theory page (evidence ladder + where each finding sits).

### Open decisions — blocking, pending Tom
These gate promotion of contingent findings; nothing depending on them is settled until ratified. To resolve one, add a `resolution:` block or move the file to `wiki/decisions/resolved/` (see [`PROTOCOL.md`](../PROTOCOL.md) §2).

- [`decisions/open/aann-stimulus-source`](decisions/open/aann-stimulus-source.md) — ratify Mahowald 2023 as the primary AANN human anchor (default), or switch.
- [`decisions/open/aann-operationalization`](decisions/open/aann-operationalization.md) — ratify the continuation-likelihood contrast + T1 threshold (default), or switch.
- [`decisions/open/way-construction-anchor`](decisions/open/way-construction-anchor.md) — ratify Option A (Goldberg 1995 examples as seed; anchor pending), or supply rated data. **New candidate Option D surfaced: Scivetti 2025 CxNLI (realizes the gestured Option C).**
- [`decisions/open/cxg-probing-anchor`](decisions/open/cxg-probing-anchor.md) — scope the CxG-probing-validity claim to AANN (default), acquire a CxG-native broad anchor, or split the claim.
- [`decisions/open/caused-motion-anchor`](decisions/open/caused-motion-anchor.md) — choose the human anchor for the caused-motion conjecture (or fall back to a verb-frame resource + queue a want). **New candidate Option D surfaced: Scivetti 2025 CxNLI.**
- [`decisions/open/conative-anchor`](decisions/open/conative-anchor.md) — choose the human anchor for the conative conjecture (default: Levin 1993 / VerbNet conative-class as partial anchor). **New candidate Option D surfaced: Scivetti 2025 CxNLI.**
- [`decisions/open/relational-anchor-shortlist`](decisions/open/relational-anchor-shortlist.md) — choose the human dyadic-interaction anchor for the relational-meaning pilot (default: Clark & Wilkes-Gibbs 1986, with Pickering & Garrod 2004 as theoretical backdrop). Opened 2026-05-29.
- [`decisions/open/comparative-correlative-anchor`](decisions/open/comparative-correlative-anchor.md) — anchor for the comparative-correlative conjecture (default: Scivetti CxNLI CC subset, pending item-level inspection; fall back to Weissweiler-2022 seed with human arm pending). Opened 2026-05-29.
- [`decisions/open/constructional-divergence-operationalization`](decisions/open/constructional-divergence-operationalization.md) — instrument (NLI vs forced-choice vs both), thresholds, and frequency-matching for the upper-ladder divergence probes (default: both instruments, 30pp/70%/15pp thresholds, frozen at item-commit). Governs the divergence-probe family; first client is the CC design. Opened 2026-05-29.

### Resolved decisions
- (none yet) — ratified decisions will be listed here, each linking its file under `wiki/decisions/resolved/`.

### Fetch backlog & governance
- [`base/wanted.md`](base/wanted.md) — prioritized sources to fetch (Tom has library access).
- Charter [`PROJECT.md`](../PROJECT.md) · run discipline [`PROTOCOL.md`](../PROTOCOL.md) · conventions [`CLAUDE.md`](../CLAUDE.md).

---

## Pages

### Controlled vocabulary

- [`meaning-senses.md`](meaning-senses.md) — typology of senses of "meaning". Mechanically required by `senselint`.

### Base — concepts

- [`base/concepts/distributional-meaning.md`](base/concepts/distributional-meaning.md) — distributional view; the null hypothesis for constructional-meaning claims. Grounded in Bender & Koller, Piantadosi & Hill, Weissweiler. (filled 2026-05-29)
- [`base/concepts/referential-meaning.md`](base/concepts/referential-meaning.md) — sense/reference/externalist; the LLM-meaning debate's hardest cases. Grounded in Bender & Koller; Putnam/Evans grounding pending. (filled 2026-05-29)
- [`base/concepts/inferential-meaning.md`](base/concepts/inferential-meaning.md) — conceptual-role / inferential semantics; the strongest pro-LLM-meaning position. Grounded in Piantadosi & Hill. (filled 2026-05-29)
- [`base/concepts/grounding.md`](base/concepts/grounding.md) — form-vs-meaning (Bender & Koller, binary) vs. grounding-as-gradual (Lyre, three-dimensional); the project's gradient stance. (filled 2026-05-29)
- [`base/concepts/formal-vs-functional-competence.md`](base/concepts/formal-vs-functional-competence.md) — Mahowald et al. 2024 distinction; structural knowledge vs. language-in-the-world. (filled 2026-05-29)
- [`base/concepts/constructional-meaning.md`](base/concepts/constructional-meaning.md) — CxG form–meaning pairing; underwrites the `constructional` tag. Grounded in Weissweiler 2023. (filled 2026-05-29)

### Base — sources

- [`base/sources/bender-koller-2020-climbing.md`](base/sources/bender-koller-2020-climbing.md) — Bender & Koller 2020, ACL; form-vs-meaning argument, octopus thought experiment; grounds `grounded` tag. **status: received** (page-level quotes extracted 2026-05-28).
- [`base/sources/lyre-2024-semantic-grounding.md`](base/sources/lyre-2024-semantic-grounding.md) — Lyre 2024, arXiv 2402.10992; grounding-as-gradual, three-dimensional typology (functional/social/causal); grounds `grounded` sub-tags. **status: received** (page-level quotes extracted 2026-05-28).
- [`base/sources/piantadosi-hill-2022-meaning-without-reference.md`](base/sources/piantadosi-hill-2022-meaning-without-reference.md) — Piantadosi & Hill 2022, arXiv 2208.02957; conceptual-role semantics, meaning without reference; grounds `inferential` tag. **status: received** (section-level quotes extracted 2026-05-28).
- [`base/sources/weissweiler-2023-cxg-insight.md`](base/sources/weissweiler-2023-cxg-insight.md) — Weissweiler et al. 2023, GURT; CxG-probing methodology, form–meaning pairing as test criterion; grounds `constructional` tag. **status: received** (section-level quotes extracted 2026-05-28).
- [`base/sources/weissweiler-2022-comparative-correlative.md`](base/sources/weissweiler-2022-comparative-correlative.md) — Weissweiler, Hofmann, Köksal & Schütze 2022, EMNLP; probes BERT/RoBERTa/DeBERTa on the English comparative correlative and finds they **recognise the structure but fail to use its meaning** — a syntax-vs-semantics dissociation. The single-construction empirical precedent the 2023 survey generalizes; the CC is also one of Scivetti 2025's 8 constructions. **status: received** (abstract verbatim from ACL Anthology + 3 section-level body quotes from ar5iv HTML, 2026-05-29).
- [`base/sources/scivetti-2025-beyond-memorization.md`](base/sources/scivetti-2025-beyond-memorization.md) — Scivetti, Tayyar Madabushi et al. 2025, IJCNLP-AACL; CxG inference benchmark over 8 phrasal constructions (incl. caused-motion, conative, way-manner) with human comparison; GPT-o1 drops >40% on syntactically-identical/semantically-divergent forms. Resolves both P2 wants. **status: received** (abstract verbatim from ACL Anthology + 3 section-level body quotes from arXiv v1 HTML, 2026-05-29).
- [`base/sources/mahowald-2024-dissociating.md`](base/sources/mahowald-2024-dissociating.md) — Mahowald et al. 2024, TiCS 28(6); formal-vs-functional competence distinction, neuroscience grounding; primary reference for `functional-vs-formal` tag. **status: received** (section-level quotes extracted 2026-05-28).
- [`base/sources/mahowald-2023-aann-judgments.md`](base/sources/mahowald-2023-aann-judgments.md) — Mahowald 2023, EACL (arXiv 2301.12564); GPT-3 (text-davinci-002) rates the AANN construction; broadly human-like on form, with the author's own caveat that this is "not the same thing as showing that it understands the meaning or function." The argument/findings record (the dataset is the separate stimuli resource); grounds [`claim/formal-competence-aann-ceiling`](findings/claims/formal-competence-aann-ceiling.md). **status: received** (abstract + 3 section-level body quotes verbatim, 2026-05-29).

### Base — resources

- [`base/resources/index.md`](base/resources/index.md) — catalog of human-anchored empirical resources.
- [`base/resources/mahowald-2023-aann-stimuli.md`](base/resources/mahowald-2023-aann-stimuli.md) — Mahowald 2023 EACL AANN stimulus suite + MTurk acceptability ratings (status: external-only); anchor for [`conjecture/aann-construction`](findings/conjectures/aann-construction.md).
- [`base/resources/scivetti-2025-cxnli-dataset.md`](base/resources/scivetti-2025-cxnli-dataset.md) — Scivetti et al. 2025 CxNLI / CxNLI-Distinction constructional NLI dataset (435 + 99 triples over 8 / 5 constructions incl. caused-motion, conative, way-manner; native-speaker baseline ≈0.90 / ≈0.83). Status: external-only (repo not reachable this run). **Candidate** human inference-rate anchor for `caused-motion-anchor`, `conative-anchor`, `way-construction-anchor` — surfaced, not adopted. (created 2026-05-29)

### Base — wants

- [`base/wanted.md`](base/wanted.md) — prioritized fetch list for Tom.

### Findings — conjectures

- [`findings/conjectures/dative-alternation-information-structure.md`](findings/conjectures/dative-alternation-information-structure.md)
- [`findings/conjectures/aann-construction.md`](findings/conjectures/aann-construction.md) — status: designed (2026-05-28)
- [`findings/conjectures/way-construction.md`](findings/conjectures/way-construction.md) — status: designed (2026-05-28); path-traversal (self-motion) inference
- [`findings/conjectures/function-word-substitutability.md`](findings/conjectures/function-word-substitutability.md)
- [`findings/conjectures/caused-motion-construction.md`](findings/conjectures/caused-motion-construction.md) — status: proposed (2026-05-29); transitive causation-of-motion from non-motion verbs; anchor pending (`caused-motion-anchor`)
- [`findings/conjectures/conative-construction.md`](findings/conjectures/conative-construction.md) — status: proposed (2026-05-29); cancellation of the completed-contact entailment (verb held constant); anchor pending (`conative-anchor`)
- [`findings/conjectures/comparative-correlative-construction.md`](findings/conjectures/comparative-correlative-construction.md) — status: proposed (2026-05-29); decoder LLMs use the CC's proportional-covariation meaning, narrowing-but-not-closing the encoder-PLM form/meaning dissociation that [`source/weissweiler-2022-comparative-correlative`](base/sources/weissweiler-2022-comparative-correlative.md) found; the project's first longitudinal (2022 encoders → 2025 decoders) construction conjecture. Anchor pending (`comparative-correlative-anchor`).

### Findings — claims / results / theory / open-questions

- [`findings/claims/formal-competence-aann-ceiling.md`](findings/claims/formal-competence-aann-ceiling.md) — status: proposed (2026-05-28); AANN acceptability ceiling is evidence of formal, not functional, linguistic competence. Grounded by Mahowald 2024 formal/functional distinction; anchored to [`resource/mahowald-2023-aann-stimuli`](base/resources/mahowald-2023-aann-stimuli.md).
- [`findings/claims/constructional-divergent-form-generalization-gap.md`](findings/claims/constructional-divergent-form-generalization-gap.md) — status: proposed (2026-05-29); LLMs track constructional form–meaning pairings "up to a point" but show a >40% generalization gap (GPT-o1) on syntactically-identical / semantically-divergent forms vs. a native-speaker baseline (≈0.90/≈0.83). The project's first claim with in-repo human-comparison empirical bearing. Anchored to [`resource/scivetti-2025-cxnli-dataset`](base/resources/scivetti-2025-cxnli-dataset.md); sits at the theory ladder's Tier 3→4 boundary. `contingent-on: []`.
- [`findings/claims/cxg-probing-surprisal-validity.md`](findings/claims/cxg-probing-surprisal-validity.md) — status: proposed (2026-05-29); surprisal contrast on form–meaning minimal pairs is a valid (but bounded) operationalization of constructional-meaning *sensitivity*. Methodological counterpart to the AANN-ceiling claim. `anchor: pending`, contingent on `cxg-probing-anchor`.
- [`findings/theory/constructional-meaning-in-llms.md`](findings/theory/constructional-meaning-in-llms.md) — status: draft (2026-05-29); the project's first theory page. A five-tier evidence ladder (form-acceptability < surprisal-contrast < gradient semantic tracking < generalization < inference-licensing) placing each existing claim/conjecture; brackets the grounding axis; flags the relational axis as future work.

### Experiments — designs

(Not part of the wiki tree, but indexed here for navigability.)

- [`experiments/designs/aann-construction-v1.md`](../experiments/designs/aann-construction-v1.md) — provisional; contingent on `aann-stimulus-source` and `aann-operationalization`.
- [`experiments/designs/way-construction-v1.md`](../experiments/designs/way-construction-v1.md) — provisional; anchor pending `way-construction-anchor` decision.
- [`experiments/designs/comparative-correlative-v1.md`](../experiments/designs/comparative-correlative-v1.md) — provisional; operationalizes [`conjecture/comparative-correlative-construction`](findings/conjectures/comparative-correlative-construction.md) as a covariation-inference probe (CC-vs-control gap, inverse-CC direction-flip, atypical-pair generalization; both NLI and forced-choice framings). Contingent on `comparative-correlative-anchor` + `constructional-divergence-operationalization`; cost < $1.

### Open questions

- [`findings/open-questions/relational-meaning-pilot.md`](findings/open-questions/relational-meaning-pilot.md) — what minimal two-agent setup constitutes evidence that meaning is being constituted *between* agents rather than computed inside each?
- [`findings/open-questions/constructional-vs-frequency-confound.md`](findings/open-questions/constructional-vs-frequency-confound.md) — status: open (2026-05-29); how to separate constructional-meaning sensitivity from an n-gram/frequency confound in surprisal-contrast probes (form-level).
- [`findings/open-questions/distributional-vs-inferential-constructional.md`](findings/open-questions/distributional-vs-inferential-constructional.md) — status: open (2026-05-29); granting constructional sensitivity, what minimal evidence shows it is inferential-role tracking vs. a distributional shadow (meaning-level; downstream of the frequency question).
- [`findings/open-questions/constructional-divergence-probe.md`](findings/open-questions/constructional-divergence-probe.md) — status: open (2026-05-29); what minimal project-run probe (panel, NLI or surprisal lane, with a memorization control) would convert the external Scivetti divergence gap into a project `result` at the Tier 3→4 boundary. The experimental cash-out of [`claim/constructional-divergent-form-generalization-gap`](findings/claims/constructional-divergent-form-generalization-gap.md); flags an operationalization gate to queue before running.

## How to extend this file

When you add a typed page, add a one-line entry here in the right section. When you retire one, leave the line and append `— retired YYYY-MM-DD`. Do not delete entries; the audit trail matters.
