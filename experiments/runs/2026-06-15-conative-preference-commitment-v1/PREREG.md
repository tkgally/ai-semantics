# PREREG — conative preference/commitment double contrast (v1) [FROZEN]

> **Status: FROZEN 2026-06-15.** An independent pre-run critic returned
> **GO-WITH-FIXES**; the one SHOULD-FIX (resist verb `snap`→`bump`, a lexical-cue-control
> purity defect) was applied pre-run and the stimuli refrozen (`stimuli.json` sha256[:16]
> `3ca3a1d50069f0cd`); `analyze.py --selftest` re-passed (30 checks). This is the binding
> pre-registration; `probe.py` runs only with this file present. It mirrors the frozen design
> `experiments/designs/conative-preference-commitment-v1.md` §4–§8. No new
> decision is opened; this run executes under the ratified
> `decisions/resolved/fresh-construction-inferential-generalization` (Option A —
> the conative), inheriting the AANN double-contrast discipline.

## 0. The bet (operationalizes `conjecture/preference-commitment-generality`)

The AANN inferential probe's preference-without-commitment dissociation (paraphrase
preference shifts in all three panel models; NLI entailment commitment carries in
only one) is a GENERAL property of constructions whose licensed inference diverges
from their distributional default — not an AANN artifact. Tested here on the
**conative** ("Maria kicked **at** the ball" → contact not guaranteed), a
cancel-direction construction where the inference-vs-default divergence is free.

## 1. Frozen materials

- `stimuli.json` — 40 items, frozen by `prep.py` (seed **20260615**), committed
  before any probe call. **sha256[:16] = `3ca3a1d50069f0cd`** (post-critic refreeze).
- Four families (verb + object + subject held constant within a stem):
  `transitive_conative` (12), `conative` (12), `resist`/LCC (8),
  `transitive_resist` (8).
- 12 conative verbs reused verbatim from `result/conative-cancel-direction-v2`
  (kick/hit/punch/slash/stab/claw/swat/jab/chop/scratch/hack/whack). 8 resist verbs:
  touch/embrace/break/shatter (reused) + crush/smash/**bump**/split (non-alternating
  contact verbs, no conative in Levin 1993).
- **Pre-run critic fix (2026-06-15, GO-WITH-FIXES):** "snap" was removed from the
  resist/LCC pool and replaced with "bump" — *snapped at* is a lexicalized idiom that
  would contaminate the lexical-cue control (conservative direction, but a purity
  defect). smash/crush remain marginal; the result page reports Δ² robustness with and
  without smash/crush in the resist pool.

## 2. Two instruments (both on the same 40 frozen items; design §3)

- **Arm 1 — paraphrase forced-choice (PREFERENCE; the WEAKER signal).** Two
  lexically parity-matched options differing ONLY by "did not necessarily":
  D (default) "<subj> made contact with the <obj>." / C (cancel) "<subj> did not
  necessarily make contact with the <obj>." Seed-counterbalanced A/B per item;
  chosen letter → reading. **Preference measure = P(cancel-reading C chosen).**
- **Arm 2 — NLI entailment (COMMITMENT; the load-bearing DISCRIMINATOR).** Premise
  = sentence; hypothesis = "<subj> made contact with the <obj>." → 0/1/2; identical
  NLI_SYS + parse_nli to the frozen conative-cancel-v2 NLI arm. **Commitment
  measure = P(withhold) = P(NLI ≠ 0).** Conative-correct = neutral (1).
- A paraphrase shift without an NLI shift is reported as **"preference without
  commitment,"** never "the model draws the inference."

## 3. The double contrast (headline; design §4)

- **Δ²_pref** = P(cancel-pref | conative) − P(cancel-pref | resist/LCC)
- **Δ²_commit** = P(withhold | conative) − P(withhold | resist/LCC)

Raw component effects (conative − transitive; resist − transitive) reported in full,
but the headline is Δ². A shift wholly attributable to the bare-*at* cue
(LCC shifts as much as the conative → Δ² ≈ 0) is a **LEXICAL-CUE ARTIFACT** and
cannot carry the headline.

## 4. Thresholds + bootstrap (frozen pre-run; design §6)

- **τ = 0.20** on the double contrast (inclusive, ≥).
- **Significance:** item-level bootstrap **95% CI lower bound > 0** (strict),
  **10,000 resamples**, fixed **seed = 20260615**. (Conative and resist verb pools
  are disjoint by necessity; the resample is a two-sample item-level bootstrap.)
- A double contrast is **positive** iff Δ² ≥ τ AND CI-lower > 0.
- **Tier-0 manipulation check** doubles as the headroom gate (§5).

## 5. Headroom precondition (conative-translated; the ratification condition; design §5)

Pre-headline, per model. NOT the AANN unification thresholds (those are not imported):

- **HEADROOM PASS:** P(NLI = entailment | transitive_conative) ≥ **0.85** AND
  P(paraphrase = D | transitive_conative) ≥ **0.85** (both inclusive).
- **HEADROOM-FAIL:** transitive contact default off-ceiling → that model's headline
  is uninterpretable.
- **Whole-design gate:** if fewer than **2 of 3** models clear → HEADROOM-FAIL →
  route to the **Option-B named fallback** (way/caused-motion near-miss variant).
  No retuning.

## 6. Per-model verdict map (design §6)

| verdict | condition |
|---|---|
| CONVERGENT-POSITIVE | Δ²_pref positive AND Δ²_commit positive |
| PARAPHRASE-ONLY | Δ²_pref positive, Δ²_commit NOT positive |
| COMMITMENT-ONLY (anomaly) | Δ²_commit positive, Δ²_pref NOT positive |
| LEXICAL-CUE ARTIFACT | raw conative shift exists but Δ² not positive on either arm |
| NULL | no shift on either arm |
| HEADROOM-FAIL | transitive contact default off-ceiling for that model |

## 7. Panel-level verdict (design §6)

- **CONFIRM (generalizes):** AANN shape reproduces — ≥1 model CONVERGENT-POSITIVE
  AND ≥1 model PARAPHRASE-ONLY.
- **FALSIFY (convergence):** all (headroom-clearing) models CONVERGENT-POSITIVE →
  dissociation plausibly AANN-specific.
- **FALSIFY (null):** all (headroom-clearing) models NULL → antecedent absent for
  the conative; instance falls, conceptual point survives un-instanced.
- **INCONCLUSIVE → fallback:** headroom fails for < 2 models → route to Option-B.

## 8. gpt-5.4-mini scoring rule (binding anti-cheat; design §7)

gpt-5.4-mini already shows conative NLI fragility (does not withhold contact for the
conative under NLI; `result/conative-cancel-direction-v2`,
`result/conative-minimal-pair-divergence-v1`). **This pre-existing, single-model
divergence must NOT be retrofitted as new confirmation.** The converging model's
identity is read from THIS run's data. gpt-5.4-mini is predicted PARAPHRASE-ONLY
here, so a genuine CONFIRM needs a **different** model to converge — a stringent,
non-circular test.

## 9. Anchor discipline (honest split; design §8)

- **NLI entailment arm (conative items):** human-anchored against the CxNLI conative
  gold via `resource/scivetti-2025-cxnli-dataset` (conative subset, ratified
  2026-05-29). Answer-key comparison + ≈0.90 aggregate Exp-1 baseline, NOT a per-item
  human gradient. CxNLI conative gold for "V-at-NP → made contact" is
  non-entailment → answer-key = withhold.
- **Paraphrase forced-choice arm + resist/LCC arm:** `anchor: internal-contrast-only`
  — no in-repo human paraphrase-preference norm; anomalous at-string has no human key.
- **No anchor invented.** The expert-stipulated conative-correct paraphrase reading
  (cancel) is labelled expert-stipulated wherever used.

## 10. Spend (design §10)

40 items × 2 instruments × 3 models = **240 calls** (+ a small verbatim retry per
unparseable response). Point estimate **≈ $0.037**; expected **≈ $0.04–0.08** billed.
`ABORT_USD = 0.50` single-run flag. Well under the $5.00/day UTC cap. Actual billed
`usage.cost` recorded; missing-cost calls counted, never silently dropped.
