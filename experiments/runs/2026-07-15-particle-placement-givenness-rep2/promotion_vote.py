#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s229 CLAIMS-PROMOTION REVIEW of the verb-particle-placement
object-givenness line (PROTOCOL sec.3 + sec.A3 decorrelation rule).

Two controlled runs on certified-disjoint items (v1 s225/s226 + rep2 s229), both PANEL CONFIRM. The
question is whether to PROMOTE a direction-only, 2/3-firewall particle `claim`, or REFUSE. One vote via
panel.B (openai/gpt-5.4-mini), cutoff-aware preamble prepended. Writes VOTE-promotion-s229.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-15. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote on "
       "whether a replicated behavioral-LLM result line should be PROMOTED to a `claim`. Promotion "
       "fixes the YARDSTICK (the human direction, the firewall control, the pre-registered lower-bound "
       "gate), never the result — the numbers stand either way, so a REFUSE costs nothing. A `claim` is "
       "the project's compounding unit and must not overreach its evidence. Be terse and adversarial: "
       "your job is to catch overreach, not to rubber-stamp. Weigh scope (direction-only vs magnitude; "
       "2/3 vs 3/3), the persistent gpt SHADOW, and whether two same-instrument disjoint-item runs count "
       "as a genuine replication. End with a line 'VOTE: <PROMOTE | PROMOTE-WITH-CONDITIONS | REFUSE>'.")

USER = r"""
THE LINE. English VERB-PARTICLE PLACEMENT (joined "picked up the box" vs split "picked the box up").
Human-attested direction (Kim et al. 2016 / Gries 1999, CC BY 4.0 — a native-speaker DIRECTION
restatement, grounding the SIGN only, not a fresh rating experiment): a definite / discourse-given object
favours the SPLIT order. Indicator = graded forced-choice, hold verb+particle+object-head fixed,
distribute 100 points by naturalness; split-pref = split/(split+joined). Resampling unit = the frame.
Panel = 3 model families (claude-sonnet-4.6, gemini-3.5-flash, gpt-5.4-mini).

THREE ARMS. Arm 1 DEFINITENESS (a/the; confoundable; consistency check only, a reversal blocks CONFIRM).
Arm 2 DISCOURSE-GIVENNESS FIREWALL (LOAD-BEARING): the scored object string is held BYTE-IDENTICAL
("the <noun>") across three context conditions GIVEN / NEW-MENTIONED / NEW; givenness lives only in one
preceding discourse sentence. Decisive contrast = GIVEN − NEW-MENTIONED (holds object-noun lexical
recency constant). Because the two scored order-strings are byte-identical across conditions, ANY
scored-string reader (string-frequency / determiner-collocation / always-split / position) yields
within-frame firewall shift = 0 BY CONSTRUCTION (certified). A positive firewall shift can only come from
integrating referential information structure. Arm 3 LENGTH (short/heavy; convergent-validity, non-gating).

THE TWO RUNS (both frozen, pre-run-critiqued, post-run recompute-verified REPRODUCED; verdict map fixed
before any call; byte-identical instrument sha-verified; items certified disjoint between runs):
- v1 (s225/s226, 40 frames, 1,680 calls, $2.58): PANEL CONFIRM. Firewall GIVEN−NEW-MENTIONED CI-LB>0 in
  2/3 (claude +0.040 [0.022,0.059], gemini +0.072 [0.049,0.095]); definiteness 3/3 consistent, 0
  reversals; length 3/3. gpt SHADOW (firewall +0.018, CI [-0.017,0.055], 18/40).
- rep2 (s229, 48 fresh frames — all triples + all nouns disjoint from v1; firewall arm enlarged 40→48 to
  power the marginal gpt leg; 2,016 calls, $3.18): PANEL CONFIRM again. Firewall CI-LB>0 in 2/3 (claude
  +0.035 [0.019,0.051], gemini +0.057 [0.032,0.080] — BOTH within v1's CIs); definiteness 3/3 consistent,
  0 reversals; length 3/3. gpt SHADOW AGAIN (firewall +0.005, CI [-0.027,0.036], 24/48) — the enlargement
  did NOT pull gpt over; its point estimate is LOWER than v1's. Supplementary robustness (28 unique-pair
  frames; pair-clustered bootstrap) confirms 2/3, verdict unrelabeled.

HONEST FENCES the proposed claim would carry: direction-only (human anchor is a sign-only restatement — no
per-item human gradient, no human-level competence); firewall-borne 2/3 NOT 3/3; gpt a persistent SHADOW
(weakest leg on the dative, marginal on the genitive firewall, SHADOW on the particle firewall twice); the
referential firewall effect is SMALL (~0.035–0.057) vs the strongly-tracked end-weight/length constraint
(+0.31–0.39, 3/3); covariate near-vacuous (R² ≤0.004) so CONFIRM rests on the firewall; behavioral /
stated-preference only, no logprob; same model versions / single lab / n=3; NOT "the distributional
shadow is defeated" (the firewall excludes scored-string shortcuts + lexical recency, not pretraining
joint-distribution mimicry). The 48-frame run reuses 38 verb+particle pairs (10 twice with a fresh
noun+context) — REQUIRED to keep the covariate byte-frozen; the within-frame firewall differences out pair
identity, so pair-reuse cannot carry the effect (disclosed; pair-clustered bootstrap shows negligible
anti-conservatism).

PRECEDENT. The project has promoted three direction-only production/covariation claims on exactly this
"two disjoint-item runs of a byte-frozen instrument + a human-direction anchor" standard: the dative
(givenness), the genitive (possessor animacy, 3/3 firewall), and the comparative-correlative. The genitive
claim is the closest sibling — but its firewall replicated 3/3 (gpt the weakest leg but clearing), whereas
the particle's firewall replicates 2/3 with gpt a persistent SHADOW.

YOUR TASK. Vote PROMOTE / PROMOTE-WITH-CONDITIONS (say exactly what scope/fences) / REFUSE (name the
defect). Address especially: (a) Do two same-instrument, certified-disjoint-item CONFIRM runs meet a
genuine "REPLICATED" bar, or is this "a second sample of the same assay"? (b) Is a 2/3-firewall line (one
of three models a persistent SHADOW) promotable AT ALL as a direction-only claim, or does the SHADOW
member mean the phenomenon is too model-specific to carry a panel claim? (c) Given the effect is SMALL
relative to end-weight and the anchor is a sign-only restatement, is "direction-only, 2/3, gpt-SHADOW,
effect-small, all fences carried verbatim" the right ceiling — or is even that too strong? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1600)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-promotion-s229.json"), "w"), indent=2)
    print("=== PROMOTION VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
