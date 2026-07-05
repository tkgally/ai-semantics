---
type: result
id: aann-inferential-v4
title: AANN inferential v4 — with a distributive-default control that finally gives the construction headroom, the AANN shifts unification paraphrase-selection in all three models (net of the lexical cue), converging across paraphrase + NLI + the grammaticalized agreement reflex in ONE model (gpt-5.4-mini); PARTIAL
meaning-senses:
  - constructional
  - inferential
  - distributional
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-13
updated: 2026-07-05
links:
  - rel: refines
    target: conjecture/aann-construction
  - rel: refines
    target: theory/constructional-meaning-in-llms
  - rel: refines
    target: result/aann-inferential-v3
  - rel: depends-on
    target: design/aann-construction-v4-inferential
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: supports
    target: open-question/distributional-vs-inferential-constructional
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: supports
    target: claim/preference-commitment-dissociation-aann-specific
---

# Result: AANN inferential probe v4 — PARTIAL (a real construction shift, convergent in one model)

> **Anchor: `internal-contrast-only`** (within-model double contrast; **no human-comparison
> claim**), the terminal state carried forward from the governing decisions
> ([`decisions/resolved/aann-inferential-default-coincidence`](../../decisions/resolved/aann-inferential-default-coincidence.md),
> [`decisions/resolved/aann-inferential-operationalization`](../../decisions/resolved/aann-inferential-operationalization.md)).
> **Chief-cost statement (verbatim, binding):** *the v4 can never say "models draw the inference
> the way humans do" — only that the construction shifts inferential behaviour relative to a
> matched control, in the direction the published semantics predicts.* The expected-inference key
> (unification = AANN-licensed) is **EXPERT-STIPULATED** (Solt 2007 unit-coercion; Dalrymple &
> King 2019; Bylinina & Nouwen 2018, named not quoted, not in-repo), a scoring key, **not** human
> judgment data.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The "small N (23 base items), single
> run, single date" caveat below was discharged by the powered replication
> [`result/aann-inferential-v6`](aann-inferential-v6.md) (2026-06-14; 40 fresh held-out adjectives,
> identical instrument — the PARTIAL replicates cell-for-cell). The dissociation this page surfaced
> (paraphrase preference without NLI commitment) was later promoted, with its conative
> non-reproduction, to [`claim/preference-commitment-dissociation-aann-specific`](../claims/preference-commitment-dissociation-aann-specific.md).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

The second attempt at the **inferential half** of [`conjecture/aann-construction`](../conjectures/aann-construction.md),
redesigned to remove the named cause of the v3 null. v3
([`result/aann-inferential-v3`](aann-inferential-v3.md)) returned a **ceiling-bounded NULL**: the
AANN-vs-control shift could not be measured because the **bare-plural control already read as a
unified evaluated stretch nearly every time** (control unification rates 0.78 / 0.96 / 1.00), so the
construction had no headroom to move the reading. v4's single structural change, per the ratified
[`decisions/resolved/aann-inferential-default-coincidence`](../../decisions/resolved/aann-inferential-default-coincidence.md)
(Option A): replace the ceiling-pinned bare-plural control with a **distributive-default control
(DDC)** whose baseline reading is genuinely distributive, and add a **lexical-cue control (LCC)** arm
so the headline is a **double contrast** Δ² = P(uni|AANN) − P(uni|LCC) — the construction's shift
*net of* the imported itemizing cue.

Frozen design: [`design/aann-construction-v4-inferential`](../../../experiments/designs/aann-construction-v4-inferential.md).
PREREG, raw data, the analysis-correction note, and run log:
[`experiments/runs/2026-06-13-aann-inferential-v4/`](../../../experiments/runs/2026-06-13-aann-inferential-v4/README.md).
831 calls, **$0.1266 billed**, **0 missing in every arm** (0 missing-cost calls). A **fresh
independent pre-run critic returned GO** (all six new + eight inherited conditions PASS; anti-cheat
PASS; analyze.py fidelity PASS; 23/23 items buildable). An **independent post-run verifier recomputed
every number from raw** — paraphrase / headroom / agreement / Tier-0 / cost: **0 mismatches** — and
**caught a load-bearing NLI-aggregation bug** in `analyze.py`, fixed to the frozen spec and re-run
(see *The NLI analysis correction* below; raw data unchanged).

## Headline (pre-registered verdict: PARTIAL)

**The distributive-default control worked: the v3 ceiling cause is removed.** The DDC reads
distributive at baseline for all three models (P(uni|DDC) = 0 / 0.22 / 0 — the N1 headroom gate
PASSES for every model, where v3's bare-plural control sat at 0.78–1.00). Against that control, **the
AANN shifts paraphrase selection toward unification in all three models**, by a large margin net of
the lexical cue (double-contrast Δ² = +0.78 / +0.70 / +0.96, every CI clear of 0 and τ=+0.20). This
is a positive that v3 could not even reach.

**But the construction's inferential signal converges across instruments in only one model.** In
**gpt-5.4-mini** the shift shows up on the paraphrase double contrast **and** the NLI entailment
double contrast **and** the grammaticalized singular-agreement reflex (CONVERGENT-POSITIVE — the
strongest single-model AANN inferential signal the project has produced). In **claude-sonnet-4.6**
and **gemini-3.5-flash** the paraphrase shift is **not** matched by NLI (does not clear the bar) or
by the agreement reflex (at ceiling, uninformative) — PARAPHRASE-ONLY. With **<2 models
CONVERGENT-POSITIVE** but **≥2 showing the paraphrase shift**, the frozen verdict map returns
**PARTIAL**.

| Per model (all Tier-0 + headroom PASS) | A claude-sonnet-4.6 | B gpt-5.4-mini | C gemini-3.5-flash |
|---|---|---|---|
| Headroom P(uni\|DDC) (PASS ≤0.30) | 0 · PASS | 0.217 · PASS | 0 · PASS |
| **Paraphrase Δ²** (PRIMARY; τ=+0.20, CI-lo>0) | **+0.783** CI[0.61,0.91] · **POS** | **+0.696** CI[0.52,0.87] · **POS** | **+0.957** CI[0.87,1.0] · **POS** |
|  — raw P(uni), AANN / DDC / LCC | 0.913 / 0 / 0.130 | 1.00 / 0.217 / 0.304 | 1.00 / 0 / 0.043 |
|  — under-pressure subset Δ² (n=10) | +0.90 | +0.70 | +1.00 |
| NLI Δ² (convergent; both-hyp, corrected) | +0.152 CI[0,0.33] · not pos | **+0.261** CI[0.07,0.46] · **POS** | −0.087 CI[−0.22,0.04] · not pos |
|  — raw affirm, AANN / DDC / LCC | 0.652 / 0.478 / 0.500 | 0.717 / 0.565 / 0.457 | 0.761 / 0.630 / 0.848 |
| **Agreement shift** (load-bearing discriminator) | 0 · not pos (ceiling) | **+0.652** CI[0.43,0.87] · **POS** | 0 · not pos (ceiling) |
|  — raw "was" rate, AANN / bare-plural ctrl | 1.00 / 1.00 | 0.957 / 0.304 | 1.00 / 1.00 |
| \|FC Δ² − NLI Δ²\| (flag ≥0.30) | 0.630 (flag) | 0.435 (flag) | 1.044 (flag) |
| **Category (PREREG §6)** | **PARAPHRASE-ONLY** | **CONVERGENT-POSITIVE** | **PARAPHRASE-ONLY** |

**Verdict: PARTIAL — a paraphrase-level constructional shift in all three models, converging to a
full cross-instrument inferential shift in one (gpt-5.4-mini).**

## What the result is, and what bounds it

**1. The methodological win: v4 removed the v3 ceiling, and the removal is the substantive
finding.** The whole point of the redesign was to engineer a control that reads *distributive* at
baseline so the construction would have somewhere to shift the reading. It worked cleanly: on the
primary forced-choice paraphrase instrument the DDC unification rate is 0 / 0.22 / 0 — far off the
v3 control's 0.78–1.00 ceiling. So where v3 had to report "untestable at this instrument (the
inference and the default coincide)," v4 can report a **measured construction effect**: holding the
distributive baseline fixed and subtracting the lexical cue, the AANN moves paraphrase selection
toward the unification reading by +0.70 to +0.96 in every model. The double contrast also clears the
**lexical-cue-artifact** bar by a wide margin (the LCC, which carries the same "on each of the
N … days" itemizing cue **without** the AANN, stays near the distributive floor: 0.130 / 0.304 /
0.043), so the shift is the **construction's**, not the imported cue's.

**2. Why PARTIAL, not SUPPORTED — the instrument and the reflex do not converge for two of three
models.** The construction's effect on the *primary* (forced-choice paraphrase) instrument is
uniform and large; its effect on the *convergent* (NLI entailment) instrument and on the
*load-bearing* (grammaticalized agreement) discriminator is **model-specific**:
- **gpt-5.4-mini — CONVERGENT-POSITIVE.** All three signals fire: paraphrase Δ² +0.70, NLI Δ²
  +0.26 (CI-lo 0.065), agreement shift +0.65 (it picks singular *was* for the AANN at 0.96 but
  plural *were* for the bare-plural control, 0.30 *was*). This is the one place the
  distributional-shadow story predicts the *opposite* of the inferential story (singular agreement
  on a plural head is distributionally dispreferred), and the construction moves it. The
  grammaticalized reflex **replicates v3** (v3: +0.74; v4: +0.65). Under the pre-registered
  headline-gating, gpt-5.4-mini earns the full headline: *the construction shifts inferential
  behaviour, including the grammaticalized singular reflex, relative to a matched control, in the
  direction the published semantics predicts.*
- **claude-sonnet-4.6 and gemini-3.5-flash — PARAPHRASE-ONLY.** The paraphrase shift is large
  (+0.78, +0.96) but the NLI double contrast does not clear the bar (claude +0.15 with CI touching
  0; gemini −0.09 — it actually affirms the unification hypothesis slightly *more* for the
  lexical-cue control than for the AANN), and the agreement reflex is **flat at ceiling** (both pick
  singular *was* for the AANN **and** the bare-plural control, so the contrast has no room to show —
  exactly as in v3). The pre-registered headline-gating is decisive and earns its keep here: a
  paraphrase shift **without** the agreement reflex is recorded as *"shift in paraphrase selection
  without the grammaticalized reflex,"* **not** *"draws the unification inference."*

So for claude and gemini the honest reading is: the construction shifts which paraphrase they
**prefer** under a forced exclusive choice, but this does **not** carry over to an entailment
commitment (NLI) or to the grammaticalized reflex — consistent with the construction moving a
graded *paraphrase preference* (a distributionally-compatible pick) rather than licensing a robust
*inference*. For gpt-5.4-mini it does carry over, on every instrument including the one a
distributional account cannot easily fake.

**3. The instrument disagreement is large and is itself a finding (not a ceiling artifact).** The
named |FC Δ² − NLI Δ²| statistic is flagged for every model (0.63 / 0.43 / 1.04) — the **largest
forced-choice-vs-NLI disagreement in the project's record**, sharpening
[`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md).
The forced-choice paraphrase instrument (pick the *better* of two paraphrases) registers the
construction effect cleanly in all three models; the NLI entailment instrument (is the unification
hypothesis *true* given the premise?) registers it only in gpt. Crucially — after the NLI analysis
correction below — this is **not** a ceiling effect: the both-hypothesis DDC affirm rates are
**off-ceiling** (0.48 / 0.57 / 0.63), so NLI had headroom; the two instruments genuinely diverge,
with the exclusive forced choice more sensitive to the construction than the permissive entailment
judgment. This is the same FC-vs-NLI axis the project has tracked since the conative, now at its
sharpest.

## The NLI analysis correction (independent post-run verifier)

Transparency note, because it changed one model's category. The independent post-run verifier
reproduced paraphrase / headroom / agreement / Tier-0 / cost / missingness with **0 mismatches**, and
**caught a real bug** in `analyze.py`: the NLI arm's frame-splitter used a plain dictionary
assignment, so with **two** NLI hypothesis rows per item (`unification_hyp` + `whole_eval_hyp`) the
second silently overwrote the first, leaving the reported NLI Δ² reflecting the
**whole-evaluation hypothesis only**. The **frozen** indicator (design §3.2/§4; PREREG) is the
**both-hypothesis** affirm rate. The fix — item-level mean over both hypotheses (identity for the
single-row paraphrase arm) — corrects the code **to the pre-registered spec**; it is **not** a
threshold retune, the fix direction was dictated by the freeze and independently confirmed by the
verifier, and the **raw data is unchanged** (no re-run). Effect: the buggy whole-eval-only NLI was
null for all three models; the spec-faithful both-hypothesis NLI is positive for **gpt-5.4-mini**
(Δ² +0.26, CI-lo 0.065), moving it to CONVERGENT-POSITIVE. The **overall PARTIAL verdict is
unchanged** (claude and gemini still have null agreement reflexes, so <2 models converge). The NLI
conclusion is therefore *contingent on the both-hypothesis aggregation* the PREREG fixed — and that
contingency is verdict-relevant for exactly one of three models (gpt's per-model category), not for
the overall verdict.

## Disputed-coding sensitivity (Condition I6)

One item carried a `key_disputed` flag (the yards inventory-edge item, carried over from v3).
Recomputing the paraphrase double contrast excluding it changes no model's category
(`category_changes: false`).

## Relation to the conjecture and the theory

- The **productive-gradient** half of [`conjecture/aann-construction`](../conjectures/aann-construction.md)
  stays SUPPORTED (v2). This result bears on the **inferential** half, and it moves it from v3's
  **"untestable at this instrument (ceiling)"** to **"detectable and partially convergent."** The
  inferential clause is now **partially supported**: the construction demonstrably shifts inferential
  behaviour relative to a headroom-bearing control, **fully (cross-instrument) in one of three
  models** and **at the paraphrase level in the other two**. It is **not** SUPPORTED outright (no
  ≥2-model convergence) and **no longer a clean null**. Any reading of the conjecture's inferential
  clause as established across the panel stays unsupported.
- Within the evidence ladder of [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
  *(Superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
  — cited here as the edition this page engaged.)*,
  this is the AANN line's first **Tier-4 (inference-licensing)** signal that clears its bar — but
  only for gpt-5.4-mini, and with the standing caution that a forced-choice paraphrase preference is
  weaker evidence than a converging NLI + agreement shift. It reinforces the recurring AANN pattern
  (strong on *form*; the *inferential use* is real but uneven across models and instruments) while
  finally putting a measured, non-ceiling number on the inferential arm.

## Bounds (binding on any reading of this result)

- **No human-comparison claim** (anchor `internal-contrast-only`). The chief-cost statement above is
  binding: this can never say models infer "the way humans do."
- **The paraphrase positive is a paraphrase-*preference* shift.** For claude and gemini, with NLI
  not converging and the agreement reflex at ceiling, read it as "the construction shifts which
  paraphrase is preferred," **not** "the model draws the unification inference." Only gpt-5.4-mini
  earns the stronger reading, and only because all three instruments — including the
  distributionally-dispreferred agreement reflex — converge.
- **claude and gemini agreement is at ceiling, not a failure.** Both pick singular *was* for the
  AANN and the bare-plural control alike, so their flat agreement shift is uninformative (a
  duration-subject singular-agreement tendency), exactly as in v3 — only gpt's control rate (0.30)
  leaves room for the contrast to show.
- **The NLI conclusion is contingent on the both-hypothesis aggregation** the PREREG fixed (see the
  correction note); it is verdict-relevant for gpt's per-model category, not the overall PARTIAL.
- **Expert-stipulated key** (theorists' analyses, not human judgment data); small N (23 base items,
  temporal + distance only); single run, single panel, single date — direction-of-effect, not
  magnitude.
- Two items' DDC/LCC controls carry an authored setting-PP ("of crisis", "at the office") the AANN
  premise lacks; because the PP appears in **both** the DDC and the LCC it cancels in the headline
  Δ² = P(uni|AANN) − P(uni|LCC).

## Provenance

Stimuli are hand-authored, reusing the AANN measure-noun classes from
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) as
**class provenance only** — Mahowald's MTurk data are 1–10 *acceptability* ratings and **cannot** be
the inference anchor (the governing decision blocks that category error). The v3 control rates quoted
above are from [`result/aann-inferential-v3`](aann-inferential-v3.md), verbatim. Independent post-run
verification reproduced every reported number from the raw data (paraphrase / headroom / agreement /
Tier-0 / cost: 0 mismatches) and identified the NLI-aggregation bug that was then fixed to the frozen
spec; 0 missing responses; cost $0.1266 billed (`usage.cost`-summed, 0 missing-cost calls).
