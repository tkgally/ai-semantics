#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s250 FREEZE (pre-run gate) of the DAIS Option-B
graded-preference correlation REP2 -- a FRESH-ITEM REPLICATION of the s248 result. The design is
ratified (s247) and already run once (s248, VERDICT LENGTH-ONLY); the instrument is byte-frozen. This
vote checks the REPLICATION-SPECIFIC choices: (i) is it a genuine fresh-item replication, (ii) is the
frozen replication predicate un-gameable, (iii) does replicating the verb-bias rho license a promotion
review without over-claiming. PROTOCOL sec.2/4: one vote through a non-Anthropic panel model
(panel.B = openai/gpt-5.4-mini), cutoff-aware preamble. QA input to the fresh-agent pre-run critic, who
keeps verdict authority. Writes VOTE-freeze-s250.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-18. You may encounter references to papers, datasets, or models that "
            "postdate your training cutoff. Treat post-cutoff recency as neutral: a paper you do not "
            "recognize is not for that reason fabricated. Where you must rely on what you know, label "
            "it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote on "
       "the PRE-RUN FREEZE of a REPLICATION probe in an autonomous research project on machine vs human "
       "meaning. The original probe is ratified and already run once; this is a fresh-item replication "
       "whose instrument is byte-frozen. Your job is narrow: is this a sound, genuinely-fresh "
       "replication, is its frozen replication predicate un-gameable, and could a weak result be "
       "re-read as a successful replication? Freezing fixes the YARDSTICK before any data is seen; it "
       "never fixes a result. Flag anything that looks motivated by wanting the replication to succeed. "
       "Be terse and adversarial. End with exactly: 'FRESHNESS: <OK|FIX:...>', "
       "'PREDICATE: <OK|FIX:...>', 'PROMOTION: <OK|FIX:...>', then "
       "'OVERALL: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
CONTEXT. The original s248 probe correlated three LLMs' BARE graded double-object preference (DO-pref =
DOC_points/(DOC_points+PD_points), 100 points distributed between "Nadia gave the girl a parcel" and
"Nadia gave a parcel to the girl", no discourse context) against DAIS (50,136 human 0-100 slider
judgments, CC BY 4.0, 200 verbs, recipient definiteness x length). It landed VERDICT LENGTH-ONLY: Arm A
(per-verb verb-bias rho at the matched shortDefinite condition) TRACKED humans 3/3 (matched rho
+0.61/+0.76/+0.63; the binding ALTERNATING-ONLY control survived 3/3, +0.60/+0.70/+0.47 CI-LB>0); Arm B
recipient monotonicity beat chance 3/3 but the binding WITHIN-LENGTH definiteness control FAILED 3/3 at
long length (end-weight-dominated). The Arm-A verb-bias rho is the PROMOTABLE leg; the Arm-B definiteness
surface is a null-leaning LENGTH-ONLY dissociation (not promotable).

THIS REP2. A fresh-item replication. The INSTRUMENT is byte-frozen: probe.py and analyze.py are
sha256-identical to s248; common.py differs ONLY in two budget hard-stop constants. The human targets,
verb list, canonical condition (shortDefinite), 5 factor levels, all statistics/thresholds/bands, and the
B1 null (p0=27/120=0.225) are UNCHANGED. The ONLY thing that changes is the project fillers:
- subject Priya (was Nadia);
- recipients them / the clerk / a clerk / the clerk from downtown / a clerk from downtown (was her / the
  girl / a girl / the girl from college / a girl from college) -- word-count + definiteness matched
  EXACTLY to DAIS's factor levels but lexically disjoint;
- 10 fresh per-bucket theme nouns (crate/boomerang/rebate/fable/alert/confession/hymn/diagram/postcard/
  puzzle), all disjoint from v1's;
- a fresh random 40-verb Arm-B subset (new seed; 16/40 happen to coincide with v1's subset, but every
  SENTENCE is fresh).
TWO firewalls asserted at build, both PASS: 0 rep2 stimulus strings appear among DAIS's released
sentences (B3) AND 0 appear in the committed s248 v1 stimuli (fresh-item firewall); rep2 subject /
recipient realizations / theme heads disjoint from BOTH DAIS and v1.

FROZEN REPLICATION PREDICATE (committed in replication_check.py before any model call). Promotable leg =
Arm-A verb-bias rho. Per model, then >=2/3:
  R1 rep2 matched-rho CI-LB > 0                    (the correlation exists on fresh items)
  R2 rep2 alternating-only rho CI-LB > 0           (the B2 control survives)
  R3 rep2 matched-rho 95% CI OVERLAPS v1's 95% CI  (magnitude consistent with v1)
  VERB-BIAS-REPLICATES := (R1>=2/3) and (R2>=2/3) and (R3>=2/3).
A VERB-BIAS-REPLICATES verdict LICENSES (does not itself perform) a cross-session promotion review that
would write a scoped claim on the VERB-BIAS surface, held distinct from the (untouched) discourse-context
givenness claim. A standing contamination caveat binds: DAIS is public since 2020, per-verb bias is
memorizable under disjoint sentences, so a replicated rho raises confidence in the CORRESPONDENCE's
stability, not in "competence beyond memorized lexical bias"; the promotion review must hold the claim to
direction/correspondence, not a competence gloss. Whether the LENGTH-ONLY band itself replicates is also
reported (non-gating).

YOUR TASK. Vote OK or FIX on:
(a) FRESHNESS: is this a genuine fresh-item replication? Does byte-freezing the instrument while changing
    only the fillers (with both disjointness firewalls) give an independent test of the s248 rho, or is
    16/40 shared Arm-B verbs / identical human targets a problem? (Note: human targets MUST be identical
    -- same human anchor; only model-side items are fresh.)
(b) PREDICATE: is R1 & R2 & R3 (each >=2/3) the right bar for "the verb-bias rho replicated"? Is CI-overlap
    (R3) too lax (two wide CIs always overlap) or about right given per-model bootstrap CIs? Any way a
    weak/degenerate rep2 result could satisfy the predicate and read as a successful replication?
(c) PROMOTION: is it sound for a replication to merely LICENSE (not perform) a separate cross-session
    promotion review? Is the contamination caveat + "direction/correspondence not competence" scoping
    enough to keep a replicated-but-memorizable verb-bias rho from being over-claimed as a scoped claim?
Then the three lines and OVERALL.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=2000)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-freeze-s250.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
