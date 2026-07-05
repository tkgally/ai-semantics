---
type: result
id: relational-history-perturbation-v2
title: The history-perturbation arm — an INCONCLUSIVE first pass at the decisive commutativity test (no falsification, no certified null; the direction control caught a would-be spurious positive)
meaning-senses:
  - relational
  - distributional
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-12
updated: 2026-07-05
links:
  - rel: refines
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the history-perturbation arm (v2) — inconclusive, with a methodological catch worth the price

> **Status: proposed (2026-06-12).** The decisive test named by
> [`conjecture/commutative-convention`](../conjectures/commutative-convention.md) — does a fresh
> matcher's interpretation of a coined term track **where in the chronology** conflicting
> convention evidence lands? — run as designed in
> [`experiments/designs/relational-history-perturbation-v2.md`](../../../experiments/designs/relational-history-perturbation-v2.md)
> under a PREREG frozen after an independent pre-run critic pass. **Verdict, pre-registered
> rule, all three models: INCONCLUSIVE/MIXED** — the conjecture's falsification clause did
> **not** fire, and the commutative null was **not** certified either. **210 calls, $0.277
> billed ($0.290 with liveness/preflight), 0 missing costs.** Independent pre-run critic
> (two blockers fixed before any finding-bearing call) + independent post-run verifier (every
> field re-derived from raw from scratch, zero mismatches; verdict rule-walk confirmed, "no
> dodging in either direction"). Run record:
> [`experiments/runs/2026-06-12-relational-history-perturbation-v2/`](../../../experiments/runs/2026-06-12-relational-history-perturbation-v2/README.md).

> **Update (2026-07-05, session 183 — wiki-coherence pass).** This line moved on:
> [`result/relational-history-perturbation-v3`](relational-history-perturbation-v3.md) (2026-06-13)
> re-ran the test on a clean instrument and supersedes this run at the verdict level (still
> INCONCLUSIVE, now located as direction-fragile), and
> [`result/relational-history-perturbation-v4`](relational-history-perturbation-v4.md) (2026-06-14)
> decoupled the confound — the answer is text position, not stamped chronology.
> [`conjecture/commutative-convention`](../conjectures/commutative-convention.md) was then
> **FALSIFIED and retired 2026-06-16** via
> [`result/relational-spontaneous-recency-a`](relational-spontaneous-recency-a.md) (Option A,
> session 20; with the [`result/relational-stamp-comprehension-b`](relational-stamp-comprehension-b.md)
> gate, session 18), and the positive was promoted to
> [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## What ran

Per panel model, per v1 near-twin pair: a **constructed contradictory convention record** — 2
distinct descriptions of twin X + 2 of twin Y (the model's **own** v1 live-game descriptions,
uniform positive feedback), content multiset byte-identical — presented under **all 6 orders**
of {X,X,Y,Y} **× 2 presentation directions** ("earliest first" vs "most recent first", lines
physically reversed, chronology identical), with a **nonce** coined term (`ZIMVOR` etc.). A
recency-resolving (path-dependent) reader picks the chronologically-last twin in **both**
directions; an attention/adjacency artifact follows the *physically*-last line in both; a
commutative reader is invariant. Primary: ρ_chron (in-pair picks landing on the
chronologically-last-line twin; commutative ⇒ ≈0.5), clustered bootstrap over (pair × sample);
per-cluster manipulation gate (both twins' consistent controls correct). The
presentation-direction arm and the per-cluster gate were **forced by the pre-run critic**
(blockers B1/B2) before any finding-bearing call.

## The numbers (gated primary; reproduced from raw by the post-run verifier)

| model | gate (clusters passing) | ρ_chron fwd [CI] | ρ_chron rev [CI] | ρ_phys rev [CI] | verdict (pre-registered) |
|-------|------------------------|-------------------|-------------------|------------------|--------------------------|
| claude | 4/6 (acc 0.83) | **0.812 [0.708, 1.000]** | 0.476 [0.273, 0.700] | 0.571 [0.400, 0.737] | INCONCLUSIVE/MIXED |
| gpt | 1/6 (acc 0.42) | 0.500 [degenerate] | 0.667 [degenerate] | 0.333 [degenerate] | INCONCLUSIVE/MIXED — **effectively uninformative** |
| gemini | 2/3 (acc 0.83) | 0.667 [degenerate] | 0.667 [0.500, 0.833] | 0.500 [degenerate] | INCONCLUSIVE/MIXED — descriptive-only (3 clusters, pre-registered) |

(out-of-pair rates 0.000 / 0.361 / 0.083 — all under the 0.5 flag. "Degenerate" = zero-width
single-/identical-cluster bootstrap intervals, which **carry no inferential weight** — stated
per the verifier, not glossed as precision.)

## Reading it honestly

1. **The falsification clause did not fire.** No model — gated or ungated — shows ρ_chron CIs
   excluding 0.5 **on the same side in both presentation arms**, the pre-registered bar for a
   non-commutative (chronology-tracking) effect. The conjecture survives, **unfalsified**.
2. **The commutative null was not certified either.** Claude's forward-arm elevation (0.812,
   CI excludes 0.5) blocks the clean-null clause. The run is what its verdict says:
   inconclusive, not a null.
3. **The methodological catch is the run's most solid finding.** Claude's forward-arm effect —
   which under the *draft* (pre-critic) design would have CI-cleanly "falsified" the conjecture
   and been surfaced as a candidate constitution effect — **vanishes when chronology and prompt
   position are decoupled** (rev arm: ρ_chron 0.476). Where the reversed arm points anywhere,
   it points at *physically-last-line position* (ρ_phys 0.571), not chronology — though it
   never meets the pre-registered artifact clause either. The direction-control arm (critic
   blocker B1) converted a would-be spurious relational positive into an identified, unresolved
   position/chronology confound. This is the same lesson as v1's `reversed` arm, one level up.
4. **gpt is effectively uninformative**, not "mixed": 1/6 clusters passed its own manipulation
   gate (control acc 0.42, out-of-pair 0.361) — consistent with the frozen live-quality census
   (gpt's v1 descriptions were the weakest: its pair-2 sample failed live 4/4). Its zero-width
   single-cluster CIs decide nothing.

## What it licenses (and does not)

- It **neither falsifies nor meaningfully strengthens**
  [`conjecture/commutative-convention`](../conjectures/commutative-convention.md); the
  conjecture **stays `proposed`** and the decisive test **remains open** — this was the first
  attempt at it, not the last word. (The conjecture's own falsification bar — "a robust,
  CI-clean order/position effect" — was explicitly not met; equally, this run must not be
  cited as the bet "holding," only as the bet *surviving an attempt*.)
- It **adds a methodological constraint for every future trajectory probe**: chronological
  recency and prompt-positional recency must be de-confounded by design (the
  presentation-direction arm is now the house pattern), and elicitation must be
  truncation-proof.
- It says **nothing human-comparative**: the measure is the probe's own within-model contrast
  (`anchor: internal-contrast-only`, per the ratified relational-line posture — the trajectory
  measure "makes no human-comparison claim",
  [`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md),
  [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md)).

## Caveats (all disclosed; the verifier's defect list in full)

1. **Claude truncation is non-random and cell-correlated.** 11/72 mixed trials NA (double
   truncation at the raised 128-token cap), **all pair-2, 8 of them forward-arm**; 10 further
   truncated-but-parsed picks may be deliberation-mentions rather than final answers (9/10
   don't end on a label; 3 sit in the gated forward pool). The forward elevation **survives
   the pre-specified sensitivity cuts** (excluding pair 2 entirely: 0.750; NAs-as-out-of-pair:
   no clause flips; dropping truncated-parsed records: 0.769) — but its CI-clean status rests
   on the full 4-cluster set, and the pair-2 forward cells retain only 4/12 trials.
2. **Degenerate CIs** (gpt's single gated cluster; gemini's identical-rate clusters) are
   bootstrap artifacts; treated as weightless throughout.
3. **Latent rule defect for any v3** (verifier): the falsification clause has no
   minimum-cluster guard — a single gated cluster's zero-width CI could mechanically fire it.
   It did not fire here; a ≥k-cluster floor must be pre-registered next time.
4. **Pilot power**, again: ≤6 clusters/model/direction; only large consistent effects are
   detectable; constructed (not live) records; uniform positive feedback; text grids
   (ratified v1-scoped yardstick).
5. **v1 limitation logged per the PREREG's promise:** v1's history lines carried `round k:`
   labels, so v1's shuffled arm was in principle reconstructible by re-sorting; v2 removed the
   labels. This makes the v1 null *less* surprising, not more — recorded on the v1 page.

## Next (for a future session's backlog, not this one)

Truncation-proof elicitation (strict forced-format single-token answers); re-certified or
regenerated gpt stimuli; more clusters per cell (more pairs and/or fresh description harvests);
a ≥k-cluster guard in the decision rule; then, if the confound resolves, the live mid-game
perturbation and mixed-feedback arms the PREREG defers.
