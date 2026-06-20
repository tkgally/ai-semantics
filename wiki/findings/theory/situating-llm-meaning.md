---
type: theory
id: situating-llm-meaning
title: Situating the project's findings on a philosophical map of meaning — where (if anywhere) LLM "meaning" lives
meaning-senses:
  - distributional
  - inferential
  - referential
  - grounded
  - constructional
  - relational
  - functional-vs-formal
status: draft
contingent-on: []
created: 2026-05-31
updated: 2026-06-20
links:
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/truth-conditional-and-use-meaning
  - rel: depends-on
    target: concept/compositionality
  - rel: depends-on
    target: concept/frame-and-prototype-semantics
  - rel: depends-on
    target: concept/semantic-holism
  - rel: depends-on
    target: concept/deflationary-and-eliminativist-llm-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: result/relational-history-perturbation-v4
  - rel: depends-on
    target: result/relational-spontaneous-recency-a
  - rel: depends-on
    target: result/relational-implicit-reassignment-control
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: depends-on
    target: result/relational-order-composition-c-altpair
  - rel: depends-on
    target: essay/output-channel-confound
  - rel: contradicts
    target: conjecture/commutative-convention
  - rel: depends-on
    target: essay/conversation-as-text-not-timeline
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v3
  - rel: depends-on
    target: result/comparative-correlative-covariation-v2
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: result/cross-axis-lexical-constructional-ordering-v1
  - rel: depends-on
    target: source/lyre-2024-semantic-grounding
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: result/dative-information-structure-v1
  - rel: depends-on
    target: result/dative-information-structure-v2
  - rel: depends-on
    target: conjecture/dative-alternation-information-structure
  - rel: depends-on
    target: essay/concordant-verdict-hides-spread
  - rel: depends-on
    target: resource/languageR-dative-corpus
---

# Theory (draft): situating the project's findings on a philosophical map of meaning

## What this page is, and is not

The project now has two empirical theory pages — the grammatical [`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md) (the evidence ladder) and the [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md) (the two wedges as one cline) — and, as of this session, a concept layer that writes up the **classical positions** on meaning the project engages: truth-conditional vs use ([`concept/truth-conditional-and-use-meaning`](../../base/concepts/truth-conditional-and-use-meaning.md)), compositionality ([`concept/compositionality`](../../base/concepts/compositionality.md)), frame and prototype semantics ([`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md)), holism ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)), internalism/externalism (in the deepened [`concept/referential-meaning`](../../base/concepts/referential-meaning.md)), the two inferentialisms (in the deepened [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)), and the eliminativist→deflationary→descriptivist spectrum ([`concept/deflationary-and-eliminativist-llm-meaning`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md)).

This page does the one thing those pages individually do not: it **positions the project's own empirical findings on the philosophical map** and asks what they **jointly** imply for *where, if anywhere, LLM "meaning" lives*. It is the synthesis the session's steer calls for.

Two disciplines bind it, hard:

1. **It claims a *positioning*, not new data.** The fixed points are the findings (cited with their verified numbers and their own caveats); the map and the placements are **interpretation**. Every "supports / strains / is silent on" below is a reading, flagged as such — not a result. The charter's "describe, don't litigate" stance ([`PROJECT.md`](../../../PROJECT.md) §1) means this page describes *where the evidence sits*; it does not adjudicate whether LLMs "really" mean.
2. **It under-claims by construction.** The findings are single-panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`), mostly small-N, mostly text-only, several internal-contrast-only, two of the four axes carrying only nulls. A philosophical map drawn over that evidence is a **provisional sketch**, not a settled location. Where a cell is empty or negative, the honest entry is "silent" or "bounded negative," never "refuted."

## The fixed points: the project's findings in one view

Four investigative axes, compressed to their load-bearing result (each links to the page that states it with full caveats):

- **Grammatical (constructional) — the evidence ladder, a dozen-plus own-design results.** Decoders reach the top text-internal rung (inference-licensing) for the **add** direction at or near ceiling (caused-motion 90–100%; *way* 77.8–100%) and **compose** construction meaning — the comparative correlative composes two-step covariation including the diagnostic negative×negative=positive case a single-clause heuristic fails ([`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md)). But the **cancel** direction (suppressing a lexical default) is harder and instrument-fragile, the **divergent-form** generalization fails (the Tier 3→4 gap), and the add-direction "withholding" turned out to be explicit-outcome parsing, not world-model integration. Reached the top rung; bounded there. **Newest fixed point — the dative alternation:** the project's first human-anchored Tier-2 grammatical positive of its own design — the more capable decoders track the information-structure constraint (given-before-new) in the human-corpus production direction on a length/animacy-matched within-item shift ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)), a *thin gradient preference* (not inference-licensing) that **replicated to 2/3** on a disjoint item set with a *widening* order-of-magnitude effect-size spread ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md)).
- **Lexical — sense gradience, a clean positive.** The panel's graded sense-relatedness rating tracks the human DURel median (Spearman **0.60–0.83**, in or above the human inter-annotator range ~0.69) and **survives** a context-similarity control ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)) — it beats the distributional shadow. The *distinctive* discrete-regime bet (polysemy vs homonymy as a separate switch) is a **powered null** ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)): no separation beyond plain graded distance.
- **Grounding (multimodal) — two bounded negatives.** Perceptual groundedness does not predict text-only sense-tracking (underpowered null), and showing the depicting image does not improve sense separation for clear homonyms because the text-only panel already separates them perfectly (AUC = 1.000 — a redundancy null, [`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)).
- **Relational — a bounded null, now bounded again by a first positive.** Homogeneous LLM dyads coordinate and reuse a coined convention, but in the v1 setting the convention is recovered from the content-*set* of prior turns, not their ordered trajectory (history lift +0.25…+0.42; ordered − shuffled +0.06…+0.11, no CI excludes 0) — coordination, not constitution ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md)). A later, decisive test (Option A: physical position neutralized by balanced rotation, order made the *sole* disambiguator) reverses the picture **where order disambiguates**: when a coined term is reassigned across stamped rounds so the content-set is symmetric, both `claude-sonnet-4.6` and `gemini-3.5-flash` recover the term by its most-recent binding **spontaneously and at ceiling** (SPONT latest-binding rate 1.000, Wilson [0.926, 1.000], physical-position at chance) — **order-sensitive / non-commutative** ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md); [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)). So the convention is non-commutative where order disambiguates and commutative where it does not: commutativity is **operationalization-dependent**, and the order-sensitivity is **thin** (latest-binding-wins), not constitution.
- **Cross-axis — the competences dissociate.** Lexical and grammatical skill transfer as *failure* (the weakest lexical tracker is the most fragile grammatically) but not as *strength*, and the same-instrument coercion bridge inverts the lexical order ([`result/cross-axis-lexical-constructional-ordering-v1`](../results/cross-axis-lexical-constructional-ordering-v1.md); n=3 models — orderings, not a coefficient).

## The map: the questions the classical positions answer

The positions the project now catalogs sort along a small number of axes. The map is these axes; the project's findings are points to be located on them.

| Axis (concept page) | One pole | Other pole |
|---|---|---|
| **What meaning ultimately is** ([`truth-conditional-and-use`](../../base/concepts/truth-conditional-and-use-meaning.md)) | a world-relation (truth-conditions, reference) | a role in use (language-games, family resemblance) |
| **What fixes content** ([`distributional`](../../base/concepts/distributional-meaning.md) / [`inferential`](../../base/concepts/inferential-meaning.md)) | co-occurrence structure | inferential role (thin internalist ↔ thick Brandomian-normative) |
| **Where content is fixed** ([`referential`](../../base/concepts/referential-meaning.md)) | inside the head (internalism / narrow content) | partly outside (externalism / reference) |
| **How content is structured** ([`compositionality`](../../base/concepts/compositionality.md) / [`frame-and-prototype`](../../base/concepts/frame-and-prototype-semantics.md)) | compositional, classical categories | constructional/frame-relative, graded/prototype |
| **How content is individuated** ([`semantic-holism`](../../base/concepts/semantic-holism.md)) | atomism / molecularism | holism (the whole web) |
| **Where LLM meaning would live** ([`relational`](../../base/concepts/relational-meaning.md)) | model-internal | constituted between agents |
| **Whether there is anything to describe** ([`deflationary-and-eliminativist`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md)) | eliminativism (no meaning) → deflationism (just distributional) | descriptivism → inflationism (genuine meaning) |

## The positioning: support / strain / silence, position by position

Each entry states the bearing as **interpretation**, names the finding that carries it, and flags what it does *not* show.

**Use over truth-conditional (at the lexical grain) — supported; truth-conditional LLM meaning is silent.** The lexical gradience positive — senses tracked as a graded, shade-into-each-other relatedness rather than a discrete inventory, with the discreteness bet a powered null — fits a **meaning-as-use / family-resemblance** picture better than a discrete truth-conditional sense inventory ([`concept/truth-conditional-and-use-meaning`](../../base/concepts/truth-conditional-and-use-meaning.md)). And the project's *method* is itself a use-theoretic bet: it reads meaning off patterns of use because it has no access to a verified truth-condition/world relation for a model. But that same gap makes the **truth-conditional pole silent**, not refuted: there is no in-repo resource that anchors reference or truth-conditions for an LLM, and (per the deepened [`concept/referential-meaning`](../../base/concepts/referential-meaning.md)) that gap is *structural*. The polysemy/homonymy null cannot separate "graded distance" from "a discrete boundary," so it strains the *discrete-senses* reading without touching the strongest truth-conditional claim.

**The dative sharpens the use-over-truth-conditional reading at the *grammatical* grain — and is the map's first human-anchored Tier-2 own-design grammatical positive.** The dative alternation is an unusually clean case for this cell: the two alternants (*gave John the book* / *gave the book to John*) are **truth-conditionally identical** — same event, same participants — so a model that shifts its preference by what is discourse-*given* is tracking a pure **information-packaging / use** distinction that makes *no* truth-conditional difference ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)). Where the lexical gradience positive *strains* the discrete truth-conditional reading, the dative *dissociates* use from truth-conditions **by construction** (length and animacy held identical across the within-item shift) and finds the panel on the use side. Two disciplines bound the placement, hard: (i) it is **direction-human-anchored only** — the corpus ([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md), Bresnan et al. 2007) fixes the human *production direction* (given recipient → double-object), not a magnitude or a per-item human judgment, so it is the first grammatical cell on this map to rest on independent human data of its own rather than an internal contrast — a real but *narrow* relaxation of discipline-2's "several internal-contrast-only" caveat, at one cell and on the direction axis alone; and (ii) it is **thin** — a gradient *preference*, explicitly not the inference-licensing (Tier-4) rung — so it bears on *use-vs-truth-conditional* and on graded/prototype structure, **not** on the thin-vs-thick *inferential* axis (it adds no entailment the lexical parts cannot supply). And it **replicated to 2/3** on a disjoint item set with the cross-model magnitude spread *widening* (gemini ≫ claude ≫ gpt; gpt's v1 pass did not replicate) — itself a working instance of discipline 2, do not flatten the panel ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md); the carry-the-spread reading discipline of [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)).

**Thin inferential / conceptual role over pure distributionalism — supported; thick (Brandomian) inferentialism — strained.** The project beats the distributional shadow on **both** grains (the gradience positive survives a context-similarity control; the CC composes beyond a single-clause heuristic). That is behavioral support for an **inferential / conceptual-role** upgrade over bare distributional mimicry — the [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) reading. But the deepened inferential page draws the sharp line: what the Tier-4 results index is a **thin, NLI-style inferential role** (inference-*preservation*), itself instrument-fragile (gpt-5.4-mini fails the conative under NLI, recovers under forced-choice) — **not** Brandom's normative-social *articulation* of content. So the support is for the *internalist, causal-functional* conceptual role (Piantadosi & Hill's), and it is friction *against* the thick normative kind. The distributional null is never fully escaped: a deflationist reads even the positives as "richer distributional structure," and behavioral evidence cannot close that off.

**Compositionality — supported at the construction grain (CxG-enlarged); strict lexical compositionality strained; cross-modal composition is an external negative.** The CC's multi-step composition (including negative×negative=positive) is the project's cleanest evidence for genuine **compositional** processing rather than a clause-level heuristic ([`concept/compositionality`](../../base/concepts/compositionality.md)). Coercion shows the relevant "parts" include *constructions*, not just lexemes — strict lexical compositionality under-predicts, and the construction supplies what the verb cannot. The contrast case is external and discriminative (the VLM bag-of-words failure on Winoground/ARO), so it is a flag, not a like-for-like result: text decoders compose where those benchmarks show VLMs do not.

**Frame / prototype category structure — behaviorally supported; representationally silent.** The graded gradience positive is exactly what prototype / graded-category structure predicts, and a graded human resource (DWUG) is itself a prototype-structure instrument ([`concept/frame-and-prototype-semantics`](../../base/concepts/frame-and-prototype-semantics.md)). But "graded *behavior*" does not establish "prototype *representation*" — it may be graded distributional similarity, the standing distributional-null question. Supported as a description of behavior; silent on the underlying representation.

**Holism — the project's own positives inherit its objection; the dissociation is a mild strain on its strongest form.** Distributional models are holistic by construction, and the conceptual-role reading the project's positives support is explicitly holist ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)). So the project's pro-meaning evidence **inherits the holism objection** (no two webs share content exactly), which the project cannot dissolve. The cross-axis **dissociation** (lexical and grammatical competences come apart at the model level) is a *mild* strain on the strongest "one entangled content store" holism — read as "behavioral competences are at least partly separable," n=3, orderings not a coefficient. Cross-model convergence in the relational pilot actually *fits* a shared-substrate holism rather than counting against it.

**Internalism over externalism (as a description) — the LLM is a clean narrow case; externalist reference is silent/un-probeable.** The LLM has only narrow access by construction; the grounding nulls show the *external* perceptual channel adds nothing measurable where text already saturates ([`concept/referential-meaning`](../../base/concepts/referential-meaning.md), deepened). This is consistent with describing the model in **narrow-content / internalist** terms — but it leaves **externalist reference untouched**: not refuted, structurally un-probeable (there is no "Twin Earth" to move a text model to). The strongest in-principle "no reference" case (Bender & Koller's missing form-to-world relation) stands as a boundary the project records, not crosses.

**Grounded — two bounded negatives; the contribution is confined to a residual the probes have not entered.** The grounding axis is, so far, a pair of nulls *for clear homonyms* ([`concept/grounding`](../../base/concepts/grounding.md)). On Lyre's gradual framing — that grounding "isn't a yes-no matter, but rather a matter of degree" ([`source/lyre-2024-semantic-grounding`](../../base/sources/lyre-2024-semantic-grounding.md), p. 10) — the project's contribution is to show the *degree* added by a picture is ≈0 exactly where text saturates, and to conjecture (not show) that it could be positive in the under-determined residual.

**Relational constitution — still negative on constitution, but the commutative reading is now falsified where order disambiguates; order-sensitive-but-thin.** The charter's most distinctive hope — meaning constituted *between* agents — is **still not seen**: the order-sensitivity the decisive test found is **thin** (a latest-binding-wins / convention-update rule, the bottom rung), **not** a convention *constituted between* agents through the live trajectory ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md)), so the relational cell stays **negative on constitution**. What has changed is the *form* of the negative. The clean order-free "bag of turns" reading the v1 null first suggested is now **falsified where order disambiguates**: with physical position neutralized by balanced rotation and order made the sole disambiguator, both models recover a reassigned term by its most-recent binding spontaneously at ceiling — they are **order-sensitive (non-commutative)**, not the order-free aggregator ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md); [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)). This also **scopes** the earlier "layout, not timeline" framing from [`result/relational-history-perturbation-v4`](../results/relational-history-perturbation-v4.md) ([`essay/conversation-as-text-not-timeline`](../essays/conversation-as-text-not-timeline.md)): position-following held where physical text-position was available and order carried no extra disambiguating signal; where position is neutralized and order is the sole cue, the models track the stamped recency. And v4's binding "position-following indistinguishable from stamp-blindness" caveat is now **resolved** — the staged Option B gate showed both models read the stamp on demand ([`result/relational-stamp-comprehension-b`](../results/relational-stamp-comprehension-b.md)), so the v4 behaviour was comprehending-but-not-spontaneously-using, not stamp-blindness. Net: the relational verdict is no longer a *clean commutative aggregation null* but **order-sensitive but thin** — non-commutative latest-wins, still short of constitution; `internal-contrast-only`; no human comparison.

A **stricter** form of thin order-sensitivity has since been mapped, and it sharpens the same verdict rather than changing the cell. Order-sensitive **composition** of two genuinely *non-commuting* moves (the relational ladder's order-sensitive rung in [`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md)) was first read as a one-model capability (only claude composed under a forced single-token format), but once a **working surface** is permitted — step-by-step output allowed, reasoning-effort held constant — all three panel models order the moves by their round stamps at/near ceiling, and this replicates across **three** generality axes — a genuinely different non-commuting operation pair (CYCLE/SWAP, generating A4, vs. the original STEP/FLIP, D4), a larger grid (K=6, D6), and a **deeper composition of three non-commuting moves** ([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md); [`result/relational-order-composition-c-altpair`](../results/relational-order-composition-c-altpair.md); [`result/relational-order-composition-c-k6`](../results/relational-order-composition-c-k6.md); [`result/relational-order-composition-three-move`](../results/relational-order-composition-three-move.md)). So spontaneous order-sensitive composition is a panel-wide **capacity** across operation pair, grid size, and depth, *working-surface-relative* (the forced-format split was an output-channel artifact, [`essay/output-channel-confound`](../essays/output-channel-confound.md), not a capability split; the deeper-composition run also returned the essay's trigger-(b) "survives a widened channel" contrast **negative** — the wide channel absorbed the deeper serial load). This is a *stricter* thin rung than latest-binding-wins — but it is **still thin and still negative on constitution**: the stamped move-list sits inert in the record, so the ordering is single-reader-recoverable, and the rich side (rung (iii), path-dependence proper) stays **documented structurally closed for text-only stimuli**. The relational cell's location is therefore unchanged — order-sensitive but thin, short of constitution — with the panel now occupying a stricter rung within the thin region.

**Eliminativism strained; deflationism fits; descriptivism vindicated.** The positives (gradience beating its shadow; CC composing) are hard to square with a strict "stochastic parrot" eliminativism — there *is* structure that beats the named null. But they do **not refute deflationism** ("still just distributional, only richer"), and behavioral evidence never can (the Bender & Koller in-principle gap). The project's **descriptivism** — neither eliminativist nor inflationary — is the stance the evidence vindicates: the yes/no question is under-determined by exactly the evidence the project can obtain, so describing the structure is the right move ([`concept/deflationary-and-eliminativist-llm-meaning`](../../base/concepts/deflationary-and-eliminativist-llm-meaning.md)).

## The synthesis verdict: where LLM "meaning" lives, on current evidence

Pulling the cells together, the project's findings jointly locate LLM "meaning" — to the extent the term applies at all — as **model-internal, thin-inferential, use-based, graded, narrow, and compositional at the construction grain**, and as **not (on current evidence) referential, not perceptually grounded, not relationally constituted, and not thickly inferential.** Said as one sentence and meant as a sketch, not a settled location:

> Where the project can see it, LLM meaning lives **inside the model** as a graded, compositional, *thin*-inferential use-structure that **beats but does not escape** the distributional shadow — and the three "between/beyond" loci where meaning might also live (a world it refers to, a perceptual ground, other agents) are, so far, each **silent or negative**.

That is a **deflation-leaning but not eliminativist** picture, which is exactly the descriptivist middle the charter chose — arrived at from the findings rather than assumed. The crucial honesty: the four loci are **empirically distinct and carry different verdicts** (model-internal: positive; referential: silent; grounded: negative-bounded; relational: negative on *constitution*, but order-sensitive — non-commutative latest-wins — where order disambiguates, [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)), and the synthesis is wrong if it flattens them. It is also wrong if read as "LLMs mean" — every positive is consistent with a richer distributionalism, and the in-principle grounding gap is untouched.

## Where the project's own three proposals sit on this map

The session's three original conjectures are precisely the bets that would update the map's **three weakest cells** — and each is falsifiable:

- [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md) sharpens the *thin / distributional-prior* character of the constructional competence: accumulation aligns with the predictive objective (easy), defeasance fights it (hard). If it generalizes under matched difficulty, the "thin inferential, distributionally-shaped" reading of the grammatical positives is strengthened; if add/cancel turn symmetric, that reading weakens.
- [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md) names *where* the **grounded** cell could turn from "negative" to a signal: the text-under-determination residual (fine polysemy; abstract/perceptually-subtle senses; VWSD). It is the one bet that could move grounding off two nulls — or confirm the modality is inert for sense.
- [`conjecture/commutative-convention`](../conjectures/commutative-convention.md) turned the **relational** null into a testable algebraic property (commutative = aggregation; non-commutative = constitution). Its history-perturbation arm has now run four realizations (v2–v4 inconclusive or position-driven, then the Option A arm), plus the Option B stamp-comprehension gate (passed) that made an A-null interpretable; **Option A falsified it**: with physical position neutralized and order the sole disambiguator, both models recovered a reassigned term by its most-recent binding spontaneously at ceiling ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)). The conjecture is now **retired / falsified** (in the regime that can test it) and the positive promoted to [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md). Commutativity proved **operationalization-dependent** — present where order carries no disambiguating signal, absent where it does — and the resulting order-sensitivity is thin (latest-binding-wins), not constitution.

So the map is not static: its three softest cells (the depth of the inferential reading, grounding, and relational constitution) each have a sharp, queued experiment attached. That is the synthesis working as the charter intends — a positioning that *generates* the next questions rather than closing them.

## What this synthesis predicts and forbids

**Predicts.** If the picture holds: the remaining open bets resolve deflation-ward (the monotonicity asymmetry generalizes; the grounding headroom is narrow) — each genuinely falsifiable, not rigged. One of the original three bets has now **resolved against**: the prediction that the relational convention would stay *commutative* under perturbation **broke** where order disambiguates — both models proved order-sensitive (non-commutative) when position was neutralized and order was the sole cue ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md); [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)). Recorded as a resolved bet that did **not** go the way this sketch predicted, scoped: commutativity held in the v1/v4 settings where order carried no disambiguating signal, and the order-sensitivity that broke the bet is thin (latest-binding-wins), so the "negative on constitution" verdict survives even though the commutativity prediction did not. The lexical and grammatical positives keep **co-occurring** in the same panel (one target cline, [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md)) while the **competences stay dissociable** (the cross-axis result). And no text-only probe, however much it climbs, reaches the referential/externalist or richly-grounded cell — those move only with a built world-relation, not a cleverer text task. *(Frame-relative, added 2026-06-16: this "only a built world-relation moves the referential cell" prediction holds on the externalist and signal-based denials of LM reference, but **not** on the internalist one — on which no world-relation lifts the cell because the missing ingredient is a mind, not a relation. The denials of LM reference are disunified in exactly this counterfactual; see [`essay/reference-denials-disunified`](../essays/reference-denials-disunified.md). The prediction is correct within the frames this map tacitly assumes; the choice among frames is off-board.)*

**Forbids.** It forbids (i) reading any single positive as "LLMs mean" full stop — the distributional null is never fully escaped and the in-principle grounding gap stands; (ii) reading the grounding negatives as **proven absence** (they are bounded/underpowered negatives), or reading the relational order-sensitivity positive as **constitution** (it is thin latest-binding-wins, the relational cell stays negative on constitution); (iii) **flattening the four loci** — model-internal, referential, grounded, and relational meaning are empirically distinct here and the project's verdicts differ across them; (iv) treating the philosophical placements as results — they are interpretation over the fixed points, and the *fixed points* are what a future run may revise.

## Status and revision hook

`status: draft`; `contingent-on: []` — this page introduces no new empirical claim of its own; it depends on findings and concept pages already in-repo. It is the philosophical-map counterpart to the two empirical theory pages, which it cross-references for depth ([`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md) for the grammatical ladder; [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md) for the one-cline framing).

Revise this page when any of the still-soft cells move: an **AANN** result lands (sharpening the formal/functional and Tier-1 placement); a **fine-polysemy / VWSD** grounding probe runs (the headroom residual tested); or a **reference-bearing resource** is built (the only thing that could make the truth-conditional/externalist cell non-silent). The relational-perturbation trigger has now **fired**: the commutativity bet was **broken** (Option A, order-disambiguating; [`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)) — this revision records that resolution; the relational cell is now order-sensitive-but-thin rather than a clean commutative null, and would move again only if order-sensitivity were shown to be a surface artifact or were lifted past latest-binding-wins toward constitution. **(Update 2026-06-17: the surface-artifact half was tested and survived — an implicit-reassignment control dropped the explicit "was reassigned" wording and the most-recent-binding behaviour persisted at ceiling in both models ([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md)), so the cell does not move; it is held more firmly at order-sensitive-but-thin. The remaining mover is the constitution direction.) **(Update 2026-06-17, rung ii: a non-overwrite-repair probe ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md)) showed both models *compose* a compatible earlier turn rather than overwriting it — the update rule is supersede-on-conflict, compose-on-compatibility. This climbs a *second* rung but **still on the thin / single-reader-recoverable side**, so the cell stays negative on constitution; the result shows the earlier turn *survives*, not order-sensitive composition, and does not reach path-dependence (rung iii). The constitution direction remains the only mover that would redraw the cell — see [`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md).)** Each would redraw one cell; none is expected to overturn the whole sketch, but the map is held as revisable, and the findings — not the placements — are the part that compounds.

**(Update 2026-06-20, session 54 — dative line placed; no cell relocated.)** The grammatical axis gained its first human-anchored Tier-2 positive of the project's own design — the dative information-structure finding ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md), sessions 51 + 53) — which this map had pre-dated and omitted. This refresh **places it**: at the *use-over-truth-conditional* cell (a truth-conditionally-neutral use distinction the panel tracks, the alternants being identical in truth-conditions by construction) and the *graded/prototype* cell, **strengthening** the synthesis verdict's **use-based** and **graded** limbs with the map's first grammatical cell anchored to independent human production data — on **direction only**. No cell is **relocated**: the positive is *thin* (a preference, not inference-licensing) and human-anchored on direction not magnitude, and it touches none of the three "between/beyond" loci (referential, grounded, relational), so the synthesis location is unchanged and only better-supported. Its 2/3 replication and *widening* effect-size spread ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md)) are folded in as a live instance of the page's discipline 2 (under-claim; do not flatten a panel — [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)).
