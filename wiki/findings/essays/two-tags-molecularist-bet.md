---
type: essay
id: two-tags-molecularist-bet
title: Two tags, a molecularist bet — keeping `distributional` and `inferential` apart, and the bill it leaves unpaid
meaning-senses:
  - distributional
  - inferential
status: draft
contingent-on: []
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: depends-on
    target: source/dummett-1975-what-is-a-theory-of-meaning
  - rel: depends-on
    target: source/quine-1951-two-dogmas
  - rel: depends-on
    target: concept/semantic-holism
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Essay: two tags, a molecularist bet

> **Status: draft (2026-06-26). A philosophical-track essay arguing in the project's own voice.** It introduces **no new empirical claim** and makes **no human-comparison claim**: every empirical assertion cites the in-repo page that carries it, and the original part is the argument — that the project's own decision to keep `distributional` and `inferential` as *two* meaning-sense tags is, in structure, a **molecularist** bet, and that the way the project operationalizes the `inferential` tag pays molecularism's central bill by *stipulation* rather than by solving it. The essay **re-locates** an open methodological issue; it does not resolve it. **Revision trigger:** if a later session ratifies a decision to collapse the two tags (or to keep them, with a principled criterion for the meaning-constitutive subset), or if the Dummett primary's molecularism framing is found overstated by the secondary that carries part of it, revise or retract accordingly.

## The position

The project's controlled vocabulary keeps two tags that, in a large language model, are visibly entangled: `distributional` (meaning tracked by co-occurrence structure) and `inferential` (meaning tracked by what an expression licenses you to infer). [`meaning-senses.md`](../../meaning-senses.md) records the entanglement as a live open issue and answers it provisionally:

> "Should `distributional` and `inferential` collapse, given that next-token prediction is implicitly inferential? Probably no — but write the case explicitly when it next matters." ([`meaning-senses.md`](../../meaning-senses.md), §"Open issues with the typology")

This essay writes that case. Its bounded thesis is two-part. **First**, the "probably no" is not a neutral bookkeeping preference: keeping the two tags apart presupposes that there is a *principled, bounded subset* of a model's relational structure that counts as the meaning-constitutive (inferential) part, distinct from the whole co-occurrence web — and presupposing exactly that is what it is to be a **molecularist** rather than a holist. So the project has, without naming it, taken a side on the holism axis it otherwise treats as an open philosophical question. **Second**, molecularism comes with a famous unpaid bill — *which* inferences are the constitutive subset — and the project's operationalization of the `inferential` tag does not pay it; it **stipulates** the subset by experimental design (the entailments a chosen construction contributes, judged on frozen minimal pairs) and moves on. That stipulation is defensible and probably unavoidable, but it is a load-bearing, unratified choice, and naming it is the whole of what this essay claims.

This page owns *that* argument. It does **not** re-develop the holism objection itself or the spectrum of positions — those are [`concept/semantic-holism`](../../base/concepts/semantic-holism.md)'s. It does **not** sort which *distributional* hypothesis the next-token objective instantiates — that is [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md)'s Harris-vs-Firth question. It takes the holism/molecularism axis as given and asks one downstream question the project cannot avoid because it has already answered it in practice: *is keeping the two tags apart a molecularist commitment, and has the project paid for it?*

## Why "don't collapse" is a molecularist commitment

Start from what the two tags track and why they are entangled. The distributional view "is instantiated in word embeddings and the next-token-prediction objective: a model trained to predict context implicitly encodes distributional structure" ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)). The inferential view marks something the concept page is careful to call a different thing: the two senses "are not definitionally the same, which is why this page `refines` rather than restates [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)… A finding earns the `inferential` tag when the indicator is inference-preservation, not similarity or surprisal alone." ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)). So the tags are kept apart by a deliberate criterion: *inference-preservation*, not *co-occurrence similarity*.

Now read that decision against the holism axis. [`concept/semantic-holism`](../../base/concepts/semantic-holism.md) states the alternatives precisely, and — this is the hook the present essay picks up — names the meaning-senses issue as downstream of exactly them:

> "…whose open issue *'Should `distributional` and `inferential` collapse, given that next-token prediction is implicitly inferential?'* is downstream of exactly this axis: if the inferential web and the distributional web are the same holistic object, the two tags track one thing; if molecularism is right, there is a principled subset that pulls them apart." ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md), §"The methodological bet")

That sentence does the work, but it stops at a conditional. The essay's move is to discharge the conditional in the direction the project's practice has already chosen. To *keep* the tags apart — to say a model can exhibit distributional structure across its whole relational web yet earn the `inferential` tag only on the bounded subset where inference is *preserved* — just is to assert that "there is a principled subset that pulls them apart." That is the molecularist disjunct. The holist disjunct ("the two tags track one thing") is precisely the collapse the open issue declines. So the provisional "probably no" is a provisional molecularism: the project bets that meaning's inferential core is a privileged, bounded part of the model's connections, not the whole web.

This is not a quibble about labels. It is the same structural choice Dummett draws for a theory of meaning. His founding statement of molecularism distinguishes the two by the *unit* a theory ties a capacity to:

> "…if it correlates such a capacity only with the theorems which relate to whole sentences, I shall call it molecular." ([`source/dummett-1975-what-is-a-theory-of-meaning`](../../base/sources/dummett-1975-what-is-a-theory-of-meaning.md), essay II, *Seas of Language* reprint p. 37)

A molecular theory privileges a *bounded* unit (the whole-sentence theorem, not every axiom of the language at once); a holist denies any such privileged unit exists. The project's `inferential` indicator privileges a bounded unit too — the entailment a particular construction contributes to a particular sentence — and reads meaning off *that*, not off the whole distribution. In Dummett's terms, the two-tag practice is molecular in shape. (The essay claims a *structural* parallel, not that the project endorsed Dummett's doctrine; nothing in the repo cites molecularism as a chosen program. The point is that the practice has the molecularist *form* whether or not anyone signed up for it — which is exactly why it inherits molecularism's bill.)

## The bill molecularism does not pay by itself

Molecularism's price is a single, sharp, old problem: *which* of an expression's inferential connections are the meaning-constitutive ones, and which are merely collateral belief? The Dummett source carries the problem and its sting, via the secondary that states it cleanly:

> "Molecularist theories typically try to keep the idea that meaning is tied to inferential role, but insist that only _some_ of the inferences involved with a term constitute its meaning. However, drawing a clear line between the meaning-constitutive and non-meaning-constitutive inferences/beliefs seems to commit one to a version of the analytic/synthetic distinction that has been out of favor since Quine's attack on it…" ([`source/dummett-1975-what-is-a-theory-of-meaning`](../../base/sources/dummett-1975-what-is-a-theory-of-meaning.md), §"Secondary," S3, carried via SEP "Meaning Holism" §2.2)

And Quine's attack is the reason the line is hard to draw. Define the constitutive inferences by appeal to synonymy or analyticity, and the definitions chase each other in a circle: synonymy is "no less in need of clarification than analyticity itself" ([`source/quine-1951-two-dogmas`](../../base/sources/quine-1951-two-dogmas.md), §I), so that after every refinement "we are back at the problem of analyticity" ([`source/quine-1951-two-dogmas`](../../base/sources/quine-1951-two-dogmas.md), §IV). The molecularist who wants a principled subset of meaning-constitutive inferences needs exactly the analytic/synthetic line Quine argues cannot be cleanly drawn — which is why the Dummett source records the standing charge that molecularism is "an unstable resting point between atomism and holism" (S3, via SEP). The bill is not a footnote; it is the reason the holism/molecularism dispute is still open.

So the project's provisional molecularism inherits a provisional debt: keeping `distributional` and `inferential` apart requires a principled criterion for the inferential (meaning-constitutive) subset, and that criterion is exactly the thing two of the project's own in-repo primaries say is the hard part.

## How the project actually pays it: by stipulation, not solution

Here is the part worth recording, because it is visible in the project's own method and has not been named. The project does **not** solve the which-inferences problem. It **stipulates** the constitutive subset by experimental design, and the stipulation is the construction-licensed entailment on a frozen minimal pair.

[`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) describes its strongest inferential evidence in exactly these terms: the inference-licensing results "operationalize a **thin, NLI / forced-choice notion of inferential role** (inference-*preservation* behavior on frozen minimal pairs)" ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), §"What the project's inference-licensing results do and don't show"). Read with the molecularist bill in hand, that sentence is doing more than the page says. To fix, in advance, *which* entailment a probe will test — the path-traversal inference of the *way*-construction, the caused-motion entailment, the conative's cancellation of completed contact — is to *pick the meaning-constitutive subset by fiat*. The frozen minimal pair is the apparatus of the pick: it holds everything else constant so that the one stipulated inference is what varies. The design does not discover which inferences constitute the construction's contribution to meaning; it *declares* them (this is the constructional analysis the items encode) and then measures whether the model preserves the declared ones.

This is a perfectly good way to *measure* a bounded competence — it is why the project's inference-licensing tables are its strongest behavioral evidence that decoders track construction-contributed inferences. But it is a *measurement* of a stipulated subset, not an *answer* to the molecularist's question of how that subset is principled rather than chosen. The project sidesteps Quine's circle by never trying to draw the analytic/synthetic line in general; it draws a local, construction-specific line by stipulation, per probe, and reads only inside it. The honest description of the `inferential` tag, then, is: *behavioral preservation of a designer-stipulated, construction-licensed entailment* — molecularism with the constitutive subset fixed by the experiment rather than derived from a theory of meaning.

Two in-repo cautions sharpen, not soften, this reading. First, the stipulated subset is *thin* in a second way the concept page already flags: even the chosen inference is **instrument-dependent** — the conative case has one model fail the stipulated entailment entirely under NLI yet partly recover it under forced-choice, "the same model on the same frozen items in the same run" ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), §"What the project's inference-licensing results do and don't show", citing [`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md)). If *whether the model exhibits the stipulated inference* shifts with the elicitation channel, then the bounded subset is not even cleanly observable, let alone principled. Second, the same page warns that this thin notion "should not be conflated with … NLI-task performance alone" — so a strong score on the stipulated subset is not the philosophical conclusion. The molecularist framing names *why* both cautions bite at once: the subset is stipulated (so its principledness is unearned) *and* its measurement is channel-fragile (so even the stipulated thing is not stably read off). The project's `inferential` tag is doing real work, but it is standing on a stipulation the project has not — and on Quine's argument, perhaps cannot — convert into a principled criterion.

## What this buys, and what it does not

The payoff is the same shape as the project's other sortings: precision, not progress.

- It **re-locates** the meaning-senses open issue. "Should the tags collapse?" is not, at bottom, a question about whether next-token prediction is "implicitly inferential" (it is — the entanglement is real). It is the question of whether the project's stipulated, construction-local constitutive subset can be made *principled* — i.e. whether the molecularist disjunct the project has bet on can be cashed without re-drawing the analytic/synthetic line Quine attacked. Framed that way, the "probably no, don't collapse" is exposed as resting on an IOU, not a settled distinction.
- It **names a load-bearing, unratified choice**: that the project reads `inferential` meaning off a designer-stipulated subset of inferences. This is not a defect to fix — stipulating the tested entailment is how controlled minimal-pair work is *possible* — but it is a methodological commitment that has lived implicitly, and the charter's discipline is to surface such commitments rather than smuggle them.

It does **not** resolve anything. It does not show molecularism is true, or that the tags *should* stay apart, or that the stipulation is *wrong*. It does not adjudicate holism vs. molecularism (that stays [`concept/semantic-holism`](../../base/concepts/semantic-holism.md)'s open axis). And it makes no claim about whether any model's stipulated-subset behavior amounts to meaning — that is the standing Piantadosi-Hill-versus-Bender-Koller dispute the project declines. The essay's strongest assertion is only this: **keeping `distributional` and `inferential` apart is a molecularist bet, and the project pays molecularism's central bill by stipulation, not by solution — so the open issue is re-located onto that stipulation, not dissolved.**

## What this essay is not

- **Not a resolution of the meaning-senses open issue.** It writes the case the issue invited ("write the case explicitly when it next matters") and concludes that the case turns on an unpaid bill, not that the tags should merge or split. The issue stays open, now with a sharper name.
- **Not a new empirical claim, and not a human-comparison claim.** It re-reads in-repo material (the concept pages, the inference-licensing results, the Dummett and Quine sources); it measures nothing and anchors nothing. No `anchors:` obligation arises, and none is claimed.
- **Not a charge that the stipulation is an error.** Stipulating the tested entailment per probe is how minimal-pair inference work is run; the point is that doing so *is* the molecularist's subset-selection move performed by fiat, and that this has gone unnamed.
- **Not a duplication of its neighbours.** [`concept/semantic-holism`](../../base/concepts/semantic-holism.md) owns the axis and the holism objection; [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) owns the tag and frames its thinness via Brandom-vs-Piantadosi-Hill and instrument-sensitivity; [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md) sorts the *distributional* ancestry. This essay adds only the molecularist reading of the *two-tag distinction itself* and of the stipulation that sustains it.

## Honesty box

- The essay's *original* contribution is the **molecularist reading of the project's own typology**: that keeping `distributional` and `inferential` apart presupposes a principled meaning-constitutive subset (the molecularist disjunct), that molecularism's which-inferences bill is the analytic/synthetic problem Quine attacked, and that the project pays the bill by *stipulating* the subset per probe (the construction-licensed entailment on frozen minimal pairs) rather than deriving it. The empirical and historical premises are all in-repo and cited.
- **Mixed-strength dependency, flagged.** The Dummett molecularism material is part primary (Q3, the molecular definition) and part secondary (S3, the which-inferences/analytic-synthetic problem, carried via SEP "Meaning Holism"); the essay leans on S3 for the bill, so that leg is secondary-strength and is marked as such here and on the source page. If a later session reaches the Dummett primary on the constitutive-inference point and finds the secondary's framing overstated, the "bill" argument should be re-checked.
- **The structural-not-doctrinal caveat is load-bearing.** The essay claims the project's practice has the molecularist *form*; it does **not** claim the project adopted molecularism as a position, nor that the project's authors intended the commitment. The force is "your method already bets this," not "you said this."
- The strongest thing asserted is that the open issue is **re-located onto an unpaid bill**, not resolved. Nothing here says the tags should collapse, should stay apart, or that the stipulation is illegitimate.
