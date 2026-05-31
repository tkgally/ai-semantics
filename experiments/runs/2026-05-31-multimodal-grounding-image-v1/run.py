#!/usr/bin/env python3
"""Run the multimodal-grounding-image-v1 probe.

Grid: 12 items x {text-only, image+text} x {durel-4pt, scale-0-100} x 3 models.
The user prompt is BYTE-IDENTICAL across conditions (modality is the only toggle);
a fixed clause in the SYSTEM prompt (constant across conditions) tells the model that
IF images are attached they depict Context 1 / Context 2 in order.

Usage:
  python3 run.py liveness   # synthetic-image plumbing check (3 calls, ~$0.001)
  python3 run.py preflight  # 1 item full cell (~12 calls), prints billed cost
  python3 run.py full       # full grid, writes raw/results.json
"""
import base64, csv, json, os, re, sys, hashlib, io

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}

SYSTEM = ("You are a careful annotator of word meaning. You will see a single target word "
          "used in two different contexts, and you rate how related the two uses of that word "
          "are in meaning. If two images are attached, they depict the referent in Context 1 "
          "and Context 2 respectively, in that order, and you may use them. Answer with only the "
          "number requested, nothing else.")

FRAMINGS = {
    "durel": ("Target word: {word}\n\nContext 1: {c1}\nContext 2: {c2}\n\n"
              "How related are the meanings of the target word in the two contexts? "
              "Use this 4-point scale:\n4 = Identical\n3 = Closely Related\n"
              "2 = Distantly Related\n1 = Unrelated\n\nAnswer with only the single number (1, 2, 3, or 4)."),
    "scale": ("Target word: {word}\n\nContext 1: {c1}\nContext 2: {c2}\n\n"
              "On a scale from 0 to 100, how related are the meanings of the target word in the "
              "two contexts? 0 = completely unrelated, 100 = identical meaning.\n\n"
              "Answer with only the number (0-100)."),
}

def clean(ctx):
    return ctx.replace("**", "")

def data_uri(path):
    b = open(path, "rb").read()
    return "data:image/jpeg;base64," + base64.b64encode(b).decode()

def parse_num(txt, lo, hi):
    if not txt:
        return None
    m = re.search(r"-?\d+(?:\.\d+)?", txt)
    if not m:
        return None
    v = float(m.group())
    return v if lo <= v <= hi else None

def load_items():
    return list(csv.DictReader(open(os.path.join(HERE, "items.csv"))))

def run_cell(item, framing, condition, mname, model):
    word = item["target_word"]
    user = FRAMINGS[framing].format(word=word, c1=clean(item["context1"]), c2=clean(item["context2"]))
    images = None
    if condition == "image":
        images = [{"url": data_uri(os.path.join(HERE, "images", item["image1"])), "detail": "low"},
                  {"url": data_uri(os.path.join(HERE, "images", item["image2"])), "detail": "low"}]
    r = call(model, SYSTEM, user, images=images)
    lo, hi = (1, 4) if framing == "durel" else (0, 100)
    return {"item_id": item["item_id"], "word": word, "stratum": item["stratum"],
            "gold": item["gold"], "framing": framing, "condition": condition,
            "model": mname, "raw": r.get("content"), "rating": parse_num(r.get("content"), lo, hi),
            "usage": r.get("usage", {}), "error": r.get("error")}

def liveness():
    from PIL import Image
    img = Image.new("RGB", (64, 64), (200, 30, 30))  # solid red
    buf = io.BytesIO(); img.save(buf, "PNG"); data = buf.getvalue()
    open(os.path.join(HERE, "images", "_liveness_red.png"), "wb").write(data)
    sha = hashlib.sha256(data).hexdigest()
    uri = "data:image/png;base64," + base64.b64encode(data).decode()
    print(f"liveness synthetic image sha256={sha}")
    recs = []
    for mname, model in MODELS.items():
        r = call(model, "You are a helpful assistant. Answer in one word.",
                 "What colour is this image?", images=[{"url": uri, "detail": "low"}])
        print(f"  {mname:7s}: {r.get('content')!r}  cost={r.get('usage',{}).get('cost')}")
        recs.append(r)
    tot, have, miss = billed_cost([recs])
    print(f"liveness billed=${tot:.5f}  (have={have} missing={miss})")

def grid(items):
    recs = []
    for it in items:
        for framing in FRAMINGS:
            for condition in ("text", "image"):
                for mname, model in MODELS.items():
                    rec = run_cell(it, framing, condition, mname, model)
                    recs.append(rec)
                    flag = "" if rec["rating"] is not None else f"  <PARSE-FAIL raw={rec['raw']!r}>"
                    print(f"  {it['item_id']:11s} {framing:5s} {condition:5s} {mname:7s} -> {rec['rating']}{flag}")
    return recs

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    items = load_items()
    if mode == "liveness":
        liveness()
    elif mode == "preflight":
        recs = grid(items[:1])
        tot, have, miss = billed_cost([recs])
        print(f"\nPREFLIGHT billed=${tot:.5f} over {len(recs)} calls "
              f"(have={have} missing={miss}); full-grid x{len(items)} ~ ${tot*len(items):.3f}")
    elif mode == "full":
        recs = grid(items)
        os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
        json.dump(recs, open(os.path.join(HERE, "raw", "results.json"), "w"), indent=2)
        tot, have, miss = billed_cost([recs])
        n_fail = sum(1 for r in recs if r["rating"] is None)
        print(f"\nFULL: {len(recs)} calls, {n_fail} parse-fails, billed=${tot:.5f} "
              f"(have={have} missing={miss})")
    else:
        print("usage: run.py [liveness|preflight|full]")

if __name__ == "__main__":
    main()
