#!/usr/bin/env python3
"""Frozen shadow-control COVARIATE (corroboration only): per-(verb+particle) MARGINAL SPLIT-ORDER rate.

Ratified freeze condition (Q2, R7): ONE exact sha'd covariate recipe = for each verb+particle pair in
the stimuli, the corpus rate at which that phrasal verb appears in SPLIT order (object between verb and
particle) vs JOINED order (particle adjacent to verb), from UD English-EWT (CC BY-SA 4.0; license
verified firsthand s218 -- LICENSE.txt "Attribution-ShareAlike 4.0 International"; in scope under the
s168 UD-treebank rule). analyze.py reports the DEFINITENESS shift's residual over this covariate.

HONEST POWER NOTE (R1/R7; the design's "expected near-vacuous"). UD-EWT is small (~250k tokens) and
transitive verb-particle tokens with a full-NP object are SPARSE, so per-verb-particle split/joined
counts are tiny. This covariate is a CORROBORATION arm, NOT the load-bearing control -- the byte-
identical firewall (Arm 2) carries the CONFIRM (it needs NO corpus). analyze.py reports the covariate's
OWN predictive validity (slope + R^2); if it barely varies / does not predict the per-frame shift,
partialling it out is near-vacuous and CONFIRM rests on Arm 2 -- stated plainly.

UD PARTICLE-VERB ANNOTATION. A phrasal-verb particle is a token with deprel compound:prt whose head is
the (verb) token. The verb's direct object is a token with deprel obj (or dobj) headed by the same verb.
Order per token instance:
  JOINED : the particle's linear position is immediately after the verb, OR before the object head
  SPLIT  : the object head sits linearly BETWEEN the verb and the particle
Counts are keyed by (verb_lemma, particle_form_lowercased). p0 = corpus base split rate over all such
particle-verb tokens that have an obj; per-pair rate is additively smoothed toward p0 with pseudocount k.

Run: python3 build_cooc_particle.py   (reads /tmp/en_ewt_{train,dev,test}.conllu; no network, no API)
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
PSEUDO_K = 4.0   # additive-smoothing pseudocount toward the corpus base split rate (frozen)


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


def count_particle_orders(paths):
    """Return split_count, joined_count keyed by (verb_lemma, particle_form); plus totals."""
    split_c = collections.Counter()
    joined_c = collections.Counter()
    tot_s = tot_j = 0
    for toks in sentences(paths):
        by_id = {t[0]: t for t in toks}
        children = collections.defaultdict(list)
        for t in toks:
            children[t[6]].append(t)
        for v in toks:
            vid, vlemma, vupos = v[0], v[2].lower(), v[3]
            if vupos not in ("VERB", "AUX"):
                continue
            prts = [k for k in children[vid] if k[7].split(":")[0] == "compound"
                    and k[7].endswith("prt")]
            objs = [k for k in children[vid] if k[7].split(":")[0] in ("obj", "dobj")]
            if not prts or not objs:
                continue
            try:
                vpos = int(vid)
            except ValueError:
                continue
            for prt in prts:
                try:
                    ppos = int(prt[0])
                except ValueError:
                    continue
                pform = prt[1].lower()
                # is there an object head linearly BETWEEN the verb and the particle?
                lo, hi = (vpos, ppos) if vpos < ppos else (ppos, vpos)
                split = False
                for ob in objs:
                    try:
                        opos = int(ob[0])
                    except ValueError:
                        continue
                    if lo < opos < hi:
                        split = True
                        break
                key = (vlemma, pform)
                if split:
                    split_c[key] += 1; tot_s += 1
                else:
                    joined_c[key] += 1; tot_j += 1
    return split_c, joined_c, tot_s, tot_j


def file_sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    stim = json.load(open(STIM))
    # collect the (verb_lemma, particle) pairs the stimuli score. Verb lemma approximated by the
    # past-tense surface -> we key the covariate on the LEMMA to match UD; map the frame's surface verb
    # to its lemma here (frozen mapping, small closed set).
    VERB_LEMMA = {
        "picked": "pick", "put": "put", "took": "take", "threw": "throw", "pulled": "pull",
        "wiped": "wipe", "hung": "hang", "locked": "lock", "folded": "fold", "rolled": "roll",
        "packed": "pack", "wrapped": "wrap", "carried": "carry", "set": "set", "lifted": "lift",
        "handed": "hand", "cleared": "clear", "shut": "shut", "brought": "bring", "turned": "turn",
        "cut": "cut", "hauled": "haul",
    }
    pairs = {}
    for fr in stim["frames"]:
        lemma = VERB_LEMMA[fr["verb"]]
        pairs[(lemma, fr["prt"].lower())] = fr["id"]

    split_c, joined_c, tot_s, tot_j = count_particle_orders(CONLLU)
    p0 = tot_s / (tot_s + tot_j) if (tot_s + tot_j) else 0.0

    per_pair = {}
    for (lemma, prt), _fid in sorted(pairs.items()):
        s, j = split_c.get((lemma, prt), 0), joined_c.get((lemma, prt), 0)
        n = s + j
        rate = (s + PSEUDO_K * p0) / (n + PSEUDO_K)
        per_pair[f"{lemma}+{prt}"] = {"split_count": s, "joined_count": j, "n_tokens": n,
                                      "marginal_split_rate_smoothed": round(rate, 4)}

    out = {
        "recipe": ("UD-English-EWT per-(verb_lemma+particle) marginal SPLIT-order rate = "
                   "(split + k*p0)/(split + joined + k), k=%.1f, p0=corpus base split rate; SPLIT = "
                   "object head linearly between the verb and its compound:prt particle, JOINED "
                   "otherwise; per (verb_lemma, particle_form). FROZEN before any model call." % PSEUDO_K),
        "source": SOURCE_URL,
        "license": "CC BY-SA 4.0 (UD English-EWT; LICENSE.txt verified firsthand s218; s168 in scope)",
        "corpus_meta": {
            "files": {os.path.basename(p): {"sha256": file_sha(p)} for p in CONLLU},
            "total_split_tokens": tot_s,
            "total_joined_tokens": tot_j,
            "corpus_base_split_rate": round(p0, 4),
            "pseudocount_k": PSEUDO_K,
        },
        "per_pair": per_pair,
    }
    payload = json.dumps(out, indent=2, ensure_ascii=False)
    open(OUT, "w").write(payload)
    sha = hashlib.sha256(payload.encode()).hexdigest()

    n_pairs = len(per_pair)
    n_any = sum(1 for v in per_pair.values() if v["n_tokens"] > 0)
    print(f"corpus: split={tot_s} joined={tot_j} base_split_rate={p0:.4f}")
    print(f"stimulus (verb+particle) pairs: {n_pairs} distinct; with >=1 corpus token: {n_any}/{n_pairs}")
    for k, v in sorted(per_pair.items()):
        print(f"  {k:16s}: split={v['split_count']} joined={v['joined_count']} "
              f"n={v['n_tokens']} rate={v['marginal_split_rate_smoothed']}")
    print(f"freq_control.json sha256: {sha}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
