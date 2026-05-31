"""Build + FREEZE the lexical-v3 item set from a homonymy-enriched WiC NOUN subset (2026-05-31).

Operationalizes design/lexical-polysemy-homonymy-v3 (status: ready; Tom decision 3a ratified the
binary WiC anchor + the homonymy-enriched contrast). The instrument is the SAME ratified graded
panel as v1 (gate Q1: DURel 4-point + 0-100), reused verbatim by probe.py. This script only builds
the frozen item table; NO model calls happen here.

STRATIFICATION (gate Q2). The polysemy/homonymy split is a DESIGN-ADDED layer WiC does not carry.
It lives in `stratification.csv` (lemma,pos,stratum,n_etymons,key_roots,source_note), authored BY
HAND from etymological sources (Wiktionary "Etymology N" sections / Etymonline distinct headwords),
each HOMONYM call backed by a quoted distinct-origin statement, applied BLIND to the model ratings
and frozen (sha256) before any probe call. NOTE (recorded in the README + result): the preferred
WordNet lexicographer-file rule was EVALUATED (explore.py) and found to OVER-CALL homonymy ~6:1
(it labels make/break/head as homonyms because WordNet's fine sense granularity scatters related
senses across lexnames), so the gate's etymology AND-condition is load-bearing and is used as the
classifier here; the WordNet structural signal is recorded as a supporting cue only. Restricted to
NOUNS (homonymy is cleanest and most concrete for nouns; matches resource/wordnet-sense-inventory).

GRANULARITY. WiC does not expose the underlying sense ids per item, so the homonym/polyseme label is
applied at the LEMMA level (a homonym lemma's different-sense (F) items are MORE LIKELY cross-etymon
than a polyseme lemma's, but some homonym-F items may be within-etymon polysemy splits). This is the
lemma-level fallback the design names; stated plainly in the result.

LICENCE / DATA HANDLING (mirrors DWUG posture; WiC is CC BY-NC 4.0). Does NOT commit the corpus
example sentences. Downloads WiC into experiments/data/wic/ (gitignored), verifies sha256; writes a
committable manifest (WiC id + lemma + pos + gold + stratum + lexical-overlap covariate, NO
sentences) and a gitignored fulltext.jsonl the probe reads. Freeze = sha256(manifest)+sha256(strat).

Run: python3 build_items.py   (downloads WiC on first run; no API)
"""
import csv
import hashlib
import os
import re
import urllib.request
import zipfile
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
WIC_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "data", "wic"))
ZIP_PATH = os.path.join(WIC_DIR, "WiC_dataset.zip")
WIC_URL = "https://pilehvar.github.io/wic/package/WiC_dataset.zip"
EXPECTED_ZIP_SHA256 = "f1a2fb67d903c5b9b1180f1035d4228f7c0254e8f5f868d556235457046bd4b2"

STRAT = os.path.join(HERE, "stratification.csv")   # committed; the frozen design layer
MANIFEST = os.path.join(HERE, "manifest.csv")      # committed (ids/gold/stratum/overlap; NO text)
FULLTEXT = os.path.join(HERE, "fulltext.jsonl")    # gitignored, local-only (the probe reads it)

STOP = set("a an the of to in on at for and or but with from by as is are was were be been "
           "being this that these those it its he she they we you i his her their our your my "
           "him them us not no so if then than too very can could would should will shall may "
           "might must do does did have has had which who whom whose what when where why how "
           "into onto over under up down out off about again more most some any all each "
           "s t re ve ll d m".split())


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_wic():
    if not os.path.exists(ZIP_PATH):
        os.makedirs(WIC_DIR, exist_ok=True)
        print(f"downloading WiC -> {ZIP_PATH}")
        urllib.request.urlretrieve(WIC_URL, ZIP_PATH)
    h = sha256_file(ZIP_PATH)
    assert h == EXPECTED_ZIP_SHA256, f"WiC sha256 mismatch! got {h}"
    extract = os.path.join(WIC_DIR, "extracted")
    if not os.path.isdir(extract):
        with zipfile.ZipFile(ZIP_PATH) as z:
            z.extractall(extract)
    return extract, h


def load_wic(extract):
    """Deterministic load. Stable id = '<split>-<5digit line index>'."""
    items = []
    for split in ("train", "dev", "test"):
        data_f = gold_f = None
        for root, _, files in os.walk(extract):
            for fn in files:
                if fn == f"{split}.data.txt":
                    data_f = os.path.join(root, fn)
                if fn == f"{split}.gold.txt":
                    gold_f = os.path.join(root, fn)
        with open(data_f, encoding="utf-8") as df, open(gold_f, encoding="utf-8") as gf:
            for i, (dl, gl) in enumerate(zip(df, gf)):
                p = dl.rstrip("\n").split("\t")
                if len(p) < 5:
                    continue
                tw, pos, idx, c1, c2 = p[0], p[1], p[2], p[3], p[4]
                i1, i2 = idx.split("-")
                items.append({"wic_id": f"{split}-{i:05d}", "target": tw, "pos": pos,
                              "idx1": int(i1), "idx2": int(i2), "ctx1": c1, "ctx2": c2,
                              "gold": gl.strip(), "split": split})
    return items


def target_surface(ctx, idx):
    toks = ctx.split(" ")
    if 0 <= idx < len(toks):
        return toks[idx]
    return ""


def content_tokens(ctx, target_surf):
    toks = re.findall(r"[a-z]+", ctx.lower())
    tgt = set(re.findall(r"[a-z]+", target_surf.lower()))
    return set(t for t in toks if t not in STOP and t not in tgt and len(t) > 1)


def overlap(c1, t1, c2, t2):
    a, b = content_tokens(c1, t1), content_tokens(c2, t2)
    if not a or not b:
        return 0.0, 0.0
    inter = len(a & b)
    return round(inter / len(a | b), 4), round(2 * inter / (len(a) + len(b)), 4)


def main():
    extract, zip_sha = ensure_wic()
    items = load_wic(extract)

    strat_rows = list(csv.DictReader(open(STRAT)))
    strat = {(r["lemma"].strip(), r["pos"].strip()): r["stratum"].strip().upper()
             for r in strat_rows}
    selected_strata = ("HOMONYM", "POLYSEME")

    # gather all noun items for stratified lemmas
    selected = []
    for it in items:
        key = (it["target"], it["pos"])
        s = strat.get(key)
        if s not in selected_strata:
            continue
        surf1 = target_surface(it["ctx1"], it["idx1"])
        surf2 = target_surface(it["ctx2"], it["idx2"])
        jac, f1 = overlap(it["ctx1"], surf1, it["ctx2"], surf2)
        selected.append({**it, "stratum": s, "surf1": surf1, "surf2": surf2,
                         "overlap_jaccard": jac, "overlap_tokenf1": f1})

    # stable item ids: stratum-gold-runningindex, sorted deterministically
    selected.sort(key=lambda d: (d["stratum"], d["gold"], d["target"], d["wic_id"]))
    for i, c in enumerate(selected):
        c["item_id"] = f"v3-{c['stratum'][0]}{c['gold']}-{i:03d}"

    # counts report
    by = defaultdict(lambda: {"T": 0, "F": 0, "lemmas": set()})
    for c in selected:
        by[c["stratum"]][c["gold"]] += 1
        by[c["stratum"]]["lemmas"].add(c["target"])

    man_cols = ["item_id", "wic_id", "lemma", "pos", "gold", "stratum",
                "overlap_jaccard", "overlap_tokenf1"]
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=man_cols)
        w.writeheader()
        for c in selected:
            w.writerow({"item_id": c["item_id"], "wic_id": c["wic_id"],
                        "lemma": c["target"], "pos": c["pos"], "gold": c["gold"],
                        "stratum": c["stratum"], "overlap_jaccard": c["overlap_jaccard"],
                        "overlap_tokenf1": c["overlap_tokenf1"]})

    import json
    with open(FULLTEXT, "w", encoding="utf-8") as f:
        for c in selected:
            f.write(json.dumps({
                "item_id": c["item_id"], "wic_id": c["wic_id"], "lemma": c["target"],
                "pos": c["pos"], "gold": c["gold"], "stratum": c["stratum"],
                "ctx1": c["ctx1"], "idx1": c["idx1"], "surf1": c["surf1"],
                "ctx2": c["ctx2"], "idx2": c["idx2"], "surf2": c["surf2"],
            }) + "\n")

    man_sha = sha256_file(MANIFEST)
    strat_sha = sha256_file(STRAT)
    print(f"WiC archive sha256: {zip_sha}")
    print(f"selected {len(selected)} items")
    for s in selected_strata:
        d = by[s]
        print(f"  {s:9s} T={d['T']:3d} F={d['F']:3d}  ({len(d['lemmas'])} lemmas: "
              f"{', '.join(sorted(d['lemmas']))})")
    print(f"MANIFEST sha256 (FREEZE): {man_sha}")
    print(f"STRATIFICATION sha256 (FREEZE): {strat_sha}")


if __name__ == "__main__":
    main()
