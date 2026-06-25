#!/usr/bin/env python3
"""VWSD grounding-headroom probe v2 — runnable harness (DAY-1 text-only build).

Implements the frozen design experiments/designs/vwsd-grounding-headroom-v2.md
(ratified gate decisions/resolved/vwsd-grounding-headroom-dv-v2, ADOPT-DEFAULT:
Option-B visual-form descriptor separability baseline / Option-A floor calibration /
Option-C leak-audit covariate / N=120 stratified draw, >=15 per stratum / raised
claude image max_tokens). Anchor: resource/vwsd-semeval-2023 (463 EN gold test).

DAY-1 = the text-only condition-(b) FREEZE, complete BEFORE any image arm:
  descriptor-full  Option-B visual-form descriptors over the 200-pool's unique images
                   (gemini, low detail) -> frozen/descriptors.json  [the ~$3.4 spend]
  leak-full        Option-C held-out gpt referent-recovery leak audit over the 200 gold
                   descriptors -> adds leak{} to frozen/descriptors.json
  text-full        descriptor-based SELECTION arm over the 200 pool items x 3 models
                   -> raw/pool_text.json  (the per-item separability covariate sep_i)
Then draw_stratified.py freezes the N=120 run set + raw/text.json, and:
  floor-full       Option-A bare-index-label calibration arm over the 120 x 3 models
                   -> raw/floor.json  (must sit at/near chance 0.10)

NO image / distract arm runs on day 1 (that is day 2+, gated by a fresh pre-run critic
GO against the observed sep_i / leak_i distributions — design condition e).

IMAGES ARE OUT OF GIT (redistribution unconfirmed; resource/vwsd-semeval-2023 License).
Read at runtime from $VWSD_IMAGES (local dir of resized EN candidates), never committed.
The annotation overlay (queries+gold) and the descriptors ARE committed.

Usage:
  python3 run.py descriptor-preflight   # describe 8 pool images, print + per-image cost
  python3 run.py descriptor-full        # describe all unique pool images -> frozen/descriptors.json (resumable, cost-guarded)
  python3 run.py leak-preflight         # leak-audit 4 gold items, print
  python3 run.py leak-full              # leak audit over 200 gold -> frozen/descriptors.json:leak
  python3 run.py text-preflight         # 2 pool items x panel, descriptor arm, cost
  python3 run.py text-full              # descriptor arm, 200 pool items -> raw/pool_text.json
  python3 run.py floor-preflight        # 2 draw items x panel, index-label arm, cost
  python3 run.py floor-full             # Option-A arm, frozen 120 -> raw/floor.json
"""
import base64, json, os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}
IMAGES_DIR = os.environ.get("VWSD_IMAGES", "")  # local, gitignored
POOL = os.path.join(HERE, "frozen", "pool_items.json")        # seeded 200-item pool
RUN_ITEMS = os.path.join(HERE, "frozen", "run_items.json")    # stratified 120 (draw_stratified.py)
DESC = os.path.join(HERE, "frozen", "descriptors.json")       # frozen descriptors + leak audit
RAWDIR = os.path.join(HERE, "raw")

# Hard spend guard for the resumable descriptor pass (day-1's only large spend).
# Day-1 estimate ~$3.4 descriptors + ~$0.3 other; abort well below the $5 daily cap.
DESC_ABORT_USD = float(os.environ.get("DESC_ABORT_USD", "4.20"))

# ----- Option-B visual-form descriptor policy (design B.1, verbatim load-bearing constraint) -----
DESC_SYS = (
    "You describe ONLY the visual form of an image. Output one short neutral phrase naming "
    "its shapes, colours, textures, spatial layout, and number of elements. Do NOT name, "
    "label, or identify what the depicted object, scene, creature, or concept IS, and do NOT "
    "use any noun that names the referent or its category. Write what an eye sees, not what a "
    "mind recognises. Example of the REQUIRED style: \"a dense cluster of small round yellowish "
    "particles.\" Example of the FORBIDDEN style (names the referent): \"a pile of mustard seeds.\""
)
DESC_USER = ("Describe ONLY the visual form of this image in one short neutral phrase "
             "(shapes, colours, textures, layout, count). Do NOT name what it depicts.")

# ----- selection arms -----
SEL_SYS_TEXT = ("You are disambiguating a word's intended meaning. You will see a target "
                "word, a short phrase using it, and ten short descriptions of candidate "
                "images numbered 1 to 10. Choose the single description that best matches "
                "the intended meaning of the target word in the phrase. Answer with only "
                "the number, 1 to 10.")
FLOOR_SYS = ("You are disambiguating a word's intended meaning. You will see a target word, "
             "a short phrase using it, and ten candidates numbered 1 to 10 given only as bare "
             "labels with no description. Choose the single candidate that best matches the "
             "intended meaning of the target word in the phrase. Answer with only the number, "
             "1 to 10.")

# ----- leak audit (Option C): held-out gpt recovers the referent from the gold descriptor -----
LEAK_SYS = ("You are shown one short description of the visual form of an image, with no other "
            "information. Infer what real-world object, creature, scene, plant, or concept the "
            "image most likely depicts. Answer with a short noun phrase only (no sentence).")

# ---------- data ----------
def load_pool():
    return json.load(open(POOL))

def load_run_items():
    return json.load(open(RUN_ITEMS))

def load_desc():
    return json.load(open(DESC)) if os.path.exists(DESC) else {
        "policy": DESC_SYS, "generator": MODELS["gemini"], "descriptors": {}, "leak": {}}

def img_path(name):
    return os.path.join(IMAGES_DIR, name)

def data_uri(name):
    p = img_path(name)
    b = open(p, "rb").read()
    ext = "png" if name.lower().endswith(".png") else "jpeg"
    return f"data:image/{ext};base64," + base64.b64encode(b).decode()

def parse_pick(txt, n=10):
    if not txt:
        return None
    s = txt.strip().strip("*.# ")
    if re.fullmatch(r"\d+", s) and 1 <= int(s) <= n:
        return int(s)
    cands = [int(x) for x in re.findall(r"\b(\d+)\b", txt) if 1 <= int(x) <= n]
    return cands[-1] if cands else None

# ---------- descriptor generation ----------
def describe(name):
    r = call(MODELS["gemini"], DESC_SYS, DESC_USER,
             images=[{"url": data_uri(name), "detail": "low"}],
             max_tokens=64, reasoning={"effort": "minimal"})
    desc = (r.get("content") or "").strip().replace("\n", " ")
    return desc, r

# ---------- leak scoring (deterministic, auditable; validity is later-ratified, design B.4) ----------
STOP = {"a", "an", "the", "of", "in", "on", "with", "and", "or", "to", "for", "by", "at",
        "image", "picture", "photo", "photograph", "depicting", "showing", "shows", "likely",
        "probably", "some", "kind", "type", "object", "scene", "thing", "view", "close", "up"}

def lemma(tok):
    t = re.sub(r"[^a-z]", "", tok.lower())
    if len(t) > 3 and t.endswith("s"):
        t = t[:-1]
    return t

def toks(s):
    return {lemma(t) for t in s.split() if lemma(t) and lemma(t) not in STOP}

def leak_score(word, phrase, recovered):
    """0 = no referent leak, 1 = partial (recovers a trigger/context token), 2 = high
    (recovers the target word itself). Compares the recovered referent to the gold
    referent label (target word + phrase). Deterministic; raw guess stored for re-grade."""
    wl = {lemma(w) for w in word.split() if lemma(w)}
    pl = toks(phrase) - wl
    rl = toks(recovered)
    if wl & rl:
        return 2, sorted(wl & rl)
    if pl & rl:
        return 1, sorted(pl & rl)
    return 0, []

# ---------- selection ----------
def text_user(it, desc):
    lines = "\n".join(f"{i+1}. {desc['descriptors'].get(name, '(no description)')}"
                      for i, name in enumerate(it["candidates"]))
    return (f"Target word: {it['word']}\nPhrase: {it['phrase']}\n"
            f"Candidate image descriptions:\n{lines}\n\n"
            "Which description best matches the intended meaning of the target word? "
            "Answer with only the number, 1 to 10.")

def floor_user(it):
    lines = "\n".join(f"{i+1}. image {i+1}" for i in range(len(it["candidates"])))
    return (f"Target word: {it['word']}\nPhrase: {it['phrase']}\n"
            f"Candidates:\n{lines}\n\n"
            "Which candidate best matches the intended meaning of the target word? "
            "Answer with only the number, 1 to 10.")

def run_text(it, desc, mname):
    r = call(MODELS[mname], SEL_SYS_TEXT, text_user(it, desc), max_tokens=16,
             reasoning={"effort": "minimal"} if mname == "gemini" else None)
    pick = parse_pick(r.get("content"))
    return {"arm": "text", "item_id": it["id"], "word": it["word"], "model": mname,
            "gold_idx": it["gold_idx"], "pick": pick,
            "correct": (pick == it["gold_idx"]) if pick else None,
            "raw": r.get("content"), "usage": r.get("usage", {}), "error": r.get("error")}

def run_floor(it, mname):
    r = call(MODELS[mname], FLOOR_SYS, floor_user(it), max_tokens=16,
             reasoning={"effort": "minimal"} if mname == "gemini" else None)
    pick = parse_pick(r.get("content"))
    return {"arm": "floor", "item_id": it["id"], "word": it["word"], "model": mname,
            "gold_idx": it["gold_idx"], "pick": pick,
            "correct": (pick == it["gold_idx"]) if pick else None,
            "raw": r.get("content"), "usage": r.get("usage", {}), "error": r.get("error")}

# ---------- helpers ----------
def _cost(recs, label):
    tot, have, miss = billed_cost([recs])
    print(f"\n{label}: {len(recs)} calls, billed=${tot:.5f} (have={have} missing={miss})")
    return tot

def _freeze(obj, path):
    json.dump(obj, open(path, "w"), indent=2, sort_keys=True)
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def _save_raw(recs, name):
    os.makedirs(RAWDIR, exist_ok=True)
    p = os.path.join(RAWDIR, name)
    json.dump(recs, open(p, "w"), indent=2)
    return p, hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---------- drivers ----------
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""

    if mode == "descriptor-preflight":
        pool = load_pool()
        names = sorted({c for it in pool for c in it["candidates"]})[:8]
        recs = []
        for nm in names:
            d, r = describe(nm)
            recs.append(r)
            print(f"  {nm}: {d!r}")
        per = _cost(recs, "DESCRIPTOR-PREFLIGHT") / max(len(recs), 1)
        uniq = len({c for it in pool for c in it["candidates"]})
        print(f"  per-image ${per:.5f}; extrapolated {uniq} pool images ~ ${per*uniq:.3f}")

    elif mode == "descriptor-full":
        pool = load_pool()
        names = sorted({c for it in pool for c in it["candidates"]})
        desc = load_desc()
        todo = [n for n in names if n not in desc["descriptors"]]
        print(f"describing {len(todo)} of {len(names)} unique pool images "
              f"({len(names)-len(todo)} already done)...")
        allrecs = []
        # resume cost ledger if present
        ledger = os.path.join(RAWDIR, "descriptor_calls.json")
        if os.path.exists(ledger):
            allrecs = json.load(open(ledger))
        running = billed_cost([allrecs])[0]
        for i, nm in enumerate(todo):
            d, r = describe(nm)
            desc["descriptors"][nm] = d
            allrecs.append(r)
            running += (r.get("usage") or {}).get("cost") or 0.0
            if i < 8 or i % 100 == 0:
                print(f"  [{i+1}/{len(todo)}] {nm}: {d!r}  (running ${running:.4f})")
            if i % 50 == 0 or i == len(todo) - 1:  # checkpoint
                _freeze(desc, DESC)
                os.makedirs(RAWDIR, exist_ok=True)
                json.dump(allrecs, open(ledger, "w"), indent=2)
            if running > DESC_ABORT_USD:
                print(f"  !! ABORT: running billed ${running:.4f} > ${DESC_ABORT_USD} cap. "
                      f"Checkpointed; rerun to resume.")
                break
        sha = _freeze(desc, DESC)
        json.dump(allrecs, open(ledger, "w"), indent=2)
        _cost(allrecs, "DESCRIPTOR-FULL (cumulative)")
        print(f"  descriptors={len(desc['descriptors'])}/{len(names)}  {DESC} sha256={sha}")

    elif mode in ("leak-preflight", "leak-full"):
        pool = load_pool()
        desc = load_desc()
        if not desc["descriptors"]:
            sys.exit("descriptors not generated yet; run descriptor-full first")
        items = pool[:4] if mode == "leak-preflight" else pool
        recs = []
        for it in items:
            gold = it["gold_name"]
            gdesc = desc["descriptors"].get(gold, "")
            r = call(MODELS["gpt"], LEAK_SYS,
                     f"Description: {gdesc}\nWhat does this image most likely depict? "
                     f"Answer with a short noun phrase only.", max_tokens=32)
            rec = (r.get("content") or "").strip().replace("\n", " ")
            score, matched = leak_score(it["word"], it["phrase"], rec)
            desc["leak"][it["id"]] = {
                "gold_name": gold, "word": it["word"], "phrase": it["phrase"],
                "gold_descriptor": gdesc, "recovered": rec,
                "leak_score": score, "matched_tokens": matched}
            recs.append(r)
            if mode == "leak-preflight" or len(recs) % 50 == 0:
                print(f"  {it['id']} [{it['word']}/{it['phrase']}] -> {rec!r}  leak={score} {matched}")
        if mode == "leak-full":
            sha = _freeze(desc, DESC)
            _, csha = _save_raw(recs, "leak_calls.json")
            dist = {s: sum(1 for v in desc["leak"].values() if v["leak_score"] == s) for s in (0, 1, 2)}
            _cost(recs, "LEAK-FULL")
            print(f"  leak distribution (0/1/2): {dist}  {DESC} sha256={sha}")
        else:
            _cost(recs, "LEAK-PREFLIGHT")

    elif mode in ("text-preflight", "text-full"):
        pool = load_pool()
        desc = load_desc()
        if not desc["descriptors"]:
            sys.exit("descriptors not generated yet; run descriptor-full first")
        items = pool[:2] if mode == "text-preflight" else pool
        recs = []
        for it in items:
            for mname in MODELS:
                rec = run_text(it, desc, mname)
                recs.append(rec)
            done = [r for r in recs if r["item_id"] == it["id"]]
            if mode == "text-preflight" or len(recs) % 60 == 0:
                print(f"  {it['id']:8s} " + " ".join(f"{r['model']}:{r['pick']}" for r in done))
        if mode == "text-full":
            p, sha = _save_raw(recs, "pool_text.json")
            nf = sum(1 for r in recs if r["pick"] is None)
            _cost(recs, "TEXT-FULL")
            print(f"  wrote {p}  sha256={sha}  parse-fails={nf}")
        else:
            per = _cost(recs, "TEXT-PREFLIGHT") / max(len(recs), 1)
            print(f"  per-(item,model) ${per:.5f}")

    elif mode in ("floor-preflight", "floor-full"):
        items = load_run_items()
        items = items[:2] if mode == "floor-preflight" else items
        recs = []
        for it in items:
            for mname in MODELS:
                rec = run_floor(it, mname)
                recs.append(rec)
            done = [r for r in recs if r["item_id"] == it["id"]]
            if mode == "floor-preflight" or len(recs) % 60 == 0:
                print(f"  {it['id']:8s} " + " ".join(f"{r['model']}:{r['pick']}" for r in done))
        if mode == "floor-full":
            p, sha = _save_raw(recs, "floor.json")
            nf = sum(1 for r in recs if r["pick"] is None)
            acc = sum(1 for r in recs if r["correct"]) / max(len(recs), 1)
            _cost(recs, "FLOOR-FULL")
            print(f"  wrote {p}  sha256={sha}  parse-fails={nf}  pooled-acc={acc:.3f} (target ~0.10)")
        else:
            per = _cost(recs, "FLOOR-PREFLIGHT") / max(len(recs), 1)
            print(f"  per-(item,model) ${per:.5f}")
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
