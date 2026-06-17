---
type: essay
id: aggregation-not-constitution
title: Aggregation, not constitution — what the relational null does and does not deflate in social theories of meaning
meaning-senses:
  - relational
  - distributional
  - inferential
status: revised
contingent-on: []
created: 2026-06-12
updated: 2026-06-17
links:
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: result/relational-spontaneous-recency-a
  - rel: depends-on
    target: result/relational-implicit-reassignment-control
  - rel: depends-on
    target: result/relational-integration-rung-ii
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: source/brennan-clark-1996-conceptual-pacts
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

> **Status: revised (2026-06-16 — trigger (a) has now fired; the deflationary leg is half-overturned. See the newest-first Revision log entry.) The project's first essay — the philosophical track arguing in its own voice.** Its empirical leg rested on one bounded pilot null ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md)) and the forward bet that generalized it ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md)). The decisive history-perturbation test — repeatedly inconclusive through v2–v4 (position-confounded) — was finally run in its **v5 / Option-A** realization on 2026-06-16, with v4's text-position confound designed out by balanced rotation, and it **fired trigger (a)**: a CI-clean, ceiling, two-model order effect ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)), promoted to [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md). Per this essay's own pre-stated trigger-(a) spec, the claim that LLM dyad conventions *are* commutative **falls**, the anti-Brandomian friction **reverses in direction only (heavily qualified)**, and "What the null does not touch" survives and *gains* force. The essay's new resting place: the convention is **order-sensitive but thin — not the clean commutative aggregation first found, but also not constitution.** A follow-up control on 2026-06-17 ([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md)) **strengthened — did not overturn** — that Option-A positive: with Option A's explicit *"was reassigned"* sentence removed and everything else byte-identical, both models still recovered the most-recent binding at ceiling, so latest-binding-wins is not a wording artifact. It does not lift the finding past the bottom rung. A second 2026-06-17 result ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md)) folds in the *next* rung: when a later turn is *compatible* with an earlier one (a refinement, not a reassignment), both models **compose** the two rather than discarding the earlier — so the update rule is fuller than overwrite (**supersede-on-conflict, compose-on-compatibility**), but still **thin** (single-reader-recoverable), still **not constitution**. It strengthens, does not overturn, the deflationary leg below. Read the triggers and the Revision log before citing the argument.

## The position

This essay argues one bounded thesis. The relational pilot's verdict — *coordination, not constitution* — made algebraically precise by the commutative/non-commutative distinction of [`conjecture/commutative-convention`](../conjectures/commutative-convention.md), genuinely bears on **social and normative theories of meaning** (meaning in the Brandomian normative-inferential sense; meaning in the conceptual-pact, partner-specific sense). But what it deflates is narrow and specific: it deflates a tempting *empirical shortcut* — the inference from observed convergent convention-use between interacting LLMs to meaning constituted between them — and it deflates nothing else. It does not refute inferentialism, does not measure normative scorekeeping, and cannot, as an under-powered null, touch any metaphysical thesis about what meaning-constitution would require.

**Updated resting place (2026-06-16).** The title "*aggregation, not constitution*" survives in its second clause but no longer in its first. The Option-A test ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)) showed that, when a coined term is reassigned across stamped rounds so that **only recency disambiguates**, both models recover it by its most-recent binding — so the convention is **not the clean commutative aggregation the essay first found**. It is also **not constitution**. The honest middle name is **order-sensitive aggregation**: a thin *latest-binding-wins* update rule — order-sensitive, but the **bottom rung** of the relational ladder, a convention-update heuristic and nothing like meaning constituted between agents. *(Refined 2026-06-17: the rung-(ii) integration result ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md)) shows the rule is not blind overwrite — a **compatible** earlier turn **survives** and the two **compose** — so the fuller statement is **supersede-on-conflict, compose-on-compatibility**. This enriches the update rule but keeps it on the **thin / single-reader-recoverable** side: composing two stated constraints is something a single reader of the record can do, so it does not lift the finding off the bottom rungs toward constitution.)* The pilot's verdict thus moves from "what the pilot found is aggregation, and the only thing that falls is the premature claim that it was already constitution" to: **the convention is order-sensitive but thin, falling short of constitution from below.** Everything that follows keeps the original argument as the historical record and marks, inline, where the new test moves it.

## The evidence, stated at its actual strength

The pilot ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md)) had two LLM agents of the same family coin referential conventions for hard-to-name figures, then asked a fresh matcher to interpret the coined term given the prior turns. The content of the record is load-bearing: giving the matcher the history lifts accuracy by +0.25 to +0.42 over the opaque nickname alone, across all three model panels. The *order* of the record is not: the ordered-minus-shuffled gap is +0.06 to +0.11 and no model's clustered-bootstrap CI excludes 0, with the coherent reversed arm no better than random shuffling. The convention is recovered from the *set* of prior turns, not their *trajectory*. The conjecture page names this property **commutativity**: the recovered convention behaves as an order-invariant function of shared content, "**order-invariant / set-based**, not **path-dependent**" ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §Statement).

That is exactly the signature [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) predicts for two next-token predictors conditioned on overlapping content — in the result page's own words, "a convergence that survives order-scrambling" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Interpretation). And the null is bounded, by its own statement: n=12 coined terms per model, sensitive only to large consistent order effects, "*direction and absence-of-large-effect*, not a precise zero" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Caveats). The yardstick — text-grid referents, the order-isolating headline, the monologue floor — was ratified 2026-06-12 by autonomous cross-session adversarial review ([`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md)); the ratification fixed the measure, never the result, and never this essay's use of it. Everything below must be read against that grain of evidence and no finer.

## What the null deflates

**First, the easy constitution claim.** There is now a real temptation in the air. Populations of LLM agents demonstrably form shared conventions through purely local interaction: "Our findings show that social conventions can spontaneously emerge in populations of Large Language Models (LLMs) through purely local interactions, without any central coordination" ([`source/ashery-2025-llm-conventions`](../../base/sources/ashery-2025-llm-conventions.md), §Discussion quote). Model dyads play iterated reference games and succeed ([`source/imai-2025-vlm-common-ground`](../../base/sources/imai-2025-vlm-common-ground.md)). It is natural — and wrong, on current evidence — to read these convergences as interacting LLMs already *constituting* meaning in the relational sense between them. The pilot supplies the missing control that the convention-emergence literature does not run: neither Ashery et al. nor Imai et al. includes an order-scramble or trajectory-dependence test (both source pages state this explicitly), so their designs cannot distinguish a convention computed inside each agent from overlapping content and then *aggregated*, from one constituted in the live exchange. Where the project did run that control (the v1 pilot), aggregation is what it found. The controlled vocabulary's wager — "the multi-agent literature is about coordination, not meaning-constitution" ([`meaning-senses.md`](../../meaning-senses.md), §`relational`) — is no longer just a programmatic remark; it has one experimental instance behind it.

> **This deflation survives as a *historical* point (2026-06-16, trigger (a)).** It does not depend on the convention being commutative. Its content is methodological: Ashery- and Imai-style designs run no order-control, so they cannot detect the order/constitution distinction *either way*. Option A's positive only sharpens this — the order effect it found is precisely what those designs are blind to, so a convergence demo without the order-control still cannot license a constitution claim (and, equally, could not have detected the thin order-sensitivity Option A did). What it *does* update: where the v1 instance read "aggregation is what it found," the honest gloss is now "an *order-sensitive* aggregation appears once the design lets order disambiguate" — the missing control matters more, not less.

**Second, the evidential status of convergence itself.** The deeper deflation is methodological. Convergent convention-use, however rich — population-wide consensus, collective bias, tipping points in Ashery et al.; near-ceiling referential accuracy in the pilot — is the *floor*, not the finding. A convention whose interpretation any fresh agent can recover from the content-bag of the record is exactly what a shared distributional substrate predicts, and predicts *without* anything existing "in the interaction and not antecedently in either party" ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §intro). The commutative/non-commutative distinction turns this from a vibe into a measurement: only a non-commutative surplus — interpretation that tracks the *path*, not just the *set* — would be evidence of constitution. Anyone who wants to claim interacting LLMs constitute meaning between them now owes that surplus, not another convergence demo.

> **What survives, what falls (2026-06-16, trigger (a)).** The methodological point above — *convergence is the floor; the surplus must be paid in a non-commutative effect under artifact-resistant controls* — **survives as method, and is now doing positive work**: it is exactly the test Option A ran and passed. But the **empirical sub-claim that LLM dyad conventions *are* commutative falls**. Where order carries disambiguating recency information, both models put "**100%** of their SPONT mass on the figure agreed at the **maximum** round" ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md), §Headline) — a non-commutative effect. Crucially, the surplus that was paid is the *thinnest* one the framework admits: "Order-sensitivity here is consistent with a thin **convention-update / overwrite** rule … which is order-sensitive but is **not** the deep [`concept/relational-meaning`](../../base/concepts/relational-meaning.md) notion of a convention *constituted between* agents" ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md), §"What this shows"). So the measurement discipline is vindicated; the convention is order-sensitive; constitution is still **not** shown.

**Third, a small piece of friction against one empirical hope.** If LLM content were normatively instituted between agents in something like Brandom's sense, the relational axis is where that should have shown up as order-sensitive, interaction-borne structure. The in-repo discussion already draws this consequence at its correct, weak strength: the pilot is "more consistent with the internalist conceptual-role picture than with a relationally-constituted one, which is a small piece of friction against expecting the Brandomian version to be the right description of these systems — and nothing stronger" ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), §"The relational bridge"). Friction, not refutation. The next section says why the stronger reading is unavailable.

> **The friction reverses in direction only — sign-flip at the commutativity grain, gap to constitution untouched (2026-06-16, trigger (a)).** Option A removes the order-invariance that fed this friction: an order-sensitive surplus is, *in direction*, what an interaction-instituted account would predict, so on the narrow question "does anything beyond order-invariant content appear?" the friction's sign flips. But the reversal must not be over-read, and the result page is explicit about why: the surplus is "a thin **latest-binding-wins** rule," "the bottom rung of order-sensitivity, not the top," and emphatically "does **not** by itself certify constitution" ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md), §"What this shows"). Brandom's account is **deontic scorekeeping** — commitments held, entitlements tracked, challenges issued and answered — and Option A measured *none* of that (its agents made no assertions they could be held to, kept no score). So the sign flips at the *commutativity* grain while the gap to genuine normative constitution is **completely untouched**: this is **not** evidence for constitution and **not** evidence for Brandom's thesis. It removes one specific count of friction (the predicted-direction surplus did, in this regime, appear) without moving anything in the section below.
>
> **The removed count of friction is more secure, not larger (2026-06-17 — implicit-reassignment control).** The 2026-06-17 control ([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md)) dropped Option A's explicit *"was reassigned"* INTRO sentence, kept everything else byte-identical (same stimuli sha256), and **both models still recovered the most-recent binding at ceiling** (SPONT latest-binding **1.000**, Wilson-95 [0.926, 1.000]; first-binding **0.000**; physical-position at exactly chance **0.250**; DIRECT **1.000** both directions; **0 NA**). So the order-sensitive surplus is robust to removing the explicit flag — the friction-removal is sturdier, the surplus is not a wording artifact. But this changes **nothing** about magnitude or direction-of-distance to constitution: the control "does **NOT** show … 'rich constitution.' Exactly as in Option A, latest-binding-wins is consistent with a thin **convention-update / overwrite** rule … which is order-sensitive but is **not** the deep [`concept/relational-meaning`](../../base/concepts/relational-meaning.md) notion of a convention *constituted between* agents" ([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md), §"What this shows — and what it does NOT"). The gap to deontic scorekeeping stays untouched; do not read the firmer footing as nearness to constitution.

## What the null does not touch

> **This section survives intact and *gains* force (2026-06-16, trigger (a)).** Option A converts the null on this axis into a thin positive, but a thin *latest-binding-wins overwrite rule* is still not constitution and still not deontic scorekeeping. Every limit below holds exactly as written; where the original said "the null cannot reach Brandom's thesis," the result now says the same of a measured order effect — the surplus paid was the bottom rung, leaving the distance to normative constitution unchanged. Read each paragraph below with that in mind: the bar these theories set was not lowered by the new positive.

**Brandom's normativity was never measured.** Brandom-style normative inferentialism (*Making It Explicit*, 1994 — characterized, not read in-repo; the project's characterization lives at [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)) locates conceptual content in deontic statuses — commitments and entitlements — instituted and tracked between interlocutors in a scorekeeping practice: "Content is a normative status in a social practice, not a causal-functional property of one head" ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), §"Brandom's normative inferentialism"). The pilot measured none of that. Its agents made no assertions they could be held to, issued and faced no challenges, kept no score of anyone's entitlements. A reference game probes whether interpretation is path-dependent; deontic scorekeeping is about *answerability*, and the pilot's design has no observable that answerability could register on. So the null cannot count against the thesis that meaning in Brandom's sense requires normative-social institution — at most it suggests that *these systems, in this game*, exhibit nothing that needs that description. A Brandomian can consistently say the pilot looked for constitution in the wrong currency, and the project has no measurement to answer back with. That is recorded here as a standing limit, not conceded reluctantly.

**Conceptual pacts are partner-specific historical commitments — now read in-repo, and the reading sharpens the contrast rather than completing it.** The conceptual-pact primary source was fetched and verified 2026-06-12 ([`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md)), exercising this essay's standing trigger (c)(ii). What it grounds: human referential conventions are **historical and partner-indexed** — "when speakers and addressees ground a reference, they are creating a conceptual pact, a temporary agreement about how the referent is to be conceptualized" (p. 1484), and the pact is indexed to *who* it was made with (Experiment 3: same terms reused 48% of the time with the same matcher vs. 18% after a matcher switch, p. 1491). What it does **not** ground — and where the earlier characterization proved imprecise — is the *when*: the paper never manipulates interaction **order**, and its own analysis runs the other way on the sequence dimension: "Frequency of use better explains our data than does simple recency" (p. 1492) — frequency being an order-insensitive statistic of the history. So the conjecture's predicted human/LLM contrast now has an anchored human leg **on the partner/historicity dimension only**; human **order-sensitivity** — the dimension that would make the human convention non-commutative in the conjecture's algebraic sense — remains untested in-repo, and on the one adjacent measure Brennan & Clark do report, the human pattern leans *frequency-like*, i.e. commutative-compatible. This essay accordingly asserts about human conventions exactly what the source carries — pacts are real, joint, and partner-indexed — and nothing about human path-dependence. The same flag covers interactive alignment (Pickering & Garrod 2004 — characterized, not read in-repo) and Lewis's game-theoretic account of convention (Lewis 1969 — characterized, not read in-repo), whose lineage the naming-game paradigm descends from ([`source/ashery-2025-llm-conventions`](../../base/sources/ashery-2025-llm-conventions.md)). What *is* in-repo and suggestive: Imai et al. find VLM dyads do not form human-like pacts — "VLMs tend to produce unnecessarily long utterances and rarely reuse previously established shorthand" ([`source/imai-2025-vlm-common-ground`](../../base/sources/imai-2025-vlm-common-ground.md), §Discussion quote) — and the pilot's own anchored secondary finding is convergence without the human compression curve (LLM expression length flat at ~8.5–10.8 words vs. the human 7.73→4.10; [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), anchored to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md)). Two independent designs find model dyads coordinating without the pact-like texture of human entrainment. Suggestive convergence of pattern; not yet an anchored human-comparison claim about pacts.

**A bounded null cannot deflate a metaphysical thesis.** This is the essay's central discipline. The theses that meaning is constitutively social (Brandom), or that referential precedents are partner-indexed commitments (Clark and colleagues), are claims about what meaning-constitution *is*. The pilot is an n=12-per-model behavioral probe of three 2026 commercial models playing one text-grid game, powered only for large order effects. The correct logical relation between them is: the null deflates *premature empirical readings* of the social theses onto current LLM populations — the claim that constitution is already observably happening between models — and is silent on the theses themselves. An essay that claimed more would be doing with a null exactly what the project refuses to do with positives: inflating a bounded result into a philosophy-sized conclusion. The synthesis page's placement is the right one: "The deflationary aggregation reading holds; constitution is not seen (bounded, under-powered for order effects — not closed)" ([`theory/situating-llm-meaning`](../theory/situating-llm-meaning.md), §"The positioning").

## Revision triggers (read before citing — the ground may move this session)

The v2 **history-perturbation arm** — reassign a coined term mid-trajectory and test whether a fresh matcher's interpretation tracks *where* in the sequence the change landed, beyond *that* the content changed — is the conjecture's named decisive test ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"What would confirm / falsify") and is being run in the same session that writes this essay. Explicitly:

- **(a) If v2 shows a robust, CI-clean order/position effect** (interpretation tracks sequence position beyond content), the conjecture is retired and this essay's deflationary leg is **half-overturned**. What falls: the second deflation above ("convergence is only the floor" survives as method, but the claim that LLM dyad conventions *are* commutative falls), and the third (the anti-Brandomian friction reverses sign — a non-commutative surplus is exactly what an interaction-instituted account would predict, though still far short of deontic scorekeeping). What survives intact: the first deflation as a *historical* point (Ashery- and Imai-style designs still cannot detect constitution without the control), everything in "What the null does not touch" (which only gains force), and the methodological core — the commutativity test itself, which would now be doing positive work. The essay moves to `status: revised` with an in-page log entry. **← FIRED 2026-06-16 via Option A** (the v5 realization of this decisive test, with v4's text-position confound designed out by balanced rotation): a CI-clean, two-model, ceiling order effect ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)). The itemized spec above was applied exactly — see the newest Revision log entry. The surplus paid was the *thin* one (latest-binding-wins), so the reversal of the third deflation is **direction-only**; "What the null does not touch" gains force rather than falling.
- **(b) If v2 extends the null** (weak or no position effect once content is matched), the deflations strengthen from "the v1 record's order is not load-bearing" to "the position of a live mid-trajectory repair is not load-bearing" — a strictly sharper aggregation verdict. What still must **not** be claimed even then: that LLMs *cannot* constitute meaning relationally (two scope extensions remain untested), anything about Brandom's thesis itself, and anything about human *order-sensitivity* (Brennan & Clark 1996, now in-repo, grounds only partner-specificity/historicity — see the Revision log).
- **(c) Standing triggers.** (i) **Image referents** (the ratified Q1→B v2 upgrade) or **cross-family dyads** showing non-commutativity where homogeneous text dyads stay commutative would *bound* the conjecture and force this essay to relativize its deflation to setting, not retire it ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §scope extensions). (ii) **Fetching Brennan & Clark 1996** converts the human leg of the predicted contrast from characterization to citable ground; whatever it actually says about history- and partner-specificity, the "characterized, not read in-repo" hedges above must be replaced by quotes — and if the characterization proves wrong, the predicted human/LLM contrast is rewritten or dropped here as well as on the conjecture page. **← EXERCISED 2026-06-12 — see the Revision log: the paper was fetched, the hedges replaced, and the human-contrast clause rewritten (partner leg anchored; the order leg was over-characterized and is now explicitly open).**

## Revision log

- **2026-06-17 (rung-(ii) integration — folds in the next rung; refines the positive's characterization; status stays `revised`).**
  Like the implicit-reassignment control below, this is a **fold-in, not a named-trigger firing** — this
  essay's triggers (a)/(b) concern the v2 history-perturbation / commutativity test (fired 2026-06-16),
  and the integration result is a *new rung*, not a re-run of that test. A non-overwrite-repair probe
  ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md); independent
  pre-run critic GO, independent post-run verifier REPRODUCED) asked whether a *compatible* earlier turn
  **survives** (integration) or is **overwritten**.
  - **The result (verbatim).** Both models integrate at ceiling: INTEG target rate **1.000** (Wilson
    [0.926, 1.000]), the pure-overwrite "latest only" reading taken **0.000**, grid-position at chance
    (0.250), DIRECT on-demand 1.000, 0 NA. "When the latest turn is *compatible* with an earlier one, both
    models **compose** the two — the earlier, non-terminal turn's content survives into the recovered
    referent, at ceiling" ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md),
    §"What this shows").
  - **What it refines.** The "order-sensitive aggregation / *latest-binding-wins*" middle name above is
    enriched to **supersede-on-conflict, compose-on-compatibility**: the rule overwrites when turns
    *conflict* (rung i) but composes when they are *compatible* (rung ii). The second deflation's
    methodological core — *convergence is the floor; constitution must be paid in a surplus no single
    reader can reconstruct* — is **untouched and gains a second instance**: integration, like overwrite,
    is on the "**thin / single-reader-recoverable** side … a single reader handed the record can compose
    the two stated constraints" ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md),
    §"What this shows"). So the positive moved up one rung *on the same side of the thin/rich cut*.
  - **What it does NOT change.** Still **not constitution** and **not deontic scorekeeping**; nothing in
    "What the null does not touch" moves. Two result-borne bounds carry: the design's constraints are
    *symmetric*, so it shows the earlier turn **survives**, not that the composition is itself
    *order-sensitive*; and the conjunction is trivially easy (DIRECT = INTEG = 1.000), so the ceiling is
    weak evidence of genuinely *spontaneous* composition. **`internal-contrast-only` — no human comparison.**
- **2026-06-17 (implicit-reassignment control — strengthens, does not overturn, the Option-A positive; status stays `revised`).**
  This entry folds in a **control**, not a trigger firing — the implicit-reassignment control is not
  one of this essay's named triggers; it strengthens the Option-A positive the essay already leans on
  → [`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md)
  (independent pre-run critic GO, independent post-run verifier REPRODUCED).
  - **What it tested.** Option A's clean positive carried one deflationary escape: maybe both models
    tracked recency only because the INTRO *told* them the term *"was reassigned … in different rounds
    you agreed it referred to different figures."* — a wording artifact. This control **removed exactly
    that sentence** and kept everything else byte-identical (same `stimuli.json` sha256, same figures,
    round quadruples, geometry, seed, the two query conditions, parse, scoring). The model must itself
    notice the term picks out different figures across rounds.
  - **The result (verbatim).** Both models still recovered the most-recent binding at ceiling: SPONT
    latest-binding rate **1.000** (Wilson-95 [0.926, 1.000]), first-binding rate **0.000**,
    physical-position-following at exactly chance **0.250 / 0.250**, DIRECT manipulation check
    **1.000** in both directions, **0 NA**; 160/160 strict parses. "Numerically indistinguishable from
    Option A … removing the explicit flag changed **nothing** in the measured behaviour"
    ([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md),
    §"The headline"). So latest-binding-wins is **not** a surface artifact of the "was reassigned" wording.
  - **What it tightens.** Binding bound (2): "spontaneous" was already *query-not-recency-directed*; it
    is now also **flag-not-directed** — the model is not told a reassignment occurred and infers the
    multiplicity from the stamped history itself ([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md),
    §"What this shows — and what it does NOT"). The third deflation's reversal (anti-Brandomian friction
    reverses in direction only) is made **sturdier, not bigger**: the order-sensitive surplus is robust
    to dropping the explicit flag, so the removed count of friction is more secure.
  - **What it does NOT change.** The finding stays the **thin** *latest-binding-wins* rule — the
    **bottom rung**, **not** constitution and **not** deontic scorekeeping. The control "does **NOT**
    show … 'rich constitution'" and "does **not** separate thin order-sensitivity from deep
    path-dependence" (same section). It is **internal-contrast-only — no human comparison**; Brennan &
    Clark 1996 still report order-*insensitive* "Frequency of use better explains our data than does
    simple recency" (p. 1492), so the predicted human/LLM contrast remains **unsettled**. Nothing in
    "What the null does not touch" moves; the gap to constitution is untouched.
- **2026-06-16 (trigger (a) fired — the deflationary leg is half-overturned; status stays `revised`).**
  The decisive history-perturbation test — inconclusive through v2 (2026-06-12), v3 (2026-06-13),
  and v4 (2026-06-14, where it was found to be position-confounded) — was finally run in its
  **v5 / Option-A** realization →
  [`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)
  (independent pre-run critic GO, independent post-run verifier REPRODUCED). Option A builds the
  setting the conjecture's own caveat flagged as missing — a coined term **reassigned** to four
  figures across four stamped, non-contiguous rounds, once each, so the **content-set is symmetric**
  and **only recency disambiguates**, with v4's text-position confound removed by balanced rotation —
  and **both models put 100% of their SPONT mass on the most-recently-bound figure** (latest-binding
  rate **1.000**, Wilson-95 [0.926, 1.000]; first-binding 0.000; physical-position at exactly chance
  0.250; DIRECT manipulation check 1.000 both directions; 0 NA). That is a robust, CI-clean,
  two-model order effect with position neutralized — **trigger (a) as pre-stated**. Applying its
  itemized spec exactly:
  - **What falls:** the second deflation's empirical sub-claim that *LLM dyad conventions are
    commutative*. It is **falsified in the regime where order disambiguates**. The methodological
    core — *convergence is the floor; the surplus must be paid in a non-commutative effect under
    artifact-resistant controls* — **survives and now does positive work** (it is the test Option A
    passed).
  - **What reverses in direction only (heavily qualified):** the third deflation, the anti-Brandomian
    friction. An order-sensitive surplus is, *in direction*, what an interaction-instituted account
    predicts, so the sign flips **at the commutativity grain**. But the surplus paid is a thin
    *latest-binding-wins* update rule, "the bottom rung of order-sensitivity, not the top," which
    "does **not** by itself certify constitution"
    ([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md),
    §"What this shows"). The gap to Brandom's deontic scorekeeping (commitments, entitlements,
    challenges — none measured) is **untouched**. This is **not** evidence for constitution or for
    Brandom; do not read the reversal as more than a removed count of friction.
  - **What survives intact:** the first deflation as a *historical* point (Ashery-/Imai-style
    designs still cannot detect the order/constitution distinction without the control); the entire
    "What the null does not touch" section (it only **gains** force — a thin overwrite rule is still
    not constitution and still not deontic scorekeeping); and the commutativity test itself.
  - **Status of the cited pages:** [`conjecture/commutative-convention`](../conjectures/commutative-convention.md)
    is **retired (falsified in the regime that can test it)**; the positive is promoted to
    [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
    (supported, internal-contrast-only).
  - **Four binding bounds carried throughout:** (1) **thin, not rich** — latest-binding-wins, bottom
    rung, not constituted-between; (2) **"spontaneous" = query not recency-directed, not cue-free**
    (the INTRO flags the reassignment) — **tightened 2026-06-17:** also **flag-not-directed**, i.e.
    the model is *not* told a reassignment occurred and infers the multiplicity from the stamped
    history itself; the explicit flag is gone but the stamped history is not, so still **not literally
    cue-free** (see the 2026-06-17 Revision log entry); (3) **internal-contrast-only — no human comparison** (Brennan
    & Clark report order-*insensitive* frequency-over-recency, so the predicted human/LLM contrast is
    still **not** settled); (4) **does not overturn v1/v4 — it bounds them**: commutativity is
    **operationalization-dependent**, present where order carries no disambiguating signal (v1) or is
    confounded with position (v4), absent where order is the sole disambiguator (Option A).
  The essay's resting place moves accordingly: the convention is **order-sensitive but thin — not the
  clean commutative aggregation first found, but also not constitution** (order-sensitive aggregation,
  a latest-wins update rule). The earlier text is kept as the historical record, with inline trigger-(a)
  markers showing where the new test moves each leg.
- **2026-06-12 (later session — trigger c-ii exercised; status `live` → `revised`).**
  [`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md)
  was fetched from a verified third-party course-site mirror and read. The "characterized, not read
  in-repo" hedges on the conceptual-pact paragraph were replaced with verbatim-quoted, paginated
  ground. **Substantive correction:** the earlier characterization ("*who* you fixed a term with,
  and *when*, matters") was right about *who* and unlicensed about *when* — Brennan & Clark test
  partner-specificity and historicity, never order, and report "Frequency of use better explains
  our data than does simple recency" (p. 1492). The predicted human/LLM contrast was rewritten
  here and on [`conjecture/commutative-convention`](../conjectures/commutative-convention.md):
  the human leg is anchored on partner/historicity, and human order-sensitivity is now an
  explicitly open question rather than an assumed contrast pole. The essay's deflationary
  argument is **unchanged** (it never rested on the human leg); what changed is that the
  predicted contrast got honester — and, if anything, slightly *less* favorable to the
  presumption that humans must come out non-commutative.
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

Not a survey of social theories of meaning — it engages exactly the two positions the project's evidence touches, through in-repo characterizations. Not a refutation of inferentialism in either its internalist or its normative form — the project's probes index thin inference-preservation and order-sensitivity, neither of which reaches Brandom's constitutive claim ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)). Not a claim about human conventions — the human side of every contrast drawn here is anchored to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) (the compression curve only) or to [`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md) (partner-specificity and historicity only — not order-sensitivity), or is explicitly characterized-not-read (Brandom; Pickering & Garrod; Lewis). And not a settled verdict: it is an argument built deliberately on a result that may be superseded before the session that wrote it ends — which is why the triggers above are part of the essay, not an appendix.

## Honesty box

- The essay's *original* contribution is the argumentative shape — which deflations the commutativity result licenses and which it forbids — not any new empirical claim; every empirical assertion cites the in-repo page that carries it.
- The strongest sentence the evidence supports is conditional: *if* a convention's interpretation is commutative in the shared content, *then* observing that convention in use is not yet evidence of meaning-constitution in the relational sense. The pilot supports the antecedent at pilot scale, for homogeneous text dyads, so far. Nothing here outruns that.
