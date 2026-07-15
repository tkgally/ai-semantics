# REVIEW — ratification of blimp-c4-matched-swap-arm-design (s232, fresh-agent adversarial reviewer)

> Independent cross-session ratifier (did not author the design). Verdict authority. One non-Anthropic
> decorrelation vote (`gpt-5.4-mini`, VOTE-ratify-s232.json, $0.004259 → ADOPT-WITH-MODIFICATION, convergent)
> is QA input. PROTOCOL §2.

**VERDICT: ADOPT-WITH-MODIFICATION** — adopt Q1-A / Q2-A / Q3-A as the ratified gates; freeze is conditioned
on four load-bearing numeric/seed pins (BLOCKERs 1–4) + four SHOULD-FIX. The gate *choices* are correct and
even-handed; the residual risk is entirely in numbers deferred to freeze on the one arm designed with the
prior drop known.

## 1. Overall — ADOPT-WITH-MODIFICATION
Dual-band (Q1-A) is the only option under which a surviving deep drop is uniquely attributable to
exact-string memorization net of both frequency channels; disjoint-fresh-both-strata with a fresh ORIGINAL
re-run (Q2-A) keeps Δacc free of known-accuracy exposure; the symmetric four-outcome map (Q3-A) is the
anti-cheat backbone, siblings correctly rejected. WITH-MODIFICATION (not ADOPT-DEFAULTS) because several
load-bearing quantities are still deferred as `~0.05`, `default ±0.30`, `consider`, "a numeric floor" —
and this is the arm built KNOWING the s210 deep-drop magnitudes (−0.095/−0.057/−0.072), so every unpinned
DoF is an anti-cheat surface. Not KEEP-OPEN: the value-laden choices are settled; what remains is blind
freeze-time computation.

## 2. Per-gate
- **Q1 → A.** Dual-band correct. ±0.30 is defensible precisely because it is a pool-feasibility knob, not
  the confound-closer (the downstream G-C4-match-adequacy set-mean ≤0.05 is the guarantee; a ±0.30 per-word
  cap forces the set-mean far below 0.05 by partial cancellation). Rule shape is genuinely blind (pool
  feasibility computable from SUBTLEX+C4 alone). Defect: numbers not yet stated, and both half-width AND
  dual-vs-primary switch float on feasibility (two knobs) — must collapse to one blind switch (BLOCKER 1).
- **Q2 → A.** Non-negotiable for this arm; Q2-C would re-inject known-accuracy exposure. Keep shallow-3
  destructive-control anchor. G-disjoint present + required.
- **Q3 → A.** Symmetric ±0.05 bands are the fence; B1's fourth outcome plugs the not-demonstrably-closed
  gap; candidacy bounded, cross-session only. B/C correctly rejected.

## 3. "Matched closely enough" (G-C4-match-adequacy)
Genuine BLIND success criterion in kind (frequency quantity, pre-model-call), and it decouples the verdict
from the band-width choice. Two seams: (a) threshold soft (`~0.05`) → pin exact `|signed set-mean gap| ≤ 0.05`
(BLOCKER 3); (b) binds set-mean only → add a per-word report + soft directional-cancellation check
(SHOULD-FIX 6). Numbers the freeze must pin: (i) per-position pool floor; (ii) Q1-A→Q1-B trigger; (iii) C4
half-width single pinned value or exact monotone rule (not both floating); (iv) exact 0.05 adequacy; (v)
single C4 stream scale; (vi) pinned RNG seed(s); (vii) exact S1 attrition fallback + ≥2-deep floor; (viii)
USABLE_FLOOR (60) + equivalence-power N.

## 4. Anti-cheat (known drop)
Existing fence strong and mostly sufficient (novel words + fresh disjoint ORIGINAL ⇒ no accuracy known at
freeze; symmetric bands; verifier-reproduced build; blind-scoring lock). Keep the blind-scoring lock as a
hard fresh-agent WRITTEN attestation (BLOCKER 4). One residual hole: **seed-shopping** — pinning the output
lexicon sha does not prevent scanning candidate seeds and committing the winner; the achieved set-mean C4
gap is a build-time quantity, so a designer could scan seeds for a lexicon that clears ≤0.05 AND selects
words suspected (from the known s210 result) to preserve/kill the drop. Predictive power weak but not zero.
Close at the seed (BLOCKER 2): one principled pre-announced date-derived seed for substitute selection AND
the disjoint subsample; PREREG forbids seed scanning; fresh-agent verifier attests the seed reproduces the
committed lexicon and no seed selection occurred.

## 5. Result-motivation — NONE
Verdict bands literally symmetric; the successor motivation (s210 scope-cap #4) leans toward the REFUSING
pole (a promotion-seeker would bet against the known prior drop); DEEP-SWAP-STABLE earns only bounded
candidacy deferred to a later cross-session review; "first-class negative" gets equal rhetorical weight.
The genuine risk is exposure (known drop), carried by §4 fences given BLOCKER 2.

## 6. Freeze conditions the ratifier requires
**BLOCKER (must-fix before freeze):**
1. Collapse Q1's two floating knobs to one blind switch — pin exact per-position pool floor + exact
   Q1-A→Q1-B trigger, with the C4 half-width fixed at a single pinned value (0.30) OR an exact monotone
   feasibility→half-width rule, not both floating. Verifier-reproduced.
2. Anti-seed-shopping — one pre-announced principled date-derived seed for substitute selection AND the
   disjoint subsample; PREREG forbids seed scanning; fresh-agent verifier attests the seed reproduces the
   committed lexicon and no seed selection occurred. Output-sha pinning alone is insufficient.
3. Harden G-C4-match-adequacy — exact `|signed set-mean C4 gap| ≤ 0.05` (drop `~`), computed pre-model-call
   at the pinned stream scale; below ⇒ STILL-INCONCLUSIVE-BY-MATCH-FAILURE.
4. Blind-scoring lock as a hard, fresh-agent, WRITTEN attestation — scoring code + exclusion criteria + the
   four-outcome decision table frozen before any re-run; verifier attests no human-readable intermediate
   output inspected until the full batch is scored.
**SHOULD-FIX:**
5. Firm S2 to a single pinned stream scale (22.3M ≫ the 3M prefix; quantization bites the rare deep words);
   band + adequacy-report at the same scale.
6. Per-word adequacy report + pre-committed soft check so a set-mean ≤0.05 achieved by within-band
   directional cancellation is visible.
7. State TOST equivalence power at expected post-attrition usable-N per deep paradigm; pin the exact S1
   attrition fallback (attrition-inconclusive vs re-verdicted deep-2, ≥2-deep-paradigm floor); size N toward
   ~150 pre-attrition if attrition threatens the ±0.05 equivalence CI.
8. Keep the refusing-pole successor motivation visible in PREREG as part of the not-result-motivated
   attestation the freeze critic signs.

On satisfaction of BLOCKERs 1–4, the ratified yardstick is Q1-A / Q2-A / Q3-A and the arm may freeze and run.
