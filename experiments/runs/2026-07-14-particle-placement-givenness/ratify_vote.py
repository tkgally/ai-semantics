#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s225 RATIFICATION of the A5 THIRD-SIBLING
open decision: particle-placement-anchor-and-indicator (PROJECT.md sec.12.3 cross-session
adversarial review). ONE vote via panel.B (openai/gpt-5.4-mini), cutoff-aware preamble.

This vote is INPUT the fresh-agent ratification reviewer weighs; it is NOT the ratification.
Writes VOTE-ratify-s225.json. No probe runs at the ratification step.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-14. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote on "
       "whether to RATIFY the OPERATIONALIZATION of a behavioral-LLM probe design. Ratifying fixes the "
       "YARDSTICK (focal constraint, indicator, shadow/shortcut control, anchor posture), NEVER the "
       "result: a null (no effect, or an effect that fails the shortcut control) is a first-class "
       "outcome. Judge whether the yardstick is sound and honest. If you would prefer a change only "
       "because it would make a larger/cleaner positive more likely, that is a violation — flag it. "
       "Be terse and adversarial. Address Q1/Q2/Q3 below explicitly, then end with a line "
       "'VOTE: <ADOPT-DEFAULTS | ADOPT-WITH-MODIFICATION | REJECT>'.")

USER = r"""
CONTEXT. Program A5 is a battery of English production-side ALTERNATIONS, each probing whether a panel of
3 LLMs tracks a soft human production constraint in the human direction, on synthetic held-out items, via
a graded forced-choice (distribute 100 points by naturalness between two phrasings of the SAME
proposition; parser target-blind; A/B counterbalanced; bootstrap over "frames"). Two siblings are landed
and promoted: the DATIVE (given recipient -> recipient-first) and the GENITIVE (animate possessor ->
s-genitive). This is the THIRD sibling: English VERB-PARTICLE PLACEMENT, "picked up the box" (JOINED,
V-Prt-DO) vs "picked the box up" (SPLIT, V-DO-Prt). It was designed in a PRIOR session (s224); a pre-run
critic there returned GO-WITH-CONDITIONS and one prior decorrelation vote returned NO-GO. The prior
BLOCKER (context->string leakage in the firewall) was FOLDED into the design via a third condition (see
Q2). You are voting fresh on whether the yardstick is now sound to RATIFY.

Q1 -- FOCAL CONSTRAINT (default: adopt A). Object INFORMATION-STATUS (givenness), primary contrast =
DEFINITENESS. Human direction (anchor: Kim et al. 2016 PACLIC, CC BY 4.0, restating Gries 1999's synthesis
of the native-speaker literature, verbatim): DEFINITE/given object -> SPLIT; INDEFINITE/new -> JOINED.
Also anchored: SHORT object -> SPLIT (a convergent leg). This re-tests the DATIVE's information-structural
driver on a NEW construction (a cross-construction generalization test). ALTERNATIVE considered and
rejected: length as a fresh non-dative driver -- rejected because only GIVENNESS affords the byte-identical
firewall below (length would reintroduce a lexical difference across conditions and forfeit the
shortcut-immune leg). Is object-givenness the right focal constraint, or is that a rigor loss?

Q2 -- INDICATOR + SHADOW CONTROL (the crux). Indicator: graded forced-choice, split-pref =
split_pts/(split_pts+joined_pts); verb + particle + object head-noun held fixed. THREE ARMS:
- Arm 1 DEFINITENESS (anchor-exact, CONFOUNDABLE, NOT decisive): "a box" vs "the box"; shift1 =
  split-pref(definite) - split-pref(indefinite). Confound: determiner differs -> could be a surface
  shadow. Role: consistency check only (directional-consistency required, NOT a hard CI gate).
- Arm 2 DISCOURSE-GIVENNESS FIREWALL (byte-identical scored strings, LOAD-BEARING, THREE conditions):
  object string held BYTE-IDENTICAL ("the box") across all conditions; information status manipulated ONLY
  in a preceding discourse context. Conditions: GIVEN (referent previously mentioned + topical);
  NEW-MENTIONED (object NOUN appears in context at matched recency but as a referentially-NEW,
  non-coreferential entity); NEW (unmentioned). DECISIVE contrast = GIVEN - NEW-MENTIONED, which holds the
  object noun's lexical priming/recency CONSTANT and varies only referential givenness -> a positive
  GIVEN-NEW-MENTIONED shift cannot be the "noun was just in context -> split" lexical-recency heuristic. The
  two scored order-strings are byte-identical across every condition, so any string-frequency/collocation/
  always-split/always-joined reader gives shift2 = 0 BY CONSTRUCTION. CONFIRM RESTS ON ARM 2.
- Arm 3 LENGTH (convergent-validity leg, secondary): short vs long object; shift3 > 0 expected.
The GIVEN / NEW-MENTIONED / NEW contexts are matched on genre, clause count, sentence type, verb lemmas,
punctuation, and length, differing ONLY in the prior-mention/referential-status manipulation, with NO
fronting/clefting/topicalization/heavy-NP/passive cue -- and this parallelism is INDEPENDENTLY certified
before freeze (non-authoring agent + this vote), not lead-agent self-audit alone. A frozen
surface-collocation covariate (verb+particle split-rate from UD-English-EWT, CC BY-SA) is corroboration
only and expected NEAR-VACUOUS (sparse), stated honestly. PRE-REGISTERED ASYMMETRIC CONFIRM RULE: firewall
shift2 (GIVEN-NEW-MENTIONED) CI-LB>0 (>=2/3 models) NECESSARY+PRIMARY; Arm 1 need only be directionally
consistent. Symmetric verdict frame: CONFIRM / SHADOW (shift2 fails) / WEAK (length leg fails) / FALSIFY.
Is the three-condition byte-identical firewall genuinely shortcut-immune now, and is leaning CONFIRM on
Arm 2 (not the near-vacuous covariate) the right call?

Q3 -- ANCHOR POSTURE (default: human-anchored on the DIRECTION only). The direction (definite/given ->
split) is a native-speaker fact from Kim et al. 2016 / Gries 1999. HONESTY CAVEAT carried from the source:
this anchor is a RESTATEMENT of the established native-speaker direction (corroborated on the paper's own
native ICE-GB corpus), NOT a fresh rating experiment like the genitive's Dubois (25 raters). So it grounds
the SIGN only; per-item human gradient is license-UNVERIFIED (verified null) and deferred. May NOT:
human-level competence; "shadow defeated" unless the firewall clears; cross-linguistic claims. Is
"human-anchored on the direction, anchor-is-a-restatement" honest, or should this be internal-contrast-only
with Kim as external corroboration (which the prior fresh critic argued would UNDER-claim a genuine
license-verified anchor)?

YOUR TASK. For each of Q1/Q2/Q3 say adopt / modify (say exactly what) / reject (name the defect). Focus on:
is the three-condition firewall now shortcut-immune (any residual channel by which a model with no
information-structural competence scores a spurious positive GIVEN-NEW-MENTIONED shift)? Is the asymmetric
CONFIRM rule sound or does it manufacture a positive? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=2000)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s225.json"), "w"), indent=2)
    print("=== RATIFY VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
