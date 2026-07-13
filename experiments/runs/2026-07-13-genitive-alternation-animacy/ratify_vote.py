#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s218 RATIFICATION of
decisions/open/genitive-alternation-anchor-and-indicator (PROTOCOL sec.2 decorrelation rule).

QA input to the fresh-agent reviewer's verdict (who keeps authority). One vote via panel.B
(openai/gpt-5.4-mini), cutoff-aware preamble prepended. Writes VOTE-ratify-s218.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-13. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether to RATIFY a value-laden methodological decision for a behavioral LLM experiment. "
       "Fixing the decision fixes the YARDSTICK, never the result; a null is a first-class outcome. "
       "If you would prefer a different option only because it would make a positive result more "
       "likely, that is a violation — flag it. Be terse and adversarial. End with a line "
       "'VOTE: <ADOPT-DEFAULTS | ADOPT-WITH-MODIFICATION | KEEP-OPEN>'.")

USER = r"""
CONTEXT. A research project probes whether current LLMs track the English GENITIVE alternation's
possessor-animacy constraint: animate possessors favour the s-genitive ("the judge's decision"),
inanimate favour the of-genitive ("the decision of the court") — a native-speaker acceptability
direction from an openly-licensed 25-speaker rating study (Dubois et al. 2023). The instrument is a
graded forced-choice: hold the possessum fixed, distribute 100 points by naturalness between the two
phrasings; s-pref = s_pts/(s_pts+of_pts); within-frame shift = s-pref(animate) - s-pref(inanimate);
human direction => shift > 0.

THE THREE SUB-QUESTIONS + PROVISIONAL DEFAULTS to ratify:

Q1 FOCAL CONSTRAINT. Default A = possessor animacy (strongest, best human-anchored genitive
constraint). Alternatives: B = end-weight (a processing/length effect, easier to separate from
surface frequency but lower value / less semantic); C = a different alternation (particle placement,
locative) lacking an in-repo openly-licensed native-speaker anchor.

Q2 INDICATOR + SHADOW CONTROL (the crux). Default (i) = graded forced-choice. The load-bearing worry:
because the two scored phrasings differ in the possessor word across animacy conditions, an
animate->s-genitive shift could be a mere shadow of the higher corpus frequency of animate-possessor
s-genitive strings. The control is hardened by a prior pre-run critic into THREE parts:
  B1: the shortcut-immune PRIMARY arm uses RARE/NONCE possessor lemmas (not novel possessum pairings
      on common possessors — those leave the possessor's MARGINAL "P(takes-'s | possessor)" channel,
      which is collinear with animacy, fully intact).
  B2: ONE frozen sha'd covariate = possessor-lemma MARGINAL s-genitive-vs-of-genitive propensity
      (not joint co-occurrence), from a license-verified corpus; analyze.py partials it out. Power is
      bounded by corpus size (a corroboration arm).
  B3: a PRE-REGISTERED CONFIRM-vs-SHADOW independence rule: CONFIRM requires shift>0 with bootstrap
      lower bound>0 in >=2/3 models AND the animacy CI with the marginal covariate included still
      excludes zero (>=2/3) AND the rare/nonce atypical-arm shift lower bound>0 (>=2/3); else SHADOW.
  Plus: possessor length + final sibilancy + definiteness matched across animacy conditions; bare
  proper-name possessors excluded; A/B counterbalanced; a collective mid-animacy level.

Q3 ANCHOR POSTURE. Default = human-anchored on the DIRECTION only (native-speaker sign fact); the
per-item human gradient is deferred to a separate license-verified dataset scout (the corpus, TLC, is
controlled). May NOT claim human-LEVEL competence, nor beating the distributional shadow unless the
controls clear it.

YOUR TASK. Vote ADOPT-DEFAULTS / ADOPT-WITH-MODIFICATION (say exactly what changes) / KEEP-OPEN (name
the specific gap). Address especially: (a) is animacy the right FIRST constraint given it is the most
frequency-collinear? (b) do B1-B3 actually close every way a no-animacy surface reader could score a
spurious CONFIRM, or is there a residual cheat-surface? (c) is direction-only human-anchoring honest
given there is no licensed per-item gradient? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1400)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s218.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
