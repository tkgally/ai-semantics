"""s237 — one NON-ANTHROPIC decorrelation vote on the A3b/C8 BLiMP swap-line CONTINUATION
review (PROTOCOL §3 instrument-line-stopping governor). Two swap-type arms have now run
(s210 SUBTLEX-matched, s235 dual-band C4-matched); a verb-swap arm would be the THIRD and
trips the governor, requiring this cross-session line-continuation review BEFORE any design.
QA input to the fresh-agent reviewer (who keeps verdict authority). panel.B (gpt-5.4-mini),
cutoff-aware preamble. Records usage.cost via billed_cost(). Writes VOTE-continuation-s237.json."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-16. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)

SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial GOVERNANCE reviewer for an autonomous research "
    "project on LLM meaning. The project has a standing 'instrument-line-stopping' rule: after a run of "
    "instrument redesigns yielding no clean read on one construct, a FURTHER redesign requires a "
    "cross-session review that weighs continuing the line against alternative uses of the same effort and "
    "budget. Your job is to decide whether one specific measurement line CONTINUES to another arm or STOPS "
    "at its current ceiling. You are NOT deciding a scientific result — you are deciding whether spending "
    "more probe budget on this line is the best use of it. Ceilings are honest outcomes; refusing to run "
    "another arm is a first-class, non-failure decision. Be skeptical, concrete, and economically honest — "
    "flag any impulse to keep running merely to avoid an inconclusive resting state. Reply in compact "
    "structured prose."
)

USER = r"""
Decide whether a measurement LINE continues to a third arm or stops. Background:

The line asks whether a chat-model panel's BLiMP grammatical-acceptability profile-alignment with humans
(reading R1: per-model Spearman of per-paradigm 2AFC accuracy vs BLiMP human agreement = +0.61/+0.54/+0.63,
all CIs exclude 0) rides on genuine grammatical competence versus exact-string / lexical-item memorization or
a frequency shadow. A binding gate makes R1 non-promotable until a content-word SWAP arm shows the profile is
stable when the exact BLiMP content words are replaced by frequency-matched novel words. Two swap arms have run:

ARM 1 (s210, SUBTLEX-matched swap): replacing open-class content words (nouns/proper-names/attributive-adjs;
verbs+adverbs held fixed) with novel words matched on SUBTLEX-US human subtitle log-frequency dropped the
DEEP-scope stratum (NPI/quantifier) on all 3 models (signed mean Delta-acc -0.095/-0.057/-0.072, all CIs
exclude 0) => NOT swap-stable. BUT the drop was CONFOUNDED: the swap words, though human-frequency-matched,
were ~1.6x rarer in a C4 pretraining-frequency proxy (+0.204 log-unit gap). So NEITHER swap-stable NOR clean
memorization. Verdict: SWAP-INCONCLUSIVE. Cost ~$1.34, 7,200 calls.

ARM 2 (s235, DUAL-BAND SUBTLEX-and-C4-matched swap): closed the +0.204 C4 gap BY CONSTRUCTION (build-time
signed set-mean C4 gap +0.0106, |.|<=0.05 = adequate) and re-ran on a fresh disjoint sample. Net of BOTH
frequency channels the deep stratum STILL drops directionally on 3/3 (Delta-acc -0.072/-0.057/-0.042, all CIs
exclude 0) but 0/3 clear the strict whole-CI<=-0.05 bar (deep CI-uppers -0.048/-0.023/-0.022, missing the bar
by as little as 0.002 on one model) and the CIs extend below -0.05, so it is neither DEEP-STILL-DROPS nor
DEEP-SWAP-STABLE. Closing C4 ATTENUATED the s210 deep drop for 2/3 (claude -0.095->-0.072, gemini
-0.072->-0.042; gpt ~unchanged) — so PART of the s210 drop was the C4 confound — but a residual survives both
proxies, too small to resolve at this N. A disclosed caution: the C4 match is on the SET MEAN, not word-by-word
(per-word |gap| 0.154, both signs partly cancel). Verdict: STILL-INCONCLUSIVE. Cost ~$1.31, 7,200 calls.
Result: R1 stays descriptive/non-promotable, exactly as before, on a now TWICE-controlled footing.

THE PROPOSED THIRD ARM: a VERB-SWAP arm with a valence guard. The two arms held verbs+adverbs FIXED (only
nouns/proper-names/adjectives were swapped), so a verb-swap arm is the one remaining perturbation direction —
it would test whether swapping the verbs (matched on frequency and subcategorization/valence to keep the
sentences grammatical) also leaves the deep-scope profile stable. It would cost ~$1.3-1.6 and one full daily
budget day, and is the THIRD swap-type redesign on this one reading.

Alternatives the same budget/effort could buy instead (non-exhaustive): (a) a larger-N re-run of the EXISTING
dual-band C4 arm to tighten the residual deep drop's CIs — the s235 deep CI-upper missed the strict bar by
0.002 on one model, so a bigger N could tip STILL-INCONCLUSIVE to a clean read either way (but does not add a
new perturbation axis); (b) a grounding-magnitude / image-referent probe (a genuinely unrun instrument, the
highest-information unrun purchase in the repo, ~$3-4, currently blocked on a license-checked image-sense
scout); (c) other program lines (lexical-relation recovery, alternation batteries) that already have promoted
claims and could compound; (d) STOP spending on R1's swap line — accept the twice-controlled ceiling as the
honest resting state (R1 is human-profile-ALIGNED but its provenance between competence, a per-word frequency
residual, and shared difficulty is left OPEN at a measured ceiling), and redeploy budget elsewhere.

Give, concisely:
1. Overall verdict on the LINE: CONTINUE-TO-VERB-SWAP / STOP-AT-CEILING / STOP-FOR-NOW-WITH-CONDITIONS (name
   the conditions that would reopen it).
2. The core economic question: is a THIRD ~$1.3-1.6 swap arm (verb-swap) the best marginal use of that budget
   given two arms already reached a twice-controlled STILL-INCONCLUSIVE, or would a-d dominate it? Rank.
3. If the line STOPS, what is the honest one-sentence resting statement about R1?
4. If a verb-swap arm WERE run, what is the realistic best-case information gain — and is it decisive for R1's
   promotion, or would R1 stay non-promotable regardless (e.g. because construction-frequency is still
   uncontrolled)? Be concrete about whether ANY swap arm can promote R1.
5. Any sign this review (or the urge to run a third arm) is motivated by wanting a particular result rather
   than by information economics? Or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1800)
    cost, n, n_missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-continuation-s237.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC CONTINUATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
