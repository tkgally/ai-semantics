---
type: design
id: relational-history-perturbation-v2
title: Relational v2 — the history-perturbation arm (mid-trajectory reassignment; the decisive commutativity test)
meaning-senses:
  - relational
  - distributional
status: ready
contingent-on: []
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: operationalizes
    target: conjecture/commutative-convention
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: concept/relational-meaning
---

# Design: relational history-perturbation probe (v2)

**The decisive test** named by
[`conjecture/commutative-convention`](../../wiki/findings/conjectures/commutative-convention.md)
(§"What would confirm / falsify") and recommended as the v2 arm by the ratified
[`decisions/resolved/relational-pilot-operationalization`](../../wiki/decisions/resolved/relational-pilot-operationalization.md):
**reassign a coined term mid-trajectory and test whether a fresh matcher's interpretation tracks
*where* in the order the change lands**, with the record's content multiset held byte-identical.

## Logic

The v1 null ([`result/relational-reference-game-v1`](../../wiki/findings/results/relational-reference-game-v1.md))
showed order-scrambling a *static, consistent* convention record does not change interpretation.
The conjecture's sharper bet concerns a record that is **internally inconsistent in a
chronology-resolvable way**: a **constructed contradictory description-set** in which the
record's evidence supports twin X early and twin Y late (the mid-trajectory "reassignment" is
simulated by composition from real v1 descriptions, not a live repair — the nonce never appears
inside the history). A path-dependent convention reader resolves the conflict by **recency**
(the convention is what it settled on *last* — the repair reading); a commutative, set-based
reader is **order-invariant** (the same 2-vs-2 content bag, however arranged, yields the same
pick distribution). Holding the multiset fixed and permuting positions turns "where the change
lands" into the *only* varying signal — the cleanest available isolation of trajectory
information. A **presentation-direction control arm** (earliest-first vs most-recent-first
rendering of the identical chronology) separates genuine chronology-tracking from a bare
prompt-position/attention artifact — the falsification clause fires only if both arms agree.

## Method (full freeze in the run's `PREREG.md`)

Per panel model, per v1 near-twin pair: records of 4 lines — 2 distinct v1 live-game
descriptions of X + 2 of Y, the model's **own** v1 descriptions, uniform positive feedback —
under **all 6 orders** of {X,X,Y,Y} **× 2 presentation directions** (fwd/rev); coined term = a
frozen **nonce** (`ZIMVOR`/`QUEXTAL`/`DRUBNIK`), so the record is the only signal. A fresh
matcher (v1 probe prompt shape; one pre-registered change — **no round-number labels**, order
purely positional + stated direction) picks the figure. **Primary:** chronological recency-pick
rate ρ_chron per direction (in-pair picks landing on the chronologically-last-*line* twin);
commutative ⇒ ρ_chron ≈ 0.5 in both arms; clustered-bootstrap CIs; ρ_phys (physically-last
twin) is the artifact diagnostic. **Gate (per cluster):** both twins' consistent-record
controls correct — clusters failing their own gate are excluded from the gated primary (an
independent pre-run critic found 15/60 harvested descriptions failed live in v1; census frozen
in `stimuli.json`). Decision rule (both-arms-agree falsification; physical-position-artifact
verdict; two-sided recency/primacy), power caveats, and multiplicity note are frozen in
`PREREG.md` before any finding-bearing call. 210 calls, est. ≈$0.35 (≤$0.80 bound).

## Anchor posture

Internal within-model contrast; **no human-comparison claim** (`anchor:
internal-contrast-only` posture, per the ratified relational line). Hawkins anchors nothing
here. The conjecture's human-contrast clause (conceptual pacts) remains a characterized
prediction pending Brennan & Clark 1996.

## Run

[`experiments/runs/2026-06-12-relational-history-perturbation-v2/`](../runs/2026-06-12-relational-history-perturbation-v2/PREREG.md)
— `build_stimuli.py` (frozen sha256 in PREREG) → `probe.py` (liveness/preflight/full) →
`analyze.py` → result page.
