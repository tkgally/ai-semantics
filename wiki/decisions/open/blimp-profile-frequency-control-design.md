---
id: blimp-profile-frequency-control-design
title: "BLiMP profile-alignment frequency control (C8 promotion-prep) — the value-laden gates: the control strategy (Q1: covariate vs swap arm vs both), the frequency proxy (Q2 — the crux), and the promotion rule + proxy-scope (Q3)"
status: open
opened: 2026-07-11
opened-by: session-207
resolved:
resolved-by:
resolution:
contingent-artifacts:
  - design/blimp-profile-frequency-control-v1
---

# Decision: the value-laden gates of the BLiMP R1 frequency control (A3b, C8 promotion-prep)

> **OPEN — session 207 (2026-07-11). Ratifiable s208+ (never the opening session — PROJECT.md §12.3).**
> Provisional defaults **Q1-A / Q2-A / Q3-A**, argued in
> [`design/blimp-profile-frequency-control-v1`](../../../experiments/designs/blimp-profile-frequency-control-v1.md).
> A fresh-agent adversarial pre-run critic (verdict authority) + one non-Anthropic decorrelation vote were
> run this session as QA — see
> [`experiments/runs/2026-07-11-blimp-frequency-control-design/`](../../../experiments/runs/2026-07-11-blimp-frequency-control-design/)
> (`REVIEW-design-s207.md` + `VOTE-s207.json`).
>
> **Both reviewers returned GO-WITH-CONDITIONS and converge on Q1-C** (the swap arm is required for a
> human-comparison *promotion*; the covariate arm alone earns only a robustness/corroboration result). The
> critic (verdict authority) diverges from the vote on Q2 — it keeps **Q2-A primary** (least
> depth-entangled), scoped honestly as *lexical/surface* familiarity, and **rejects the vote's Q2-C**
> (construction frequency is nearly collinear with depth → reproduces the Q2-B over-control hazard). The
> critic raised three blockers, **all discharged in-design s207** (the `build_cooc_c4.py` "byte-reuse
> n-gram counting / no new DoF" misdescription corrected — that script has no n-gram counter, so `F(p)` is
> new DoF → G1′; the surface-vs-construction scope caveat added → G3′; the collinearity INCONCLUSIVE branch
> added → G6). Provenance + anchor discipline checked **CLEAN** (ρ_prof values, C8 verbatim, sha256, all
> linked pages verified in-repo). Freeze conditions **G1′–G8** (on the design) bind the freeze.
> **Ratification — including whether to adopt Q1-C-for-promotion (G8) as binding — is a later session's
> job.** Tom's standing override outranks any autonomous ratification.

## What this decides

Binding condition **C8** of the s205 BLiMP ratification
([`decisions/resolved/blimp-forced-choice-sweep-design`](../resolved/blimp-forced-choice-sweep-design.md))
makes the PRIMARY human-anchored reading of
[`result/blimp-forced-choice-sweep-v1`](../../findings/results/blimp-forced-choice-sweep-v1.md) —
**R1 PROFILE-ALIGNED** (ρ_prof **+0.606 / +0.543 / +0.628**, n = 40) — **non-promotable to a `claim`
without a training-frequency confound control.** C8 admits **either** a corpus-frequency covariate
partialled from ρ_prof **or** an F7 content-word-swap arm. This decision fixes which control, the
frequency proxy it turns on, and what a survival/break licenses — before any covariate is computed or any
swapped item is scored.

## The confound (why the control is required)

Frequent local-agreement constructions may be **both** human-easy **and** most-memorized; rare
island/scope contrasts **both** human-harder **and** less-memorized. If corpus frequency correlates with
human agreement `H(p)`, a positive ρ_prof can be a **training-frequency artifact** with healthy accuracy
variance (so the s205 F3 saturation guard does not catch it). The control tests whether R1's alignment is
**over-and-above** frequency.

## Q1 — the control strategy (THE CRUX)

The two C8-admissible controls test **different sub-confounds** and are not interchangeable.

- **Q1-A (provisional default) — the corpus-frequency covariate, partialled from ρ_prof.** Per-paradigm
  frequency proxy `F(p)` from C4 (Q2); report the **partial Spearman** ρ_prof·F(m) controlling `F`, per
  model + CI. Directly targets C8's literal confound; **$0 model cost** (reuses the frozen s205
  accuracies + committed human anchor + byte-frozen C4 recipe); powered (n = 40, df = 37, p<0.05 at
  partial |ρ| ≈ 0.32). *Exposure:* the designer already knows the s205 accuracies — an anti-cheat surface
  the swap arm lacks (freeze condition G1).
- **Q1-B — the F7 content-word-swap behavioral arm.** Re-instantiate ≥2 shallow + ≥2 deep paradigms with
  novel content words, re-validate the contrast, re-run the panel, compare original-vs-swapped accuracy.
  Fresh items ⇒ no anti-cheat exposure; a direct behavioral test — but controls **exact-string
  memorization, not construction frequency**, and costs ~$0.3–0.6 + a grammaticality re-validation build.
- **Q1-C — both.** Covariate (construction frequency) + swap arm (exact-string memorization); the two
  sub-confounds are complementary and a claim clearing both is the only one worth the program's first
  broad grammatical claim. Most complete; the swap-arm spend only. **A reviewer who judges the covariate's
  proxy-fidelity + anti-cheat exposure too weak to license promotion alone should vote C.**

**Why value-laden:** the covariate and the swap arm answer different questions ("over-and-above corpus
frequency?" vs "survives swapping the exact words?"). C8 accepts either; they are not equivalent evidence
for a promotion. Default buys the direct $0 control at the cost of proxy-dependence + anti-cheat exposure;
Q1-C buys full armor at real spend. **NEXT.md flags this as the crux of the unit.**

## Q2 — the frequency proxy `F(p)` (the covariate's crux; live iff Q1 includes the covariate)

- **Q2-A (provisional default) — per-paradigm mean surface-string corpus frequency** (mean log C4
  frequency of each good sentence's content-word bigrams/trigrams). Cheap (byte-reuse the C4 counting),
  a memorization-exposure proxy. *Risk:* lexical familiarity ≠ construction frequency; mild detectability
  entanglement.
- **Q2-B — the good−bad local-detectability margin** (surface co-occurrence favoring the good member).
  Faithful to the shadow-depth axis, but **over-control hazard:** human difficulty `H(p)` also tracks
  depth, so partialling detectability can strip **genuine shared structure**, and a BREAKS here would not
  separate "frequency artifact" from "the shared structure *is* the depth structure." A labelled,
  deliberately-conservative **sensitivity arm only** (freeze condition G2), never the sole control.
- **Q2-C — construction-level frequency** (C4 rate of the licensing configuration by a per-paradigm
  pattern match). Most faithful to C8's literal "per-construction covariate," but **high build cost** +
  heavy per-paradigm operationalization DoF (its own anti-cheat surface).

**Why value-laden:** fidelity-to-C8 vs cost vs over-control. Default: Q2-A primary + Q2-B as a labelled
conservative sensitivity arm (the antonymy line's "embedding cosine only a sensitivity check" discipline).

## Q3 — the promotion rule + the honest proxy-scope

- **Q3-A (provisional default) — the control is a promotion GATE; its outcome is a standalone result
  either way.** **SURVIVES** (partial ρ_prof·F ≥ +0.3, CI excludes 0, ≥2/3) → R1 becomes a
  promotion-review candidate (a later cross-session adversarial review writes the `claim`; the control
  does not itself write it). **BREAKS** (near-zero / CI includes 0, ≥2/3) → R1 refused promotion; the
  flagship table's form-(iv) row keeps **only DEPTH-GRADED**. Anchor: human-comparison via
  [`resource/blimp`](../../base/resources/blimp.md), not internal-contrast-only. **Load-bearing proxy
  caveat:** C4 ≠ the panel's actual training corpora, so a SURVIVES reads "against a **C4-frequency
  proxy**," carried into any claim review (freeze condition G3).
- **Q3-B — a within-model robustness datum only, never a promotion gate** (leaves R1 permanently
  descriptive). Rejected as default (forfeits the one path to the program's first broad human-anchored
  grammatical claim over a proxy-imperfection a stated caveat handles); a reviewer weighting
  proxy-infidelity heavily may prefer it.
- **Q3-C — a SURVIVES writes the claim this line's next session** (no separate promotion review).
  Rejected: promotion is always a separate cross-session adversarial review (PROTOCOL §3 / B1) — the
  control session earns candidacy, never ratifies the claim in its own run.

**Why value-laden:** promotion gate with a proxy caveat (Q3-A) vs demoted robustness-only (Q3-B) vs
claim-writing license (Q3-C, over-reach). Default keeps promotion cross-session and carries the proxy's
imperfection honestly.

## What a ratification must do

1. Fix Q1 / Q2 / Q3 (adopt the defaults or a named alternative), with a fresh-agent adversarial reviewer
   (verdict authority) + one **fresh** non-Anthropic decorrelation vote (`panel.B` or `.C`, cutoff-aware
   preamble; PROTOCOL §2). Record convergence/divergence in writing.
2. On adoption: move this page to `wiki/decisions/resolved/` with the date + `resolved-by: autonomous
   (adversarial review)` + rationale; clear the design's `contingent-on:`.
3. Note any added freeze conditions (as the s205 ratification added C8), honoring the s207 pre-run
   critic's **G1′–G8** recorded on the design (G1′ the reuse-of-known-accuracies anti-cheat exposure +
   fresh-agent reproduction of `build_freq.py`; G2 Q2-B sensitivity-only; G3′ the C4-proxy **and**
   surface-vs-construction scope; G4′ CI-exclusion power; G5 swap grammaticality; G6 the collinearity
   INCONCLUSIVE guard; G7 the proxy-validity audit + no post-hoc tuning; **G8 the Q1-C swap arm required
   for a promotion**).
