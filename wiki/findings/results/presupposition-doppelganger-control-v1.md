---
type: result
id: presupposition-doppelganger-control-v1
title: "The presupposition corner BEATS a matched surface-cue doppelgänger (BEATS-DOPPELGANGER, pooled 3/3) — but the residual is keyed to the trigger WORD-FORM and surface-cue-reconstructable, so it does NOT beat the distributional shadow; the clean FLAT null did not obtain"
meaning-senses:
  - inferential
  - distributional
  - constructional
status: proposed
anchor: pending
contingent-on:
  - presupposition-doppelganger-internal-contrast-anchor
created: 2026-07-03
updated: 2026-07-03
links:
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: essay/presupposition-environment-gated
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Result: the presupposition doppelgänger (matched surface-cue) control v1

Program item **A1a** — the flagship's owed matched-surface-cue control for the presupposition corner
of [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md). It converts
the essay's *reading* ("presupposition sits at the shadow-saturated end — its within-model behavior is
reconstructable by follow-the-surface-cue") from a bet into a **measured** contrast. Run record:
[`experiments/runs/2026-07-03-presupposition-doppelganger/`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/PREREG.md),
manifest sha `4500fc5b…`. Ratified design gate:
[`decisions/resolved/presupposition-doppelganger-control-design`](../../decisions/resolved/presupposition-doppelganger-control-design.md)
(opened s172, ratified s173, RATIFY-WITH-NIT; the non-Anthropic vote dissented REJECT and was weighed
and rebutted).

## One-line finding — and the load-bearing asymmetry (read BEFORE citing)

The pre-registered verdict is **BEATS-DOPPELGANGER**: on all three models the presupposition trigger's
P-endorsement over the projecting frames (negation + question) exceeds the matched non-presupposing
doppelgänger's by a wide margin (pooled residual **+0.78 / +0.47 / +0.94**; robust across all nine S4
cutoffs). **So the clean FLAT null — the cleanly-licensed "shadow-saturated" prize the design named — did
NOT obtain: the doppelgänger does not endorse the content equally.**

**But BEATS is the UNDER-LICENSED outcome, and this is the whole point of the pre-run corrections B1/B2**
([`decisions/resolved/presupposition-doppelganger-control-design`](../../decisions/resolved/presupposition-doppelganger-control-design.md)).
A positive residual here does **NOT** establish "presupposition beats the distributional shadow" and does
**NOT** move the corner to the beater side. A **verb-sensitive surface-cue follower** — which any
distributional next-token learner is — reconstructs this residual, because the powered D1 doppelgängers
vary the **trigger word** (`realize`→`suspect`, `stopped`→`considered`), whose distributions differ. The
decisive disanalogy with the comparative-correlative beater
([`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md)): the CC
clears controls that reuse the **same words** and vary only the construction; these D1 controls vary the
word. So the honest reading is: **the panel's endorsement is keyed to the trigger word-form above bare
complement presence** — a lexical/constructional discrimination that is itself distributionally encoded —
**not** a residual over-and-above co-occurrence. It **does not fire the essay's first revision trigger**,
which requires "a residual a surface-cue account **cannot** reconstruct, held stably across frames and
contexts."

## Scope — LOAD-BEARING

**Within-model contrast only; no human comparison.** The signal is *the trigger leg endorses the content
more than the matched doppelgänger leg, within the same model* — not that the model matches any human
judgment. No human doppelgänger/projection baseline is claimed, measured, or needed. The result does not
certify that a model *represents* a presupposition/assertion split (endorsement under embedding is read
off forced-choice answers; text-consistency is not mechanism), and does not adjudicate the projection
problem. **Anchor is `anchor: pending`** on
[`decisions/open/presupposition-doppelganger-internal-contrast-anchor`](../../decisions/open/presupposition-doppelganger-internal-contrast-anchor.md)
(opened this session) → eventual `internal-contrast-only`, ratified only by an independent **later**
session (charter §12.3), structurally parallel to the three already-ratified sibling anchors
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md)
and siblings). **Not self-ratified here.**

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. Neutral system prompt that never
  mentions presupposition / projection / triggers / doppelgängers / the right answer.
- **Items** (project-authored, no external corpus). 22 base scenarios — **factive / aspectual / cleft
  6 each (powered)** + **definite 4 (exploratory, dropped from every verdict per S1)** — × 2 legs
  (trigger vs. D1 doppelgänger) × 4 frames (plain / negation / question / conditional) + 1 D2
  metalinguistic structure-defeat leg = **198 item-conditions/model, 594 calls**. Each item one forced
  choice — *"does it follow that: ⟨P⟩? YES / NO / UNCLEAR."* `endorsed` == parses to YES.
- **Powered, verdict-bearing residual N (S3, honest):** only the two projecting frames of the three
  powered families carry the residual → **72 residual-bearing conditions/model** (36 trigger + 36
  doppelgänger). NOT 198, NOT 128.
- **Cost.** **$0.1033 billed** (`usage.cost`-summed: claude $0.0606 / gpt $0.0185 / gemini $0.0242), 0
  missing cost, **0 unparsed** answers. Under the $2.50 single-run flag; UTC-2026-07-03 day total after
  this run well under $5.00. Pre-flight (6 calls, $0.0005) extrapolated in range.

## Numbers (from `results.json`; independently reproduced from raw)

**Per model — pooled over the three powered families** (rates over negation + question):

| model | trigger_project | doppel_project | **residual** | label |
|-------|-----------------|----------------|--------------|-------|
| A claude-sonnet-4.6 | 0.97 | 0.19 | **+0.78** | beats |
| B gpt-5.4-mini | 0.69 | 0.22 | **+0.47** | beats |
| C gemini-3.5-flash | 1.00 | 0.06 | **+0.94** | beats |

Verdict per the frozen map (SANITY 0.60 / RESID 0.30 / FLATBAND 0.15): **BEATS-DOPPELGANGER** (pooled
3/3). **S4 sensitivity:** BEATS in **all nine** RESID∈{0.25,0.30,0.35} × FLATBAND∈{0.10,0.15,0.20} cells
— the verdict is not a threshold artifact.

**Per family (PRIMARY, S2 — the families are heterogeneous control types):**

| family | A residual (trig/dop) | B residual (trig/dop) | C residual (trig/dop) | panel |
|--------|----------------------|-----------------------|-----------------------|-------|
| factive (`realize…`→`suspect…`) | +0.83 (0.92/0.08) | +0.58 (0.75/0.17) | +0.83 (1.00/0.17) | **BEATS 3/3** |
| aspectual (`stopped…`→`considered…`) | +1.00 (1.00/0.00) | +0.75 (0.75/0.00) | +1.00 (1.00/0.00) | **BEATS 3/3** |
| **cleft** (it-cleft→plain assertion) | +0.50 (1.00/0.50) | +0.08 (0.58/0.50) **control-FAILED** | +1.00 (1.00/0.00) | **BEATS 2/3** [N1] |
| definite* (exploratory) | +1.00 | +0.88 | +1.00 | *not in verdict* |

**The cleft family is the load-bearing wrinkle (B1's one exception).** It is the *only* powered leg that
holds the content words constant and varies only the construction — so a cleft residual is the one that
could speak (weakly) to a *construction-grain* shadow rather than a lexical one. And it is exactly here
that the signal is weakest and most model-dependent:

- **gpt-5.4-mini control-FAILS the cleft** (trigger_project 0.58 < 0.60): it does not reliably project
  the existential from `It wasn't X who Y-ed`. Its cleft residual is **+0.08 — essentially FLAT** (within
  the shadow-saturated band). So on the one model where we can look at a clean construction-grain
  control, the cleft leg is near-saturated (N1: the cleft panel therefore rests on 2/2).
- The cleft residual that *does* appear (claude +0.50, gemini +1.00) is **carried entirely by the
  NEGATION cell.** Reading the raw answers: under negation the plain-assertion doppelgänger correctly
  cancels the existential (`The deputy didn't authorize the transfer` → "someone authorized?" = NO), while
  the cleft keeps `who Y-ed` on the surface (`It wasn't X who Y-ed` → YES). Under the **question** frame
  the doppelgänger is **confounded**: claude and gpt answer YES to "someone authorized?" for the plain
  `Did the deputy authorize the transfer?` too, so the question frame does not discriminate. **The cleft
  residual is thus itself a negation-frame surface-cue difference** — precisely the kind B1 says a
  surface-cue account reconstructs.

**Descriptive (not verdict-bearing):**

- **D2 metalinguistic structure-defeat** (`d2_endorse` 0.00 / 0.06 / 0.00; `d2_residual` +0.97 / +0.64 /
  +1.00): when the trigger word-form is kept but the presupposition is defeated by a quotation/exercise
  framing, all three models **withhold** P. This shows the panel is not the *crudest* bare-complement
  follower — but it is fully consistent with a **frame- and verb-sensitive** surface-cue follower (the
  metalinguistic framing is itself a strong surface cue), and D2 does not compose with the four frames, so
  it cannot demonstrate the cross-frame stability the essay's trigger demands. Descriptive only.
- **plain-frame doppelgänger endorse** 0.33 (all three): in the plain frame the models endorse the
  doppelgänger's complement content a third of the time — a direct read on partial surface-following.
- **conditional_residual** +0.33 / +0.06 / +0.28 (descriptive; excluded from the primary per N2, grounded
  in [`result/presupposition-projection-v1`](presupposition-projection-v1.md)'s published conditional
  collapse). Dropping it *raised* trigger_project and made the positive easier — evidence the exclusion
  was not a positive-hunt (N2 confirmed directionally).

## Interpretation (calibrated)

- **What the data support.** The panel **discriminates the presupposition trigger from a matched
  non-presupposing doppelgänger** — robustly, across families and cutoffs. This rules out the *crudest*
  surface-cue follower (one keyed only to bare complement presence, which would have produced the flat
  null). The models' endorsement is **keyed to the trigger word-form** — factivity/aspect/cleft-structure
  above the shared complement material.
- **What the data do NOT support (the honest ceiling).** This is **not** "presupposition beats the
  distributional shadow." (i) For factive/aspectual the D1 control varies the **word**, so any residual is
  attributable to the words' different distributions — a verb-sensitive surface-cue account reconstructs
  it. (ii) The one construction-grain leg (cleft) gives **no clean cross-panel residual**: gpt is
  near-flat and control-fails, and the claude/gemini residual is carried by a negation-frame surface cue.
  (iii) The residual is not shown **stable across frames** (the question frame is confounded; the
  conditional collapses; D2 does not compose). So the essay's first **revision trigger does not fire**.
- **What the measurement changes for the shadow-depth placement.** The corner is **no longer a pure
  reading** — a matched control has now run. But it lands in the **under-licensed middle**, not at either
  clean pole: it is **not** the flat null the "shadow-saturated" placement's strongest form would predict
  (the doppelgänger *is* discriminated), and it is **not** a shadow-beater (the discrimination is
  word-form-keyed and surface-cue-reconstructable). The most honest re-statement of the placement: the
  presupposition corner is **shadow-saturated in the essay's precise sense** — *its residual is one a
  surface-cue account can reconstruct* — **but it is not behaviorally flat**; the trigger-vs-doppelgänger
  contrast is real and word-form-keyed. The corner stays a **marked reading**, now with a measured caveat,
  rather than moving to the beater side.

## Gates

- **Pre-run critic (independent fresh agent): GO** — every factive/aspectual/cleft doppelgänger validated
  as a genuine matched non-presupposing control (triggers presuppose P and survive negation; doppelgängers
  entail P in no frame); definite correctly quarantined from the verdict; scoring/thresholds/S4/N1
  faithful to the frozen spec; freeze guard armed, sha pinned; no leakage; cost bounded. No BLOCKER/
  SHOULD-FIX. One non-Anthropic vote (panel.B) converged GO-WITH-NIT (naturalness nits only).
- **Post-run verifier (independent fresh agent): REPRODUCED, 0 discrepancies** — pooled residuals
  (+0.778 / +0.472 / +0.944), every per-family cell, the gpt cleft control-fail (trigger_project 0.583 <
  0.60), all nine S4 cells, unparsed=0, missing-cost=0, and the re-summed billed cost ($0.1033) re-derived
  from `raw/*.json` with an independent parser/scorer. It independently confirmed the cleft
  question-frame confound and noted it **suppresses** the residual (inflates doppel_project), so it does
  not manufacture the BEATS verdict — but the cleft signal for claude/gpt is a **negation-only** effect,
  and the interpretation must not lean on the cleft question frame (honored above).

## What this feeds

- **Program A1a `[x]`** — the owed matched-surface-cue control is **run**; the presupposition corner of
  the shadow-depth table is now **measured**, not a pure reading.
- **[`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md)** — the first
  revision trigger **does not fire** (BEATS is under-licensed; no residual a surface-cue account cannot
  reconstruct). The essay's Honesty-box statement that the placement was a reading/bet is updated in-page
  to *reading with a measured caveat*: the corner is not flat, but its residual is surface-cue-
  reconstructable, so the shadow-saturated placement stands (weakened form).
- **[`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md)** — the presupposition corner
  row is updated from "reading/bet, control owed" to "reading, control RUN → BEATS-DOPPELGANGER
  (under-licensed; word-form-keyed; not a beater-side move)"; still **not** a measured shadow-beater and
  **not** a measured flat-null.
- Opens the honest follow-up the cleft wrinkle names: a **construction-grain-only** doppelgänger battery
  (cleft-family expansion, negation-only discriminating cell, controlling the question-frame confound)
  is the one leg that could in principle reach a residual not reducible to a lexical distribution — still
  bounded by B1 (a cleft residual is a negation-frame surface cue), but the least-confounded next probe.
