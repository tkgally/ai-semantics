#!/usr/bin/env python3
"""enumerate_pools.py — $0 feasibility enumeration for the s200 conjecture's fresh-inventory test.

(Filename avoids shadowing the stdlib `enum` module — do not rename back to enum.py.)

Question (NEXT.md s201 backlog pick 1): is a WITHIN-NOUN sub-inventory contrast that dissociates
the conjecture's C2 (tail-alignment) condition from POS genuinely CONSTRUCTIBLE, or is the honest
move a scout/feasibility note + a pivot to the A6 cross-linguistic route?

Conjecture: wiki/findings/conjectures/decoupling-relation-inventory-shape.md
Note (writes up this output): wiki/findings/notes/decoupling-fresh-inventory-scout-v1.md

WHAT THIS COUNTS (no model call, no corpus stream, no money):
  For each candidate FRESH noun sub-relation (the sub-types WordNet splits meronymy/holonymy into,
  plus instance-hypernymy/hyponymy and attribute), how many eligible cue lemmas are available that
  (a) are single-word alphabetic forms >= 3 chars, (b) are DISJOINT from the 707 s186 + 612 s193
  cues already probed, and (c) yield >= 1 single-word relatum. These are the coarse-relation
  extraction primitives (member/part/substance {holonyms,meronyms}) that the frozen s186/s193
  relata() UNIONS into the coarse "holonymy"/"meronymy" buckets — so splitting them is the natural
  within-noun fresh inventory.

CAVEAT — these are UPPER BOUNDS: no SubTLEX Lg10WF band ([2.0,4.5]) filter and no RELMIN=1.5
relatum-frequency filter (SUBTLEX is gitignored/absent here), and no C4 cue-strength measured. Item
counts are therefore NOT the binding constraint on constructibility; the note explains what is.
"""
import json
import os
from nltk.corpus import wordnet as wn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")


def load_cues(path):
    d = json.load(open(path))
    s = set()
    for _, its in d["items"].items():
        for it in its:
            s.add(it["cue"])
    return s


s186 = load_cues(os.path.join(ROOT, "experiments/runs/2026-07-06-antonymy-shadow-saturation/items.json"))
s193 = load_cues(os.path.join(ROOT, "experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/items.json"))
probed = s186 | s193

subrels = {
    "member_meronymy": lambda s: s.member_meronyms(),
    "part_meronymy": lambda s: s.part_meronyms(),
    "substance_meronymy": lambda s: s.substance_meronyms(),
    "member_holonymy": lambda s: s.member_holonyms(),
    "part_holonymy": lambda s: s.part_holonyms(),
    "substance_holonymy": lambda s: s.substance_holonyms(),
    "instance_hypernymy": lambda s: s.instance_hypernyms(),
    "instance_hyponymy": lambda s: s.instance_hyponyms(),
    "attribute": lambda s: s.attributes(),
}

pools = {r: set() for r in subrels}
for syn in wn.all_synsets("n"):
    for lem in syn.lemmas():
        nm = lem.name().replace("_", " ").lower()
        if " " in nm or not nm.isalpha() or len(nm) < 3 or nm in probed:
            continue
        for r, fn in subrels.items():
            got = set()
            for s in fn(syn):
                for l in s.lemmas():
                    x = l.name().replace("_", " ").lower()
                    if " " not in x and x.isalpha():
                        got.add(x)
            if got:
                pools[r].add(nm)

out = {
    "probed_excluded": {"s186": len(s186), "s193": len(s193), "total": len(probed)},
    "pool_upper_bound_no_freq_filter": {r: len(pools[r]) for r in subrels},
    "note": "UPPER BOUNDS — no Lg10WF band, no RELMIN, no C4 cue-strength. Item counts are not the "
            "binding constraint; see the note page for the structural design tension.",
}
print(json.dumps(out, indent=2))
with open(os.path.join(HERE, "enum.json"), "w") as f:
    json.dump(out, f, indent=2)
