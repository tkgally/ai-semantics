---
type: result
id: third-construction-headroom-harvest-v1
title: Caused-motion (add-direction) third-construction headroom harvest — no off-ceiling headroom buildable; Option C realized ("AANN-specific so far" stays terminal on current resources)
meaning-senses:
  - constructional
  - inferential
  - distributional
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: depends-on
    target: design/third-construction-preference-commitment-v1
  - rel: depends-on
    target: conjecture/preference-commitment-generality
  - rel: depends-on
    target: result/argument-structure-coercion-v2
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: contradicts
    target: conjecture/preference-commitment-generality
  - rel: depends-on
    target: concept/coercion
---

# Result: the caused-motion headroom harvest fails the gate — the add-direction third-construction test is not buildable; Option C is realized

> **Scope caveat (binding, read first — Carry-forward 1 of the ratified decision).** This is a fair but
> **narrower** point in construction-space — *add-direction* instrument-divergence — **not** the AANN
> unification shape. A null/Option-C outcome here does **not** settle the cancel-direction / unification
> *shape* question (the Option-B route stays in reserve for a future session).
>
> **Anchor: `internal-contrast-only`.** Every number below is a **within-model** affirm-rate measurement
> used to decide whether off-ceiling headroom exists. It makes **no human-comparison claim** and cites
> no human gradient (the terminal `internal-contrast-only` state ratified in
> [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)).
> No human number is invented; CxNLI is **not** cited for any AANN-uniqueness claim.

## One-line finding

Built and ran the **pre-headline headroom/harvest arm** (design §5, G1–G4) of the frozen caused-motion
preference/commitment design. **The headroom gate FAILS: only 1 of 3 models clears the ≤ 0.50 hard
ceiling** on baseline marginal-construction affirm (claude 0.625 FAIL, gpt-5.4-mini 0.479 PASS, gemini
0.552 FAIL; G4 requires ≥ 2/3). Per the ratified binding fallback (Carry-forward 2), the design **does
not run the headline; it routes to Option C** — *"AANN-specific so far"* stays the terminal close on
current resources. **No retuning, no second harvest.**

The harvest also explains *why*, and the explanation is the substance of the finding: the marginal verb
pool is **bimodal, not a contestable middle band**. Low-propulsion physical verbs read **at ceiling**
(the construction coerces causal-motion verb-independently); cognition/stative verbs read **at floor**
(the items are *anomalous*, not contestable). There is essentially nothing in between — so no usable
off-ceiling band exists from which to build a clean double contrast.

## What ran (design §5 harvest arm)

- **Run:** `experiments/runs/2026-06-15-third-construction-preference-commitment-v1/` (prep.py freezes the
  candidate pool, sha256 `79aa83e4c2a79a53`; harvest.py runs the baseline arm + evaluates G1–G4).
- **Authorization:** an **independent pre-run critic** (fresh agent, this session) rendered
  **GO-FOR-HARVEST** — numbers-integrity PASS, all six inherited guardrails present, anti-cheat PASS,
  freeze discipline sound — authorizing the **harvest arm only** (~288–360 calls) and **gating the
  headline** on the harvest clearing G2 for ≥ 2/3 models, with a FAIL routing to Option C.
- **Candidate pool (frozen pre-run):** 24 marginal verbs (12 **M1** cognition/stative + 12 **M2**
  low-propulsion physical) + 6 **clean** propulsion reference verbs (reused verbatim from
  [`result/caused-motion-near-miss-v2c`](caused-motion-near-miss-v2c.md): sneeze/cough/blow/puff/huff/fan),
  each paired with 2 rotating light-inanimate objects → 60 items.
- **Instruments (both well-formed frames):** paraphrase forced-choice (affirm = chose the construction
  reading "*&lt;subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move*") + NLI entailment (affirm =
  entailment, label 0). Temperature 0; gemini `reasoning: {effort: minimal}`.
- **Calls:** 360 finding-bearing (60 items × 2 instruments × 3 models), **0 missing-cost, 0 missing
  value**. (Cost + a disclosed duplicate-run note in §Spend.)

## The gate (design §5) — verdict FAIL → Option C

Per-model baseline affirm on the **marginal** construction arm (pooled over both instruments, n = 96/model)
and the **clean** reference arm (n = 24/model). Recomputed independently from `raw/*.json` via a separate
code path (numbers identical to `harvest.py`):

| model | marginal affirm (G1) | G2 (≤ 0.50 ceiling) | clean affirm (G3) | G3 (≥ 0.85 floor) |
|---|---|---|---|---|
| claude-sonnet-4.6 (A) | **0.625** | **FAIL** | 1.000 | PASS |
| gpt-5.4-mini (B) | **0.479** | PASS | 0.917 | PASS |
| gemini-3.5-flash (C) | **0.552** | **FAIL** | 1.000 | PASS |

**G4 (whole-design gate): 1 / 3 models clear G2 → FAIL.** The headroom precondition is not met. Per
**Carry-forward 2** of [`decisions/resolved/aann-uniqueness-third-construction`](../../decisions/resolved/aann-uniqueness-third-construction.md):
the design must not run the headline and routes to **Option C**. The clean arm clears G3 in all three
models (≥ 0.917), confirming the construction is *available* and that marginality — not a broken
instrument — is what depresses the marginal baseline.

## Why the gate failed: the marginal pool is bimodal, not a contestable band

The aggregate G1 (0.48–0.63) is **not** a genuine "licensed-but-contestable" middle. It is the average of
a floor and a ceiling. Pooled across all models and both instruments (n = 144 each):

| marginality dimension | example | pooled affirm | reading |
|---|---|---|---|
| **M1 cognition / stative** | *Maria knew the feather off the table.* | **0.174** | off-ceiling, but the item is **anomalous** — models reject it |
| **M2 low-propulsion physical** | *Maria blinked the feather off the table.* | **0.931** | **at ceiling** — the construction coerces causal-motion verb-independently |

Per-model × dimension × instrument (affirm rate):

| model | M1 FC | M1 NLI | M2 FC | M2 NLI |
|---|---|---|---|---|
| claude (A) | 0.29 | 0.21 | **1.00** | **1.00** |
| gpt (B) | 0.17 | 0.00 | **1.00** | 0.75 |
| gemini (C) | 0.29 | 0.08 | **0.88** | **0.96** |

Every M2 cell is at or near ceiling; every M1 cell is at or near floor. The split is robust across
instruments and models. Per-verb, the ordering is starkly bimodal: all 12 M2 verbs affirm 0.83–1.00
(nod/giggle/yawn/sigh at 1.00), while 11 of 12 M1 verbs affirm ≤ 0.50 (notice/perceive/recognize at 0.00).

**The interpretation.** The caused-motion construction, in the add direction, behaves like the
*way*-construction the design itself flagged as un-depressable
([`result/argument-structure-coercion-v2`](argument-structure-coercion-v2.md)): for **any verb that is
even minimally physically plausible** (a blink, a hum, a nod), the construction *adds* the
causation-of-motion entailment at ceiling — the construction does the work verb-independently. The only
way to push the baseline off-ceiling is to use a **cognition/stative** verb, which does not depress a
*contestable* causal reading so much as produce an **anomalous** sentence the models reject outright.

This corrects the design's load-bearing hypothesis. The design inferred a usable middle band from the v2
`resist` arm's 0–70% caused-motion affirm — but that 0–70% was driven by **cognition** verbs (M1), the
anomalous floor, **not** by low-propulsion physical verbs. This harvest measured the physical
low-propulsion class (M2) directly for the first time and found it **at ceiling**, not in a middle band.
So the headroom the design hoped to engineer **does not exist** in the add direction: there is no class of
caused-motion verbs that is both *grammatically usable in the lexical-cue control frame* (which needs an
intransitive-capable verb — M2 qualifies, M1 does not) **and** *off-ceiling in a contestable way*. M2 is
usable but at ceiling; M1 is off-ceiling but anomalous and cannot carry the coordinated-*and* /
displaced control frames cleanly. The two requirements are, on these resources, mutually exclusive.

## Bearing on the conjecture and the claim

- [`conjecture/preference-commitment-generality`](../conjectures/preference-commitment-generality.md)
  stays **tested → not confirmed**. This is its **second** failed generalization attempt: the conative
  (cancel-direction) was **INCONCLUSIVE** (the bare-*at* lexical cue absorbed the preference shift), and
  the caused-motion (add-direction) is now **Option-C / no buildable headroom**. Neither *falsifies* the
  conjecture (a headroom-fail "neither confirms nor falsifies and routes to the fallback," per the
  conjecture's own verdict map), but the generality bet is now **un-instanced in both inference
  directions** on current in-repo resources. The `contradicts` link records the evidential drift: the
  add-direction generality instance fails to materialize, which makes the unconditional generality bet
  less likely without falsifying it.
- [`claim/preference-commitment-dissociation-aann-specific`](../claims/preference-commitment-dissociation-aann-specific.md)
  stays `supported` and calibrated to **"AANN-specific so far."** Per the decision, Option C does **not**
  strengthen it to AANN-*uniqueness* — it records that a *fair, clean* third-construction test is not
  buildable from the in-repo anchored add-direction constructions without engineering that reintroduces
  the very ceiling / anomaly artifacts the v3 and conative results exposed. "So far" remains the honest
  ceiling on the claim.
- **A small positive byproduct for the theory of add-direction coercion.** The harvest is the first
  in-repo measurement of caused-motion affirm on **low-propulsion physical** verbs (as opposed to clean
  propulsion or cognition resisters). It shows the add-direction coercion is **verb-independent across
  the whole physically-plausible range** — strengthening the
  [`concept/coercion`](../../base/concepts/coercion.md) observation that the add direction is the
  "construction does the work" regime, in contrast to the cancel direction where the lexical default
  competes. (Internal-contrast-only; within-model.)

## Honest limits

- **One add-direction construction, on three decoders.** Caused-motion was the *best* add-direction lever
  in the repo (the v2 `resist` asymmetry); *way* is worse (verb-independent at 70–100%). That caused-motion
  has no buildable headroom does not prove *no* add-direction construction could — only that the in-repo
  anchored ones cannot, on these resources.
- **The bimodality could be probed further** (e.g. a graded propulsion-strength manipulation between the
  M1 anomaly floor and the M2 physical ceiling), but doing so would be **engineering after seeing the
  result** — exactly the operationalization-gate trap the protocol forbids. If a future session wants it,
  it must surface a fresh decision, not retune this design.
- **Not a falsification.** Per the symmetric verdict map, a headroom-fail is **inconclusive for this
  instance**, not a counter-instance. The conjecture's conceptual "two constructs" point survives
  un-instanced in the add direction.

## Spend

**$0.0805 billed** for one full 360-call harvest (`usage.cost`-summed, 0 missing). **Disclosed
duplicate run:** two full harvest invocations executed (a first launch whose wrapper `tee` errored but
whose Python in fact completed, and a relaunch — the two appear to have overlapped, judging by the raw-file
timestamps) — the cost-log carries two identical `$0.0805` entries, so **actual billed ≈ $0.161** (~720
API calls; only one 360-record set is saved). The scientific result is unaffected (the saved 360 records
recompute to identical numbers via a separate code path, 0 missing-cost).
Process lesson recorded: do not relaunch a probe whose first invocation may have run despite a wrapper
error — check `raw/` first. ABORT_USD = 0.30 (per invocation) never approached. **Day total 2026-06-15
(sessions 12–13 + this) ≈ $0.26 of $5.00.**
