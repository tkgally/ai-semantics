"""s231 — one NON-ANTHROPIC decorrelation vote on the BLiMP R1 C4-FREQUENCY-MATCHED SWAP arm design gates.
PROTOCOL §2/§A3: QA input to the fresh-agent critic (who keeps verdict authority). panel.B (gpt-5.4-mini),
cutoff-aware preamble. Records usage.cost via billed_cost(). Writes VOTE-s231.json + prints a summary."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-15. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)

SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial PRE-RUN design critic for an autonomous "
    "research project on LLM meaning. Your job is to find fatal flaws BEFORE any money is spent, and to "
    "vote GO / GO-WITH-CONDITIONS / NO-GO on each value-laden gate. Be skeptical and concrete. "
    "Ratification fixes the measuring yardstick, never the desired result — flag any choice that looks "
    "aimed at a particular outcome. Reply in compact structured prose."
)

USER = r"""
Design under review: a C4-FREQUENCY-MATCHED content-word-swap arm — the honest successor to a prior swap arm
that landed INCONCLUSIVE on a frequency confound.

Background (the prior arm). An earlier BLiMP forced-choice sweep (40 human-validated English grammatical
minimal-pair paradigms, 3 closed chat models, temperature 0, behavioral 2AFC, both orders) produced reading
R1 = PROFILE-ALIGNED (per-model Spearman of per-paradigm forced-choice accuracy vs BLiMP per-paradigm HUMAN
agreement = +0.606/+0.543/+0.628, all CIs exclude 0 — "the panel is hard where humans are hard"). A binding
gate (G8) makes R1 non-promotable without controlling a training-frequency confound and requires BOTH: (arm 1)
a corpus-frequency COVARIATE — RAN, SURVIVES-COVARIATE 3/3, a robustness datum only; (arm 2) a CONTENT-WORD
SWAP — RAN, and it landed SWAP-INCONCLUSIVE: on 6 frame-safe paradigms (3 shallow local-agreement + 3
scope-deep NPI/quantifier), replacing the open-class content words (nouns/proper-names/attributive-adjectives;
verbs+adverbs held fixed) with novel words matched within +-0.10 SUBTLEX-US Lg10WF (a HUMAN subtitle-frequency
norm) dropped forced-choice accuracy on the DEEP stratum on all three models (signed mean Delta-acc
-0.095/-0.057/-0.072, all bootstrap CIs exclude 0). BUT the drop is CONFOUNDED: over 3,000,000 C4 sentences
the original words' mean unigram log-frequency is 2.817 vs the swap set's 2.614 — a +0.204 log-unit gap (swap
words ~1.6x rarer in PRETRAINING; 2.3% never occur). So the deep drop is NEITHER swap-stable NOR a clean
exact-string-memorization signal — it is tangled with the swap set being rarer in pretraining. The prior
result registered the fix explicitly: a C4-FREQUENCY-MATCHED swap arm; only then could a deep drop be read as
exact-string memorization rather than pretraining rarity.

What THIS arm does. The measurement instrument is inherited BYTE-FROZEN from the prior swap arm (same
elicitation, same 6 frame-safe paradigms, same substitution recipe, same +-0.05 signed-CI equivalence bands,
same diagnostics). The ONLY new operationalization: match the swap substitutes on C4 PRETRAINING-proxy
log-frequency, not only on human SUBTLEX frequency — closing the +0.204 gap by construction — then re-run the
deep (and shallow-anchor) stratum. SYMMETRIC verdict: DEEP-STILL-DROPS under C4-matching => a CLEANER
exact-string-memorization signal (survives both frequency controls), R1 refused promotion more firmly, a
first-class negative; DEEP-NO-LONGER-DROPS (SWAP-STABLE) => the prior drop WAS the C4 confound, and with the
prior SURVIVES-COVARIATE, R1 becomes a bounded promotion-review CANDIDATE (a later cross-session review writes
the claim); STILL-INCONCLUSIVE => reported. Bands identical for the two poles.

Anti-cheat note you must weigh: unlike the prior arm (swapped accuracies unknown at freeze), THIS arm is
designed KNOWING the prior deep-drop magnitudes. Fences claimed: (1) the C4-matched condition's accuracies are
still unknown at freeze (novel words; ORIGINAL re-run fresh on a DISJOINT sample), so no accuracy in Delta-acc
is known when the recipe is frozen; (2) symmetric pre-registered bands; (3) build-only DoF, verifier-reproduced
before scoring; C4 counting reuses the prior import-pinned streaming adapter (no new corpus adoption).

Three gates (it does NOT re-open the ratified G8 / covariate-and-swap-required structure — only HOW the
C4-matched arm is built and scored):

Q1 (THE CRUX — the C4-frequency-matching operationalization):
  A [DEFAULT] = DUAL-BAND: substitute matched within +-0.10 SUBTLEX Lg10WF AND within a pinned C4 log-freq
      band (default +-0.30) of the original, per word; eligible pool = the INTERSECTION, seeded-deterministic
      selection; controls BOTH the human- and the pretraining-frequency channel per word; a position with an
      empty intersection is DROPPED-AND-LOGGED, never force-filled by widening the band (possible power loss,
      restated).
  B = C4-PRIMARY: match on the C4 band only, report (not bind) the achieved SUBTLEX gap; larger pool, less
      attrition, but RE-OPENS the human-frequency gap the prior arm controlled.
  C = SET-LEVEL C4 mean-match (swap-set mean C4 = orig-set mean, not per word); cheapest on attrition, permits
      large per-item C4 mismatches that cancel in the mean; sensitivity cross-check only, not default.

Q2 (run scope + ORIGINAL baseline):
  A [DEFAULT] = re-run the SAME 6 frame-safe paradigms, BOTH strata, on a FRESH seeded ~100-pair subsample
      DISJOINT from the prior sample, ORIGINAL re-run fresh in-session => within-run PAIRED Delta-acc, no
      known-accuracy exposure on either condition; deep-3 load-bearing, near-ceiling shallow-3 the
      destructive-control anchor.
  B = deep-3 only (~half cost); drops the cheap shallow anchor.
  C = reuse the prior ORIGINAL accuracies as baseline; re-imports known-accuracy exposure + cross-session
      drift; rejected.

Q3 (the disambiguation verdict + promotion rule):
  A [DEFAULT] = the symmetric map above; candidacy bounded to "not exact-string memorization, not the surface
      freq proxy, not the pretraining-proxy freq gap" — STILL NOT construction-frequency-controlled; promotion
      always cross-session.
  B = treat any stable outcome as a mere robustness datum, never re-open promotion (too conservative given the
      prior SURVIVES is already in hand).
  C = write the R1 claim this/the run session (rejected; cross-session always).

Cost of the RUN (from OBSERVED prior economics, not a low pre-flight): 6 x ~100 pairs x 2 conditions x 2
orders x 3 models = ~7,200 calls ~= $1.3-1.6, under the $2.50 single-run flag, one full-$5 UTC day. This
design session's only spend is this one vote.

Give, concisely:
1. Overall GO / GO-WITH-CONDITIONS / NO-GO on running this C4-matched swap arm after gate ratification.
2. A per-gate vote: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale.
3. The single biggest methodological risk specific to the C4-MATCHING itself (dual-band pool attrition /
   the +-0.30 C4 band width / SUBTLEX-vs-C4 tension), and the one freeze-time condition you would add.
4. Given the arm is designed KNOWING the prior deep-drop magnitudes, is the symmetric-verdict + disjoint-
   fresh-sample + verifier-reproduced-build fence sufficient anti-cheat, or does the known-drop exposure need
   a further guard? One paragraph.
5. Any place the design looks aimed at a desired result (e.g. aimed at RE-OPENING R1's promotion), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1800)
    cost, n, n_missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-s231.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC DECORRELATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
