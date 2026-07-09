#!/usr/bin/env python3
"""Verb-relation feasibility measurement for the s198 verb-relation decoupling DESIGN.
Measures, per candidate WordNet VERB relation, how many frequency-band-eligible cue verbs
supply >=1 single-word in-band relatum — before and after excluding all prior cue lemmas
(s186 nouns, s193 fresh nouns, s196 adjectives) as a homograph guard. Also reports the
troponymy-depth (min_depth over the cue's first verb synset) distribution — the H2 analog.
Nothing here is frozen; this is design-time feasibility only."""
import csv, json, os
from nltk.corpus import wordnet as wn

HERE = "/home/user/ai-semantics"
SUB = os.path.join(HERE, "experiments/data/subtlex-us/SUBTLEXus74286wordstextversion.txt")
FMIN, FMAX = 2.0, 4.5     # byte-identical to s186/s193 cue band
RELMIN = 1.5              # min relatum freq
VOCAB_MINLEN = 3

def load_freq():
    freq = {}
    with open(SUB, encoding="latin-1") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            try: freq[row["Word"].lower()] = float(row["Lg10WF"])
            except (ValueError, KeyError): pass
    return freq

freq = load_freq()

# ---- gather prior cue lemmas to exclude (homograph guard) ----
prior = set()
for path, sub in [
    ("experiments/runs/2026-07-06-antonymy-shadow-saturation/items.json", None),
    ("experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/items.json", None),
    ("experiments/runs/2026-07-09-adjective-antonymy-replication/items.json", None),
]:
    d = json.load(open(os.path.join(HERE, path)))
    for r, its in d["items"].items():
        for it in its:
            prior.add(it["cue"])
print(f"prior cue lemmas to exclude (homograph guard): {len(prior)}")

def relata(lem, syn, rel):
    out = set()
    if rel == "antonymy":
        for a in lem.antonyms(): out.add(a.name().replace("_"," ").lower())
    elif rel == "synonymy":
        for l in syn.lemmas():
            if l.name()!=lem.name(): out.add(l.name().replace("_"," ").lower())
    elif rel == "hypernymy":         # the more-general verb (troponymy inverse): whisper->talk
        for s in syn.closure(lambda x:x.hypernyms(), depth=4):
            for l in s.lemmas(): out.add(l.name().replace("_"," ").lower())
    elif rel == "troponymy":         # more specific manner (hyponyms): talk->whisper
        for s in syn.closure(lambda x:x.hyponyms(), depth=4):
            for l in s.lemmas(): out.add(l.name().replace("_"," ").lower())
    elif rel == "entailment":
        for s in syn.entailments():
            for l in s.lemmas(): out.add(l.name().replace("_"," ").lower())
    elif rel == "cause":
        for s in syn.causes():
            for l in s.lemmas(): out.add(l.name().replace("_"," ").lower())
    elif rel == "alsosee":
        for s in syn.also_sees():
            for l in s.lemmas(): out.add(l.name().replace("_"," ").lower())
    elif rel == "verbgroup":
        for s in syn.verb_groups():
            for l in s.lemmas():
                if l.name()!=lem.name(): out.add(l.name().replace("_"," ").lower())
    return {x for x in out if " " not in x and freq.get(x,0.0) >= RELMIN}

RELS = ["antonymy","synonymy","hypernymy","troponymy","entailment","cause","alsosee","verbgroup"]

# eligible cue pools
cue_gold = {r:{} for r in RELS}
cue_gold_fresh = {r:{} for r in RELS}
for syn in wn.all_synsets("v"):
    for lem in syn.lemmas():
        nm = lem.name().replace("_"," ").lower()
        if " " in nm: continue
        fw = freq.get(nm)
        if fw is None or not (FMIN <= fw <= FMAX): continue
        for r in RELS:
            g = relata(lem, syn, r)
            if g:
                cue_gold[r].setdefault(nm,set()).update(g)
                if nm not in prior:
                    cue_gold_fresh[r].setdefault(nm,set()).update(g)

print("\nRelation      | in-band cues | fresh(excl prior) | median gold size")
for r in RELS:
    n = len(cue_gold[r]); nf = len(cue_gold_fresh[r])
    golds = sorted(len(g) for g in cue_gold_fresh[r].values())
    med = golds[len(golds)//2] if golds else 0
    print(f"  {r:11s} | {n:5d}        | {nf:5d}             | {med}")

# troponymy-depth (min_depth of first verb synset) distribution over the FRESH troponymy+hypernymy pools
def depth(cue):
    ss = wn.synsets(cue, pos="v")
    return ss[0].min_depth() if ss else None
for r in ["troponymy","hypernymy","entailment"]:
    ds = [depth(c) for c in cue_gold_fresh[r]]
    ds = [d for d in ds if d is not None]
    if ds:
        import statistics
        print(f"\n{r} fresh pool: min_depth n={len(ds)} range {min(ds)}-{max(ds)} "
              f"mean {statistics.mean(ds):.2f} distinct {len(set(ds))}")
