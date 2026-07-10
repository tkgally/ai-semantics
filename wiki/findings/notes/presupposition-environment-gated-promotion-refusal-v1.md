---
type: note
id: presupposition-environment-gated-promotion-refusal-v1
title: "Promotion review of the environment-gated presupposition line — REFUSE (records a refusal, not a claim): the environment-gating DIRECTION replicated on each signature, but the matched-surface-cue control that would license 'survives its controls' is single-run and under-licensed, and the accommodation leg cannot behaviorally separate genuine gating from contradiction-detection + yes-bias; internal-contrast-only"
meaning-senses:
  - inferential
  - distributional
status: recorded
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-10
updated: 2026-07-10
links:
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/projection-trigger-inventory-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: result/accommodation-cue-strength-v1
  - rel: depends-on
    target: result/presupposition-doppelganger-control-v1
  - rel: depends-on
    target: essay/presupposition-environment-gated
---

# Promotion review — environment-gated presupposition line — **REFUSE**

> **Verdict: REFUSE (2026-07-10, s203).** Cross-session, independent, adversarial claims-promotion
> review ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item **B1**, last candidate) of whether the
> "presupposition corner is **environment-gated in both directions**" reading
> ([`essay/presupposition-environment-gated`](../essays/presupposition-environment-gated.md), `status:
> live`) should be promoted to a standing `claim`. The fresh reviewer produced none of the underlying
> work. **The decision is to NOT promote.** The environment-gating *direction* genuinely replicated on
> each signature, and that stays a legitimate `live` reading; what does **not** clear the standing-claim
> bar is *survived its controls*. This note **records the refusal** and closes program item B1's last
> candidate honestly.
>
> **This note carries NO new measurement.** It is a $0 promotion-review record. Per the `note` discipline
> ([`CLAUDE.md`](../../../CLAUDE.md) §Page types), it must **never** be cited as support for any claim; it
> neither strengthens nor weakens the underlying results, which stand exactly as written.
>
> `anchor: internal-contrast-only` — the entire line is ratified internal-contrast-only (every underlying
> result scores only within-model rates over the model's own YES/NO/UNCLEAR answers, no human key), so this
> refusal note inherits that terminal declaration and makes **no human comparison** anywhere.

## The bar

PROTOCOL §3 promotes a result-line to a standing `claim` only when it has **REPLICATED** (fresh items or a
second run) **AND SURVIVED ITS CONTROLS**; the output is a `claim` citing results/magnitudes, **or a
written refusal**. A written refusal is a first-class outcome — the review does not promote to look
productive, and does not refuse reflexively. Promotion would fix the *yardstick*, never the result.

## What replicated (this is real, and stays a `live` reading)

The environment-gating **direction** is genuine on both signatures:

- **Projection is frame-gated, twice.** [`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md)
  (s158) found the presupposition survives **negation** cleanly (P endorsed near-ceiling while the matched
  entailment cancels to **E = 0.00**) and **collapses under the conditional antecedent** for every model
  (presup-survival **0.42 / 0.17 / 0.17**, at or near the matched-entailment leg). The conditional collapse
  then **replicated on four brand-new trigger families** in
  [`result/projection-trigger-inventory-v1`](../results/projection-trigger-inventory-v1.md) (s160,
  conditional-frame P = **0.25 / 0.17 / 0.00**; negation-only gap **+0.75 / +0.67 / +0.75** with E cancelling
  to 0.00 on all three). The frame, not the trigger, governs survival. This is a real, fresh-family
  replication of the direction, and the matched-entailment control bites cleanly (a yes-bias would leave E
  surviving; it did not).

- **Accommodation is context-gated, and the gate is graded.**
  [`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md) (verdict
  GATED-ACCOMMODATION **3/3**) found near-ceiling endorsement in a neutral context (**1.00 / 0.92 / 1.00**)
  and substantial withholding under explicit contradiction (**0.33 / 0.58 / 0.42**; accommodation-gap
  **+0.67 / +0.33 / +0.58**). A second run,
  [`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md) (verdict GRADED-GATE
  **3/3**), split the single denial into hedged vs emphatic and found every model backs off the denied P
  harder under the stronger denial (strength-gradient **+0.33 / +0.17 / +0.67**) — ruling out a *pure*
  contradiction-detector (which would gate weak and strong equally, FLAT).

So the reading's spine — *endorsement tracks the licensing environment, in both signatures* — is
directionally replicated and survives a yes-bias check on each leg. That is exactly why the essay is
correctly `live`. Nothing here retracts it.

## What did NOT survive its controls (why this is a reading, not yet a claim)

The line fails the §3 *survived its controls* half on two independent counts, both load-bearing:

1. **The matched-surface-cue control is single-run and under-licensed — no clean result either way.**
   [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)
   (s173, program A1a) is the project's own designated test of whether this corner's behavior is *more than*
   surface-cue-reconstructable. Its verdict was **BEATS-DOPPELGANGER** (pooled residual **+0.78 / +0.47 /
   +0.94**), but the result page is emphatic that this is the **UNDER-LICENSED** outcome: the powered
   factive/aspectual doppelgängers vary the **trigger word-form** (`realize`→`suspect`,
   `stopped`→`considered`), so any residual "is attributable to the words' different distributions — a
   verb-sensitive surface-cue account reconstructs it." **The clean FLAT null did not obtain, and neither did
   a clean beater**: the corner lands in "the under-licensed middle." The one construction-grain leg (cleft,
   which holds content words constant and varies only the construction) gives **no clean cross-panel
   residual** — gpt-5.4-mini **control-FAILS** it (trigger_project **0.583 < 0.60**, cleft residual **+0.08**,
   essentially FLAT), and the claude/gemini cleft residual is **carried entirely by the negation cell**, i.e.
   itself a negation-frame surface-cue difference. The control is **single-run**, and the residual is not
   shown **stable across frames** (the question frame is confounded; the conditional collapses; the D2 leg
   does not compose). "Survives its controls rather than being reconstructable from surface cue/word-form
   effects" is therefore **not** cleanly met, and it has not been replicated.

2. **The accommodation leg's own control is admittedly inconclusive.** The accommodation result page states,
   in its own words, that the gate leg **"cannot behaviorally separate genuine accommodation-*blocking* from
   generic contradiction-detection + yes-bias."** The GRADED-GATE second run narrows this (it rules out a
   *pure* contradiction-detector) but explicitly **"does not resolve the mechanism"**, and both readings it
   leaves standing are distributional. The residual **yes-bias pocket is located, not hypothetical**
   (gpt-5.4-mini endorses the cleft existential **100%** even under explicit contradiction), and B's
   graded margin is thin (**+0.17**, only ~a fifth of one item above the 0.15 bar; the verdict hinges on ~2 items). The essay itself calls the accommodation
   signature "the softer of the two." So on the leg that carries half of the "in *both* directions"
   unification, the key adversarial alternative is admitted-unresolved.

Add the standing bounds: **one grammatical corner**, **small synthetic N** (12 project-authored scenarios
per line), **n = 3** commercial models, **internal-contrast-only**, and — decisively for what a claim would
*add* — the line **confirms the distributional side** (the essay's thesis is that environment-gating *is* the
distributional description) rather than beating a shadow. Unlike the model precedent
[`claim/lexical-relation-recovery-cue-strength-decoupling`](../claims/lexical-relation-recovery-cue-strength-decoupling.md)
(s197), which promoted a twice-replicated **framework correction** on two corpus families with its controls
untouched, the compounding object here would be a *reading that its own strongest control cannot yet
license*. A scoped promotion could be worded to fence the beater over-read, but it would still be pinning
"survives its controls" to a single under-licensed run — which is exactly what the bar forbids.

## The decorrelation vote (convergent — recorded)

The non-Anthropic decorrelation vote (`gpt-5.4-mini`) returned **REFUSE**, decisive reason verbatim: *"the
control evidence is not clean enough to show the line survives controls rather than merely being
reconstructable from surface cue/word-form effects."* Its rationale matched this review's independently:
projection-gating replicated across two runs, but the doppelgänger control is under-licensed and
word-form-confounded (no clean flat null, no clean control-defeat), and the accommodation leg is especially
fragile (the result page cannot separate genuine accommodation-blocking from contradiction-detection +
yes-bias). **Convergence here is signal, not merely comfort** — a fresh Anthropic reviewer and a
non-Anthropic model reached REFUSE on the same specific control gap, from the same verified pages. Verdict
authority rests with this fresh review; the vote is recorded as corroboration.

## The exact strengthening path that WOULD earn promotion

This is not a permanent bar — it is a "not yet," with a named probe. The doppelgänger result page itself
names the least-confounded next probe, and it is exactly the decorrelation vote's "what would change it":

- **A second, clean, word-form-constant control run.** A **construction-grain-only doppelgänger battery**
  (cleft-family expansion, using the **negation-only** discriminating cell, and controlling the
  question-frame confound), holding the trigger **word-form constant** so only the construction varies —
  run as a **replication** of the matched-surface-cue control, with the environment-gating pattern
  replicating **while the control stays flat or dissociates** (a residual a surface-cue account cannot
  reconstruct, or a clean flat null, held stably across frames). On the accommodation side, an instrument
  that behaviorally separates accommodation-blocking from contradiction-detection + yes-bias would close the
  softer leg.

If a future session runs that control cleanly and it replicates the gating while the surface-cue control
dissociates, this line clears the §3 bar and a scoped `claim` becomes earnable. Until then it remains a
`live` reading at `internal-contrast-only` strength.

## Status

`status: recorded`. **REFUSE** — the environment-gated presupposition line is **not** promoted to a standing
claim this session. The underlying results and the `live` essay are unchanged. Program item **B1**'s last
candidate is **closed with an honest refusal**. `contingent-on: []`. This note carries **no new measurement**
and **must not be cited as support for any claim**.
