#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s238 PRE-RUN CRITIQUE of the particle-placement-givenness
POWERED MAGNITUDE run (PROTOCOL sec.A decorrelation rule).

No new decision is opened (the design was ratified s225; the line is a promoted claim). This is a
pre-run critique of the MAGNITUDE run + POOLING analysis as frozen. QA input to the fresh-agent pre-run
critic (who keeps GO/NO-GO authority). One vote via panel.B (openai/gpt-5.4-mini), cutoff-aware preamble
prepended. Writes VOTE-critic-s238.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-16. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether a FROZEN behavioral-LLM MAGNITUDE probe + its POOLING analysis are sound to RUN "
       "AS-IS. The measurement instrument is already ratified and byte-frozen; the direction of the "
       "effect is an already-promoted claim. This run does ONE new thing: estimate the SIZE of the "
       "effect (a within-model magnitude + bootstrap interval) by adding a third disjoint item arm "
       "and pooling. You are NOT re-litigating the design or the direction; you are catching any way "
       "the POOLING or the new items could produce a MISLEADING magnitude/interval. Running fixes "
       "the YARDSTICK, never the result; a fresh arm that reverses or fails to be positive (NO-LIFT) "
       "is a first-class outcome. If you would prefer a change only because it would make a larger/"
       "cleaner magnitude more likely, that is a violation — flag it. Be terse and adversarial. End "
       "with a line 'VOTE: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
CONTEXT. Current LLMs, on English VERB-PARTICLE PLACEMENT, shift their split-order preference toward
discourse-GIVEN objects in the human-attested direction (a definite/given object -> the SPLIT order,
"picked the barrel up", over the JOINED order "picked up the barrel"; Kim et al. 2016 / Gries 1999, a
native-speaker direction, openly licensed). Instrument = graded forced-choice: hold verb+particle+object
head-noun fixed, distribute 100 points by naturalness between the two orders of the SAME proposition;
split-pref = split_pts/(split_pts+joined_pts). The LOAD-BEARING control is a byte-identical discourse-
givenness FIREWALL: the scored object string is held byte-identical ("the <noun>") across GIVEN /
NEW-MENTIONED / NEW, and the givenness manipulation lives ONLY in one preceding discourse sentence, so
the decisive within-frame contrast shift2 = mean(split-pref|GIVEN) - mean(split-pref|NEW-MENTIONED) is
scored on identical strings — ANY string-frequency / determiner-collocation / lexical-recency reader
yields 0 by construction (certified). Resampling unit = the frame.

This DIRECTION + firewall-survival is already a promoted, standing claim, but scoped 2/3 and DIRECTION-
ONLY. It was found on TWO disjoint firewall runs (v1 40 frames, rep2 48 frames): for CLAUDE and GEMINI
the firewall shift2 clears CI-LB>0 on both runs (claude +0.040/+0.035; gemini +0.072/+0.057, both rep2
legs within v1's CIs). GPT is a PERSISTENT, REPLICATED SHADOW: its determiner effect is +0.100 both runs
but its firewall shift does NOT survive (+0.018 v1, +0.005 rep2, CI includes 0 both times; the rep2
enlargement to power it did not pull it over — its estimate DROPPED). The claim carries NO within-model
magnitude at all (its fence (j)).

WHAT THIS RUN DOES. Attach a within-model MAGNITUDE + interval to the firewall shift2. It adds a THIRD,
fresh, FIREWALL-ONLY arm of 48 frames, every (verb,particle,noun) triple and every object noun CERTIFIED
disjoint from BOTH prior runs (48 fresh nouns, 0 of the 88 prior triples / 86 prior nouns). The new items
were authored blind to model responses. Then analyze_merged.py POOLS the three disjoint firewall arms ->
136 frames and reports, per model: pooled mean shift2 = the magnitude, bootstrap 95% CI over 136 frames +
a sign test; ALSO the FRESH-48-only estimate (blind check) and the PRIOR-88-only estimate, side by side.

WHAT IS BYTE-FROZEN vs NEW:
- Byte-IDENTICAL (sha-verified): probe.py, freq_control.json, the prompt, parser, graded forced-choice,
  resampling unit, and the firewall context template-triple (re-used byte-identical).
- common.py identical except one budget constant (HARD_STOP_USD 3.80 -> 1.60; firewall-only is cheaper,
  ~864 calls ~$1.32). Never touches measurement.
- NEW: the 48-frame firewall-only item set (build_items.py, certified disjoint from v1 U rep2); and
  analyze_merged.py, the POOLING analysis (frozen before any call).

TWO DELIBERATE CHOICES YOU SHOULD PRESSURE-TEST:
1. FIREWALL-ONLY (Arms 1 definiteness & 3 length DROPPED). The magnitude the claim owes is the load-
   bearing FIREWALL shift2 (the confoundable definiteness arm is exactly where gpt shadows; length is a
   secondary convergent leg). This mirrors the genitive-MAG run being TYPICAL-ONLY (it dropped its
   already-twice-replicated firewall and re-ran only the magnitude-bearing arm). Also keeps the paid run
   ~$1.32.
2. POOLING with prior data. The 136-frame pooled interval REUSES the 88 already-seen frames (whose
   firewall shifts are known) plus 48 fresh-BLIND frames. To fence this the analysis ALSO reports the
   NEW-48-only estimate and the PRIOR-88-only estimate side by side.

THE GATE (2/3, gpt not gated). The claim's scope is claude+gemini; gpt is a displayed, replicated SHADOW.
So: MAGNITUDE ATTACHED iff (gate 1) the FRESH-48 arm clears CI-LB>0 for BOTH claude and gemini, AND
(gate 2) the POOLED-136 CI-LB>0 for BOTH claude and gemini. gpt is NOT part of any gate — its estimate is
reported; if gpt's pooled firewall UNEXPECTEDLY clears CI-LB>0, that is a first-class DISCLOSURE, not
folded into the headline. NO-LIFT if the fresh arm reverses/non-positive for either of claude/gemini or
the pooled CI-LB<=0 for either.

YOUR TASK. Vote GO / GO-WITH-CONDITIONS (say exactly what changes) / NO-GO (name the specific defect).
Address especially: (a) is a POOLED interval over 88-known + 48-blind frames a legitimate way to "attach
a magnitude", or does reusing the data that established the direction make the interval misleadingly tight
— and does reporting new-48-only + prior-88-only alongside adequately fence that? (b) is dropping Arms 1 &
3 defensible for a MAGNITUDE run on the firewall, or does re-running only the firewall miss a check that
could reveal the pooled firewall magnitude is confounded on these specific new items (note: the firewall
scored strings are byte-identical across conditions, so scored-string shortcuts give 0 by construction —
is that enough)? (c) is the 2/3 gate (claude+gemini gated, gpt a displayed non-gated SHADOW) the right
bar for attaching a magnitude to a 2/3-scoped claim, or should gpt's continued-shadow / possible-lift be
handled differently? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1600)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-critic-s238.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
