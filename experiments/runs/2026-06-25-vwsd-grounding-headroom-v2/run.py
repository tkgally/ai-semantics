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

DAY-2+ (the IMAGE then DISTRACT arms; session 112 ran the IMAGE arm). These are gated by the
s108 pre-run-critic GO + a fresh UTC day; condition (d) raises claude image max_tokens 16 -> 512.
Both are resumable + day-splittable: IMG_LIMIT=N caps fresh items per sub-batch, IMG_ABORT_USD
hard-stops on THIS sub-batch's new spend (so each stays under the $2.50 single-run prudence flag):
  image-full     IMAGE arm over the frozen 120 x 3 -> raw/image.json   [session 112: DONE]
  distract-full  DISTRACT word-ablated control -> raw/distract.json    [NOT yet run; null reported FIRST]

Usage:
  python3 run.py descriptor-preflight   # describe 8 pool images, print + per-image cost
  python3 run.py descriptor-full        # describe all unique pool images -> frozen/descriptors.json (resumable, cost-guarded)
  python3 run.py leak-preflight         # leak-audit 4 gold items, print
  python3 run.py leak-full              # leak audit over 200 gold -> frozen/descriptors.json:leak
  python3 run.py text-preflight         # 2 pool items x panel, descriptor arm, cost
  python3 run.py text-full              # descriptor arm, 200 pool items -> raw/pool_text.json
  python3 run.py floor-preflight        # 2 draw items x panel, index-label arm, cost
  python3 run.py floor-full             # Option-A arm, frozen 120 -> raw/floor.json
  python3 run.py image-preflight        # 2 draw items x panel, IMAGE arm, re-measured per-call cost (condition d)
  IMG_LIMIT=60 python3 run.py image-full     # IMAGE arm sub-batch (resumable) -> raw/image.json
  python3 run.py distract-preflight     # 2 draw items x panel, DISTRACT arm, cost
  IMG_LIMIT=60 python3 run.py distract-full  # DISTRACT arm sub-batch (resumable) -> raw/distract.json
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
# ----- IMAGE arm (the main grounding arm) and DISTRACT (word-ablated) control (design B.4 arms 4-5) -----
# Prompts mirror v1 verbatim (run dir 2026-06-24-vwsd-grounding-headroom-v1) so the only
# operationalization change is condition (d): claude image-arm max_tokens raised 16 -> 512.
SEL_SYS_IMAGE = ("You are disambiguating a word's intended meaning. You will see a target "
                 "word, a short phrase using it, and ten candidate images numbered 1 to 10 "
                 "in order. Choose the single image that best matches the intended meaning "
                 "of the target word in the phrase. Answer with only the number, 1 to 10.")
DISTRACT_SYS = ("You will see ten images numbered 1 to 10 in order. With no other "
                "information, choose the single image that is the most prototypical, "
                "canonical, everyday depiction of a clearly recognizable common concept. "
                "Answer with only the number, 1 to 10.")
DISTRACT_USER = ("The ten candidate images follow, in order 1 to 10. Which one is the most "
                 "prototypical, canonical, everyday image? Answer with only the number, 1 to 10.")
# Condition (d): claude image-arm max_tokens raised 16 -> 512 so reasoning-then-answer is not
# truncated before a parseable 1-10 selection; gpt/gemini keep a generous selection budget too.
IMG_MAXTOK = {"claude": 512, "gpt": 512, "gemini": 512}
# Day-split guards (charter §8 / design Budget condition f): per-sub-batch item cap + hard
# cost abort, so each image/distract sub-batch stays under the $2.50 single-run prudence flag
# and the running UTC tally stays under $5. Resume across UTC days by re-running (skips done items).
IMG_ABORT_USD = float(os.environ.get("IMG_ABORT_USD", "2.40"))
IMG_LIMIT = int(os.environ.get("IMG_LIMIT", "0"))  # 0 = no per-batch item cap (full arm)

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

def image_user(it):
    return (f"Target word: {it['word']}\nPhrase: {it['phrase']}\n"
            "The ten candidate images follow, in order 1 to 10. Which image best matches "
            "the intended meaning of the target word? Answer with only the number, 1 to 10.")

def run_image(it, mname, arm):
    """IMAGE / DISTRACT arm. arm='image' shows the word+phrase; arm='distract' ablates them.
    parse_pick takes the FINAL emitted index (design condition d: with raised max_tokens the
    model may reason aloud before the number)."""
    imgs = [{"url": data_uri(name), "detail": "low"} for name in it["candidates"]]
    sys_p = SEL_SYS_IMAGE if arm == "image" else DISTRACT_SYS
    usr = image_user(it) if arm == "image" else DISTRACT_USER
    r = call(MODELS[mname], sys_p, usr, images=imgs, max_tokens=IMG_MAXTOK[mname],
             reasoning={"effort": "minimal"} if mname == "gemini" else None)
    pick = parse_pick(r.get("content"))
    return {"arm": arm, "item_id": it["id"], "word": it["word"], "model": mname,
            "gold_idx": it["gold_idx"], "pick": pick,
            "correct": (pick == it["gold_idx"]) if pick else None,
            "raw": r.get("content"), "usage": r.get("usage", {}), "error": r.get("error")}

def _run_image_arm(arm):
    """Resumable, day-splittable driver for the IMAGE / DISTRACT arm over the frozen 120.
    Accumulates into raw/<arm>.json; skips items already complete (all 3 models present);
    stops after IMG_LIMIT fresh items (0 = no cap) or when the running billed cost crosses
    IMG_ABORT_USD. Re-run on a later UTC day to finish the remaining items."""
    if not IMAGES_DIR or not os.path.isdir(IMAGES_DIR):
        sys.exit(f"$VWSD_IMAGES not set / not a dir: {IMAGES_DIR!r}")
    items = load_run_items()
    out = os.path.join(RAWDIR, f"{arm}.json")
    recs = json.load(open(out)) if os.path.exists(out) else []
    done = {iid for iid in {r["item_id"] for r in recs}
            if sum(1 for r in recs if r["item_id"] == iid) >= len(MODELS)}
    todo = [it for it in items if it["id"] not in done]
    if IMG_LIMIT > 0:
        todo = todo[:IMG_LIMIT]
    prior = billed_cost([recs])[0]
    print(f"{arm.upper()} arm: {len(done)}/{len(items)} items already complete; "
          f"running this batch over {len(todo)} fresh items (prior billed ${prior:.4f}, "
          f"this-batch abort ${IMG_ABORT_USD} of NEW spend).")
    ran, batch_spend = 0, 0.0  # IMG_ABORT_USD guards THIS sub-batch's new spend only (day-split)
    for it in todo:
        batch = [run_image(it, m, arm) for m in MODELS]
        recs.extend(batch)
        batch_spend += billed_cost([batch])[0]
        ran += 1
        json.dump(recs, open(out, "w"), indent=2)  # checkpoint every item
        picks = " ".join(f"{r['model']}:{r['pick']}" for r in batch)
        print(f"  {it['id']:8s} {picks}   (this-batch ${batch_spend:.4f}, cum ${prior+batch_spend:.4f}, "
              f"{ran} items this batch)")
        if batch_spend > IMG_ABORT_USD:
            print(f"  !! ABORT: this-batch billed ${batch_spend:.4f} > ${IMG_ABORT_USD}. "
                  f"Checkpointed; rerun (next sub-batch) to resume.")
            break
    sha = hashlib.sha256(open(out, "rb").read()).hexdigest()
    ndone = len({r["item_id"] for r in recs
                 if sum(1 for x in recs if x["item_id"] == r["item_id"]) >= len(MODELS)})
    nf = sum(1 for r in recs if r["pick"] is None)
    _cost(recs, f"{arm.upper()} (cumulative)")
    print(f"  wrote {out}  sha256={sha}  items-complete={ndone}/{len(items)}  parse-fails={nf}")

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

    elif mode in ("image-preflight", "distract-preflight"):
        arm = "image" if mode.startswith("image") else "distract"
        if not IMAGES_DIR or not os.path.isdir(IMAGES_DIR):
            sys.exit(f"$VWSD_IMAGES not set / not a dir: {IMAGES_DIR!r}")
        items = load_run_items()[:2]
        recs, per_model = [], {m: [0.0, 0] for m in MODELS}
        for it in items:
            for mname in MODELS:
                rec = run_image(it, mname, arm)
                recs.append(rec)
                c = (rec["usage"] or {}).get("cost") or 0.0
                per_model[mname][0] += c
                per_model[mname][1] += 1
                print(f"  {it['id']:8s} {mname:7s} -> pick={rec['pick']} correct={rec['correct']} "
                      f"raw_len={len(rec['raw'] or '')} ${c:.5f}")
        per = _cost(recs, mode.upper()) / max(len(recs), 1)
        print(f"  per-(item,model) ${per:.5f}  (condition d: re-measured claude cost = "
              f"${per_model['claude'][0]/max(per_model['claude'][1],1):.5f}/call)")
        for m in MODELS:
            print(f"    {m:7s}: ${per_model[m][0]/max(per_model[m][1],1):.5f}/call")
        # full-arm extrapolation over the frozen 120
        print(f"  extrapolated {arm} arm (120 items x 3 models): "
              f"~${per*360:.3f} (vs design placeholder ~$6.9)")

    elif mode in ("image-full", "distract-full"):
        _run_image_arm("image" if mode.startswith("image") else "distract")

    else:
        print(__doc__)

if __name__ == "__main__":
    main()
