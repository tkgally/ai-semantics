#!/usr/bin/env python3
"""VWSD grounding-headroom NL-baseline probe — runnable harness (the MAGNITUDE follow-up).

Implements the frozen design experiments/designs/vwsd-grounding-headroom-nlbaseline.md
under the ratified competence standard (decisions/resolved/vwsd-nlbaseline-competence-dv,
ADOPT-DEFAULT Q1-C) with the three deferred numbers ratified s127
(decisions/resolved/vwsd-nlbaseline-audit-params, ADOPT-DEFAULTS):
  P1 = graded none/partial/high recovery, band metric = the HIGH-recovery rate
  P2 = author = panel.A (claude-sonnet-4.6); held-out auditors = panel.B (gpt-5.4-mini)
       + panel.C (gemini-3.5-flash); band on the TWO-AUDITOR MEAN high-recovery
  P3 = two-sided target band [0.60, 0.95] on the high-recovery rate

The ONLY new text channel vs v2 is a COMPETENT NATURAL-LANGUAGE description that NAMES
the depicted referent plainly and completely (v2 BARRED naming; v1's captions named and
SATURATED — this is the fluent middle). The frozen 120 items, the IMAGE arm, and the
DISTRACT control are REUSED VERBATIM BY SHA from the v2 run dir (they are properties of
the items + images + models, not of the text channel) — no re-spend on them.

Anchor: resource/vwsd-semeval-2023 (463 EN gold test); frozen N=120 subset (sha 7f9e52fa…).

Arms (only the first three are NEW spend; IMAGE/DISTRACT are reused from v2):
  desc-preflight   describe 6 candidate images with claude, print + per-image cost
  desc-full        author NL descriptions over the 1158 unique candidate images of the
                   frozen 120 (claude, low detail, NAMES ALLOWED) -> frozen/nl_descriptors.json
                   (resumable, checkpointed, hard DESC_ABORT_USD guard for day-splitting)
  text-preflight   2 items x panel, NL-description selection arm, per-call cost
  text-full        TEXT-NL selection arm over the frozen 120 x 3 models -> raw/text_nl.json
                   (the per-item NL separability covariate sep_nl_i)
  audit-preflight  4 gold descriptions x the two held-out auditors, print recovery + score
  audit-full       held-out adequacy audit: panel.B + panel.C recover the referent from each
                   of the 120 GOLD descriptions (text-only, no image/word/gold); graded
                   none/partial/high (v2's deterministic leak_score, raw guess stored) ->
                   adds audit{} to frozen/nl_descriptors.json + raw/audit_calls.json

The FREEZE (design condition b) = desc-full + text-full + audit-full all complete and
checksummed BEFORE the reused IMAGE arm is read. Then a FRESH INDEPENDENT pre-run critic
must GO against the observed sep_nl_i + adequacy-audit distributions (must certify: NOT an
oracle restatement [audit high-recovery < 0.95]; NOT a degenerate-weak channel [>= 0.60];
sep_nl_i genuinely pre-frozen; DISTRACT credited first). A NO-GO defers and relaxes nothing.

IMAGES ARE OUT OF GIT (resource/vwsd-semeval-2023 License & redistribution). Fetched at
runtime into $VWSD_IMAGES (572MB resized EN zip, sha b9f2f1e1…af8f), never committed.

Usage:
  export VWSD_IMAGES=/path/to/extracted/test_images_resized
  export OPENROUTER_API_KEY=...
  python3 run.py desc-preflight
  DESC_ABORT_USD=4.50 python3 run.py desc-full     # resumable; rerun to continue
  python3 run.py text-preflight
  python3 run.py text-full
  python3 run.py audit-preflight
  python3 run.py audit-full
"""
import base64, json, os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}
AUTHOR = "claude"                 # P2: NL author = panel.A (held out from the auditors)
AUDITORS = ["gpt", "gemini"]      # P2: two held-out auditors = panel.B + panel.C
BAND = (0.60, 0.95)              # P3: two-sided target band on the two-auditor MEAN high-recovery

IMAGES_DIR = os.environ.get("VWSD_IMAGES", "")           # local, gitignored
RUN_ITEMS = os.path.join(HERE, "frozen", "run_items.json")   # the v2 frozen 120 (sha 7f9e52fa…)
NLDESC = os.path.join(HERE, "frozen", "nl_descriptors.json")  # NL descriptions + adequacy audit
RAWDIR = os.path.join(HERE, "raw")

# Hard spend guard for the resumable descriptor pass (the run's only large spend).
# Day-splittable: rerun to resume; the guard caps THIS process's cumulative ledger spend.
DESC_ABORT_USD = float(os.environ.get("DESC_ABORT_USD", "4.50"))
DESC_LIMIT = int(os.environ.get("DESC_LIMIT", "0"))   # 0 = no per-batch item cap

# ----- NL description policy (Q1-C: names ALLOWED, plain + complete, competent describer) -----
# The deliberate inverse of v2's Option-B visual-form policy: v2 FORBADE naming the referent
# ("a pile of mustard seeds" was the FORBIDDEN style); here naming it plainly is REQUIRED.
NLDESC_SYS = (
    "You write a competent, natural-language description of a single image for a reader who "
    "cannot see it. Name the depicted object, creature, scene, plant, or concept plainly and "
    "completely, exactly as an ordinary competent describer would — say what it IS, not merely "
    "what shapes and colours appear. Use one or two plain sentences. Do not hedge, do not list "
    "alternatives, do not mention that it is an image or a photo. Example of the REQUIRED style: "
    "\"A small heap of mustard seeds, the tiny round yellow-brown seeds of the mustard plant, "
    "piled together.\""
)
NLDESC_USER = ("Describe this image in one or two plain sentences, naming what it depicts "
               "plainly and completely.")

# ----- TEXT-NL selection arm (text-only: target word + phrase + the 10 NL descriptions) -----
# Byte-identical instruction to v2's descriptor-selection arm (the only change is that the
# descriptions now NAME the referent), so the arms are directly comparable.
SEL_SYS_TEXT = ("You are disambiguating a word's intended meaning. You will see a target "
                "word, a short phrase using it, and ten short descriptions of candidate "
                "images numbered 1 to 10. Choose the single description that best matches "
                "the intended meaning of the target word in the phrase. Answer with only "
                "the number, 1 to 10.")

# ----- adequacy audit (held-out referent recovery; the v2 leak instrument, opposite direction) -----
AUDIT_SYS = ("You are shown one short description of an image, with no other information. "
             "Infer what real-world object, creature, scene, plant, or concept the image "
             "most likely depicts. Answer with a short noun phrase only (no sentence).")

# ---------- data ----------
def load_run_items():
    return json.load(open(RUN_ITEMS))

def unique_candidates(items):
    return sorted({c for it in items for c in it["candidates"]})

def load_nldesc():
    return json.load(open(NLDESC)) if os.path.exists(NLDESC) else {
        "policy": NLDESC_SYS, "author": MODELS[AUTHOR],
        "auditors": [MODELS[a] for a in AUDITORS], "band": list(BAND),
        "descriptors": {}, "audit": {}}

def img_path(name):
    return os.path.join(IMAGES_DIR, name)

def data_uri(name):
    b = open(img_path(name), "rb").read()
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

# ---------- NL description authoring ----------
def describe(name):
    r = call(MODELS[AUTHOR], NLDESC_SYS, NLDESC_USER,
             images=[{"url": data_uri(name), "detail": "low"}], max_tokens=128)
    desc = (r.get("content") or "").strip().replace("\n", " ")
    return desc, r

# ---------- recovery scoring (deterministic, auditable; the v2 leak_score, verbatim) ----------
# Reused verbatim from the v2 harness (decisions/resolved/vwsd-nlbaseline-audit-params P1:
# "Reuse v2's graded scheme verbatim"). 2 = HIGH (recovers the target word itself), 1 = PARTIAL
# (recovers a trigger/context token from the phrase), 0 = NONE. Raw guess stored for a later
# model re-grade (the scoring rule's VALIDITY mirrors v2's design B.4 later-ratification posture).
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

def recovery_score(word, phrase, recovered):
    wl = {lemma(w) for w in word.split() if lemma(w)}
    pl = toks(phrase) - wl
    rl = toks(recovered)
    if wl & rl:
        return 2, sorted(wl & rl)
    if pl & rl:
        return 1, sorted(pl & rl)
    return 0, []

# ---------- TEXT-NL selection ----------
def text_user(it, nld):
    lines = "\n".join(f"{i+1}. {nld['descriptors'].get(name, '(no description)')}"
                      for i, name in enumerate(it["candidates"]))
    return (f"Target word: {it['word']}\nPhrase: {it['phrase']}\n"
            f"Candidate image descriptions:\n{lines}\n\n"
            "Which description best matches the intended meaning of the target word? "
            "Answer with only the number, 1 to 10.")

def run_text(it, nld, mname):
    r = call(MODELS[mname], SEL_SYS_TEXT, text_user(it, nld), max_tokens=16,
             reasoning={"effort": "minimal"} if mname == "gemini" else None)
    pick = parse_pick(r.get("content"))
    return {"arm": "text_nl", "item_id": it["id"], "word": it["word"], "model": mname,
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

    if mode == "desc-preflight":
        if not IMAGES_DIR or not os.path.isdir(IMAGES_DIR):
            sys.exit(f"$VWSD_IMAGES not set / not a dir: {IMAGES_DIR!r}")
        items = load_run_items()
        names = unique_candidates(items)[:6]
        recs = []
        for nm in names:
            d, r = describe(nm)
            recs.append(r)
            print(f"  {nm}: {d!r}")
        uniq = len(unique_candidates(items))
        per = _cost(recs, "DESC-PREFLIGHT") / max(len(recs), 1)
        print(f"  per-image ${per:.5f}; extrapolated {uniq} unique images ~ ${per*uniq:.3f}")

    elif mode == "desc-full":
        if not IMAGES_DIR or not os.path.isdir(IMAGES_DIR):
            sys.exit(f"$VWSD_IMAGES not set / not a dir: {IMAGES_DIR!r}")
        items = load_run_items()
        names = unique_candidates(items)
        nld = load_nldesc()
        todo = [n for n in names if n not in nld["descriptors"]]
        if DESC_LIMIT > 0:
            todo = todo[:DESC_LIMIT]
        print(f"authoring {len(todo)} of {len(names)} unique NL descriptions "
              f"({len(names)-len(todo)} already done); DESC_ABORT_USD=${DESC_ABORT_USD}...")
        ledger = os.path.join(RAWDIR, "descriptor_calls.json")
        allrecs = json.load(open(ledger)) if os.path.exists(ledger) else []
        running = billed_cost([allrecs])[0]
        os.makedirs(RAWDIR, exist_ok=True)
        for i, nm in enumerate(todo):
            d, r = describe(nm)
            nld["descriptors"][nm] = d
            allrecs.append(r)
            running += (r.get("usage") or {}).get("cost") or 0.0
            if i < 6 or i % 100 == 0:
                print(f"  [{i+1}/{len(todo)}] {nm}: {d!r}  (running ${running:.4f})")
            if i % 25 == 0 or i == len(todo) - 1:   # checkpoint
                _freeze(nld, NLDESC)
                json.dump(allrecs, open(ledger, "w"), indent=2)
            if running > DESC_ABORT_USD:
                print(f"  !! ABORT: running billed ${running:.4f} > ${DESC_ABORT_USD} cap. "
                      f"Checkpointed; rerun to resume.")
                break
        sha = _freeze(nld, NLDESC)
        json.dump(allrecs, open(ledger, "w"), indent=2)
        _cost(allrecs, "DESC-FULL (cumulative)")
        print(f"  descriptors={len(nld['descriptors'])}/{len(names)}  {NLDESC} sha256={sha}")

    elif mode in ("text-preflight", "text-full"):
        items = load_run_items()
        nld = load_nldesc()
        if len(nld["descriptors"]) < len(unique_candidates(items)):
            sys.exit(f"NL descriptors incomplete ({len(nld['descriptors'])}/"
                     f"{len(unique_candidates(items))}); run desc-full first")
        items = items[:2] if mode == "text-preflight" else items
        recs = []
        for it in items:
            for mname in MODELS:
                recs.append(run_text(it, nld, mname))
            done = [r for r in recs if r["item_id"] == it["id"]]
            if mode == "text-preflight" or len(recs) % 60 == 0:
                print(f"  {it['id']:8s} " + " ".join(f"{r['model']}:{r['pick']}" for r in done))
        if mode == "text-full":
            p, sha = _save_raw(recs, "text_nl.json")
            nf = sum(1 for r in recs if r["pick"] is None)
            _cost(recs, "TEXT-NL-FULL")
            print(f"  wrote {p}  sha256={sha}  parse-fails={nf}")
        else:
            per = _cost(recs, "TEXT-NL-PREFLIGHT") / max(len(recs), 1)
            print(f"  per-(item,model) ${per:.5f}")

    elif mode in ("audit-preflight", "audit-full"):
        items = load_run_items()
        nld = load_nldesc()
        if len(nld["descriptors"]) < len(unique_candidates(items)):
            sys.exit(f"NL descriptors incomplete; run desc-full first")
        sel = items[:4] if mode == "audit-preflight" else items
        recs = []
        for it in sel:
            gold = it["gold_name"]
            gdesc = nld["descriptors"].get(gold, "")
            entry = {"gold_name": gold, "word": it["word"], "phrase": it["phrase"],
                     "gold_descriptor": gdesc, "auditors": {}}
            for a in AUDITORS:
                r = call(MODELS[a], AUDIT_SYS,
                         f"Description: {gdesc}\nWhat does this image most likely depict? "
                         f"Answer with a short noun phrase only.", max_tokens=32,
                         reasoning={"effort": "minimal"} if a == "gemini" else None)
                rec = (r.get("content") or "").strip().replace("\n", " ")
                score, matched = recovery_score(it["word"], it["phrase"], rec)
                entry["auditors"][a] = {"recovered": rec, "recovery_score": score,
                                        "matched_tokens": matched}
                recs.append(r)
            if mode == "audit-preflight":
                print(f"  {it['id']} [{it['word']}/{it['phrase']}]")
                for a in AUDITORS:
                    e = entry["auditors"][a]
                    print(f"     {a:7s} -> {e['recovered']!r}  score={e['recovery_score']} {e['matched_tokens']}")
            nld["audit"][it["id"]] = entry
        if mode == "audit-full":
            sha = _freeze(nld, NLDESC)
            _, csha = _save_raw(recs, "audit_calls.json")
            # band metric = HIGH-recovery rate (fraction scoring 2), per auditor + two-auditor mean
            per_auditor = {}
            for a in AUDITORS:
                vals = [v["auditors"][a]["recovery_score"] for v in nld["audit"].values()]
                dist = {s: sum(1 for x in vals if x == s) for s in (0, 1, 2)}
                hi = dist[2] / max(len(vals), 1)
                per_auditor[a] = {"dist": dist, "high_recovery_rate": hi}
            mean_hi = sum(per_auditor[a]["high_recovery_rate"] for a in AUDITORS) / len(AUDITORS)
            _cost(recs, "AUDIT-FULL")
            for a in AUDITORS:
                pa = per_auditor[a]
                print(f"  {a:7s} none/partial/high = {pa['dist'][0]}/{pa['dist'][1]}/{pa['dist'][2]}  "
                      f"high-recovery rate = {pa['high_recovery_rate']:.3f}")
            inband = BAND[0] <= mean_hi <= BAND[1]
            print(f"  TWO-AUDITOR MEAN high-recovery = {mean_hi:.3f}  band {BAND}  "
                  f"=> {'IN BAND' if inband else 'OUT OF BAND (pre-run-critic NO-GO)'}")
            print(f"  {NLDESC} sha256={sha}")
        else:
            _cost(recs, "AUDIT-PREFLIGHT")

    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
