"""Build + freeze the off-ceiling CANCEL-DIRECTION conative item set (2026-05-30).

Pre-registration (charter s8): EMITS experiments/data/conative-cancel-v2/items.csv,
run + committed BEFORE any probe call. This is the COMPANION harder-conative
(cancel-direction) probe that design/argument-structure-coercion-v2 s5 + hook 3 call
for, governed by the SAME ratified gate (decisions/resolved/cc-v2-difficulty-
operationalization, 2026-05-30 amendment unifies CC + caused-motion + way + companion
conative). No new decision. No logprobs needed (behavioral NLI+FC) -> runs on the
existing 3-family behavioral panel (config/models.md).

WHY (de-confound the add/cancel asymmetry from ceiling)
-------------------------------------------------------
The project carries a TENTATIVE generalization: decoders more readily LICENSE a
construction's ADDED inference (caused-motion, way -> v1 ceiling) than SUPPRESS a
lexically-default one (the conative's completed-contact -> v1 off-ceiling, fragile).
But "add easier than cancel" is currently CONFOUNDED WITH CEILING: the add probes ran
at ceiling, the cancel probe ran off ceiling. This probe puts the CANCEL direction in
the SAME conflicting-cue paradigm as the off-ceiling add-direction v2
(2026-05-29-argument-structure-coercion-probe-v2), so the two directions can be
compared at matched task structure.

THE CANCEL DIRECTION
--------------------
The conative ("kicked AT the ball") CANCELS the contact entailment that the transitive
("kicked the ball") carries. Hypothesis throughout: "<subj> made contact with <obj>."

Conditions per Levin conative-class verb (verb + object held constant; typical object):
  transitive (d1): "Maria kicked the ball."                      contact ENTAILED   affirm-gold YES
  conative   (d2): "Maria kicked at the ball."                   contact SUPPRESSED  affirm-gold NO (construction-correct = withhold)
  cue        (d3): "Maria kicked at the ball, and the ball       contact RE-ASSERTED affirm-gold YES
                    sailed across the field."                    by an explicit consequence that conflicts with the conative's cancellation

The CUE condition is the cancel-direction mirror of the add-direction's cue: there an
explicit clause DENIED the added inference (and the model should withhold); here an
explicit consequence RE-ASSERTS the suppressed inference (and the model should affirm).
The matched discriminators:
  - SUPPRESSION (no cue): 100 - conative_affirm = construction-following with no cue.
    Compare to add-direction CANONICAL affirm (licensing with no cue).
  - CUE-FOLLOWING: cue_affirm = does the model update toward contact under the explicit
    cue, overriding the conative? Compare to add-direction's cue (where cue-following =
    100 - cue_affirm, i.e. withholding the denied inference).
If suppression-no-cue stays LOWER than licensing-no-cue even with the cue arm present,
the asymmetry is about DIRECTION (real). If both directions handle the cue comparably
and only the no-cue canonical differs, the v1 asymmetry was about canonical difficulty.
Either reading is first-class; no pass bar manufactures it.

RESIST ARM (mirror of the add-direction's coercion-resisting verb)
------------------------------------------------------------------
Non-alternating contact verbs (touch-/break-class; do NOT take the conative in Levin
1993) forced into the conative frame: "Maria touched at the wall." Anomalous; gold
uncertain -> NA, report the affirm rate only (mechanical contact-affirm here vs the
transitive baseline is the quantity).

HUMAN ANCHOR: pending / internal-contrast-only (ratified Option-4 logic, same as the
add-direction v2). Scivetti CxNLI has no conflicting-cue items; the contact-cued
conative's "correct" reading is contestable for humans -> NO human baseline asserted.
The transitive vs conative MINIMAL PAIR retains the v1 phenomenon-level conative anchor
(Scivetti conative subset, ratified) but the CUE arm is internal-contrast-only.

Run: python3 build_items.py   (no API; writes the frozen CSV)
"""
import csv, hashlib, os

# Levin (1993) conative-alternation verbs (hit/swat/cut classes): the transitive robustly
# entails completed contact; the conative "V at NP" cancels it. Reuses the v1 conative
# verb set (experiments/runs/2026-05-29-conative-minimal-pair-probe-v1) with its typical
# objects, plus a per-verb CONTACT-CONSEQUENCE clause that entails contact occurred WITHOUT
# echoing the hypothesis verb "made contact" (so the cue is a real-world consequence, not a
# restatement of the gold).
# (verb, past, typical_object, contact_consequence_clause)
CONATIVE = [
    ("kick",    "kicked",    "ball",     "and the ball sailed across the field"),
    ("hit",     "hit",       "pinata",   "and the pinata burst open"),
    ("punch",   "punched",   "bag",      "and the bag swung back hard"),
    ("slash",   "slashed",   "rope",     "and the rope split in two"),
    ("stab",    "stabbed",   "mattress", "and the blade sank deep into it"),
    ("claw",    "clawed",    "curtain",  "leaving deep gashes in it"),
    ("swat",    "swatted",   "balloon",  "and the balloon shot across the room"),
    ("jab",     "jabbed",    "pad",      "and the pad jolted backward"),
    ("chop",    "chopped",   "log",      "and the log split cleanly"),
    ("scratch", "scratched", "post",     "leaving a long gouge in it"),
    ("hack",    "hacked",    "branch",   "and the branch came clean off"),
    ("whack",   "whacked",   "melon",    "and the melon split open"),
]
# Verb/object/cue revision (pre-run, after the independent adversarial critique, 2026-05-30):
# - swat object cushion -> balloon: "swatted at the cushion" (stationary) is marginal and
#   "tumbled off the sofa" under-determines contact (a cushion can be jostled); "swatted the
#   balloon" robustly entails contact, "swatted at the balloon" cancels, and "shot across the
#   room" entails forceful contact.
# - strike/bell -> whack/melon: "strike at" has a dominant idiomatic aim/attack reading
#   ("strike at the enemy/root") so "struck at the bell" is a marginal physical conative, and
#   "the bell rang out" only weakly entails THIS subject's contact. whack is a clean Levin
#   hit-class conative; "the melon split open" entails forceful contact.
# - jab cue "shuddered from the blow" -> "jolted backward": "from the blow" presupposes a
#   landed strike (edges toward restating the contact hypothesis); "jolted backward" entails
#   contact without the near-circular phrasing.
# KNOWN WEAK-CONTRAST PAIRS (kept, flagged): scratch/claw are surface-contact verbs whose "at"
# frame still implies iterative grazing contact, so the conative cancels EFFECTIVE/completed
# contact only weakly -> these may pull conative_affirm up; reported with this caveat, not
# scored as the headline suppression cells alone.

# Non-alternating contact verbs (touch-class touch/kiss; break-class break/shatter): do NOT
# take the conative in Levin (1993). The "V at NP" frame is anomalous -> resist arm.
CONTROL = [
    ("touch",   "touched",   "wall"),
    ("embrace", "embraced",  "child"),   # was kiss: "kiss at" alternates (air-kissing); embrace does not
    ("break",   "broke",     "vase"),
    ("shatter", "shattered", "window"),
]

# Same subject across a verb's conditions (true minimal pair); rotate so no name dominates.
SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
            "Aisha", "Sam", "Wei", "Dana", "Hana", "Luca", "Iris", "Mara"]


def rows():
    out, si = [], 0
    # Arm 1: conative-class verbs -> transitive (d1) / conative (d2) / cue (d3)
    for verb, past, obj, consequence in CONATIVE:
        subj = SUBJECTS[si % len(SUBJECTS)]; si += 1
        obj_np = f"the {obj}"
        hyp = f"{subj} made contact with {obj_np}."
        conds = [
            # condition, difficulty, sentence, nli_gold, fc_gold, affirm_correct
            ("transitive", "1", f"{subj} {past} {obj_np}.",                       "0", "YES",       "1"),
            ("conative",   "2", f"{subj} {past} at {obj_np}.",                    "1", "CANT_TELL", "0"),
            ("cue",        "3", f"{subj} {past} at {obj_np}, {consequence}.",     "0", "YES",       "1"),
        ]
        for cond, diff, sent, ng, fg, ac in conds:
            out.append(dict(item_id=f"con-{verb}-{cond}", construction="conative",
                stem=f"{verb}-{subj}", condition=cond, difficulty=diff, sentence=sent,
                nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg, affirm_correct=ac))
    # Arm 2: control (non-alternating) verbs -> transitive (d1) / resist=anomalous conative (d2, NA)
    for verb, past, obj in CONTROL:
        subj = SUBJECTS[si % len(SUBJECTS)]; si += 1
        obj_np = f"the {obj}"
        hyp = f"{subj} made contact with {obj_np}."
        conds = [
            ("transitive", "1", f"{subj} {past} {obj_np}.",    "0",  "YES", "1"),
            ("resist",     "2", f"{subj} {past} at {obj_np}.", "NA", "NA",  "NA"),
        ]
        for cond, diff, sent, ng, fg, ac in conds:
            out.append(dict(item_id=f"ctrl-{verb}-{cond}", construction="conative-control",
                stem=f"{verb}-{subj}", condition=cond, difficulty=diff, sentence=sent,
                nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg, affirm_correct=ac))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                       "conative-cancel-v2", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "construction", "stem", "condition", "difficulty", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    nco = sum(1 for r in rs if r["construction"] == "conative")
    print(f"wrote {len(rs)} items ({nco} conative-class + {len(rs)-nco} control) -> {out}")
    print(f"  conative: {len(CONATIVE)} verbs x (transitive/conative/cue); "
          f"control: {len(CONTROL)} verbs x (transitive/resist)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
