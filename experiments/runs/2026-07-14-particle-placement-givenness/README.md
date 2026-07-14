# 2026-07-14 — verb-particle placement object-givenness probe (program A5, session 225)

The **third** production-side sibling of program A5 (after the dative and genitive). Tests whether the
panel's **verb-particle placement** preference (joined *picked up the box* vs split *picked the box up*)
shifts in the **human-direction** (definite/given object → split; Kim et al. 2016 / Gries 1999), and —
the crux — whether that shift **survives a byte-identical discourse-givenness firewall** or is merely the
model reading off which order-string it has seen more often. The same information-structural driver as the
dative, on a new construction → a **cross-construction generalization** test.

## Pipeline

1. `build_items.py` → `stimuli.json` (frozen; sha in `PREREG.md`) + `certification.json`. 40 frames ×
   {Arm 1 definiteness (definite/indefinite), Arm 2 firewall (GIVEN/NEW-MENTIONED/NEW), Arm 3 length
   (short/long)} × A/B = 560 trials. Certifies Arm-2 scored strings byte-identical across the three
   context conditions ⇒ every scored-string shortcut reader yields within-frame Arm-2 shift 0; Arm-2
   context parallelism (matched length/clauses, noun 1/1/0, no leak); firewall arm ≥ definiteness arm.
2. `build_cooc_particle.py` → `freq_control.json` (frozen; sha in `PREREG.md`). The corroboration
   covariate: per-(verb+particle) marginal SPLIT-order rate from UD English-EWT (CC BY-SA 4.0, license
   verified firsthand s218). Near-vacuous — only 16/38 stimulus verb+particle pairs have any corpus
   token (honest power note in-file / PREREG); CONFIRM rests on Arm 2.
3. `ratify_vote.py` → `VOTE-ratify-s225.json` (non-Anthropic decorrelation vote for the ratification).
4. `probe.py liveness` (format gate) → `probe.py full` (1,680 calls; refuses unless both shas are in
   `PREREG.md`) → `raw/probe-<model>.jsonl`.
5. `analyze.py` → `analysis.json`: within-frame shifts (definiteness / firewall GIVEN−NEW-MENTIONED /
   length), covariate-adjusted intercept + predictive validity, the asymmetric pre-registered verdict.

## Ratification (s225, cross-session adversarial review)

Decision [`decisions/resolved/particle-placement-anchor-and-indicator`](../../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
→ **ADOPT-WITH-MODIFICATION** (Q1-A object givenness / Q2-(i) graded FC + byte-identical three-condition
firewall / Q3 human-anchored on direction), binding conditions R1–R7. Fresh reviewer record:
[`REVIEW-ratify-s225.md`](REVIEW-ratify-s225.md); weighed non-Anthropic vote [`VOTE-ratify-s225.json`](VOTE-ratify-s225.json)
(voted **REJECT** — weighed-and-addressed, not a veto; see the review for the point-by-point disposition).

## Independent Arm-2 certification (freeze (ix), R2/R3)

A non-authoring fresh agent certified the discourse-context parallelism → **CERTIFY-A**: R2(a) noun
mention/recency matched; R2(b) GIVEN discourse-given vs NEW-MENTIONED referentially-new (noun primed);
R2(c) no structural-priming leak; R3 the definite object comparably felicitous (accommodation cost is the
signature of non-givenness, not a rival construct). Advisory non-blocking noun-naturalness notes
(`valve`, `drawer`, `branch`, `thread`) recorded; byte-identity means they cannot bias the decisive
contrast, so the certified set is frozen as-is.

## The shadow control (the crux)

- **Byte-identical three-condition firewall (Arm 2) = the shortcut-immune LOAD-BEARING control (carries
  the CONFIRM).** The object string is byte-identical across GIVEN/NEW-MENTIONED/NEW; only the preceding
  context varies. No scored-string statistic can move shift₂. The decisive **GIVEN − NEW-MENTIONED**
  contrast holds object-noun lexical priming/recency constant → isolates referential information structure.
- **Covariate = corroboration (near-vacuous).** UD-EWT particle-verb tokens are sparse; `analyze.py`
  reports its own predictive validity (b1, R²). CONFIRM rests on Arm 2 (R1/R7); framed narrowly
  directional — no "distributional shadow defeated" (the firewall excludes scored-string shortcuts +
  lexical recency, not pretraining joint-distribution mimicry).

## Result

→ `result/particle-placement-givenness-v1` (written after the run; post-run fresh-agent verifier record
in that page). Frozen run dir — do not re-run/retune; a FALSIFY/reversal triggers a pre-registered v2.
