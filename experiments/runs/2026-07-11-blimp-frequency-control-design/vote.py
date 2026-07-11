"""s207 — one NON-ANTHROPIC decorrelation vote on the BLiMP R1 frequency-control (C8) design gates.
PROTOCOL §2/§A3: QA input to the fresh-agent critic (who keeps verdict authority). panel.B (gpt-5.4-mini),
cutoff-aware preamble. Records usage.cost via billed_cost(). Writes VOTE-s207.json + prints a summary."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-11. You may encounter references to papers, datasets, or models that postdate "
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
Design under review: a TRAINING-FREQUENCY CONFOUND CONTROL for one already-run result.

Background. An earlier probe (BLiMP forced-choice sweep, 40 human-validated English grammatical
minimal-pair paradigms, 3 closed chat models, temperature 0, behavioral 2-alternative forced choice)
produced reading R1 = PROFILE-ALIGNED: per model, the Spearman across the 40 paradigms of the model's
per-paradigm forced-choice accuracy vs BLiMP's per-paradigm HUMAN agreement is positive on all three
(rho_prof = +0.606 / +0.543 / +0.628, n=40, all CIs exclude 0). Interpretation: "the panel is
grammatically hard where humans are hard." A binding freeze condition (C8) declared R1 NON-PROMOTABLE to
a claim until a training-frequency confound is controlled, because frequent local-agreement constructions
may be BOTH human-easy AND most-memorized, and rare island/scope contrasts BOTH human-harder AND
less-memorized — so a positive rho_prof could be a training-frequency artifact (with healthy accuracy
variance, so a variance/saturation guard does not catch it). C8 admits EITHER a corpus-frequency covariate
partialled from rho_prof, OR a content-word-swap arm.

This design turns C8 into three gates. The frozen prior accuracies + committed per-paradigm human anchor
are REUSED verbatim; C4 (22.3M sentences, ODC-BY, already frozen) is the proxy corpus.

Q1 (control strategy — THE CRUX):
  A [DEFAULT] = corpus-frequency covariate F(p) per paradigm from C4; report the PARTIAL Spearman of
      accuracy vs human-agreement CONTROLLING F, per model + CI. $0 model cost (reuses frozen accuracies);
      powered (n=40, df=37, p<0.05 at partial |rho|~0.32). Targets construction frequency directly.
      Exposure: the designer already KNOWS the prior accuracies, so "freeze the covariate before computing
      it" is weaker than a blind freeze.
  B = content-word-swap behavioral arm on >=2 shallow + >=2 deep paradigms (novel words, re-validate the
      contrast, re-run, compare original-vs-swapped accuracy). Fresh items => no anti-cheat exposure; but
      controls EXACT-STRING memorization, NOT construction frequency; costs ~$0.3-0.6 + a grammaticality
      re-validation build.
  C = both (covariate for construction frequency + swap arm for exact-string memorization; complementary).

Q2 (the frequency proxy F(p), live iff Q1 uses the covariate):
  A [DEFAULT] = per-paradigm mean surface-string C4 frequency of content-word bigrams/trigrams (a
      familiarity/exposure proxy). Cheap. Risk: lexical familiarity != construction frequency; mild
      detectability entanglement.
  B = the good-minus-bad local-detectability margin (surface co-occurrence favoring the good member) = the
      shadow-depth axis itself. OVER-CONTROL hazard: human difficulty also tracks depth, so partialling
      detectability may strip GENUINE shared structure, and a break under B would not separate "frequency
      artifact" from "the shared structure IS the depth structure." Proposed as a labelled conservative
      SENSITIVITY arm only, never the sole control.
  C = construction-level frequency (C4 rate of the licensing configuration, per-paradigm pattern match).
      Faithful to C8's literal wording; high build cost + heavy per-paradigm DoF.

Q3 (promotion rule + proxy scope): C4 is a PROXY for the panel's unknown pretraining distribution.
  A [DEFAULT] = the control is a promotion GATE, outcome a standalone result either way. SURVIVES (partial
      rho >= +0.3, CI excludes 0, >=2/3) => R1 becomes a promotion-review CANDIDATE (a later, separate,
      cross-session adversarial review writes the claim). BREAKS (near-zero / CI includes 0, >=2/3) => R1
      refused promotion, keeps only its within-panel DEPTH-GRADED sibling. Load-bearing caveat: SURVIVES
      means "against a C4-frequency PROXY," not "against actual training frequency."
  B = a within-model robustness datum only, never a promotion gate (R1 stays permanently descriptive).
  C = a SURVIVES writes the claim in the control session itself (no separate promotion review).

Anti-cheat scaffolding proposed: the proxy definition + C4 counting recipe (byte-reused from a frozen
prior script, asserted at import) + partial-rho method + SURVIVES/BREAKS bands are all frozen in PREREG
BEFORE F(p) is computed; a fresh freeze critic checks the recipe was not tuned to preserve/kill rho (e.g.
a scrambled paradigm->H mapping should not systematically SURVIVE). BREAKS, SWAP-DROPS, and corr(F,H)~=0
(no confound present) are pre-named first-class outcomes.

Give, concisely:
1. Overall GO / GO-WITH-CONDITIONS / NO-GO on running this control after gate ratification.
2. A per-gate vote: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale.
3. The single biggest methodological risk, and the one freeze-time condition you would add.
4. Is the covariate (reusing the already-known accuracies) a strong enough control to license a HUMAN-
   COMPARISON promotion, or is the swap arm (or both) needed? One paragraph.
5. Any place the design looks aimed at a desired result (anti-cheat), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1600)
    cost, n, n_missing = billed_cost([[r]])  # billed_cost returns (cost, n, n_missing)
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-s207.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC DECORRELATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
