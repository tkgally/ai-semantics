"""Build + freeze the off-ceiling argument-structure coercion v2 item set (2026-05-29).

Pre-registration (charter §8): EMITS experiments/data/argument-structure-coercion-v2/items.csv,
run + committed BEFORE any probe call. Operationalizes design/argument-structure-coercion-v2
under the RATIFIED difficulty gate (decisions/resolved/cc-v2-difficulty-operationalization,
2026-05-29: UNIFY + adopt default). The difficulty axes were fixed by that decision BEFORE
this build — no retuning. No logprobs needed (behavioral NLI+FC), so this runs on the
existing 3-family behavioral panel (config/models.md).

WHY v2 (escape the v1 ceiling)
------------------------------
The two add-direction v1 positives (caused-motion, way) were CEILING results on easy
controls -> they cannot separate:
  (H-deep)    the model COMPUTES the construction's added inference (and would WITHHOLD it
              when a resolving cue blocks it), versus
  (H-default) the model DEFAULTS to "yes" on a well-formed coercion (a learned
              "this frame -> yes" template a conflicting cue cannot override).
On the v1 instruments these predict the SAME near-ceiling affirm rate. v2 forces them apart.

PRIMARY ARM = CONFLICTING-CUE MINIMAL PAIR (the key discriminator)
-----------------------------------------------------------------
Hold the construction + verb CONSTANT; toggle a later clause that explicitly DENIES the
construction's added inference:
  canonical : "Maria sneezed the napkin off the table."                      affirm-gold YES
  cue       : "Maria sneezed the napkin off the table, but the napkin never moved." affirm-gold NO
The cue sentence is internally resolved: the second clause STATES the inference is false.
A model that still affirms the inference is privileging the construction template over the
explicit denial (H-default). A model that withholds is respecting the cue (H-deep).
Indicator: affirm-construction-inference rate per condition; the KEY numbers are the cue
affirm rate (low = cue-respecting / H-deep; high = template / H-default) and the
canonical->cue DROP. Reading rule (ratified, report-the-rate): cue affirm >=70% in >=2/3
models = robustly template/cue-ignoring; ~chance/low = cue-respecting. No pass bar that
manufactures a result; the null (either direction) is first-class.

SECONDARY ARM = COERCION-RESISTING VERB (graded-ladder middle rung)
------------------------------------------------------------------
Same frame, a verb whose semantics RESIST the coercion (cognition/stative for caused-motion;
self-motion-precluding for way): "Maria knew the napkin off the table." / "Mia slept her way
down the hall." Anomalous coercions; affirm-gold NO (the inference is not warranted). Report
the rate: mechanical affirmation here is further H-default evidence; flagging anomaly is H-deep.

GRADED DIFFICULTY LADDER: canonical (d1) < resist-verb (d2) < cue-conflict (d3).
Degradation shape (ratified): affirm rate monotone-declining with shallow slope = graceful
(stressable computation); flat-at-ceiling-then-cliff = brittle template. The slope is read
off the frozen d1->d2->d3 affirm rates (no threshold tuned after the fact).

HUMAN ANCHOR: pending / internal-contrast-only (ratified Option-4 logic). The Scivetti CxNLI
subsets contain NO conflicting-cue / coercion-resisting items, and the "correct" reading of
an anti-cued coercion is itself contestable for humans -> NO human baseline is asserted; the
result is read as an internal H-deep-vs-H-default contrast. No human label invented.

Run: python3 build_items.py   (no API; writes the frozen CSV)
"""
import csv, hashlib, os

# ---- caused-motion stems: inanimate objects (crisp physical motion) -----------------
# (verb, past, ger, resist_past, resist_ger, subj, obj, obj_pron, path, deny_clause)
CM = [
    ("sneeze","sneezed","sneezing","knew","knowing","Maria","the napkin","it","off the table","but the napkin never moved"),
    ("cough","coughed","coughing","understood","understanding","Jordan","the crumbs","they","across the counter","but the crumbs stayed in place"),
    ("huff","huffed","huffing","believed","believing","Lena","the papers","they","off the desk","but the papers did not budge"),
    ("whistle","whistled","whistling","knew","knowing","Tomas","the feather","it","off the ledge","but the feather stayed on the ledge"),
    ("gasp","gasped","gasping","remembered","remembering","Omar","the dust","it","off the shelf","but the dust never moved"),
    ("snore","snored","snoring","assumed","assuming","Nina","the petals","they","off the nightstand","but the petals stayed put"),
    ("hiccup","hiccuped","hiccuping","doubted","doubting","Carlos","the coins","they","off the counter","but the coins did not move"),
    ("puff","puffed","puffing","believed","believing","Dana","the wrapper","it","off the tray","but the wrapper never moved"),
    ("cough","coughed","coughing","knew","knowing","Sam","the ash","it","off the table","but the ash stayed where it was"),
    ("sneeze","sneezed","sneezing","understood","understanding","Ravi","the confetti","it","off the table","but the confetti stayed on the table"),
]

# ---- way stems: self-motion-precluding resist verbs ---------------------------------
# (verb, past, resist_past, subj, pron, poss, path, start_place)
WAY = [
    ("whistle","whistled","slept","Mia","she","her","down the hall","the doorway"),
    ("hum","hummed","fainted","Theo","he","his","through the crowd","the entrance"),
    ("laugh","laughed","slept","Priya","she","her","across the room","the corner"),
    ("sing","sang","fainted","Lena","she","her","up the stairs","the bottom step"),
    ("mutter","muttered","slept","Karl","he","his","along the corridor","his office door"),
    ("chat","chatted","dozed","Hana","she","her","through the gallery","the lobby"),
    ("joke","joked","fainted","Owen","he","his","down the aisle","his seat"),
    ("eat","ate","slept","Sofia","she","her","across the buffet","the entrance"),
    ("gossip","gossiped","dozed","Bea","she","her","across the lobby","the door"),
    ("drink","drank","fainted","Nico","he","his","down the bar","the first stool"),
]


def rows():
    out = []
    # caused-motion: hypothesis is verb-specific (uses the sentence verb's gerund)
    for (v,past,ger,rpast,rger,subj,obj,opron,path,deny) in CM:
        objcap = obj[0].upper()+obj[1:]
        canon = f"{subj} {past} {obj} {path}."
        resist = f"{subj} {rpast} {obj} {path}."
        cue = f"{subj} {past} {obj} {path}, {deny}."
        conds = [
            # cond, difficulty, sentence, gerund-for-hyp, nli_gold, fc_gold, affirm_correct
            ("canonical","1",canon,ger,"0","YES","1"),
            ("resist","2",resist,rger,"2","NO","0"),
            ("cue","3",cue,ger,"2","NO","0"),
        ]
        for cond,diff,sent,g,nli_gold,fc_gold,ac in conds:
            hyp = f"{subj}'s {g} caused {obj} to move."
            out.append(dict(item_id=f"cm-{v}-{subj}-{cond}", construction="caused-motion",
                stem=f"{v}-{subj}", condition=cond, difficulty=diff, sentence=sent,
                nli_hypothesis=hyp, nli_gold=nli_gold, fc_gold=fc_gold, affirm_correct=ac))
    # way: hypothesis is verb-independent (subject moved from one place to another)
    for (v,past,rpast,subj,pron,poss,path,start) in WAY:
        hyp = f"{subj} moved from one place to another."
        canon = f"{subj} {past} {poss} way {path}."
        resist = f"{subj} {rpast} {poss} way {path}."
        cue = f"{subj} {past} {poss} way {path}, but {pron} never left {start}."
        conds = [
            ("canonical","1",canon,"0","YES","1"),
            ("resist","2",resist,"2","NO","0"),
            ("cue","3",cue,"2","NO","0"),
        ]
        for cond,diff,sent,nli_gold,fc_gold,ac in conds:
            out.append(dict(item_id=f"way-{v}-{subj}-{cond}", construction="way",
                stem=f"{v}-{subj}", condition=cond, difficulty=diff, sentence=sent,
                nli_hypothesis=hyp, nli_gold=nli_gold, fc_gold=fc_gold, affirm_correct=ac))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","data",
                                       "argument-structure-coercion-v2","items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id","construction","stem","condition","difficulty","sentence",
            "nli_hypothesis","nli_gold","fc_gold","affirm_correct"]
    with open(out,"w",newline="") as f:
        w = csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rs)
    h = hashlib.sha256(open(out,"rb").read()).hexdigest()[:16]
    nc = sum(1 for r in rs if r["construction"]=="caused-motion")
    print(f"wrote {len(rs)} items ({nc} caused-motion + {len(rs)-nc} way) -> {out}")
    print(f"  conditions: canonical/resist/cue x {len(CM)} cm stems + {len(WAY)} way stems")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
