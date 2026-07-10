#!/usr/bin/env python3
"""build_cooc_c4.py — contrastive-frame C4 cue-strength control for the FRESH-SUB-RELATION scout (s202).

REUSES the FROZEN G² machinery from the s193 build_cooc_c4.py by IMPORT (signed_g2, compute_control,
stream_sentences, K, FRAME_WIN, CONNECTIVES, C4_BASE, NUM_SHARDS) and asserts the frozen constants are
identical. The co-occurrence + contrastive-frame counting loop is copied VERBATIM from that module's
main() (only the Hearst second arm is DROPPED — this scout measures the frame cue-strength predictor
only; there is no H2 taxonomic arm here). So the cue-strength numbers are computed on exactly the
byte-frozen apparatus (K=3, FRAME_WIN=4, the s193 CONNECTIVES) and the SAME C4 shard set the s193/s199
noun/verb decoupling numbers were measured on — making the fresh sub-types' cue-strengths comparable to
the coarse s193 reference (hypernymy 0.008 / synonymy 0.006 / meronymy 0.019 / holonymy 0.031 /
hyponymy 0.036 / antonymy 0.149).

CORPUS (recipe-not-corpus; streamed + discarded, nothing committed): allenai/c4 en shards
c4-train.00000/00001/00002-of-01024.json.gz (ODC-BY; the s193-frozen shard set — deterministic
22,329,495 sentences / 388,243,981 tokens). resource/cooccurrence-corpus-scouting.md (s185 license scout).

Emits counts.json (raw Nsent/Ntok/df/co_sent/co_frame) and control.json (signed-G² top-k per cue,
frame + sent variants). Anti-cheat: no model output is read; the control is computed independently.
$0 — no model call.
"""
import importlib.util
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
S193_BUILD = os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy", "build_cooc_c4.py")

# ---- import the FROZEN s193 build module and reuse its machinery ----
_spec = importlib.util.spec_from_file_location("s193_build_cooc_c4", os.path.abspath(S193_BUILD))
_s193 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_s193)

K = _s193.K
FRAME_WIN = _s193.FRAME_WIN
CONNECTIVES = _s193.CONNECTIVES
signed_g2 = _s193.signed_g2
compute_control = _s193.compute_control
stream_sentences = _s193.stream_sentences

# freeze-check: the constants this scout relies on are exactly s193's (which s193 in turn asserts == s186)
assert (K, FRAME_WIN) == (3, 4), "frozen K/FRAME_WIN drift vs s193"
assert CONNECTIVES == {
    "and", "or", "nor", "but", "versus", "vs", "than", "to", "from", "either",
    "neither", "both", "between", "whether", "against", "unlike", "whereas",
    "while", "not", "opposed", "contrast",
}, "frozen CONNECTIVES drift vs s193"
# and verify s193's own G² identity chain (s193 -> s186) still holds
_s193._assert_frozen_g2()


def main():
    items = json.load(open(os.path.join(HERE, "items.json")))
    vocab = set(json.load(open(os.path.join(HERE, "vocab.json")))["vocab"])
    cues = set()
    for r, lst in items["items"].items():
        for it in lst:
            cues.add(it["cue"])
    target = vocab | cues
    conn = CONNECTIVES

    df = {}
    co_sent = {c: {} for c in cues}
    co_frame = {c: {} for c in cues}
    Nsent = 0
    Ntok = 0
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
        cue_here = [c for c in present if c in cues]
        if not cue_here:
            continue
        vset = list(present.keys())
        for c in cue_here:
            cs = co_sent[c]
            cf = co_frame[c]
            cpos = present[c]
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
                        if d == 1 or any(b in conn for b in between):
                            framed = True
                            break
                    if framed:
                        break
                if framed:
                    cf[v] = cf.get(v, 0) + 1
        if Nsent % 2_000_000 == 0:
            print(f"  {Nsent} sentences, {Ntok} tokens, {time.time()-t0:.0f}s", flush=True)

    print(f"stream done: {Nsent} sentences, {Ntok} tokens, {time.time()-t0:.0f}s", flush=True)
    counts = {"Nsent": Nsent, "Ntok": Ntok, "K": K, "frame_win": FRAME_WIN,
              "df": df, "co_sent": co_sent, "co_frame": co_frame}
    with open(os.path.join(HERE, "counts.json"), "w") as f:
        json.dump(counts, f)
    control = compute_control(counts, cues, vocab)
    with open(os.path.join(HERE, "control.json"), "w") as f:
        json.dump(control, f, indent=1)
    print(f"control.json written ({len(control['cues'])} cues). Nsent={Nsent} Ntok={Ntok}")


if __name__ == "__main__":
    main()
