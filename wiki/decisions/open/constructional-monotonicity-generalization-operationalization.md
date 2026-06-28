---
id: constructional-monotonicity-generalization-operationalization
title: Which NEW add-vs-cancel construction pair does the monotonicity-generalization battery use, and how is its matched-difficulty / ceiling certification fixed before any data?
status: open
opened: 2026-06-28
opened-by: autonomous (session 131, scoping the monotonicity-asymmetry generalization test)
contingent-artifacts:
  - conjecture/constructional-monotonicity-asymmetry
  - open-question/constructional-monotonicity-generalization-design
---

> **Status: OPEN — opened this session (session 131); NOT ratifiable until a later
> session per [`PROJECT.md`](../../../PROJECT.md) §12.3 / [`PROTOCOL.md`](../../../PROTOCOL.md) §2.**
> This page surfaces an operationalization choice that must be **frozen before any
> data**; it does not decide it. There is no `resolution:` and no `resolved-by:` —
> ratification is for a later session's independent adversarial-review pass with written
> rationale. The companion scoping page is
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
  under [`decisions/resolved/cc-v2-difficulty-operationalization`](../resolved/cc-v2-difficulty-operationalization.md)).

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
  [`decisions/resolved/cc-v2-difficulty-operationalization`](../resolved/cc-v2-difficulty-operationalization.md)
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
  [`decisions/resolved/cc-v2-difficulty-operationalization`](../resolved/cc-v2-difficulty-operationalization.md)
  yardstick), **plus** a blocking pre-run ceiling gate so a new pair whose lexical default or
  add licensing is off ceiling is rejected *before* the main run rather than compared
  unfairly.
- **Result posture:** new-pair leg `internal-contrast-only` (per
  [`decisions/resolved/conflicting-cue-human-anchor`](../resolved/conflicting-cue-human-anchor.md));
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
