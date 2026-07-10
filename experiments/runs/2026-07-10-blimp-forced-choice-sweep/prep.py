#!/usr/bin/env python3
"""prep.py — build the FROZEN instrument for the BLiMP forced-choice sweep (A3b, s205).

RATIFIED s205: Q1-B / Q2-A / Q3-A (decisions/resolved/blimp-forced-choice-sweep-design).
This script realizes Q1-B by the MAXIMAL DEFENSIBLE WHOLE-CATEGORY rule (F6-sharp + the ratification
vote's mechanical anti-cherry-pick condition): select EVERY paradigm in the on-axis `linguistics_term`
categories; assign each to a depth stratum by a STRUCTURAL locality rule; NO within-category / within-
stratum hand-picking; publish excluded categories with structural reasons. Selection references ONLY
BLiMP's own structural metadata (paradigm_meta.json = each file's linguistics_term/field), NEVER the
human-agreement values (those are joined afterward only as the anchor). Human-agreement-BLIND by
construction.

Outputs (committed as the frozen instrument, BEFORE any model call):
  - items.json       : the frozen 2AFC instrument (per paradigm: stratum, human_agreement anchor, sha256
                       of the full source file, and the seeded N-pair subsample).
  - paradigms.json   : the selection manifest (selected 40 + excluded categories with reasons + the
                       stratum map + per-paradigm human anchor + sha256 pins).
Full 1,000-pair .jsonl files are streamed, sha256-pinned, sampled, and NOT committed (recipe-not-corpus,
CC-BY; only the frozen 30-pair subsample travels in items.json).
"""
import csv, hashlib, json, os, random, urllib.request, urllib.error, sys
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / ".." / ".." / "data" / "blimp"
RAWFILES = HERE / "paradigm_files"      # gitignored; full .jsonl land here transiently
RAWFILES.mkdir(exist_ok=True)
BASE = "https://raw.githubusercontent.com/alexwarstadt/blimp/master/data/{}.jsonl"

SEED = 20260710
N_PER_PARADIGM = 30                      # 40 paradigms x 30 pairs x 2 orders x 3 models = 7,200 calls
F4_FLOOR = 0.60                          # human-agreement floor for the reading-2 accuracy strata

# ---- The MECHANICAL structural selection rule (frozen; human-agreement-blind) --------------------
# On-axis categories = the locality-of-dependency cline this design operationalizes. Each maps to a
# depth stratum. subject_verb_agreement is split by BLiMP's own `distractor_` marker (which ENCODES an
# intervener between controller and verb) — a structural criterion, not a hand-pick.
#
#   stratum key -> (rank, human-readable)
STRATA = {"local": (1, "shallow-local (adjacent agreement, n-gram/local-window detectable)"),
          "medium": (2, "medium (agreement across an intervener)"),
          "scope": (3, "deep-scope (c-command polarity/quantifier licensing, non-adjacent)"),
          "island": (4, "deep-structural (long-distance filler-gap / island constraints)")}

# category -> stratum, for whole-category assignment. subject_verb_agreement handled specially below.
CATEGORY_STRATUM = {
    "determiner_noun_agreement": "local",
    "npi_licensing": "scope",
    "quantifiers": "scope",
    "island_effects": "island",
    "filler_gap_dependency": "island",
}
# The reading-2 depth contrast: shallow = {local}; deep = {scope, island}. medium reported separately.
SHALLOW = {"local"}
DEEP = {"scope", "island"}

# Off-axis categories excluded with STRUCTURAL reasons (published, F6).
EXCLUDED_REASONS = {
    "binding": "Binding-domain / coreference (principle A): a c-command+domain referential-dependency "
               "constraint on a different axis than morphological agreement / polarity licensing / "
               "filler-gap extraction — not on the locality-of-agreement/extraction cline.",
    "anaphor_agreement": "Reflexive gender/number agreement is a binding-domain phenomenon (same "
               "rationale as binding); excluded to keep the agreement strata about controller-target "
               "morphological agreement only.",
    "argument_structure": "Verb argument-realization well-formedness (causative/inchoative/transitive/"
               "passive/drop-argument): a lexical-semantic selection phenomenon, not a locality-graded "
               "structural dependency.",
    "s-selection": "Semantic selectional restriction (animacy): lexical-semantic, off the "
               "structural-locality axis.",
    "control_raising": "Control/raising A-movement + PRO: a distinct movement/interpretation axis; "
               "several items are existential-there raising that would confound with the there-quantifier "
               "items.",
    "irregular_forms": "Morphological irregularity (past-participle forms): a morphological-lexical "
               "contrast, not a structural dependency.",
    "ellipsis": "Ellipsis (n-bar) licensing: a distinct anaphoric/deletion phenomenon; only 2 paradigms.",
}


def stratum_for(uid, category):
    if category == "subject_verb_agreement":
        return "medium" if uid.startswith("distractor_") else "local"
    return CATEGORY_STRATUM.get(category)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch_full(uid):
    dest = RAWFILES / f"{uid}.jsonl"
    if not dest.exists():
        for attempt in range(4):
            try:
                urllib.request.urlretrieve(BASE.format(uid), dest)
                break
            except Exception as e:  # noqa: BLE001
                if attempt == 3:
                    raise
    return dest


def main():
    # human anchor (joined AFTER selection; never used to select)
    human = {}
    with open(DATA / "human_validation_summary.csv") as f:
        for row in csv.DictReader(f):
            human[row["Condition"]] = float(row["total_mean"])
    meta = json.load(open(HERE / "paradigm_meta.json"))
    meta = {k: v for k, v in meta.items() if v}   # drop the 2 CSV rows whose data file 404'd

    # SELECT: every fetchable paradigm in an on-axis category.
    onaxis_cats = set(CATEGORY_STRATUM) | {"subject_verb_agreement"}
    selected, excluded = [], []
    for uid, m in sorted(meta.items()):
        cat = m["linguistics_term"]
        if cat in onaxis_cats:
            st = stratum_for(uid, cat)
            selected.append((uid, cat, st))
        else:
            excluded.append((uid, cat))

    # Build the frozen subsamples.
    paradigms, items = [], {}
    for uid, cat, st in selected:
        assert uid in human, f"selected paradigm {uid} has no human-agreement row"
        path = fetch_full(uid)
        sha = sha256_file(path)
        pairs_all = [json.loads(l) for l in open(path) if l.strip()]
        assert len(pairs_all) == 1000, f"{uid}: expected 1000 pairs, got {len(pairs_all)}"
        rng = random.Random(int(hashlib.sha256(f"{SEED}-{uid}".encode()).hexdigest()[:12], 16))
        sample = rng.sample(pairs_all, N_PER_PARADIGM)
        pl = [{"pairID": str(p.get("pairID")), "good": p["sentence_good"], "bad": p["sentence_bad"]}
              for p in sample]
        h = human[uid]
        paradigms.append({"uid": uid, "category": cat, "stratum": st, "stratum_rank": STRATA[st][0],
                          "human_agreement": h, "f4_pass": h >= F4_FLOOR,
                          "sha256_full": sha, "n_pairs": len(pl)})
        items[uid] = pl

    # order-flip note: probe.py builds BOTH presentation orders per pair at run time (Q2-A).
    manifest = {
        "seed": SEED, "n_per_paradigm": N_PER_PARADIGM, "f4_floor": F4_FLOOR,
        "n_selected": len(selected), "n_calls_expected": len(selected) * N_PER_PARADIGM * 2 * 3,
        "selection_rule": ("Q1-B via the maximal defensible WHOLE-CATEGORY rule: every paradigm in the "
                           "on-axis linguistics_term categories (determiner_noun_agreement; the local + "
                           "distractor split of subject_verb_agreement; npi_licensing; quantifiers; "
                           "island_effects; filler_gap_dependency); no within-category hand-picking; "
                           "selection references only BLiMP's own structural metadata, human-agreement-"
                           "blind. subject_verb_agreement split by the structural `distractor_` marker."),
        "strata": {k: {"rank": v[0], "desc": v[1]} for k, v in STRATA.items()},
        "shallow_strata": sorted(SHALLOW), "deep_strata": sorted(DEEP),
        "paradigms": paradigms,
        "excluded_categories": {cat: EXCLUDED_REASONS.get(cat, "off-axis")
                                for cat in sorted({c for _, c in excluded})},
        "excluded_paradigms": sorted(f"{u} [{c}]" for u, c in excluded),
        "note_404": ["coordinate_structure_constraint_subject_extraction (human 0.514)",
                     "wh_questions_object_gap_long_distance (human 0.47)"],
        "note_404_reason": ("2 human-validation-CSV rows have NO data file on master (404) — excluded "
                            "for data-availability (structural), NOT for their human-agreement values; "
                            "both happen to be low-agreement, flagged as a limitation (their absence "
                            "removes 2 of the hardest human points, mildly conservative for reading 1)."),
    }
    json.dump({"manifest": manifest}, open(HERE / "paradigms.json", "w"), indent=1)
    json.dump({"seed": SEED, "n_per_paradigm": N_PER_PARADIGM, "paradigms": paradigms, "items": items},
              open(HERE / "items.json", "w"), indent=1)

    # freeze-time summary (printed; the numbers go verbatim into PREREG)
    from collections import Counter
    byst = Counter(p["stratum"] for p in paradigms)
    print(f"SELECTED {len(selected)} paradigms; expected calls {manifest['n_calls_expected']}")
    for st in ("local", "medium", "scope", "island"):
        ps = [p for p in paradigms if p["stratum"] == st]
        hs = [p["human_agreement"] for p in ps]
        print(f"  [{st}] n={byst[st]:2d}  human {min(hs):.3f}-{max(hs):.3f} (mean {sum(hs)/len(hs):.3f})")
    below = [p["uid"] for p in paradigms if not p["f4_pass"]]
    print(f"F4 (<{F4_FLOOR}) excluded from reading-2 accuracy strata: {below or 'NONE'}")
    print(f"EXCLUDED categories: {sorted(manifest['excluded_categories'])}")
    hh = [p["human_agreement"] for p in paradigms]
    print(f"human-agreement range over selected: {min(hh):.3f}-{max(hh):.3f}")


if __name__ == "__main__":
    main()
