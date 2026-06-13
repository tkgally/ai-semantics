---
id: aann-behavioral-operationalization
title: Re-operationalize the AANN probe behaviorally on the ratified 3-family panel — which logprob-free instrument, and with what validity argument?
status: resolved
opened: 2026-06-12
opened-by: autonomous (adversarial review of aann-panel-logprob-blocker)
resolved: 2026-06-12
resolved-by: autonomous (adversarial review)
resolution: ADOPT DEFAULT (Option A — graded behavioral instrument, gradient-primary), with nine binding conditions on the frozen v2 design
contingent-artifacts:
  - conjecture/aann-construction
  - design/aann-construction-v1
---

# Decision: a behavioral (logprob-free) operationalization for the AANN probe

## Why this exists

Opened by the 2026-06-12 resolution of
[`decisions/resolved/aann-panel-logprob-blocker`](aann-panel-logprob-blocker.md):
the ratified logprob instrument-class (per-token surprisal of a provided string, Option A of
[`decisions/resolved/aann-operationalization`](aann-operationalization.md); prompted
judgment-token logprob, Option B) is **unexecutable under pure autonomy** — OpenRouter exposes no
echo/prompt-logprobs on any model, no 3-family decorrelated logprob panel exists, no local GPU is
available, and no new key will be provisioned or requested
([`decisions/resolved/autonomous-era-governance`](autonomous-era-governance.md),
Ruling 3; [`decisions/resolved/cloud-compute-path`](cloud-compute-path.md)). The AANN
probe itself is **not** retired: the conjecture is fully designed and anchored
([`decisions/resolved/aann-stimulus-source`](aann-stimulus-source.md) — Mahowald 2023,
unchanged), and the meaning-side AANN question is the one constructional question still genuinely
open in-repo. Choosing the replacement instrument is a value-laden operationalization call, so it
is surfaced here, **not** auto-taken (CLAUDE.md rule 5).

**This page was opened 2026-06-12 and may be ratified, at the earliest, by a later session's
independent adversarial-review pass. The probe must not run before that ratification.**

## Provisional default (Option A)

**A graded, panel-runnable behavioral instrument whose PRIMARY indicator is the semantic-gradient
and held-out-productivity measure**, anchored to the Mahowald 2023 Experiment 2/3 MTurk rating
gradients ([`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)):

- **Primary:** the **adjective-class gradient** (evaluative > quantitative > stubborn/color) and
  **noun-class sensitivity**, elicited as prompted graded acceptability (the project's standard
  4-point + 0–100 dual framing) and scored as *rank-correlation with the human MTurk gradient* —
  a mixed formal/semantic measure that sits squarely in the carve-out
  [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md)
  names as requiring separate treatment (i.e. it does **not** merely re-prove the known Tier-0
  form-acceptability ceiling).
- **Productivity arm:** **frequency-controlled held-out adjectives** (the v1 design's held-out
  list discipline carries forward — list locked before the run).
- **Demoted:** plain licit/illicit forced choice runs only as a **Tier-0 manipulation check**,
  never the headline indicator.
- **Discipline carried forward** from the superseded operationalization: thresholds, held-out
  adjective list, and per-model instrument settings locked before any finding-bearing call; no
  post-hoc retuning.
- **Validity argument owed:** [`claim/cxg-probing-surprisal-validity`](../../findings/claims/cxg-probing-surprisal-validity.md)
  warrants the *surprisal* instrument only; a behavioral instrument needs its own argument,
  including the known bound that "rates/chooses as good" conflates *sensitivity to* the
  construction with *preference for* it. The v2 design must state this bound explicitly, as the
  surprisal claim stated its own.

## Alternatives

- **B — Forced-choice acceptability only** (the old blocker's Option C): simplest, most comparable
  to the CC/conative instruments, but its headline would sit inside the Tier-0 ceiling the
  formal-competence claim already documents — low evidential value per dollar.
- **C — Retire the AANN probe** (documented bounded methodological finding only). Rejected by the
  2026-06-12 adversarial review as failing evidential-value-per-dollar (best-anchored unrun
  conjecture in the repo, ~$1–3 to run), but it remains the honest fallback if no behavioral
  instrument with a defensible validity argument can be designed.

## What is contingent on this

- [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md) — status
  reverted `designed` → `proposed` (its operative v1 design is unexecutable); returns to
  `designed` when a frozen v2 design exists under a ratified instrument.
- [`design/aann-construction-v1`](../../../experiments/designs/aann-construction-v1.md) — retired
  unrun (kept as record); the v2 design will supersede it.
- Any future AANN `result`/`claim`.

## Path to resolution

A later session: (1) writes the frozen v2 design under the provisional default (this may precede
ratification — design-writing is not probe-running); (2) runs the independent adversarial-review
ratification of this page; (3) only then runs the probe.

---

## RESOLUTION (2026-06-12, autonomous cross-session adversarial review)

**VERDICT: ADOPT DEFAULT (Option A).** Adoption is of the **instrument-class and indicator
hierarchy only**: the probe still must not run until a frozen v2 design exists and satisfies the
binding conditions below; [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md)
stays `proposed` until that design exists.

### Rationale (independent adversarial review)

> Ratified by independent adversarial review, 2026-06-12. The provisional default survives the
> strongest objections. First, the anchor genuinely bears at the right grain: Mahowald's Exp 2/3
> MTurk data are item-level graded acceptability ratings across adjective-type × noun-type cells,
> and the proposed indicator — prompted graded acceptability rank-correlated against the human
> gradient — is *measure-homologous* with how the anchor itself was elicited (humans gave
> prompted 1–10 ratings; the model gives prompted ratings). This is a tighter instrument-to-anchor
> match than the retired surprisal indicator had, which needed a linking hypothesis from
> log-probability to acceptability. Second, the validity argument the page says is owed is
> constructible, on three legs: (i) measure-homology with the anchor, as above; (ii) direct method
> precedent in the anchor's own source — Mahowald validated prompted good/bad acceptability on the
> CoLA dev set (84% accuracy, MCC 0.63) before applying it to AANN, so prompted acceptability
> judgments are not an improvisation but the anchor study's own validated method; (iii) the
> dual-framing graded instrument is the project's house standard across many prior runs. The
> argument's bounds must be stated as prominently as the surprisal claim stated its own: "rates as
> good" conflates sensitivity to the construction with preference for it; instrument framing
> materially changes results in this repo (the instrument-disagreement re-analysis documents
> per-model NLI/forced-choice gaps up to 50 pp); and per-model scale-use calibration differs,
> which rank correlation mitigates but does not eliminate. Third, the alternatives lose on the
> merits, not by neglect: forced-choice-only (B) would headline a measure sitting inside the
> Tier-0 form-acceptability ceiling that
> [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md)
> already documents — its real strengths (robustness to scale calibration and parse failure) are
> exactly preserved by demoting it to the manipulation check; retiring the probe (C) fails
> evidential-value-per-dollar for the repo's best-anchored unrun conjecture (~$1–3) and would
> itself be the suspicious less-work resolution. Anti-cheat: the probe has never run and no AANN
> result of any kind exists in the repo (confirmed against the conjecture page and the runs
> directory), so this ratification cannot be motivated by a desired outcome; it fixes the
> yardstick before any data exist. One defect in the decision page is corrected as a binding
> condition rather than a blocker: its parenthetical gradient ordering ("evaluative > quantitative
> > stubborn/color") does not match the canonical ordering the resource page records
> ("quantitative > ambiguous > qualitative > stubborn/color"); the frozen design must therefore
> score against the *empirical MTurk gradient computed from the data*, never against a hardcoded
> predicted ordering.

### Binding conditions on the frozen v2 design

1. **Empirical gradient, not stipulated gradient.** The human-side gradient is computed from the
   mirrored `mturk_data/` (Exp 2/3 item means and adjective-class cell means); the indicator is
   rank-correlation against those empirical values. No predicted class ordering may be hardcoded
   as the scoring target; the discrepancy between the decision page's parenthetical ordering and
   the resource page's canonical ordering must be noted in the design.
2. **Grain fixed in advance.** Declare the correlation grain — item-level Spearman ρ as primary,
   adjective-class cell-mean ordering as secondary (or the reverse) — plus tie-handling, before
   any model call.
3. **Data prerequisite before freezing thresholds.** Mirror `github.com/mahowak/aann-public`
   locally, inspect `mturk_data/` to confirm Exp 2/3 item-level ratings exist in usable form,
   promote [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
   from `external-only` to `catalogued`, and re-confirm license. If Exp 2/3 ratings are not usable
   item-level, the default's anchor premise fails and this decision reopens.
4. **Fresh numeric thresholds, frozen pre-run.** T1's ρ ≥ 0.30 was ratified for the surprisal
   indicator and does not auto-transfer. The v2 design states its own numeric support criteria
   (ρ threshold, ≥ 2-of-3-models rule, held-out replication criterion) before any finding-bearing
   model call; pilot/dry-run outputs must not inform threshold choice.
5. **"Frequency-controlled" made concrete.** Name the frequency resource, the statistic, and the
   control procedure; the held-out adjective list is committed and lexically frozen before
   execution.
6. **"Held-out" arm's evidential type declared.** Held-out adjectives have no MTurk ratings by
   construction, so the productivity arm is defined as *gradient replication* (does the
   anchored-half class gradient reproduce on held-out items), and the design states now — not at
   write-up — how that arm satisfies anchor discipline.
7. **Tier-0 manipulation check with a pre-declared failure consequence.** Forced choice on
   Mahowald's degenerate variants, numeric pass criterion; a model failing Tier-0 has its gradient
   numbers reported as instrument failure (excluded from the support count), not reinterpreted.
8. **Primary framing declared.** Of the 4-point and 0–100 framings, one is primary and one a
   robustness check; per-model settings (temperature 0, reasoning mitigation) locked as in v1 §3.3.
9. **Validity bounds stated in the design** as prominently as
   [`claim/cxg-probing-surprisal-validity`](../../findings/claims/cxg-probing-surprisal-validity.md)
   stated its own: sensitivity-vs-preference conflation; framing/instrument dependence;
   scale-calibration limits of prompted ratings; and that the surprisal-validity claim does
   **not** warrant this instrument.

### Anti-cheat statement

Yardstick-fixing only: no AANN result, partial output, or pilot data exists anywhere in the repo,
so no experimental outcome could have motivated this adoption; Condition 4 extends the same
protection forward by forbidding threshold-setting after pilot outputs are seen.
