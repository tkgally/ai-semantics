---
id: aann-quant-temporal-inversion-design
title: "AANN quant×temporal inversion probe — anchor scope (anchored-narrow vs wide-unanchored vs hybrid), the class-vs-lexical scoring threshold, and the non-quant reference baseline that defines 'inversion'"
status: open
opened: 2026-07-06
opened-by: session-188
contingent-artifacts:
  - design/aann-quant-temporal-inversion-v1
resolved:
resolved-by:
---

# Decision: the value-laden gates of the quant×temporal inversion widening probe

## Why this is owed

[`open-question/aann-quant-temporal-inversion`](../../findings/open-questions/aann-quant-temporal-inversion.md)
asks whether the one panel-wide model-vs-human AANN inversion cell — **quantity adjectives × temporal
nouns** ("a scant three days"), humans-highest / models-lowest
([`result/aann-temporal-why-reanalysis`](../../findings/results/aann-temporal-why-reanalysis.md), H4) —
is the **whole quantity-adjective class** or **a few lexical items**. The OQ sketches the probe but
freezes nothing; the design [`design/aann-quant-temporal-inversion-v1`](../../../experiments/designs/aann-quant-temporal-inversion-v1.md)
(landed this session) turns it into a runnable probe — and doing so forces choices that **are**
value-laden. The OQ names the sharpest one itself:

> "a widened probe either (a) restricts to Mahowald-attested quant×temporal items (fully anchored, but
> limited to the existing inventory — which may not be wide enough to separate class from item), or (b)
> authors new items and reads those as `internal-contrast-only` unless a human rating is obtained. This
> trade-off — anchored-but-narrow vs wide-but-partly-unanchored — is the operationalization choice a real
> design session would freeze."
> ([`open-question/aann-quant-temporal-inversion`](../../findings/open-questions/aann-quant-temporal-inversion.md),
> *Human-anchor status*)

Nothing here changes any finding; it fixes the **yardstick** for a probe that has **not run** and
**spends nothing** this session. Ratifying is eligible from **the next session** (never the opening
session), per [`PROJECT.md`](../../../PROJECT.md) §12.3: independent adversarial review + one non-Anthropic
panel vote; Tom's standing override outranks.

## Gate Q1 — anchor scope

The load-bearing subtlety (verified in-repo): the located inversion compares the **v2b held-out** quant
adjectives (project-assigned: *ample, lavish, negligible, respectable, skimpy, towering, colossal,
modest, scant, sizable* — no human rating) against Mahowald's **anchored** quant-class human mean (8.45),
whose adjectives are a **different** set (*mere, staggering, whopping, hefty, paltry, meager, extra,
measly, substantial, record-setting*). Items Mahowald actually rated carry a genuine human-comparison;
items beyond his set do not. Options:

- **A — anchored-but-narrow.** Restrict the probe to **Mahowald-attested** quant×temporal items (his 10
  quant adjectives × temporal nouns), scored item-matched against `adjexp_turk.csv`. **Fully
  human-anchored** (`anchors:` → [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)),
  and a *stronger* human comparison than v2b's held-out gradient-replication. **But** 10 modifiers may be
  **too thin to separate class from item**, and it cannot test the OQ's core ask (widen *beyond* the thin
  inventory).
- **B — wide-but-partly-unanchored.** Author a wide modifier set (Mahowald's + new), read the whole thing
  as **`internal-contrast-only`** (within-model, against a non-quant baseline). **Wide enough** to
  separate class from item, needs no anchor obligation — **but** discards the genuine human-comparison the
  attested items would supply, and answers a *weaker* question (a within-model contrast) than the OQ's
  human-comparison framing invites, given a real human anchor is in-repo.
- **C — HYBRID (provisional default).** An **anchored Mahowald core** (Arm 1: his own quant×temporal
  items, carrying the item-matched human-comparison claim, `anchors:` → the resource) **plus** a **widened
  internal-contrast extension** (Arm 2: beyond-Mahowald modifiers, no human claim), **reported
  separately**. The two arms answer complementary halves: Arm 1 asks whether the inversion holds across
  Mahowald's *own* attested set (fully anchored, but ~10 modifiers); Arm 2 widens the modifier count to
  resolve class-vs-item robustly (internal-contrast on the new items). Each arm states its evidential type
  and anchor status at exactly its strength; no human rating is invented for Arm 2.

**Why C is the reasoned default.** The trade-off in A-vs-B is a false dilemma: the anchored core and the
widened extension are **not mutually exclusive** — they touch disjoint modifier sets and can share one
frozen occasion. C keeps the human-comparison claim honest and *maximal* where a human rating actually
exists (Arm 1, item-matched), while paying the internal-contrast honesty tax only where it must (Arm 2).
It matches the project's blessed hybrid pattern (a human-anchored arm + an internal-contrast arm reported
separately; cf. the AANN gradient line's anchored + held-out split, and the terminal
`internal-contrast-only` state for arms making no human claim). The **cost** is small — the whole battery
is ~660 calls, ≈ $0.10–0.20 (design §7) — so C's extra arm is not a budget reason to prefer A or B. The
one caution C must carry (a freeze-time condition, not a blocker): the two arms are **reported
separately** and the widened Arm 2 is **never** presented as a human comparison; senselint anchor
discipline is satisfied by Arm 1's `anchors:` link, with Arm 2's items explicitly internal-contrast.

## Gate Q2 — the class-vs-lexical scoring threshold

How is CLASS vs LEXICAL decided **in advance**? The design's per-modifier indicator (frozen before any
call): modifier *j* **inverts** for model *m* iff `A_m(j) < B_m` (its mean acceptability is below the
model's non-quant temporal baseline); `p_m` = fraction of the K ≈ 20 quant modifiers that invert.
Options for the cut:

- **A (provisional default) — a broad-vs-few count with a bottom-drop confirmation, ≥ 2/3 panel.**
  **CLASS** iff `p_m ≥ 0.70` on ≥ 2/3 Tier-0-passing models; **LEXICAL** iff `p_m ≤ 0.30` **and** dropping
  the bottom-3 modifiers lifts the pooled quant-cell mean to ≥ B_m on ≥ 2/3 models; **MIXED/SUBTYPE**
  otherwise (or when the inverters are predominantly one quantity-polarity subtype). The **bottom-drop**
  clause is what makes "a few items" *operational* — a lexical effect is precisely one that a handful of
  modifiers carry. The **NULL** (widened quant cell no longer lowest of the four classes for ≥ 2/3) is a
  first-class, pre-named outcome.
- **B — a continuous per-modifier dispersion read** (e.g. the spread of `A_m(j) − B_m` across modifiers,
  class = uniformly-below, lexical = one long left tail). More information, but harder to pre-commit to a
  verdict and more sensitive to K and to per-modifier item noise.
- **C — an anchored-only threshold** (decide class-vs-lexical purely on Arm 1's Mahowald modifiers with
  human means). Cleanest anchoring, but couples the threshold to Q1 = A and to ~10 modifiers.

**Why A is the reasoned default.** It is a **pre-committed, threshold-first** rule (X = 0.70 / Y = 0.30,
≥ 2/3) with a bottom-drop clause that directly instantiates "a few items," and it names the null and the
subtype outcome as first-class — the anti-cheat posture PROTOCOL §B requires (no tuning the indicator
after seeing which modifiers win). X and Y are **surfaced as the value-laden numbers they are**: a
reviewer may tighten them (e.g. 0.75 / 0.25) but not loosen them post hoc, and the modifier list, K, and
subtype labels are frozen with the item set. The 0.70/0.30 band leaves a deliberate MIXED/SUBTYPE middle
rather than forcing a binary — honest about the graded reality the re-analysis already saw (the inversion
"recurs across the inventory" but with per-noun structure).

## Gate Q3 — the non-quant reference baseline that *defines* "inversion" (the further freeze choice)

`B_m` — the non-quant temporal baseline the quant cell must sit **below** to count as inverting — is
itself a value-laden choice, because it fixes *what the quant cell is measured against*. Options:

- **A (provisional default) — fresh Mahowald-own ambig/pos/neg temporal reference items on the SAME
  occasion.** ~4 adjectives × 3 classes × ~3 items, anchored, rated in the same run as the quant arm. Puts
  the four-class comparison on one comparable occasion, reproduces the re-analysis table directly, and
  avoids cross-run scale drift.
- **B — reuse v2b's frozen non-quant temporal ratings as B_m.** $0 for the baseline, but mixes two
  occasions/scales (a model's 0–100 calibration can drift between runs), weakening the within-occasion
  contrast.
- **C — a fixed absolute cut** (e.g. the quant cell below the model's global temporal mean). Simplest, but
  discards the per-class structure that *is* the finding (quant below *all three* non-quant classes).

**Why A is the reasoned default.** The inversion is intrinsically a **within-occasion, between-class**
contrast (quant lowest among four classes for models, highest for humans); measuring the reference in the
same run removes calibration drift as a confound and makes the four-class table an apples-to-apples
reproduction. The added cost is ~36 items (~108 calls, cents). Its one condition: the reference adjectives
are frozen with the item set, not chosen to make the quant cell look low.

## Further freeze choices (folded, not separate gates)

- **Modifier-set anti-cheat.** The K ≈ 20 modifier list is **frozen before any call** by a pre-declared
  inclusion rule (Mahowald's quant set + the OQ/handoff-named additions), **not** curated after seeing
  which invert. Recorded here so a later curation cannot masquerade as design.
- **Subtype as a pre-registered descriptive stratum.** The small-quantity vs large-quantity polarity split
  is declared **descriptive-secondary** (it can surface a SUBTYPE reading) and is **never** promoted to
  the primary verdict post hoc.

## Provisional defaults, together

**Q1-C** (hybrid: anchored Mahowald core + widened internal-contrast extension, reported separately) ·
**Q2-A** (broad-vs-few count `p_m ≥ 0.70` class / `≤ 0.30` + bottom-drop lexical, ≥ 2/3, MIXED/SUBTYPE
middle, NULL first-class) · **Q3-A** (fresh Mahowald-own non-quant reference on the same occasion). These
cohere: Q1-C supplies both an anchored per-modifier human comparison (Arm 1) and a wide enough modifier
count for Q2-A's count-based verdict (Arm 2); Q3-A gives Q2-A its within-occasion baseline; and the
anti-cheat freeze of the modifier list, K, thresholds, and reference set binds all three.

## Design-review inputs the ratification must weigh (added s188)

The design was reviewed s188 by a fresh-agent pre-run critic (**GO-WITH-CONDITIONS**; no fabrication —
every cited figure verified) + a decorrelated non-Anthropic vote (**NO-GO**, convergent in substance) —
full record in [`experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md`](../../../experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md).
Both bear directly on these gates:

- **Q1-C — adopt, but condition on an S1 human-N feasibility gate.** Arm 1's per-modifier human means
  depend on a currently-gitignored file (`adjexp_turk.csv`; only class-level means are committed). If
  per-modifier rating-N is thin, Q1-C degrades in practice to "class-level anchor + widened
  internal-contrast" — closer to Option B. Ratify C **with** the S1/S2/S3 conditions written in.
- **Q2 — both reviewers judge the 0.70/0.30 count + bottom-3-drop wording arbitrary/unstable** and push
  toward a tighter, more **monotone** primary criterion (i.e. Option **B**, the continuous per-modifier
  dispersion read, as primary — with the count secondary/descriptive). Weigh Q2-B vs Q2-A. The verdict map
  also needs a frozen **NULL-vs-CLASS/LEXICAL precedence** rule (critic B2) and an inversion indicator
  matched to "below **all three** non-quant cells," not the pooled mean (critic S4).
- **Q3-A — adopt (right call);** carry the N1 clarification (a structural, not same-cell, four-class
  reproduction) and the S2 tourist/tourish fix onto the anchored reference items.
- **Two freeze choices to surface as gates:** per-modifier noun/numeral balance (critic B1) and
  tourist-vs-tourish on anchored items (critic S2).

None of this changes a finding; it sharpens the yardstick the ratification fixes.

## Ratification status (OPEN — not ratifiable this session)

`resolved-by:` is **blank**. This decision is **opened this session (s188)** and, per
[`PROJECT.md`](../../../PROJECT.md) §12.3 and [`PROTOCOL.md`](../../../PROTOCOL.md) §2, is **eligible for
autonomous cross-session adversarial ratification from the next session (s189+)** — never in the session
that opened it. To ratify: a fresh adversarial-review agent (not this design's author) reads the decision,
its options, the provisional defaults, and the contingent design, returns a verdict with written
rationale, **decorrelated by one non-Anthropic panel vote**; then applies it (move to
`wiki/decisions/resolved/`, set `resolved-by: autonomous (adversarial review)`, promote/scope the design).
Ratification fixes the **yardstick, never the result**; the null and the inverted/subtype outcomes stay
first-class. Tom's standing override outranks any autonomous ratification.

## What ratification unblocks

Fix Q1–Q3 → freeze `prep.py` (modifier list, K, reference set, seed, Zipf audit, per-modifier human-mean
inclusion threshold, subtype labels) + `PREREG` (the §6 statistics/thresholds) → independent pre-run
critic + one non-Anthropic vote → run the reused v2b instrument on the panel (~660 calls, ≈ $0.10–0.20) →
post-run recompute-from-raw verifier → a `result` page (Arm 1 `anchors:` →
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md); Arm 2
internal-contrast) refining
[`result/aann-temporal-why-reanalysis`](../../findings/results/aann-temporal-why-reanalysis.md) and
bearing on [`claim/aann-behavioral-gradient`](../../findings/claims/aann-behavioral-gradient.md) and
[`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md). Contingent artifact:
[`design/aann-quant-temporal-inversion-v1`](../../../experiments/designs/aann-quant-temporal-inversion-v1.md).
