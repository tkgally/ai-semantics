#!/usr/bin/env python3
"""AANN temporal held-out widening (v2b) — data prep (NO model calls).

Caveat-2 follow-up to result/aann-behavioral-gradient-v2: the v2 held-out
temporal stratum was ~ -0.2 for all three models over only 4 class-cells x
4 single items each — too thin to read. This prep widens the temporal
stratum WITHIN the same ratified v2 instrument (design
experiments/designs/aann-construction-v2.md; addendum
experiments/designs/aann-temporal-heldout-v2b.md).

Geometry (deterministic, no model calls):
  4 temporal-eligible adjective classes (ambig, neg, pos, quant — the only
  classes valid on temporal nouns in Mahowald's Exp-2 design; the class-cell
  count CANNOT exceed 4) x 10 held-out adjectives each (6 NEW frequency-
  matched + the 4 v2 held-out carryovers) x 2 items per adjective
  = 80 items, rotated over all 5 Mahowald temporal nouns, both nums
  (three/five), and all 3 Exp-2 temporal templates.

Pre-run critic fixes (2026-06-13, GO after fixes) add two arms, embedded here
so the run dir stays self-contained:
  - tier0: the 24 v2 Tier-0 forced-choice pairs, copied VERBATIM from the
    committed v2 stimuli.json (fresh per-run instrument check, blocker 1);
  - robustness_4pt: a fixed 40-item subsample of the 80 main items (one item
    per adjective, class- and template-balanced, seeded deterministic
    selection — rule documented in select_4pt_subset), blocker 2.
The 80 main items are untouched by these additions (verified by diff at
freeze time).

PROVENANCE / MIRROR-INDEPENDENCE. The gitignored upstream mirror
(experiments/data/aann-public/) is NOT required and is absent in this
checkout. Everything is rebuilt from the COMMITTED, FROZEN v2 artifacts:

  ../2026-06-12-aann-behavioral-probe-v2/stimuli.json
      - Mahowald's 50 adjectives + their classes + wordfreq Zipf values
        (frozen 2026-06-12; verified below to match local wordfreq exactly)
      - the 5 temporal nouns of Mahowald's inventory (days, hours, months,
        weeks, years — all appear in the committed anchored sample)
      - the 3 temporal templates, recovered exactly from committed anchored
        sentences (consistency-asserted across all temporal items),
        INCLUDING the upstream template typo "The tourish stayed" (kept
        deliberately: instrument continuity with v2; held-out items make no
        item-level human comparison)
      - the v2 held-out 24 (exclusion list + the 16 temporal carryovers)
  ../2026-06-12-aann-behavioral-probe-v2/human_class_means.csv
      - the human anchored temporal class-cell yardstick (copied into
        stimuli.json verbatim so the run dir is self-contained)

FREQUENCY CONTROL (same procedure as v2, Condition 5): resource = wordfreq
3.x Zipf scale ('en'); statistic = per-class MEDIAN Zipf; requirement = the
new-adjective class median within +/-0.5 of the Mahowald class median
(asserted mechanically below; the combined new+carryover median is asserted
too). wordfreq is REQUIRED; if it is missing this script fails with an
explicit message — Zipf values are never invented or hardcoded. As an extra
guard the committed v2 Zipf values are re-derived from the local wordfreq
and must match EXACTLY (commensurability across wordfreq versions), else
the script aborts.
"""
import csv
import itertools
import json
import random
import re
import statistics
import sys
from pathlib import Path

try:
    from wordfreq import zipf_frequency
except ImportError:
    sys.exit(
        "FATAL: wordfreq is not installed (pip install wordfreq). The frequency "
        "control (Zipf median match, design Condition 5) cannot run without it, "
        "and Zipf values may NOT be invented. Install wordfreq 3.x and re-run."
    )

HERE = Path(__file__).parent
V2 = HERE / ".." / "2026-06-12-aann-behavioral-probe-v2"
SEED = 20260613  # the 80-item build is pure rotation (no random draws); the
                 # 4-point subsample selection uses this seed (one randrange
                 # draw per class, see select_4pt_subset) — fully deterministic

# ------------------------------------------------------------------ frozen lists
# NEW held-out adjectives, 6 per temporal-eligible class. None appear in
# Mahowald's 50 or in the v2 held-out 24 (asserted below). Chosen 2026-06-13,
# before any model call, to satisfy the per-class Zipf median match.
NEW_HELD_OUT = {
    "ambig": ["extraordinary", "unbelievable", "spectacular",
              "phenomenal", "breathtaking", "astounding"],
    "pos":   ["glorious", "magnificent", "elegant",
              "heavenly", "splendid", "exquisite"],
    "neg":   ["depressing", "grim", "vile",
              "gloomy", "wretched", "sickening"],
    "quant": ["ample", "respectable", "lavish",
              "negligible", "towering", "skimpy"],
}
TEMPORAL_CLASSES = sorted(NEW_HELD_OUT)  # ambig, neg, pos, quant
NUMS = ["three", "five"]


def uppercasefirst(s):
    return re.sub("([a-zA-Z])", lambda x: x.groups()[0].upper(), s, 1)


def a_an(nextword):
    return "an" if nextword[0] in "aeiou" else "a"


def load_v2():
    stim = json.load(open(V2 / "stimuli.json"))
    yardstick = {}
    with open(V2 / "human_class_means.csv") as f:
        for r in csv.DictReader(f):
            if r["nounclass"] == "temporal":
                yardstick[r["adjclass"]] = {"n": int(r["n"]), "mean": float(r["mean"])}
    return stim, yardstick


def recover_temporal_templates(stim):
    """Recover the 3 Exp-2 temporal templates exactly from committed anchored
    sentences. Each anchored id ends in -sent-temporal-{tpl}; the sentence was
    built as uppercasefirst(f"{first} {a_an(adj)} {adj} {num} {noun}{second}.").
    Consistency is asserted across every temporal item."""
    templates = {}
    for s in stim["anchored"]:
        if s["nounclass"] != "temporal":
            continue
        tpl = int(s["id"].rsplit("-", 1)[1])
        mid = f"{a_an(s['adj'])} {s['adj']} {s['num']} {s['noun']}"
        sent = s["sentence"]
        idx = sent.lower().find(mid.lower())
        assert idx > 0, (s["id"], sent)  # all temporal templates have a nonempty first
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


def select_4pt_subset(items, seed):
    """Pre-run critic blocker 2: the fixed, pre-declared 40-item 4-point framing
    robustness subsample. SELECTION RULE (deterministic, seeded, documented):

      - exactly ONE of each adjective's 2 items (40 adjectives -> 40 items);
      - class balance is automatic (10 adjectives per class -> 10 items/class);
      - TEMPLATE balance enforced per class: each adjective's pair spans 2 of
        the 3 templates, so a one-per-adjective selection has per-class
        template counts summing to 10; the most balanced multiset possible is
        {3, 3, 4}, and the selection must achieve it in every class;
      - determinism: classes in sorted order; within a class, adjectives in
        the frozen build order (new-6 sorted, then carryover-4 sorted) and each
        adjective's items in build order (k = 0, 1); the 2^10 per-adjective
        item-index tuples are enumerated in lexicographic order, filtered to
        the template-balanced ones, and ONE is picked per class by
        random.Random(seed) via a single rng.randrange draw per class
        (seed = 20260613, the run seed).

    Returns the 40 item ids in class-then-build order. Asserted: 40 ids, one
    per adjective, 10 per class, per-class template counts {3, 3, 4}.
    """
    rng = random.Random(seed)
    by_class = {}
    for it in items:  # insertion order == frozen build order
        by_class.setdefault(it["adjclass"], {}).setdefault(it["adj"], []).append(it)
    chosen = []
    for ac in sorted(by_class):
        pairs = list(by_class[ac].values())
        assert all(len(p) == 2 for p in pairs) and len(pairs) == 10, ac
        balanced = []
        for combo in itertools.product((0, 1), repeat=len(pairs)):
            counts = [0, 0, 0]
            for pair, k in zip(pairs, combo):
                counts[pair[k]["template"]] += 1
            if sorted(counts) == [3, 3, 4]:
                balanced.append(combo)
        combo = balanced[rng.randrange(len(balanced))]
        chosen.extend(pair[k] for pair, k in zip(pairs, combo))
    # mechanical guards
    assert len(chosen) == 40 and len({it["adj"] for it in chosen}) == 40
    for ac in sorted(by_class):
        cls = [it for it in chosen if it["adjclass"] == ac]
        assert len(cls) == 10, ac
        tc = sorted([it["template"] for it in cls].count(t) for t in (0, 1, 2))
        assert tc == [3, 3, 4], (ac, tc)
    return [it["id"] for it in chosen]


def main():
    stim, yardstick = load_v2()
    assert sorted(yardstick) == TEMPORAL_CLASSES, sorted(yardstick)

    # ---- committed Mahowald facts (from the frozen v2 stimuli)
    mahowald_zipf, mahowald_class = {}, {}
    for s in stim["anchored"]:
        mahowald_zipf[s["adj"]] = s["zipf"]
        mahowald_class[s["adj"]] = s["adjclass"]
    assert len(mahowald_zipf) == 50, len(mahowald_zipf)
    temporal_nouns = sorted({s["noun"] for s in stim["anchored"]
                             if s["nounclass"] == "temporal"})
    assert temporal_nouns == ["days", "hours", "months", "weeks", "years"], temporal_nouns
    v2_held = {s["adj"]: s for s in stim["held_out"]}
    assert len(v2_held) == 24, len(v2_held)
    carryover = {ac: sorted(a for a, s in v2_held.items()
                            if s["adjclass"] == ac and ac in NEW_HELD_OUT)
                 for ac in TEMPORAL_CLASSES}
    assert all(len(v) == 4 for v in carryover.values()), carryover

    # ---- commensurability guard: committed v2 Zipf values must match the local
    # wordfreq EXACTLY, else new Zipf values would not be comparable.
    drift = [(a, z, zipf_frequency(a, "en")) for a, z in mahowald_zipf.items()
             if abs(z - zipf_frequency(a, "en")) > 1e-9]
    drift += [(a, s["zipf"], zipf_frequency(a, "en")) for a, s in v2_held.items()
              if abs(s["zipf"] - zipf_frequency(a, "en")) > 1e-9]
    assert not drift, (
        "FATAL: local wordfreq disagrees with the committed v2 Zipf values; "
        f"versions are not commensurable. Mismatches: {drift}"
    )

    templates = recover_temporal_templates(stim)

    # ---- frequency-match audit (Condition 5 procedure, mechanical)
    audit = []
    for ac in TEMPORAL_CLASSES:
        m = statistics.median(z for a, z in mahowald_zipf.items()
                              if mahowald_class[a] == ac)
        new_z = [zipf_frequency(w, "en") for w in NEW_HELD_OUT[ac]]
        comb_z = new_z + [zipf_frequency(w, "en") for w in carryover[ac]]
        nmed, cmed = statistics.median(new_z), statistics.median(comb_z)
        ok = abs(m - nmed) <= 0.5 and abs(m - cmed) <= 0.5
        audit.append({"adjclass": ac, "mahowald_median": round(m, 4),
                      "new6_median": round(nmed, 4),
                      "combined10_median": round(cmed, 4),
                      "pass": ok})
        print(f"freq-match {ac}: mahowald {m:.2f} | new-6 {nmed:.2f} | "
              f"combined-10 {cmed:.2f} -> {'OK' if ok else 'VIOLATION'}")
        assert ok, ac
        # exclusions: never in Mahowald's 50, never (for the NEW list) in the v2 24
        assert not set(NEW_HELD_OUT[ac]) & set(mahowald_zipf), ac
        assert not set(NEW_HELD_OUT[ac]) & set(v2_held), ac

    # ---- items: per class, 10 adjectives (6 new + 4 carryover) x 2 items,
    # pure rotation over nouns/nums/templates (balanced and deterministic)
    items = []
    for ac in TEMPORAL_CLASSES:
        adjs = ([(w, "new") for w in sorted(NEW_HELD_OUT[ac])]
                + [(w, "v2-carryover") for w in carryover[ac]])
        for j, (adj, src) in enumerate(adjs):
            for k in range(2):
                noun = temporal_nouns[(2 * j + k) % 5]
                num = NUMS[(j + k) % 2]
                tpl = (j + k) % 3
                items.append({
                    "id": f"heldout2-{adj}-{num}-{noun}-temporal-{tpl}",
                    "arm": "heldout-temporal", "adj": adj, "adjclass": ac,
                    "source": src, "num": num, "noun": noun,
                    "nounclass": "temporal", "template": tpl,
                    "sentence": build_sentence(templates, tpl, adj, num, noun),
                    "human_rating": None,  # held-out by construction
                    "zipf": zipf_frequency(adj, "en"),
                })

    # ---- mechanical sanity: counts, uniqueness, per-adjective item distinctness
    assert len(items) == 80, len(items)
    assert len({it["id"] for it in items}) == 80
    by_adj = {}
    for it in items:
        by_adj.setdefault(it["adj"], []).append(it)
    assert len(by_adj) == 40
    for adj, pair in by_adj.items():
        assert len(pair) == 2 and pair[0]["noun"] != pair[1]["noun"] \
            and pair[0]["template"] != pair[1]["template"], adj

    # ---- fresh Tier-0 arm (pre-run critic blocker 1): the 24 v2 forced-choice
    # pairs, reused BYTE-IDENTICALLY — copied verbatim (same JSON objects) from
    # the committed v2 stimuli.json so the run dir stays self-contained.
    tier0 = stim["tier0"]
    assert len(tier0) == 24, len(tier0)
    for t in tier0:
        assert set(t) == {"id", "arm", "contrast", "A", "B", "aann_position"}, t
        assert t["aann_position"] in ("A", "B"), t

    # ---- 4-point framing robustness subsample (pre-run critic blocker 2)
    subset_ids = select_4pt_subset(items, SEED)

    out = {
        "seed": SEED,
        "built_from": {
            "v2_stimuli": "../2026-06-12-aann-behavioral-probe-v2/stimuli.json",
            "v2_human_class_means": "../2026-06-12-aann-behavioral-probe-v2/human_class_means.csv",
            "note": ("mirror-independent: rebuilt entirely from the committed, "
                     "frozen v2 artifacts; wordfreq verified to reproduce the "
                     "committed Zipf values exactly"),
        },
        "human_temporal_class_means": yardstick,  # the anchored-half yardstick
        "templates_temporal": {str(k): list(v) for k, v in sorted(templates.items())},
        "freq_audit": audit,
        "items": items,
        "tier0": tier0,  # the 24 v2 pairs, verbatim (fresh Tier-0 arm, critic blocker 1)
        "robustness_4pt": {  # fixed pre-declared subsample (critic blocker 2)
            "rule": ("one item per adjective; class-balanced (10/class, automatic); "
                     "per-class template counts forced to the most-balanced multiset "
                     "{3,3,4}; deterministic + seeded: classes sorted, adjectives in "
                     "frozen build order, 2^10 item-index tuples enumerated "
                     "lexicographically, one balanced tuple drawn per class with "
                     "random.Random(seed)"),
            "seed": SEED,
            "ids": subset_ids,
        },
        "counts": {
            "class_cells": len(TEMPORAL_CLASSES),
            "adjectives_per_class": 10,
            "new_adjectives": sum(len(v) for v in NEW_HELD_OUT.values()),
            "carryover_adjectives": sum(len(v) for v in carryover.values()),
            "items_per_adjective": 2,
            "items": len(items),
            "tier0_pairs": len(tier0),
            "robustness_4pt_items": len(subset_ids),
            "calls_per_model": len(items) + len(tier0) + len(subset_ids),
            "calls_total": (len(items) + len(tier0) + len(subset_ids)) * 3,
        },
    }
    with open(HERE / "stimuli.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out["counts"], indent=2))
    print("wrote stimuli.json")


if __name__ == "__main__":
    main()
