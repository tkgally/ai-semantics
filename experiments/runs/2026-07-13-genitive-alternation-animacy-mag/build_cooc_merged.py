#!/usr/bin/env python3
"""Merged frozen shadow-control COVARIATE for the POOLED magnitude analysis (s222).

Identical FROZEN recipe to build_cooc_gen.py (byte-frozen; PSEUDO_K=4.0, same UD-English-EWT corpus,
same s/of-genitive counting, same additive smoothing toward the corpus base rate) -- the ONLY change
is the lemma SET: the UNION of TYPICAL possessor lemmas across all THREE pooled disjoint arms (s218 +
rep2 + mag), so analyze_merged.py has a propensity for every pooled frame's animate/inanimate
possessor. The recipe is frozen; extending the lemma set does not touch it (each lemma's propensity
is computed independently from the same corpus counts + the same corpus-wide base rate).

Run (after fetching the corpus to /tmp/en_ewt_{train,dev,test}.conllu): python3 build_cooc_merged.py
"""
import hashlib
import json
import os
import statistics as st

# reuse the byte-frozen counting machinery + constants verbatim
from build_cooc_gen import CONLLU, PSEUDO_K, SOURCE_URL, count_genitives, file_sha

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.dirname(HERE)
STIMS = [
    os.path.join(RUNS, "2026-07-13-genitive-alternation-animacy", "stimuli.json"),
    os.path.join(RUNS, "2026-07-13-genitive-alternation-animacy-rep2", "stimuli.json"),
    os.path.join(HERE, "stimuli.json"),
]
# named freq_control.json (the name the byte-frozen probe.py freeze-gate checks); this IS the frozen
# covariate for the mag run -- the merged-lemma-set variant of the frozen build_cooc_gen recipe.
OUT = os.path.join(HERE, "freq_control.json")


def main():
    lemmas = set()
    for sp in STIMS:
        stim = json.load(open(sp))
        for fr in stim["frames"]:
            if fr["arm"] != "typical":
                continue
            for lv in ("animate", "collective", "inanimate"):
                lemmas.add(fr[lv].split()[-1].lower())

    s_count, of_count, tot_s, tot_of = count_genitives(CONLLU)
    p0 = tot_s / (tot_s + tot_of) if (tot_s + tot_of) else 0.0

    per_lemma = {}
    for lem in sorted(lemmas):
        s, o = s_count.get(lem, 0), of_count.get(lem, 0)
        n = s + o
        prop = (s + PSEUDO_K * p0) / (n + PSEUDO_K)
        per_lemma[lem] = {"s_count": s, "of_count": o, "n_genitive": n,
                          "marginal_s_propensity_smoothed": round(prop, 4)}

    out = {
        "recipe": ("UD-English-EWT possessor-lemma marginal s-genitive propensity = "
                   "(s_count + k*p0)/(s_count + of_count + k), k=%.1f, p0=corpus base rate; per "
                   "lowercased lemma. FROZEN recipe (byte-identical to build_cooc_gen.py); lemma set "
                   "= UNION of typical possessors across s218 + rep2 + mag." % PSEUDO_K),
        "source": SOURCE_URL,
        "license": "CC BY-SA 4.0 (UD English-EWT; LICENSE.txt verified firsthand s218; s168 in scope)",
        "arms_pooled": ["s218", "rep2", "mag"],
        "corpus_meta": {
            "files": {os.path.basename(p): {"sha256": file_sha(p)} for p in CONLLU},
            "total_s_genitive_possessors": tot_s,
            "total_of_genitive_possessors": tot_of,
            "corpus_base_rate_s": round(p0, 4),
            "pseudocount_k": PSEUDO_K,
        },
        "per_lemma": per_lemma,
    }
    payload = json.dumps(out, indent=2, ensure_ascii=False)
    open(OUT, "w").write(payload)
    sha = hashlib.sha256(payload.encode()).hexdigest()
    nz = sum(1 for r in per_lemma.values() if r["n_genitive"] > 0)
    print(f"corpus: s-gen={tot_s} of-gen={tot_of} base_rate_s={p0:.4f}")
    print(f"merged lemma set: {len(per_lemma)} typical possessor lemmas "
          f"({nz} with >=1 corpus genitive; the rest fall back to the base rate)")
    print(f"  mean smoothed propensity over all lemmas: "
          f"{st.mean(r['marginal_s_propensity_smoothed'] for r in per_lemma.values()):.4f}")
    print(f"freq_control_merged.json sha256: {sha}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
