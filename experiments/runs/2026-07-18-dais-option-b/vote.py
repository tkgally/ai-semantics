#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s248 FREEZE (pre-run gate) of the DAIS Option-B
graded-preference correlation probe. The DESIGN is already ratified (s247, Q1-A/Q2-A/Q3-A +
B1-B3/S1-S3); this vote checks whether the FROZEN instrument honors the binding freeze conditions
before any model call. PROTOCOL sec.2/4: one vote through a non-Anthropic panel model
(panel.B = openai/gpt-5.4-mini), cutoff-aware preamble. QA input to the fresh-agent pre-run critic,
who keeps verdict authority. Writes VOTE-freeze-s248.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-18. You may encounter references to papers, datasets, or models that "
            "postdate your training cutoff. Treat post-cutoff recency as neutral: a paper you do not "
            "recognize is not for that reason fabricated. Where you must rely on what you know, label "
            "it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote on "
       "the PRE-RUN FREEZE of a behavioral probe in an autonomous research project on machine vs human "
       "meaning. The design is already ratified; your job is narrow: does the FROZEN instrument honor "
       "its binding freeze conditions, and is there any way a weak or confounded result could later be "
       "re-read as success? Ratifying/freezing fixes the YARDSTICK before any data is seen; it NEVER "
       "fixes a result, and if any choice looks motivated by wanting a stronger finding, flag it. Be "
       "terse and adversarial. End with exactly: 'B1: <OK|FIX:...>', 'B2: <OK|FIX:...>', "
       "'B3: <OK|FIX:...>', 'BANDS: <OK|FIX:...>', then 'OVERALL: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
THE PROBE. Correlate three current LLMs' BARE graded double-object preference (DO-pref = DOC_points/
(DOC_points+PD_points); distribute 100 points between "Nadia gave the girl a parcel" and "Nadia gave a
parcel to the girl", no discourse context) against a verified CC-BY human dataset (DAIS: 50,136 human
0-100 slider judgments, 200 verbs, recipient definiteness x length varied on isolated pairs). Two arms:
- ARM A (verb-bias, 200 verbs x 1 canonical condition=shortDefinite "the girl" x 3 models = 600 calls):
  Spearman rho(model per-verb DO-pref, human per-verb mean) at the MATCHED condition. Human per-verb
  gradient is dominated by the Levin alternating(100)/non-alternating(100) split.
- ARM B (definiteness/length surface, 40 random alternating verbs x 5 conditions x 3 models = 600 calls):
  per-verb monotonicity rate + within-length definiteness contrast.

FROZEN CHOICES honoring the ratified BLOCKERS (stimuli.json sha pinned in PREREG before any call):

B1 (pin the Arm-B monotonicity predicate + chance null). SUCCESS(verb) := Spearman rho_s(model's 5
condition-mean DO-prefs, human direction ranks 5>4>3>2>1) >= +0.50; an all-tied verb = non-success.
NULL p0 := P(rho_s >= 0.50 | 5 means a uniform random permutation) = 27/120 = 0.225 (exact over 120
perms). Powered measure = per-model monotonicity RATE over 40 verbs, one-sided binomial H0: rate<=0.225,
"beats chance" = p<0.05 (needs >=14/40 = 35%; power >=0.98 at true rate>=0.50). The 5-point marginal rho
is a direction check only.

B2 (frequency/classification control = a CONJUNCT of the flagship TRACKS label, not a side-caveat). The
binding control = ALTERNATING-ONLY rho (restrict to the 100 alternating verbs, removing the
subcategorization split) with a bootstrap CI; TRACKS requires alternating-only rho CI-LB>0 on >=2/3
models. A full-rho that clears but whose control fails earns only "VERB-BIAS-ONLY (may be lexical)". A
partial rho | classification + within-class freq rank is also reported.

B3 (disjointness at the recipient-lexicalization level + fidelity audit). Project recipient
realizations her / the girl / a girl / the girl from college / a girl from college -- word-count and
definiteness matched EXACTLY to DAIS's factor levels him / the man / a man / the man from work / a man
from work, but lexically disjoint. Mechanically asserted at build: 0 of 400 project stimulus strings
appear among DAIS's 10,000 released sentences; no project theme head-noun sits in DAIS's 333 theme
heads; subject "Nadia" disjoint from DAIS's 8 subjects. A fidelity-audit table pins each condition.

BANDS (deterministic decision-tree; armX flags are >=2/3-of-3-models):
  if armB_mono and armB_within: TRACKS-HUMAN-SURFACE if (armA_full_ci_lb>0 and armA_alt_control) else SURFACE-ONLY
  elif armB_mono and not armB_within: LENGTH-ONLY
  elif armA_full and not armB_mono: VERB-BIAS-ONLY (+"may be lexical" if control fails)
  else: DECOUPLED-OR-NULL
  + CONTAMINATION-CEILING flag if any matched-rho >= 0.95 (rho read as memorization upper bound). A
  standing contamination caveat binds any non-null band (per-verb bias is memorizable under disjoint
  sentences). Single run -> result stays `proposed`; anchor scoped to the definiteness/length + verb-bias
  surface, NOT the tested discourse-context givenness claim.

YOUR TASK. Vote OK or FIX on each of B1, B2, B3, BANDS. Address especially:
(a) B1: is p0=0.225 the correct chance baseline for the rho_s>=0.5 predicate, and is treating all-tied
    verbs as non-successes right? Any way the monotonicity rate could beat chance without real
    definiteness/length tracking?
(b) B2: is ALTERNATING-ONLY rho the right binding control, and is making it a TRACKS conjunct enough to
    stop a memorized subcategorization split from earning the flagship label?
(c) B3: does word-count+definiteness-matched-but-lexically-disjoint recipient construction faithfully
    instantiate DAIS's factor while keeping the contamination firewall? Does holding the theme fixed and
    letting it cancel between DOC/PD introduce any asymmetry?
(d) BANDS: is the decision-tree exhaustive and un-gameable -- can a weak/confounded result land in a
    band that reads as success? Is CONTAMINATION-CEILING a real fence or a fig leaf here?
Then the four lines and OVERALL.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=2000)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-freeze-s248.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
