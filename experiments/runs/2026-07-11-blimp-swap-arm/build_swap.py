#!/usr/bin/env python3
"""build_swap.py — FROZEN builder for the BLiMP R1 content-word-swap arm (A3b, s210, C8 promotion-prep).

RATIFIED s210 (decisions/resolved/blimp-swap-arm-design): Q1-A / Q2-B / Q3-A + noun-only-swap (G-coverage)
+ G-margin-justification. This script is the frozen recipe. It is committed + PREREG'd BEFORE any model
call, and independently reproduced by a fresh-agent verifier (G5-plus) before any item is scored. Because
the swapped-condition accuracies are UNKNOWN until probe.py runs, the swap arm has no known-accuracy
exposure; its only DoF is this build.

WHAT IT DOES (deterministic, seeded):
  1. Fetch + sha256-pin the 2012 "SUBTLEX-US with PoS" file (Q2-B; POS from the published Dom_PoS column,
     frequency = Lg10WF = log10(FREQcount+1) — computed here from FREQcount, matching Brysbaert&New 2009).
     -> content pools: singular-noun lemmas (Dom_PoS Noun, nltk-singular), proper names (Dom_PoS Name),
     attributive adjectives (Dom_PoS Adjective). The only human DoF is MEMBERSHIP (junk filters below);
     never per-item hand-assignment (G-lexicon-determinism).
  2. Fetch + sha256-pin the frame-safe candidate BLiMP paradigms.
  3. SELECT 3 shallow + 3 deep frame-safe paradigms by a deterministic SWAPPABILITY score (mean count of
     swappable open-class positions/item over a fixed seeded sample), ties by UID alphabetical, BLIND to
     accuracy and human agreement (Q1-A).
  4. For each selected paradigm, draw a FRESH seeded ~100-pair subsample and build the swapped counterpart:
     replace COMMON NOUNS + PROPER NAMES + ATTRIBUTIVE ADJECTIVES (the frame-safe categories with NO
     subcategorization frame), matched within +-0.10 Lg10WF, POS/number preserved, holding EXACT the
     contrast locus (except the det-noun carve-out: the locus head noun's lemma is swapped with its number
     feature preserved) and the whole closed-class functional skeleton, main verbs, and adverbs. Mechanical
     re-validation (Q3-A): broken pairs dropped/logged/reported.
  5. Emit selection.json, items_swap.json (both ORIGINAL and SWAP good/bad per pair), build_report.txt.

Outputs are the frozen instrument; probe.py then runs BOTH conditions (orig + swap) fresh, both orders.
"""
import csv, hashlib, io, json, math, os, random, re, sys, urllib.request, zipfile, difflib
from pathlib import Path
from collections import Counter
import nltk
from nltk.corpus import wordnet as wn  # noqa: F401 (ensures corpus present)

HERE = Path(__file__).parent
CACHE = HERE / ".cache"            # gitignored; the full lexicon + paradigm files land here transiently
CACHE.mkdir(exist_ok=True)

# ---- frozen constants (PREREG) --------------------------------------------
SEED = 20260711                    # fresh-sample seed (distinct from s205's 20260710)
SEL_SEED = 77770711                # selection-sample seed (structural swappability scoring)
SEL_N = 80                         # pairs/paradigm for the swappability score
TARGET_N = 100                     # target usable paired items/paradigm (G-power)
SAMPLE_N = 130                     # draw this many, keep first TARGET_N usable
USABLE_FLOOR = 60                  # below this a paradigm is dropped + power re-stated (G-power)
BAND = 0.10                        # +-0.10 Lg10WF match band (Q2-A/B; the resource page's named use)
PCT_DOM = 0.75                     # Dom_PoS dominance floor for pool membership (junk filter)

SUBTLEX_ZIP = ("https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/"
               "subtlexus/subtlexus1.zip")   # -> "SUBTLEX-US frequency list with PoS and Zipf information.xlsx"
SUBTLEX_ZIP_SHA = "458128f90a28c4f396cb2a5b23ac93c56f745ee8cfca9be2afedad4091d15090"
SUBTLEX_XLSX_SHA = "3a8cb93a4e28988c2ce722a63f6b8d394acdc42ebe2ab6e1f0e484ee0d4167a7"

BLIMP_URL = "https://raw.githubusercontent.com/alexwarstadt/blimp/master/data/{}.jsonl"
# frame-safe candidate sets (Q1-A; island/filler-gap + irregular_* EXCLUDED — G-frame).
SHALLOW_CANDIDATES = ["determiner_noun_agreement_1", "determiner_noun_agreement_2",
                      "regular_plural_subject_verb_agreement_1", "regular_plural_subject_verb_agreement_2"]
DEEP_CANDIDATES = ["matrix_question_npi_licensor_present", "npi_present_1", "npi_present_2",
                   "only_npi_licensor_present", "only_npi_scope",
                   "sentential_negation_npi_licensor_present", "sentential_negation_npi_scope",
                   "existential_there_quantifiers_1", "existential_there_quantifiers_2",
                   "superlative_quantifiers_1", "superlative_quantifiers_2"]
DET_NOUN_FAMILY = {"determiner_noun_agreement_1", "determiner_noun_agreement_2"}
NP_LEFT = {"DT", "JJ", "JJR", "JJS", "IN", "PRP$", "POS", "NN", "NNS", "NNP", "NNPS", "CD", "PDT", "WDT", "TO"}

# ---- morphology helpers ----------------------------------------------------
def is_alpha(w): return bool(re.fullmatch(r"[a-z]+", w)) and len(w) >= 3
def looks_plural(w): return w.endswith("s") and not re.search(r"(ss|us|is|ous)$", w)
def pluralize(l):
    if re.search(r"(s|x|z|ch|sh)$", l): return l + "es"
    if re.search(r"[^aeiou]y$", l): return l[:-1] + "ies"
    return l + "s"
def singularize(w):
    if w.endswith("ies"): return w[:-3] + "y"
    if w.endswith("es") and re.search(r"(s|x|z|ch|sh)es$", w): return w[:-2]
    if w.endswith("s"): return w[:-1]
    return w

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()

# ---- 1. lexicon + pools ----------------------------------------------------
def load_lexicon():
    xlsx = CACHE / "subtlex_pos.xlsx"
    if not xlsx.exists():
        for attempt in range(4):
            try:
                req = urllib.request.Request(SUBTLEX_ZIP, headers={"User-Agent": "Mozilla/5.0"})
                raw = urllib.request.urlopen(req, timeout=120).read()
                break
            except Exception:
                if attempt == 3: raise
        assert sha256_bytes(raw) == SUBTLEX_ZIP_SHA, "SUBTLEX zip sha256 mismatch"
        z = zipfile.ZipFile(io.BytesIO(raw))
        data = z.read(z.namelist()[0])
        assert sha256_bytes(data) == SUBTLEX_XLSX_SHA, "SUBTLEX xlsx sha256 mismatch"
        xlsx.write_bytes(data)
    import openpyxl
    wb = openpyxl.load_workbook(xlsx, read_only=True)
    ws = wb.active
    it = ws.iter_rows(values_only=True)
    hdr = list(next(it))
    iW, iF, iP, iPct = (hdr.index("Word"), hdr.index("FREQcount"),
                        hdr.index("Dom_PoS_SUBTLEX"), hdr.index("Percentage_dom_PoS"))
    lex = {}
    for r in it:
        w = r[iW]
        if w is None: continue
        w = str(w)
        try: fc = int(r[iF] or 0)
        except (TypeError, ValueError): fc = 0
        try: pct = float(r[iPct])
        except (TypeError, ValueError): pct = 0.0
        lex[w] = {"lg": round(math.log10(fc + 1), 4), "pos": r[iP], "pct": pct}
    return lex

# minimal profanity/offensive-term junk filter (membership rule; keeps the instrument clean — the
# forced-choice cancels shared content, so this does not affect the contrast, only register hygiene).
JUNK = frozenset("""shit fuck fucking fucked cunt bitch bastard damn ass asshole dick cock pussy
whore slut nigger fag faggot piss crap wank bollocks twat prick""".split())

def build_pools(lex):
    """Deterministic pools. Membership is the only DoF (G-lexicon-determinism)."""
    names, nouns_sg, adjs = [], [], []
    # nltk-tag isolated forms to keep only genuine singulars in the noun-lemma pool (excludes irregular
    # plurals men/children/feet/data that Dom_PoS 'Noun' alone would admit).
    for w, d in lex.items():
        if not is_alpha(w) or d["pct"] < PCT_DOM: continue
        if w in JUNK: continue                                      # register hygiene (membership filter)
        if w.endswith("ing") or w.endswith("ed"): continue          # gerund/participle/past guard
        if d["pos"] == "Name":
            names.append((w, d["lg"]))
        elif d["pos"] == "Noun" and not looks_plural(w):
            if nltk.pos_tag([w])[0][1] == "NN":                      # singular only
                nouns_sg.append((w, d["lg"]))
        elif d["pos"] == "Adjective":
            adjs.append((w, d["lg"]))
    names.sort(key=lambda x: x[1]); nouns_sg.sort(key=lambda x: x[1]); adjs.sort(key=lambda x: x[1])
    return names, nouns_sg, adjs

# ---- 2. swap engine --------------------------------------------------------
def detok(ts):
    s = " ".join(ts)
    s = re.sub(r"\s+([.,;:!?])", r"\1", s); s = re.sub(r"\s+n't", "n't", s)
    s = re.sub(r"\s+'(s|re|ve|ll|d|m)\b", r"'\1", s); s = re.sub(r"\s+'", "'", s)
    return s

def fix_articles(ts):
    out = ts[:]
    for i in range(len(out) - 1):
        low = out[i].lower()
        if low in ("a", "an"):
            nxt = re.sub(r"[^a-z]", "", out[i + 1].lower())
            art = "an" if nxt[:1] in "aeiou" else "a"
            out[i] = art.capitalize() if out[i][:1].isupper() else art
    return out

def cap_like(o, n): return n.capitalize() if o[:1].isupper() else n

def locus_idx(g, b):
    sm = difflib.SequenceMatcher(a=g, b=b, autojunk=False); L = set()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal": L.update(range(i1, i2))
    return L

def pick(pool, target, seedkey, need_form=None, lex=None):
    """Deterministic seeded freq-matched pick from the full eligible in-band set (G-lexicon-determinism)."""
    elig = [l for l, g in pool if abs(g - target) <= BAND]
    if not elig: return None
    rng = random.Random(int(hashlib.sha256(seedkey.encode()).hexdigest()[:12], 16))
    order = elig[:]; rng.shuffle(order)
    for l in order:
        form = need_form(l) if need_form else l
        if form in lex and abs(lex[form]["lg"] - target) <= BAND:
            return l
    return None

def swap_pair(uid, pid, good, bad, family, pools, lex):
    names, nouns_sg, adjs = pools
    g = nltk.word_tokenize(good); b = nltk.word_tokenize(bad)
    tags = nltk.pos_tag(g); L = locus_idx(g, b)
    gnew, bnew, subs = g[:], b[:], []
    content = 0
    detnoun = family == "det_noun"
    for i, (w, t) in enumerate(tags):
        wl = w.lower()
        is_noun = t in ("NN", "NNS") and lex.get(wl, {}).get("pos") == "Noun"
        is_name = t in ("NNP", "NNPS") and bool(re.fullmatch(r"[A-Z][a-z]+", w))
        is_adj = t == "JJ" and lex.get(wl, {}).get("pos") == "Adjective"
        if is_noun or is_name or is_adj: content += 1
        if wl.endswith("ing"): continue
        in_locus = i in L
        # det-noun carve-out: locus head noun swapped, number preserved; irregular pairs dropped (G-frame).
        if in_locus and detnoun and is_noun:
            gw, bw = g[i].lower(), (b[i].lower() if i < len(b) else "")
            if pluralize(gw) == bw: sg_is, gpl, bpl = "g", False, True
            elif pluralize(bw) == gw: sg_is, gpl, bpl = "b", True, False
            else:
                return None                     # irregular / unexpected contrast noun -> drop pair
            base = lex.get(gw if not gpl else singularize(gw), {}).get("lg") or lex.get(gw, {}).get("lg") or 2.0
            newl = pick(nouns_sg, base, f"{uid}|{pid}|{i}|dn", need_form=lambda l: pluralize(l), lex=lex)
            if not newl: return None
            gform = pluralize(newl) if gpl else newl
            bform = pluralize(newl) if bpl else newl
            gnew[i] = cap_like(w, gform)
            if i < len(bnew): bnew[i] = cap_like(bnew[i], bform)
            subs.append(("dn-noun", w, gnew[i])); continue
        if in_locus: continue
        if is_name:
            # sv guard: a proper name BEFORE the agreement locus is the subject; its number is ambiguous,
            # so swapping it could flip subject-verb agreement (e.g. plural "the Borgias" -> a singular
            # name). Hold subject names fixed in sv paradigms (objects, after the verb, stay swappable).
            if family == "sv" and L and i < min(L):
                continue
            tl = lex.get(wl, {}).get("lg"); target = tl if tl is not None else names[len(names) // 2][1]
            nn = pick(names, target, f"{uid}|{pid}|{i}|nm", lex=lex)
            if nn:
                gnew[i] = cap_like(w, nn)
                for j, x in enumerate(bnew):
                    if x == w: bnew[j] = cap_like(x, nn)
                subs.append(("name", w, nn, tl is not None))
        elif is_noun:
            left = tags[i - 1][1] if i > 0 else "DT"
            if left not in NP_LEFT: continue           # require NP-internal context (excludes bare verbs)
            plural = looks_plural(wl); lemma = singularize(wl) if plural else wl
            base = lex.get(wl, {}).get("lg") or lex.get(lemma, {}).get("lg") or 2.0
            newl = pick(nouns_sg, base, f"{uid}|{pid}|{i}|nn",
                        need_form=lambda l: (pluralize(l) if plural else l), lex=lex)
            if newl:
                form = pluralize(newl) if plural else newl
                gnew[i] = cap_like(w, form)
                for j, x in enumerate(bnew):
                    if x == w: bnew[j] = cap_like(x, form)
                subs.append(("noun", w, form))
        elif is_adj:
            nxt = tags[i + 1][1] if i + 1 < len(tags) else ""
            if nxt not in ("NN", "NNS", "JJ"): continue   # attributive only
            base = lex.get(wl, {}).get("lg") or 2.0
            na = pick(adjs, base, f"{uid}|{pid}|{i}|jj", lex=lex)
            if na:
                gnew[i] = cap_like(w, na)
                for j, x in enumerate(bnew):
                    if x == w: bnew[j] = cap_like(x, na)
                subs.append(("adj", w, na))
    gnew = fix_articles(gnew); bnew = fix_articles(bnew)
    # ---- Q3-A mechanical re-validation (drop, never repair) --------------------------------------
    if not subs: return None                                  # (i) at least one swap
    gs, bs = detok(gnew), detok(bnew)
    if gs == good and bs == bad: return None                  # nothing changed
    if gs == bs: return None                                  # (iv) swap collapsed the contrast
    # (ii/iv) the good/bad contrast must survive with the SAME structure: same number of differing
    # token-positions between the swapped good and bad as between the original good and bad.
    orig_locus = locus_idx(nltk.word_tokenize(good), nltk.word_tokenize(bad))
    swap_locus = locus_idx(nltk.word_tokenize(gs), nltk.word_tokenize(bs))
    if len(swap_locus) != len(orig_locus): return None        # contrast changed shape -> drop
    # (iii) no residual "a/an"-before-vowel error introduced by the swap
    for s in (gs, bs):
        if re.search(r"\b[Aa] [aeiou]", s) or re.search(r"\b[Aa]n [^aeiou ]", s): return None
    return {"pairID": pid, "good": good, "bad": bad, "good_swap": gs, "bad_swap": bs,
            "subs": subs, "nsub": len(subs), "ncontent": content,
            "coverage": round(len(subs) / max(content, 1), 3)}

# ---- 3. selection + build --------------------------------------------------
def fetch_paradigm(uid):
    dest = CACHE / f"{uid}.jsonl"
    if not dest.exists():
        for attempt in range(4):
            try:
                urllib.request.urlretrieve(BLIMP_URL.format(uid), dest); break
            except Exception:
                if attempt == 3: raise
    pairs = [json.loads(l) for l in open(dest) if l.strip()]
    sha = sha256_bytes(open(dest, "rb").read())
    return pairs, sha

def swappability_score(uid, pairs, family, pools, lex):
    rng = random.Random(int(hashlib.sha256(f"{SEL_SEED}-{uid}".encode()).hexdigest()[:12], 16))
    samp = rng.sample(pairs, min(SEL_N, len(pairs)))
    counts = []
    for p in samp:
        r = swap_pair(uid, str(p.get("pairID")), p["sentence_good"], p["sentence_bad"], family, pools, lex)
        counts.append(r["nsub"] if r else 0)
    return sum(counts) / len(counts)

def family_of(uid):
    return "det_noun" if uid in DET_NOUN_FAMILY else ("sv" if "subject_verb" in uid else "deep")

def main():
    lex = load_lexicon()
    pools = build_pools(lex)
    names, nouns_sg, adjs = pools
    pool_sha = sha256_bytes(json.dumps({"names": names, "nouns_sg": nouns_sg, "adjs": adjs},
                                       sort_keys=True).encode())

    # score + select (blind to accuracy/human)
    sha_map = {}; scores = {}
    cand_pairs = {}
    for uid in SHALLOW_CANDIDATES + DEEP_CANDIDATES:
        pairs, sha = fetch_paradigm(uid); sha_map[uid] = sha; cand_pairs[uid] = pairs
        scores[uid] = round(swappability_score(uid, pairs, family_of(uid), pools, lex), 4)
    def top3(cands):
        return sorted(cands, key=lambda u: (-scores[u], u))[:3]
    sel_shallow = top3(SHALLOW_CANDIDATES); sel_deep = top3(DEEP_CANDIDATES)
    selected = [(u, "shallow") for u in sel_shallow] + [(u, "deep") for u in sel_deep]

    # build the fresh ~100-pair swapped instrument for the selected 6
    items = {}; report = []
    for uid, stratum in selected:
        pairs = cand_pairs[uid]; fam = family_of(uid)
        rng = random.Random(int(hashlib.sha256(f"{SEED}-{uid}".encode()).hexdigest()[:12], 16))
        samp = rng.sample(pairs, min(SAMPLE_N, len(pairs)))
        usable, drops = [], 0
        for p in samp:
            if len(usable) >= TARGET_N: break
            r = swap_pair(uid, str(p.get("pairID")), p["sentence_good"], p["sentence_bad"], fam, pools, lex)
            if r is None: drops += 1; continue
            usable.append(r)
        items[uid] = usable
        covs = [r["coverage"] for r in usable]; nsubs = [r["nsub"] for r in usable]
        report.append({"uid": uid, "stratum": stratum, "family": fam, "n_usable": len(usable),
                       "drops_in_scan": drops, "mean_coverage": round(sum(covs) / len(covs), 3),
                       "mean_nsub": round(sum(nsubs) / len(nsubs), 2),
                       "below_floor": len(usable) < USABLE_FLOOR})

    out = {"seed": SEED, "sel_seed": SEL_SEED, "band": BAND, "target_n": TARGET_N,
           "pool_sizes": {"names": len(names), "nouns_sg": len(nouns_sg), "adjs": len(adjs)},
           "pool_sha_partial": pool_sha,
           "subtlex_xlsx_sha256": SUBTLEX_XLSX_SHA,
           "swappability_scores": scores,
           "selected_shallow": sel_shallow, "selected_deep": sel_deep,
           "paradigm_sha256": sha_map, "build_report": report}
    json.dump(out, open(HERE / "selection.json", "w"), indent=1)
    json.dump({"seed": SEED, "selected": [u for u, _ in selected],
               "strata": {u: s for u, s in selected}, "items": items},
              open(HERE / "items_swap.json", "w"), indent=1)

    print("=== SELECTION (swappability score = mean swappable positions/item; blind to acc/human) ===")
    for u in SHALLOW_CANDIDATES: print(f"  shallow {u:46s} {scores[u]:.3f}{'  <SELECTED>' if u in sel_shallow else ''}")
    for u in DEEP_CANDIDATES: print(f"  deep    {u:46s} {scores[u]:.3f}{'  <SELECTED>' if u in sel_deep else ''}")
    print(f"\npools: names={len(names)} nouns_sg={len(nouns_sg)} adjs={len(adjs)}")
    print("\n=== BUILD REPORT (G-coverage) ===")
    for r in report:
        print(f"  [{r['stratum']:7s}] {r['uid']:46s} n={r['n_usable']:3d} cov={r['mean_coverage']:.2f} "
              f"nsub={r['mean_nsub']:.1f} drops={r['drops_in_scan']}{'  <BELOW FLOOR>' if r['below_floor'] else ''}")
    # audit sample
    print("\n=== AUDIT SAMPLE (2 pairs/selected paradigm) ===")
    for uid, _ in selected:
        for r in items[uid][:2]:
            print(f"[{uid}]")
            print("  o+", r["good"]); print("  o-", r["bad"])
            print("  s+", r["good_swap"]); print("  s-", r["bad_swap"], f"(cov={r['coverage']})")


if __name__ == "__main__":
    main()
