# PREREG — add-arm headroom calibration (frozen before any probe call)

**Date:** 2026-06-28 (session 133)
**Frozen items:** `experiments/data/addarm-headroom-calibration/items.csv`, sha256[:16] **`471a5940ba8f65ff`** (emitted by `build_items.py`, committed before any API call).
**Discharges (or fails to discharge):** the s132 KEEP-OPEN **BLOCKER (prerequisite 1)** on [`decisions/open/constructional-monotonicity-generalization-operationalization`](../../../wiki/decisions/open/constructional-monotonicity-generalization-operationalization.md) — "**Demonstrated add-arm headroom on frozen calibration items**." Design-level companion: [`open-question/constructional-monotonicity-addarm-headroom`](../../../wiki/findings/open-questions/constructional-monotonicity-addarm-headroom.md).
**Conjecture in the background:** [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md). **This calibration does NOT test the conjecture** — it only decides whether a future battery's *add arm* can be built without the degeneracy trap.
**Human anchor:** **none asserted — `internal-contrast-only`.** This is a within-model construction-vs-control affirm-rate measurement to decide build feasibility; it makes **no human-comparison claim** and invents no human label.

## What runs

For two candidate ADD constructions, the no-cue **licensing gap** is measured per verb:

| arm | example (resultative) | hypothesis | want |
|---|---|---|---|
| `construction` | "Maria hammered the metal flat." | "The metal became flat." | **ceiling** affirm (construction licenses the added entailment) |
| `control` | "Maria hammered the metal." | "The metal became flat." | **off-ceiling** affirm (bare default does NOT supply it) |

- **resultative** (12 verbs): the decision's provisional, **at-risk** add arm. Verbs span the canonicity spectrum.
- **intrans-motion** (12 verbs): a **plausible-but-unverified** alternative. Manner verb + directional PP adds translational motion; hypothesis phrased **generically** ("moved to a different place"), not goal-specific.

Per-verb **headroom = construction_affirm − control_affirm**. A verb has real headroom only if the construction licenses the entailment (high) AND the control does **not** already supply it (low). A control already at ceiling = the AANN default-coincidence trap → no headroom.

- **Indicators:** NLI (label 0 = entailment = affirm; **primary**) and forced-choice (YES = affirm; **robustness / instrument-fragility read**). Temperature 0, the 3-family behavioral panel ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C). 48 items × 2 instruments × 3 models = **288 calls**.
- Cost recorded as **API-billed `usage.cost`** via `experiments/lib/openrouter.py` (`billed_cost`). Pre-flight estimate ≈ $0.10–0.20.

## FROZEN reading rule (the headroom gate) — set before any data, NOT tunable after

A verb is **HEADROOM-CLEAN** if, in the panel aggregate (mean of the 3 models, **NLI primary**):

- construction licensing affirm **≥ 0.80** (at/near ceiling), **AND**
- control default affirm **≤ 0.40** (off ceiling — at/near the ~0.33 chance baseline for a 3-way YES/NO/CANT_TELL).

A **CONSTRUCTION DEMONSTRATES HEADROOM** if **≥ 4 of its 12 verbs** are headroom-clean in the panel aggregate **AND ≥ 1** such verb is headroom-clean in **≥ 2/3 models** individually (so a clean add arm can actually be assembled from surviving verbs, robust across the panel).

**Threshold rationale (principled, not tuned to a hoped result):** 0.80 ceiling mirrors the project's ratified "≥70% follow-construction" robustness language ([`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md)) tightened for a *licensing* arm; 0.40 floor ≈ "not above the 3-way chance baseline" as the operational meaning of *off ceiling*; ≥4/12 (one-third) as the minimum non-trivial clean subset from which an add arm could be drawn. These mirror the **provisional SHAPES** in the s132 feasibility page (illustrative 90% / 30% placeholders), fixed here to **concrete numbers against this frozen item set** as the s132 review's gap 2 requires.

## Pre-registered outcomes (all first-class; the falsify arm is LIVE)

- **Resultative passes, intrans-motion irrelevant** → the decision's provisional add arm has demonstrated headroom; prerequisite (1) discharged for resultative.
- **Resultative FAILS (controls mostly at ceiling)** → the degeneracy worry is **borne out**; resultative is not a clean add arm. If intrans-motion **passes**, that **names a cleaner add construction** (the prerequisite's explicit alternative). Both are reported as found.
- **Both fail** → no clean add arm among the two tested candidates on these items; prerequisite (1) **not** discharged; the conjecture's generalization line stays blocked, recorded as an honest null. No threshold relaxed, no verb re-binned after seeing outputs.

## Anti-cheat (binding)

- Items **frozen + sha256-hashed (`471a5940ba8f65ff`) and committed before the first probe call**; no item/verb added, dropped, or re-binned after.
- The reading rule above is **frozen before any data**; verdicts are read mechanically by `analyze.py`. No threshold tuned post-hoc.
- An **independent fresh-agent pre-run critic** reviews the frozen items + this PREREG and returns GO/NO-GO **before any spend**; a NO-GO **defers** the run rather than relaxing the bar.
- **Post-run**, an independent fresh agent recomputes every number from `raw/*.json` (separate from `analyze.py`).
- This calibration **ratifies nothing and freezes no operationalization decision**; it supplies the evidence the s132 review's blocker requires. Ratification of the operationalization decision remains a later session's independent adversarial-review pass.

## Known limits (stated before data)

- **Design-feasibility only.** A *pass* says a clean add arm *can be built*; it is **not** a test of the monotonicity conjecture and licenses no claim about add-vs-cancel.
- **Bare-transitive control is one control framing**, not the only conceivable one; a verb failing here fails *this* control, and the verdict is read per-verb so the construction's clean subset survives a few degenerate verbs.
- Small-N (12 verbs/construction), single run, panel-as-instrument, `internal-contrast-only` — a direction-of-feasibility signal, not a magnitude or a human comparison.
