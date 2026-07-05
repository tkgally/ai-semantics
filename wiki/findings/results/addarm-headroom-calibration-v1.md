---
type: result
id: addarm-headroom-calibration-v1
title: Add-arm headroom calibration — a genuinely non-entailing control exists and the resultative add arm has real licensing headroom; the default-coincidence trap is real but verb-specific and avoidable
meaning-senses:
  - constructional
  - inferential
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-07-05
links:
  - rel: refines
    target: open-question/constructional-monotonicity-addarm-headroom
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
  - rel: depends-on
    target: concept/coercion
---

# Result: add-arm headroom calibration v1

> **Design-feasibility calibration, `internal-contrast-only`.** This result decides whether a non-degenerate **add arm** can be built for a future monotonicity-generalization battery; it is **not** a test of [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md) and makes **no human-comparison claim** — it measures only within-model construction-vs-control affirm rates. The `internal-contrast-only` posture follows the same ratified logic as the conflicting-cue arms ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)); this calibration is even further from a human claim (pure instrument design). Pre-registration, run record, and every number: [`experiments/runs/2026-06-28-addarm-headroom-calibration/`](../../../experiments/runs/2026-06-28-addarm-headroom-calibration/README.md).

## Why this ran

The session-132 independent review of [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../decisions/resolved/constructional-monotonicity-generalization-operationalization.md) returned **KEEP-OPEN**, with a load-bearing **blocker (prerequisite 1)**: the decision's provisional **resultative** add arm had *undemonstrated, plausibly degenerate* headroom — the worry (the "default-coincidence trap") that a non-resultative control might supply the state-change entailment **for free**, pinning the add arm at ceiling with nothing to measure, so "add easy" would be a tautology of the arm construction rather than a finding. The review demanded a frozen calibration probe **before any main run** showing either that a genuinely non-result-entailing control exists with real add headroom, **or** naming a cleaner add construction. The design-level companion [`open-question/constructional-monotonicity-addarm-headroom`](../open-questions/constructional-monotonicity-addarm-headroom.md) specified the test; this result runs it.

## What was measured

For two candidate ADD constructions, the no-cue **licensing gap** per verb. Each verb has a `construction` arm (sentence WITH the construction) and a `control` arm (bare verb + identical arguments, construction removed), both asked the **same** added-entailment hypothesis. `affirm` = NLI label 0 (entailment) | forced-choice YES. Per-verb **headroom = construction_affirm − control_affirm**. 48 items × {NLI, FC} × 3 models = 288 calls, temperature 0, the behavioral panel (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash).

- **resultative** (the decision's at-risk provisional arm), 12 verbs spanning the canonicity spectrum — manner verbs whose bare default plausibly does *not* entail the result (hammer flat, kick open, paint white, …) vs telic verbs whose default plausibly *does* (freeze solid, sharpen sharp, …).
- **intrans-motion** (a plausible-but-unverified alternative), 12 manner-of-motion verbs + directional PP; added entailment phrased **generically** ("moved to a different place"), not goal-specific, so an off-ceiling control reflects the construction's contribution, not an unmentioned goal noun.

**Frozen gate (set before any data):** a verb is *headroom-clean* iff panel-aggregate (NLI) construction affirm ≥ 0.80 **and** control affirm ≤ 0.40; a construction *demonstrates headroom* iff ≥ 4/12 verbs are clean **and** ≥ 1 is clean in ≥ 2/3 models.

## One-line finding

**A genuinely non-entailing control exists, and the resultative add arm has real licensing-no-cue headroom against it: the s132 degeneracy worry is not borne out.** Both candidate constructions clear the frozen gate; the default-coincidence trap is **real but verb-specific and avoidable by verb selection**.

## Numbers (verified)

| construction | construction affirm (NLI, mean) | control affirm (NLI, mean) | headroom-clean (aggregate) | clean in ≥2/3 models | trap verbs (control at/near ceiling) | demonstrates headroom |
|---|---|---|---|---|---|---|
| **resultative** | **1.000** | **0.250** | **10/12** | 10 | freeze (1.00), sharpen (1.00) | **YES** |
| **intrans-motion** | **0.972** | **0.333** | **7/12** | 8 (+sway) | drift (1.00), slide (1.00), swing (1.00), bounce (0.67) | **YES** |

- **Resultative, headroom-clean (10/12):** beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe. The construction licenses the result-state entailment at ceiling (1.0); the bare-transitive control is *off* ceiling — e.g. "hammered the metal" does not entail "the metal became flat"; "kicked the door" does not entail "the door became open." Even `wipe`/`scrub`, predicted as plausible traps, came back off-ceiling (control 0.00 / 0.33). Only the genuinely telic `freeze→solid` and `sharpen→sharp` had controls already at ceiling — the trap end of the spectrum, present **by design**, correctly flagged degenerate.
- **Intrans-motion, headroom-clean (7/12 aggregate; 8 in ≥2/3 models):** bob, float, rock, roll, spin, twirl, wobble (+ sway robustly but below aggregate ceiling). Trap verbs are the displacement-encoding ones (drift, slide, swing, bounce — bare "drifted"/"slid" already entail change of location); pure manner verbs (spin, float, bob, wobble, rock, twirl) have full headroom. `sway` missed on the **construction** side (0.67) — the "swayed *toward* the door" weakness the pre-run critic flagged (a *toward*-PP need not entail net displacement); a conservative miss, not a control-trap.
- **Forced-choice tracks NLI and is marginally cleaner** (resultative control 0.111; intrans control 0.306), so the NLI verdict is conservative; no instrument fragility flips the headroom call (relevant to the conjecture's confirm-leg-2, which is about NLI-vs-FC divergence — none here that would matter).

## What this discharges

This **discharges the s132 review's blocker (prerequisite 1)**: a genuinely non-result-entailing control demonstrably exists, and the resultative add arm has real licensing-no-cue headroom against it — so the resultative arm is **not** degenerate when verb-selected away from the telic trap verbs (`freeze`, `sharpen`). It also (a) **names a cleaner-or-equal alternative** (intrans-motion, with its own verified verb pool), satisfying the prerequisite's explicit "or" branch, and (b) hands the operationalization decision a **concrete usable verb pool** and a **verified trap-verb exclusion list** for whichever construction it later freezes.

It does **not** discharge prerequisites 2–4 (concrete frozen thresholds for the main battery; an explicit pre-frozen add/cancel direction assignment; the reconsidered scope decision), and it **does not ratify** the operationalization decision — that remains a later session's independent adversarial-review pass. *[Update, s183: that review happened — ratification attempt 2 (session 134, same day, 2026-06-28) returned ADOPT-WITH-MODS, resolving [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../decisions/resolved/constructional-monotonicity-generalization-operationalization.md), with this calibration's verb pool and trap-verb exclusions adopted into the frozen pairing.]*

## What this does and does not license

- **Does:** establish that a non-degenerate add arm with genuine headroom **can be built** (the feasibility the s132 blocker required) for both candidate constructions; supply the verb pools and trap exclusions.
- **Does not:** test the monotonicity conjecture (this measures feasibility only, never add-vs-cancel); make any human comparison (`internal-contrast-only`); or ratify the operationalization decision.
- **Limits:** small-N (12 verbs/construction), single run, panel-as-instrument — a direction-of-feasibility signal, not a magnitude. The **bare-transitive is one control framing**, not the only conceivable one; a verb failing here fails *this* control, which is why the verdict is read per-verb so the clean subset survives a few degenerate verbs. The add direction's *depth* remains bounded ([`result/coercion-implicit-cue-v2b`](coercion-implicit-cue-v2b.md): "explicit-outcome parsing, not world-model integration") — a headroom-clean add arm is a buildable instrument, not a standalone competence claim.

## Provenance

- Every figure is reproduced verbatim from [`experiments/runs/2026-06-28-addarm-headroom-calibration/raw/results.json`](../../../experiments/runs/2026-06-28-addarm-headroom-calibration/README.md) and was independently recomputed from the per-call `raw/*.json` by a read-only post-run verifier (exact match; 288/288 priced, 0 parse failures).
- The degeneracy worry this addresses is quoted from [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../decisions/resolved/constructional-monotonicity-generalization-operationalization.md) ("Ratification attempt 1 — session 132") and [`open-question/constructional-monotonicity-addarm-headroom`](../open-questions/constructional-monotonicity-addarm-headroom.md); the base-accuracy context (resultative 0.77–0.89) from [`result/scivetti-cxnli-answer-key-v1`](scivetti-cxnli-answer-key-v1.md), *Per-construction accuracy*.
- Spend: **$0.06833 billed** (UTC 2026-06-28).
