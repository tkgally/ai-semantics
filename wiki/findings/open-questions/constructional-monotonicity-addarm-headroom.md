---
type: open-question
id: constructional-monotonicity-addarm-headroom
title: "Does the resultative add arm have genuine headroom — and what design would a clean, non-degenerate add control for the monotonicity-generalization battery require?"
meaning-senses:
  - constructional
  - inferential
status: answered
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: refines
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: open-question/constructional-monotonicity-generalization-design
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
  - rel: depends-on
    target: result/coercion-implicit-cue-v2b
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Open question: add-arm headroom for the monotonicity-generalization battery (design-level feasibility, not a probe)

> **ANSWERED — 2026-06-28 (session 133): headroom DEMONSTRATED; the blocker is discharged.** The frozen calibration this page specified was run — [`result/addarm-headroom-calibration-v1`](../results/addarm-headroom-calibration-v1.md) ([`run record`](../../../experiments/runs/2026-06-28-addarm-headroom-calibration/README.md)). **Both** candidate add constructions clear the frozen headroom gate: **resultative** 10/12 verbs headroom-clean (construction affirm 1.000, control 0.250); **intrans-motion** 7/12 (construction 0.972, control 0.333). The s132 degeneracy worry is **not** borne out — a genuinely non-result-entailing control exists and the resultative add arm has real licensing-no-cue headroom against it. The default-coincidence trap is **real but verb-specific and avoidable**: only the telic/displacement verbs degenerate (resultative `freeze→solid`, `sharpen→sharp`; intrans `drift`, `slide`, `swing`, `bounce`). This **discharges prerequisite (1)** of the s132 review; it does **not** discharge prerequisites 2–4 and **ratifies nothing** (the operationalization decision stays `open`). The design-level analysis below stands as the spec the calibration executed.

> **Why this page exists.** The session-132 independent adversarial review of the
> operationalization decision
> [`decisions/open/constructional-monotonicity-generalization-operationalization`](../../decisions/open/constructional-monotonicity-generalization-operationalization.md)
> returned **KEEP-OPEN**, and its **load-bearing blocker** is **undemonstrated add-arm
> headroom** for the resultative add arm (the decision's provisional pair, Option A1 used
> as the new-pair leg of Option A3). This page works that one blocker at the **design
> level only**. It does **not** demonstrate headroom — demonstrating headroom requires a
> frozen calibration probe a *later* session runs — and it **ratifies nothing, freezes
> nothing, and re-opens nothing already settled**. Everything forward-looking here is
> provisional. The companion scoping page is
> [`open-question/constructional-monotonicity-generalization-design`](constructional-monotonicity-generalization-design.md);
> the conjecture under test is
> [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md).

## Frame: the s132 KEEP-OPEN blocker, stated plainly

The first cross-session boundary having passed, the session-132 review read the decision,
its scoping page, the conjecture, the conative-cancel-v2 paradigm and its governing
decision, the conflicting-cue posture, the descriptive answer-key result, and the Scivetti
resource, and **kept the operationalization open**. It affirmed the surfacing discipline
(freeze-and-hash, independent pre-run critic, live falsify arms, "fixes the yardstick never
the result") as ratifiable in posture, but named four must-discharge-before-freeze gaps.
The **first is the blocker**: Option A3 commits the add arm to the **resultative** (via
Option A1), and the review judged that arm's headroom *undemonstrated and plausibly
degenerate*. This page sharpens that gap into a concrete design requirement and a candidate
survey, so a later session has a precise thing to calibrate. It is a **sharpening of the
gate, not a step through it**.

## Why the resultative add arm risks degeneracy

Three things, read together, make the resultative add arm a live degeneracy risk.

**1. The conjecture's own mechanism says adding is distributionally cheap.** The
conjecture's *Mechanism* section (LABELED speculation) holds that "Adding a
construction-licensed inference is **distributionally cheap**: the construction's own
co-occurrence statistics support the added entailment … so a next-token predictor can
affirm the added inference from the construction's distribution alone"
([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md),
*Mechanism*). That cheapness is exactly what pins an add arm at ceiling — which is *why*
the add direction has been at or near ceiling across the project's probes — and a ceiling
add arm with nothing to measure is the failure this page guards.

**2. The AANN default-coincidence trap.** The descriptive answer-key result's
*Interpretation* / *What this does and does not license* establishes the general shape of
this trap, and the decision page names it directly against the resultative arm: the worry is
that "a non-resultative control may supply the state-change entailment *for free*" so the
add arm cannot move. The mechanism is the one the answer-key result flags for a *match*:
"Answer-key agreement only; contamination is possible …, so a *match* cannot distinguish
learned construction-meaning from item memorization. The *shortfall* … is the robust
direction — failure survives possible contamination, a match does not"
([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md),
*What this does and does not license*). An add arm whose control already licenses the
entailment is the structural analogue: there is no off-ceiling signal in which the
construction's contribution could show.

**3. Resultative is already at the top of its range, with no off-ceiling licensing
signal.** On the human Scivetti items the resultative's base answer-key accuracy is
**0.894 / 0.773 / 0.894** (claude / gpt / gemini)
([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md),
*Per-construction accuracy*) — i.e. **0.77–0.89**, with no off-ceiling licensing arm
anywhere in that descriptive probe. So the only in-repo evidence on the resultative shows
it near the top of its band and supplies no headroom signal at all.

**The structural point.** Resultatives canonically attach to verbs whose action *already
co-occurs with the result state* (this is the coercion picture: the construction "imposes
its own meaning onto a verb that does not lexically carry it" — but for a *typical*
resultative verb the result state is highly co-occurring in the construction's distribution;
see [`concept/coercion`](../../base/concepts/coercion.md)).
A non-resultative control framing may therefore supply the state-change entailment **for
free**, pinning the add arm's licensing-no-cue at ceiling with nothing to measure. And a
**ceiling-pinned add arm would make "add easy / cancel hard" a near-tautology of the *arm
construction*** — the add arm tests not whether the construction contributes the entailment
but whether the control already carries it — **rather than a finding** about the conjecture.
This is an *inadvertent* path to spurious confirmation: the anti-cheat concern here runs
toward a degenerate add arm, **not** toward manufactured suppression on the cancel side.

## What a clean add control requires

State the requirement sharply. A non-degenerate add construction needs a **control framing
whose default does NOT already license the added entailment**, so that the construction's
contribution is the only thing that can move the no-cue licensing arm **off the control's
floor**. Equivalently: the discriminating cell is the construction's licensing-no-cue
reading *minus* the control's no-cue reading; if the control is already at ceiling on the
entailment, that difference is structurally near zero regardless of what the model is doing,
and the add arm carries no information. This mirrors how the matched paradigm reads the
*cancel* side — the conative's discriminating cell is "suppression-no-cue = `100 −
conative_affirm` (construction-following with no cue) — the matched analogue of the
add-direction's canonical/licensing-no-cue (~70–100%, mostly ceiling)"
([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md),
*Numbers*) — except that for the add arm the requirement is the **converse**: a control
whose entailment is **at floor**, not at ceiling, so the construction has room to lift it.

How a later session would test this **on frozen calibration items, BEFORE the main run**
(described, not run here):

1. Build, for the candidate add construction, a small **frozen calibration subset** of
   minimal pairs: each item paired with a **non-construction control framing** of the same
   verb + arguments whose default does *not* state or strongly imply the added entailment.
2. **Freeze and sha256-hash** that calibration subset before any probe call, exactly as the
   decision's anti-cheat clause requires of the main item set.
3. Read the control arm's no-cue entailment rate. The pair **passes the headroom gate** only
   if the control is genuinely **off ceiling** (the added entailment is *not* supplied for
   free) AND the construction's licensing-no-cue is at ceiling — so the construction
   contributes a real lift. This is the numeric content the decision's Option B2 ("an
   explicit pre-run ceiling gate that BLOCKS the run if either arm's base is off ceiling")
   needs to be operable: B2 already blocks an off-ceiling *cancel default*; the add arm needs
   the **dual** check — a control that is off ceiling on the added entailment, or the add arm
   has no headroom.
4. If the control is at ceiling on the entailment, **reject the pair and pick a cleaner add
   construction** before the main run — never relax the bar after seeing it.

This page does **not** run steps 1–4; it specifies them. Demonstrating headroom is a probe
for a later session.

## Candidate add constructions, with honest headroom assessment

Drawn **only** from constructions named in the conjecture, the scoping page, or the Scivetti
resource — Scivetti's eight are, verbatim, "Causative-With, Caused-Motion,
Comparative-Correlative, Conative, Intransitive Motion, Let-Alone, Resultative, Way-Manner"
([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md))
— plus "other Levin alternations" as a class (named in the conjecture's confirm-leg 1) and
**AANN as the cautionary precedent** (the default-coincidence trap; *not* a Scivetti
construction — the resource is explicit: "**AANN.** … is **not** among the 8 constructions.
Do not cite this dataset for AANN"). No dataset is invented; anchor status is flagged
honestly throughout. **No pair is picked here — picking is the decision's job, ratified by a
later session.**

- **Resultative (the decision's provisional add arm).** Headroom: **at risk / undemonstrated**
  — the whole reason this page exists. Per §"Why the resultative add arm risks degeneracy":
  base accuracy 0.77–0.89 with no off-ceiling signal, and a control verb plausibly supplying
  the state-change entailment for free. Anchor: a *descriptive* human-annotated answer key on
  its Scivetti items (n = 66), but **not** a ratified anchor construction (the four ratified
  are caused-motion, conative, way-manner, comparative-correlative). A clean control would
  need a verb whose lexical default leaves the result-state *open*, not entailed — feasible in
  principle, but **must be demonstrated on frozen calibration items**, not assumed.
- **Caused-Motion and Way-Manner — already used; replication, not generalization.** These are
  the project's existing **add** legs
  ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md),
  *The evidence this abstracts over*). Confirm-leg 1 requires a pair "**beyond** caused-motion
  / way / conative," so re-using either tests replication, not the conjecture's generalization
  claim. They are candidate add arms only for the *anchored-replication* leg (the decision's
  A3 first leg), not for the generalization verdict.
- **Causative-With.** A Scivetti construction (base accuracy 0.926–0.982 — at the top of the
  range). Plausibly carries an added causation/instrument entailment a bare control might not
  supply, so it is a *candidate* with possible headroom — but its very high base accuracy is a
  yellow flag for the same ceiling risk, and it has only a descriptive (non-ratified) answer
  key. Headroom: **plausible but unverified**; would need the same calibration gate.
- **Intransitive-Motion.** A Scivetti construction (base accuracy 0.797–0.899). Whether it
  *adds* an entailment a control lacks, or simply restates motion the verb already denotes,
  is exactly the coincidence question — for a genuinely non-motion verb it could have headroom,
  for a motion verb it would not. Headroom: **direction-dependent and unverified**; descriptive
  anchor only.
- **Let-Alone and Comparative-Correlative — phrasal / non-add-coercion in character.**
  Let-alone is a scalar coordinator (and the project's known channel-sensitive item — see
  [`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md) and its
  working-surface follow-up); comparative-correlative is a covariation construction, already a
  ratified anchor but not framed as an add-vs-control coercion. Neither maps cleanly onto the
  "add an entailment a non-licensing verb lacks" shape the add arm needs. Headroom: **poor
  fit** for this design.
- **Conative.** This is the project's **cancel** leg, not an add candidate
  ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)); listed
  only to mark it as out of scope for the add arm.
- **Other Levin alternations (a class, not a dataset).** The conjecture names them; the scoping
  page warns they have "**no in-repo human anchor at all**" and "are not all cleanly 'add' vs
  'cancel,'" so the direction assignment "becomes a judgement call that must be frozen and
  justified." Some alternations plausibly *add* an entailment with a clean non-adding control
  (real headroom), but the class is heterogeneous; any specific pair would run
  `internal-contrast-only` and owes an explicit, pre-frozen direction assignment (the s132
  review's gap 3). Headroom: **pair-dependent; unanchored**.
- **AANN — the cautionary precedent, not a candidate.** AANN is the construction whose
  default-coincidence trap the decision names; it is **not** a Scivetti construction and not an
  add candidate here. It is listed only as the worked example of exactly the failure the add
  arm must avoid: an arm where the "default" reading already coincides with the construction's
  contribution, leaving nothing to measure.

The honest summary: **no candidate has *demonstrated* add-arm headroom in-repo.** The
resultative is at-risk; causative-with and intransitive-motion are plausible-but-unverified;
the rest are poor-fit, out-of-scope, or unanchored. Establishing headroom for *any* of them
is a frozen calibration probe a later session must run before the pair can be frozen.

## Concrete frozen-threshold SHAPES (provisional, not decided)

The s132 review's gap 2 asks for **concrete frozen thresholds** for the B2 ceiling gate and
the degradation slope/cliff rule, as fixed numbers set before data, **not** inherited by
pointer from conative-cancel-v2. The reason the inheritance-by-pointer is wrong is in the
governing decision's own ratified wording: the slope criterion is "degradation read as
'monotone with slope < a fixed pp-drop-per-difficulty-step = graceful, else brittle cliff',
**the slope threshold frozen WITH the item set**" — and the cliff-threshold is to be "a fixed
pp-drop-per-difficulty-step, **frozen with the item set**" (the cc-v2 governing decision,
*resolution* and *Provisional default*; see
[`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md)). That phrase — *frozen with the
item set* — makes the threshold **item-set-specific**, not a portable constant: a new
construction pair owes its **own** frozen numbers.

The following are **provisional shapes a later session would fix** against the new frozen
item set — placeholders to make the gap concrete, **not decisions and not ratifiable here**:

- **B2 ceiling cutoff (shape).** A fixed rate, e.g. *base licensing-no-cue (add) and base
  lexical-default (cancel) each ≥ 90% in ≥ 2/3 models on the frozen calibration subset, else
  the pair is rejected.* The **add-arm dual** this page argues for would add: *and the
  non-construction control's no-cue entailment ≤ a fixed floor (e.g. ≤ 30%) in ≥ 2/3 models,
  else the add arm has no headroom and the pair is rejected.* The numbers `90%` and `30%` are
  **illustrative placeholders**; the actual cutoffs must be fixed against the new item set
  before any data.
- **Degradation slope / cliff threshold (shape).** A fixed pp-drop-per-difficulty-step
  separating "graceful" from "brittle cliff," e.g. *< 25 pp per step = graceful, ≥ 25 pp =
  cliff* — again an **illustrative placeholder** whose real value the new item set fixes, per
  the cc-v2 rule that the slope threshold is frozen with the items, not transported.

These shapes exist to show the gap is fillable, **not** to fill it. Re-using the cc-v2
*reading-rule shape* (report-the-rate; "≥70% follow-construction in ≥2/3 models = robust";
monotone-slope-vs-cliff) is fine and continuous; **transporting its frozen numbers is not**.

## Scope and limits

- **Design-only; demonstrates nothing.** This page does not run a probe, does not demonstrate
  add-arm headroom, and does not show any model behavior. Headroom is established by a frozen
  calibration probe a later session runs, not by this analysis.
- **Ratifies nothing; freezes nothing.** It does not ratify the operationalization decision,
  does not pick a pair, and does not fix any threshold. The decision
  [`decisions/open/constructional-monotonicity-generalization-operationalization`](../../decisions/open/constructional-monotonicity-generalization-operationalization.md) stays
  **open**; this page only sharpens its load-bearing blocker.
- **Direction-of-effect, not magnitude; small-N intrinsic.** Any battery this feasibility
  analysis serves inherits the project's small-N, single-run, panel-as-subjects regime
  ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md):
  "12 verbs × 3 conditions × 3 models; rates carry wide per-cell uncertainty. Read as a
  direction-of-effect signal, not a precise magnitude").
- **Both directions are already bounded.** The add direction's depth is bounded —
  [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) shows its
  withholding is "explicit-outcome parsing, not world-model integration" — so the
  generalization question is only about the **relative** reliability of add vs cancel, and a
  headroom-clean add arm does not become a standalone competence claim.
- **The add/cancel posture is settled elsewhere and not re-opened.** The new-pair leg runs
  `internal-contrast-only` per the ratified conflicting-cue posture; that posture was affirmed
  by the s132 review and is **not** re-examined here.

## Status: answered (the calibration ran; headroom demonstrated)

This page restated the s132 KEEP-OPEN blocker, laid out why the resultative add arm *risked*
degeneracy, specified what a clean add control requires and how a later session would test it
on frozen calibration items, surveyed candidate add constructions, and proposed provisional
frozen-threshold *shapes*. Session 133 **executed that spec**: [`result/addarm-headroom-calibration-v1`](../results/addarm-headroom-calibration-v1.md)
froze the shapes into concrete numbers (construction affirm ≥ 0.80, control affirm ≤ 0.40,
≥ 4/12 clean), passed an independent pre-run critic, ran the probe ($0.068 billed), and a
post-run verifier reproduced every figure. **Verdict: both candidate constructions demonstrate
headroom; the resultative degeneracy worry is refuted (verb-selected); the trap is real but
verb-specific.** Prerequisite (1) is **discharged**. The operationalization decision
[`decisions/open/constructional-monotonicity-generalization-operationalization`](../../decisions/open/constructional-monotonicity-generalization-operationalization.md)
**remains open** — prerequisites 2–4 (concrete main-battery thresholds, pre-frozen direction
assignment, reconsidered scope) are still owed, and ratification is a later session's
independent adversarial-review pass. This page is `answered`; it ratifies nothing.
