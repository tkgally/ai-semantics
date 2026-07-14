#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s224 PRE-RUN CRITIQUE of the A5 THIRD-SIBLING design:
verb-particle placement object-givenness probe (PROTOCOL sec.A3 decorrelation rule).

A NEW decision is opened this session (particle-placement-anchor-and-indicator); this vote is QA input
to the s225+ cross-session ratification, NOT the ratification. One vote via panel.B (openai/gpt-5.4-mini),
cutoff-aware preamble prepended. Writes VOTE-critic-s224.json. No probe runs this session.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-14. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote on "
       "whether a PROVISIONAL behavioral-LLM probe DESIGN and its open operationalization decision are "
       "sound to RATIFY-then-RUN in a later session. You are NOT ratifying (a later fresh agent does "
       "that); you are QA input. Judge the OPERATIONALIZATION: focal constraint, indicator, the "
       "shadow/shortcut control, anchor posture, and every way the design could manufacture a positive "
       "or a misleading verdict. Ratifying fixes the YARDSTICK, never the result; a null (no effect, or "
       "an effect that fails the shortcut control) is a first-class outcome. If you would prefer a change "
       "only because it would make a larger/cleaner positive more likely, that is a violation — flag it. "
       "Be terse and adversarial. End with a line 'VOTE: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
CONTEXT. Program A5 is a battery of English production-side ALTERNATIONS, each probing whether a panel of
3 LLMs tracks a soft human production constraint in the human direction, on synthetic held-out items, via
a graded forced-choice (distribute 100 points by naturalness between two phrasings of the SAME
proposition; parser target-blind; A/B counterbalanced; bootstrap over "frames"). Two siblings are landed
and promoted: the DATIVE (given recipient -> recipient-first) and the GENITIVE (animate possessor ->
s-genitive). This design is the THIRD sibling: English VERB-PARTICLE PLACEMENT, "picked up the box"
(JOINED, V-Prt-DO) vs "picked the box up" (SPLIT, V-DO-Prt).

FOCAL CONSTRAINT (Q1-A default): object INFORMATION-STATUS (givenness), primary contrast = DEFINITENESS.
Human direction (anchor: Kim et al. 2016 PACLIC, CC BY 4.0, restating Gries 1999's synthesis of the
native-speaker literature, verbatim): a DEFINITE/given object favours SPLIT; an INDEFINITE/new object
favours JOINED. Also anchored: SHORT object -> SPLIT, LONG -> JOINED (a convergent leg). This is the SAME
information-structural driver as the dative, on a new construction -> a cross-construction generalization
test.

INDICATOR (Q2-(i) default): graded forced-choice, split-pref = split_pts/(split_pts+joined_pts); verb +
particle + object head-noun held fixed.

THREE ARMS:
- Arm 1 DEFINITENESS (primary human-direction contrast): "a box" vs "the box", everything else identical;
  shift1 = split-pref(definite) - split-pref(indefinite); human dir shift1 > 0. CONFOUND: the two
  conditions differ by determiner, so shift1 could be a shadow of the higher surface frequency of
  definite-object split-order strings.
- Arm 2 DISCOURSE-GIVENNESS FIREWALL (load-bearing shortcut control): object string held BYTE-IDENTICAL
  ("the box" in both), information status manipulated ONLY in a preceding discourse context (given =
  referent previously mentioned/topical; new = unmentioned). The two scored order-strings ("picked up the
  box" / "picked the box up") are BYTE-IDENTICAL across the given/new conditions. shift2 =
  split-pref(given) - split-pref(new). CLAIM: any always-split/always-joined/string-frequency/determiner-
  collocation reader gives shift2 = 0 BY CONSTRUCTION (identical strings), so a positive shift2 can only
  come from integrating the discourse context = information structure. The CONFIRM RESTS ON ARM 2.
- Arm 3 LENGTH (convergent-validity leg, secondary): short vs long object; shift3 > 0 expected.

SHADOW CONTROL. The byte-identical firewall (Arm 2) is the primary shortcut control (no scored-string
statistic can produce shift2 != 0). A frozen surface-collocation covariate (verb+particle split-rate from
UD-English-EWT, CC BY-SA) is reported as corroboration only and EXPECTED NEAR-VACUOUS (sparse in a small
corpus), stated honestly.

PRE-REGISTERED CONFIRM-vs-SHADOW RULE: shift1 CI-LB>0 (>=2/3 models) AND firewall shift2 CI-LB>0 (>=2/3),
else SHADOW. Symmetric verdict frame: CONFIRM / SHADOW / WEAK (length leg fails) / FALSIFY (no shift or
reversal).

GUARDS: object length/type(full lexical NP - NO pronouns, which are near-categorically split)/concreteness
/animacy/VP-idiomaticity held constant across conditions; GIVEN vs NEW discourse contexts matched in
length + lexical content EXCEPT the givenness manipulation; A/B counterbalanced; bootstrap over frames;
N powered in FRAMES with the firewall arm >= the definiteness arm; item set frozen (sha256) before any
call; no attested example sentences lifted (contamination).

ANCHOR POSTURE (Q3-default): human-anchored on the DIRECTION ONLY. Honesty caveat carried from the source:
the Kim et al. anchor is a RESTATEMENT of the established native-speaker direction (via Gries 1999),
corroborated on the paper's own native ICE-GB corpus, NOT a fresh rating experiment like the genitive's
Dubois (25 raters). So it grounds the SIGN only; per-item human gradient is license-UNVERIFIED (verified
null) and deferred. May NOT: human-level competence; "shadow defeated" unless the firewall clears; cross-
linguistic claims.

YOUR TASK. Vote GO / GO-WITH-CONDITIONS (say exactly what changes) / NO-GO (name the specific defect).
Address especially: (a) is the byte-identical discourse-givenness firewall (Arm 2) GENUINELY shortcut-
immune, or is there a channel by which a model with no information-structural competence scores a spurious
positive shift2 (e.g., lexical PRIMING / mere-mention of the object noun in the given context biasing
order independent of referential givenness; a positional/recency artifact; the given-context sentence
leaking a syntactic cue)? What authoring constraint on the GIVEN vs NEW contexts closes that channel? (b)
is leaning the CONFIRM on Arm 2 (rather than the corpus covariate) the right call given the covariate is
expected near-vacuous, or does that over-rely on a single arm? (c) is object-givenness (re-testing the
dative's driver on a new construction) the right FOCAL constraint, or is length (a fresh non-dative
driver) the more informative first cut? (d) is "human-anchored on the direction, anchor-is-a-restatement"
honest, or should this be internal-contrast-only with Kim as external corroboration? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1800)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-critic-s224.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
