#!/usr/bin/env python3
"""VWSD grounding-headroom probe v1 — runnable harness.

Implements the frozen design experiments/designs/vwsd-grounding-headroom-v1.md
(ratified DV decision decisions/resolved/vwsd-grounding-headroom-dv, ADOPT MODIFIED,
Option A / interaction-as-test-of-record / Q3 narrow human-anchored posture).

Three behavioural arms over the SemEval-2023 VWSD English gold test (463 items, 10
candidate images each; gold = human-curated correct image):

  TEXT     text-only caption-based selection (no images shown; candidates are short
           neutral captions). This is BOTH the per-item text-only SEPARABILITY covariate
           AND the baseline against which image-induced improvement is measured. Computed
           and FROZEN (checksummed) BEFORE any image condition runs (binding mod 2).
  IMAGE    image-conditioned selection (the same prompt, candidates shown as the 10 real
           images, low detail). The main arm.
  DISTRACT word-ablated control (10 images, NO target word/phrase; "pick the most
           prototypical/canonical image"). The surface-salience distraction control whose
           null is reported FIRST (binding mod 3): if gold is selected >> chance with no
           word, image selection is salience-driven, not sense-driven.

Captioning (one-time, frozen pre-image artifact): each unique EN candidate image is
captioned once by panel.C (gemini, cheap) into a short neutral noun phrase. Captions are
the text proxy the ratified DV ("image identities masked to text labels") requires.

IMAGES ARE OUT OF GIT (redistribution unconfirmed; resource/vwsd-semeval-2023 License).
They are read at runtime from $VWSD_IMAGES (a local dir of the resized EN candidates) and
never committed. The annotation overlay (queries+gold) and captions ARE committed.

Usage:
  python3 run.py caption-preflight   # caption 8 images, print billed cost
  python3 run.py caption-full        # caption all unique EN images -> frozen/captions.json
  python3 run.py text-preflight      # 2 items x panel, text arm, billed cost
  python3 run.py text-full           # text-only covariate, all frozen items -> raw/text.json (FREEZE)
  python3 run.py image-preflight     # 2 items x panel, image arm, billed cost
  python3 run.py distract-preflight  # 2 items x panel, distraction arm, billed cost
  python3 run.py image-full          # image arm, frozen items -> raw/image.json
  python3 run.py distract-full       # distraction arm, frozen items -> raw/distract.json
"""
import base64, json, os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}
IMAGES_DIR = os.environ.get("VWSD_IMAGES", "")  # local, gitignored
DATA = os.path.join(HERE, "frozen", "en.test.data.v1.1.txt")
GOLD = os.path.join(HERE, "frozen", "en.test.gold.v1.1.txt")
ITEMS = os.path.join(HERE, "frozen", "run_items.json")       # frozen 50-item run subset (seed 20260624)
CAPTIONS = os.path.join(HERE, "frozen", "captions.json")     # frozen captions

# ---------- data ----------
def load_items():
    return json.load(open(ITEMS))

def load_captions():
    return json.load(open(CAPTIONS))

def img_path(name):
    return os.path.join(IMAGES_DIR, name)

def data_uri(name):
    p = img_path(name)
    b = open(p, "rb").read()
    ext = "png" if name.lower().endswith(".png") else "jpeg"
    return f"data:image/{ext};base64," + base64.b64encode(b).decode()

def parse_pick(txt, n=10):
    """Return the chosen 1..n index (int) or None. Robust to a chatty reply: bare number
    wins; else the LAST in-range integer (the model's final answer). raw always logged."""
    if not txt:
        return None
    s = txt.strip().strip("*.# ")
    if re.fullmatch(r"\d+", s) and 1 <= int(s) <= n:
        return int(s)
    cands = [int(x) for x in re.findall(r"\b(\d+)\b", txt) if 1 <= int(x) <= n]
    return cands[-1] if cands else None

# ---------- captioning ----------
CAP_SYS = ("You are a precise image captioner. In a short neutral noun phrase of 3 to 10 "
           "words, name the main concrete subject of the image. Name the object or scene "
           "only; no sentences, no commentary, no guesses about word meaning.")
CAP_USER = "Caption this image in a short neutral noun phrase."

def caption_images(names):
    out = {}
    recs = []
    for i, name in enumerate(names):
        r = call(MODELS["gemini"], CAP_SYS, CAP_USER,
                 images=[{"url": data_uri(name), "detail": "low"}],
                 max_tokens=64, reasoning={"effort": "minimal"})
        cap = (r.get("content") or "").strip().replace("\n", " ")
        out[name] = cap
        recs.append(r)
        if i < 8 or i % 200 == 0:
            print(f"  [{i+1}/{len(names)}] {name}: {cap!r}")
    return out, recs

# ---------- selection arms ----------
SEL_SYS_TEXT = ("You are disambiguating a word's intended meaning. You will see a target "
                "word, a short phrase using it, and ten short descriptions of candidate "
                "images numbered 1 to 10. Choose the single description that best matches "
                "the intended meaning of the target word in the phrase. Answer with only "
                "the number, 1 to 10.")
SEL_SYS_IMAGE = ("You are disambiguating a word's intended meaning. You will see a target "
                 "word, a short phrase using it, and ten candidate images numbered 1 to 10 "
                 "in order. Choose the single image that best matches the intended meaning "
                 "of the target word in the phrase. Answer with only the number, 1 to 10.")
DISTRACT_SYS = ("You will see ten images numbered 1 to 10 in order. With no other "
                "information, choose the single image that is the most prototypical, "
                "canonical, everyday depiction of a clearly recognizable common concept. "
                "Answer with only the number, 1 to 10.")

def text_user(it, caps):
    lines = "\n".join(f"{i+1}. {caps[name]}" for i, name in enumerate(it["candidates"]))
    return (f"Target word: {it['word']}\nPhrase: {it['phrase']}\n"
            f"Candidate image descriptions:\n{lines}\n\n"
            "Which description best matches the intended meaning of the target word? "
            "Answer with only the number, 1 to 10.")

def image_user(it):
    return (f"Target word: {it['word']}\nPhrase: {it['phrase']}\n"
            "The ten candidate images follow, in order 1 to 10. Which image best matches "
            "the intended meaning of the target word? Answer with only the number, 1 to 10.")

DISTRACT_USER = ("The ten candidate images follow, in order 1 to 10. Which one is the most "
                 "prototypical, canonical, everyday image? Answer with only the number, 1 to 10.")

def run_text(it, caps, mname):
    r = call(MODELS[mname], SEL_SYS_TEXT, text_user(it, caps), max_tokens=16,
             reasoning={"effort": "minimal"} if mname == "gemini" else None)
    pick = parse_pick(r.get("content"))
    return {"arm": "text", "item_id": it["id"], "word": it["word"], "model": mname,
            "gold_idx": it["gold_idx"], "pick": pick,
            "correct": (pick == it["gold_idx"]) if pick else None,
            "raw": r.get("content"), "usage": r.get("usage", {}), "error": r.get("error")}

def run_image(it, mname, arm):
    imgs = [{"url": data_uri(name), "detail": "low"} for name in it["candidates"]]
    if arm == "image":
        r = call(MODELS[mname], SEL_SYS_IMAGE, image_user(it), images=imgs, max_tokens=16,
                 reasoning={"effort": "minimal"} if mname == "gemini" else None)
    else:
        r = call(MODELS[mname], DISTRACT_SYS, DISTRACT_USER, images=imgs, max_tokens=16,
                 reasoning={"effort": "minimal"} if mname == "gemini" else None)
    pick = parse_pick(r.get("content"))
    return {"arm": arm, "item_id": it["id"], "word": it["word"], "model": mname,
            "gold_idx": it["gold_idx"], "pick": pick,
            "correct": (pick == it["gold_idx"]) if pick else None,
            "raw": r.get("content"), "usage": r.get("usage", {}), "error": r.get("error")}

# ---------- drivers ----------
def _cost(recs, label):
    tot, have, miss = billed_cost([recs])
    print(f"\n{label}: {len(recs)} calls, billed=${tot:.5f} (have={have} missing={miss})")
    return tot

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode.startswith(("text", "image", "distract")):
        items = load_items()
        caps = load_captions() if mode.startswith("text") else None

    if mode == "caption-preflight":
        names = [l.split("\t")[2] for l in open(DATA)][:8]
        _, recs = caption_images(names)
        per = _cost(recs, "CAPTION-PREFLIGHT") / max(len(recs), 1)
        # unique EN images = 4090
        print(f"  per-image ${per:.5f}; extrapolated 4090 images ~ ${per*4090:.3f}")
    elif mode == "caption-full":
        # caption every unique candidate image across the frozen item set
        items = load_items()
        names = sorted({c for it in items for c in it["candidates"]})
        print(f"captioning {len(names)} unique images...")
        caps, recs = caption_images(names)
        json.dump(caps, open(CAPTIONS, "w"), indent=2, sort_keys=True)
        sha = hashlib.sha256(open(CAPTIONS, "rb").read()).hexdigest()
        _cost(recs, "CAPTION-FULL")
        print(f"  wrote {CAPTIONS}  sha256={sha}")
    elif mode in ("text-preflight", "image-preflight", "distract-preflight"):
        recs = []
        for it in items[:2]:
            for mname in MODELS:
                if mode == "text-preflight":
                    rec = run_text(it, caps, mname)
                else:
                    rec = run_image(it, mname, "image" if mode == "image-preflight" else "distract")
                recs.append(rec)
                print(f"  {it['id']:14s} {mname:7s} -> pick={rec['pick']} correct={rec['correct']}")
        per = _cost(recs, mode.upper()) / max(len(recs), 1)
        print(f"  per-(item,model) ${per:.5f}")
    elif mode in ("text-full", "image-full", "distract-full"):
        arm = mode.split("-")[0]
        recs = []
        for it in items:
            for mname in MODELS:
                if arm == "text":
                    rec = run_text(it, caps, mname)
                else:
                    rec = run_image(it, mname, arm)
                recs.append(rec)
            done = [r for r in recs if r["item_id"] == it["id"]]
            print(f"  {it['id']:14s} " + " ".join(f"{r['model']}:{r['pick']}" for r in done))
        os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
        out = os.path.join(HERE, "raw", f"{arm}.json")
        json.dump(recs, open(out, "w"), indent=2)
        sha = hashlib.sha256(open(out, "rb").read()).hexdigest()
        nf = sum(1 for r in recs if r["pick"] is None)
        _cost(recs, mode.upper())
        print(f"  wrote {out}  sha256={sha}  parse-fails={nf}")
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
