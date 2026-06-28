---
id: constructional-monotonicity-generalization-operationalization
title: Which NEW add-vs-cancel construction pair does the monotonicity-generalization battery use, and how is its matched-difficulty / ceiling certification fixed before any data?
status: resolved
resolved: 2026-06-28
resolved-by: autonomous (adversarial review)
resolution: "ADOPT-WITH-MODS (session 134, independent fresh-agent adversarial review; producing sessions 133/134 excluded as sole ratifier). (a) PAIR: Option A1 as a single new-pair internal-contrast-only leg — ADD = resultative (verb pool beat/boil/cut/hammer/kick/paint/push/scrub/squeeze/wipe; exclude trap verbs freeze, sharpen), CANCEL = for-durative aspectual (semelfactive-iteration) coercion; A3's anchored-replication leg is DROPPED (prereq 4). (b) CERTIFICATION: Option B1 + B2 with the prerequisite-(2) frozen numbers — B2 admits a pair only if add licensing-no-cue affirm >= 0.80 AND bare-verb control <= 0.40 AND the cancel lexical default >= 0.80, all in >=2/3 models on a frozen MAIN-item calibration subset, else re-pair before spend; asymmetry read at a frozen 20 pp margin (confirm/symmetric/reversal); instrument-fragility at a frozen >=10 pp NLI-vs-FC margin; cc-v2 cue-arm reading rule inherited unchanged. MODS: (1) the CANCEL verb pool must be disjoint from the ADD pool — kick and bounce removed; (2) deduplicate the cancel pool (blink had been listed twice); (3) the cancel-arm B2 default is certified with the affirm-'only once' indicator, NO-GO re-pairs before spend. Fixes the yardstick, never the result; the battery is NOT run, nor any threshold re-tuned, in this ratifying session."
opened: 2026-06-28
opened-by: autonomous (session 131, scoping the monotonicity-asymmetry generalization test)
contingent-artifacts:
  - conjecture/constructional-monotonicity-asymmetry
  - open-question/constructional-monotonicity-generalization-design
---

> **Status: RESOLVED 2026-06-28 — ADOPT-WITH-MODS, by autonomous independent adversarial
> review (session 134).** Opened s131; prerequisite (1) blocker discharged s133; prerequisites
> 2–4 supplied s134; ratified the same session by a fresh independent reviewer (the cross-session
> boundary from the s131 opening having long passed, and the producing sessions 133/134 excluded
> as the *sole* ratifier — the reviewer was an independent fresh agent). The yardstick (pair,
> certification, frozen thresholds, scope) is now **fixed**; see the YAML `resolution:` and the
> "Ratification attempt 2" section at the foot. The spend-bearing battery is **not** run in this
> ratifying session. The companion scoping page is
> [`open-question/constructional-monotonicity-generalization-design`](../../findings/open-questions/constructional-monotonicity-generalization-design.md).

# Decision: construction pair + matched-difficulty certification for the monotonicity-generalization battery

## Why this exists

[`conjecture/constructional-monotonicity-asymmetry`](../../findings/conjectures/constructional-monotonicity-asymmetry.md)
(`status: proposed`) bets that current decoders find a construction's **added** inference
easy to license but its **default** inference hard to suppress. Its sole decisive test is a
**matched-difficulty, ceiling-controlled add-vs-cancel battery on a NEW construction pair**,
with the [`result/conative-cancel-direction-v2`](../../findings/results/conative-cancel-direction-v2.md)
paradigm as the template (the scoping page
[`open-question/constructional-monotonicity-generalization-design`](../../findings/open-questions/constructional-monotonicity-generalization-design.md)
states the confirm/falsify criteria in full).

Two value-laden choices must be **frozen before any model output is seen**, because choosing
them after seeing data is the canonical retuning trap ([`CLAUDE.md`](../../../CLAUDE.md) rule
5; the same discipline the function-word and conative designs imposed):

- **(a) WHICH new add-vs-cancel construction pair(s)** the matched-difficulty battery uses
  (confirm-leg 1 requires a pair **beyond** caused-motion / way / conative).
- **(b) the matched-difficulty / ceiling-certification criterion** — what must be true of
  the frozen item set so the add-vs-cancel comparison is at **matched task structure**, not
  **add-at-ceiling vs cancel-off-ceiling** (mirroring how conative-cancel-v2 was certified
  under [`decisions/resolved/cc-v2-difficulty-operationalization`](cc-v2-difficulty-operationalization.md)).

## The named failure mode this gate guards

**Tuning the construction-pair and/or the difficulty bar until the asymmetry appears** —
trying pairs, verb sets, or ceiling thresholds until one shows add-easy/cancel-hard, then
reporting it as if it had been pre-registered. Because the conjecture is a *forward bet the
project authored*, the temptation to confirm it is real. The guard is the same as the
existing add-direction designs: **freeze-and-hash the item set + an independent pre-run
critic GO/NO-GO** against the frozen set, before any spend. A NO-GO defers the run rather
than relaxing the bar. Ratifying this decision fixes the **yardstick**, never the result.

## (a) Which new add-vs-cancel construction pair

Options drawn only from constructions/alternations named in the conjecture or its cited
pages (no invented dataset). For each, the in-repo human-anchor status is stated honestly.

- **Option A1 — Resultative (ADD) vs a fresh aspectual/conative-type coercion (CANCEL).**
  The conjecture's own example pairing. **Resultative** is one of Scivetti's eight
  constructions ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md))
  and was probed descriptively in
  [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
  (n = 66), so the add arm has a *descriptive* human-annotated answer key on its Scivetti
  items — but resultative is **not** a ratified anchor construction, and a paired fresh
  cancel coercion has **no in-repo human anchor**. **Trade-off:** the clearest realization
  of confirm-leg 1's example, and the add arm is at least item-grounded; but the cancel arm
  is own-design and `internal-contrast-only`, and the resultative's added entailment
  (state-change) must be built so a non-resultative control verb does **not** already supply
  it (else the add arm has no headroom — the AANN default-coincidence trap,
  [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
  *Interpretation*).
- **Option A2 — a Levin alternation pair (ADD or CANCEL per the alternation).** The
  conjecture names "other Levin alternations." **Trade-off:** a rich inventory of matched
  minimal pairs and a clean own-design contrast, but **no in-repo human anchor at all**
  (Levin's inventory is not a `resource` page), so the whole battery is
  `internal-contrast-only`; and Levin alternations are not all cleanly "add" vs "cancel," so
  the direction assignment itself becomes a judgement call that must be frozen and
  justified, not chosen to fit.
- **Option A3 — two-leg split: a within-Scivetti matched re-test of the OLD three (anchored)
  PLUS a NEW own-design pair (internal-contrast).** Run both: the anchored leg
  (Caused-Motion / Way-Manner add vs Conative cancel, on Scivetti items, in the common
  conflicting-cue paradigm) carries the human-comparison answer-key claim on its base arm;
  the new-pair leg carries the *generalization* verdict, `internal-contrast-only`.
  **Trade-off:** the most honest mapping of the design tension the scoping page names
  (generalization wants a new pair; human-comparison wants the old three) — it gives each its
  proper claim strength — but it is **two builds, two freezes, two pre-run critics**, the
  largest scope and cost, and the generalization verdict still rests on the unanchored leg.

## (b) Matched-difficulty / ceiling-certification criterion

The certification that makes the add-vs-cancel comparison fair, mirroring conative-cancel-v2.
What must be true of the **frozen** item set, certified by an independent pre-run critic
**before** any model output:

- **Option B1 — adopt the conative-cancel-v2 certification unchanged.** Both arms in one
  conflicting-cue paradigm; the **add arm's licensing-no-cue at ceiling** AND the **cancel
  arm's lexical default at ceiling** on the frozen items, certified *before* any suppression
  is read — so the discriminating cell is the no-cue construction reading, exactly as in
  conative-cancel-v2 ("suppression-no-cue = `100 − conative_affirm` … the matched analogue of
  the add-direction's canonical/licensing-no-cue"). The governing decision
  [`decisions/resolved/cc-v2-difficulty-operationalization`](cc-v2-difficulty-operationalization.md)
  already fixes the reading rule (report-the-rate; "≥70% follow-construction in ≥2/3 models =
  robust"; degradation monotone-slope-vs-cliff). **Trade-off:** maximal continuity and
  re-uses a ratified yardstick (no new reading rule to tune); but it presupposes the new pair
  *has* a ceiling lexical default to suppress and a ceiling add licensing — which must be
  demonstrated on the frozen set, not assumed.
- **Option B2 — B1 plus an explicit pre-run ceiling gate that BLOCKS the run if either arm's
  base is off ceiling.** Add a numeric GO/NO-GO: if, on a frozen calibration subset, the add
  arm's licensing-no-cue or the cancel arm's lexical-default base is **not** at ceiling
  (e.g. < a frozen threshold in ≥2/3 models), the pair is **rejected** and a different pair
  chosen *before* the main run — so the comparison can never silently become add-at-ceiling
  vs cancel-off-ceiling because the cancel default never reached ceiling. **Trade-off:**
  strictly closes the "the new pair wasn't actually matched" hole the whole gate exists for;
  but it adds a calibration step (cost) and risks rejecting otherwise-interesting pairs whose
  default sits just under ceiling.
- **Option B3 — match on a difficulty proxy independent of the asymmetry.** Equate the add
  and cancel item sets on a pre-registered difficulty proxy (e.g. base NLI accuracy on a
  neutral control framing, or item length / verb frequency) rather than on per-arm ceiling.
  **Trade-off:** controls a broader notion of difficulty, but a proxy can be gamed and is one
  more knob to tune; and base-accuracy matching is *exactly* the level
  [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
  showed is "**baseline-difficulty-confounded and is not the matched-difficulty test**," so a
  proxy must not *replace* the no-cue ceiling certification, only supplement it.

## Provisional default (NOT ratifiable until a later session)

- **(a) Pair:** **Option A3** — the two-leg split (within-Scivetti anchored re-test of the
  old three **plus** a new own-design **resultative-add vs fresh-cancel** pair, i.e. A1 as
  the new-pair leg). It is the only option that honours both confirm-leg 1's "new pair"
  requirement and the human-anchor obligation, by keeping the human-comparison claim on the
  anchored leg and the generalization verdict on the `internal-contrast-only` new-pair leg.
- **(b) Certification:** **Option B1 + B2** — adopt the conative-cancel-v2 certification and
  reading rule unchanged (re-using the ratified
  [`decisions/resolved/cc-v2-difficulty-operationalization`](cc-v2-difficulty-operationalization.md)
  yardstick), **plus** a blocking pre-run ceiling gate so a new pair whose lexical default or
  add licensing is off ceiling is rejected *before* the main run rather than compared
  unfairly.
- **Result posture:** new-pair leg `internal-contrast-only` (per
  [`decisions/resolved/conflicting-cue-human-anchor`](conflicting-cue-human-anchor.md));
  anchored leg human-comparison on its base arm only, cue arms `internal-contrast-only`. A
  future human-rated harder anchor is queued in `wanted.md`, not blocked on.

**Anti-cheat (binding before any spend).** The chosen pair + items + ceiling certification
are **frozen and sha256-hashed before the first probe call**; no item or pair is
added/dropped/re-binned after. An **independent pre-run critic** certifies, against the
frozen set, that (i) the add and cancel arms are at matched task structure (both bases at
ceiling, or the pair is rejected per B2), and (ii) **no difficulty-only reader reproduces
the add-easy/cancel-hard asymmetry** — a NO-GO defers the run rather than relaxing the bar.
The **falsify arms stay live**: a symmetric matched result, or a reversal (the new pair's
cancel easy / add hard), is recorded as a clean falsification, with no re-pairing or
re-tuning after seeing outputs. Ratifying this decision fixes the **yardstick**, never the
result; the probe is **not** run, nor the pair/certification re-tuned, in any session that
ratifies.

## What the later ratifying reviewer should weigh

1. Is the **two-leg split (A3)** worth its doubled build cost, or should the project run only
   the new-pair `internal-contrast-only` leg (A1/A2) and rely on the existing
   [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
   for the human-anchored side?
2. Does the **resultative add arm** have genuine headroom — can a non-resultative control be
   built whose default does **not** already carry the state-change entailment — or does the
   AANN default-coincidence trap recur, leaving the add arm unable to move?
3. Is the **blocking ceiling gate (B2)** the right strictness, or does it risk discarding
   informative near-ceiling pairs; and is the conative-cancel-v2 reading rule (B1) directly
   transportable to a new construction, or does the new pair need its own frozen slope
   threshold (as cc-v2 froze its cliff-threshold with the item set)?
4. Is `internal-contrast-only` the honest posture for the new-pair leg, or does opening this
   line imply a human-comparison ambition that should make fetching a new human-rated
   constructional anchor a goal rather than an optional upgrade?

## Ratification attempt 1 — session 132 (2026-06-28): KEEP-OPEN

Per [`PROTOCOL.md`](../../../PROTOCOL.md) §2, the first cross-session boundary having passed
(opened session 131, eligible session ≥ 132), an **independent fresh-agent adversarial review**
read this decision, its companion scoping page, the conjecture, the cc-v2 paradigm and its
governing decision, the conflicting-cue posture, the descriptive answer-key result, and the
Scivetti resource, and returned **KEEP-OPEN**. The decision **remains `open`**; the yardstick is
**not** frozen and the spend-bearing battery stays blocked. The review affirmed the surfacing
discipline (freeze-and-hash, independent pre-run critic, live falsify arms, "fixes the yardstick
never the result") as exemplary and ratifiable in posture — but identified concrete,
must-discharge-before-freeze gaps. **A future session may re-attempt ratification only after the
four prerequisites below are supplied** (the first is the load-bearing blocker):

1. **Demonstrated add-arm headroom on frozen calibration items (the blocker).** Option A3 commits
   to the **resultative** add arm (via A1), but the review judged its headroom *undemonstrated and
   plausibly degenerate*: resultatives canonically attach to verbs whose action already co-occurs
   with the result state, so a non-resultative control may supply the state-change entailment *for
   free* — the AANN default-coincidence trap the decision itself names, with resultative already at
   0.77–0.89 base accuracy in
   [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
   and no off-ceiling licensing signal there. If the add arm pins at ceiling with nothing to
   measure, "add easy / cancel hard" becomes a near-tautology of the arm construction rather than a
   finding — an *inadvertent* path to spurious confirmation (the anti-cheat concern runs toward a
   degenerate add arm, not toward manufactured suppression). A future session must show, on frozen
   calibration items *before* the main run, that a genuinely non-result-entailing control exists and
   the resultative add arm has real licensing-no-cue headroom against it — **or name a cleaner add
   construction**. The companion feasibility analysis opened this session,
   [`open-question/constructional-monotonicity-addarm-headroom`](../../findings/open-questions/constructional-monotonicity-addarm-headroom.md),
   begins this work at the design level (it does **not** demonstrate headroom — that needs a probe).
2. **Concrete frozen thresholds for B2 and the slope rule.** B1+B2 re-uses the cc-v2 *reading-rule
   shape*, but the review noted cc-v2's cliff/slope threshold was frozen **with its item set**
   (item-set-specific, not a portable constant). The new pair therefore owes its **own** frozen
   ceiling cutoff and slope threshold, as fixed numbers set before data — not inherited by pointer.
   The decision currently leaves both as "e.g." placeholders.
3. **An explicit, justified add/cancel direction assignment for the chosen pair, frozen in
   advance** — especially relevant if A2 (Levin) is ever reconsidered, since Levin alternations
   "are not all cleanly add vs cancel" and the direction call must not be chosen to fit.
4. **A reconsidered scope decision once (1) is known.** With
   [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
   already covering the anchored base comparison (and finding it "small and inconsistent in sign,"
   explicitly "not the matched-difficulty test"), the review questioned whether A3's second
   (anchored-replication) leg earns its doubled build cost, or whether a single
   feasibility-verified new-pair `internal-contrast-only` leg is the more honest and economical
   yardstick. The `internal-contrast-only` posture for the new-pair leg (weigh-question 4) was
   affirmed as correct and ratifiable on its own.

## Prerequisite (1) DISCHARGED — session 133 (2026-06-28); decision stays OPEN

The s132 blocker (prerequisite 1, "demonstrated add-arm headroom on frozen calibration items")
is **discharged**. A frozen, pre-registered calibration probe was built, passed an independent
pre-run critic (GO), run ($0.068 billed), and verified by an independent post-run agent (every
number reproduced): [`result/addarm-headroom-calibration-v1`](../../findings/results/addarm-headroom-calibration-v1.md)
([`run record`](../../../experiments/runs/2026-06-28-addarm-headroom-calibration/README.md);
[`open-question/constructional-monotonicity-addarm-headroom`](../../findings/open-questions/constructional-monotonicity-addarm-headroom.md)
now `answered`). On a frozen gate (construction licensing-no-cue affirm ≥ 0.80 **and** a
non-construction control's affirm ≤ 0.40, ≥ 4/12 verbs):

- **Resultative DEMONSTRATES HEADROOM** — 10/12 verbs headroom-clean (construction affirm
  **1.000**, control **0.250**). The degeneracy worry is **not** borne out: a genuinely
  non-result-entailing bare-transitive control exists ("hammered the metal" ⊬ "the metal became
  flat"; "kicked the door" ⊬ "the door became open"). Only the genuinely telic `freeze→solid`
  and `sharpen→sharp` had controls already at ceiling — the trap is **real but verb-specific and
  avoidable by verb selection** (verified exclusion list: `freeze`, `sharpen`).
- **Intrans-motion also DEMONSTRATES HEADROOM** — 7/12 aggregate (8 in ≥ 2/3 models;
  construction **0.972**, control **0.333**), naming a cleaner-or-equal alternative add arm
  (trap verbs: `drift`, `slide`, `swing`, `bounce`). This satisfies the prerequisite's explicit
  "**or name a cleaner add construction**" branch.

**What this means for ratification.** The load-bearing blocker is cleared, and the decision now
has a **concrete usable verb pool + verified trap-exclusion list** for either construction. But
prerequisites **2** (concrete frozen B2 ceiling cutoff + slope/cliff threshold as fixed numbers
for the *main* battery item set — the calibration froze numbers for the *calibration*, not the
main run), **3** (explicit pre-frozen add/cancel direction assignment for the chosen pair), and
**4** (the reconsidered scope decision — whether A3's anchored-replication leg earns its doubled
cost now that a single feasibility-verified new-pair `internal-contrast-only` leg is shown
viable) are **still owed**. **The decision therefore stays `open`; this session ratifies
nothing** (it produced the discharging evidence — anti-cheat §2 bars the producing session from
also being the sole ratifier). A future session may re-attempt ratification once 2–4 are
discharged; an independent fresh-agent review then fixes the yardstick (never the result).

## Prerequisites 2–4 supplied — session 134 (2026-06-28); a $0 design unit

Per the s132 review's instruction ("A future session may re-attempt ratification only after the
four prerequisites below are supplied") and the s133 handoff ("set prerequisites 2–4 … first;
then a fresh review can ratify"), this session — which did **not** produce the prerequisite-(1)
discharging evidence (that was s133) — supplies the three remaining prerequisites as **frozen,
provisional-until-ratified** design choices, folded into this same decision (no second decision
opened). They fix numbers and assignments **before any main-battery data exists**, so the
anti-cheat concern (tuning to a desired result) is structurally absent — no battery has run.
A fresh independent reviewer ratifies (or keeps open) the yardstick below; the producing session
does not self-ratify, and the ratifying session does **not** run the battery.

### Prerequisite (2) — concrete frozen thresholds for the MAIN battery (fixed numbers)

These are **the main battery's own** frozen numbers (item-set-specific per the cc-v2 rule that the
slope/cliff threshold is "frozen WITH the item set"); they are **not** inherited from the
calibration set ([`result/addarm-headroom-calibration-v1`](../../findings/results/addarm-headroom-calibration-v1.md)
froze numbers for the *calibration*). All read panel-aggregate NLI unless stated; "≥2/3 models"
means the per-model value also clears the bar in at least two of the three panel models.

- **B2 blocking ceiling gate (run on a frozen calibration subset of the MAIN items, before the
  main run).** A pair is **admitted** only if, on that subset:
  1. **Add arm has real headroom:** construction licensing-no-cue affirm **≥ 0.80** AND a
     non-construction (bare-verb) control affirm **≤ 0.40**, in ≥2/3 models. (Re-applies the
     calibration's verified headroom criterion to the main item set; resultative already cleared it
     10/12 on the calibration set, but the main items must re-clear it.)
  2. **Cancel arm has a real default to suppress:** the lexical-default affirm (the inference the
     cancel construction is meant to suppress, measured on the bare/default frame) **≥ 0.80** in
     ≥2/3 models. (Mirrors cc-v2's transitive default at 91.7–100%.)
  If **either** fails, the pair is **rejected** and a different pair/verb-pool chosen **before** the
  main run — so the comparison can never silently become add-at-ceiling vs cancel-off-ceiling
  because the cancel default never reached ceiling.
- **Asymmetry-direction threshold (the "cliff" analogue, frozen).** On the discriminating no-cue
  cell — add licensing-no-cue vs cancel suppression-no-cue (`= 100 − cancel-construction_affirm`,
  exactly cc-v2's definition) — the verdict is read by a fixed **20 pp** margin:
  - **Confirms direction (confirm-leg 1):** add_no-cue − cancel_no-cue **≥ 20 pp** in ≥2/3 models.
  - **Symmetric → falsifies:** |add_no-cue − cancel_no-cue| **< 20 pp** in ≥2/3 models.
  - **Reversal → falsifies:** cancel_no-cue − add_no-cue **≥ 20 pp** in ≥2/3 models.
  The 20 pp margin is set against cc-v2's observed cancel-vs-add gaps (add ~ceiling 100 vs cancel
  suppression-no-cue 0–83), frozen here before any new-pair data, and is the project's choice, not
  a tuned bar; the falsify arms stay live.
- **Instrument-fragility threshold (confirm-leg 2), frozen.** The cancel arm's NLI-vs-FC
  disagreement on the no-cue cell must exceed the add arm's by **≥ 10 pp** in ≥2/3 models for
  confirm-leg 2 to register (cc-v2 showed gpt-mini cancel NLI 0 vs FC 33.3 = 33 pp, add near-uniform).
- **Cue-arm reading rule (inherited, unchanged):** the ratified cc-v2 rule — "≥ 70 % follow-
  construction in ≥ 2/3 models = robust; ~chance/cue-following = informative partial-null"
  ([`decisions/resolved/cc-v2-difficulty-operationalization`](cc-v2-difficulty-operationalization.md)) —
  governs the explicit-conflicting-cue arms of both directions; no new number is introduced for them.

### Prerequisite (3) — explicit, justified add/cancel direction assignment for the chosen pair

The chosen NEW pair instantiates the conjecture's own example — "**resultatives that *add* an
entailment versus aspectual/conative-type coercions that *cancel* a default**" — with the cancel
partner taken as an **aspectual** (not conative) coercion, so the pair is genuinely **beyond**
caused-motion / way / conative (confirm-leg 1's "new pair" requirement):

- **ADD arm = the resultative construction.** It **adds** the result-state entailment the bare
  verb lacks ("hammered the metal flat" ⊨ "the metal became flat"; bare "hammered the metal" ⊭ it).
  Verified headroom-clean verb pool (from the calibration, re-gated by B2 on the main items):
  **beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe**; **exclude the trap verbs
  `freeze`, `sharpen`** (telic; control already at ceiling).
- **CANCEL arm = the *for*-durative aspectual coercion of a semelfactive/punctual verb.** It
  **cancels** the single-bounded-event default ("the light flashed" ⊨ "it flashed once"; "the
  light flashed *for an hour*" coerces iteration → cancels "only once"). Provisional verb pool
  (semelfactive/punctual, **disjoint from the ADD pool** per the s134 ratification MOD-1, and
  de-duplicated per MOD-2): **flash, knock, tap, blink, jump, cough, nod** (battery session freezes
  the final set, verifying zero overlap with the resultative pool — `kick` and `bounce` removed
  because they appear in the add/calibration pools); the indicator is affirm-"happened only once"
  (the contestable default certified by B2 per MOD-3, NO-GO re-pairs before spend), default
  at ceiling on the bare frame (B2-gated), suppressed under the *for*-durative. This is the
  textbook aspectual coercion (Moens & Steedman / Pustejovsky-style), a **fresh** cancel
  construction distinct from the conative — so the cancel arm's own feasibility (default-at-ceiling
  + suppression headroom) is **certified by the B2 gate before the main run**, exactly as the
  add arm's was by the s133 calibration; if it fails B2, the battery session picks another cancel
  coercion before spending. The direction assignment is fixed here (add = resultative; cancel =
  *for*-durative aspectual) and **not** chosen to fit, closing the prerequisite-(3) gap the s132
  review flagged for the Levin option ("not all cleanly add vs cancel").

### Prerequisite (4) — reconsidered scope: run the single new-pair leg, drop A3's anchored leg

With prerequisite (1) discharged (a non-degenerate new ADD arm is buildable) the s132 review's own
weigh-question 1 resolves toward economy: **run only the new-pair `internal-contrast-only` leg
(A1-as-new-pair), and DROP A3's within-Scivetti anchored-replication leg.** Rationale:

- [`result/scivetti-cxnli-answer-key-v1`](../../findings/results/scivetti-cxnli-answer-key-v1.md)
  already covers the anchored base comparison for the old three and found it "small and inconsistent
  in sign," explicitly "**not** the matched-difficulty test" — so the anchored leg would re-measure
  a base the project already has, at doubled build/freeze/critic cost, without adding a
  human-comparison claim the matched-difficulty contrast can actually carry (the cue arms are
  `internal-contrast-only` either way).
- The generalization verdict rests, in **both** A3 and this single-leg design, on the unanchored
  new-pair leg; dropping the anchored leg removes cost, not evidential force.
- **Result posture (unchanged, affirmed):** the new-pair leg is `internal-contrast-only` per
  [`decisions/resolved/conflicting-cue-human-anchor`](conflicting-cue-human-anchor.md);
  no human-comparison claim is made; a future human-rated constructional anchor stays queued in
  `wanted.md`, not blocked on. (This narrows the provisional default's option (a) from **A3** to
  **A1-as-single-new-pair-leg**; option (b)'s **B1 + B2** certification is retained, now with the
  concrete numbers of prerequisite (2).)

### What is now owed before the spend-bearing battery

Nothing further at the *yardstick* level once a fresh review ratifies the above. The battery-
building session then: (i) freezes the resultative-add + *for*-durative-cancel item set and
sha256-hashes it; (ii) runs the B2 calibration subset and applies the blocking gate (NO-GO →
re-pair before spend); (iii) on GO, obtains an **independent pre-run critic GO** against the frozen
set; (iv) runs the matched battery and reads it by the frozen thresholds of prerequisite (2), with
the falsify arms live. The ratifying session runs **none** of this (anti-cheat §2).

## Ratification attempt 2 — session 134 (2026-06-28): ADOPT-WITH-MODS

Per [`PROTOCOL.md`](../../../PROTOCOL.md) §2, an **independent fresh-agent adversarial review**
(not the orchestrator that supplied prerequisites 2–4 this session; producing sessions 133/134
excluded as the *sole* ratifier) read this decision in full, its companion scoping page, the
conjecture, the cc-v2 paradigm + its governing resolved decision, the conflicting-cue posture, the
s133 add-arm headroom calibration, the descriptive answer-key result, the Scivetti resource, and
the coercion concept, and returned **ADOPT-WITH-MODS**. The yardstick is **fixed** (pair = A1
single new-pair `internal-contrast-only` leg; certification = B1 + B2 with the prerequisite-(2)
frozen numbers; A3's anchored leg dropped per prerequisite 4). The review confirmed the structural
anti-cheat case is strong (every prerequisite-(2) number is a threshold, not an observed value; no
main-battery data exists, so the retuning trap cannot apply; falsify arms are live and symmetric)
and that the `internal-contrast-only` posture is honestly scoped (no smuggled human-comparison
claim). Three **yardstick-hygiene** mods were required and are now applied above:

- **MOD-1 (verb-pool disjointness).** The CANCEL pool must be disjoint from the ADD pool;
  `kick` and `bounce` removed (they appear in the resultative/intrans-motion add pools), closing a
  verb-artifact-vs-direction confound. Applied in prerequisite (3).
- **MOD-2 (deduplicate).** The cancel pool had listed `blink` twice; the frozen set must contain
  distinct verbs. Applied.
- **MOD-3 (gated contestable default).** Because "happened only once" is a contestable
  entailment, the cancel arm's B2 default is certified with that explicit indicator and a NO-GO
  (default < 0.80 in ≥2/3 models) **re-pairs** the cancel coercion before any spend rather than
  relaxing the bar. Made binding in prerequisites (2)/(3).

The reviewer verified the cited cc-v2 numbers against their source (suppression-no-cue range 0–83;
gpt-mini cancel NLI 0 vs FC 33.3 = 33 pp) and found no over-claim and clean anchor discipline. The
one substantive defect (D1: the verb-pool overlap/duplication) is fixed by MOD-1/MOD-2. **This
fixes the yardstick, never the result; no battery is run and no threshold re-tuned in this
session.**

### Downstream artifact promotions (applied session 134)

- [`conjecture/constructional-monotonicity-asymmetry`](../../findings/conjectures/constructional-monotonicity-asymmetry.md)
  **stays `proposed`** — the decisive test is now *operationalized and ratified*, but no battery has
  run, so it does not advance to `designed`/`tested`. Not promoted.
- [`open-question/constructional-monotonicity-generalization-design`](../../findings/open-questions/constructional-monotonicity-generalization-design.md)
  → **`answered`**: both gates it surfaced are now resolved (operationalization ratified; human-anchor
  question resolved as `internal-contrast-only` for the new-pair leg).
- [`open-question/constructional-monotonicity-addarm-headroom`](../../findings/open-questions/constructional-monotonicity-addarm-headroom.md)
  — already `answered` (s133); unchanged.
