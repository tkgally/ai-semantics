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

Eight decisions were ratified 2026-05-29 (see *Resolved decisions* below). **Four are now open** (one prior + three opened by the 2026-05-29 probe-run session):

- [`decisions/open/aann-panel-logprob-blocker`](decisions/open/aann-panel-logprob-blocker.md) — **blocks the AANN probe.** Its ratified indicator (continuation-likelihood logprob contrast + `p("good")` fallback) needs token logprobs, but the ratified panel exposes none on OpenRouter (verified 2026-05-29). Substitute the panel (default), the small-model lane, or re-operationalize? Opened 2026-05-29.
- [`decisions/open/relational-anchor-shortlist`](decisions/open/relational-anchor-shortlist.md) — choose the human dyadic-interaction anchor for the relational-meaning pilot (default: Clark & Wilkes-Gibbs 1986, with Pickering & Garrod 2004 as theoretical backdrop). Opened 2026-05-29. *(The broader two-AI relational experiment — "Decision 9" in Tom's walkthrough — has not yet been taken.)*
- [`decisions/open/lexical-sense-gradience-anchor`](decisions/open/lexical-sense-gradience-anchor.md) — anchor for the first lexical conjecture (default: Usim graded usage-similarity + WiC binary cross-check). **Updated 2026-05-29: the requested Usim inspection ran** — scale + counts now verified from primary sources (5-point scale; 34 lemmas / 1530 pairs / 3 annotators), but the released file is **not currently fetchable** (Box 404 / mirror 503) and **no explicit data license** exists. Intellectual fit confirmed; access/licensing is the standing blocker. Still open. Non-blocking (the conjecture is `proposed`).
- [`decisions/open/cc-v2-difficulty-operationalization`](decisions/open/cc-v2-difficulty-operationalization.md) — difficulty axes/thresholds for a harder comparative-correlative v2 (to escape the v1 ceiling). Non-urgent; the v1 result stands on its own. Opened 2026-05-29.

### Resolved decisions
Ratified by Tom 2026-05-29. Ratifying an anchor/operationalization fixes the *yardstick*, not the *result* — the conjectures/designs below remain untested/unrun.
- [`decisions/resolved/aann-stimulus-source`](decisions/resolved/aann-stimulus-source.md) — **Mahowald 2023** is the AANN human anchor.
- [`decisions/resolved/aann-operationalization`](decisions/resolved/aann-operationalization.md) — continuation-likelihood contrast + prompted-acceptability fallback + **T1**; held-out adjectives locked pre-run.
- [`decisions/resolved/caused-motion-anchor`](decisions/resolved/caused-motion-anchor.md) — anchored to the **Scivetti CxNLI** dataset.
- [`decisions/resolved/conative-anchor`](decisions/resolved/conative-anchor.md) — anchored to the **Scivetti CxNLI** dataset.
- [`decisions/resolved/way-construction-anchor`](decisions/resolved/way-construction-anchor.md) — anchored to the **Scivetti CxNLI** dataset.
- [`decisions/resolved/comparative-correlative-anchor`](decisions/resolved/comparative-correlative-anchor.md) — anchored to the **Scivetti CxNLI** CC subset.
- [`decisions/resolved/cxg-probing-anchor`](decisions/resolved/cxg-probing-anchor.md) — **Option A**: claim stays AANN-scoped; cross-construction generality stays provisional.
- [`decisions/resolved/constructional-divergence-operationalization`](decisions/resolved/constructional-divergence-operationalization.md) — default: both instruments + 30/70/15-pp thresholds, frozen pre-run.

  *The four Scivetti-anchored decisions were ratified together as one bundle after the de-anonymized dataset repo ([github.com/melissatorgbi/beyond-memorization](https://github.com/melissatorgbi/beyond-memorization)) was inspected and confirmed to carry per-item construction labels + a single gold answer per item.*

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
- [`base/resources/wic-graded-usage-similarity.md`](base/resources/wic-graded-usage-similarity.md) — Usim graded usage-similarity ratings (Erk, McCarthy & Gaylord 2009/2013) — graded 5-point human usage-similarity judgments; the candidate gradience anchor for [`conjecture/lexical-sense-gradience`](findings/conjectures/lexical-sense-gradience.md), with WiC (Pilehvar & Camacho-Collados 2019, binary, CC BY-NC 4.0) as the binary cross-check. Status: external-only (license/counts unverified this run — see page). (created 2026-05-29)
- [`base/resources/scivetti-2025-cxnli-dataset.md`](base/resources/scivetti-2025-cxnli-dataset.md) — Scivetti et al. 2025 CxNLI / CxNLI-Distinction constructional NLI dataset (435 + 99 triples over 8 / 5 constructions; native-speaker baseline ≈0.90 / ≈0.83). Status: partial (de-anonymized repo inspected 2026-05-29: per-item construction labels + single gold answer per item). **Ratified anchor (2026-05-29)** for the caused-motion, conative, way, and comparative-correlative conjectures — answer-key + aggregate baseline. (created 2026-05-29)

### Base — wants

- [`base/wanted.md`](base/wanted.md) — prioritized fetch list for Tom.

### Findings — conjectures

- [`findings/conjectures/dative-alternation-information-structure.md`](findings/conjectures/dative-alternation-information-structure.md)
- [`findings/conjectures/aann-construction.md`](findings/conjectures/aann-construction.md) — status: designed (2026-05-28)
- [`findings/conjectures/way-construction.md`](findings/conjectures/way-construction.md) — status: **tested** (2026-05-29); path-traversal (self-motion) inference from non-motion verbs. **Probed this session** → [`result/way-construction-traversal-v1`](findings/results/way-construction-traversal-v1.md): confirmed above the ratified bar (way 77.8–100%, gap 77.7–100 pp, 3/3 models, both instruments; anti-motion guard holds; idiomatic guard 0%). gpt-5.4-mini the conservative outlier (4–5 scattered non-affirms). Anchored to the Scivetti way-manner subset (`way-construction-anchor`, ratified).
- [`findings/conjectures/function-word-substitutability.md`](findings/conjectures/function-word-substitutability.md)
- [`findings/conjectures/caused-motion-construction.md`](findings/conjectures/caused-motion-construction.md) — status: **tested** (2026-05-29); transitive causation-of-motion from non-motion verbs. **Probed this session** → [`result/caused-motion-minimal-pair-divergence-v1`](findings/results/caused-motion-minimal-pair-divergence-v1.md): confirmed **at ceiling** (cm 90–100%, gap 70–100 pp, 3/3 models, atypical-robust; causation-specific control passed). Lead caveat: ceiling on easy controls. Anchored to the Scivetti caused-motion subset (`caused-motion-anchor`, ratified).
- [`findings/conjectures/conative-construction.md`](findings/conjectures/conative-construction.md) — status: **tested** (2026-05-29); cancellation of the completed-contact entailment (verb held constant). **Probed this session** → [`result/conative-minimal-pair-divergence-v1`](findings/results/conative-minimal-pair-divergence-v1.md): P1 confirmed at the ratified bar (forced-choice gap 42–88 pp 3/3 models; NLI 54–67 pp 2/3), P2/P3 supported; standing caveat = gpt-5.4-mini fails under NLI but recovers under forced-choice. Anchored to the Scivetti conative subset (`conative-anchor`, ratified).
- [`findings/conjectures/comparative-correlative-construction.md`](findings/conjectures/comparative-correlative-construction.md) — status: **tested** (2026-05-29); decoder LLMs use the CC's proportional-covariation meaning. **Probed this session** → [`result/comparative-correlative-covariation-v1`](findings/results/comparative-correlative-covariation-v1.md): the "use" core is supported at ceiling; the "narrows-but-not-closes" clause is *not* supported by the v1 instrument (panel matched the human baseline). Anchored to the Scivetti CC subset (`comparative-correlative-anchor`, ratified).
- [`findings/conjectures/lexical-sense-gradience.md`](findings/conjectures/lexical-sense-gradience.md) — status: proposed (2026-05-29); the project's **first lexical (non-grammatical) conjecture**. LLM same/different-sense behavior is monotonic in human-rated usage similarity, with an intermediate regime for polysemy absent for homonymy, separable from a context-similarity (`distributional`) shadow. Sharpens [`open-question/lexical-polysemy-gradience`](findings/open-questions/lexical-polysemy-gradience.md). Candidate anchor: Usim graded usage-similarity (`external-only`); `contingent-on: lexical-sense-gradience-anchor` (open).

### Findings — claims / results / theory / open-questions

- [`findings/claims/formal-competence-aann-ceiling.md`](findings/claims/formal-competence-aann-ceiling.md) — status: proposed (2026-05-28); AANN acceptability ceiling is evidence of formal, not functional, linguistic competence. Grounded by Mahowald 2024 formal/functional distinction; anchored to [`resource/mahowald-2023-aann-stimuli`](base/resources/mahowald-2023-aann-stimuli.md).
- [`findings/claims/constructional-divergent-form-generalization-gap.md`](findings/claims/constructional-divergent-form-generalization-gap.md) — status: proposed (2026-05-29); LLMs track constructional form–meaning pairings "up to a point" but show a >40% generalization gap (GPT-o1) on syntactically-identical / semantically-divergent forms vs. a native-speaker baseline (≈0.90/≈0.83). The project's first claim with in-repo human-comparison empirical bearing. Anchored to [`resource/scivetti-2025-cxnli-dataset`](base/resources/scivetti-2025-cxnli-dataset.md); sits at the theory ladder's Tier 3→4 boundary. `contingent-on: []`.
- [`findings/claims/cxg-probing-surprisal-validity.md`](findings/claims/cxg-probing-surprisal-validity.md) — status: proposed (2026-05-29); surprisal contrast on form–meaning minimal pairs is a valid (but bounded) operationalization of constructional-meaning *sensitivity*. Methodological counterpart to the AANN-ceiling claim. Anchored to `resource/mahowald-2023-aann-stimuli` (AANN-scoped); cross-construction generality stays provisional (`cxg-probing-anchor` resolved 2026-05-29, Option A).
- [`findings/theory/constructional-meaning-in-llms.md`](findings/theory/constructional-meaning-in-llms.md) — status: draft (updated 2026-05-29); the project's first theory page. A five-tier evidence ladder (form-acceptability < surprisal-contrast < gradient semantic tracking < generalization < inference-licensing) placing each claim/conjecture/result; brackets the grounding axis; flags the relational axis as future work. Revised to absorb the first own-design probe result (CC) at Tier 4.

### Findings — results

- [`findings/results/way-construction-traversal-v1.md`](findings/results/way-construction-traversal-v1.md) — status: proposed (2026-05-29); **the project's own way-construction minimal-pair probe** (the third own-design argument-structure probe; does the construction *add* a self-motion / path-traversal entailment onto non-motion verbs — *whistled his way down the hall*?). **Confirmed above the ratified bar**: affirm-path-traversal rate 77.8–100%, gap (way − location control) 77.7–100 pp, 3/3 models, both instruments; the anti-motion verb-reading guard holds at/near ceiling; the idiomatic over-generalization guard is at 0% and the ctrl-motion positive floor at 100%. gpt-5.4-mini is the conservative outlier (declines 4–5 scattered items *hum/eat/chat/snack* as "may or may not have moved" — a cautious entailment bar, not verb-reading failure; it affirms the anti-motion items at 100%). Patterns with caused-motion (the "add" direction is easy). Lead caveat: ceiling on relatively easy controls. Anchored to [`resource/scivetti-2025-cxnli-dataset`](base/resources/scivetti-2025-cxnli-dataset.md); `contingent-on: []`. Cost $0.072. (0 NA / 360 calls.)
- [`findings/results/comparative-correlative-covariation-v1.md`](findings/results/comparative-correlative-covariation-v1.md) — status: proposed (2026-05-29); **the project's first probe of its own design to run** (charter §5.4). The 2026 decoder panel deploys the comparative correlative's covariation meaning at ceiling — construction-driven (T1 +80–90pp over matched controls), direction-tracking (T2 inverse-flip 95–100%), n-gram-robust (T3 no atypical collapse) — matching the Scivetti ≈0.90 human baseline (93–100%). A *positive* Tier-4 result that **overshoots** the conjecture's "narrows-but-not-closes" bet (the Weissweiler-2022 encoder form/meaning dissociation is not reproduced by this instrument). Lead caveat: ceiling on an easy instrument is weak evidence for the strong reading; harder v2 queued. Anchored to [`resource/scivetti-2025-cxnli-dataset`](base/resources/scivetti-2025-cxnli-dataset.md); `contingent-on: []`. Cost $0.12.
- [`findings/results/caused-motion-minimal-pair-divergence-v1.md`](findings/results/caused-motion-minimal-pair-divergence-v1.md) — status: proposed (2026-05-29); **the project's own caused-motion minimal-pair probe** (the converse of conative: does the construction *add* a causation-of-motion entailment onto non-motion verbs?). **Confirmed at ceiling**: affirm-caused-motion rate 90–100%, gap 70–100 pp over controls, 3/3 models, both instruments, robust to atypical/low-frequency verbs (P3); the causation-specific control (object moves by *another* cause) is correctly withheld (0–20%) — genuine causal attribution, not motion detection. Asymmetry: *adding* an entailment is easy (ceiling) where *cancelling* one (conative) was harder. Lead caveat: ceiling on relatively easy controls. `contingent-on: []`. Cost $0.044. (0 NA / 180 calls.)
- [`findings/results/conative-minimal-pair-divergence-v1.md`](findings/results/conative-minimal-pair-divergence-v1.md) — status: proposed (2026-05-29); **the project's own verb-held-constant conative minimal-pair probe** (the cleaner follow-up to the distinction probe's "conative collapses hardest"). Affirm-completed-contact gap (transitive − conative): **forced-choice 42–88 pp in 3/3 models; NLI 54–67 pp in 2/3**, replicating across verbs, persisting on low-frequency objects (P3) and construction-specific (P2). Discriminating wrinkle: **gpt-5.4-mini fails the conative under NLI** (calls *kicked at the ball* an entailment of contact) but recovers under forced-choice — instrument-fragility. **Refines** [`result/cxnli-distinction-divergence-v1`](findings/results/cxnli-distinction-divergence-v1.md) (the clean minimal pair shows more conative competence than Scivetti's adversarial distinction items). `contingent-on: []`. Cost $0.071. (0 NA / 336 calls.)
- [`findings/results/cxnli-distinction-divergence-v1.md`](findings/results/cxnli-distinction-divergence-v1.md) — status: proposed (2026-05-29); **project-run replication of the Scivetti divergent-form gap** (the cash-out of [`open-question/constructional-divergence-probe`](findings/open-questions/constructional-divergence-probe.md)). Panel-as-subjects on Scivetti's base (Exp1) vs. distinction (Exp2) NLI items, 5 argument-structure constructions: base 84–96% (≈ human ≈0.90) but distinction 39–64% (well below human ≈0.83) — a **30–45 pp drop (mean ≈39), convergent across all 3 models, conative hardest (55–75 pp)**. The *discriminating* (off-ceiling) negative complement to the CC ceiling positive. Supports [`claim/constructional-divergent-form-generalization-gap`](findings/claims/constructional-divergent-form-generalization-gap.md) with the project's own evidence. `contingent-on: []`. Cost $0.16. (0 NA / 600 calls.)

### Experiments — designs

(Not part of the wiki tree, but indexed here for navigability.)

- [`experiments/designs/aann-construction-v1.md`](../experiments/designs/aann-construction-v1.md) — provisional; contingent on `aann-stimulus-source` and `aann-operationalization`.
- [`experiments/designs/way-construction-v1.md`](../experiments/designs/way-construction-v1.md) — **RUN 2026-05-29** → [`result/way-construction-traversal-v1`](findings/results/way-construction-traversal-v1.md). The project's own way-construction minimal pairs (18 non-motion verbs × {way, ctrl-loc, ctrl-motion} + 6 idiomatic guards); the design's logprob indicator was unavailable on OpenRouter, so its ratified greedy-completion fallback (NLI + forced-choice) was used — the ratified divergence operationalization (no new decision). Cost $0.072.
- [`experiments/designs/comparative-correlative-v1.md`](../experiments/designs/comparative-correlative-v1.md) — **RUN 2026-05-29** → [`result/comparative-correlative-covariation-v1`](findings/results/comparative-correlative-covariation-v1.md). Operationalized the CC conjecture as a covariation-inference probe (CC-vs-control gap, inverse-CC direction-flip, atypical-pair generalization; NLI + forced-choice). Both governing decisions ratified; cost $0.12.
- [`experiments/designs/comparative-correlative-v2.md`](../experiments/designs/comparative-correlative-v2.md) — provisional; a *harder* follow-up to escape the v1 ceiling (conflicting-cue CC, multi-step composition, near-miss controls, graded difficulty ladder). Contingent on `cc-v2-difficulty-operationalization` (open); unrun.
- [`experiments/designs/conative-construction-v1.md`](../experiments/designs/conative-construction-v1.md) — **RUN 2026-05-29** → [`result/conative-minimal-pair-divergence-v1`](findings/results/conative-minimal-pair-divergence-v1.md). The project's own verb-held-constant conative minimal pairs (12 Levin conative-class verbs × typical/atypical × transitive/conative + 4 control verbs); reuses the ratified divergence operationalization (no new decision). Cost $0.071.
- [`experiments/designs/caused-motion-construction-v1.md`](../experiments/designs/caused-motion-construction-v1.md) — **RUN 2026-05-29** → [`result/caused-motion-minimal-pair-divergence-v1`](findings/results/caused-motion-minimal-pair-divergence-v1.md). The project's own caused-motion stimuli (10 non-motion verbs × cm/ctrl-loc/ctrl-sep); reuses the ratified divergence operationalization (no new decision). Cost $0.044.

### Experiments — run records

- [`experiments/runs/2026-05-29-way-construction-probe-v1/`](../experiments/runs/2026-05-29-way-construction-probe-v1/README.md) — way-construction minimal-pair probe, own stimuli (→ result/way-construction-traversal-v1).
- [`experiments/runs/2026-05-29-comparative-correlative-probe-v1/`](../experiments/runs/2026-05-29-comparative-correlative-probe-v1/README.md) — CC covariation probe (→ result/comparative-correlative-covariation-v1).
- [`experiments/runs/2026-05-29-cxnli-distinction-probe-v1/`](../experiments/runs/2026-05-29-cxnli-distinction-probe-v1/README.md) — CxNLI base-vs-distinction probe (→ result/cxnli-distinction-divergence-v1).
- [`experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/`](../experiments/runs/2026-05-29-conative-minimal-pair-probe-v1/README.md) — conative minimal-pair probe, own stimuli (→ result/conative-minimal-pair-divergence-v1).
- [`experiments/runs/2026-05-29-caused-motion-minimal-pair-probe-v1/`](../experiments/runs/2026-05-29-caused-motion-minimal-pair-probe-v1/README.md) — caused-motion minimal-pair probe, own stimuli (→ result/caused-motion-minimal-pair-divergence-v1).
- `experiments/runs/2026-05-28-panel-calibration/` — bootstrap liveness probe.

### Open questions

- [`findings/open-questions/relational-meaning-pilot.md`](findings/open-questions/relational-meaning-pilot.md) — what minimal two-agent setup constitutes evidence that meaning is being constituted *between* agents rather than computed inside each?
- [`findings/open-questions/constructional-vs-frequency-confound.md`](findings/open-questions/constructional-vs-frequency-confound.md) — status: open (2026-05-29); how to separate constructional-meaning sensitivity from an n-gram/frequency confound in surprisal-contrast probes (form-level).
- [`findings/open-questions/distributional-vs-inferential-constructional.md`](findings/open-questions/distributional-vs-inferential-constructional.md) — status: open (2026-05-29); granting constructional sensitivity, what minimal evidence shows it is inferential-role tracking vs. a distributional shadow (meaning-level; downstream of the frequency question).
- [`findings/open-questions/lexical-polysemy-gradience.md`](findings/open-questions/lexical-polysemy-gradience.md) — status: open (2026-05-29); the project's first **lexical** (non-grammatical) wedge: does LLM in-context sense behavior reproduce the graded polysemy lexicographers document, or collapse to discrete senses — separable from a context-similarity (`distributional`) shadow? Candidate anchors: WiC / graded usage-similarity / WordNet-SemCor (none in-repo yet; no decision opened).
- [`findings/open-questions/constructional-divergence-probe.md`](findings/open-questions/constructional-divergence-probe.md) — status: **answered** (2026-05-29) → [`result/cxnli-distinction-divergence-v1`](findings/results/cxnli-distinction-divergence-v1.md). The minimal project-run probe it called for was built and run (panel-as-subjects on Scivetti base vs. distinction); the divergence gap reproduced. Its named follow-up — the project's *own* minimal-pair conative probe with a memorization/frequency arm — was **also built and run this session** → [`result/conative-minimal-pair-divergence-v1`](findings/results/conative-minimal-pair-divergence-v1.md) (which *refines* the distinction collapse: clean minimal pairs show more conative competence than the adversarial distinction items).

## How to extend this file

When you add a typed page, add a one-line entry here in the right section. When you retire one, leave the line and append `— retired YYYY-MM-DD`. Do not delete entries; the audit trail matters.
