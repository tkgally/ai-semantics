#!/usr/bin/env python3
"""control_hypernymy_gold.py — gold-construction control for the s202 scout's key interpretive claim.

The scout finds instance_hypernymy (direct-gold) is cue-strength-RICH (frame-G²/C4 0.0306), whereas the
COARSE hypernymy the s193 run measured was cue-strength-POOR (0.008, at the floor — the C1 head
disaligner). But the two used DIFFERENT gold: coarse hypernymy = a DEPTH-4 hypernym CLOSURE (abstract
superordinates); instance_hypernymy = the DIRECT single-step "kind". A reviewer could object the gap is a
gold-construction artifact, not a relational fact. This control settles it: recompute the SAME s193
coarse-hypernymy cues' frame cue-strength under BOTH golds on the SAME C4 shard set + frozen G² machinery:
  (a) depth-4 closure gold  -> should REPRODUCE the s193 ~0.008 (a sanity check of this pipeline)
  (b) direct depth-1 gold   -> the construction comparable to instance_hypernymy
If (b) >> (a), the coarse head disaligner's low cue-strength is (partly) a property of the ABSTRACT
CLOSURE gold, and the DIRECT IS-A "kind" term is cue-strength-rich whether coarse or instance — a
mechanistic wrinkle bearing on how robust the conjecture's C1 vehicle is. $0; no model call.
"""
import importlib.util
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
S193_BUILD = os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy", "build_cooc_c4.py")
S193_ITEMS = os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy", "items.json")
RELMIN = 1.5

_spec = importlib.util.spec_from_file_location("s193_build_cooc_c4", os.path.abspath(S193_BUILD))
_s193 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_s193)
K, FRAME_WIN, CONNECTIVES = _s193.K, _s193.FRAME_WIN, _s193.CONNECTIVES
signed_g2, compute_control, stream_sentences = _s193.signed_g2, _s193.compute_control, _s193.stream_sentences


def soundness(produced, gold):
    if not produced:
        return None
    return sum(1 for w in produced if w in gold) / len(produced)


def load_freq():
    import csv
    SUB = os.path.join(HERE, "..", "..", "data", "subtlex-us", "SUBTLEXus74286wordstextversion.txt")
    freq = {}
    with open(SUB, encoding="latin-1") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            try:
                freq[row["Word"].lower()] = float(row["Lg10WF"])
            except (ValueError, KeyError):
                pass
    return freq


def direct_hypernym_gold(cue, freq):
    """DIRECT (depth-1) hypernym gold — the 'kind' term, comparable to instance_hypernymy's construction."""
    from nltk.corpus import wordnet as wn
    out = set()
    for syn in wn.synsets(cue, pos="n"):
        for h in syn.hypernyms():
            for l in h.lemmas():
                x = l.name().replace("_", " ").lower()
                if " " not in x and x.isalpha() and freq.get(x, 0.0) >= RELMIN:
                    out.add(x)
    return out


def main():
    items = json.load(open(S193_ITEMS))
    vocab = set(json.load(open(os.path.join(HERE, "vocab.json")))["vocab"])
    freq = load_freq()
    hyp = items["items"]["hypernymy"]
    cues = [it["cue"] for it in hyp]
    closure_gold = {it["cue"]: set(it["gold"]) for it in hyp}          # depth-4 closure (s193)
    direct_gold = {c: direct_hypernym_gold(c, freq) for c in cues}     # depth-1 direct
    cueset = set(cues)
    target = vocab | cueset

    df = {}
    co_sent = {c: {} for c in cueset}
    co_frame = {c: {} for c in cueset}
    Nsent = Ntok = 0
    t0 = time.time()
    for toks in stream_sentences():
        Nsent += 1
        Ntok += len(toks)
        present = {}
        for i, t in enumerate(toks):
            if t in target:
                present.setdefault(t, []).append(i)
        if not present:
            continue
        for w in present:
            df[w] = df.get(w, 0) + 1
        cue_here = [c for c in present if c in cueset]
        if not cue_here:
            continue
        vset = list(present.keys())
        for c in cue_here:
            cs, cf, cpos = co_sent[c], co_frame[c], present[c]
            for v in vset:
                if v == c:
                    continue
                cs[v] = cs.get(v, 0) + 1
                framed = False
                for pi in cpos:
                    for pj in present[v]:
                        d = abs(pi - pj)
                        if d == 0 or d > FRAME_WIN:
                            continue
                        lo, hi = (pi, pj) if pi < pj else (pj, pi)
                        between = toks[lo + 1:hi]
                        if d == 1 or any(b in CONNECTIVES for b in between):
                            framed = True
                            break
                    if framed:
                        break
                if framed:
                    cf[v] = cf.get(v, 0) + 1
        if Nsent % 5_000_000 == 0:
            print(f"  {Nsent} sentences, {time.time()-t0:.0f}s", flush=True)

    counts = {"Nsent": Nsent, "Ntok": Ntok, "K": K, "frame_win": FRAME_WIN,
              "df": df, "co_sent": co_sent, "co_frame": co_frame}
    ctrl = compute_control(counts, cueset, vocab)["cues"]

    def rel_cue_strength(goldmap):
        vals = []
        for c in cues:
            cand = [v for v, g, o in ctrl.get(c, {}).get("frame", [])]
            s = soundness(cand, goldmap[c])
            if s is not None:
                vals.append(s)
        return round(sum(vals) / len(vals), 4) if vals else None

    gsz_closure = round(sum(len(closure_gold[c]) for c in cues) / len(cues), 2)
    gsz_direct = round(sum(len(direct_gold[c]) for c in cues) / len(cues), 2)
    out = {
        "Nsent": Nsent, "n_cues": len(cues),
        "coarse_hypernymy_frame_cue_strength_closure_gold": rel_cue_strength(closure_gold),
        "coarse_hypernymy_frame_cue_strength_direct_gold": rel_cue_strength(direct_gold),
        "gold_size_mean_closure": gsz_closure, "gold_size_mean_direct": gsz_direct,
        "s193_reported_closure": 0.0083,
        "instance_hypernymy_frame_direct_gold_s202": 0.0306,
    }
    with open(os.path.join(HERE, "results_hypernymy_gold.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
