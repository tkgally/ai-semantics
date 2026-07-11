---
id: blimp-swap-arm-design
title: "BLiMP R1 content-word-swap arm (C8 promotion-prep, Q1-C's second required control) — the value-laden operationalization gates: paradigm & item selection (Q1), the swap operationalization (Q2 — the crux), and grammaticality re-validation without human subjects (Q3)"
status: open
opened: 2026-07-11
opened-by: session-209
resolved:
resolved-by:
resolution:
contingent-artifacts:
  - design/blimp-swap-arm-v1
---

# Decision: the value-laden operationalization gates of the BLiMP R1 content-word-swap arm (A3b, C8 promotion-prep)

> **OPEN — session 209 (2026-07-11).** Ratifiable **s210+** (never the opening session; PROTOCOL §2). A
> fresh-agent adversarial reviewer + one non-Anthropic decorrelation vote fix Q1–Q3 next session; freeze +
> run follow. Tom's standing override outranks any autonomous ratification.
>
> **s209 pre-run critique + in-design discharge.** The fresh-agent critic (verdict authority) returned
> **GO-WITH-CONDITIONS** (concur Q1-A / Q2-A / Q3-A; provenance + anchor **CLEAN**) with **two BLOCKERS**,
> both **discharged in-design this session**, and the non-Anthropic vote converged (GO-WITH-CONDITIONS,
> Q1-A/Q2-A/Q3-A, $0.004603). **BLOCKER-1** (POS-preservation ≠ grammaticality-preservation where a swapped
> verb's subcategorization frame or a noun's irregular morphology is entangled with the contrast) →
> **Q1-A hardened to a frame-safe paradigm set** (regular det–noun + regular subject–verb agreement shallow;
> `npi_licensing` ∪ `quantifiers` deep; island/filler-gap + `irregular_*` excluded, deep-pole generality
> cost reported) + new freeze condition **G-frame**. **BLOCKER-2** (the parent's "e.g. |Δacc|≤0.05"
> mean-of-absolutes is un-ratified + noise-biased + under-powered at N=30) → **G-metric** (a signed-CI
> TOST-style equivalence test) + **G-power** (N≈100 paired items/paradigm; corrected cost 7,200 calls
> ≈ $1.3–1.6, under the $2.50 flag). Plus **G-lexicon-determinism** (seeded deterministic substitute
> selection; the only human DoF is membership) and **G-freq-pretraining** (a mandatory C4 pretraining-proxy
> frequency cross-check, closing the seam between the two arms). The promotion candidacy is **bounded**
> ("not explained by exact-string memorization or the tested surface frequency proxy" — not
> construction-frequency- or template-difficulty-controlled). Record:
> [`REVIEW-design-s209.md`](../../../experiments/runs/2026-07-11-blimp-swap-arm-design/REVIEW-design-s209.md)
> + [`VOTE-s209.json`](../../../experiments/runs/2026-07-11-blimp-swap-arm-design/VOTE-s209.json). Nothing
> frozen, nothing run.

## What is (and is NOT) at stake

Binding condition **G8** of the ratified C8 design
([`decisions/resolved/blimp-profile-frequency-control-design`](../resolved/blimp-profile-frequency-control-design.md))
made the **content-word-swap arm** of Q1-C **required for a human-comparison PROMOTION** of
[`result/blimp-forced-choice-sweep-v1`](../../findings/results/blimp-forced-choice-sweep-v1.md)'s reading
**R1 PROFILE-ALIGNED**. The s208 **covariate arm** already returned **SURVIVES-COVARIATE 3/3**
([`result/blimp-profile-frequency-control-covariate-v1`](../../findings/results/blimp-profile-frequency-control-covariate-v1.md),
a robustness result); per G8 the swap arm is the outstanding requirement, and **promotion candidacy needs
SURVIVES ∧ SWAP-STABLE**. **This decision does NOT re-open** Q1-C / Q2-A / Q3-A / G8 (all ratified s208) —
those fixed *that* the swap arm is required and *why*. It fixes only **how the swap arm is built and
scored**: the design [`design/blimp-swap-arm-v1`](../../../experiments/designs/blimp-swap-arm-v1.md) turns
that operationalization into three gates. Each is a yardstick choice, never a result — the bands are
pre-registered identically for SWAP-STABLE and SWAP-DROPS.

## The three gates (provisional defaults; ratified s210+)

### Q1 — paradigm & item selection (accuracy-blind AND human-agreement-blind)

The parent design fixes ≥2 shallow + ≥2 deep; the open choices are how many, which (by a structural
swappability rule, never by the s205 accuracies or human-agreement values), and what the ORIGINAL baseline
is.

- **Q1-A (provisional default, hardened s209 for frame-safety) — 3 shallow + 3 deep = 6 **frame-safe**
  paradigms** (regular det–noun + regular subject–verb agreement shallow; `npi_licensing` ∪ `quantifiers`
  deep; island/filler-gap + `irregular_*` **excluded**, deep-pole generality cost reported — G-frame), **by
  a deterministic frame-safe swappability rule; ORIGINAL = ≈100 fresh paired items/paradigm re-run fresh this
  session** (within-run paired Δ, no known-accuracy exposure; N≈100 for the equivalence test). ~7,200 calls,
  ~$1.3–1.6 (under the $2.50 flag).
- **Q1-B** — the ≥2 + ≥2 minimum (4 paradigms); cheaper, but no within-stratum replication.
- **Q1-C** — reuse the s205 frozen original accuracies as the baseline (do not re-run originals); halves
  the calls but re-imports the known-accuracy exposure the swap arm exists to escape.

### Q2 — the swap operationalization (THE CRUX): frequency-balancing norm + POS/morphology-preserving substitution

The swap is valid only if the replaced words are novel, **frequency-matched** (so a Δacc is not a frequency
drop — the covariate arm's confound must not re-enter), and **POS/morphology-preserving** (so the
grammatical minimal contrast survives, G5). The contrast locus and the whole closed-class functional
skeleton are held exactly; only open-class lemmas are swapped, re-inflected to the original features.

- **Q2-A (provisional default) — SUBTLEX-US `Lg10WF` banding + a frozen, hand-curated, POS-labelled content
  lexicon**, each replacement matched within **±0.10 `Lg10WF`** of the original.
  ([`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md) is license-verified,
  recipe-not-corpus, and already names this ±0.10 use; the plain 2009 file has **no POS**, so the POS
  labelling is a curation DoF, frozen + verifier-reproduced.) Matches on the **human-validated** frequency
  norm.
- **Q2-B** — fetch + license-check the 2012 "SUBTLEX-US with PoS" file for auditable POS selection (removes
  the curation DoF; adds a not-yet-in-repo fetch under the s168 no-unlicensed-adoption rule; fall back to
  Q2-A if the license check fails).
- **Q2-C** — C4 log-frequency banding (reuse the s208 machinery); balances the swap on the same corpus
  family as the covariate arm, but on a *pretraining proxy*, not the human-validated norm. Admissible as a
  labelled sensitivity cross-check only; rejected as primary.

### Q3 — grammaticality re-validation without human subjects (G5) + the honest promotion scope

The no-human-subjects rule means re-validation is mechanical, never a new human acceptability judgement.

- **Q3-A (provisional default) — mechanical construction-preservation + integrity check (POS/morphology
  match; contrast locus byte-identical; real-word membership in-band; no new agreement coincidence); a
  broken pair is dropped, logged, reported; a paradigm below a pre-registered usable-pair floor is dropped
  and power re-stated; the lead spot-audits a fixed sample as researcher (not subject).** Promotion scope:
  SWAP-STABLE ∧ (s208) SURVIVES → R1 becomes a promotion-review **candidate** (a later cross-session
  adversarial review writes the claim); SWAP-DROPS → refused, table form-(iv) keeps only DEPTH-GRADED.
- **Q3-B** — add an automated acceptability screen (frozen parser / off-panel LLM) to drop semantically
  anomalous swaps; tighter but its own DoF and risks importing a model's grammaticality opinion. Labelled,
  reported filter only if adopted.
- **Q3-C** — treat SWAP-STABLE as writing the R1 claim this session (rejected: promotion is always a
  separate cross-session adversarial review).

## Why each is value-laden (surface, don't smuggle)

- **Q1:** more paradigms buy within-stratum replication at linear spend; re-running originals buys a clean
  paired within-run Δ at 2× calls but preserves the swap arm's freedom from the known-accuracy exposure.
- **Q2 (the crux):** SUBTLEX-US (human-validated) vs C4 (pretraining-proxy) as the match norm changes what a
  stable/dropped result *means*; hand-curated vs fetched POS trades a DoF against a license-check build.
- **Q3:** purely-mechanical re-validation + a researcher spot-audit (respecting no-human-subjects, not
  importing a model's acceptability opinion) vs an automated acceptability screen with its own DoF; and
  whether a SWAP-STABLE earns candidacy or (over-reaching) writes the claim.

## The pre-named nulls (symmetry — the anti-cheat guarantee)

SWAP-DROPS (R1 rides on exact-string / lexical-item memorization — a first-class negative that refuses the
program its flagship claim), SWAP-INCONCLUSIVE (mixed across strata), an INSTRUMENT-FAILURE void, and a
paradigm dropped for too many broken-pair drops are **all pre-registered first-class outcomes**. Because the
swapped-condition accuracies are **unknown at freeze**, the swap arm carries **no known-accuracy exposure**;
its only DoF is the build, fenced by a fresh-agent verifier reproducing the swap-build from the recipe
before any item is scored (G5-plus).

## Provisional default (if not ratified, nothing runs)

**Q1-A (frame-safe) / Q2-A / Q3-A**, with freeze conditions **G5-plus, G-frame, G-metric, G3′ (travels),
G-freq, G-freq-pretraining, G-lexicon-determinism, G-power** and the standard fences (PREREG before any swap
build or model call; independent pre-run freeze critic + one non-Anthropic vote; `ABORT_USD`;
[`predictions.md`](../../predictions.md) row at freeze; the s205 INSTRUMENT-FAILURE guard verbatim; the
bounded-candidacy scope). The design is marked `contingent-on` this decision until ratified.

## Pointer for the ratifying session (s210+)

1. A **fresh agent** (not the s209 design author) runs the adversarial ratification review (verdict
   authority) + one **non-Anthropic** decorrelation vote (`panel.B`/`panel.C`), fixing Q1/Q2/Q3.
2. Weigh especially **Q2** (the crux): is SUBTLEX-US the right match norm, or should the swap be balanced on
   the same C4 proxy the covariate arm used (Q2-C), and is the hand-curated POS lexicon's DoF acceptable
   under G5-plus or does it warrant fetching the 2012 PoS file (Q2-B)?
3. Confirm the swap arm's **anti-cheat advantage** (unknown-at-freeze accuracies) is preserved by Q1-A's
   re-run-originals choice, and that G5-plus's verifier reproduction is adequate for the build DoF.
4. On ratification, clear the design's `contingent-on`, freeze (`build_swap.py` + `probe.py` +
   `analyze_swap.py` + PREREG, verifier-reproduced before scoring), and run (~$0.3–0.5).
