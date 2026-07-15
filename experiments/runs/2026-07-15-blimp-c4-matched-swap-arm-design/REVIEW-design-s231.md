# Pre-run design critique — BLiMP R1 C4-frequency-matched swap arm (s231)

**Design under review:** [`design/blimp-c4-matched-swap-arm-v1`](../../designs/blimp-c4-matched-swap-arm-v1.md);
gates [`decisions/open/blimp-c4-matched-swap-arm-design`](../../../wiki/decisions/open/blimp-c4-matched-swap-arm-design.md).

Two independent reviews per PROTOCOL §2/§A3: a **fresh-agent adversarial pre-run critic** (verdict authority,
did not author the design) and one **non-Anthropic decorrelation vote** (QA input, `panel.B` = `gpt-5.4-mini`,
`VOTE-s231.json`, **$0.005444**). Both converged **GO-WITH-CONDITIONS / Q1-A / Q2-A / Q3-A**. The critic's
two BLOCKERS + three SHOULD-FIX are **discharged in-design this session** (the s209 precedent: pre-run
BLOCKERS on a *design* are folded into freeze-time conditions; the design stays `draft`, ratifiable s232+).

## Fresh-agent critic (verdict authority) — GO-WITH-CONDITIONS

- **Per-gate:** Q1 → A (dual-band the only thing that makes a surviving drop uniquely exact-string), Q2 → A
  (disjoint fresh both strata, ORIGINAL re-run fresh — keeps Δacc exposure-free), Q3 → A (genuinely
  symmetric, but the outcome set was incomplete — see B1).
- **Provenance/anchor CLEAN.** Every quoted figure matches its source page verbatim (s210 deep drops
  −0.095/−0.057/−0.072; C4 gap +0.204 from orig 2.817 vs swap 2.614 over exactly 3,000,000 sentences; s208
  partials +0.572/+0.510/+0.606; ρ_prof +0.606/+0.543/+0.628). All three cited resources exist and bear on
  the design. One flag: `resource/cooccurrence-corpus-scouting` is a `status: scouting` page and C4 was never
  formally *adopted* as a corpus resource (used via the `build_cooc_c4.py` adapter) — citing it for the C4
  license posture is accurate and the only correct in-repo target, but the scouting-status lean is flagged.
- **Anti-cheat:** adequately fenced, conditional on B2 + S1. Notably the registered successor motivation
  (s210 scope-cap #4) tilts toward the *refusing* pole, which cuts against a promotion-seeking read. No prose
  is outright result-aimed.

### BLOCKERS (discharged in-design s231)

- **B1 — no achieved-match success criterion + no match-failure outcome.** The design pinned the *input* C4
  band (±0.30) but never pre-registered *how closed is closed enough*. Pool-availability asymmetry (for a
  C4-rare original, in-band substitutes may exist only above it; for a common one, only below) + coarse
  3M-count quantization for exactly the rare deep-scope words that drove +0.204 can leave a **residual
  directional set-mean gap** even with per-word banding. → **Discharged: G-C4-match-adequacy** — pre-register
  reporting the achieved **per-word AND set-mean** C4 gap, require |achieved set-mean gap| **≤ ~0.05**
  (comparable to the achieved SUBTLEX gap of 0.049), else a pre-named **STILL-INCONCLUSIVE-BY-MATCH-FAILURE**
  outcome (added to Q3 / the verdict map). A yardstick condition, not outcome-aiming.
- **B2 — pool-feasibility check is not a blind, rule-based GO/NO-GO.** "Band width pinned after a
  pool-feasibility check" with no numeric floor + no pre-committed Q1-A→Q1-B trigger leaves the band width +
  the dual-vs-primary choice selectable *after seeing which words survive*, knowing the s210 result. →
  **Discharged: G-C4-band tightened** — pre-register a numeric per-position intersection-pool floor + the
  exact Q1-A→Q1-B fallback trigger, decided before any swap item is built and blind to accuracies.

### SHOULD-FIX (folded)

- **S1 — paradigm-attrition seam.** If C4-attrition pushes a deep paradigm below `USABLE_FLOOR=60`, dropping
  it re-weights the deep Δ̄ — and `only_npi_scope` was the noisy INCONCLUSIVE-driving paradigm in s210. →
  Pre-register (before build) whether a below-floor deep paradigm yields **attrition-inconclusive** vs a
  re-verdicted **deep-2**.
- **S2 — larger C4 stream for banding.** Consider the covariate arm's 22.3M-sentence C4 (vs the 3M
  diagnostic) so per-word bands aren't quantization-limited for rare words; keep the achieved-gap report at
  the **same** stream scale as the band. → Recorded as a freeze option.
- **S3 — ±0.30 motivation is loose.** "Narrower than the +0.204 gap" conflates a per-word half-width with a
  set-mean gap (and ±0.30 > 0.204 anyway). → Re-motivate the half-width on pool-feasibility + achieved-gap
  grounds, not that phrasing.

## Non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.005444) — GO-WITH-CONDITIONS, Q1-A/Q2-A/Q3-A

Convergent. Its conditions align with and reinforce the critic's: **(i)** intersection-pool **selection
bias** — a nonrandom eligible subset could become a new item-selection confound; pre-register per-paradigm
eligible-fraction diagnostics + an **attrition cap** (≈ B2 + S1). **(ii)** a hard **blinding** guard given the
known prior direction: lock the scoring code + exclusion criteria + the three-outcome decision table before
any re-run, and require the verifier to attest **no human-readable intermediate outputs are inspected until
the whole batch is scored** (folded into G5-plus/blind-scoring). **(iii)** mild caution that the "bounded
candidacy / first-class negative" framing and the dual-band's ambiguity-tolerance are outcome-sensitive — met
by the symmetric bands + B1's match-failure pole + the blind-scoring guard.

## Disposition

All B1/B2/S1/S2/S3 + the vote's blinding guard are **folded into the design + decision this session**. Nothing
frozen, nothing run. Ratifiable s232+ (fresh reviewer + one non-Anthropic vote); freeze + run after
ratification.
