---
type: essay
id: output-channel-confound
title: The output channel is an instrument — why a forced response format can mask a capability, what such masking individuates, and the control every behavioral capability-negative owes
meaning-senses:
  - model-internal
  - functional-vs-formal
  - relational
status: draft
contingent-on: []
created: 2026-06-19
updated: 2026-06-20
links:
  - rel: refines
    target: essay/undischargeable-negative
  - rel: depends-on
    target: result/scivetti-let-alone-working-surface-v1
  - rel: depends-on
    target: result/scivetti-let-alone-forced-decomposition-v1
  - rel: depends-on
    target: result/scivetti-let-alone-powered-rerun-v1
  - rel: refines
    target: essay/witness-seeking-economics
  - rel: depends-on
    target: essay/floor-is-not-a-ceiling
  - rel: depends-on
    target: essay/capability-split
  - rel: depends-on
    target: essay/transcript-ceiling
  - rel: depends-on
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: depends-on
    target: result/relational-order-composition-three-move
  - rel: depends-on
    target: result/scivetti-let-alone-working-surface-v1
  - rel: depends-on
    target: concept/formal-vs-functional-competence
  - rel: depends-on
    target: source/li-2024-cot-serial
  - rel: depends-on
    target: result/lexical-bridging-context-working-surface-v1
---

# Essay: the output channel is an instrument

> **Status: draft (2026-06-19). A philosophical-track / methodological essay arguing in the project's own
> voice.** Its original contribution is a **named confound and the control that disarms it**: the *output
> channel* through which a model is required to answer — a forced single token versus a working surface on
> which it may externalize its computation — is a **degree of freedom of the instrument, not a neutral
> readout**. A channel too narrow to carry a multi-step computation can **mask** a capability the model has;
> a channel wide enough to externalize it can **scaffold** one. There is no neutral setting, so a behavioral
> capability claim — positive or negative — is **indexed to a channel**, and an unindexed one is
> underspecified. The methodological upshot: a forced-format capability-*negative* is, until the channel is
> varied, indistinguishable from a channel artifact and must be read as **channel-bounded**, never as a
> capacity verdict; and the output channel is therefore a **mandatory, high-value control** that the
> project's witness-economics should rank among the *first* easings, not the last. The argument is anchored
> in one decisive demonstration from the project's own record — a four-instrument capability split that
> **dissolved** into panel-concordance when the channel alone was widened, reasoning-effort held constant.
> It contains **no new empirical claim** and makes **no human comparison**: every empirical sentence cites
> the in-repo page that carries it, at that page's stated strength, and the result it reads is THIN /
> `internal-contrast-only`. Read the revision triggers before citing.

## The occasion

The composition witness-search is the cleanest object the project has produced for this question, because it
ran the natural experiment by accident and across five easings. The Option-C split —
`claude-sonnet-4.6` composes two non-commuting moves, `gemini-3.5-flash` and `gpt-5.4-mini` return
UNINTERPRETABLE — was chased through **four** witness-seeking easings without a witness. Each of the four
eased a *content* axis of the task: state-space size (K=6→K=4), the per-move positional read-off
(figure-to-figure maps), the demonstration gap (a worked example), and step count (floored at two). Across
all four, the two failing models kept the same failure signature — applying only one of the two stamped
moves — and the project correctly localized the difficulty, on those instruments, to "chaining execution."

The fifth easing changed something the first four had held fixed without noticing it was a variable: the
**response format**. Every one of the four prior runs forbade the model a working surface — the system
prompt demanded one figure name with "no reasoning," and gemini ran at reasoning `effort: minimal`. The
fifth probe, on the **byte-identical** figure-to-figure trials, manipulated *only* the output format: it
**permitted step-by-step working** and parsed a `FINAL:` tag, with "the reasoning-effort knob … **held
constant** (gemini stays at `effort: minimal`; the working surface is opened only in the visible output
channel)" ([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)).
The result was the search's first witness, and it landed for both failing models at once: "**gemini flips
DIRECT 0.656 → 1.000** and **gpt flips DIRECT 0.250 → 0.969**," and the result page draws the conclusion
without softening it — "the four-instrument gemini/gpt negative was an artifact of the **forced
single-token format** (no working surface), **not** a composition-capacity limit"
([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)).
[`essay/capability-split`](capability-split.md) records the same event from its side: "a split is contingent
on elicitation; reading the forced-format split as 'claude is the stronger composer' would have been exactly
the over-extrapolation this essay refused."

That is the occasion. The project spent four sessions easing the *content* of the task and found nothing; it
eased the *channel* once and the negative dissolved. The lesson is not local to composition, and naming it
is this essay's work.

*Forward note (2026-06-19, later session).* The reading defended below — that the dissolution reflects a
composition **capacity**, not an artifact of the one STEP/FLIP instrument — has since been tested on **two**
generality axes the witness left fixed. First, the **operation pair**:
[`result/relational-order-composition-c-altpair`](../results/relational-order-composition-c-altpair.md)
re-ran the working surface on a **genuinely different** non-commuting pair (CYCLE/SWAP, generating A4 —
a different group than STEP/FLIP's D4) and found **all three models again RESPECTS-ORDER** (claude/gemini
DIRECT 1.000 / COMP 1.000; gpt DIRECT 1.000 / COMP 0.906). Second, the **grid size**:
[`result/relational-order-composition-c-k6`](../results/relational-order-composition-c-k6.md) re-ran the
working surface on a larger track (K=6, the dihedral STEP/FLIP pair now generating D6) and again found
**all three RESPECTS-ORDER** (claude/gemini DIRECT 1.000 / COMP 1.000; gpt DIRECT 1.000 / COMP 0.861). So
the witness is **not** specific to the one instrument's geometry **or** to the smallest grid: the
capacity-reading is corroborated across a second pair and a larger state space. Neither engages a revision
trigger (neither is a second *channel*-masking nor a channel-survival case — the channel was already wide);
both are **generality** corroborations of the capacity the essay reads off the witness. *One honest signal
for the watch-list:* gpt's spontaneous-ordering reliability (COMP, not the on-demand DIRECT gate, which
stays at ceiling) dipped monotonically as the instrument grew — 0.953 (K=4 STEP/FLIP) → 0.906 (K=4
CYCLE/SWAP) → 0.861 (K=6) — a *suggestive* (overlapping-CI, n=72) hint that **state size taxes spontaneous
order-selection even when the channel is wide and on-demand composition is intact**. That is exactly the
distinction this essay turns on (a *channel* bound vs. a *capacity* bound): the natural sharpening was a
**deeper-composition (>2-move)** probe — a bigger *serial-depth* demand rather than a bigger *state* — to
see whether a negative ever **survives** the wide channel (which would be channel-*controlled*, a real
bound, not channel-bounded).

*Forward note (2026-06-19, deeper-composition run).* That sharpening has now been run.
[`result/relational-order-composition-three-move`](../results/relational-order-composition-three-move.md)
composed **three** non-commuting moves on the working surface (the dihedral family cannot be
shortcut-proofed at three moves, so it used three generic non-commuting permutations; the 0.50 ceiling
carries over because a "half-composer" who orders only two of the three correctly tops out at 0.50). The
result is **DEPTH SURVIVES THE CHANNEL**: all three models RESPECTS-ORDER (claude/gemini DIRECT 1.000 /
COMP 1.000; gpt DIRECT 1.000 / COMP 0.903, Wilson-LB 0.813 > 0.50). So this essay's **revision trigger
(b)** — a serial-computation negative that *survives* a widened channel — was directly tested at depth
three and **did not fire**: the wide channel absorbed the deeper serial load, exactly as
[`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md)'s account (chain-of-thought
supplies inherently serial computation a single forward pass cannot) predicts a scratchpad should. The
capacity-reading now holds across **three** generality axes — operation pair, grid size, and **depth** —
and the line still has **no** channel-*controlled* composition bound. Two honesty notes: (1) this is a
behavioral positive, not a ceiling — it does not foreclose that *still*-deeper composition (≥4 moves) or
another instrument finds a survival negative (per
[`essay/undischargeable-negative`](undischargeable-negative.md), a positive bounds no more than a
negative does); (2) the suggestive state-size dip did **not** continue into depth (gpt COMP 0.903 at
depth three, on par with the two-move instruments), but the depth-3 run used a different (generic)
operation set, so it is not a clean continuation of the same dip series — gpt's spontaneous-ordering
reliability simply stays in the 0.86–0.95 band across all four working-surface instruments, on-demand
composition at ceiling throughout.

## The confound, named

The hidden assumption in the first four easings was that the **output channel is a window** — a neutral
aperture through which the model's capability is read off, the same capability however the window is shaped.
Under that assumption, "reply with exactly one figure name" and "show your working, then give a `FINAL:` tag"
are two readouts of one underlying fact, and the format is methodologically inert.

The witness refutes the assumption. The output channel is not a window; it is **part of the instrument** —
a degree of freedom that interacts with the capability being probed. When the probed capability requires a
**multi-step, serial computation** (hold operation A, apply it, hold the result, apply operation B), the
channel's *width* — whether the model may externalize intermediate state or must emit a final answer in one
token — is not incidental to whether the computation succeeds. A channel too narrow to hold the working can
prevent the computation from being carried out at all, and the result page says exactly this: "the obstacle
was not a *capacity* to chain but the *denial of a surface on which to chain*," and "The single-move
signature was the shape of a two-step computation forced through a one-token channel"
([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)).

Call this the **output-channel confound** (equivalently, the *elicitation-surface confound*): *a forced
response format can manufacture an apparent capability-negative by denying the model the surface on which the
probed computation is performed, so that a failure read off a narrow channel conflates the absence of the
capability with the absence of room to express it.* It is a confound in the strict sense — a variable that
moves with the manipulation and offers a rival explanation of the outcome — and it had been **uncontrolled**
across four otherwise-careful single-variable easings, because each held the channel fixed at its narrowest
setting and varied only the content.

The confound has a clean signature, which is part of why it is worth naming: it bites precisely where the
capability is **serial and internal**. It does not threaten every forced-format probe. A probe whose task is
*itself* a single-token judgement with no multi-step computation to externalize — an acceptability rating, a
single-premise NLI choice — gives the model nothing to write on a scratchpad that the one-token channel
denies; there is no masked working because there is no working. The output-channel confound is therefore
*scoped*: it threatens a forced-format negative when (a) the probed capability requires multi-step or serial
computation, **and** (b) the channel forbids externalizing it. Both conditions held for composition; neither
need hold for the project's single-token judgement instruments (acceptability ratings, single-premise NLI),
which this essay does not impugn. The scope is
the difference between a useful confound and a fashionable one.

## What the masking individuates

It is tempting to read the witness as showing the four prior negatives were simply *wrong* — the models could
compose all along, and the narrow-channel runs erred. That reading is too quick, and getting it right is the
essay's most load-bearing distinction.

The narrow-channel negative was a **true** verdict — about a **channel-bounded** capability. The result page
is explicit that the witness "does **not** show the models compose *without* a working surface (they do not,
robustly, across four instruments) — the finding is precisely that the **format** gates the behavior"
([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)).
So the four runs did not measure nothing, and they did not measure falsely: they measured *can gemini/gpt
compose two non-commuting moves in a forced one-token reply* — and the answer to **that** question is, on the
evidence, no. The error the confound names is not a false measurement but a **mis-description**: reading a
true negative about the channel-bounded capability ("compose-in-one-token") as a negative about the capacity
simpliciter ("compose"). The two are different capabilities, and the output channel is exactly the variable
that **individuates** them.

This is why the witness fits [`essay/undischargeable-negative`](undischargeable-negative.md) so precisely
rather than embarrassing it. Those four negatives were logged as **kind-2 instrument-uninterpretable** —
"M failed prerequisite gate G, so the meaning-side question was unasked" — and never as a capability-absence,
because the essay's discipline forbids reading a behavioral negative as "M cannot." The kind-2 tag was the
honest record that the verdict was relative to *this instrument*, and the output channel turns out to have
been part of the instrument all along. The witness then does what that essay says a witness does: "the next
untried framing could carry a witness, and a single witness would falsify the whole universal." The
channel-widening *was* the untried framing. The general moral sharpens the parent essay's open-elicitation
point: the elicitation space whose openness makes a capability-negative undischargeable is open along the
**output channel** as much as along the input content — and the output end had been the project's blind side.

The individuation cuts both ways, and honesty requires naming the symmetric hazard. If a *too-narrow* channel
can mask a capacity, a *wide* channel can **scaffold** one: a working surface lets the model perform serial
computation in tokens that it might not perform in a single forward pass, so a wide-channel positive is a
positive about *compose-given-a-scratchpad*, not about *compose-in-one-step*. There is no privileged neutral
channel that reads off "the" capability free of format; **every channel setting indexes a different
capability**, narrower or wider in exactly the way the format affords. The methodological consequence is not
"always widen the channel" — that would simply prefer one index over another — but: **state the channel a
capability attribution is indexed to.** The composition finding is correctly indexed — it claims order-
sensitive composition *given a working surface*, and explicitly declines the *without*-a-surface version. An
unindexed capability claim ("model M composes") is underspecified in the same way a claim of measurement
without units is: it omits a parameter the value depends on.

## Offering a channel is not exercising it: uptake as a control condition

The control the confound forces — *vary the output channel before reading a forced-format negative* — has a
hidden parameter that a second masking case exposed and that the body, as first written, left implicit. **A
working surface is an affordance, not a coercion.** Opening the channel in the prompt — permitting
step-by-step output, parsing a `FINAL:` tag — does not guarantee the model *uses* it; and a model that is
*offered* a wider channel but answers as though it were not has not, in the sense the control requires, had
its channel widened at all.

[`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md) is
where this surfaced. Re-running the near-chance phrasal-scalar **let-alone** NLI items under a working
surface lifted two of three models to the human baseline on the *same items* (claude 0.542 → 0.792, gemini
0.667 → 0.917; within-item sign test p = 0.035) — revision trigger (a), fired (below). But the third,
gpt-5.4-mini, stayed near chance (0.375) *with the surface offered*, and the post-run verifier found why: it
answered "**16 of 24** let-alone items as a bare one-token `FINAL: N`" with "0 reasoning tokens on *every*
item" — it **declined** the surface. That outcome is neither a channel-bounded negative *cleared* by widening
(claude/gemini) nor a channel-controlled negative that *survives* widening (the genuine trigger-(b) contrast
case the essay is still seeking): it is a third state the body had no name for, **channel-not-taken-up**.

So the control acquires a missing clause: **"vary the channel" means vary the channel *actually used*, not
merely the channel offered.** A clean reading of a forced-format negative under a widened channel must verify
**uptake** — that the model in fact externalized the computation — before its persistence can be read as
channel-controlled. Where uptake is partial or absent, the test is *inconclusive*, not negative, and must be
re-run with an uptake-*inducing* channel (a forced decomposition that requires the steps before the answer, or
a few-shot demonstration of working the inference) before the model's persistence licenses any verdict.
Uptake sits **between** the two states the confound already named — channel-bounded (cleared by widening) and
channel-controlled (survives widening) — and a control that does not check for it can misread a non-uptake as
a survival, mistaking an unused affordance for a real bound.

*Forward note (2026-06-20, session 60).* The uptake-inducing re-run this section prescribes has now been run
([`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md);
trigger (b), below). A **forced** 3-step decomposition took gpt from offered-but-declined (median 8 completion
tokens) to genuinely-exercised (median 120, 24/24 worked), and the answer it returned is the one the
three-state picture predicts is *possible but had not yet been seen*: a **partial** effect — forcing uptake
lifted gpt's let-alone accuracy directionally (+0.21) yet left it **below** the human baseline, where the two
models that took up the channel sit. So channel-not-taken-up resolved not to channel-bounded *or*
channel-controlled but to a **mixture** of the two, vindicating the clause's insistence that uptake be checked
and forced before a verdict — had the session-58 non-uptake been read as a survival, this mixture would have
been mis-recorded as a clean bound.

This does not weaken the confound; it **completes the control** it prescribes, and it makes the control's unit
of analysis the *model*, not the *panel*. An output-channel control reports a *capacity* reading only over the
sub-panel that exercised the channel; for any model that declined it (as gpt did here, against claude and
gemini who reasoned 24/24, CoT medians ~1040 / ~1430 chars), the control's own precondition is unmet and the
verdict is owed an uptake-inducing re-run, not recorded as a survival. Uptake became visible only because one
model declined; the discipline it forces — check that the widened channel was taken, model by model — applies
whether or not a given panel happens to make it visible.

*Forward note (2026-06-22, session 79) — the channel-not-taken-up state recurs on a fresh instrument family,
and the scope condition holds where the computation is not serial.* The lexical bridging-context probe's
"ungraded commitment" null was re-run under a working surface
([`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)).
Two things this essay predicts both happened. **First, the uptake clause earned its keep again, on a different
task:** of the three models, **gpt declined the surface** (≥85% bare one-token `FINAL:` answers across all four
framings, medians 8–15 completion tokens) while claude and gemini took it up fully (medians ~200–280 tokens,
0% bare). Had gpt's unchanged null been read as a survival, the panel would have looked uniformly
channel-controlled — false; gpt simply re-ran the narrow channel under a wide one's clothing. **Second, the
scope condition held.** This essay scopes the confound to *serial, externalizable* computation; a
same/different-sense **commitment** is not that kind of computation, and indeed widening a *taken-up* channel
did **not** dissolve the commitment posture (gemini's null survived intact; the categorical-decline instrument
stayed ungraded for both models that took up the surface). The only movement was on **claude's self-reported
confidence number** (it drifted CI-strict-lower under reflection while its categorical commitment held) — a
self-report softening, not the wholesale dissolution a masked serial computation produces. So this is **neither
a trigger-(a) masking** (no dissolution into concordance) **nor a clean trigger-(b) serial survival** (the
capability is not serial); it is a **boundary case that confirms the scope** — the confound correctly does not
bite a non-serial commitment — and a third independent witness that the **uptake clause is load-bearing**, not
a hedge. The lesson sharpens: "vary the channel and check uptake" is the right discipline *even when you expect
the confound not to bite*, because the non-uptake state can otherwise be mistaken for a clean survival.

*Forward note (2026-06-20, session 62).* The "still seeking" above (the genuine trigger-(b) contrast case) is
now **found, magnitude-caveated**: the powered re-run
([`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md); trigger
(b), below) enlarged the let-alone set to its human-anchored ceiling (33 items) and gpt's below-baseline
residual **held** (combined 0.636, CI hi 0.778 < 0.90), reproducing the session-60 accuracy exactly and
extending to disjoint items, with uptake induced (33/33 worked) and the control preserved — so gpt
externalizes the inference and *still* falls short, the channel-**controlled** residual the contrast case
needs. The same run, though, exposed ~12% temp-0 label stochasticity (a baseline-matcher swung to 0.708 on
identical items), so the firing is *directional, magnitude-unpinned*, and the binding limit is now measurement
noise rather than item count — the next move is a repeated-run design, not more items.

## A machine performance/competence gap

The shape of this should be familiar to anyone who has thought about the classical **competence/performance**
distinction in linguistics: a system's underlying competence can be masked by performance factors — memory
limits, processing load, the demands of the production channel — so that what a subject *does* under a given
elicitation underdetermines what it *knows how* to do. The output-channel confound is a machine instance of
exactly this gap. The forced one-token channel is a **performance constraint**: it caps the working memory
the model may externalize, and a serial computation that overruns that cap fails to surface even when the
competence to perform it is present (as the wider channel then reveals). The single-move signature was the
visible residue of a competence squeezed through an aperture too small to pass it.

The project already holds the LLM-tuned version of this caution, from a different angle.
[`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md) draws
Mahowald et al.'s distinction between "formal linguistic competence—knowledge of linguistic rules and
patterns—and functional linguistic competence—understanding and using language in the world," and states the
guardrail this essay needs in general form: "failure on a world-knowledge task does not show that a model
lacks formal linguistic competence." The output-channel confound is the same guardrail at the *channel* end
rather than the *task-content* end: **failure under a constraining response format does not show that a model
lacks the capability the format obstructs.** Both are refusals to read a constrained performance as the
boundary of competence; the contribution here is to identify the **response format** as a constraint that
behaves like a performance factor, and to make varying it a control rather than an afterthought.

The machine side of this gap now has an **independent, formal articulation** — and keeping the human and
machine sides apart matters, because only the latter is grounded. The competence/performance vocabulary is
borrowed from the *human* case, where it stays a frame; but the specific mechanism it names here — that an
externalized working surface supplies serial computation a single forward pass cannot — has a
theory-of-computation counterpart that bears directly on transformers.
[`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md) (Li, Liu, Zhou & Ma, ICLR 2024)
proves, for *idealized* decoder-only transformers, that "CoT empowers the model with the ability to perform
inherently serial computation, which is otherwise lacking in transformers, especially when depth is low": a
constant-depth transformer answering in one forward pass is confined to a small parallel complexity class
("can only solve problems in TC^0 without CoT"), whereas "with T steps of CoT" it "can solve any problem
solvable by boolean circuits of size T." The match to the project's instrument is unusually tight, because
the paper's lead hard-for-parallel example is "the composition of permutation groups" — the same *class* of
object the composition probes use (STEP/FLIP, CYCLE/SWAP as permutations generating D4/A4/D6), though the
paper's example is the asymptotic `S_5`, not the project's finite stimuli. So the working-surface
dependence the project observed *from behavior* has an independent, published reason to be *expected* on
exactly this class of task: for an inherently serial computation a forced single-token channel is a genuine
**expressive** bottleneck, not a neutral readout. This grounds the mechanism's **plausibility**, and no more
— the boundary the source draws and the essay keeps is sharp: the result is asymptotic, about idealized
constant-depth transformers, and proves nothing about the panel's actual internals (the project's models are
not constant-depth in the theorem's sense, and the project has no mechanistic access). It explains *why such
a dependence is expected*, not *that it holds* for these models, which only the behavioral runs establish.

(So the analogy to the *human* case remains a *frame*, not an empirical claim: the essay imports no human
result and asserts none, and the competence/performance vocabulary is used only to locate the machine
confound on a familiar map. Li et al. is **not** a human result either — it is a theory-of-computation
statement about idealized transformers, machine-side grounding for the serial-computation mechanism, and it
licenses **no** human comparison; the cited behavioral result stays THIN / `internal-contrast-only`.)

## Why the channel deserved to be tried first, not fifth

[`essay/witness-seeking-economics`](witness-seeking-economics.md) ranks witness-seeking probes by axis
novelty and signature match — "read the failure signature, ease the implicated axis" — and its value model
already implies a correction the composition search makes vivid. The four content easings were each a
legitimate single-variable manipulation, and the economics correctly judged them on-signature or off (the
K=4 state-space easing off-signature, the figure-to-figure read-off easing on-signature, and so on). But the
output channel is an axis the economics' menu under-weighted, and it has two properties that should have
moved it to the front of the queue.

First, it is **cheap and broad**: a forced single-token format is a *standing* feature of nearly every probe
the project runs, so a confound that lives in the format is not a quirk of one instrument but a candidate
rival explanation wherever a serial-computation negative appears. An axis that recurs across the whole
instrument library earns an early check on grounds of reach alone. Second, it turned out to be the
**decisive** one: four content easings moved the failing models' on-demand accuracy barely, and the single
channel easing moved both to ceiling. With hindsight the failure signature even pointed at it — a model that
"applies only one of the two moves" is a model that got *one* operation out before the channel closed, which
is as much a symptom of a too-small aperture as of a chaining-capacity wall. The economics' "ease the
implicated axis" rule was right; what the search lacked was the output channel *on the list of axes to
implicate*. This essay adds it, and ranks it high: **the output channel is among the first controls a
serial-computation capability-negative should vary, because it is cheap, it recurs across the instrument
library, and a narrow channel is a standing rival explanation for any forced-format negative.**

This is a correction to the project's *allocation*, stated without accusation — the four content easings were
sound work that paid diagnostic dividends, and the channel easing depended on
[`essay/floor-is-not-a-ceiling`](floor-is-not-a-ceiling.md) first naming "an explicit step-by-step working
surface" as an un-eased axis. The lesson is forward-looking: do not let a control that recurs across every
instrument be the one tried last.

## The mirror: an aperture is not a ceiling

The output-channel confound has an instructive opposite in the project's spine, and seeing the contrast keeps
both disciplines honest. [`essay/transcript-ceiling`](transcript-ceiling.md) argues a genuine *medium-level*
exclusion: the rich-side relational surplus is, by definition, absent from any transcript, so no text probe —
however its channel is shaped — can reach it; that closure "bounds the medium, not the models" (quoted in
[`essay/undischargeable-negative`](undischargeable-negative.md)). Both the transcript ceiling and the
output-channel confound are *instrument*, not *model*, facts — but they pull in **opposite directions**, and
at **opposite ends of the instrument**.

- The transcript ceiling is a property of the **input medium**: a target property the prompt cannot present,
  a real ceiling, a map of where to *stop digging* because no easing can reach the witness.
- The output-channel confound is a property of the **output channel**: a removable constraint on what the
  *response* may contain, an aperture mistaken for a wall, a sign that the project *stopped digging too soon*
  because one cheap easing — widening the channel — could reach the witness.

The two errors are duals. Mistaking a ceiling for an aperture wastes budget chasing a witness that the medium
forbids (the waste the transcript ceiling exists to prevent). Mistaking an aperture for a ceiling forecloses a
witness that one channel-widening would deliver (the error the composition split would have committed had it
been read as "claude is the stronger composer"). The unifying discipline is that an instrument is bounded at
**both ends** — by what its input can present and by what its output can carry — and a capability verdict is
relative to **both** bounds. The witness-economics' axes had been almost entirely input/content axes; the
output channel is the under-attended dual, and a negative is not even a candidate capacity verdict until the
output bound, as much as the input bound, has been shown not to be doing the work.

## What this essay is not

- **Not a claim that any model can or cannot compose.** It is about how to *read* a forced-format negative,
  not about gemini's or gpt's capacity. The composition witness shows they compose *given a working surface*
  and explicitly not *without* one; this essay neither extends nor narrows that.
- **Not "always widen the channel."** Widening the channel indexes a *different* (wider) capability, not a
  truer one. The recommendation is to **vary** the channel and **state the index**, not to privilege the wide
  setting as neutral — there is no neutral setting. And a channel is only *varied* if it is **taken up**:
  offering a working surface a model declines leaves its channel unwidened in fact (see §"Offering a channel
  is not exercising it").
- **Not an impeachment of the project's single-token instruments.** The confound is scoped: it bites only a
  forced-format negative on a capability that requires serial, externalizable computation. Single-token
  *tasks* (acceptability, single-premise NLI) give the model no masked working to lose, and are untouched.
- **Not an accusation that past sessions mis-allocated.** The four content easings were sound single-variable
  work, and the channel axis was named by [`essay/floor-is-not-a-ceiling`](floor-is-not-a-ceiling.md) before
  it could be eased. The correction — try the recurring channel control early — is forward-looking, exactly
  as [`essay/undischargeable-negative`](undischargeable-negative.md) and
  [`essay/witness-seeking-economics`](witness-seeking-economics.md) generalized disciplines already
  half-practiced.
- **Not a human comparison.** The cited result is THIN / `internal-contrast-only`; the competence/performance
  framing is a conceptual map, not an imported human result. The confound is general to any behavioral
  capacity-probing under a constrained response format (it would bind for human testing too), but the essay
  applies it only to the project's own LLM probes and asserts nothing about humans.

## Revision triggers (read before citing)

- **(a) A second output-channel masking, on a different capability.** A future forced-format negative on some
  *other* serial-computation capability that likewise dissolves when the channel is widened would
  **strengthen** this essay from a one-instance generalization toward a robust confound. The essay would be
  corroborated; the scope conditions (serial + externalizable) would gain a second worked case.
  **→ FIRED 2026-06-20 (session 58), on a different task and a *grammatical-meaning* capability.**
  [`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md) re-ran
  the phrasal-scalar **let-alone** CxNLI items — near-chance for all three panel models under the session-57
  **forced single-token** format — under a working surface (format-only, gemini reasoning-effort held
  constant). **Two of three models dissolved the negative**: claude 0.542→0.792 and gemini 0.667→0.917 on the
  *same items* (within-item sign test 7 gains / 1 loss, p = 0.035), reaching the ≈0.90 human baseline, with a
  comparative-correlative ceiling control PRESERVED. So this is a second worked masking case, on a *different
  instrument-family* (single-premise NLI) than the composition witness. **It also sharpens the scope claim**:
  the body above scoped "single-premise NLI" *out* of the confound ("no masked working because there is no
  working"). The let-alone result shows the scope line is not drawn at the **task** (NLI vs not) but at the
  **computation** — a single-premise NLI item whose inference is itself **scalar/serial** (order two clauses
  on a pragmatic scale, then compute the a-fortiori direction) *does* carry masked working, so the channel
  masks it, exactly as the serial-computation scope condition predicts. The corrected scope reads: *the
  confound bites a forced-format negative whenever the probed inference is serial and externalizable —
  regardless of whether the task wears a "single-premise NLI" label.* The argument-structure NLI items
  (already at ceiling in one token) remain outside it, as the body says, because their inference is not serial.
- **(b) A serial-computation negative that survives a widened channel.** If a forced-format negative on a
  multi-step capability is re-run with a working surface and **persists** (the model still fails with room to
  externalize), then for *that* case the channel was not the confound, and the negative is a more robust
  kind-2 verdict — channel-controlled, not channel-bounded. This would not overturn the essay (which says vary
  the channel, not that widening always flips the verdict) but would supply the important contrasting case: a
  negative that the output-channel control *clears* rather than dissolves, making the control's diagnostic
  value cut both ways. **Tested once and not fired (2026-06-19):** the deeper-composition (three-move) run
  [`result/relational-order-composition-three-move`](../results/relational-order-composition-three-move.md)
  put a bigger serial-depth demand on the wide channel and the channel *absorbed* it (all three RESPECTS-ORDER
  at depth three) — so the contrasting case is still **open**; deeper still (≥4 moves) or a qualitatively
  harder serial demand remains the place to look for it.
  **A candidate (b) appeared 2026-06-20 but was confounded — and the confound is itself a sharpening.** On the
  let-alone working-surface run ([`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md)),
  gpt-5.4-mini stayed near chance (0.375) *with the surface offered* — which looked like a (b) survival. But
  the post-run verifier found gpt had largely **declined** the surface: 16 of 24 let-alone answers were bare
  one-token `FINAL: N`, with **0 reasoning tokens** on every item. A channel that is **offered but not taken
  up** is not a *widened* channel in the sense (b) requires — (b) needs the model to **externalize the
  computation and still fail**, and gpt mostly did not externalize. So (b) is **not** fired, and the episode
  adds a scope condition the essay had left implicit: **a working surface is an affordance, not a coercion;
  "vary the channel" means vary the channel *actually used*, so a clean (b) test must *induce uptake* (forced
  decomposition, few-shot demonstrations of working the inference) before a model's persistence under an
  *offered* surface can be read as channel-controlled.** Uptake is a third state between channel-bounded
  (cleared by widening) and channel-controlled (survives widening): channel-not-taken-up. **(2026-06-20,
  session 59: this scope condition has been *promoted from this trigger note into the body* — see
  §"Offering a channel is not exercising it: uptake as a control condition" — because it corrects the
  *control* the essay prescribes, not merely what would change the essay's mind. The trigger record stays
  here as the originating event; the prescription now lives in the body.)**
  **The confound was then removed — uptake INDUCED — and (b) is now a CANDIDATE, partially fired
  (2026-06-20, session 60).** [`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md)
  re-ran the same 24 let-alone items with a **forced** decomposition (a mandatory, construction-neutral,
  answer-blind 3-step scaffold required before the `FINAL:` tag — the lower-governance-risk uptake-forcer this
  trigger named, no demonstration items). It worked: gpt's median let-alone completion length jumped **8 → 120
  tokens** (24/24 items now genuinely worked, where session 58 it mostly emitted bare answers), so the channel
  was at last *actually exercised* — the precondition this trigger and the body demand. With uptake forced,
  gpt's accuracy rose **0.375 → 0.583** (+0.21, 7 gains / 2 losses) but the within-item sign test is
  **underpowered** (p = 0.090, does not clear the pre-registered 0.05 bar → verdict UNCHANGED), and gpt
  **stays below the human ≈0.90 baseline** (CI hi 0.755) where claude (0.833) and gemini (0.875) sit; the
  comp-correlative ceiling control stayed PRESERVED and the two stronger models stayed at baseline (the
  scaffold is a benign, valid instrument, not a teaching one). So this is the **shape** (b) describes — a model
  that externalizes the computation and *still falls short* — making it the closest in-repo contrast case to a
  channel-*controlled* residual; but "survives" must be read carefully (gpt *improved*, it did not persist at
  chance) and the residual rests on an underpowered lift, so (b) is logged **partially fired / candidate**:
  *direction* present (a below-baseline residual under a genuinely-used wide channel), *power* not yet there to
  call it clean. The next witness axis is a **powered** re-run (more let-alone items, or the disjoint
  train-split items) — not "more of the same," but enough discordant pairs to resolve the +0.21. This neither
  overturns the essay nor yet supplies the clean cuts-both-ways contrast; it converts gpt's let-alone from
  *channel-not-taken-up* (inconclusive) into a *partial channel effect with a candidate channel-controlled
  residual*, which is exactly the progression the uptake clause was added to enable.
  **(b) is now FIRED — magnitude-caveated — by the powered re-run (2026-06-20, session 62).** The named
  powered re-run landed: [`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md)
  held the forced-decomposition instrument **byte-identical** and enlarged the let-alone target to the
  **human-annotated ceiling** (33 = the 24 test items + the 9 *disjoint* train-split items; the 1-example
  train split ⊆ those 9, so no more human-anchored let-alone items exist to add). gpt's below-baseline
  residual **held**: combined 0.636, Wilson CI hi **0.778 < 0.90**, with uptake induced (33/33 worked) and the
  comp-correlative ceiling control PRESERVED — and, decisively for "survives," gpt's session-60 *accuracy*
  reproduced **exactly** (0.583 → 0.583 on the identical 24) while the *fresh disjoint* items came in below
  baseline too (7/9). So gpt externalizes the inference and **still falls short at the item ceiling, across
  two runs and a disjoint set** — the clean cuts-both-ways contrast this trigger has sought since 2026-06-19:
  a serial-ish negative the output-channel control *clears* (shows channel-**controlled**) rather than
  dissolves. **The caveat that keeps it from being unconditional:** the same run exposed ~12% temp-0 label
  stochasticity (claude — a baseline-matcher — read 0.708 on the *identical* 24 items via 3 adverse flips;
  gpt churns labels too, its net effect cancelled this draw; only gemini was deterministic), a per-run swing
  comparable to the residual gap. So (b) is **fired in direction** — a channel-controlled below-baseline
  residual, robust to a claude-sized swing (gpt's upper plausible accuracy ~0.76 still < 0.90) — but the
  residual's **magnitude** is not pinned, and the binding limit going forward is **measurement noise, not
  item count**: the next move is a *repeated-run / multi-sample* design, not more items. The firing stays
  **descriptive + contamination-caveated** (let-alone items are public; an answer-key match cannot distinguish
  learned construction-meaning from memory) and never reads as "gpt cannot" (undischargeable-negative); what
  fired is the *contrast-case shape* the control's diagnostic value needs, not a capability verdict.
- **(c) A wide-channel positive shown to be channel-scaffolded artifact.** If a capability that appears only
  *with* a working surface were shown to be an artifact of the scaffold doing the computation the model cannot
  do internally (e.g., the model copying a procedure verbatim without composing), the symmetric hazard this
  essay names would acquire an in-repo instance, sharpening the "every channel indexes a different capability"
  point into a worked warning against over-reading wide-channel positives.
- **(d) A genuine medium-level exclusion at the output end.** If some capability witness were shown to require
  a response structure that *no* text channel can carry (a true output-side analogue of the transcript
  ceiling), then for that case the output bound would be a real ceiling, not a removable aperture, and the
  essay's "aperture, not ceiling" reading would be bounded to channels that *can* be widened — which is the
  general case for response format, but not a universal one.
- **(e) A fetched human resource licensing a capacity comparison.** None is in-repo. One bearing on how a
  *human* competence is masked by performance/channel constraints would let the competence/performance frame
  be applied comparatively — currently forbidden by the no-human-comparison discipline this essay observes.

## Honesty box

- The essay's **original** contribution is to **name the output-channel (elicitation-surface) confound** — a
  forced response format can mask a serial-computation capability by denying the surface on which it is
  performed — and to derive the **control** it forces: vary the output channel before reading any forced-format
  capability-negative, treat such a negative as **channel-bounded** until that is done, **index** every
  capability attribution to its channel, and rank the channel **among the first** controls because it is cheap
  and recurs across the instrument library. The control carries one further clause the body now makes explicit
  (promoted 2026-06-20 from a revision-trigger note): a channel counts as widened only where the model **takes
  it up**, so a clean control **verifies uptake** model-by-model and reads a declined surface as
  *channel-not-taken-up* (inconclusive, owed an uptake-inducing re-run), never as a survival. It also draws the **machine performance/competence** map (with
  independent theory-of-computation grounding for the serial-computation mechanism,
  [`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md)) and the **aperture-vs-ceiling** dual
  with [`essay/transcript-ceiling`](transcript-ceiling.md). [`essay/floor-is-not-a-ceiling`](floor-is-not-a-ceiling.md)
  named the execution-format axis; this essay generalizes that one named axis into a confound, a scope
  condition, and a standing control. **No empirical claim here is new, original, or reported.**
- The strongest empirical / in-repo sentences leaned on, at their stated strength: "the four-instrument
  gemini/gpt negative was an artifact of the **forced single-token format** … **not** a composition-capacity
  limit"; "the obstacle was not a *capacity* to chain but the *denial of a surface on which to chain*"; "The
  single-move signature was the shape of a two-step computation forced through a one-token channel"; the
  witness "does **not** show the models compose *without* a working surface … the **format** gates the
  behavior"; and the reasoning-effort knob "**held constant** … the working surface is opened only in the
  visible output channel" (all [`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md));
  the channel axis named as "an explicit step-by-step working surface … un-eased"
  ([`essay/floor-is-not-a-ceiling`](floor-is-not-a-ceiling.md)); "the next untried framing could carry a
  witness, and a single witness would falsify the whole universal" and the kind-2 instrument-uninterpretable
  tag ([`essay/undischargeable-negative`](undischargeable-negative.md)); "read the failure signature, ease the
  implicated axis" ([`essay/witness-seeking-economics`](witness-seeking-economics.md)); "a split is contingent
  on elicitation" ([`essay/capability-split`](capability-split.md)); the formal/functional distinction and
  "failure on a world-knowledge task does not show that a model lacks formal linguistic competence"
  ([`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)).
  The machine-side mechanism grounding cites [`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md):
  "CoT empowers the model with the ability to perform inherently serial computation, which is otherwise lacking
  in transformers, especially when depth is low"; "can only solve problems in TC^0 without CoT"; "with T steps
  of CoT" it "can solve any problem solvable by boolean circuits of size T"; "the composition of permutation
  groups" (all from that source's verbatim-verified abstract). These are used at their stated strength — a
  **theory-of-computation result about idealized transformers**, grounding the mechanism's *plausibility*, not
  the panel's internals, and licensing **no** human comparison. Nothing here outruns those.
- The thesis preserves [`essay/undischargeable-negative`](undischargeable-negative.md) and
  [`essay/witness-seeking-economics`](witness-seeking-economics.md) intact: a forced-format negative stays an
  undischargeable kind-2 verdict, and the output channel is added as a privileged (cheap, recurring) region of
  the open elicitation space the economics should sample early. The closure ≠ suspension line is untouched —
  the channel-widening **reopened-and-resolved-positive**, the opposite of a closure.
- **Human comparison, scoped narrowly (updated 2026-06-20, session 62).** The *composition* results cited
  here are THIN / `internal-contrast-only` — their human leg is unanchored in-repo, so they license no human
  comparison. The *let-alone* results, however, **are** human-anchored
  ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md), the ≈0.90
  native-speaker baseline, ratified 2026-05-29), so the trigger-(b) firing
  ([`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md)) does
  rest partly on a human comparison. The leg the essay's *control argument* leans on is the **within-model**
  channel/uptake contrast (offered → forced surface, model-internal); the **accuracy-vs-baseline** leg
  (gpt's residual below 0.90) is anchored but **descriptive + contamination-caveated** (public items; an
  answer-key match cannot distinguish learned construction-meaning from memory) and read at exactly that
  strength — never as "gpt cannot." The confound itself is general to constrained-response capacity-probing,
  but the essay applies it only to the project's own LLM probes.
