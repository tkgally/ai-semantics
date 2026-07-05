---
type: result
id: aann-inferential-v6
title: AANN inferential v6 — powered panel replication of v4 on 40 fresh held-out adjectives REPLICATES the PARTIAL result; the paraphrase double-contrast shift holds in all three models, and gpt-5.4-mini's cross-instrument convergence (paraphrase + NLI + agreement reflex) replicates; PARTIAL
meaning-senses:
  - constructional
  - inferential
  - distributional
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-14
updated: 2026-07-05
links:
  - rel: refines
    target: conjecture/aann-construction
  - rel: refines
    target: theory/constructional-meaning-in-llms
  - rel: refines
    target: result/aann-inferential-v4
  - rel: supports
    target: result/aann-inferential-v4
  - rel: depends-on
    target: design/aann-construction-v6-inferential
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

# Result: AANN inferential probe v6 — PARTIAL (a clean powered replication of v4)

> **Anchor: `internal-contrast-only`** (within-model double contrast; **no
> human-comparison claim**), the terminal state carried forward from the governing
> decisions
> ([`decisions/resolved/aann-inferential-default-coincidence`](../../decisions/resolved/aann-inferential-default-coincidence.md),
> [`decisions/resolved/aann-inferential-operationalization`](../../decisions/resolved/aann-inferential-operationalization.md)).
> **Chief-cost statement (verbatim, binding):** *the v6 can never say "models draw the
> inference the way humans do" — only that the construction shifts inferential
> behaviour relative to a matched control, in the direction the published semantics
> predicts.* The expected-inference key (unification = AANN-licensed) is
> **EXPERT-STIPULATED** (Solt 2007 unit-coercion; Dalrymple & King 2019; Bylinina &
> Nouwen 2018, named not quoted, not in-repo), a scoring key, **not** human judgment
> data.

A **powered panel replication** of [`result/aann-inferential-v4`](aann-inferential-v4.md)
(PARTIAL). v4's binding bounds named its own weakness: *"small N (23 base items),
single run, single panel, single date — direction-of-effect, not magnitude."* v6
attacks that bound with the **same yardstick** and a **fresh, larger item set**:
**40 hand-authored base items** (temporal 20 / distance 20, nearly doubling v4's 23
and rebalancing the distance class) whose **40 adjectives are all held-out** —
mechanically asserted disjoint from v4's 21 *and* the
[`result/aann-agreement-reflex-v5`](aann-agreement-reflex-v5.md) probe's 30 (so a
positive here is the construction *generalizing* to a fresh inventory, not a
re-measurement). The instrument, parsing, four arms, thresholds, headroom gate,
verdict map, and analysis code are **identical to v4** (`analyze.py` byte-identical
save run name / design path / bootstrap seed; the only logic-touching diffs are inside
`--selftest`, verified by the pre-run critic). **No new decision** was opened: v6 runs
under the already-ratified AANN inferential instruments.

Frozen design: [`design/aann-construction-v6-inferential`](../../../experiments/designs/aann-construction-v6-inferential.md).
PREREG, raw data, and run log:
[`experiments/runs/2026-06-14-aann-inferential-v6/`](../../../experiments/runs/2026-06-14-aann-inferential-v6/README.md).
1392 calls, **$0.2138 billed**, **0 missing in every arm** (0 missing-cost calls). A
**fresh independent pre-run critic returned GO** (no BLOCKER/SHOULD-FIX; all 14 binding
conditions PASS; replication fidelity + anti-cheat verified; 40 adjectives verified
held-out; selftest 38 checks). An **independent post-run verifier recomputed every
headline number from raw** with its own code — paraphrase / headroom / NLI / agreement
/ Tier-0 / cost / missingness: **0 mismatches** — and confirmed the v4 NLI-aggregation
bug class is **absent** (the fix was carried forward correctly from the start).

## Headline (pre-registered verdict: PARTIAL — both replication questions answered yes)

**Question 1 — does the panel-wide paraphrase double-contrast shift hold up when
powered? YES.** All three models read the DDC distributive at baseline (P(uni|DDC) =
0 / 0.225 / 0 — N1 headroom PASS for every model), and against that control **all
three shift paraphrase selection toward unification** by a large margin net of the
lexical cue (double-contrast Δ² = **+0.875 / +0.575 / +0.90**, every CI clear of 0).

**Question 2 — does gpt-5.4-mini's cross-instrument convergence replicate? YES.** In
**gpt-5.4-mini** the shift again shows up on the paraphrase double contrast **and** the
NLI entailment double contrast **and** the grammaticalized singular-agreement reflex
(CONVERGENT-POSITIVE). In **claude-sonnet-4.6** and **gemini-3.5-flash** the paraphrase
shift is again **not** matched by NLI or by the agreement reflex (flat at ceiling) —
PARAPHRASE-ONLY. With **<2 models CONVERGENT-POSITIVE** but **all three** showing the
paraphrase shift, the frozen verdict map returns **PARTIAL** — identical to v4.

| Per model (all Tier-0 24/24 + headroom PASS) | A claude-sonnet-4.6 | B gpt-5.4-mini | C gemini-3.5-flash |
|---|---|---|---|
| Headroom P(uni\|DDC) (PASS ≤0.30) | 0 · PASS | 0.225 · PASS | 0 · PASS |
| **Paraphrase Δ²** (PRIMARY; τ=+0.20, CI-lo>0) | **+0.875** CI[0.775,0.975] · **POS** | **+0.575** CI[0.425,0.725] · **POS** | **+0.900** CI[0.80,0.975] · **POS** |
|  — raw P(uni), AANN / DDC / LCC | 0.95 / 0 / 0.075 | 1.00 / 0.225 / 0.425 | 0.975 / 0 / 0.075 |
|  — under-pressure subset Δ² (n=22) | +0.955 | +0.545 | +0.864 |
| NLI Δ² (convergent; both-hyp) | +0.150 CI[0.01,0.28] · not pos | **+0.225** CI[0.08,0.38] · **POS** | −0.025 CI[−0.14,0.09] · not pos |
|  — raw affirm, AANN / DDC / LCC | 0.625 / 0.50 / 0.475 | 0.713 / 0.50 / 0.488 | 0.775 / 0.60 / 0.80 |
| **Agreement shift** (load-bearing discriminator) | 0 · not pos (ceiling) | **+0.60** CI[0.43,0.75] · **POS** | 0 · not pos (ceiling) |
|  — raw "was" rate, AANN / bare-plural ctrl | 1.00 / 1.00 | 0.825 / 0.225 | 1.00 / 1.00 |
| \|FC Δ² − NLI Δ²\| (flag ≥0.30) | 0.725 (flag) | 0.350 (flag) | 0.925 (flag) |
| **Category (PREREG §6)** | **PARAPHRASE-ONLY** | **CONVERGENT-POSITIVE** | **PARAPHRASE-ONLY** |

**Verdict: PARTIAL — a paraphrase-level constructional shift in all three models,
converging to a full cross-instrument inferential shift in one (gpt-5.4-mini). The
v4 PARTIAL result replicates cell-for-cell on a fresh, larger, held-out item set.**

## The replication payoff — v4 vs v6 side by side

The numbers track v4 closely across every load-bearing cell — the point of the
exercise. v6 is a separate run, on a separate UTC date, with **zero adjective overlap**:

| | v4 (N=23) | v6 (N=40, fresh) |
|---|---|---|
| Paraphrase Δ² (A/B/C) | +0.78 / +0.70 / +0.96 | +0.875 / +0.575 / +0.90 |
| Headroom P(uni\|DDC) (A/B/C) | 0 / 0.22 / 0 | 0 / 0.225 / 0 |
| gpt NLI Δ² | +0.26 (pos) | +0.225 (pos) |
| gpt agreement shift | +0.65 | +0.60 |
| claude / gemini NLI | +0.15 / −0.09 (neither pos) | +0.15 / −0.025 (neither pos) |
| claude / gemini agreement | 0 / 0 (ceiling) | 0 / 0 (ceiling) |
| Per-model categories | PARA-ONLY / CONV-POS / PARA-ONLY | PARA-ONLY / CONV-POS / PARA-ONLY |
| Stratum verdict | PARTIAL | PARTIAL |

So the v4 reading is **substantially strengthened**: the construction effect on the
primary paraphrase instrument is now shown to be **stable in magnitude across two
disjoint item sets**, not just a direction-of-effect; the gpt-only cross-instrument
convergence is **not a single-date / small-N artifact** — it replicates including the
distributionally-dispreferred singular-agreement reflex (the one signal a distributional
account cannot easily fake); and the claude/gemini ceiling on the agreement reflex
reproduces on a second, larger sample (a stable duration/distance singular-agreement
tendency, not a failure of the contrast). *[Reconciliation note, s183:
[`result/aann-agreement-reflex-v5`](aann-agreement-reflex-v5.md), run the same day
(2026-06-14), found claude off the ceiling on its temporal held-out items, clearing the
pre-registered bar (+0.333) — v5 reads the ceiling as item-set-bound, and the two pages
measure different (mechanically disjoint) item sets, so the readings do not conflict.]*

## What the result is, and what bounds it

**1. The paraphrase positive is robust and powered.** Where v4 could only claim
"direction-of-effect, not magnitude," v6 shows the double contrast at +0.58 to +0.90
in every model, on 40 fresh held-out adjectives, with bootstrap CIs well clear of 0 and
the lexical-cue control near the distributive floor (P(uni|LCC) 0.075 / 0.425 / 0.075).
The shift is the **construction's**, not the imported itemizing cue's. (gpt's LCC at
0.425 is the highest lexical-cue leakage on the panel — its Δ² is correspondingly the
smallest of the three, but still positive and CI-clear.)

**2. Why PARTIAL, not SUPPORTED — the instrument and the reflex still do not converge
for two of three models.** As in v4: only **gpt-5.4-mini** carries the shift onto the
NLI entailment instrument (Δ² +0.225, CI-lo 0.075) **and** the grammaticalized
agreement reflex (+0.60; it picks singular *was* for the AANN at 0.825 but plural
*were* for the bare-plural control, 0.225 *was*). **claude and gemini are
PARAPHRASE-ONLY** — the NLI double contrast does not clear the bar (claude +0.15;
gemini −0.025 — it again affirms the unification hypothesis slightly *more* for the
lexical-cue control than for the AANN), and the agreement reflex is **flat at ceiling**
(both pick singular *was* for the AANN **and** the bare-plural control). The
pre-registered headline-gating records this as *"shift in paraphrase selection without
the grammaticalized reflex,"* **not** *"draws the unification inference."*

**3. The instrument disagreement is large and replicates as a finding.** The named
|FC Δ² − NLI Δ²| statistic is flagged for every model (0.725 / 0.35 / 0.925), as in v4,
and is **not** a ceiling artifact: the both-hypothesis DDC affirm rates are off-ceiling
(0.50 / 0.50 / 0.60), so NLI had headroom. The exclusive forced-choice paraphrase
instrument is consistently more sensitive to the construction than the permissive
entailment judgment — the same FC-vs-NLI axis the project has tracked since the
conative, now replicated at its sharpest, sharpening
[`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md).

## Disputed-coding sensitivity (Condition I6)

One item carried a `key_disputed` flag (the `freezing forty yards` inventory-edge
item). Recomputing the paraphrase double contrast excluding it changes no model's
category (`category_changes: false`; Δ² excl-disputed +0.872 / +0.590 / +0.923).

## Relation to the conjecture and the theory

- This result **replicates and strengthens** [`result/aann-inferential-v4`](aann-inferential-v4.md)
  and the **inferential** half of [`conjecture/aann-construction`](../conjectures/aann-construction.md).
  The inferential clause stays **partially supported**, now on firmer ground: the
  construction demonstrably shifts inferential behaviour relative to a headroom-bearing
  control — **fully (cross-instrument) in one of three models** and **at the paraphrase
  level in all three** — and the effect is stable across two disjoint, fresh item sets.
  It is still **not** SUPPORTED outright (no ≥2-model cross-instrument convergence) and
  is no longer reachable as a clean null.
- Within the evidence ladder of [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
  *(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
  — cited here as the edition this page engaged.)*,
  this confirms the AANN line's first **Tier-4 (inference-licensing)** signal as a
  replicable, powered effect for gpt-5.4-mini, with the standing caution that a
  forced-choice paraphrase preference is weaker evidence than a converging NLI +
  agreement shift. It reinforces the recurring AANN pattern (strong on *form*; the
  *inferential use* is real but uneven across models and instruments) and removes the
  "single-date / small-N" caveat that bounded v4.

## Bounds (binding on any reading of this result)

- **No human-comparison claim** (anchor `internal-contrast-only`). The chief-cost
  statement above is binding: this can never say models infer "the way humans do."
- **The paraphrase positive is a paraphrase-*preference* shift.** For claude and
  gemini, with NLI not converging and the agreement reflex at ceiling, read it as "the
  construction shifts which paraphrase is preferred," **not** "the model draws the
  unification inference." Only gpt-5.4-mini earns the stronger reading, and only because
  all three instruments — including the distributionally-dispreferred agreement reflex —
  converge.
- **claude and gemini agreement is at ceiling, not a failure.** Both pick singular
  *was* for the AANN and the bare-plural control alike (1.00 / 1.00), so their flat
  agreement shift is uninformative (a duration/distance singular-agreement tendency),
  reproducing v4 on a second sample — only gpt's control rate (0.225) leaves room for
  the contrast to show.
- **Still a single panel, expert-stipulated key.** v6 removes the small-N and
  single-date caveats but **not** the single-panel caveat (same three models) or the
  expert-stipulated-key caveat (theorists' analyses, not human judgment data). The
  measure-noun inventory is temporal + distance only; the object/mass class stays
  dropped.
- Direction and now magnitude are stable across two item sets; this is a within-model,
  within-panel replication, not a human benchmark.

## Provenance

Stimuli are hand-authored, reusing the AANN measure-noun classes from
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
as **class provenance only** — Mahowald's MTurk data are 1–10 *acceptability* ratings
and **cannot** be the inference anchor (the governing decision blocks that category
error). The v4 rates quoted in the comparison table are from
[`result/aann-inferential-v4`](aann-inferential-v4.md), verbatim. Independent post-run
verification reproduced every reported number from the raw data (paraphrase / headroom /
NLI / agreement / Tier-0 / cost / missingness: 0 mismatches); 0 missing responses; cost
$0.2138 billed (`usage.cost`-summed, 0 missing-cost calls).
