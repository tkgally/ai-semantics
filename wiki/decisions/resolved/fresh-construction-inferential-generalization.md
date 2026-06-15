---
id: fresh-construction-inferential-generalization
title: How to test whether the AANN "preference-without-commitment" double-contrast dissociation is AANN-specific or a general property — choosing the fresh construction to carry the instrument
status: resolved
opened: 2026-06-14
opened-by: autonomous (workflow session 2026-06-14)
resolved: 2026-06-15
resolved-by: autonomous (adversarial review)
resolution: ADOPT DEFAULT (Option A — apply the double-contrast preference/commitment instrument to the CONATIVE), with Option B's harder near-miss variant as the named binding fallback if the conative proves unbuildable under the binding conditions. The conative is the only in-repo candidate that simultaneously supplies (i) a built-in, free inference-vs-default divergence (cancel-direction), (ii) a ratified in-repo human anchor (CxNLI conative subset), and (iii) a demonstrated off-ceiling baseline. Anti-cheat PASS (the binding conditions bias against a free positive; the symmetric conjecture cannot be spun either way; the pre-registered scoring rule forbids retrofitting gpt-5.4-mini's pre-existing conative NLI fragility as new evidence). Fabrication CLEAN; anchor honesty correct. One yardstick-translation condition added at ratification (see Ratification §): the AANN headroom thresholds (P(uni|control) ≤ 0.30 / ≤ 0.50) were defined for the unification reading and MUST be re-stated in conative terms in the frozen design (conative affirm-contact demonstrably off the transitive ceiling), since v1/v2 conative cells range up to 66.7%.
provisional-default: Option A (apply the double-contrast preference/commitment instrument to the CONATIVE — a cancel-direction, CxNLI-anchored construction whose licensed inference runs opposite to the verb's distributional default, which by construction supplies headroom)
contingent-artifacts:
  - conjecture/preference-commitment-generality
eligible-for-ratification: YES — opened 2026-06-14, ratified 2026-06-15 (a later session; PROTOCOL §2 boundary held)
---

# Decision: which fresh construction carries the preference/commitment generalization test

> **RESOLVED 2026-06-15 (autonomous adversarial review, cross-session — opened by the
> 2026-06-14 eleventh session, ratified by the next session per PROJECT.md §12.3). Verdict:
> ADOPT DEFAULT (Option A — the conative), with Option B's harder near-miss variant as the
> binding fallback.** An independent reviewer (a fresh agent, author of none of these pages)
> read the decision, its options, the provisional default, the contingent conjecture, the
> candidate-construction result pages, and the CxNLI anchor resource, and returned **ADOPT
> DEFAULT** — anti-cheat **PASS**, fabrication **CLEAN**, anchor honesty **correct**. See the
> **Ratification** section at the foot of this page for the verdict, the verified numbers, and
> the one yardstick-translation condition added. Tom's standing override outranks this
> autonomous ratification. The contingent conjecture
> [`conjecture/preference-commitment-generality`](../../findings/conjectures/preference-commitment-generality.md)
> stays a forward bet until a design+result exists; its anchor status moves to the split status
> (entailment arm CxNLI answer-key; FC/cue arms internal-contrast-only) only when that result lands.

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
([`decisions/resolved/aann-inferential-default-coincidence`](aann-inferential-default-coincidence.md)):
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
[`decisions/resolved/aann-inferential-default-coincidence`](aann-inferential-default-coincidence.md)
(itself inheriting the eight conditions of
[`decisions/resolved/aann-inferential-operationalization`](aann-inferential-operationalization.md)),
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

## Ratification (2026-06-15, autonomous adversarial review)

**VERDICT: ADOPT DEFAULT (Option A — the conative).** Reviewer: an independent fresh agent,
author of none of these pages; the decision was opened 2026-06-14 (eleventh session) and reviewed
2026-06-15 (a later session), so the PROTOCOL §2 boundary held.

**Verified numbers (each checked against its cited source page).** Transitive default affirm-contact
**92–100%** ([`result/conative-minimal-pair-divergence-v1`](../../findings/results/conative-minimal-pair-divergence-v1.md));
conative affirm-contact **13–66.7%** across v1/v2 cells (off-ceiling); way **77.8–100%**
([`result/way-construction-traversal-v1`](../../findings/results/way-construction-traversal-v1.md));
caused-motion **90–100%** ([`result/caused-motion-minimal-pair-divergence-v1`](../../findings/results/caused-motion-minimal-pair-divergence-v1.md))
— the add-direction pair runs at ceiling, the no-dissociation regime, confirming Option B is a poor
host. The CxNLI conative triple (premise *"I sipped at the Heineken."*, hypothesis *"The Heineken was
not the target of my sipping."*, relation **Contradiction**, Table 9) and the ≈0.90 Exp-1 native
baseline match [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
verbatim; the AANN-exclusion note ("not among the 8 constructions; do not cite this dataset for
AANN") is correctly quoted.

**Anti-cheat PASS.** The headroom precondition makes a null informative and forbids running where a
positive would be unfalsifiable; the lexical-cue double contrast disqualifies a shift a matched cue
alone could produce; the conjecture is symmetric (falsified by full convergence in all three *or* a
full null in all three); and the pre-registered scoring rule for gpt-5.4-mini's known conative NLI
fragility forbids retrofitting the pre-existing single-model divergence as new evidence. The default
fixes a **yardstick**, not a result.

**One condition added at ratification (yardstick translation, binding on the frozen design).** The
AANN headroom thresholds (P(uni|control) ≤ 0.30 PASS / ≤ 0.50 MARGINAL) were defined for the
*unification* reading. The conative quantity is the **transitive-vs-conative affirm-contact gap** (or,
equivalently, the conative affirm-contact rate sitting demonstrably **off the transitive ceiling**).
The frozen design must **re-state the headroom gate in conative terms** and re-verify it on the
frozen items rather than importing the AANN's numeric ≤0.30/≤0.50 thresholds uncritically — v1/v2
conative cells range up to 66.7%, above the AANN 0.50 hard ceiling, so the gate must be a
*construction-effect headroom* statement (conative affirm meaningfully below the transitive ≥0.92
ceiling, with room for both instruments to diverge), not a literal P(uni)≤0.30 import.

**Contingent artifacts.** [`conjecture/preference-commitment-generality`](../../findings/conjectures/preference-commitment-generality.md)
stays `proposed` and a forward bet; its `contingent-on` is cleared at the moment a frozen design under
this ratified default exists. Its anchor moves from `pending` to the split status (entailment arm
CxNLI answer-key + ≈0.90 aggregate baseline, NOT a per-item gradient; FC/cue arms
internal-contrast-only) only when an actual result lands.

## Status / handoff note

Opened 2026-06-14; **ratified 2026-06-15 (this section).** The
contingent conjecture
[`conjecture/preference-commitment-generality`](../../findings/conjectures/preference-commitment-generality.md)
is written under this decision's provisional default and stays in provisional language until a later
session ratifies (or amends) the default. The frozen design + independent pre-run critic + the run
itself belong to a *later* session, after ratification — this unit only surfaces the decision and
the forward conjecture, runs no probe, spends nothing, and authors no stimulus items.
