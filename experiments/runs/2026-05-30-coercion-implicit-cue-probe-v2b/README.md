# Run record — caused-motion implicit-cue probe v2b

**Date:** 2026-05-30
**Design (frozen, pre-registered):** [`design/coercion-implicit-cue-v2b`](../../designs/coercion-implicit-cue-v2b.md)
**Governing decision (ratified):** [`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (conflicting-cue primary + graded ladder + report-the-rate). **No new decision.**
**Conjecture probed:** [`conjecture/caused-motion-construction`](../../../wiki/findings/conjectures/caused-motion-construction.md)
**Refines:** [`result/argument-structure-coercion-v2`](../../../wiki/findings/results/argument-structure-coercion-v2.md) (the explicit-cue add-direction v2)
**Result page:** [`result/coercion-implicit-cue-v2b`](../../../wiki/findings/results/coercion-implicit-cue-v2b.md)

## What ran

The **v2b** the add-direction v2 deferred: an **implicit world-knowledge** conflicting cue. v2 showed the caused-motion ceiling drops to floor under an *explicit* outcome denial ("…but the napkin never moved"). v2b asks whether the model also blocks a **physically impossible** coercion (a sneeze moving an immovable object) **from world knowledge alone**, with no outcome stated — graded against the explicit cue as the within-experiment calibration.

- **Indicator:** affirm-caused-motion rate (FC YES / NLI entailment) on "&lt;subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move"; temperature 0, no logprobs → existing 3-family behavioral panel.
- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C).
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `9aad20a22d183402`, after the pre-run critique fixes below): 30 items — 10 scenes (verb+path held constant) × {canonical (light object), implicit-wk (immovable object, no outcome), explicit (immovable + outcome denial)}.

## Conditions & key comparison

| condition | example | affirm-motion gold |
|---|---|---|
| `canonical` | Maria sneezed the dust off the pedestal. | YES (ceiling anchor) |
| `implicit-wk` | Maria sneezed the bolted-down bust off the pedestal. | NO (world-knowledge; contestable) |
| `explicit` | …off the pedestal, but it never budged. | NO (outcome stated; calibration) |

**Discriminator:** implicit-wk affirm vs explicit affirm. ~equal & low → world knowledge alone blocks the coercion (strong H-deep); implicit-wk ≫ explicit → the explicit outcome is needed. **Instrument note (reported):** under NLI the implicit-wk premise *asserts* the motion (conflict is only with external world knowledge), so the NLI-vs-FC gap on that cell is itself a datum.

## Human anchor

**Pending / internal-contrast-only** (Option-4 logic, same as v2). The `canonical` arm keeps the v1/v2 phenomenon-level caused-motion anchor (Scivetti); the cue cells have **no in-repo human baseline** (no Scivetti impossible-coercion items; the "correct" reading is contestable for humans) → **no human-level claim**. No human label invented.

## Pre-registration / no-retuning

- Difficulty axis (conflicting-cue), graded ladder, reading rule, and human-anchor scope were **fixed by the ratified gate BEFORE this build**.
- Items frozen + committed **before any probe call** (sha256[:16] `438d746e51352776`).
- **Adversarial pre-run pass:** independent read-only subagent critique (see below).
- `analyze.py` reports affirm rate per condition + the implicit-vs-explicit gap + canonical→cue drops; no threshold tuned after the run.

## Files

- `build_items.py` — emits + freezes `experiments/data/coercion-implicit-cue-v2b/items.csv`.
- `probe.py` — runner (NLI + FC × 3 models), copied from the add-direction v2.
- `analyze.py` — affirm rate per condition; implicit−explicit gap; canonical→cue drops; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Pre-run critique

An **independent read-only adversarial subagent** critiqued the frozen stimuli before the run. It found a **BLOCKER** — `huff`/`puff` lexicalize directed air-propulsion (the design's own disqualifier, like "blow"), so their canonical YES could be *literal* rather than *coerced*; and `gasp` (an inward intake — wrong direction) and `snore` (non-directed vibration — feeble) made physically implausible canonicals. Applied the fix (re-froze `438d746e51352776` → `9aad20a22d183402`):

- **huff/puff/gasp/snore → wheeze/splutter/hiccup/sneeze** — all intransitive involuntary outbursts whose transitive caused-motion is genuinely coerced (the canonical YES can only come from the construction, not from a lexicalized propulsion sense).
- **Path refits:** the gasp scene's dangling "off its base" (only fit the heavy column) → "off the ledge" with object "granite urn"; Aisha's "away from the wall" (bookcase-specific) → "off the shelf" with "cast-iron skillet"; the grand-piano "across the stage" → "off the table" with "solid bronze statuette" — so the canonical reads cleanly for the light object too.

Critic confirmed: immovability descriptors ("bolted-down", "cast-iron", "two-ton", …) all clearly signal a breath cannot move the object; deny-clauses all cleanly deny motion; gold mechanics correct throughout. The known NLI-implicit-wk contestability is a documented reported feature, not a defect. The sneeze-Maria / cough-Jordan,Sam / whistle scenes were judged clean as-is.

## Results / cost

180 calls, **0 NA**, cost **$0.039** (A $0.028 / B $0.002 / C $0.009). **Headline: the models do NOT block the impossible coercion from world knowledge alone — they need the explicit outcome statement.** With only the in-premise immovability descriptor, affirm-caused-motion stays near-ceiling (implicit-wk 90–100%; gpt-5.4-mini FC the lone exception at 40%); only the **explicit** outcome denial drives it to floor (0%, gpt-5.4-mini FC 10%). implicit − explicit = NLI [100, 90, 100] pp, FC [90, 30, 100] pp. So the v2 cue-sensitivity is **explicit-outcome parsing, not world-model integration** — and even under FC (where world knowledge should engage), claude (90%) and gemini (100%) still affirm the impossible coercion; only gpt-5.4-mini partially engages it. Full write-up at [`result/coercion-implicit-cue-v2b`](../../../wiki/findings/results/coercion-implicit-cue-v2b.md); reproducible from `raw/results.json`.

**NOTE — path bug caught + fixed:** same hardcoded-`ITEMS`-path bug as the cancel-direction run (the copied `probe.py` pointed at `argument-structure-coercion-v2/items.csv`). The pre-fix run loaded the wrong stimuli; the path was corrected to `coercion-implicit-cue-v2b/items.csv` and the probe re-run on the correct frozen items. Numbers above are from the corrected run.

**Post-run verification:** every figure independently recomputed from `raw/*.json` by a read-only adversarial subagent.
