---
type: note
id: blimp-c4-matched-swap-arm-freeze-v1
title: "Freeze record — BLiMP R1 C4-frequency-matched content-word-swap arm (the s210 SWAP-INCONCLUSIVE successor): the ratified dual-band recipe (SUBTLEX ±0.10 AND C4 ±0.30 per word) + the disjoint fresh sample frozen and pre-run-gated (ratifier ADOPT-WITH-MODIFICATION Q1-A/Q2-A/Q3-A with B1–B4 + S5–S8 all honored; freeze critic + two non-Anthropic votes), but the finding-bearing RUN is DEFERRED to a full-$5 UTC day (freeze session had ~$1.81 of the $5/UTC cap left; the run projects ~$1.3–1.6). No measurement here — this is a build/freeze method record."
meaning-senses:
  - constructional
  - measurement-epistemic
status: recorded
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-15
updated: 2026-07-15
links:
  - rel: depends-on
    target: result/blimp-swap-arm-v1
  - rel: depends-on
    target: design/blimp-c4-matched-swap-arm-v1
  - rel: depends-on
    target: result/blimp-profile-frequency-control-covariate-v1
---

# Freeze record — BLiMP R1 C4-frequency-matched content-word-swap arm (A3b; the s210 SWAP-INCONCLUSIVE successor)

> **Status: recorded (s232, 2026-07-15).** A build/freeze **method record** — it carries **no new
> measurement** (`raw/` is empty; nothing has been run or peeked) and is never cited as support for a
> claim. It records that the C4-frequency-matched swap arm was **ratified**, forked, frozen, and
> pre-run-gated this session, and that its finding-bearing **run was deferred** to a full-$5 UTC day for
> budget reasons. `anchor: internal-contrast-only` — this note asserts no human comparison; the arm it
> freezes is a within-model exact-string-memorization control, and any human-comparison force lives on the
> deferred result. The empirical successor to
> [`result/blimp-swap-arm-v1`](../results/blimp-swap-arm-v1.md) (SWAP-INCONCLUSIVE).

## Why this arm exists

The s210 content-word-swap arm returned **SWAP-INCONCLUSIVE**: the load-bearing **deep-scope** stratum
dropped 3/3 under a SUBTLEX-frequency-matched swap (Δ̄acc −0.095 / −0.057 / −0.072, all CIs exclude 0), but
the drop is **confounded by a +0.204 C4 pretraining-frequency gap** — the swap words matched the human
SUBTLEX-US `Lg10WF` norm yet were ~1.6× rarer in the C4 pretraining proxy (2.3% never occur over 3M
sentences). So the deep drop is **neither** SWAP-STABLE **nor** clean exact-string memorization; the C8
chain closed on that ambiguity ([`result/blimp-swap-arm-v1`](../results/blimp-swap-arm-v1.md) scope-cap #4
named the fix). This arm closes the confound by matching the swap substitutes on the **C4 pretraining proxy**
too, so a deep drop that **survives** can only be exact-string memorization (net of both frequency proxies),
and a deep drop that **vanishes** clears the suspicion.

## What was frozen this session (s232)

- **Ratified** the open decision
  ([`decisions/resolved/blimp-c4-matched-swap-arm-design`](../../decisions/resolved/blimp-c4-matched-swap-arm-design.md);
  opened s231, eligible s232) by an independent cross-session **fresh-agent adversarial reviewer** (verdict
  authority) that **weighed** one non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.004259) — both
  **ADOPT-WITH-MODIFICATION**, convergent on **Q1-A DUAL-BAND / Q2-A / Q3-A**.
- **The ratified recipe** (the only new operationalization vs the byte-frozen s210 instrument): each
  substitute must be in-band on **both** SUBTLEX-US `Lg10WF` (±0.10) **AND** C4 pretraining-proxy
  log-frequency (±0.30) of the original — the **intersection** pool, seeded-deterministic. This controls
  **both** the human- and the pretraining-frequency channel per word.
- **Four binding freeze BLOCKERs + four SHOULD-FIX honored** (the ratifier's + the two votes' conditions):
  **B1** one BLIND switch — C4 half-width fixed 0.30, per-position pool floor 5, Q1-A→Q1-B trigger 0.25, all
  accuracy-blind and pre-committed; **B2** anti-seed-shopping — the only seed (`20260715`, date-derived) is
  pre-announced for the disjoint subsample, substitute selection is **seed-free** (per-position item-hash);
  **B3** exact `|signed set-mean C4 gap| ≤ 0.05` at the pinned 22.3M stream scale or
  STILL-INCONCLUSIVE-BY-MATCH-FAILURE; **B4** the blind-scoring lock (scoring code + the four-outcome table
  frozen before any re-run); **S5** single pinned 22.3M C4 stream; **S6** per-word C4 report + soft
  directional-cancellation flag; **S7** N sized 130→160 + the exact attrition fallback; **S8** the
  refusing-pole successor motivation kept visible.
- **The disjoint sample is frozen + certified** at freeze
  ([`build_disjoint_sample.py`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/build_disjoint_sample.py)
  → `disjoint_sample.json`, sample_sha256 `1f90050c…`): the 6 s210 paradigms, drawn from pairs **minus** the
  s210 kept ids, **0 overlap** with s210 on all 6 — disjoint **by construction**.
- **Freeze critic (verdict authority) → GO-WITH-CONDITIONS** + a second non-Anthropic vote (`gpt-5.4-mini`,
  $0.004198, convergent). B1–B4 all PASS with no promotion-seeking retune; the critic caught **one real
  BLOCKER** — a dead-code attrition-exclusion bug in the scorer (a below-floor paradigm was never dropped
  from the pooled delta) — **fixed at freeze** so the code matches the ratified attrition rule, plus two
  cheap SHOULD-FIX (a build-time adequacy abort so a bad match cannot spend, and a drop-criterion wording
  reconcile) done the same session. Two run-time conditions (a single irrevocable fallback branch; an
  immutable pre-scoring artifact bundle) fold to the deferred run.
- **The frozen recipe** — a self-contained fork of the s210 builder
  ([`build_swap_c4.py`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/build_swap_c4.py); the
  8 inherited morphology/detok/locus helpers verified **byte-identical** to s210), the byte-frozen probe
  (`probe.py`, identical to s210 except the items filename), the scorer with the four-outcome table
  ([`analyze_swap_c4.py`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/analyze_swap_c4.py)),
  and the PREREG
  ([`PREREG.md`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/PREREG.md)). A `predictions.md`
  bet is registered at freeze, no outcome pre-filled.

## Why the run is deferred (budget, not doubt)

The run projects **~$1.3–1.6** (7,200 calls; sized from the **observed** s210 economics, not a low
pre-flight). s232 landed on the tight **2026-07-15 UTC** budget day with only **~$1.81** of the $5/UTC cap
left (s229 $3.182446 + s231 $0.005444 prior); forcing a >$1.3 run alongside this session's own freeze-critic
vote into ~$1.81 is the reckless move the budget rule (CLAUDE.md §8) and the s225-halt lesson warn against.
Per the **s228→s229 precedent**, the finding-bearing run is deferred to the next full-$5 UTC day; nothing has
been run or peeked (`raw/` empty). The C4-banded build + probe run at the deferred run, **independently
reproduced by a fresh-agent verifier before scoring** (G5-plus).

## What a completed run will (and will NOT) show

A **DEEP-STILL-DROPS** sharpens the exact-string / lexical-item memorization reading (R1 refused promotion
more firmly — a first-class negative). A **DEEP-SWAP-STABLE**, with the s208
[`result/blimp-profile-frequency-control-covariate-v1`](../results/blimp-profile-frequency-control-covariate-v1.md)
SURVIVES-COVARIATE, makes R1 a **bounded** cross-session promotion-review candidate. Either way the arm still
does **not** control **construction** frequency or template difficulty (G3′ travels), C4 is only a
pretraining **proxy**, and n = 3 models, per-model per-stratum, never pooled. This note records the freeze
only; the reading is the deferred result's to earn.
