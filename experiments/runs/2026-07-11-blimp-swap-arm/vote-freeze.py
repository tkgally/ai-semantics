"""s210 — one NON-ANTHROPIC decorrelation vote at the FREEZE stage of the BLiMP swap arm.
PROTOCOL §A3: QA input to the fresh-agent freeze critic (verdict authority). panel.B, cutoff-aware preamble."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-11. You may encounter references to papers, datasets, or models that postdate "
            "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
            "for that reason fabricated. Where you must rely on what you know, label it as such.")
SYSTEM = (PREAMBLE + "\n\nYou are an independent, adversarial FREEZE-stage critic for an autonomous research "
          "project. The design is ratified and the instrument is BUILT but NOT yet scored; your job is a "
          "GO / GO-WITH-CONDITIONS / NO-GO on running it, focused on whether the frozen build faithfully "
          "realizes the ratified recipe and whether anything could bias the result. Be concrete and skeptical.")

USER = r"""
FREEZE-stage review of a built-but-unscored BLiMP content-word-swap arm (the second, promotion-required
control on a grammatical-profile result). RATIFIED gates: Q1-A (6 frame-safe paradigms, ~100 fresh paired
items each) / Q2-B (POS from the published 2012 SUBTLEX-US-with-PoS file; frequency match on SUBTLEX-US
Lg10WF within +-0.10) / Q3-A (mechanical re-validation; bounded candidacy). BUILD RULING: swap COMMON NOUNS
+ PROPER NAMES + ATTRIBUTIVE ADJECTIVES only (frame-safe, no subcategorization frame); hold the contrast
locus, the closed-class skeleton, MAIN VERBS, and ADVERBS fixed.

THE FROZEN BUILD (deterministic, seeded):
- Selected 6 by a swappability score (mean count of swappable positions/item, blind to accuracy/human),
  ties by UID alphabetical. Shallow: determiner_noun_agreement_2 (2.125), determiner_noun_agreement_1
  (1.738), regular_plural_subject_verb_agreement_1 (1.387). Deep (scope): sentential_negation_npi_scope
  (3.038), only_npi_scope (2.888), superlative_quantifiers_1 (1.962).
- Swap engine: locate the contrast locus (tokens differing between the good and bad member; never swapped,
  except a det-noun carve-out where the locus head noun's lemma is swapped with its number preserved and
  irregular-plural pairs are dropped). A common noun is swapped only in an NP-internal left context (after a
  det/adj/prep/possessive/number/noun — this excludes bare sentence-final main verbs a POS tagger mis-tags
  as nouns) with number preserved (plurals rule-pluralized + attestation-checked); a proper name only if
  title-case (and, in subject-verb paradigms, NOT the pre-verb subject, whose number is ambiguous and could
  flip agreement); an adjective only if attributive. Each substitute is same-POS, within +-0.10 Lg10WF,
  drawn seeded-deterministically from the full eligible in-band set. a/an re-normalized after swap.
- Mechanical re-validation (drop, never repair): >=1 swap; the good/bad contrast survives with the SAME
  number of differing token-positions (no collapsed/new contrast); no a/an-before-vowel error. A dropped
  pair is logged; a paradigm below 60 usable pairs is dropped + power re-stated.
- Achieved coverage (fraction of swap-eligible tokens actually replaced): shallow 0.70-0.98, deep 0.97-0.98
  (all clear the pre-registered 0.50 coverage floor; a below-floor paradigm's SWAP-STABLE would be excluded
  from the >=2/3 verdict — G-coverage).

METRIC (ratified, G-metric): per model, per stratum, Delta_pair = acc_swap_pair - acc_orig_pair (orig and
swap of the same pairID paired; both conditions re-run FRESH, both orders). Stratum-mean Delta with a
bootstrap CI over pairs. SWAP-STABLE iff the CI sits WITHIN +-0.05 on BOTH strata for >=2/3 models
(TOST-style equivalence); SWAP-DROPS iff Delta <= -0.05 with CI excluding 0 in a stratum on >=2/3; else
SWAP-INCONCLUSIVE. Shallow near ceiling => the scope-deep-3 carry the test. Because both conditions are
re-run fresh, the swapped accuracies are UNKNOWN at freeze — the +-0.05 margin cannot be tuned to a known
result. Cost of the run ~$1.3-1.6, ABORT_USD 1.60/model.

REPRESENTATIVE FROZEN SWAP PAIRS (original good/bad -> swapped good/bad):
- det_noun: "Karla would buy that hamster / those hamster" -> "Indianapolis would buy that badger / those badger"
- subj-verb: "The Borgias have questioned Sherry / The Borgias has questioned Sherry" -> "The Borgias have questioned Molly / The Borgias has questioned Molly" (subject 'Borgias' held fixed; only the object name swapped)
- sent_neg_npi_scope: "Some waitress that has alarmed Martin did not ever weep / ...has not alarmed Martin did ever weep" -> "Some hammer that has alarmed Vegas did not ever weep / ...has not alarmed Vegas did ever weep"
- only_npi_scope: "Only this patient that a lot of actresses hate will ever leave many banks / This patient that only a lot of actresses hate..." -> "Only this queen that a world of scrolls hate will ever leave many toys / This queen that only a world of scrolls hate..."
- superlative_q: "No customer should discover more than nine waitresses / at least nine waitresses" -> "No meantime should discover more than nine maggots / at least nine maggots"
(Some substitutes are semantically odd, e.g. "No meantime should discover"; note the 2AFC compares the two
members which SHARE the identical swapped content, so semantic oddity cancels and cannot bias Delta-acc.)

GIVE, CONCISELY:
1. Overall GO / GO-WITH-CONDITIONS / NO-GO on running the probe now.
2. Does the frozen swap engine faithfully preserve each paradigm's grammatical minimal contrast? Name any
   paradigm or construction where a noun/name/adjective swap (as described) could BREAK grammaticality or
   FLIP the good/bad polarity for a non-memorization reason that the mechanical re-validation would miss.
3. Is the "semantic oddity cancels in the 2AFC" argument correct, or could an odd swapped item bias Delta-acc?
4. Any residual anti-cheat concern (something tunable to a desired SWAP-STABLE or SWAP-DROPS), or "none".
5. One freeze-time condition you would add before the run, or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1600)
    cost, n, nm = billed_cost([[r]])
    json.dump({"model": PANEL["B"], "usage": r.get("usage"), "billed_cost": cost, "n": n,
               "n_missing": nm, "error": r.get("error"), "content": r.get("content")},
              open(os.path.join(os.path.dirname(__file__), "VOTE-freeze-s210.json"), "w"), indent=2)
    print("=== NON-ANTHROPIC FREEZE VOTE (panel.B) === $%.6f" % (cost or 0), "err:", r.get("error"))
    print(r.get("content"))

if __name__ == "__main__":
    main()
