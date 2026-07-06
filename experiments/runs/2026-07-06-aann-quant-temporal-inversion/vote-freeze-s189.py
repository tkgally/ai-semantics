#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the FROZEN probe (PROTOCOL §A3 freeze-stage). One vote via
openai/gpt-5.4-mini. QA input to the fresh-agent freeze-stage pre-run critic — not authoritative."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("You are a methodology reviewer giving a final GO/NO-GO on a FROZEN behavioral probe about "
            "to spend money. Your training cutoff may predate this project; judge only the frozen design "
            "on its internal merits. Be adversarial and terse. All outcomes must stay reachable; the "
            "verdict logic must not be tunable after seeing the data.")

FROZEN = """FROZEN AANN quant×temporal inversion probe (about to run ~972 calls, ~$0.17). Reuses a
byte-frozen 0-100 acceptability instrument; only the item set + verdict code are new (verdict code
self-tested to reach CLASS/LEXICAL/MIXED/NULL on synthetic data before any call).

QUESTION: in "a <ADJ> three days" (AANN), one prior cell inverts panel-wide: for QUANTITY adjectives x
TEMPORAL nouns, humans rate acceptability HIGHEST of 4 adjective classes, all 3 frontier models LOWEST.
Is the inversion the WHOLE quantity class or a FEW lexical items?

ITEMS (frozen stimuli.json): K=20 quant modifiers, each on an IDENTICAL balanced frame (5 temporal
nouns x 2 numerals x rotated template = 10 items/modifier; asserted 2/noun, 5/numeral). The 20 split
into 10 Mahowald-attested (mere/staggering/whopping/hefty/paltry/meager/extra/measly/substantial/
record-setting -- carry human temporal means N=11-24, ARM 1 anchored) + 10 widened (good/full/whole/
solid/bare genuinely-new + scant/skimpy/ample/towering/colossal v2b-carryover -- NO human rating, ARM 2
internal-contrast). Plus 60 non-quant reference items (4 ambig + 4 pos + 4 neg adjectives x 5 items),
rated the SAME occasion to define each model's non-quant class means. Tier-0 manipulation check (24) +
4-point framing arm (40) re-run fresh. Frequency: per-modifier Zipf recorded + reported as a partial;
the +/-0.5 Zipf MATCH is deliberately NOT enforced (it would exclude natural high-freq quantity words
good/full/whole -- exactly what the class-vs-lexical test needs).

SCORING (frozen before any call; self-tested):
 A_m(j)=mean 0-100 over modifier j's 10 items. B_m^min = MIN over {ambig,pos,neg} of the model's
 non-quant temporal class mean. d_m(j)=A_m(j)-B_m^min.
 NULL FIRST: if pooled quant-cell mean is NOT the lowest of the 4 class cells for the model -> NULL.
 Else read the SHAPE of {d_m(j)}: CLASS iff median(d)<0 AND Q3(d)<=0; LEXICAL iff median(d)>=0 AND
 pooled quant-cell mean < B_m^min (tail-carried); MIXED otherwise. Panel = category for >=2/3 Tier-0
 passers. The 0.70/0.30 inversion COUNT is computed but DESCRIPTIVE-ONLY (not verdict-bearing).
 ARM 1 human comparison: per-modifier model-low/human-high sign + Spearman(model, human) over the 10
 anchored modifiers (flagged noisy). Tourish-template exclusion recompute is gate-bearing.

PRE-REGISTERED BET: widened quant cell stays lowest for >=2/3 (NOT NULL) and the distribution is
CLASS or MIXED rather than LEXICAL. A NULL or LEXICAL is a genuine loss, written as such.

VOTE: (1) is this a FAIR test where NULL/CLASS/LEXICAL/MIXED are ALL genuinely reachable and none is
baked in by the baseline choice (MIN vs pooled) or the item set? (2) is the anchor discipline sound
(Arm 1 legitimate human comparison, Arm 2 strictly internal-contrast, no invented ratings)? (3) any
freeze defect that must be fixed BEFORE spending? Reply: VERDICT: GO | GO-WITH-CONDITIONS | NO-GO, then
<=5 bullets (each BLOCKER/SHOULD-FIX/NIT + concrete fix)."""

r = call(PANEL["B"], PREAMBLE, FROZEN, temperature=0, max_tokens=700)
print(r["content"])
print("\n--- billed:", billed_cost([[r]])[0], "err:", r.get("error"))
with open("vote-freeze-s189-nonanthropic.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${billed_cost([[r]])[0]:.6f}; model {PANEL['B']}; s189 freeze-stage decorrelation vote]\n")
