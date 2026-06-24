---
id: vwsd-grounding-headroom-dv
title: What is the dependent variable for a VWSD grounding-headroom probe, given that VWSD's gold is binary correct-image selection but the conjecture's prediction 1 is built on a graded relatedness Δ?
status: resolved
opened: 2026-06-24
opened-by: autonomous (session 98, surfacing the VWSD DV gate)
resolved: 2026-06-24
resolved-by: autonomous (adversarial review)
resolution: adopt-modified (Option A / Q2 interaction as test of record / Q3 narrow human-anchored posture — five tightening modifications)
anchor: human-anchored (VWSD gold-test selection accuracy; binary, not graded — scoped to the gating shape, NOT prediction-1-as-written)
contingent-artifacts:
  - conjecture/distributional-saturation-grounding-headroom
  - design/vwsd-grounding-headroom-v1
  - result/vwsd-grounding-headroom-v1
---

> **Status: RESOLVED (2026-06-24, session 99, autonomous adversarial review — cross-session: opened
> by session 98 on 2026-06-24, ratified by session 99; the session boundary held). VERDICT: ADOPT
> MODIFIED.** An independent fresh-agent reviewer ratified the provisional default's core
> architecture — **Q1 Option A** (image-conditioned selection accuracy vs a text-only baseline),
> **Q2 the interaction** (per-item text-only separability × image-induced selection improvement,
> predicted negative) **as the sole test of record** (a bare main-effect lift is descriptive only),
> and the **Q3 narrow human-anchored posture** (selection accuracy vs human gold; explicitly **not**
> prediction-1-as-written, **not** reference) — with **five tightening modifications** (none makes a
> positive likelier; all close cheat-surfaces). The reviewer confirmed Option A faithfully
> instantiates the conjecture's load-bearing *gating* clause without smuggling a different claim (it
> preserves the gated-interaction structure and is honest it sacrifices the graded-against-human-gradient
> part VWSD cannot supply), that the text-only baseline is genuinely pre-freezable, and that the
> verdict fixes the **yardstick, not the result** (every element makes a spurious positive harder and
> keeps both falsifier arms live).
>
> **Five binding modifications (written into the build spec; tightenings only):**
> 1. **Numeric stratification floor.** The frozen design must specify the exact per-item text-only
>    separability metric and require the under-determined and saturated strata each hold **≥ a stated
>    minimum number of EN gold items** with a reported separability distribution, so the interaction
>    is not read off a handful of extreme items; the pre-run critic certifies the strata are not
>    degenerate.
> 2. **The text-only baseline freeze is a committed artifact, not a procedure.** The per-model,
>    per-item separability scores are **written to a frozen, checksummed file before any image
>    condition runs**, and the analysis reads from that file — "no retuning" made mechanically
>    auditable.
> 3. **Distraction-null reporting is mandatory and ordered first.** The same-referent /
>    surface-dissimilarity control-arm result is reported **before** the interaction is credited; a
>    negative interaction that does not survive the control is recorded as the **distraction null, not
>    headroom**, with no retuning.
> 4. **Power/coarseness caveat is a mandatory result caveat.** Because binary per-item accuracy is a
>    coarse read of the per-item residual on a 463-item anchor, the eventual result must carry an
>    explicit limit that a flat (null) interaction is **"no detectable gating OR underpowered,"** not
>    proven absence of headroom.
> 5. **Conjecture scope note** (applied this session): one line added to
>    [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md)
>    recording that the VWSD operationalization tests the gating *shape* via a selection-accuracy
>    interaction and is **explicitly not** a test of prediction-1-as-written, which remains open for a
>    future graded-image resource. Status unchanged (`proposed`).
>
> **Contingent-artifact disposition.** The conjecture stays **`proposed`** (this gate is against its
> prediction-1 *operationalization on VWSD*, not a defect in it). A build session is **cleared to
> author `design/vwsd-grounding-headroom-v1`** as the frozen prereg carrying all binding conditions
> below **plus** modifications 1–4. **[`result/vwsd-grounding-headroom-v1`](../../findings/results/vwsd-grounding-headroom-v1.md) is NOT cleared** — it may be
> produced only after the design is frozen, the fetch+checksum done, and a **fresh independent pre-run
> critic returns GO** against the frozen design; a NO-GO defers the run and never relaxes a condition.
> Neither contingent `*-v1` artifact exists yet.
>
> **BUILT + RUN, session 100 (2026-06-24).** Both contingent artifacts now exist:
> [`design/vwsd-grounding-headroom-v1`](../../../experiments/designs/vwsd-grounding-headroom-v1.md)
> (frozen, all five mods) and [`result/vwsd-grounding-headroom-v1`](../../findings/results/vwsd-grounding-headroom-v1.md).
> Data fetched + checksummed (images out of git). A fresh independent **pre-run critic returned GO**
> (binding condition d) on a 50-item budget-bounded subset; the run honored every mod — the caption-text
> baseline **saturated** (under-determined bin 7 < the mod-1 floor 8), so the **binned interaction was
> suppressed** automatically; the **distraction null was reported first and is clean**; the power caveat
> is foregrounded; an independent **post-run verifier reproduced** every number. Verdict: **neither
> confirms nor falsifies** the gating prediction (caption-leakage confound + floor + underpower). The
> yardstick this decision fixed held; the result claimed nothing the data does not carry.
>
> Anti-cheat: the reviewer confirmed the verdict is not motivated by wanting a particular result
> (every modification makes a spurious positive harder and keeps the falsify/null arms live).
> Ratifying fixes the **yardstick**, never the result; the probe must not be run, nor the DV
> re-tuned, in this ratifying session (and it was not — $0, no probe).

> **Status (historical): OPEN (2026-06-24, session 98).** This page surfaced a value-laden
> operationalization gate (CLAUDE.md rule 5; charter §8) and **took no position that binds a
> run**. It recorded options, a *provisional* default, and binding pre-spend conditions, ratifiable
> at the earliest by a **later** session's independent adversarial-review pass (now done — see the
> resolution block above), per [`PROJECT.md`](../../../PROJECT.md) §12.3.
>
> The two contingent artifacts named below — `design/vwsd-grounding-headroom-v1` and
> [`result/vwsd-grounding-headroom-v1`](../../findings/results/vwsd-grounding-headroom-v1.md) — **do not yet exist**; they are the design spec and result a
> ratifying-then-building sequence would produce. The conjecture
> [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md)
> exists and stays `proposed`; this gate is queued against its prediction 1, not a defect in it.

# Decision: the dependent variable for a VWSD grounding-headroom probe

## Why this exists

The grounding-headroom conjecture's load-bearing test is **prediction 1 ("headroom gating")**. As
written, it is a claim about a **graded** quantity and an **interaction**, not a main effect. From
[`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md)
(Predictions, item 1):

> "Run the existing image probe's instrument on a set stratified by **text-only baseline
> separability**. Δ (image-induced movement toward the human sense-relatedness signal) should be
> **near zero in the saturated stratum** ... and **positive in the under-determined stratum** ...
> The within-set signature is a **negative correlation, across items, between text-only baseline
> separability and image-induced improvement**."

The conjecture is explicit that the load-bearing object is the **interaction**, not a level: "the
claim is specifically that Δ is **conditioned on text under-determination**, so the test must vary
that condition and read the interaction, not a main effect." And its instrument is a **graded**
relatedness rating: any test "reuses the *same* DURel-style graded-relatedness instrument the
lexical program validated."

VWSD does **not** supply a graded signal. The scouted anchor
[`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md) names this as a sharp
known limit:

> "**Binary gold, not a graded relatedness signal.** VWSD gold is 'which one image is correct,' not
> a per-pair human *gradient*. It therefore **cannot** replace the project's DURel/DWUG-style graded
> sense-relatedness instrument ...; it tests *selection accuracy*, not *graded similarity*. ... Using
> it requires either adopting accuracy-against-human-gold as the DV or building a graded layer VWSD
> does not provide."

And its "Pointer for next visit" (item 1) already flags the same fork:

> "Note that VWSD's native DV is **selection accuracy vs. human gold**, not the DURel-style graded
> relatedness the conjecture's existing instrument uses — decide and freeze which DV before
> running."

So a VWSD probe necessarily tests a **re-shaped operationalization** — image-conditioned *selection
accuracy* against a text-only baseline, in the text-under-determined regime — and **not**
prediction-1-as-written (the graded-Δ × separability interaction). Choosing and freezing that DV is
the gate this page surfaces. The mismatch is real on both sides: VWSD's gold is binary
correct-image, and prediction 1's signature is a graded cross-item correlation. The decision is how
to honor what the conjecture *genuinely* predicts without overclaiming that VWSD tests its
prediction-1-as-written.

VWSD does have a structural *fit* the conjecture wants: it is image-native by construction (the
resource records that "the target word is generally necessary to understand the full context" and
that "the sense distinctions are given in the visual modality"), which instantiates the
**under-determined** cell. The fit is to the *regime*; the mismatch is to the *measure*.

## The sub-questions

### Q1 — What is the DV?

- **Option A — image-conditioned selection accuracy vs. a text-only baseline, in the
  under-determined regime** (this is the natural, native VWSD measure). The DV is: does adding the
  image move correct-sense selection above what the text (target word + 1–2 trigger words) alone
  supports? This directly tests "does the image move sense selection *where text under-determines*"
  — the conjecture's qualitative core (grounding acts only in the residual). It is a **re-shaping**:
  it replaces the graded-Δ × separability interaction with an image-vs-text accuracy lift in a
  regime VWSD guarantees is under-determined. It does **not** test prediction-1-as-written.
- **Option B — construct a graded layer VWSD does not provide**, so prediction-1-as-written can be
  tested. E.g. derive a graded relatedness / confidence signal from model behavior over the 10
  candidates (a score distribution, a margin, a rank profile) and treat *that* as the graded Δ,
  stratifying by text-only separability. **Honest risk flags:** (i) the graded signal would be a
  *model-derived* construct, not a human-anchored gradient — it cannot be validated against a human
  relatedness distribution because VWSD provides none ("No per-item human gradient / no released
  human relatedness distribution"), so it risks circularity (model-internal score regressed on a
  model-internal covariate, with the only human signal being binary accuracy). (ii) Its validity as
  a stand-in for the DURel-style instrument is unestablished and would itself need a separate
  validation the conjecture's instrument already has. (iii) It re-opens, rather than closes, the
  operationalization gate. Option B should be entertained only if the constructed signal can be
  anchored to *something* human (e.g. binary accuracy as a coarse check), and even then its claim is
  weaker than the existing graded instrument's.
- **Option C — do not use VWSD for prediction 1 at all.** Use VWSD only for a *complementary*
  selection-accuracy sub-claim (image moves sense selection in an image-native, text-under-determined
  task — a finding that bears on the conjecture's spirit), and leave the graded-Δ × separability
  interaction (prediction-1-as-written) for a future **graded** image resource (e.g. the not-yet-built
  fine-polysemy image set the conjecture names, which is paired to the DURel instrument). This keeps
  the conjecture's prediction 1 cleanly testable later and uses VWSD for what it natively supports.

### Q2 — Under a selection DV, what is the text-only baseline, and how is "headroom" stratified?

Prediction 1's whole force is an **interaction with text-under-determination**; a bare
image-vs-no-image accuracy lift is a *main effect* and does not, on its own, establish the gating
the conjecture demands. The conjecture's "anchor caveats" are explicit that the stratifier is a
**measured, pre-frozen, per-model covariate**:

> "Text-only baseline separability is a *measured covariate*, not a human label. ... the covariate
> must be computed and frozen *before* the image condition is run, on pain of retuning the indicator
> after seeing results (the operationalization gate the protocol forbids)."

> "the stratification must be computed per-model ... The hypothesis is about the model's own
> residual, which is why prediction 1 reads an *interaction*, not a fixed word list."

Under a **selection** DV this re-shapes as follows:

- **Text-only baseline = a text-only condition's per-item ability to pick the gold sense from
  context alone.** Operationally: present the same model the target word + trigger words (no image,
  or with image identities masked to text labels) and measure how well it isolates the gold sense
  per item — a text-only separability score frozen **per model, per item, before any image
  condition runs** (the pre-registration / per-model-covariate discipline the conjecture's anchor
  caveats demand). VWSD's by-design minimal context means most items should sit in the
  under-determined band, but separability is not uniform across items — that within-task variance is
  what the stratification reads.
- **The interaction, not the main effect, is the test.** The DV of record is the *relationship*
  between per-item text-only separability and per-item image-induced selection improvement —
  predicted **negative** (less text-separable items gain more from the image), the selection-DV
  analogue of prediction 1's "negative correlation, across items, between text-only baseline
  separability and image-induced improvement." A flat relationship is the null.
- **Distraction control is obligatory.** Prediction 1's distraction caveat carries over verbatim in
  force: a model that does zero sense computation and merely rates "two visibly different pictures →
  less related" reproduces a positive on surface dissimilarity alone. The resource's caveat 4 says
  the same for VWSD: "a model can score above chance by surface image dissimilarity alone; any sense
  claim needs the same-referent distraction control the prior image probe built." So the design must
  carry a same-referent / surface-dissimilarity control arm and report the distraction null, or a
  positive accuracy lift is the distraction null, not headroom.

### Q3 — Anchor posture and honest scope

Under Option A (the recommended default), the human-comparison claim is **narrow and explicit**:

- **What it establishes:** image-conditioned *selection accuracy* against the **human-curated gold
  image** (the 463 EN gold-test items; trial 16), in a task whose context is by construction
  text-under-determining. The sense locus is `grounded.perceptual` × `referential.sense` ×
  `human-comparison` (the resource's own grounding statement). The force is: the model's sense
  selection is *sensitive to* perceptual input in the under-determined residual, contrasted with the
  saturated-regime redundancy null already on record.
- **What it does NOT establish:** (i) **not** prediction-1-as-written — it is selection accuracy,
  not the graded-Δ × separability interaction against a human relatedness gradient; the graded test
  remains open for a future graded-image resource. (ii) **not** reference — the resource is explicit
  that "A model picking the gold image shows behavior *sensitive to* perceptual input in the
  under-determined residual; it is **not** evidence of a perceptual symbol system or of
  reference-fixing"; `referential.externalist` stays untouched. (iii) **not** a graded human
  judgment — VWSD has no per-item human gradient.
- **Caveats the eventual result must carry forward** (all from
  [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md)): **binary gold** (no
  graded signal); **limited annotator independence** (English annotators "includ[ed] the authors of
  this paper"; the seed sense↔image link is BabelNet-automatic, so the human signal is
  curatorial/confirmatory over an automatic seed, and **no inter-annotator agreement is reported**);
  **image redistribution unconfirmed** (CC-BY-NC line covers "the dataset" without specifying images;
  third-party image sources; redistribution not cleared); **anchor only to the gold test/trial
  split** (the 12,869 training instances are silver).

## Provisional default (to be adopted, modified, or rejected by a later session)

**Default: Option A for Q1**, with **Q2's interaction (not the bare accuracy main effect) as the
test of record**, under the **Q3 narrow human-anchored posture**.

Rationale — calibrated, not a survey:

- Option A tests *something the conjecture genuinely predicts* — that grounding moves sense behavior
  in the text-under-determined regime, read as an **interaction** with per-item text-only
  separability — while being honest that it is **not** prediction-1-as-written. It uses VWSD's native
  human signal (binary gold) rather than manufacturing a graded layer the resource warns has no human
  validation.
- Option B is **not** the default: its graded signal would be model-derived with no human gradient to
  validate against, so it risks dressing a model-internal contrast as a test of the human-anchored
  graded prediction — the weaker, gate-reopening path. It stays available only if a later session can
  anchor the constructed signal honestly.
- Option C is the **honest fallback if a reviewer judges even the interaction-on-accuracy too far
  from prediction 1 to credit**: run VWSD as a complementary selection-accuracy sub-claim and reserve
  prediction-1-as-written for a future graded-image resource. The default (A) is preferred over C
  only because A's interaction recovers the *gating shape* the conjecture's load-bearing clause names,
  whereas C abandons the gating test on VWSD entirely.

This default is **provisional and ratifiable only next session**. Adopting it fixes the *yardstick*
(which DV, which baseline, which control, which anchor posture), never any result. It must not be
read as a finding that grounding helps in the residual — only as the cleanest VWSD operationalization
of the conjecture's testable structure.

## Binding pre-spend conditions (all must hold before any model call)

Mirroring the rigor of [`decisions/resolved/dative-anchor-and-indicator`](dative-anchor-and-indicator.md):

(a) **Fetch + checksum, images out of git.** Download the **572 MB resized EN test set + the gold EN
test queries**, checksum them, and **keep images out of git** — image redistribution is unconfirmed
(resource License & redistribution), so **fetch-at-runtime only**, no re-hosting. Anchor **only** to
the gold test/trial split; the training split is silver and is not an anchor.

(b) **Prereg the DV before any model call.** The DV (selection-accuracy interaction vs. per-item
text-only separability), the text-only baseline procedure, the stratification, and the analysis
ordering (interaction is the test of record; bare main-effect lift is descriptive only) are written
into `design/vwsd-grounding-headroom-v1` and frozen **before** any image condition runs. The
text-only separability covariate is computed **per model, per item, and frozen pre-image** — no
retuning after seeing image results.

(c) **Distraction control built in.** The design carries the **same-referent / surface-dissimilarity
distraction control** the prior image probe built and the conjecture/resource both require, and
reports the distraction null; a positive accuracy lift that does not survive the control is the
distraction null, not headroom.

(d) **Fresh independent pre-run critic GO/NO-GO.** Before any spend, an independent critic certifies,
against the **frozen** design, that the DV honestly tests the conjecture's gating structure (not
prediction-1-as-written by sleight), that the text-only baseline is genuinely pre-frozen, and that no
surface-dissimilarity-only reader beats the interaction — **GO/NO-GO**. A **NO-GO defers the run, it
does not relax any condition.**

(e) **Pre-flight budget estimate** (charter §8) recorded in [`config/budget.md`](../../../config/budget.md) before the run; actual
recorded after.

## Anti-cheat note

Ratifying this decision fixes the **yardstick** (which DV, which baseline, which control, which
anchor posture and scope), never the **result**. The probe must not be run, nor the DV re-tuned, in
the session that ratifies. The text-only separability covariate, once frozen, is not re-derived after
seeing image results. A pre-run-critic **NO-GO defers the run, never relaxes a condition**. And no
positive accuracy lift counts as headroom unless it survives the distraction control — surface
dissimilarity reproduces a positive with zero sense computation.
