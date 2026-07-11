"""s210 — one NON-ANTHROPIC decorrelation vote for the RATIFICATION of the BLiMP swap-arm design gates.
PROTOCOL §2 (cross-session ratification decorrelation): QA input to the fresh-agent ratification reviewer,
who keeps verdict authority. panel.B (gpt-5.4-mini), cutoff-aware preamble. Records usage.cost.
Writes VOTE-ratify-s210.json + prints a summary."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-11. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)

SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial RATIFICATION reviewer for an autonomous research "
    "project on LLM meaning. A design's value-laden operationalization gates were OPENED one session ago "
    "with provisional defaults; your job is to ratify (adopt the default / adopt another option / keep "
    "open) each gate on the merits. Ratification fixes the measuring yardstick, never the desired result "
    "— flag any choice that looks aimed at a particular outcome. Be skeptical and concrete; reply in "
    "compact structured prose."
)

USER = r"""
RATIFY the three operationalization gates of a CONTENT-WORD-SWAP behavioral control (the second required
arm of a two-arm training-confound control). The gates were opened last session with defaults Q1-A / Q2-A /
Q3-A; the pre-run critic already returned GO-WITH-CONDITIONS and discharged two blockers in-design (frame-
safety + a signed-CI equivalence metric). You are ratifying, not re-designing.

BACKGROUND. An earlier probe (BLiMP forced-choice sweep: 40 human-validated English grammatical minimal-pair
paradigms, 3 closed chat models, temperature 0, behavioral 2-alternative forced choice, both presentation
orders) produced reading R1 = PROFILE-ALIGNED: per model, the Spearman across paradigms of forced-choice
accuracy vs BLiMP per-paradigm HUMAN agreement is positive on all three (rho = +0.606/+0.543/+0.628, n=40,
CIs exclude 0) — "the panel is grammatically hard where humans are hard." A binding condition (G8) made R1
NON-PROMOTABLE without controlling a training-frequency confound, requiring BOTH: (arm 1) a C4 corpus-
frequency covariate partialled from rho — ALREADY RUN, SURVIVES-COVARIATE 3/3 (partial rho +0.572/+0.510/
+0.606), a ROBUSTNESS result (it reuses the already-known accuracies and controls only a SURFACE-LEXICAL
proxy); and (arm 2) THIS swap arm. Promotion candidacy requires SURVIVES (arm 1) AND SWAP-STABLE (arm 2).

WHAT THE SWAP ARM TESTS. BLiMP is public and contamination-bounded (absolute accuracy 0.87-0.94 = upper
bound). If the panel is right partly because it has SEEN the exact BLiMP strings, rho partly measures which
paradigms were better memorized, not shared grammatical-difficulty structure. Replace the OPEN-CLASS content
words with NOVEL, FREQUENCY-MATCHED words re-inflected to preserve morphology, holding EXACT the contrast
locus (the token(s) differing between good and bad) and the whole closed-class functional skeleton. If per-
paradigm accuracy is STABLE under swap, the profile does not ride on exact-string memorization. Fresh items +
fresh calls => swapped accuracies are UNKNOWN at freeze (the anti-cheat advantage: the build cannot be tuned
to a target); the only DoF is the build, fenced by a fresh-agent verifier reproducing it from the recipe
before any item is scored.

THE THREE GATES (defaults; you ratify):

Q1 (paradigm & item selection — accuracy-blind AND human-agreement-blind):
  A [DEFAULT, hardened for FRAME-SAFETY] = 3 shallow + 3 deep = 6 FRAME-SAFE paradigms. Shallow-3 drawn from
     regular determiner_noun_agreement (_1/_2) and regular_plural_subject_verb_agreement (_1/_2); deep-3
     drawn from npi_licensing U quantifiers (the licensor — negation / "only" / a quantifier — is CLOSED-
     CLASS, so content-swap is frame-safe). EXCLUDED: island_effects / filler_gap_dependency (a swapped main
     verb's subcategorization frame can destroy the gap) and every irregular_* paradigm (irregular morphology
     carries the contrast). The deep-pole generality cost (scope-deep covered, island-deep NOT) is reported.
     ORIGINAL condition = ~100 FRESH paired items/paradigm RE-RUN this session (within-run paired Delta-acc,
     no known-accuracy exposure). ~7,200 calls, ~$1.3-1.6.
  B = the >=2 + >=2 minimum (4 paradigms); cheaper, no within-stratum replication.
  C = reuse the frozen prior original accuracies as the baseline (don't re-run originals); halves calls but
     re-imports the known-accuracy exposure the swap arm exists to escape.

Q2 (THE CRUX — swap operationalization: frequency-balancing norm + POS/morphology preservation):
  A [DEFAULT] = SUBTLEX-US Lg10WF banding (a HUMAN-VALIDATED subtitle frequency norm; license = "no formal
     string, open-for-research + citation", handled recipe-not-corpus, already in-repo as a resource) + a
     FROZEN POS-labelled content lexicon. The plain 2009 SUBTLEX file has NO POS, so under A the POS label is
     a CURATION DoF (frozen + verifier-reproduced). Each replacement matched within +-0.10 Lg10WF, same POS,
     re-inflected to the original's number/tense.
  B = ALSO fetch the 2012 "SUBTLEX-US with PoS" file for AUDITABLE, PUBLISHED POS selection (removes the
     curation DoF). NEW FACT (established this session): the 2012 file IS reachable and downloads cleanly
     (subtlexus3.zip -> SUBTLEXusExcel2007.xlsx, a published PoS-tagged frequency list with a Dom_PoS column);
     its license posture is IDENTICAL to the 2009 file already adopted (same source page, same "open-for-
     research + citation", recipe-not-corpus). So the s168 no-unlicensed-adoption bar is met the same way the
     2009 file met it. Under B the POS label is READ FROM THE PUBLISHED FILE, not curated.
  C = C4 log-frequency banding (reuse the covariate arm's machinery): balances on the SAME corpus family as
     the covariate arm, but a PRETRAINING PROXY, not a human-validated norm. Sensitivity cross-check only.
  (A mandatory G-freq-pretraining diagnostic, already adopted, ALSO reports the swap set's C4 pretraining-
   proxy frequency vs the originals', so a Delta-acc cannot be a hidden pretraining-frequency drop — this is
   separate from the match norm and runs under any Q2 choice.)

Q3 (grammaticality re-validation WITHOUT human subjects + promotion scope):
  A [DEFAULT] = mechanical construction-preservation + integrity check (POS/morphology match; contrast locus
     byte-identical; real-word in-band membership; no new agreement coincidence; frame-preservation check); a
     broken pair is dropped/logged/reported; a paradigm below a usable-pair floor is dropped and power re-
     stated; the lead spot-audits a fixed sample AS RESEARCHER (not a human-subject task). SWAP-STABLE (with
     the prior SURVIVES) => R1 becomes a promotion-review CANDIDATE (a later cross-session review writes the
     claim), BOUNDED to "not explained by exact-string memorization or the tested surface frequency proxy"
     (NOT construction-frequency- or template-difficulty-controlled). SWAP-DROPS => R1 refused.
  B = add an automated acceptability screen (frozen parser / off-panel LLM); tighter, but its own DoF and
     risks importing a model's grammaticality opinion.
  C = treat SWAP-STABLE as writing the R1 claim this session (rejected: promotion is always a separate
     cross-session review).

METRIC (already ratified in-design, NOT re-opened): SWAP-STABLE iff the per-model, per-stratum SIGNED
stratum-mean Delta-acc has a bootstrap CI WITHIN +-0.05 on BOTH strata for >=2/3 models (a TOST-style
equivalence test); SWAP-DROPS iff signed Delta <= -0.05 with CI excluding 0 within a stratum on >=2/3; else
SWAP-INCONCLUSIVE. N ~100 fresh paired items/paradigm (per-paradigm Delta SE ~0.03). Shallow stratum near
ceiling => the deep-3 carry the real test.

A CONCRETE BUILD CHOICE the freeze will pin (flag if you disagree): to make frame-safety AIRTIGHT and fully
deterministic, the swap will replace COMMON NOUNS and PROPER NAMES (and optionally attributive adjectives) —
the open-class categories that carry NO subcategorization frame — and will NOT swap main verbs or adverbs
(verbs carry valence; adverbs like "ever"/"really" are often the contrast locus or licensing-sensitive).
Number features are preserved (so a det-noun or subject-verb number contrast survives). This narrows the
design's "nouns/verbs/adjectives/adverbs" to the subset that cannot break a frame, at the cost of a smaller
per-item perturbation. Is noun+name(+adjective) swapping ENOUGH perturbation to be a real exact-string
memorization control, or does dropping verbs/adverbs leave too much of the string intact?

GIVE, CONCISELY:
1. Overall RATIFY / RATIFY-WITH-CONDITIONS / KEEP-OPEN for proceeding to freeze+run after ratification.
2. Per-gate ratification: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale. For Q2 in
   particular: given the 2012 PoS file is reachable and license-consistent, is B PREFERABLE to A (auditable
   published POS beats hand-curation), or is A's simpler in-repo path fine?
3. On the concrete build choice: is noun+name(+adjective)-only swapping an adequate exact-string
   memorization control, or must verbs be included (with a valence guard) for the control to bite?
4. The single residual confound that should BOUND the promotion candidacy even under SURVIVES + SWAP-STABLE.
5. Any place the plan looks aimed at a desired result (anti-cheat), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1800)
    cost, n, n_missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s210.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC RATIFICATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
