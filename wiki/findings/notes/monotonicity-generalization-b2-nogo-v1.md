---
type: note
id: monotonicity-generalization-b2-nogo-v1
title: Monotonicity-generalization battery — B2 ceiling gate NO-GO; the add arm is buildable at ceiling but the ratified for-durative cancel arm is not, because its "only once" default is a defeasible implicature the panel floors under strict NLI
meaning-senses:
  - constructional
  - inferential
status: recorded
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-07-06
links:
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: refines
    target: note/addarm-headroom-calibration-v1
  - rel: refines
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: concept/coercion
---

# Result: monotonicity-generalization battery — B2 ceiling-gate NO-GO

> **Reclassified 2026-07-06 (session 185, campaign P3 / program B6): result → note.** A design-feasibility B2 ceiling-gate outcome (NO-GO); the spend-bearing battery was not run — a gate record, no finding about LLM meaning. Per the `note` page type (CLAUDE.md) it carries **no new measurement about LLM meaning**; `status: recorded`. History-preserving reclassification — nothing measured, scoped, or decided on this page changes.

> **Design-feasibility gate outcome, `internal-contrast-only`.** This records the **B2
> blocking ceiling gate** firing on the matched-difficulty add-vs-cancel battery — the
> sole decisive test of [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md).
> The gate is a **NO-GO**: the spend-bearing asymmetry battery was therefore **not run**
> (the rule is "a NO-GO defers the run rather than relaxing the bar"). This makes **no
> human-comparison claim** — it measures only within-model affirm rates to decide whether
> the ratified arms can be built at matched ceiling. Pre-registration, run record, every
> number: [`experiments/runs/2026-06-28-monotonicity-generalization-battery/`](../../../experiments/runs/2026-06-28-monotonicity-generalization-battery/README.md).

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The awaited cancel arms landed the
> same UTC day: [`note/monotonicity-c2-privative-calibration-v1`](monotonicity-c2-privative-calibration-v1.md)
> (session 137, B2 GO — category default 1.00 in 3/3),
> [`result/monotonicity-c2-battery-v1`](../results/monotonicity-c2-battery-v1.md) (session 137, WEAK CONFIRM
> across the M2 domain mismatch), and [`result/monotonicity-within-verbal-battery-v1`](../results/monotonicity-within-verbal-battery-v1.md)
> (session 141, within-verbal CONFIRM — asymmetry ≥ 0.20 in 3/3 models, M2 discharged).
> [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
> is now `tested`. *(Back-annotation added by a maintenance pass; nothing measured or decided on
> this page changes.)*

## Why this ran

The s134 independent adversarial review **ratified** the operationalization of the
matched-difficulty add-vs-cancel generalization battery
([`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../decisions/resolved/constructional-monotonicity-generalization-operationalization.md),
ADOPT-WITH-MODS), fixing a **new** construction pair (**ADD = resultative**;
**CANCEL = the *for*-durative aspectual coercion of a semelfactive**) and a frozen **B2
blocking ceiling gate** that must pass *before* the main run. The decision is explicit
that the cancel arm's default — affirm-"happened only once" — is a *contestable*
entailment (MOD-3), and prescribes the failure path in advance: **a B2 NO-GO re-pairs the
cancel coercion before any spend rather than relaxing the bar.** This session built and
froze the battery and ran the B2 calibration; this result reports the gate outcome.

## What was measured

The frozen B2 gate, run on a calibration subset of the main items (4 add verbs ×
{control, construction} + 4 cancel verbs × {default}; `affirm` = NLI label 0 = entailment
| forced-choice YES; NLI primary, temperature 0, the behavioral panel
claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash; 12 items × 2 instruments × 3 models =
72 calls). The pair is **admitted** only if, in ≥2/3 models:

- **ADD headroom:** resultative `construction` licensing-no-cue affirm **≥ 0.80** AND bare
  `control` affirm **≤ 0.40**; AND
- **CANCEL default (MOD-3):** lexical-default affirm ("only once" on the bare frame)
  **≥ 0.80**.

The cancel **suppression** (construction) cell was deliberately held *out* of the
calibration, so the add-vs-cancel asymmetry magnitude was **not computable** at the gate —
the anti-cheat separation between "is the arm well-formed?" and "what is the asymmetry?"
held.

## One-line finding

**The gate is a NO-GO: the resultative add arm is buildable at ceiling (construction affirm
1.00, control 0.00 in 3/3 models), but the ratified *for*-durative cancel arm is not — its
"only once" default is affirmed at 0.00 in 3/3 models under both instruments. The failure
is structural, not verb-selection: single-occurrence is a defeasible quantity implicature,
not a lexical entailment, so a strict-NLI default can never reach the matched ceiling.**

## Numbers (verified)

Affirm rates, NLI primary; each cell n = 4 calibration items (identical across both
instruments here):

| arm | cell | model A (claude) | model B (gpt-mini) | model C (gemini) | gate target | pass? |
|---|---|---|---|---|---|---|
| ADD | construction (license) | 1.00 | 1.00 | 1.00 | ≥ 0.80 | ✓ 3/3 |
| ADD | control (bare) | 0.00 | 0.00 | 0.00 | ≤ 0.40 | ✓ 3/3 |
| CANCEL | default ("only once") | **0.00** | **0.00** | **0.00** | ≥ 0.80 | **✗ 0/3** |

- **ADD passes cleanly:** the resultative licenses the result-state entailment at ceiling
  ("hammered the metal flat" ⊨ "the metal became flat"), the bare control does not
  ("hammered the metal" ⊭ it) — re-confirming [`note/addarm-headroom-calibration-v1`](addarm-headroom-calibration-v1.md)
  on the frozen main items, in 3/3 models on both instruments.
- **CANCEL fails at floor:** every cancel `default` item (flash, jump, cough, nod), in all
  three models, returned NLI label **1 (neutral)** — never **0 (entailment)** — so affirm =
  0.00. The panel judges "The light flashed" as **not entailing** "The light flashed only
  once": a single flash is *consistent with* the sentence but not *forced* by it. Forced-
  choice agrees (0.00). The result is **uniform** across all four verbs, both calibration-
  subset and (by the same structure) the held-out verbs (knock, tap, blink).

Independently recomputed from the per-call `raw_calib/*.json` by a read-only post-run
verifier: exact match to `raw_calib/gate.json` on every cell; 72/72 priced, 0 parse
failures, NO-GO confirmed.

## Why this is structural, not a bad verb pool

The matched conflicting-cue paradigm ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md))
requires the cancelled inference to sit **at ceiling on the bare frame**, so that
suppression has something to suppress. cc-v2's cancel direction worked because the
transitive's contact entailment *is* a near-ceiling lexical entailment ("kicked the ball"
⊨ contact, 91.7–100%) that the conative then cancels. The *for*-durative/semelfactive
design instead targets a **Gricean quantity implicature** (single-occurrence): a
semelfactive is by definition a *repeatable* point-event, so "flashed once" is a defeasible
default the speaker *implicates*, never an entailment the sentence *carries*. Under a strict
NLI instrument ("the hypothesis **must** be true given the premise") a defeasible implicature
is correctly labelled neutral — so **no choice of semelfactive verb can lift this default to
the ≥ 0.80 ceiling.** Re-pairing verbs within the ratified frame is futile; the gate's
NO-GO is a property of the *operationalization*, not the verb list.

This is the lesson the gate exists to catch, arriving from the opposite direction the s132
review feared: the add-arm degeneracy worry was refuted (s133), but the **cancel** arm
turns out to have the matched-ceiling problem — its default is *too weak*, not too strong.

## What this does and does not license

- **Does:** establish, with a clean verified gate, that the ratified cancel arm
  (*for*-durative semelfactive, "only once" indicator) **cannot be built at matched
  ceiling** under the project's strict-NLI-primary instrument; and that the add arm
  **can**. It hands the re-design a sharp constraint: a workable cancel arm needs a default
  that is a **(near-)entailment at ceiling on the bare frame**, not a cancellable
  implicature.
- **Does not:** test the monotonicity conjecture. The asymmetry was **never read** — the
  cancel-suppression cell was held out of the gate and the main battery was not run. In
  particular, the panel's "neutral" verdict on "only once" is **not** evidence about the
  models' *defeasance ability*; it is evidence that single-occurrence is **not an
  entailment** for these models, so there is no ceiling default to fail to suppress here.
- **Does not** make any human comparison (`internal-contrast-only`), nor re-open or
  re-tune the ratified yardstick (the asymmetry/fragility/cue thresholds were untouched and
  unused).

## What happens next

The decision pre-authorized "re-pair the cancel coercion before spend" for a B2 NO-GO. Because
the failure is **structural to the ratified for-durative/semelfactive frame** (not a verb
choice), the honest next step is a **cancel-arm re-design**, not a within-frame re-pair —
which is a *yardstick* change and therefore a cross-session decision, surfaced (not ratified)
in s135 and **ratified s136** in [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md)
(independent adversarial review: **ADOPT C1 telic-completion conditional on its own B2 calibration**,
C2 privative fallback, then a principled-limit closure if both fail; the re-designed cancel arm must
itself clear a fresh B2 default-at-ceiling gate before any asymmetry is read).
[`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
stays **`proposed`**: its decisive test is built and the add arm is ready, but it awaits a
cancel arm that can reach matched ceiling.

## Provenance

- Every figure is reproduced verbatim from
  [`raw_calib/gate.json`](../../../experiments/runs/2026-06-28-monotonicity-generalization-battery/README.md)
  and independently recomputed from the per-call `raw_calib/*.json` by a read-only post-run
  verifier (exact match; 72/72 priced, 0 parse failures).
- The matched-ceiling requirement and the cc-v2 contact-entailment ceiling (91.7–100%) are
  quoted from [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md); the
  add-arm headroom context (resultative construction 1.000 / control 0.250) from
  [`note/addarm-headroom-calibration-v1`](addarm-headroom-calibration-v1.md). The
  contestable-default failure path is the ratified decision's own MOD-3.
- Spend: **$0.01720 billed** (UTC 2026-06-28), the calibration probe only; the asymmetry
  battery was not run.
