#!/usr/bin/env python3
"""prep.py — FROZEN item build for the FRESH relation-recovery / taxonomic-proxy probe (H1 + H2).

Design: experiments/designs/lexical-relation-recovery-taxonomic-proxy-v1.md
Gates RATIFIED s193: wiki/decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design.md
  Q1-C (across-relation n=6 PRIMARY verdict-of-record; item-level POWERED SECONDARY descriptive-only)
  Q2-B (C4 PRIMARY control corpus — see build_cooc_c4.py)
  Q3-A (IS-A depth PRIMARY proxy, frozen here + a corpus Hearst-frame SECOND arm, in build_cooc_c4.py)
  Q4   internal-contrast-only

WHAT THIS FREEZES (anti-cheat: run BEFORE any model call; nothing here reads model output)
------------------------------------------------------------------------------------------
1. items.json  — for each of the 6 WordNet noun relations, up to N_PER_REL FRESH cue nouns
   (DISJOINT from the 707 s186 cue lemmas), each with its word-form-level gold relatum set AND
   its pre-registered IS-A path depth (min_depth of the cue's FIRST noun synset — the pilot's
   frozen spec, note/taxonomic-proxy-recovery-pilot-v1; predicted sign NEGATIVE).
2. vocab.json — the control's candidate pool V: all single-word SubTLEX nouns with Lg10WF>=2.0.

FRESHNESS (the three changes that make this a genuine fresh test of H1/H2; freeze-condition 6):
- FRESH cues: the exact 707 committed s186 cue lemmas (items.json under
  experiments/runs/2026-07-06-antonymy-shadow-saturation/) are EXCLUDED before sampling; asserted
  per-relation 0-overlap. New SEED = 20260708.
- A DIFFERENT control corpus (Q2-B): C4 web text, not s186's Simple English Wikipedia (build_cooc_c4.py).
- A pre-registered taxonomic proxy (H2 arm): IS-A depth (here) + a corpus Hearst-frame proxy (build_cooc_c4.py).

DESIGN DECISIONS FROZEN HERE (byte-preserved from the s186 prep.py where noted; see PREREG.md):
- POS: nouns only (WordNet's taxonomic relations exist only for nouns). No pooling across POS.
- Frequency band: Lg10WF in [2.0, 4.5]  (byte-identical to s186 — the iconic-outlier cap included).
- Frequency matching: all six relations matched to a COMMON Lg10WF profile (antonymy's FRESH profile,
  the sparsest/binding relation), by stratified per-bin sampling.
- N_PER_REL = 120 target (equal); antonymy is capped LOWER by WordNet nominal sparsity after
  excluding the s186 cues (freeze-condition 6 / rider) and reported at its ACHIEVED N.
- Gold = word-form level, aggregated across senses of the cue. Relatum single-word, SubTLEX Lg10WF>=1.5.
  The relata() function, closures, RELMIN, VOCAB_MIN, STOPLIST are BYTE-IDENTICAL to s186 prep.py.
- SEED = 20260708 (fixed). Deterministic; re-running reproduces items.json byte-identical.

Inputs (committed / re-derivable):
- experiments/data/subtlex-us/SUBTLEXus74286wordstextversion.txt (gitignored, sha-pinned
  c5f86f065...; re-fetch via experiments/data/subtlex-us/prep.py — verified this session).
- WordNet 3.0 via nltk (resource/wordnet-sense-inventory; BSD-style license verified in-repo).
- experiments/runs/2026-07-06-antonymy-shadow-saturation/items.json (the 707 cues to exclude).
"""
import csv
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SUBTLEX = os.path.join(HERE, "..", "..", "data", "subtlex-us",
                       "SUBTLEXus74286wordstextversion.txt")
S186_ITEMS = os.path.join(HERE, "..", "2026-07-06-antonymy-shadow-saturation", "items.json")

SEED = 20260708
FMIN, FMAX = 2.0, 4.5      # cue frequency band (Lg10WF) — byte-identical to s186
RELMIN = 1.5               # minimum relatum frequency (Lg10WF) — byte-identical to s186
VOCAB_MIN = 2.0            # candidate-pool floor (Lg10WF) for control vocabulary V — byte-identical
VOCAB_MINLEN = 3           # drop <=2-char forms — byte-identical to s186
N_PER_REL = 120            # target (s186 used 130; antonymy pool shrinks after excluding s186 cues)
BIN_W = 0.25               # frequency-matching bin width — byte-identical to s186
RELS = ["antonymy", "synonymy", "hypernymy", "hyponymy", "holonymy", "meronymy"]

# Closed-class / function-word stoplist — BYTE-IDENTICAL to s186 prep.py.
STOPLIST = set("""
a an the this that these those some any no every each all both few many much most more
i you he she it we they me him her us them my your his its our their mine yours ours theirs
who whom whose which what where when why how there here
and or nor but so yet for as if then than because although though while whereas unless until
of in on at by to from with without within into onto upon over under above below between among
about across after before behind beneath beside besides beyond during except inside outside
through throughout toward towards up down off out near around against per via
is am are was were be been being do does did done have has had having will would shall should
can could may might must ought need dare going gonna wanna
not never very too also just only even still yet again once ever always often sometimes
this that here there now then thus hence therefore however moreover otherwise
one two three four five six seven eight nine ten first second next last
mr mrs ms dr st etc eg ie am pm
he'd she'd don isn wasn aren couldn wouldn shouldn didn doesn hasn haven won
o s t d m re ve ll y n r
""".split())


def load_freq():
    freq = {}
    with open(SUBTLEX, encoding="latin-1") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            try:
                freq[row["Word"].lower()] = float(row["Lg10WF"])
            except (ValueError, KeyError):
                pass
    return freq


def relata(lem, syn, rel, freq):
    # BYTE-IDENTICAL to s186 prep.py relata().
    if rel == "antonymy":
        out = set()
        for a in lem.antonyms():
            out.add(a.name().replace("_", " ").lower())
    elif rel == "synonymy":
        out = set()
        for l in syn.lemmas():
            if l.name() != lem.name():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "hypernymy":
        out = set()
        for s in syn.closure(lambda x: x.hypernyms(), depth=4):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "hyponymy":
        out = set()
        for s in syn.closure(lambda x: x.hyponyms(), depth=4):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "holonymy":
        out = set()
        for s in (syn.member_holonyms() + syn.part_holonyms()
                  + syn.substance_holonyms()):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "meronymy":
        out = set()
        for s in (syn.member_meronyms() + syn.part_meronyms()
                  + syn.substance_meronyms()):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    return {x for x in out if " " not in x and freq.get(x, 0.0) >= RELMIN}


def is_a_depth(cue):
    """PRE-REGISTERED PRIMARY H2 proxy (pilot spec, frozen): min_depth of the cue's FIRST noun
    synset. Gold-INDEPENDENT (a property of the cue, not the answer set). Predicted sign NEGATIVE."""
    from nltk.corpus import wordnet as wn
    ss = wn.synsets(cue, pos="n")
    return ss[0].min_depth() if ss else None


def build():
    from nltk.corpus import wordnet as wn
    freq = load_freq()

    # s186 cues to EXCLUDE (freshness; freeze-condition 6)
    s186 = json.load(open(S186_ITEMS))
    s186_cues = set()
    for r in RELS:
        for it in s186["items"][r]:
            s186_cues.add(it["cue"])
    print(f"excluding {len(s186_cues)} s186 cue lemmas (fresh-disjoint discipline)")

    # Candidate pool V — BYTE-IDENTICAL to s186.
    noun_forms = set()
    for syn in wn.all_synsets("n"):
        for lem in syn.lemmas():
            nm = lem.name().replace("_", " ").lower()
            if " " in nm:
                continue
            if len(nm) < VOCAB_MINLEN or nm in STOPLIST or not nm.isalpha():
                continue
            if freq.get(nm, 0.0) >= VOCAB_MIN:
                noun_forms.add(nm)
    vocab = sorted(noun_forms)

    # Eligible cues + aggregated word-form gold per relation — s186 logic, MINUS the s186 cues.
    cue_gold = {r: {} for r in RELS}
    for syn in wn.all_synsets("n"):
        for lem in syn.lemmas():
            nm = lem.name().replace("_", " ").lower()
            if " " in nm or nm in s186_cues:        # <-- the freshness exclusion
                continue
            fw = freq.get(nm)
            if fw is None or not (FMIN <= fw <= FMAX):
                continue
            for r in RELS:
                g = relata(lem, syn, r, freq)
                if g:
                    cue_gold[r].setdefault(nm, set()).update(g)

    for r in RELS:
        print(f"  fresh eligible pool {r:12s}: {len(cue_gold[r])}")

    def binof(w):
        return int((freq[w] - FMIN) / BIN_W)

    # Common frequency profile = antonymy's FRESH per-bin counts scaled to N_PER_REL (s186 logic).
    ant_cues = list(cue_gold["antonymy"].keys())
    ant_bins = {}
    for w in ant_cues:
        ant_bins[binof(w)] = ant_bins.get(binof(w), 0) + 1
    total_ant = len(ant_cues)
    target = {}
    for b, c in ant_bins.items():
        target[b] = round(N_PER_REL * c / total_ant)
    drift = N_PER_REL - sum(target.values())
    for b in sorted(target, key=lambda b: -target[b]):
        if drift == 0:
            break
        step = 1 if drift > 0 else -1
        if target[b] + step >= 0:
            target[b] += step
            drift -= step

    rng = random.Random(SEED)
    items = {}
    profile = {}
    for r in RELS:
        by_bin = {}
        for w in cue_gold[r]:
            by_bin.setdefault(binof(w), []).append(w)
        chosen = []
        for b in sorted(target):
            pool = sorted(by_bin.get(b, []))
            want = target[b]
            if len(pool) <= want:
                chosen.extend(pool)
            else:
                chosen.extend(rng.sample(pool, want))
        if len(chosen) < N_PER_REL:
            remaining = sorted(set(cue_gold[r]) - set(chosen))
            rng.shuffle(remaining)
            chosen.extend(remaining[:N_PER_REL - len(chosen)])
        chosen = sorted(chosen)[:N_PER_REL] if len(chosen) >= N_PER_REL else sorted(chosen)
        if len(chosen) > N_PER_REL:
            chosen = sorted(rng.sample(chosen, N_PER_REL))
        items[r] = [{"cue": w, "lg10wf": round(freq[w], 4),
                     "is_a_depth": is_a_depth(w),
                     "gold": sorted(cue_gold[r][w])} for w in chosen]
        fws = sorted(freq[w] for w in chosen)
        depths = [d for d in (is_a_depth(w) for w in chosen) if d is not None]
        profile[r] = {
            "n": len(chosen),
            "lg10wf_median": round(fws[len(fws) // 2], 3),
            "lg10wf_min": round(fws[0], 3),
            "lg10wf_max": round(fws[-1], 3),
            "mean_is_a_depth": round(sum(depths) / len(depths), 3),
            "n_depth_resolved": len(depths),
        }

    out_items = {
        "seed": SEED, "pos": "noun", "band": [FMIN, FMAX], "relmin": RELMIN,
        "n_per_rel_target": N_PER_REL, "relations": RELS, "profile": profile,
        "excluded_s186_cue_lemmas": len(s186_cues), "items": items,
    }
    with open(os.path.join(HERE, "items.json"), "w") as f:
        json.dump(out_items, f, indent=1, sort_keys=True)
    with open(os.path.join(HERE, "vocab.json"), "w") as f:
        json.dump({"vocab_min_lg10wf": VOCAB_MIN, "size": len(vocab), "vocab": vocab}, f)

    # ---- ASSERTIONS: disjointness from s186 (freeze-condition 6) ----
    for r in RELS:
        fresh = set(x["cue"] for x in items[r])
        ov = fresh & s186_cues
        assert not ov, f"OVERLAP with s186 in {r}: {sorted(ov)[:5]}"
    print("\nDISJOINTNESS OK: 0 overlap with the 707 s186 cue lemmas, all 6 relations.")

    print("\nitems.json written. per-relation profile (FRESH cues):")
    for r in RELS:
        p = profile[r]
        print(f"  {r:12s} n={p['n']:3d}  Lg10WF median={p['lg10wf_median']} "
              f"[{p['lg10wf_min']}, {p['lg10wf_max']}]  mean IS-A depth={p['mean_is_a_depth']} "
              f"(resolved {p['n_depth_resolved']}/{p['n']})")
    print(f"vocab.json: |V|={len(vocab)} candidate nouns (Lg10WF>={VOCAB_MIN})")


if __name__ == "__main__":
    build()
