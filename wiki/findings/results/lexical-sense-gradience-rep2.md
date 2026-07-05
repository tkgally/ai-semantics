---
type: result
id: lexical-sense-gradience-rep2
title: "Lexical sense gradience rep2 — the owed cross-date replication: on 200 fresh v1-disjoint DWUG pairs the panel's graded sense-relatedness rating rank-tracks the human DURel median 3/3 (all CIs overlap v1), and the topic-partial shadow-beater survives 3/3, discharging the single-run flag for the direction/agreement claim"
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: proposed
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-07-05
updated: 2026-07-05
links:
  - rel: supports
    target: claim/lexical-sense-gradience
  - rel: supports
    target: conjecture/lexical-sense-gradience
  - rel: refines
    target: result/lexical-sense-gradience-v1
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Result: lexical sense gradience rep2 — the owed A2a cross-date replication

**One-line:** on **200 fresh DWUG EN pairs drawn disjoint from v1** (0 shared pairs), on a fresh
date, the byte-frozen instrument reproduces v1: **all three panel models' graded sense-relatedness
rating rank-tracks the human DURel median** — Spearman **0.715 / 0.528 / 0.808** (claude / gpt-5.4-mini /
gemini) on the 4-point framing, **0.739 / 0.631 / 0.801** on the 0–100 framing — **every rep2 point
estimate falls within v1's 95% CI and every CI overlaps v1**, and the monotonic signal **survives
partialling out the model's own topic-similarity rating 3/3** (partial ρ | topic 0.60/0.39/0.66 durel,
0.64/0.51/0.64 cont). The graded direction and the topic-partial shadow-beater **replicate cross-date
3/3 on both framings**, discharging the **single-run flag** on the direction/agreement claim
([`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md)). It was the **last owed A2a
re-run** — the only remaining flagship positive without a cross-date replication.

Run record: [`experiments/runs/2026-07-05-lexical-sense-gradience-probe-rep2/`](../../../experiments/runs/2026-07-05-lexical-sense-gradience-probe-rep2/README-rep2.md).
v1: [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md). Design (frozen, unchanged):
[`design/lexical-sense-gradience-v1`](../../../experiments/designs/lexical-sense-gradience-v1.md).
Anchor: [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (DWUG EN v3.0.0).
Cost **$0.68507 billed** (1800 calls, 0 NA).

## What ran (byte-frozen instrument, fresh disjoint items)

The instrument's behavioral logic and analysis are **byte-frozen from v1** (`analyze.py` sha256
identical; `probe.py` differs only in the single input-path constant, `diff`-verified — see the run
README). Fresh items: **200 pairs, 50 per rounded human DURel level 1–4, 41 lemmas, within-period,
≥2-annotator gold**, drawn with a fresh seed (`20260705`) after **excluding every v1 pair** from the
candidate pool. Manifest freeze sha256 `9b6b66bd…`; DWUG archive sha256 identical to v1's freeze.
Three framings per item (`durel`/`cont`/`topic`), temperature 0, logprob-free, the standing 3-family
panel — all identical to v1.

**Disjointness scope (honest, per the pre-run critic's condition C1).** The probed item is a
**pair**; **0 rep2 pairs appear in v1** (asserted + independently re-verified). DWUG's corpus is a
finite inventory of uses per lemma, so a single usage can recombine into a *different* fresh pair:
**61/357** rep2 usages also appear in some v1 pair. This is a **cross-date replication of the same
instrument on fresh pairs** — **not** two fully independent draws, and weaker than the AANN rep2's
"0 shared surface items" (AANN *generates* items; DWUG cannot). No naive pooling/meta-analysis treats
v1 and rep2 as independent.

## Result — v1 vs rep2 (independently re-verified from raw JSON)

Spearman ρ(model sense, human DURel median), n=200, bootstrap 95% CI. Each rep2 cell beside its v1 value:

| model · framing | v1 ρ (95% CI) | **rep2 ρ (95% CI)** | overlap? |
|---|---|---|---|
| claude · durel | 0.679 (0.59–0.75) | **0.715 (0.642–0.777)** | ✓ |
| claude · cont  | 0.696 (0.61–0.78) | **0.739 (0.664–0.799)** | ✓ |
| gpt · durel    | 0.601 (0.49–0.69) | **0.528 (0.409–0.639)** | ✓ |
| gpt · cont     | 0.675 (0.58–0.75) | **0.631 (0.530–0.723)** | ✓ |
| gemini · durel | 0.804 (0.75–0.85) | **0.808 (0.748–0.852)** | ✓ |
| gemini · cont  | 0.825 (0.76–0.87) | **0.801 (0.740–0.848)** | ✓ |

Partial ρ | topic (the shadow-beater = clause c) and the covariate controls:

| model · framing | partial \| topic (v1 → **rep2**) | partial \| overlap (**rep2**) | ρ(sense,topic) (**rep2**) | ρ n≥3 (**rep2**) |
|---|---|---|---|---|
| claude · durel | 0.52 → **0.604** | 0.71 | 0.631 | 0.702 |
| claude · cont  | 0.54 → **0.640** | 0.735 | 0.631 | 0.626 |
| gpt · durel    | 0.50 → **0.392** | 0.52 | 0.504 | 0.496 |
| gpt · cont     | 0.58 → **0.506** | 0.626 | 0.616 | 0.535 |
| gemini · durel | 0.73 → **0.657** | 0.807 | 0.707 | 0.778 |
| gemini · cont  | 0.75 → **0.639** | 0.798 | 0.731 | 0.742 |

1800 calls, **0 NA** in every arm. n≥3-annotator subset = 64/200 (v1: 48/200); the n≥3 ρ tracks the
full-set direction for every model.

**Three readings (the same three as v1 — all reproduce):**

1. **Graded-sense tracking replicates (clause a), 3/3, both framings.** Every rep2 base ρ is positive,
   clear of zero (lowest CI bound gpt-durel 0.409), and **within v1's CI** — the direction is not a
   one-draw artifact. Per-human-level means are broadly **monotonic** (e.g. claude `cont`:
   13.1 → 19.8 → 38.3 → 40.3 → 62.2 → 66.9 → 78.7 across levels 1.0→4.0). gemini strongest (0.80–0.81),
   claude at/above the human–human agreement (ρ≈0.69: claude durel 0.715 / cont 0.739), gpt weakest.
2. **Not just a context shadow (clause c) — the topic partial survives 3/3.** Partialling out the
   model's own topic-similarity rating leaves a clearly positive, non-collapsing partial for all three
   models on both framings (0.60/0.39/0.66 durel; 0.64/0.51/0.64 cont). Lexical overlap is again
   near-degenerate, so the overlap partial ≈ base (the *surface* shadow is ruled out a priori, not by
   partialling — S1). The sense signal carries rank information about human sense-relatedness **beyond**
   the model's perception of context similarity — modestly, by a model-internal single-lab control (S2).
3. **Instrument-sensitivity theme reproduces.** gpt-5.4-mini is again the noisiest model under the
   *ordinal* DURel framing (base ρ 0.528, partial | topic 0.392, mid-level means non-monotonic — the
   2.5 dip recurs) and cleaner under the *continuous* framing (0.631) — the lexical reappearance of the
   project's standing elicitation-format sensitivity, on the same model, on fresh items.

## The one honest wrinkle: gpt drifts down (within CI), and it is the weakest cell

gpt-5.4-mini's ordinal-DURel base ρ moved **0.601 → 0.528** and its topic partial **0.50 → 0.392** —
the largest per-cell drop in the panel. Both remain **positive, non-collapsing, and CI-overlapping
v1**, so the *direction* replicates; but gpt is the model whose graded sense-tracking is (a) most
elicitation-format-dependent and (b) closest to — and this draw, on the ordinal framing, **below** —
the human–human agreement band. So the replication is **panel-level 3/3 on direction**, with gpt
carried honestly as the weakest and most fragile corner, exactly as v1 flagged it. claude drifted
*up* (0.679→0.715 durel), gemini held (0.804→0.808 durel); gemini's `cont` topic partial dipped
0.75→0.639 (still strong). No cell reverses sign or collapses.

## What this does and does not change

- **Discharges the single-run flag** on [`claim/lexical-sense-gradience`](../claims/lexical-sense-gradience.md)'s
  **direction/agreement** core: the graded ρ vs the DURel median and its survival of the topic partial
  are now **cross-date replicated** on fresh pair-disjoint items, not a single draw. This is the flagged
  strengthening the claim's *Bounds* named ("a second run on fresh DWUG pairs … would be the natural
  strengthening").
- **Does NOT upgrade to a twice-powered independent magnitude, a representational claim, or a broad
  "model understanding" reading** (pre-run critic C1/C2 + non-Anthropic vote). It is cross-date
  **stability of the same instrument** on fresh pairs from the same finite corpus. The topic control
  is still model-internal and modest; the gold is still 2-rater for 136/200 pairs; the level-1 floor
  still mixes homonymy (S4). The magnitudes are stated **as a replicated direction/agreement**, not a
  human effect-size comparison and not a per-item human comparison.
- **Does NOT touch clause (b)** (polysemy as a discrete regime beyond graded distance), which remains a
  separate powered null ([`result/lexical-polysemy-homonymy-v3`](lexical-polysemy-homonymy-v3.md)).

## Caveats (carried forward from v1, unchanged)

- **Behavioral, not representational.** A stated-rating rank correlation; silent on graded sense
  *representations*.
- **The topic control is model-internal and single-lab** (S2); the lexical-overlap control is
  near-degenerate (S1). Modest positive support against a topic shadow, not a decisive dissociation.
- **Gold reliability** (S3): 136/200 pairs rest on 2 annotators; half-integer levels are not treated as
  reliable graded gold. The n≥3 subset (64/200) ρ is reported above and tracks the full set.
- **Homonymy floor** (S4): the "Unrelated" end partly mixes homonymy, not graded polysemy.
- **Scope.** 200 pairs, 41 CCOHA lemmas, single temp-0 run per model on this date, DURel framing,
  English. A cross-date replication of direction/agreement, not a coverage benchmark; no claim beyond
  these lemmas/register/framing/panel.
- **Cost note (for future pre-flights).** Total $0.68507 — **far below v1's $3.134**, entirely because
  gemini billed **$0.174** here vs **$2.606** in v1 (its internal-reasoning-token burn on this
  instrument is date/item-dependent, not a fixed property). The DWUG sense instrument is **not
  reliably** a >$2.50 single-run: budget against the billed expectation, but v1's gemini spike was an
  anomaly, not the norm.

## Verification

Independent fresh-agent **post-run verifier** recomputed every ρ / partial / ρ(sense,topic) from
`raw/*.json` + `manifest.csv` (its own tie-averaged Spearman + partial formula + CSV join, **not** the
run's `analyze.py`), re-checked the disjointness, the 0-NA / 1800-call / 0-missing-cost counts, and the
anti-cheat → **REPRODUCED (0 discrepancies)**: max abs diff **0.0005** across all 24 statistics (pure
3-decimal rounding), n=200/0 NA per arm confirmed, **0 shared pairs / 61 shared usages** independently
reproduced, and the human gold confirmed absent from every model prompt (attached post-hoc only). The
verifier's one note — a small **local non-monotonicity at the human-2.5 bucket** (means dip below the
2.0 bucket for gpt/gemini `cont`) — is the noisy **2-rater half-integer** gold (S3), not a direction
problem: endpoints and overall trend rise strongly. Pre-run: independent fresh-agent critic (NO-GO on
B1 — the frozen probe's input path — fixed + smoke-tested before spend) + one non-Anthropic
decorrelation vote (GO-WITH-CONDITIONS); all conditions honored above.
