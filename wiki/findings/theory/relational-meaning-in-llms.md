---
type: theory
id: relational-meaning-in-llms
title: Relational meaning in LLMs — the second ladder has a well-characterized floor and no positive bottom rung
meaning-senses:
  - relational
  - distributional
  - model-internal
  - human-comparison
status: draft
contingent-on: []
created: 2026-06-29
updated: 2026-06-29
links:
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: open-question/relational-meaning-pilot
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: result/relational-spontaneous-recency-a
  - rel: depends-on
    target: result/relational-history-perturbation-v4
  - rel: depends-on
    target: result/relational-integration-rung-ii
  - rel: depends-on
    target: result/relational-order-composition-c
  - rel: depends-on
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: essay/aggregation-not-constitution
  - rel: depends-on
    target: essay/update-is-not-constitution
  - rel: depends-on
    target: essay/transcript-ceiling
  - rel: depends-on
    target: essay/rung-iv-instrument
  - rel: depends-on
    target: resource/hawkins-tangrams
  - rel: refines
    target: theory/constructional-meaning-in-llms
---

# Theory: relational meaning in LLMs — the second ladder's floor is mapped; no positive bottom rung

> **Status: draft (2026-06-29). A synthesis page — the recursive theoretical object for the
> relational axis.** It consolidates the whole "relational axis / second ladder" arc into one place:
> the convention-formation pilot, the coined-term reassignment line, the order-of-operations
> composition line, and the seven essays the philosophical track has built around them. It **promotes
> and expands** the relational subsection of
> [`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md) (§"The under-explored
> axis: relational meaning") — that page records the relational axis as "one bounded negative" and
> defers the rest; this page carries the now-substantial arc. Every empirical number below is copied
> verbatim from the result page that carries it; almost every trajectory/order finding is
> `anchor: internal-contrast-only` (a within-model contrast making **no human-comparison claim**), and
> the **single** human-comparison point in the whole arc is the Hawkins-anchored convergence-without-
> compression observation. Those scopes are preserved exactly. This is a **thin-positive /
> floor-characterizing arc**, not an all-null one: it has a genuine order-sensitivity *positive* (the
> project's deflationary commutativity bet was falsified and retired), but every such positive is
> **thin** — model-internal and transcript-recoverable, not meaning *constituted between* agents. The
> honest headline is that the second ladder has a well-characterized **floor** and **no positive bottom
> rung** (constitution), and that the rich rung is documented **structurally out of reach for text-only
> probes**. Read the scope/caveats and revision triggers before citing.

## The thesis

The charter's distinctive wedge is **relational meaning** — content constituted *between* a model and a
person, or between models, rather than computed *inside* one agent and read off
([`concept/relational-meaning`](../../base/concepts/relational-meaning.md)). That page frames the axis
as a **second ladder**: "The relational axis is not a higher rung of the same ladder; it is a *second
ladder* whose bottom rung is not yet defined"
([`concept/relational-meaning`](../../base/concepts/relational-meaning.md)). The discriminating measure the project sharpened is **trajectory-dependence**: a convention
constituted *between* agents would have a recovered interpretation that depends on the *ordered history*
of the exchange and not merely on the *set* of utterances — operationally, a **live-vs-shuffled gap**
that holds the content of prior turns constant and destroys only their ordering. The deflationary
alternative is itself a `distributional` story ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)):
two next-token predictors conditioned on overlapping content converge and entrain *from co-occurrence
content alone*, and that convergence **survives order-scrambling**. So relational meaning-constitution
requires a *surplus* over distributional convergence; the live-vs-shuffled gap is exactly that surplus
([`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md)).

The arc now has a substantial body of findings. They include a genuine *positive* — order-sensitivity
(non-commutativity) where order carries disambiguating information, which falsified the project's own
deflationary commutativity bet (sub-line 2 below). But on the one question the second ladder turns on —
*is any of it meaning constituted between agents?* — they converge on a single negative:

> **Every apparent relational signal the project has been able to probe reduces to a WITHIN-model /
> WITHIN-transcript phenomenon.** Coordination is real; convention-*use* is real; order- and
> position-effects exist and are sometimes order-*sensitive* in a strict, non-commutative sense. But
> none of it is meaning *constituted between* agents. Each apparent climb moved the models to a
> stricter dependence *on the same (thin) side* of a single decidable cut — recoverable by any single
> reader of the record — never across it. The transcript medium imposes a built-in ceiling, and the
> within-text routes to a positive are now substantially mapped and **exhausted or suspended**.

The floor is crisp. The bottom rung of the second ladder — a *positive* demonstration of meaning
constituted between agents — has **not** been built, and a leading reading is that it cannot be built
with text stimuli at all.

## The arc, mapped into its three sub-lines

### Sub-line 1 — convention-formation (the reference-game pilot)

The axis's **first in-repo result** ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md),
2026-05-31) built the iterated dyadic reference game
[`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md) named:
homogeneous LLM dyads coin a compressed label for hard-to-name figures, then a fresh matcher
interprets the opaque coined nickname under arms that hold the record content byte-identical and vary
only its order. The load-bearing question is trajectory-dependence.

**Verdict: a first-class relational NULL — convergence WITHOUT trajectory-dependence, uniform across
all three models.** The history's *content* is load-bearing (history_lift, `ordered − coined_only`, is
**+0.333 / +0.417 / +0.250** for claude / gpt / gemini — all positive point estimates), but its
*order* is not: the ORDER gap (`ordered − shuffled`) is **+0.083 / +0.056 / +0.111**, and **no
model's clustered-bootstrap CI excludes 0**. The coherent `reversed` arm is no better than — sometimes
worse than — random `shuffled` (claude reversed 0.750 < shuffled 0.833; gemini 0.750 < 0.806), so the
small positive ORDER gaps are order-insensitive noise around a content-driven baseline. The coined
convention is recovered from the **set** of prior turns, not their **ordered trajectory** — coordination,
not constitution; the deflationary distributional story survives order-scrambling.

**The lone human-comparison point in the whole arc falls out of the same run** and carries the arc's
only `anchors` link, to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md):
**convergence without human-like compression.** All three dyads reach near-ceiling referential
*accuracy* within a few repetitions (claude 0.67→1.00, gpt 0.42→0.75, gemini 0.92→1.00) but keep
referring-expression length roughly constant (~8.5–10.8 words), whereas the human Hawkins dyads
**compress** from 7.73 to 4.10 words while accuracy rises 0.78→0.94. This is the run's **only**
human-comparison claim and the only measure Hawkins anchors. Its scope is bounded hard by the Hawkins
page's own "What it CANNOT ground" section: the comparison crosses referent modality and channel
(text-grid LLM games under a word budget vs. human image-tangram unconstrained speech), and gemini ran
at ceiling from rep 1, so the no-compression claim is weakest for gemini. **The load-bearing
trajectory measure is, by contrast, an INTERNAL within-model contrast and is NOT anchored by Hawkins**
— the live-vs-shuffled contrast is novel to the LLM probe and unanchored by any human resource. Keep
the two scopes apart: the null makes no human comparison; the compression observation makes no
trajectory claim.

### Sub-line 2 — coined-term reassignment (the conversation-history line)

This line asks the sharper question the pilot's own caveat flagged as missing: a setting where the
content-set is *symmetric* and **only recency disambiguates**. It runs through a staged decision and
four perturbation versions before its decisive arms.

**The perturbation arm (v2–v4): position, not chronology.** The decisive commutativity test was run
three times. v2 ([`result/relational-history-perturbation-v2`](../results/relational-history-perturbation-v2.md))
and v3 ([`result/relational-history-perturbation-v3`](../results/relational-history-perturbation-v3.md))
were both **INCONCLUSIVE/MIXED**: a forward chronology elevation appeared but did not survive direction
reversal, and the design could not separate "chronologically last" from "physically last in the text."
v4 ([`result/relational-history-perturbation-v4`](../results/relational-history-perturbation-v4.md))
performed the within-arm decoupling and earned a clean reading: **both models track physical
TEXT-POSITION, not stamped chronology.** claude → TEXT-POSITION ARTIFACT (Δ_pos CI-clean 0.698
[0.594, 0.804]; Δ_chron null 0.509 [0.465, 0.556]); gemini → INCONCLUSIVE/MIXED, same direction
(position-dominant, the small Δ_chron elevation shown by the verifier to carry zero residual chronology
signal). In the conflict cells both models pick the physically-last (chronologically-*earlier*) twin
~0.69–0.75 of the time. The binding caveat: position-following here was *indistinguishable from
stamp-blindness* — the design could not establish whether the models parse the round numbers as recency
at all.

**The comprehension gate (Option B): stamp comprehended on demand.** That ambiguity was resolved by
[`result/relational-stamp-comprehension-b`](../results/relational-stamp-comprehension-b.md): both models
read the round stamp as a recency value when directly asked — **accuracy 1.000** each (Wilson
[0.926, 1.000]), position-following at exactly chance (0.250) → both PASS. So v4's position-following is
**comprehending-but-not-spontaneously-using**, not stamp-blindness. This is a gate, not a relational
finding; it made an Option-A null interpretable for the first time.

**Spontaneous recency (Option A): latest-binding-wins.** With physical position neutralized and a
coined term `DAX` reassigned across four stamped, non-contiguous rounds (content-set symmetric, only
recency disambiguates), [`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)
found both models recover the term by its **most-recent binding, spontaneously and at ceiling**: SPONT
latest-binding rate **1.000** (48/48, Wilson [0.926, 1.000]) for both, first-binding rate 0.000,
physical-position-following at exactly chance (0.250), DIRECT on-demand check 1.000. This is **the first
positive evidence of order-sensitivity on the relational axis** — order-sensitive (non-commutative)
where order carries disambiguating information. It **falsified** the project's deflationary
[`conjecture/commutative-convention`](../conjectures/commutative-convention.md) (now retired) and was
promoted to [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md).
Crucially, it is **thin**: latest-binding-wins is a convention-*update* / overwrite rule, order-sensitive
but **not** a convention constituted *between* agents through the live trajectory. The v1/v4 nulls are
**not overturned but bounded**: commutativity is operationalization-dependent — present where order
carries no disambiguating signal (v1) or is confounded with position (v4), absent where order is the
sole disambiguator (Option A).

**The control and the integration rungs (still thin).** Three follow-ups bound the positive without
lifting it. The implicit-reassignment control
([`result/relational-implicit-reassignment-control`](../results/relational-implicit-reassignment-control.md))
dropped Option A's explicit "was reassigned" flag and kept everything byte-identical; both models still
recovered the most-recent binding at ceiling (SPONT 1.000), so the order-sensitivity is **not a wording
artifact**. Rung (ii) integration ([`result/relational-integration-rung-ii`](../results/relational-integration-rung-ii.md))
showed that when a later turn is *compatible* with an earlier one, both models **compose** the two
rather than overwriting (INTEG target 1.000, overwrite rate 0.000) — so the update rule is
**supersede-on-conflict, compose-on-compatibility** — and this survives burial depth 2
([`result/relational-integration-depth`](../results/relational-integration-depth.md): INTEG 1.000,
"drop-the-oldest" reader taken 0.000). But the integration design's constraints are *symmetric*, so it
shows *survival* of a compatible turn, which a commutative conjunction passes equally — not order-sensitive
composition. All three results are **single-reader-recoverable**: thin, not constitution.

### Sub-line 3 — order-of-operations composition (the C series)

This line closes the gap rung (ii) left open: is the composition itself **order-sensitive
(non-commutative)**, or only *survival* of a compatible turn? Option C
([`result/relational-order-composition-c`](../results/relational-order-composition-c.md)) makes order
genuinely load-bearing — a coined token undergoes **two stamped, non-commuting operations** (STEP/FLIP
on a track), so the two stamp orders reach **different** end states, and only ordering the two moves by
their stamps clears the 0.50 print/canonical ceiling. The gap is **adjudicated THIN before the run**
(the stamped move-list is in the record; single-reader-recoverable: *"respects operation order,"* not
rung iii).

**The first verdict was a split — under a forced single-token format.** In the original Option-C run,
**claude** orders the two non-commuting moves by their round stamps spontaneously and at ceiling
(COMP 1.000, 72/72, Wilson [0.949, 1.000]; DIRECT on-demand gate 0.861 PASS) → RESPECTS-ORDER, while
**both gemini (DIRECT 0.583) and gpt (DIRECT 0.194)** could not compose the two moves even when told
the order → UNINTERPRETABLE for each. So, on that instrument, order-sensitive composition was occupied
by **one model of three**. Four forced-format easings — K=4
([`result/relational-order-composition-c-easier-k4`](../results/relational-order-composition-c-easier-k4.md)),
figure-to-figure maps ([`result/relational-order-composition-c-figure-to-figure`](../results/relational-order-composition-c-figure-to-figure.md)),
and a worked-example scaffold ([`result/relational-order-composition-c-worked-example`](../results/relational-order-composition-c-worked-example.md))
— **all failed to find a witness**; the failure signature was *single-move reading* (applying only one
of the two stamped moves), localizing the difficulty to chaining execution. Each non-witness *bounded*
the negative without closing it (a behavioral capability-negative is undischargeable).

**But the split was an artifact of denying a working surface — and the capacity is a panel property.**
The execution-format witness run
([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md))
changed *only* the response format on the byte-identical trials — from a forced single token to a
**working surface** (step-by-step output permitted, `FINAL:`-tag parsed; reasoning-effort knob held
constant) — and flipped **both** previously-UNINTERPRETABLE models to RESPECTS-ORDER: gemini DIRECT
0.656→**1.000** (COMP 1.000), gpt DIRECT 0.250→**0.969** (COMP 0.953), claude unchanged at ceiling.
So the four-instrument negative was an artifact of the forced single-token format, **not** a
composition-capacity limit. The capacity then **replicated across three generality axes** — operation
pair (CYCLE/SWAP, generating A4 vs. the witness's D4:
[`result/relational-order-composition-c-altpair`](../results/relational-order-composition-c-altpair.md)),
grid size (K=6: [`result/relational-order-composition-c-k6`](../results/relational-order-composition-c-k6.md)),
and **composition depth (three non-commuting moves**:
[`result/relational-order-composition-three-move`](../results/relational-order-composition-three-move.md),
all three RESPECTS-ORDER) — all panel-concordant. So order-sensitive composition is a panel-wide
**capacity given a working surface**, generalizing across pair, grid size, and depth.

**Two scopes carry, and they are the whole point.** First, the capacity is **working-surface-relative**:
under a forced single token the panel does *not* compose (only claude did) — a fact about elicitation,
not about constitution. Second, and decisively, it is **still THIN** throughout: a single reader of the
stamped move-list applies it in order and reads off the answer. RESPECTS-ORDER is *"respects operation
order,"* a stricter dependence than rung (ii) survival, but it is **not** rung (iii) path-dependence and
**not** between-agent constitution. The cross-family-dyad arm — the one remaining instrument-generality
direction toward a richer setting — was **attempted 2026-06-20 and SUSPENDED before any spend** (the
pre-run gate found the operationalization unusually leak-prone; per
[`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md) the expected thin ceiling did
not justify the build cost). A suspension is a reopenable spending record, **not a null**.

## The unifying interpretation: order-effects are real, constitution is not

The three sub-lines tell one story when read through the deflationary `distributional` spine and the
philosophical track's essays.

**Aggregation, not constitution.** The pilot's verdict — coordination, not constitution — is made
algebraically precise by the commutative/non-commutative distinction
([`essay/aggregation-not-constitution`](../essays/aggregation-not-constitution.md)). Convergent
convention-*use*, however rich, is the **floor**, not the finding: a convention whose interpretation any
fresh agent recovers from the content-bag of the record is exactly what a shared distributional substrate
predicts, *without* anything existing "in the interaction and not antecedently in either party." The
Option-A positive does not lift this: the surplus paid was the *thinnest* the framework admits
(latest-binding-wins), so the anti-Brandomian friction reverses in *direction only* — an order-sensitive
surplus is what an interaction-instituted account would predict — while the gap to genuine deontic
scorekeeping (commitments, entitlements, challenges, none measured) is **untouched**. The grounded
interactive-alignment framework now in-repo
([`essay/alignment-names-the-floor`](../essays/alignment-names-the-floor.md)) supplies a positive
mechanistic *name* for that floor: pervasive, multi-level convergence is exactly what an automatic,
resource-free priming mechanism delivers *short of* a meeting of minds — so naming the floor with it
**raises** the constitution bar rather than lowering it.

**A conversation is a text, not a timeline — read regime-dependently.** The v4-vs-Option-A contrast
breaks the clean aggregation/constitution dichotomy
([`essay/conversation-as-text-not-timeline`](../essays/conversation-as-text-not-timeline.md)): the
models are neither a constitution reader (they do not track stated chronology) nor a clean order-free
bag of turns (they are strongly position-driven). They read **whichever cue the task makes
load-bearing** — text position in v4, stamped recency in Option A, the conjunction of both turns in
integration — a serial-position end-weighting that a next-token predictor over a linear prompt produces
for free.

**Updating is not constituting — and the thin/rich cut tracks the medium.** The rung-ladder
([`essay/update-is-not-constitution`](../essays/update-is-not-constitution.md)) names a decidable cut: a
convention is merely **updated** (thin) if its recovered interpretation is a function of the record's
*content + stamps*, computable by **any single reader**; it is **constituted** (rich) only if recovery
requires a surplus **no single reader could reconstruct**. Rungs (i) overwrite and (ii) integration are
firm but thin; rung (iii) is path-dependence proper; rung (iv) is between-agent constitution, entirely
unbuilt. The throughline of the whole arc is that every result sits on the thin side, and
[`essay/transcript-ceiling`](../essays/transcript-ceiling.md) argues *why*: single-reader-recoverability
is most likely a property of the **medium**. The rich side is *defined* as the surplus a record omits,
and **a text-only stimulus is a final content+stamps record** — so a text probe's reachable space is the
thin side, entire. The within-text routes are not merely unexplored; they are exhausted (the pilot,
reassignment, integration) or **structurally closed** (Option C, the strongest order-load-bearing text
design buildable, came back documented closed for text).

## Where the bottom rung would have to be built

> **Forward-looking conjecture, not a claim.** What follows is a clearly-labelled conjecture about
> instruments, drawn from [`essay/rung-iv-instrument`](../essays/rung-iv-instrument.md) and the
> transcript-ceiling escape-hatch logic. It reports no result and predicts nothing about whether any
> model has or lacks the capacity in question; that is untested by construction.

If the transcript ceiling holds, a genuine relational positive likely requires a setting **outside the
transcript medium** — a live, stateful interaction whose between-party surplus is **not reconstructable
from the final text**. The rung-(iv) instrument essay specifies the requirement: such an instrument is
"not a record to be *read* but a practice to be *participated in* and *scored*," recording observables
that exist only between parties and only while the interaction is live — commitments *undertaken*
(answerability instituted by the other party's uptake), entitlements *granted or withheld by the
interlocutor*, challenges *issued and answered*. These are statuses instituted by uptake, not contents
a string states; recording them requires a live two-party normative practice, not a depiction of one.
Two disciplines bound this conjecture sharply. First, **rung (iii) is not rung (iv)**: a non-text medium
that merely carried arrival-order surplus would *bound* the transcript ceiling (reaching path-dependence
proper) without reaching constitution, which requires the normative observables on top. Second, the
project has **no** in-repo human dyadic-interaction resource carrying normative observables, and the
ratified relational anchor (Clark & Wilkes-Gibbs 1986) is unfetched and scoped to collaborative
reference, not scorekeeping — so building such an instrument would first require opening a new
`decisions/` question. The conjecture names where to look; it does not promise the project will look
there.

## Honest scope and caveats

- **Pilot scale, single panel/date/run.** Every result is single panel/date/run with small N
  (n=12 coined terms/model in v1; n=48/model SPONT in the reassignment and composition arms);
  direction-of-effect, not magnitude. The ceiling effects (1.000 with Wilson LB 0.926) are clean but
  **saturated** — they establish *direction*, not a finer estimate of where a behavior would fail.
- **Internal-contrast-only for the trajectory/order findings.** v2–v4, Option A/B, the implicit control,
  the integration rungs, and the entire C series are `anchor: internal-contrast-only` — within-model
  contrasts over byte-identical content, making **no human-comparison claim**. No in-repo resource
  grounds human order-/path-sensitivity at this grain (Brennan & Clark report an order-*insensitive*
  frequency-over-recency statistic; Hawkins anchors convergence/compression only).
- **The one human-comparison point is bounded by modality/channel mismatch.** Convergence-without-
  compression (sub-line 1) is the arc's only Hawkins-anchored claim; it crosses referent modality and
  channel and is weakest for gemini (already at ceiling). It says nothing about trajectory-dependence.
- **Suspensions ≠ nulls.** The cross-family-dyad composition arm and the ≥4-move depth arm are
  **suspended on budget + low prior** (reopenable spending records), not nulls and not closures. The
  depth/pair/grid generality that *was* tested came back panel-concordant RESPECTS-ORDER (thin).
- **The documented closure is medium-bound and is a promotable outcome, not a failure.** Rung (iii)'s
  rich side is structurally closed *for text-only stimuli* (a transcript is a content+stamps record); a
  non-text medium is untested and out of scope. Per the ratified rung-(iii) decision this documented
  closure is fully promotable.
- **No metaphysical verdict.** A bounded behavioral arc cannot deflate any thesis about what
  meaning-constitution *is*; it deflates the premature empirical reading that constitution is already
  observable between LLMs, and is silent on the theses themselves.

## Explicit revision triggers

This synthesis is revisable; each trigger names the evidence that would force a rewrite.

- **(a) A relational POSITIVE earning a genuine trajectory effect.** A design that isolates a
  path-dependent, between-agent surplus — interpretation tracking the live, ordered trajectory *beyond*
  what the final content+stamps record encodes, under artifact-resistant controls and judged by the
  adjudication gate *not* single-reader-recoverable — would climb off the floor and falsify the central
  negative. The pilot's named live-vs-shuffled gap, on a medium that can carry it, is the canonical
  shape.
- **(b) A non-transcript (rung-iv) instrument.** A relational instrument in a different medium that
  records normative observables (commitments / entitlements / challenges instituted by uptake) would
  move rung (iv) from "characterized" to "measurable" and would bound the transcript ceiling explicitly
  to text-only probes. This would require a new `decisions/` question and a human dyadic-interaction
  resource the repo does not yet hold.
- **(c) A cross-family reopening.** Reopening the suspended cross-family-dyad (heterogeneous) arm with a
  cleaner, less leak-prone design — or any sign of a between-agent surplus appearing where homogeneous
  text dyads stay thin — would bound the floor-characterization to homogeneous text-grid dyads rather
  than confirm it wholesale.
- **(d) A human order/path anchor.** A fetched human resource bearing on human order- or path-sensitivity
  (none is in-repo; Clark & Wilkes-Gibbs 1986 is unfetched) would, for the first time, license a human
  comparison on the trajectory measure — currently an IOU, not a finding — and could turn the lone
  human-comparison point from compression-only into a full relational contrast.

## What this page supersedes and what it does not

This page **promotes and expands** the relational subsection of
[`theory/constructional-meaning-in-llms`](constructional-meaning-in-llms.md) (§"The under-explored
axis: relational meaning"), which records the axis as standing at "one bounded negative" and defers the
rest; the orchestrator stubs that subsection to point here. It does **not** supersede that page's
constructional or grounding content. It is a synthesis, not a result: it states nothing more strongly
than the result pages it consolidates, and its one positive (order-sensitive composition, panel-wide
given a working surface) and its one human-comparison point (convergence-without-compression) are
carried at exactly their cited strength and scope.
