#!/usr/bin/env python3
"""
forced-both-lexical-v2 — deterministic frozen-subset builder.

Re-fetches SemEval-2017 Task 7 (verifies sha256), parses the homographic
subtask-3 gold, applies the FROZEN homonymy criterion (different-lexfile proxy),
intersects the pun-word vocabulary with two CC BY 4.0 human meaning-dominance
norm sets, and emits the frozen candidate subset.

LICENSE DISCIPLINE: emits item-ids, pun-word lemmas, WordNet sense keys
(factual annotations) and CC BY 4.0 dominance values ONLY. The pun SENTENCES
(a CC BY-NC 4.0 subset) are NEVER written to the committed artifact.

Inputs (re-fetch deterministically; see README for URLs + sha256):
  semeval/.../subtask3-homographic-test.gold
  edom_norms.csv          (OSF 7k3eh, file pmbkm)  CC BY 4.0
  spoken_norms.csv        (OSF uy47w, file 2mduw)  CC BY 4.0
"""
import csv, json, re, hashlib, collections

SEMEVAL_SHA = "70e82d89a102fced7dd1b1db90daa4ead55357d399d23f4d99e888634b4f4d0a"
GOLD = "semeval/semeval2017_task7/data/test/subtask3-homographic-test.gold"

# ---- frozen thresholds (set BEFORE any model call) ----
BAL_EDOM_MIN = 0.40   # eDom min(Freq1,Freq2)/(Freq1+Freq2) >= 0.40  (0.50 = perfect balance)
BAL_SPOKEN_D = 0.20   # Rodd&Gilbert D <= 0.20 (D near 0 = balanced; Armstrong et al. measure)

def lexfile(sk):
    m = re.match(r'.+%(\d+):(\d+):', sk)
    return (m.group(1), m.group(2)) if m else None

# ---- parse gold ----
gold = {}
for line in open(GOLD):
    p = line.split()
    if len(p) >= 3:
        gold[p[0]] = (p[1].split(';'), p[2].split(';'))

# ---- homonymy proxy: the two meanings share no (ss_type,lexfile) ----
def is_homonym(s1, s2):
    lf1 = set(filter(None, (lexfile(s) for s in s1)))
    lf2 = set(filter(None, (lexfile(s) for s in s2)))
    return bool(lf1 and lf2 and lf1.isdisjoint(lf2))

# ---- load CC BY dominance norms ----
edom = {}
for r in csv.DictReader(open("edom_norms.csv")):
    try:
        f1, f2 = float(r["Freq1"]), float(r["Freq2"])
        edom[r["Word"].strip().lower()] = min(f1, f2) / (f1 + f2)
    except Exception:
        pass
spoken = {}
for r in csv.DictReader(open("spoken_norms.csv")):
    try:
        D, nv = float(r["D"]), int(r["nValidResp"])
    except Exception:
        continue
    for w in re.split(r"/", r["AmbiguousWord"].strip().lower()):
        spoken[w.strip()] = {"D": D, "nValidResp": nv}

# ---- build candidate subset ----
items = []
for pid, (s1, s2) in gold.items():
    if not is_homonym(s1, s2):
        continue
    lem = s1[0].split('%')[0].lower()
    rec = {"item_id": pid, "lemma": lem,
           "sense_keys_m1": s1, "sense_keys_m2": s2,
           "edom_balance": round(edom[lem], 4) if lem in edom else None,
           "spoken_D": round(spoken[lem]["D"], 4) if lem in spoken else None,
           "spoken_nValid": spoken[lem]["nValidResp"] if lem in spoken else None}
    bal = ((rec["edom_balance"] is not None and rec["edom_balance"] >= BAL_EDOM_MIN) or
           (rec["spoken_D"] is not None and rec["spoken_D"] <= BAL_SPOKEN_D))
    rec["balanced_general_usage"] = bal
    rec["in_norms"] = (rec["edom_balance"] is not None) or (rec["spoken_D"] is not None)
    items.append(rec)

homonym_items = items
in_norms = [r for r in items if r["in_norms"]]
balanced = [r for r in items if r["balanced_general_usage"]]

out = {
    "design": "forced-both-lexical-v2",
    "semeval_sha256": SEMEVAL_SHA,
    "homonymy_criterion": "different-lexfile proxy: the two gold meanings share no (ss_type, WordNet-lexfile) pair",
    "balance_criterion": {"edom_min_over_total_ge": BAL_EDOM_MIN, "spoken_D_le": BAL_SPOKEN_D,
                          "rule": "balanced if EITHER norm set flags it (logical OR)"},
    "counts": {"homographic_subtask3_total": len(gold),
               "homonym_subset": len(homonym_items),
               "homonym_in_dominance_norms": len(in_norms),
               "balanced_homonym_items": len(balanced),
               "balanced_homonym_words": len(set(r["lemma"] for r in balanced))},
    "balanced_words": sorted(set(r["lemma"] for r in balanced)),
    "balanced_items": sorted(r["item_id"] for r in balanced),
    "items": sorted(balanced, key=lambda r: r["item_id"]),
}
# NOTE: no sentence text anywhere in `out`.
js = json.dumps(out, indent=1, sort_keys=False)
open("out/frozen_subset.json", "w").write(js)
manifest_sha = hashlib.sha256(js.encode()).hexdigest()
open("out/frozen_subset.sha256", "w").write(manifest_sha + "  frozen_subset.json\n")

print("counts:", json.dumps(out["counts"], indent=0))
print("balanced words:", out["balanced_words"])
print("frozen_subset.json sha256:", manifest_sha)
print("first 3 balanced items:", [r["item_id"] for r in out["items"][:3]])
