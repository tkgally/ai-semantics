# RATIFICATION REVIEW — BLiMP forced-choice sweep gates (A3b), s205

**Decision:** [`decisions/open/blimp-forced-choice-sweep-design`](../../../wiki/decisions/open/blimp-forced-choice-sweep-design.md)
(opened s204, eligible s205+). **Procedure (PROTOCOL §2):** fresh-agent adversarial reviewer (verdict
authority) + one **fresh** non-Anthropic decorrelation vote (`gpt-5.4-mini`), cutoff-aware preamble. Both
independent of the s204 session that wrote the design. **Outcome: RATIFY-WITH-CONDITIONS — adopt
Q1-B / Q2-A / Q3-A; carry F2–F7; add binding C8.** Both reviewers converge on the three gate choices;
the fresh agent adds one promotion-blocking condition (C8), the vote adds a mechanical anti-cherry-pick
sharpening (already satisfied by the whole-category selection rule frozen at freeze).

---

## Fresh-agent adversarial reviewer (VERDICT AUTHORITY)

**ONE-LINE VERDICT: RATIFY-WITH-CONDITIONS** — adopt Q1-B / Q2-A / Q3-A as written, carry freeze
conditions F2–F7, and add one binding condition (**C8**) that closes the frequency-confound anti-cheat
gap: the PROFILE-ALIGNED human-comparison reading is **non-promotable to a `claim`** without a
training-frequency discriminator (the F7 content-word-swap arm, or a pre-registered frequency covariate
partialled from ρ_prof).

### A. Overall: RATIFY-WITH-CONDITIONS
Each gate choice is defensible; all three defaults adopted. The anti-cheat scaffolding (pre-registered ρ
bands with an explicit INCONCLUSIVE dead-zone, first-class PROFILE-DIVERGES / DEPTH-FLAT / instrument-
failure nulls, freeze-before-call fencing) is genuinely good and not result-motivated. F1 (the s204
critic's most-insisted blocker) is **genuinely discharged**: `human_validation_summary.csv` is committed
(69 rows, sha256 `ea0e7c21…`), `resource/blimp.md` catalogues the per-paradigm profile, and every human
value the design cites was independently confirmed to match the committed CSV verbatim (e.g.
`determiner_noun_agreement_1` 0.9578, `only_npi_scope` 0.72, `wh_island` 0.73,
`coordinate_structure_constraint_subject_extraction` 0.5142). No fabrication. Not unconditional because
one risk — non-uniform, human-agreement-correlated contamination — is the exact failure mode that would
*manufacture* the PRIMARY positive (PROFILE-ALIGNED), and its only real discriminator (F7) was
"recommended, not blocking." Elevating it is a yardstick tightening (legitimate under tighten-not-loosen),
not a rejection.

### B. Per-gate ruling
- **Q1 — ADOPT B** (depth-stratified curated subset), with the F6 sharpening. The curation objection is
  adequately defended by F6 (structural/locality selection, human-agreement-blind, excluded paradigms
  published). Crucially the committed data show the human profile is **not monotonic in structural
  depth** — `adjunct_island` (0.94) and `existential_there_quantifiers_1` (0.94) are structurally deep
  yet human-easy, while `distractor_agreement` (0.81/0.857) is shallower yet human-harder. That
  dissociation makes reading 1 (human profile) and reading 2 (structural depth) genuinely separable
  rather than circular, so a curated set cannot trivially bake in alignment. Full 67 (C) is not required,
  but if the structural rule cheaply yields >16 paradigms the freeze should prefer more.
- **Q2 — ADOPT A** (both-orders, position-bias-netted 2AFC). Correct and essentially uncontested: the
  behavioral analog of BLiMP's probability scoring for a logprob-free panel, with order-averaged accuracy
  primary, consistency accuracy as the bias-hardened robustness check, and order-flip rate as a pre-named
  INSTRUMENT-FAILURE diagnostic. The 2× cost is justified — uncontrolled position bias could masquerade
  as a per-paradigm profile signal, precisely the headline.
- **Q3 — ADOPT A** (genuine human-comparison anchor, not internal-contrast-only). Anchoring is the
  *honest* declaration: a real per-paradigm human key exists, so `internal-contrast-only` would be
  dishonest (it is the terminal state for results that make *no* human comparison; this one does).
  Contamination threatens the **validity** of the comparison, not its **type**. F3 guards the ceiling
  case (near-zero variance → INCONCLUSIVE) but **not** the moderate-variance case whose *ordering* is
  driven by training frequency correlated with human ease — which is why C8 makes the swap/frequency
  control promotion-blocking.

### C. Biggest remaining risk + condition
**Non-uniform, human-agreement-correlated contamination manufacturing a spurious PROFILE-ALIGNED.**
Frequent local-agreement constructions are plausibly both human-easy and most-memorized; rare
island/scope contrasts both human-harder and less-memorized. If exposure tracks `H(p)`, ρ_prof is
inflated by a training-frequency artifact, not shared grammatical-difficulty structure — with perfectly
healthy across-paradigm variance, so **F3 does not cover it.**

> **C8 (binding, mirrors the adjective-antonymy ratification's added C8):** A PROFILE-ALIGNED verdict
> (reading 1) is **non-promotable to a `claim`** unless a training-frequency confound has been controlled
> — either the F7 content-word-swap arm on ≥2 shallow and ≥2 deep paradigms (original-vs-swapped accuracy
> pre-registered), **or** a pre-registered corpus-frequency proxy for each construction partialled from
> ρ_prof — decided and frozen in PREREG before any model call. Absent this, reading 1 may run and be
> reported **descriptively only**, exactly as under the F2 low-n downgrade.

Two sharpenings (not new blockers): **(F6-sharp)** the strongest F6 classifies *all 67* structurally and
includes by a reproducible rule rather than hand-picking ~16, reducing the which-paradigms-enter DoF.
**(F2-note)** even at n=16 the +0.4 band sits *below* two-sided significance (Spearman needs ≈0.50 at
n=16); the freeze must state this and either raise n materially or hold reading 1 to
descriptive/directional.

### D. Anti-cheat check
1. **"Human-comparison framing" a way to claim a positive while absolutes are uninterpretable?** Honest
   as a *type* (a real key exists; relative profile survives a uniform boost; absolute demoted to upper
   bound). But a PROFILE-ALIGNED positive rides entirely on ρ_prof, the quantity the frequency confound
   can fabricate — which is exactly what C8 closes. With C8 the positive is earned only when the confound
   is controlled.
2. **"Reading 1 descriptive-only if underpowered" an escape hatch that quietly downgrades a null?**
   Answered by *symmetry*, made a **binding reading of F2**: promotability/descriptive-only status is
   determined solely by the freeze-time achieved-n power calculation, **before any model call**, and
   applies identically regardless of the observed sign of ρ_prof. So a PROFILE-DIVERGES null at low n is
   a first-class descriptive null, not buried. No thresholds/strata/selection reverse-engineered from
   accuracies; the non-monotonic human profile confirms the instrument can separate the two stories.

**Disposition:** RATIFY-WITH-CONDITIONS → move the decision to resolved with `resolved-by: autonomous
(adversarial review)`; add C8 to the design's freeze conditions; drop `anchor: pending` →
`anchors: resource/blimp`; clear `contingent-on:` at freeze.

---

## Non-Anthropic decorrelation vote (`gpt-5.4-mini`, QA input) — billed $0.0025515

**RATIFY-WITH-CONDITIONS.** Per-gate: **Q1-B** (structurally frozen depth-stratified ≥16-paradigm subset
is the right yardstick; full 67 muddies the axis) · **Q2-A** (both-orders 2AFC least biased; single-order
confounds position bias) · **Q3-A** (treat BLiMP as contamination-limited, absolute accuracy an upper
bound, center relative human-comparison analyses; contamination arm useful but not required for
ratification). **Biggest risk:** selection bias could silently optimize the correlation/depth result;
**partly covered by F6**, but add **one condition**: a *mechanical* inclusion rule strict enough to
prevent hand-picked exemplars **within** each stratum, reporting all excluded candidates with reasons.
**Anti-cheat:** "mildly" — Q1-B's framing still leaves room to curate a nicer subset; the extra
anti-cherry-pick rule closes it.

**Convergence:** both reviewers adopt Q1-B / Q2-A / Q3-A. The fresh agent (authority) adds C8
(frequency-confound → non-promotable). The vote's added mechanical anti-cherry-pick rule is **satisfied
at freeze** by the whole-category selection rule (take *every* paradigm in the on-axis `linguistics_term`
categories — no within-category / within-stratum hand-picking — and publish excluded categories with
structural reasons); this also realizes the fresh agent's F6-sharp ("classify all 67, include by a
reproducible rule"). Divergence: none on gate choices.

## How the freeze honors the ratification
- **Q1-B via the maximal defensible rule (F6-sharp + vote's mechanical rule):** select **all paradigms
  in the on-axis categories** (`determiner_noun_agreement`, the local + distractor split of
  `subject_verb_agreement`, `npi_licensing`, `quantifiers`, `island_effects`, `filler_gap_dependency`) →
  **40 paradigms**, well above F2's ≥16 floor and enough that ρ_prof is genuinely powered (n=40:
  two-sided p<0.05 at ρ≈0.31). Off-axis categories excluded with structural reasons.
- **C8:** reading 1 runs but is **descriptive/directional + non-promotable on this run alone**; the
  frequency-confound control (F7 swap arm / frequency-covariate partial) is pre-registered as the
  binding gate a later promotion-prep session must clear. The verdict-bearing outputs this run are
  reading 2 (within-panel depth gradient) and reading 2h (human-anchored excess-over-dip); a descriptive
  contamination diagnostic (per-model absolute-accuracy dispersion, F3) is reported.
- **F2 symmetry:** descriptive-only status is fixed by the freeze-time n=40 power calc, identical for
  PROFILE-ALIGNED and PROFILE-DIVERGES.
