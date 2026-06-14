---
id: fresh-construction-inferential-generalization
title: How to test whether the AANN "preference-without-commitment" double-contrast dissociation is AANN-specific or a general property — choosing the fresh construction to carry the instrument
status: open
opened: 2026-06-14
opened-by: autonomous (workflow session 2026-06-14)
provisional-default: Option A (apply the double-contrast preference/commitment instrument to the CONATIVE — a cancel-direction, CxNLI-anchored construction whose licensed inference runs opposite to the verb's distributional default, which by construction supplies headroom)
contingent-artifacts:
  - conjecture/preference-commitment-generality
eligible-for-ratification: NO — opened this session; not eligible until a later session (PROTOCOL §2; never ratify in the opening session)
---

# Decision: which fresh construction carries the preference/commitment generalization test

> **OPENED 2026-06-14 (autonomous workflow session). NOT eligible for ratification this
> session.** Per PROTOCOL §2, a decision is never ratifiable in the session that opened it;
> surfacing and ratifying must be separated by at least one session boundary. A *later* session may
> ratify via an independent adversarial-review pass (PROJECT.md §12.3); Tom's standing override
> outranks any autonomous ratification. The provisional default below governs the contingent design
> and conjecture, but any design under this decision must carry `contingent-on:
> fresh-construction-inferential-generalization` and stay in provisional language until ratified.

## The question

The AANN inferential probe produced the project's sharpest cross-instrument dissociation, now
**replicated cell-for-cell** on a fresh, larger, held-out item set
([`result/aann-inferential-v6`](../../findings/results/aann-inferential-v6.md), replicating
[`result/aann-inferential-v4`](../../findings/results/aann-inferential-v4.md)): a forced-choice
**paraphrase preference** shifts toward the construction's licensed reading in all three panel
models, but the NLI **entailment commitment** (and the grammaticalized agreement reflex) carries
over in **only one** model (gpt-5.4-mini), with claude and gemini **paraphrase-only**. The essay
[`essay/preference-without-commitment`](../../findings/essays/preference-without-commitment.md)
argues this is a *type* difference — the two instruments measure distributional compatibility vs.
inferential commitment — and that for two of three models "use" decomposes into a preference
component without a commitment component.

**The open question this decision governs:** is that preference/commitment dissociation an
**AANN-specific artifact**, or a **general property** of constructions whose licensed inference
diverges from their distributional default? The dissociation has so far been instanced on a single
construction (AANN), under one panel, against an expert-stipulated key. To test generality we must
run the **same double-contrast preference-vs-commitment instrument on a fresh construction** — but
*which* construction is a value-laden operationalization choice (it determines what a positive or
null can mean), so it is surfaced here rather than chosen silently mid-design.

The instrument to be generalized is the **double contrast** ratified for AANN
([`decisions/resolved/aann-inferential-default-coincidence`](../resolved/aann-inferential-default-coincidence.md)):
a forced-choice paraphrase arm and an NLI entailment arm on the *same frozen items*, with the
headline a within-design double contrast (target-vs-lexical-cue-control) so a measured shift cannot
be a lexical-cue artifact, gated by a **headroom precondition** (the control baseline must be
demonstrably off-ceiling) and a **mandatory lexical-cue control arm**. Any design under this
decision inherits that discipline (see *Binding conditions*).

## Options

### Option A — apply the double-contrast instrument to the CONATIVE (provisional default)

The conative ("Maria kicked **at** the ball" → did not necessarily make contact) is a
**cancel-direction** construction: the licensed inference (no completed contact) runs *opposite* to
the verb's distributional default (*kick* lexically implies contact). This is the same
"inference-vs-default divergence" the AANN's distributive-default control had to *engineer*; the
conative supplies it **for free**, because the default points the other way — echoing the v4
decision's Option-B cancel-direction fallback logic.

- **Inference/default divergence:** maximal and built-in. The verb-held-constant minimal pair
  ([`result/conative-minimal-pair-divergence-v1`](../../findings/results/conative-minimal-pair-divergence-v1.md))
  shows the transitive default at or near ceiling (affirm-contact 92–100%) while the conative
  affirm-contact is off-ceiling and model/instrument-dependent — so there is genuine headroom for a
  construction effect *and* for the two instruments to diverge.
- **In-repo human anchor:** YES. `Conative` is one of the 8 constructions in the Scivetti CxNLI
  dataset ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md),
  ratified 2026-05-29 as the human anchor for caused-motion / conative / way / comparative-correlative).
  The catalog records a verbatim conative NLI triple — premise *"I sipped at the Heineken."*,
  hypothesis *"The Heineken was not the target of my sipping."*, relation **Contradiction** (Table 9)
  — and a native-speaker baseline (Exp 1 ≈0.90). **Caveat:** the release gives a *single* adjudicated
  gold label per item, so it grounds an **answer-key** comparison and an aggregate baseline, **not a
  per-item human gradient**. A result here *could* therefore carry a genuine human-comparison NLI
  claim on the entailment arm, where AANN's could not.
- **Headroom precondition buildable:** YES, and already demonstrated off-ceiling in v1 (conative
  affirm 13–66.7% across cells, vs transitive ~ceiling). The cancel direction is exactly where the
  AANN's headroom problem does not arise.
- **Known wrinkle to design around:** the conative already exposes cross-instrument fragility in
  gpt-5.4-mini (it fails conative suppression under NLI — calls *kicked at the ball* an entailment
  of contact — while partly recovering under forced-choice;
  [`result/conative-cancel-direction-v2`](../../findings/results/conative-cancel-direction-v2.md)).
  This is *informative* for the generality question (it is a second site of preference/commitment
  divergence) but the design must pre-register how it scores a model that inverts the expected
  NLI direction, so the result is not read as confirmation-by-coincidence.

### Option B — a different in-repo CxNLI-anchored construction (way / caused-motion)

Both the way-construction (*whistled her way down the hall* → traversed) and caused-motion
(*sneezed the napkin off the table* → caused motion) are CxNLI-anchored **add-direction**
constructions: the construction *adds* an entailment the bare verb lacks.

- **Inference/default divergence:** present in principle, but **both ran at ceiling**
  ([`result/way-construction-traversal-v1`](../../findings/results/way-construction-traversal-v1.md):
  way rate 77.8–100%, gap +77.7–100 pp, all three models, both instruments;
  [`result/caused-motion-minimal-pair-divergence-v1`](../../findings/results/caused-motion-minimal-pair-divergence-v1.md):
  cm rate 90–100%, gaps +70–100 pp). The essay already notes these add-direction positives
  *converge across instruments* because both compatibility and commitment move together — so they
  are precisely the cases *without* the dissociation, and a preference/commitment split has little
  room to appear.
- **In-repo human anchor:** YES (same CxNLI page).
- **Headroom precondition buildable:** **NO at the current item difficulty** — the headroom
  precondition (control off-ceiling, target ≤0.30 or hard-ceiling ≤0.50) fails when the
  construction itself reads at ceiling on both instruments. To get headroom one would have to
  engineer adversarial / near-miss items (the caused-motion near-miss v2c line did this), which
  reintroduces the AANN-style "engineer the control" cost the conative avoids.

### Option C — an un-anchored novel construction

Pick a fresh construction with a clean inference/default divergence but **no in-repo human anchor**
(e.g. a construction outside CxNLI's 8 and outside Mahowald's AANN stimuli).

- **Inference/default divergence:** could be chosen to be ideal.
- **In-repo human anchor:** **NONE** — the result would be forced to `anchor: internal-contrast-only`
  (a within-model contrast, no human-comparison claim), or would have to queue a fresh anchor
  decision and very likely build/ingest a new resource first. **Flag the anchor cost:** this is a
  real cost the project's anchor discipline (CLAUDE.md §anchor) charges against; with two
  CxNLI-anchored cancel/divergent candidates already in-repo, paying it is hard to justify for a
  first generalization test. **Provisionally rejected** on anchor-cost grounds unless a specific
  un-anchored construction is shown to have a divergence that no anchored one matches.

### Option D (no-go) — keep the dissociation AANN-scoped

Decline to generalize: record the preference/commitment dissociation as an AANN-instanced
methodological finding (now replicated across two AANN item sets) and run no fresh-construction
test. **Risk:** under-explores a forward bet the essay and the conjecture both make; leaves the
"AANN-specific vs general" question permanently open. The floor if A–C all prove unbuildable.

## Provisional default and its rationale

**Option A (the conative), with Option B's harder near-miss variant as the named fallback only if
the conative proves unbuildable under the binding conditions.** Rationale: the conative is the
*only* in-repo candidate that combines (i) a clean, **built-in** inference-vs-default divergence (it
is cancel-direction, so the divergence is free, not engineered), (ii) an **in-repo human anchor**
(CxNLI conative subset, answer-key + ≈0.90 baseline), and (iii) a **demonstrated off-ceiling
baseline** so the headroom precondition is already met by prior runs. The add-direction
constructions (Option B) ran at ceiling — exactly the no-dissociation regime — so they cannot host
the preference/commitment split without re-engineering headroom; the un-anchored route (Option C)
pays an anchor cost two anchored candidates make unnecessary. One-sentence default: **the conative
is the cleanest divergence with an in-repo anchor and buildable headroom.**

A nuance the ratifying session must weigh: because the conative already shows gpt-5.4-mini's
NLI-fails/FC-recovers fragility, the design must pre-register a scoring rule that prevents reading
the *existing* instrument fragility as *new* confirmation of the generalization conjecture — the
test is whether the **full panel** reproduces the qualitative AANN pattern (paraphrase shift in all,
commitment in a minority, one model converging), not whether any one model diverges.

## Binding conditions inherited from the ratified AANN decision

Any design under this decision inherits the discipline of
[`decisions/resolved/aann-inferential-default-coincidence`](../resolved/aann-inferential-default-coincidence.md)
(itself inheriting the eight conditions of
[`decisions/resolved/aann-inferential-operationalization`](../resolved/aann-inferential-operationalization.md)),
adapted to the fresh construction:

1. **Headroom precondition.** The control baseline (the inference the construction is to
   shift) must be demonstrably **off-ceiling** in a pre-registered sanity check before the
   construction contrast is interpreted (the AANN target was control unification ≤0.30, hard
   ceiling ≤0.50). For the conative this is the transitive-vs-conative affirm-contact gap, already
   shown off-ceiling in v1; the design must re-verify it on the frozen fresh items. **If the chosen
   construction reads at ceiling on both instruments, the design must not run** — route to the
   fallback.
2. **Mandatory lexical-cue control arm.** The headline must be a **double contrast** — the
   construction must move the reading *more than a matched non-construction string carrying the same
   lexical cue moves it*. A shift wholly attributable to the lexical cue is declared a **lexical-cue
   artifact** and cannot carry the headline. (For the conative the natural cue-control is the
   non-alternating / anomalous *at*-string family the v1 and v2 probes already used.)
3. **Pre-registered decision rule (verdict map frozen before the run).** The per-model
   categories — PARAPHRASE-ONLY / CONVERGENT-POSITIVE / NULL — and the panel-level verdict
   (confirm/falsify of the generality conjecture) must be fixed in the frozen design, with the
   thresholds (τ on the double contrast, CI rule) carried from the AANN instrument unless explicitly
   re-justified. **No retuning the indicator after seeing results** (PROTOCOL §8 operationalization
   gate).
4. **Both instruments on the same frozen items, agreement-style discriminator weighted above the
   paraphrase arm where one exists.** The paraphrase arm is the *weaker* signal (the AANN decision
   and result are explicit that a paraphrase-preference shift is weaker than a converging NLI shift);
   a paraphrase shift without a commitment shift is reported as "preference without commitment," not
   "draws the inference." The conative has no AANN-style grammaticalized agreement reflex, so the NLI
   commitment arm carries the discriminator role and the design must say so.
5. **Anchor status stated precisely and honestly.** If the conative (or another CxNLI construction)
   is used and the result makes a human-comparison NLI claim against the CxNLI gold labels, the
   result is **human-anchored** via [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
   on the entailment arm (answer-key comparison + ≈0.90 baseline; **not** a per-item gradient). The
   forced-choice paraphrase arm and any cue arm without an in-repo human norm stay
   `internal-contrast-only`. If an un-anchored construction is chosen (Option C), the whole result is
   `internal-contrast-only` and a fresh anchor decision must be queued. **No anchor may be invented.**

## Anti-cheat note

The binding conditions are constructed to bias **against** a free positive, exactly as the AANN
decision's were:

- The **headroom precondition** makes a *null* informative (it cannot be dismissed as ceiling) and
  forbids running where a positive would be unfalsifiable.
- The **lexical-cue double contrast** disqualifies a shift that a matched cue alone could produce —
  a measured paraphrase shift only counts net of the cue.
- The conjecture is **symmetric**: it is confirmed by reproducing the *qualitative pattern*
  (paraphrase shift broad, commitment narrow, one model converging) and **falsified** by either full
  cross-instrument convergence in all models *or* a full null in all — so neither a uniform positive
  nor a uniform negative can be spun as confirmation.
- The known gpt-5.4-mini conative fragility must be pre-registered *as a scoring rule*, so the
  existing divergence cannot be retrofitted as new evidence for generality.
- This decision fixes the **yardstick** (which construction, what counts), never a result. A later
  session motivated by wanting a particular outcome must not ratify it (PROTOCOL §2 anti-cheat).

## Status / handoff note

Opened this session; **carry in NEXT.md as "opened this session (not yet eligible)."** The
contingent conjecture
[`conjecture/preference-commitment-generality`](../../findings/conjectures/preference-commitment-generality.md)
is written under this decision's provisional default and stays in provisional language until a later
session ratifies (or amends) the default. The frozen design + independent pre-run critic + the run
itself belong to a *later* session, after ratification — this unit only surfaces the decision and
the forward conjecture, runs no probe, spends nothing, and authors no stimulus items.
