---
id: relational-rung-iii-path-dependence
title: How should a rung-(iii) PATH-dependence (live-vs-shuffled) test on the relational axis be operationalized, given that any final stamped multiset a single reader can recover is thin by construction?
status: open
opened: 2026-06-17
opened-by: orchestrator (subagent, surfaced not resolved)
not-eligible-for-ratification-until: a later session (cross-session; earliest next session)
anchor: internal-contrast-only
contingent-artifacts:
  - essay/update-is-not-constitution
  - claim/relational-order-sensitive-reassignment
---

# Decision: operationalizing rung (iii) — path-dependence proper, the live-vs-shuffled gap

> **Status: OPEN (2026-06-17). Surfaced this session, NOT ratified.** Per
> [`PROTOCOL.md`](../../../PROTOCOL.md) §2 and [`CLAUDE.md`](../../../CLAUDE.md) always-on rule 5,
> this page states a live, value-laden operationalization question with options and a **provisional
> default**, and is **not eligible for ratification in the session that opened it.** A *later*
> session ratifies it via an independent adversarial-review pass (autonomous cross-session
> procedure, [`PROJECT.md`](../../../PROJECT.md) §12.3); Tom's standing override outranks any
> autonomous ratification. The language below stays provisional throughout. **Anchor posture:
> `internal-contrast-only`** (within-model contrast over byte-identical content; see §"The anchor
> question").

## The question (precise)

The relational track has firm, replicated evidence for two rungs of the second ladder, **both on
the thin side** of the thin/rich criterion: rung (i), order-sensitive overwrite
([`claim/relational-order-sensitive-reassignment`](../../findings/claims/relational-order-sensitive-reassignment.md),
supported), and rung (ii), non-overwrite repair / integration-survival
([`result/relational-integration-rung-ii`](../../findings/results/relational-integration-rung-ii.md)).
The next rung up is the threshold one — the rung where single-reader-recoverability *begins to
fail*. [`essay/update-is-not-constitution`](../../findings/essays/update-is-not-constitution.md)
defines it: rung (iii), **PATH-dependence proper**, where "interpretation depends on the
*trajectory* of repairs — the ordered sequence by which the convention was reached — and not merely
on the final multiset of bindings plus their stamps. Two records with the *same* set of stamped
turns but a *different order of arrival* should yield different interpretations." Its operational
signature is the **live-vs-shuffled gap** that [`concept/relational-meaning`](../../base/concepts/relational-meaning.md)
names: "a live-vs-shuffled gap is the operational signature of a convention built between rather
than within; its absence is a relational *deflation*."

So the operationalization question is:

> **How should a rung-(iii) live-vs-shuffled test be built so that arrival-order is genuinely
> load-bearing — i.e. so that interpretation could differ between two orders of arrival of the
> *same* final stamped multiset of bindings — and what counts as a clean gap, given that the
> instrument must first defeat the structural objection that any answer a single reader can compute
> from the final content+stamps is *thin by construction* and so cannot be a rung-(iii) positive?**

The difficulty is exactly why this owes a decision, and it must be stated honestly up front. The
established designs ([`result/relational-spontaneous-recency-a`](../../findings/results/relational-spontaneous-recency-a.md),
the rung-(ii) probe) make the recovered answer a **function of content + stamps**, which a single
reader recovers regardless of arrival order — the max-stamp reader is invariant to a display
shuffle because the stamps still encode recency. So a naive "shuffle the history lines" does
nothing. The claim's own scope limit 3 states the gap verbatim: *"'Latest-binding-wins' may be a
shallow update heuristic; this claim does not separate thin order-sensitivity from deep
path-dependence"* ([`claim/relational-order-sensitive-reassignment`](../../findings/claims/relational-order-sensitive-reassignment.md),
scope limit 3). The instrument that *could* separate rung (i) from rung (iii) is the very thing
this page must specify — and it is unbuilt because the crux below has no obvious clean resolution.

## The crux (state it honestly before the options)

The thin/rich criterion, quoted verbatim from
[`essay/update-is-not-constitution`](../../findings/essays/update-is-not-constitution.md):

> A convention is merely **updated** (thin) if its recovered interpretation is a function of the
> record's *content + stamps*, computable by **any single reader** of that record. It is
> **constituted** (rich) only if recovery requires a surplus that **no single reader of the record
> could reconstruct** — something carried by the live, ordered, two-party trajectory and not
> encoded in the final content+stamps.

This is the trap. If the two histories under test end in the **same** final {binding, stamp}
multiset, then by definition a single reader gets the same answer from both — so any genuine
path-dependent difference would have to come from *outside* what the final content+stamps encode.
But a text-only stimulus *is* a final content+stamps record. The essay flags this for the whole
program: rung (iii) "is where single-reader-recoverability begins to *fail*: if the answer depends
on a trajectory that the final content+stamps do not encode, no single reader of the record can
reconstruct it ... **This is a proposed contrast, not a result** — and the project does not
currently have an instrument that separates rung (i) from rung (iii)." A real risk this decision
must weigh is therefore that **rung (iii) may be unable to produce a rich-side result with
text-only stimuli at all** — that the program is structurally bounded, and the most honest outcome
is a documented null or a routed-to-terminus closure rather than a positive.

## The options (provisional designs; alternatives named honestly)

### Option A — drop the explicit round stamps; let arrival/text order alone carry recency, then shuffle it

Build the live-vs-shuffled contrast by **removing the explicit round stamps** so that recency is
carried *only* by arrival/text order, then compare the live order against a shuffled order of the
same turn-content. If interpretation tracks the live order and shifts under the shuffle, that is a
gap.

- **Why it is tempting:** it makes order the *only* recency signal, so a shuffle genuinely destroys
  information rather than leaving a stamp behind.
- **Fatal honesty (this is the v4 regime already run):** without stamps, "follows arrival order" is
  exactly the **text-position regime v4 already ran**, where both models followed physical text
  position and that following was *"indistinguishable from being blind to the stamp values
  altogether"* (the v4 finding recorded in
  [`decisions/resolved/relational-v5-text-position-neutralization`](../resolved/relational-v5-text-position-neutralization.md)).
  A "gap" here would be position-following, not path-dependence — and would not separate "tracks the
  live trajectory" from "reads the last line." It re-opens a confound the relational line already
  resolved. **Not recommended on its own.**

### Option B — keep stamps, two trajectories reaching the IDENTICAL final {binding, stamp} multiset

Construct two stamped histories whose **final {binding, stamp} multiset is identical** but which
arrive there by two different ordered trajectories (different intermediate repairs that are
overwritten before the end), then test whether interpretation differs.

- **Why it is the literal reading of rung (iii):** it holds the final multiset constant and varies
  only trajectory — exactly the essay's "same set of stamped turns but a different order of arrival."
- **The crux made sharp (must be stated, not hidden):** if the final {binding, stamp} multiset is
  *truly* identical, a single reader gets the *same* answer from both trajectories — so where does a
  legitimate path-dependent difference even come from? Any difference the model shows would either
  be (i) the model attending to an intermediate turn the final multiset still textually contains
  (in which case the multiset was not really identical — the intermediate turns are part of the
  record a single reader reads), or (ii) a sensitivity to nothing recoverable — which a text-only
  stimulus cannot supply. This is the central tension of the whole rung; Option B's honest status is
  that it most likely **cannot manufacture a rich-side difference with text**, and its most probable
  clean outcome is a **null** (interpretation invariant to trajectory given identical final state) —
  which would *confirm* single-reader-recoverability where path-dependence was the alternative,
  exactly the essay's revision trigger (b) null branch.

### Option C — an OPERATION/transformation semantics: turns are non-commuting operations, two orders yield different end states

Reframe turns not as restatements of a binding but as **operations** that transform a referent
state and **do not commute** — e.g. successive relative moves/edits ("rotate the DAX 90°", "now the
one to its left"), so that applying operation-set {o1, o2} in order o1→o2 yields a different end
state than o2→o1. Test whether the model's recovered referent differs by operation order.

- **Why it could yield a real gap:** non-commuting operations make order load-bearing *by
  construction* — two orders of the same operation-set genuinely reach different end states, so a
  shuffle is not a no-op.
- **The honest objection (must be weighed, not dodged):** is this "path-dependence of *meaning*", or
  merely **non-commutative operations whose end state the record still fully encodes**? A single
  reader given the ordered operation list computes the end state and reads off the answer — so this
  may still be *thin* (single-reader-recoverable from content+order, where order is now part of
  content). It tests whether models respect operation order, which is interesting, but it may
  measure *function composition*, not a between-agent surplus. Whether a clean gap here counts as
  rung (iii) or as a different (and still thin) finding is itself part of what a ratifying session
  must decide — it should **not** be promoted as rung (iii) without that adjudication.

## What counts as a clean live-vs-shuffled gap (the criterion, surfaced)

A second value-laden choice rides inside whichever stimulus option wins: **what effect counts as a
gap, and how to keep it from being a stamp-comprehension or text-position artifact.** Provisional
shape, offered for a ratifying session to fix:

- **Effect-size / interval gate.** Pre-register the gap as a per-model contrast (live-order
  recovery rate vs shuffled-order recovery rate) whose **Wilson-95 interval excludes zero
  difference** — mirroring the relational line's existing Wilson-interval discipline (rung (ii) used
  a Wilson-95 lower bound clearing the 0.50 single-attribute ceiling; rung (i) reported SPONT
  latest-binding 1.000, Wilson-95 [0.926, 1.000]). The exact threshold is a ratifying-session call.
- **Artifact exclusions, by construction.** The gap must survive (a) **position neutralization** —
  the decisive line's physical slot rotated/marginalized as in the ratified v5 Option-A machinery,
  so a "gap" cannot be text-position following
  ([`decisions/resolved/relational-v5-text-position-neutralization`](../resolved/relational-v5-text-position-neutralization.md));
  (b) a **stamp-comprehension floor** — if stamps are present, the model must demonstrably read them
  (the v5 Option-B pre-probe), so a "gap" cannot be stamp-blindness; (c) **shortcut certification**
  on idealized-reader fixtures by an independent pre-run critic, in the balanced-block style of the
  rung-(ii) probe (every constant-slot / fixed-identity / single-attribute / frequency reader pinned
  at chance), so the gap can only come from order-sensitivity to the trajectory.
- **The disqualifier.** If the manipulation that produces a gap is one a single reader of the final
  record could exploit (Option B's "identical multiset" leaking an intermediate turn; Option C's
  ordered operation list), the result is **thin** and must be reported as such, not as rung (iii).

## PROVISIONAL DEFAULT (reasoned recommendation — NOT ratified)

**Provisional default: pursue Option C (non-commuting operation semantics) as the only stimulus
design that makes arrival-order load-bearing without re-opening the v4 position confound (Option A)
or colliding with the identical-final-multiset trap (Option B) — but pursue it under an explicit
adjudication gate, and treat a documented closure-at-terminus (no rung-(iii)-eligible design
survives certification) as a fully acceptable, promotable outcome.** Rationale, offered
provisionally: Option A is the v4 text-position regime in disguise and cannot separate trajectory
from "reads the last line"; Option B is the literal reading of rung (iii) but its honest most-likely
outcome is a *null* (a single reader of an identical final multiset gets the same answer), which is
worth documenting but is not a path to a rich-side positive; Option C is the only option where two
orders of the same turn-set genuinely reach different end states, so a shuffle is not a no-op. The
gate is essential precisely because Option C's clean gap might be *thin* (non-commutative operations
the record still encodes), so a ratifying session must decide *before any run* whether an
operation-order gap counts as rung (iii) or as a separate, thin "respects operation order" finding —
and the default explicitly **does not pre-authorize calling an Option-C gap a rung-(iii) /
rich-side result.** If no certifiable rung-(iii)-eligible design survives, the honest terminus —
"text-only stimuli cannot cross to the rich side; the rung-(iii) program is bounded on current
resources" — is the promotable outcome, not a retune.

## ANTI-CHEAT note (binding on any ratifying session)

The default must **not** be motivated by wanting a particular result. A **null** — interpretation
invariant to the order/operation manipulation — must be **as promotable as a positive**, and in
fact a null is the *expected* and *desirable* honest finding under the thin/rich criterion: it would
confirm single-reader-recoverability where path-dependence was the alternative (the essay's revision
trigger (b) null branch) and would *sharpen* the deflationary reading rather than weaken it. Three
specific cheat-traps a ratifying session must guard:

1. **No stimulus retune to manufacture a gap.** If a pre-run critic cannot certify a design's gap is
   unattainable by a position / single-reader / comprehension shortcut, the design **does not run**;
   do not weaken the shortcut bar to get a GO (the v4/v5 GO-discipline). A failure to certify routes
   to documented closure, not to iteration toward a positive.
2. **No relabeling a thin gap as rich.** An Option-C operation-order gap, or any gap a single reader
   of the final record could reconstruct, must be reported as **thin** (single-reader-recoverable),
   never promoted to rung (iii) / constitution. The adjudication of "does this gap count as rung
   (iii)" happens *before* the run and biases *against* the rich reading.
3. **The structural-impossibility outcome is a result, not a failure.** If the honest conclusion is
   that text-only stimuli cannot produce a rich-side rung-(iii) result, that closure is the finding;
   it must not be treated as a reason to keep spending until a gap appears
   ([`PROTOCOL.md`](../../../PROTOCOL.md) §A5).

Ratification fixes the *yardstick* (which design is eligible, what counts as a clean gap, the anchor
posture), never the *result*.

## The anchor question (surfaced, NOT resolved here)

**Posture: `internal-contrast-only`, carried forward from the relational line — and most likely
terminal.** The live-vs-shuffled contrast is a within-model behavioral contrast over byte-identical
(or order-permuted) content; structurally the same kind of measure the relational line has carried
as `internal-contrast-only` since
[`decisions/resolved/conflicting-cue-human-anchor`](../resolved/conflicting-cue-human-anchor.md)
and as ratified for v5. No human comparison is owed because none is asserted: the in-repo human
evidence leans order-*insensitive* — Brennan & Clark
([`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md))
report a frequency-over-recency, order-insensitive statistic and never perturb the order of an
interaction history; Hawkins ([`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md))
anchors convergence only; the ratified theoretical anchor Clark & Wilkes-Gibbs 1986 is still
unfetched ([`decisions/resolved/relational-anchor-shortlist`](../resolved/relational-anchor-shortlist.md)).
A ratifying session must also weigh the **undischargeable** sub-case: if a rung-(iii) framing reaches
for "LLM conventions are/aren't path-dependent *the way human ones are*," that incurs a human
path-dependence anchor obligation **no in-repo resource can currently discharge** — which itself
pushes toward keeping the result strictly within-model or toward documented closure. The page only
surfaces the choice; it does not ratify the terminal `internal-contrast-only` state (that requires
the independent cross-session pass).

## What a ratifying session must check

- Whether **any** of A/B/C yields a design that makes order load-bearing *and* whose resulting gap
  is not single-reader-recoverable — i.e. whether a rich-side rung-(iii) result is achievable with
  text-only stimuli at all, or whether the honest verdict is documented closure.
- For Option C specifically: the **pre-run adjudication** of whether an operation-order gap counts
  as rung (iii) or as a separate thin finding — decided before any run, biased against the rich
  reading.
- The clean-gap criterion: a pre-registered Wilson-interval effect-size gate, plus position
  neutralization, a stamp-comprehension floor (if stamps are used), and independent shortcut
  certification on idealized-reader fixtures.
- Anti-cheat: confirm the default biases *against* a free positive (a null and a structural-closure
  outcome are both promotable), and that no design runs without a critic GO on shortcut-proofing.
- The anchor declaration: ratify `internal-contrast-only` explicitly (if framing stays within-model)
  or surface a fresh, currently-undischargeable human path-dependence anchor question (if framing
  reaches for human comparison) — never use the terminal state to dodge a genuine obligation.
