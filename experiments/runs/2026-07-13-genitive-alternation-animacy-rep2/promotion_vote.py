#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s221 CROSS-SESSION PROMOTION REVIEW of the
genitive-alternation possessor-animacy line (now a REPLICATED PAIR: s218 v1 + s220 rep2, both
CONFIRM 3/3). PROTOCOL sec.2/sec.3 decorrelation rule.

QA input to the fresh-agent promotion reviewer (who keeps PROMOTE/REFUSE authority). One vote via
panel.B (openai/gpt-5.4-mini), cutoff-aware preamble prepended. Writes VOTE-promotion-s221.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-13. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether a REPLICATED behavioral-LLM result line should be PROMOTED to a standing `claim`. "
       "Promotion fixes the YARDSTICK, never the result: a written REFUSAL is a first-class outcome, "
       "and if you would prefer to promote only because a claim looks more productive, that is a "
       "violation. Be terse and adversarial. The promotion rule is conjunctive: promote only if the "
       "line has (1) REPLICATED (fresh disjoint items or a genuine second run) AND (2) SURVIVED ITS "
       "CONTROLS. A scoped claim may trade away MAGNITUDE (promote direction-only) but may NEVER trade "
       "away replication. End with a line 'VOTE: <PROMOTE-DIRECTION-ONLY | PROMOTE-FULL | REFUSE>'.")

USER = r"""
CONTEXT. The line: current LLMs track the English GENITIVE alternation's possessor-animacy constraint
-- animate possessors favour the s-genitive ("the judge's decision"), inanimate favour the of-genitive
("the decision of the judge"), the native-speaker acceptability DIRECTION from an openly-licensed
25-speaker rating study (Dubois et al. 2023). Instrument = graded forced-choice: hold the possessum
fixed, distribute 100 points by naturalness between the two phrasings; within-frame shift =
s-pref(animate) - s-pref(inanimate); human direction => shift > 0. Panel = 3 models (a Claude, a
Gemini, a GPT). The load-bearing control is a NONCE/RARE-POSSESSOR FIREWALL: rare/nonce possessors
carry no per-lemma corpus genitive statistic, animacy is conveyed only by a gloss ("a small wild
animal called a X" vs "a hard grey mineral called a X"), and nonce string-forms are balanced so a
no-animacy surface reader scores exactly 0 on the firewall arm. A frozen UD-EWT possessor-lemma
marginal-propensity covariate is the secondary control.

THE TWO RUNS (byte-frozen instrument; rep2's items CERTIFIED disjoint from v1 -- 0 shared possessor
lemmas, 0 shared nonce strings):
- v1 (s218, N=36 typical + 24 nonce frames): PANEL CONFIRM 3/3. Typical shift +0.134/+0.181/+0.141
  (all bootstrap CI-LB > 0). Nonce firewall +0.109/+0.205/+0.055 (all CI-LB > 0), but the gpt nonce
  leg was MARGINAL: 16/24 frames positive, one-sided sign-p 0.076.
- rep2 (s220, N=36 typical + 36 nonce frames, nonce arm enlarged to power the weak gpt leg): PANEL
  CONFIRM 3/3 AGAIN, both conjuncts. Typical +0.146/+0.150/+0.099 (CI-LB > 0). Nonce firewall
  +0.151/+0.279/+0.078 (CI-LB > 0). The gpt nonce leg is now DECISIVE: 25/36 frames, sign-p 0.014.

THE HONEST FENCES (reproduced on both runs; a claim would have to carry them verbatim):
- COVARIATE VACUITY. The UD-EWT propensity covariate has essentially no predictive validity (R^2
  0.002-0.038 v1; <=0.013 rep2; animate mean propensity slightly BELOW inanimate). So the
  covariate-adjusted-intercept leg is near-vacuous, and CONFIRM rests on the NONCE FIREWALL, not on
  the covariate. Only ONE control type is actually load-bearing.
- GPT IS THE WEAK FIREWALL LEG (decisive on the powered rep2 arm, but still the smallest: nonce
  +0.078 vs gemini +0.279). Magnitudes decorrelate ~3.6-4x across models. Displayed, never averaged.
- THE GRADIENT IS AN ANIMATE/NON-ANIMATE BINARY, not a smooth Zaenen 5-level ramp: the "collective"
  mid-level patterns WITH inanimate (~0.02-0.03 above it), not midway, on both runs.
- DIRECTION-ONLY ANCHOR. The Dubois human fact is a native-speaker acceptability DIRECTION (a
  separate-rating task, not forced-choice), so it anchors the sign only -- no per-item human gradient,
  no human-level competence claim. The nonce firewall is a within-model shortcut control, corroboratory
  (not a causal proof the distributional shadow is defeated): the animal-vs-mineral gloss that carries
  animacy also covaries with concreteness / taxonomic class / plausibility (R5 fence).

THE PRECEDENT. The sibling dative-alternation line was promoted DIRECTION-ONLY (magnitude deferred)
after a replicated pair (v1+v2 disjoint), citing both results, the human production-direction anchor,
and carrying its spread + weak-gpt-member caveats verbatim. The comparative-correlative likewise.

YOUR TASK. Vote PROMOTE-DIRECTION-ONLY / PROMOTE-FULL / REFUSE. Address especially: (a) is the
REPLICATED conjunct genuinely met -- two runs, certified-disjoint items, both CONFIRM 3/3 on BOTH the
typical direction AND the nonce firewall -- or is there a reason two runs of the SAME byte-frozen
instrument (same possessums, same gloss templates) is not an independent replication? (b) is the
CONTROLS conjunct genuinely met given only ONE control type (the nonce firewall) is load-bearing and
the covariate is near-vacuous -- does a single surviving control suffice for "survived its controls",
or is that too thin? (c) if you would promote, is DIRECTION-ONLY the right scope (magnitude deferred,
like the dative), and are the four fences above the correct and complete set to carry verbatim, or is
one missing/overstated? (d) is there any residual over-read a direction-only claim would still smuggle
(e.g. the nonce firewall being read as "the distributional shadow is defeated", or the binary being
read as a smooth animacy gradient)? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1600)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-promotion-s221.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) — s221 promotion review ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
