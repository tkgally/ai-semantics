---
type: essay
id: floor-is-not-a-ceiling
title: A floor is not a ceiling — why the ≥2-move bound on two-move composition does not structurally close the witness-search, and what distinguishes a task-parameter floor from a kind-3 reach-closure
meaning-senses:
  - model-internal
  - functional-vs-formal
  - relational
status: draft
contingent-on: []
created: 2026-06-19
updated: 2026-06-19
links:
  - rel: refines
    target: essay/witness-seeking-economics
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: depends-on
    target: essay/transcript-ceiling
  - rel: depends-on
    target: essay/capability-split
  - rel: depends-on
    target: result/relational-order-composition-c-worked-example
  - rel: depends-on
    target: concept/formal-vs-functional-competence
---

# Essay: a floor is not a ceiling

> **Status: draft (2026-06-19). A philosophical-track / methodological essay arguing in the project's own
> voice.** It answers a question another essay explicitly posed.
> [`essay/witness-seeking-economics`](witness-seeking-economics.md) names a **structural bound** (a kind-3
> reach-closure) as "the highest-value terminator in the economics," and its **revision trigger (b)** invites
> exactly the argument this essay attempts: "an analogous bound for some *thin-side* composition capability
> would be new." The composition witness-search is now suspended across four instruments
> ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md)),
> and that result's suspension note records the structural bound as "**none yet**." This essay asks whether
> the bound can be supplied — whether the **≥2-move floor** on two-move composition, plus the behavioral
> localization of the difficulty to "chaining execution," licenses a kind-3 reach-closure that would upgrade
> the suspension from budget-based to structural. **Its answer is no, and the no is the contribution:** no
> reach-closure of the transcript-ceiling type is available here. The original move is a **criterion** that
> says *why* — a sharp distinction between a **task-parameter floor** (which the composition case has, and
> which cannot be a kind-3 reach-closure) and a **medium-level exclusion** (which the transcript ceiling has,
> and which can). It contains **no new empirical claim** and makes **no human comparison**: every empirical
> sentence cites the in-repo page that carries it, at that page's stated strength, and the result it reads is
> a non-witness null / `internal-contrast-only`. Read the revision triggers before citing.

## The occasion

The project's recent methodological spine ends on an open invitation. [`essay/undischargeable-negative`](undischargeable-negative.md)
established that a behavioral capability-negative can never be closed from behavior, only witnessed away;
[`essay/witness-seeking-economics`](witness-seeking-economics.md) added the spending discipline and singled
out one move as worth more than any number of probes — a **structural bound**:

> a **structural argument can bound the witness-search space** without closing anything. If one can argue
> that a whole *class* of easings cannot help — that no member of it could carry a witness — then the open
> search collapses to a bounded one, and the budget that would have been spent enumerating that class is
> freed at the cost of zero probes. ([`essay/witness-seeking-economics`](witness-seeking-economics.md))

with the crucial discipline that "a structural argument of this kind bounds the *reach of an instrument
class*, not the *capacity of the model* — it is the parent essay's **kind-3 reach-closure**, not a
capability-absence." The economics' own revision trigger (b) then names the missing instance: the
transcript ceiling is the exemplar for the *rich-side* relational question, but "an analogous bound for some
*thin-side* composition capability would be new."

The empirical state has now reached the point where that invitation is live. The Option-C split — `claude-sonnet-4.6`
composes two non-commuting moves, `gemini-3.5-flash` and `gpt-5.4-mini` return UNINTERPRETABLE — has been
chased through **four** witness-seeking easings without a witness, each one an honest single-variable
manipulation
([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md)
and the three results it refines). The failure has been behaviorally localized: across the figure-to-figure
and worked-example runs the difficulty is "**not** that the procedure is undemonstrated; it is the
**execution** of holding and applying two operations in sequence in this instrument." And the one remaining
un-eased axis is bounded below: an "order-sensitive *composition* requires **≥ 2** moves by construction, so
'fewer chaining steps' cannot go below two and remain a composition." The worked-example result records the
structural question as still open:

> **(iii) Structural bound on the remaining search:** **none yet** for this thin-side composition
> capability … No argument yet shows a fewer-steps or alternative-operation design *cannot* carry a witness —
> though the ≥2-move floor narrows what a "fewer-steps" easing could be.
> ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md))

This essay takes up the "none yet." It asks, as the economics' trigger (b) invites: can the ≥2-move floor be
turned into a kind-3 reach-closure?

## The candidate argument, stated at its strongest

It is worth building the best version of the bound before refusing it, because the refusal turns on a
distinction the strong version makes vivid.

- **Premise 1 (the floor).** A non-commuting composition requires at least two operations — with fewer than
  two there is nothing whose order could matter. So the "fewer chaining steps" easing axis cannot be pushed
  below two and still pose the task. The axis is *floored*.
- **Premise 2 (the localization).** Four eased instruments have stripped away the peripheral axes —
  state-space size, the per-move positional read-off, and the demonstration/comprehension gap — and the
  single-move-reader signature survived each removal, intensifying under the worked example (gpt "applies
  only one of the two moves 84.4% of the time" with the order stated and a chain shown). So the residual
  difficulty is *chaining execution itself*, not any peripheral axis.
- **Candidate conclusion.** Therefore the residual difficulty is the **irreducible core** of a two-move
  composition. Any easing must either (a) ease one of the peripheral axes already discharged — low expected
  information, no witness expected — or (b) drop below the ≥2-move floor, at which point the instrument is no
  longer a composition. No easing *of this task* can carry a witness. The search space is structurally
  bounded: a kind-3 reach-closure.

If this went through, it would be the highest-value terminator the economics describes — it would retire the
remaining composition witness-search at zero spend, exactly as the transcript ceiling retired the rich-side
text-probe program. It does not go through, for three independent reasons, each sufficient on its own.

## Why it is not a kind-3 reach-closure

### (A) Its load-bearing premise is a behavioral universal — so it smuggles in the empty fourth box

The candidate's force comes from Premise 2: the difficulty *is* chaining execution, the irreducible core.
But "the difficulty is chaining execution" is read off the *behavior* — the persisting single-move signature
across instruments. By [`essay/undischargeable-negative`](undischargeable-negative.md), behavior can deliver
the existential ("here is what the difficulty was on these instruments") but never the universal ("the
difficulty *is*, across all elicitations, chaining execution, and nothing eases it"). The step from
"chaining execution survived four easings" to "chaining execution is the irreducible core that no easing can
relieve" is precisely the silent upgrade the typology exists to forbid: it is "M cannot chain two moves"
wearing the costume of a structural argument. The fourth box — "a **capability-absence** ('M cannot do X')
established *from behavior*. No probe, and no pile of probes, fills it" — does not become fillable because the
probes are recast as premises of a bound.

Contrast the transcript ceiling, which is a genuine kind-3 closure precisely because **its premise is not
behavioral**. Its closure rests on "The rich side is defined by what the record lacks" and "A transcript
states a record and nothing more" — facts about the *medium*, provable without running any probe. The
composition argument has no analogous non-behavioral premise; its Premise 2 is exactly the behavioral
localization that the undischargeable-negative result says cannot bear universal weight. A kind-3 bound built
on a kind-4 premise is not kind-3. It is a kind-4 claim with extra steps.

### (B) The ≥2-move floor bounds one axis; the elicitation space stays open along others

Even granting Premise 2 *as localization* (the difficulty, on these instruments, lives in chaining rather
than read-off — which the result pages do support, at `internal-contrast-only` strength), the candidate
conclusion overreaches in Premise 1's scope. The ≥2-move floor bounds exactly **one** axis: the *number of
chaining steps*. It says nothing about the other axes along which an instrument can vary while still posing a
genuine two-move non-commuting composition — and several of those are un-eased and open:

- **Operation-pair familiarity.** STEP/FLIP on a small ring is one synthetic, low-prior operation pair. A
  non-commuting pair the models have strong priors over (two everyday transformations seen at scale) is a
  different elicitation of the *same* capability, and a witness on *any* non-commuting pair would fire the
  existential. The project already holds this axis open: the Option-C result names "other operation pairs"
  among its untested directions, and the easings to date deliberately froze the pair to isolate other
  variables. Whether "STEP/FLIP-on-a-ring is unusually hard, or two-move composition itself is the wall" is
  an open empirical question, not one the floor settles.
- **Execution-format scaffolding.** The on-demand DIRECT gate *states* the order but does not scaffold the
  *execution* into externalized steps. An elicitation that decomposes the execution itself (an explicit
  step-by-step working surface) eases the localized difficulty directly, and is un-eased. The worked example
  *demonstrated* the mechanic on disjoint items; it did not restructure the model's own response format —
  a distinct lever.
- **Many-shot rather than one demonstration.** The worked-example run used a single example. The number of
  demonstrations is its own axis; one non-witness at k=1 does not bound k>1.

None of these is exotic; two are already in the project's own backlog as *fresh* axes. Their existence is
fatal to the candidate, because "no easing can carry a witness" is the open ∀ over elicitations that
[`essay/undischargeable-negative`](undischargeable-negative.md) shows behavior cannot establish — and the
floor closes only the sub-region "fewer than two moves" of one axis, leaving the witness-bearing region (≥2
moves, open along operation-pair, format, and shot-count) fully populated. The floor narrows *one direction
of easing*; it does not bound the space.

### (C) A task-parameter floor is the wrong *type* of object to be a reach-closure

The first two objections defeat the candidate. The third explains the defeat in a way that generalizes — and
is this essay's actual contribution. Set the two structures side by side:

- The **transcript ceiling** excludes the witness by *medium*. The target property (the rich-side surplus)
  is **defined as** what the record omits, and the instrument **is** a record, so the witness cannot lie in
  any instrument of the class. The exclusion is definitional and class-level: it holds for *every* instrument
  in the class, however the task's parameters are set. That is what "*this instrument-class* cannot reach the
  question" means — a kind-3 reach-closure.
- The **≥2-move floor** excludes only designs *below a parameter value* of a task whose witness, if it exists,
  lives *at or above* that value. It is silent on whether an at-or-above-floor instrument carries the witness
  — which is the whole question. A bound that floors the cheap-easing region from below while leaving the
  witness-bearing region open is not a closure of the *search*; it is a closure of *one direction of easing*.

So the general criterion:

> **A difficulty-bound is a kind-3 reach-closure only if it excludes the witness from an entire instrument
> *class* by a property of that class — characteristically a definitional, medium-level exclusion (the target
> property is constitutively absent from anything in the class). A bound on a *task parameter* — a floor or
> ceiling on a knob of the task — excludes only a sub-region of one easing axis and leaves the class
> otherwise open; it is *not* a reach-closure.** Not every floor is a ceiling.

The transcript ceiling is a ceiling because it bounds the medium from **outside** the task's parameters: no
setting of any knob puts the rich-side surplus into a transcript. The ≥2-move bound is a floor **inside** the
task's parameters: it caps how far one knob can be turned, and the witness-bearing settings sit above it,
still open. The two are different logical types. Reading the floor as a ceiling — "you cannot make the task
easier by *removing moves*, therefore no easing can help" — equivocates between "this knob bottoms out here"
and "the question is out of reach," which is the equivocation the criterion forbids.

## The verdict on trigger (b): a reasoned null, not a placeholder

By all three lights, **no kind-3 structural bound of the transcript-ceiling type is available for thin-side
two-move composition.** Trigger (b) of the economics is therefore answered, and answered in the negative:
the composition witness-search **cannot** be terminated structurally; it can only be **suspended on budget**.
The worked-example result's item (iii) — "none yet" — is upgraded from a contingent placeholder to a
*reasoned* finding, with a different and more useful content than the placeholder carried. It is not "we have
not yet found a bound" (an invitation to keep looking for one). It is: **no bound of the available type can
exist here**, because the only candidate (the ≥2-move floor) is a task-parameter floor, not a medium
exclusion — wrong in type — and the residual-difficulty localization that would be needed to argue otherwise
is a behavioral universal the project may not assert.

This is a real result for the spending decision, even though it is a null. It tells future sessions two
things. First, that hunting for a structural terminator on this line is itself a poor use of the budget —
there is none of the right type to find, so the witness-search here will *always* be a budget suspension,
never a structural closure. Second, it points the budget, if it is spent here at all, at the axes the floor
leaves open — a different operation pair, an execution-format scaffold, many-shot — rather than at the
exhausted peripheral axes or at the foreclosed "fewer steps" direction. The null does not extend the search
by sharpening a target (as a diagnostic-dividend non-witness does); it bounds the *meta-search* — the search
for a way to stop searching — by showing one hoped-for terminator is unavailable.

## How this sharpens the economics rather than overturning it

[`essay/witness-seeking-economics`](witness-seeking-economics.md) ranks a structural bound as the
highest-value move "precisely *because* it claims so little about the model: only that a class of instruments
cannot reach the question." This essay leaves that ranking intact and supplies the test the ranking
presupposed: a candidate bound earns the rank **only if it is a genuine kind-3 reach-closure** — only if it
excludes the witness from an instrument class by a class-level property — and **not** if it merely floors a
task parameter. The economics said "prefer a structural bound to exhaustion"; this essay adds the gate that
must be passed before a candidate counts as a structural bound at all. The transcript ceiling passes it (a
definitional medium exclusion). The ≥2-move floor fails it (a task-parameter floor). Both are now legible as
instances of one criterion, which is exactly the unification the methodological spine has been building
toward.

The **closure ≠ suspension** line is not merely untouched but reinforced. The most dangerous way for that
line to be crossed is *not* an honest "M cannot" — those are easy to catch — but a budget suspension dressed
as a structural closure, a parameter floor mistaken for a reach-closure, which would let the highest-value
terminator be invoked illegitimately and a witness-search be declared structurally over when it is only
expensive. This essay names that error and supplies the guard against it: when a structural bound is claimed,
check that it is a medium exclusion and not a parameter floor. A floor you mistake for a ceiling is a map of
where to stop digging that points at solid ground.

## What this essay is not

- **Not a claim that any model can or cannot compose.** It is about whether the *witness-search* can be
  structurally terminated, not about gemini's or gpt's capacity. Their Option-C verdicts stay **kind-2
  instrument-uninterpretable**, undischargeable, per their pages. Indeed objection (A) is precisely a refusal
  to convert those negatives into a capacity claim by the back door of a structural argument.
- **Not a claim that no structural bound could ever close the composition question.** A *non-behavioral*
  argument — an architectural expressivity bound, a mechanistic result — could still close the **capacity**
  question off the behavioral axis (the off-typology route of
  [`essay/undischargeable-negative`](undischargeable-negative.md) trigger (a)). This essay denies only that a
  transcript-ceiling-style **reach-closure on the witness-search** is available, and that the ≥2-move floor
  supplies one. Capacity-closure and reach-closure are different objects; denying the second leaves the first
  open.
- **Not an accusation that the suspension note erred.** The worked-example result wrote "none yet," which was
  correct and appropriately tentative; this essay converts the tentative placeholder into a reasoned null,
  exactly as [`essay/undischargeable-negative`](undischargeable-negative.md) and
  [`essay/witness-seeking-economics`](witness-seeking-economics.md) generalized disciplines already
  half-practiced.
- **Not a general law that floors never close searches.** The criterion is conditional: a *task-parameter*
  floor is not a reach-closure. A different bound — even one phrased as a "floor" — that turned out to be a
  definitional medium exclusion would pass the gate. The claim is about the *type* of the ≥2-move bound, not
  about the word "floor."
- **Not a human comparison.** The cited result is `internal-contrast-only`; the criterion is general to any
  budgeted capability-search (it would bind for human probing too), but the essay applies it only to the
  project's own LLM probes and asserts nothing about humans.

## Revision triggers (read before citing)

- **(a) A non-behavioral architectural / expressivity / mechanistic bound on two-move composition.** Such an
  argument would close the **capacity** question off the behavioral axis — the off-typology "proof-closed
  absence" of [`essay/undischargeable-negative`](undischargeable-negative.md) trigger (a). It would *not*
  overturn this essay (whose claim is about the unavailability of a *reach-closure on the witness-search*),
  but would require noting that a capacity-closure had arrived by a route this essay explicitly left open.
  The essay is sharpened, not retired.
- **(b) A witness found on one of the open axes** (a different / more familiar non-commuting operation pair,
  an execution-format scaffold, a many-shot demonstration). This would directly **confirm** objection (B):
  the elicitation space was open along an axis the floor did not touch, so the floor was never a closure. The
  central claim is strongly corroborated and the specific suspension is reopened-and-resolved-positive,
  exactly as the economics predicts a cheap targeted probe can do.
- **(c) A genuine medium-level exclusion discovered for some composition witness.** If an argument showed
  that a text instrument *constitutively cannot express* some structure a composition witness would require —
  a definitional, class-level exclusion of the transcript-ceiling type — then a kind-3 reach-closure *would*
  exist for that sub-case, and this essay would be bounded to the cases it examined (where the only candidate
  was a parameter floor). This is the form a real composition reach-closure would have to take, and naming it
  is part of the contribution.
- **(d) A demonstration that the open axes are themselves finite and exhaustible.** If the operation-pair /
  format / shot-count axes were shown to be a *finite, exhaustible* set (the elicitation-space horn of
  [`essay/undischargeable-negative`](undischargeable-negative.md) trigger (b)), the search could be
  terminated by **exhaustion** — a different terminator from a reach-closure, and one this essay does not
  address. The criterion would stand; the suspension's grounds would change from "budget" to "exhausted."
- **(e) A fetched human resource licensing a capacity comparison.** None is in-repo. One bearing on how a
  *human* capability-search is bounded under finite resources would let the criterion be applied
  comparatively — currently forbidden by the no-human-comparison discipline this essay observes.

## Honesty box

- The essay's **original** contribution is the **criterion** distinguishing a **task-parameter floor** (a
  bound on a knob of the task; not a kind-3 reach-closure) from a **medium-level exclusion** (a definitional,
  class-level exclusion of the target from the instrument class; a genuine kind-3 reach-closure), and the
  **verdict** that thin-side two-move composition has no bound of the second type — so the composition
  witness-search can only ever be *suspended on budget*, never *structurally closed*. This answers
  [`essay/witness-seeking-economics`](witness-seeking-economics.md) trigger (b) in the negative and upgrades
  the worked-example result's suspension-note item (iii) from a tentative "none yet" to a reasoned null. **No
  empirical claim here is new, original, or reported.**
- The strongest empirical / in-repo sentences leaned on, at their stated strength: the composition difficulty
  is localized to "the **execution** of holding and applying two operations in sequence in this instrument,"
  and an "order-sensitive *composition* requires **≥ 2** moves by construction," with the structural bound
  recorded as "**none yet**"
  ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md));
  a structural bound "bounds the *reach of an instrument class*, not the *capacity of the model* — it is the
  parent essay's **kind-3 reach-closure**," and is "the highest-value terminator in the economics"
  ([`essay/witness-seeking-economics`](witness-seeking-economics.md)); the empty fourth box is "a
  **capability-absence** ('M cannot do X') established *from behavior*. No probe, and no pile of probes, fills
  it," and a kind-3 closure closes "a *reach* claim … not a *capacity* claim"
  ([`essay/undischargeable-negative`](undischargeable-negative.md)); the transcript ceiling rests on "The rich
  side is defined by what the record lacks" and "A transcript states a record and nothing more"
  ([`essay/transcript-ceiling`](transcript-ceiling.md)); the negatives stay instrument-bounded, never "lacks
  order-sensitive composition in general" ([`essay/capability-split`](capability-split.md);
  [`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)).
  Nothing here outruns those.
- The thesis preserves [`essay/undischargeable-negative`](undischargeable-negative.md) and
  [`essay/witness-seeking-economics`](witness-seeking-economics.md) intact: it denies a *behavioral*
  reach-closure for the witness-search, leaving a *non-behavioral* capacity-closure open (trigger (a)), and it
  reinforces the closure ≠ suspension line by guarding against a parameter floor masquerading as a
  reach-closure.
- **No human comparison** is made or owed: the cited result is `internal-contrast-only`, and the human leg of
  every cited contrast is unanchored in-repo. The criterion is general to budgeted capability-search, but the
  essay applies it only to the project's own LLM probes.
