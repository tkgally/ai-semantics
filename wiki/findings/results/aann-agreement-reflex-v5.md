---
type: result
id: aann-agreement-reflex-v5
title: AANN agreement-reflex generalization v5 — on fresh held-out items the singular-agreement reflex is NOT gpt-specific (gpt replicates; claude shows it off the ceiling, on the temporal subset and near the bar; gemini stays at ceiling) → REFLEX-GENERALIZES-TO-PANEL, bounded
meaning-senses:
  - constructional
  - functional-vs-formal
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-14
updated: 2026-07-05
links:
  - rel: refines
    target: conjecture/aann-construction
  - rel: refines
    target: result/aann-inferential-v4
  - rel: refines
    target: result/aann-inferential-v3
  - rel: refines
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: design/aann-agreement-reflex-generalization-v5
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: supports
    target: open-question/distributional-vs-inferential-constructional
---

# Result: AANN agreement-reflex generalization v5 — REFLEX-GENERALIZES-TO-PANEL (bounded)

> **Anchor: `internal-contrast-only`** (within-model AANN-vs-bare-plural agreement shift; **no
> human-comparison claim**), the terminal state carried forward from
> [`decisions/resolved/aann-inferential-operationalization`](../../decisions/resolved/aann-inferential-operationalization.md)
> (Condition 3 names the singular/plural agreement contrast the load-bearing discriminator) and the
> terminal-state precedent
> [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md).
> **Chief-cost statement (verbatim, binding):** *the v5 can never say "models pick the singular
> agreement the way humans do" — only that the construction shifts the within-model singular-agreement
> choice relative to a matched bare-plural control, in the direction the published AANN semantics
> predicts.* The expected-agreement key (singular *was* = AANN-licensed) is **EXPERT-STIPULATED**
> (Solt 2007; Dalrymple & King 2019; Bylinina & Nouwen 2018 — named, not quoted, not in-repo), a
> scoring key, not human data — and the agreement *shift* does not even depend on it (it is a
> within-model contrast).

The dedicated grammatical-reflex generalization probe NEXT.md backlog item 2(a) named: does
gpt-5.4-mini's singular-agreement reflex — singular *was* for the AANN (*a beautiful three days*),
plural *were* for the bare-plural control (*three beautiful days*) — **replicate on fresh held-out
items**, and do claude/gemini, which sat at the agreement ceiling in v3/v4, show any contrast off it?
This reuses the ratified v4 agreement arm **unchanged** (same was/were forced choice, same bare-plural
control, same single-shift indicator) on **30 fresh held-out adjective×measure-noun items** (zero
overlap with the 21 v3/v4 adjectives), with a **descriptive-only** count-noun ceiling diagnostic and a
Tier-0 manipulation check. It takes **no new operationalization decision** (a fresh pre-run critic
confirmed it stays inside the ratified instrument class).

Frozen design: [`design/aann-agreement-reflex-generalization-v5`](../../../experiments/designs/aann-agreement-reflex-generalization-v5.md).
PREREG, raw data, analysis, run log:
[`experiments/runs/2026-06-14-aann-agreement-reflex-v5/`](../../../experiments/runs/2026-06-14-aann-agreement-reflex-v5/README.md).
**246 calls, $0.0320 billed, 0 missing in every arm** (0 missing-cost calls). A **fresh independent
pre-run critic returned GO** (decision-class PASS — inside the ratified instrument class, no new
decision; anti-cheat PASS — the bar τ=+0.30 is set *stricter* than v3/v4's +0.20, biasing against a
free positive; freshness / fidelity / verdict-tree / provenance / anchor all PASS; 0 BLOCKERs). An
**independent post-run verifier recomputed every number from raw** — shift / CIs / was-rates / Tier-0 /
diagnostic / cost / verdict-tree: **0 mismatches** (unlike v4, no aggregation bug), and rebuilt
`chose_was` from the stimuli counterbalance map rather than trusting the raw row fields (0 row-letter
mismatches on all 180 agreement rows).

## Headline (pre-registered verdict: REFLEX-GENERALIZES-TO-PANEL)

On fresh held-out items the singular-agreement reflex is **not gpt-specific**. gpt-5.4-mini
**replicates** it; **claude-sonnet-4.6 shows it off the ceiling** and clears the pre-registered bar
(so the frozen tree returns REFLEX-GENERALIZES-TO-PANEL, claude's GENERALIZES outranking gpt's
REPLICATE); gemini-3.5-flash **stays at the ceiling** and is structurally uninformative, as in v3/v4.
**But claude's "generalizes" is bounded** (see *What bounds it* below): it is carried entirely by the
temporal subset, sits one item above the bar, and the v3/v4 "ceiling" was itself item-set-bound — so
read it as *"the construction shifts claude's agreement choice on the temporal held-out items,"* not as
a strong, class-general property.

| Per model (all Tier-0 12/12 PASS) | A claude-sonnet-4.6 | B gpt-5.4-mini [reflex-bearer] | C gemini-3.5-flash |
|---|---|---|---|
| **Agreement shift** P(was\|AANN) − P(was\|ctrl) (τ=+0.30, CI-lo>0) | **+0.333** CI[0.167,0.50] · **POS** | **+0.433** CI[0.233,0.633] · **POS** | +0.133 CI[0.033,0.267] · not pos |
|  — raw was-rate, AANN / bare-plural ctrl | 1.00 / 0.667 | 0.867 / 0.433 | 1.00 / 0.867 |
|  — control was-rate vs ceiling (≥0.85) | 0.667 · off ceiling | 0.433 · off ceiling | 0.867 · **at ceiling** |
| Diagnostic (descriptive-only) P(were\|count plural) | 1.00 | 1.00 | 1.00 |
| **Category (PREREG §6)** | **GENERALIZES-TO-PANEL** | **REPLICATES** | **CEILING-UNINFORMATIVE** |

**Verdict: REFLEX-GENERALIZES-TO-PANEL** — the held-out agreement reflex is present off-ceiling in at
least one of {claude, gemini} (here claude), so the reflex is **not gpt-specific**; gpt replicates it
on fresh items; gemini remains at the structural ceiling.

## What the result is

**1. gpt-5.4-mini's reflex replicates on held-out items — somewhat attenuated, still clear.** The
reflex-bearer's held-out shift is **+0.433** (CI-lo 0.233), clearing the *stricter* τ=+0.30 bar with a
CI well clear of 0. It is smaller than v3 (+0.739) and v4 (+0.652) — gpt's AANN was-rate drops to 0.867
(from 0.957 in v4) and its control was-rate is 0.433 (from 0.304) — but the contrast survives fresh
items and a higher bar. The v3/v4 reflex was not tied to those particular items.

**2. The reflex is NOT gpt-specific — claude shows it off the ceiling.** This is the result's news.
In v3/v4 claude sat at the agreement ceiling (AANN/control was-rate 1.00/1.00 — uninformative). On the
fresh held-out set its bare-plural control was-rate comes **off the ceiling** (0.667), while it still
picks singular *was* for the AANN at 1.00 — a clean **+0.333** within-item shift (CI-lo 0.167) that
clears the pre-registered bar. So the v3/v4 reading "the agreement discriminator is structurally blind
for claude" was **item-set-bound, not a stable fact**: on a fresh, larger sample the construction does
shift claude's agreement choice.

**3. gemini stays at the ceiling.** gemini's control was-rate is 0.867 (≥ 0.85), so it is read
CEILING-UNINFORMATIVE per the frozen rule — both AANN and bare-plural pull singular agreement, the
contrast has no room to show. This **confirms the v3/v4 structural-blindness reading for gemini on a
second item sample** (it is not a failure; the discriminator simply cannot speak for a model that picks
*was* for the bare plural too).

**4. The diagnostic confirms the ceiling is notional-singular-for-quantity, not "always *was*."** All
three models pick *were* for genuine **count-noun** bare plurals (*three excited dogs ___*) at 1.00. So
where claude/gemini pick *was* for a bare-plural **quantity** subject, that is a notional-singular
reading of duration/extent subjects — they *can* and do pick *were* for an ordinary count plural. (This
arm is descriptive-only; it enters no verdict branch, verified in code and by the post-run verifier.)

## What bounds it (binding on any reading)

The independent post-run verifier confirmed every number and flagged three bounds the headline must
carry — none changes the frozen verdict, all constrain its reading:

- **claude's shift is a clean WITHIN-ITEM construction contrast, not a frame artifact.** The verifier
  confirmed mechanically that for all 30 items the AANN and bare-plural frames share a **byte-identical
  post-blank continuation** and differ **only** in the subject NP (article+adj+num+noun vs
  num+adj+noun). So the +0.333 is a genuine construction effect, not a continuation-wording difference.
- **…but it is carried entirely by the temporal subset, and is near the bar.** All 10 of claude's
  control-*were* picks are **temporal** (days/weeks/months/hours/years); on the **distance** subset
  (*miles*) claude stays at **full ceiling** (12/12 control *was*). And +0.333 clears τ=+0.30 by a
  **single item** (10/30 control *were*); one or two fewer and it would fall below the bar. So
  "generalizes to claude" means *"the construction shifts claude's choice on the temporal held-out
  items,"* a thin, class-bound margin — **not** a strong class-general property.
- **The v3/v4 ceiling and the v5 off-ceiling do not contradict — both are item-set-bound.** v5's
  held-out set is 18/30 temporal, and only the temporal control frames moved; the v3/v4 sets gave a
  ceiling on their (different) mix. The two results reflect different class mixes, not a change in the
  model.
- **No human-comparison claim** (anchor `internal-contrast-only`): this can never say a model picks
  the singular agreement *the way humans do*. The expected-agreement key is expert-stipulated; the
  agreement shift is a within-model contrast that does not depend on it.
- **Single run, single panel, single date; small N** (30 held-out items, ≥8/cell floor met). It is a
  direction-of-effect generalization result, not a magnitude estimate.

## Relation to the conjecture, the prior results, and the ladder

- The **agreement reflex is a `functional-vs-formal` *form/agreement* signal, not an inference.** As in
  v3/v4 (and the pre-registered headline-gating there), a singular-agreement shift is **not** read as
  "the model draws the unification inference" — it is the grammaticalized morphosyntactic reflex of the
  construction's single-unit construal, the one place a distributional account predicts the *opposite*
  (singular agreement on a plural head is distributionally dispreferred). v5 says this reflex
  **generalizes beyond gpt** (to claude, off-ceiling, on the temporal held-out items) and **replicates
  in gpt** on fresh items; it does **not** upgrade the inferential verdict.
- It **refines [`result/aann-inferential-v4`](aann-inferential-v4.md)'s** "the agreement reflex is
  flat at ceiling for claude and gemini." That reading was **item-set-bound**: on fresh held-out items
  claude comes off ceiling and shows the reflex; gemini does not. v4's overall PARTIAL inferential
  verdict is **unchanged** (v5 tests only the agreement-reflex generalization, not the paraphrase/NLI
  inferential question).
- On the evidence ladder of
  [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
  *(Superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
  — cited here as the edition this page engaged.)*, this sits at
  the **form/agreement rung**, not the inference rung. It strengthens the recurring AANN pattern
  (strong and now panel-generalizing on *form/agreement*; inferential *use* uneven across models and
  instruments per v4) by showing the agreement reflex is robust to held-out items and present in two of
  three models — while keeping the standing caution that a grammaticalized reflex is not inference.

## Provenance

Stimuli are hand-authored, reusing the AANN measure-noun classes (temporal + distance) from
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) as
**class provenance only** — Mahowald's MTurk data are 1–10 *acceptability* ratings and **cannot** anchor
an agreement measure; no human there was asked an agreement question. The v3/v4 reflex numbers quoted in
the design/PREREG (+0.739, +0.652, was-rates 0.96/0.22 and 0.957/0.304, the 1.00/1.00 ceiling) are
verbatim from [`result/aann-inferential-v3`](aann-inferential-v3.md) and
[`result/aann-inferential-v4`](aann-inferential-v4.md). Independent post-run verification reproduced
every reported v5 number from the raw data (shift / CI / was-rate / Tier-0 / diagnostic / cost /
verdict-tree: 0 mismatches); 0 missing responses; stimuli sha256 matches the value frozen in PREREG.md;
cost $0.0320 billed (`usage.cost`-summed, 0 missing-cost calls).
