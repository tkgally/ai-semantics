---
type: conjecture
id: aann-construction
title: LLMs treat the AANN ("a beautiful three days") construction as a unit, not a syntactic accident
meaning-senses:
  - constructional
  - functional-vs-formal
status: tested
contingent-on: []
created: 2026-05-28
updated: 2026-07-05
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: operationalizes
    target: design/aann-construction-v2
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
---

# Conjecture: LLMs treat the AANN construction as a productive unit

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The gradient half of this conjecture
> has since been promoted and cross-date replicated. Session 176 promoted the line as
> [`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md) (cross-session adversarial
> review); session 178 landed the second-date powered replication
> [`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md) — the anchored
> gradient replicates for all three models on 408 fresh items disjoint from v2 (cell ρ
> 0.692 / 0.702 / 0.735, every CI overlapping v2), with one recorded wobble: gpt-5.4-mini's Tier-0
> manipulation check fell to 18/24 that occasion (Tier-0-excluding it from the conjecture-level
> support count, which replicates via A+C, while its graded gradient is undiminished), and the
> temporal held-out hole reproduced for claude and gemini (A, C).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## Statement

The **AANN construction** — *a* + Adjective + Numeral + Plural-Noun, as in *a beautiful three days*, *a remarkable five miles*, *a long six months* — is a marked English construction where the indefinite article scopes over a plural NP, and it carries a characteristic meaning: the measured quantity is presented as a coherent, unified, often evaluated stretch. This is the canonical CxG-probing target in the Weissweiler / Tayyar Madabushi line.

The conjecture: current LLMs treat AANN as a **productive construction** in Goldberg's sense — they generalize it to held-out lexical material in a way that tracks the construction's characteristic semantics (unification + evaluation), not merely the surface pattern.

## Why this is interesting

- AANN is the cleanest existing CxG-probing target, and the recent literature gives a ready-made human-anchor inventory of licit and illicit AANN instantiations.
- It splits cleanly along `functional-vs-formal`: the *form* (a + Adj + Num + N.PL) is learnable from a small number of training examples; the *function* (unification + evaluation) is what would make this `constructional` meaning rather than memorized template.
- It is the right size for a first-pass loop turn: one construction, one probe family, multiple panel models.

## Predictions

1. LLMs assign higher continuation likelihood to AANN with **evaluatively-loaded** adjectives (*beautiful*, *gruelling*, *remarkable*) than with **neutral measure-modifying** adjectives (*approximate*, *roughly*), even controlling for unigram frequency — because the construction's meaning is partly evaluative.
2. LLMs distinguish licit AANN from minimally-different illicit variants (*a three beautiful days*; *the beautiful three days*) at a level consistent with construction-specific learning rather than n-gram coverage.
3. Panel divergence: models with more code/structured-text in training will show *less* AANN sensitivity (it's a marked colloquial construction); this is itself informative about whether constructional meaning is uniformly recoverable from text.

## What would confirm / falsify

- **Confirm:** AANN-licit vs. illicit surprisal contrast on held-out lexical items tracks the human-rated acceptability gradient in [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md), in ≥2 of 3 panel models. Concrete threshold per [`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md) (ratified 2026-05-29: continuation-likelihood contrast (Option A) + prompted-acceptability fallback + threshold T1).
- **Weak:** contrast exists for items that appeared in training (memorization) but does not generalize to held-out adjectives.
- **Falsify:** flat or inverse contrast pattern; or contrast that tracks unigram frequency of adjective alone, not the construction.

## Human anchor

Catalogued as [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) (status: `external-only` until a future run mirrors the released repo). Mahowald 2023 (EACL) — templatic AANN stimulus generator plus MTurk acceptability ratings — supersedes the earlier "Weissweiler line" pointer in the bootstrap version of this conjecture; the Weissweiler CxG-probing papers remain a candidate secondary anchor. The anchor question was resolved 2026-05-29: Mahowald 2023 is the ratified AANN anchor (see [`decisions/resolved/aann-stimulus-source`](../../decisions/resolved/aann-stimulus-source.md)).

→ Anchor and operationalization decisions (both ratified 2026-05-29):

- [`decisions/resolved/aann-stimulus-source`](../../decisions/resolved/aann-stimulus-source.md) — ratified: Mahowald 2023 is the primary AANN anchor (Weissweiler retained as candidate secondary).
- [`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md) — ratified: continuation-likelihood contrast (Option A) + prompted-acceptability fallback + threshold T1 + held-out adjectives, locked before the run.

## Status note

**Updated 2026-06-12: status reverted `designed` → `proposed`.** The v1 design's ratified
indicator (the logprob/surprisal contrast, Options A and B of
[`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md))
was declared **unexecutable under pure autonomy** by the cross-session adversarial review that
resolved [`decisions/resolved/aann-panel-logprob-blocker`](../../decisions/resolved/aann-panel-logprob-blocker.md)
(no OpenRouter logprobs, no local GPU, no key will be provisioned), so "designed" would be false —
[`experiments/designs/aann-construction-v1.md`](../../../experiments/designs/aann-construction-v1.md)
is retired unrun. The indicator question was **reopened** as
[`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md)
(provisional default: gradient-primary behavioral instrument on the existing panel, Mahowald
Exp 2/3 ratings as anchor). The predictions and falsification *substance* above stand; only the
indicator clause ("surprisal contrast", "continuation likelihood") is reopened — read those
through whatever instrument the new decision ratifies. The conjecture returns to `designed` when
a frozen v2 design exists under a ratified instrument.

**Updated 2026-06-12 (later session): status `proposed` → `designed`.** The instrument decision
was **ratified** by the cross-session adversarial-review procedure
([`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md),
ADOPT DEFAULT with nine binding conditions), the Mahowald repo was mirrored and verified (MIT;
Exp-2 item-level ratings usable), and the frozen behavioral v2 design now exists:
[`experiments/designs/aann-construction-v2.md`](../../../experiments/designs/aann-construction-v2.md)
(gradient-primary, dual-framing, frequency-controlled held-out arm, Tier-0 manipulation check;
read predictions 1–2 above through that instrument — "continuation likelihood" becomes "prompted
graded acceptability", with the gradient scored against the **empirical** Exp-2 MTurk cell means,
never a stipulated ordering). `contingent-on` cleared accordingly.

**Updated 2026-06-12 (same session, post-run): status `designed` → `tested` — SUPPORTED.**
The probe ran the same session (permitted: the ratification preceded the design — the decision
was opened in an earlier session) → [`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md):
all three models pass every pre-registered gate (anchored gradient ρ 0.68–0.75 at cell grain;
frequency and noun-class guards clean; held-out class-gradient replication 0.75–0.83 on the
locked frequency-matched adjective list; Tier-0 23–24/24; $0.3125, 0 missing). Read it through
the instrument's bounds: this supports the **productive-gradient** half of the conjecture
(behavior tracks the human acceptability gradient and generalizes it to novel adjectives); the
**inferential half** (does the model *use* the unification/evaluation meaning?) remains untested
— the natural v3. Prediction 3 (gpt underperforms on the gradient) was **not** borne out — a
small disconfirmed expectation, recorded on the result page. Held-out replication is uneven by
noun class (temporal stratum negative; see the result's caveat 2).

**Update 2026-06-13 (opened): the inferential-half v3 was gated** by the decision
[`decisions/resolved/aann-inferential-operationalization`](../../decisions/resolved/aann-inferential-operationalization.md)
(indicator choice + the anchor sub-question — Mahowald's acceptability ratings do not anchor an
inference measure). **Update 2026-06-13 (next session): that decision is now RATIFIED**
(autonomous adversarial review, ADOPT DEFAULT WITH CONDITIONS): the inferential indicator is the
**A+B two-instrument package** (paraphrase forced-choice primary; entailment NLI convergent arm;
the grammaticalized singular/plural agreement contrast as the load-bearing discriminator), under
eight binding pre-run conditions, with the v3 result fixed at **`anchor: internal-contrast-only`**
(within-model AANN-vs-control shift; no human-comparison claim) scored against an explicitly
expert-stipulated literature key. So the inferential half now has a **ratified instrument and
anchor status**; it becomes `designed` once a frozen v3 design exists satisfying the eight
conditions, and `tested` only after a cross-session frozen run produces a result. Any reading of
this conjecture as supported on the unification/evaluation clause stays unsupported until then.
The gradient half's `tested` status is unaffected. The companion temporal held-out widening
(v2 caveat 2; same ratified instrument, no new decision) **ran the same session** →
[`result/aann-temporal-heldout-v2b`](../results/aann-temporal-heldout-v2b.md): widening the
temporal stratum 5× (16 → 80 items) confirms caveat 2 was real — the temporal stratum is
**uniformly negative at every grain** for all three models, so held-out AANN *productivity*
(generalizing the gradient to novel adjectives) is **noun-class-dependent** (strong for
object/distance, absent for temporal). This refines, and does not overturn, the v2 overall
SUPPORTED verdict.

**Update 2026-06-13 (next session): the inferential half is now TESTED — a ceiling-bounded NULL.**
The frozen v3 design ran (after repair + a fresh pre-run-critic GO + independent post-run
verification) → [`result/aann-inferential-v3`](../results/aann-inferential-v3.md). At the ratified
A+B instrument (paraphrase forced-choice primary + entailment NLI convergent + singular-agreement
discriminator), **no model shifts unification-vs-distributive inference relative to a matched
control** (paraphrase shift +0.17 / +0.04 / 0.00, none clears τ=0.20 with CI-lo>0; verdict NULL).
But the null is **ceiling-bounded, not a competence verdict**: the unification reading is the
**default for the plural control too** (control raw rates 0.78–1.00), so the construction has no
headroom to *shift* the inference — exactly the "inference and default coincide" hardness
[`open-question/distributional-vs-inferential-constructional`](../open-questions/distributional-vs-inferential-constructional.md)
named. The one positive signal is **gpt-5.4-mini's grammaticalized singular-agreement reflex
(+0.74)** (a `functional-vs-formal` form-reflex, not an inference), which the pre-registered
headline-gating correctly does **not** let count as "draws the unification inference." So: the
inferential clause is **neither supported nor cleanly disconfirmed** — it is **untestable at this
instrument as designed** (a future probe needs a control whose default reading is *distributive*).
The productive-gradient half's SUPPORTED status is unaffected; $0.0910, 0 missing.

**Update 2026-06-13 (fifth session): the inferential half is now PARTIAL — the v3 ceiling was
removed and a real construction effect appeared.** The v4 redesign ran (after a fresh pre-run-critic
GO + independent post-run verification) → [`result/aann-inferential-v4`](../results/aann-inferential-v4.md).
The single change — replacing the ceiling-pinned bare-plural control with a **distributive-default
control** (an itemizing "on each of the three days…" frame) plus a **lexical-cue control** so the
headline is a double contrast Δ² = P(uni|AANN) − P(uni|LCC) — **worked**: the new control reads
distributive at baseline for all three models (P(uni|DDC) = 0 / 0.22 / 0, where v3's control sat at
0.78–1.00). Against it, **all three models shift paraphrase selection toward the unification reading**
(Δ² +0.78 / +0.70 / +0.96, net of the lexical cue) — the positive v3 could not reach. But the shift
**converges across instruments in only one model**: **gpt-5.4-mini is CONVERGENT-POSITIVE**
(paraphrase + NLI entailment + the grammaticalized singular-agreement reflex +0.65, replicating v3's
+0.74), while **claude and gemini are PARAPHRASE-ONLY** (the shift does not carry to NLI, and their
agreement reflex is flat at ceiling). Verdict **PARTIAL** (<2 models converge). So the inferential
clause moves from "untestable at this instrument" to **partially supported**: a measured construction
effect, fully convergent in one model, paraphrase-level in two — **not** established across the panel.
`anchor: internal-contrast-only`; $0.1266, 0 missing. (An independent verifier caught an
NLI-aggregation bug fixed to the frozen spec; the overall PARTIAL verdict was unchanged by the fix —
see the result page.)

**Update 2026-06-14 (sixth session): the singular-agreement reflex GENERALIZES beyond gpt on fresh
held-out items (a `functional-vs-formal` form-rung result, not an inference upgrade).** The dedicated
reflex-generalization probe ran (fresh pre-run-critic GO + independent post-run verification, 0
mismatches) → [`result/aann-agreement-reflex-v5`](../results/aann-agreement-reflex-v5.md). Reusing the
ratified agreement arm **unchanged** on 30 fresh held-out adjective×measure-noun items (0 overlap with
v3/v4) at a *stricter* bar (τ=+0.30): **gpt-5.4-mini REPLICATES** its reflex (+0.43, smaller than v3's
+0.74 / v4's +0.65 but clearing the higher bar), and — the news — **claude-sonnet-4.6 shows the reflex
off the ceiling** (+0.33; its bare-plural control was-rate falls to 0.667 where v3/v4 had it pinned at
1.00), so the reflex is **not gpt-specific** → verdict **REFLEX-GENERALIZES-TO-PANEL**. **gemini stays
at the ceiling** (control was-rate 0.867, structurally blind, confirming the v3/v4 reading on a second
sample). Bounds the verifier flagged and the result carries: claude's shift is a clean within-item
contrast but **carried entirely by the temporal subset** (distance stays at full ceiling) and sits one
item above the bar — read as "the construction shifts claude's agreement choice on the temporal
held-out items," not a class-general property; v3/v4's "ceiling" and v5's "off-ceiling" are both
item-set-bound and do not contradict. This is a **form/agreement-rung** generalization (the reflex is
robust to held-out items and present in two of three models); it does **not** change the **inferential**
verdict, which stays at v4's PARTIAL. `anchor: internal-contrast-only`; $0.0320, 0 missing.

**Update 2026-06-14 (ninth session): the inferential PARTIAL REPLICATES, powered, on fresh held-out
adjectives.** A powered panel replication of v4 ran (fresh pre-run-critic GO + independent post-run
verification, 0 mismatches) → [`result/aann-inferential-v6`](../results/aann-inferential-v6.md). Same
yardstick as v4 (instrument, thresholds, verdict map, analysis code identical), single change the item
set: **40 fresh hand-authored base items** (temporal 20 / distance 20, nearly doubling v4's 23,
rebalancing the distance class), all **40 adjectives held-out** (disjoint from v4's 21 and the
v5-reflex probe's 30). Both pre-registered questions answered **yes**: (1) the panel-wide paraphrase
double-contrast shift **holds up powered** — all three models paraphrase-positive (Δ²
+0.875 / +0.575 / +0.90, headroom PASS all, DDC 0 / 0.225 / 0); (2) **gpt-5.4-mini's cross-instrument
convergence replicates** — CONVERGENT-POSITIVE again (paraphrase + NLI Δ² +0.225 + agreement reflex
+0.60), while claude and gemini are again PARAPHRASE-ONLY (NLI null, agreement flat at ceiling 1.00/1.00).
Verdict **PARTIAL**, cell-for-cell as v4 (per-model categories PARA-ONLY / CONV-POS / PARA-ONLY). The
inferential clause is unchanged in *status* (partially supported) but now on **firmer ground**: the
construction effect is shown stable in **magnitude across two disjoint item sets**, removing v4's
"small-N / single-date / direction-not-magnitude" caveat (the **single-panel** and
**expert-stipulated-key** caveats remain). `anchor: internal-contrast-only`; $0.2138, 0 missing.

## Notes / caveats

- Memorization is the main confound; the held-out lexical-item check is the main defense.
- The Weissweiler line has done a version of this; the project's contribution is the **meaning-sense tagging** and the **cross-model decorrelation** angle, not novel probing of AANN per se.
