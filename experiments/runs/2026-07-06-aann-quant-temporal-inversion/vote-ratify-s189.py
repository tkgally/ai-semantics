#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the RATIFICATION of the decision
`aann-quant-temporal-inversion-design` (PROTOCOL §2). One vote through
openai/gpt-5.4-mini via the probe REST path. QA input to the fresh-agent
ratification reviewer's verdict — not authoritative. Cutoff-aware preamble.

The load-bearing ratification question is Q2-A vs Q2-B (both s188 reviewers judged
the 0.70/0.30 count wording arbitrary and pushed toward a monotone/continuous read)."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("You are a methodology reviewer ratifying a frozen measurement yardstick (not a result). "
            "Your training cutoff may predate this project; judge only the decision described below on "
            "its internal merits — do not defer to remembered conventions. Be adversarial and terse. "
            "Ratification fixes the yardstick, never the result: every outcome (CLASS/LEXICAL/MIXED/NULL) "
            "must stay genuinely reachable.")

DECISION = """DECISION UNDER RATIFICATION: how to score a behavioral probe that asks whether one AANN
model-vs-human inversion cell (QUANTITY adjectives x TEMPORAL nouns: humans rate "a scant three days"
HIGHEST of 4 adjective classes, all 3 frontier models rate it LOWEST) is the WHOLE quantity-adjective
class or a FEW lexical items. The probe reuses a byte-frozen 0-100 graded-acceptability instrument;
only the item set + scoring logic are new. K=20 quantity modifiers x ~10 balanced temporal items each;
~10 Mahowald-attested modifiers carry item-level human ratings (anchored Arm 1), ~10 beyond-Mahowald
modifiers are internal-contrast (Arm 2). Non-quant reference items rated the SAME occasion define each
model's non-quant temporal baseline B_m.

Per quant modifier j, model m: A_m(j) = mean acceptability of j's temporal items. Modifier j INVERTS
iff A_m(j) < B_m. p_m = fraction of K modifiers that invert.

THREE GATES:

Q1 anchor scope. A=anchored-narrow (Mahowald items only, ~10 modifiers, fully human-anchored but maybe
too thin to separate class from item). B=wide-unanchored (author wide set, all internal-contrast, wide
enough but discards the human comparison). C (DEFAULT)=HYBRID (anchored Arm 1 + widened internal-contrast
Arm 2, reported separately). A prior review flagged: Arm 1's per-modifier human means depend on a
gitignored file (only class-level means committed); if per-modifier rating-N is thin, C degrades in
practice toward B. Provisional default C, conditioned on a per-modifier human-N feasibility gate.

Q2 class-vs-lexical scoring threshold. A (DEFAULT)=a count rule: CLASS iff p_m>=0.70; LEXICAL iff
p_m<=0.30 AND dropping the bottom-K*Y modifiers lifts the pooled quant cell to >=B_m; MIXED otherwise;
NULL first-class (quant cell no longer lowest of 4 classes for >=2/3 models). B=a continuous per-modifier
dispersion read (distribution of A_m(j)-B_m across modifiers; class = uniformly below, lexical = one long
left tail), monotone, no arbitrary 0.70/0.30 cut. BOTH prior reviewers judged the 0.70/0.30 count wording
arbitrary/unstable and pushed toward B as the PRIMARY read with the count secondary/descriptive.
THE KEY RATIFICATION QUESTION: should Q2-A or Q2-B be the primary verdict criterion?

Q3 baseline B_m. A (DEFAULT)=fresh Mahowald-own non-quant temporal reference rated the SAME occasion.
B=reuse frozen prior non-quant ratings (mixes occasions/scales). C=fixed absolute cut. Default A.

Also to freeze: inversion defined as A_m(j) < MIN(non-quant class means) not the pooled mean (the property
is "below ALL THREE non-quant cells"); NULL-vs-CLASS/LEXICAL precedence (evaluate NULL on the cell mean
first); per-modifier noun/numeral/template balance; per-modifier Zipf partial.

VOTE: (1) Q2-A vs Q2-B as the PRIMARY criterion — which, and why? (2) adopt Q1-C (with the human-N gate)?
(3) adopt Q3-A? (4) any gate where a default bakes in a result or blocks an outcome? Reply:
VERDICT: ADOPT-DEFAULTS | ADOPT-WITH-CHANGES | KEEP-OPEN, then name your Q2 pick explicitly, then <=5
bullet issues (each with a concrete fix)."""

r = call(PANEL["B"], PREAMBLE, DECISION, temperature=0, max_tokens=700)
print(r["content"])
print("\n--- billed:", billed_cost([[r]])[0], "err:", r.get("error"))
with open("vote-ratify-s189-nonanthropic.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${billed_cost([[r]])[0]:.6f}; model {PANEL['B']}; s189 ratification decorrelation vote]\n")
