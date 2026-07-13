#!/usr/bin/env python3
"""Frozen shadow-control COVARIATE (critic B2): per-possessor-lemma MARGINAL s-genitive propensity.

Ratified freeze condition: ONE exact sha'd covariate recipe (no "and/or") = the possessor lemma's
marginal P(takes-'s | possessor) = s-genitive count / (s-genitive + of-genitive count), derived from
UD English-EWT (CC BY-SA 4.0; license verified firsthand s218 -- LICENSE.txt "Attribution-ShareAlike
4.0 International"; in scope under the s168 UD-treebank rule). This is the channel a NO-ANIMACY
surface reader would exploit: animate nouns take the possessive 's more often than inanimate nouns
REGARDLESS of possessum, so the possessor's marginal genitive propensity is collinear with animacy.
analyze.py partials THIS out of the animacy shift (the corroboration leg of B3); the PRIMARY
shortcut control remains the nonce arm (a nonce possessor has no per-lemma statistic).

HONEST POWER NOTE (critic "power bounded by corpus size"; R2/R5). UD-EWT is small (~250k tokens);
per-lemma genitive counts are sparse, so this covariate is a CORROBORATION arm, not a definitive
firewall. build_items self-audit + analyze.py report the covariate's OWN predictive validity (does
propensity_diff predict the model's per-frame shift at all?). If it is too weak to absorb collinear
variance, CONFIRM rests on the nonce arm and the covariate leg is weak corroboration -- stated
plainly (the ratification's R2 + the non-Anthropic vote's "corroboratory, not definitive").

GENITIVE ANNOTATION (UD). possessor = a NOUN/PROPN dependent:
  s-genitive : deprel nmod:poss with a possessive-clitic 'case' child ('s / ' / s / ’s)
  of-genitive: deprel nmod    with a 'case' child whose lemma is 'of'
Counts are per LOWERCASED LEMMA. The base rate p0 = total-s / (total-s + total-of) over all such
possessors; per-lemma propensity is additively smoothed toward p0 with pseudocount k so a sparse
lemma is not an all-or-nothing 0/1 (recipe frozen here, before any model call).

Run: python3 build_cooc_gen.py   (reads /tmp/en_ewt_{train,dev,test}.conllu; no network, no API)
"""
import collections
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = os.path.join(HERE, "stimuli.json")
CONLLU = [f"/tmp/en_ewt_{s}.conllu" for s in ("train", "dev", "test")]
SOURCE_URL = ("https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/"
              "en_ewt-ud-{train,dev,test}.conllu")
OUT = os.path.join(HERE, "freq_control.json")
PSEUDO_K = 4.0   # additive-smoothing pseudocount toward the corpus base rate (frozen)

POSS_CLITICS = {"'s", "’s", "s", "'", "’"}


def sentences(paths):
    for p in paths:
        toks = []
        for line in open(p, encoding="utf-8"):
            line = line.rstrip("\n")
            if not line:
                if toks:
                    yield toks
                toks = []
                continue
            if line.startswith("#"):
                continue
            c = line.split("\t")
            if len(c) < 8 or "-" in c[0] or "." in c[0]:
                continue
            toks.append(c)  # 0id 1form 2lemma 3upos 4xpos 5feats 6head 7deprel
        if toks:
            yield toks


def count_genitives(paths):
    s_count = collections.Counter()
    of_count = collections.Counter()
    tot_s = tot_of = 0
    for toks in sentences(paths):
        children = collections.defaultdict(list)
        for t in toks:
            children[t[6]].append(t)
        for t in toks:
            tid, form, lemma, upos, dep = t[0], t[1], t[2], t[3], t[7]
            if upos not in ("NOUN", "PROPN"):
                continue
            deprel = dep.split(":")[0]
            casekids = [k for k in children[tid] if k[7].split(":")[0] == "case"]
            caseforms = {k[1].lower() for k in casekids}
            caselemmas = {k[2].lower() for k in casekids}
            if dep == "nmod:poss" and (caseforms & POSS_CLITICS):
                s_count[lemma.lower()] += 1
                tot_s += 1
            elif deprel == "nmod" and "of" in caselemmas:
                of_count[lemma.lower()] += 1
                tot_of += 1
    return s_count, of_count, tot_s, tot_of


def file_sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    stim = json.load(open(STIM))
    # collect the TYPICAL arm's possessor nouns (lemmas) -- the covariate is defined only for real
    # possessors; nonce possessors have no corpus statistic by design.
    lemmas = set()
    for fr in stim["frames"]:
        if fr["arm"] != "typical":
            continue
        for lv in ("animate", "collective", "inanimate"):
            noun = fr[lv].split()[-1].lower()   # 'the patient' -> 'patient'
            lemmas.add(noun)

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
                   "(s_count + k*p0)/(s_count + of_count + k), k=%.1f, p0=corpus base rate; "
                   "s-genitive = nmod:poss with possessive-clitic case child; of-genitive = nmod "
                   "with 'of' case child; per lowercased lemma. FROZEN before any model call." % PSEUDO_K),
        "source": SOURCE_URL,
        "license": "CC BY-SA 4.0 (UD English-EWT; LICENSE.txt verified firsthand s218; s168 in scope)",
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

    # console summary: mean smoothed propensity by animacy level (the collinearity the covariate is
    # meant to capture -- animate should sit ABOVE inanimate if the covariate has any grip)
    def level_props(level):
        vals = []
        for fr in stim["frames"]:
            if fr["arm"] != "typical":
                continue
            noun = fr[level].split()[-1].lower()
            vals.append(per_lemma[noun]["marginal_s_propensity_smoothed"])
        return vals
    import statistics as st
    print(f"corpus: s-gen={tot_s} of-gen={tot_of} base_rate_s={p0:.4f}")
    for lv in ("animate", "collective", "inanimate"):
        v = level_props(lv)
        nz = sum(1 for fr in stim["frames"] if fr["arm"] == "typical"
                 and per_lemma[fr[lv].split()[-1].lower()]["n_genitive"] > 0)
        print(f"  {lv:11s}: mean smoothed prop={st.mean(v):.4f}  "
              f"(lemmas with >=1 corpus genitive: {nz}/36)")
    print(f"freq_control.json sha256: {sha}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
