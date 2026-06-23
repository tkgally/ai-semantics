---
type: essay
id: no-admissible-certifier
title: "No admissible certifier — when a required stimulus premise can be read only by a barred human subject or the model under test, and why that gap is a boundary the project's two rules jointly draw"
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: draft
contingent-on: []
created: 2026-06-23
updated: 2026-06-23
links:
  - rel: refines
    target: essay/design-out-not-model-out
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: depends-on
    target: result/forced-both-lexical-build-attempt-v1
  - rel: depends-on
    target: essay/layer-specialness-vs-always-resolvability
---

# Essay: no admissible certifier

> **Status: draft (2026-06-23). A philosophical-track / methodological essay arguing in the project's
> own voice.** Its original contribution is the naming of a **design-epistemics gap** the project has
> now hit in the flesh: a behavioral probe needs its stimuli to satisfy certain **premises** — properties
> the design *assumes* — and to certify a premise without contaminating the test, the certifier must be
> *neither the model under test* (anti-circularity) *nor a fresh human subject* (the no-human-subjects
> rule routes all human bearing through **existing** resources). When a required premise is one that
> **only** a fresh human judgement on the constructed item, or the model's own output, could read — and
> no existing resource pre-encodes it — the premise has **no admissible certifier** and the item is
> **uncertifiable from in-repo means**. The essay argues this is not a hard problem but a *boundary*: a
> joint consequence of two rules that are each correct, with a single, principled escape — an existing
> human-labeled resource that pre-encodes the property. It is anchored in one worked case from the
> project's own record, the session-91 forced-both lexical **build attempt**, but the gap it names is
> general. It contains **no new empirical claim** and makes **no human comparison**; the probe it reads
> ran no model and is `internal-contrast-only`. Read the revision triggers before citing.

## The occasion

The project tried, in session 91, to build the one stimulus that would settle a live fork — and could
not, for a reason worth lifting out of that result and stating on its own terms. The fork is
[`essay/layer-specialness-vs-always-resolvability`](layer-specialness-vs-always-resolvability.md)'s:
the surviving lexical commit-without-hedging is either **(A)** a fact about the word-sense layer or
**(B)** mere resolvability, and the one stimulus that pulls those apart is a *genuinely-unresolvable
lexical item* — a forced-both pun / zeugma where committing to one reading discards half the content.
A ratified gate
([`decisions/resolved/forced-both-lexical-operationalization`](../../decisions/resolved/forced-both-lexical-operationalization.md))
fixed the yardstick for building such an item. The build was attempted; it
**terminated at certification**:

> "**The forced-both lexical item cannot be cleanly certified — the blocker is Q1-ii, the independent
> (not-model-based) balance check, exactly where the gate and essay said it would be.**"
> ([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md))

Three of the gate's four questions were satisfiable. The fourth — certify, *without consulting the
model*, that neither sense dominates the constructed sentence — was not. And the result page is exact
about *why* it was not, in a sentence that is this essay's seed:

> "The only instruments that could read the constructed item's balance directly are (i) a human
> annotator on that sentence (closed) or (ii) the model's own response (forbidden — the circular
> operationalization-tuning failure the gate exists to prevent)."
> ([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md))

Two readers, both barred. That is not a statement about how hard the balance is to measure; it is a
statement that *every instrument that could measure it is ruled out in advance*. The essay's claim is
that this shape — **a required premise with no admissible reader** — is a recurring, nameable boundary,
not a one-off accident of one pun.

## The premise/conclusion cut, and the certifier tripod

A behavioral probe has two kinds of proposition attached to it. There is the **conclusion** — what the
model's behavior is read to show — and there are the **premises** — the properties the stimulus must
*already have* for the conclusion to be interpretable at all. "This item is forced-both, not a leaning
homonym" is a premise: if it is false, a confident single pick means nothing, because a leaning homonym
draws a confident pick too. The project's freeze-before-run discipline exists precisely to settle the
premises *before* any output, so that no premise can be quietly back-fitted to the result.

To certify a premise without contaminating the test, the certifier is hemmed in on two sides, by two
standing rules that are each load-bearing:

- **Not the model under test (anti-circularity).** Certifying a stimulus premise by consulting the very
  model whose behavior the premise will be used to interpret is the operationalization-tuning failure
  the protocol forbids: it lets the conclusion be smuggled into the premise. The gate states the ruling
  in its own anti-cheat voice — where the certification "cannot be made independent of model output, the
  honest move is to *declare the item uncertified*, not to relax the criterion"
  ([`decisions/resolved/forced-both-lexical-operationalization`](../../decisions/resolved/forced-both-lexical-operationalization.md),
  Q1). This rule is what keeps the project's positives clean; nothing here argues against it.

- **Not a fresh human subject (the no-human-subjects rule).** [`CLAUDE.md`](../../../CLAUDE.md) rule 4 is
  blunt: "**No human subjects.** Tom is the monitor, not a subject. All human bearing comes from existing
  resources (treebanks, sense-annotated corpora, dictionaries, acceptability sets, construction
  inventories)." Human evidence is admissible — that is the whole anchor discipline — but only as it
  comes *pre-encoded in an existing resource*, never as a fresh judgement elicited for this item. This
  rule is what keeps the project's human anchors auditable and reproducible; nothing here argues against
  it either.

So a premise's certifier must satisfy a tripod: **(1)** be independent of the model under test, **(2)**
carry any human bearing through an existing resource rather than a fresh subject, and **(3)** be in place
*before* the run (the freeze rule). Most premises the project certifies clear the tripod easily — a
frequency band reads off SUBTLEX, a sense distinction off a sense inventory, an acceptability contrast
off a published norm set. The tripod is not usually a wall. The essay is about the case where it is.

## The gap: a premise readable only by a barred instrument

The wall appears when a required premise P has the following profile: the *only* instruments that can
read P on the relevant item are **(i)** a fresh human judgement on that item or **(ii)** the model's own
output — and **no existing resource pre-encodes P for that item**. Then leg (i) is barred by rule 4
(it is a fresh subject, not an existing resource), leg (ii) is barred by anti-circularity, leg (3) is
moot because there is nothing admissible to freeze, and P is **uncertifiable from in-repo means**. There
is no admissible certifier — not because P is metaphysically obscure, but because the project's two
rules, applied together, remove every reader P happens to have.

The session-91 in-item balance is exactly this profile, and the result page walks each leg to its bar.
A human annotator on the constructed sentence is "closed: the project takes **no human subjects**
… all human bearing comes from *existing* resources, none of which rate these author-constructed
sentences"
([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md)).
The model's own response is "forbidden — the circular operationalization-tuning failure the gate exists
to prevent." That leaves only an existing corpus signal, and the one that decomposes word frequency by
sense (SemCor via WordNet) fails for a *deeper* reason than sparsity:

> "A SemCor balance ratio measures **general-usage** sense balance across the corpus. It does **not**
> measure the balance of the *specific constructed co-predication sentence*."
> ([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md))

This is the part that turns an accident into a boundary. The premise P here is not a property of a word
in general; it is a property of *the particular sentence the project constructed*. No pre-existing
resource rates a sentence that did not exist until the build wrote it. So even a perfectly
frequency-balanced word "leaves Q1-ii's in-item balance uncertified"
([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md)):
the only readers of a *constructed item's* balance are a human looking at that item or the model parsing
it, and both are barred. The premise has no admissible certifier, and the gate's fail-safe disposition
fires: declare the item uncertified, run no model, spend nothing.

## Why this is a *third* thing, not the two methodology essays restated

Two existing essays sit next to this one, and the value of naming the gap is partly in seeing that it is
neither of them.

**It is not the undischargeable negative.** [`essay/undischargeable-negative`](undischargeable-negative.md)
is about the **conclusion** side: a behavioral probe "can *witness* a capability … but can **never**
close out a capability's *absence*," so "No behavioral negative is ever written as a capability-absence"
([`essay/undischargeable-negative`](undischargeable-negative.md)). That asymmetry governs what model
*behavior* licenses you to infer. The gap here is upstream of any behavior: it is about whether the
**premise** of a probe can be established at all, *before* the model is queried. One essay polices what
comes out of the test; this one polices what is allowed to go in. The session-91 outcome is not even a
behavioral negative — no model ran — so the undischargeable-negative typology does not classify it; it
is a *fourth* kind of non-result, an **uncertifiable-premise** stop, and the two essays partition cleanly
into input-side and output-side limits.

**It is not "design it out."** [`essay/design-out-not-model-out`](design-out-not-model-out.md) says a
nuisance covariate that is "degenerate — zero-variance, hence perfectly collinear — within the condition
of interest … must be designed out at construction time, not modelled out at analysis time." That essay's
whole force is that there *is* an admissible fix: change the construction. The gap here is the case where
**you cannot design it out either** — and for an instructive reason. In-item balance is *constituted by
the construction*: as the session-91 result page found, a co-predication frame sets the balance by "the
relative pull of the two complements"
([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md)),
so the very act of building the sentence creates the property. You cannot design the property away
without designing the stimulus away (an unbalanced forced-both item is not the stimulus the fork needs).
The property is simultaneously *made by construction* and *unreadable without a barred instrument*. So
this essay **refines** design-out-not-model-out by adding the regime past the end of its line: design-out
is the prescribed control for a nuisance you can fix by construction; the no-admissible-certifier gap is
the case where the property you must certify is neither a nuisance to remove nor fixable by construction,
because construction is what *produces* it and only a barred reader can *measure* it. Design-out covers
"make the property go away"; this covers "the property must be there, must be certified, and has no
admissible certifier."

## The escape is the anchor discipline, which is why the scout matters

The gap is real but **local and liftable**, and naming its escape hatch is the constructive half of the
essay. The barred legs are *fresh* human judgement and the model's *own* output. What is **not** barred
is an *existing* human-labeled resource that pre-encodes the property: it carries human bearing the
admissible way (rule 4's "existing resources"), it is not the model under test (anti-circularity
satisfied), and it can be fetched, checksummed and frozen before the run (the freeze rule satisfied). A
released corpus of human-annotated puns/zeugmas with per-item co-activation or balance labels would be
exactly such a certifier — and the forced-both result page says so, listing as the thing that would lift
its wall "a released corpus of human-annotated puns/zeugmas with per-item balance or co-activation
labels (none in-repo or on `wanted.md` today)"
([`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md)).

This is why the uncertifiable-premise gap and the project's **resource-anchor discipline** are two views
of one thing. The anchor rule — every empirical claim about LLM meaning carries an `anchors:` link to a
*resource*, or queues the anchor question — is usually read as a guard on *conclusions*. The gap shows it
is equally a guard on *premises*: an existing human-labeled resource is the only admissible way to import
a human-sourced property into a probe at all, whether that property grounds the conclusion or certifies
the stimulus. So the high-value move against an uncertifiable-premise stop is never "relax the rule" and
never "elicit a fresh judgement"; it is **scout for an existing resource that already encodes the
property**, and if one is found, ratify it as an anchor across a session boundary (never in the session
that finds it) before any item leans on it. The gap thus has a precise, in-discipline remedy, and the
parked forced-both fork is parked *on that remedy*, waiting for the resource — not abandoned.

## The honest price of two good rules

The deepest point is the one easiest to flinch from: the no-admissible-certifier gap is the **joint cost
of two rules the project should keep**. No-human-subjects buys auditable, reproducible human anchoring and
forecloses a whole class of researcher-degrees-of-freedom; anti-circularity buys clean separation of
premise from conclusion. Each is correct. But *together* they make a class of stimulus premises —
precisely those readable only by a fresh subject or the model — uncertifiable from in-repo means. A
different project, willing to run a small annotation study, could certify the session-91 sentence's
balance in an afternoon; a less disciplined project could "certify" it by asking the model and not
noticing the circle. This project can do neither, and that is a feature with a bill. The findings are
cleaner *because* the rules bind; the cost is that some questions stay parked until the right pre-encoded
resource turns up. An honest methodology names the bill rather than hiding it — and names it as a cost of
the discipline working, not of the discipline failing. The session-91 stop is the discipline succeeding:
it refused to run a test it could not honestly set up, and wrote the refusal down.

## What this essay is not

- **Not an argument to relax either rule.** The reverse: it shows both rules are doing exactly their job
  when they jointly produce the gap, and that the in-discipline remedy (an existing pre-encoded resource)
  is available without weakening either.
- **Not a claim the property is uncertifiable *in principle*.** A human-subjects annotation study, or a
  model-based check, *could* read the in-item balance; the claim is only that the property is
  uncertifiable under **these** rules from **in-repo** means. The boundary is the project's, not the
  world's.
- **Not a finding about any model.** The worked case ran no model and is `internal-contrast-only`; nothing
  here asserts how any LLM treats puns, senses, or anything else. It is a claim about how the project may
  and may not *build* a probe.
- **Not the undischargeable negative and not design-out.** It is the input-side, premise-certification
  complement to the former (which governs conclusions) and the past-the-end-of-the-line case for the
  latter (which assumes an admissible construction-time fix exists).
- **Not a human comparison.** The escape hatch *is* a human-anchored resource, but no human number enters
  this essay; the gap and its remedy are stated structurally.

## Revision triggers (read before citing)

- **(a) A pre-encoding resource is found and ratified.** If a session scouts a released, licensed,
  open-access resource that pre-encodes the barred property (e.g. per-item human co-activation / balance
  labels for puns/zeugmas) and a *later* session ratifies it as an anchor, the gap is **locally lifted**
  for that property: the premise gains an admissible certifier and the parked probe becomes buildable.
  This would be the escape hatch firing exactly as the essay predicts; the essay is confirmed, not
  retired, and gains a worked example of the remedy. (This is the active backlog item the session-91
  result and [`NEXT.md`](../../../NEXT.md) both queue.)
  **Partially exercised 2026-06-23 (session 92), the same session this essay was written.** A scout found
  a released, open-access resource — SemEval-2017 Task 7's homographic puns
  ([`resource/semeval2017-pun-corpus`](../../base/resources/semeval2017-pun-corpus.md)) — that
  pre-encodes the **co-activation** half of the barred property (per-item human "two senses jointly
  present" labels on the *specific* pun sentence), and an anchor decision was **queued** for cross-session
  ratification ([`decisions/open/sense-coactivation-anchor-semeval-puns`](../../decisions/open/sense-coactivation-anchor-semeval-puns.md)).
  This is the escape hatch behaving exactly as the essay says it must — and instructively, it works by
  **replacing the constructed item with an attested, pre-labeled one**, not by certifying the
  uncertifiable constructed sentence (you do not certify what has no admissible certifier; you adopt items
  that arrived certified). The trigger has **not fully fired**: ratification is cross-session (not this
  one), and — sharper for this essay's thesis — the **balance** half (that *this* sentence does not lean)
  still has **no admissible certifier**: the dominance norms the scout also found
  ([`resource/homonym-meaning-dominance-norms`](../../base/resources/homonym-meaning-dominance-norms.md))
  are **general per-word** usage, not the specific sentence's balance, so the in-item-balance premise
  remains exactly the no-admissible-certifier gap this essay names. The escape lifts co-activation;
  the gap persists for in-item balance — confirmation, not refutation.
- **(b) A second in-repo case of the same profile.** If another build hits a required premise readable
  only by a fresh subject or the model under test, with no pre-encoding resource, this essay should be
  cited to classify it as an uncertifiable-premise stop and the typology checked for whether the two
  cases share more than their shape. Flagged, not assumed; the present scope is the one forced-both case.
- **(c) A claimed certifier that turns out to consult the model or a fresh subject.** If a future build
  proposes to certify such a premise by a route that, on inspection, reduces to asking the model or
  eliciting a fresh judgement, that is the gap reappearing in disguise and the anti-circularity /
  no-human-subjects guards must catch it — the essay is the reason to look. A "certifier" that is really
  one of the two barred legs wearing a corpus costume is the failure mode to watch.
- **(d) An amendment to either rule.** The gap's boundary is drawn by no-human-subjects (rule 4) and
  anti-circularity. If Tom amends either — say, by sanctioning a narrow, pre-registered annotation
  protocol — the boundary moves and a class of now-uncertifiable premises becomes certifiable. The essay
  would be re-scoped to the rules as amended; the structural point (a premise's certifier is hemmed by
  whatever rules are in force) is unaffected.
- **(e) A representational or non-behavioral certifier becomes available.** If a representation-level
  method could read a stimulus property without behavioral output from the model under test (and without
  a fresh subject), it would supply a new admissible leg to the tripod for some premises. Nothing in-repo
  licenses that today; the panel is behavioral, n=3 commercial.

## Honesty box

- The essay's **original** contribution is the **premise/conclusion cut applied to certification**, the
  **certifier tripod** (independent of the model under test; human bearing only via an existing resource;
  in place before the run), the **no-admissible-certifier gap** (a required premise readable only by a
  fresh subject or the model under test, with no pre-encoding resource, is uncertifiable from in-repo
  means), the placement of that gap as a *third* thing distinct from
  [`essay/undischargeable-negative`](undischargeable-negative.md) (conclusion-side) and
  [`essay/design-out-not-model-out`](design-out-not-model-out.md) (which assumes an admissible
  construction-time fix), and the identification of the **resource-anchor discipline as the gap's only
  in-discipline escape**. **No empirical claim here is new, original, or reported.**
- The strongest sentences leaned on, at their stated strength:
  - From [`result/forced-both-lexical-build-attempt-v1`](../results/forced-both-lexical-build-attempt-v1.md):
    "**The forced-both lexical item cannot be cleanly certified — the blocker is Q1-ii, the independent
    (not-model-based) balance check, exactly where the gate and essay said it would be.**"; "The only
    instruments that could read the constructed item's balance directly are (i) a human annotator on that
    sentence (closed) or (ii) the model's own response (forbidden — the circular operationalization-tuning
    failure the gate exists to prevent)."; "A SemCor balance ratio measures **general-usage** sense
    balance across the corpus. It does **not** measure the balance of the *specific constructed
    co-predication sentence*."; "even a perfectly frequency-balanced homonym leaves Q1-ii's in-item
    balance uncertified."; and the lift condition "a released corpus of human-annotated puns/zeugmas with
    per-item balance or co-activation labels (none in-repo or on `wanted.md` today)".
  - From [`CLAUDE.md`](../../../CLAUDE.md) rule 4: "**No human subjects.** Tom is the monitor, not a
    subject. All human bearing comes from existing resources (treebanks, sense-annotated corpora,
    dictionaries, acceptability sets, construction inventories)."
  - From [`decisions/resolved/forced-both-lexical-operationalization`](../../decisions/resolved/forced-both-lexical-operationalization.md):
    where certification "cannot be made independent of model output, the honest move is to *declare the
    item uncertified*, not to relax the criterion."
  - From [`essay/undischargeable-negative`](undischargeable-negative.md): a behavioral probe "can
    *witness* a capability … but can **never** close out a capability's *absence*"; "No behavioral
    negative is ever written as a capability-absence."
  - From [`essay/design-out-not-model-out`](design-out-not-model-out.md): a degenerate covariate "must be
    designed out at construction time, not modelled out at analysis time."
  Nothing here outruns those.
- **No human comparison** is made or owed: the worked probe ran no model and is `internal-contrast-only`,
  and this essay's original argument is methodological, so it carries no resource-anchor obligation. The
  escape hatch it identifies *is* a human-anchored resource, but the essay imports no human number and
  asserts none.
- **Provenance note (weaker than page-level).** The general methodology literature on circularity in
  measurement and on the premise/conclusion structure of an experiment is large, but this essay rests its
  rule on a from-scratch generalization of one in-repo build attempt and two in-repo methodology essays,
  not on an ingested external methods source — the same weakest-point that
  [`essay/design-out-not-model-out`](design-out-not-model-out.md) names for itself. An ingest of a
  methodology source on construct validity / circular operationalization would strengthen the grounding;
  flagged, not dodged.
