---
type: result
id: aann-quant-temporal-inversion-v1
title: "AANN quant×temporal inversion: class or lexical? — NULL. The located inversion does not reproduce on a widened quantity-modifier set; it was an inventory artifact of the thin held-out sample (and NOT the scant/mere small-quantity items the OQ hypothesized)"
meaning-senses:
  - constructional
  - human-comparison
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: refines
    target: result/aann-temporal-why-reanalysis
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: result/aann-temporal-heldout-v2b
  - rel: depends-on
    target: conjecture/aann-construction
---

# Result — AANN quant×temporal inversion is an inventory artifact (VERDICT: NULL)

> **Status: proposed (a reading-bearing NULL; the reading is "inventory artifact, not a quant-class
> productivity hole").** Froze + ran s189 (2026-07-06) under the ratified design
> [`design/aann-quant-temporal-inversion-v1`](../../../experiments/designs/aann-quant-temporal-inversion-v1.md)
> and decision [`decisions/resolved/aann-quant-temporal-inversion-design`](../../decisions/resolved/aann-quant-temporal-inversion-design.md)
> (ADOPT-WITH-CHANGES: Q1-C human-N-gated / **Q2-B monotone-primary** / Q3-A). Freeze-stage pre-run
> critic **GO** (anti-cheat PASS); non-Anthropic vote NO-GO weighed and rebutted; independent post-run
> recompute-from-raw verifier reproduced every figure. **Anchor:** Arm 1 (Mahowald-attested quant
> modifiers) `anchors:` → [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md);
> Arm 2 (widened) internal-contrast. The overall result makes a within-model four-class contrast (the
> NULL is a within-model fact), so the front-matter carries `internal-contrast-only`; Arm 1's human leg
> is the anchored secondary. **$0.1815 billed** (972 calls, 0 missing).

## The question and the verdict

The one panel-wide model-vs-human AANN inversion cell — **quantity adjectives × temporal nouns** ("a
scant three days"), where humans rate acceptability **highest** of four adjective classes and every panel
model rated it **lowest** ([`result/aann-temporal-why-reanalysis`](aann-temporal-why-reanalysis.md), H4) —
was located on a **thin, project-assigned held-out** quant set (10 adjectives on 5 nouns). Is the
inversion the **whole quantity-adjective class** or **a few lexical items**
([`open-question/aann-quant-temporal-inversion`](../open-questions/aann-quant-temporal-inversion.md))?

**VERDICT: NULL, panel-wide (3/3 Tier-0-passing models).** On a widened, source-documented quantity-
modifier set (**K=20**: 10 Mahowald-attested + 5 genuinely-new + 5 v2b-carryover, small- and large-
polarity), each rated on an identical balanced temporal frame, the **quant cell is no longer the lowest
of the four adjective classes for any model** — so, by the pre-registered NULL-first precedence, the
located inversion **does not reproduce**. It was an **artifact of the thin held-out quant inventory**, not
a property of the quantity class. The pre-registered bet ([`predictions.md`](../../predictions.md)) that
the inversion would survive widening (not-NULL, CLASS-or-MIXED) is a **loss**, written as one.

## The four-class comparison (models this occasion; humans committed) — quant is 2nd, not lowest

| adjective class (× temporal) | human mean | claude (A) | gpt (B) | gemini (C) |
|---|---|---|---|---|
| ambig | 8.25 | **65.8 (highest)** | **65.4 (highest)** | **94.8 (highest)** |
| **quant (widened K=20)** | **8.45 (highest)** | **56.7 (2nd)** | **52.0 (2nd)** | **81.7 (2nd)** |
| pos | 8.02 | 49.8 | 38.9 | 69.3 |
| neg | 7.57 | 45.3 | 22.6 | 79.0 |

*(Model 0–100 class means over this occasion's items; human means committed
`human_class_means.csv`, 1–10. Tier-0 manipulation check passed 3/3: A 21/24, B 21/24, C 23/24 ≥ 20.)*
Compared with the re-analysis's held-out table (quant **lowest** at 43.0 / 30.1 / 68.8), the widened
quant cell **rises to 2nd of four** for every model — above pos and neg, below only ambig. The models'
four-class *ordering* still differs from the human one (models put **ambig** highest, humans put
**quant** highest), but the specific "quant lowest / inverts" cell **dissolves**.

## The monotone per-modifier read (Q2-B primary) — no inversion

Per quant modifier *j* and model *m*: `A_m(j)` = mean 0–100 over *j*'s 10 items; `B_m^min` = min over
{ambig, pos, neg} of the model's non-quant temporal class mean; `d_m(j) = A_m(j) − B_m^min` (negative =
inverts). The distribution of `{d_m(j)}` sits **well above zero** for all three models:

| | median d | Q3 d | inversion count (p = fraction with d<0) |
|---|---|---|---|
| claude (A) | **+15.6** | +21.6 | 0.20 |
| gpt (B) | **+38.1** | +40.1 | 0.10 |
| gemini (C) | **+25.0** | +25.9 | 0.20 |

The **typical** quantity modifier is nowhere near inverting; only 2–4 of 20 sit below the lowest
non-quant baseline. (Since the NULL test — quant cell not lowest — fires first, the CLASS/LEXICAL/MIXED
shape read is moot; it is reported for completeness and, consistent with NULL, is not CLASS.)

## Which modifiers *do* invert — the legible lexical structure of the artifact

The handful of inverting modifiers (negative `d`) are the **low-frequency, large-magnitude,
semantically-marginal-on-temporal** items — precisely the kind the thin held-out sample over-weighted:

- **towering** inverts **3/3** (d = −21.2 / −14.8 / −50.2); **ample** 2/3 (A, C); **colossal** 1/3 (A);
  **skimpy** 2/3 (B, C); **substantial** 1/3 (C); **hefty** 1/3 (A). ("a towering three days", "a
  colossal three days" are odd; these are Zipf 3.2–3.7.)
- **Every natural, higher-frequency quantity modifier sits well above baseline (does NOT invert):**
  mere, extra, good, full, whole, solid, staggering, whopping, record-setting, measly, paltry, scant —
  all strongly positive across all three models.

**The OQ's own hypothesis is falsified in passing.** The re-analysis and the OQ named *scant/mere/measly/
paltry* — the **small-quantity "only X"** items — as the candidate carriers. They are **not**: *scant*
(d = +21.4 / +39.6 / +22.8), *mere* (+25.1 / +45.0 / +26.2), *measly*, *paltry* all sit high above
baseline. The small-vs-large polarity split shows **no inversion signature** (small-polarity median d is
as positive as large, or more). What inverts is **lexical frequency / oddness**, not quantity-polarity:
the per-modifier `d` correlates **positively** with Zipf frequency (Spearman +0.32 / +0.28 / +0.37 —
lower-frequency modifiers have lower `d`). So *within* the widened quant set, the residual inversion
tracks **frequency**, exactly the artifact H3 ruled out *at the class level* but which re-emerges
*at the item level* once the inventory is widened.

## Arm 1 — the anchored human comparison confirms the dissolution on Mahowald's OWN set

Over the 10 **Mahowald-attested** quant modifiers (per-modifier gradient comparison, S3 — not
item-matched; human means over 11–24 singly-rated items each, N=193 total, so the 10-point rank
correlation is **underpowered/noisy**):

- **Number of Mahowald quant modifiers showing the model-low/human-high inversion: A 1/10 (hefty), B
  0/10, C 1/10 (substantial).** On Mahowald's own attested quant set, essentially **no** modifier
  reproduces the inversion — the strongest, fully-anchored form of the null.
- Model-vs-human per-modifier Spearman: A **+0.55**, B **+0.60**, C **+0.81** — positive; the models
  rank-track the human per-modifier gradient *among* the quant items (the direction is right; it is the
  cross-class "quant lowest" claim that fails).

## Robustness

- **Template-invariant.** Dropping the "tourish" template-2 items (Mahowald's own spelling — the freeze
  finding is that his raters saw "tourish", so it is kept; the exclusion is the sensitivity view) yields
  **NULL for all three models** — the null is not a template artifact.
- **Tier-0 clean** 3/3 this occasion; the instrument (`probe.py`) is byte-identical to the v2b graded-
  acceptability instrument (`diff` = the `ABORT_USD` safety constant only); the §6 verdict code is new,
  self-tested to reach CLASS/LEXICAL/MIXED/NULL before any call.
- **Verifier REPRODUCED** every headline figure from raw (independent recompute; see
  [`VERIFIER-REPORT.md`](../../../experiments/runs/2026-07-06-aann-quant-temporal-inversion/VERIFIER-REPORT.md)).

## What this refines

- [`result/aann-temporal-why-reanalysis`](aann-temporal-why-reanalysis.md) **H4**: the *location* of the
  inversion (in the held-out quant×temporal cell) stands as a description of that frozen sample, but its
  *interpretation* is now scoped — the negative sign was carried by the specific low-frequency large-
  magnitude held-out adjectives (*towering, colossal, sizable, lavish, respectable, ample*), not by the
  quantity class. The "clean, localized, panel-wide inversion" does **not** generalize.
- [`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md): the claim's noted
  **temporal-stratum negative** (v2b) is now understood as **inventory-specific**, not a class property —
  it does not widen the claim's scope, and if anything narrows the temporal caveat to "sensitive to
  low-frequency marginal adjectives," not "quantity adjectives invert."
- [`open-question/aann-quant-temporal-inversion`](../open-questions/aann-quant-temporal-inversion.md):
  **answered** — the class-vs-lexical question resolves to **neither a clean class effect nor the
  hypothesized scant/mere lexical effect**, but a **frequency/inventory artifact** dissolving the cell
  once the modifier set is widened.

## Scope and limits

- Panel n=3, single occasion (one date). The direction is uniform (3/3 NULL) and template-robust, but
  this is one instrument on one panel.
- The reference arm uses ~4 non-quant adjectives/class on a partial num/template rotation (a **structural**
  four-class reproduction, N1 — not the committed full-class cells); only class-level means feed B_m.
- Arm 1's per-modifier human means are noisy (11–24 singly-rated items/modifier); the anchored Spearman is
  reported as directional, not a powered magnitude.
- The verdict is a within-model four-class contrast plus an anchored per-modifier gradient; it makes **no**
  claim that people would (or would not) rate any widened item a particular way — new widened items carry
  no human rating and none was invented (Arm 2 internal-contrast).
- This does not touch the AANN form-ceiling (Tier-0) or the inferential line; it sharpens exactly one
  graded cell.

## Provenance

Frozen instrument reused from [`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md); human
gradient [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
(Exp-2, MTurk 1–10). Run: `experiments/runs/2026-07-06-aann-quant-temporal-inversion/` (`prep.py`,
`stimuli.json`, `PREREG.md`, `analyze.py`, `probe.py`, `raw/`, `results.json`, `REVIEW-freeze-s189.md`,
`VERIFIER-REPORT.md`). Billed $0.1815 (A $0.1130 / B $0.0264 / C $0.0421; 0 missing), UTC 2026-07-06.
