---
type: design
id: relational-history-perturbation-v4
title: Relational v4 — the within-arm chronology/position decoupling (a non-adjacent perturbation point; the decisive commutativity test the v3 forward arm could not reach)
meaning-senses:
  - relational
  - distributional
  - model-internal
status: "drafted — NOT RUN; design only"
contingent-on: []
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: operationalizes
    target: conjecture/commutative-convention
  - rel: supersedes
    target: design/relational-history-perturbation-v3
  - rel: depends-on
    target: result/relational-history-perturbation-v3
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: concept/relational-meaning
  - rel: supports
    target: open-question/relational-meaning-pilot
---

# Design: relational history-perturbation probe (v4)

> # ⚠️ DRAFT — DESIGN ONLY — NOT RUN ⚠️
> **No model calls. No spend. No run directory. No stimuli built.** This is a
> design-writing artifact: it specifies an experiment that **has not happened** and
> **must not be run** until an independent pre-run critic GOes it and the orchestrator
> freezes a `PREREG.md`. Every number in the §"What v3 actually found" block below is
> **quoted from the v3 result/run pages**, which were actually run; **no v4 numbers exist
> anywhere in this file** and none may be fabricated. The cost figure is an **estimate for
> a run that has not occurred**.

This design supersedes
[`design/relational-history-perturbation-v3`](relational-history-perturbation-v3.md) and
exists for **one precise reason**: v3 produced a forward chronology elevation that
**vanished under direction reversal**, and — critically — its forward arm **could not, by
construction, separate "chronologically last" from "physically last in the presented
text."** v4 keeps the v3 instrument's shape, fixes its two named power/panel defects, and
adds the one structural change that lets a **single arm** dissociate chronology from
text-position: a **non-adjacent perturbation point**.

## What v3 actually found (quoted verbatim — no new numbers)

From [`result/relational-history-perturbation-v3`](../../wiki/findings/results/relational-history-perturbation-v3.md):

> **Verdict, pre-registered rule: INCONCLUSIVE/MIXED for the two informative models
> (claude, gemini); METHODOLOGICAL NULL for gpt.** The falsification clause did **not**
> fire and the commutative null was **not** certified.

The clean, well-powered model (gemini, gate 0.92, 7/9 clusters, both trial floors passed)
showed a strong forward signal that did not survive reversal. Quoting the result page's
own number table and honest reading:

> | gemini | 7/9 (acc 0.92) | **0.780 [0.659, 0.902]** | 0.595 [0.500, 0.738] | 0.500 [0.429, 0.571] | 24 ✓ / 36 ✓ | INCONCLUSIVE/MIXED |

> "Forward ρ_chron and ρ_phys are **identical by construction** in this design — the
> chronologically-last and physically-last lines coincide in the forward arm — so the
> forward column alone cannot separate chronology-tracking from position-tracking; only
> the reversed arm decouples them."

And the over-claim the v3 post-run verifier explicitly **refuted** (this is the reading
v4 must NOT smuggle back in):

> "A first-pass reading called this 'physical position, not stated chronology.' **That is
> an over-claim and is not what the data show.** A pure physical-position-following account
> predicts the reversed-arm ρ_phys to be *above* 0.5 … but gemini's reversed ρ_phys
> collapses to **exactly 0.500 (chance)**, which *refutes* that account, not supports it.
> … **The only defensible claim is the weaker one: the forward elevation does not survive
> direction reversal under *either* interpretation** … The position-vs-chronology question
> itself stays open; this design does not resolve it."

The result page names the fix this design implements:

> "A design that separates the two *within* a single arm (e.g. a non-adjacent perturbation
> point) is the real next step if the position-vs-chronology question is to be answered
> rather than bounded."

**The precise v3 cause v4 removes:** v3's history is a 4-line record (2 descriptions of X +
2 of Y) where the chronologically-last line is *always* the physically-last line in the
forward arm (ρ_chron ≡ ρ_phys forward, by construction), and the reversal arm decouples
the two only *across* conditions, not *within* one. The two competing readings of the
forward elevation — "tracks stated chronology" vs. "tracks the last line of text" — are
therefore **confounded inside every forward cell** and only separable by comparing two
*different* presentation directions, where the signal turned out to be direction-fragile.
v4 dissolves that confound by making chronology and text-position **vary independently
inside a single presented record**.

## The mechanism — a non-adjacent perturbation point (the one structural change)

### v3's geometry, and why it confounds

In v3 each mixed record is 4 lines, rendered as a list under an INTRO that states the
direction ("earliest first" / "most recent first"); the chronological order is conveyed
*purely by physical position plus the stated direction*. So "the chronologically-last
evidence" and "the physically-last line" are the **same line** in forward and are swapped
*wholesale* in reverse. No single record ever contains a line that is chronologically late
but physically early (or vice versa). Chronology and text-position are perfectly collinear
within an arm.

### v4's geometry — explicit per-line chronology, broken collinearity

v4 keeps text-grid referents, near-twin pairs, byte-identical content multisets, nonce
coined terms, fresh-matcher probe-shaped elicitation, and the within-model contrast — the
ratified v2/v3 instrument class. The single change is in **how chronology is conveyed and
where the decisive evidence sits**:

1. **Chronology is stamped explicitly on each line, not inferred from position.** Each
   evidence line carries an explicit, unambiguous **round/turn timestamp** (e.g.
   "Round 1: …", "Round 2: …", "Round 5: …"). Now "what came earlier in the conversation"
   is carried by the *stamp*, and "what sits earlier in the presented text" is carried by
   *line order* — two channels that can be set independently. (This is the minimal
   addition that makes the dissociation expressible at all; the v3 INTRO direction-label
   becomes secondary scaffolding rather than the sole carrier of chronology.)

2. **A non-adjacent perturbation point: the chronologically-decisive evidence sits in the
   physical middle, with chronologically-earlier filler lines *after* it in the text.**
   The record describes a coined term first attached to twin X, then **reassigned to twin
   Y at a chosen round** (the perturbation), and the decisive Y-evidence (the most recent
   round) is placed at a **non-terminal physical position**, followed in the text by lines
   that are chronologically *earlier* (the original X-evidence, or low-numbered rounds).
   The "most recent in chronology" line is therefore **not** the "last line of text" — the
   two are dissociated **inside one record, in one presentation arm**.

3. **The 2×2 (or 2×2-equivalent) the v3 single contrast could not reach.** Within a single
   arm, v4 crosses two binary factors over the otherwise byte-identical content multiset:

   | | text-position of decisive evidence: EARLY | text-position of decisive evidence: LATE |
   |---|---|---|
   | **chronologically-latest = Y (reassigned-to-Y)** | cell A | cell B |
   | **chronologically-latest = X (reassigned-to-X)** | cell C | cell D |

   - A **chronology reader** picks the chronologically-latest twin regardless of where that
     line sits in the text: predicts Y in A and B, X in C and D — a main effect of
     *chronology* (the stamp), **no** main effect of text-position.
   - A **text-position reader** picks whichever twin's evidence is physically last in the
     record, regardless of stamp: predicts a main effect of *text-position*, **no** main
     effect of chronology.
   - A **content-only (commutative/aggregation) reader** is at chance on the discriminating
     pick: the content multiset is byte-identical across all four cells (only stamps and
     line order move), so an order-and-position-insensitive set reader shows **neither**
     main effect — ρ near 0.5 throughout. This is the conjecture's bet.

   The two main effects are **orthogonal within a single arm**, which is exactly what the
   v3 forward arm (collinear) and the v3 cross-arm contrast (direction-fragile) could not
   deliver. The presentation-direction arm is **retained** from v3 as a secondary,
   convergent check (the house pattern: a robust effect should survive reversal), but it is
   **no longer load-bearing for the chronology-vs-position decoupling** — the 2×2 carries
   that within a single arm. This demotes the very feature whose fragility made v3
   inconclusive from "the only decoupler" to "a robustness cross-check."

### The exact contrast and headline statistic

- **Primary headline statistic — the chronology main effect, Δ_chron.** Over gated,
  parsed, in-pair mixed trials, the fraction of picks landing on the
  **chronologically-latest twin** (by stamp), computed **at each level of text-position**
  (decisive-line-early vs decisive-line-late) and **pooled**:
  Δ_chron = ρ(pick = chronologically-latest twin) − 0.5, with the *position* factor
  balanced so the content multiset and per-twin salience cancel across the symmetric design
  (the v2/v3 cancellation algebra, applied to the 2×2). A chronology reader gives Δ_chron
  CI-clean above 0; a content-only reader gives Δ_chron CI-including-0.
- **Co-primary discriminant — the text-position main effect, Δ_pos.** The fraction of picks
  landing on the **physically-last-line twin**, pooled across chronology levels, centered at
  0.5. This is the diagnostic that v3 could only obtain by reversing the whole record; v4
  obtains it **within an arm**. A text-position reader gives Δ_pos CI-clean above 0 while
  Δ_chron is null.
- **The decoupling is the joint reading of (Δ_chron, Δ_pos):** because the two factors are
  crossed and orthogonal within one arm, the pair separates the three readers cleanly,
  which a single ρ on a collinear record cannot:
  - (Δ_chron clean-positive, Δ_pos null) → **chronology-tracking** (non-commutative; the
    falsification of the conjecture's invariance bet).
  - (Δ_pos clean-positive, Δ_chron null) → **text-position-tracking** (a methodological
    artifact about prompt geometry; says nothing relational — the honest home for the
    reading the v3 verifier refused to assert because v3 could not earn it).
  - (both null) → **commutative / content-only** (the conjecture's bet, strengthened).
  - (both clean-positive) or (arms/cells disagree) → INCONCLUSIVE/MIXED.

This is the dissociation the project's handoff asked for: chronology and physical position
are decoupled **WITHIN a single arm**, so the decisive verdict no longer hinges on a
fragile across-direction comparison.

## Conditions (frozen geometry — to be pinned in a future run's PREREG, NOT here)

Per panel model, per near-twin pair (X, Y), per certified description sample s, the v4 cell
set is the 2×2 above (chronologically-latest twin ∈ {X, Y} × decisive-line text-position ∈
{early, late}) **× presentation direction {fwd, rev}** (retained convergent check), over a
**byte-identical content multiset** within a cluster (same 2-X-descriptions + 2-Y-descriptions
bag; only the round-stamps and the line order move). Cluster = (pair × sample), the bootstrap
and gating unit, exactly as v2/v3.

- **CONSISTENT controls (manipulation gate), retained from v3:** per-cluster control records
  where all evidence (and all stamps) point to ONE twin, in both presentation directions; the
  gate requires all controls correct. Retained as defense-in-depth on top of per-description
  certification.
- **A v4-specific control the 2×2 enables — the "stamp-respect" check.** Because chronology is
  now an explicit stamp rather than a position cue, v4 adds a **single-twin stamp-ordering
  control**: a consistent record whose lines are *shuffled in text but correctly stamped*, to
  verify each model reads the stamps at all before any chronology pick is interpreted. A model
  that ignores stamps fails this control and is read as **stamp-blind → METHODOLOGICAL NULL on
  the chronology question** (it cannot, even in principle, show stamp-driven chronology
  tracking; its picks reduce to text-position). This control is what licenses the Δ_chron
  reading; it is pre-registered as gating, not descriptive.
- The exact per-cluster cell count, the number of filler lines needed to place the decisive
  line non-terminally while holding the multiset byte-identical, and whether the 2×2 needs a
  balanced "both-twins-late-vs-early" rotation to cancel per-twin salience, are **frozen in the
  run's PREREG after the pre-run critic**, not invented here. The design commits to the
  *structure* (orthogonal chronology × position within an arm, byte-identical multiset, gated
  by certification + the stamp-respect control); the run fixes the integers.

## Panel decision (the v3 fix-list, item by item)

The v3 result/run leaves two explicit panel defects, named in its Caveats §1–2 and its
"v4 choice" handoff. v4 resolves both:

- **gpt: DROP from the v4 finding-bearing panel.** The v3 result is unambiguous: gpt
  "never clears certification past 6/9 clusters" and reached only **1/6** passing
  manipulation-gate clusters (control acc 0.58), a **METHODOLOGICAL NULL** carrying "no
  commitment-bearing commutativity signal." Its description quality "has been the relational
  line's weak link since v1." v4 introduces a *more demanding* stimulus (a multi-line
  reassignment record with stamps), which would not raise gpt's certification yield — it
  would lower it. Re-sourcing gpt's stimuli is not a free move: the v3 design already
  argued that *new figures* would "add an uncontrolled stimulus dimension (uncertified
  difficulty profile) in the very run whose job is to remove stimulus noise," and a fresh
  *harvest* already failed gpt twice (v1 live + v3 certified-with-top-up). **Decision:**
  gpt is **dropped from the v4 finding-bearing panel** and run, if at all, only as a
  **descriptive, never-gating** appendix (its picks reported, never entering a verdict),
  exactly as the v3 cross-model cross-check was deferred. Rationale (one line): two
  independent harvest+certification attempts have shown gpt cannot supply solo-decodable
  near-twin descriptions at this difficulty, so spending finding-bearing calls on it buys a
  foregone METHODOLOGICAL NULL.
- **claude: RAISE power (more clusters/items).** v3 left claude **under-powered** —
  floor36 unmet (30 < 36 gated in-pair trials/direction), 5/9 clusters passing the gate —
  so even an all-null claude could not be null-certified. **Decision:** v4 raises claude's
  cluster/item count above the v3 nominal so that, at the v3-observed gate-survival rate,
  claude clears the **≥36 null-certification floor and the ≥24 effect floor in every
  cell of the 2×2** with margin. The concrete route (more description samples per pair on
  the *existing* frozen v1 figures, mirroring v3's "harvest route not new-figures route,"
  so comparability with v1/v2/v3 is preserved and no uncertified difficulty profile is
  introduced; the exact sample count is frozen in the run PREREG against the v3-realized
  gate-survival rate). Rationale (one line): the clean model must be powered to *certify a
  null* and to *resolve the 2×2 in every cell*, or v4 reproduces v3's "can't certify either
  way" outcome for the only model worth reading.
- **gemini: retained at raised power.** gemini was the v3 clean read (gate 0.92, both
  floors passed); v4 retains it and raises its cluster count in step with claude so the 2×2
  is powered in every cell.

Net finding-bearing panel: **claude + gemini, both at raised power; gpt descriptive-only or
dropped.** Cross-family divergence between the two retained models stays first-class data,
as for the whole relational line.

## Frozen analysis plan (to be pinned in the run PREREG pre-run; mirrored as code, as in v3)

All thresholds, floors, the bootstrap, and the verdict map are **frozen pre-run** and the
verdict mapper is **code** (an ordered, exhaustive if/else tree with an explicit final
else), exactly as v3's `analyze.py verdict()`. No retuning after seeing data.

- **Headline statistics:** Δ_chron (chronology main effect, centered at 0.5) and Δ_pos
  (text-position main effect, centered at 0.5), each computed over gated, parsed, in-pair
  mixed trials, pooled across the orthogonal factor and across presentation direction, with
  the per-twin-salience cancellation balanced by design.
- **CIs:** clustered bootstrap, 10,000 resamples over (pair × sample) clusters per model,
  PREREG-seeded, percentile method — the v3 machinery unchanged. **Degenerate (zero-width)
  CIs carry no inferential weight and satisfy no clause** (the v3 rule, retained).
- **Guards and floors (the v3 fix-list, retained and applied to the 2×2):**
  - **≥k-gated-cluster guard, k = 3**, applied symmetrically to every CI-bearing clause
    (so no single degenerate cluster can decide anything — the v3 latent-defect fix).
  - **Trial floors:** ≥24 gated in-pair parsed trials **per cell of the discriminating
    factor** for any effect clause (chronology-tracking or position-tracking); **≥36** for
    null-certification (the heavier burden on an absence claim). claude's raised power
    exists precisely to clear these.
  - **Stamp-respect control** must pass (per model) before any Δ_chron reading is
    interpreted; failure → METHODOLOGICAL NULL on the chronology question.
- **Verdict map (frozen; ordered if/else, first clause that fires wins; precedence
  METHODOLOGICAL NULL > UNDER-POWERED > the CI clauses > final else):**
  1. **METHODOLOGICAL NULL** — < 3 gated clusters in any cell, OR the stamp-respect control
     fails (stamp-blind), whatever the point estimates say.
  2. **UNDER-POWERED** — out-of-pair > 0.5 on parsed picks.
  3. **commutative-convention FALSIFIED (non-commutative, chronology-tracking)** — Δ_chron
     CI excludes 0.5 (above) **and** Δ_pos CI includes 0.5, with the ≥24 floor met in every
     cell; **and** (convergent, not required) the presentation-direction arms agree in sign.
     → the conjecture's invariance bet falsified for that model under forced-label
     elicitation; the positive is *surfaced, not auto-promoted* (contingency discipline).
  4. **TEXT-POSITION ARTIFACT** — Δ_pos CI excludes 0.5 (above) **and** Δ_chron CI includes
     0.5, ≥24 floor met. → a methodological finding about prompt geometry / instruction
     neglect; **says nothing relational** (this is the honest terminal home for the reading
     the v3 verifier refused to assert because v3's collinear forward arm could not earn it).
  5. **commutative-convention's invariance bet, COMMUTATIVE-NULL-CERTIFIED** — Δ_chron CI
     **and** Δ_pos CI both include 0.5 (non-degenerate) with the ≥36 floor met in every cell.
     → extends the v1/v3 null to "position *and* stamped-chronology of a reassignment do not
     move the pick"; the conjecture stays `proposed`, **strengthened, not proven**;
     "certified" means the pre-registered null clause fired, never a precise zero.
  6. **clean NULL but floor unmet** (named-gap sub-label) — both CIs include 0.5
     (non-degenerate), guard holds, out-of-pair ≤ 0.5, but the ≥36 floor is unmet in some
     cell → no clause fires; the absence may not be certified on that n.
  7. **Else: INCONCLUSIVE / MIXED** — exhaustively everything else (both effects clean;
     cells/arms disagree; a degenerate CI; a both-directions/within-cell pattern below the
     ≥24 floor). Reported with point estimates and no substantive label.
- **Minimum-cluster guard (the v3 fix-list, explicit):** k = 3 gated clusters per cell, and
  the per-cell ≥24/≥36 floors, are the **honest pre-registered decision rule** that stops a
  thin or degenerate cell from mechanically firing any clause — the same guard that v3
  introduced and that this design carries into the richer 2×2.
- **Sensitivity cuts (descriptive only, never verdict-bearing):** leave-one-pair-out;
  strict-format-only; NAs-as-out-of-pair; pair-level bootstrap; and the
  presentation-direction split (fwd-only / rev-only) as a robustness readout on the demoted
  reversal check. None flips a primary verdict.
- **Power caveat (pre-registered, honest):** still pilot-scale. Only a consistent
  Δ_chron or Δ_pos ≳ 0.7 (i.e. ≳ 0.2 above 0.5) is reliably CI-clean at this cluster count;
  a CI-including-0.5 remains *inconclusive-leaning-null*, not a precise zero. A symmetric
  U-shaped serial-position profile would dilute Δ_pos toward 0.5 (disclosed; the v3 note
  carried forward); the explicit stamps are intended to make Δ_chron *less* susceptible to
  serial-position dilution than v3's position-only chronology cue, but this is a design
  expectation, not a guarantee, and is flagged as such.

## Anchor discipline

**`anchor: internal-contrast-only`** — consistent with how v1/v2/v3 were scoped, and the
right call here. Justification:

- The novel **trajectory / chronology-vs-position** measure (Δ_chron, Δ_pos) is the
  **project's own contribution** and a **within-model contrast**: it compares one model's
  picks across byte-identical-content records that differ only in stamp and line order. It
  makes **no human-comparison claim**.
- **No in-repo human resource anchors order-sensitivity.**
  [`source/brennan-clark-1996-conceptual-pacts`](../../wiki/base/sources/brennan-clark-1996-conceptual-pacts.md)
  grounds **historicity and partner-specificity** ("a fresh human partner really does reset
  the pact, the direct analogue of the pilot's fresh-matcher design"), **not** order: the
  paper "never scrambles or reorders an interaction history," and reports "Frequency of use
  better explains our data than does simple recency" (p. 1492) — an order-*insensitive*
  statistic. So Brennan–Clark cannot anchor the v4 measure. Hawkins
  ([`resource/hawkins-tangrams`](../../wiki/base/resources/hawkins-tangrams.md)) anchors the
  convergence/compression baseline **only**, and its own page states the
  live-vs-shuffled / trajectory measure is "novel to the LLM probe and unanchored by any
  human resource."
  [`source/ashery-2025-llm-conventions`](../../wiki/base/sources/ashery-2025-llm-conventions.md)
  and [`source/imai-2025-vlm-common-ground`](../../wiki/base/sources/imai-2025-vlm-common-ground.md)
  are model-side foils with **no order-scramble control and no order-sensitivity baseline** —
  they sharpen the gap v4 fills, they do not anchor it.
- Therefore v4 is **internal-contrast-only**, terminally (per the ratified relational-line
  posture:
  [`decisions/resolved/relational-pilot-operationalization`](../../wiki/decisions/resolved/relational-pilot-operationalization.md),
  [`decisions/resolved/relational-fetchable-anchor`](../../wiki/decisions/resolved/relational-fetchable-anchor.md);
  terminal-state mechanics from
  [`decisions/resolved/conflicting-cue-human-anchor`](../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)).
  The conjecture's human-contrast clause stays a **characterized prediction**, anchored on
  the partner/historicity leg only, with the order-sensitivity leg an explicitly open
  question on both sides of the contrast — unchanged from v3.

## Gate check — does v4 stay inside the ratified instrument class?

**Provisional verdict: yes; this design does NOT open a new operationalization decision
page** — but the one borderline call is **flagged for the orchestrator** (see §Return /
"Open issue for the orchestrator" below), since surfacing a decision is the orchestrator's
call, not a subagent's. Justification, choice by choice:

- **Instrument class unchanged:** text-grid referents, near-twin pairs, fresh-matcher
  probe-shaped elicitation, constructed contradictory records with byte-identical multisets,
  nonce coined terms, internal within-model contrast — all the v2/v3 instrument the ratified
  [`decisions/resolved/relational-pilot-operationalization`](../../wiki/decisions/resolved/relational-pilot-operationalization.md)
  recommended as the perturbation arm. The ratification is v1-scoped, so this is a justified
  reuse, not a claimed entitlement.
- **The panel change (drop gpt, raise claude/gemini power) is instrument hygiene**, not a
  construct change — it changes *who* and *how many*, not *what is measured*.
- **The one borderline call, flagged not smuggled — explicit per-line chronology stamps +
  a non-adjacent perturbation point.** v3 conveyed chronology *purely by position*; v4
  conveys it by an explicit stamp and deliberately places the decisive line non-terminally.
  Judged here as **inside-class**: it is the *same* construct (does interpretation track
  *where in the chronology* conflicting evidence lands) measured with a *sharper* indicator
  that finally decouples the two confounded readings the v3 verifier flagged as unresolved.
  But because it changes the **operational indicator of "chronology"** from position to an
  explicit stamp — and the stamp introduces its own readability assumption (handled by the
  new stamp-respect control) — a reasonable critic could call this a new *operationalization*
  of "chronological position" rather than mere hygiene. **I do not invent a decision page**
  (per the task constraint and house rule 5's "surface, don't ratify in-session"); I
  **flag it for the orchestrator** to decide whether a `decisions/open/` page is warranted
  before v4 may run. `contingent-on` is left **empty** on the provisional judgement that
  this is inside-class hygiene; if the orchestrator opens a decision page, this design's
  `contingent-on` must be amended to name it and downstream artifacts marked contingent.

## Pre-flight cost estimate (ESTIMATE ONLY — for a run that has NOT happened)

Reusing the v3 measured billed rate (quoted from the v3 result/run, the only real numbers):
v3's finding-bearing probe billed **$0.386 for 384 calls** (≈$0.0010/call, probe-shaped);
its full session (harvest + certification + preflight + probe) billed **$0.611**. v4's
finding-bearing call count differs from v3 because: gpt is dropped (−~96 finding-bearing
calls), claude+gemini are run at raised power (more clusters/cells → more calls), and the
2×2 cell structure replaces v3's 6-order × 2-direction layout. The **net** call count is of
the same order as v3 (dropping one model roughly offsets raising the other two's power); a
**defensible estimate, explicitly not a result, is ≈$0.50–0.90 finding-bearing**, with the
harvest+certification+preflight overhead (v3: ≈$0.22) on top, for **≈$0.7–1.1 total**.

- This stays under the **$2.50 single-run flag** and well under the **$5.00/day** cap, but a
  **pre-registered hard stop at $1.50 projected total** is retained from v3 (re-design, don't
  push through), with per-phase ledgering and a per-model checkpoint inside the probe phase.
- **This is an estimate for a NOT-RUN experiment.** No spend has occurred; the actual billed
  `usage.cost` would be recorded per phase in `config/budget.md` *if and when* a future
  session, after a fresh pre-run critic GO, actually runs it.

## What this design does NOT do (named-null discipline)

- **It does not run.** No model has been called; no stimuli exist; no `experiments/runs/`
  directory exists for v4. The decisive test **remains open** until a real run under a frozen
  PREREG produces real data.
- **It does not claim the v3 forward elevation was "physical position."** The v3 verifier
  refuted that reading; v4 is built precisely because the position-vs-chronology question is
  **open**. If v4 fires the TEXT-POSITION ARTIFACT clause, *that* would be the first
  defensible position-tracking finding — but it is a **methodological** result about prompt
  geometry, not a relational one, and would be written as such.
- **It does not make a human-comparison claim.** `internal-contrast-only`; no in-repo
  resource anchors order-sensitivity (see §Anchor discipline). A measured Δ_chron would be a
  within-model contrast, never a "humans are non-commutative, models are/aren't" claim.
- **It does not resolve cross-family generality, image referents, or live (non-constructed)
  reassignment.** Those remain the named scope extensions of the conjecture; v4 stays on the
  frozen v1 text-grid figures with constructed records and homogeneous per-model probes.
- **A null is a first-class result.** If v4 certifies the commutative null (both effects null
  at the ≥36 floor), that is a *strengthening* of the deflationary aggregation reading, not a
  failure of the run — written as the named null the relational line keeps writing, never
  retuned away. If v4 again lands INCONCLUSIVE/MIXED, that too is reported plainly, with the
  located gap, exactly as v3 did.

## Run plan (for a FUTURE session — not this one)

When (and only when) a future session runs this: a new run directory
`experiments/runs/<date>-relational-history-perturbation-v4/` with the v3 harness shape —
`harvest.py` (+ certification) → `build_trials.py` (frozen sha256 in `PREREG.md`) →
`probe.py` (liveness/format-gate, preflight, full) → `analyze.py` (the frozen verdict tree
as code) → result page. **`PREREG.md` is frozen only after an independent pre-run critic
pass and before any finding-bearing call.** This design is the authoritative spec for the
*structure*; the run PREREG fixes the integers (cell counts, filler-line counts, raised
cluster count) and may not loosen any guard, floor, or the verdict map without a logged
critic revision.

> # ⚠️ END OF DRAFT — NOT RUN. No spend has occurred. No v4 numbers exist. ⚠️
