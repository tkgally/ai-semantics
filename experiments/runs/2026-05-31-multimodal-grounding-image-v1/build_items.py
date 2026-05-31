#!/usr/bin/env python3
"""Build + freeze the multimodal-grounding-image-v1 stimulus set.

Constructed minimal-pair set keyed to Princeton WordNet noun synsets (the existing
human sense inventory; Tom's authorized option b). Two strata:
  - DISTINCT-F : visually-distinct homonyms, two DIFFERENT synsets  -> human gold = different
  - SAME-T     : same synset, two contexts + two DIFFERENT photos of that referent
                 (the surface-similarity / distraction control) -> human gold = same

Images: Wikimedia Commons API, prefer Public-Domain / CC0 / CC-BY(-SA); downscaled
locally (Pillow, longest side <=256, JPEG q=40, metadata stripped) and sha256-frozen.
The downscaled local JPEG (not the Commons thumb) is the frozen artifact that gets sent.

Run: python3 build_items.py   (writes items.csv, manifest.json, ATTRIBUTION.md, images/*.jpg)
Freeze: after visual review, sha256s are pinned in PREREG.md; no image swapped after.
"""
import csv, io, json, hashlib, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
os.makedirs(IMG, exist_ok=True)
UA = "ai-semantics-research/0.1 (tomgally@gmail.com)"
API = "https://commons.wikimedia.org/w/api.php"

# Each context: (image_key, wordnet_synset, sense_gloss, commons_search_query)
# Sentences are constructed; the target word is wrapped in **double asterisks** for marking.
ITEMS = [
    # ---------- DISTINCT-F : visually-distinct homonyms (gold = different) ----------
    dict(id="bat-F", word="bat", stratum="distinct-F", gold="different",
         c1="The **bat** flew out of the dark cave at dusk.",
         s1="bat.n.01", g1="nocturnal flying mammal", q1="fruit bat flying mammal",
         c2="She gripped the **bat** and waited for the next pitch.",
         s2="bat.n.05", g2="club for hitting a ball", q2="wooden baseball bat isolated"),
    dict(id="crane-F", word="crane", stratum="distinct-F", gold="different",
         c1="A **crane** waded slowly through the shallow marsh.",
         s1="crane.n.05", g1="long-necked wading bird", q1="sandhill crane bird marsh",
         c2="The **crane** lifted the steel beam to the top floor.",
         s2="crane.n.04", g2="machine for lifting heavy loads", q2="construction tower crane site"),
    dict(id="bank-F", word="bank", stratum="distinct-F", gold="different",
         c1="We sat on the grassy **bank** of the slow river.",
         s1="bank.n.01", g1="sloping land beside water", q1="grassy river bank water"),
    # bank-F c2 added below in code (financial)
    dict(id="pitcher-F", word="pitcher", stratum="distinct-F", gold="different",
         c1="He filled the **pitcher** with cold water for the table.",
         s1="pitcher.n.02", g1="vessel with a handle and spout", q1="ceramic water pitcher jug",
         c2="The **pitcher** threw a sharp curveball past the batter.",
         s2="pitcher.n.01", g2="baseball player who pitches", q2="baseball pitcher throwing mound"),
    dict(id="mouse-F", word="mouse", stratum="distinct-F", gold="different",
         c1="A small **mouse** scurried under the kitchen door.",
         s1="mouse.n.01", g1="small rodent", q1="house mouse rodent",
         c2="She clicked the **mouse** to open the file.",
         s2="mouse.n.04", g2="hand-operated computer device", q2="computer mouse device white"),
    dict(id="seal-F", word="seal", stratum="distinct-F", gold="different",
         c1="The **seal** basked on the rocky shore near the waves.",
         s1="seal.n.09", g1="marine mammal", q1="harbor seal animal shore",
         c2="He pressed the red wax **seal** onto the envelope.",
         s2="seal.n.02", g2="device incised to make an impression", q2="red wax seal stamp envelope"),
    # ---------- SAME-T : same synset, two different photos (gold = same) ----------
    dict(id="bank-T", word="bank", stratum="same-T", gold="same",
         c1="She deposited her paycheck at the **bank** downtown.",
         s1="bank.n.02", g1="financial institution", q1="bank building exterior street",
         c2="The **bank** approved his mortgage loan last week.",
         s2="bank.n.02", g2="financial institution", q2="bank branch facade entrance"),
    dict(id="crane-T", word="crane", stratum="same-T", gold="same",
         c1="A **crane** waded through the reeds at dawn.",
         s1="crane.n.05", g1="long-necked wading bird", q1="grey crane bird wetland",
         c2="The **crane** spread its wide wings and called loudly.",
         s2="crane.n.05", g2="long-necked wading bird", q2="crane bird flying wings"),
    dict(id="mouse-T", word="mouse", stratum="same-T", gold="same",
         c1="A **mouse** scurried under the old wooden door.",
         s1="mouse.n.01", g1="small rodent", q1="brown mouse rodent ground",
         c2="The cat chased a tiny **mouse** across the floor.",
         s2="mouse.n.01", g2="small rodent", q2="field mouse rodent grass"),
    dict(id="pitcher-T", word="pitcher", stratum="same-T", gold="same",
         c1="He filled the **pitcher** with iced lemonade.",
         s1="pitcher.n.02", g1="vessel with a handle and spout", q1="glass pitcher jug water",
         c2="A blue **pitcher** sat in the middle of the table.",
         s2="pitcher.n.02", g2="vessel with a handle and spout", q2="ceramic jug pitcher pottery"),
    dict(id="seal-T", word="seal", stratum="same-T", gold="same",
         c1="The **seal** dove off the rock into the cold sea.",
         s1="seal.n.09", g1="marine mammal", q1="seal animal swimming sea",
         c2="A grey **seal** rested on the sandy beach.",
         s2="seal.n.09", g2="marine mammal", q2="grey seal beach haul out"),
    dict(id="bat-T", word="bat", stratum="same-T", gold="same",
         c1="She gripped the **bat** and stepped up to the plate.",
         s1="bat.n.05", g1="club for hitting a ball", q1="baseball bat wood isolated",
         c2="He swung the **bat** hard and missed the ball.",
         s2="bat.n.05", g2="club for hitting a ball", q2="aluminum baseball bat sport"),
]
# add bank-F c2 (financial) — distinct-F second context
for it in ITEMS:
    if it["id"] == "bank-F":
        it.update(c2="She deposited her paycheck at the **bank** downtown.",
                  s2="bank.n.02", g2="financial institution", q2="bank building exterior street")

OK_LIC = ("public domain", "pd", "cc0", "cc-by", "cc by", "attribution")

def api_get(params):
    params = {**params, "format": "json"}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def search_files(query, n=12):
    d = api_get(dict(action="query", list="search", srnamespace=6,
                     srsearch=query, srlimit=n))
    return [m["title"] for m in d.get("query", {}).get("search", [])]

def imageinfo(title):
    d = api_get(dict(action="query", titles=title, prop="imageinfo",
                     iiprop="url|extmetadata|size|mime", iiurlwidth=512))
    pages = d.get("query", {}).get("pages", {})
    for _, p in pages.items():
        ii = p.get("imageinfo")
        if not ii:
            continue
        info = ii[0]
        em = info.get("extmetadata", {})
        lic = (em.get("LicenseShortName", {}).get("value", "") or "").strip()
        artist = (em.get("Artist", {}).get("value", "") or "").strip()
        mime = info.get("mime", "")
        return dict(thumburl=info.get("thumburl"), url=info.get("url"),
                    license=lic, artist=artist, mime=mime,
                    w=info.get("width"), h=info.get("height"))
    return None

def lic_ok(lic, mime):
    if not lic:
        return False
    if mime not in ("image/jpeg", "image/png", "image/webp"):
        return False
    ll = lic.lower()
    if "nc" in ll.replace("cc-by", "") and "noncommercial" not in ll and "by-nc" in ll:
        return False
    return any(k in ll for k in OK_LIC)

def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read()

def pick_and_download(query, out_key):
    from PIL import Image
    import re
    for title in search_files(query):
        info = imageinfo(title)
        if not info or not info.get("thumburl"):
            continue
        if not lic_ok(info["license"], info["mime"]):
            continue
        try:
            raw = fetch_bytes(info["thumburl"])
            im = Image.open(io.BytesIO(raw)).convert("RGB")
        except Exception as e:
            print(f"   skip {title}: {e}")
            continue
        # downscale longest side <=256
        w, h = im.size
        scale = min(1.0, 256.0 / max(w, h))
        nw, nh = max(1, int(w*scale)), max(1, int(h*scale))
        im2 = im.resize((nw, nh), Image.LANCZOS)
        outpath = os.path.join(IMG, out_key + ".jpg")
        buf = io.BytesIO()
        im2.save(buf, format="JPEG", quality=40, optimize=True)
        data = buf.getvalue()
        with open(outpath, "wb") as f:
            f.write(data)
        sha = hashlib.sha256(data).hexdigest()
        artist = re.sub("<[^>]+>", "", info["artist"])[:120]
        print(f"   [{out_key}] {title}  lic={info['license']}  {nw}x{nh}  {len(data)}B")
        return dict(image_key=out_key, query=query, commons_file=title,
                    source_page="https://commons.wikimedia.org/wiki/" + title.replace(" ", "_"),
                    thumburl=info["thumburl"], license=info["license"], artist=artist,
                    orig_w=info["w"], orig_h=info["h"], final_w=nw, final_h=nh,
                    jpeg_quality=40, bytes=len(data), sha256=sha)
    print(f"   !! NO usable image for query: {query}")
    return None

def main():
    manifest = []
    rows = []
    for it in ITEMS:
        for side in ("1", "2"):
            key = f"{it['id']}_{side}"
            print(f"sourcing {key} ({it['word']}, {it['stratum']}) q={it['q'+side]!r}")
            m = pick_and_download(it["q"+side], key)
            if m is None:
                m = dict(image_key=key, query=it["q"+side], commons_file=None, sha256=None)
            m.update(item_id=it["id"], target_word=it["word"], stratum=it["stratum"],
                     wordnet_synset=it["s"+side], sense_gloss=it["g"+side])
            manifest.append(m)
            time.sleep(0.3)
        rows.append(dict(item_id=it["id"], target_word=it["word"], stratum=it["stratum"],
                         gold=it["gold"], context1=it["c1"], context2=it["c2"],
                         synset1=it["s1"], synset2=it["s2"], gloss1=it["g1"], gloss2=it["g2"],
                         image1=f"{it['id']}_1.jpg", image2=f"{it['id']}_2.jpg"))
    with open(os.path.join(HERE, "items.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(HERE, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    # attribution
    with open(os.path.join(HERE, "ATTRIBUTION.md"), "w") as f:
        f.write("# Image attribution (Wikimedia Commons)\n\n")
        f.write("All images downscaled locally (<=256px, JPEG q40). Source/license per image:\n\n")
        for m in manifest:
            if m.get("commons_file"):
                f.write(f"- **{m['image_key']}** ({m['target_word']}, {m['sense_gloss']}): "
                        f"[{m['commons_file']}]({m['source_page']}) — {m['license']}"
                        f" — {m.get('artist','')}\n")
    n_ok = sum(1 for m in manifest if m.get("sha256"))
    print(f"\nDONE: {len(rows)} items, {n_ok}/{len(manifest)} images sourced.")

if __name__ == "__main__":
    main()
