---
type: result
id: relational-history-perturbation-v3
title: The history-perturbation arm (v3) — the commutativity test on a clean, well-powered instrument, and still INCONCLUSIVE; the forward chronology signal does not survive direction reversal
meaning-senses:
  - relational
  - distributional
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: refines
    target: result/relational-history-perturbation-v2
  - rel: depends-on
    target: conjecture/commutative-convention
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the history-perturbation arm (v3) — the same verdict, now from a clean instrument

> **Status: proposed (2026-06-13).** The decisive test named by
> [`conjecture/commutative-convention`](../conjectures/commutative-convention.md) — does a fresh
> matcher's interpretation of a coined term track **where in the chronology** conflicting
> convention evidence lands, or only the content *set*? — re-run after the v2 post-run
> verifier's five-item fix-list was implemented, under a PREREG frozen post-critic
> ([`experiments/designs/relational-history-perturbation-v3.md`](../../../experiments/designs/relational-history-perturbation-v3.md)).
> **Verdict, pre-registered rule: INCONCLUSIVE/MIXED for the two informative models (claude,
> gemini); METHODOLOGICAL NULL for gpt.** The falsification clause did **not** fire and the
> commutative null was **not** certified. **384 finding-bearing calls, $0.386 billed ($0.611
> with all phases), 0 missing costs, 0 truncation, strict-compliance 1.000, 0 retries, 0 NA.**
> Independent pre-run critic (3 blockers + 6 should-fixes applied before any finding-bearing
> call) + independent post-run verifier (every field re-derived from raw from scratch, **zero
> mismatches**; it also flagged and corrected an over-claim in the first-pass reading — see
> §"Reading it honestly"). Run record:
> [`experiments/runs/2026-06-13-relational-history-perturbation-v3/`](../../../experiments/runs/2026-06-13-relational-history-perturbation-v3/README.md).

## Why a v3 at all

[`result/relational-history-perturbation-v2`](relational-history-perturbation-v2.md) returned
INCONCLUSIVE/MIXED, but its post-run verifier left a five-item defect list that made the
inconclusiveness hard to read as *substantive* rather than *instrumental*: claude lost 11
forward-concentrated trials to truncation (and 10 more truncated-but-parsed picks were suspect),
gpt passed only 1/6 of its own manipulation gates (weak live-game descriptions), clusters were
thin (≤6/model/direction), and the falsification clause had no minimum-cluster guard. v3 repairs
all five — **and the point of repairing them was to find out whether a clean instrument changes
the verdict.** It does not. That is the result.

The five fixes, and that they worked mechanically:

1. **Truncation-proof elicitation.** A reply with `finish_reason == "length"` is **never parsed
   for a pick** (parse-fail → stern retry → NA). Outcome: **0 truncation, 0 NA, 0 retries, strict
   compliance 1.000** across all 384 calls — the v2 truncation failure class is gone.
2. **Re-certified stimuli.** Descriptions were freshly harvested and **each individually
   certified** against the same model's own matcher before use (the disclosed bias direction
   sharpens the X-vs-Y conflict, which works *against* a spurious null). claude reached 9/9 and
   gemini 9/9 certified clusters; **gpt reached only 6/9 even after the one pre-registered
   top-up** (recorded shortfall) — its stimulus quality is still the weak point.
3. **More clusters** (9 nominal/model vs v2's ≤6) and (4) a **pre-registered ≥3-gated-cluster
   guard** plus **≥24-trial floor on falsification/artifact, ≥36 on null-certification**, so no
   single degenerate cluster can mechanically decide anything.
5. **Both presentation directions retained** (the v2 house pattern) — every chronology clause
   requires CI agreement in **both** arms.

This run must **not** be pooled with or numerically compared to v2 (different elicitation format,
fresh nonces, freshly-certified stimuli); v3 supersedes at the verdict level only.

## The numbers (gated primary; reproduced from raw by the post-run verifier, 0 mismatches)

| model | gate (clusters passing) | ρ_chron fwd [CI] | ρ_chron rev [CI] | ρ_phys rev [CI] | floors (24/36) | verdict (pre-registered) |
|-------|------------------------|-------------------|-------------------|------------------|----------------|--------------------------|
| claude | 5/9 (acc 0.83) | **0.600 [0.533, 0.667]** | 0.500 [0.367, 0.667] | 0.500 [0.400, 0.600] | 24 ✓ / 36 ✗ | INCONCLUSIVE/MIXED |
| gpt | 1/6 (acc 0.58) | 0.667 [degenerate] | 0.500 [degenerate] | 0.500 [degenerate] | ✗ / ✗ | **METHODOLOGICAL NULL** |
| gemini | 7/9 (acc 0.92) | **0.780 [0.659, 0.902]** | 0.595 [0.500, 0.738] | 0.500 [0.429, 0.571] | 24 ✓ / 36 ✓ | INCONCLUSIVE/MIXED |

(out-of-pair rates 0.000 / 0.236 / 0.009 — all under the 0.5 flag. "Degenerate" = zero-width
single-cluster bootstrap intervals, which **carry no inferential weight**. Forward ρ_chron and
ρ_phys are **identical by construction** in this design — the chronologically-last and
physically-last lines coincide in the forward arm — so the forward column alone cannot separate
chronology-tracking from position-tracking; only the reversed arm decouples them.)

## Reading it honestly

1. **The falsification clause did not fire.** The pre-registered bar for a non-commutative
   (chronology-tracking) effect is a CI-clean ρ_chron elevation **surviving both presentation
   arms with ≥24 gated trials/direction**. No model meets it. gemini — the one clean,
   well-powered read (gate 0.92, 7/9 clusters, both floors passed, 0 truncation) — shows a
   strong forward elevation (ρ_chron 0.780, CI excludes 0.5) that **does not survive reversal**:
   in the reversed arm ρ_chron drops to 0.595 with a CI whose lower bound sits **exactly at
   0.500**. The conjecture survives, unfalsified.
2. **The commutative null was not certified either.** gemini's CI-clean forward elevation blocks
   the clean-null clause; claude's floor36 is unmet (30 < 36) and its arms disagree (forward CI
   excludes 0.5, reverse does not). The run is what its verdict says: inconclusive.
3. **The corrected interpretation (the post-run verifier's catch).** A first-pass reading called
   this "physical position, not stated chronology." **That is an over-claim and is not what the
   data show.** A pure physical-position-following account predicts the reversed-arm ρ_phys to be
   *above* 0.5 (the matcher would keep following the physically-last line) — but gemini's
   reversed ρ_phys collapses to **exactly 0.500 (chance)**, which *refutes* that account, not
   supports it. And because forward ρ_chron ≡ ρ_phys by construction, the forward elevation
   cannot be attributed to position over chronology either. **The only defensible claim is the
   weaker one: the forward elevation does not survive direction reversal under *either*
   interpretation** — so whatever drives the forward picks (chronology, position, a recency
   heuristic, or a forward-only prompt-shape effect), it is not a stable, direction-invariant
   tracking of *where* conflicting evidence lands. The position-vs-chronology question itself
   stays open; this design does not resolve it.
4. **gpt is a METHODOLOGICAL NULL, not "mixed."** Even after certification + the one top-up, gpt
   passed only 1/6 of its own both-twin manipulation gates (control acc 0.58, out-of-pair
   0.236), so it carries **no commitment-bearing commutativity signal** despite a degenerate
   single-cluster forward ρ_chron of 0.667. gpt's description quality has been the relational
   line's weak link since v1; this is the cleanest statement of it yet.

## What it licenses (and does not)

- It **neither falsifies nor certifies**
  [`conjecture/commutative-convention`](../conjectures/commutative-convention.md); the conjecture
  **stays `proposed`**. But the *character* of the inconclusiveness has changed: v2 was
  inconclusive partly because the instrument was muddy; v3's instrument is clean (0 truncation,
  gemini at full power), and it is **still inconclusive because the forward signal is
  direction-fragile**. That is a more informative null than v2's — it locates the open question
  precisely (a forward-only elevation of unknown origin) rather than leaving it under
  instrumental noise. The decisive test **remains open**; this run must not be cited as the bet
  "holding," only as the bet surviving a second, cleaner attempt.
- It **confirms the v2 methodological constraints as load-bearing**: truncation-proof
  elicitation and the direction-control arm both did real work here (the former eliminated the
  NA class; the latter dissolved gemini's forward elevation). Both are now the house pattern for
  trajectory probes.
- It says **nothing human-comparative**: the measure is the probe's own within-model contrast
  (`anchor: internal-contrast-only`, per the ratified relational-line posture — the trajectory
  measure makes no human-comparison claim,
  [`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md),
  [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md)).

## Caveats (all disclosed)

1. **gpt remains uninformative** for the commutativity question (1 gated cluster); the relational
   line cannot read gpt on this test until its description quality clears certification at more
   than 6/9 clusters. Fresh per-model description harvesting, or dropping gpt from this
   particular probe, is the v4 choice.
2. **claude is under-powered** (floor36 unmet, 30 gated in-pair trials/direction; 5/9 clusters)
   and its leave-one-pair-out sensitivity cuts drift between INCONCLUSIVE/MIXED and the named
   gap sub-label (descriptive only; the primary verdict is unaffected).
3. **The forward arm cannot separate chronology from position by construction** — only the
   reversed arm decouples them, and at this power the reversed arm lands at/near chance. A design
   that separates the two *within* a single arm (e.g. a non-adjacent perturbation point) is the
   real next step if the position-vs-chronology question is to be answered rather than bounded.
4. **Scope limits (from the frozen PREREG, repeated per the verifier):** stimuli are
   **harvested-and-certified, not live-game by-products**; certification selects for
   **individually decodable** lines, so the result is conditional on evidence lines that work
   singly and says nothing about conventions whose lines are only interpretable in context; any
   verdict holds **under forced-label elicitation** only (suppressing visible deliberation could
   change the pick mechanism); the both-directions requirement is two **correlated** tests (same
   clusters/stimuli), not two independent ones; a symmetric serial-position profile would dilute
   ρ_chron toward 0.5 in both arms — a bias *toward* the conjecture's own bet, disclosed.
5. **Pilot power**, still: ≤9 clusters/model/direction; constructed (not live) records; uniform
   positive feedback; text grids (the ratified v1-scoped yardstick).

## Provenance / reproduction

Run dir [`experiments/runs/2026-06-13-relational-history-perturbation-v3/`](../../../experiments/runs/2026-06-13-relational-history-perturbation-v3/README.md):
frozen `PREREG.md` (sha256-pinned `stimuli.json`), `harvest.py` / `certify.py` /
`build_trials.py` / `probe.py` / `analyze.py`, raw JSONL per model, `analysis.json`, and
`VERIFIER-REPORT.md` (independent re-derivation, 0 mismatches; the over-claim correction in §3
is the verifier's). Refines [`result/relational-history-perturbation-v2`](relational-history-perturbation-v2.md);
`anchor: internal-contrast-only`; `contingent-on: []`.
