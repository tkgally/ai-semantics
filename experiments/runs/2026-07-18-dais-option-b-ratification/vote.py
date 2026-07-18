#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s247 cross-session ADVERSARIAL RATIFICATION of the
DAIS Option-B graded-preference correlation DESIGN decision
(decisions/open/dais-graded-preference-correlation-design, opened s246). Q1 (contamination-safe
stimulus construction), Q2 (N/arms/cost/split), Q3 (anchor/verdict/promotability).

PROTOCOL sec.2 decorrelation rule: one vote through a non-Anthropic panel model (panel.B =
openai/gpt-5.4-mini), cutoff-aware preamble prepended. This is QA input to the fresh-agent
reviewer, who keeps verdict authority. Writes VOTE-ratify-s247.json.

Ratifying a DESIGN fixes the YARDSTICK (stimulus posture, N/arms, anchor scope, verdict bands),
NEVER a result — the probe is NOT run in this (the ratifying) session. If a preference for a
particular option is motivated by wanting a stronger finding, that is a violation to flag.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-18. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on a cross-session DESIGN-OPERATIONALIZATION decision in an autonomous research project on "
       "machine vs human meaning. The design correlates three current LLMs' graded preference on the "
       "English dative alternation against a verified, CC-BY-licensed human ratings dataset (DAIS). "
       "Ratifying a design fixes the YARDSTICK (the contamination-safe stimulus posture, the N/arms/"
       "cost split, the anchor scope, the verdict bands) BEFORE any data is seen; it NEVER fixes a "
       "result, and the probe is NOT run in this ratifying session. If any option looks attractive "
       "only because it would make a finding look stronger, or would let the dataset anchor a "
       "manipulation it does not measure, that is a violation — flag it. Be terse and adversarial. "
       "End with three lines exactly: 'Q1: <A|B|MODIFY:...>', 'Q2: <A|B|MODIFY:...>', "
       "'Q3: <A|B|MODIFY:...>', then a final line 'OVERALL: <RATIFY | RATIFY-WITH-MODIFICATION | "
       "REJECT | KEEP-OPEN>'.")

USER = r"""
THE LINE. A project claim (CLAIM-GIVENNESS) already shows three current LLMs shift their dative
preference (double-object "gave him the book" vs prepositional "gave the book to him") toward the
double-object form when the RECIPIENT is discourse-GIVEN -- via a byte-identical within-item FIREWALL
(the two scored phrasings held byte-identical across an item's two discourse contexts; the given/new
manipulation lives ONLY in the surrounding context). That claim is anchored on its DIRECTION only
(Bresnan et al. 2007 production corpus); it has NO human EFFECT-SIZE anchor.

THE RESOURCE (DAIS; Hawkins, Yamakoshi, Griffiths & Goldberg 2020; CC BY 4.0; verified firsthand).
50,136 human 0-100 slider judgments over 5,000 dative sentence PAIRS, 200 verbs. DAIS varies the
DEFINITENESS and LENGTH of the recipient on ISOLATED sentence pairs (5 recipient conditions:
pronoun / short-definite / short-indefinite / long-definite / long-indefinite). It has NO discourse-
context given/new manipulation. Human DO-preference falls monotonically pronoun 37.7 > shortDef 30.5
> shortIndef 25.2 > longDef 20.8 > longIndef 18.3 (a ~20-point graded human magnitude). A prior
cross-session ratification (s245) adopted DAIS as a SCOPED SECONDARY companion anchor for the
DEFINITENESS/LENGTH + verb-bias preference surface, EXPLICITLY NOT the discourse-context givenness
shift, and wired it at the CONJECTURE layer (NO claim-level anchor link). It reserved a "human-vs-
model magnitude correlation on DAIS" as a separate powered future unit -- OPTION B.

THE DESIGN UNDER RATIFICATION (Option B, now designed). Correlate the panel's BARE graded DO-
preference (no discourse context, matching DAIS's isolated-pair slider task) against DAIS's human
gradient, in TWO arms:
- ARM A (verb-bias magnitude, n up to 200): per-verb model DO-pref vs human per-verb mean DOpreference,
  Spearman rho. Well-powered. BUT the per-verb gradient is dominated by the Levin alternating vs
  non-alternating split (non-alternating verbs are PO-only, humans floor them on the DO slider), which
  a model can reproduce from lexical subcategorization/verb frequency alone -- NOT graded info-structure
  sensitivity. So a BINDING frequency/classification control (partial rho over verb frequency rank
  and/or restricted to alternating verbs) is required before any "graded sensitivity beyond lexical
  bias" reading.
- ARM B (the definiteness/length preference surface -- DAIS's named grounding): within ~40 alternating
  verbs x 5 recipient conditions, does the panel reproduce the human recipient gradient? Powered
  measure = per-verb MONOTONICITY RATE (fraction of verbs whose model gradient is monotone in the human
  direction), tested against chance; the 5-point rho is a direction check only (n=5, no CI). BUT the 5
  conditions covary length WITH definiteness, so a pure END-WEIGHT/length-only reader reproduces the
  full gradient with ZERO definiteness sensitivity. So a BINDING within-length definiteness control
  (shortDef - shortIndef and longDef - longIndef, length held fixed; human: +5.35 short, +2.47 long)
  is required before a "definiteness-sensitive, not length-counting" reading.

THREE GATES TO RATIFY (fix the yardstick; tighten-not-loosen; nothing run this session):

Q1 -- CONTAMINATION-SAFE STIMULUS CONSTRUCTION (the crux; DAIS public since 2020).
- Q1-A (default): FULLY PROJECT-CONSTRUCTED frames. DAIS supplies only the verb list + human ratings;
  every DOC/PD stimulus is built from PROJECT-chosen theme + recipient fillers instantiating the 5
  factor levels, theme held fixed across conditions; a freeze-time verbatim-disjointness assertion
  confirms no probe stimulus string appears in DAIS's released sentences. Strongest firewall; but the
  stimuli drift furthest from DAIS's exact realizations, so a LOW rho could be "our fillers differ"
  rather than "no surface" -- reported as a fence.
- Q1-B: DAIS verbs + PARAPHRASED DAIS frames. Closer to DAIS items; weaker firewall (paraphrases of
  memorized items still cue the memorized rating).
- Q1-C: DAIS's exact sentences + memorization side-probe. REJECTED up front (lifting sentences is the
  fence; a side-probe cannot un-ring memorization).

Q2 -- N, ARMS, COST, SPLIT (cap is $5/UTC-day; a $2.50 single-run "prefer-split" flag).
- Q2-A (default): Arm A all 200 verbs x 1 canonical condition (600 calls) + Arm B ~40 alternating verbs
  x 5 conditions (600 calls) ~= 1,200 calls ~= $2.6 (above the $2.50 flag), frozen as SEPARABLE runs
  (per-arm hard stop; split across two UTC days if the day's headroom is short, or run as the day's
  only spend on a full-$5 day). Keeps Arm A fully powered where power is cheap; spends the second arm
  on the confound-cleaner definiteness/length surface.
- Q2-B: full 200 x 5 grid on all 3 models (~3,000 calls, ~$6.5). Richest; over cap, unsplittable;
  rejected unless a later session judges it worth two full-$5 days.
- Q2-C: ~12-verb micro-pilot as the claim-carrying N. REJECTED as under-powered; folded into Q2-A as
  the pre-run liveness/format gate only.

Q3 -- ANCHOR, VERDICT MAP, PROMOTABILITY.
- Q3-A (default): anchor=human-anchored, anchors -> resource/dais-dative-ratings, SCOPED to the
  definiteness/length + verb-bias preference surface, NOT the discourse-context givenness shift. TWO
  binding controls (Arm-A frequency/classification; Arm-B within-length definiteness). Verdict bands:
  TRACKS-HUMAN-SURFACE / LENGTH-ONLY / VERB-BIAS-ONLY / SURFACE-ONLY / DECOUPLED / null; a near-perfect
  rho flagged a CONTAMINATION-CEILING (memorization upper bound, not competence); single run -> result
  stays `proposed` (a claim needs a fresh-item replication + a cross-session promotion review, held
  distinct from the givenness claim).
- Q3-B: anchor=internal-contrast-only. REJECTED: this genuinely compares model vs a human rating
  surface; internal-contrast would UNDER-claim.
- Q3-C: promote on this run. REJECTED: a single run is not a promotion.

YOUR TASK. For EACH of Q1/Q2/Q3 vote A / B / MODIFY (say exactly what to change and why). Address
especially:
(a) Is the Q1-A firewall (fully project-constructed stimuli, verbatim-disjointness assertion) genuinely
    the cleanest contamination posture, and is the drift risk adequately fenced -- or does it so decouple
    the stimuli from DAIS's factor realizations that the correlation is measuring the wrong thing?
(b) Does Q2-A buy the right power for the money? Is putting Arm A at ONE canonical condition (200 verbs
    x 1) sound, or does the single-condition choice bias the verb-bias correlation? Is ~40 verbs enough
    for Arm B's monotonicity-rate test against chance?
(c) Is Q3-A's anchor scoping HONEST -- does wiring anchors -> DAIS on the NEW result (not the tested
    givenness claim) correctly keep the scope fence the s245 decision drew? Are the two binding controls
    the right gates, and are the verdict bands pre-committed tightly enough that a weak rho cannot be
    re-read as success? Is CONTAMINATION-CEILING a real fence or a fig leaf?
Then the three Q lines and the OVERALL line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=2000)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s247.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
