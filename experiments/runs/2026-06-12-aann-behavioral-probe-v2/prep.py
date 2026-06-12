#!/usr/bin/env python3
"""AANN behavioral probe v2 — data prep (NO model calls).

Builds, deterministically (seed 20260612), from the gitignored MIT-licensed mirror
experiments/data/aann-public/ (upstream commit c8095a0008cd6538717de5cc937f90ce5944e688):

  human_cell_means.csv   per (adjective x nounclass) cell: n ratings, mean 1-10 rating
                         (computed from ALL 3,600 non-filler Exp-2 ratings)
  human_class_means.csv  per (adjclass x nounclass) cell: n, mean
  stimuli.json           anchored sample (2 items/cell, reconstructed sentences,
                         per-item single human rating), 4-point robustness subset flags,
                         held-out items (frozen adjective list below), Tier-0 forced-choice
                         pairs, per-adjective Zipf frequencies (wordfreq 3.x)

Sentence reconstruction follows aann_experiments.py get_sents_dict() exactly:
  uppercasefirst(f"{first} {a_an(adj)} {adj} {num} {noun}{second}.")
including the upstream template typo "The tourish stayed" (human raters saw it).
"""
import csv, json, random, re, statistics, sys
from collections import defaultdict
from pathlib import Path

from wordfreq import zipf_frequency

HERE = Path(__file__).parent
MIRROR = HERE / ".." / ".." / "data" / "aann-public"
SEED = 20260612

# ---------------------------------------------------------------- frozen held-out list
# Condition 5: frequency resource = wordfreq 3.x Zipf scale ('en'); per-class median
# Zipf within +/-0.5 of the Mahowald class median; none appear in Mahowald's 50.
HELD_OUT = {
    "ambig":    ["stunning", "shocking", "dreadful", "marvelous"],
    "pos":      ["gorgeous", "delightful", "pleasant", "wonderful"],
    "neg":      ["ghastly", "dreary", "revolting", "repulsive"],
    "quant":    ["sizable", "modest", "scant", "colossal"],
    "stubborn": ["huge", "wide", "short", "flat"],
    "color":    ["black", "white", "brown", "pink"],
}
# noun classes each held-out class is probed on (mirrors adj_exp.csv validity: the four
# full classes generalize everywhere -- we take 3 spanning classes; stubborn is valid on
# objects+human; color on objects only)
HELD_OUT_NOUNCLASSES = {
    "ambig": ["temporal", "objects", "distance"],
    "pos": ["temporal", "objects", "distance"],
    "neg": ["temporal", "objects", "distance"],
    "quant": ["temporal", "objects", "distance"],
    "stubborn": ["objects", "human"],
    "color": ["objects"],
}


def uppercasefirst(s):
    return re.sub("([a-zA-Z])", lambda x: x.groups()[0].upper(), s, 1)


def a_an(nextword):
    return "an" if nextword[0] in "aeiou" else "a"


def load_mirror():
    adjrows = list(csv.DictReader(open(MIRROR / "generate_sentence_templates" / "adj_exp.csv")))
    templates = defaultdict(list)
    for r in csv.DictReader(open(MIRROR / "generate_sentence_templates" / "templates_adj.csv")):
        if r["type"]:
            templates[r["type"]].append((r["first"], r["second"]))
    ratings = [r for r in csv.DictReader(open(MIRROR / "mturk_data" / "adjexp_turk.csv"))
               if not r["value"].startswith("filler")]
    return adjrows, templates, ratings


def parse_item_id(value, known_adjs):
    # {adj}-{num}-{noun}-sent-{experiment}-{template}; adj may contain '-' (record-setting)
    for adj in sorted(known_adjs, key=len, reverse=True):
        if value.startswith(adj + "-"):
            rest = value[len(adj) + 1:].split("-")
            num, noun, marker, exp, tpl = rest[0], rest[1], rest[2], rest[3], rest[4]
            assert marker == "sent", value
            return adj, num, noun, exp, int(tpl)
    raise ValueError(value)


def build_sentence(templates, exp, tpl, adj, num, noun):
    first, second = templates[exp][tpl]
    return uppercasefirst(f"{first} {a_an(adj)} {adj} {num} {noun}{second}.".lstrip(" "))


def main():
    rng = random.Random(SEED)
    adjrows, templates, ratings = load_mirror()
    adjclass = {r["word"]: r["info"] for r in adjrows if r["cat"] == "adj"}
    nounrows = [r for r in adjrows if r["cat"] == "noun"]
    nouns_by_class = defaultdict(list)
    for r in nounrows:
        nouns_by_class[r["info"]].append(r["word"])

    # ---- per-item human ratings (each Exp-2 item has exactly one rating)
    items = {}
    for r in ratings:
        adj, num, noun, exp, tpl = parse_item_id(r["value"], adjclass.keys())
        items.setdefault(r["value"], {"adj": adj, "num": num, "noun": noun,
                                      "nounclass": exp, "template": tpl,
                                      "ratings": []})["ratings"].append(int(r["answer"]))

    # ---- human cell means (full data; the yardstick)
    cells = defaultdict(list)
    class_cells = defaultdict(list)
    for it in items.values():
        for v in it["ratings"]:
            cells[(it["adj"], it["nounclass"])].append(v)
            class_cells[(adjclass[it["adj"]], it["nounclass"])].append(v)
    with open(HERE / "human_cell_means.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["adjective", "adjclass", "nounclass", "n", "mean"])
        for (adj, nc), vals in sorted(cells.items()):
            w.writerow([adj, adjclass[adj], nc, len(vals), round(statistics.mean(vals), 4)])
    with open(HERE / "human_class_means.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["adjclass", "nounclass", "n", "mean"])
        for (ac, nc), vals in sorted(class_cells.items()):
            w.writerow([ac, nc, len(vals), round(statistics.mean(vals), 4)])

    # ---- anchored sample: 2 items per (adjective x nounclass) cell, seeded
    by_cell = defaultdict(list)
    for iid, it in items.items():
        by_cell[(it["adj"], it["nounclass"])].append(iid)
    anchored = []
    for cell in sorted(by_cell):
        picks = sorted(by_cell[cell])
        rng.shuffle(picks)
        for iid in picks[:2]:
            it = items[iid]
            anchored.append({
                "id": iid, "arm": "anchored", "adj": it["adj"],
                "adjclass": adjclass[it["adj"]], "num": it["num"], "noun": it["noun"],
                "nounclass": it["nounclass"],
                "sentence": build_sentence(templates, it["nounclass"], it["template"],
                                           it["adj"], it["num"], it["noun"]),
                "human_rating": it["ratings"][0],
                "zipf": zipf_frequency(it["adj"], "en"),
            })
    # 4-point robustness subset: first item of every 4th cell (deterministic, ~100 items)
    for i, s in enumerate(anchored):
        s["robustness_4pt"] = (i % 8 == 0) or (i % 8 == 1)

    # ---- held-out arm (no human ratings by construction)
    held = []
    for ac in sorted(HELD_OUT):
        for j, adj in enumerate(HELD_OUT[ac]):
            for k, nc in enumerate(HELD_OUT_NOUNCLASSES[ac]):
                noun = sorted(nouns_by_class[nc])[(j + k) % len(nouns_by_class[nc])]
                num = ["three", "five"][(j + k) % 2]
                tpl = (j + k) % len(templates[nc])
                held.append({
                    "id": f"heldout-{adj}-{num}-{noun}-{nc}-{tpl}", "arm": "held-out",
                    "adj": adj, "adjclass": ac, "num": num, "noun": noun, "nounclass": nc,
                    "sentence": build_sentence(templates, nc, tpl, adj, num, noun),
                    "human_rating": None, "zipf": zipf_frequency(adj, "en"),
                })

    # ---- Tier-0 forced choice: 6 tuples x 4 degenerate variants (mainexp templates)
    main_templates = {"temporal": ("The family spent", " in London"),
                      "objects": ("She bought", "")}
    tier0_tuples = [("beautiful", "three", "days", "temporal"),
                    ("remarkable", "five", "weeks", "temporal"),
                    ("gruesome", "three", "paintings", "objects"),
                    ("mere", "five", "marbles", "objects"),
                    ("ugly", "three", "desks", "objects"),
                    ("whopping", "five", "months", "temporal")]
    tier0 = []
    for adj, num, noun, nc in tier0_tuples:
        first, second = main_templates[nc]
        aann = uppercasefirst(f"{first} {a_an(adj)} {adj} {num} {noun}{second}.")
        variants = {
            "reverse_mods": uppercasefirst(f"{first} {a_an(num)} {num} {adj} {noun}{second}."),
            "no_mod": uppercasefirst(f"{first} {a_an(num)} {num} {noun}{second}."),
            "no_plural": uppercasefirst(f"{first} {a_an(adj)} {adj} {num} {noun[:-1]}{second}."),
            "no_a": uppercasefirst(f"{first} {adj} {num} {noun}{second}."),
        }
        for vname, vsent in sorted(variants.items()):
            aann_is_a = rng.random() < 0.5
            tier0.append({"id": f"tier0-{adj}-{num}-{noun}-{vname}", "arm": "tier0",
                          "contrast": vname,
                          "A": aann if aann_is_a else vsent,
                          "B": vsent if aann_is_a else aann,
                          "aann_position": "A" if aann_is_a else "B"})

    out = {"seed": SEED, "anchored": anchored, "held_out": held, "tier0": tier0,
           "counts": {"anchored": len(anchored),
                      "robustness_4pt": sum(s["robustness_4pt"] for s in anchored),
                      "held_out": len(held), "tier0": len(tier0)}}
    with open(HERE / "stimuli.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out["counts"], indent=2))
    # frequency-match audit (Condition 5)
    mahowald_by_class = defaultdict(list)
    for w_, c_ in adjclass.items():
        mahowald_by_class[c_].append(zipf_frequency(w_, "en"))
    for ac in sorted(HELD_OUT):
        m = statistics.median(mahowald_by_class[ac])
        h = statistics.median(zipf_frequency(w_, "en") for w_ in HELD_OUT[ac])
        flag = "OK" if abs(m - h) <= 0.5 else "VIOLATION"
        print(f"freq-match {ac}: mahowald median {m:.2f} vs held-out {h:.2f} -> {flag}")
        assert flag == "OK", ac
        assert not set(HELD_OUT[ac]) & set(adjclass), ac


if __name__ == "__main__":
    main()
