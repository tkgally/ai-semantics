---
type: result
id: function-word-modal-second-instrument
title: "A second inferential instrument registers the modal swaps 3-way NLI left null: will→would shifts a forced-choice modal-force preference in all three models, and the shall→should NLI panel-split dissolves into concordance — the modal nulls relocate from the relation to the NLI instrument's calibration"
meaning-senses:
  - constructional
  - inferential
  - distributional
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: refines
    target: essay/function-words-not-one-category
  - rel: refines
    target: result/function-word-modal-widening
  - rel: depends-on
    target: result/function-word-modal-widening
  - rel: depends-on
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# The will→would null was the instrument, not the relation — a second indicator registers it

> **A within-model, cross-instrument contrast (`anchor: internal-contrast-only`).** It tests **essay
> revision trigger (c)** of
> [`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md) — *"the single
> most decisive trigger"*: is the `will`→`would` 3-way-NLI null
> ([`result/function-word-modal-widening`](function-word-modal-widening.md)) the **instrument's**
> insensitivity or the **relation's** genuine inferential inertness? It holds the modal swap **fixed**
> (the frozen will/shall/must items, reused **verbatim**) and changes only the **indicator**, from
> 3-way NLI entailment-flip to a single-token **forced-choice modal-force preference**. It makes **no
> human comparison** and needs no human anchor. Run:
> `experiments/runs/2026-06-21-modal-second-instrument/`. Stimuli frozen + hashed (file sha
> `a1eb83a8…`, canonical `a12b2da0…`); `certify.py` `"ok": true` (per-arm n≥15; hedge-position
> balanced; **0 modal-lemma leaks** in options; 58/58 base–fn single-modal-token diff; 58/58 base–ct
> same-modal) **before any model output**, under an independent fresh-agent pre-run critic (**GO**, no
> blockers). Analysis **reproduced from raw by an independent fresh-agent post-run verifier —
> verdict REPRODUCED**: every per-arm × model cell (base_strong_pref, shift_fn, shift_ct, hedge
> counts) matched to the digit by its own script (no `analyze.py` import); file sha
> `a1eb83a8…`/canonical `a12b2da0…` recomputed and matched; all 58 items + 174 premise fields
> byte-identical to the source run; 522/522 rows re-parsed (0 unparsed); billed re-summed to
> $0.12322 (0 missing). The verifier required three caveats be carried verbatim (the `will`-arm
> fairness asymmetry, claude-`will` as the weakest cell, `shall`'s single `buy`→`give` content pair)
> — all three are stated below. **Billed: $0.1232** (claude $0.0730 / gpt $0.0192 / gemini $0.0303 +
> liveness $0.0007; 3 models × 174 calls = 522 finding-bearing, **0 unparsed, 0 missing `usage.cost`**).

## The question (essay trigger c)

The session-71 NLI run left `will`→`would` near-null (claude 0/20, gpt 0/20, gemini 3/20) and split the
panel on `shall`→`should` (gemini 0.778 vs claude/gpt 0.056). The companion essay's §"A calibrated
reading" offered an interpretation it explicitly could not yet separate from the alternative: *"a sizeable
part of what looks like 'function words carry more inferential load' is really 'the swaps that flip our
**one** inferential instrument are the ones that change a relation that instrument is calibrated to.'"*
Trigger (c) names the decider: *"If an indicator beyond 3-way NLI … **does** register the modal or scalar
swaps that NLI leaves near-null, that would relocate the effect from 'type of grammatical relation' to
'instrument sensitivity.'"* This probe is that indicator.

## Design (frozen, certified)

The will/shall/must **matched** items from [`result/function-word-modal-widening`](function-word-modal-widening.md)
are reused **verbatim** (same sentences, same content controls) — so the frequency/length matching is
**inherited** (already certified there) and not re-derived. Only the indicator changes:

- **NLI (the old instrument):** premise → hypothesis, output a digit 0/1/2 (entailment/neutral/contradiction);
  flip = the label changes when the modal is swapped.
- **Forced choice (the new instrument):** read the sentence; pick which of two paraphrases of its
  **modal force** fits better — a **STRONG** option (the base modal's force) vs a **HEDGE** option (the
  swapped modal's force); output a single letter A/B.

| arm | STRONG paraphrase | HEDGE paraphrase |
|-----|------|------|
| `will`→`would` | "definitely happens or is the case" | "conditional or hypothetical — happening only if certain circumstances hold" |
| `shall`→`should` | "strictly required or mandatory" | "advisable or recommended, but not strictly required" |
| `must`→`might` | "required or certain to occur" | "merely possible or optional — not required and not certain" |

**Same single-token output channel as NLI** (one letter, no working surface) — so a divergence from the
NLI result is the **question type** (graded modal-force preference vs 3-way entailment), not channel
width (this controls the output-channel confound the project mapped). Option strings carry **no modal
lemma** (no will/would/shall/should/must/might), and HEDGE position (A/B) is **counterbalanced ~50/50**
within each arm and **fixed within an item** across conditions, so a modal-blind or position-biased reader
contributes ~0 to the within-item shift. Per item × model, 3 calls — `base`, `fn` (modal swapped), `ct`
(content swapped, **modal unchanged**, the falsify control). `picked_hedge ∈ {0,1}` from the chosen letter
vs the item's hedge-letter; **shift_fn = picked_hedge(fn) − picked_hedge(base) ∈ {−1,0,1}** is the primary
readout.

## Headline: the second instrument registers every modal swap NLI left null or split

Per-arm comparison — NLI flip rate (old) vs forced-choice shift (new), claude / gpt / gemini:

| arm | NLI `flip_fn` | FC `shift_fn` | FC fn-hedge / n | base-strong (manip check) |
|-----|------|------|------|------|
| `will`→`would` (future→conditional) | 0.000 / 0.000 / 0.150 | **+0.300 / +0.550 / +0.850** | 6/20 · 13/20 · 17/20 | 1.00 / 0.90 / 1.00 |
| `shall`→`should` (obligation→advisory) | 0.056 / 0.056 / **0.778** | **+0.889 / +1.000 / +1.000** | 17/18 · 18/18 · 18/18 | 0.94 / 1.00 / 1.00 |
| `must`→`might` (necessity→possibility) | 1.000 / 1.000 / 1.000 | **+1.000 / +1.000 / +1.000** | 20/20 · 20/20 · 20/20 | 1.00 / 1.00 / 1.00 |

Bootstrap 95% CIs on `shift_fn` clear zero in every cell (`will` claude [+0.10,+0.50], gpt [+0.35,+0.75],
gemini [+0.70,+1.00]). The **content-swap control** (modal unchanged) is `shift_ct` ≈ 0 everywhere
(ct-hedge 0–1 of n; the modal-blind/position-bias readers cancel as designed). **base-strong preference is
high in every arm** (0.90–1.00) — the manipulation check the pre-run critic required as a per-arm
interpretation gate: the models read the **base** modal as STRONG, so each arm's shift is interpretable,
not a measurement artifact.

Three things follow, and they all point the same way:

1. **`will`→`would`: the NLI null is an instrument fact.** Under 3-way NLI all three models read "the
   agency *would* see the client → is going to see the client" as **still entailment** (flip 0/0/3 of 20).
   Under the forced choice the **same models, on the same sentences, shift toward the conditional/irrealis
   reading** — gemini 17/20, gpt 13/20, claude 6/20, every CI above zero. So the future→conditional swap
   is **not** inferentially inert; 3-way NLI's entailment frame simply does not register it, while a
   modal-force preference does. **The null relocates to the instrument.**
2. **`shall`→`should`: the NLI panel-split dissolves into concordance.** Under NLI only gemini graded
   *should* as weaker than *required* (0.778); claude and gpt collapsed *should* ≈ *required* (0.056).
   Under the forced choice **all three** distinguish advisory from required at near-ceiling (17/18, 18/18,
   18/18). So the split was **not** a stable model difference in how these models read deontic strength —
   it was an artifact of the NLI "is required to" entailment frame, under which claude and gpt declined to
   call *should*-buy a non-entailment of required-buy. Given a direct preference, they make the
   distinction. **The split relocates to the instrument too.**
3. **`must`→`might`: concordant ceiling on both instruments.** The loud necessity→possibility (with a
   deontic→epistemic flavor cross) registers at ceiling under NLI *and* under forced choice (20/20 all
   three). A swap that changes a relation **either** instrument is calibrated to read flips both.

## What this does to the essay (trigger c): relocates the modal effect to instrument calibration

[`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md) §"A calibrated
reading" hedged between two readings of the modal null — "the **type** of grammatical relation changed"
vs "the **instrument's** sensitivity to that relation" — and named trigger (c) as the decider, *"the
essay's strongest reason for hedging the calibrated reading."* **Trigger (c) fires positive.** A second
indicator, holding the modal swap byte-identical, **does** register the `will`→`would` swap (and the
`shall`→`should` swap for claude/gpt) that NLI leaves null. So the modal near-null is **not** a fact about
the future→conditional *relation* being inferentially inert — it is a fact about **3-way NLI's
calibration**. This vindicates the §"A calibrated reading" thesis in its strongest form: *the inferential
indicator's calibration co-determines the result.* What looked, under one instrument, like "this modal
swap carries no inferential load" is, under a second instrument on the same stimuli, a registered shift.

This sharpens — it does not overturn — [`result/function-word-modal-widening`](function-word-modal-widening.md).
That result's gradient ("loud category mismatch registers in all > within-scale deontic strength registers
in one model > subtle future→conditional registers in none") was **correct about 3-way NLI specifically**.
This result shows the gradient is a property of *that instrument's calibration*, not of the modal swaps:
under a forced-choice modal-force preference the gradient **flattens** — all three modal swaps register,
two of them at or near ceiling for the whole panel.

## What this establishes / does not (the honest bounds — the pre-run critic's required disclosures)

- **Establishes (within-model, cross-instrument):** the `will`→`would` NLI null and the `shall`→`should`
  NLI split are **instrument-specific**, not relation-intrinsic. A single-token forced-choice modal-force
  preference, on the byte-identical frozen stimuli, registers both — so the inferential indicator's
  calibration co-determines whether a modal swap "counts." This is direct evidence for the essay's
  §"A calibrated reading" caveat.
- **The `will`-arm fairness asymmetry (load-bearing — do not over-read the positive).** The HEDGE option
  for `will` explicitly names "conditional or hypothetical," which is exactly the irrealis reading
  standalone *would* carries — so the forced choice is **structurally more disposed** to register
  `will`→`would` than NLI's entailment frame was. The honest reading is therefore "**an instrument that
  explicitly offers the irrealis paraphrase registers the swap that 3-way NLI's entailment frame does
  not**," **not** "the future→conditional relation is robustly inferential across instruments." What the
  result licenses is the *relocation* (the NLI null was not relation-intrinsic), not the stronger claim
  that the models compute the modal's truth-conditional contribution. A registered **preference** is
  weaker than a computed **entailment** — the same gap the project's AANN line named "preference without
  commitment."
- **claude's `will` arm is the weakest cell (6/20, +0.30)** and is read as such: claude registers the
  `will`→`would` shift least even on the forced choice (it most resists reading standalone *would* as
  hedged), where gemini registers it most (17/20). The relocation claim rests on **all three** clearing
  zero, not on any one cell being strong.
- **`shall` rests on a single content pair (`buy`→`give`)** — inherited from the source run (the
  |ΔLg10WF| gap-0.759 supply ceiling under faithful matching). The dissolution of the split is clean (17/18,
  18/18, 18/18) but the arm is thin; read the `shall` cell narrowly.
- **`must`→`might` flavor cross carries over** (deontic→epistemic) — but here it is concordant across both
  instruments, so it is the least load-bearing arm (it confirms the instrument is alive, nothing finer).
- **Does not establish:** any **human comparison** (`internal-contrast-only`) — this result takes no
  position on which reading of *would*/*should* is normatively correct; a BLiMP/NLI human baseline remains
  the optional, not-in-repo Posture-2 upgrade. It is **one** second instrument (a forced-choice preference)
  at temperature 0; a continuation-preference or a graded scalar questionnaire could register differently.
  It does **not** show the modal swaps are inferential "in general" — only that the NLI null was not the
  last word.

## Limitations

- **Single forced-choice instrument, temperature 0.** The strong cells (must, shall, gemini-will) far
  exceed any plausible temp-0 jitter; claude-will (6/20) and gpt-will (13/20) are the cells nearest a
  borderline, but both CIs clear zero.
- **Inherited matching / single corpus norm.** Frequency is SUBTLEX-US `Lg10WF` only (the matching is
  inherited from the source run, not re-derived). Per-arm n is 18–20 (a per-arm characterization, not a
  conjecture re-test; no new operationalization decision was owed — the forced-choice indicator is named
  in the ratified [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)
  Q2(i) "graded forced-choice rate" **and** essay trigger (c), confirmed by the independent pre-run critic).
- **Two instruments differ in more than question type for the `will` arm** (the fairness asymmetry above):
  the relocation is well-supported; the further claim that the relation is "robustly inferential" is not,
  and is not made.
