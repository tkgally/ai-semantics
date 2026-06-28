"""Build + freeze the WITHIN-VERBAL matched ADD-vs-CANCEL monotonicity battery
(2026-06-28, session 141).

The decisive WITHIN-VERBAL generalization test the conjecture has needed since the M2
domain-mismatch caveat. It pairs TWO VERBAL arms (no domain mismatch), so a positive
asymmetry here is the clean within-verbal confirm that DISCHARGES M2 (unlike the s137 C2
battery, whose only B2-passing cancel default was NOMINAL/taxonomic).

Reached because:
  - s139 survey (result/monotonicity-verbal-cancel-survey-v1): the causative-inchoative
    RESULT-STATE default is held at ceiling (NLI affirm 1.00, 3/3) -- a B2-passing VERBAL
    default, refuting the un-findability scarcity worry.
  - s140 calibration (result/monotonicity-causative-progressive-cancel-v1): the PROGRESSIVE
    suppresses that default in all 3 models (NLI cancel_no_cue 66.7/66.7/33.3 pp; FC
    100/100/50), and an explicit result-consequence cue re-licenses -- a genuine same-verb
    constructional cancel, the conative-shaped pattern. PER-VERB UNEVEN (dissolved clean,
    shattered/melted resist under NLI) -- carried into this battery, NOT averaged away.

THE FROZEN PAIR (matched conflicting-cue paradigm; template result/conative-cancel-v2 and
the s137 C2 battery, the privative cancel arm swapped for the progressive cancel arm):
  ADD arm    = the s135 frozen RESULTATIVE arm, REUSED VERBATIM (read straight from
               experiments/data/monotonicity-generalization-battery/items.csv,
               sha256[:16] 80bd4b60b55a3e60). 10 verbs x control/construction/cue. The
               decision forbids rebuilding it; this script copies the arm==add rows
               byte-for-byte (a verbatim self-check asserts the source sha).
  CANCEL arm = the s140 CAUSATIVE-INCHOATIVE PROGRESSIVE cancellation (VERBAL). 6 verbs x
               default/construction/cue, identical strings to the s140 frozen calibration
               (sha 5ba8a996fa70cf55), the s140 'progressive' condition renamed
               'construction' to fit the battery analyzer.

  ADD:    control      "Maria beat the cream."                 -> bare default (want low; B2 control)
          construction "Maria beat the cream stiff."           -> LICENSING-no-cue (want ceiling) = add_no_cue
          cue          "...stiff, but the cream did not become stiff." -> explicit DENIAL; follow-cue = WITHHOLD
  CANCEL: default      "Sam broke the vase."                   -> result default (want ceiling; B2 default)
          construction "Sam was breaking the vase."            -> SUPPRESSION; cancel_no_cue = 1 - affirm
          cue          "...the vase, and the pieces scattered across the floor." -> explicit RE-ASSERTION; follow-cue = AFFIRM
The add cue DENIES the licensed inference; the cancel cue RE-ASSERTS the suppressed result
(an explicit consequence that entails it WITHOUT echoing the hypothesis verb) -- mirror
images, both internally conflicting (as cc-v2 / s135 / the C2 battery were).

FROZEN THRESHOLDS (ratified s134, UNTOUCHED; read by analyze.py):
  B2 gate (read from the same run, before the asymmetry is reported): add construction
    >= 0.80 AND control <= 0.40; cancel default >= 0.80; each in >= 2/3 models.
  Asymmetry: add_no_cue - cancel_no_cue >= 0.20 (>=2/3) CONFIRMS; |.|<0.20 SYMMETRIC
    (falsifies); <= -0.20 REVERSAL (falsifies).
  Instrument-fragility: cancel NLI-vs-FC disagreement - add's >= 0.10 (>=2/3) = leg 2.
  Cue: >= 0.70 follow-cue (>=2/3) robust.

M1 (binding on the result page): the B2 default-at-ceiling pass is what licenses reading a
cancel suppression FAILURE as DEFEASANCE (the gate certifies the result default is a real
model-held entailment -- already established at 1.00 in s139, re-read here).
M2 DISCHARGED (binding on the result page): BOTH arms are VERBAL (resultative ADD,
progressive CANCEL), so any asymmetry is a CLEAN WITHIN-VERBAL contrast -- the domain
mismatch the C2 battery had to accept is GONE. This is the headline improvement over the
weak C2 confirm.
PER-VERB DISCIPLINE (binding): report the cancel arm PER VERB; do NOT drop shattered/melted
to inflate suppression (that would be operationalization-tuning, PROTOCOL §8).

DESIGN NOTE (anti-cheat, disclosed): unlike the C2 battery's two-stage build (B2 calib run
first with the suppression cell held out), this battery runs all cells in ONE pass and the
analyzer reads the B2 gate BEFORE reporting the asymmetry. This is safe because the
thresholds are the FROZEN ratified s134 set (not tunable here) and the reading rule is
committed in PREREG before the run; nothing is tuned after data. The B2 cells (default,
control, construction) are the same frozen strings already B2-confirmed in s139/s135/s137.

HUMAN ANCHOR: none -- `internal-contrast-only` (ratified conflicting-cue-human-anchor). No
human-comparison claim, no human label invented.

Run: python3 build_items.py   (no API; writes + sha256-hashes the frozen CSV)
"""
import csv
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ADD_SRC = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "monotonicity-generalization-battery", "items.csv"))
ADD_SRC_SHA = "80bd4b60b55a3e60"   # frozen s135 add arm; verbatim-reuse self-check

# s140 causative-inchoative progressive cancel pool (identical strings to the s140 frozen
# calibration, sha 5ba8a996fa70cf55). (subj, v_past, v_prog, obj, inch, result_consequence)
PROGRESSIVE = [
    ("Sam",   "broke",     "breaking",  "vase",    "broke",     "the pieces scattered across the floor"),
    ("Mara",  "shattered",  "shattering", "window", "shattered", "glass sprayed across the room"),
    ("Devin", "melted",     "melting",   "snowman", "melted",    "a puddle spread across the lawn"),
    ("Priya", "tore",       "tearing",   "page",    "tore",      "the two halves came apart in her hands"),
    ("Lena",  "cracked",    "cracking",  "egg",     "cracked",   "yolk ran down the side of the bowl"),
    ("Omar",  "dissolved",  "dissolving", "tablet", "dissolved", "the water turned cloudy"),
]
# B2 calib subset (cancel DEFAULT cells only; mirrors the C2 battery's 4-cancel subset).
CALIB_CANCEL = {"vase", "snowman", "egg", "tablet"}


def add_rows_verbatim():
    """Read the s135 frozen add arm byte-for-byte (verbatim reuse, decision STEP 2)."""
    h = hashlib.sha256(open(ADD_SRC, "rb").read()).hexdigest()[:16]
    assert h == ADD_SRC_SHA, f"ADD source sha {h} != frozen {ADD_SRC_SHA} -- refuse to build"
    rows = [r for r in csv.DictReader(open(ADD_SRC)) if r["arm"] == "add"]
    return rows


def cancel_rows():
    out = []
    for subj, vpast, vprog, obj, inch, cons in PROGRESSIVE:
        hyp = f"The {obj} {inch}."
        calib = "1" if obj in CALIB_CANCEL else "0"
        conds = [
            # condition, sentence, nli_gold, fc_gold, affirm_correct, calib
            ("default",      f"{subj} {vpast} the {obj}.",
             "0", "YES", "1", calib),
            ("construction", f"{subj} was {vprog} the {obj}.",
             "1", "NO", "0", "0"),
            ("cue",          f"{subj} was {vprog} the {obj}, and {cons}.",
             "0", "YES", "1", "0"),
        ]
        for cond, sent, ng, fg, ac, cl in conds:
            out.append(dict(item_id=f"can-{obj}-{cond}", arm="cancel",
                construction="causative-progressive", stem=obj, condition=cond,
                sentence=sent, nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg,
                affirm_correct=ac, calib=cl))
    return out


def main():
    out = os.path.abspath(os.path.join(
        HERE, "..", "..", "data", "monotonicity-within-verbal-battery", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    add = add_rows_verbatim()
    can = cancel_rows()
    rs = add + can
    cols = ["item_id", "arm", "construction", "stem", "condition", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct", "calib"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    ncalib = sum(1 for r in rs if r["calib"] == "1")
    add_verbs = {r["stem"] for r in add}
    can_verbs = {r["stem"] for r in can}
    print(f"wrote {len(rs)} items ({len(add)} add [verbatim s135] + {len(can)} cancel) -> {out}")
    print(f"  add: {len(add_verbs)} resultative verbs x (control/construction/cue) [REUSED, sha {ADD_SRC_SHA}]")
    print(f"  cancel: {len(can_verbs)} causative-inchoative verbs x (default/construction/cue) [VERBAL -> M2 discharged]")
    print(f"  calib subset: {ncalib} items (add source-calib + cancel default {sorted(CALIB_CANCEL)})")
    print(f"  add/cancel stem overlap = {add_verbs & can_verbs or 'NONE (clean)'}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
