---
type: open-question
id: constructional-monotonicity-generalization-design
title: "How would a matched-difficulty, ceiling-controlled battery test whether the add/cancel monotonicity asymmetry generalizes to a NEW construction pair — and which pair, with what human anchor?"
meaning-senses:
  - constructional
  - inferential
status: open
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: refines
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Open question: a matched-difficulty generalization test for the add/cancel monotonicity asymmetry

> **Why this page exists.** [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
> is `status: proposed` — the project's forward bet that current decoders treat a
> construction's inferences as readily **additive** (license an added entailment) but
> resist **retraction** (suppress a lexical default less reliably). Its "What would
> confirm / falsify" section names a single decisive test: a **matched-difficulty,
> ceiling-controlled add-vs-cancel battery on NEW construction pairs**, with the
> [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)
> paradigm as the template. This page takes that conjecture from `proposed` toward
> `designed` **without running anything and without picking the design**. It is a
> **scoping** page: it states sharply what the generalization test must show, lays out
> candidate new construction pairs, fixes the matched-difficulty paradigm by pointer,
> surfaces the human-anchor tension honestly, and names the two gates a later session
> must open and (cross-session) ratify. Provisional defaults are recorded; **neither
> gate is decided here**.

## What the generalization test must show (verbatim from the conjecture)

The conjecture's confirm/falsify criteria are the yardstick. Quoted from
[`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md),
*What would confirm / falsify*:

**Confirms (jointly):**

1. "The asymmetry **generalizes to new add-vs-cancel construction pairs** beyond
   caused-motion / way / conative — for example, other Levin alternations, or
   resultatives that *add* an entailment versus aspectual/conative-type coercions that
   *cancel* a default — tested at **matched difficulty and ceiling** (the add and cancel
   arms placed in a common paradigm, as conative-cancel-v2 did); AND"
2. "The cancel direction is reliably **more instrument-fragile** (larger
   NLI-vs-forced-choice disagreement) than the add direction on the same items — the
   pattern already seen for the conative."

**Falsifies (either):**

- "A matched, ceiling-controlled battery shows **symmetric** add/cancel performance —
  once difficulty is equated, the add and cancel arms are statistically
  indistinguishable; OR"
- "The asymmetry **reverses** for some construction class — a construction whose *cancel*
  direction is easy and whose *add* direction is hard."

And the conjecture's own scope discipline on the null: "A null on the generalization test
(the asymmetry fails to extend beyond the three constructions seen so far) would retire
the conjecture as an artifact of those particular items, not establish a competing claim."

### Why a NEW add-vs-cancel pair is required

The de-confounded asymmetry rests on exactly **three constructions**, across two
directions: the **add** leg is caused-motion plus the *way*-construction
([`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md),
[`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md)),
and the **cancel** leg is the conative
([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)).
Re-running any of those three cannot test *generalization* — it tests replication.
Confirm-leg 1 is, by its own wording, a claim about **new pairs**: the asymmetry must
show up for an add-vs-cancel pair the project has **not** already used. So the
generalization test needs at least a **fourth** construction (and ideally a fresh
add/cancel *pair*) beyond caused-motion / way / conative. This is the structural reason a
matched re-test of the existing three, however clean, is necessary-but-not-sufficient for
the conjecture — and the source of the design tension below (the human anchor only covers
the old three).

## The matched-difficulty / ceiling-control paradigm (fixed by pointer, not re-invented)

The conjecture names [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)
as the template, and this page does **not** re-specify it — it points at it, so the
generalization test inherits the already-ratified difficulty operationalization
([`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md))
rather than spawning a parallel one. The load-bearing features to carry over:

- **A common conflicting-cue paradigm for both arms.** conative-cancel-v2 "put the cancel
  direction into the *same* conflicting-cue paradigm the add-direction v2 used, so the two
  are compared at matched task structure." The generalization battery must place its new
  add arm and new cancel arm in **one** paradigm, so "add easier than cancel" cannot be an
  artifact of the add items merely being easier.
- **Cancel measured as suppression-with-no-cue against a ceiling lexical default.** The
  discriminating cell in conative-cancel-v2 is the **no-cue** construction reading:
  "suppression-no-cue = `100 − conative_affirm` (construction-following with no cue) — the
  matched analogue of the add-direction's canonical/licensing-no-cue (~70–100%, mostly
  ceiling)." The new pair needs a lexical default that is itself **at ceiling** (so the
  cancel arm has a real default to suppress), with the cancel arm read as how reliably the
  construction holds that default down — against the add arm's matched licensing-no-cue.
- **The dual indicator (NLI + forced-choice).** Both instruments are kept (per the
  governing decision: "keep both NLI + forced-choice"). Confirm-leg 2 *is* the cancel
  direction's predicted **larger instrument-fragility** — the NLI-vs-forced-choice
  disagreement the conative already showed: gpt-5.4-mini "fails conative suppression
  entirely under NLI" (conative affirm 100%; §"One-line finding") yet "recovers under FC
  (66.7%)" (§"Two distinct off-ceiling failures"). So the dual
  instrument is not redundancy here; the *size of its disagreement on the cancel arm vs the
  add arm* is one of the two confirms.

## Candidate new add-vs-cancel construction pairs (drawn only from named sources)

These are candidates the matched-difficulty battery **could** use, drawn **only** from
constructions/alternations already named in the conjecture or its cited pages. For each,
the honest in-repo human-anchor status is stated — **most have none**, and no dataset is
invented.

- **Resultative (ADD) vs an aspectual/conative-type coercion (CANCEL).** The conjecture
  itself offers this pairing — "resultatives that *add* an entailment versus
  aspectual/conative-type coercions that *cancel* a default." The **Resultative** is one of
  Scivetti's eight constructions
  ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md):
  "Causative-With, Caused-Motion, Comparative-Correlative, Conative, Intransitive Motion,
  Let-Alone, Resultative, Way-Manner") and was probed descriptively in
  [`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md)
  (n = 66, acc 0.77–0.89) — but it is **not** one of the four ratified-anchor constructions
  (caused-motion, conative, way-manner, comparative-correlative; ratified 2026-05-29). So
  the resultative add arm has a *descriptive* human-annotated answer key on its Scivetti
  items but **no ratified human-comparison anchor** for a matched contrast, and a paired
  cancel coercion would be a fresh own-design construction with **no in-repo human anchor**.
- **Other Levin alternations (ADD or CANCEL, depending on the alternation).** The conjecture
  names "other Levin alternations" as a candidate source. These are own-design minimal-pair
  families with **no in-repo human anchor** — Levin's alternation inventory is not catalogued
  as a `resource` page, so any Levin-alternation pair would run `internal-contrast-only`
  unless and until a human-rated anchor is fetched and ratified. (Do **not** treat the
  conjecture's mention as a dataset; it is a class of phenomena, not a labelled corpus.)
- **The *way*-construction's near-neighbours / a fresh add coercion paired with a fresh
  cancel coercion.** [`concept/coercion`](../../base/concepts/coercion.md) frames the
  add/cancel directions generally; any new add coercion (a construction that contributes an
  entailment the verb lacks) paired with a new cancel coercion (a construction that
  suppresses a lexical default) would satisfy confirm-leg 1's "new pair" requirement. All
  such own-design pairs carry **no in-repo human anchor** and would be `internal-contrast-only`.

The candidate list deliberately **avoids inventing a dataset**: the only in-repo
human-annotated constructional resource is Scivetti CxNLI, and what it affords is treated
honestly in the next section.

## The human-anchor question (surfaced honestly)

This is the load-bearing difficulty. The candidate human anchor is the **Scivetti CxNLI
dataset** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)),
cited by the feature that bears: it carries human-annotated NLI triples for the add-type
**Caused-Motion** and **Way-Manner** and the cancel-type **Conative**, with a native-speaker
baseline (≈0.90 on Exp 1), and it is the ratified answer-key anchor for those constructions.
But two limits constrain its use here, both verbatim from the resource page's *Known limits*
/ *What it cannot ground*:

1. **It can anchor only its own constructions.** Its human-comparison force is confined to
   the constructions it labels — for the add/cancel question, that is **Caused-Motion,
   Way-Manner, and Conative**: precisely the **old three** the generalization test must go
   *beyond*. The resource page is explicit that AANN and any non-listed construction are not
   grounded by it; a brand-new construction pair is, by the same logic, **not** anchored.
2. **A single gold label per item, not a gradient.** "the release gives a *single*
   adjudicated gold label per item, not a per-item multi-rater distribution — so it anchors
   an answer-key comparison, not a graded human-judgment gradient." So even on its own
   constructions it supports an **answer-key** comparison, not the per-item human-rating
   gradient a matched-difficulty *gradient* contrast might want.

It follows that a **new** add-vs-cancel pair built for generalization would likely have **no
in-repo human anchor**, so its off-ceiling cue arms would be `internal-contrast-only` — the
already-ratified posture for exactly this situation
([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md):
"leave the internal-contrast-only results … as internal-contrast-only … they make no
human-comparison claim"). That is a strictly **weaker, within-model** claim, and the
existing cancel-direction result already lives under it
([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md) carries
`anchor: internal-contrast-only`).

### The resulting design tension, and a provisional resolution (not a decision)

The tension is sharp: **generalization wants a NEW pair (unanchored), but human-comparison
wants Scivetti's THREE existing constructions (anchored).** The two pull in opposite
directions and cannot both be maximized in one arm.

**Provisional default (NOT a decision):** run **two legs**, kept distinct in their claim
strength —

- **A human-anchored leg:** a within-Scivetti **matched-difficulty re-test of the existing
  three** (Caused-Motion / Way-Manner as add, Conative as cancel) placed in the common
  conflicting-cue paradigm. This leg can make a *human-comparison* answer-key statement on
  the base arm (anchored to Scivetti), with its off-ceiling cue arms `internal-contrast-only`
  — the exact posture conative-cancel-v2 already uses. It tests **replication at matched
  difficulty**, not generalization.
- **A new-pair internal-contrast leg:** the chosen NEW add-vs-cancel pair (e.g.
  resultative-add vs a fresh cancel coercion) in the *same* paradigm, run
  `internal-contrast-only` (no human anchor), to test **confirm-leg 1's "new pair"**
  requirement.

The generalization verdict then rests on the **new-pair leg** (within-model), with the
anchored leg supplying the human-calibrated replication. This split is **laid out, not
chosen**; which new pair, and how the two legs' verdicts combine, is the operationalization
gate below.

## The two gates (surfaced, not resolved)

This page surfaces two decisions a future session must open and — per the cross-session rule
([`PROJECT.md`](../../../PROJECT.md) §12.3, [`CLAUDE.md`](../../../CLAUDE.md) rule 5) —
**ratify in a later session**, each with a provisional default recorded but neither decided
here:

1. **Operationalization gate** (created this session as a `wiki/decisions/open/` entry,
   [`decisions/open/constructional-monotonicity-generalization-operationalization`](../../decisions/open/constructional-monotonicity-generalization-operationalization.md)):
   **which** new add-vs-cancel construction pair(s) the matched-difficulty battery uses, and
   the **matched-difficulty / ceiling-certification criterion** (what must be true of the
   frozen item set so the comparison is *add-at-matched-structure vs cancel-at-matched-
   structure*, not *add-at-ceiling vs cancel-off-ceiling* — mirroring how conative-cancel-v2
   was certified). Provisional default: the resultative-add vs fresh-cancel pair as the
   new-pair leg, with the ceiling-certification mirroring the
   [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md)
   reading rule (the add arm's licensing-no-cue at ceiling, the cancel arm's lexical default
   at ceiling, before any suppression is read). **Not decided here.**
2. **Human-anchor question** (the load-bearing difficulty above): whether a new pair can be
   given any in-repo human anchor, or runs `internal-contrast-only`. Provisional default:
   `internal-contrast-only` for the new-pair leg (per the ratified conflicting-cue posture),
   with the within-Scivetti leg carrying the only human-comparison claim, scoped to the three
   anchored constructions. **Not decided here.** A future human-rated harder anchor would be
   queued in `wanted.md`, not blocked on.

## Scope and limits

- **Small N is intrinsic.** Every input result is small-N, single-run, single-date, panel-as-
  subjects ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md):
  "12 verbs × 3 conditions × 3 models; rates carry wide per-cell uncertainty. Read as a
  direction-of-effect signal, not a precise magnitude."). The generalization battery would
  inherit this: a **direction-of-effect** probe, not a coverage benchmark.
- **Direction-of-effect, not magnitude.** The asymmetry is a direction claim (add easier than
  cancel), not a calibrated effect size; a matched battery tests *whether the direction
  reappears on a new pair*, not how large it is.
- **The asymmetry is a forward bet, not established.** The conjecture is explicit that it is
  "a forward bet that it *generalizes*; it is explicitly **not** presented as established."
  This page scopes a test, it does not assume the outcome — a symmetric or reversed result on
  the new pair is a first-class falsification, and a null retires the conjecture rather than
  establishing a rival.
- **Both directions are already bounded.** Neither direction is a deep competence:
  [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) bounds the add
  direction's depth (its withholding is "explicit-outcome parsing, not world-model
  integration"), so the generalization test asks only about the **relative** reliability of
  the two directions, not about either as a standalone competence.
- **Base-level accuracy is not the test.** [`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md)
  already showed that at the base answer-key level the add/cancel difference is "small and
  **inconsistent in sign**" — that is *consistent with* the conjecture's scope (the asymmetry
  is posited for the de-confounded suppression-with-no-cue arms, not base NLI accuracy) and is
  **not** the matched-difficulty test. The generalization test lives in the cue arms, not the
  base answer key.

## Status: open (scoping only)

This page does not run anything and ratifies neither gate. It states the generalization
test's confirm/falsify criteria, argues why a NEW construction pair is required, lists
candidate pairs (with honest anchor status), fixes the matched-difficulty paradigm by
pointer to [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md),
surfaces the human-anchor tension, and names the two gates with provisional defaults. The
operationalization gate is opened as a companion `wiki/decisions/open/` page this session;
both it and the human-anchor question await a **later** session's independent
adversarial-review ratification before any probe runs.
