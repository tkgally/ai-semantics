---
type: design
id: conative-preference-commitment-v1
title: conative preference/commitment v1 — does the AANN "preference without commitment" dissociation generalize to a fresh divergent-default construction?
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: provisional
anchor: pending
contingent-on: []
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: operationalizes
    target: conjecture/preference-commitment-generality
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v1 — conative preference/commitment double contrast

> **Status: provisional → frozen at the `PREREG.md` step after a fresh independent pre-run-critic
> GO.** This design runs entirely under the **ratified** decision
> [`decisions/resolved/fresh-construction-inferential-generalization`](../../wiki/decisions/resolved/fresh-construction-inferential-generalization.md)
> (Option A — the conative; ratified 2026-06-15, autonomous adversarial review), inheriting the AANN
> double-contrast discipline ([`decisions/resolved/aann-inferential-default-coincidence`](../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)).
> No new decision is opened: the yardstick is fixed. It operationalizes
> [`conjecture/preference-commitment-generality`](../../wiki/findings/conjectures/preference-commitment-generality.md).

## 1. The question

The AANN inferential probe produced the project's sharpest cross-instrument dissociation, replicated
cell-for-cell across two item sets ([`result/aann-inferential-v6`](../../wiki/findings/results/aann-inferential-v6.md),
[`result/aann-inferential-v4`](../../wiki/findings/results/aann-inferential-v4.md)): a forced-choice
**paraphrase preference** shifts toward the licensed reading in **all three** panel models, but the
NLI **entailment commitment** carries over in **only one** (gpt-5.4-mini). The forward bet
([`conjecture/preference-commitment-generality`](../../wiki/findings/conjectures/preference-commitment-generality.md))
is that this **preference-without-commitment** dissociation is a *general* property of constructions
whose licensed inference diverges from their distributional default, not an AANN artifact.

This design tests that bet on the **conative** ("Maria kicked **at** the ball" → may not have made
completed contact) — a **cancel-direction** construction: the licensed inference (no guaranteed
contact) runs *opposite* to the verb's distributional default (*kick* lexically implies contact), so
the inference-vs-default divergence and the headroom the AANN had to *engineer* are here **for free**.

## 2. Conditions (the three item families; verb + object held constant within a stem)

Hypothesis / contact proposition throughout: *"&lt;subj&gt; made contact with &lt;obj&gt;."*

| family | example | role | contact default |
|---|---|---|---|
| `transitive` (conative verbs) | Maria kicked the ball. | **headroom anchor** — the lexical default the conative suppresses; must read at ceiling | ENTAILED |
| `conative` (target) | Maria kicked at the ball. | **the construction** — licensed cancel-direction | SUPPRESSED (licensed: not guaranteed) |
| `resist` / **LCC** (non-alternating verbs in `V at NP`) | Maria touched at the wall. | **lexical-cue control** — same bare *at* cue, **not** a licensed conative | anomalous |
| `transitive` (resist verbs) | Maria touched the wall. | resist-baseline (resist verbs entail contact transitively) | ENTAILED |

- **Conative verbs (target):** the 12 Levin (1993) conative-alternation hit/swat/cut-class verbs from
  the frozen [`result/conative-cancel-direction-v2`](../../wiki/findings/results/conative-cancel-direction-v2.md)
  set (kick/hit/punch/slash/stab/claw/swat/jab/chop/scratch/hack/whack), with their typical objects.
  These already ran off-ceiling under the conative frame (v1/v2).
- **Resist verbs (LCC):** non-alternating contact verbs that do **not** take the conative in Levin
  1993 (touch/break-class), expanded to **8** for a stabler cue baseline (touch, embrace, break,
  shatter, + four more in the same non-alternating contact families — see `prep.py`). Forced into the
  anomalous `V at NP` frame, they carry the bare *at* cue **without** the licensed conative
  construction. **This is the cue control the ratified decision names** ("the non-alternating /
  anomalous *at*-string family the v1 and v2 probes already used"). Verb-class differs from the
  target by necessity (only non-alternating verbs are non-conative) — the double contrast is therefore
  *licensed-conative-vs-anomalous-at-string*, not a perfect lexical minimal pair; this caveat is
  inherited from, and made explicit by, the ratified decision, and is restated on the result page.

## 3. The two instruments (both on the same frozen items)

### Arm 1 — paraphrase forced-choice (the PREFERENCE signal; the *weaker* instrument)

Present the sentence and two lexically parity-matched paraphrases; ask which the sentence better
supports. The two options differ **only** by the cancellation operator *"did not necessarily"*:

- option **D** (default reading): *"&lt;subj&gt; made contact with &lt;obj&gt;."*
- option **C** (cancel reading): *"&lt;subj&gt; did not necessarily make contact with &lt;obj&gt;."*

A/B letter assignment is **seed-counterbalanced** per item (fixed seed, recorded). Parse the chosen
letter → reading. **Preference measure** = P(cancel-reading C chosen). This indexes graded
distributional *compatibility* with the cancel reading.

### Arm 2 — NLI entailment (the COMMITMENT signal; the load-bearing DISCRIMINATOR)

Premise = sentence; Hypothesis = *"&lt;subj&gt; made contact with &lt;obj&gt;."*; relation 0/1/2
(entailment / neutral / contradiction), single-token, temperature 0 — identical instrument to the
frozen conative-cancel-v2 NLI arm. The conative-correct answer is **neutral** (1): contact is *not
guaranteed* but not impossible. **Commitment-to-cancellation measure** = P(withholds the contact
entailment) = P(NLI ≠ 0). (Reported alongside the precise P(NLI = neutral) and the P(NLI = entailment)
"still commits to contact" rate, so the verdict does not hinge on collapsing neutral+contradiction.)

The conative has **no AANN-style grammaticalized agreement reflex**, so — exactly as the ratified
decision requires (binding condition 4) — the **NLI commitment arm carries the discriminator role**;
the paraphrase arm is explicitly the weaker signal. A paraphrase shift without an NLI shift is
reported as **"preference without commitment,"** never as "the model draws the inference."

## 4. The double contrast (headline; net of the bare-*at* cue)

For each instrument, the headline is the **double contrast** — the construction must move the reading
*more than the matched anomalous at-string moves it*:

- **Δ²_pref** = P(cancel-pref | `conative`) − P(cancel-pref | `resist`/LCC)
- **Δ²_commit** = P(withhold | `conative`) − P(withhold | `resist`/LCC)

A shift wholly attributable to the bare *at* cue (the LCC shifts as much as the conative → Δ² ≈ 0) is
declared a **LEXICAL-CUE ARTIFACT** and cannot carry the headline. The raw component effects
(conative − transitive; resist − transitive) are reported in full for transparency, but the **headline
is Δ²** (per binding condition 2).

## 5. Headroom precondition (conative-translated; the ratification condition)

The ratified decision adds one **yardstick-translation** condition: the AANN P(uni|control) ≤ 0.30 /
≤ 0.50 thresholds were defined for the *unification* reading and must **not** be imported literally.
The conative-appropriate gate, re-verified on the frozen items **pre-headline, per model**:

- **HEADROOM PASS (per model):** the contact default is at ceiling on the `transitive` items — both
  P(NLI = entailment | transitive) ≥ **0.85** **and** P(paraphrase = D | transitive) ≥ **0.85** — so
  there is genuine room for the conative to suppress it.
- **HEADROOM-FAIL (per model):** the transitive contact default is not at ceiling → no room to read a
  construction effect; that model's headline is uninterpretable.
- **Whole-design gate:** if fewer than **2 of 3** models clear headroom, the design's headline does
  not stand and the run routes to the **Option-B named fallback** (way/caused-motion near-miss
  variant), exactly as the ratified decision specifies. No retuning.

## 6. Thresholds, bootstrap, verdict map (frozen pre-run — no post-hoc tuning)

- **τ = 0.20** on the double contrast (carried from the AANN instrument, binding condition 3).
- **Significance:** item-level bootstrap **95% CI lower bound > 0** on Δ², **10,000 resamples**,
  fixed **seed = 20260615**. A double contrast counts as "positive" iff Δ² ≥ τ **and** CI-lower > 0.
- **Tier-0 manipulation check:** on the `transitive` items the model must affirm contact (the headroom
  gate doubles as this); a model failing it is flagged INSTRUMENT-SUSPECT for that arm.

### Per-model verdict map

| verdict | condition |
|---|---|
| **CONVERGENT-POSITIVE** | Δ²_pref positive **and** Δ²_commit positive |
| **PARAPHRASE-ONLY** (preference without commitment) | Δ²_pref positive, Δ²_commit **not** positive |
| **COMMITMENT-ONLY** (surprise) | Δ²_commit positive, Δ²_pref **not** positive — reported as an anomaly, not folded into "confirm" |
| **LEXICAL-CUE ARTIFACT** | a raw conative shift exists but Δ² (net of LCC) not positive on either arm |
| **NULL** | no shift on either arm (conative ≈ transitive) |
| **HEADROOM-FAIL** | transitive contact default off-ceiling for that model |

### Panel-level verdict (the conjecture's symmetric confirm/falsify)

- **CONFIRM (generalizes):** the **qualitative AANN shape** reproduces — Δ²_pref positive in most or
  all of the panel, Δ²_commit positive in a **minority**, with **≥ 1 model CONVERGENT-POSITIVE and
  ≥ 1 model PARAPHRASE-ONLY**.
- **FALSIFY (convergence):** **all three** models CONVERGENT-POSITIVE (full cross-instrument
  convergence) → the dissociation is plausibly AANN-specific.
- **FALSIFY (null):** **all three** models NULL (no preference shift to dissociate from) → the
  antecedent is absent for the conative; the instance falls, the conceptual point survives un-instanced.
- **INCONCLUSIVE → fallback:** headroom fails for < 2 models → route to Option-B; no headline.

## 7. Pre-registered scoring rule for the known gpt-5.4-mini conative fragility (binding anti-cheat)

gpt-5.4-mini **already** shows conative NLI fragility — under NLI it affirms contact for the conative
(does **not** withhold; [`result/conative-cancel-direction-v2`](../../wiki/findings/results/conative-cancel-direction-v2.md),
[`result/conative-minimal-pair-divergence-v1`](../../wiki/findings/results/conative-minimal-pair-divergence-v1.md)).
**This pre-existing, single-model divergence must NOT be retrofitted as new confirmation of the
generality conjecture.** The test is whether the **full panel** reproduces the AANN *shape*; the
identity of any CONVERGENT-POSITIVE model is read **from this run's data**, not assumed. Note in
advance: in AANN, gpt-5.4-mini was the *converger*; on the conative its prior fragility predicts it
will be PARAPHRASE-ONLY here, so a genuine CONFIRM needs a **different** model to converge — making
this a stringent, non-circular test.

## 8. Anchor discipline (binding condition 5; honest split)

- The **NLI entailment arm** makes a human-comparison claim against the CxNLI conative gold labels:
  **human-anchored** via [`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)
  (conative subset, ratified 2026-05-29 as the conative anchor) — an **answer-key comparison + ≈0.90
  aggregate Exp-1 baseline, NOT a per-item human gradient** (the release gives a single adjudicated
  gold label per item). The CxNLI conative gold for "V-at-NP → made contact" is **non-entailment** (the
  catalogued triple *"I sipped at the Heineken."* / *"The Heineken was not the target of my sipping."*
  is **Contradiction**, Table 9), so the answer-key for the conative items' contact-entailment
  hypothesis is **neutral/non-entailment** — the conative-correct withhold.
- The **paraphrase forced-choice arm** and the **resist/LCC arm** stay **`anchor: internal-contrast-only`**
  — no in-repo human paraphrase-preference norm exists, and the anomalous at-string has no human
  reading key. The result page declares this split precisely.
- **No anchor invented.** The expert-stipulated conative-correct paraphrase reading (cancel) is labelled
  expert-stipulated wherever used.

## 9. Files & freeze discipline (binding condition I8, inherited)

- `experiments/runs/2026-06-15-conative-preference-commitment-v1/prep.py` — stimulus authoring; emits
  `stimuli.json` (frozen, seed 20260615); asserts the parity/headroom-buildability/LCC-isolation
  checks; **no model calls**.
- `.../stimuli.json` — frozen materials (committed before any probe call; sha256 recorded in README).
- `.../probe.py` — panel calls (paraphrase-FC + NLI, temperature 0, gemini `reasoning:{effort:"minimal"}`
  + token cap per the cost-driver mitigation); **refuses to run without a frozen `PREREG.md` and a
  present `analyze.py`**; codes `ABORT_USD = 0.50`.
- `.../analyze.py` — frozen analysis (double contrast, bootstrap, headroom gate, verdict map);
  `--selftest` must pass before freeze.
- `.../PREREG-draft.md` → `PREREG.md` (frozen only after the fresh independent pre-run-critic GO).

## 10. Spend — pre-flight estimate

≈12 conative verbs × {transitive, conative} + 8 resist verbs × {transitive, resist} = **40 items**;
40 × 2 instruments × 3 models = **240 calls** (+ a small verbatim retry per unparseable response). At
the AANN v6 measured shape ($0.0001524/billed call), **≈ $0.037 point estimate; expected ≈ $0.04–0.08
billed** (cf. conative v1 $0.071, conative v2 $0.30 — v2 ran longer FC prompts). Well under the
single-run flag and the **$5.00/day UTC** cap ([`config/budget.md`](../../config/budget.md); day total
2026-06-15 before this run: $0.00). Actual billed `usage.cost` recorded in the run record; missing-cost
calls counted, never silently dropped.
