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
import json
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
SEED = 20260613  # recorded for provenance; the build below is pure rotation,
                 # deterministic with no random draws

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
        "counts": {
            "class_cells": len(TEMPORAL_CLASSES),
            "adjectives_per_class": 10,
            "new_adjectives": sum(len(v) for v in NEW_HELD_OUT.values()),
            "carryover_adjectives": sum(len(v) for v in carryover.values()),
            "items_per_adjective": 2,
            "items": len(items),
            "calls_per_model": len(items),
            "calls_total": len(items) * 3,
        },
    }
    with open(HERE / "stimuli.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out["counts"], indent=2))
    print("wrote stimuli.json")


if __name__ == "__main__":
    main()
