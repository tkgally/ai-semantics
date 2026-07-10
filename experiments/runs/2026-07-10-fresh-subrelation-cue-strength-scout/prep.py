#!/usr/bin/env python3
"""prep.py — FRESH-SUB-RELATION item build for the C4 cue-strength scout (s202).

NEXT.md s202 backlog pick 1 / note/decoupling-fresh-inventory-scout-v1: measure the
contrastive-frame C4 cue-strength of the FRESH un-probed noun sub-relations to decide whether a
C2-*dissociating* within-noun sub-inventory pair is assemblable (the binding pre-step the s201
scout named). This is a $0 corpus computation — NO model call, NO verdict-bearing output, NO human
anchor. It feeds a DESIGN decision that a later session ratifies; it settles no empirical claim.

Conjecture under test (a registered bet, NOT confirmed): conjecture/decoupling-relation-inventory-shape
  C1: a low-cue/high-recovery HEAD DISALIGNER present; C2: NO ALIGNED TAIL (worst-recovered
  relations are not the lowest-cue-strength ones). The decoupling appears iff C1 AND C2.

WHAT THIS FREEZES (anti-cheat: nothing here reads model output):
  items.json — for each fresh noun sub-relation, up to N_PER_REL cue nouns (DISJOINT from the
    1,319 already-probed cues = 707 s186 + 612 s193), each with its word-form-level DIRECT gold
    relatum set and Lg10WF. Gold uses the DIRECT sub-relation (member/part/substance
    {meronyms,holonyms}, instance_{hypernyms,hyponyms}) — NOT the coarse union the s186/s193
    relata() computed, and NOT a taxonomic closure. This is the natural fresh-inventory split.
  vocab.json — the control's candidate pool V: single-word SubTLEX NOUNS with Lg10WF>=2.0
    (BYTE-IDENTICAL construction to s193 vocab.json).

DESIGN NOTES / honest scope:
  - `attribute` (syn.attributes()) is DROPPED: its relata are ADJECTIVES (POS 'a'), incommensurable
    with the noun candidate pool V — the frame control's top-k are nouns, so an adjective gold would
    read as a spurious cue-strength floor. Measuring it needs a separate cross-POS control; out of
    scope for this scout. Documented in the note.
  - Frequency band [2.0,4.5] + RELMIN 1.5 are BYTE-IDENTICAL to s186/s193, so the fresh cues sit in
    the SAME frequency band the coarse numbers were measured on. The PRIMARY scout samples up to
    N_PER_REL per relation WITHOUT strict per-bin matching (a scout, not a claim-carrying freeze);
    analyze.py adds a frequency-matched-subset ROBUSTNESS pass so any residual frequency imbalance
    in the cue-strength ORDERING is visible. The eventual frozen design (later session, with critic)
    does the rigorous matched freeze.
  - SEED fixed; deterministic. Re-running reproduces items.json byte-identical.

Inputs (committed / re-derivable):
  - experiments/data/subtlex-us/SUBTLEXus74286wordstextversion.txt (gitignored; sha256-pinned
    c5f86f065..., re-fetched + verified this session via that dir's prep.py recipe URL).
  - WordNet 3.0 via nltk (resource/wordnet-sense-inventory; BSD-style license verified in-repo).
  - experiments/runs/2026-07-06-antonymy-shadow-saturation/items.json (707 s186 cues to exclude).
  - experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/items.json (612 s193 cues to exclude).
"""
import csv
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SUBTLEX = os.path.join(HERE, "..", "..", "data", "subtlex-us",
                       "SUBTLEXus74286wordstextversion.txt")
S186_ITEMS = os.path.join(HERE, "..", "2026-07-06-antonymy-shadow-saturation", "items.json")
S193_ITEMS = os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy", "items.json")

SEED = 20260710
FMIN, FMAX = 2.0, 4.5      # cue frequency band (Lg10WF) — byte-identical to s186/s193
RELMIN = 1.5               # minimum relatum frequency (Lg10WF) — byte-identical to s186/s193
VOCAB_MIN = 2.0            # candidate-pool floor (Lg10WF) for control vocabulary V — byte-identical
VOCAB_MINLEN = 3           # drop <=2-char forms — byte-identical to s186/s193
N_PER_REL = 120            # target (report ACHIEVED per relation; sparse sub-types fall short)

# FRESH noun sub-relations. DIRECT gold (single sub-type), NOT the coarse union.
SUBRELS = {
    "member_meronymy": lambda s: s.member_meronyms(),
    "part_meronymy": lambda s: s.part_meronyms(),
    "substance_meronymy": lambda s: s.substance_meronyms(),
    "member_holonymy": lambda s: s.member_holonyms(),
    "part_holonymy": lambda s: s.part_holonyms(),
    "substance_holonymy": lambda s: s.substance_holonyms(),
    "instance_hypernymy": lambda s: s.instance_hypernyms(),
    "instance_hyponymy": lambda s: s.instance_hyponyms(),
}
RELS = list(SUBRELS.keys())

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


def load_cues(path):
    d = json.load(open(path))
    s = set()
    for _, its in d["items"].items():
        for it in its:
            s.add(it["cue"])
    return s


def direct_relata(syn, fn, freq):
    """DIRECT sub-relation gold, word-form level, single-word, relatum Lg10WF>=RELMIN."""
    out = set()
    for r in fn(syn):
        for l in r.lemmas():
            x = l.name().replace("_", " ").lower()
            if " " not in x and x.isalpha() and freq.get(x, 0.0) >= RELMIN:
                out.add(x)
    return out


def build():
    from nltk.corpus import wordnet as wn
    freq = load_freq()

    probed = load_cues(S186_ITEMS) | load_cues(S193_ITEMS)
    print(f"excluding {len(probed)} already-probed cue lemmas (707 s186 + 612 s193; fresh-disjoint)")

    # Candidate pool V — BYTE-IDENTICAL construction to s193 vocab.json.
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

    # Eligible cues + aggregated DIRECT word-form gold per fresh sub-relation (band-filtered, disjoint).
    cue_gold = {r: {} for r in RELS}
    for syn in wn.all_synsets("n"):
        for lem in syn.lemmas():
            nm = lem.name().replace("_", " ").lower()
            if " " in nm or nm in probed or not nm.isalpha():
                continue
            fw = freq.get(nm)
            if fw is None or not (FMIN <= fw <= FMAX):
                continue
            for r, fn in SUBRELS.items():
                g = direct_relata(syn, fn, freq)
                if g:
                    cue_gold[r].setdefault(nm, set()).update(g)

    print("\neligible pools (band [2.0,4.5] + RELMIN 1.5 + disjoint; before N cap):")
    for r in RELS:
        print(f"  {r:20s}: {len(cue_gold[r])}")

    rng = random.Random(SEED)
    items = {}
    profile = {}
    for r in RELS:
        pool = sorted(cue_gold[r])
        chosen = sorted(rng.sample(pool, N_PER_REL)) if len(pool) > N_PER_REL else pool
        items[r] = [{"cue": w, "lg10wf": round(freq[w], 4),
                     "gold": sorted(cue_gold[r][w])} for w in chosen]
        if chosen:
            fws = sorted(freq[w] for w in chosen)
            gsz = [len(cue_gold[r][w]) for w in chosen]
            profile[r] = {
                "n": len(chosen),
                "eligible_pool": len(pool),
                "lg10wf_median": round(fws[len(fws) // 2], 3),
                "lg10wf_min": round(fws[0], 3),
                "lg10wf_max": round(fws[-1], 3),
                "gold_size_median": sorted(gsz)[len(gsz) // 2],
                "gold_size_mean": round(sum(gsz) / len(gsz), 2),
            }
        else:
            profile[r] = {"n": 0, "eligible_pool": len(pool)}

    out_items = {
        "seed": SEED, "pos": "noun", "band": [FMIN, FMAX], "relmin": RELMIN,
        "n_per_rel_target": N_PER_REL, "relations": RELS, "gold": "direct-subrelation",
        "excluded_probed_cue_lemmas": len(probed), "profile": profile, "items": items,
    }
    with open(os.path.join(HERE, "items.json"), "w") as f:
        json.dump(out_items, f, indent=1, sort_keys=True)
    with open(os.path.join(HERE, "vocab.json"), "w") as f:
        json.dump({"vocab_min_lg10wf": VOCAB_MIN, "size": len(vocab), "vocab": vocab}, f)

    # ---- ASSERTIONS: disjointness from the 1,319 probed cues ----
    for r in RELS:
        fresh = set(x["cue"] for x in items[r])
        ov = fresh & probed
        assert not ov, f"OVERLAP with probed cues in {r}: {sorted(ov)[:5]}"
    print("\nDISJOINTNESS OK: 0 overlap with the 1,319 probed cue lemmas, all sub-relations.")

    print("\nitems.json written. per-relation profile (FRESH cues):")
    for r in RELS:
        p = profile[r]
        if p["n"]:
            print(f"  {r:20s} n={p['n']:3d}  Lg10WF median={p['lg10wf_median']} "
                  f"[{p['lg10wf_min']}, {p['lg10wf_max']}]  gold median={p['gold_size_median']}")
        else:
            print(f"  {r:20s} n=0 (eligible pool {p['eligible_pool']})")
    print(f"vocab.json: |V|={len(vocab)} candidate nouns (Lg10WF>={VOCAB_MIN})")


if __name__ == "__main__":
    build()
