---
type: design
id: aann-construction-v3-inferential
title: AANN construction probe v3 — inferential (unification + whole-evaluation), AANN-vs-control shift, paraphrase-FC primary + NLI convergent + grammaticalized agreement discriminator
meaning-senses:
  - constructional
  - inferential
status: repaired 2026-06-13 (object class dropped); re-frozen for a fresh pre-run critic
contingent-on:
  - aann-inferential-operationalization
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: operationalizes
    target: conjecture/aann-construction
  - rel: depends-on
    target: decisions/resolved/aann-inferential-operationalization
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: supports
    target: open-question/distributional-vs-inferential-constructional
---

# Experiment design v3 — AANN construction (inferential: unification + whole-evaluation)

> **Repair note (2026-06-13, a later session than the NO-GO).** The prior session's independent
> pre-run critic returned **NO-GO** over a real object-class stimulus defect (the "formed one
> continuous stretch" unification paraphrase is anomalous for mass/area nouns; the dollar items
> dropped their plural measure noun and were not well-formed AANN), plus a parser bug. Per the
> pre-authorized repair list, this session (a *later* one — no anti-retuning boundary crossed; no
> data existed) **dropped the object class entirely** rather than re-author it: the unification
> ("continuous stretch") reading is natural for genuine extents (time, distance) and anomalous for
> mass/area/money, so restricting to **temporal (13) + distance (10) = 23 items** sharpens rather
> than degrades the construct test. The parser now strips markdown-bold/quotes (B3); `noun_sg`
> fixed (S1, "yards"→"yard"); the lexical-overlap parity metric's scope documented (S2). The result
> is **scoped to temporal + distance measure nouns only**, stated on the result page. The repaired
> materials were then reviewed by a **fresh** independent pre-run critic before the run; full repair
> record: run README, [`experiments/runs/2026-06-13-aann-inferential-v3/README.md`](../runs/2026-06-13-aann-inferential-v3/README.md).

**Governing decision:** [`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md)
— **RESOLVED 2026-06-13** (autonomous cross-session adversarial review): ADOPT DEFAULT WITH
CONDITIONS — the A+B two-instrument package (paraphrase forced-choice primary, entailment NLI
convergent arm, grammaticalized singular/plural agreement sub-probe the load-bearing
discriminator; Option C demoted), under **eight binding pre-run conditions**, with the v3 result
fixed at `anchor: internal-contrast-only` scored against an explicitly **expert-stipulated**
literature key. This design is the operationalization of the **inferential half** of
[`conjecture/aann-construction`](../../wiki/findings/conjectures/aann-construction.md), which v2
left untested (v2's [`result/aann-behavioral-gradient-v2`](../../wiki/findings/results/aann-behavioral-gradient-v2.md)
supported only the **productive-gradient** half). It is written to satisfy all eight conditions;
each is cited where it bites, and the §0 checklist maps every condition to its location.

**This design may be drafted under the resolved decision (design-writing is not probe-running),
but the v3 probe may not run until an independent pre-run critic reviews this design + the frozen
PREREG + stimuli** (`experiments/runs/2026-06-13-aann-inferential-v3/`). The decision's ratification
fixes the *yardstick* (instrument class, indicator hierarchy, anchor status), not any *result*.

**Freeze discipline.** Everything in this page and the run materials — items, paraphrase
wordings, NLI hypotheses, was/were pairs, A/B letter assignments, lexical-overlap counts, the
expected-inference key, thresholds, per-model settings — is frozen **before any finding-bearing
model call**. No threshold may be set or retuned from any pilot/dry-run output (Condition 8). The
analysis code (`analyze.py`) exists at freeze with the decision rule baked in, and `probe.py`
refuses to run without a frozen `PREREG.md` and `analyze.py` present (the v2b house guard).

## 0. The eight conditions → where this design satisfies each (Condition map)

| # | Binding condition (decision §Ratification) | Where satisfied here |
|---|---|---|
| 1 | Primary instrument fixed before any call: **A (paraphrase FC) primary**, B (NLI) convergent; never reselected post-hoc | Front-matter `status`/this page §2 (PRIMARY-INSTRUMENT LOCK); `PREREG-draft.md` "Primary instrument"; `analyze.py` headline reads Arm A only |
| 2 | Indicator = AANN-vs-control **shift**, never raw AANN rate; control pairing + lexical-overlap parity | §2 (all arms compute a differential); `stimuli.json` per-item `lexical_overlap` counts (parity asserted in `prep.py`); raw rates descriptive only in `analyze.py` |
| 3 | Grammaticalized agreement sub-probe is the **load-bearing discriminator**, reported separately, weighted above paraphrase | §3 (Agreement sub-probe + headline-gating rule); `analyze.py` `headline()` downgrades wording if agreement null |
| 4 | At least some items place the **distributive paraphrase as locally-fluent continuation**; under-pressure subset analysed separately | §2 (under-pressure subset); `stimuli.json` per-item `local_fluency` field; `analyze.py` reports the subset shift separately |
| 5 | `anchor: internal-contrast-only`; no human-comparison claim; Mahowald = provenance only; literature key **expert-stipulated**; chief-cost statement verbatim | §4 (Anchor) carries the verbatim chief-cost sentence; key labelled expert-stipulated here and in `stimuli.json` |
| 6 | Disputed literature codings flagged item-level, excluded from / sensitivity-tested against headline | §5; `stimuli.json` per-item `key_disputed` flag; `analyze.py` recomputes the headline excluding flagged items |
| 7 | **\|FC shift − NLI shift\|** per model a reported named statistic; pre-declared convergence/disagreement rule; Tier-0 manipulation check with pre-declared failure consequence | §6 (convergence rule + the named statistic); §3.1 Tier-0; `analyze.py` `convergence` + `tier0` |
| 8 | Thresholds/items/wordings/settings frozen pre-run; pre-flight budget recorded; named null fallback | This page (frozen throughout) + `PREREG-draft.md` §thresholds/budget; §7 names the charter-preferred null fallback |

## 1. Construct

The AANN noun phrase (*a beautiful three days*) presents the measured quantity as **a single
unified, evaluated stretch** — one three-day span evaluated as beautiful *as a whole* — **not** a
distributive plural (*three separate days, each individually beautiful*). This is the
characteristic-semantics clause of [`conjecture/aann-construction`](../../wiki/findings/conjectures/aann-construction.md),
in the `constructional` + `inferential` senses
([`wiki/meaning-senses.md`](../../wiki/meaning-senses.md)). The question this design operationalizes:
does the construction make a model **draw the unification / whole-evaluation inference** —
measured **only** as the AANN-vs-control *shift* (Condition 2), never the raw AANN rate, never as
a human-comparison claim (Condition 5).

This is distinct from v2's territory (graded acceptability of the form): a model can rate *a
beautiful three days* acceptable, and even track the human acceptability gradient (v2 SUPPORTED),
without using the unification/evaluation semantics. v3 tests the latter.

## 2. Indicator — the two-instrument package, on the same frozen items

**PRIMARY-INSTRUMENT LOCK (Condition 1).** **Arm A (paraphrase forced-choice) is the primary
instrument.** Arm B (entailment NLI) is the convergent robustness arm. This is fixed here, in the
front matter, and in `PREREG-draft.md`, before any model call; it is never reselected after seeing
outputs. There is no "winning instrument" chosen post-hoc; the headline reads Arm A, with Arm B as
convergence evidence and the disagreement statistic (§6) reported, never averaged away.

Every arm is built on the **same frozen base items**: **23** AANN base sentences (the count and
geometry are fixed in `stimuli.json`; see §8), spanning **two** of Mahowald's measure-noun classes
— **temporal (13) and distance (10)** — each with a lexically-matched non-AANN **control**. (The
object/mass measure-noun class was dropped in the 2026-06-13 repair: see the banner above and the
run README. Restricting to genuine *extents* — time and distance — is also what makes the
"continuous stretch" unification paraphrase well-formed, so the indicator is not confounded by an
anomalous paraphrase.)

### Arm A — paraphrase forced-choice (PRIMARY)

- **Premise:** AANN sentence (*We spent a beautiful three days in Rome*) vs. its
  lexically-matched non-AANN **control** (*We spent three beautiful days in Rome*).
- **Forced choice** between a **unification** paraphrase ("the three days formed one continuous
  stretch, beautiful as a whole") and a **distributive** paraphrase ("each of the three days was
  individually beautiful").
- **Counterbalance:** the A/B letter assignment of the two paraphrases is counterbalanced across
  items (each item carries a frozen `fc_letter_unification` ∈ {A,B}; half and half, seeded) to
  block the position bias. `analyze.py` reads the *content* choice (unification vs distributive),
  not the letter.
- **Lexical-overlap parity (Condition 2):** neither paraphrase may share more surface content
  words (lemma-level, stopwords removed) with the premise than the other. The per-item overlap
  count for each paraphrase is recorded in `stimuli.json` (`lexical_overlap.unification`,
  `lexical_overlap.distributive`) and parity (equal counts, or within the frozen tolerance of 1
  with the direction flagged) is asserted mechanically in `prep.py`.
- **Indicator:** **P(unification | AANN) − P(unification | control)** = the **shift**. The raw
  AANN unification rate is descriptive only.

**Under-pressure subset (Condition 4).** A pre-declared subset of items (`local_fluency:
"distributive"` in `stimuli.json`) is authored so that the **distributive** paraphrase is the
*locally-fluent* continuation (the surface/world-knowledge gradient favours "each day"), making
the unification choice the inference-against-the-distributional-grain — the "core move" of
[`open-question/distributional-vs-inferential-constructional`](../../wiki/findings/open-questions/distributional-vs-inferential-constructional.md).
Each item's local-fluency direction (`unification` | `distributive` | `neutral`) is declared
frozen; the under-pressure subset's shift is analysed **separately** from the full-set shift.

### Arm B — entailment NLI (convergent robustness)

- **Same premises** (AANN vs control).
- **Hypotheses**, in the house NLI affirm/withhold framing, probing the licensed inferences:
  1. **singularity / unification** — "the stay was a single continuous stretch" (affirm for AANN);
  2. **whole-evaluation** — "the stretch as a whole was beautiful" (affirm) vs the distributive
     foil "each day individually was beautiful" (the construction does not entail the
     distributive reading; the foil is the contrast, not a target affirm).
- **Indicator:** the affirm-rate **shift** AANN vs control on the unification/whole-evaluation
  hypotheses (Condition 2). NLI's known Gricean permissiveness (NLI admits post-hoc readings FC's
  strict framing withholds — [`result/caused-motion-near-miss-v2c`](../../wiki/findings/results/caused-motion-near-miss-v2c.md))
  is exactly why B is convergent, not headline; the shift design subtracts the baseline.

## 3. Agreement sub-probe — the load-bearing discriminator (Condition 3)

The grammaticalized singular/plural reflex of the construction: the AANN phrase takes **singular**
agreement despite a plural noun head.

- **Items:** *A beautiful three days ___ what we needed* (AANN → singular **was**) vs *Three
  beautiful days ___ what we needed* (control → plural **were**). Forced choice was/were,
  **counterbalanced** (frozen `agr_letter_was` ∈ {A,B}).
- **Indicator:** **P(singular "was" | AANN) − P(singular "was" | control)** = the
  singular-agreement **shift**.
- **Why load-bearing:** singular agreement on a plural head is **distributionally dispreferred** in
  general text, so a positive AANN-specific singular-agreement shift is the one place the
  distributional-shadow story predicts the *opposite* of the inferential story (the decision's
  ratification reasoning). It is reported **separately** and weighted **above** the paraphrase arm.

**Headline-gating rule (Condition 3, frozen):** if Arm A (paraphrase) shift is positive (passes
its threshold) **but the agreement shift is null** (does not pass), the headline is **"shift in
paraphrase selection WITHOUT the grammaticalized reflex"** — **not** "draws the unification
inference." Only when the agreement shift is *also* positive may the headline read "the
construction shifts inferential behaviour, including the grammaticalized singular reflex, in the
direction the published semantics predicts." This rule is baked into `analyze.py` `headline()`.

### 3.1 Tier-0 manipulation check (Condition 7)

A pre-declared can't-fail sanity arm: the AANN **well-formed vs ill-formed** forced choice reused
from v2/v2b (the 4 Mahowald degenerate variants `reverse_mods`, `no_mod`, `no_plural`, `no_a`),
AANN position counterbalanced. **Pass: ≥ 20/24 AANN-preferred per model** (the v2/v2b bar).
**Pre-declared failure consequence:** a model failing Tier-0 has its inference numbers reported as
**instrument failure** — its shift/headline is reported descriptively and **excluded** from the
cross-model count; it is never reinterpreted as a substantive inference result. If fewer than 2
models pass Tier-0, the v3 verdict is **INSTRUMENT FAILURE** (no substantive inference verdict).

## 4. Anchor (Condition 5)

The v3 result will carry **`anchor: internal-contrast-only`**: its force is the **within-model
AANN-vs-control shift** (does the construction shift paraphrase choice / entailment behaviour /
agreement relative to the minimally different non-AANN control). **No human-comparison claim is
made.** This terminal state is **ratified for the v3 result** by the governing decision's adoption
(the `internal-contrast-only` ratification CLAUDE.md requires; precedent
[`decisions/resolved/conflicting-cue-human-anchor`](../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)).

[`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md)
is linked **only as stimulus provenance** (the AANN noun-class inventory and templates this
design's items reuse) and as the v2 gradient anchor — **never** as the inference anchor.
Mahowald's MTurk data are 1–10 *acceptability* ratings; no human there was asked the
unification-vs-distributive question, so reusing it as an inference anchor would be a category
error (the decision blocks this explicitly).

The expected-inference **key** (the unification reading = the AANN-licensed answer) is
**EXPERT-STIPULATED**: it is the design author's coding of the published AANN semantics — the
unification/whole-evaluation analysis the conjecture page describes and the constraint literature
names (Solt 2007 on unit-coercion; Dalrymple & King 2019; Bylinina & Nouwen 2018). **These papers
are not in-repo; they are named only as the analyses the stipulation rests on, exactly as the
decision page names them — no quotes are fabricated from them.** The key is a *scoring key*, not a
behavioral-human anchor, and is labelled expert-stipulated on this design, in `stimuli.json`, and
on the eventual result page.

**Chief-cost statement (verbatim, Condition 5, binding on the result page):** *the v3 can never
say "models draw the inference the way humans do" — only that the construction shifts inferential
behaviour relative to a matched control, in the direction the published semantics predicts.*

## 5. Disputed-coding flagging (Condition 6)

Any item whose unification/distributive key the AANN-semantics literature does **not** clearly
settle is flagged item-level (`key_disputed: true` in `stimuli.json`, with a one-line reason). The
headline shift is computed **both** on all items **and** on the non-disputed subset; if the verdict
category differs, a mandatory caveat attaches. The key is not presented as settled where the
literature genuinely disputes it. (Items where world-knowledge *alone* forces the unification
reading are excluded at authoring time, so the shift cannot be a world-knowledge artifact.)

## 6. Reported statistics, convergence rule, and the named disagreement statistic (Condition 7)

Per model, the design computes:

- **Arm A shift** (primary): P(unification|AANN) − P(unification|control), full set and the
  under-pressure subset separately.
- **Arm B shift** (convergent): affirm-rate shift on the unification/whole-evaluation hypotheses.
- **Agreement shift** (load-bearing discriminator): P(was|AANN) − P(was|control).
- **|FC shift − NLI shift|** per model — a **reported named statistic**, fed to
  [`open-question/instrument-sensitivity-constructional-inference`](../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md),
  **never averaged away** (the disagreement *is* the signal for that question).

**Frozen shift threshold τ = +0.20** (a 20-percentage-point AANN-vs-control shift), inclusive
(≥ +0.20 passes), with a 10,000-resample bootstrap 95% CI over items whose lower bound must
exceed 0 for a "positive" shift. τ is set from the v2-band design discipline (a shift smaller than
20 pp on a binary forced choice is not distinguishable from counterbalancing/labelling noise at
this item count) and is fixed before any model output exists (Condition 8).

**Pre-declared convergence-vs-disagreement rule (Condition 7, frozen):**

- **CONVERGENT-POSITIVE** for a model: Arm A shift ≥ τ (CI lower > 0) **AND** Arm B shift ≥ τ
  (CI lower > 0) **AND** agreement shift ≥ τ (CI lower > 0). Headline: "the construction shifts
  inferential behaviour, including the grammaticalized singular reflex, in the predicted direction."
- **PARAPHRASE-ONLY** for a model: Arm A shift ≥ τ but the **agreement** shift is null. Headline
  (Condition 3): "shift in paraphrase selection WITHOUT the grammaticalized reflex" — **not**
  "draws the unification inference."
- **INSTRUMENT-DISAGREEMENT** for a model: |FC shift − NLI shift| ≥ 0.30 (the ≤50 pp in-repo
  bound's mid-band; a per-model instrument-fragility caveat is mandatory, fed to the
  instrument-sensitivity open question), regardless of headline category.
- **NULL** for a model: Arm A shift < τ or its CI straddles 0.

**v3 verdict (over Tier-0-passing models only):**

- **SUPPORTED (inferential half):** ≥ 2 of 3 Tier-0-passing models are CONVERGENT-POSITIVE.
- **PARTIAL (paraphrase-without-reflex):** ≥ 2 models reach PARAPHRASE-ONLY but < 2 are
  CONVERGENT-POSITIVE — a `constructional`-shift-without-the-grammaticalized-reflex finding.
- **NULL:** < 2 models reach even PARAPHRASE-ONLY — the construction does not shift inferential
  behaviour relative to the control at this instrument; written as a first-class null (§7).
- **INSTRUMENT FAILURE:** fewer than 2 models pass Tier-0.

Every outcome, including the null, is a first-class result. No threshold is retuned post-hoc.

## 7. Validity argument and its bounds

**For the instrument:** (i) the **AANN-vs-control shift** subtracts the article-cue distributional
baseline, so the indicator is a differential, not a raw rate exposed to the distributional shadow;
(ii) the **grammaticalized agreement sub-probe** is the one place the distributional story predicts
the opposite of the inferential story, foregrounded as the discriminator; (iii) the **convergence**
design across two house instruments, primary fixed in advance, with the disagreement reported as a
statistic, matches the only headline this repo's instrument-sensitivity record would let stand.

**Bounds (binding on any result's prose):**

- The shift shows the construction *changes which reading the model commits to relative to a
  matched control*; it does **not** show the unification semantics is *represented*, and it makes
  **no** human-comparison claim (Condition 5).
- A paraphrase-only positive (no agreement reflex) is **not** "draws the unification inference"
  (Condition 3).
- Forced choice and NLI carry **known, opposite, systematic** biases at this tier (gpt-5.4-mini's
  FC excluded-middle crack; NLI's Gricean permissiveness); the disagreement statistic and the
  mandatory fragility caveat are the defences, not an averaged headline.
- The expert-stipulated key is theorists' analyses, **not** human judgment data (Condition 5/6).

**Named null fallback (Condition 8):** if, at design or pre-run-critic time, neither arm can be
given a defensible internal-contrast validity argument at this tier, the ratified fallback is the
charter-preferred null — leave the inferential half an **open question** with the governing
decision page and this design as its record, rather than run an uninterpretable probe.

## 8. Pre-flight cost (config/budget.md)

Geometry (frozen in `stimuli.json`): **23 base items** (temporal 13 / distance 10). Per model the
calls are: Arm A paraphrase FC ({AANN, control}) **46**, Arm B NLI (2 hypotheses × {AANN, control})
**23 × 2 × 2 = 92**, agreement FC ({AANN, control}) **46**, Tier-0 **24** = **208 calls/model × 3 =
624 calls**. ~80 tokens in / ~8 out each (FC/NLI are single-token picks; same shape as v2/v2b).

Pre-flight from v2b's **measured billed** per-call rates (single-token FC/NLI arms, the same
prompt shape): A ≈ $0.00033, B ≈ $0.00008, C ≈ $0.00012 per call → at 208 calls/model ≈ $0.069 (A)
+ $0.017 (B) + $0.025 (C) ≈ **$0.11 point estimate** across all three models for 624 calls. The
known **~4.5× rate-card undercount** is already absorbed (these are *billed* v2b rates, not
rate-card); allowing for the one verbatim retry per unparseable response and variance,
**expected ≈ $0.11–0.20 billed**. This lands **well under $1** — but note it must be **flagged if
it could exceed $1**, and it cannot here at this geometry. A single-run **ABORT_USD = $0.50** flag
is coded in `probe.py` (well under the $2.50 single-run flag and the $5.00/day budget). Today's
prior spend is tracked in `config/budget.md`; the actual billed `usage.cost` is recorded in the
run record after the (later, post-critic) run.

## 9. Run protocol

1. `prep.py` (no model calls) authors and freezes `stimuli.json` (items, paraphrases, NLI
   hypotheses, was/were pairs, counterbalancing, lexical-overlap parity asserted, key, dispute
   flags, Tier-0 pairs).
2. Independent **pre-run critic** reviews this design + `PREREG-draft.md` + `stimuli.json` before
   any call. The orchestrator freezes `PREREG.md` only after a GO.
3. `probe.py`: all calls via [`experiments/lib/openrouter.py`](../lib/openrouter.py)
   (`usage: include`); refuses to run without `PREREG.md` and `analyze.py`; per-slot max_tokens +
   gemini `reasoning:{effort:"minimal"}`; one verbatim retry per unparseable response, then
   missing; billed-cost logging; ABORT_USD flag.
4. `analyze.py` computes exactly the §6 statistics with the frozen thresholds and the
   headline-gating + convergence rule baked in; an independent post-run verifier checks numbers
   against raw before the result page is written.
5. Result page (later session, post-run) `wiki/findings/results/aann-inferential-v3.md`,
   `anchor: internal-contrast-only`, carrying the §4 chief-cost statement verbatim.

## 10. What this design does not do

No human-comparison claim anywhere (Condition 5). No raw-AANN-rate headline (Condition 2). No
post-hoc instrument selection (Condition 1) or threshold retuning (Condition 8). No Option-C
generation-and-code arm (demoted by the decision; its coding step imports an un-ratified
LLM-judge / no-inter-rater fragility). No reuse of Mahowald's acceptability ratings as an
inference anchor. It does not, and cannot, claim the model draws the inference *the way humans do*.
