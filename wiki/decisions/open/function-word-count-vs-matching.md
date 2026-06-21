---
id: function-word-count-vs-matching
title: The function-word swap probe's ≥200-item count conflicts with faithful frequency+length matching — how to resolve (relax which constraint, or pay the authoring cost)?
status: open
opened: 2026-06-21
opened-by: autonomous (session 67, the build session for the ratified function-word-anchor-design)
contingent-artifacts:
  - conjecture/function-word-substitutability
links:
  - rel: depends-on
    target: decisions/resolved/function-word-anchor-design
  - rel: depends-on
    target: resource/subtlex-us-frequency
---

> **Status: OPEN (2026-06-21, session 67). Ratifiable, at the earliest, by a later session's
> independent adversarial-review pass.** This decision was forced by the build session: the
> ratified [`decisions/resolved/function-word-anchor-design`](../resolved/function-word-anchor-design.md)
> fixed a yardstick that — applied faithfully — yields **80 matched items, not the ≥200**
> the conjecture's confirm criterion (and binding condition (e)) require. The build is frozen,
> certified SOUND on every matching/shortcut-reader/integrity check, and **NO-GO on the run**
> only because of the count. See [`result/function-word-swap-build-v1`](../../findings/results/function-word-swap-build-v1.md)
> and `experiments/runs/2026-06-21-function-word-vs-content-swap/` (build.py, certify.py,
> certification.json, matching-report.json).

# Decision: how to resolve the ≥200-count vs tight-matching tension

## Why this exists (the measured obstacle)

The ratified yardstick requires each content-swap control to be matched to its function
word on **frequency at BOTH ends** (content-out within |ΔLg10WF| ≤ 0.10 of the function-out
word; content-in within 0.10 of the function-in word, mirroring the within-pair spread) **and
on length**. The build session discovered that the *length* match must be a **signed +1**
(every named function swap lengthens the word by exactly one character — `because`→`although`,
`some`→`every`, `will`→`would`), because a length-only reader otherwise reproduces the whole
function>content asymmetry: function swaps are uniformly +1, so if content swaps are
length-neutral (Δ0) the reader perfectly separates the conditions (this is exactly what
binding condition (i) forbids, and the build's first certification pass caught it — length-only
asymmetry 0.46 before the fix, 0.00 after).

Under all of these at once — frequency ±0.10 at both ends, signed +1 length, same coarse POS,
a **coherent** swap, and **one** content control per carrier (more than one re-uses the
identical function-swap NLI query and would double-count the function arm) — the supply of
clean items collapses:

- The high-yield **person-noun route dies entirely**: no open-class person noun sits at
  Lg10WF ≈ 3.33 (to match `although`) with +1 length against a ≈4.74 partner. The `because`
  person frames (which alone could have supplied ~90 items) produce **zero** valid pairs.
- The **`the`→`a` determiner swap admits NO frequency-matched content control at all** — no
  open-class word reaches Lg10WF ≈ 6.0 (the resource page predicted exactly this). It can run
  only as a **function-only characterizing arm** (no content contrast).
- Only ~13 distinct content swap-out words survive matching across the three usable function
  pairs, so items = (distinct out-word × coherent carrier) tops out near **80** at quality,
  resting on a handful of distinct content pairs (man→girl, give/help/talk/call→build/serve,
  say→hear/feel/show, take→leave, way→room, time→place, sure→tight/empty, thing→advice,
  see→take/tell).

The ratified decision **anticipated this** ("over-matching can leave too few items to reach
the ≥200-pair target") and bound the session to **defer rather than relax** ("a NO-GO defers
the run rather than relaxing the matching"). This page is that deferral, made decidable.

## The question

Reaching ≥200 *faithfully-matched* items is not strictly impossible, but under the current
tolerances it is expensive and would rest on very low content-pair lexical diversity. Which
adjustment best preserves the probe's validity while making it runnable?

## Options

- **Option A — Pay the authoring cost; keep every tolerance.** Author enough additional
  coherent carriers (the bottleneck is carriers, not pairs) to reach ≥200 (out-word × carrier)
  combinations, accepting that the content swaps rest on ~13 out-words repeated across many
  carriers. *Cost:* low content-pair diversity (a reportable limitation; the conjecture's
  "not driven by a few **classes**" — prediction 3 — is still checkable since 4 semantic
  classes are present, but per-**pair** diversity is poor); a large authoring lift (likely >1
  session). *Keeps the yardstick exactly.* **Provisional-default-adjacent** but flagged as the
  weakest on diversity.

- **Option B — Relax the length match to a reported covariate (|ΔLg10WF|-only matching).**
  Drop the signed-+1 length requirement; allow Δlen ∈ {0, +1} and instead **regress length-delta
  out of the flip-rate contrast** (or report the length-stratified contrast), certifying that
  the *length-controlled residual* asymmetry is not reproducible by a length reader. *Cost:* the
  build-time GO/NO-GO shortcut-reader guard (condition (i)) becomes an analysis-time control —
  a real change to the freeze discipline. *Benefit:* restores the person-noun and many object
  routes (Δ0 pairs), plausibly clearing ≥200 with good diversity. **This page's provisional
  default** (see below), because a 1-character length change is independently implausible as a
  driver of NLI flips and a regressed covariate is a standard, auditable control.

- **Option C — Multiple content controls per carrier, with explicit function-arm
  de-duplication.** Allow several frequency/length-matched content controls per carrier while
  measuring each distinct function-swap NLI query **once**; the primary contrast becomes
  mean(flip_fn over distinct function-swaps) − mean(flip_ct over content-swaps), two rates over
  possibly different-sized sets. *Cost:* "≥200 matched **pairs**" becomes "≥200 content
  measurements against ~80 function measurements" — a departure from the paired framing that
  needs its own power statement. *Benefit:* reaches ≥200 content measurements cheaply.

- **Option D — Lower the count threshold with an explicit power analysis.** Keep faithful
  matching; run the ~80-item set, but only after a pre-registered power analysis shows ~80
  matched items give adequate power for the expected effect size, and **re-label the confirm
  criterion** (the conjecture currently says ≥200). *Cost:* amends the conjecture's own confirm
  bar; a small-N result is more fragile. *Benefit:* runs the cleanest (most faithfully matched)
  set with no constraint relaxation.

- **Option E — Lower the frequency tolerance / widen the swap inventory.** Tighten or widen
  |ΔLg10WF| (e.g. 0.15) to admit more pairs, or add function-word pairs beyond the named four
  (other determiners/modals/subordinators/quantifiers) to multiply out-words. *Cost:* widening
  the tolerance weakens the frequency control (the decision allows tightening, not loosening,
  without a new decision — hence this page); adding function pairs is a scope change.

## Provisional default (for the reviewer to confirm or overturn)

**Option B** (relax length to a reported, regressed-out covariate), **combined with a capped
dose of Option A** (author to ≥200 with the restored routes). Rationale: it is the change that
*least* weakens the scientific control — a 1-character orthographic change is not a credible
alternative explanation for an inference flip, and moving it from a hard freeze-gate to an
auditable analysis-time covariate is standard practice — while restoring enough supply (the
person-noun and object routes) to reach ≥200 with genuine content-pair diversity and all four
semantic classes. The signed-+1 *frequency-magnitude* match (mirrored spread) and the
freeze-and-hash discipline are **kept**; only the length constraint moves from gate to covariate.

**Anti-cheat:** whichever option is ratified, the falsify arm (content-swap flip rate ≥
function-swap flip rate = a clean positive for the distributional camp) stays live and the set
is frozen+hashed before any model output; a relaxation must not be chosen *because* it makes a
positive likelier. Ratifying this fixes the yardstick, never the result. The `internal-contrast-only`
posture is unchanged.

## What the reviewer should weigh

1. Is the signed-+1 length match genuinely *necessary* (condition (i)), or is a regressed
   length covariate (Option B) an equally faithful control that a length-only reader cannot
   exploit? Re-derive the length-only reader against a Δ0-permitting set to check.
2. Does Option A's low content-pair diversity (≈13 out-words across 200 carriers) threaten the
   conjecture's "not driven by a few categories" claim, given 4 semantic classes are present?
3. Is the paired framing ("≥200 matched **pairs**") essential, or is Option C's two-rate
   contrast (≥200 content vs ~80 function measurements) a legitimate, better-powered design?
4. Should the conjecture's own ≥200 confirm bar be amended (Option D) given the matching makes
   it costly — or is that moving the goalposts?
