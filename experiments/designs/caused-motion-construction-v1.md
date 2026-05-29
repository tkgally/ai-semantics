# Design: caused-motion minimal-pair probe v1

**Status:** frozen 2026-05-29 (pre-registration); run same day.
**Conjecture:** [`conjecture/caused-motion-construction`](../../wiki/findings/conjectures/caused-motion-construction.md).
**Governing decision (ratified):** [`decisions/resolved/constructional-divergence-operationalization`](../../wiki/decisions/resolved/constructional-divergence-operationalization.md) — both instruments, gap ≥30 pp, atypical within 15 pp, frozen at item-commit. **No new decision opened** (reuses the ratified divergence operationalization, like the conative probe).
**Anchor (ratified):** [`decisions/resolved/caused-motion-anchor`](../../wiki/decisions/resolved/caused-motion-anchor.md) — Scivetti CxNLI caused-motion subset (answer-key + aggregate baseline). Descriptive inventory: Goldberg (1995, ch. 7).

## Why this probe

The third own-design probe in the argument-structure wedge, after the conative ([`result/conative-minimal-pair-divergence-v1`](../../wiki/findings/results/conative-minimal-pair-divergence-v1.md)). Where the conative tests whether the construction *removes* an entailment (completed contact), caused-motion tests whether it **adds** one: Goldberg's canonical case that argument-structure meaning is not projected from the verb. *Sneeze* is intransitive and denotes no motion, yet *Maria sneezed the napkin off the table* entails the napkin moved and her sneezing caused it. An affirmed causation-of-motion inference here cannot come from the verb's lexical frame — it must be `constructional`.

## Stimuli (frozen — `experiments/data/caused-motion/items.csv`, sha256[:16] `ebb37ae501d455ca`)

30 items: 10 non-motion verbs × 3 forms, emitted by `build_items.py` and committed **before** any probe call.

- **cm** (caused-motion frame): *Maria sneezed the napkin off the table.* → caused-motion **entailed** (NLI 0 / FC YES).
- **ctrl-loc** (intransitive verb; object stated to stay): *Maria sneezed. The napkin stayed on the table.* → **contradiction** of the causal hypothesis (motion denied; NLI 2 / FC NO).
- **ctrl-sep** (object moves, but by another cause, co-temporal): *The napkin blew off the table in a draft while Maria sneezed.* → **not-entailed / neutral** (the premise asserts an alternative cause but does not deny a verb-contribution; NLI 1 / FC CANT_TELL). The **causation-specific** control: motion is present but not caused by the verb.

Primary indicator = **affirm caused-motion rate** on the hypothesis "*&lt;Subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move.*" (FC YES, or NLI entailment).

- **Typical verbs** (canonical coercions): sneeze, cough, huff, laugh, whistle.
- **Atypical verbs** (low-frequency-in-construction = the memorization/frequency control, P3): hiccup, shiver, yawn, snore, shudder.
- **Object animacy** is recorded so the result can report the **inanimate-propulsion core** (sneeze/cough/huff/hiccup/shiver — crisp "caused to move") separately from animate volitional self-movers (laugh/whistle/yawn/snore/shudder — a softer caused-motion: the agent could refuse).

The set was revised **before running** after an adversarial coherence pass: (i) ctrl-sep gold corrected from contradiction to neutral/CANT_TELL (an alternative cause does not contradict a joint-causation hypothesis); (ii) *wink*→*huff* (the "winked the waiter over" summoning reading is too soft); (iii) an `animacy` split added. shudder/shiver themselves denote body-motion, so a positive cm there is less diagnostic of pure constructional coercion — kept for the atypical arm, flagged in Limits.

## Instruments, decision rule (frozen)

Both NLI (0/1/2) and forced-choice (YES/NO/CANT_TELL); same prompts/temperature-0 parse as the conative/CC/CxNLI probes. Confirm bar (conjecture): **cm rate ≥70%**, **gap ≥30 pp** vs. the worst control, in ≥2/3 models, **holding for atypical verbs** (atypical within 15 pp of typical). A flat cm-vs-control rate is a first-class null for the `distributional` position.

## Panel, cost, scope

Panel ([`config/models.md`](../../config/models.md)) as subjects; 30 × 2 instruments × 3 = **180 calls**; ≪ $0.10. **Limits accepted up front:** N=10 verbs (cm N=10/model); single run/date; behavioral only; the animate-object cm items are a softer reading (reported split); shudder/shiver verbs denote motion; ctrl-sep changes both "construction absent" and "competing cause present" together; Scivetti anchor is answer-key/aggregate and these are the project's own items (phenomenon-level comparison).
