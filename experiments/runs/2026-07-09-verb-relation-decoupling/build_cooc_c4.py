#!/usr/bin/env python3
"""build_cooc_c4.py — FROZEN distributional control build on C4 (Q3 internal-contrast; verb probe).

The contrastive-frame G² computation is BYTE-IDENTICAL to the s193 build_cooc_c4.py (signed_g2,
compute_control, K, FRAME_WIN, CONNECTIVES) — VERIFIED by an assertion at import against the s193
source, which itself is byte-verified against the s186 build_cooc.py. ONLY two things change, both by
design (freeze-condition 6 / decision Q1/Q2): the CUE set is now VERBS, and the candidate pool V is now
single-word SubTLEX VERBS. The sentence-streaming IO adapter (gzipped C4) is unchanged from s193.

DROPPED vs s193: the corpus Hearst-frame ("X such as Y") SECOND arm. Q2-C (ratified s199) REJECTS a
corpus troponymy-frame arm up front — verb troponymy has no clean lexico-syntactic frame, and the s193
nominal Hearst arm LOST even where well-motivated. The single H2 vehicle is the STRUCTURAL
troponymy-depth proxy frozen in prep.py (Q2-A). So this build computes ONLY the contrastive-frame G²
control (the H1 cue-strength predictor); no hearst.json is written.

CORPUS (recipe-not-corpus; nothing committed — streamed and discarded, bounded disk):
    allenai/c4, en config, shards c4-train.00000/00001/00002-of-01024.json.gz via the HuggingFace
    resolve URL. License: ODC-BY (+ Common-Crawl terms — carried to the result provenance).
    resource/cooccurrence-corpus-scouting.md (s185 license scout, verified firsthand). The s193-frozen
    shard set (00000-00002; deterministic 22,329,495 sentences / 388,243,981 tokens). A PROXY for the
    panel's (unknown) pretraining distribution.

TWO CONTROLS (both frozen; frame-G² PRIMARY, sent-G² SENSITIVITY) — identical roles to s186/s193.

Emits counts.json (raw Nsent/Ntok/df/co_sent/co_frame — for the verifier to recompute) and control.json
(signed-G² ranked top-k per cue, both variants). Anti-cheat: no model output is read here; the control
is computed independently of the panel.
"""
import gzip
import io
import json
import math
import os
import re
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
S193 = os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy", "build_cooc_c4.py")

# ---- FROZEN G² PARAMS — must byte-match s193/s186 (asserted below) ----
K = 3                      # control produces top-k candidates
FRAME_WIN = 4              # max token distance for a contrastive frame
CONNECTIVES = {
    "and", "or", "nor", "but", "versus", "vs", "than", "to", "from", "either",
    "neither", "both", "between", "whether", "against", "unlike", "whereas",
    "while", "not", "opposed", "contrast",
}

# ---- FROZEN C4 corpus spec (pin shards; assert volume >= s186's) ----
C4_BASE = "https://huggingface.co/datasets/allenai/c4/resolve/main/en/c4-train.{:05d}-of-01024.json.gz"
NUM_SHARDS = 3             # 00000..00002 — the s193-frozen shard set
S186_NSENT = 21_300_000    # s186 Simple-English-Wikipedia volume (result page)
S186_NTOK_APPROX = 320_000_000

_nonword = re.compile(r"[^a-z\s]+")
_sent = re.compile(r"[.!?]+\s")


def stream_sentences():
    """C4 IO ADAPTER (byte-identical to s193; touches no counting/weighting logic)."""
    for si in range(NUM_SHARDS):
        url = C4_BASE.format(si)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=180) as resp:
            gz = gzip.GzipFile(fileobj=resp)
            buf = io.TextIOWrapper(gz, encoding="utf-8", errors="ignore")
            for line in buf:
                if not line.strip():
                    continue
                try:
                    txt = json.loads(line)["text"].lower()
                except Exception:
                    continue
                for sent in _sent.split(txt):
                    toks = _nonword.sub(" ", sent).split()
                    if toks:
                        yield toks
        print(f"  [shard {si} done]", flush=True)


def signed_g2(o11, dfc, dfv, N):
    """Dunning (1993) log-likelihood, signed by attraction/repulsion. BYTE-IDENTICAL to s186/s193."""
    if o11 <= 0:
        return 0.0
    o12 = dfc - o11
    o21 = dfv - o11
    o22 = N - dfc - dfv + o11
    if min(o12, o21, o22) < 0:
        return 0.0
    row1, row2 = dfc, N - dfc
    col1, col2 = dfv, N - dfv
    g2 = 0.0
    for o, r_, c_ in ((o11, row1, col1), (o12, row1, col2),
                      (o21, row2, col1), (o22, row2, col2)):
        e = r_ * c_ / N
        if o > 0 and e > 0:
            g2 += o * math.log(o / e)
    g2 *= 2.0
    e11 = row1 * col1 / N
    return g2 if o11 >= e11 else -g2


def compute_control(counts, cues, vocab):
    """BYTE-IDENTICAL to s186/s193 compute_control."""
    N = counts["Nsent"]
    df = counts["df"]
    out = {"K": counts["K"], "frame_win": counts["frame_win"], "Nsent": N, "cues": {}}
    for c in cues:
        dfc = df.get(c, 0)
        rec = {"df": dfc, "frame": [], "sent": []}
        for variant, co in (("frame", counts["co_frame"][c]),
                            ("sent", counts["co_sent"][c])):
            scored = []
            for v, o11 in co.items():
                if v not in vocab or v == c:
                    continue
                g = signed_g2(o11, dfc, df.get(v, 0), N)
                if g > 0:
                    scored.append((v, round(g, 3), o11))
            scored.sort(key=lambda x: (-x[1], x[0]))
            rec[variant] = scored[:counts["K"]]
        out["cues"][c] = rec
    return out


def _assert_frozen_g2():
    """freeze-condition 6: verify the G² COMPUTATION is unchanged vs the s193 build_cooc_c4.py.

    Import the s193 module and check (a) the frozen constants are identical, and (b) MY signed_g2 and
    compute_control produce byte-identical outputs to s193's across a battery of inputs. This proves
    computational identity (what condition 6 requires) without being brittle to docstring/comment text;
    only the cue POS (->verbs) and candidate pool V (->verbs) change by design.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("s193_build_cooc", os.path.abspath(S193))
    s193 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s193)
    assert s193.K == K and s193.FRAME_WIN == FRAME_WIN and s193.CONNECTIVES == CONNECTIVES, \
        "frozen constant DRIFT (K/FRAME_WIN/CONNECTIVES) vs s193"
    tests = [(0, 5, 5, 100), (1, 5, 5, 100), (3, 10, 8, 1000), (7, 12, 40, 100000),
             (5, 5, 5, 20), (2, 3, 100, 50000), (50, 60, 55, 1_000_000), (1, 1, 1, 10)]
    for a in tests:
        assert abs(s193.signed_g2(*a) - signed_g2(*a)) < 1e-12, f"signed_g2 DRIFT at {a}"
    cnt = {"Nsent": 1000, "K": K, "frame_win": FRAME_WIN, "df": {"x": 40, "a": 30, "b": 20, "c": 10},
           "co_sent": {"x": {"a": 25, "b": 5, "c": 8}}, "co_frame": {"x": {"a": 20, "b": 2, "c": 6}}}
    voc = {"a", "b", "c"}
    assert s193.compute_control(cnt, {"x"}, voc) == compute_control(cnt, {"x"}, voc), \
        "compute_control DRIFT vs s193"
    print("freeze-condition 6 OK: signed_g2 + compute_control produce byte-identical output to the s193 "
          "build_cooc_c4.py; K/FRAME_WIN/CONNECTIVES identical. Only the cue POS (->verbs) + V (->verbs) differ.")


def main():
    _assert_frozen_g2()
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
    print(f"total {Nsent} sentences, {Ntok} tokens in {time.time()-t0:.0f}s", flush=True)

    assert Nsent >= S186_NSENT, f"C4 volume {Nsent} < s186 {S186_NSENT} sentences — stream more shards"
    assert Ntok >= S186_NTOK_APPROX, f"C4 tokens {Ntok} < s186 ~{S186_NTOK_APPROX}"
    print(f"volume OK: {Nsent} sentences >= s186 {S186_NSENT}; {Ntok} tokens >= ~{S186_NTOK_APPROX}.")

    counts = {"Nsent": Nsent, "Ntok": Ntok, "df": df, "co_sent": co_sent,
              "co_frame": co_frame, "K": K, "frame_win": FRAME_WIN,
              "num_shards": NUM_SHARDS}
    json.dump(counts, open(os.path.join(HERE, "counts.json"), "w"))

    control = compute_control(counts, cues, vocab)
    json.dump(control, open(os.path.join(HERE, "control.json"), "w"), indent=1)
    print("counts.json + control.json written.")


if __name__ == "__main__":
    main()
