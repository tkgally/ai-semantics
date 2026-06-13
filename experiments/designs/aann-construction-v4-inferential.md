---
type: design
id: aann-construction-v4-inferential
title: AANN construction probe v4 — inferential (unification + whole-evaluation), DOUBLE-CONTRAST against a distributive-default control with a within-design lexical-cue control arm, paraphrase-FC primary + NLI convergent + grammaticalized agreement discriminator (bare-plural control)
meaning-senses:
  - constructional
  - inferential
  - distributional
status: "drafted — pre-run critic pending (NOT YET RUN; no model calls made)"
contingent-on:
  - aann-inferential-default-coincidence
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: operationalizes
    target: conjecture/aann-construction
  - rel: depends-on
    target: decisions/resolved/aann-inferential-default-coincidence
  - rel: depends-on
    target: decisions/resolved/aann-inferential-operationalization
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: supports
    target: open-question/distributional-vs-inferential-constructional
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
---

# Experiment design v4 — AANN construction (inferential: unification + whole-evaluation), double-contrast against a distributive-default control

> **DRAFT — NOT RUN. No model calls have been made.** This design is written under the resolved
> Option-A decision [`decisions/resolved/aann-inferential-default-coincidence`](../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)
> (RESOLVED 2026-06-13, autonomous adversarial review: ADOPT Option A — engineer a
> distributive-default control — with Option B the binding fallback, under **six** amended binding
> conditions). It is a design-writing artifact only: **no probe has run, no stimulus set is frozen,
> no run directory exists.** The v4 probe may run **only after** a **fresh independent pre-run
> critic** reviews this design *plus* a frozen `PREREG.md` *plus* the `prep.py`-authored stimulus
> set in a **later** step, and returns GO. The run, if it happens, stays
> **`anchor: internal-contrast-only`** (within-model contrast; no human-comparison claim) — no
> human AANN-inference data exists and this ratification cannot change that.

**Governing decisions.** The frozen *yardstick* for v4 is set by two ratified, cross-session
decisions:

- [`decisions/resolved/aann-inferential-default-coincidence`](../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)
  — the decision this design **implements**: adopt a distributive-default control (Option A) to give
  an AANN unification shift the **headroom** v3 lacked, under **six** binding conditions (headroom
  precondition; mandatory within-design lexical-cue control arm; lexical-overlap parity
  re-justified; agreement sub-probe stays load-bearing with a *bare-plural* control; anchor
  internal-contrast-only + verbatim chief-cost statement; named-null fallback to Option B).
- [`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md)
  — the prior decision v4 **inherits**: the A+B two-instrument package (paraphrase forced-choice
  primary, entailment NLI convergent, grammaticalized singular/plural agreement sub-probe the
  load-bearing discriminator), under **eight** binding conditions. v4 inherits all eight **except**
  the Condition-2 amendment (the minimal-pair / overlap-parity clause), which is **re-justified**
  in §3.3 because the control now differs lexically from the AANN premise *by design*.

**Why v4 exists (the v3 cause this design removes).** v3
([`result/aann-inferential-v3`](../../wiki/findings/results/aann-inferential-v3.md)) returned a
**ceiling-bounded NULL**: at the paraphrase + NLI + agreement instrument, no model shifts the
unification-vs-distributive reading relative to the **bare-plural** control *three beautiful days*
— **because the models already read that bare plural as a unified evaluated stretch nearly every
time**. v3's documented control raw rates: paraphrase control **0.78 / 0.96 / 1.00** (claude / gpt /
gemini), NLI control **0.87 / 0.83 / 1.00**. The AANN-vs-control shift design subtracts a baseline
already at the unification ceiling, leaving no headroom. v4's single structural change: replace the
ceiling-pinned bare-plural paraphrase/NLI control with a **distributive-default control** — an
explicitly itemizing frame whose *baseline* reading is genuinely distributive — and add a third arm
that proves any measured shift is the **construction's**, not the imported lexical cue's. (These v3
numbers are quoted from the v3 result page; **no new numbers are invented** here.)

**Freeze discipline.** Everything in this page and the eventual run materials — item shapes,
distributive-default control frames, lexical-cue control frames, paraphrase wordings, NLI
hypotheses, was/were pairs, A/B letter assignments, lexical-overlap counts, the expert-stipulated
expected-inference key, the headroom-precondition gate, all thresholds, and per-model settings —
must be frozen **before any finding-bearing model call** (inherited Condition 8). No threshold may
be set or retuned from any pilot/dry-run output. The **full frozen stimulus set is authored later
by `prep.py`** (no model calls); this design specifies only the *shapes* and 2–3 worked illustrative
items. The analysis (`analyze.py`) must exist at freeze with the decision rule baked in, and
`probe.py` must refuse to run without a frozen `PREREG.md` and `analyze.py` present (the house
guard carried from v2b/v3).

---

## 0. Condition map — the SIX new conditions + the EIGHT inherited conditions → where satisfied

### Six new binding conditions (from `aann-inferential-default-coincidence` §Ratification)

| # | New binding condition | Where satisfied here |
|---|---|---|
| N1 | **Headroom precondition** — the distributive-default control's *baseline* unification rate must be off-ceiling (target ≤ 0.30, hard ceiling ≤ 0.50) **per model**, checked **pre-headline**; if not met, do not proceed → route to Option B | §5 (Headroom-precondition gate, pre-registered, gates the entire paraphrase/NLI headline); §6 verdict map routes to Option-B NAMED NULL if it fails |
| N2 | **Mandatory within-design lexical-cue control arm** — a non-AANN string carrying the *same* distributive lexical cue, so the interpretable quantity is a **double contrast**; spell out the **LEXICAL-CUE-ARTIFACT** verdict if the cue alone accounts for the whole shift | §3 (three-arm layout incl. the lexical-cue control), §4 (double-contrast headline statistic Δ²), §6 (LEXICAL-CUE-ARTIFACT verdict + its decision rule) |
| N3 | **Lexical-overlap parity re-justified, not waived** — paraphrase-option parity stays in force; the *control-premise* lexical asymmetry is quantified per-item and is exactly what arm N2 neutralizes | §3.3 (re-justification of inherited Condition 2; per-item `control_lexical_delta`); §3.1 (paraphrase-option parity unchanged) |
| N4 | **Agreement sub-probe stays the load-bearing discriminator; its control stays the BARE PLURAL** (not the distributive-default control), reported separately, weighted above paraphrase; headline-gating unchanged | §3.4 (agreement sub-probe, control = bare plural *three beautiful days*); §3.5 (headline-gating rule); §6 |
| N5 | **`anchor: internal-contrast-only` + verbatim chief-cost statement carry forward**; literature key stays expert-stipulated | §7 (Anchor); §7 carries the v4-adapted verbatim chief-cost statement |
| N6 | **Named-null fallback to Option B is binding** — if N1–N2 cannot be satisfied at design / pre-run-critic time, the design **must not run** and redirects to the cancel-direction (conative) route | §8 (Named-null fallback) and §6 (verdict map: HEADROOM-FAIL → Option-B NAMED NULL) |

### Eight inherited binding conditions (from `aann-inferential-operationalization` §Ratification)

| # | Inherited condition | Status in v4 / where satisfied |
|---|---|---|
| I1 | Primary instrument fixed before any call: **A (paraphrase FC) primary**, B (NLI) convergent; never reselected | §3 (PRIMARY-INSTRUMENT LOCK); front-matter `status`; `PREREG.md` "Primary instrument"; `analyze.py` headline reads Arm A |
| I2 | Indicator = AANN-vs-control **shift**, never raw AANN rate; control pairing + lexical-overlap parity | **AMENDED for v4** — re-justified in §3.3: the headline is now a *double* contrast (Δ²) against a distributive-default control + a lexical-cue control; raw rates descriptive only. Paraphrase-option parity (§3.1) unchanged; control-premise asymmetry quantified + neutralized by arm N2 |
| I3 | Grammaticalized agreement sub-probe is the **load-bearing discriminator**, separate, weighted above paraphrase | §3.4–3.5 (control = bare plural, per N4); `analyze.py` `headline()` downgrades wording if agreement null |
| I4 | At least some items place the **distributive paraphrase / reading as locally-fluent**; under-pressure subset analysed separately | Re-cast in v4: the **distributive-default control is itself the under-pressure condition** by construction (its baseline reading is distributive). A pre-declared subset is additionally authored where the distributive paraphrase is the locally-fluent continuation; §3.1, analysed separately |
| I5 | `anchor: internal-contrast-only`; no human-comparison claim; Mahowald = provenance only; key expert-stipulated; chief-cost verbatim | §7 (= N5) |
| I6 | Disputed literature codings flagged item-level, excluded from / sensitivity-tested against headline | §3.6 (`key_disputed` per item; `analyze.py` recomputes headline excluding flagged items) |
| I7 | **\|FC shift − NLI shift\|** per model a reported named statistic; convergence/disagreement rule; Tier-0 manipulation check + pre-declared failure consequence | §4 (named statistic), §6 (convergence rule), §3.7 (Tier-0) |
| I8 | Thresholds/items/wordings/settings frozen pre-run; pre-flight budget recorded; named null fallback | This page (frozen) + `PREREG.md`; §9 budget; §8 named null fallback |

---

## 1. Construct (unchanged from v3)

The AANN noun phrase (*a beautiful three days*) presents the measured quantity as **a single
unified, evaluated stretch** — one three-day span evaluated as beautiful *as a whole* — **not** a
distributive plural (*three separate days, each individually beautiful*). This is the
characteristic-semantics clause of [`conjecture/aann-construction`](../../wiki/findings/conjectures/aann-construction.md),
in the `constructional` + `inferential` senses ([`wiki/meaning-senses.md`](../../wiki/meaning-senses.md)).
v4 operationalizes: does the construction make a model **draw the unification / whole-evaluation
inference**, measured **only** as a within-model contrast (now a *double* contrast, §4), never a
raw AANN rate, never a human-comparison claim.

Distinct from v2's territory (graded acceptability of the form): a model can rate the form
acceptable and even track the human acceptability gradient (v2 SUPPORTED) without using the
unification/evaluation semantics. v4 — like v3 — tests the latter. **The single change from v3 is
the control**, chosen to remove v3's named ceiling cause.

## 2. Scope (inherited from the v3 repair — do NOT reintroduce the object/mass class)

Items span the two measure-noun classes v3's repair retained: **temporal** and **distance**. The
object/mass measure-noun class stays **dropped** (the v3 repair found the "continuous stretch"
unification paraphrase anomalous for mass/area/money nouns; see the v3 design banner and run
README). Restricting to genuine *extents* (time, distance) is what keeps the "continuous stretch"
unification reading well-formed. The full frozen item count and per-class split are authored by
`prep.py` and frozen in `stimuli.json` before any call; this design fixes the *shapes* (§3) and the
**design geometry assumption** used for the §9 budget (a v3-comparable base item count, ~23, plus
the added third arm).

## 3. Indicator — THREE arms on the same frozen items (the double contrast)

**PRIMARY-INSTRUMENT LOCK (inherited Condition I1).** **Arm A (paraphrase forced-choice) is the
primary instrument.** Arm B (entailment NLI) is the convergent robustness arm. Fixed here, in the
front matter, and in `PREREG.md`, before any model call; never reselected post-hoc. The headline
reads Arm A; Arm B is convergence evidence; the disagreement statistic (§4) is reported, never
averaged away.

The structural difference from v3 is the **control geometry**. v4 carries **three premise frames**
per base item, so each measure-noun item generates a triple:

1. **AANN** — the construction. *We spent a beautiful three days in Rome.*
2. **Distributive-default control (DDC)** — an explicitly itemizing / day-by-day frame whose
   *baseline* reading is genuinely **distributive**, replacing v3's ceiling-pinned bare plural.
   *On each of the three days in Rome, the weather was beautiful.* (or *Day by day across the three
   days in Rome, it was beautiful.*) The DDC resists the whole-stretch reading, so an AANN
   unification shift has **somewhere to register** (this is what removes the v3 ceiling cause —
   subject to the N1 headroom gate, §5).
3. **Lexical-cue control (LCC)** — a **non-AANN** string carrying the **same distributive lexical
   cue** as the DDC but **without** the AANN construction. *On each of the three beautiful days in
   Rome, we relaxed.* (the itemizing "on each of the three … days" cue, with no AANN). This arm
   isolates how much of any measured shift is the **lexical cue alone**, independent of the AANN
   construction (Condition N2).

The interpretable quantity is therefore a **double contrast** (§4): the AANN must shift toward
unification **more than the lexical cue alone moves a matched non-AANN string**. If the cue alone
accounts for the whole shift, the paraphrase arm is declared a **LEXICAL-CUE ARTIFACT** (§6) and
cannot carry the headline.

### 3.1 Arm A — paraphrase forced-choice (PRIMARY)

- **Premise frames:** the three frames above (AANN, DDC, LCC) for each base item.
- **Forced choice** (same two options across all three frames, per item) between a **unification**
  paraphrase ("the three days formed one continuous stretch, beautiful as a whole") and a
  **distributive** paraphrase ("each of the three days was individually beautiful").
- **Counterbalance:** A/B letter assignment of the two paraphrase options counterbalanced across
  items (frozen `fc_letter_unification` ∈ {A,B}; half/half, seeded). `analyze.py` reads the
  *content* choice (unification vs distributive), not the letter.
- **Paraphrase-option lexical-overlap parity (inherited Condition I2, UNCHANGED):** neither of the
  two **paraphrase options** may share more surface content words (lemma-level, stopwords removed)
  with the premise than the other. Per-item overlap counts recorded in `stimuli.json`
  (`lexical_overlap.unification`, `lexical_overlap.distributive`); parity (equal, or within frozen
  tolerance 1 with direction flagged) asserted mechanically in `prep.py`. **This is the parity that
  stays in force per Condition N3** — it concerns the two *options*, not the premise frames.
- **Indicator (per frame):** P(unification | frame). The headline is the **double contrast** built
  from these (§4); raw rates are descriptive only.
- **Under-pressure subset (inherited Condition I4):** the DDC is *itself* the under-pressure
  condition by construction (its default reading is distributive). Additionally, a pre-declared
  subset (`local_fluency: "distributive"`) is authored where even within the AANN frame the
  distributive paraphrase is the locally-fluent continuation; that subset's double contrast is
  analysed **separately** from the full-set headline.

### 3.2 Arm B — entailment NLI (convergent robustness)

- **Same three premise frames** (AANN, DDC, LCC).
- **Hypotheses**, in the house NLI affirm/withhold framing:
  1. **singularity / unification** — "the stay was a single continuous stretch" (affirm for AANN);
  2. **whole-evaluation** — "the stretch as a whole was beautiful" (affirm) vs the distributive foil
     "each day individually was beautiful" (the construction does not *entail* the distributive
     reading; the foil is the contrast, not a target affirm).
- **Indicator (per frame):** affirm rate on the unification / whole-evaluation hypotheses; the
  headline is again the **double contrast** (§4). NLI's known Gricean permissiveness (NLI admits
  post-hoc readings FC's strict framing withholds —
  [`result/caused-motion-near-miss-v2c`](../../wiki/findings/results/caused-motion-near-miss-v2c.md))
  is exactly why B is convergent, not headline; the double-contrast design subtracts both the DDC
  baseline and the lexical-cue contribution.

### 3.3 Re-justification of inherited Condition 2 (the amended minimal-pair / overlap-parity clause)

Inherited Condition I2 required the indicator to be an AANN-vs-control **shift** with the control a
**lexically-matched minimal pair** (the bare plural *three beautiful days*). v4 **breaks the
minimal-pair property by design**: the DDC differs lexically from the AANN premise (it imports
"on each of", "day by day"), so a raw AANN-vs-DDC shift could be a **lexical-cue artifact** rather
than evidence the AANN *licenses* unification. The decision (Condition N2) authorizes this break
**only** with two guardrails, both implemented here:

- **(a) The lexical-cue control arm (LCC, §3.1/3.2) operationalizes the artifact worry as a measured
  subtraction**, not an assertion. The headline is the **double contrast** Δ² (§4): AANN-vs-DDC
  *minus* LCC-vs-DDC. If the lexical cue alone (LCC) moves the reading as much as the AANN does, Δ²
  → 0 and the paraphrase arm is a LEXICAL-CUE ARTIFACT (§6) — disqualified from the headline. This
  is exactly the structural bias *against a free positive* the ratification demands.
- **(b) The per-item control-premise lexical asymmetry is quantified, not waived (Condition N3).**
  Each item records `control_lexical_delta` in `stimuli.json` — the count of content words the DDC
  adds/removes relative to the AANN premise — and the LCC is authored to carry the **same** delta
  (the LCC is the DDC's lexical cue grafted onto a non-AANN plural, so its cue-content matches). The
  *paraphrase-option* parity (§3.1) is untouched and stays in force. The amendment is therefore:
  the *premises* are no longer minimal pairs, but the *interpretable contrast* is restored to a
  construction-isolating one by the double subtraction. This re-justification is the v4 design's
  written answer to Condition N3 and is checked by the pre-run critic.

### 3.4 Arm — agreement sub-probe (the LOAD-BEARING discriminator; control = BARE PLURAL, Condition N4)

The grammaticalized singular/plural reflex: the AANN phrase takes **singular** agreement despite a
plural noun head. **Per binding Condition N4, this sub-probe's control stays the BARE PLURAL**
*three beautiful days* — **not** the distributive-default control. (The DDC's itemizing frame would
contaminate the agreement contrast with overt distributive morphology; the clean grammaticalized
reflex is the AANN-vs-bare-plural pairing v3 already used, where v3 found the only off-ceiling
positive: gpt-5.4-mini +0.739, control *was*-rate 0.22 — ample headroom, quoted from the v3 result,
not re-derived.)

- **Items:** *A beautiful three days ___ what we needed* (AANN → singular **was**) vs *Three
  beautiful days ___ what we needed* (bare-plural control → plural **were**). Forced-choice
  was/were, counterbalanced (frozen `agr_letter_was` ∈ {A,B}).
- **Indicator:** **P(was | AANN) − P(was | bare-plural control)** = the singular-agreement **shift**
  (a single contrast, *not* the double contrast — the bare plural is the right control here because
  singular agreement on a plural head is *distributionally dispreferred*, so the distributional
  story predicts the *opposite* of the inferential story; no lexical-cue control is needed or
  wanted).
- **Why load-bearing:** it is the one place the distributional-shadow story predicts the opposite of
  the inferential story. Reported **separately** and weighted **above** the paraphrase arm.

### 3.5 Headline-gating rule (inherited Condition I3 / N4, frozen)

If Arm A's **double-contrast** Δ² is positive (passes §4 threshold) **but the agreement shift is
null** (does not pass), the headline is **"shift in paraphrase selection WITHOUT the grammaticalized
reflex"** — **not** "draws the unification inference." Only when the agreement shift is *also*
positive may the headline read: *the construction shifts inferential behaviour, including the
grammaticalized singular reflex, relative to a matched control, in the direction the published
semantics predicts.* Baked into `analyze.py` `headline()`.

### 3.6 Disputed-coding flagging (inherited Condition I6)

Any item whose unification/distributive key the AANN-semantics literature does not clearly settle is
flagged item-level (`key_disputed: true`, with a one-line reason). The double-contrast headline is
computed **both** on all items **and** on the non-disputed subset; if the verdict category differs,
a mandatory caveat attaches. Items where world-knowledge *alone* forces the unification reading are
excluded at authoring time so the shift cannot be a world-knowledge artifact.

### 3.7 Tier-0 manipulation check (inherited Condition I7)

A pre-declared can't-fail sanity arm: the AANN **well-formed vs ill-formed** forced choice reused
from v2/v2b/v3 (the 4 Mahowald degenerate variants `reverse_mods`, `no_mod`, `no_plural`, `no_a`),
AANN position counterbalanced. **Pass: ≥ 20/24 AANN-preferred per model** (the v2/v2b/v3 bar).
**Pre-declared failure consequence:** a model failing Tier-0 has its inference numbers reported as
**instrument failure** — its shift/headline reported descriptively and **excluded** from the
cross-model count; never reinterpreted as a substantive inference result. If fewer than 2 models
pass Tier-0, the v4 verdict is **INSTRUMENT FAILURE**.

## 4. Analysis — the double-contrast headline statistic, threshold, convergence

Per model, per arm (A primary, B convergent), the design computes from the three frame rates:

- **AANN shift** = P(unification | AANN) − P(unification | DDC). (How much the construction moves
  the reading off the distributive default.)
- **Lexical-cue shift** = P(unification | LCC) − P(unification | DDC). (How much the *lexical cue
  alone* moves a matched non-AANN string off the distributive default.)
- **Double contrast Δ²** = (AANN shift) − (lexical-cue shift) = **the headline statistic.** This is
  the construction's contribution *net of* the lexical cue. Δ² > 0 means the AANN shifts toward
  unification **more** than the cue alone does.

**Frozen threshold τ = +0.20** (a 20-percentage-point net double-contrast shift), inclusive
(≥ +0.20 passes), with a **10,000-resample item-level bootstrap 95% CI on Δ²** whose **lower bound
must exceed 0** for a "positive" double contrast. τ is **reused from v3 unchanged** (a net shift
smaller than 20 pp on a binary forced choice is not distinguishable from counterbalancing/labelling
noise at this item count); it is fixed before any model output exists (Condition I8). Reusing v3's
τ rather than loosening it keeps the design biased against a free positive, as the ratification
demands; the bootstrap is now on the *difference of differences*, which is *more* conservative than
v3's single difference (wider CI for the same item count), so the bar is, if anything, harder — this
is deliberate and is **not** a retuning toward a positive.

- **Agreement shift** (load-bearing, §3.4) = P(was | AANN) − P(was | bare-plural control); same
  τ = +0.20 with bootstrap-CI-lower > 0. (Single contrast — see §3.4.)
- **Named disagreement statistic** **|FC Δ² − NLI Δ²|** per model — reported, fed to
  [`open-question/instrument-sensitivity-constructional-inference`](../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md),
  **never averaged away** (flag ≥ 0.30, the mid-band of the ≤50 pp in-repo bound).

## 5. Headroom-precondition gate (Condition N1) — checked PRE-HEADLINE, per model

**This gate runs and is read BEFORE any AANN contrast is interpreted.** It is the pre-registered
manipulation/sanity check that the v3 ceiling cause has actually been removed:

> **Gate:** for each model, the **DDC baseline unification rate** — P(unification | DDC) on the
> primary paraphrase arm — must be **materially off-ceiling**: **target ≤ 0.30**, **hard ceiling
> ≤ 0.50**.

- If P(unification | DDC) ≤ 0.30 for a model: PASS — the control reads distributive at baseline, the
  AANN has headroom to shift, the model's double contrast is interpreted.
- If 0.30 < P(unification | DDC) ≤ 0.50: MARGINAL — interpreted only with a mandatory
  reduced-headroom caveat attached to that model's number; counts toward the cross-model verdict
  only if Δ² clears τ with CI-lower > 0 *and* the caveat is carried.
- If P(unification | DDC) > 0.50 for a model: **HEADROOM-FAIL** — the DDC still reads unification at
  (or near) ceiling, the v3 cause is **not** removed for this model, and **the design has not
  achieved its purpose.** The model's paraphrase/NLI numbers are reported descriptively as
  *headroom-failed* and **excluded** from the substantive headline.
- **Whole-design gate:** if **fewer than 2 of 3 models** clear the headroom precondition (PASS or
  MARGINAL), the v4 paraphrase/NLI headline **must not be interpreted at all** → the design routes
  to the **Option-B NAMED NULL** (§6, §8): record that no distributive-default control could be
  built that gives the construction headroom at this instrument, and redirect inferential effort to
  the cancel-direction (conative) route.

The NLI arm carries an analogous DDC-baseline check (affirm rate on the unification hypothesis for
the DDC ≤ 0.30 target / ≤ 0.50 ceiling), reported alongside but not gating the *primary* (paraphrase)
headline, which the FC gate governs.

## 6. Verdict map (over Tier-0-passing, headroom-clearing models)

Per model (paraphrase arm primary), after the §5 headroom gate:

- **CONVERGENT-POSITIVE:** Δ² (FC) ≥ τ (CI-lo > 0) **AND** Δ² (NLI) ≥ τ (CI-lo > 0) **AND** agreement
  shift ≥ τ (CI-lo > 0), with the model clearing the headroom precondition. Headline: "the
  construction shifts inferential behaviour, including the grammaticalized singular reflex, relative
  to a matched control, in the direction the published semantics predicts."
- **PARAPHRASE-ONLY:** Δ² (FC) ≥ τ but the **agreement** shift is null. Headline (Condition I3/N4):
  "shift in paraphrase selection WITHOUT the grammaticalized reflex" — **not** "draws the unification
  inference."
- **LEXICAL-CUE ARTIFACT (new in v4, Condition N2):** the **AANN shift** ≥ τ **but Δ² < τ** (or its
  CI straddles 0) **because the lexical-cue shift accounts for it** — i.e. P(unification | LCC) moves
  as much as P(unification | AANN) off the DDC baseline (operationally: AANN shift ≥ τ **and**
  lexical-cue shift ≥ (AANN shift − τ), so the net Δ² fails). The paraphrase arm is declared a
  **lexical-cue artifact** for that model: the measured movement is attributable to the imported
  itemizing cue, **not** to the AANN construction. It **cannot carry the headline** and is reported
  as such.
- **INSTRUMENT-DISAGREEMENT:** |FC Δ² − NLI Δ²| ≥ 0.30 — a mandatory per-model instrument-fragility
  caveat, fed to the instrument-sensitivity open question, regardless of category.
- **NULL:** Δ² (FC) < τ or its CI straddles 0, and the lexical-cue-artifact condition does not apply
  (i.e. the AANN simply did not move the reading off the distributive default).

**v4 overall verdict (over Tier-0-passing, headroom-clearing models):**

- **SUPPORTED (inferential half):** ≥ 2 models CONVERGENT-POSITIVE.
- **PARTIAL (paraphrase-without-reflex):** ≥ 2 models PARAPHRASE-ONLY but < 2 CONVERGENT-POSITIVE —
  a `constructional`-shift-without-the-grammaticalized-reflex finding.
- **LEXICAL-CUE ARTIFACT:** ≥ 2 models LEXICAL-CUE ARTIFACT — the apparent shift is the imported
  cue, not the construction; the paraphrase arm carries no inferential headline. A first-class
  (and disciplined) outcome: the double contrast did its job.
- **NULL:** < 2 models reach even PARAPHRASE-ONLY (and not a lexical-cue artifact) — the construction
  does not shift inferential behaviour relative to the distributive-default control at this
  instrument; a first-class null.
- **HEADROOM-FAIL → OPTION-B NAMED NULL (Condition N1/N6):** < 2 models clear the headroom
  precondition — the design did not remove the v3 cause; record the inferential half as terminally
  untestable-at-paraphrase-instrument for AANN and **redirect to Option B** (the cancel-direction /
  conative route), per the decision's binding fallback (§8).
- **INSTRUMENT FAILURE:** < 2 models pass Tier-0.

Every outcome, including every null and the lexical-cue-artifact and headroom-fail outcomes, is a
first-class result. No threshold is retuned post-hoc.

## 7. Anchor (Condition N5 / inherited I5)

The v4 result will carry **`anchor: internal-contrast-only`** — its force is the **within-model
double contrast** (does the construction shift paraphrase choice / entailment behaviour / agreement
*net of the lexical cue*, relative to a distributive-default control). **No human-comparison claim
is made.** This terminal state carries forward from the governing decisions; no human AANN-inference
data exists and this ratification cannot change that. (Per CLAUDE.md, the `internal-contrast-only`
state for the AANN inferential line was ratified by
[`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md)
and reaffirmed by [`decisions/resolved/aann-inferential-default-coincidence`](../../wiki/decisions/resolved/aann-inferential-default-coincidence.md);
precedent [`decisions/resolved/conflicting-cue-human-anchor`](../../wiki/decisions/resolved/conflicting-cue-human-anchor.md).)

[`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md) is
linked **only as stimulus-class provenance** (the AANN measure-noun inventory and templates the
items reuse) and as the v2 gradient anchor — **never** as the inference anchor. Mahowald's MTurk
data are 1–10 *acceptability* ratings; no human there was asked the unification-vs-distributive
question, so reusing it as an inference anchor would be the category error the governing decision
explicitly blocks.

The expected-inference **key** (unification = the AANN-licensed reading; distributive = the DDC's
baseline reading) is **EXPERT-STIPULATED**: the design author's coding of the published AANN
semantics — the unification/whole-evaluation analysis the conjecture page describes and the
constraint literature names (**Solt 2007** on unit-coercion; **Dalrymple & King 2019**;
**Bylinina & Nouwen 2018**). **These papers are not in-repo; they are named only as the analyses
the stipulation rests on, exactly as v3 and the decision page name them — no quotes are fabricated
from them.** The key is a *scoring key*, not a behavioral-human anchor, labelled expert-stipulated
on this design, in `stimuli.json`, and on the eventual result page.

**Chief-cost statement (verbatim, binding on the result page, adapted to v4 per Condition N5):**
*the v4 can never say models draw the inference the way humans do — only that the construction
shifts inferential behaviour relative to a matched control, in the direction the published
semantics predicts.*

## 8. Named-null fallback to Option B (Condition N6, binding)

If **at design or independent-pre-run-critic time** no distributive-default control can be built
that satisfies Conditions N1 (a credible off-ceiling baseline) and N2 (a matched lexical-cue control
that makes the double contrast interpretable) — for example, if the pre-run critic judges that every
DDC frame either (a) cannot plausibly read distributive at baseline for these models, or (b) imports
a lexical cue that cannot be cleanly matched by a non-AANN LCC — then **the design must not run.**
The disciplined outcome is to record the AANN inferential half as **terminally
untestable-at-paraphrase-instrument**, and **redirect inferential effort to Option B**: the
**cancel-direction / conative route**, where the construction must *suppress* a lexically-default
entailment and the inference *can* be separated from the default because the default points the
other way (the precedent
[`result/conative-minimal-pair-divergence-v1`](../../wiki/findings/results/conative-minimal-pair-divergence-v1.md)
shows that route works). This is the decision's own Option-A fallback trigger and the v3 template's
named-null discipline. The same redirect is the verdict-map outcome if the run proceeds but
**HEADROOM-FAIL** fires post-hoc (§6).

## 9. Pre-flight cost (config/budget.md)

**This estimate is for a run that has NOT happened. No model calls have been made.** Geometry
(to be frozen in `stimuli.json` by `prep.py`): a v3-comparable base item count (~**23**: temporal
~13 / distance ~10). The structural change from v3 is the **added third premise frame (LCC)** on the
paraphrase and NLI arms (the agreement arm and Tier-0 are unchanged — agreement keeps the bare-plural
control only, per N4).

Per model, on the same per-call shape as v3 (single-token FC/NLI picks, ~80 tok in / ~8 out):

| Arm | v3 frames | v4 frames | v3 calls/model | v4 calls/model |
|---|---|---|---|---|
| A paraphrase FC | AANN, control (2) | AANN, DDC, LCC (3) | 46 | 23 × 3 = **69** |
| B NLI (2 hyps) | AANN, control (2) | AANN, DDC, LCC (3) | 92 | 23 × 2 × 3 = **138** |
| Agreement FC | AANN, bare-plural control (2) | unchanged (2) | 46 | **46** |
| Tier-0 | — | unchanged | 24 | **24** |
| **Per model** | | | **208** | **277** |

**v4 total ≈ 277 calls/model × 3 = ~831 calls** (vs v3's 624). The added LCC arm raises per-model
calls by ~33% (the paraphrase + NLI arms each gain one frame; the two single-contrast arms are
unchanged).

**Pre-flight dollar estimate from v3's measured billed rate.** v3 ran **624 calls for $0.0910
billed** = **$0.0001458 per call** (billed `usage.cost`, the ~4.5× rate-card undercount already
absorbed since this is billed, not rate-card). At the same per-call shape and rate, **831 calls ≈
831 × $0.0001458 ≈ $0.121 billed** (point estimate). Allowing for the one verbatim retry per
unparseable response and variance, **expected ≈ $0.12–0.20 billed**. This lands **well under $1**
and **well under the $5.00/day UTC budget cap** ([`config/budget.md`](../../config/budget.md));
it is **not** flaggable as a >$1 run at this geometry. A single-run **ABORT_USD = $0.50** flag is to
be coded in `probe.py` (as in v3), well under the day cap. The pre-flight estimate is recorded here
per CLAUDE.md rule 8; the actual billed `usage.cost` would be recorded in the run record **after**
the later, post-critic run — **which has not occurred.**

## 10. Run protocol (later session, after a fresh pre-run-critic GO)

1. `prep.py` (no model calls) authors and freezes `stimuli.json`: base items, the three premise
   frames per item (AANN, DDC, LCC), paraphrase options + option-parity counts, NLI hypotheses,
   was/were pairs (bare-plural control), counterbalancing, per-item `control_lexical_delta`,
   expert-stipulated key, `key_disputed` flags, `local_fluency` direction, Tier-0 pairs.
2. A **fresh independent pre-run critic** (not this design's author/orchestrator) reviews this design
   + `PREREG.md` + `stimuli.json` before any call. It checks specifically: that the DDC plausibly
   reads distributive at baseline (the N1 precondition is *buildable*); that the LCC cleanly matches
   the DDC's lexical cue without the AANN (N2); that paraphrase-option parity holds (N3); that the
   agreement control is the bare plural (N4); anti-cheat. The orchestrator freezes `PREREG.md` only
   after a **GO**. A **NO-GO on N1/N2 buildability triggers the Option-B fallback (§8)**, not a run.
3. `probe.py`: all calls via [`experiments/lib/openrouter.py`](../lib/openrouter.py)
   (`usage: include`); refuses to run without `PREREG.md` and `analyze.py`; per-slot max_tokens +
   gemini `reasoning:{effort:"minimal"}`; one verbatim retry per unparseable response then missing;
   billed-cost logging; ABORT_USD flag.
4. `analyze.py` computes exactly the §4–§6 statistics with frozen thresholds and the
   headroom-precondition gate + headline-gating + verdict map (incl. LEXICAL-CUE ARTIFACT and
   HEADROOM-FAIL) baked in; an independent post-run verifier recomputes every number from raw before
   the result page is written.
5. Result page (later session, post-run) `wiki/findings/results/aann-inferential-v4.md`,
   `anchor: internal-contrast-only`, carrying the §7 chief-cost statement verbatim.

## 11. What this design does not do

No human-comparison claim anywhere (Condition N5/I5). No raw-AANN-rate headline (Condition I2 as
amended — the headline is the double contrast Δ²). No post-hoc instrument selection (I1) or
threshold retuning (I8) — τ is reused from v3, the bootstrap is *more* conservative, not less. No
Option-C generation-and-code arm (demoted by the prior decision). No reuse of Mahowald's
acceptability ratings as an inference anchor. The agreement sub-probe's control stays the bare
plural, not the distributive-default control (N4). And it **has not run**: no model calls, no frozen
stimulus set, no run directory — the probe may run only after a fresh independent pre-run critic
GO on this design + a frozen PREREG + stimuli. It does not, and cannot, claim the model draws the
inference *the way humans do*.
