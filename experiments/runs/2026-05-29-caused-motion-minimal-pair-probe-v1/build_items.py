"""Build and freeze the caused-motion minimal-pair item set (probe v1, 2026-05-29).

Pre-registration (charter §8): EMITS experiments/data/caused-motion/items.csv and must
be run and committed BEFORE any probe call. Instantiates conjecture/caused-motion-
construction with the project's OWN stimuli (not Scivetti's items), under the ratified
constructional-divergence-operationalization (both instruments NLI + forced-choice;
T1 gap >=30pp; atypical within-15pp; cm rate >=70% per the conjecture's confirm bar).

DESIGN (frozen here, before the run)
------------------------------------
Goldberg's (1995) caused-motion construction `Subj V Obj Obl(path)` coerces a
causation-of-motion entailment onto NON-motion, NON-transitive verbs:
  "Maria sneezed the napkin off the table." -> the napkin moved, AND her sneezing caused it.
*sneeze* is intransitive and denotes no motion, so an affirmed causation-of-motion
inference here cannot come from the verb's lexical frame -- it must be CONSTRUCTIONAL.

PRIMARY INDICATOR: "affirm caused-motion rate" on the hypothesis
  "<Subj>'s <gerund> caused <obj> to move."  (FC answer YES, or NLI label 0).
The conjecture (confirm bar): cm rate >=70% with a >=30pp gap vs. controls, in >=2/3
models, holding for held-out/low-frequency verbs.

THREE FORMS per verb (verb held constant; only the construction/causal structure varies):
  cm        caused-motion frame              -> caused motion: YES   (NLI 0)
  ctrl-loc  intransitive verb; object stated to STAY put
            ("Maria sneezed. The napkin stayed on the table.")
                                             -> caused motion: NO    (NLI 2, contradiction)
  ctrl-sep  object moves, but by ANOTHER cause, co-temporal with the verb
            ("The napkin blew off the table in a draft while Maria sneezed.")
                                             -> V-caused motion: NO  (NLI 2, contradiction)
ctrl-loc handles the no-motion case; ctrl-sep is the CAUSATION-SPECIFIC control (motion
is present but not caused by the verb), guarding against a model that just detects motion.
The path-PP that could telegraph motion on its own (conjecture caveat) is present in BOTH
cm and ctrl-sep, so the cm-vs-ctrl-sep contrast isolates causal attribution, not the PP.

ARMS:
  - typical verbs (canonical caused-motion coercions: sneeze, cough, laugh, whistle, wink)
  - atypical verbs (low-frequency-in-construction non-motion verbs: yawn, snore, hiccup,
    shudder, shiver) = the memorization/frequency control (P3): the construction should
    still coerce caused-motion for verbs that essentially never appear in this frame.

Run: python3 build_items.py   (no API; just writes the frozen CSV)
"""
import csv, hashlib, os

# (verb, past, gerund, typicality, animacy, subject, obj_np, static_loc, cm_sentence, sep_sentence)
# animacy = object animacy: "inanimate" objects give a CRISP physical-propulsion
# "caused to move" reading; "animate" objects (actor/dog/cat...) are volitional
# self-movers responding to a signal -- a softer caused-motion (the agent could refuse).
# The result reports the inanimate-propulsion CORE separately (adversarial-pass fix).
VERBS = [
    ("sneeze", "sneezed", "sneezing", "typical", "inanimate", "Maria", "the napkin", "on the table",
     "Maria sneezed the napkin off the table.",
     "The napkin blew off the table in a draft while Maria sneezed."),
    ("cough", "coughed", "coughing", "typical", "inanimate", "Jordan", "the crumbs", "on the counter",
     "Jordan coughed the crumbs across the counter.",
     "The crumbs scattered across the counter when a fan switched on as Jordan coughed."),
    ("huff", "huffed", "huffing", "typical", "inanimate", "Lena", "the papers", "on the desk",
     "Lena huffed the papers off the desk.",
     "The papers slid off the desk when the window blew open while Lena huffed."),
    ("laugh", "laughed", "laughing", "typical", "animate", "Priya", "the actor", "on the stage",
     "Priya laughed the actor off the stage.",
     "The actor strode off the stage on cue while Priya laughed."),
    ("whistle", "whistled", "whistling", "typical", "animate", "Tomas", "the dog", "in the room",
     "Tomas whistled the dog out of the room.",
     "The dog wandered out of the room after a scent while Tomas whistled."),
    ("hiccup", "hiccuped", "hiccuping", "atypical", "inanimate", "Carlos", "the coins", "on the counter",
     "Carlos hiccuped the coins off the counter.",
     "The coins slid off the counter when the table tilted as Carlos hiccuped."),
    ("shiver", "shivered", "shivering", "atypical", "inanimate", "Sam", "the snow", "on his coat",
     "Sam shivered the snow off his coat.",
     "The snow slid off his coat in the wind while Sam shivered."),
    ("yawn", "yawned", "yawning", "atypical", "animate", "Omar", "the cat", "on his lap",
     "Omar yawned the cat off his lap.",
     "The cat sprang off his lap to chase a moth while Omar yawned."),
    ("snore", "snored", "snoring", "atypical", "animate", "Nina", "the kitten", "on the bed",
     "Nina snored the kitten off the bed.",
     "The kitten leapt off the bed at a sudden noise while Nina snored."),
    ("shudder", "shuddered", "shuddering", "atypical", "animate", "Aisha", "the spider", "on her sleeve",
     "Aisha shuddered the spider off her sleeve.",
     "The spider dropped off her sleeve on its own while Aisha shuddered."),
]
# NOTE (adversarial pass): shudder/shiver themselves denote body-motion, so a positive cm
# there is less diagnostic of pure constructional coercion (the body movement can
# physically dislodge the object) -- flagged in the result's Limits, kept for the
# atypical/frequency arm but not load-bearing for the lexicon-excludes-motion argument.


def rows():
    out = []
    for v, past, ger, typ, anim, subj, obj, loc, cm, sep in VERBS:
        hyp = f"{subj}'s {ger} caused {obj} to move."
        ctrl_loc = f"{subj} {past}. {obj[0].upper()}{obj[1:]} stayed {loc}."
        forms = [
            ("cm", cm, "0", "YES", "1"),              # caused motion entailed
            ("ctrl-loc", ctrl_loc, "2", "NO", "0"),   # object stayed -> contradiction (motion denied)
            # ctrl-sep: object moved by ANOTHER cause; the premise asserts an alternative
            # cause but does NOT deny a verb-contribution, so the causal hypothesis is
            # NOT-ENTAILED (neutral), not contradicted (adversarial-pass fix). Affirming
            # V-caused-motion is still wrong (affirm_correct=0).
            ("ctrl-sep", sep, "1", "CANT_TELL", "0"),
        ]
        for form, sent, nli_gold, fc_gold, affirm_correct in forms:
            out.append(dict(
                item_id=f"{v}-{form}", verb=v, typicality=typ, animacy=anim, form=form,
                subject=subj, obj_np=obj, sentence=sent, nli_hypothesis=hyp,
                nli_gold=nli_gold, fc_gold=fc_gold, affirm_correct=affirm_correct))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                       "data", "caused-motion", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "verb", "typicality", "animacy", "form", "subject", "obj_np",
            "sentence", "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    nt = sum(1 for v in VERBS if v[3] == "typical")
    print(f"wrote {len(rs)} items ({len(VERBS)} verbs x 3 forms) -> {out}")
    print(f"  typical verbs: {nt}, atypical verbs: {len(VERBS)-nt}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
