#!/usr/bin/env python3
"""prep.py — FROZEN item build for the A1b antonymy shadow-saturation probe (v1).

Program A1b; design experiments/designs/lexical-relation-shadow-saturation-v1.md;
gates ratified wiki/decisions/resolved/antonymy-internal-contrast-scoring.md (Q1-C/Q2-A/Q3).

WHAT THIS FREEZES (anti-cheat: run BEFORE any model call; nothing here reads model output)
------------------------------------------------------------------------------------------
1. items.json  — for each of the 6 WordNet noun relations, N=130 cue NOUNS, each with its
   word-form-level gold relatum set (Cao's word-form task granularity). NOUN-scoped because
   WordNet's taxonomic relations (hyper/hypo/holo/mero) exist only for nouns; adjectives carry
   only antonymy/synonymy, so a 6-relation cross-relation ranking is inherently nominal. The
   adjective-antonymy replication (J&K's home POS) is named future work, not run here.
2. vocab.json — the control's candidate pool V: all single-word SubTLEX nouns with Lg10WF>=2.0.
   The distributional control ranks ALL of V by co-occurrence G² with a cue (build_cooc.py),
   takes top-k, and is scored against the same WordNet gold — so it faces the same distractor
   space the model does, not a gold-only shortlist.

DESIGN DECISIONS FROZEN HERE (see PREREG.md for the full pre-registration):
- POS: nouns only (reason above). POS reported; no pooling across POS (there is only one).
- Frequency band: Lg10WF in [2.0, 4.5]. Excludes the very-highest-frequency iconic pairs
  (man/woman etc., Lg10WF>4.5) that Cao-2025b flags as G² outliers — the outlier cap.
- Frequency matching: all six relations are matched to a COMMON Lg10WF profile (the antonymy
  distribution, the sparsest and hence binding relation), by stratified per-bin sampling, so
  raw-recovery differences across relations are not a unigram-frequency artifact.
- N = 130 per relation (equal; antonymy pool is 233 in-band, so no sub-power cap needed).
- Gold = word-form level, aggregated across senses of the cue (Cao's task is word-form, not
  sense level). Relatum must be single-word and in SubTLEX with Lg10WF>=1.5.
- SEED = 20260706 (fixed). Deterministic; re-running reproduces items.json byte-identical.

Inputs (committed / re-derivable):
- experiments/data/subtlex-us/SUBTLEXus74286wordstextversion.txt (gitignored, sha-pinned;
  re-fetch via experiments/data/subtlex-us/prep.py). sha256 verified in that recipe.
- WordNet 3.0 via nltk (resource/wordnet-sense-inventory; BSD-style license verified in-repo).
"""
import csv
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUBTLEX = os.path.join(HERE, "..", "..", "data", "subtlex-us",
                       "SUBTLEXus74286wordstextversion.txt")

SEED = 20260706
FMIN, FMAX = 2.0, 4.5      # cue frequency band (Lg10WF)
RELMIN = 1.5               # minimum relatum frequency (Lg10WF)
VOCAB_MIN = 2.0            # candidate-pool floor (Lg10WF) for control vocabulary V
VOCAB_MINLEN = 3          # drop <=2-char forms (single-letter/abbrev WordNet noun homographs)
N_PER_REL = 130
BIN_W = 0.25              # frequency-matching bin width
RELS = ["antonymy", "synonymy", "hypernymy", "hyponymy", "holonymy", "meronymy"]

# Closed-class / function-word stoplist. Many are ALSO WordNet single-word noun lemmas
# (a, i, s, in, no, so, do, be, o, ...) and are high-frequency, so they would otherwise
# flood the co-occurrence control's top-k with content-free candidates. The candidate pool
# V is meant to be open-class content nouns (the space the model's relata live in), so these
# are excluded from V. Frozen here (does not touch item selection — cues/gold are unaffected).
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
    with open(SUBTLEX) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            try:
                freq[row["Word"].lower()] = float(row["Lg10WF"])
            except (ValueError, KeyError):
                pass
    return freq


def relata(lem, syn, rel, freq):
    from nltk.corpus import wordnet as wn
    out = set()
    if rel == "antonymy":
        for a in lem.antonyms():
            out.add(a.name().replace("_", " ").lower())
    elif rel == "synonymy":
        for l in syn.lemmas():
            if l.name() != lem.name():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "hypernymy":
        for s in syn.hypernyms():
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "hyponymy":
        for s in syn.hyponyms():
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "holonymy":
        for s in (syn.member_holonyms() + syn.part_holonyms()
                  + syn.substance_holonyms()):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "meronymy":
        for s in (syn.member_meronyms() + syn.part_meronyms()
                  + syn.substance_meronyms()):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    return {x for x in out if " " not in x and freq.get(x, 0.0) >= RELMIN}


def build():
    from nltk.corpus import wordnet as wn
    freq = load_freq()

    # Candidate pool V: single-word SubTLEX nouns with Lg10WF>=VOCAB_MIN.
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

    # Eligible cues + aggregated word-form gold per relation (over all senses of the cue).
    cue_gold = {r: {} for r in RELS}
    for syn in wn.all_synsets("n"):
        for lem in syn.lemmas():
            nm = lem.name().replace("_", " ").lower()
            if " " in nm:
                continue
            fw = freq.get(nm)
            if fw is None or not (FMIN <= fw <= FMAX):
                continue
            for r in RELS:
                g = relata(lem, syn, r, freq)
                if g:
                    cue_gold[r].setdefault(nm, set()).update(g)

    def binof(w):
        return int((freq[w] - FMIN) / BIN_W)

    # Common frequency profile = antonymy's per-bin counts scaled to N_PER_REL.
    ant_cues = list(cue_gold["antonymy"].keys())
    ant_bins = {}
    for w in ant_cues:
        ant_bins[binof(w)] = ant_bins.get(binof(w), 0) + 1
    total_ant = len(ant_cues)
    target = {}
    for b, c in ant_bins.items():
        target[b] = round(N_PER_REL * c / total_ant)
    # fix rounding drift to hit exactly N_PER_REL
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
                chosen.extend(pool)          # take all if short (redistribute below)
            else:
                chosen.extend(rng.sample(pool, want))
        # if short of N (a relation lacked a bin), top up from remaining eligible cues
        if len(chosen) < N_PER_REL:
            remaining = sorted(set(cue_gold[r]) - set(chosen))
            rng.shuffle(remaining)
            chosen.extend(remaining[:N_PER_REL - len(chosen)])
        chosen = sorted(chosen)[:N_PER_REL] if len(chosen) >= N_PER_REL else sorted(chosen)
        # deterministic final draw of exactly N (seeded) when we have a surplus
        if len(chosen) > N_PER_REL:
            chosen = sorted(rng.sample(chosen, N_PER_REL))
        items[r] = [{"cue": w, "lg10wf": round(freq[w], 4),
                     "gold": sorted(cue_gold[r][w])} for w in chosen]
        fws = sorted(freq[w] for w in chosen)
        profile[r] = {
            "n": len(chosen),
            "lg10wf_median": round(fws[len(fws) // 2], 3),
            "lg10wf_min": round(fws[0], 3),
            "lg10wf_max": round(fws[-1], 3),
        }

    out_items = {
        "seed": SEED, "pos": "noun", "band": [FMIN, FMAX], "relmin": RELMIN,
        "n_per_rel": N_PER_REL, "relations": RELS, "profile": profile, "items": items,
    }
    with open(os.path.join(HERE, "items.json"), "w") as f:
        json.dump(out_items, f, indent=1, sort_keys=True)
    with open(os.path.join(HERE, "vocab.json"), "w") as f:
        json.dump({"vocab_min_lg10wf": VOCAB_MIN, "size": len(vocab),
                   "vocab": vocab}, f)

    print("items.json written. per-relation frequency profile:")
    for r in RELS:
        p = profile[r]
        print(f"  {r:12s} n={p['n']:3d}  Lg10WF median={p['lg10wf_median']}  "
              f"[{p['lg10wf_min']}, {p['lg10wf_max']}]")
    print(f"vocab.json: |V|={len(vocab)} candidate nouns (Lg10WF>={VOCAB_MIN})")
    # report cue overlap across relations
    allc = {r: set(x["cue"] for x in items[r]) for r in RELS}
    import itertools
    ov = max(len(allc[a] & allc[b]) for a, b in itertools.combinations(RELS, 2))
    print(f"max pairwise cue overlap across relations: {ov} (cues may serve multiple relations)")


if __name__ == "__main__":
    build()
