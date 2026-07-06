#!/usr/bin/env python3
"""build_cooc.py — FROZEN distributional control build (Q1-C primary: contrastive-frame G²).

Streams a license-verified corpus (Simple English Wikipedia, CC BY-SA 4.0 + GFDL — the
same Wikimedia license the s185 scout verified for English Wikipedia;
resource/cooccurrence-corpus-scouting.md), and for the frozen cue set (items.json) and
candidate pool V (vocab.json) computes two co-occurrence statistics, then the control's
ranked top-k relata per cue.

CORPUS (recipe-not-corpus; the dump is NOT committed — gitignored, re-fetchable):
    https://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-pages-articles.xml.bz2
    License: CC BY-SA 4.0 + GFDL (dumps.wikimedia.org/legal.html).
    A PROXY for the panel's (unknown) pretraining distribution — condition 2 (proxy-corpus
    fence): the residual measures the shadow cast by THIS proxy, not the training data.

TWO CONTROLS (both frozen; PRIMARY named in PREREG):
- frame-G² (PRIMARY, Q1-A / condition 3, the project's own synthesis): Dunning (1993) G²
  over co-occurrence RESTRICTED to a symmetric/contrastive frame — c and v within <=4 tokens
  with a coordinating/contrastive connective between them, or immediately adjacent (conjoined).
  Neither Cao (all-intrasentential G²) nor Justeson & Katz (frames, not via G²) computed a
  frame-weighted G²; this construction is the project's, frozen here, cited as ours.
- sent-G² (SENSITIVITY): standard Dunning over all same-sentence co-occurrence (Cao's method).
  Reported side-by-side to show whether the residual ranking is control-choice robust.
(The Q1-B static-embedding cosine sensitivity is DEFERRED as a documented omission — the
ratified decision makes it "only a labelled sensitivity check"; the primary corpus G² is
built here, so deferring the third sensitivity is a legitimate scope cut, not a downgrade to
the weaker control. Named in PREREG + result.)

Emits: counts.json (raw Nsent/df/co_sent/co_frame — for the verifier to recompute) and
control.json (signed-G² ranked top-k per cue, both variants). Anti-cheat: no model output is
read here; the control is computed independently of the panel (the conjecture's requirement).
"""
import bz2
import json
import math
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.environ.get("WIKI_BZ2",
    "/tmp/claude-0/-home-user-ai-semantics/9bcb490d-ed29-5542-aa31-e37f4825359c/scratchpad/simplewiki.xml.bz2")

K = 3                      # control produces top-k candidates
FRAME_WIN = 4             # max token distance for a contrastive frame
CONNECTIVES = {
    "and", "or", "nor", "but", "versus", "vs", "than", "to", "from", "either",
    "neither", "both", "between", "whether", "against", "unlike", "whereas",
    "while", "not", "opposed", "contrast",
}

_tag = re.compile(r"<[^>]+>")
_wikilink = re.compile(r"\[\[([^\]|]+\|)?([^\]]+)\]\]")
_tmpl = re.compile(r"\{\{[^}]*\}\}")
_ref = re.compile(r"&[a-z]+;")
_nonword = re.compile(r"[^a-z\s]+")
_sent = re.compile(r"[.!?]+\s")


def clean(line):
    s = _wikilink.sub(lambda m: m.group(2), line)
    s = _tmpl.sub(" ", s)
    s = _tag.sub(" ", s)
    s = _ref.sub(" ", s)
    return s.lower()


def stream_sentences(path):
    with bz2.open(path, "rt", encoding="utf-8", errors="ignore") as f:
        for line in f:
            s = clean(line)
            for sent in _sent.split(s):
                toks = _nonword.sub(" ", sent).split()
                if toks:
                    yield toks


def main():
    items = json.load(open(os.path.join(HERE, "items.json")))
    vocab = set(json.load(open(os.path.join(HERE, "vocab.json")))["vocab"])
    cues = set()
    gold = {}                      # (rel, cue) -> set(gold)
    for r, lst in items["items"].items():
        for it in lst:
            cues.add(it["cue"])
            gold[(r, it["cue"])] = set(it["gold"])
    target = vocab | cues          # words we track
    conn = CONNECTIVES

    df = {}                        # sentence document frequency, w in target
    co_sent = {}                   # co_sent[cue][v]
    co_frame = {}
    for c in cues:
        co_sent[c] = {}
        co_frame[c] = {}
    Nsent = 0
    t0 = time.time()
    for toks in stream_sentences(SCRATCH):
        Nsent += 1
        # positions of target tokens
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
                # frame test: any (c,v) occurrence within FRAME_WIN with a connective between
                # or immediately adjacent
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
        if Nsent % 400000 == 0:
            print(f"  {Nsent} sentences, {time.time()-t0:.0f}s", flush=True)
    print(f"total {Nsent} sentences in {time.time()-t0:.0f}s", flush=True)

    counts = {"Nsent": Nsent, "df": df, "co_sent": co_sent, "co_frame": co_frame,
              "K": K, "frame_win": FRAME_WIN}
    json.dump(counts, open(os.path.join(HERE, "counts.json"), "w"))

    control = compute_control(counts, cues, vocab)
    json.dump(control, open(os.path.join(HERE, "control.json"), "w"), indent=1)
    print("counts.json + control.json written.")


def signed_g2(o11, dfc, dfv, N):
    """Dunning (1993) log-likelihood, signed by attraction/repulsion."""
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


if __name__ == "__main__":
    main()
