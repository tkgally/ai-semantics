---
type: essay
id: presence-is-not-balance
title: "Presence is not balance — why an attested ambiguity certifies that two senses are both there, never that they are evenly weighted, and what that splits apart for any anchor"
meaning-senses:
  - referential
  - distributional
  - human-comparison
status: revised
contingent-on: []
created: 2026-06-23
updated: 2026-07-05
links:
  - rel: refines
    target: essay/no-admissible-certifier
  - rel: depends-on
    target: result/forced-both-lexical-build-attempt-v2
  - rel: depends-on
    target: result/forced-both-lexical-build-attempt-v1
  - rel: depends-on
    target: resource/semeval2017-pun-corpus
  - rel: depends-on
    target: resource/homonym-meaning-dominance-norms
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: essay/layer-specialness-vs-always-resolvability
---

# Essay: presence is not balance

> **Status: revised (drafted 2026-06-23; revised 2026-06-23, session 94 — trigger (b) attempted
> and not met). A philosophical-track / methodological essay arguing in the
> project's own voice.** Its original move is a distinction — between a **co-presence** premise (two
> senses are both in play in an item) and a **balance** premise (neither of the two dominates) — and
> the claim that *an attested ambiguity can discharge the first and is structurally silent on the
> second*, so a single human-annotated resource can be a sound anchor for one while inventing an
> anchor for the other. It **makes no human comparison** and adds **no empirical claim**: every
> empirical sentence cites the in-repo page that carries it, at that page's stated strength. Read the
> revision triggers before citing. The essay generalizes a point the session-93 ratification of
> [`decisions/resolved/sense-coactivation-anchor-semeval-puns`](../../decisions/resolved/sense-coactivation-anchor-semeval-puns.md)
> reached on one case; it does **not** re-ratify that decision.

## The occasion

A scout found a released corpus — the SemEval-2017 Task 7 puns
([`resource/semeval2017-pun-corpus`](../../base/resources/semeval2017-pun-corpus.md)) — that
pre-encodes, per item, the two WordNet senses each pun evokes on the actual sentence. The corpus was
adopted (session 93, cross-session adversarial review) as the
[`decisions/resolved/forced-both-lexical-operationalization`](../../decisions/resolved/forced-both-lexical-operationalization.md)
gate's **Q4 sense-co-activation** anchor — and, in the same ruling, *refused* as a discharge of that
gate's **Q1-ii**, the demand for an independent check that **neither sense dominates**. The reviewer's
Q-B-1 reasoning turned on one sentence the resource page already concedes: in a pun "co-presence is
guaranteed, *equal salience is not measured*"
([`resource/semeval2017-pun-corpus`](../../base/resources/semeval2017-pun-corpus.md)).

That single resource being *adopted for one premise and rejected for another* is worth lifting out of
the decision and stating as a general point, because the two premises it splits — co-presence and
balance — are routinely run together under one word, "ambiguous," and the project will meet the
conflation again wherever it reaches for attested ambiguous data. This essay names the split and the
asymmetry that rides on it.

## The distinction

Two different facts can be asserted of an item that "has two senses":

- **Co-presence** (a.k.a. co-activation): *both* readings are genuinely in play in this item — neither
  is absent, neither is a mere lexical possibility left untouched by the context. This is an
  **existential, on/off** property: at least-two-senses-operative-here.
- **Balance** (the absence of dominance): of the two readings that are present, *neither leads* — they
  are roughly equal in salience. This is a **relative, graded** property: a comparison of weights, not
  a count of what is present.

The relation between them is one-directional and weak. Balance presupposes co-presence (you cannot
weigh what is not there), so a balanced item is a co-present item. But co-presence does **not** entail
balance: two readings can both be fully operative while one is the salient default and the other a
recessive second. A set with two non-zero elements is not thereby a set with two equal elements. The
inference "both senses are present, therefore neither dominates" is the quantifier slide from *some
of each* to *equal amounts of each*, and it is invalid.

This is not a pedantic gap that happens to be empty in practice. The class of items that most cleanly
*certifies* co-presence — attested puns — is, by the mechanics of the genre, **biased against**
balance. A homographic pun works by leading the reader down a salient default reading and then
springing a second, less-expected sense; the humor is the gap between a dominant surface meaning and
a subordinate surprise. So the very feature that makes a pun a gold-standard witness of co-presence
(two senses provably both required to get the joke) is in tension with balance (one of them is
typically the setup, the other the punchline). The resource that best discharges the first premise is
among the *worst*-placed to discharge the second. Presence and balance are not just logically
distinct; on the natural data, they pull apart.

## Why an attestation can certify one and not the other

The asymmetry has a clean source. An attestation certifies what it is an attestation *of*. A pun's
gold annotation is a record that two senses are **jointly required** to read the item as its author
and annotators read it — so the attestation *is of* co-presence, and discharges that premise directly:
the joint requirement is the thing observed. But the annotation records no comparison of the two
senses' weights; it does not say which reading a first-pass reader lands on, or by how much. Balance
is a fact about **relative salience in this context**, and salience is graded, reader-relative, and
not what a "these two senses are both evoked" label measures. The label is silent on balance not by
oversight but by **type**: it is a presence record, and balance is a weight relation.

This is exactly where the project's own forced-both build attempt hit its wall, and the build
attempt's structural finding is the general lesson in miniature. A frequency-based balance proxy —
even a perfectly frequency-balanced homonym — "does **not** measure the balance of the *specific
constructed co-predication sentence*," because a forced-both frame "yokes **each sense to its own
complement**, so the in-item balance is set by the *relative pull*" of those complements, a property
of the constructed item that no general-usage statistic sees
([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md)).
Generalize off "frequency proxy" to *any presence-or-frequency record*: a record that two senses are
available, or that they are equifrequent in the corpus at large, is the wrong type of object to
certify that they are evenly weighted **in this sentence**. Presence labels and corpus-frequency
balances are both blind to in-item salience for the same reason — neither is a measurement of the
contextual weighting that "no dominance" is a claim about.

## The corollary for anchors

The methodological payoff is a rule for reading any human-annotated resource against a premise:

> **An attested ambiguous stimulus discharges a co-presence premise and is silent on a balance
> premise. A resource may therefore be a sound anchor for "both senses are here" while inventing an
> anchor for "neither sense dominates" — the two must be sourced separately, and the balance source
> must be graded and transferable to the specific item, not merely a presence record or a
> general-usage frequency.**

Read this way, the session-93 ruling is a worked instance, not an exception: the SemEval gold is
*adopted* as the co-presence (Q4) anchor and *withheld* from the no-dominance (Q1-ii) demand, and the
balance step is routed to a *different* kind of resource — the word-grain dominance norms
([`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md),
human, per-word, a balanced homonym being one whose dominance is near zero). And the rule keeps even
*that* honest: the dominance norms are **general-usage, not the specific sentence's** balance, so they
are the right *type* of object (a graded weight, not a presence record) but still owe an **argued
transfer-to-item step** before they can certify that *this* constructed sentence does not lean — the
same in-item gap the build attempt named, softened (a graded human balance signal now exists) but not
closed (it is word-grain, not sentence-grain). The rule does not hand the balance premise a free
anchor; it tells you what *kind* of anchor could discharge it and what that anchor still owes.

## Where the split comes from in the concept of sense

The presence/balance distinction is not an artifact of measurement; it tracks something in the
structure of lexical ambiguity itself. [`concept/polysemy`](../../base/concepts/polysemy.md) draws the
homonymy/polysemy line by *whether co-presence is even natural*: for genuine homonyms (unrelated
senses sharing a form) "there is no bridging context where both senses are co-present" — disambiguation
is "expected and clean" — whereas polysemy lives on a cline with "intermediate and bridging cases where
two senses are co-present and judgements are genuinely indeterminate." A pun on a homonym is therefore an
**engineered** co-presence: it forces together two senses that do not naturally co-occur, which is
precisely why the forced-both line wants homonymic puns (the unrelated-sense subset) as its strongest
stimuli. But engineering co-presence does nothing to engineer *balance*: yoking two unrelated senses
into one context makes them both present by construction and leaves their relative salience to the
contingent pull of the frame. The concept page's "genuinely indeterminate" *judgements* of polysemous
bridges are a balance-like notion — an indeterminate judgement is one where neither reading wins — but
they are a property of natural polysemy cases, not something an attested-pun label exports. So even the part of the lexicon where co-presence and gradience travel
together does not license reading balance off a presence record; and the homonymic case the
forced-both line actually uses is exactly the case where co-presence is artificial and balance is
least guaranteed.

## How this relates to the neighbouring essays

- It **refines** [`essay/no-admissible-certifier`](no-admissible-certifier.md). That essay's lesson is
  that some premises (a constructed sentence's in-item balance, readable only by a barred human subject
  or the model under test) have **no admissible certifier** — and that the escape is to *replace the
  constructed item with one that arrived certified*. This essay sharpens the escape's small print:
  arriving-certified is **premise-relative**. The attested pun arrives certified *for co-presence* and
  uncertified *for balance*; adopting it for the first does not import it for the second. Where
  no-admissible-certifier asks "is there any admissible certifier for this premise?", this essay warns
  against a subtler error one step in — mistaking a sound certifier for *one* premise as a certifier
  for a *different* premise it is silent on. The presence/balance pair is the case where that mistake
  is most tempting, because one word ("ambiguous") names both.
- It serves [`essay/layer-specialness-vs-always-resolvability`](layer-specialness-vs-always-resolvability.md)
  without disturbing it. That essay's discriminating test needs forced-both items where **neither sense
  dominates**, because a lean suppresses `UNCLEAR` and manufactures a spurious **(A) layer-specialness**
  win. This essay explains *why* the co-presence anchor the project just adopted cannot quietly satisfy
  that demand, and so why the separate dominance step the gate's Q1-ii insists on is not bureaucratic
  caution but a type-correctness requirement: co-presence and no-dominance are different premises, and
  the burden the deflationary reading places on (A) is defended only if the second is sourced in its own
  right.

## Revision triggers (read before citing)

- **(a) A resource that certifies in-item balance directly.** If a released, human-annotated resource
  ever supplies a *per-item, graded* "neither sense dominates in this sentence" signal (not a
  general-usage frequency, not a mere presence label), the balance premise gains its own admissible
  anchor and the asymmetry this essay names is *discharged for that data* — the distinction stands, but
  the gap it describes is closed in that case. The essay is confirmed-and-narrowed, not retired: it
  would have correctly predicted that such a resource is a *different type* of object from a presence
  record.
- **(b) A demonstrated argued transfer-to-item from a general-usage balance norm.** If a future build
  makes the case (frozen, not assumed) that a word-grain dominance norm transfers to a specific
  constructed frame — bounding the relative-pull effect rather than ignoring it — then the
  [`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md)
  route discharges balance after all, and this essay's "still owes a transfer step" clause is the thing
  that was paid. Confirmation of the rule's shape, with the owed step now met. **ATTEMPTED AND NOT MET
  2026-06-23 (session 94):** the forced-both v2 build tried exactly this transfer — selecting attested
  homographic pun items whose word is balanced in *general usage* by these norms (43 items, 23 words) —
  and a fresh pre-run critic ruled the transfer **not arguable**: word-grain balance is the wrong grain
  for a pun sentence's in-item balance, the genre directionally installs the lean (so it cannot be
  averaged away), and — a fresh corroboration of this essay's core — the two human word-grain norms
  **disagreed on balance 11/11** on the items present in both. The owed step was *not* paid; this
  essay's "still owes a transfer step" clause stands, strengthened →
  [`result/forced-both-lexical-build-attempt-v2`](../results/forced-both-lexical-build-attempt-v2.md).
- **(c) An attested-ambiguity genre that is balance-unbiased.** The pun argument leans on a genre whose
  mechanics *bias toward* a dominant/recessive split. If some attested forced-both genre were shown to
  carry no such bias (its items are co-present **and** typically balanced by construction), then for
  that genre presence would be better evidence for balance than this essay allows. The logical
  distinction (presence does not *entail* balance) is untouched; the empirical "they pull apart on
  natural data" claim would be bounded to the pun-like genres.
- **(d) A finding that models read the salient-default sense regardless of annotated co-presence.** If a
  probe showed panel models systematically committing to one annotated sense of a pun (the surface
  default) far more than the other, that would be *behavioral* corroboration that co-presence labels do
  not predict balanced uptake — strengthening this essay's core. (It would be an
  `internal-contrast-only` within-model observation about uptake, not a human comparison; noted here as
  a prediction the rule makes, not a claim made.)

## Honesty box

- The essay's **original** contribution is the **distinction** between a **co-presence premise** and a
  **balance premise**, the **asymmetry** that an attested ambiguity discharges the first and is silent
  on the second (silent by *type*, a presence record being the wrong object to measure a weight
  relation), and the **anchor rule** that follows — a resource may soundly anchor co-presence while
  inventing an anchor for balance, so the two must be sourced separately and the balance source must be
  graded and item-transferable. **No empirical claim here is new, original, or reported.**
- The strongest in-repo sentences leaned on, at their stated strength: a pun's "co-presence is
  guaranteed, *equal salience is not measured*" and the abstract's puns "violate their
  one-sense-per-context assumption"
  ([`resource/semeval2017-pun-corpus`](../../base/resources/semeval2017-pun-corpus.md)); a balance proxy
  "does **not** measure the balance of the *specific constructed co-predication sentence*" because the
  frame yokes "**each sense to its own complement**, so the in-item balance is set by the *relative
  pull*" of the complements, with the gate's Q1-ii recorded as "certify, *independent of model output*,
  that neither sense dominates"
  ([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md));
  the gate's Q1-ii is the no-dominance demand and Q-B-1 refuses co-activation as its discharge
  ([`decisions/resolved/forced-both-lexical-operationalization`](../../decisions/resolved/forced-both-lexical-operationalization.md),
  [`decisions/resolved/sense-coactivation-anchor-semeval-puns`](../../decisions/resolved/sense-coactivation-anchor-semeval-puns.md));
  for homonyms "there is no bridging context where both senses are co-present," while polysemy has
  "intermediate and bridging cases where two senses are co-present and judgements are genuinely
  indeterminate" ([`concept/polysemy`](../../base/concepts/polysemy.md)); the dominance norms are **general-usage, not
  the specific sentence's** balance
  ([`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md)).
  Nothing here outruns those.
- **No human comparison** is made or owed: the essay is about *what human-anchored resources can and
  cannot certify*, not a contrast of model against human behavior; every result it touches is a NULL /
  not-yet-run / `internal-contrast-only` page. It does not re-ratify the session-93 decision (it was
  written the session that applied that ratification); it generalizes a point that ratification reached
  on one case, with its own revision triggers.
