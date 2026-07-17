#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s245 cross-session ADVERSARIAL RATIFICATION of the
DAIS graded-acceptability anchor decision (decisions/open/dais-dative-rating-anchor, opened s244).

PROTOCOL sec.2 decorrelation rule: one vote through a non-Anthropic panel model (panel.B =
openai/gpt-5.4-mini), cutoff-aware preamble prepended. This is QA input to the fresh-agent
reviewer, who keeps verdict authority. Writes VOTE-ratify-s245.json.

Ratifying an anchor fixes the YARDSTICK (which human surface DAIS grounds + the scope note),
never a result — no result moves under the default. If a preference for a particular option is
motivated by wanting a stronger finding, that is a violation to flag.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-17. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on a cross-session ANCHOR-ADOPTION decision in an autonomous research project on machine "
       "vs human meaning. The question is whether to adopt a verified, licensed human-ratings "
       "dataset (DAIS) as a SCOPED SECONDARY human anchor for one behavioral claim's "
       "graded-acceptability leg. Ratifying an anchor fixes the YARDSTICK (which human surface the "
       "dataset grounds, and the exact scope wording), NEVER a result: no experimental result "
       "moves under the default option, and no probe is run in this session. If any option looks "
       "attractive only because it would make a finding look stronger, that is a violation — flag "
       "it. Your job is to catch OVER-CLAIM: any wording that would let this dataset anchor a "
       "manipulation it does not actually measure. Be terse and adversarial. End with a line "
       "'VOTE: <ADOPT-A | ADOPT-A-WITH-MODIFICATION | ADOPT-OTHER | KEEP-OPEN>'.")

USER = r"""
THE LINE. A behavioral claim (call it CLAIM-GIVENNESS) states: three current LLMs, on the English
DATIVE ALTERNATION (double-object "gave him the book" vs prepositional "gave the book to him"),
shift their production preference toward the double-object form when the RECIPIENT is discourse-GIVEN
and toward the prepositional form when the THEME is given -- the human-attested information-structure
direction. The decisive control is a byte-identical within-item FIREWALL: the two scored phrasings are
held byte-identical across an item's two discourse contexts, and the given/new manipulation lives ONLY
in the surrounding context sentence, so any length/order/position shortcut yields shift=0 by
construction. The claim is human-anchored on its DIRECTION leg only, via the Bresnan et al. (2007)
`languageR::dative` PRODUCTION corpus (which codes recipient/theme accessibility -> realization). The
claim states PLAINLY that it has NO per-item human ACCEPTABILITY rating and NO human EFFECT-SIZE anchor
for the effect; a graded-rating upgrade (Bresnan & Ford 2010) was ratified an "opportunistic upgrade
only, not a precondition" and was never used.

THE NEW RESOURCE (DAIS; Hawkins, Yamakoshi, Griffiths & Goldberg 2020, EMNLP; CC BY 4.0, verified
firsthand last session). 50,136 human slider judgments over 5,000 dative sentence PAIRS, 200 verbs.
Each judgment is a graded 0-100 preference between the DO and PO phrasings of the SAME proposition
(0=strong PO, 100=strong DO). CRUCIAL DESIGN FACT: DAIS varies the DEFINITENESS and LENGTH of the
recipient/theme on ISOLATED sentence pairs (5 recipient conditions: pronoun / short-definite /
short-indefinite / long-definite / long-indefinite). It does NOT carry a discourse-CONTEXT given/new
manipulation. Firsthand, the human DO-preference falls monotonically pronoun 37.7 > shortDef 30.5 >
shortIndef 25.2 > longDef 20.8 > longIndef 18.3 -- a ~20-point graded human magnitude in the same
directional family (given-like recipients raise DO preference).

THE DECISION. Adopt DAIS as an anchor for CLAIM-GIVENNESS, and if so exactly how? Options:
- OPTION A (provisional default): ADOPT DAIS as a SECONDARY graded-acceptability COMPANION anchor
  (alongside, not replacing, the Bresnan production anchor). Its scoped force: it grounds the graded
  VERB / ARGUMENT-DEFINITENESS PREFERENCE SURFACE (a per-item human acceptability gradient + a human
  effect-size), EXPLICITLY NOT the project's discourse-context givenness shift (which stays anchored
  to the production DIRECTION only). Mechanics: add a new `anchors:` typed link from CLAIM-GIVENNESS
  to the DAIS resource page WITH a one-paragraph scope note; soften the claim's "no human effect-size
  anchor" sentence to "no human effect-size anchor FOR THE DISCOURSE-CONTEXT GIVENNESS SHIFT; a graded
  human preference surface for verb/argument-definiteness is available via DAIS." No result changes; no
  probe required (an anchor-catalogue upgrade, like B&F 2010's ratified status). A future OPTIONAL
  probe could correlate model per-verb DO-preference against the DAIS human gradient -- OUT OF SCOPE
  here.
- OPTION B: as A, but also BIND a follow-up powered probe now (run the panel on a DAIS-derived stimulus
  set, report a human-vs-model Spearman correlation). Heavier: needs a frozen design, pre-run critic,
  powered N, and spend; inherits a contamination caution (DAIS public since 2020). NOTE: project rule
  bars running that probe in THIS (the ratifying) session.
- OPTION C: CATALOGUE ONLY -- do not wire DAIS as an anchor to any claim; the instrument mismatch means
  it does not ground the actual within-item givenness probe, and adding it invites production/
  acceptability conflation. Claim's honest "no acceptability / no effect-size anchor" stays as-is.
- OPTION D: DECLINE -- demote the resource page to a mere source note.

THREE FENCES THE RATIFICATION MUST HOLD (from the decision page):
1. INSTRUMENT MISMATCH. DAIS varies definiteness/length on ISOLATED pairs; the project probe
   manipulates discourse-context GIVENNESS on byte-identical phrasings. Definiteness/length are CUES TO
   information status but are NOT the context-driven given/new manipulation. So DAIS must not be allowed
   to anchor the within-item givenness shift.
2. MEASURE MISMATCH. Slider PREFERENCE != corpus PRODUCTION probability (correlated, not identical).
   Adoption must not blur the production/acceptability distinction.
3. CONTAMINATION. DAIS public since 2020; any USE must anchor the factor->rating relation, not lift
   DAIS sentences as probe stimuli.

YOUR TASK. Vote ADOPT-A / ADOPT-A-WITH-MODIFICATION (say exactly what wording/mechanics change) /
ADOPT-OTHER (name it) / KEEP-OPEN (name what's missing). Address especially:
(a) Is Option A's scoping HONEST, or does adding an `anchors:` typed link FROM the givenness claim TO
    DAIS -- when the claim's actually-TESTED force is the discourse-givenness shift, which DAIS does NOT
    measure -- risk implying (to a reader or a machine-read link graph) that DAIS anchors the tested
    effect? Is a scope note enough to fence a blunt front-matter link, or is the cleaner wiring to
    record DAIS's adoption on the RESOURCE page + soften the claim's prose WITHOUT a load-bearing
    `anchors:` link on the claim?
(b) Does Option A over-use or under-use the resource relative to C? Is "the graded verb/argument-
    definiteness preference surface" a real thing DAIS grounds for THIS claim, given the claim tests
    neither verb-class nor definiteness/length but discourse context?
(c) Is deferring the human-vs-model magnitude COMPARISON (Option B) to a separate powered session the
    right call, or is adopting-without-comparing an empty gesture?
Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1800)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s245.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
