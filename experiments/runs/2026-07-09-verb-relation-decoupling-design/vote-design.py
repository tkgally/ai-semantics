#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s198 DESIGN of the verb-relation decoupling probe
(PROTOCOL §2/§A3). One vote through the non-Anthropic slot via the probe REST path.
QA input to the fresh-agent design critic's verdict — NOT authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer. Your training cutoff may "
            "predate this project; treat post-cutoff papers/datasets/models as neutral, not "
            "fabricated. Judge the design below on its internal merits; be adversarial and terse.")

DESIGN = """We are reviewing (NOT ratifying) the DESIGN of a frozen-but-not-yet-run behavioral probe.
It is internal-contrast (NO human comparison). It is the DECISIVE test of a registered conjecture.

BACKGROUND (three prior internal-contrast runs, relatum-production over WordNet relations, panel of 3
frontier models, temp 0, scored vs WordNet with Soundness + HIT@3):
  - NOUNS: raw contrastive-frame co-occurrence (G2) cue-strength does NOT rank-predict which relation
    the panel recovers best (across-relation Spearman rho_cue ~ -0.09 at s186, +0.09 at s193; twice
    replicated -> now a nouns-only 'claim'). s193 diagnosed WHY: hypernymy, a LOW-cue-strength but
    taxonomically CENTRAL relation, is the best-recovered, scrambling recovery rank vs cue-strength;
    a pre-registered IS-A path-depth proxy out-predicts cue-strength 2/3 models (H2).
  - ADJECTIVES (s196): the decoupling did NOT replicate (rho_cue +0.4/+0.8/+0.4; item-level ~+0.25) --
    cue-strength regains predictive traction. Reason: adjectives have NO IS-A taxonomy (WordNet
    min_depth() is a degenerate constant 0), so no central low-cue relation to scramble the order; H2
    was UNCOMPUTABLE. So the cross-POS decoupling claim is BLOCKED.
  - The conjecture (registered s197): the decoupling is the SIGNATURE OF A LEXICAL HIERARCHY -- it
    reappears in any POS with an IS-A-like backbone, vanishes without one.

WHY VERBS ARE DECISIVE: nouns and adjectives differ on BOTH axes at once (hierarchy+decoupling vs
neither), so they can't separate 'has a hierarchy' from other noun/adjective differences. VERBS have a
real hierarchy (TROPONYMY: 'to whisper is to talk in a manner') but are a different POS. Verified this
session (nltk WordNet 3.0 + SubTLEX Lg10WF band [2.0,4.5], excluding all 1740 prior cue lemmas as a
homograph guard): fresh in-band cue counts hypernymy 2006, synonymy 1448, troponymy 1136, entailment
242, antonymy 140, cause 126, verbgroup 429 (near-synonym), alsosee 0 (unusable). Verb min_depth() is
NON-DEGENERATE (0-11, 12 distinct values) -> H2's depth proxy IS computable here, unlike adjectives.

THE PROBE: relatum-production over WordNet VERB relations, fresh cues disjoint from all prior sets,
freq-matched, outlier-capped; contrastive-frame G2 control BYTE-FROZEN from s193's build_cooc (only cue
POS changes) on C4 web text; a pre-registered TROPONYMY-DEPTH proxy (min_depth of the cue's first verb
synset, predicted sign NEGATIVE) frozen before recovery. Two verdict-bearing clauses:
  H-verb-1 (decoupling): across-relation rho_cue near-zero/negative (<= +0.30, >=2/3) = REAPPEARS
    (hierarchy=>decoupling confirmed out of nouns); clearly positive (>= +0.50, >=2/3) = BREAKS
    (falsifies the conjecture's central identification despite the verified verb hierarchy). [+0.30,+0.50]
    pre-registered as an explicit INCONCLUSIVE band broken by a powered item-level arm.
  H-verb-2 (mechanism): troponymy-depth OUT-PREDICTS cue-strength on recovery rank (|rho_depth|-|rho_cue|
    >= 0.20, predicted-negative, >=2/3) = the noun H2 becomes a TWO-POS pattern; else DEPTH-FAILS.

THREE GATES to review (options; provisional defaults in [brackets]):

Q1 - verb relation inventory + registered primary clause.
   A: 4-relation taxonomic core {hypernymy, troponymy, synonymy, antonymy} (drops entailment; 4 pts)
   B: 6-relation add {entailment, cause} (max spread but cause binds at floor 126, may drop after matching)
   [C]: 5-relation {hypernymy, troponymy, synonymy, entailment, antonymy}; H1 decoupling = registered
        PRIMARY, H2 troponymy-depth = registered CO-PRIMARY; powered item-level (~600 cues) SECONDARY
        descriptive-only; 'cause' added as a 6th ONLY if it survives freq-matching at >=100 cues
        (mechanical rule, pre-registered either way). Unlike the adjective probe where the thin inventory
        forced the antonymy-shadow clause to primary, here H1 IS the headline (the conjecture's decisive
        test) and 5 relations is an adequate rank test.

Q2 - the troponymy-depth proxy spec (H2 DOES transfer -- verbs have a real hierarchy).
   [A]: min_depth over the cue's first VERB synset (byte-analogous to the noun proxy, pos='v'), single
        frozen proxy, predicted sign negative. Keeps a verb confirmation a genuine REPLICATION of the
        noun mechanism.
   B: a richer/multi proxy (mean min_depth over senses, or troponym-branching centrality) -- more bets,
      multiple-comparison burden, breaks the like-for-like parallel.
   C: a corpus troponymy-'Hearst'-frame arm -- REJECTED up front (verb troponymy has no clean 'X such as
      Y' frame; the s193 nominal Hearst arm LOST even where well-motivated).

Q3 - anchor: [internal-contrast-only]. Recovery scored vs WordNet as a shared target that CANCELS in the
     contrast; predictors (contrastive-frame G2, troponymy-depth) are corpus/lexicon statistics; no human
     baseline.

ANTI-CHEAT: every cue set, outlier cap, k, relation inventory (incl. the cause-inclusion rule), depth
proxy, rho_cue bands, rho_depth margin, and calibration floor is frozen in PREREG before ANY model call;
DECOUPLING-BREAKS, DEPTH-FAILS, and both-null are all pre-named first-class outcomes.

VOTE: For EACH gate say ADOPT-<letter> (or KEEP-OPEN + what's missing). Then judge: (1) is this a FAIR,
non-question-begging test where DECOUPLING-REAPPEARS / DECOUPLING-BREAKS / DEPTH-OUT-PREDICTS /
DEPTH-FAILS / null are ALL genuinely reachable? (2) Is verbs genuinely the decisive third point that
separates 'has a hierarchy' from other POS differences, and is the design right that H2 transfers to
verbs (unlike adjectives)? (3) Any BLOCKER before freeze? Reply with per-gate letters first, then <=7
terse bullets."""

r = call(PANEL["B"], PREAMBLE, DESIGN, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-design.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s198 verb-design vote]\n")
