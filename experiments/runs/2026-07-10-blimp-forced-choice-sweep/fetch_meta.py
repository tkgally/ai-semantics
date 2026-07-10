"""Fetch the FIRST line of each BLiMP paradigm file to record its own structural metadata
(UID, linguistics_term, field) -- the human-agreement-BLIND basis for F6 stratum assignment.
Paradigm names come from the committed human_validation_summary.csv Condition column."""
import csv, json, urllib.request, urllib.error, os
BASE = "https://raw.githubusercontent.com/alexwarstadt/blimp/master/data/{}.jsonl"
here = os.path.dirname(__file__)
csvp = os.path.join(here, "..", "..", "data", "blimp", "human_validation_summary.csv")
conds = []
with open(csvp) as f:
    for row in csv.DictReader(f):
        conds.append(row["Condition"])
meta = {}
missing = []
for c in conds:
    try:
        req = urllib.request.Request(BASE.format(c), headers={"Range": "bytes=0-2000"})
        with urllib.request.urlopen(req, timeout=30) as r:
            chunk = r.read().decode("utf-8", "replace")
        first = chunk.splitlines()[0]
        obj = json.loads(first)
        meta[c] = {"UID": obj.get("UID"), "linguistics_term": obj.get("linguistics_term"),
                   "field": obj.get("field")}
    except urllib.error.HTTPError as e:
        missing.append((c, e.code)); meta[c] = None
    except Exception as e:
        missing.append((c, str(e)[:60])); meta[c] = None
json.dump(meta, open(os.path.join(here, "paradigm_meta.json"), "w"), indent=1)
print("fetched", sum(1 for v in meta.values() if v), "of", len(conds))
print("missing/404:", missing)
# summarize by linguistics_term
from collections import defaultdict
bycat = defaultdict(list)
for c, v in meta.items():
    if v: bycat[v["linguistics_term"]].append(c)
for cat in sorted(bycat):
    print(f"\n[{cat}] ({len(bycat[cat])})")
    for c in sorted(bycat[cat]): print("   ", c)
