#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s228 PRE-RUN CRITIQUE of the verb-particle-placement REP2
(fresh-item replication) probe (PROTOCOL sec.A3 decorrelation rule).

No new decision is opened (the design was ratified s225); this is a pre-run critique of the REPLICATION
as frozen. QA input to the fresh-agent pre-run critic (who keeps GO/NO-GO authority). One vote via
panel.B (openai/gpt-5.4-mini), cutoff-aware preamble prepended. Writes VOTE-critic-s228.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-15. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether a FROZEN behavioral-LLM replication probe is sound to RUN AS-IS. The design is "
       "already ratified and byte-frozen; the item set is new. You are NOT re-litigating the design; "
       "you are catching any way the FRESH ITEMS or the ONE change (a larger firewall arm) could bias "
       "the replication, or any residual cheat-surface. Running fixes the YARDSTICK, never the "
       "result; a failure-to-replicate (SHADOW / WEAK / FALSIFY) is a first-class outcome. If you "
       "would prefer a change only because it would make a positive replication more likely, that is "
       "a violation — flag it. Be terse and adversarial. End with a line "
       "'VOTE: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
CONTEXT. A prior single run (v1, s225/s226) found current LLMs shift their English VERB-PARTICLE
PLACEMENT preference in the human direction: a given/definite object favours the SPLIT order
("picked the box up") over the JOINED order ("picked up the box") — a native-speaker direction from an
openly-licensed source (Kim et al. 2016 / Gries 1999), grounding the SIGN only. Instrument = graded
forced-choice: hold verb + particle + object head-noun fixed, distribute 100 points by naturalness
between the two orders; split-pref = split_pts/(split_pts+joined_pts). Resampling unit = the frame
(verb+particle+object-head-noun). THREE arms: Arm 1 DEFINITENESS (a/the, confoundable, consistency
check only); Arm 2 DISCOURSE-GIVENNESS FIREWALL (the object string held BYTE-IDENTICAL "the <noun>"
across three context conditions GIVEN / NEW-MENTIONED / NEW; givenness lives only in one preceding
discourse sentence; decisive contrast GIVEN − NEW-MENTIONED holds object-noun lexical priming/recency
constant; LOAD-BEARING, carries the CONFIRM); Arm 3 LENGTH (short/heavy-NP, convergent-validity leg,
non-gating). Because Arm 2's two scored order-strings are byte-identical across the three conditions,
any scored-string reader (always-split / always-joined / string-frequency / determiner-collocation /
position) yields within-frame firewall shift 0 BY CONSTRUCTION (certified). v1 came out PANEL CONFIRM
(firewall GIVEN−NEW-MENTIONED cleared CI-LB>0 in 2/3: claude +0.040, gemini +0.072; Arm-1 consistent
3/3), but gpt was a pre-named SHADOW (firewall +0.018, CI [-0.017,0.055], 18/40 frames) and it was a
SINGLE run. The project's promotion rule requires REPLICATED-AND-controls-survived. This is the
fresh-item replication.

WHAT IS FROZEN vs NEW:
- Byte-IDENTICAL from v1 (sha-verified): probe.py, analyze.py, build_cooc_particle.py, freq_control.json
  (the prompt, parser, graded forced-choice, resampling unit, the CONFIRM/SHADOW/WEAK/FALSIFY verdict
  rule, the covariate recipe AND its data), and the Arm-2 discourse context template (given/newment/new).
- common.py identical except one budget constant (HARD_STOP_USD 3.50 -> 3.80) because the item count grew.
  Never touches measurement.
- NEW item set only: 48 frames (v1 had 40). Every (verb, particle, noun) TRIPLE and every object noun is
  certified DISJOINT from v1's 40 (all 48 nouns are fresh, not in v1's noun set). Every verb+particle pair
  is drawn from v1's frozen 38-pair set (10 flexible pairs recur with a second distinct fresh noun to reach
  48 frames), so the byte-frozen covariate freq_control.json and analyze.py's VERB_LEMMA cover every frame
  with NO re-freeze. Arm-2 context template is byte-identical; parallelism (14/14/14 words, noun 1/1/0, one
  comma, declarative, no particle-adjacent leak) re-certified over the fresh nouns.

THE ONE DELIBERATE CHANGE: the firewall arm is enlarged 40 -> 48 frames, because in v1 the gpt firewall
leg was marginal (mean +0.018, CI [-0.017,0.055], 18/40 frames positive). More paired firewall contrasts
give that weak leg's bootstrap CI + sign test more power. All three arms scale with frame count (each
frame carries all three arms); the enlargement is applied to the whole frame set, concentrating power in
the load-bearing firewall arm without changing the per-frame arm balance.

THE COVARIATE (honest, pre-registered as weak). A frozen per-(verb+particle) marginal SPLIT-order rate
from UD-English-EWT is near-vacuous (16/38 pairs any corpus token; base split rate 0.42). CONFIRM rests
on the byte-identical firewall arm (which needs no corpus); analyze.py reports the covariate's own R^2.

YOUR TASK. Vote GO / GO-WITH-CONDITIONS (say exactly what changes) / NO-GO (name the specific defect).
Address especially: (a) is triple-disjointness + all-fresh-nouns the RIGHT freshness criterion for a
replication, or does REUSING the 38 verb+particle PAIRS (with new nouns) leave a shared-item confound
that would make this less than an independent replication of a particle-PLACEMENT effect? (b) does
enlarging the frame set to 48 (all arms grow, firewall included) bias the verdict in any direction, or is
it a legitimate targeted power increase on the known-weak firewall leg? (c) with 10 pairs recurring across
two frames (same split_rate x, different noun), is there any residual way a no-givenness surface reader
could score a spurious firewall-arm shift on these specific new items — or any way the fresh contexts
(byte-identical template, new noun filled in) could leak the answer or make the definite object
differentially felicitous across GIVEN/NEW-MENTIONED/NEW? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1400)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-critic-s228.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
