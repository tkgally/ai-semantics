---
id: aann-inferential-operationalization
title: Operationalize the AANN conjecture's MEANING clause — which indicator shows the unification + evaluation inferences are drawn, and what (if anything) anchors it?
status: open
opened: 2026-06-13
opened-by: autonomous (workflow session 2026-06-13, v3 follow-up to the v2 gradient result)
contingent-artifacts:
  - conjecture/aann-construction
---

# Decision: an inferential operationalization for the AANN v3 probe

## Why this exists

The v2 behavioral probe ran 2026-06-12 and came back SUPPORTED:
[`result/aann-behavioral-gradient-v2`](../../findings/results/aann-behavioral-gradient-v2.md)
shows all three panel models' prompted acceptability rank-tracks the human MTurk gradient and
replicates it on frequency-matched held-out adjectives. But that result's own scope section is
explicit: it says **nothing about the inferential half** of
[`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md) — "does the
model draw the unified-stretch/evaluative paraphrase?" — which it names "a different indicator,
explicitly out of this design's scope (§8) and the natural v3 question." The conjecture's
status note says the same: v2 supports the **productive-gradient** half; the **inferential
half** (does the model *use* the construction's unification/evaluation semantics, in the
`constructional` + `inferential` senses?) remains untested.

The clause to operationalize is the conjecture's characteristic-semantics claim: the AANN noun
phrase (*a beautiful three days*) presents the measured quantity as **a single unified,
evaluated stretch** — one three-day span, evaluated as beautiful as a whole — not a plural
count of individuals each bearing the property (*three separate days, each beautiful*). The
question is which indicator shows a model **draws the inferences this semantics licenses**,
rather than merely rating the form acceptable (the v2 territory) or echoing its distributional
signature.

Choosing that indicator is a value-laden operationalization call, so it is surfaced here, not
auto-taken (CLAUDE.md rule 5). It has the same shape as the ratified v2 instrument decision
([`decisions/resolved/aann-behavioral-operationalization`](../resolved/aann-behavioral-operationalization.md))
and is its successor question.

**This page was opened 2026-06-13. Eligible for ratification: next session at the earliest,
via the independent adversarial-review procedure (PROJECT.md §12.3). The v3 design may be
drafted before ratification (design-writing is not probe-running), but no AANN v3 probe may
run this session, and no finding-bearing call may be made until this page is resolved.**

## The decision (two parts)

1. **Indicator:** which instrument operationalizes the unification + evaluation inference?
2. **Anchor:** what grounds the result — explicitly including the honest admission that the
   existing AANN anchor does **not** transfer (see "The anchor sub-question" below).

Both parts must be resolved together; a ratified indicator with an unsettled anchor status
would just reopen at the verification gate.

## Options for the indicator

### Option A — paraphrase forced-choice (provisional default, paired with B)

Minimal-pair paraphrase selection. Premise: an AANN sentence (*We spent a beautiful three days
in Rome*). Forced choice between a **unification-respecting** paraphrase ("one unified
three-day stretch, evaluated as beautiful as a whole") and a **distributive** paraphrase
("three separate days, each of which was beautiful"). Control arm: the minimally different
non-AANN string (*three beautiful days*), where the distributive reading is at least available
and on some analyses preferred — the indicator is the **AANN-vs-control shift** in paraphrase
choice, not the raw AANN choice rate.

- **What it measures:** whether the construction *changes which reading the model commits to* —
  the closest behavioral analogue of "drawing the unification inference," in the `inferential`
  sense.
- **Distributional-shadow confound:** the model could select the unification paraphrase
  because *a* + singular-flavored language co-occur distributionally (the article alone cues
  "one ..."), without computing anything about the described stretch — the worry
  [`open-question/distributional-vs-inferential-constructional`](../../findings/open-questions/distributional-vs-inferential-constructional.md)
  states as "a distributional probe wearing a meaning-shaped mask" (where "meaning" there is
  the constructional/inferential sense). Mitigations the design must carry: lexical-overlap
  parity between the two paraphrases (neither may share more surface material with the
  premise), the non-AANN control arm as the subtraction, and at least some items where the
  distributive paraphrase is the locally fluent continuation (inference under distributional
  pressure, that open question's "core move").
- **Instrument-fragility risk:** forced-choice is precisely where gpt-5.4-mini cracked on the
  comparative correlative ([`open-question/instrument-sensitivity-constructional-inference`](../../findings/open-questions/instrument-sensitivity-constructional-inference.md):
  an excluded-middle over-inference localized to FC; per-model NLI-vs-FC gaps up to 50 pp in
  one cell). A forced binary between two paraphrases that are *both* often pragmatically true
  (a beautiful stretch usually contains beautiful days) invites exactly such artifacts.
- **Cost shape:** cheap. v2-scale call counts (low hundreds of items × 3 models × locked
  settings); v2 cost $0.3125 for 1,782 calls. Well under $1.

### Option B — entailment-style NLI (provisional default, paired with A)

Premise: AANN sentence vs. minimal non-AANN control (*a beautiful three days* / *three
beautiful days*, lexically matched). Hypotheses probe the licensed inferences directly,
affirm/withhold (the house NLI framing): singularity/unification ("the stay was a single
continuous stretch"; "the days are presented as one unit"), whole-evaluation ("the stretch,
*as a whole*, was beautiful" vs "each day, taken individually, was beautiful"), and — the
sharpest sub-probe — the **singular/plural agreement contrast**, which is grammaticalized
rather than pragmatic: *A beautiful three days **was** what we needed* vs *Three beautiful
days **were** what we needed* style continuations/judgments, where the AANN phrase's singular
construal has a hard morphosyntactic reflex.

- **What it measures:** whether the construction licenses/withholds specific entailments —
  the `inferential` sense operationalized as the meaning-senses page prescribes ("entailment
  datasets, NLI behavior").
- **Distributional-shadow confound:** affirm/withhold can ride on world-knowledge
  plausibility; worse, the unification and distributive readings are *Gricean neighbors*
  (each-day-beautiful is a natural post-hoc inference from a-beautiful-stretch), so NLI's
  known permissiveness — [`result/caused-motion-near-miss-v2c`](../../findings/results/caused-motion-near-miss-v2c.md)
  found NLI uniformly admits Gricean readings that FC's strict-entailment framing withholds —
  will blur exactly the contrast at issue. The agreement sub-probe is the defense: singular
  agreement with a plural noun head is distributionally *dispreferred* in general text, so
  affirming it for AANN subjects specifically cuts against the local gradient.
- **Instrument-fragility risk:** the converse of A's — NLI collapsed gpt-5.4-mini's conative
  inference entirely (−8 pp gap where FC showed +42 pp). A single-instrument NLI headline
  would be exposed to the same objection in reverse.
- **Cost shape:** cheap, same shape as A; the two together remain in the v2 cost band
  (estimate ≲ $1 combined at v2-like item counts; pre-flight estimate owed before any run,
  CLAUDE.md rule 8).

### Option C — generation-and-code

Free continuation or open answer ("How was the trip?"; "What does this sentence say about the
days?"), post-coded for unification-consistent language (singular anaphora, "the stretch,"
singular agreement in the model's own production, whole-evaluation predicates).

- **What it measures:** spontaneous use of the construal in production — in principle the
  strongest evidence that the unification semantics is *used*, not just selected when offered.
- **Distributional-shadow confound:** strongest of the three — generated singular language may
  simply echo the article *a* in the prompt; production fluency is the distributional signal
  in nearly pure form.
- **Instrument-fragility risk:** the coding step is the instrument, and it is the riskiest
  part: hand-coding by the session is a judgement call with no inter-rater check (no human
  subjects available, CLAUDE.md rule 4), and model-coding imports an LLM-judge validity
  question the repo has not ratified. Adds a fragility *layer* on top of the elicitation
  fragility the open question documents.
- **Cost shape:** moderately more expensive (longer generations) plus a coding pass; the real
  cost is validity, not dollars.

## Provisional default (indicator)

**A + B as a two-instrument package** — paraphrase forced-choice and entailment-style NLI on
the same frozen items, mirroring the house NLI+FC pattern used for the conative, caused-motion
and way probes — **with the singular/plural agreement contrast included in both arms as the
sharpest single probe** (grammaticalized, hence least Gricean-permeable and most resistant to
the plausibility shadow). One instrument must be pre-registered as primary before any model
call; the provisional proposal is **A (paraphrase forced-choice) primary, B as the convergent
robustness arm**, because A's AANN-vs-control *shift* design directly subtracts the
distributional baseline, while B's affirm/withhold absolute rates are more exposed to the
Gricean-neighbor problem. Per-instrument disagreement is reported as a named statistic
(|FC shift − NLI shift| per model), feeding
[`open-question/instrument-sensitivity-constructional-inference`](../../findings/open-questions/instrument-sensitivity-constructional-inference.md)
rather than being averaged away. Option C is **demoted to an optional exploratory arm at
most** (never the headline; run only if budget and a pre-declared coding rubric exist), for
the validity reasons above. Discipline carries forward from the v2 decision: thresholds,
item lists, per-model settings locked before any finding-bearing call; no post-hoc retuning;
a Tier-0-style manipulation check with a pre-declared failure consequence.

Rationale in brief: a single instrument is indefensible at exactly this tier — the in-repo
instrument-sensitivity record shows Tier-4 inference measures can swing up to 50 pp with
framing, in *both* directions (NLI collapse on the conative; FC crack on the comparative
correlative) — so convergence across the two house instruments, with the primary fixed in
advance, is the only headline this repo's own methodology pages would let stand.

## The anchor sub-question (decide here, not at write-up)

**Mahowald's MTurk ratings are acceptability ratings; they do not anchor an inference
measure.** [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
records 1–10 *acceptability* judgments (Exp 1–3); no human in that dataset was ever asked
whether *a beautiful three days* denotes one evaluated stretch or three beautiful days. The
resource anchored v2 because v2's indicator was itself graded acceptability
(measure-homology was the ratified validity leg); a paraphrase-choice or entailment indicator
has **no measure-homologous human data in-repo**. Reusing the v2 anchor here would be a
category error, and this page exists partly to block it.

Honest options:

- **(i) `anchor: internal-contrast-only`.** The v3 result's force is the within-model
  AANN-vs-control contrast (does the construction shift paraphrase choice / entailment
  behavior relative to the minimally different non-AANN string); **no human-comparison claim
  is made.** Per CLAUDE.md, this terminal state requires ratification (precedent:
  [`decisions/resolved/conflicting-cue-human-anchor`](../resolved/conflicting-cue-human-anchor.md),
  ratified by Tom; from 2026-06-12 the autonomous cross-session procedure applies) — adopting
  this page under the autonomous procedure can ratify it for the v3 result, since the anchor
  status is part of this decision.
- **(ii) Literature-stipulated gold key.** Author-coded expected inferences from the published
  AANN semantics literature — the unification/evaluation analysis the conjecture page
  describes, and the constraint literature the resource page names (Solt 2007 on
  unit-coercion; Dalrymple & King 2019; Bylinina & Nouwen 2018). This fixes *which answers
  count as unification-consistent* (a scoring key), but it is **expert-stipulated, not
  behavioral-human-anchored**: no human judgment data, only theorists' analyses. It must not
  be dressed up as a human anchor; at most it is the key under option (i)'s internal contrast,
  and any of its codings that the literature genuinely disputes must be flagged item-level.
- **(iii) Defer until a human inference dataset is found.** A human-rated AANN
  paraphrase/inference set would be the real anchor; **none is known in-repo** and none is
  catalogued in the resource pages. Honest, but it blocks the v3 indefinitely on a dataset
  that may not exist; the queue-in-`wanted.md` route remains open regardless of the choice
  here.

**Provisional default (anchor): (i) + (ii) combined** — the v3 result runs
`anchor: internal-contrast-only` (within-model AANN-vs-control shift; no human-comparison
claim), scored against a literature-stipulated expected-inference key that is explicitly
labeled as expert-stipulated in the design and on the result page. The Mahowald resource
remains linked only as the *stimulus provenance and v2 gradient anchor*, never as the
inference anchor. If a human AANN-inference dataset is later found, promoting to a
human-comparison claim is a **new** anchor question, opened fresh (the
conflicting-cue precedent's rule). The chief cost of this default is stated plainly: the v3
can then never say "models draw the inference *the way humans do*" — only that the
construction shifts the models' inferential behavior relative to a matched control, in the
direction the published semantics predicts.

## What is contingent on this

- The AANN v3 design (`design/aann-construction-v3` — **does not exist yet**; it may be
  drafted under the provisional default before ratification, but it is contingent on this
  page and must say so in its front matter).
- Any v3 run, result, or claim — **none may happen this session** (opened 2026-06-13;
  ratification is cross-session, PROJECT.md §12.3).
- The inferential half of
  [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md): its
  status (`tested` — SUPPORTED on the gradient half) is *not* reverted by this page, but any
  reading of the conjecture as supported on the unification/evaluation clause is contingent
  here until a ratified v3 instrument produces a result.

## Path to resolution

A later session: (1) optionally drafts the frozen v3 design under the provisional default
(design-writing is not probe-running); (2) runs the independent adversarial-review
ratification of this page — both the indicator package and the anchor status (i)+(ii), which
includes the `internal-contrast-only` ratification CLAUDE.md requires; (3) only then runs the
probe, with thresholds and item lists frozen pre-run and a pre-flight budget estimate
recorded. If the review finds neither A nor B survivable as a validity argument (e.g. the
distributional-shadow mitigations are judged insufficient at this tier), the honest fallback
is to leave the inferential half as an open question with this page's analysis as its record
— a null-shaped outcome the charter prefers over an uninterpretable run.
