"""Build + freeze the IMPLICIT-WORLD-KNOWLEDGE caused-motion cue probe (v2b, 2026-05-30).

Pre-registration (charter s8): EMITS experiments/data/coercion-implicit-cue-v2b/items.csv,
run + committed BEFORE any probe call. This is the v2b the add-direction v2 deferred (its
README: "the cue is an EXPLICIT verbal denial ... a subtler world-knowledge cue is v2b").
Governed by the SAME ratified gate (decisions/resolved/cc-v2-difficulty-operationalization,
which fixes conflicting-cue as the primary axis + the graded ladder + report-the-rate). No
new decision. Behavioral NLI+FC, temperature 0, no logprobs -> existing 3-family panel.

WHAT v2 LEFT OPEN
-----------------
The add-direction v2 (2026-05-29) showed the caused-motion / way ceilings are cue-sensitive:
under an EXPLICIT denial ("...off the table, BUT THE NAPKIN NEVER MOVED") all 3 models drop
to floor -> they respect an explicit outcome statement (H-deep over H-default). But an
explicit "never moved" clause directly contradicts the hypothesis IN THE PREMISE; it does
not test whether the model integrates WORLD KNOWLEDGE to block a physically-impossible
coercion when no outcome is stated.

THE v2b MANIPULATION: implicit (world-knowledge) cue, graded against the explicit one
-------------------------------------------------------------------------------------
Hold verb + path constant; vary the OBJECT and the cue type:
  canonical    (d1): light/movable object        "Maria sneezed the dust off the pedestal."
                     -> caused motion plausible; affirm-gold YES (the v1/v2 ceiling anchor)
  implicit-wk  (d2): immovable object via an IN-PREMISE descriptor (bolted-down / cast-iron /
                     two-ton) that requires WORLD KNOWLEDGE to see the conflict, NO outcome
                     stated  "Maria sneezed the bolted-down bust off the pedestal."
                     -> a sneeze cannot move a bolted-down bust; affirm-gold NO (world-
                        knowledge-respecting), but CONTESTABLE (see human-anchor note)
  explicit     (d3): same immovable object + an EXPLICIT outcome denial (the v2-style cue,
                     here as the WITHIN-EXPERIMENT CALIBRATION)
                     "Maria sneezed the bolted-down bust off the pedestal, but it never budged."
                     -> affirm-gold NO, unambiguous (outcome stated)

KEY COMPARISON (the discriminator): implicit-wk affirm vs explicit affirm.
  - implicit-wk ~= explicit (both low)  => the model integrates the immovability descriptor /
    detects the world-knowledge anomaly WITHOUT needing an explicit outcome -> a STRONGER
    H-deep signal than v2 established.
  - implicit-wk >> explicit            => the model needs the explicit outcome statement; it
    does NOT block a physically-impossible coercion from world knowledge alone -> the v2
    cue-sensitivity was outcome-statement-parsing, not world-model integration.
Instrument note (reported, not corrected): under NLI the implicit-wk premise ASSERTS the
caused motion (the conflict is only with external world knowledge about "bolted-down"), so a
premise-internal NLI reading may affirm; under FC ("is it true that ...") world knowledge is
more naturally engaged. The NLI-vs-FC gap on the implicit-wk cell is itself a first-class
datum (cf. open-question/instrument-sensitivity-constructional-inference).

Reading rule (RATIFIED report-the-rate): affirm rate per condition; the headline is the
implicit-vs-explicit comparison + the canonical->cue drops, NOT a manufactured pass bar.
No threshold tuned after the run.

HUMAN ANCHOR: pending / internal-contrast-only (ratified Option-4 logic, same as v2). No
Scivetti conflicting-cue items; the physically-impossible coercion's "correct" reading is
contestable for humans -> NO human baseline asserted on the cue cells. No human label invented.

Run: python3 build_items.py   (no API; writes the frozen CSV)
"""
import csv, hashlib, os

# (verb, past, ger, subj, light_obj, heavy_obj_with_descriptor, path, deny_clause)
# verbs are involuntary breath/sound verbs that do NOT lexicalize propulsion -> the caused-
# motion reading is COERCED by the construction (Goldberg's canonical "sneezed the napkin off
# the table"). heavy objects carry an in-premise immovability descriptor (world knowledge).
SCENES = [
    ("sneeze","sneezed","sneezing","Maria","dust","bolted-down bust","off the pedestal","but it never budged"),
    ("cough","coughed","coughing","Jordan","crumbs","cast-iron anvil","across the floor","but it did not move"),
    ("wheeze","wheezed","wheezing","Lena","dry leaves","two-ton boulder","down the slope","but it stayed put"),
    ("whistle","whistled","whistling","Tomas","feather","solid-oak wardrobe","across the room","but it never shifted"),
    ("splutter","spluttered","spluttering","Omar","petals","granite urn","off the ledge","but it remained in place"),
    ("hiccup","hiccuped","hiccuping","Nina","confetti","solid bronze statuette","off the table","but it did not budge"),
    ("sneeze","sneezed","sneezing","Carlos","lint","steel safe","off the counter","but it stayed where it was"),
    ("hiccup","hiccuped","hiccuping","Dana","sawdust","granite slab","off the table","but it stayed put"),
    ("cough","coughed","coughing","Sam","ash","iron stove","across the kitchen","but it never moved"),
    ("sneeze","sneezed","sneezing","Aisha","glitter","cast-iron skillet","off the shelf","but it did not move"),
]
# Verb revision (pre-run, after the independent adversarial critique, 2026-05-30):
# huff/puff -> wheeze/splutter/hiccup and gasp/snore -> splutter/sneeze/hiccup. huff/puff
# LEXICALIZE directed air-propulsion (the docstring's own disqualifier, like "blow"), so
# their canonical YES could be literal rather than COERCED; gasp is an inward intake (wrong
# direction) and snore is non-directed vibration (feeble) -> implausible canonicals. The
# replacements are all INTRANSITIVE involuntary outbursts whose transitive caused-motion is
# genuinely coerced (sneeze/cough/wheeze/splutter/hiccup). Paths refit to the light object
# (gasp scene's dangling "off its base" -> "off the ledge"; Aisha "away from the wall" ->
# "off the shelf") so the canonical reads cleanly for both objects.


def rows():
    out = []
    for (v,past,ger,subj,light,heavy,path,deny) in SCENES:
        light_np, heavy_np = f"the {light}", f"the {heavy}"
        conds = [
            # condition, difficulty, object_np, sentence-tail, nli_gold, fc_gold, affirm_correct
            ("canonical","1",light_np, f"{subj} {past} {light_np} {path}.",                 "0","YES","1"),
            ("implicit-wk","2",heavy_np, f"{subj} {past} {heavy_np} {path}.",                "1","NO","0"),
            ("explicit","3",heavy_np, f"{subj} {past} {heavy_np} {path}, {deny}.",           "2","NO","0"),
        ]
        for cond,diff,obj_np,sent,ng,fg,ac in conds:
            hyp = f"{subj}'s {ger} caused {obj_np} to move."
            out.append(dict(item_id=f"cm-{v}-{subj}-{cond}", construction="caused-motion",
                stem=f"{v}-{subj}", condition=cond, difficulty=diff, sentence=sent,
                nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg, affirm_correct=ac))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","data",
                                       "coercion-implicit-cue-v2b","items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id","construction","stem","condition","difficulty","sentence",
            "nli_hypothesis","nli_gold","fc_gold","affirm_correct"]
    with open(out,"w",newline="") as f:
        w = csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rs)
    h = hashlib.sha256(open(out,"rb").read()).hexdigest()[:16]
    print(f"wrote {len(rs)} items ({len(SCENES)} scenes x canonical/implicit-wk/explicit) -> {out}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
