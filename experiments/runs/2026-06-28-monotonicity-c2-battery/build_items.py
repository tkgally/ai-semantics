"""Build + freeze the C2 MATCHED-DIFFICULTY ADD-vs-CANCEL MONOTONICITY battery
(2026-06-28, session 137) -- STEP 2 of decisions/resolved/monotonicity-cancel-arm-redesign.

Reached because STEP 1 (C1 telic-completion) was a B2 NO-GO and STEP 1b (C2 privative) was
a B2 GO (result/monotonicity-c2-privative-calibration-v1, category default 1.00 in 3/3).
M2 (the deliberate written conjecture-scope amendment to a nominal/adjectival privative
cancel arm) was applied before STEP 1b.

THE FROZEN PAIR (STEP 2):
  ADD arm    = the s135 frozen RESULTATIVE arm, REUSED VERBATIM (read straight from
               experiments/data/monotonicity-generalization-battery/items.csv,
               sha256[:16] 80bd4b60b55a3e60). 10 verbs x control/construction/cue. The
               decision forbids rebuilding it; this script copies the arm==add rows
               byte-for-byte (a verbatim self-check asserts the source sha).
  CANCEL arm = the C2 PRIVATIVE-MODIFIER cancellation (M2-broadened scope). A bare head
               noun entails its category ("Sam bought a gun" |= "a weapon"); a privative
               modifier cancels it ("Sam bought a fake gun" |/= "a weapon"). 8 nouns x
               default/construction/cue. Nouns + frozen privatives from the STEP-1b GO
               calibration (sha 39598ee7ad97f33d).

THE MATCHED CONFLICTING-CUE PARADIGM (template: result/conative-cancel-direction-v2;
identical structure to the s135 battery, cancel coercion swapped):
  ADD:    control      "Sam <v> the <obj>."             -> bare default (want low; B2 control)
          construction "Sam <v> the <obj> <res>."       -> LICENSING-no-cue (want ceiling) = add_no_cue
          cue          "...<res>, but ... did not become <res>." -> explicit DENIAL; follow-cue = WITHHOLD
  CANCEL: default      "Sam bought a gun."              -> category default (want ceiling; B2 default)
          construction "Sam bought a fake gun."         -> SUPPRESSION; cancel_no_cue = 1 - affirm
          cue          "...a fake gun, but it was a real weapon." -> explicit RE-ASSERTION; follow-cue = AFFIRM
The add cue DENIES the licensed inference; the cancel cue RE-ASSERTS the suppressed
category -- mirror images, both deliberately internally-conflicting (as cc-v2 / s135 were).

FROZEN THRESHOLDS (ratified s134, UNTOUCHED; read by analyze.py / analyze_calib.py):
  B2 gate (calib subset, before the main read): add construction >= 0.80 AND control
    <= 0.40; cancel category default >= 0.80; each in >= 2/3 models.
  Asymmetry: add_no_cue - cancel_no_cue >= 0.20 (>=2/3) CONFIRMS; |.|<0.20 SYMMETRIC
    (falsifies); <= -0.20 REVERSAL (falsifies).
  Instrument-fragility: cancel NLI-vs-FC disagreement - add's >= 0.10 (>=2/3) = leg 2.
  Cue: >= 0.70 follow-cue (>=2/3) robust.

M1 (binding on the result page): the B2 default-at-ceiling pass is what licenses reading a
cancel suppression FAILURE as DEFEASANCE (the gate certifies the category default is a real
model-held entailment, closing the s135 "the inference was never an entailment" confound).
M2 LIVE CAVEAT (binding on the result page): the ADD arm is VERBAL (resultative) and the
CANCEL arm is NOMINAL/ADJECTIVAL (privative), so any asymmetry is across a DOMAIN
DIFFERENCE, not a clean within-verbal contrast -- a broadened, weaker version of the
original verbal-only bet.

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

# C2 privative cancel pool: (noun, subject, past_verb, category, privative).
# Identical to the STEP-1b GO calibration (sha 39598ee7ad97f33d); privatives now USED.
PRIVATIVE = [
    ("gun",     "Sam",    "bought",  "weapon",             "fake"),
    ("diamond", "Priya",  "bought",  "gemstone",           "fake"),
    ("rose",    "Jordan", "bought",  "flower",             "artificial"),
    ("tiger",   "Lena",   "saw",     "animal",             "toy"),
    ("apple",   "Omar",   "held",    "fruit",              "plastic"),
    ("pearl",   "Nina",   "wore",    "jewel",              "imitation"),
    ("sword",   "Carlos", "carried", "weapon",             "toy"),
    ("violin",  "Maria",  "played",  "musical instrument", "toy"),
]
# B2 calib subset (mirrors s135 sizing: 4 add verbs already calib=1 in the source +
# 4 cancel nouns here). Cancel default cells only (suppression cell held OUT of calib).
CALIB_CANCEL = {"gun", "diamond", "tiger", "apple"}

VOWELS = "aeiou"


def art(word):
    return "an" if word[0].lower() in VOWELS else "a"


def add_rows_verbatim():
    """Read the s135 frozen add arm byte-for-byte (verbatim reuse, decision STEP 2)."""
    h = hashlib.sha256(open(ADD_SRC, "rb").read()).hexdigest()[:16]
    assert h == ADD_SRC_SHA, f"ADD source sha {h} != frozen {ADD_SRC_SHA} -- refuse to build"
    rows = [r for r in csv.DictReader(open(ADD_SRC)) if r["arm"] == "add"]
    # the source has no privative_modifier column; add an empty one for a uniform schema
    for r in rows:
        r["privative_modifier"] = ""
    return rows


def cancel_rows():
    out = []
    for noun, subj, verb, cat, priv in PRIVATIVE:
        np_bare = f"{art(noun)} {noun}"
        np_priv = f"{art(priv)} {priv} {noun}"   # art() keys on the privative's first letter
        hyp = f"{subj} {verb} {art(cat)} {cat}."
        calib = "1" if noun in CALIB_CANCEL else "0"
        conds = [
            # condition, sentence, nli_gold, fc_gold, affirm_correct, calib
            ("default",      f"{subj} {verb} {np_bare}.",
             "0", "YES", "1", calib),
            ("construction", f"{subj} {verb} {np_priv}.",
             "2", "NO", "0", "0"),
            ("cue",          f"{subj} {verb} {np_priv}, but it was a real {cat}.",
             "0", "YES", "1", "0"),
        ]
        for cond, sent, ng, fg, ac, cl in conds:
            out.append(dict(item_id=f"can-{noun}-{cond}", arm="cancel",
                construction="privative", stem=noun, condition=cond,
                sentence=sent, nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg,
                affirm_correct=ac, calib=cl, privative_modifier=priv))
    return out


def main():
    out = os.path.abspath(os.path.join(
        HERE, "..", "..", "data", "monotonicity-c2-battery", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    add = add_rows_verbatim()
    can = cancel_rows()
    rs = add + can
    cols = ["item_id", "arm", "construction", "stem", "condition", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct", "calib",
            "privative_modifier"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    ncalib = sum(1 for r in rs if r["calib"] == "1")
    add_verbs = {r["stem"] for r in add}
    can_nouns = {r["stem"] for r in can}
    print(f"wrote {len(rs)} items ({len(add)} add [verbatim s135] + {len(can)} cancel) -> {out}")
    print(f"  add: {len(add_verbs)} resultative verbs x (control/construction/cue) [REUSED, sha {ADD_SRC_SHA}]")
    print(f"  cancel: {len(can_nouns)} privative nouns x (default/construction/cue)")
    print(f"  calib subset: {ncalib} items (add cut/hammer/kick/push + cancel {sorted(CALIB_CANCEL)})")
    print(f"  add/cancel stem overlap = {add_verbs & can_nouns or 'NONE (clean)'}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
