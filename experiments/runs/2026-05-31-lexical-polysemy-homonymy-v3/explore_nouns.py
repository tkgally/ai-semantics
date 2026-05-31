"""Second exploration pass: list NOUN (lemma) WiC availability for the by-hand
etymology review. Homonymy is cleanest for nouns; the WordNet structural signal is a
supporting cue only (it over-calls homonymy for verbs, ~6:1, so it is NOT the classifier).
We print, for every noun lemma with >=1 T AND >=1 F item, the WiC counts + WordNet
structural signal (n_synsets, n_clusters, lexfiles), sorted by item count, so the
orchestrator can hand-pick the clean homonyms (etymology-verified) and a matched polyseme
sample. No model calls.
"""
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore import ensure_wic, load_wic, classify  # noqa: E402

extract = ensure_wic()
items = load_wic(extract)
avail = defaultdict(lambda: {"T": 0, "F": 0})
for it in items:
    if it["pos"] == "N":
        avail[it["target"]][it["gold"]] += 1

rows = []
for lemma, cnt in avail.items():
    if cnt["T"] >= 1 and cnt["F"] >= 1:
        c = classify(lemma, "N")
        rows.append((lemma, cnt["T"], cnt["F"], c["n_syn"], c["n_clusters"],
                     "|".join(c["lexfiles"])))

rows.sort(key=lambda r: -(r[1] + r[2]))
print(f"NOUN lemmas with >=1 T AND >=1 F item: {len(rows)}\n")
print(f"{'lemma':16s} {'T':>3s} {'F':>3s} {'syn':>3s} {'clu':>3s}  lexfiles")
for lemma, t, f, ns, nc, lf in rows:
    print(f"{lemma:16s} {t:3d} {f:3d} {ns:3d} {nc:3d}  {lf}")
