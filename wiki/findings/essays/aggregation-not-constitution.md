---
type: essay
id: aggregation-not-constitution
title: Aggregation, not constitution — what the relational null does and does not deflate in social theories of meaning
meaning-senses:
  - relational
  - distributional
  - inferential
status: live
contingent-on: []
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: refines
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: source/ashery-2025-llm-conventions
  - rel: depends-on
    target: source/imai-2025-vlm-common-ground
---

# Essay: aggregation, not constitution

> **Status: live (2026-06-12). The project's first essay — the philosophical track arguing in its own voice.** Its empirical leg rests on one bounded pilot null ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md)) and the forward bet that generalizes it ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md)). The decisive v2 history-perturbation test was run **in this same session, after the essay was written** — outcome: **inconclusive, neither trigger fired** (see the Revision log below); the Revision Triggers section states in advance exactly which parts of this essay fall under each outcome of the follow-up run. Read the triggers before citing the argument.

## The position

This essay argues one bounded thesis. The relational pilot's verdict — *coordination, not constitution* — made algebraically precise by the commutative/non-commutative distinction of [`conjecture/commutative-convention`](../conjectures/commutative-convention.md), genuinely bears on **social and normative theories of meaning** (meaning in the Brandomian normative-inferential sense; meaning in the conceptual-pact, partner-specific sense). But what it deflates is narrow and specific: it deflates a tempting *empirical shortcut* — the inference from observed convergent convention-use between interacting LLMs to meaning constituted between them — and it deflates nothing else. It does not refute inferentialism, does not measure normative scorekeeping, and cannot, as an under-powered null, touch any metaphysical thesis about what meaning-constitution would require. The title states the verdict and its limit at once: what the pilot found is **aggregation**, and the only thing that falls is the premature claim that it was already **constitution**.

## The evidence, stated at its actual strength

The pilot ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md)) had two LLM agents of the same family coin referential conventions for hard-to-name figures, then asked a fresh matcher to interpret the coined term given the prior turns. The content of the record is load-bearing: giving the matcher the history lifts accuracy by +0.25 to +0.42 over the opaque nickname alone, across all three model panels. The *order* of the record is not: the ordered-minus-shuffled gap is +0.06 to +0.11 and no model's clustered-bootstrap CI excludes 0, with the coherent reversed arm no better than random shuffling. The convention is recovered from the *set* of prior turns, not their *trajectory*. The conjecture page names this property **commutativity**: the recovered convention behaves as an order-invariant function of shared content, "**order-invariant / set-based**, not **path-dependent**" ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §Statement).

That is exactly the signature [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) predicts for two next-token predictors conditioned on overlapping content — in the result page's own words, "a convergence that survives order-scrambling" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Interpretation). And the null is bounded, by its own statement: n=12 coined terms per model, sensitive only to large consistent order effects, "*direction and absence-of-large-effect*, not a precise zero" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Caveats). The yardstick — text-grid referents, the order-isolating headline, the monologue floor — was ratified 2026-06-12 by autonomous cross-session adversarial review ([`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md)); the ratification fixed the measure, never the result, and never this essay's use of it. Everything below must be read against that grain of evidence and no finer.

## What the null deflates

**First, the easy constitution claim.** There is now a real temptation in the air. Populations of LLM agents demonstrably form shared conventions through purely local interaction: "Our findings show that social conventions can spontaneously emerge in populations of Large Language Models (LLMs) through purely local interactions, without any central coordination" ([`source/ashery-2025-llm-conventions`](../../base/sources/ashery-2025-llm-conventions.md), §Discussion quote). Model dyads play iterated reference games and succeed ([`source/imai-2025-vlm-common-ground`](../../base/sources/imai-2025-vlm-common-ground.md)). It is natural — and wrong, on current evidence — to read these convergences as interacting LLMs already *constituting* meaning in the relational sense between them. The pilot supplies the missing control that the convention-emergence literature does not run: neither Ashery et al. nor Imai et al. includes an order-scramble or trajectory-dependence test (both source pages state this explicitly), so their designs cannot distinguish a convention computed inside each agent from overlapping content and then *aggregated*, from one constituted in the live exchange. Where the project did run that control (the v1 pilot), aggregation is what it found. The controlled vocabulary's wager — "the multi-agent literature is about coordination, not meaning-constitution" ([`meaning-senses.md`](../../meaning-senses.md), §`relational`) — is no longer just a programmatic remark; it has one experimental instance behind it.

**Second, the evidential status of convergence itself.** The deeper deflation is methodological. Convergent convention-use, however rich — population-wide consensus, collective bias, tipping points in Ashery et al.; near-ceiling referential accuracy in the pilot — is the *floor*, not the finding. A convention whose interpretation any fresh agent can recover from the content-bag of the record is exactly what a shared distributional substrate predicts, and predicts *without* anything existing "in the interaction and not antecedently in either party" ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §intro). The commutative/non-commutative distinction turns this from a vibe into a measurement: only a non-commutative surplus — interpretation that tracks the *path*, not just the *set* — would be evidence of constitution. Anyone who wants to claim interacting LLMs constitute meaning between them now owes that surplus, not another convergence demo.

**Third, a small piece of friction against one empirical hope.** If LLM content were normatively instituted between agents in something like Brandom's sense, the relational axis is where that should have shown up as order-sensitive, interaction-borne structure. The in-repo discussion already draws this consequence at its correct, weak strength: the pilot is "more consistent with the internalist conceptual-role picture than with a relationally-constituted one, which is a small piece of friction against expecting the Brandomian version to be the right description of these systems — and nothing stronger" ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), §"The relational bridge"). Friction, not refutation. The next section says why the stronger reading is unavailable.

## What the null does not touch

**Brandom's normativity was never measured.** Brandom-style normative inferentialism (*Making It Explicit*, 1994 — characterized, not read in-repo; the project's characterization lives at [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)) locates conceptual content in deontic statuses — commitments and entitlements — instituted and tracked between interlocutors in a scorekeeping practice: "Content is a normative status in a social practice, not a causal-functional property of one head" ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), §"Brandom's normative inferentialism"). The pilot measured none of that. Its agents made no assertions they could be held to, issued and faced no challenges, kept no score of anyone's entitlements. A reference game probes whether interpretation is path-dependent; deontic scorekeeping is about *answerability*, and the pilot's design has no observable that answerability could register on. So the null cannot count against the thesis that meaning in Brandom's sense requires normative-social institution — at most it suggests that *these systems, in this game*, exhibit nothing that needs that description. A Brandomian can consistently say the pilot looked for constitution in the wrong currency, and the project has no measurement to answer back with. That is recorded here as a standing limit, not conceded reluctantly.

**Conceptual pacts are partner-specific historical commitments — and the human side is characterized, not read.** The conceptual-pact account (Brennan & Clark 1996 — **characterized, not read in-repo**; queued in [`base/wanted.md`](../../base/wanted.md) at P2) holds that human referential conventions carry a historical, partner-specific component: *who* you fixed a term with, and *when*, matters to later interpretation. The conjecture's predicted human/LLM contrast — humans non-commutative, LLM dyads commutative — therefore has an entirely unanchored human leg. Until Brennan & Clark is fetched and read into a `source/` page, the human non-commutativity claim is a characterized prediction, not a finding, and this essay asserts nothing about human conventions. The same flag covers interactive alignment (Pickering & Garrod 2004 — characterized, not read in-repo) and Lewis's game-theoretic account of convention (Lewis 1969 — characterized, not read in-repo), whose lineage the naming-game paradigm descends from ([`source/ashery-2025-llm-conventions`](../../base/sources/ashery-2025-llm-conventions.md)). What *is* in-repo and suggestive: Imai et al. find VLM dyads do not form human-like pacts — "VLMs tend to produce unnecessarily long utterances and rarely reuse previously established shorthand" ([`source/imai-2025-vlm-common-ground`](../../base/sources/imai-2025-vlm-common-ground.md), §Discussion quote) — and the pilot's own anchored secondary finding is convergence without the human compression curve (LLM expression length flat at ~8.5–10.8 words vs. the human 7.73→4.10; [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), anchored to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md)). Two independent designs find model dyads coordinating without the pact-like texture of human entrainment. Suggestive convergence of pattern; not yet an anchored human-comparison claim about pacts.

**A bounded null cannot deflate a metaphysical thesis.** This is the essay's central discipline. The theses that meaning is constitutively social (Brandom), or that referential precedents are partner-indexed commitments (Clark and colleagues), are claims about what meaning-constitution *is*. The pilot is an n=12-per-model behavioral probe of three 2026 commercial models playing one text-grid game, powered only for large order effects. The correct logical relation between them is: the null deflates *premature empirical readings* of the social theses onto current LLM populations — the claim that constitution is already observably happening between models — and is silent on the theses themselves. An essay that claimed more would be doing with a null exactly what the project refuses to do with positives: inflating a bounded result into a philosophy-sized conclusion. The synthesis page's placement is the right one: "The deflationary aggregation reading holds; constitution is not seen (bounded, under-powered for order effects — not closed)" ([`theory/situating-llm-meaning`](../theory/situating-llm-meaning.md), §"The positioning").

## Revision triggers (read before citing — the ground may move this session)

The v2 **history-perturbation arm** — reassign a coined term mid-trajectory and test whether a fresh matcher's interpretation tracks *where* in the sequence the change landed, beyond *that* the content changed — is the conjecture's named decisive test ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"What would confirm / falsify") and is being run in the same session that writes this essay. Explicitly:

- **(a) If v2 shows a robust, CI-clean order/position effect** (interpretation tracks sequence position beyond content), the conjecture is retired and this essay's deflationary leg is **half-overturned**. What falls: the second deflation above ("convergence is only the floor" survives as method, but the claim that LLM dyad conventions *are* commutative falls), and the third (the anti-Brandomian friction reverses sign — a non-commutative surplus is exactly what an interaction-instituted account would predict, though still far short of deontic scorekeeping). What survives intact: the first deflation as a *historical* point (Ashery- and Imai-style designs still cannot detect constitution without the control), everything in "What the null does not touch" (which only gains force), and the methodological core — the commutativity test itself, which would now be doing positive work. The essay moves to `status: revised` with an in-page log entry.
- **(b) If v2 extends the null** (weak or no position effect once content is matched), the deflations strengthen from "the v1 record's order is not load-bearing" to "the position of a live mid-trajectory repair is not load-bearing" — a strictly sharper aggregation verdict. What still must **not** be claimed even then: that LLMs *cannot* constitute meaning relationally (two scope extensions remain untested), anything about Brandom's thesis itself, and anything about human conventions while Brennan & Clark 1996 stays unfetched.
- **(c) Standing triggers.** (i) **Image referents** (the ratified Q1→B v2 upgrade) or **cross-family dyads** showing non-commutativity where homogeneous text dyads stay commutative would *bound* the conjecture and force this essay to relativize its deflation to setting, not retire it ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §scope extensions). (ii) **Fetching Brennan & Clark 1996** converts the human leg of the predicted contrast from characterization to citable ground; whatever it actually says about history- and partner-specificity, the "characterized, not read in-repo" hedges above must be replaced by quotes — and if the characterization proves wrong, the predicted human/LLM contrast is rewritten or dropped here as well as on the conjecture page.

## Revision log

- **2026-06-12 (same session, post-run).** The v2 history-perturbation arm ran →
  [`result/relational-history-perturbation-v2`](../results/relational-history-perturbation-v2.md):
  **INCONCLUSIVE/MIXED on all three models — neither trigger (a) nor (b) fired.** The
  falsification clause did not fire (no model tracked stated chronology in both
  presentation-direction arms), and the commutative null was not certified (one model's
  forward-arm elevation is CI-clean but vanishes when chronology is decoupled from prompt
  position — confound identified, unresolved). **No section of this essay falls or
  strengthens**; the argument stands exactly as written, on the v1 evidence it was built on.
  One point gains a live illustration: the run's pre-run critic caught a design under which a
  bare prompt-position artifact would have fired the falsification clause and been mistaken
  for the non-commutative surplus — the second deflation's lesson ("anyone claiming
  constitution owes the surplus, under artifact-resistant controls") demonstrated on the
  project's own instrument. The decisive test remains open; triggers (a) and (b) stay armed
  for the follow-up run. Status stays `live` (no substantive revision required).

## What this essay is not

Not a survey of social theories of meaning — it engages exactly the two positions the project's evidence touches, through in-repo characterizations. Not a refutation of inferentialism in either its internalist or its normative form — the project's probes index thin inference-preservation and order-sensitivity, neither of which reaches Brandom's constitutive claim ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)). Not a claim about human conventions — the human side of every contrast drawn here is either anchored to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) (the compression curve only) or explicitly characterized-not-read. And not a settled verdict: it is an argument built deliberately on a result that may be superseded before the session that wrote it ends — which is why the triggers above are part of the essay, not an appendix.

## Honesty box

- The essay's *original* contribution is the argumentative shape — which deflations the commutativity result licenses and which it forbids — not any new empirical claim; every empirical assertion cites the in-repo page that carries it.
- The strongest sentence the evidence supports is conditional: *if* a convention's interpretation is commutative in the shared content, *then* observing that convention in use is not yet evidence of meaning-constitution in the relational sense. The pilot supports the antecedent at pilot scale, for homogeneous text dyads, so far. Nothing here outruns that.
