---
id: aann-quant-temporal-inversion-design
title: "AANN quant×temporal inversion probe — anchor scope, the class-vs-lexical scoring criterion, and the non-quant reference baseline that defines 'inversion'"
status: resolved
opened: 2026-07-06
opened-by: session-188
resolved: 2026-07-06
resolved-by: autonomous (adversarial review)
contingent-artifacts:
  - design/aann-quant-temporal-inversion-v1
---

# Decision: the value-laden gates of the quant×temporal inversion widening probe

> **RESOLVED 2026-07-06 (session 189, autonomous cross-session adversarial review + one
> non-Anthropic decorrelation vote — opened by session 188, ratified s189; the surfacing/ratifying
> boundary held). VERDICT: ADOPT-WITH-CHANGES — Q1-C (conditioned on a human-N feasibility gate) /
> Q2-**B** as the *primary* criterion (a change from the provisional Q2-A count) / Q3-A.** The
> resolution, the binding freeze conditions, and the anti-cheat rationale are in
> [§ Resolution](#resolution-s189) at the foot. The gate statements below are the s188 record,
> unchanged.

## Why this is owed

[`open-question/aann-quant-temporal-inversion`](../../findings/open-questions/aann-quant-temporal-inversion.md)
asks whether the one panel-wide model-vs-human AANN inversion cell — **quantity adjectives × temporal
nouns** ("a scant three days"), humans-highest / models-lowest
([`result/aann-temporal-why-reanalysis`](../../findings/results/aann-temporal-why-reanalysis.md), H4) —
is the **whole quantity-adjective class** or **a few lexical items**. The OQ sketches the probe but
freezes nothing; the design [`design/aann-quant-temporal-inversion-v1`](../../../experiments/designs/aann-quant-temporal-inversion-v1.md)
(landed s188) turns it into a runnable probe — and doing so forces choices that **are**
value-laden. The OQ names the sharpest one itself:

> "a widened probe either (a) restricts to Mahowald-attested quant×temporal items (fully anchored, but
> limited to the existing inventory — which may not be wide enough to separate class from item), or (b)
> authors new items and reads those as `internal-contrast-only` unless a human rating is obtained. This
> trade-off — anchored-but-narrow vs wide-but-partly-unanchored — is the operationalization choice a real
> design session would freeze."
> ([`open-question/aann-quant-temporal-inversion`](../../findings/open-questions/aann-quant-temporal-inversion.md),
> *Human-anchor status*)

Nothing here changes any finding; it fixes the **yardstick** for a probe that has **not run** and
**spends nothing** at the opening session.

## Gate Q1 — anchor scope

The load-bearing subtlety (verified in-repo): the located inversion compares the **v2b held-out** quant
adjectives (project-assigned: *ample, lavish, negligible, respectable, skimpy, towering, colossal,
modest, scant, sizable* — no human rating) against Mahowald's **anchored** quant-class human mean (8.45),
whose adjectives are a **different** set (*mere, staggering, whopping, hefty, paltry, meager, extra,
measly, substantial, record-setting*). Items Mahowald actually rated carry a genuine human-comparison;
items beyond his set do not. Options:

- **A — anchored-but-narrow.** Restrict the probe to **Mahowald-attested** quant×temporal items (his 10
  quant adjectives × temporal nouns), scored item-matched against `adjexp_turk.csv`. Fully
  human-anchored, but 10 modifiers may be too thin to separate class from item, and it cannot test the
  OQ's core ask (widen *beyond* the thin inventory).
- **B — wide-but-partly-unanchored.** Author a wide modifier set, read the whole thing as
  **`internal-contrast-only`**. Wide enough to separate class from item, no anchor obligation — but
  discards the genuine human-comparison the attested items would supply.
- **C — HYBRID (provisional default).** An **anchored Mahowald core** (Arm 1) **plus** a **widened
  internal-contrast extension** (Arm 2), **reported separately**. Arm 1 asks whether the inversion holds
  across Mahowald's *own* attested set (fully anchored); Arm 2 widens the modifier count to resolve
  class-vs-item robustly (internal-contrast on the new items). Each arm states its evidential type and
  anchor status at exactly its strength; no human rating is invented for Arm 2.

## Gate Q2 — the class-vs-lexical scoring criterion

How is CLASS vs LEXICAL decided **in advance**? Per-modifier indicator (frozen before any call):
modifier *j* **inverts** for model *m* iff `A_m(j) < B_m`; `p_m` = fraction of the K ≈ 20 quant
modifiers that invert. Options for the cut:

- **A (provisional default) — a broad-vs-few count with a bottom-drop confirmation, ≥ 2/3 panel.**
  **CLASS** iff `p_m ≥ 0.70`; **LEXICAL** iff `p_m ≤ 0.30` **and** dropping the bottom-3 modifiers lifts
  the pooled quant-cell mean to ≥ B_m; **MIXED/SUBTYPE** otherwise; **NULL** first-class.
- **B — a continuous per-modifier dispersion read** (the distribution of `A_m(j) − B_m` across
  modifiers; class = uniformly-below, lexical = one long left tail). More information, harder to pre-commit
  to a verdict *unless* the reference point is fixed a priori.
- **C — an anchored-only threshold** (decide purely on Arm 1's Mahowald modifiers with human means).
  Cleanest anchoring, but couples the threshold to Q1 = A and to ~10 modifiers.

## Gate Q3 — the non-quant reference baseline that *defines* "inversion"

`B_m` — the non-quant temporal baseline the quant cell must sit **below** to count as inverting.

- **A (provisional default) — fresh Mahowald-own ambig/pos/neg temporal reference items on the SAME
  occasion.** Puts the four-class comparison on one comparable occasion, avoids cross-run scale drift.
- **B — reuse v2b's frozen non-quant temporal ratings as B_m.** $0, but mixes two occasions/scales.
- **C — a fixed absolute cut.** Simplest, but discards the per-class structure that *is* the finding.

## Design-review inputs the ratification must weigh (added s188)

The design was reviewed s188 by a fresh-agent pre-run critic (**GO-WITH-CONDITIONS**) + a decorrelated
non-Anthropic vote (**NO-GO**, convergent in substance) — full record in
[`REVIEW-design-s188.md`](../../../experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md).
Both bear on these gates: **Q1-C** adopt but condition on an S1 human-N feasibility gate; **Q2** both
reviewers judged the 0.70/0.30 count + bottom-3-drop wording arbitrary/unstable and pushed toward a
tighter **monotone** primary criterion (Q2-B), with the count secondary; the verdict map needs a frozen
**NULL-vs-CLASS/LEXICAL precedence** (B2) and an inversion indicator matched to "below **all three**
non-quant cells" (S4), not the pooled mean; **Q3-A** adopt, carrying N1 (structural four-class
reproduction) and S2 (tourist/tourish); surface per-modifier noun/numeral balance (B1) and the
modifier-set anti-cheat (S7/S8) as freeze gates.

---

## Resolution (s189) {#resolution-s189}

**Ratified 2026-07-06 (session 189), autonomous cross-session adversarial review + one non-Anthropic
decorrelation vote. VERDICT: ADOPT-WITH-CHANGES.** The decision was opened s188 and is ratified s189 —
the boundary held (the fresh reviewer and the s189 orchestrator did no s188 design work). Both the
fresh-agent reviewer and the non-Anthropic vote (`openai/gpt-5.4-mini`, panel.B, $0.00233325) **converged
on the same changes**, and the s188 design-stage non-Anthropic vote had already converged in substance —
three decorrelated votes on the same package.

### Q1 — ADOPT C-hybrid, conditioned on a precise, pre-committed human-N feasibility gate

C is structurally right (Arm 1 and Arm 2 touch disjoint modifier sets and share one frozen occasion, so
the A-vs-B dilemma is false). **The condition (frozen in the PREREG before any per-modifier human mean is
computed):** at freeze, `prep.py` reports each Mahowald quant modifier's **temporal-item** rating-N from
the reclone; a modifier enters Arm 1's per-modifier human-comparison leg **only if** its temporal
rating-N ≥ a floor of **10**; below-floor modifiers fall back to the class-level comparison only. **Meta-
gate:** if fewer than **7 of 10** Mahowald quant modifiers clear the floor, Arm 1's per-modifier leg is
dropped and the result page must state that C degraded in practice to "class-level anchor + widened
internal-contrast" (Option B in substance). Carry **S3**: Arm 1 is a per-modifier **gradient** comparison
(model means on a balanced frame vs Mahowald's per-modifier human means), **not** "item-matched," unless
items are restricted to Mahowald's exact tuples. *This keeps the anchoring strength set by data
feasibility, not asserted.* **[Freeze finding, s189: the gate PASSES cleanly — all 10 Mahowald quant
modifiers have temporal rating-N ≥ 11 (staggering 24, whopping/measly/extra/record-setting 21–23,
meager 21, hefty 19, mere 16, paltry 14, substantial 11; total 193, matching the committed pooled class
mean 8.4508 n=193). So Q1-C proceeds at full strength (per-modifier leg viable, though each per-modifier
human mean is over 11–24 singly-rated items and is correspondingly noisy — the per-modifier Spearman is
underpowered and is reported with that caveat).]**

### Q2 — ADOPT **Q2-B** as the PRIMARY verdict criterion; the 0.70/0.30 count is demoted to descriptive secondary

Both s188 reviewers and this session's fresh reviewer and non-Anthropic vote agree the 0.70/0.30 counts
are arbitrary bright lines on a K≈20 axis where one modifier = 0.05 of `p_m` (a single near-boundary
modifier flips the panel category), the bottom-3-drop clause is independently arbitrary (S5: "3" is fixed
regardless of K), and the underlying reality is graded. The **monotone primary read** (threshold-free,
pre-committable, frozen before any call):

For quant modifier *j* and model *m*, the signed margin
`d_m(j) = A_m(j) − min_c(non-quant class mean_c)` (**S4**: the *min* over {ambig, pos, neg}, not the
pooled mean — the finding's property is "below **all three** non-quant cells"). Read the **shape of the
{d_m(j)} distribution** against the finding's own zero:

- **CLASS** — the distribution sits wholesale below zero: **median d_m(j) < 0 AND upper quartile
  (Q3) ≤ 0** (even the least-inverting quant modifiers are at/below the lowest non-quant baseline).
- **LEXICAL** — center at/above zero with a driving left tail: **median d_m(j) ≥ 0** (the typical quant
  modifier is *not* inverted) **yet the pooled quant-cell mean < min(non-quant)** (the cell-level
  inversion exists but is carried by the tail).
- **MIXED / graded** — median near zero with substantial spread; neither wholesale-below nor
  clean-center-plus-tail.
- **Panel verdict** = the category holding for **≥ 2/3** Tier-0-passing models.

The cut point is **zero = the finding's own baseline**, not an invented fraction, so there is nothing to
tune. **B2 precedence (frozen):** evaluate **NULL first** on the aggregate quant-cell mean — if the
widened quant cell is **not** the lowest of the four adjective-class cells for ≥ 2/3 models, verdict =
**NULL** regardless of the per-modifier distribution; only if not-NULL, read CLASS/LEXICAL/MIXED on the
{d_m(j)} shape. The **0.70/0.30 count and the bottom-drop survive as descriptive secondary** reporting,
never verdict-bearing. **Subtype (small-vs-large quantity polarity) is descriptive-only** (**S6**: removed
from the verdict map).

### Q3 — ADOPT A (fresh same-occasion Mahowald-own non-quant reference)

Correct: the inversion is intrinsically a within-occasion, between-class contrast; same-run reference
removes calibration drift for cents. Carry **N1** (this is a *structural* four-class reproduction on a new
occasion, ~4 non-quant adjectives/class — not the §1 table's full-class cells; say so) and **S2** (use
what Mahowald's humans actually saw on the anchored/reference items; make the template-2 exclusion
recompute gate-bearing). **[Freeze finding, s189 (reverses the S2 assumed direction): the "tourish" typo
is in Mahowald's OWN generated stimuli — `generate_sentence_templates/templates_adj.csv` and
`aann-sents/aann_sentences.txt` both read "The tourish stayed …", so Mahowald's MTurk raters saw
"tourish". Faithfulness therefore means KEEPING "tourish" (as v2b did), not "correcting" it to "tourist";
the freeze uses "tourish" uniformly and runs the template-2-exclusion sensitivity recompute as a
gate-bearing robustness check.]**

### Anti-cheat check — PASS; all four outcomes reachable

The one default that baked in an outcome was the provisional **pooled `B_m`** (biases toward CLASS, S4) —
corrected to **min**. The bottom-3-drop (the only mechanism that made LEXICAL reachable, and arbitrary) is
demoted to descriptive. **Modifier-set curation is bound as an anti-cheat condition (S7/S8):** the exact
K = 20 is enumerated in the PREREG with a documented source + polarity per modifier; Arm 2 must retain
large-magnitude modifiers (reversing the design's drop) and mark each modifier genuinely-new vs
v2b-carryover, and **a CLASS verdict must survive the genuinely-new-subset read reported separately**. Under
the ratified scoring all four outcomes are reachable: **NULL** (aggregate cell not lowest — evaluated
first), **CLASS** (median & Q3 below zero), **LEXICAL** (median ≥ 0 but pooled cell below min via the
tail), **MIXED** (median near zero, spread). None foreclosed. Ratification fixes the **yardstick, never
the result**: the null and the inverted/lexical/mixed outcomes stay first-class.

### Binding freeze conditions carried onto the freeze/run session

**B1** identical noun×numeral×template frame per modifier (balanced Latin square), asserted per-modifier;
**B2** NULL-first precedence (above); **S1** human-N gate (above; passed); **S2** tourish faithfulness +
gate-bearing exclusion recompute (above); **S3** "per-modifier gradient comparison," not "item-matched";
**S4** min-baseline indicator; **S5** drop-count tied to K (now demoted to descriptive anyway); **S6**
subtype descriptive-only; **S7** Arm 2 retains large-magnitude + genuinely-new subset reported
separately; **S8** exact K = 20 enumerated with per-modifier source; **S9** per-modifier Zipf partial into
the read; **S10** reframe "byte-frozen instrument" as "the *calling* instrument is byte-frozen; the item
set and the §6 verdict logic are new, frozen in PREREG and self-tested." **N1/N2** carried.

### Application

The contingent design [`design/aann-quant-temporal-inversion-v1`](../../../experiments/designs/aann-quant-temporal-inversion-v1.md)
is promoted: `contingent-on` cleared; anchor structure fixed (Arm 1 `anchors:` →
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md), Arm 2
internal-contrast). The probe **freezes + runs this session (s189)** under the conditions above, with a
freeze-stage pre-run critic + one non-Anthropic vote and a post-run recompute-from-raw verifier. Tom's
standing override outranks this autonomous ratification. Logged in [`log.md`](../../../log.md).
