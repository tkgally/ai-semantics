#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s219 PROMOTION REVIEW of the genitive-alternation
animacy line (PROTOCOL sec.3 claims-promotion rule; sec.2 decorrelation rule).

QA input to the fresh-agent reviewer's verdict (who keeps authority). One vote via panel.B
(openai/gpt-5.4-mini), cutoff-aware preamble prepended. Writes VOTE-promotion-s219.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-13. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether to PROMOTE a single experimental result to a standing 'claim'. Promotion fixes "
       "the YARDSTICK, never the result; a written REFUSAL is a first-class, non-embarrassing "
       "outcome, and a review that promotes to look productive is a violation. If you would vote "
       "PROMOTE only because the result is exciting, flag it. Be terse and adversarial. End with a "
       "line 'VOTE: <PROMOTE | PROMOTE-SCOPED | REFUSE>'.")

USER = r"""
THE BAR (the project's standing rule). A result line is promoted to a standing 'claim' only when it
has (1) REPLICATED — fresh items or a genuine second run — AND (2) SURVIVED ITS CONTROLS. The output
is a claim citing results/magnitudes/anchors, OR a written refusal. Every promoted claim in this
project to date rested on >=2 runs (the sibling dative alternation was promoted only after a v1+v2
pair, direction-only, with the magnitude deferred to a later powered re-run; the comparative-
correlative likewise). No claim has ever been promoted from a single run.

THE CANDIDATE. The English GENITIVE alternation animacy probe, ONE run (session 218):
- Instrument: graded forced-choice, s-genitive ("the judge's decision") vs of-genitive ("the
  decision of the judge"); within-frame shift = s-pref(animate) - s-pref(inanimate); human direction
  (Dubois et al. 2023, 25 native speakers, CC BY 4.0) => shift > 0. Possessor length, final
  sibilancy, definiteness matched within frame by construction.
- Verdict: PANEL CONFIRM 3/3 on all three pre-registered conditions.
  * Typical-frame animacy shift +0.134 / +0.181 / +0.141 (claude/gemini/gpt), all bootstrap CI-LB > 0.
  * NONCE/FIREWALL arm (rare/nonce possessors with NO per-lemma corpus genitive statistic; animacy
    carried only by a gloss; nonce string-forms balanced): shift +0.109 / +0.205 / +0.055, all
    CI-LB > 0. This is the load-bearing shadow control: a no-animacy reader that only learned "which
    possessor lemma takes 's more often" scores zero here.
  * Covariate-adjusted intercept CI-LB > 0 (3/3).
- Post-run independent verifier: REPRODUCED-WITH-NOTES (0 material discrepancies).

THE HONEST FENCES already on the result page:
  (a) SINGLE RUN. No fresh-item replication yet.
  (b) The frozen frequency covariate is near-vacuous (R^2 0.002-0.038; UD-EWT per-lemma genitive
      counts too sparse), so the CONFIRM rests on the NONCE arm, not the covariate.
  (c) gpt is the WEAK leg on the firewall: mean +0.055, only 16/24 frames positive, one-sided
      sign-test p = 0.076 — it CLEARS the pre-registered CI-LB rule but marginally.
  (d) The gradient is animate-vs-nonanimate, NOT a smooth 3-level ramp (collective patterns with
      inanimate; graded prediction only weakly supported).
  (e) Direction-only human anchor; no per-item human gradient, no human-level claim; the control is
      "corroboratory, not a proof the distributional shadow is defeated."

YOUR TASK. Given the bar, vote whether this single run should be PROMOTED to a standing claim now.
Address specifically: (a) does surviving a strong shadow control (the nonce firewall) on a SINGLE run
substitute for the replication half of the bar, or not? (b) if not PROMOTE, is a REFUSE-pending-
fresh-item-replication the honest outcome, or is a narrowly-scoped PROMOTE-SCOPED (direction-only,
gpt-weak-leg + covariate-vacuity + single-run flags) defensible by analogy to the dative's
direction-only v1+v2 promotion? (c) name the single cheapest thing that would flip a REFUSE to a
PROMOTE. Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1400)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-promotion-s219.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
