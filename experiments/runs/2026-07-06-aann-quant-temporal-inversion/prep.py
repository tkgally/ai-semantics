#!/usr/bin/env python3
"""AANN quant×temporal inversion — class-vs-lexical widening probe: DATA PREP (NO model calls).

Freezes the item set (stimuli.json) for the probe operationalizing
open-question/aann-quant-temporal-inversion, per the design
experiments/designs/aann-quant-temporal-inversion-v1.md and the ratified decision
wiki/decisions/resolved/aann-quant-temporal-inversion-design.md
(s189 ADOPT-WITH-CHANGES: Q1-C human-N-gated / Q2-B monotone-primary / Q3-A).

THE QUESTION. Is the one panel-wide AANN model-vs-human inversion cell — QUANTITY adjectives x
TEMPORAL nouns ("a scant three days": humans rate HIGHEST of 4 adjective classes, every model
LOWEST) — a property of the whole quantity class or a few lexical items? Widen the quantity-modifier
set (K=20) and the temporal frame; count how the per-modifier margin below the non-quant baseline is
distributed.

THE CALLING INSTRUMENT IS BYTE-FROZEN (reused from v2b: probe.py prompts/parsing/settings — P100
0-100 acceptability, P4 4-point framing, PT0 Tier-0 forced choice, temperature 0, per-slot
max_tokens, gemini reasoning minimal). ONLY the item set (this file) and the analyze.py §6 verdict
logic are new (frozen in PREREG, self-tested before any call). See design S10.

BINDING FREEZE CONDITIONS honored here (from the ratified decision):
  B1  every modifier gets the IDENTICAL noun x numeral x template frame (balanced Latin rotation),
      asserted per-modifier: 10 items = 5 nouns x 2 numerals, template = cell_index % 3 (identical
      across modifiers -> per-modifier noun/numeral/template counts identical). No noun-mix confound.
  S1  human-N feasibility gate: report each Mahowald quant modifier's TEMPORAL rating-N from the
      recloned adjexp_turk.csv; a modifier enters Arm 1's per-modifier human leg iff N >= 10; meta-
      gate: if < 7/10 clear, Arm 1's per-modifier leg is dropped (recorded). [Gate PASSES: all 10.]
  S2  the "tourish" template-2 spelling is Mahowald's OWN (templates_adj.csv / aann_sentences.txt
      read "The tourish stayed ..."), so his MTurk raters saw "tourish"; faithfulness KEEPS it (as
      v2b did). A template-2-exclusion sensitivity recompute is gate-bearing in analyze.py.
  S4  inversion is defined against MIN(non-quant class mean), not the pooled mean (analyze.py).
  S7  Arm 2 retains large-magnitude modifiers (reversing the design's drop) and marks each modifier
      genuinely-new vs v2b-carryover; the genuinely-new subset is reported separately (analyze.py).
  S8  the exact K=20 is enumerated below with a documented source + quantity-polarity per modifier.
  S9  per-modifier Zipf is recorded; a per-modifier Zipf partial enters the read (analyze.py). NOTE
      the design's inherited +/-0.5 class-median Zipf MATCH is deliberately NOT enforced on the
      widened set: it would exclude exactly the natural high-frequency quantity modifiers (good 6.12,
      full 5.54, whole 5.46) the class-vs-lexical test needs. Frequency is controlled by the partial,
      not by exclusion; this deviation is surfaced in the PREREG.
  Q3-A the non-quant baseline is fresh Mahowald-own ambig/pos/neg temporal reference rated the SAME
      occasion (60 reference items); N1: a STRUCTURAL four-class reproduction on a new occasion
      (~4 adjectives/class), not the committed full-class cells.

PROVENANCE. Structure (templates, tier0 pairs, class labels) rebuilt from the COMMITTED frozen v2
artifacts (mirror-independent). The Arm-1 human per-modifier means come from the recloned pinned
Mahowald mirror (MIT, commit c8095a0008cd6538717de5cc937f90ce5944e688) at
experiments/data/aann-public/mturk_data/adjexp_turk.csv — reclone before running this file. Human
ratings are NEVER invented; only ratings present in the resource enter, and Arm-2 items carry no
human rating by construction.
"""
import csv
import json
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

try:
    from wordfreq import zipf_frequency
except ImportError:
    sys.exit("FATAL: wordfreq not installed (pip install wordfreq). Zipf values may NOT be invented.")

HERE = Path(__file__).parent
V2 = HERE / ".." / "2026-06-12-aann-behavioral-probe-v2"
ADJEXP = HERE / ".." / ".." / "data" / "aann-public" / "mturk_data" / "adjexp_turk.csv"
SEED = 20260706

NOUNS = ["days", "hours", "months", "weeks", "years"]   # committed v2 temporal-noun order
NUMS = ["three", "five"]
HUMAN_N_FLOOR = 10          # S1: per-modifier temporal rating-N floor for Arm 1's per-modifier leg
META_GATE_MIN = 7           # S1: >= this many of 10 Mahowald quant modifiers must clear the floor

# --------------------------------------------------------------- K=20 quant modifiers (S8)
# Each: (modifier, arm, polarity, source). arm1 = Mahowald-attested (anchored, human means);
# arm2 = widened internal-contrast. polarity: "small" (diminishing / "only X") vs "large"
# (augmentative). source documents provenance so the list cannot be curated post hoc.
QUANT_MODIFIERS = [
    # --- Arm 1: Mahowald 2023 Table 1 `quant` class (all carry temporal human ratings) ---
    ("mere",           "arm1", "small", "mahowald-2023-table1-quant"),
    ("staggering",     "arm1", "large", "mahowald-2023-table1-quant"),
    ("whopping",       "arm1", "large", "mahowald-2023-table1-quant"),
    ("hefty",          "arm1", "large", "mahowald-2023-table1-quant"),
    ("paltry",         "arm1", "small", "mahowald-2023-table1-quant"),
    ("meager",         "arm1", "small", "mahowald-2023-table1-quant"),
    ("extra",          "arm1", "large", "mahowald-2023-table1-quant"),
    ("measly",         "arm1", "small", "mahowald-2023-table1-quant"),
    ("substantial",    "arm1", "large", "mahowald-2023-table1-quant"),
    ("record-setting", "arm1", "large", "mahowald-2023-table1-quant"),
    # --- Arm 2a: genuinely-new (neither Mahowald nor v2b held-out); OQ/handoff widening targets ---
    ("good",  "arm2-new", "large", "oq-handoff-widening-target"),
    ("full",  "arm2-new", "large", "oq-handoff-widening-target"),
    ("whole", "arm2-new", "large", "oq-handoff-widening-target"),
    ("solid", "arm2-new", "large", "oq-handoff-widening-target"),
    ("bare",  "arm2-new", "small", "oq-handoff-widening-target"),
    # --- Arm 2b: v2b held-out quant carryover (continuity; retains large-magnitude per S7) ---
    ("scant",    "arm2-v2b", "small", "v2b-heldout-quant"),
    ("skimpy",   "arm2-v2b", "small", "v2b-heldout-quant"),
    ("ample",    "arm2-v2b", "large", "v2b-heldout-quant"),
    ("towering", "arm2-v2b", "large", "v2b-heldout-quant"),
    ("colossal", "arm2-v2b", "large", "v2b-heldout-quant"),
]

# --------------------------------------------------------------- non-quant reference (Q3-A)
# 4 adjectives x 3 non-quant classes, from the committed v2 temporal class labels (high rating-N).
# Rated the SAME occasion to define each model's non-quant temporal baseline B_m and reproduce the
# four-class comparison (N1: structural, ~4/class, not the committed full-class cells).
REFERENCE = {
    "ambig": ["astonishing", "impressive", "remarkable", "surprising"],
    "pos":   ["beautiful", "charming", "lovely", "soothing"],
    "neg":   ["disgusting", "hideous", "ugly", "uninviting"],
}


def uppercasefirst(s):
    return re.sub("([a-zA-Z])", lambda x: x.groups()[0].upper(), s, 1)


def a_an(nextword):
    return "an" if nextword[0] in "aeiou" else "a"


def recover_temporal_templates(stim):
    """Recover the 3 Exp-2 temporal templates exactly from committed anchored sentences (identical
    procedure to v2b). Keeps Mahowald's 'tourish' spelling (S2 finding)."""
    templates = {}
    for s in stim["anchored"]:
        if s["nounclass"] != "temporal":
            continue
        tpl = int(s["id"].rsplit("-", 1)[1])
        mid = f"{a_an(s['adj'])} {s['adj']} {s['num']} {s['noun']}"
        sent = s["sentence"]
        idx = sent.lower().find(mid.lower())
        assert idx > 0, (s["id"], sent)
        first = sent[:idx].rstrip(" ")
        second = sent[idx + len(mid):]
        assert second.endswith("."), sent
        second = second[:-1]
        if tpl in templates:
            assert templates[tpl] == (first, second), (tpl, templates[tpl], (first, second))
        else:
            templates[tpl] = (first, second)
    assert sorted(templates) == [0, 1, 2], sorted(templates)
    return templates


def build_sentence(templates, tpl, adj, num, noun):
    first, second = templates[tpl]
    return uppercasefirst(f"{first} {a_an(adj)} {adj} {num} {noun}{second}.".lstrip(" "))


def human_temporal_means():
    """Per-adjective temporal acceptability mean + N from the recloned adjexp_turk.csv.
    Item id form: {adjective}-{numeral}-{noun}-sent-{nounclass}-{template}; the rating is `answer`
    (1-10). Returns {adj: {"n": n, "mean": mean}}. Never invents a rating."""
    if not ADJEXP.exists():
        sys.exit(f"FATAL: {ADJEXP} not found — reclone the pinned Mahowald mirror (MIT, commit "
                 "c8095a0008cd6538717de5cc937f90ce5944e688) before freezing. Human means may NOT "
                 "be invented.")
    by_adj = defaultdict(list)
    for r in csv.DictReader(open(ADJEXP)):
        v = r["value"]
        if "-sent-" not in v:
            continue
        left, right = v.split("-sent-")
        if right.split("-")[0] != "temporal":
            continue
        lt = left.split("-")               # adj-num-noun ; adj may be hyphenated (record-setting)
        adj = "-".join(lt[:-2])
        try:
            by_adj[adj].append(float(r["answer"]))
        except ValueError:
            continue
    return {a: {"n": len(v), "mean": round(statistics.mean(v), 4)} for a, v in by_adj.items()}


def main():
    stim = json.load(open(V2 / "stimuli.json"))

    # committed human class means (the human side of the four-class comparison)
    human_class = {}
    with open(V2 / "human_class_means.csv") as f:
        for r in csv.DictReader(f):
            if r["nounclass"] == "temporal":
                human_class[r["adjclass"]] = {"n": int(r["n"]), "mean": float(r["mean"])}
    assert sorted(human_class) == ["ambig", "neg", "pos", "quant"], sorted(human_class)

    # verify committed temporal-noun order (mirror-independent structural check)
    committed_nouns = sorted({s["noun"] for s in stim["anchored"] if s["nounclass"] == "temporal"})
    assert committed_nouns == NOUNS, (committed_nouns, NOUNS)

    templates = recover_temporal_templates(stim)
    tourish_tpl = [t for t, (f, _) in templates.items() if "tourish" in f.lower()]
    assert len(tourish_tpl) == 1, ("expected exactly one 'tourish' template", templates)
    tourish_tpl = tourish_tpl[0]

    hmeans = human_temporal_means()

    # ---- S1 human-N feasibility gate (report per Mahowald quant modifier; floor 10)
    arm1_mods = [m for (m, arm, *_ ) in QUANT_MODIFIERS if arm == "arm1"]
    assert len(arm1_mods) == 10
    s1_gate = []
    for m in arm1_mods:
        rec = hmeans.get(m, {"n": 0, "mean": None})
        s1_gate.append({"modifier": m, "temporal_rating_n": rec["n"],
                        "human_temporal_mean": rec["mean"],
                        "enters_per_modifier_leg": rec["n"] >= HUMAN_N_FLOOR})
    n_clear = sum(g["enters_per_modifier_leg"] for g in s1_gate)
    arm1_per_modifier_leg = n_clear >= META_GATE_MIN
    print(f"S1 human-N gate: {n_clear}/10 Mahowald quant modifiers clear N>={HUMAN_N_FLOOR} "
          f"-> per-modifier leg {'ENABLED' if arm1_per_modifier_leg else 'DROPPED (C degrades to B)'}")
    for g in s1_gate:
        print(f"   {g['modifier']:16s} N={g['temporal_rating_n']:3d} mean={g['human_temporal_mean']} "
              f"{'clear' if g['enters_per_modifier_leg'] else 'BELOW-FLOOR'}")

    # ---- quant items: 20 modifiers x 10 items (B1 identical balanced frame)
    # 10 cells = 5 nouns x 2 numerals; cell index c = noun_i*2 + num_j (0..9); template = c % 3.
    # Every modifier sees the identical (noun, num, template) multiset -> no noun-mix confound.
    items = []
    for (mod, arm, polarity, source) in QUANT_MODIFIERS:
        zipf = zipf_frequency(mod, "en")
        assert zipf > 0, f"zipf 0 for {mod}"
        for noun_i, noun in enumerate(NOUNS):
            for num_j, num in enumerate(NUMS):
                c = noun_i * 2 + num_j
                tpl = c % 3
                items.append({
                    "id": f"quant-{mod}-{num}-{noun}-temporal-{tpl}",
                    "arm": arm, "adj": mod, "adjclass": "quant", "polarity": polarity,
                    "source": source, "num": num, "noun": noun, "nounclass": "temporal",
                    "template": tpl, "cell": c,
                    "sentence": build_sentence(templates, tpl, mod, num, noun),
                    "human_rating": None, "zipf": zipf,
                })
    n_quant = len(items)
    assert n_quant == 20 * 10 == 200, n_quant

    # ---- non-quant reference items: 4 adj x 3 classes x 5 items (one per noun; num/tpl rotated)
    for cls in ["ambig", "pos", "neg"]:
        for adj in REFERENCE[cls]:
            zipf = zipf_frequency(adj, "en")
            for noun_i, noun in enumerate(NOUNS):
                num = NUMS[noun_i % 2]
                tpl = noun_i % 3
                items.append({
                    "id": f"ref-{adj}-{num}-{noun}-temporal-{tpl}",
                    "arm": "reference", "adj": adj, "adjclass": cls, "polarity": None,
                    "source": "committed-v2-temporal-class-label", "num": num, "noun": noun,
                    "nounclass": "temporal", "template": tpl, "cell": noun_i,
                    "sentence": build_sentence(templates, tpl, adj, num, noun),
                    "human_rating": None, "zipf": zipf,
                })
    n_ref = len(items) - n_quant
    assert n_ref == 12 * 5 == 60, n_ref

    # ---- mechanical B1 assertions: every quant modifier has the identical frame multiset
    by_mod = defaultdict(list)
    for it in items:
        if it["adjclass"] == "quant":
            by_mod[it["adj"]].append(it)
    assert len(by_mod) == 20
    ref_frame = None
    for mod, its in by_mod.items():
        assert len(its) == 10, (mod, len(its))
        frame = sorted((it["noun"], it["num"], it["template"]) for it in its)
        # per-modifier noun/num counts identical
        nouns_c = sorted([it["noun"] for it in its].count(n) for n in NOUNS)
        nums_c = sorted([it["num"] for it in its].count(u) for u in NUMS)
        assert nouns_c == [2, 2, 2, 2, 2], (mod, nouns_c)
        assert nums_c == [5, 5], (mod, nums_c)
        if ref_frame is None:
            ref_frame = frame
        assert frame == ref_frame, (mod, "frame differs -> B1 violated")
    assert len({it["id"] for it in items}) == len(items), "duplicate ids"

    # ---- per-modifier Zipf record (S9) — descriptive; the +/-0.5 MATCH is NOT enforced (see header)
    zipf_by_mod = {m: round(zipf_frequency(m, "en"), 4) for (m, *_ ) in QUANT_MODIFIERS}
    mahowald_quant_zipf_median = round(statistics.median(zipf_by_mod[m] for m in arm1_mods), 4)

    # ---- Tier-0 arm: the 24 v2 forced-choice pairs, verbatim (fresh per-occasion instrument check)
    tier0 = stim["tier0"]
    assert len(tier0) == 24, len(tier0)
    for t in tier0:
        assert set(t) == {"id", "arm", "contrast", "A", "B", "aann_position"}, t

    # ---- 4-point framing-robustness subsample (40 items): 2 template-spread quant items per
    # modifier (cells 0 and 5 = days/three/tpl0 and weeks/five/tpl2), deterministic, on the arm
    # that carries the verdict. Tests whether the quant 0-100 read survives the 4-point framing.
    subset_ids = []
    for (mod, *_ ) in QUANT_MODIFIERS:
        for c in (0, 5):
            match = [it["id"] for it in by_mod[mod] if it["cell"] == c]
            assert len(match) == 1, (mod, c, match)
            subset_ids.append(match[0])
    assert len(subset_ids) == 40 and len(set(subset_ids)) == 40, len(subset_ids)

    out = {
        "seed": SEED,
        "design": "aann-quant-temporal-inversion-v1",
        "decision": "resolved/aann-quant-temporal-inversion-design (s189 ADOPT-WITH-CHANGES)",
        "built_from": {
            "v2_stimuli": "../2026-06-12-aann-behavioral-probe-v2/stimuli.json",
            "v2_human_class_means": "../2026-06-12-aann-behavioral-probe-v2/human_class_means.csv",
            "arm1_human_means": "../../data/aann-public/mturk_data/adjexp_turk.csv "
                                "(pinned mirror c8095a0008cd6538717de5cc937f90ce5944e688, MIT)",
        },
        "templates_temporal": {str(k): list(v) for k, v in sorted(templates.items())},
        "tourish_template": tourish_tpl,   # S2: gate-bearing exclusion recompute keys on this
        "nouns": NOUNS, "numerals": NUMS,
        "human_class_means_temporal": human_class,          # committed (four-class human side)
        "min_nonquant_human_class": min(
            (c for k, c in human_class.items() if k != "quant"),
            key=lambda c: c["mean"]),                       # neg 7.5673 — descriptive reference
        "arm1_human_per_modifier": {g["modifier"]: g for g in s1_gate},
        "s1_gate": {"floor": HUMAN_N_FLOOR, "meta_gate_min": META_GATE_MIN,
                    "n_clear": n_clear, "per_modifier_leg_enabled": arm1_per_modifier_leg},
        "quant_modifiers": [{"modifier": m, "arm": a, "polarity": p, "source": s,
                             "zipf": zipf_by_mod[m]} for (m, a, p, s) in QUANT_MODIFIERS],
        "mahowald_quant_zipf_median": mahowald_quant_zipf_median,
        "reference_adjectives": REFERENCE,
        "items": items,
        "tier0": tier0,
        "robustness_4pt": {
            "rule": ("2 template-spread quant items per modifier (cells 0 and 5 = days/three/tpl0 "
                     "and weeks/five/tpl2); 40 items on the quant arm (the verdict-bearing arm)"),
            "seed": SEED, "ids": subset_ids,
        },
        "counts": {
            "quant_modifiers": 20, "items_per_quant_modifier": 10, "quant_items": n_quant,
            "reference_adjectives": 12, "items_per_reference_adjective": 5, "reference_items": n_ref,
            "main_items": len(items), "tier0_pairs": len(tier0),
            "robustness_4pt_items": len(subset_ids),
            "calls_per_model": len(items) + len(tier0) + len(subset_ids),
            "calls_total": (len(items) + len(tier0) + len(subset_ids)) * 3,
        },
    }
    with open(HERE / "stimuli.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out["counts"], indent=2))
    print(f"min(non-quant) human class = neg {out['min_nonquant_human_class']['mean']}; "
          f"quant human class = {human_class['quant']['mean']}")
    print("wrote stimuli.json")


if __name__ == "__main__":
    main()
