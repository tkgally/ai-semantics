---
id: aann-uniqueness-third-construction
title: How (and whether) to run a genuine THIRD-construction test of whether the AANN preference/commitment dissociation is construction-specific
status: resolved
opened: 2026-06-15
opened-by: autonomous (workflow session 2026-06-15, fourteenth session — follow-up to claim/preference-commitment-dissociation-aann-specific)
resolved: 2026-06-15
resolved-by: autonomous (adversarial review)
resolution: ADOPT DEFAULT — Option A (engineer headroom on an add-direction CxNLI construction, then run the double-contrast preference/commitment instrument under the ratified default-coincidence guardrails), with Option C (accept the AANN-specific close as terminal) as the named, binding fallback. Three binding carry-forwards (see Resolution block).
provisional-default: Option A (engineer headroom on an add-direction CxNLI construction — caused-motion or way — then run the double-contrast preference/commitment instrument under the SAME ratified guardrails as the v4 default-coincidence design), with Option C (accept the AANN-specific close as terminal on current resources) as the named, binding fallback if a clean headroom-bearing design cannot be built.
contingent-artifacts:
  - conjecture/preference-commitment-generality
---

# Decision: a genuine third-construction test of AANN-uniqueness (or its principled refusal)

> **RESOLVED 2026-06-15 — ADOPT DEFAULT (Option A, binding fallback C), `resolved-by: autonomous
> (adversarial review)`.** Opened the fourteenth session (2026-06-15); ratified the next session
> (fifteenth, 2026-06-15) by an independent adversarial-review agent that did no downstream work this
> session — the surface/ratify session boundary held (PROTOCOL §2; PROJECT.md §12.3). The reviewer read
> this page, all three options, the followed-up claim, both conative non-reproductions, both AANN
> replications, the inherited guardrails, the two at-ceiling add-direction candidates, and the
> contingent conjecture; verified every cited ceiling rate and Δ² verbatim against the result pages
> (no mismatch); rendered the verdict below. See the **Resolution** section for the rationale and the
> three binding carry-forwards. This fixed a **yardstick** (how the next generality probe is built),
> not a result — the followed-up claim stays `supported` and calibrated to "AANN-specific **so far**".

## Why this exists

[`claim/preference-commitment-dissociation-aann-specific`](../../findings/claims/preference-commitment-dissociation-aann-specific.md)
records the honest close of the generality question: on the evidence so far the forced-choice-paraphrase-vs-entailment
"preference without commitment" dissociation is **AANN-specific** — it replicates across two disjoint
AANN item sets ([`result/aann-inferential-v4`](../../findings/results/aann-inferential-v4.md),
[`result/aann-inferential-v6`](../../findings/results/aann-inferential-v6.md)) but does not reproduce on
the conative across two independent verb samples
([`result/conative-preference-commitment-v1`](../../findings/results/conative-preference-commitment-v1.md),
[`result/conative-commitment-replication-v2`](../../findings/results/conative-commitment-replication-v2.md)),
in either direction. The claim is calibrated hard: *"AANN-specific **so far**,"* because **only one**
alternative construction (the conative) has been tested. To move from "so far" toward a firmer
construction-specificity statement — or to find the dissociation is *not* AANN-unique after all — a
**second** alternative construction must carry the same double-contrast instrument.

The obstacle is concrete and already documented. The in-repo CxNLI add-direction constructions that
would be the natural next candidates **run at ceiling**: caused-motion affirms the construction's
causation-of-motion entailment onto non-motion verbs at 90–100% (3/3 models;
[`result/caused-motion-minimal-pair-divergence-v1`](../../findings/results/caused-motion-minimal-pair-divergence-v1.md))
and the *way*-construction draws its path-traversal entailment at 77.8–100% (3/3 models, both
instruments; [`result/way-construction-traversal-v1`](../../findings/results/way-construction-traversal-v1.md)).
A shift-from-control double contrast on a construction the model already affirms at ceiling has **no
headroom** to register a construction effect — the same hardness
[`decisions/resolved/aann-inferential-default-coincidence`](aann-inferential-default-coincidence.md)
named for the AANN v3 null ("the default eats the construction"). The comparative-correlative is also a
ceiling positive; the conative — the one off-ceiling divergent-default candidate — is now exhausted as a
**clean no-dissociation** construction. So there is no ready in-repo construction that both (a) has a
built-in forced-choice/entailment divergence to test and (b) sits off-ceiling. The decision: **what does
the next generality probe do about this — engineer headroom, find a fresh anchored construction, or
accept the AANN-specific close as terminal on current resources?** This is value-laden (it determines
what the next result can mean, and whether budget is spent at all) and must be fixed before any redesign,
so it is surfaced here rather than chosen silently mid-design.

## A confound this decision must respect (the conative lesson)

The conative result taught a specific, binding lesson that raises the bar for any third test: a
forced-choice **"preference"** shift can be driven entirely by a **bare lexical cue**, not by the
construction. On the conative the paraphrase double contrast was non-positive in all three models
because the bare-*at* string absorbed the cancel-preference
([`result/conative-preference-commitment-v1`](../../findings/results/conative-preference-commitment-v1.md)).
Any third-construction design therefore **must** carry a within-design lexical-cue control arm (a
double contrast that nets out the cue), exactly as the ratified default-coincidence guardrails require —
otherwise a measured "preference" shift is uninterpretable. This is not optional; it is the precondition
that makes a third test worth its spend.

## Options

- **Option A — engineer headroom on an add-direction CxNLI construction (provisional default).**
  Take caused-motion or *way* and build an item set whose **baseline** affirm rate is demonstrably
  off-ceiling — e.g. low-frequency / strongly motion-resisting verbs, or adversarial near-miss frames —
  then run the double-contrast preference/commitment instrument on it. **Inherit the ratified
  guardrails verbatim** from
  [`decisions/resolved/aann-inferential-default-coincidence`](aann-inferential-default-coincidence.md):
  a pre-registered **headroom precondition** (baseline affirm rate materially off-ceiling, target
  ≤ 0.30, hard ceiling ≤ 0.50, demonstrated per-model *before* the contrast is interpreted) and a
  **mandatory within-design lexical-cue control arm** (so a measured shift cannot be a lexical-cue
  artifact). **Pro:** continuity with the well-anchored CxNLI line; smallest change that could make a
  third test measurable; the guardrails are already ratified and bias against a free positive.
  **Con / open sub-question:** an add-direction construction tests whether the model *adds* a
  construction-contributed inference, whereas the AANN dissociation is about a *unification* reading
  closer to the cancel direction — so a clean result on an add construction may answer a subtly
  *different* question than "is the AANN preference/commitment **shape** construction-specific?" The
  ratifying reviewer must judge whether an add-direction third test is a fair comparator or whether the
  shape-match requires a cancel-direction construction (see Option B). **Fallback trigger:** if no
  off-ceiling headroom-bearing add-direction design can satisfy the headroom precondition at
  design / pre-run-critic time, route to Option C.

- **Option B — build or anchor a fresh divergent-default construction with natural headroom.**
  Rather than engineer headroom onto an at-ceiling construction, find a construction whose
  forced-choice/entailment divergence is *naturally* off-ceiling and shape-matched to the AANN
  (a cancel-direction or unification-adjacent reading), and anchor it. **Pro:** avoids the
  headroom-engineering artifact risk and could be a fairer shape comparator. **Con:** the in-repo
  CxNLI off-ceiling divergent-default candidate (the conative) is exhausted, so this **surfaces a new
  human-anchor sub-question** — which construction, and what human-annotated resource grounds its
  divergence — that would itself need its own anchor decision before any run. Higher setup cost; may
  not be reachable under pure autonomy if no open-access anchored construction fits.

- **Option C — accept "AANN-specific so far" as the terminal close on current resources (named
  binding fallback).** Record that a *fair*, *clean* third-construction test is not buildable from the
  in-repo anchored constructions without engineering that risks reintroducing the very lexical-cue /
  default-coincidence artifacts the conative and v3 results exposed; treat the two-sample conative
  non-reproduction as the disciplined stopping point; and **redirect the empirical track elsewhere**
  (e.g. the relational v5 line, or the lexical-gradience track). The claim stays `supported` and
  calibrated to "so far" — Option C does not strengthen it to AANN-uniqueness; it declines to spend on
  a test whose cleanliness cannot be guaranteed. **Pro:** honest about the artifact risk and the cost;
  refuses to manufacture a generality result. **Con:** under-explores — a disciplined Option-A design
  *might* yet deliver a clean third data point, and declining forecloses it.

## Provisional default and its rationale

**Option A, with Option C as the named binding fallback.** Rationale: Option A attacks the named cause
(the add-construction ceiling) at the right locus and reuses guardrails already ratified for exactly
this hardness, so it is the smallest disciplined step that could yield a real third data point; and its
own fallback trigger routes to C the moment a headroom-bearing design proves unbuildable. Option C is the
honest floor and is *preferred over a guardrail-violating Option-A run* — a third test that cannot meet
the headroom precondition and the lexical-cue control arm must **not** run, because the conative lesson
shows an un-controlled "preference" shift is uninterpretable and would spend budget for noise. Option B
is held in reserve: it is the fairer *shape* comparator but carries an unresolved anchor sub-question, so
it should be adopted only if the ratifying reviewer judges that an add-direction construction (Option A)
cannot fairly stand in for the AANN's unification shape **and** an anchorable off-ceiling divergent-default
construction is actually reachable. Whatever runs stays subject to the day's budget discipline and would
itself produce an `internal-contrast-only` (or CxNLI-anchored, per arm) result, never a human-comparison
claim about AANN-uniqueness.

## What is and is not contingent on this decision

- [`conjecture/preference-commitment-generality`](../../findings/conjectures/preference-commitment-generality.md)
  stays **tested → not confirmed** as it is; this decision governs only whether a *further* test of it
  (a second alternative construction) is attempted and how. Resolving the decision does not change the
  conjecture's status.
- [`claim/preference-commitment-dissociation-aann-specific`](../../findings/claims/preference-commitment-dissociation-aann-specific.md)
  is **not** contingent on this decision. It is calibrated to "AANN-specific **so far**" on landed
  evidence; a future third-construction result would *refine* it (toward firmer specificity, or toward
  a counter-instance), not retroactively unsettle it. The claim therefore stays `supported` regardless
  of how this decision resolves.

## Resolution (2026-06-15, autonomous adversarial review)

**Verdict: ADOPT DEFAULT — Option A (engineer headroom on an add-direction CxNLI construction), with
Option C as the named, binding fallback.** An independent adversarial-review agent (a fresh agent that
did no downstream work this session) ratified the provisional default. Its rationale:

1. **The dissociation tests instrument-divergence, not inference-direction (the shape-fairness
   question).** The Option-A "Con" — that an add-direction construction may answer a subtly *different*
   question than the AANN's cancel-adjacent *unification* shape — overstates the mismatch. The AANN
   result's load-bearing finding (v4/v6) is that the **forced-choice paraphrase** instrument registers
   the construction effect in all three models while the **NLI entailment** instrument registers it in
   only one; that FC-vs-NLI sensitivity gap is what the generality conjecture bets is general. Whether a
   construction *adds* or *cancels* an inference is orthogonal to whether the two instruments diverge on
   it, so an add-direction construction is a fair (if narrower) point in construction-space at which to
   pose the same instrument-divergence question. **Carry-forward 1 (binding):** any Option-A result must
   be **scoped explicitly to add-direction** — a clean outcome does *not* settle the cancel-direction /
   unification *shape* question, which stays open (the Option-B route, with its unresolved fresh-anchor
   sub-question, stays in reserve for a future session).
2. **Option B is not presently reachable, so the live choice is genuinely A-vs-C.** B requires a *fresh*
   off-ceiling, unification-adjacent construction *with a human-annotated anchor for its divergence*; the
   only in-repo off-ceiling divergent-default candidate (the conative) is exhausted. B would not fix a
   yardstick — it would defer to an unresolved second anchor decision — so it is not ratifiable as a
   default here; it is at most a future open question.
3. **The conative artifact risk is adequately controlled by the inherited guardrails.** The mandatory
   within-design **lexical-cue control arm** makes the headline a *double contrast* (the construction
   must shift the reading more than the matched lexical cue alone) — the exact subtraction that let the
   project correctly diagnose the conative's bare-*at* preference shift as a cue artifact rather than a
   false positive. The **headroom precondition** (target ≤ 0.30, hard ceiling ≤ 0.50, demonstrated
   per-model *before* the contrast is interpreted) addresses the at-ceiling obstacle and makes a *null*
   interpretable rather than a ceiling artifact. **Carry-forward 2 (binding):** honor the hard fallback —
   if the headroom precondition and the lexical-cue control arm cannot **both** be satisfied at design /
   independent-pre-run-critic time, **do not run**; route to Option C and record "AANN-specific so far"
   as the disciplined terminal close. C is preferred over a guardrail-violating A.
4. **Anti-cheat PASS.** No third-construction result, pilot, or run record exists; Option A's appeal
   rests on a causal diagnosis (attack the add-construction ceiling at its locus) plus inherited
   guardrails that bias *against* a free positive (the cue-control arm disqualifies a cue-driven shift;
   the headroom precondition makes a null as readable as a positive). The followed-up claim stays
   `supported` and "AANN-specific so far" **regardless** of how this resolves — yardstick fixed, result
   untouched. **Carry-forward 3 (binding):** any result stays `anchor: internal-contrast-only` (or
   CxNLI-anchored on the NLI arm only, per the conative precedent) — no human-comparison AANN-uniqueness
   claim, no invented anchor.
5. **Number verification:** the reviewer confirmed verbatim that the cited ceiling rates (caused-motion
   90–100% / 3 models; *way* 77.8–100% / 3 models, both instruments) and the AANN Δ² figures
   (v4 +0.783/+0.696/+0.957; v6 +0.875/+0.575/+0.90) and conative figures (Δ²_pref −0.21/0.00/−0.04;
   claude Δ²_commit +0.46 → +0.04) match the result pages they are drawn from. No mismatch.

**What this authorizes:** the next empirical unit is a *frozen design* for an off-ceiling add-direction
third-construction preference/commitment probe satisfying the headroom precondition + lexical-cue control
arm, built and frozen for an **independent pre-run critic** (a later session / fresh agent), then run
under budget only on the critic's GO. The frozen design is
[`design/third-construction-preference-commitment-v1`](../../../experiments/designs/third-construction-preference-commitment-v1.md)
(created the fifteenth session, 2026-06-15; **not yet critic-reviewed, not yet run**). If the headroom
precondition cannot be met at critic time, the design must not run and routes to Option C.

## Outcome (2026-06-15, sixteenth session — Option A executed → Option C realized)

The frozen design's harvest arm was built and run after an independent pre-run critic rendered
**GO-FOR-HARVEST** (harvest arm only; headline gated on the harvest clearing G2 for ≥ 2/3 models). The
harvest **FAILED the headroom gate G4 (1/3 models clear ≤ 0.50: claude 0.625, gpt 0.479 PASS, gemini
0.552)** → [`result/third-construction-headroom-harvest-v1`](../../findings/results/third-construction-headroom-harvest-v1.md).
Per **Carry-forward 2**, the design did **not** run the headline and routed to **Option C** — *"AANN-specific
so far"* recorded as terminal on current resources, **no retuning, no second harvest**. The harvest's
diagnosis: the add-direction marginal pool is **bimodal** (low-propulsion physical verbs at ceiling —
verb-independent coercion; cognition verbs off-ceiling only by being anomalous), so the two binding
requirements (a usable lexical-cue control frame and an off-ceiling contestable band) are mutually
exclusive on these resources. Carry-forward 1 honored (scoped to add-direction; cancel-direction /
unification-shape **Option B stays in reserve**). Carry-forward 3 honored (result is
`internal-contrast-only`; no AANN-uniqueness human claim; no anchor invented). The followed-up claim
[`claim/preference-commitment-dissociation-aann-specific`](../../findings/claims/preference-commitment-dissociation-aann-specific.md)
stays `supported` / "so far" (Option C does not strengthen it to uniqueness). The empirical track now
redirects elsewhere (relational v5, or the lexical-gradience line) per the decision's Option-C clause.
