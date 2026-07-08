#!/usr/bin/env python3
"""build_cooc_c4.py — FROZEN distributional control build on C4 (Q2-B, ratified s193).

The FRESH-test control corpus (freeze-condition 4 + ratifier rider 1): the contrastive-frame G²
computation is BYTE-IDENTICAL to the s186 build_cooc.py (signed_g2, FRAME_WIN, CONNECTIVES, K,
weighting, compute_control) — VERIFIED by an assertion at import against the s186 source. ONLY the
sentence-streaming/IO adapter changes: s186 streamed a Simple-English-Wikipedia bz2 XML dump; this
streams gzipped C4 (web register), the genuine register-decorrelation the ratifier ruled primary.

CORPUS (recipe-not-corpus; nothing committed — streamed and discarded, bounded disk):
    allenai/c4, en config, shards c4-train.00000/00001/00002-of-01024.json.gz via the HuggingFace
    resolve URL. License: ODC-BY (+ Common-Crawl terms — carried to the result provenance, rider 3).
    resource/cooccurrence-corpus-scouting.md (s185 license scout, verified firsthand).
    A PROXY for the panel's (unknown) pretraining distribution — the residual measures the shadow
    cast by THIS proxy, not the training data. DIFFERENT source-family from s186's Simple Wikipedia,
    so a positive H1 outcome cannot be a same-corpus artifact (the whole point of Q2-B).

TWO CONTROLS (both frozen; frame-G² PRIMARY, sent-G² SENSITIVITY) — identical roles to s186.

H2 SECOND ARM (Q3-A, freeze-condition 5): a corpus Hearst-frame definitional-density proxy per cue,
computed in the SAME streaming pass. Hearst (1992) lexico-syntactic genus/species patterns; a cue
gets a Hearst hit when it falls within HEARST_WIN tokens of a frozen trigger n-gram. PREDICTED SIGN
POSITIVE (theory-set, frozen before counting: cues appearing more in genus-naming/definitional frames
are more definitionally central, and the essay predicts definitionally-central relations recover
better). IS-A depth (prep.py) is the PRIMARY proxy; a Hearst-only H2 win is reported qualified/weaker.

Emits counts.json (raw Nsent/Ntok/df/co_sent/co_frame/hearst — for the verifier to recompute) and
control.json (signed-G² ranked top-k per cue, both variants) + hearst.json (per-cue density).
Anti-cheat: no model output is read here; the control + proxy are computed independently of the panel.
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
S186 = os.path.join(HERE, "..", "2026-07-06-antonymy-shadow-saturation", "build_cooc.py")

# ---- FROZEN G² PARAMS — must byte-match s186 (asserted below) ----
K = 3                      # control produces top-k candidates
FRAME_WIN = 4              # max token distance for a contrastive frame
CONNECTIVES = {
    "and", "or", "nor", "but", "versus", "vs", "than", "to", "from", "either",
    "neither", "both", "between", "whether", "against", "unlike", "whereas",
    "while", "not", "opposed", "contrast",
}

# ---- FROZEN Hearst proxy params (Q3-A second arm; predicted sign POSITIVE) ----
HEARST_WIN = 3
HEARST_TRIGRAMS = {("and", "other"), ("or", "other"), ("such", "as"),
                   ("and", "any", "other"), ("or", "any", "other")}
HEARST_UNIGRAMS = {"including", "especially"}   # "X including/especially Y"
# note: ("such","as") also fires the "such X as Y" pattern via the window either side.

# ---- FROZEN C4 corpus spec (ratifier rider 1: pin shards; assert volume >= s186's) ----
C4_BASE = "https://huggingface.co/datasets/allenai/c4/resolve/main/en/c4-train.{:05d}-of-01024.json.gz"
NUM_SHARDS = 3             # 00000..00002; ~7.5M sentences/shard => ~22.5M > s186's 21.3M
S186_NSENT = 21_300_000    # s186 Simple-English-Wikipedia volume (result page)
S186_NTOK_APPROX = 320_000_000

_nonword = re.compile(r"[^a-z\s]+")
_sent = re.compile(r"[.!?]+\s")


def stream_sentences():
    """C4 IO ADAPTER (the ONLY change from s186; touches no counting/weighting logic)."""
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
    """Dunning (1993) log-likelihood, signed by attraction/repulsion. BYTE-IDENTICAL to s186."""
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
    """BYTE-IDENTICAL to s186 compute_control."""
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
    """freeze-condition 4: verify the G² COMPUTATION is unchanged vs s186 build_cooc.py.

    Import the s186 module and check (a) the frozen constants are identical, and (b) MY signed_g2 and
    compute_control produce byte-identical outputs to s186's across a battery of inputs. This proves
    computational identity (what condition 4 requires) without being brittle to docstring/comment text;
    only the sentence-streaming IO adapter differs by design.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("s186_build_cooc", os.path.abspath(S186))
    s186 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s186)
    assert s186.K == K and s186.FRAME_WIN == FRAME_WIN and s186.CONNECTIVES == CONNECTIVES, \
        "frozen constant DRIFT (K/FRAME_WIN/CONNECTIVES) vs s186"
    # signed_g2 battery
    tests = [(0, 5, 5, 100), (1, 5, 5, 100), (3, 10, 8, 1000), (7, 12, 40, 100000),
             (5, 5, 5, 20), (2, 3, 100, 50000), (50, 60, 55, 1_000_000), (1, 1, 1, 10)]
    for a in tests:
        assert abs(s186.signed_g2(*a) - signed_g2(*a)) < 1e-12, f"signed_g2 DRIFT at {a}"
    # compute_control on a tiny synthetic counts (identical output)
    cnt = {"Nsent": 1000, "K": K, "frame_win": FRAME_WIN, "df": {"x": 40, "a": 30, "b": 20, "c": 10},
           "co_sent": {"x": {"a": 25, "b": 5, "c": 8}}, "co_frame": {"x": {"a": 20, "b": 2, "c": 6}}}
    voc = {"a", "b", "c"}
    assert s186.compute_control(cnt, {"x"}, voc) == compute_control(cnt, {"x"}, voc), \
        "compute_control DRIFT vs s186"
    print("freeze-condition 4 OK: signed_g2 + compute_control produce byte-identical output to s186 "
          "build_cooc.py; K/FRAME_WIN/CONNECTIVES identical. Only the C4 IO adapter differs.")


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
    hearst = {c: 0 for c in cues}       # Hearst-frame participation count per cue
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
            # --- Hearst proxy (second arm): count if c is within HEARST_WIN of a trigger ---
            hit = False
            for pi in cpos:
                lo = max(0, pi - HEARST_WIN - 2)
                hi = min(len(toks), pi + HEARST_WIN + 3)
                window = toks[lo:hi]
                if any(u in window for u in HEARST_UNIGRAMS):
                    hit = True
                if not hit:
                    for a in range(len(window) - 1):
                        if (window[a], window[a + 1]) in HEARST_TRIGRAMS or \
                           (a + 2 < len(window) and (window[a], window[a + 1], window[a + 2]) in HEARST_TRIGRAMS):
                            hit = True
                            break
                if hit:
                    break
            if hit:
                hearst[c] += 1
        if Nsent % 2_000_000 == 0:
            print(f"  {Nsent} sentences, {Ntok} tokens, {time.time()-t0:.0f}s", flush=True)
    print(f"total {Nsent} sentences, {Ntok} tokens in {time.time()-t0:.0f}s", flush=True)

    # rider 1: assert achieved volume >= s186's before trusting G²
    assert Nsent >= S186_NSENT, f"C4 volume {Nsent} < s186 {S186_NSENT} sentences — stream more shards"
    assert Ntok >= S186_NTOK_APPROX, f"C4 tokens {Ntok} < s186 ~{S186_NTOK_APPROX}"
    print(f"rider 1 OK: {Nsent} sentences >= s186 {S186_NSENT}; {Ntok} tokens >= ~{S186_NTOK_APPROX}.")

    counts = {"Nsent": Nsent, "Ntok": Ntok, "df": df, "co_sent": co_sent,
              "co_frame": co_frame, "K": K, "frame_win": FRAME_WIN,
              "num_shards": NUM_SHARDS}
    json.dump(counts, open(os.path.join(HERE, "counts.json"), "w"))

    control = compute_control(counts, cues, vocab)
    json.dump(control, open(os.path.join(HERE, "control.json"), "w"), indent=1)

    # Hearst density = hits / df (rate per cue occurrence); df from the same pass
    hd = {c: (hearst[c] / df.get(c, 1) if df.get(c, 0) else 0.0) for c in cues}
    json.dump({"hearst_win": HEARST_WIN,
               "trigrams": sorted("|".join(t) for t in HEARST_TRIGRAMS),
               "unigrams": sorted(HEARST_UNIGRAMS),
               "predicted_sign": "positive",
               "hearst_count": hearst, "df": {c: df.get(c, 0) for c in cues},
               "hearst_density": hd},
              open(os.path.join(HERE, "hearst.json"), "w"), indent=1)
    print("counts.json + control.json + hearst.json written.")


if __name__ == "__main__":
    main()
