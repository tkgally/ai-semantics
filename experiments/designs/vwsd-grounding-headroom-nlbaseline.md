# Design — VWSD grounding-headroom NL-baseline probe (magnitude follow-up; BUILT + FROZEN s127, DEFERRED at the audit gate)

> **SESSION 127 OUTCOME (2026-06-28): BUILT + FROZEN, then DEFERRED by a fresh pre-run-critic NO-GO.**
> The channel was authored (1158 fluent NL descriptions, claude, names allowed; competent on
> inspection), the TEXT-NL arm ran (acc .833/.767/.842; `sep_nl_i` strata under-det 18 / sat 77, both
> clearing the ≥15 floor), and the held-out adequacy audit ran (gpt+gemini). The audit landed **OUT OF
> BAND** (two-auditor mean high-recovery **0.342** < the `[0.60,0.95]` lower bound) → a pre-run-critic
> **NO-GO that defers the magnitude read and relaxes nothing; the reused IMAGE arm was NOT read.** An
> independent critic verified the NO-GO is a **scorer-validity artifact, not a degenerate channel**
> (~64/70 "none" items are faithful category recoveries the literal-target-word-lemma scorer mis-scored;
> the design-B.4 gap). Outcome recorded:
> [`result/vwsd-grounding-headroom-nlbaseline-audit-v1`](../../wiki/findings/results/vwsd-grounding-headroom-nlbaseline-audit-v1.md);
> run dir `experiments/runs/2026-06-28-vwsd-grounding-headroom-nlbaseline/` (`PRERUN-CRITIC.md`). The
> magnitude read is now gated on a **valid recovery-scoring rule** —
> [`decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity`](../../wiki/decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md)
> (opened s127, eligible s128+; default Q-A = held-out model re-grade of category match). All frozen
> artifacts are reusable verbatim; the re-attempt owes a cross-session-ratified re-grade + a fresh
> critic GO, **no re-authoring spend**.

> **SESSION 128 OUTCOME (2026-06-28): re-graded under the ratified VALID scorer → STILL DEFERRED (clean
> degenerate NO-GO).** The scorer-validity decision was ratified cross-session (ADOPT Q-A WITH
> MODIFICATIONS: held-out two-judge **cross-only category-match** re-grade of the stored guesses vs the
> human gold `{word, phrase}`, band `[0.60,0.95]` fixed) and the stored auditor guesses were re-graded
> (480 text-only calls, `regrade.py`, frozen rubric sha `55a67e39…` committed before the run; no images).
> The re-graded band metric is **0.438** — *higher* than the literal-lemma 0.342 (the literal scorer was
> partly under-counting) but **still below the 0.60 floor**, a **degenerate-side NO-GO**. A fresh
> independent pre-run critic ([`PRERUN-CRITIC-REGRADE.md`](../runs/2026-06-28-vwsd-grounding-headroom-nlbaseline/PRERUN-CRITIC-REGRADE.md))
> verified the 0.438 is a **valid** strict-recovery rate (HIGH verdicts not rubber-stamped; PARTIAL/NONE
> not over-strict; κ 0.608) — **not** a scorer artifact this time — so the s127 "channel is competent"
> optimism is not borne out, the IMAGE arm is **still not read**, and **prediction 3 remains UNTESTED.**
> Outcome: [`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../../wiki/findings/results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md).
> On VWSD this competence-audited fluent-channel route to the magnitude is **blocked under the ratified
> standard**; a different magnitude instrument may be needed. (Non-blocking nuance queued in `NEXT.md`:
> the band was calibrated on the literal-lemma floor; re-deriving it on the category-match metric would
> only *raise* the floor, strengthening the NO-GO — it does not rescue the run.)

**Status:** built + frozen, magnitude read deferred (competence standard ratified 2026-06-27, session 123) — the
operationalization decision [`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../wiki/decisions/resolved/vwsd-nlbaseline-competence-dv.md)
was **ratified cross-session (ADOPT-DEFAULT Q1-C)**, so the competence standard the whole magnitude read
hinges on is now **fixed in shape** (fresh fluent descriptions under a fixed plain-naming policy **plus**
a held-out adequacy audit with a pre-registered two-sided target band). **The design is NOT yet frozen
and no result is cleared:** a LATER session must still (1) author the NL descriptions to that standard
and pin the deferred numbers — the audit's **band edges**, the **held-out audit model** identity, and
the **recovery-scoring rule** (the ratification fixed the standard's *shape*, not these figures).
**Those three numbers were ratified cross-session as a slate —
[`decisions/resolved/vwsd-nlbaseline-audit-params`](../../wiki/decisions/resolved/vwsd-nlbaseline-audit-params.md)
(opened session 126, ratified session 127, 2026-06-28, autonomous adversarial review: P1 = graded
none/partial/high with band metric = high-recovery rate; P2 = author panel.A claude-sonnet-4.6 +
held-out auditors panel.B gpt-5.4-mini + panel.C gemini-3.5-flash, band on the two-auditor mean;
P3 = `[0.60, 0.95]`)** — so the audit's scoring rule, auditors/author, and band edges are now
**fixed before any NL description is authored** (satisfying "band set before authoring"); the freeze
may now proceed (still gated by the author+freeze+critic+pre-flight steps below); (2)
**freeze + checksum** the NL descriptors, the adequacy-audit scores, and `sep_nl_i` **before** the reused
IMAGE arm is read; (3) obtain a **fresh independent pre-run-critic GO**; and (4) record a pre-flight that
clears the $5/day UTC cap. Any of those failing **defers** the run and **relaxes nothing**; a pre-run-critic
NO-GO (e.g. the standard cannot be hit without leaking gold) is an allowed, honest outcome. Anchored (as a
*future result* would be) to
[`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md). Companion to the frozen
[`design/vwsd-grounding-headroom-v2`](vwsd-grounding-headroom-v2.md) and the run it produced,
[`result/vwsd-grounding-headroom-v2`](../../wiki/findings/results/vwsd-grounding-headroom-v2.md), whose
first-class Limitation 1 this design exists to answer. Run dir (to be created by the executing session,
NOT now): `experiments/runs/<date>-vwsd-grounding-headroom-nlbaseline/`.

> **This is a DRAFT, contingent on an OPEN decision — no probe, no freeze, no spend.** Authoring this
> page generates no NL descriptors, scores no adequacy audit, fetches no images, and makes no model
> call. The result `result/vwsd-grounding-headroom-nlbaseline` **does NOT exist and is NOT cleared**. It
> is gated on a *later session* completing all of: (1) **DONE** — the decision
> [`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../wiki/decisions/resolved/vwsd-nlbaseline-competence-dv.md)
> was **ratified cross-session (session 123, ADOPT-DEFAULT Q1-C)** so the competence standard for the NL
> channel is fixed in shape, and the three deferred numbers (band edges, audit model(s)+author, recovery-scoring
> rule) were **ratified session 127 (ADOPT-DEFAULTS) — [`decisions/resolved/vwsd-nlbaseline-audit-params`](../../wiki/decisions/resolved/vwsd-nlbaseline-audit-params.md)**;
> (2) the new TEXT-NL descriptors authored to that ratified standard, the adequacy audit
> scored, and the recomputed separability covariate `sep_nl_i` all **frozen + checksummed BEFORE the
> reused IMAGE arm is read** (mirrors v2 condition b); (3) a **fresh independent pre-run critic GO**
> against the frozen NL-baseline design *and* the observed `sep_nl_i` + adequacy-audit distributions
> (mirrors v2 condition e), specifically certifying the NL channel is neither an oracle restatement of
> gold nor a degenerate-weak channel; (4) a pre-flight budget estimate that clears the $5/day UTC cap.
> Any of those failing **defers** the run and **relaxes no condition**. A pre-run-critic NO-GO is an
> allowed, honest outcome (e.g. the competence standard cannot be hit without leaking gold), and defers
> the magnitude read.

## Why this design exists (the v2 magnitude gap, and the v1→v2→NL symmetry)

[`result/vwsd-grounding-headroom-v2`](../../wiki/findings/results/vwsd-grounding-headroom-v2.md)
**SUPPORTS the gating *shape*** of prediction 1 of
[`conjecture/distributional-saturation-grounding-headroom`](../../wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
(3/3 models in the predicted direction, distraction-controlled), but it **could not** test the
conjecture's prediction 3 — that the residual headroom for concrete sense is **narrow**. The reason is
its own first-class Limitation 1, quoted **verbatim** from that result page (Limitations, item 1):

> "**The headroom magnitude is operationalization-inflated.** The TEXT arm uses Option-B descriptors
> that *deliberately* strip the referent name (the v2 fix for v1's caption leakage). So "text-failed"
> means "the visual-form-only descriptor + target word + trigger under-determined the sense," not "a
> competent natural-language description failed." The image rescuing ~45% of such cells confirms the
> gating **shape** but says nothing about the **size** of the residual a fluent text channel would
> leave — that is why prediction 3 ("narrow headroom for concrete sense") is **not** supported or
> refuted here. A natural-language (non-abstracted) baseline would test magnitude; v2 tests shape."

That last sentence — *"A natural-language (non-abstracted) baseline would test magnitude; v2 tests
shape."* — is the lever this design picks up. The v2 result's "Bearing on the conjecture" closes the
same way: *"a natural-language-baseline run is owed to test magnitude."*

**The v1 → v2 → NL-baseline symmetry (make it explicit, because the value of this design lives in it):**

| run | text channel | what it did to the headroom | consequence |
|---|---|---|---|
| **v1** | referent-**NAMING** captions ("a pile of mustard seeds") | **saturated** the baseline (.86–.88; only 7 under-determined items, below floor) | underpowered + confounded; gating *un-testable* |
| **v2** | referent-**BARRED** visual-form descriptors | **manufactured** headroom (referent names stripped, so "text-failed" is partly an artifact of the instrument) | gating *shape* testable + supported, but magnitude inflated → prediction 3 untestable |
| **NL-baseline (this design)** | competent natural-language description, **names ALLOWED** | the *powered, stratified, clean middle* | tests whether the residual stays **narrow** under *ordinary* language (supports prediction 3) or is **wide** (refutes the narrow-headroom sub-bet) |

v1 named the referent and saturated; v2 barred the referent and manufactured headroom. The NL-baseline
is the fluent middle: a description that names the depicted referent *normally*, as a competent
describer would, neither stripping identity (v2's artifact) nor reducing to a caption-string the model
trivially matches (v1's saturation). Its whole result hinges on **the standard of "competence" the
description channel is held to** — and that is exactly the value-laden gate this design refuses to
settle on its own (see Limitation 1 of this design and the ratified decision).

**What this design tests — and explicitly does NOT.** It tests prediction 3 ("narrow headroom for
concrete sense") of the conjecture, read as the **width of the residual a fluent text channel leaves**
on VWSD selection. It stays **gating-shape-on-binary-selection**: it is **NOT** prediction-1-as-written
(VWSD gold is binary correct-image, not a graded human relatedness gradient) and **NOT** reference
(`referential.externalist` untouched). It refines the magnitude reading of the same gating structure v2
already supports; it does not re-open whether the gating shape holds (v2 settled that direction).

## What is reused unchanged (this is a CHEAP follow-up — only the text channel changes)

The single thing that changes between v2 and this design is the **text channel**. The frozen items, the
image-bearing selection arm, and the clean word-ablated control are all properties of the items + images
+ models, **not** of the text descriptors — so they are reused unchanged and need **no re-spend**:

- **The SAME frozen stratified N=120 items.** `frozen/run_items.json`, sha256 `7f9e52fa…` (seed
  20260625; under-determined 35 / saturated 85 under the v2 covariate, both clearing the ≥15 floor).
  Reused verbatim — the magnitude read must be on the *same* items v2 read so v2's shape result and this
  design's magnitude result are directly comparable. **No re-draw, no re-stratification on the NL
  covariate** (re-drawing on `sep_nl_i` would let this design pick its own favorable items — forbidden;
  the draw stays the v2 draw, and `sep_nl_i` is reported *over* it, see below).
- **The SAME already-clean DISTRACT control.** `raw/distract.json`, sha256 `f8fbb6be…` (pooled .097 ≈
  chance; no model's Wilson lower bound exceeds .10 — [`result/vwsd-grounding-headroom-v2`](../../wiki/findings/results/vwsd-grounding-headroom-v2.md),
  §1). The word-ablated control removes the target word and trigger and shows the model only the ten
  **images**; it **does not depend on the text channel at all**, so it need **NOT be re-run**. This
  design **cites the v2 result for it** and credits it FIRST, exactly as v2's binding condition 3
  requires — a positive image lift that does not survive this already-shown-clean control is the
  distraction null, not headroom.
- **The SAME IMAGE arm.** `raw/image.json`, sha256 `6884eea0…430870` (s112; same images, same selection
  prompt, same frozen items, claude `max_tokens` raised 16→512, 0 parse-fails). The image-conditioned
  selection is a property of the items + images + models, **not** of the text descriptors, so it is
  **reusable unchanged**. This design reads the image-rescue rate *in the NL-text-failed cells* off this
  same frozen IMAGE arm — no image-bearing selection is re-run.

So the **only new spend** is: (i) authoring the new natural-language candidate descriptions (text /
caption-authoring over the unique candidate images in the 120, **no image-bearing selection**), (ii)
the new **TEXT-NL selection arm** (text-only: target word + trigger + the ten NL descriptions, pick
1–10; × 3 models), and (iii) a **held-out adequacy audit** of the NL descriptions (text-only). All
three are text/caption-authoring or text-only selection — **no image-bearing selection arm is re-run** —
which is precisely why this is a cheap follow-up. (See Budget.)

## Anchor and scope (Q3 narrow posture — unchanged from v2, carried verbatim in force)

Carried forward **unchanged** from v2 and the resolved v2 gate's Q3 (no widening):

- **Anchor:** the human-curated VWSD **English gold test** (the 463 EN gold; gold = the human-selected
  correct image after human-authored trigger words + human distractor curation). This design uses the
  **same frozen stratified N=120 subset** as v2, not the full set. Sense locus `grounded.perceptual` ×
  `referential.sense` × `human-comparison`.
- **Establishes (if it runs clean):** the **width** of the residual that a *fluent, referent-naming*
  text channel leaves under-determined on VWSD selection — i.e. whether prediction 3's "narrow headroom"
  holds in *ordinary language* (narrow residual + modest image rescue) or fails (wide residual + large
  image rescue). It refines the *magnitude* reading of the gating shape v2 already supports.
- **Does NOT establish:** (i) **not** prediction-1-as-written (VWSD gold is binary; no graded human
  relatedness gradient); (ii) **not** reference (`referential.externalist` untouched — a model picking
  the gold image shows behavior *sensitive to* the word→sense→image mapping, not a perceptual symbol
  system or reference-fixing); (iii) **not** an absolute magnitude — the residual width is *"how narrow
  under THIS competence standard"*, a property of a model-authored channel held to a fixed, audited
  standard, never an absolute property of language (see the ratified decision's honesty note).
- **Caveats carried to the result, verbatim in force** (all from
  [`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md)): **binary gold** (no
  graded signal); **limited annotator independence** (English annotators "includ[ed] the authors of
  this paper"; BabelNet-automatic seed; no inter-annotator agreement reported); **image redistribution
  unconfirmed** (images out of git, fetch-at-runtime only, never re-hosted); **anchored only to the gold
  test split** (the 12,869 training instances are silver).

## Data (binding condition a — unchanged; images out of git)

Identical handling to v2. The reused IMAGE arm (`raw/image.json`) was already produced against the
resized EN test images fetched at runtime and checksummed (v2 re-verified sha256 `b9f2f1e1…af8f`, exact
match to the session-100 fetch), **kept OUT of git** (redistribution unconfirmed —
[`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md), License & redistribution).
The NL-descriptor authoring step (the only new image-reading step) reads those same runtime-fetched
images to *author text*; it produces text descriptors, never re-hosts image bytes. The annotation
overlay (queries + gold) stays committed under `frozen/`, usable under CC-BY-NC for non-commercial
research with attribution. Anchored **only** to the gold test split.

## The new TEXT-NL arm (the only new text channel)

A **competent natural-language candidate description** per unique candidate image in the frozen 120 —
**names ALLOWED**, authored to the competence standard fixed by the ratified decision
[`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../wiki/decisions/resolved/vwsd-nlbaseline-competence-dv.md).
Unlike v2's Option-B descriptors, the NL description is permitted (indeed required) to name the depicted
referent plainly and completely, as a competent describer would — *"a pile of mustard seeds"* is now
allowed, where v2 barred it. The point is to measure the residual a *fluent* channel leaves, not a
de-referented one.

- **Author model + policy.** Fixed by the ratified decision (adopted default Q1-C: fresh fluent
  descriptions under a *"name the depicted referent plainly and completely, as a competent describer
  would"* policy, **plus** a held-out adequacy audit — option Q1-C). The authoring policy is **NOT**
  finalized here; it is whatever the cross-session ratification fixes.
- **The recomputed separability covariate `sep_nl_i`.** Per item, `sep_nl_i` = fraction of the 3 models
  correct in the TEXT-NL arm (0, 1/3, 2/3, 1), computed from **these** NL descriptions — the *NL*
  analogue of v2's `sep_i`. It is reported **over the same frozen 120 items** (the v2 draw); it is **not**
  used to re-draw or re-stratify the sample (that would be retuning on the conditioning variable). The
  strata of record stay the v2 draw; `sep_nl_i` is the NL channel's own text-failure indicator.
- **Frozen + checksummed before the reused image comparison is read.** The NL descriptions, the adequacy
  audit scores, and `sep_nl_i` are written to a checksummed frozen file (e.g.
  `frozen/nl_descriptors.json` + `raw/text_nl.json`) and committed **before** the (already-existing)
  IMAGE arm is read against them (mirrors v2 condition b — "no retuning" stays mechanically auditable).
  Because the IMAGE arm already exists frozen, the discipline here is symmetric: the NL channel is frozen
  before anyone computes the rescue rate, so the rescue rate cannot drive the NL authoring.

## The test of record (the MAGNITUDE read — both outcomes first-class)

The read is the **SIZE of the residual under the fluent channel**, two components, in the mandated
order:

1. **Distraction null — credited FIRST (binding, reused).** The v2 DISTRACT null (`raw/distract.json`,
   pooled .097 ≈ chance) is cited and credited **before** any rescue is read. No image-conditioned
   gold-selection counts as headroom unless it survives this already-clean control. (Reused, not re-run
   — it does not depend on the text channel.)
2. **The residual width.** The fraction of item×model cells the fluent NL description leaves
   **text-failed** (`t_nl,im = 0`) — i.e. how often a *competent, referent-naming* description still
   fails to fix the sense. This is the magnitude prediction 3 is about: *how much residual a fluent text
   channel leaves*. A **small** residual width supports "narrow headroom"; a **large** one is the first
   refuting signal.
3. **The image-rescue rate in those NL-text-failed cells.** Among cells where the NL description failed
   (`t_nl,im = 0`), the rate at which the reused frozen IMAGE arm is right (`g_im = 1`), contrasted with
   IMAGE accuracy where the NL description already succeeded. Distraction-controlled by the reused clean
   DISTRACT null (step 1).

**Prediction 3 ("narrow") predicts a SMALL residual width + a MODEST image rescue** — most concrete,
depictable VWSD items should be fixable by a fluent description, leaving few text-failed cells and
little for the image to rescue. **A WIDE residual + a LARGE image rescue REFUTES the narrow-headroom
sub-bet** while leaving the v2-established gating *shape* intact (a wide-but-still-gated residual still
shows image rescue concentrated in the text-failed cells; it just shows the residual is not narrow).
**Both outcomes are pre-registered as first-class** (write-the-null discipline): this design does not
pre-judge whether the headroom is narrow or wide — it fixes the yardstick that would tell them apart.

**Companion reads (descriptive only).** Per-item NL-induced improvement `Δ_nl,i = mean_m(g_im) −
mean_m(t_nl,im)` regressed on `sep_nl_i` (Spearman + OLS, per-model and pooled); the conjecture predicts
a negative slope. **Demoted to companion**, carrying the **same mechanical-ceiling caveat the v2 design
states**: per-item accuracy is binary, so an item where NL-text is already correct has `Δ ≤ 0` by
construction, and the under-determined stratum is *defined* by text-failure, so a raw negative `Δ`–`sep`
correlation is partly mechanical. The non-mechanical content is the **cell-level rescue rate in the
NL-text-failed cells** and whether it **survives the DISTRACT control** — the slope is companion only.

**Strata + floor.** Items binned by `sep_nl_i` (saturated `sep_nl_i = 1`; under-determined `sep_nl_i ≤
1/3`); the full `sep_nl_i` distribution and both bin counts are reported. The binned read is credited
only if each reported bin holds **≥ 15 items** (the v2 floor, carried). Critically, the NL channel may
**saturate** the way v1's captions did (a fluent description that names the referent may make almost
every item text-solvable) — in which case the under-determined bin falls below floor, the binned read is
**not** reported, and the result falls back to the continuous + cell-level reads with the power caveat
foregrounded. **That saturation is itself an informative outcome**: if a competent NL channel saturates,
the residual is *narrow by direct observation* (few text-failed cells), which is prediction-3-supporting
in substance even when it costs the binned read — and it is reported as such, honestly, not patched by
re-binning. No post-hoc re-binning.

## Power / coarseness caveat (MANDATORY in the result)

N = 120 of the 463 EN gold, binary per-item accuracy, a coarse read of the magnitude. A narrow observed
residual is **"narrow under this competence standard on these 120 items,"** not a proven law; a wide
residual is the first refuting signal, not a refutation by itself. The magnitude is **competence-bound**
(the ratified decision's central caveat): it is a property of the model-authored NL channel held to the
ratified standard, never an absolute property of ordinary language. A flat/ambiguous read is **"no
detectable magnitude difference OR underpowered,"** never proven.

## Pre-run critic gate (binding — mirrors v2 condition e, plus the NEW failure mode)

Before any spend that commits the run, a **fresh independent critic** (not the orchestrator that does
the build) must return **GO/NO-GO** against this frozen NL-baseline design **and** the observed
`sep_nl_i` + adequacy-audit distributions. It must specifically certify:

1. **The new failure mode (oracle restatement).** The NL descriptions did **NOT** degenerate into an
   **oracle restatement of the gold** — a description so complete it trivially confirms "narrow
   headroom" as an artifact (the *mirror* of v2's manufactured-headroom artifact). The adequacy audit's
   recovery rate must sit **below** the pre-registered upper bound (it must not be ≈ 100% trivial
   recovery of the exact gold).
2. **v2's own failure mode (degenerate weakness).** The NL descriptions are **NOT** so weak that they
   manufacture headroom (v2's failure) — the adequacy audit's recovery rate must sit **at or above** the
   pre-registered lower bound (a competent describer's floor).
3. **Standard reused-arm discipline.** `sep_nl_i` is genuinely pre-frozen (NL descriptions + adequacy
   audit + TEXT-NL arm checksummed **before** the reused IMAGE arm is read); the DISTRACT control is
   cited clean and credited first; and no surface-dissimilarity-only reader beats the read.

**A NO-GO defers the run and relaxes nothing** — and may legitimately conclude the competence standard
cannot be hit on VWSD without leaking gold (deferring the magnitude gate), exactly as v2's critic could
rule the non-caption baseline un-authorable.

## Anti-cheat note (the guards this design honors)

Freezing this design (a *later* session's act, not this one) fixes the **yardstick** — the NL
description policy fixed by the ratified decision, the adequacy-audit target band, the reuse of the v2
frozen 120 / IMAGE / DISTRACT arms, the `sep_nl_i` covariate, the ≥15 floor, the anchor posture and
scope — **never the result**. The NL descriptions and `sep_nl_i`, **once frozen + checksummed, are not
re-derived after reading the reused IMAGE arm's rescue rate** — that commitment is what makes "no
retuning" auditable. **There is NO retuning of the competence standard after seeing rescue rates** — the
adequacy-audit target band is set before authoring and read against the audit, never adjusted to land a
narrow-or-wide result. The DISTRACT null is credited **first** (reused clean); no image lift counts as
headroom unless it survives it. A pre-run-critic NO-GO defers, never relaxes. **Both** a narrow and a
wide residual are pre-registered as first-class outcomes; this design pre-judges neither. The magnitude
it would measure is always *"how narrow under THIS ratified competence standard"* — never an absolute.
