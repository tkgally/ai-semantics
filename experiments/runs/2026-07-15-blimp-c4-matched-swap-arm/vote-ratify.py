"""s232 — one NON-ANTHROPIC decorrelation vote on the RATIFICATION of the BLiMP R1
C4-FREQUENCY-MATCHED SWAP arm design gates (decisions/open/blimp-c4-matched-swap-arm-design,
opened s231, eligible s232). PROTOCOL §2: QA input to the fresh-agent adversarial ratifier (who
keeps verdict authority). panel.B (gpt-5.4-mini), cutoff-aware preamble. Records usage.cost via
billed_cost(). Writes VOTE-ratify-s232.json + prints a summary."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-15. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)

SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial RATIFICATION reviewer for an autonomous "
    "research project on LLM meaning. A design's value-laden operationalization gates were opened one "
    "session ago with provisional defaults; your job now, a SEPARATE session, is to decide whether to "
    "ADOPT those defaults, ADOPT-WITH-MODIFICATION, or KEEP-OPEN. Ratification fixes the measuring "
    "yardstick, NEVER the desired result — flag any choice that looks aimed at a particular outcome. "
    "Be skeptical and concrete. Reply in compact structured prose."
)

USER = r"""
Ratify (or not) the operationalization gates of a C4-FREQUENCY-MATCHED content-word-swap arm — the honest
successor to a prior swap arm that landed INCONCLUSIVE on a pretraining-frequency confound. The gates were
opened last session (s231) with provisional defaults Q1-A / Q2-A / Q3-A, both pre-run reviews (a fresh-agent
critic + one non-Anthropic vote) returned GO-WITH-CONDITIONS, and two BLOCKERS + three SHOULD-FIX were
discharged into freeze-time conditions in-design. You are the cross-session ratifier.

Background (the prior arm). A BLiMP forced-choice sweep (40 human-validated English grammatical minimal-pair
paradigms, 3 closed chat models, temperature 0, behavioral 2AFC, both orders) produced reading R1 =
PROFILE-ALIGNED (per-model Spearman of per-paradigm forced-choice accuracy vs BLiMP per-paradigm HUMAN
agreement = +0.606/+0.543/+0.628, all CIs exclude 0). A binding gate (G8) makes R1 non-promotable without
controlling a training-frequency confound and requires BOTH: (arm 1) a corpus-frequency COVARIATE — RAN,
SURVIVES-COVARIATE 3/3; (arm 2) a CONTENT-WORD SWAP — RAN, landed SWAP-INCONCLUSIVE: on 6 frame-safe
paradigms (3 shallow local-agreement + 3 scope-deep NPI/quantifier), replacing open-class content words
(nouns/proper-names/attributive-adjectives; verbs+adverbs fixed) with novel words matched within +-0.10
SUBTLEX-US Lg10WF (a HUMAN subtitle-frequency norm) dropped DEEP-stratum accuracy on all three models
(signed mean Delta-acc -0.095/-0.057/-0.072, all bootstrap CIs exclude 0). BUT the drop is CONFOUNDED: over
3,000,000 C4 sentences the original words' mean unigram log-frequency is 2.817 vs the swap set's 2.614 — a
+0.204 log-unit gap (swap words ~1.6x rarer in PRETRAINING; 2.3% never occur). So the deep drop is NEITHER
swap-stable NOR a clean exact-string-memorization signal.

The C4-matched arm. Instrument inherited BYTE-FROZEN (same elicitation, same 6 frame-safe paradigms, same
substitution recipe, same +-0.05 signed-CI equivalence bands). ONLY new operationalization: match the swap
substitutes on C4 PRETRAINING-proxy log-frequency too, closing the +0.204 gap by construction, then re-run.
SYMMETRIC verdict: DEEP-STILL-DROPS => a CLEANER exact-string-memorization signal (survives both frequency
controls), R1 refused promotion more firmly, a first-class negative; DEEP-SWAP-STABLE => the prior drop WAS
the C4 confound, and with the prior SURVIVES-COVARIATE, R1 becomes a bounded promotion-review CANDIDATE (a
later cross-session review writes/refuses the claim); STILL-INCONCLUSIVE => reported; and (a discharged
BLOCKER) STILL-INCONCLUSIVE-BY-MATCH-FAILURE => the achieved set-mean C4 gap did not clear an adequacy
threshold, so no DROPS/STABLE verdict is read.

The gates you are ratifying (defaults in brackets):
Q1 (THE CRUX — the C4-matching op):
  A [DEFAULT] = DUAL-BAND: substitute matched within +-0.10 SUBTLEX Lg10WF AND within a pinned C4 log-freq
      band (default +-0.30) of the original, per word; eligible pool = the INTERSECTION, seeded-deterministic;
      controls BOTH frequency channels per word; empty-intersection position DROPPED-AND-LOGGED, never
      band-widened. Freeze-time conditions folded in: G-C4-band (a BLIND numeric per-position pool floor + a
      pre-committed Q1-A->Q1-B fallback trigger, decided before build, blind to accuracies) and
      G-C4-match-adequacy (report achieved per-word AND set-mean C4 gap; require |set-mean gap| <= ~0.05 or
      land STILL-INCONCLUSIVE-BY-MATCH-FAILURE).
  B = C4-PRIMARY (match C4 band only, report SUBTLEX gap); larger pool, but re-opens the human-frequency gap.
  C = SET-LEVEL C4 mean-match; cheapest, permits per-item mismatches that cancel in the mean; sensitivity only.
Q2 (scope + ORIGINAL baseline):
  A [DEFAULT] = re-run the SAME 6 frame-safe paradigms, BOTH strata, on a FRESH seeded ~100-pair subsample
      DISJOINT from the prior sample, ORIGINAL re-run fresh in-session => within-run PAIRED Delta-acc, no
      known-accuracy exposure on either condition.
  B = deep-3 only (~half cost). C = reuse prior ORIGINAL accuracies (known-accuracy exposure; rejected).
Q3 (disambiguation verdict + promotion rule):
  A [DEFAULT] = the symmetric map above; candidacy bounded to "not exact-string memorization, not the surface
      freq proxy, not the pretraining-proxy freq gap" — STILL NOT construction-frequency-controlled; promotion
      always cross-session.
  B = any stable outcome a mere robustness datum, never re-open promotion (too conservative given SURVIVES in
      hand). C = write the R1 claim this/run session (rejected; cross-session always).

Anti-cheat exposure you must weigh: THIS arm is designed KNOWING the prior deep-drop magnitudes
(-0.095/-0.057/-0.072). Fences: (1) the C4-matched condition's accuracies are still unknown at freeze (novel
words; ORIGINAL re-run fresh on a DISJOINT sample), so no accuracy in Delta-acc is known at freeze; (2)
symmetric pre-registered bands (DROPS=refuse and STABLE=candidacy carry identical bands); (3) build-only DoF,
verifier-reproduced before scoring, blind-scoring lock (scoring code + exclusion criteria + the four-outcome
decision table frozen before any re-run; verifier attests no human-readable intermediate output inspected
until the whole batch is scored). Cost of the RUN ~$1.3-1.6 (one full-$5 UTC day); this session's only spend
is this vote; the run itself is DEFERRED to a fresh full-$5 UTC day.

Give, concisely:
1. Overall verdict: ADOPT-DEFAULTS / ADOPT-WITH-MODIFICATION / KEEP-OPEN.
2. Per-gate: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), one line of rationale each.
3. Is the folded G-C4-band + G-C4-match-adequacy pair sufficient to make "matched closely enough" a BLIND,
   pre-committed criterion rather than an after-the-fact judgement? If not, what one numeric rule is missing?
4. Given the arm is designed KNOWING the prior deep-drop magnitudes, is the symmetric-verdict + disjoint-
   fresh-sample + verifier-reproduced + blind-scoring fence sufficient anti-cheat, or is a further guard
   needed? One paragraph.
5. Any place the design looks aimed at a desired result (e.g. aimed at RE-OPENING R1's promotion), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1800)
    cost, n, n_missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s232.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC RATIFICATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
