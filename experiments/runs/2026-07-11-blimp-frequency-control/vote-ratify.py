"""s208 — one NON-ANTHROPIC decorrelation vote on the RATIFICATION of the BLiMP R1 frequency-control (C8)
design gates (decision blimp-profile-frequency-control-design, opened s207). PROTOCOL §2: QA input to the
fresh-agent ratification reviewer (who keeps verdict authority). panel.B (gpt-5.4-mini), cutoff-aware
preamble, FRESH vote (decorrelated from the s207 design vote). Records usage.cost via billed_cost().
Writes VOTE-ratify-s208.json + prints a summary."""
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
    "project on LLM meaning. A design's value-laden gates were OPENED one session ago with provisional "
    "defaults; your job now is to vote whether to FIX (ratify) each gate at its default or a named "
    "alternative, BEFORE any freeze/run. Ratification fixes the measuring yardstick, never the desired "
    "result — flag any choice that looks aimed at a particular outcome. Be skeptical and concrete. Reply "
    "in compact structured prose."
)

USER = r"""
Decision under ratification: the value-laden gates of a TRAINING-FREQUENCY CONFOUND CONTROL for one
already-run result. Opened last session with provisional defaults Q1-A / Q2-A / Q3-A. Last session's
pre-run design critic (a fresh agent, verdict authority) AND one non-Anthropic vote BOTH returned
GO-WITH-CONDITIONS and BOTH converged on Q1-C (the swap arm is required for a human-comparison PROMOTION;
the covariate arm alone earns only a robustness/corroboration result). You are a FRESH, decorrelated vote.

Background. An earlier probe (BLiMP forced-choice sweep, 40 human-validated English grammatical
minimal-pair paradigms, 3 closed chat models, temperature 0, behavioral 2-alternative forced choice)
produced reading R1 = PROFILE-ALIGNED: per model, the Spearman across the 40 paradigms of per-paradigm
forced-choice accuracy vs BLiMP's per-paradigm HUMAN agreement is positive on all three (rho_prof =
+0.606 / +0.543 / +0.628, n=40, all CIs exclude 0) = "the panel is grammatically hard where humans are
hard." A binding freeze condition (C8) declared R1 NON-PROMOTABLE until a training-frequency confound is
controlled, because frequent local-agreement constructions may be BOTH human-easy AND most-memorized, and
rare island/scope contrasts BOTH human-harder AND less-memorized, so a positive rho_prof could be a
training-frequency artifact (with healthy accuracy variance, so a saturation guard misses it). C8 admits
EITHER a corpus-frequency covariate partialled from rho_prof, OR a content-word-swap arm. The frozen prior
accuracies + committed per-paradigm human anchor are REUSED verbatim; C4 (22.3M sentences, ODC-BY, frozen)
is the proxy corpus.

Q1 (control strategy — THE CRUX):
  A [DEFAULT] = corpus-frequency covariate F(p) per paradigm from C4; report the PARTIAL Spearman of
      accuracy vs human-agreement CONTROLLING F, per model + bootstrap CI. $0 model cost (reuses frozen
      accuracies); powered (n=40, df=37, p<0.05 at partial |rho|~0.32). Exposure: the designer already
      KNOWS the prior accuracies, so "freeze the covariate before computing it" is weaker than a blind
      freeze (mitigated by: PREREG the F(p) recipe before computing it + a fresh-agent independently
      reproduces the counting code from the frozen spec + a scrambled-mapping negative control).
  B = content-word-swap behavioral arm on >=2 shallow + >=2 deep paradigms. Fresh items => no anti-cheat
      exposure; controls EXACT-STRING memorization, NOT construction frequency; ~$0.3-0.6 + a build.
  C = both.

Q2 (the frequency proxy F(p), live iff Q1 uses the covariate):
  A [DEFAULT] = per-paradigm mean surface-string C4 frequency of content-word bigrams/trigrams (a
      familiarity/exposure proxy). Cheap; least depth-entangled. Risk: lexical familiarity != construction
      frequency. Reported honestly as controlling "surface-lexical familiarity," not construction freq.
  B = the good-minus-bad local-detectability margin = the shadow-depth axis itself. OVER-CONTROL hazard:
      human difficulty also tracks depth, so partialling it may strip GENUINE shared structure. Proposed as
      a labelled conservative SENSITIVITY arm only, never the sole control.
  C = construction-level frequency (per-paradigm pattern match). Faithful to C8's literal wording but
      nearly collinear with depth (reproduces the B over-control hazard) + high per-paradigm DoF. Last
      session's fresh critic kept Q2-A primary and REJECTED Q2-C for this reason; last session's vote
      preferred Q2-C.

Q3 (promotion rule + proxy scope): C4 is a PROXY for the panel's unknown pretraining distribution.
  A [DEFAULT] = the control is a promotion GATE, outcome a standalone result either way. SURVIVES (partial
      rho CI excludes 0, >=2/3) => R1 becomes a promotion-review CANDIDATE (a later separate cross-session
      adversarial review writes the claim). BREAKS (CI includes 0, >=2/3) => R1 refused promotion, keeps
      only its within-panel DEPTH-GRADED sibling. Load-bearing caveat: SURVIVES means "against a
      C4-frequency PROXY," not "against actual training frequency."
  B = robustness datum only, never a promotion gate (R1 stays permanently descriptive).
  C = a SURVIVES writes the claim in the control session itself (rejected: promotion is always separate).

Also proposed as a binding freeze condition (G8, both last-session reviewers converged): the Q1-C swap arm
is REQUIRED for a promotion; the covariate arm alone earns only a robustness/corroboration result. And a
collinearity guard (G6): if corr(F,H) is above a frozen high threshold, the partial rho is reported
INCONCLUSIVE (over-control-suspect), distinct from SURVIVES/BREAKS and from corr(F,H)~=0 (no confound =>
R1 corroborated).

Give, concisely:
1. Overall RATIFY / RATIFY-WITH-CONDITIONS / KEEP-OPEN.
2. A per-gate vote: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale.
3. Do you endorse G8 (swap arm required for a PROMOTION; covariate alone = robustness only) as binding? Y/N + why.
4. The single biggest residual risk in adopting the defaults, and one freeze-time condition you would add.
5. Any place the gate defaults look aimed at a desired result (anti-cheat), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1800)
    cost, n, n_missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s208.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC RATIFICATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
