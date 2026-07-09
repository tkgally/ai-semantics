#!/usr/bin/env python3
"""prep.py — FROZEN item build for the ADJECTIVE-antonymy replication probe (H1 + antonymy-shadow).

Design: experiments/designs/adjective-antonymy-replication-v1.md
Gates RATIFIED s196: wiki/decisions/resolved/adjective-antonymy-replication-design.md
  Q1-C (antonymy-shadow clause PRIMARY verdict-of-record; across-relation decoupling H1 CO-PRIMARY at
        true low power; item-level cue-strength->recovery POWERED SECONDARY, descriptive-only)
  Q2-A (NO structural-proxy arm — H2 does NOT transfer: WordNet has no adjective IS-A taxonomy;
        adjective min_depth() is a degenerate constant 0. No is_a_depth field here.)
  Q3   internal-contrast-only

WHAT THIS FREEZES (anti-cheat: run BEFORE any model call; nothing here reads model output)
------------------------------------------------------------------------------------------
1. items.json  — for each of the 4 WordNet ADJECTIVE relations, up to N_PER_REL FRESH cue adjectives
   (DISJOINT from the 707 s186 noun cue lemmas — the exclusion also covers noun/adjective homographs
   like light/right/fine), each with its word-form-level gold relatum set. NO is_a_depth (H2 does not
   transfer; Q2-A).
2. vocab.json — the control's candidate pool V: all single-word SubTLEX ADJECTIVES with Lg10WF>=2.0.

FRESHNESS / POS (the change that makes this a genuine fresh POS-crossing test of H1, and the reason
H2 cannot transfer):
- POS = ADJECTIVES (WordNet POS 'a' head + 's' satellite, via nltk). The noun probes (s186, s193)
  stand on nouns only; J&K MEASURED contrastive-frame saturation on predicative adjectives, so this
  is the home-POS re-test. WordNet's IS-A taxonomy (and H2's IS-A-depth proxy) does NOT exist for
  adjectives -> H2 is not tested (Q2-A).
- FRESH cues: the 707 committed s186 cue lemmas (items.json under
  experiments/runs/2026-07-06-antonymy-shadow-saturation/) are EXCLUDED before sampling; asserted
  per-relation 0-overlap. New SEED = 20260709.
- Relation inventory (Q1-C): antonymy (J&K home relation), synonymy (synset co-members), similar
  (synset.similar_tos() satellite clustering, the adjective near-synonymy relation), alsosee
  (synset.also_sees()). All four clear powered N after freq-matching + s186 disjointness.

DESIGN DECISIONS FROZEN HERE (byte-preserved from the s186/s193 prep.py where noted; see PREREG.md):
- Frequency band: Lg10WF in [2.0, 4.5]  (byte-identical to s186/s193 — the iconic-outlier cap
  included: the very-high-frequency iconic antonym pairs big/good/hot that J&K/Cao flag as G^2
  outliers sit above Lg10WF 4.5 and are excluded by the band).
- Frequency matching: all four relations matched to a COMMON Lg10WF profile (ANTONYMY's fresh
  per-bin profile — the primary relation, and one of the two sparsest), by stratified per-bin
  sampling (the s193 discipline).
- N_PER_REL = 130 target (equal, powered ~120-150; PROTOCOL sec.4). Each relation reported at its
  ACHIEVED N. (Measured eligible pools s196: antonymy 512, synonymy 1475, similar 1993, alsosee 482
  fresh in-band cues with a single-word gold relatum -> all clear 130.)
- Gold = word-form level, aggregated across senses of the cue. Relatum single-word, SubTLEX
  Lg10WF>=1.5. RELMIN, VOCAB_MIN, VOCAB_MINLEN, BIN_W, STOPLIST are BYTE-IDENTICAL to s186/s193
  prep.py; the relata() adjective branches are the POS-specific parallel of the s186 relata().
- SEED = 20260709 (fixed). Deterministic; re-running reproduces items.json byte-identical.

Inputs (committed / re-derivable):
- experiments/data/subtlex-us/SUBTLEXus74286wordstextversion.txt (gitignored, sha-pinned
  c5f86f065...; re-fetch via experiments/data/subtlex-us/prep.py — verified this session).
- WordNet 3.0 via nltk (resource/wordnet-sense-inventory; BSD-style license verified in-repo).
- experiments/runs/2026-07-06-antonymy-shadow-saturation/items.json (the 707 noun cues to exclude).
"""
import csv
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SUBTLEX = os.path.join(HERE, "..", "..", "data", "subtlex-us",
                       "SUBTLEXus74286wordstextversion.txt")
S186_ITEMS = os.path.join(HERE, "..", "2026-07-06-antonymy-shadow-saturation", "items.json")

SEED = 20260709
FMIN, FMAX = 2.0, 4.5      # cue frequency band (Lg10WF) — byte-identical to s186/s193
RELMIN = 1.5               # minimum relatum frequency (Lg10WF) — byte-identical to s186/s193
VOCAB_MIN = 2.0            # candidate-pool floor (Lg10WF) for control vocabulary V — byte-identical
VOCAB_MINLEN = 3           # drop <=2-char forms — byte-identical to s186/s193
N_PER_REL = 130            # target (equal); powered ~120-150 (PROTOCOL sec.4)
BIN_W = 0.25               # frequency-matching bin width — byte-identical to s186/s193
RELS = ["antonymy", "synonymy", "similar", "alsosee"]
POS = ["a", "s"]           # WordNet adjective heads ('a') + satellites ('s')

# Closed-class / function-word stoplist — BYTE-IDENTICAL to s186/s193 prep.py.
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
    """ADJECTIVE relation gold — the POS-specific parallel of the s186/s193 noun relata().
    Single-word, SubTLEX Lg10WF>=RELMIN, word-form level."""
    out = set()
    if rel == "antonymy":
        for a in lem.antonyms():
            out.add(a.name().replace("_", " ").lower())
    elif rel == "synonymy":
        for l in syn.lemmas():
            if l.name() != lem.name():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "similar":
        for s in syn.similar_tos():
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "alsosee":
        for s in syn.also_sees():
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    return {x for x in out if " " not in x and freq.get(x, 0.0) >= RELMIN}


def build():
    from nltk.corpus import wordnet as wn
    freq = load_freq()

    # s186 noun cues to EXCLUDE (freshness; covers noun/adjective homographs)
    s186 = json.load(open(S186_ITEMS))
    s186_cues = set()
    for r in s186["items"]:
        for it in s186["items"][r]:
            s186_cues.add(it["cue"])
    print(f"excluding {len(s186_cues)} s186 noun cue lemmas (fresh-disjoint discipline)")

    # Candidate pool V — single-word ADJECTIVE forms (POS a+s), Lg10WF>=VOCAB_MIN.
    adj_forms = set()
    for pos in POS:
        for syn in wn.all_synsets(pos):
            for lem in syn.lemmas():
                nm = lem.name().replace("_", " ").lower()
                if " " in nm:
                    continue
                if len(nm) < VOCAB_MINLEN or nm in STOPLIST or not nm.isalpha():
                    continue
                if freq.get(nm, 0.0) >= VOCAB_MIN:
                    adj_forms.add(nm)
    vocab = sorted(adj_forms)

    # Eligible cues + aggregated word-form gold per relation — s186 logic, MINUS the s186 cues.
    cue_gold = {r: {} for r in RELS}
    for pos in POS:
        for syn in wn.all_synsets(pos):
            for lem in syn.lemmas():
                nm = lem.name().replace("_", " ").lower()
                if " " in nm or nm in s186_cues:        # <-- freshness exclusion
                    continue
                fw = freq.get(nm)
                if fw is None or not (FMIN <= fw <= FMAX):
                    continue
                for r in RELS:
                    g = relata(lem, syn, r, freq)
                    if g:
                        cue_gold[r].setdefault(nm, set()).update(g)

    for r in RELS:
        print(f"  fresh eligible pool {r:10s}: {len(cue_gold[r])}")

    def binof(w):
        return int((freq[w] - FMIN) / BIN_W)

    # Common frequency profile = ANTONYMY's FRESH per-bin counts scaled to N_PER_REL (s193 logic).
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
                     "gold": sorted(cue_gold[r][w])} for w in chosen]
        fws = sorted(freq[w] for w in chosen)
        golds = [len(cue_gold[r][w]) for w in chosen]
        profile[r] = {
            "n": len(chosen),
            "lg10wf_median": round(fws[len(fws) // 2], 3),
            "lg10wf_min": round(fws[0], 3),
            "lg10wf_max": round(fws[-1], 3),
            "gold_size_median": sorted(golds)[len(golds) // 2],
            "gold_size_mean": round(sum(golds) / len(golds), 3),
        }

    out_items = {
        "seed": SEED, "pos": "adjective", "wn_pos": POS, "band": [FMIN, FMAX], "relmin": RELMIN,
        "n_per_rel_target": N_PER_REL, "relations": RELS, "profile": profile,
        "excluded_s186_cue_lemmas": len(s186_cues), "items": items,
    }
    with open(os.path.join(HERE, "items.json"), "w") as f:
        json.dump(out_items, f, indent=1, sort_keys=True)
    with open(os.path.join(HERE, "vocab.json"), "w") as f:
        json.dump({"vocab_min_lg10wf": VOCAB_MIN, "size": len(vocab), "vocab": vocab}, f)

    # ---- ASSERTIONS: disjointness from s186 (freshness) ----
    for r in RELS:
        fresh = set(x["cue"] for x in items[r])
        ov = fresh & s186_cues
        assert not ov, f"OVERLAP with s186 in {r}: {sorted(ov)[:5]}"
    print("\nDISJOINTNESS OK: 0 overlap with the 707 s186 cue lemmas, all 4 relations.")

    print("\nitems.json written. per-relation profile (FRESH adjective cues):")
    for r in RELS:
        p = profile[r]
        print(f"  {r:10s} n={p['n']:3d}  Lg10WF median={p['lg10wf_median']} "
              f"[{p['lg10wf_min']}, {p['lg10wf_max']}]  gold size median={p['gold_size_median']} "
              f"mean={p['gold_size_mean']}")
    print(f"vocab.json: |V|={len(vocab)} candidate adjectives (Lg10WF>={VOCAB_MIN})")


if __name__ == "__main__":
    build()
