"""Build and freeze the conative minimal-pair item set (probe v1, 2026-05-29).

Pre-registration (charter §8): this script EMITS
experiments/data/conative/items.csv and must be run and the CSV committed BEFORE
any probe call. The item set instantiates conjecture/conative-construction with the
project's OWN verb-held-constant minimal pairs (NOT Scivetti's items), under the
ratified divergence operationalization (constructional-divergence-operationalization:
both instruments NLI + forced-choice; T1 gap >=30pp; atypical within-15pp).

DESIGN (frozen here, before the run)
------------------------------------
The conative alternation holds the VERB constant and varies only the construction:
  transitive  "Maria kicked the ball."      -> entails completed contact
  conative    "Maria kicked at the ball."   -> contact NOT entailed (attempted/directed-at)
We probe whether the panel affirms completed contact LESS for the conative *at*-frame
than for the matched transitive, with the verb held constant.

PRIMARY INDICATOR: "affirm completed-contact rate" per frame
  = forced-choice answer YES, or NLI label 0 (entailment), on the contact hypothesis.
  Predicted gap (conjecture P1): transitive_affirm - conative_affirm >= 30pp,
  replicating across the Levin conative-class verbs (not one verb), in >=2/3 models.

ARMS
  1. conative-class verbs x {typical, atypical} object  (Levin hit/swat/cut classes:
     all take the conative). Typical vs atypical objects = the memorization/frequency
     control (conjecture P3 / constructional-vs-frequency-confound): the non-completion
     reading should PERSIST for low-frequency objects (atypical gap within 15pp of typical).
  2. control (non-alternating) verbs (touch- and break-class: do NOT take the conative),
     typical object only. P2 verb-class prediction: the contact-cancellation should be
     WEAKER/absent here (the *at*-frame is not a licit conative). Gold for the control
     CONATIVE cell is uncertain (the string is anomalous), so that cell is reported as an
     affirm-rate, NOT scored for accuracy (nli_gold/fc_gold = NA).

Verb-class membership is from Levin (1993) conative-alternation classes (hit, swat, cut)
vs. non-alternating contact classes (touch, break) -- the descriptive premise of P2.
Names/objects are hand-authored so the contrast is the construction, not plausibility.

Run: python3 build_items.py   (no API; just writes the frozen CSV)
"""
import csv, hashlib, os

# verb : (past_tense, typical_object, atypical_object)
# All 12 are Levin (1993) conative-alternation verbs (hit / swat / cut classes).
CONATIVE_VERBS = [
    ("kick",    "kicked",    "ball",     "gourd"),
    ("hit",     "hit",       "pinata",   "gong"),
    ("punch",   "punched",   "bag",      "effigy"),
    ("slash",   "slashed",   "rope",     "tarp"),
    ("stab",    "stabbed",   "mattress", "bolster"),
    ("claw",    "clawed",    "curtain",  "settee"),
    ("swat",    "swatted",   "cushion",  "divan"),
    ("jab",     "jabbed",    "pad",      "mannequin"),
    ("chop",    "chopped",   "log",      "sapling"),
    ("scratch", "scratched", "post",     "lectern"),
    ("hack",    "hacked",    "branch",   "bramble"),
    ("strike",  "struck",    "bell",     "cymbal"),
]
# Verb-set revision (pre-run, after the adversarial coherence pass, 2026-05-29):
# - bite -> stab and peck -> strike: bite/peck have a dominant ITERATIVE-contact reading,
#   so "bit/pecked at NP" can still entail contact (wrong-direction gold) and their bare
#   transitive only weakly entails completed contact (conjecture Notes/caveats: anchor on
#   verbs where the transitive's completion entailment is robust). stab/strike are clean
#   Levin swat/hit-class conatives where "V the NP" robustly entails contact and "V at NP"
#   cancels it.
# - swat object fly -> cushion: "swatted the fly" does not robustly entail contact
#   (you swat AND MISS), which would shrink the T-vs-conative gap for non-constructional
#   reasons; a swatted cushion is contacted. swat's transitive contact is still the softest
#   of the set -- noted in the result's Limits.
# - hit object drum/anvil -> pinata/gong: "hit at the pinata" is a more idiomatic conative.
# All 12 verbs are Levin (1993) conative-alternation verbs (hit/swat/cut classes).

# Non-alternating contact verbs: touch-class (touch, kiss) and break-class (break,
# shatter) do NOT take the conative in Levin (1993). Typical object only.
CONTROL_VERBS = [
    ("touch",   "touched",   "wall"),
    ("kiss",    "kissed",    "child"),
    ("break",   "broke",     "vase"),
    ("shatter", "shattered", "window"),
]

# Subjects rotate so no single name dominates; the SAME subject is used across the two
# frames of a verb (true minimal pair: only "at" differs) and across its object types.
SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
            "Aisha", "Sam", "Wei", "Dana", "Hana", "Luca", "Iris", "Mara"]


def rows():
    out = []
    si = 0
    # Arm 1: conative-class verbs, typical + atypical objects
    for verb, past, typ_obj, atyp_obj in CONATIVE_VERBS:
        subj = SUBJECTS[si % len(SUBJECTS)]; si += 1
        for otype, obj in (("typical", typ_obj), ("atypical", atyp_obj)):
            obj_np = f"the {obj}"
            hyp = f"{subj} made contact with {obj_np}."
            for frame in ("transitive", "conative"):
                at = "at " if frame == "conative" else ""
                sent = f"{subj} {past} {at}{obj_np}."
                # construction-correct: transitive affirms contact; conative does not.
                affirm_correct = "1" if frame == "transitive" else "0"
                nli_gold = "0" if frame == "transitive" else "1"  # entail vs neutral
                fc_gold = "YES" if frame == "transitive" else "CANT_TELL"
                out.append(dict(
                    item_id=f"{verb}-{otype}-{frame}", verb=verb, verb_class="conative",
                    object_type=otype, frame=frame, subject=subj, object_np=obj_np,
                    sentence=sent, nli_hypothesis=hyp, nli_gold=nli_gold, fc_gold=fc_gold,
                    affirm_correct=affirm_correct))
    # Arm 2: control (non-alternating) verbs, typical object only
    for verb, past, obj in CONTROL_VERBS:
        subj = SUBJECTS[si % len(SUBJECTS)]; si += 1
        obj_np = f"the {obj}"
        hyp = f"{subj} made contact with {obj_np}."
        for frame in ("transitive", "conative"):
            at = "at " if frame == "conative" else ""
            sent = f"{subj} {past} {at}{obj_np}."
            if frame == "transitive":
                affirm_correct, nli_gold, fc_gold = "1", "0", "YES"
            else:
                # control conative string is anomalous -> gold uncertain, not scored
                affirm_correct, nli_gold, fc_gold = "NA", "NA", "NA"
            out.append(dict(
                item_id=f"{verb}-control-{frame}", verb=verb, verb_class="control",
                object_type="control", frame=frame, subject=subj, object_np=obj_np,
                sentence=sent, nli_hypothesis=hyp, nli_gold=nli_gold, fc_gold=fc_gold,
                affirm_correct=affirm_correct))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                       "data", "conative", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "verb", "verb_class", "object_type", "frame", "subject",
            "object_np", "sentence", "nli_hypothesis", "nli_gold", "fc_gold",
            "affirm_correct"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    nc = sum(1 for r in rs if r["verb_class"] == "conative")
    print(f"wrote {len(rs)} items -> {out}")
    print(f"  conative-class: {nc} ({len(CONATIVE_VERBS)} verbs x 2 obj-types x 2 frames)")
    print(f"  control: {len(rs)-nc} ({len(CONTROL_VERBS)} verbs x 2 frames)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
