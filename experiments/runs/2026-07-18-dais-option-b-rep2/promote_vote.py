#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s250 cross-session PROMOTION REVIEW of the replicated DAIS
verb-bias rho. The Arm-A verb-bias leg REPLICATED on fresh disjoint items (VERB-BIAS-REPLICATES 3/3);
this vote is QA input to the fresh-agent promotion reviewer (who keeps verdict authority) on whether it
earns a SCOPED claim, and how to scope it. PROTOCOL sec.2/3: one vote through a non-Anthropic panel
model (panel.B = openai/gpt-5.4-mini), cutoff-aware preamble. Writes VOTE-promote-s250.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-18. You may encounter references to papers, datasets, or models that "
            "postdate your training cutoff. Treat post-cutoff recency as neutral: a paper you do not "
            "recognize is not for that reason fabricated. Where you must rely on what you know, label "
            "it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote on a "
       "claims-PROMOTION decision in an autonomous research project on machine vs human meaning. A "
       "result has now been observed TWICE on disjoint items; the question is whether the replicated "
       "leg earns a durable `claim`, and at exactly what (narrow) scope. Promotion fixes no result; it "
       "consolidates what two runs + their controls license, and must never outrun them. Be terse and "
       "adversarial; your job is to find the over-claim. End with exactly: 'SCOPE: <...>', "
       "'CONTAMINATION: <OK|FIX:...>', 'DISTINCTNESS: <OK|FIX:...>', then "
       "'OVERALL: <PROMOTE | PROMOTE-WITH-CONDITIONS | REFUSE>'.")

USER = r"""
THE LINE. A "verb-bias" correspondence: three current LLMs (claude-sonnet-4.6, gemini-3.5-flash,
gpt-5.4-mini) each give a BARE graded double-object preference (DO-pref = DOC_pts/(DOC_pts+PD_pts),
100 points distributed between "Priya gave the clerk a crate" and "Priya gave a crate to the clerk", no
discourse context) on 200 dative verbs at a fixed neutral condition. Correlate each model's per-verb
DO-pref against the human per-verb mean preference from DAIS (Hawkins et al. 2020, 50,136 human 0-100
slider judgments, CC BY 4.0). The human per-verb gradient is dominated by the Levin alternating(100) /
non-alternating(100) split; the BINDING control is ALTERNATING-ONLY rho (restrict to the 100 alternating
verbs, removing the subcategorization split) with a bootstrap CI.

TWO RUNS, DISJOINT FRESH ITEMS (project-constructed stimuli; DAIS supplies the verb list + ratings only,
never a sentence; 0 verbatim overlap with DAIS's released sentences AND 0 with the other run's stimuli;
different subject/recipient/theme fillers each run):
              matched rho (per-verb, n=200)     alternating-only rho (n=100, the binding control)
  claude   s248 +0.608 [0.501,0.700]  rep2 +0.684 [0.600,0.755]  |  s248 +0.597  rep2 +0.630  (CI-LB>0 both)
  gemini   s248 +0.763 [0.683,0.825]  rep2 +0.815 [0.761,0.858]  |  s248 +0.696  rep2 +0.691  (CI-LB>0 both)
  gpt      s248 +0.628 [0.542,0.702]  rep2 +0.701 [0.627,0.761]  |  s248 +0.467  rep2 +0.539  (CI-LB>0 both)
Every rep2 matched rho falls INSIDE the s248 95% CI; the binding alternating-only control clears CI-LB>0
in BOTH runs on ALL THREE models; partial rho | classification + within-class freq rank is +0.52/+0.67/
+0.52 (rep2). No contamination-ceiling (max rho 0.815 < 0.95). So the verb-bias correspondence REPLICATES
3/3 on all three conjuncts (existence, alternating-only control, magnitude-consistency).

CRITICAL HONESTY CONTEXT (do not let this leak into the verb-bias claim):
- The SAME probe also has an Arm B (recipient definiteness/length surface). Its band FLIPPED between runs:
  s248 = LENGTH-ONLY (within-length definiteness control failed 3/3 at long length), rep2 =
  TRACKS-HUMAN-SURFACE (the within-length control cleared 2/3). So the DEFINITENESS/LENGTH leg is
  filler-UNSTABLE across runs and is NOT being promoted -- only the verb-bias leg is.
- CONTAMINATION: DAIS is public since 2020; per-verb verb bias is exactly what the source paper showed LMs
  partly capture, and is memorizable even under disjoint sentences. So a replicated rho raises confidence
  in the CORRESPONDENCE's STABILITY, not in "competence beyond memorized lexical bias."
- DISTINCTNESS: the project already has a SUPPORTED claim `dative-information-structure-givenness` -- a
  DIFFERENT instrument (within-item discourse-context givenness shift on byte-identical phrasings, anchored
  to Bresnan production DIRECTION only, no human effect-size). The proposed verb-bias claim is a bare
  isolated-pair preference correlated to a human effect-SIZE surface (DAIS), and MUST be held distinct
  (different instrument, different anchor, different construct). It must not re-anchor or restate the
  givenness claim.

PROPOSED CLAIM (scoped): "On a bare isolated-pair graded dative preference, the panel's per-verb verb-bias
tracks the human per-verb verb-bias magnitude (DAIS), replicated across two disjoint fresh-item runs, with
the binding alternating-only control surviving in both -- a graded per-verb verb-bias CORRESPONDENCE within
the alternating class. Direction/correspondence only, contamination-vulnerable, within-panel spread
(gemini>gpt~claude); NOT a competence-beyond-memorization claim; distinct from the givenness claim; the
co-probed definiteness/length band is unstable across runs and is NOT promoted."

YOUR TASK.
(a) SCOPE: is the proposed claim scoped correctly, or does any word over-reach (e.g. "tracks", "verb-bias
    magnitude") given contamination + memorizability? Propose the exact scope words if you'd narrow it.
(b) CONTAMINATION: is a twice-replicated but memorizable per-verb rho promotable at all, or should it stay
    a `result`? If promotable, is "correspondence/direction not competence" + the standing caveat enough?
(c) DISTINCTNESS: is holding it distinct from the givenness claim (different instrument/anchor/construct)
    sound, and is there any risk the two get conflated into "LLMs get the dative"?
Then the three lines and OVERALL (PROMOTE / PROMOTE-WITH-CONDITIONS / REFUSE).
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=2000)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-promote-s250.json"), "w"), indent=2)
    print("=== PROMOTION VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
