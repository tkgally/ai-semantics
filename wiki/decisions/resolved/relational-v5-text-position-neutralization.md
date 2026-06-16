---
id: relational-v5-text-position-neutralization
title: How should a relational v5 design separate "follows stamped chronology" from "follows text position", and does it need a human anchor or is it internal-contrast-only?
status: resolved
opened: 2026-06-15
opened-by: orchestrator (subagent, surfaced not resolved)
resolved: 2026-06-16
resolved-by: autonomous (adversarial review)
resolution: adopt-default (Option B then A, staged; C the binding fallback); anchor internal-contrast-only
contingent-artifacts:
  - conjecture/commutative-convention
---

# Decision: relational v5 — neutralizing text-position so chronology-following can be seen

> **Status: RESOLVED (2026-06-16) — `resolved-by: autonomous (adversarial review)`.** Opened the
> seventeenth session (2026-06-15); ratified the next session (2026-06-16) by an **independent
> adversarial reviewer** (a fresh agent, not the one doing the downstream work), per
> [`PROTOCOL.md`](../../../PROTOCOL.md) §2 and [`PROJECT.md`](../../../PROJECT.md) §12.3. The
> session boundary held. Tom's standing override outranks this autonomous ratification.
>
> ## Ruling
> **VERDICT: adopt the provisional default — Option B then Option A, staged.** Run the cheap
> stamp-comprehension pre-probe (Option B) first; an Option-A position-rotated, stamp-gated
> chronology arm runs **only for models that pass B**. **Option C is the binding fallback** at
> both gates. **ANCHOR: `internal-contrast-only`** — v5's framing is held strictly within-model;
> no human-comparison claim may be promoted from any v5 result (the human side is undischargeable
> on current resources — Brennan & Clark report an order-*insensitive* statistic, Hawkins anchors
> only convergence — and none is owed because no human contrast is asserted). **ANTI-CHEAT: PASS.**
>
> **Reviewer's reasoning on the two flagged checks.** (1) *Staged B→A is sound and A-alone does
> not subsume B:* Option A's rotation neutralizes position as a competing signal but does not by
> itself establish there is a chronology signal to detect, so an A-only null stays the uninterpretable
> "blind vs comprehending-but-not-using" object; B resolves that at lowest cost. A B-pass is held
> to the narrow license (can read a stamp on demand, not "spontaneously weights it"). (2) *Option A's
> stamp-requiring task cannot be certified unsolvable in the abstract* — it is the single largest
> leak risk — so the ruling ratifies the routing: if a pre-run critic cannot certify it on
> idealized-reader fixtures, the arm does not run and routes to C. Cost/benefit favors the staged
> path (sub-$1 B + a ~$0.63-scale A, well inside $5/day) over closing at C now, because the
> stamp-blindness-vs-chronology-neglect distinction is genuinely relational and not retuned.
>
> **Binding carry-forwards the running session must honor:**
> 1. **Stage strictly B → A.** Pre-register a comprehension floor as the B gate; only passers earn A.
> 2. **Freeze the B stamp format before the B run**, with idealized-reader fixtures + an
>    independent pre-run critic GO. A B-fail for **both** panel models **closes the line at C** —
>    it must **not** trigger a stamp-format retune or a B re-run ("do not tune until comprehension
>    appears").
> 3. **Certify Option A's stamp-requiring task UNSOLVABLE by a positional/lexical shortcut** on
>    idealized-reader fixtures, via independent pre-run critic, before any A run; if it cannot be
>    certified, **route to C** — do not weaken the task to get a GO.
> 4. **Hold the A-null interpretation to its narrow wording:** a B-pass + A-null licenses only
>    "comprehends recency on demand but does not spontaneously weight it here" — never "comprehends
>    recency" in general, never "the models chose to ignore recency." Carry v4's scope limit verbatim.
> 5. **Anchor `internal-contrast-only`, framing strictly within-model.** Any reach for "the way
>    humans do" is a new, currently-undischargeable anchor question — open it fresh.
> 6. **Keep C binding** at both gates; keep [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md)
>    `proposed` with its inconclusiveness located until/unless a clean A result moves it.
> 7. **Budget:** pre-flight each phase; honor a $1.50-class per-arm hard stop; record actuals.
> 8. **Governance:** this fixes the yardstick only — it pre-authorizes no v5 *result*; the running
>    session still owns its own pre-run/post-run critic passes and verification gates.
>
> **Realization (2026-06-16, eighteenth session — Option B executed):** the staged design was
> implemented as the run [`experiments/runs/2026-06-16-relational-stamp-comprehension-b/`](../../../experiments/runs/2026-06-16-relational-stamp-comprehension-b/)
> and the result is [`result/relational-stamp-comprehension-b`](../../findings/results/relational-stamp-comprehension-b.md).
> See that page for the B verdict and which models (if any) earned an Option-A arm.
>
> The original surfacing text (options, provisional default, anchor question) is preserved below
> unchanged as the record the reviewer assessed.

---

> **Status (as surfaced): OPEN (2026-06-15). Surfaced, not resolved.** Per [`PROTOCOL.md`](../../../PROTOCOL.md) §2
> and [`CLAUDE.md`](../../../CLAUDE.md) always-on rule 5, this page states the live
> operationalization question with options and a **provisional default**, and is **not** ratified
> in the session that opened it. A *later* session ratifies it via an independent adversarial-review
> pass (autonomous cross-session procedure, [`PROJECT.md`](../../../PROJECT.md) §12.3); Tom's standing
> override outranks any autonomous ratification. The language below stays provisional throughout.

## The question (precise)

The relational history-perturbation arm has now run four times. The v4 result decoupled stamped
chronology from physical text-position *within a single presentation arm* and found that **both
models follow text-position, not the stamped chronology** — and, critically, that **following
text-position is here indistinguishable from being blind to the stamp values altogether**. That
leaves the decisive relational question (does interpretation track *where in the live history* a
convention was fixed, beyond merely *which content* is present?) unanswerable by any probe whose
"latest convention" coincides with "the last line of the prompt."

So the v5 operationalization question is:

> **How should a v5 design be built so that "follows stamped chronology" is genuinely separable
> from "follows text position" — and, prior to that, how (or whether) v5 should first establish
> that the models comprehend the stamp values at all — with a named human anchor, or an explicit
> `internal-contrast-only` declaration?**

Two sub-questions ride inside it, and the options below take different stances on their ordering:

1. **Comprehension first or geometry first?** v4 cannot distinguish "the model read the round
   stamps and chose position over them" from "the model never parsed the round numbers as recency
   at all." A geometry fix that neutralizes position is wasted effort if the models are simply
   stamp-blind — there would be no chronology signal to detect regardless of geometry.
2. **What anchors a position-following / chronology-following contrast?** It is a within-model
   contrast over byte-identical content; no in-repo human resource currently grounds order- or
   position-sensitivity. Whether v5 *needs* a human anchor or is terminally `internal-contrast-only`
   is itself unresolved (see §"The anchor question", below).

## Why this is live now (the v4 finding, verbatim)

v4 made the within-arm decoupling work and reported a clean direction. Quoting
[`result/relational-history-perturbation-v4`](../../findings/results/relational-history-perturbation-v4.md)
verbatim, with the page as locator:

- The headline, from the result's status block: *"both models track physical text-position, not
  stamped chronology. **claude → TEXT-POSITION ARTIFACT** (Δ_pos CI-clean, Δ_chron null); **gemini
  → INCONCLUSIVE/MIXED**, same direction (strongly position-dominant, with a small chronology
  residual that leaves both CIs off 0.5)."*
  (§ status block.)
- The conflict-cell reading: *"In the EARLY (conflict) cells — where the most-recent-round line
  sits early and an older line sits last — **both models pick the physically-last twin ~0.69–0.75
  of the time, i.e. they pick the chronologically-*earlier* twin against the stamp.** That is
  text-position following."* (§ "The two headline statistics".)
- The scope limit that motivates the comprehension sub-question, verbatim: *"position-following
  here is indistinguishable from stamp-blindness. The stamp-respect control is a single-twin
  record; passing it … shows only that a model is **not derailed by non-monotonic stamp layout** —
  it does **not** prove the model reads the stamp *values* as recency. So this result must **not**
  be read as 'the models chose to ignore recency.' The defensible statement is narrower: **when
  stamped chronology and physical position conflict, both models' picks are governed by physical
  position; whether they parse the round numbers as recency at all is not established by this
  design.**"* (§ "Reading it honestly".)
- The named confound for the whole line, verbatim: *"any future chronology/recency probe over a
  *linear* prompt must decouple stamped recency from physical position, or it cannot distinguish
  'tracks the latest convention' from 'reads the last line.' v4 is the template."*
  (§ "The methodological achievement".)

The downstream [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md)
**stays `proposed` — neither falsified nor certified** (v4 update, 2026-06-14): the models do not
track stamped chronology (so no constituted, path-dependent convention appeared) but are strongly
position-driven (so the commutative null is not strengthened either). v5 is the design that would
move that conjecture off `proposed`, and it cannot be built without first taking the call this page
surfaces.

## The options (provisional designs; alternatives named honestly)

### Option A — randomize/rotate the decisive line's text-position, and gate scoring on a task that REQUIRES the stamp value

Build v5 so the decisive (most-recent-round) line's **physical position is randomized/rotated
across trials** (uniformly over the available slots), so that, *averaged over trials*, "physically
last" carries no information about "chronologically latest" — text-position is neutralized by
design rather than by a single orthogonal crossing as in v4. Crucially, **gate the headline on a
task whose correct answer can only be produced by reading the stamp value**: e.g. ask the matcher
to recover the convention as it stood *at a named round* (not "now"), or to report which of two
twins was the most-recently-coined referent, where the answer is forced to depend on the round
numbers and not on any positional heuristic.

- **Why:** v4 already proved the orthogonal-crossing machinery works at cov 0; rotation generalizes
  it from a 2-level DPOS factor to a position-marginalized design, which both raises power and makes
  "follows text-position" a *flat* (uninformative) strategy rather than a competing signal. Gating
  on a stamp-requiring task is what would let a genuine chronology-follower *score above chance*
  where v4's design left chronology-following and stamp-blindness fused.
- **Design sketch:** keep the ratified v1–v4 instrument class (text-grid referents on the frozen v1
  figures, near-twin pairs, byte-identical content multisets, nonce coined terms, fresh-matcher
  forced-format elicitation, within-model contrast). Add: (a) a position-rotation factor over the
  decisive line; (b) a **stamp-requiring scoring task** (the "as of round k" query) as the headline,
  with the v4-style position/chronology pick retained as a diagnostic; (c) the v4 stamp-respect
  control kept as a manipulation check, *not* as evidence of value-comprehension.
- **Cost / feasibility:** comparable per-trial cost to v4 (still text grids, harvested-and-certified
  stimuli); the rotation multiplies trials per cluster, so power demands more clusters or more
  trials per cluster — plausibly a modest spend increase over v4's ~$0.63 finding-bearing, still
  well inside the $5.00/day budget for a single arm. The harder feasibility risk is **stimulus
  certification**: the v3/v4 fix-lists already show only claude+gemini reliably supply solo-decodable
  near-twin lines at this difficulty (gpt was dropped), and an "as of round k" task tightens the
  decodability demand further.
- **Anchor situation:** still a within-model contrast over byte-identical content → no in-repo human
  resource grounds it; would be `internal-contrast-only` *if* that terminal state is ratified for v5
  (see §"The anchor question"). The stamp-requiring task does **not** by itself create a
  human-comparison claim.
- **Honest risk:** if a stamp-requiring task is itself solvable by a non-chronological positional or
  lexical shortcut, the gate leaks — this option's whole force rests on the task being *unsolvable*
  without reading the round value, which an independent pre-run critic must verify on idealized-reader
  fixtures before any run (the v4 discipline).

### Option B — a stamp-comprehension PRE-PROBE, run BEFORE any chronology test

Before spending on any geometry-decoupled chronology arm, run a cheap, separate **stamp-comprehension
pre-probe** that establishes whether the models read the round stamps *as values* at all — e.g.
present a stamped record and ask directly which round is most recent, or which convention was coined
latest, in a setting where position is neutralized and only the stamp value disambiguates. Only if a
model demonstrably comprehends the stamp does a full chronology-vs-position arm (Option A) run for
that model.

- **Why:** v4's binding scope limit is that position-following is *indistinguishable from
  stamp-blindness*. Option B resolves that ambiguity directly and first, so a later chronology arm can
  be read cleanly: a model that fails the pre-probe is stamp-blind (the v4 result is fully explained,
  no further geometry work needed for it); a model that passes earns the right to a chronology arm
  whose null would then mean something ("comprehends recency but does not use it to fix the
  convention").
- **Design sketch:** a minimal forced-choice or short-answer probe over stamped records, position
  neutralized (rotate or shuffle line order), scored on whether the model identifies the
  stamp-designated most-recent item. Pre-register a comprehension floor (e.g. ≥ some pre-set accuracy)
  as the gate to proceed to Option A. Run as its own cheap wave; route per-model.
- **Cost / feasibility:** the cheapest option — a small forced-choice probe, likely a fraction of a
  v4-scale arm. Highly feasible; it is essentially a manipulation check promoted to a gating
  pre-probe. Low stimulus-certification burden (no near-twin decodability needed for the comprehension
  check itself).
- **Anchor situation:** comprehension of a stamp value is a within-model behavioral check — again
  `internal-contrast-only` in spirit; it makes no human-comparison claim. It does not by itself
  advance the relational conjecture; it *gates* whether advancing it is even possible on current
  resources.
- **Honest risk:** a pass on a direct "which round is latest?" probe shows the model *can* read
  stamps when asked to, but not that it *spontaneously* weights them when coining/recovering a
  convention — so Option B is a necessary precondition, not a substitute for Option A. Best read as
  *staged with* A (B then A), not as an alternative that answers the relational question alone.

### Option C — accept the v4 text-position result as TERMINAL for the relational-history question on current resources (the do-not-spend fallback)

Declare that the relational-history / chronology-following line has reached its honest terminus on
the current instrument and resources: v4 cleanly located the confound and showed both models are
position-driven (and possibly stamp-blind), and no further spend on this arm is warranted until a
materially different resource or instrument is available (e.g. a human order-perturbation anchor, or
a non-linear / non-text elicitation that dissolves the position confound structurally). Keep
[`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md)
`proposed` with its inconclusiveness *located*, and redirect effort to the conjecture's named scope
extensions (image referents, cross-family dyads) or to other tracks.

- **Why:** the charter's modesty rule and the "stop early if only spend-bearing units remain and the
  anchor is not in-repo or queueable" guidance ([`PROTOCOL.md`](../../../PROTOCOL.md) §A5) both bear.
  v4 already extracted the reusable methodological gain (the located confound, the orthogonal-decoupling
  template); a fifth iteration risks the "quietly tuning the operationalization until a null becomes
  positive" failure mode if it is motivated by wanting a chronology signal to appear.
- **Design sketch:** none — this is the no-run fallback. It would close this decision by routing to
  the conjecture's existing scope-extension bets rather than a v5 history arm.
- **Cost / feasibility:** zero spend. Maximally feasible.
- **Anchor situation:** moot — no new result is produced. The existing v4 result stays
  `anchor: internal-contrast-only` as already ratified for the relational line.
- **Honest risk:** terminating here forecloses the one clean follow-up (Option A/B) that could
  distinguish stamp-blindness from chronology-neglect — a distinction that *is* relationally
  meaningful and that v4 explicitly left open. Premature closure would under-use a tractable, in-budget
  next step.

## PROVISIONAL DEFAULT (reasoned recommendation — NOT ratified)

**Provisional default: Option B then Option A, staged — a cheap stamp-comprehension pre-probe first,
and a position-rotated, stamp-gated chronology arm only for models that pass it.** Rationale, offered
provisionally:

- v4's own binding scope limit is that **position-following is indistinguishable from stamp-blindness**
  (quoted above). Option B resolves exactly that ambiguity at the lowest cost, and its outcome
  *changes what Option A can mean*: without B, an Option-A chronology null is uninterpretable (blind or
  comprehending-but-not-using?); with B, it is clean. So B is the precondition that makes A worth its
  spend.
- Option A is the only design on offer that could move the conjecture off `proposed` in the
  chronology direction, and v4 already proved its core machinery (orthogonal decoupling) works — so
  abandoning the line outright (Option C) would forego a tractable, in-budget step that addresses a
  *genuinely* relational distinction, not a retuned one.
- Option C remains the **binding fallback**: if the pre-probe shows the models are stamp-blind (B
  fails for both surviving panel models), then there is no chronology signal to chase on this
  instrument, and the line terminates honestly at v4 — *do not retune the stamp format until something
  positive appears.* Likewise, if an independent pre-run critic cannot certify that Option A's
  stamp-requiring task is unsolvable by a positional/lexical shortcut (the v4 GO-discipline), the arm
  does not run and routes to C.

This default is **explicitly provisional and not ratified**; a later session's adversarial reviewer
should test specifically (a) whether B's "can read a stamp when asked" really licenses A's "null means
comprehending-but-not-using", and (b) whether the staged B→A spend is justified versus closing at C.

## The anchor question (surfaced, NOT resolved)

**Does v5 need a human anchor, or is it terminally `internal-contrast-only`?** This is left open here
deliberately:

- The chronology-vs-position contrast is a **within-model contrast over byte-identical content**
  differing only in stamp and line order — structurally the same kind of measure that the relational
  line has carried as `internal-contrast-only` since
  [`decisions/resolved/conflicting-cue-human-anchor`](conflicting-cue-human-anchor.md)
  and as applied to v4. On that reading, v5 needs **no** resource anchor and should declare
  `internal-contrast-only` — but **only after** an independent cross-session ratification, never as a
  way to dodge a genuine anchor obligation ([`CLAUDE.md`](../../../CLAUDE.md) §typed-links/anchor
  discipline).
- The countervailing consideration: a v5 that interprets a chronology *null* as evidence about
  whether LLM conventions are path-dependent edges toward a **human-comparison** reading (the
  [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md) predicts
  a human/LLM contrast at exactly this grain). The conjecture itself records that **no in-repo
  resource anchors human order-sensitivity**: Brennan & Clark 1996
  ([`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md))
  anchors historicity and partner-specificity but never perturbs the *order* of an interaction
  history (its historical variables are frequency and recency, not sequence position — the source
  page records that "The paper never scrambles or reorders an interaction history") and reports the
  verbatim *"Frequency of use better explains our data than does simple recency"* — an
  order-*insensitive* statistic — so it cannot ground a human order-/position-sensitivity comparison. Hawkins
  ([`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md)) anchors the convergence
  baseline only.
- **The unresolved tension:** if v5's force is kept strictly within-model (does *this* model's pick
  track stamp value vs text position), `internal-contrast-only` is the honest terminal state and no
  anchor is owed. If v5's framing reaches for "LLM conventions are/aren't path-dependent *the way
  human ones are*," then it incurs a human-anchor obligation that **no in-repo resource can currently
  discharge** — which would itself push toward keeping the result internal-contrast-only or toward
  Option C. A later session must decide which framing v5 actually carries before any result is
  promoted; this page only surfaces the choice.

## What a ratifying session must check

- Whether the staged B→A default is the right ordering, or whether A's rotation alone (Option A only)
  already neutralizes position well enough to skip the pre-probe.
- Whether Option A's stamp-requiring task can be certified unsolvable by a non-chronological shortcut
  on idealized-reader fixtures (the v4 GO-discipline) — if not, route to C.
- The anchor declaration: ratify `internal-contrast-only` for v5 explicitly (if the framing stays
  within-model), or require a queued human order-perturbation anchor (if the framing reaches for
  human comparison) — never let the terminal state be used to dodge a genuine obligation.
- Anti-cheat: confirm the default biases *against* a free positive (a stamp-blind pre-probe outcome
  must be allowed to *close* the line at C, not trigger a stamp-format retune), and that ratification
  fixes the yardstick, never the result.
