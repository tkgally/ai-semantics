---
type: essay
id: inherited-not-constituted
title: Inherited, not constituted — Grindrod's metasemantic route and the project's behavioral null, drawn as one line from opposite directions
meaning-senses:
  - referential
  - distributional
  - relational
status: draft
contingent-on: []
created: 2026-06-14
updated: 2026-06-14
links:
  - rel: depends-on
    target: source/grindrod-2024-linguistic-intentionality
  - rel: refines
    target: essay/aggregation-not-constitution
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: conjecture/commutative-convention
---

# Essay: inherited, not constituted

> **Status: draft (2026-06-14). A philosophical-track essay arguing in the project's own voice.** Its claim is an *argumentative convergence*, not a new empirical result: it places a published metasemantic argument (Grindrod 2024) alongside the project's own behavioral relational null and argues that the two draw the same line — *the content an LLM deploys is located in something prior and public, not in the model's originating act and not in the live exchange* — from opposite directions. The essay introduces **no new empirical claim of its own**; every empirical assertion inside it cites the in-repo page that carries it. The convergence is one of *picture*, not a shared proof, and the section "The gap" states exactly why the two legs do not license each other. Read that section before citing the convergence.

## The position

This essay argues one bounded thesis. Two arguments in the project's orbit reach, by routes that never touch, the same conclusion about where the content an LLM deploys comes from — and they should be read as a genuine convergence, provided the gap between their methods is kept in full view.

- **Grindrod 2024 ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md)) argues from *metasemantics*.** Its move is to ask not whether an LLM is a source of *mental* content but whether its *outputs* meet the conditions a theory of *linguistic* content sets. On Evans' naming-practices account and Millikan's teleosemantics, they plausibly do — because **linguistic** intentionality is constitutively dependent on a *pre-existing public linguistic system that the model inherits from its training corpus*. The model does not *originate* the content; it inherits it.
- **The project's first essay ([`essay/aggregation-not-constitution`](aggregation-not-constitution.md)) argues from *behavior*.** Its relational pilot null shows that what looks like meaning constituted *between* interacting LLMs is really **aggregation** — a convention computed inside each model from shared content and then pooled — **not constitution**, which would be content existing in the live interaction and antecedently in neither party.

The thesis: these are **the same line drawn from opposite directions.** Both locate the content the model deploys in something **prior and public** — Grindrod in the inherited public language, the project in the shared content each agent brings to the exchange — and both deny that the content is *originated in the model's own act* or *constituted in the live dyadic interaction*. That shared negative — *not constituted here* — is the precise content of the convergence. The essay's discipline is in saying that and no more: it is a convergence of **picture**, not a shared argument, and one side's verdict is positive while the other's is a null.

## Grindrod's claim, at its actual strength

Grindrod's question is the project's own framing question put metasemantically: do LLMs *meaningfully use* the words they produce, or are they "merely clever prediction machines, simulating language use by producing statistically plausible text" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"What it is", quoting the paper)? His distinctive move is to shift the *level* of the question — away from a *mental* metasemantics (the conditions under which a mental state has content) toward a *linguistic* one (the conditions under which a linguistic item has content). The abstract states the payoff that turns on that shift:

> "I will argue that it is a mistake to think that the failure of LLMs to meet plausible conditions for mental intentionality thereby renders their outputs meaningless, and that a distinguishing feature of linguistic intentionality – dependency on a pre-existing linguistic system – allows for the plausible result that LLM outputs are meaningful." ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §Abstract)

The §5 Conclusion gives the same dependency claim in its load-bearing form, and names the two theories that make it good:

> "Instances of linguistic intentionality are reliant on a pre-existing linguistic system in a way that instances of mental intentionality need not be. Indeed, this is a feature of language that is made much of by both metasemantic theories considered: in Evans' notion that the meaning of name partly consists in the naming practice that circulates around the community, and in Millikan's notion that the meaning of a linguistic item is understood in terms of its history of reproduction." ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §5 Conclusion)

Two facts about this verdict are load-bearing for the convergence and must travel with it. **First, it is hedged-positive, not triumphant.** The source page records the hedge verbatim: "there is some plausibility to the idea that communicative intentions might play some necessary role on the production of a meaningful token. Ultimately, a great deal of further work will need to be done to defend a positive answer to the meaningful usage question" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §5 Conclusion). **Second, and decisively for this essay, Grindrod's relation is model-and-its-corpus, not between-agents.** The source page draws the boundary itself: the account is "about a single model's relation to an inherited public language (an aggregation-style, model-and-its-corpus picture), not about meaning constituted between agents; it should not be cited on between-agent constitution" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"What it cannot ground"). That boundary is what makes the convergence with the project's *between-agents* null exact rather than loose — it is set out below.

## The project's behavioral leg

The project's first essay reaches a structurally parallel conclusion without any metasemantics, from a black-box probe. Its relational pilot had two LLM agents coin referential conventions for hard-to-name figures, then asked a fresh matcher to recover the coined term from the record. The verdict, in the essay's own words, is "*coordination, not constitution*" ([`essay/aggregation-not-constitution`](aggregation-not-constitution.md), §"The evidence, stated at its actual strength"). The mechanism behind that verdict is the aggregation/constitution distinction the project's conjecture supplies:

> "A convention is **computed inside each agent** from the shared content and then **aggregated** across agents (two systems independently arriving at the same label from overlapping evidence)." ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"The distinction that makes \"coordination, not constitution\" precise")

against its contrast:

> "A convention **constituted *between*** agents would be one whose content \"exists in the interaction and not antecedently in either party\"." ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"The distinction that makes \"coordination, not constitution\" precise", quoting [`concept/relational-meaning`](../../base/concepts/relational-meaning.md))

The pilot found the first, not the second: the coined convention was recovered from the content-*set* of the prior turns, not their ordered trajectory — the signature [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) predicts for next-token predictors conditioned on overlapping content. The deflationary reading the project draws from this is itself a content-and-substrate story: the convergence "would *survive* order-scrambling" because two predictors drift toward a shared label "purely from co-occurrence content" ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §"How the project operationalizes the tag"). So the content the dyad coordinates on is **prior and shared** — present in each agent before the exchange, pooled in it — not minted *between* them. That is the behavioral leg's location of content: prior and shared, not constituted-in-interaction.

The project's essay is scrupulous that this is a *bounded* null, "powered only for large order effects" ([`essay/aggregation-not-constitution`](aggregation-not-constitution.md), §"What the null does not touch"), and that it deflates only "a tempting *empirical shortcut* — the inference from observed convergent convention-use between interacting LLMs to meaning constituted between them" ([`essay/aggregation-not-constitution`](aggregation-not-constitution.md), §"The position"). The convergence claimed here inherits that boundedness; it cannot make the behavioral leg carry more than the leg itself does.

## Where they converge

Strip both arguments to their negative core and they coincide. Each denies that the content an LLM deploys is **originated by the model in the present act**; each locates that content in something **prior and public**:

- For **Grindrod**, the prior-and-public thing is the **inherited linguistic system** — Evans' "naming practice that circulates around the community" and Millikan's "history of reproduction" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §5 Conclusion). The model's outputs are meaningful *because* they ride on content the public language already carries, not because the model fixes content itself.
- For the **project**, the prior-and-public thing is the **shared content each agent brings** to the dyad — the overlapping distributional substrate from which a coordinated convention is *aggregated*, not the live trajectory of the exchange ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"The distinction that makes \"coordination, not constitution\" precise").

The two even share a name for the shape: the source page itself calls Grindrod's relation "an aggregation-style, model-and-its-corpus picture" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"What it cannot ground"), and "aggregation" is exactly the project's word for what its null found. So the convergence is sharp: *both locate content in the prior-and-public, neither in the model's originating act, neither in the live dyadic exchange* — "not constituted (here / between agents)" is the same content on both sides.

There is a second, subtler way they illuminate each other. The project's relational result is a **null** (no between-agent constitution seen), while Grindrod's verdict is **positive** (outputs are meaningful, via inherited content). These are not in tension — they are mutually illuminating at exactly one strength: **the project's null is what you would expect if Grindrod is right that the content is inherited-and-public rather than constituted-in-interaction.** If the content the model deploys is already deposited in the public language it inherited, then no surplus should appear in the live exchange that was not antecedently in each party — which is precisely the project's bounded finding. That is the strongest form the mutual-illumination claim may take, and it is stated as an expectation-match, not a proof. The next section says why it can be no more than that.

## The gap (metasemantic vs behavioral)

This is the essay's central discipline, and the reason the convergence is of *picture* and not *argument*. The two legs reason at different levels, and **neither licenses the other's conclusion.**

- **Grindrod reasons metasemantically.** He asks what conditions a *linguistic item* must meet to carry content, and argues — from Evans and Millikan — that LLM outputs meet them. This is conceptual analysis "over a survey-level description of transformer LLMs"; the source page is explicit that "the paper reports no experiments, probes, or measurements" and "cannot serve as the `anchors:` resource for a claim or result" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"What it cannot ground"). No measurement follows from his argument, and his argument follows from no measurement.
- **The project reasons behaviorally.** It runs a black-box probe and reads off whether interpretation is order-sensitive. A behavioral null about trajectory-dependence is silent on the metasemantic question of what *conditions* content carriage requires; it can show that constitution *was not observed in this game*, never that the metasemantic conditions for content are or are not met.

So the two cannot stand in for one another. **The project's behavioral null does not confirm Grindrod's metasemantic thesis**: a null about between-agent order-effects is compatible with several metasemantic stories, not only his. **And Grindrod's metasemantic verdict does not confirm the project's null**: that content is inherited-and-public is a *claim about conditions*, and the project would still have to *measure* the absence of a constitutive surplus to show the dyad does not, in fact, mint content between its members (which it did, at pilot scale and power, and no further). What each side would need to actually license the other is explicit:

- For the behavioral leg to license Grindrod's verdict, it would need to operationalize his metasemantic conditions — Evans-style naming-practice dependence, Millikan-style reproduction history — into a measurable indicator and test it. The project has no such operationalization, and building one is non-trivial.
- For Grindrod's verdict to license the project's null, his metasemantic conditions would have to *entail* a specific, testable prediction about between-agent order-effects. He draws no such prediction; his account is, by the source page's own boundary, not a between-agent account at all.

The honest summary: the two arguments **point the same way and meet at the same picture**, and that coincidence is worth recording because it is non-obvious — a metasemantic argument and a behavioral probe, with nothing methodological in common, converging on *inherited-and-public, not originated-or-constituted-here*. But a coincidence of conclusion reached by disjoint methods is suggestive, not jointly probative. The essay claims the convergence; it does not claim either leg as evidence for the other.

## Revision triggers (read before citing)

The convergence is contingent on the legs that compose it, and either could move.

- **(a) If a future relational experiment shows non-commutative constitution between agents** — a robust, CI-clean order/position effect where homogeneous text dyads previously stayed commutative ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"What would confirm / falsify") — the convergence **weakens on the behavioral side**: the project's leg would then show constitution *between agents* exactly where Grindrod's model-and-corpus framing expects only inherited public content, and the "same line from opposite directions" reading would have to be relativized to the settings where the null still holds (homogeneous text-grid dyads), not retired wholesale. As of this writing the perturbation arm has run four times (v2–v4) and the conjecture stays `proposed` — "neither falsified nor certified" ([`conjecture/commutative-convention`](../conjectures/commutative-convention.md), §"Update 2026-06-14"); the trigger is armed, not fired.
- **(b) If the project ever catalogues a rebuttal to Grindrod's metasemantic move** — an in-repo source contesting that linguistic intentionality is constitutively dependent on a pre-existing system, or contesting the Evans/Millikan application to LLMs — revisit the Grindrod leg at its new, contested strength and re-state the convergence accordingly. Grindrod's verdict is "the author's argued position, not a consensus" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"Known limits"); a catalogued counter changes how much weight the metasemantic leg can bear.
- **(c) If the behavioral leg's null is overturned in its own essay** ([`essay/aggregation-not-constitution`](aggregation-not-constitution.md), which carries its own revision triggers), this essay's behavioral leg inherits that revision; re-read the convergence against whatever the first essay then says.

## What this essay is not

- **Not a claim that the behavioral null confirms Grindrod, nor that Grindrod confirms the null.** The gap section forbids both readings explicitly; the convergence is of picture, not of proof.
- **Not a between-agent reading of Grindrod.** His account is model-and-its-corpus, and the source page states it "should not be cited on between-agent constitution" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"What it cannot ground"). The convergence uses Grindrod's leg only on the model↔inherited-language relation, and reads the between-agents denial off the *project's* leg.
- **Not an endorsement that LLMs "understand" or have mental content.** Grindrod *denies* LLMs are sources of mental intentionality and his positive verdict is for *linguistic* meaningful usage, hedged on communicative intentions ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"What it cannot ground"); the project's stance is descriptivist, "describe, don't litigate" ([`source/grindrod-2024-linguistic-intentionality`](../../base/sources/grindrod-2024-linguistic-intentionality.md), §"Bearing on this project"). Neither leg, and so neither this essay, asserts understanding.
- **Not a settled verdict.** It is an argued convergence over two legs that may each move, with triggers attached so the move is visible.

## Honesty box

- The essay's *original* contribution is the **argumentative shape** — that a metasemantic argument and a behavioral null draw one line ("inherited-and-public, not originated-or-constituted-here") from opposite directions, and the precise statement of the gap that keeps this a convergence of picture rather than a shared proof. It is **not** a new empirical claim; every empirical assertion in it cites the in-repo page that carries it.
- The strongest thing the essay asserts about the relation between its two legs is an **expectation-match**: the project's bounded behavioral null is *what one would expect* if the content an LLM deploys is inherited-and-public rather than constituted-in-interaction. It does not assert confirmation in either direction. Nothing here outruns that.
