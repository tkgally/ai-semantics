---
type: essay
id: origo-supplied-not-occupied
title: "The origo is supplied, never occupied — why a tool-clock probe tests an as-if behavior, not whether the model is in a context"
meaning-senses:
  - referential
  - grounded
  - distributional
status: revised
contingent-on: []
created: 2026-06-30
updated: 2026-07-01
links:
  - rel: refines
    target: essay/indexical-character-learnable-content-supplied
  - rel: depends-on
    target: result/tool-origo-deictic-anchor-v1
  - rel: depends-on
    target: source/braun-2015-indexicals-sep
  - rel: depends-on
    target: concept/grounding
  - rel: refines
    target: essay/reference-as-premise-bound
  - rel: depends-on
    target: essay/transcript-ceiling
  - rel: depends-on
    target: essay/conversation-as-text-not-timeline
  - rel: depends-on
    target: result/indexical-character-application-v1
---

# Essay: the origo is supplied, never occupied

> **Status: draft (2026-06-30). A philosophical-track essay arguing in the project's own voice.** Its
> contribution is a *structural diagnosis*, not a new empirical result: it sharpens **trigger (b)** of the
> parent essay [`essay/indexical-character-learnable-content-supplied`](indexical-character-learnable-content-supplied.md)
> by separating three claims that essay's "content" half runs together, and arguing that a tool-augmented
> clock/location probe tests only the weakest of the three. The essay introduces **no new empirical
> claim**; every empirical or textual assertion cites the in-repo page that carries it. It makes **no
> human comparison** in either direction (`internal-contrast-only` posture is in force, as for the parent
> essay; this essay asserts no human/model contrast). Read "Three claims, not one" and "What this does NOT
> show" before citing any sentence here.

## The position

The parent essay split an indexical's meaning along Kaplan's seam — **character** (the convention-fixed
rule, argued to sit on the distributional side as an *affordance*) and **content** (the value at an
*occupied* context, argued to sit on the grounding side, the load-bearing claim) — and pre-registered a
revision trigger that imagines lifting the content half off its peg:

> "**(b) The model is given an origo.** A finding in which the system is supplied a *live* context it
> occupies (a tool-augmented setup with a real clock/location as its own deictic anchor, or a
> grounded/embodied probe) would test whether content can shift from premise-supplied to
> situation-supplied." ([`essay/indexical-character-learnable-content-supplied`](indexical-character-learnable-content-supplied.md),
> Revision triggers)

This essay argues one bounded thesis: **trigger (b), as written, conflates three distinct claims, and the
tool-clock probe it gestures at can only touch the weakest one.** Once the three are pulled apart, the
*strong* reading of the content half is plausibly **not settleable by any text-channel behavioral probe**
— it is premise-bound in the sense [`essay/reference-as-premise-bound`](reference-as-premise-bound.md)
named, and a built-in limit of the text medium in the sense [`essay/transcript-ceiling`](transcript-ceiling.md)
named. That is offered as a *documented in-principle limit* — a first-class result of the philosophical
track — not as a failure to find anything. What stays genuinely testable is a narrow *as-if* question,
and the essay carves it out and labels it honestly.

## Three claims, not one

The parent essay's content half — "the content requires a context the model does not occupy" — bundles
three claims that have very different evidential standings. Pulling them apart is the whole move.

**(i) The architectural claim.** The model occupies **no Kaplanian context**. On Kaplan's theory, as the
survey states it, "Each context has associated with it at least an agent, time, location, and possible
world. The content of ‘I’ with respect to a context \(c\) is the agent of \(c\). The content of ‘here’ is
the location of \(c\). The content of ‘now’ is the time of \(c\)" ([`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md),
§3.2). The architectural claim says a text-only model is not the *agent* of an utterance situation, has no
clock-time it *inhabits*, no location it is *in* as opposed to *describing*, no world it occupies — exactly
the parent essay's "it is not the agent of an utterance situation; it is not at a location; its ‘now’ is
not a clock time it inhabits; it has no world it is *in* as opposed to *describing*"
([`essay/indexical-character-learnable-content-supplied`](indexical-character-learnable-content-supplied.md),
"The two halves"). This is a claim about what the model *is*, not about what it *does*.

**(ii) The channel claim — the load-bearing, defensible one.** *Every* origo reaches the model through
the **described** channel: as text it conditions on. The parent essay already commits to this for the
honest borderline case, the system prompt that hands the model a date:

> "a prompt-supplied date is *text the model conditions on* — a **described** origo — not a context the
> model is the agent of, the way a human speaker's ‘now’ is the time they are *in*. … whatever it has
> arrives, without exception, through the **described** channel; the architectural fact the essay leans on
> is precisely that this is the *only* channel by which a context can reach it."
> ([`essay/indexical-character-learnable-content-supplied`](indexical-character-learnable-content-supplied.md),
> "The two halves")

The channel claim simply applies that same logic to a **tool-return**. A `get_current_time()` result, or a
`get_location()` result, is text the model reads — it arrives in the context window as a string the model
conditions on, exactly as a prompt-supplied date does. There is no architectural difference between "the
system prompt says it is June 30, 2026" and "a tool call returned `2026-06-30T14:00:00+09:00`": both are
described origos, both reach the model through the one channel. So a tool **does not convert a described
origo into an occupied one.** It only adds another *described* channel — a more dynamic, externally-sourced
one, but a described one all the same. This is the claim that does the work, and it is defensible precisely
because it is the parent essay's own channel logic, not a new premise.

**(iii) The behavioral *as-if* question — the genuinely testable residue.** Given a clock/location tool,
does the model *spontaneously treat tool-state as the deictic anchor* for an unanchored ‘now’/‘here’ —
querying the tool to resolve a bare "what time is it now?" rather than resolving from narrated text or
refusing? This is a real, runnable question about behavior. But a positive answer can show only that the
model *behaves as if* tool-state were its origo. It **cannot** certify that the model *occupies* a context;
it cannot settle (i). Behaving as-if-anchored and being-anchored come apart exactly where the project has
already learned they come apart — see the next section.

## The consequence for trigger (b)

Read through this three-way split, trigger (b) conflates (i), (ii), and (iii). A tool-clock probe tests
**(iii)** — does the model query the tool and treat the return as its ‘now’? It does **not** test (ii):
whether the tool-return is a described or an occupied origo is settled *before* the probe runs, by the
channel claim, and the channel claim says it is described (it is a string the model conditions on). And it
does **not** test (i): no behavioral output certifies that the model is the *agent* of a context, because
the same behavior is producible by a system that merely reads the tool-return as one more described input.

Crucially, by the parent essay's own channel logic, **even a clean positive on (iii) leaves (i) and (ii)
untouched.** The project has already seen the shape of this. [`essay/conversation-as-text-not-timeline`](conversation-as-text-not-timeline.md)
found that the models read a conversation's temporal "now" off **described** textual structure — physical
line position when available and sufficient, an explicit per-line round stamp when position is neutralized,
"SPONT latest-binding rate = 1.000 … Physical-position-following is at exactly chance"
([`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md), as cited in
[`essay/conversation-as-text-not-timeline`](conversation-as-text-not-timeline.md)) — not off a clock the
model inhabits. The model's temporal "now" tracked a *described* time-structure the text supplied; which
described cue governed was regime-dependent. A clock tool adds a fresh, externally-sourced described cue to
that repertoire; it does not give the model a timeline it is *on*. So the parent essay's already-recorded
re-reading — that the conversation finding is "character-application over a textual context, precisely
because there is no occupied one to apply it to"
([`essay/indexical-character-learnable-content-supplied`](indexical-character-learnable-content-supplied.md),
"A prediction the project can recognize") — carries straight over to the tool case: a tool-return is one
more textual context to apply the character to.

So the **strong** reading of the content half — claims (i) and (ii), that the model occupies no context
and that every origo reaches it as described text — is plausibly **premise-bound and not settleable by any
text-channel behavioral probe (tool-augmented or not)**. This is the same shape as two standing positions
of the project:

- [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) argued that whether an LLM's words
  *refer* is "premise-bound, not evidence-bound" — "no behavioral probe the project runs adjudicates it,"
  because "the parties already agree on every fact a probe could supply" and disagree only on a premise
  fixed "off-board." The architectural claim (i) has exactly that structure: whether the model *occupies*
  a context is not a hidden empirical fact a probe uncovers; both a deflationist and an inflationist can
  agree on every behavioral fact (the model queries the tool, reads the return, resolves ‘now’) and still
  disagree on whether that constitutes occupying a context. The disagreement lives upstream of behavior.
- [`essay/transcript-ceiling`](transcript-ceiling.md) argued that single-reader-recoverability is
  plausibly "a property of the medium, not the models" — a text-only probe "is **structurally ceilinged**"
  because "the probe's instrument and the criterion's denominator are the same object." The channel claim
  (ii) is a sibling: a tool-return is still text the model conditions on, so a text(+tool) probe cannot
  reach *outside* the described channel to find an occupied one. As that essay puts the discipline, the
  ceiling "bounds the medium, not the models" — and that is exactly the posture here. The limit is on what
  a text-channel probe can certify, not a claim that these models are impoverished.

Frame this, then, as a **documented in-principle limit**, the way the transcript ceiling is documented:
"A ceiling you can name is a map of where to stop digging" ([`essay/transcript-ceiling`](transcript-ceiling.md),
"Why naming the ceiling is itself knowledge"). Naming where the content half stops being probe-decidable is
knowledge, not a null result to be lamented.

## What stays testable, honestly scoped

The diagnosis does not close the corner; it *scopes* it. Claim (iii) — the *as-if* question — is the
genuinely-empirical residue, and it is worth running, provided it is labelled for what it is. The
companion [`conjecture/tool-origo-deictic-anchor`](../conjectures/tool-origo-deictic-anchor.md)
pre-registers exactly (iii) as a bounded behavioral bet, adopting this essay's conclusion as its ceiling
(a positive certifies neither (i) nor (ii)). The project
already has a clean precedent for staying inside the described regime and reporting only what that licenses:
[`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md) resolved
indexicals to their content "against a fully **described origo** at **ceiling**," and stated plainly that
the probe "deliberately stays in the **described** regime and so bears **only** on the character half. It is
**not** evidence on grounding, reference, or trigger (b) (an origo-occupying setup)"
([`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md), "What this
does and does not license"). A trigger-(b) tool probe should inherit exactly that discipline, with one
addition that this essay's three-way split makes mandatory:

1. **Scope the probe to (iii), the as-if question.** Measure whether the model spontaneously queries a
   clock/location tool to resolve an otherwise-unanchored ‘now’/‘here’, and treats the return as the anchor.
   That is runnable and informative.
2. **Label it explicitly as NOT certifying occupation.** A positive shows as-if-anchoring (the model
   behaves as if tool-state were its origo); it does **not** show the model occupies a Kaplanian context
   (i), and by the channel claim (ii) it does not convert the described tool-return into an occupied one.
   The result page must say so, the way the character-application result fenced its scope.
3. **Surface the operationalization gate before any stronger claim.** Before a run dares to read a positive
   on (iii) as bearing on (i) or (ii), the session should write a `wiki/decisions/open/` entry asking
   **"can any tool-return count as ‘occupied’, or is it still ‘described’?"** — the parent essay's
   [`NEXT.md`](../../../NEXT.md) already flags this exact question ("does a tool-supplied clock count as ‘occupied’ or still
   ‘described’?"). This essay's answer is that, under the channel claim, it is described; but that is an
   *argued* default, and a stronger claim must pass an independent adversarial-review ratification, not be
   smuggled in by a probe that only ever tested (iii).

## What this does NOT show

- **No human comparison, in either direction.** The essay makes a *structural* claim about what a
  text-channel (tool-augmented) probe of a model can and cannot certify about indexical content. It does
  **not** claim humans do or do not occupy contexts, nor that human and model deixis diverge or converge on
  any measured axis. `internal-contrast-only` posture is in force, as for the parent essay; every result it
  leans on ([`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md),
  the conversation-as-text findings) is itself internal-contrast-only.
- **Not a proof that the content half is untestable.** The claim is the careful one: the *strong* reading
  (claims (i)/(ii)) is **plausibly** not settleable by *text-only(+tool)* means. It is not a proven
  impossibility; it is a conjecture about the reach of a probe, hedged and carrying explicit revision
  triggers (below). A *non-text* route could move it.
- **The channel claim is the parent essay's, applied — not a new premise.** Claim (ii) extends the parent
  essay's own "a prompt-supplied date is a *described* origo" reasoning to tool-returns. If the parent
  essay's channel reasoning is wrong, so is (ii); this essay does not independently establish the channel
  premise, it inherits and applies it.
- **Claim (iii) is genuinely open and genuinely testable.** Nothing here says the as-if probe is pointless
  — the opposite: it is the one piece of trigger (b) a probe *can* reach, and the essay recommends running
  it, scoped. A positive on (iii) would be a real finding about behavior; it just would not certify (i) or
  (ii).
- **The Kaplanian factorization is contested.** As the parent essay and source page both flag, "The clean
  two-level character/content factorization is the *standard* frame the project leans on, not a settled
  theorem" ([`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md), Honest
  bounds). If the factorization fails, the three-way split this essay draws over the content half must be
  re-stated.

## Revision triggers (pre-registered)

This essay is a conjecture about the reach of a probe and is explicitly revisable. Each trigger names
evidence that would move it.

- **(a) A genuinely embodied / grounded / persistent-agent setup.** A finding in which the system is given
  a live context it plausibly *occupies* — not a text-channel tool-return but genuine perceptual/action
  [grounding](../../base/concepts/grounding.md) (in the sense [`concept/grounding`](../../base/concepts/grounding.md)
  decomposes: `grounded.perceptual`, `grounded.causal`, `grounded.social`), or a persistent embodied agent
  with its own clock/location as a non-described anchor — would move claim (i) from "plausibly not
  settleable by a text probe" to "in play," and would bound this essay explicitly to the *text-channel*
  regime (which is its intended scope; such a result would confirm the scoping rather than overturn the
  thesis).
- **(b) An extended-mind / active-externalist account on which tool-mediated access constitutes occupying
  a context.** A philosophical account that argues a tool the system reliably queries is *part of* the
  system's context-fixing apparatus — so that tool-mediated access to a clock just *is* the system
  occupying a temporal context — would **weaken claim (ii)** directly: it would deny that a tool-return is
  merely "another described channel" and re-classify it as constitutive of an occupied origo. The essay
  would then have to be re-stated as scoped to a non-extended-mind reading of "occupied."
- **(c) Kaplan's primary alters the character/content factorization (parent essay trigger (a)).** If
  Kaplan 1989a enters at primary strength and qualifies the character/content split (e.g. the "_usually_"
  hedge on character-as-linguistic-meaning, [`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md),
  §3.1), the three-way split this essay draws over the content half inherits that revision.
- **(d) An as-if (iii) probe result, with its scope.** A run that tests (iii) — does the model
  spontaneously treat tool-state as its deictic anchor? — would be folded in as a result about *behavior*,
  with the explicit scope that a positive shows as-if-anchoring and does **not** certify occupation (i) or
  convert the described channel (ii). A *negative* (the model does not treat tool-state as an anchor even
  when available) would be the more interesting outcome and would sharpen, not overturn, the essay.

> **Update (2026-07-01, session 156): trigger (d) FIRED — folded in, sharpening not overturning.**
> [`result/tool-origo-deictic-anchor-v1`](../results/tool-origo-deictic-anchor-v1.md) ran (iii) as a
> pre-registered 3-arm probe. The result is **neither a clean positive nor a clean negative but MIXED
> (control-failure)**: on the unanchored test arm the panel spontaneously queries the tool and binds the
> indexical to tool-state at ceiling (100%, 3/3) — which *looks* like the as-if positive — **but** the
> anchored control shows the same tool overriding a *narrated* origo 47–60% of the time, so the behavior
> is **generic tool-deference, not unanchored-specific origo adoption**, and the clean as-if reading is
> not obtainable. This **reinforces** the essay exactly as pre-committed: even the one behaviorally
> testable slice (iii) does not cleanly deliver "the model treats tool-state as *its* deictic origo," so
> claims (i) and (ii) remain untouched (and, as the essay predicts, *cannot* be reached by this channel).
> The scope-inheritance the essay demanded held: the result carries `internal-contrast-only`, makes no
> occupation claim, and left the deferred "tool-return = occupied?" gate unfired. No sentence of the
> argument below is retracted; this note logs the fold-in.

## Honesty box

- The essay's **original** contribution is the **three-way split** of the parent essay's content half —
  (i) architectural / (ii) channel / (iii) as-if — and the argument that a tool-clock probe tests only
  (iii), so the strong reading (i)/(ii) is plausibly not settleable by a text-channel behavioral probe.
  That diagnosis is the essay's own; the parent essay states the *ingredients* (the content half, the
  described-channel reasoning, trigger (b)) but not the split or its consequence for the trigger. **No
  empirical claim here is new.**
- The strongest thing the essay asserts is that **no text-channel (tool-augmented) behavioral probe
  certifies claim (i) or converts claim (ii)** — an argued structural claim about a probe's reach, in the
  same family as [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) (premise-bound) and
  [`essay/transcript-ceiling`](transcript-ceiling.md) (medium-bound), not a proof that no method whatever
  could. The limits section bounds it to the text-channel frame and to a non-extended-mind reading of
  "occupied"; triggers (a) and (b) name what would move it.
- **No human comparison** is made or owed: the posture is `internal-contrast-only`, every cited result is
  internal-contrast-only, and the claim is strictly about what a text-channel probe of an LLM can and
  cannot reach. No human-annotated resource is invoked or fabricated.
