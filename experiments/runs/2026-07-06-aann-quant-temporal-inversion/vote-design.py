#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the DESIGN-STAGE frozen-to-be probe (PROTOCOL §A3).
One vote through openai/gpt-5.4-mini via the probe REST path. QA input to the fresh-agent
design pre-run critic's GO/NO-GO — not authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("You are a methodology reviewer. Your training cutoff may predate this project; "
            "judge only the design described below on its internal merits — do not defer to "
            "remembered conventions. Be adversarial and terse.")

DESIGN = """A frozen-TO-BE behavioral probe (no model data collected yet; design under review). Internal-contrast
on new items + item-matched human comparison on anchored items.

FINDING IT SHARPENS: In the AANN construction ("a scant three days" = article-adjective-numeral-noun), a prior
$0 re-analysis found ONE panel-wide model-vs-human inversion cell: for QUANTITY adjectives x TEMPORAL nouns,
HUMANS rate acceptability HIGHEST of four adjective classes (mean 8.45/10) but every one of 3 frontier models
rates it LOWEST. Drop that one cell and the remaining temporal ranking flips positive for all 3 models. The
inversion currently rests on a THIN, DISJOINT basis: model means came from 10 project-assigned HELD-OUT quant
adjectives on 5 nouns, scored against Mahowald's human quant-class mean whose adjectives are a DIFFERENT set.

QUESTION: is the inversion a property of the WHOLE quantity-adjective class, or carried by a FEW lexical items
(scant/mere)?

INSTRUMENT: reuse a BYTE-FROZEN prior graded-acceptability instrument (0-100 acceptability elicitation, a
4-point framing-robustness arm, a forced-choice Tier-0 manipulation check that already passes 3/3). ONLY the
item set is new. Tier-0 + framing re-run fresh this occasion.

ITEMS (~156 main): ~120 quant items = K~20 quantity modifiers x ~6 temporal items each. The K~20 splits into
~10 MAHOWALD-ATTESTED modifiers (mere/staggering/whopping/hefty/paltry/meager/extra/measly/substantial/
record-setting -- these carry ITEM-LEVEL human ratings -> Arm 1, human-comparison, anchored) and ~10
BEYOND-Mahowald modifiers (scant/bare/skimpy/negligible/modest/ample/solid/full/good/whole -- NO human rating ->
Arm 2, internal-contrast only, no invented ratings). Balanced across a small-vs-large quantity-polarity subtype
(pre-registered DESCRIPTIVE stratum). Plus ~36 non-quant reference items (Mahowald's own ambig/pos/neg temporal
adjectives) rated the SAME occasion to define each model's non-quant temporal baseline B_m. Zipf frequency-matched.

SCORING (all frozen before any call; no tuning after seeing which invert): per quant modifier j and model m,
A_m(j)=mean acceptability of j's temporal items; modifier j INVERTS iff A_m(j) < B_m. p_m = fraction of the K
modifiers that invert. VERDICT MAP (>=2/3 Tier-0-passing models): CLASS iff p_m>=0.70; LEXICAL iff p_m<=0.30
AND dropping the bottom-3 modifiers lifts the pooled quant cell to >=B_m; MIXED/SUBTYPE otherwise (or if the
inverters are predominantly one polarity subtype). NULL (first-class, pre-named): if the widened quant cell is
no longer LOWEST of the four classes for >=2/3, the located inversion was an artifact of the thin held-out
sample. Arm 1 also reports per-modifier model-low/human-high sign + Spearman vs Mahowald human means. Cost
~$0.10-0.20, ABORT_USD=$0.40.

DECISION DEFAULTS UNDER REVIEW: Q1 anchor scope = C HYBRID (anchored Arm 1 + internal-contrast Arm 2, reported
separately); Q2 threshold = the 0.70/0.30 count + bottom-drop above; Q3 baseline B_m = fresh Mahowald-own
non-quant reference on the same occasion.

Vote: is this a FAIR, non-question-begging test where ALL outcomes (CLASS / LEXICAL / MIXED-SUBTYPE / NULL) are
genuinely reachable; is the anchor discipline sound (Arm 1 a legitimate item-matched human comparison, Arm 2
strictly internal-contrast with no invented human rating); is B_m defined so the inversion is not baked in; and
are the Q1-C / Q2 / Q3 defaults right? Reply: VERDICT: GO | GO-WITH-CONDITIONS | NO-GO, then <=5 bullet issues
(each BLOCKER/SHOULD-FIX/NIT + concrete fix)."""

r = call(PANEL["B"], PREAMBLE, DESIGN, temperature=0, max_tokens=700)
print(r["content"])
print("\n--- billed:", billed_cost([[r]])[0], "err:", r.get("error"))
with open("vote-design-nonanthropic.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${billed_cost([[r]])[0]:.6f}; model {PANEL['B']}; s188 design-stage decorrelation vote]\n")
