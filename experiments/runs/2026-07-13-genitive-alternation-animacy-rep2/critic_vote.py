#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s220 PRE-RUN CRITIQUE of the genitive-animacy REP2
(fresh-item replication) probe (PROTOCOL sec.A3 decorrelation rule).

No new decision is opened (the design was ratified s218); this is a pre-run critique of the
REPLICATION as frozen. QA input to the fresh-agent pre-run critic (who keeps GO/NO-GO authority).
One vote via panel.B (openai/gpt-5.4-mini), cutoff-aware preamble prepended. Writes VOTE-critic-s220.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-13. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether a FROZEN behavioral-LLM replication probe is sound to RUN AS-IS. The design is "
       "already ratified and byte-frozen; the item set is new. You are NOT re-litigating the design; "
       "you are catching any way the FRESH ITEMS or the ONE change (a larger nonce arm) could bias "
       "the replication, or any residual cheat-surface. Running fixes the YARDSTICK, never the "
       "result; a failure-to-replicate (SHADOW / WEAK / FALSIFY) is a first-class outcome. If you "
       "would prefer a change only because it would make a positive replication more likely, that is "
       "a violation — flag it. Be terse and adversarial. End with a line "
       "'VOTE: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
CONTEXT. A prior single run (s218) found current LLMs track the English GENITIVE alternation's
possessor-animacy constraint: animate possessors favour the s-genitive ("the judge's decision"),
inanimate favour the of-genitive ("the decision of the judge") — a native-speaker acceptability
direction from an openly-licensed 25-speaker rating study (Dubois et al. 2023). Instrument = graded
forced-choice: hold the possessum fixed, distribute 100 points by naturalness between the two
phrasings; s-pref = s_pts/(s_pts+of_pts); within-frame shift = s-pref(animate) - s-pref(inanimate);
human direction => shift > 0. Resampling unit = the frame. s218 came out CONFIRM 3/3 (typical shift
+0.134/+0.181/+0.141; nonce-firewall shift +0.109/+0.205/+0.055) but was a SINGLE run, and the
project's promotion rule requires REPLICATED-AND-controls-survived (conjunctive). This is the
fresh-item replication.

WHAT IS FROZEN vs NEW:
- Byte-IDENTICAL from s218 (sha-verified): the prompt, parser, graded forced-choice, resampling unit,
  the pre-registered CONFIRM/SHADOW/WEAK/FALSIFY verdict rule, the covariate recipe, analyze.py.
- common.py identical except one budget constant (HARD_STOP_USD 1.30 -> 1.90) because the item count
  grew. Never touches measurement.
- NEW item set only: 36 typical frames (animate/collective/inanimate real possessors) + 36 nonce
  frames (animate/inanimate rare/nonce possessors, animacy carried ONLY by a gloss "a small wild
  animal called a <s>" vs "a hard grey mineral called a <s>", nonce strings orthographically balanced
  so the animate-slot and inanimate-slot string multisets are identical). Every typical possessor
  lemma and every nonce string is CERTIFIED disjoint from s218 (0 shared). Within every frame,
  possessor length + final-sibilancy + definiteness are matched across animacy levels (certified), so
  length/sibilancy/position/always-s/always-of readers give within-frame shift 0.

THE ONE DELIBERATE CHANGE: the nonce arm is enlarged 24 -> 36 frames, because in s218 the gpt nonce
leg was marginal (mean +0.055, 16/24 frames positive, one-sided sign-p 0.076). More paired nonce
contrasts give that weak leg's sign test + bootstrap CI more power. The typical arm stays 36.

THE COVARIATE (honest, pre-registered as weak). A frozen per-possessor-lemma marginal s-genitive
propensity from UD-English-EWT partials out the possessor's marginal genitive-propensity from the
typical-arm shift. At this freeze it is AGAIN near-vacuous: only 4/36 animate and 2/36 inanimate
typical lemmas have any corpus genitive, and the mean smoothed propensity is essentially flat
(animate 0.1728 vs inanimate 0.1760, animate slightly BELOW). So the PRE-REGISTERED reading is that
CONFIRM rests on the NONCE arm (the covariate leg is weak corroboration); analyze.py reports the
covariate's own R^2.

YOUR TASK. Vote GO / GO-WITH-CONDITIONS (say exactly what changes) / NO-GO (name the specific defect).
Address especially: (a) is disjointness of possessor lemmas + nonce strings the RIGHT freshness
criterion for a replication, or does re-using the same possessUMS / same gloss templates leave a
shared-item confound that would make this less than an independent replication? (b) does enlarging ONLY
the nonce arm (not the typical arm) bias the verdict in any direction, or is it a legitimate targeted
power increase on the known-weak leg? (c) given the covariate is again near-vacuous, is "CONFIRM rests
on the nonce arm, covariate leg weak" the honest framing, or is there a residual way a no-animacy
surface reader could score a spurious nonce-arm shift on these specific new nonce items (e.g. the
animal-vs-mineral gloss doing semantic work beyond animacy)? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1400)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-critic-s220.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
