"""Build + freeze the coercion-as-sense-modulation bridge stimuli (v2, 2026-05-31).

Operationalizes design/coercion-as-sense-modulation-v2 — the NON-COERCING TRANSITIVE CONTROL
that settles the v1 inherent confound (pre-run critic I1): v1's coerced arm always added
object+path structure the (intransitive) control lacked, so a positive gap could not separate
"the model registers a SENSE shift" from "the model rates ANY added argument structure as less
verb-related." v2 adds, per verb, a STRUCTURE-MATCHED conventional-transitive arm (V + NP + PP,
a lexically conventional sense) alongside the coerced way-construction arm (V + POSS way + PP).
Both add comparable argument structure; only the coerced arm coerces a new sense. The decisive
new contrast is coerced-way vs transitive-ctrl: if coerced < transitive (both with added
arguments), the drop is SENSE-specific, not a surface-structure artifact.

Scope: the WAY-construction (where the within-verb conventional-transitive control is clean;
sound/manner-of-action verbs have bare + conventional-transitive + way-coercion uses). The
caused-motion verbs of v1 (sneeze/cough...) are intransitive and have NO conventional transitive,
so their surface confound is not cleanly controllable within-verb — noted as a v2 scope limit.

Arms per verb (sentence 1 = bare reference, verb marked «»; sentence 2 = arm frame):
  coerced-way    : V + POSS way + path  (the way-construction coercion)        -> predicted LOWER
  transitive-ctrl: V + conventional direct object + PP (same sense, +structure) -> predicted HIGH
  elab-ctrl      : V + adverbial (intransitive, no object; replicates v1)       -> predicted HIGH
  polysemy-anchor: a genuine lexical sense shift (calibrates the LOW end)

Internal-contrast-only (anchor pending; own constructed sentences, no human gold). The instrument
is the DWUG-validated lexical-v1 relatedness rating. No pass bar; reading rule fixed pre-run.

Run: python3 build_items.py   (no API; writes + freezes items.csv)
"""
import csv
import hashlib
import os
from collections import Counter

# verb, bare ref, coerced-way (V+way+PP), transitive-ctrl (V+NP+PP, conventional), elab-ctrl (V+adv)
WAY = [
    ("whistle", "She «whistled».",
     "She «whistled» her way down the long hall.",
     "She «whistled» a tune to the baby.",
     "She «whistled» softly in the dark."),
    ("sing", "He «sang».",
     "He «sang» his way into the finals.",
     "He «sang» a ballad to the crowd.",
     "He «sang» loudly all evening long."),
    ("hum", "She «hummed».",
     "She «hummed» her way through the recital.",
     "She «hummed» a melody to the child.",
     "She «hummed» quietly at her desk."),
    ("dance", "He «danced».",
     "He «danced» his way across the stage.",
     "He «danced» a waltz with the bride.",
     "He «danced» happily through the night."),
    ("shout", "He «shouted».",
     "He «shouted» his way to the front.",
     "He «shouted» a warning to the crowd.",
     "He «shouted» angrily at the referee."),
    ("fight", "He «fought».",
     "He «fought» his way through the crowd.",
     "He «fought» a fierce battle with the rebels.",
     "He «fought» bravely until the end."),
    ("write", "He «wrote».",
     "He «wrote» his way into the canon.",
     "He «wrote» a letter to the editor.",
     "He «wrote» carefully every morning."),
    ("read", "She «read».",
     "She «read» her way through the syllabus.",
     "She «read» a poem to the class.",
     "She «read» silently for a full hour."),
]
# verb, sense-A use, sense-B use (a genuine lexical sense shift; calibrates the LOW end)
POLY = [
    ("run", "She «ran» a marathon.", "She «ran» a successful company."),
    ("draw", "He «drew» a quick picture.", "He «drew» his sword from its sheath."),
    ("charge", "The cavalry «charged» the hill.", "The shop «charged» a small fee."),
    ("set", "She «set» the dinner table.", "The sun «set» behind the hills."),
]


def rows():
    out = []
    for verb, bare, coerced, transitive, elab in WAY:
        out.append(dict(item_id=f"coerced-{verb}", verb=verb, arm="coerced-way",
                        predicted="low", marked1=bare, marked2=coerced))
        out.append(dict(item_id=f"trans-{verb}", verb=verb, arm="transitive-ctrl",
                        predicted="high", marked1=bare, marked2=transitive))
        out.append(dict(item_id=f"elab-{verb}", verb=verb, arm="elab-ctrl",
                        predicted="high", marked1=bare, marked2=elab))
    for verb, a, b in POLY:
        out.append(dict(item_id=f"poly-{verb}", verb=verb, arm="polysemy-anchor",
                        predicted="low", marked1=a, marked2=b))
    return out


def main():
    out = os.path.join(os.path.dirname(__file__), "items.csv")
    rs = rows()
    for r in rs:  # sanity: the verb is marked in both sentences
        assert "«" in r["marked1"] and "«" in r["marked2"], r["item_id"]
    cols = ["item_id", "verb", "arm", "predicted", "marked1", "marked2"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    print(f"wrote {len(rs)} items -> {out}")
    print(f"  arms: {dict(Counter(r['arm'] for r in rs))}")
    print(f"  sha256[:16] = {h}  (freeze hash)")


if __name__ == "__main__":
    main()
