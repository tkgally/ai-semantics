---
id: blimp-c4-matched-swap-arm-design
title: "BLiMP R1 C4-frequency-matched swap arm (the s210 SWAP-INCONCLUSIVE successor) — the value-laden operationalization gates: the C4-frequency-matching op (Q1 — the crux), the run scope + ORIGINAL baseline (Q2), and the disambiguation verdict + promotion rule (Q3)"
status: open
opened: 2026-07-15
opened-by: session-231
provisional-default: "Q1-A (DUAL-BAND: substitute matched within ±0.10 SUBTLEX-US Lg10WF AND within a pinned C4 log-frequency band, default ±0.30, of the original — the intersection pool, seeded-deterministic selection; controls both the human- and the pretraining-frequency channel per word; drop-and-log a position with an empty intersection, never widen the band) / Q2-A (re-run the SAME 6 s210 frame-safe paradigms, both strata, on a FRESH seeded ≈100-pair subsample DISJOINT from the s210 sample, ORIGINAL re-run fresh in-session → within-run paired Δacc with no known-accuracy exposure) / Q3-A (the symmetric disambiguation map: DEEP-STILL-DROPS → cleaner exact-string memorization, R1 refused more firmly; DEEP-SWAP-STABLE → the s210 drop was the C4 confound, SWAP-STABLE obtains, with s208 SURVIVES-COVARIATE R1 becomes a bounded promotion-review CANDIDATE, a later cross-session review writes the claim; STILL-INCONCLUSIVE → reported. Bounded to 'not exact-string memorization, not the surface freq proxy, not the pretraining-proxy freq gap' — still NOT construction-frequency-controlled). Ratifiable s232+ by a fresh-agent adversarial reviewer + one non-Anthropic decorrelation vote; freeze + run after ratification."
contingent-artifacts:
  - design/blimp-c4-matched-swap-arm-v1
---

# Decision: the operationalization gates of the BLiMP R1 C4-frequency-matched swap arm (A3b)

> **OPEN — opened session 231 (2026-07-15). Ratifiable s232+** (never in the session that opened it,
> PROTOCOL §2). Provisional defaults **Q1-A / Q2-A / Q3-A** (front-matter). The design that these gates
> govern: [`design/blimp-c4-matched-swap-arm-v1`](../../../experiments/designs/blimp-c4-matched-swap-arm-v1.md).
> The s231 pre-run design critic (fresh agent, verdict authority) + one non-Anthropic decorrelation vote are
> recorded under
> [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm-design/`](../../../experiments/runs/2026-07-15-blimp-c4-matched-swap-arm-design/).
> Nothing frozen, nothing run. Tom's standing override outranks any autonomous ratification.

## What is (and is NOT) at stake

The s210 content-word-swap arm ([`result/blimp-swap-arm-v1`](../../findings/results/blimp-swap-arm-v1.md))
returned **SWAP-INCONCLUSIVE**: the load-bearing **deep-scope** stratum dropped 3/3 under a
SUBTLEX-frequency-matched swap (Δ̄acc −0.095 / −0.057 / −0.072, all CIs exclude 0), but the drop is
**confounded by a +0.204 C4 pretraining-frequency gap** — the swap words matched the originals on the
**human** SUBTLEX-US `Lg10WF` norm yet were ~1.6× rarer in the C4 pretraining proxy. So the deep drop is
**neither** SWAP-STABLE **nor** a clean exact-string-memorization signal, and the result registered the fix
explicitly (scope cap #4): a **C4-frequency-matched** swap arm, "only then could a deep drop be read as
exact-string memorization rather than pretraining rarity." This decision fixes **how** that C4-matched arm is
built and scored. It does **not** re-open the ratified C8 gates (Q1-C both-arms, G8, the covariate/swap
requirement — all resolved s208/s210); those fix *that* the swap arm is required and *why*. The **measurement
instrument is inherited byte-frozen from s210** (elicitation, the 6 frame-safe paradigms, the substitution
recipe, the ±0.05 equivalence bands, the diagnostics); the **only new operationalization** is the
C4-frequency-matching of the substitute lexicon. This is a **disambiguation** of an INCONCLUSIVE landing into
two first-class, symmetrically-banded outcomes — not a promotion-seeking retune (the anti-cheat fence below).

## GATE Q1 (THE CRUX) — the C4-frequency-matching operationalization

A word can be human-frequent (high SUBTLEX) yet pretraining-rare (low C4), so a single-norm match on one norm
leaves a residual gap on the other. The choice: which norm(s) bind, how tightly.

- **Q1-A (provisional default) — DUAL-BAND.** Substitute matched within **±0.10 SUBTLEX-US `Lg10WF`** (the
  s210 band, kept) **AND** within a **pinned C4 log-frequency band** (default **±0.30 log-units**, pinned at
  freeze after a pool-feasibility check) of the original, per replaced word; eligible pool = the
  **intersection**, seeded-deterministic selection. Controls **both** frequency channels per word, so a
  surviving deep drop cannot be either a human- or a pretraining-frequency artifact. **Cost:** a thinner
  intersection pool ⇒ more dropped positions ⇒ possible power loss (restated per G-power); a position with an
  empty intersection is **dropped-and-logged**, never force-filled by widening the band.
- **Q1-B — C4-PRIMARY.** Match on the C4 band only; report (do not bind) the achieved SUBTLEX gap. Larger
  pool, less attrition; but **re-opens the human-frequency gap** the s210 arm controlled. The ratifier may
  prefer this if the dual-band pool proves unworkably thin.
- **Q1-C — SET-LEVEL C4 mean-match.** Match the swap-set mean C4 to the original-set mean, not per word.
  Cheapest on attrition; permits large per-item C4 mismatches that cancel in the mean. Admissible as a
  labelled sensitivity cross-check of Q1-A, not the default.

**Why value-laden.** Dual-band buys a two-confound-clean per-word Δacc at the cost of pool attrition/power;
C4-primary buys power by re-exposing the human-frequency channel; set-level buys the most power at the cost
of per-item match quality. The default pays attrition to control both channels per word — the whole point of
the successor arm being that *neither* frequency proxy can explain a surviving drop.

## GATE Q2 — run scope (which strata/paradigms) + the ORIGINAL baseline

- **Q2-A (provisional default)** — re-run the **same 6 s210 frame-safe paradigms, both strata**, on a **fresh
  seeded ≈100-pair subsample DISJOINT from the s210 sample**, **ORIGINAL re-run fresh in-session** →
  within-run paired Δacc, no known-accuracy exposure on either condition. Deep-3 load-bearing; near-ceiling
  shallow-3 the destructive-control anchor.
- **Q2-B** — deep-3 only (~$0.67); drops the cheap shallow anchor. Rejected as default.
- **Q2-C** — reuse the s210 ORIGINAL accuracies as baseline; re-introduces known-accuracy exposure +
  cross-session drift. Rejected (the s210 design rejected the identical option identically).

## GATE Q3 — the disambiguation verdict + the promotion rule

- **Q3-A (provisional default)** — the symmetric map on the C4-matched deep stratum (inherited G-metric):
  **DEEP-STILL-DROPS** (Δ̄ ≤ −0.05, CI excl 0, ≥2/3) → cleaner exact-string/lexical-item memorization, R1
  refused promotion more firmly (first-class negative); **DEEP-SWAP-STABLE** (Δ̄ CI within ±0.05, ≥2/3, both
  strata) → the s210 drop was the C4 confound, SWAP-STABLE obtains, and with the s208 **SURVIVES-COVARIATE**,
  R1 becomes a **bounded promotion-review CANDIDATE** (bounded to "not exact-string memorization, not the
  surface freq proxy, not the pretraining-proxy freq gap"; **still not** construction-frequency-controlled;
  a later cross-session review writes/refuses the `claim`); **STILL-INCONCLUSIVE** → reported. Promotion is
  **always cross-session** — this run earns candidacy, never ratifies.
- **Q3-B** — treat any stable outcome as a mere robustness datum, never re-open promotion. Too conservative
  (the s208 SURVIVES is in hand → a genuine two-confound-clean SWAP-STABLE is exactly the G8 conjunction the
  program pre-committed earns candidacy). Rejected.
- **Q3-C** — write the R1 claim this/the run session. Rejected (cross-session always).

## Anti-cheat fence (LOAD-BEARING — the s210 deep drop is KNOWN at design time)

Unlike the s210 arm (swapped accuracies unknown at freeze), this arm is designed knowing the s210 deep-drop
magnitudes. Three fences: (1) the **C4-matched condition's** accuracies are still unknown at freeze (novel
words, ORIGINAL re-run fresh on a **disjoint** sample) — no accuracy in the Δacc is known when the recipe is
frozen; the C4 band is a mechanical criterion, not an accuracy target. (2) The verdict map is **symmetric**:
DEEP-STILL-DROPS (refuse) and DEEP-SWAP-STABLE (candidacy) carry identical bands — a design *motivated by
wanting R1 promoted* is the anti-cheat violation the charter forbids, and the fresh-agent ratifier must
confirm the disambiguation framing is not result-motivated. (3) Build-only DoF, **verifier-reproduced**
before scoring (G5-plus); the C4 counting reuses the s208/s210 `build_cooc_c4.py` adapter import-pinned (no
new corpus adoption; the in-repo C4 license posture —
[`resource/cooccurrence-corpus-scouting`](../../base/resources/cooccurrence-corpus-scouting.md)).

## Freeze conditions that carry (from the s210 design + this design)

**Inherited byte-frozen from the s210 PREREG:** G-frame (frame-safe paradigm restriction; island/filler-gap
+ irregular_* excluded; scope-deep pole only, generality cost reported), G-metric (signed-CI TOST-style
equivalence, ±0.05 bands), G-coverage (0.50 floor; a low-coverage paradigm's verdict excluded), G-power (N≈100
fresh pairs, usable-pair floor, power-restatement), G-freq (achieved ±0.10 SUBTLEX gap reported), G3′ (the
construction-frequency caveat travels; controls exact-string memorization + now both frequency proxies, NOT
construction frequency), G8 (SURVIVES-COVARIATE ∧ SWAP-STABLE required for candidacy). **New this design:**
**G-C4-band** (the C4 band width pinned at freeze after a pool-feasibility check, never widened after seeing
survivors; empty-intersection positions dropped-and-logged), **G-disjoint** (the sample certified disjoint
from the s210 sample, independently re-verified at freeze), **G5-plus extended** (the ratifier checks the
disambiguation framing is not a promotion-seeking retune). The standard fences carry: PREREG before any build
or model call; independent freeze critic + one non-Anthropic vote; `ABORT_USD`; `predictions.md` row at
freeze; the s205 INSTRUMENT-FAILURE guard verbatim.

## What each ratification path licenses

- **ADOPT DEFAULTS (Q1-A / Q2-A / Q3-A):** freeze the dual-band C4-matched arm on the 6 s210 paradigms,
  disjoint fresh sample, symmetric disambiguation verdict; run one full-$5 UTC day (~$1.3–1.6).
- **ADOPT-WITH-MODIFICATION (e.g. Q1-B if the dual-band pool is too thin, or Q2-B deep-3 only for budget):**
  freeze with the modification recorded; the freeze session honors the ratified variant.
- **KEEP OPEN:** if the reviewer finds the disambiguation framing under-fenced or the C4-band feasibility
  unestablished, name what is missing and carry the decision forward.

## Instrument-line governor (recorded)

This is the **second** swap-type arm on R1 (s210 SUBTLEX-matched → this C4-matched); **not** yet at the
PROTOCOL §3 instrument-stopping threshold (3 null-yielding redesigns on one construct — and s208 SURVIVED, so
no null streak). A **third** swap redesign (e.g. the s210-named verb-swap-with-valence-guard arm) would trip
the governor and require a cross-session line-continuation review before it runs.
