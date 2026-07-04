---
type: result
id: aann-behavioral-gradient-rep2
title: AANN behavioral gradient — second-date, fresh-item powered REPLICATION (rep2); the anchored acceptability gradient replicates cross-date for all three models (cell ρ 0.69 / 0.70 / 0.74, every CI overlapping v2, frequency- and noun-class-guarded), and the conjecture-level SUPPORTED verdict replicates via A+C — with one honest new wrinkle, gpt-5.4-mini's Tier-0 manipulation check dropping to 18/24 on the objects/evaluative items this occasion, excluding it from the support count even though its graded gradient is undiminished
meaning-senses:
  - constructional
  - distributional
  - functional-vs-formal
  - human-comparison
status: proposed
anchor: resource/mahowald-2023-aann-stimuli
contingent-on: []
created: 2026-07-04
updated: 2026-07-04
links:
  - rel: supports
    target: claim/aann-behavioral-gradient
  - rel: supports
    target: conjecture/aann-construction
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: result/aann-behavioral-gradient-v2
  - rel: depends-on
    target: claim/formal-competence-aann-ceiling
  - rel: refines
    target: theory/constructional-meaning-in-llms-v2
---

# Result: AANN behavioral gradient — rep2, the owed cross-date fresh-item replication (SUPPORTED, replicates)

The A2a owed **second-date powered re-run** of the AANN anchored acceptability gradient — the
"overall positive" whose only gap, named in
[`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md), was *"there is no
second-date replication of the overall positive."* This run supplies exactly that: a **fresh-item,
second-date** replication on the **byte-identical frozen v2 instrument**, against the
**byte-identical human anchor**, with the anchored arm drawn **disjoint from v2** (408 fresh
sentence items, **0 shared surface items**, each mapping to the same 204 human cells).

Frozen design: [`design/aann-construction-v2`](../../../experiments/designs/aann-construction-v2.md)
(unchanged; rep2 is the same instrument on a fresh sample). PREREG, prep, raw data, and run record:
[`experiments/runs/2026-07-04-aann-behavioral-gradient-rep2/`](../../../experiments/runs/2026-07-04-aann-behavioral-gradient-rep2/README.md).
**1,782 calls, $0.3092 billed, zero missing responses in every arm.** Instrument identity to v2 is
sha256-verified (`probe.py` `ec8f7334…`, `analyze.py` `4ce5a709…`); the human tables
(`human_cell_means.csv`, `human_class_means.csv`) are byte-identical to v2 (verified by `diff`).
Independent fresh-agent **pre-run critic GO**; one **non-Anthropic decorrelation vote**
(`openai/gpt-5.4-mini`) **GO-WITH-CONDITIONS**, its three conditions honored below; independent
fresh-agent **post-run verifier**.

## Headline — the anchored gradient replicates cross-date on fresh items (3/3)

The claim's beater property (a graded model–human acceptability correlation that **survives
partialling out word-frequency**) replicates on a **second date** with **fresh, disjoint** items for
**all three models**, at cell ρ statistically indistinguishable from v2:

| Anchored arm (204 cells) | A claude-sonnet-4.6 | B gpt-5.4-mini | C gemini-3.5-flash |
|---|---|---|---|
| **rep2** cell-level Spearman ρ | **0.6922** | **0.7024** | **0.7351** |
| rep2 bootstrap 95% CI (excludes 0) | 0.6027–0.7619 | 0.6167–0.7699 | 0.6578–0.7947 |
| — v2 for comparison | 0.7017 [0.61,0.77] | 0.6843 [0.60,0.75] | 0.7505 [0.68,0.81] |
| rep2 Zipf frequency guard, partial ρ (≥0.20) | 0.6873 | 0.6902 | 0.7223 |
| rep2 noun-class guard, within-class mean ρ (≥0.25) | 0.5451 | 0.6061 | 0.5951 |
| rep2 gradient gates all pass? | ✅ | ✅ | ✅ |

**All three anchored gradients pass every gradient gate** (ρ≥0.40, CI excludes 0, frequency partial
≥0.20, noun-class guard ≥0.25), with **no frequency-confounded pass** (the partials barely move off
the raw ρ, as in v2). Cross-date CI overlap is complete — the three comparisons, stated explicitly
(pre-run-critic NIT; non-Anthropic-vote condition 1's falsifiability target):

- **A:** rep2 [0.603, 0.762] vs v2 [0.61, 0.77] — **overlap** (ρ 0.692 vs 0.702).
- **B:** rep2 [0.617, 0.770] vs v2 [0.60, 0.75] — **overlap** (ρ 0.702 vs 0.684).
- **C:** rep2 [0.658, 0.795] vs v2 [0.68, 0.81] — **overlap** (ρ 0.735 vs 0.751).

No downward, non-overlapping CI for any model. The pre-registered success criterion for "the overall
positive replicates" (≥2/3 Tier-0-passing models re-pass the anchored arm at a CI overlapping v2's
interval) is **met**, and in fact the **gradient itself** replicates for all three models including
the one that is Tier-0-excluded below. Secondary grain (28 class-cells, descriptive): ρ = 0.879 /
0.889 / 0.909 (v2: 0.85 / 0.84 / 0.92). Item-level against single human ratings (descriptive floor,
single-rater noise): 0.469 / 0.482 / 0.473 (v2: 0.49 / 0.45 / 0.45).

## The pre-registered conjecture-level verdict: SUPPORTED — with a changed composition

`analyze.py` emits **SUPPORTED** on the frozen verdict map (≥2 of 3 Tier-0-passing models achieve
the anchored pass, and every anchored passer also passes held-out). But the **composition of the
support differs from v2**, and this is the run's honest new content:

| | Tier-0 (≥20/24) | anchored gates | held-out (≥0.50) | counts toward verdict? |
|---|---|---|---|---|
| A claude | **22/24** ✅ | pass | 0.8311 ✅ | yes |
| C gemini | **22/24** ✅ | pass | 0.7821 ✅ | yes |
| B gpt | **18/24** ❌ | *pass (0.7024)* | *0.7929* | **no — Tier-0-excluded** |

Per the frozen rule ("a model failing Tier-0 has its gradient numbers **reported but not counted**"),
**B is excluded from the support count on the manipulation check**, and SUPPORTED rests on **A + C**
(2 of the 2 Tier-0 passers, both also passing held-out). This is the same verdict label as v2, on a
strictly-obeyed frozen map — but v2 had all three pass Tier-0 (23 / 23 / 24), and here **B drops to
18/24**.

**B's Tier-0 drop is genuine, not a parse artifact, and it is interpretable.** All six of B's misses
are **clean single-letter answers** (verified in the raw), and all six fall on exactly two
item-tuples — **"gruesome three paintings"** and **"ugly three desks"** — i.e. the **objects**
noun-class with **negative-evaluative** adjectives, the most **marginal** AANN environment (objects
nouns license AANN far more weakly than temporal/measure nouns). On this fresh occasion gpt-5.4-mini
did not reliably prefer e.g. *"She bought a gruesome three paintings"* over its reverse-order /
no-article / no-modifier degenerate variants. So the finding is precise: **B's graded gradient is
undiminished (0.702, CI overlaps v2), but its formal AANN preference is fragile on the marginal
objects/evaluative items** — enough to fail the ≥20/24 gate this occasion. This *sharpens* rather than
contradicts the claim: the graded-gradient property (what the claim asserts) is robust across dates
and items for all three; the coarse binary form-ceiling can wobble at the margin.

(A and C both pass Tier-0 cleanly. C's two misses are **verbose "Neither sentence is grammatically
correct or natural in English…" prose** on the two `no_plural` items: in **both**, C's *stated* pick
is **B — the AANN answer** ("B is the marginally more coherent option"), but the first-bare-token
parser grabbed the article "a" from the surrounding prose and scored "A" — the identical defect v2
flagged for C. **Corrected to C's stated intent, C is 24/24.** A's two misses are clean single
letters. Neither changes any gate — C passes at 22/24 as scored, 24/24 corrected.)

## Held-out arm (bonus — byte-identical items, second date)

The held-out adjective list is lexically frozen, so these 60 items are byte-identical to v2 (a
same-items second-date re-run, not a fresh-item replication — labelled as such). The **overall
held-out positive replicates for all three** (class-cell ρ **0.8311 / 0.7929 / 0.7821**; v2: 0.834 /
0.814 / 0.753), and the **temporal-stratum hole reproduces for A and C** (temporal ρ **−0.20 / −0.20**,
as in v2 and the v2b widening). B's temporal stratum comes out **+0.8** this occasion (v2: negative)
— but on only ~4 class-cells one rank swap flips the sign, and B is Tier-0-excluded from the verdict
regardless; this is noted, not read into. The noun-class-dependent-productivity picture
([`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md)) is unchanged: strong on
objects/distance, absent/fragile on temporal.

## Anchor discipline

Anchored to [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
(Exp-2 MTurk ratings; 3,600 non-filler items aggregated to the 204 cell means — the **same** table
v2 used, byte-identical). The fresh model items are a **disjoint** 2-item-per-cell sample (v2's items
removed from each cell's pool before the seeded draw; every cell retained **≥4 candidates**, min pool
6 − 2 = 4 — non-Anthropic-vote condition 2), so the comparison is fresh sentences against the same
human gradient. The **held-out arm carries no independent human claim** (gradient replication against
the human anchored-half ordering, on adjectives with no human ratings by construction). The reading
is scoped to **cross-date replication of the anchored positive on fresh items** — it does **not**
re-open v2's own SUPPORTED verdict, and makes no new representation, inference-licensing, or
human-parity claim (non-Anthropic-vote condition 3).

## What this adds to the claim

[`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md) was promoted `supported`
but **single-run-scoped**, its lead bound being exactly "no second-date replication of the overall
positive." rep2 discharges that bound for the **graded gradient** (the claim's core): the
frequency- and noun-class-guarded anchored gradient now replicates **on two dates, on disjoint
items, 3/3**, with overlapping intervals. The claim's magnitude was already powered; what it lacked
was cross-date replication of the positive, and it now has it. The one qualification rep2 adds is at
the **form-ceiling** layer, not the gradient: one model's binary Tier-0 preference is fragile on the
marginal objects/evaluative items — which is why the claim's `supported` attaches to the **graded
gradient-tracking** statement, never to a panel-uniform form-competence reading.

## Caveats (post-run verifier's required list — none change the verdict)

1. **B (gpt) is Tier-0-excluded (18/24), genuinely.** Its gradient is fully in line with v2 but does
   not count toward the conjecture verdict; SUPPORTED rests on A + C. The exclusion is a real
   behavioral fact on marginal objects/evaluative items, not an instrument failure.
2. **C's two Tier-0 misses are verbose "neither"-prose mis-parses** (the v2 first-bare-token defect),
   not genuine preferences for the degenerate variant; C passes at 22/24 (or higher) regardless.
3. **Held-out is a same-items re-run, not fresh** (frozen list); it replicates the overall positive
   and (A, C) the temporal hole, but is labelled bonus, not the primary fresh-item target.
4. **Cell-averaging is load-bearing** (item-level ρ 0.47–0.48, the descriptive floor); **crowdsourced
   MTurk anchor**; **behavioral not representational**; **scale-use calibration differs by model** —
   all as in v2, unchanged by this run.

## Verification chain

Pre-run: independent fresh-agent critic **GO** (instrument + anchor byte-identity verified;
disjointness mechanically proven — 408 items, 0 shared, 204 cells × 2, every cell ≥4 candidates;
anti-cheat clean; criterion falsifiable). Non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`)
**GO-WITH-CONDITIONS**, three conditions honored (bootstrap procedure stated: 10,000-resample
percentile bootstrap over the 204 cells, per-model, seed 20260612; post-exclusion candidate counts
reported; read scoped to cross-date replication). Freeze: PREREG committed before any model call.
Post-run: independent fresh-agent verifier, own code (own rank/Spearman/partial/bootstrap, seed
20260612), recomputed every gate from raw — **REPRODUCED, 0 discrepancies**: every per-model number,
CI (to the digit), the SUPPORTED verdict, the B-on-Tier-0 exclusion (B's gradient itself passes all
four gates), the C parse-artifact (both C misses stated "B", the AANN answer), the three-way v2 CI
overlap, corpus safety (longest non-Tier-0 raw string 3 chars; human tables + instrument sha-identical
to v2; anchored items 0-shared with v2), and the $0.309183 → $0.3092 billed cost all checked out.
