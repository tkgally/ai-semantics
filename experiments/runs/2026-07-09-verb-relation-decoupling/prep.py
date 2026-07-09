#!/usr/bin/env python3
"""prep.py — FROZEN item build for the VERB-relation decoupling probe (H-verb-1 + H-verb-2).

Design: experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md
Gates RATIFIED s199: wiki/decisions/resolved/verb-relation-decoupling-design.md
  Q1-C (5-relation across-relation arm PRIMARY [H1 decoupling] + H2 troponymy-depth CO-PRIMARY;
        item-level POWERED SECONDARY descriptive-only; `cause` a CONDITIONAL 6th — mechanical rule below)
  Q2-A (troponymy-depth = min_depth of the cue's FIRST verb synset, pos="v"; predicted sign NEGATIVE;
        byte-analogous to the noun is_a_depth — a verb win is a REPLICATION of the noun mechanism)
  Q3   internal-contrast-only

WHAT THIS FREEZES (anti-cheat: run BEFORE any model call; nothing here reads model output)
------------------------------------------------------------------------------------------
1. items.json  — for each core VERB relation, up to N_PER_REL FRESH cue verbs (POS-agnostic-surface
   DISJOINT from the 1,740 prior cue lemmas: s186 nouns + s193 fresh nouns + s196 adjectives — the
   homograph guard, freeze-condition 4 / B-vote), each with its word-form-level gold relatum set AND
   its pre-registered troponymy-depth (min_depth of the cue's FIRST verb synset; Q2-A; predicted NEG).
2. vocab.json — the control's candidate pool V: all single-word SubTLEX VERBS with Lg10WF>=2.0.
3. B1 (s199 ratifier) — the achieved per-relation mean troponymy-depths on the FROZEN sample and the
   NUMERIC degeneracy bound: DEPTH_DEGENERATE iff the NON-antonymy mean-depth RANGE < DEGEN_MAX_RANGE.
   Computed here, before any model call; frozen into items.json + PREREG. If degenerate, H2 is
   under-powered SYMMETRICALLY (B2): a DEPTH-FAILS is non-falsifying AND a DEPTH-OUT-PREDICTS is not
   banked as noun-equivalent.

MECHANICAL `cause`-inclusion rule (Q1-C / freeze-condition 5, locked BEFORE any inspection):
  `cause` is added as a SIXTH relation IFF its ACHIEVED matched-N (after frequency-matching to the
  binding profile) is >= CAUSE_MIN (100). Decided mechanically here, pre-registered either way; `cause`
  never enters or exits after recovery is seen. If it drops out, the arm is 5-point and this is reported.

THIN-RELATION fallback for the CORE set (freeze-condition 3, covers antonymy/entailment not only cause):
  Any CORE relation whose achieved matched-N < CORE_FLOOR (80) is reported at its achieved N and
  NEVER silently dropped or reweighted; if a core relation falls below CORE_FLOOR the arm is reported at
  its true (reduced) point-count and flagged. (Design-time fresh pools: antonymy 140, entailment 242,
  troponymy 1136, synonymy 1448, hypernymy 2006 — all clear CORE_FLOOR; measured for real here.)

DESIGN DECISIONS FROZEN HERE (byte-preserved from the s186/s193/s196 prep.py where noted; see PREREG.md):
- POS: VERBS (WordNet POS 'v', via nltk). No pooling across POS.
- Frequency band: Lg10WF in [2.0, 4.5]  (byte-identical to s186/s193/s196 — the iconic-outlier cap:
  the very-high-frequency iconic antonym pairs come/go, rise/fall, live/die that J&K/Cao flag as G^2
  outliers sit above Lg10WF 4.5 and are excluded by the band).
- Frequency matching: all chosen relations matched to a COMMON Lg10WF profile (ANTONYMY's FRESH per-bin
  profile — the binding relation, freeze-condition 3), by stratified per-bin sampling (s193/s196 logic).
- N_PER_REL = 130 target (equal, powered ~120-150; PROTOCOL sec.4). Each relation reported at ACHIEVED N.
- Gold = word-form level, aggregated across ALL verb senses of the cue. Relatum single-word, SubTLEX
  Lg10WF>=1.5. RELMIN, VOCAB_MIN, VOCAB_MINLEN, BIN_W, STOPLIST are BYTE-IDENTICAL to s186/s193/s196
  prep.py; the relata() verb branches are the POS-specific parallel (verified in the s198 feasibility.py).
- SEED = 20260709 (fixed). Deterministic; re-running reproduces items.json byte-identical.

Inputs (committed / re-derivable):
- experiments/data/subtlex-us/SUBTLEXus74286wordstextversion.txt (gitignored, sha-pinned
  c5f86f065...; re-fetch via experiments/data/subtlex-us/prep.py — verified this session s199).
- WordNet 3.0 via nltk (resource/wordnet-sense-inventory; BSD-style license verified in-repo).
- the three prior items.json (s186 nouns / s193 fresh nouns / s196 adjectives) — 1,740 cues to exclude.
"""
import csv
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SUBTLEX = os.path.join(HERE, "..", "..", "data", "subtlex-us",
                       "SUBTLEXus74286wordstextversion.txt")
PRIOR_ITEMS = [
    os.path.join(HERE, "..", "2026-07-06-antonymy-shadow-saturation", "items.json"),   # s186 nouns
    os.path.join(HERE, "..", "2026-07-08-relation-recovery-taxonomic-proxy", "items.json"),  # s193 nouns
    os.path.join(HERE, "..", "2026-07-09-adjective-antonymy-replication", "items.json"),  # s196 adjs
]

SEED = 20260709
FMIN, FMAX = 2.0, 4.5      # cue frequency band (Lg10WF) — byte-identical to s186/s193/s196
RELMIN = 1.5               # minimum relatum frequency (Lg10WF) — byte-identical
VOCAB_MIN = 2.0            # candidate-pool floor (Lg10WF) for control vocabulary V — byte-identical
VOCAB_MINLEN = 3           # drop <=2-char forms — byte-identical
N_PER_REL = 130            # target (equal); powered ~120-150 (PROTOCOL sec.4)
BIN_W = 0.25               # frequency-matching bin width — byte-identical
CORE = ["antonymy", "synonymy", "hypernymy", "troponymy", "entailment"]  # 5-relation core (Q1-C)
CAUSE_MIN = 100            # `cause` enters as a 6th IFF achieved matched-N >= this (freeze-condition 5)
CORE_FLOOR = 80            # a core relation below this is reported/flagged, never dropped (condition 3)
DEGEN_MAX_RANGE = 0.50     # B1: non-antonymy mean-depth RANGE < this => depth spread DEGENERATE (H2
                           # under-powered symmetrically). Rationale in PREREG: at within-relation depth
                           # SD ~2 and N~130 one SE ~0.18, so a non-antonymy 4-relation range must clear
                           # ~2.5-3 SE (~0.5) to be a real, above-noise depth test; frozen before any call.

# Closed-class / function-word stoplist — BYTE-IDENTICAL to s186/s193/s196 prep.py.
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
    """VERB relation gold — the POS-specific parallel of the s186/s193 noun relata() (verified byte-
    equivalent to the s198 feasibility.py verb branches). Single-word, SubTLEX Lg10WF>=RELMIN, word-form."""
    out = set()
    if rel == "antonymy":
        for a in lem.antonyms():
            out.add(a.name().replace("_", " ").lower())
    elif rel == "synonymy":
        for l in syn.lemmas():
            if l.name() != lem.name():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "hypernymy":              # the more-general verb (troponymy inverse): whisper->talk
        for s in syn.closure(lambda x: x.hypernyms(), depth=4):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "troponymy":              # more-specific manner (hyponyms): talk->whisper
        for s in syn.closure(lambda x: x.hyponyms(), depth=4):
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "entailment":
        for s in syn.entailments():
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    elif rel == "cause":
        for s in syn.causes():
            for l in s.lemmas():
                out.add(l.name().replace("_", " ").lower())
    return {x for x in out if " " not in x and freq.get(x, 0.0) >= RELMIN}


def trop_depth(cue):
    """PRE-REGISTERED H2 proxy (Q2-A, frozen): min_depth of the cue's FIRST verb synset. Gold-INDEPENDENT
    (a property of the cue, not the answer set). Predicted sign NEGATIVE. Byte-analogous to the noun
    is_a_depth() (only pos="n" -> pos="v")."""
    from nltk.corpus import wordnet as wn
    ss = wn.synsets(cue, pos="v")
    return ss[0].min_depth() if ss else None


def build():
    from nltk.corpus import wordnet as wn
    freq = load_freq()

    # 1,740 prior cue lemmas to EXCLUDE — POS-agnostic surface match (condition 4).
    prior = set()
    for path in PRIOR_ITEMS:
        d = json.load(open(path))
        for r, its in d["items"].items():
            for it in its:
                prior.add(it["cue"])
    print(f"excluding {len(prior)} prior cue lemmas (POS-agnostic surface homograph guard)")

    # Candidate pool V — single-word VERB forms, Lg10WF>=VOCAB_MIN.
    verb_forms = set()
    for syn in wn.all_synsets("v"):
        for lem in syn.lemmas():
            nm = lem.name().replace("_", " ").lower()
            if " " in nm:
                continue
            if len(nm) < VOCAB_MINLEN or nm in STOPLIST or not nm.isalpha():
                continue
            if freq.get(nm, 0.0) >= VOCAB_MIN:
                verb_forms.add(nm)
    vocab = sorted(verb_forms)

    # Eligible fresh cues + aggregated word-form gold per relation (CORE + cause), s186 logic MINUS prior.
    ALL_RELS = CORE + ["cause"]
    cue_gold = {r: {} for r in ALL_RELS}
    for syn in wn.all_synsets("v"):
        for lem in syn.lemmas():
            nm = lem.name().replace("_", " ").lower()
            if " " in nm or nm in prior:          # <-- the freshness / homograph exclusion
                continue
            fw = freq.get(nm)
            if fw is None or not (FMIN <= fw <= FMAX):
                continue
            for r in ALL_RELS:
                g = relata(lem, syn, r, freq)
                if g:
                    cue_gold[r].setdefault(nm, set()).update(g)

    for r in ALL_RELS:
        print(f"  fresh eligible pool {r:11s}: {len(cue_gold[r])}")

    def binof(w):
        return int((freq[w] - FMIN) / BIN_W)

    # Common frequency profile = ANTONYMY's FRESH per-bin counts scaled to N_PER_REL (binding relation).
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

    def sample_rel(r):
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
        if len(chosen) > N_PER_REL:
            chosen = sorted(rng.sample(chosen, N_PER_REL))
        return sorted(chosen)

    # Sample CORE (in fixed order for determinism) then decide `cause` mechanically.
    chosen = {r: sample_rel(r) for r in CORE}
    cause_chosen = sample_rel("cause")
    cause_n = len(cause_chosen)
    include_cause = cause_n >= CAUSE_MIN
    print(f"\nMECHANICAL cause-inclusion (freeze-condition 5): achieved matched-N={cause_n} "
          f">= {CAUSE_MIN}? -> {'INCLUDE (6-point arm)' if include_cause else 'EXCLUDE (5-point arm)'}")
    if include_cause:
        chosen["cause"] = cause_chosen
    rels = CORE + (["cause"] if include_cause else [])

    # CORE thin-relation floor check (freeze-condition 3).
    below_floor = [r for r in CORE if len(chosen[r]) < CORE_FLOOR]
    if below_floor:
        print(f"!! CORE relations below floor {CORE_FLOOR} (reported at achieved N, NOT dropped): {below_floor}")
    else:
        print(f"CORE thin-relation floor OK: all core relations >= {CORE_FLOOR}.")

    items = {}
    profile = {}
    for r in rels:
        ch = chosen[r]
        items[r] = [{"cue": w, "lg10wf": round(freq[w], 4),
                     "trop_depth": trop_depth(w),
                     "gold": sorted(cue_gold[r][w])} for w in ch]
        fws = sorted(freq[w] for w in ch)
        depths = [d for d in (trop_depth(w) for w in ch) if d is not None]
        golds = [len(cue_gold[r][w]) for w in ch]
        profile[r] = {
            "n": len(ch),
            "lg10wf_median": round(fws[len(fws) // 2], 3),
            "lg10wf_min": round(fws[0], 3),
            "lg10wf_max": round(fws[-1], 3),
            "mean_trop_depth": round(sum(depths) / len(depths), 3) if depths else None,
            "n_depth_resolved": len(depths),
            "gold_size_median": sorted(golds)[len(golds) // 2],
            "gold_size_mean": round(sum(golds) / len(golds), 3),
        }

    # ---- B1 (s199 ratifier): NUMERIC degeneracy verdict on the FROZEN sample (pre-recovery) ----
    # B1 as ratified is a floor on the NON-ANTONYMY *CORE-4* mean-depth range {synonymy, hypernymy,
    # troponymy, entailment} — the FIXED backbone, INDEPENDENT of the mechanical `cause` decision (so a
    # shallow conditionally-included `cause` cannot manufacture non-degeneracy). The cause-inclusive
    # range + the full-set SD are recorded too, for transparency, but do NOT drive the verdict.
    mean_depths = {r: profile[r]["mean_trop_depth"] for r in rels}
    CORE_NONANT = [r for r in ["synonymy", "hypernymy", "troponymy", "entailment"] if r in mean_depths]
    core4_vals = [mean_depths[r] for r in CORE_NONANT if mean_depths[r] is not None]
    core4_range = round(max(core4_vals) - min(core4_vals), 4) if len(core4_vals) >= 2 else None
    non_ant_incl_cause = [mean_depths[r] for r in rels if r != "antonymy" and mean_depths[r] is not None]
    non_ant_incl_cause_range = (round(max(non_ant_incl_cause) - min(non_ant_incl_cause), 4)
                                if len(non_ant_incl_cause) >= 2 else None)
    all_vals = [mean_depths[r] for r in rels if mean_depths[r] is not None]
    m = sum(all_vals) / len(all_vals)
    depth_sd = round((sum((v - m) ** 2 for v in all_vals) / len(all_vals)) ** 0.5, 4)
    depth_degenerate = (core4_range is not None and core4_range < DEGEN_MAX_RANGE)
    print(f"\nB1 DEPTH-SPREAD (frozen, pre-recovery): mean depths {mean_depths}")
    print(f"   VERDICT-DRIVING non-antonymy CORE-4 range = {core4_range}  (bound DEGEN_MAX_RANGE={DEGEN_MAX_RANGE})")
    print(f"   [transparency] non-antonymy incl-cause range = {non_ant_incl_cause_range}; full-set depth SD = {depth_sd}")
    print(f"   => DEPTH SPREAD {'DEGENERATE (H2 under-powered SYMMETRICALLY per B1/B2)' if depth_degenerate else 'NON-DEGENERATE (H2 a real test)'}")

    out_items = {
        "seed": SEED, "pos": "verb", "wn_pos": "v", "band": [FMIN, FMAX], "relmin": RELMIN,
        "n_per_rel_target": N_PER_REL, "relations": rels, "core": CORE,
        "cause_included": include_cause, "cause_achieved_n": cause_n, "cause_min": CAUSE_MIN,
        "core_floor": CORE_FLOOR, "core_below_floor": below_floor,
        "excluded_prior_cue_lemmas": len(prior),
        "b1_depth_spread": {
            "mean_trop_depth": mean_depths,
            "verdict_driving_core4_nonant_range": core4_range,
            "core4_nonant_relations": CORE_NONANT,
            "non_antonymy_incl_cause_range": non_ant_incl_cause_range,
            "depth_sd": depth_sd,
            "degen_max_range": DEGEN_MAX_RANGE,
            "depth_degenerate": depth_degenerate,
        },
        "profile": profile, "items": items,
    }
    with open(os.path.join(HERE, "items.json"), "w") as f:
        json.dump(out_items, f, indent=1, sort_keys=True)
    with open(os.path.join(HERE, "vocab.json"), "w") as f:
        json.dump({"vocab_min_lg10wf": VOCAB_MIN, "size": len(vocab), "vocab": vocab}, f)

    # ---- ASSERTIONS: disjointness from all 1,740 prior cues (freeze-condition 4 / anti-cheat) ----
    for r in rels:
        fresh = set(x["cue"] for x in items[r])
        ov = fresh & prior
        assert not ov, f"OVERLAP with prior cues in {r}: {sorted(ov)[:5]}"
    print(f"\nDISJOINTNESS OK: 0 overlap with the {len(prior)} prior cue lemmas, all {len(rels)} relations.")

    print("\nitems.json written. per-relation profile (FRESH verb cues):")
    for r in rels:
        p = profile[r]
        print(f"  {r:11s} n={p['n']:3d}  Lg10WF median={p['lg10wf_median']} "
              f"[{p['lg10wf_min']}, {p['lg10wf_max']}]  mean trop-depth={p['mean_trop_depth']} "
              f"(resolved {p['n_depth_resolved']}/{p['n']})  gold median={p['gold_size_median']}")
    print(f"vocab.json: |V|={len(vocab)} candidate verbs (Lg10WF>={VOCAB_MIN})")


if __name__ == "__main__":
    build()
