---
type: result
id: aann-inferential-v3
title: AANN inferential v3 — the construction does NOT shift unification-vs-distributive inference at the paraphrase or NLI instruments (a first-class null, ceiling-bounded); the one positive signal is gpt-5.4-mini's grammaticalized singular-agreement reflex
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: refines
    target: conjecture/aann-construction
  - rel: refines
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: design/aann-construction-v3-inferential
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: supports
    target: open-question/distributional-vs-inferential-constructional
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
---

# Result: AANN inferential probe v3 — NULL (ceiling-bounded), with one grammatical exception

> **Anchor: `internal-contrast-only`** (within-model AANN-vs-control shift; **no human-comparison
> claim**), the terminal state ratified for this result by the governing decision's adoption
> ([`decisions/resolved/aann-inferential-operationalization`](../../decisions/resolved/aann-inferential-operationalization.md)).
> **Chief-cost statement (verbatim, binding):** *the v3 can never say "models draw the inference
> the way humans do" — only that the construction shifts inferential behaviour relative to a
> matched control, in the direction the published semantics predicts.* The expected-inference key
> (unification = AANN-licensed) is **EXPERT-STIPULATED** (the design author's coding of the
> published AANN semantics — Solt 2007 unit-coercion; Dalrymple & King 2019; Bylinina & Nouwen
> 2018, named not quoted, not in-repo), a scoring key, **not** human judgment data.

The first run of the AANN **inferential** probe, testing the half of
[`conjecture/aann-construction`](../conjectures/aann-construction.md) that v2 left untested. v2
([`result/aann-behavioral-gradient-v2`](aann-behavioral-gradient-v2.md), SUPPORTED) showed the
**productive-gradient** half — models' graded acceptability tracks the human gradient and
generalizes to novel adjectives. v3 asks the **inferential** half: does the construction make a
model **draw the unification / whole-evaluation inference** (*a beautiful three days* = one unified
evaluated stretch, not three separately-evaluated days), measured **only** as the AANN-vs-control
*shift*?

Frozen design: [`design/aann-construction-v3-inferential`](../../../experiments/designs/aann-construction-v3-inferential.md)
(repaired this session — the object/mass measure-noun class was dropped after the prior session's
pre-run critic found its unification paraphrases anomalous; scope is now **temporal + distance
measure nouns only**). PREREG, raw data, repair record, and run log:
[`experiments/runs/2026-06-13-aann-inferential-v3/`](../../../experiments/runs/2026-06-13-aann-inferential-v3/README.md).
624 calls, **$0.0910 billed**, **zero missing responses in every arm** (0 missing-cost calls). A
**fresh independent pre-run critic returned GO** on the repaired materials (all five prior defects
fixed, all eight binding conditions PASS, anti-cheat PASS); an **independent post-run verifier
recomputed every shift, CI, raw rate, and Tier-0 count from the raw data with its own code — 0
mismatches**, NULL verdict reproduced to the digit.

## Headline (pre-registered verdict: NULL)

**No model produced an AANN-vs-control shift on the primary paraphrase arm that clears the frozen
bar (τ = +0.20 with bootstrap-CI-lower > 0).** Under the frozen verdict map (NULL when fewer than
two Tier-0-passing models reach even paraphrase positivity), the result is a **first-class NULL**.

| Per model (Tier-0 passers, all three) | A claude-sonnet-4.6 | B gpt-5.4-mini | C gemini-3.5-flash |
|---|---|---|---|
| Tier-0 manipulation check (≥ 20/24) | 24/24 | 22/24 | 24/24 |
| **Arm A paraphrase shift** (PRIMARY; τ = +0.20, CI-lo > 0) | +0.174 · CI [0.04, 0.35] · **not pos** (< τ) | +0.043 · **not pos** | 0.000 · **not pos** |
|  — raw unification rate, AANN / control | 0.96 / 0.78 | 1.00 / 0.96 | 1.00 / 1.00 |
|  — under-pressure subset shift (n=10) | +0.20 | 0.00 | 0.00 |
| Arm B NLI shift (convergent) | 0.000 · not pos | +0.043 · not pos | 0.000 · not pos |
|  — raw affirm rate, AANN / control | 0.87 / 0.87 | 0.87 / 0.83 | 1.00 / 1.00 |
| **Agreement shift** (load-bearing discriminator) | 0.000 · not pos | **+0.739 · CI [0.57, 0.91] · POSITIVE** | 0.000 · not pos |
|  — raw "was" rate, AANN / control | 1.00 / 1.00 | 0.96 / 0.22 | 1.00 / 1.00 |
| \|FC − NLI\| (named statistic; flag ≥ 0.30) | 0.174 (no flag) | 0.000 (no flag) | 0.000 (no flag) |
| Category (PREREG headline-gating) | **NULL** | **NULL** | **NULL** |

**Verdict: NULL — no AANN-vs-control inferential shift at this instrument.**

## What the null is, and what bounds it

**1. The dominant mechanism is a ceiling/default confound on the meaning arms, not clean evidence
of absence.** The unification paraphrase and the unification/whole-evaluation NLI hypotheses are
chosen/affirmed at near-ceiling rates for **both** the AANN premise **and its plural control**
(paraphrase raw rates: control already 0.78 / 0.96 / 1.00; NLI control 0.87 / 0.83 / 1.00). The
models read *three beautiful days* as describing a unified, whole-evaluated stretch **just as
readily** as *a beautiful three days*. The construction therefore has **no headroom to shift** the
reading — the unification interpretation is the **default** for the bare plural measure phrase, not
something the AANN form has to license. So the null says: at this instrument, **the construction's
unification inference is not separable from the plural phrase's default unification reading.** It
is *not* a clean finding that the models lack the inference.

This is exactly the hardness that [`open-question/distributional-vs-inferential-constructional`](../open-questions/distributional-vs-inferential-constructional.md)
predicted: "the senses predict the *same* answer in the easy cases … the distinguishing cases are
the rare ones." The design's pre-registered defence was the **under-pressure subset** (Condition 4
— items where the *distributive* paraphrase is the locally-fluent continuation, putting the
unification choice against the distributional grain, the open question's "core move"). It did not
rescue the arm: the under-pressure shift is +0.20 for claude (at, not above, threshold on a subset,
and the full-set headline is what gates) and **0.00** for both gpt and gemini. The inference and the
default coincide even under local distributional pressure.

**2. The one substantive positive signal is gpt-5.4-mini's grammaticalized singular-agreement
reflex (+0.739).** The load-bearing discriminator — the construction's singular agreement on a
plural head (*A beautiful three days **was** what we needed*) — is the one place the
distributional-shadow story predicts the **opposite** of the inferential story (singular agreement
on a plural noun is distributionally dispreferred in general text). gpt-5.4-mini shows it strongly
and AANN-specifically: it picks singular *was* for the AANN frame (0.96) but plural *were* for the
matched control (0.22 *was*), a +0.74 shift with a CI well clear of zero. **The construction does
move this model — but on its grammatical reflex, not on the paraphrase/entailment inference.**

The pre-registered **headline-gating rule (Condition 3)** is decisive here, and it earned its
keep: because gpt's *primary* (paraphrase) arm is null, the agreement reflex **does not** license
the headline "draws the unification inference." gpt-5.4-mini is recorded as **NULL on the
inferential question**, with the agreement reflex carried as a noted exception — a grammatical
constructional reflex present **without** a corresponding inferential-paraphrase shift. This is the
honest reading the design was built to force: a singular-agreement preference is consistent with
either a grammaticalized form-reflex *or* the unification semantics, and on its own it cannot
distinguish them.

**3. claude and gemini show 0.00 agreement shift — but at ceiling, not by differentiating.**
Both pick singular *was* at rate 1.00 for **both** the AANN frame and the plural control
(*Three beautiful days ___ what we needed* → *was*, too). So their flat agreement shift is another
ceiling effect (a duration/amount subject pulls singular agreement regardless of the article cue),
not a demonstration that they fail the reflex. Only gpt-5.4-mini's control rate (0.22) leaves room
for the contrast to show — and there it does.

## Instrument-disagreement (Condition 7, fed to the open question)

The named **|FC shift − NLI shift|** statistic is small for every model (0.17 / 0.00 / 0.00; none
reaches the 0.30 flag), so this run adds a **low-disagreement** data point to
[`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md):
paraphrase-FC and entailment-NLI **agree** here (both near-ceiling, both null on the shift) — unlike
the conative, where they diverged sharply for gpt-5.4-mini. That agreement is itself partly a
ceiling artefact (two instruments cannot disagree much when both are pinned near 100% in both
conditions), so it bounds, rather than resolves, the instrument-sensitivity question.

## Disputed-coding sensitivity (Condition 6)

One item carried a `key_disputed` flag (the yards inventory-edge item). Recomputing the paraphrase
arm excluding it changes no model's positivity (still null for all three; `category_changes:
false`). The null is not an artefact of the single disputed coding.

## Relation to the conjecture and the theory

- The **productive-gradient** half of [`conjecture/aann-construction`](../conjectures/aann-construction.md)
  stays SUPPORTED (v2); this result bears **only** on the **inferential** half, and it is a
  **ceiling-bounded null**: at the paraphrase and NLI instruments the construction does not shift
  the unification inference relative to a matched control — but largely because the control already
  carries that reading. The conjecture's inferential clause is therefore **not supported**, and
  also **not cleanly disconfirmed**; it is **untestable at this instrument** as designed, for the
  reason the open question named. Any future probe must engineer a control whose default reading is
  **distributive**, so the construction has somewhere to move the inference *to*.
- The agreement reflex is a genuine `constructional` + `functional-vs-formal` signal in
  gpt-5.4-mini: the construction's grammaticalized singular agreement is tracked AANN-specifically.
  Within the evidence ladder of [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md),
  this sits at the **form/agreement** rung, not the inference rung — consistent with the recurring
  pattern that AANN competence is strong on *form* (v2 gradient; Tier-0 ceilings) and unproven on
  *inferential use*.

## Bounds (binding on any reading of this result)

- **No human-comparison claim** (anchor `internal-contrast-only`). The chief-cost statement above
  is binding: this can never say models infer "the way humans do."
- **The null is ceiling-bounded, not a competence verdict.** It does not show the models lack the
  unification inference; it shows the paraphrase/NLI instrument cannot separate the construction's
  inference from the plural phrase's default unification reading. Read it as a **measurement** null
  with a precise, named cause, not as "the construction carries no inferential force."
- The expert-stipulated key is theorists' analyses, not human judgment data (Condition 5/6).
- A single positive arm (gpt's agreement) under the load-bearing-discriminator rule does **not**
  license an inferential-shift claim (Condition 3).

## Provenance

Stimuli are hand-authored, reusing the AANN measure-noun classes from
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) as
**class provenance only** — Mahowald's MTurk data are 1–10 *acceptability* ratings and are
**not** (and cannot be) the inference anchor (the governing decision blocks that category error).
Independent post-run verification reproduced every reported number from the raw data; 0 missing
responses; cost $0.0910 billed (`usage.cost`-summed, 0 missing-cost calls).
