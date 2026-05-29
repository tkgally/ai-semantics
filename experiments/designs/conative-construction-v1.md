# Design: conative minimal-pair probe v1

**Status:** frozen 2026-05-29 (pre-registration); run same day.
**Conjecture:** [`conjecture/conative-construction`](../../wiki/findings/conjectures/conative-construction.md).
**Governing decision (ratified):** [`decisions/resolved/constructional-divergence-operationalization`](../../wiki/decisions/resolved/constructional-divergence-operationalization.md) — both instruments (NLI + forced-choice), gap threshold ≥30 pp, atypical within 15 pp, frozen at item-commit. **No new decision is opened by this design** (it reuses the ratified divergence operationalization, as NEXT.md anticipated).
**Anchor (ratified):** [`decisions/resolved/conative-anchor`](../../wiki/decisions/resolved/conative-anchor.md) — Scivetti CxNLI conative subset (answer-key + aggregate baseline). Verb-class inventory: Levin (1993) conative-alternation classes.

## Why this probe

The session's CxNLI base-vs-distinction replication ([`result/cxnli-distinction-divergence-v1`](../../wiki/findings/results/cxnli-distinction-divergence-v1.md)) found the **conative the single hardest construction in every panel model** (55–75 pp base→distinction drop) — but on *Scivetti's* items. This probe tests the *same completion-entailment contrast with the project's own verb-held-constant minimal pairs*, the cleaner design the conjecture calls for: the verb is identical across the two frames, so any difference in the completed-contact inference cannot come from the verb's lexical entry — it must be `constructional`.

## The contrast

| frame | example | does it entail completed contact? |
|---|---|---|
| transitive `V NP` | *Maria kicked the ball.* | **yes** (entailed) |
| conative `V at NP` | *Maria kicked at the ball.* | **no** (attempted/directed-at; contact not entailed) |

The verb (*kick*) is held constant; only the construction (direct object vs. *at*-oblique) varies.

## Stimuli (frozen — `experiments/data/conative/items.csv`, sha256[:16] `9ae53279dc483827`)

56 items, emitted by `build_items.py` and committed **before** any probe call:

- **Arm 1 — conative-class verbs** (48 items): 12 Levin (1993) conative-alternation verbs (hit / swat / cut classes) — *kick, hit, punch, slash, stab, claw, swat, jab, chop, scratch, hack, strike* — each crossed with {typical, atypical} object × {transitive, conative} frame.
  - **Typical vs. atypical object = the memorization/frequency control** (P3 / [`open-question/constructional-vs-frequency-confound`](../../wiki/findings/open-questions/constructional-vs-frequency-confound.md)): atypical objects (*gourd, gong, effigy, tarp, bolster, settee, divan, mannequin, sapling, lectern, bramble, cymbal*) are lower-frequency collocations, so a non-completion reading that **persists** there is less plausibly a memorized-string artifact.
- **Arm 2 — control (non-alternating) verbs** (8 items): touch-class (*touch, kiss*) and break-class (*break, shatter*) — verbs that do **not** take the conative in Levin. Typical object, both frames. P2 prediction: the contact-cancellation should be **weaker/absent** here. The control **conative** string (*touched at the wall*) is **anomalous**, so its gold is `NA` — that cell is reported as an affirm-rate only, never scored for accuracy.

The verb set was revised **before running**, after an adversarial coherence pass: *bite*→*stab* and *peck*→*strike* (bite/peck have a dominant iterative-contact reading, so "V at NP" can still entail contact — a wrong-direction gold); *swat* object *fly*→*cushion* (a swatted fly is not robustly contacted, which would shrink the gap for non-constructional reasons). See `build_items.py` header for the full rationale.

## Instruments (both; ratified)

- **NLI**: premise = sentence; hypothesis = "*&lt;Subj&gt; made contact with &lt;obj&gt;.*"; label 0/1/2. Construction-correct gold: transitive → 0 (entailment); conative → 1 (neutral — the conative *cancels* the entailment, it does not assert non-contact, so neutral not contradiction).
- **Forced-choice**: "*Based only on the sentence, did &lt;Subj&gt; make contact with &lt;obj&gt;? YES / NO / CANT_TELL*". Construction-correct gold: transitive → YES; conative → CANT_TELL.

Same NLI system prompt and temperature-0 greedy parse as the comparative-correlative and CxNLI probes (one instrument across the project's probes). No logprobs needed (panel exposes none on OpenRouter).

## Primary indicator and decision rule (frozen)

**Affirm completed-contact rate** = FC answer YES, or NLI label 0 (entailment).

- **P1 (core):** `gap = transitive_affirm − conative_affirm ≥ 30 pp` in ≥2/3 panel models, **replicating across verbs** (a majority of the 12 verbs show a positive gap, not one verb carrying it). Confirms the conjecture's "use" core.
- **P3 (frequency-orthogonal):** the typical-object gap and atypical-object gap differ by **≤15 pp** (the non-completion reading persists for low-frequency objects).
- **P2 (verb-class):** the control-verb gap is **smaller** than the conative-class gap (the effect is construction-specific, not a generic "*at* = atelic" effect). Interpreted cautiously — the control conative is anomalous.

A **null** (flat affirm-rate across frames) is a first-class result for the `distributional` position (charter §8) and will be written as such.

## Panel, cost, scope

- Panel ([`config/models.md`](../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C), as subjects. 56 × 2 instruments × 3 = **336 calls**; estimated ≪ $0.10 (well under the $5 single-run flag).
- **Scope / limits this design accepts up front:** N = 12 verbs (24 items/frame/model); single run, single date; behavioral NLI/FC only; shared-priors caveat (charter §2.5); *swat*'s transitive contact is the softest of the set; the contact hypothesis predicate ("made contact with") is verb-neutral but reads most naturally for impact verbs. The Scivetti anchor gives an *answer-key + aggregate* human baseline, not a per-item gradient, and our items are the project's own (not Scivetti's), so the human comparison is to the *phenomenon*, not item-matched.
