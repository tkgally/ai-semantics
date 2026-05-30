"""Build + freeze the coercion-as-sense-modulation bridge stimuli (v1, 2026-05-30).

Operationalizes design/coercion-as-sense-modulation-v1 (the lexicon-grammar BRIDGE): reuses
the lexical v1 DURel/continuous relatedness instrument on CONSTRUCTIONAL coercion stimuli.
The target is the VERB, marked with «guillemets» in both sentences. Each item = one verb,
sentence1 = a bare/neutral use, sentence2 = the arm's frame:
  coerced-cm   : the caused-motion coercion (verb + object + path) -> predicted LOWER relatedness
  coerced-way  : the way-construction coercion (verb + POSS way + path) -> predicted LOWER
  control-elab : a length-matched NON-coercing elaboration of the same verb -> predicted HIGH
  polysemy-anchor: a genuine lexical sense shift of a polysemous/homonymous verb (calibrates
                   the low end; the instrument must read these LOW or a null is uninterpretable)

The KEY contrast is within-verb: control-elab (high) vs coerced (?) — a positive gap means the
model registers constructional coercion as lexical sense modulation. Internal-contrast-only
(anchor pending). No human gold. Own constructed sentences (committable; no corpus/licence).

Run: python3 build_items.py    (no API; writes the frozen CSV)
"""
import csv
import hashlib
import os

# verb, bare-use, caused-motion coercion, non-coercing elaboration  (verb marked with «»)
CM = [
    ("sneeze", "She «sneezed».", "She «sneezed» the napkin off the table.",
     "She «sneezed» twice during the lecture."),
    ("cough", "He «coughed».", "He «coughed» the crumb across the table.",
     "He «coughed» quietly into his sleeve."),
    ("blow", "She «blew» softly.", "She «blew» the dust off the shelf.",
     "She «blew» gently on her hot tea."),
    ("puff", "He «puffed».", "He «puffed» the feather off his palm.",
     "He «puffed» slowly on his pipe."),
    ("huff", "She «huffed».", "She «huffed» the wrapper off the tray.",
     "She «huffed» in obvious frustration."),
    ("fan", "He «fanned» himself.", "He «fanned» the smoke out of the room.",
     "He «fanned» himself in the summer heat."),
]
# verb, bare-use, way-construction coercion, non-coercing elaboration
WAY = [
    ("whistle", "She «whistled».", "She «whistled» her way down the hall.",
     "She «whistled» a cheerful little tune."),
    ("sing", "He «sang».", "He «sang» his way through the crowd.",
     "He «sang» a quiet evening lullaby."),
    ("dance", "She «danced».", "She «danced» her way across the stage.",
     "She «danced» gracefully all evening long."),
    ("joke", "He «joked».", "He «joked» his way out of trouble.",
     "He «joked» with his old friends."),
    ("smile", "She «smiled».", "She «smiled» her way into the job.",
     "She «smiled» warmly at the arriving guests."),
    ("bluff", "He «bluffed».", "He «bluffed» his way past the guard.",
     "He «bluffed» during the late card game."),
]
# verb, sense-A use, sense-B use  (a genuine lexical sense shift; calibrates the LOW end)
POLY = [
    ("run", "She «ran» a marathon.", "She «ran» a successful company."),
    ("draw", "He «drew» a quick picture.", "He «drew» his sword from its sheath."),
    ("charge", "The cavalry «charged» the hill.", "The shop «charged» a small fee."),
    ("break", "He «broke» the window.", "He «broke» for lunch at noon."),
    ("set", "She «set» the dinner table.", "The sun «set» behind the hills."),
    ("bank", "They sat on the river «bank».", "She deposited it at the «bank»."),  # homonymy floor
]


def rows():
    out = []
    for vset, kind in ((CM, "coerced-cm"), (WAY, "coerced-way")):
        for verb, bare, coerced, elab in vset:
            out.append(dict(item_id=f"{kind}-{verb}", verb=verb, arm=kind,
                            predicted="low", marked1=bare, marked2=coerced))
            out.append(dict(item_id=f"control-{verb}", verb=verb, arm="control-elab",
                            predicted="high", marked1=bare, marked2=elab))
    for verb, a, b in POLY:
        out.append(dict(item_id=f"poly-{verb}", verb=verb, arm="polysemy-anchor",
                        predicted="low", marked1=a, marked2=b))
    return out


def main():
    out = os.path.join(os.path.dirname(__file__), "items.csv")
    rs = rows()
    # sanity: the verb is marked in both sentences of every item
    for r in rs:
        assert "«" in r["marked1"] and "«" in r["marked2"], r["item_id"]
    cols = ["item_id", "verb", "arm", "predicted", "marked1", "marked2"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    from collections import Counter
    print(f"wrote {len(rs)} items -> {out}")
    print(f"  arms: {dict(Counter(r['arm'] for r in rs))}")
    print(f"  sha256[:16] = {h}  (freeze hash)")


if __name__ == "__main__":
    main()
