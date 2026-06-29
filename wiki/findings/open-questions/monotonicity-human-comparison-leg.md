---
type: open-question
id: monotonicity-human-comparison-leg
title: "Can the add/cancel monotonicity asymmetry get a human-comparison leg — or is it un-instrumentable on the project's available resources?"
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: open
contingent-on: []
created: 2026-06-29
updated: 2026-06-29
links:
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: resource/scalar-implicature-anchor-scouting
  - rel: depends-on
    target: result/monotonicity-within-verbal-battery-v1
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: essay/construct-validity-without-a-criterion
  - rel: depends-on
    target: essay/no-admissible-certifier
---

# Open question: can the monotonicity asymmetry get a human-comparison leg, or is it un-instrumentable here?

> **Scoping verdict (session 144, 2026-06-29): on the project's currently-held resources the
> *asymmetry's* human-comparison leg is un-instrumentable. No model was run; nothing was spent.**
> The conjecture's *per-construction answer-key* arm already has a human comparison
> ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md)), but the
> **load-bearing finding — the matched-difficulty add-easy/cancel-hard *gap*** — does not, because the
> one held human anchor (Scivetti CxNLI) supplies (i) a single adjudicated binary gold per item, **not**
> the graded *robustness* signal the asymmetry is measured in, and (ii) no difficulty-matching across the
> add and cancel arms, so the naive add-vs-cancel contrast on its items is **baseline-difficulty-confounded**
> (already shown). The project's *actual* cancel arms (aspectual progressive, privative, telic-completion,
> single-occurrence) are also **not among Scivetti's 8 constructions**. This is a fact about the
> **available resources** (and the no-human-subjects rule), not a claim that the asymmetry is false or
> that no resource could ever anchor it — see *What would unlock it* and the surfaced-not-dismissed routes.
> The page below states the question precisely, shows what the answer-key probe already settled, gives the
> three reasons the asymmetry leg is blocked, and binds a do-not-re-grind discipline. **It runs nothing,
> ratifies nothing, spends nothing.**

## Why this page exists

Every result establishing the [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md)
— current decoder LLMs treat a construction's inferences as readily *additive* but resist *retraction* —
carries `anchor: internal-contrast-only`: its force is a **within-model** contrast (add arm vs cancel arm
at matched difficulty), with **no human-comparison claim**. The most recent and cleanest leg is the
within-verbal battery ([`result/monotonicity-within-verbal-battery-v1`](../results/monotonicity-within-verbal-battery-v1.md));
the conjecture records the residue it leaves plainly — "what remains open is human comparison and whether
the partial/uneven suppression is defeasance *competence* or strict-NLI *labeling*"
([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md),
the s141 within-verbal-confirm update).

The conjecture names a **candidate** human anchor — the Scivetti CxNLI dataset
([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)), the
project's ratified human inference anchor for four CxG constructions — and a probe against it has already
run. So the live question is not "is there any human anchor at all" but the sharper one: **does the
available human anchor support a human comparison of the *asymmetry itself*, or only of the arms taken
singly?** This page answers that, in the spirit of [`open-question/grounding-magnitude-instrument`](grounding-magnitude-instrument.md)
(a parallel un-instrumentability scoping) and as the negative outcome of revision trigger (a) of
[`essay/construct-validity-without-a-criterion`](../essays/construct-validity-without-a-criterion.md)
("a criterion leg becomes available for some construct" — here it does not, for *this* construct).

## The question, sharply

> **Can the matched-difficulty add-easy/cancel-hard asymmetry be compared against a human baseline using
> a resource the project holds (or could ratify) — i.e. is there a human signal of the *relative*
> robustness of an added constructional entailment versus a cancelled lexical default? Or is the
> asymmetry's human-comparison leg un-instrumentable on current resources, leaving the finding
> permanently `internal-contrast-only` until a graded-robustness human resource on matched
> categorical/defeasible pairs is released?**

## What the answer-key probe already settled

The full Scivetti Exp-1 base task has been run against the human gold and the ≈0.90 native-speaker
baseline ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md), 2026-06-20,
390 items, 8 constructions). That result already computed the naive add-vs-cancel contrast on the human
items — ADD (caused-motion ∪ way-manner) vs CANCEL (conative) base accuracy: claude **0.870 vs 0.962**
(cancel *higher*), gpt +0.035, gemini +0.021, "small and **inconsistent in sign**" — and recorded the
verdict verbatim:

> "The contrast here is baseline-difficulty-confounded and is not the matched-difficulty test the
> conjecture requires — it neither confirms nor falsifies"
> ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md), §Interpretation 3).

So the human-anchored *per-construction accuracy* comparison exists and is honest, but it is **not** a
human anchor for the asymmetry: at base ceiling both directions sit near-ceiling, the conative is in fact
*highest* for claude, and the items are not matched for difficulty across arms. The asymmetry the
conjecture posits is, by its own scope statement, a property of the **de-confounded suppression-with-no-cue
cue arms** (the [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)
paradigm), not of base NLI accuracy.

## Why Scivetti cannot anchor the asymmetry's human leg (three reasons)

1. **Single binary gold, not a robustness gradient.** The asymmetry is measured as a *graded* contrast —
   how reliably an added entailment is affirmed (near-ceiling) versus how reliably a default is *suppressed
   under a conflicting cue* (off-ceiling, instrument-fragile). The human anchor would have to encode a
   comparable human *robustness/cancellability* signal. Scivetti does not: by inspection "the release
   gives a single adjudicated gold label per item, not a per-item multi-rater distribution"
   ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md),
   *What it can ground*), and its *Known limits* put it plainly: "The human bearing is an aggregate
   accuracy/agreement figure, not per-item graded human inference ratings". A binary entailment/neutral/contradiction gold cannot say *how robustly* a human
   holds a default against a cue. The conjecture page already concedes this: the anchor "delivers a single
   adjudicated gold label per item, **not** a per-item human-rating gradient … The conjecture does not
   assume a human gradient the anchor cannot supply."
2. **No difficulty-matching across the arms.** The whole point of the conjecture's confirm criterion is
   "matched difficulty / ceiling control — … never add-at-ceiling vs cancel-off-ceiling." Scivetti's items
   are heterogeneous constructions collected for an NLI benchmark, not add/cancel minimal pairs equated for
   difficulty — which is exactly why the answer-key contrast came out baseline-difficulty-confounded. The
   matched-difficulty property is a feature of the project's **own** controlled cue arms, not a property
   recoverable from Scivetti's gold.
3. **Construction mismatch on the cancel side.** The project's cancel arms that establish the de-confounded
   asymmetry are aspectual/lexical defeasance — the conative (completed contact), the progressive
   (causative-inchoative result), privative modifiers (taxonomic category), telic completion,
   single-occurrence. Of these, **only the conative** is among Scivetti's 8 constructions, and it was
   already answer-keyed (0.82–0.96, near-ceiling base accuracy, *not* the off-ceiling suppression the
   asymmetry needs). The progressive/privative/completion/quantity cancel phenomena the project actually
   measured are **absent** from the Scivetti inventory, so even an answer-key comparison of *those* arms is
   impossible there.

Together these are the negative of trigger (a) in
[`essay/construct-validity-without-a-criterion`](../essays/construct-validity-without-a-criterion.md): a
criterion leg for the asymmetry would need a resource that *pre-encodes* graded human robustness on matched
defeasible/categorical pairs; the only relevant resource held pre-encodes neither the gradient nor the
matching, and the no-human-subjects rule bars eliciting one fresh. The asymmetry therefore lives, lawfully,
in the criterion-less nomological-net regime that essay describes — `internal-contrast-only` is the correct
posture, not a dodge.

## What would unlock it

A human-comparison leg for the asymmetry would require **a human resource that supplies, on matched-difficulty
categorical-vs-defeasible minimal pairs, a graded human signal of how robustly each inference is held under
a conflicting cue** — e.g. per-item multi-rater cancellability/robustness ratings (not a single binary gold)
over add-type and cancel-type constructional pairs equated for baseline difficulty. The project holds no such
resource (Scivetti is single-gold; the off-ceiling cue arms are `internal-contrast-only` by ratified decision,
[`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)),
and cannot build one in-house (it would require forbidden fresh human-subject elicitation). The honest route
is an **externally-released** graded-cancellability dataset over matched constructional pairs — parallel to
the grounding-magnitude page's "the only route is an externally-released graded-image set"
([`open-question/grounding-magnitude-instrument`](grounding-magnitude-instrument.md)).

**The nearest external candidate already scouted, and why even it falls short.** The closest thing to a
graded human *cancellability* signal the project has surveyed is the scalar-implicature line
([`resource/scalar-implicature-anchor-scouting`](../../base/resources/scalar-implicature-anchor-scouting.md),
`status: scouting`): van Tiel-style *scalar diversity* data measures a per-scale **graded human inference
rate** — exactly the kind of "how robustly is a defeasible inference drawn/cancelled" signal a binary gold
lacks. But that scout already concluded "the human-comparison upgrade stays blocked" (no clean, licensed,
on-target open dataset found), and even an ideal scalar-diversity set would supply only a **cancel-side**
human signal (defeasibility rates), with **no matched human add-licensing arm** and **no construction
overlap** with the project's actual cancel arms (progressive / privative / completion) — so it could not
yield the matched *gap* this page is about. It is recorded here as the nearest miss, which *confirms* the
verdict rather than softening it: the missing instrument is genuinely absent across the resources scouted so
far, not merely un-looked-for.

## Surfaced-not-dismissed routes (each blocked, but recorded)

Two partial routes were steelmanned rather than waved away; both fall short, and neither is run or ratified
here:

- **Confine the human claim to the per-construction answer-key arms.** Legitimate, and **already done**
  ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md)): it yields a
  human-anchored per-construction accuracy comparison, but **not** a human comparison of the *gap*
  (baseline-difficulty-confounded). Re-running it would be re-grinding and would not produce an asymmetry
  anchor. So this route exists but does not answer the question.
- **Split Scivetti's gold by label as a defeasance proxy** (treat entailment-gold items as "categorical/add"
  and neutral-gold items — "the hypothesis may or may not be true given the premise" — as "defeasible/cancel",
  then ask whether the model's accuracy/robustness pattern matches the human entailment/neutral split). This
  is a $0 re-analysis of already-collected data, but it is **doubly confounded**: (i) it inherits the same
  baseline-difficulty confound (the entailment-gold and neutral-gold items are not matched for difficulty and
  span heterogeneous constructions), and (ii) "NLI-neutral = the cancelled lexical default the project
  measures" is a **contestable operationalization** — neutral-gold spans many sources of non-entailment, not
  specifically lexical-default cancellation under a construction. Adopting that mapping is a value-laden
  methodological choice that would require its own `wiki/decisions/open/` entry and **cross-session
  ratification** before any read; it cannot be adopted in the session that proposes it. It is recorded here
  as a *possible future route requiring ratification*, not a design endorsed now — and even ratified, the
  difficulty confound would likely keep it weak.

## Do-not-re-grind discipline (binding)

- **Do not re-run the Scivetti answer-key probe** ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md))
  to "get a human asymmetry" — the per-construction contrast on its items is baseline-difficulty-confounded
  by construction, and re-running yields the same confound.
- **Do not declare the asymmetry human-anchored** off the per-construction accuracy match — the answer-key
  arm anchors the *arms taken singly*, never the *gap*.
- **Do not elicit fresh human judgments** to build the missing gradient — barred by [`CLAUDE.md`](../../../CLAUDE.md)
  rule 4 (no human subjects).
- A re-attempt owes either an **externally-released graded-cancellability human resource** over matched pairs,
  or a **cross-session-ratified** operationalization for any gold-split proxy — not a re-read of existing
  Scivetti data dressed as an asymmetry anchor.

## Honest bottom line

- The monotonicity asymmetry's **arms** have a human comparison (per-construction Scivetti accuracy); its
  **gap** — the actual finding — does not, and **cannot on the resources the project holds**, because the
  one held anchor supplies a single binary gold rather than a robustness gradient, offers no
  difficulty-matching across arms, and omits the project's actual cancel constructions.
- This keeps the conjecture `tested` and `internal-contrast-only`; the human-comparison residue the
  within-verbal battery flagged stays **open and un-instrumentable on current resources**, not resolved and
  not falsified.
- **What would resolve it:** an externally-released graded human-cancellability dataset over matched
  categorical/defeasible constructional pairs (the criterion leg trigger (a) of the construct-validity essay
  would then fire for this construct); failing that, the finding remains a clean within-model contrast — the
  correct and only posture for a construct no existing resource pre-encodes.

## Status: open (scoping only)

This page runs nothing, ratifies nothing, and spends nothing. It records the session-144 scoping verdict —
the asymmetry's human-comparison leg is un-instrumentable on the project's available resources — states the
three reasons, names what an unlocking resource would have to supply, and surfaces (without adopting) the two
partial routes. The conjecture's human-comparison residue is now documented here as the live frontier rather
than carried implicitly across result pages.
