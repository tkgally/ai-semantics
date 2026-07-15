#!/usr/bin/env python3
"""build_swap_c4.py — FROZEN builder for the BLiMP R1 C4-FREQUENCY-MATCHED content-word-swap arm
(A3b, s232; the s210 SWAP-INCONCLUSIVE honest successor).

RATIFIED s232 (decisions/resolved/blimp-c4-matched-swap-arm-design): Q1-A DUAL-BAND / Q2-A / Q3-A, with the
s231-critic BLOCKERS + the s232 ratification-vote condition folded into the BLIND, PRE-COMMITTED numeric
rules pinned below. This script is a SELF-CONTAINED fork of the s210 build_swap.py: the substitution recipe,
POS/morphology guards, det-noun carve-out, sv guard, and mechanical re-validation are BYTE-IDENTICAL to
s210 (verifier asserts this against the s210 source). The ONLY new operationalization is Q1-A: each
substitute must fall inside BOTH the ±0.10 SUBTLEX-US Lg10WF band (s210) AND a ±0.30 C4 pretraining-proxy
log-frequency band of the original — the INTERSECTION pool, seeded-deterministic selection.

WHY A SEPARATE FILE (not an import): the frozen recipe must be reproducible from ITSELF alone (G5-plus);
the s210 helpers are copied verbatim so the verifier can byte-diff them against s210/build_swap.py.

PIPELINE (deterministic, seeded; $0 model cost — build compute + a bounded C4 stream):
  0. Load the frozen DISJOINT pair sample (disjoint_sample.json, pinned + sha'd at FREEZE, s232 — the 6
     s210 paradigms, a fresh seed, drawn from pairs MINUS the s210 kept ids so disjointness is guaranteed
     by construction). The paradigm selection is INHERITED byte-frozen from s210 (same 6 uids).
  1. Load + sha-pin the 2012 SUBTLEX-US-with-PoS file -> the same content pools as s210 (names / singular
     nouns / attributive adjectives). Membership is the only lexicon DoF (G-lexicon-determinism).
  2. Build the C4 target vocabulary = all pool lemmas + their rule-pluralizations + every open-class form in
     the frozen sample's good/bad sentences. Stream the s208/s210 C4 adapter (build_cooc_c4.stream_sentences)
     over a BOUNDED, PINNED prefix (NUM_SHARDS=3 => ~22.3M sentences, the covariate-arm scale, S2 adopted)
     and count unigram occurrences of the target vocab. c4log(w) = log10(count[w] + 1). $0 model cost.
  3. For each frozen pair, build the swapped counterpart with pick_c4(): a substitute must be in-band on
     BOTH SUBTLEX (±0.10) AND C4 (±0.30) of the original FORM. Empty/below-floor intersections are
     DROPPED-AND-LOGGED (never band-widened). The pre-committed BLIND Q1-A->Q1-B fallback trigger is
     evaluated on the observed empty-intersection FRACTION (blind to model accuracies).
  4. Emit selection_c4.json (pools, C4 band report, per-position pool-size distribution, the trigger
     evaluation), items_swap_c4.json (ORIGINAL + C4-matched SWAP good/bad per pair), build_report_c4.txt.

Outputs are the frozen instrument; probe.py then runs BOTH conditions (orig + C4-swap) fresh, both orders,
so the swapped accuracies are UNKNOWN at freeze (anti-cheat). analyze_swap_c4.py scores + reports the
achieved per-word AND set-mean C4 gap (G-C4-match-adequacy) and applies the four-outcome decision table.
"""
import csv, hashlib, io, json, math, os, random, re, sys, urllib.request, zipfile, difflib
import importlib.util
from pathlib import Path
from collections import Counter
import nltk

HERE = Path(__file__).parent
CACHE = HERE / ".cache"
CACHE.mkdir(exist_ok=True)

# ---- frozen constants (PREREG s232) ---------------------------------------
# INHERITED byte-frozen from the s210 PREREG:
SEL_PARADIGMS = {                                  # the 6 s210-selected uids (selection inherited, not re-run)
    "determiner_noun_agreement_2": "shallow",
    "determiner_noun_agreement_1": "shallow",
    "regular_plural_subject_verb_agreement_1": "shallow",
    "sentential_negation_npi_scope": "deep",
    "only_npi_scope": "deep",
    "superlative_quantifiers_1": "deep",
}
TARGET_N = 100                     # target usable paired items/paradigm (G-power, inherited)
SAMPLE_N = 160                     # draw this many (from the disjoint pool), keep first TARGET_N usable
                                   #   (SHOULD-FIX 7: 130->160 headroom so dual-band attrition still reaches TARGET_N)
USABLE_FLOOR = 60                  # below this a paradigm is dropped + power re-stated (G-power, inherited)
BAND = 0.10                        # ±0.10 SUBTLEX-US Lg10WF band (s210, inherited)
PCT_DOM = 0.75                     # Dom_PoS dominance floor for pool membership (junk filter, inherited)

# NEW this design (Q1-A DUAL-BAND; all BLIND + PRE-COMMITTED, decided before build, blind to accuracies):
C4_BAND = 0.30                     # ±0.30 C4 log-freq band half-width (Q1-A default; G-C4-band)
C4_NUM_SHARDS = 3                  # S2 ADOPTED: the covariate-arm C4 scale (~22.3M sentences), not the 3M diag
POOL_FLOOR = 5                     # per-position minimum INTERSECTION size to treat a position as matchable;
                                   #   an intersection with < POOL_FLOOR candidates is DROPPED-AND-LOGGED (G-C4-band)
TRIGGER_FRAC = 0.25                # BLIND Q1-A->Q1-B fallback: if > 25% of swap-eligible positions are dropped
                                   #   for a below-floor/empty intersection, the WHOLE build re-runs under Q1-B
                                   #   (C4-primary; SUBTLEX reported, not bound). Pre-committed, blind to accuracies.

SUBTLEX_ZIP = ("https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/"
               "subtlexus/subtlexus1.zip")
SUBTLEX_ZIP_SHA = "458128f90a28c4f396cb2a5b23ac93c56f745ee8cfca9be2afedad4091d15090"
SUBTLEX_XLSX_SHA = "3a8cb93a4e28988c2ce722a63f6b8d394acdc42ebe2ab6e1f0e484ee0d4167a7"

BLIMP_URL = "https://raw.githubusercontent.com/alexwarstadt/blimp/master/data/{}.jsonl"
DET_NOUN_FAMILY = {"determiner_noun_agreement_1", "determiner_noun_agreement_2"}
NP_LEFT = {"DT", "JJ", "JJR", "JJS", "IN", "PRP$", "POS", "NN", "NNS", "NNP", "NNPS", "CD", "PDT", "WDT", "TO"}

# the s208/s210 C4 streaming adapter (import-pinned; no new corpus adoption; ODC-BY read firsthand)
C4_ADAPTER = HERE / ".." / "2026-07-08-relation-recovery-taxonomic-proxy" / "build_cooc_c4.py"

# ---- morphology helpers (BYTE-IDENTICAL to s210 build_swap.py) -------------
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

# ---- 1. lexicon + pools (BYTE-IDENTICAL to s210 build_swap.py) -------------
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

JUNK = frozenset("""shit fuck fucking fucked cunt bitch bastard damn ass asshole dick cock pussy
whore slut nigger fag faggot piss crap wank bollocks twat prick""".split())

def build_pools(lex):
    names, nouns_sg, adjs = [], [], []
    for w, d in lex.items():
        if not is_alpha(w) or d["pct"] < PCT_DOM: continue
        if w in JUNK: continue
        if w.endswith("ing") or w.endswith("ed"): continue
        if d["pos"] == "Name":
            names.append((w, d["lg"]))
        elif d["pos"] == "Noun" and not looks_plural(w):
            if nltk.pos_tag([w])[0][1] == "NN":
                nouns_sg.append((w, d["lg"]))
        elif d["pos"] == "Adjective":
            adjs.append((w, d["lg"]))
    names.sort(key=lambda x: x[1]); nouns_sg.sort(key=lambda x: x[1]); adjs.sort(key=lambda x: x[1])
    return names, nouns_sg, adjs

# ---- 2. C4 counting (NEW — the only added pass; $0 model cost) -------------
def load_c4_adapter():
    spec = importlib.util.spec_from_file_location("build_cooc_c4", C4_ADAPTER)
    cooc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cooc)
    return cooc

def build_c4_targets(sample, pools):
    """Deterministic C4 target vocabulary: pool lemmas + their rule-pluralizations + every lowercase
    alphabetic token in the frozen sample's good/bad sentences. The stream only counts these (dict
    membership), so a large target set is free."""
    names, nouns_sg, adjs = pools
    targets = set()
    for l, _ in names + nouns_sg + adjs:
        targets.add(l); targets.add(pluralize(l))
    for uid, pairs in sample.items():
        for p in pairs:
            for s in (p["sentence_good"], p["sentence_bad"]):
                for t in re.findall(r"[a-z]+", s.lower()):
                    targets.add(t)
    return targets

def count_c4(targets, cooc):
    counts = {w: 0 for w in targets}
    seen = 0
    # bound the stream at the covariate-arm scale (S2): NUM_SHARDS shards of the C4 adapter
    orig_shards = getattr(cooc, "NUM_SHARDS", None)
    try:
        cooc.NUM_SHARDS = C4_NUM_SHARDS
        for toks in cooc.stream_sentences():
            for t in toks:
                if t in counts: counts[t] += 1
            seen += 1
    finally:
        if orig_shards is not None: cooc.NUM_SHARDS = orig_shards
    return counts, seen

def c4log(w, c4):
    return math.log10(c4.get(w, 0) + 1)

# ---- 3. swap engine (BYTE-IDENTICAL to s210 EXCEPT pick_c4 dual-band) ------
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

def pick_c4(pool, target, seedkey, c4, c4_target, mode, stats, need_form=None, lex=None):
    """DUAL-BAND (Q1-A) seeded freq-matched pick. eligible = in-band on SUBTLEX (±BAND) AND, in dual-band
    mode, in-band on C4 (±C4_BAND) of the original FORM. Q1-B (c4_primary) drops the SUBTLEX bind and keeps
    only the C4 band. Returns (lemma | None). stats['elig_sizes'] accumulates the per-position intersection
    size; a below-floor/empty intersection returns None and is counted as a dropped position (the BLIND
    Q1-A->Q1-B trigger reads this fraction)."""
    if mode == "c4_primary":
        elig = [l for l, g in pool if abs(c4log(form0(l, need_form), c4) - c4_target) <= C4_BAND]
    else:  # dual-band (default)
        elig = [l for l, g in pool
                if abs(g - target) <= BAND
                and abs(c4log(form0(l, need_form), c4) - c4_target) <= C4_BAND]
    stats["elig_sizes"].append(len(elig))
    if len(elig) < POOL_FLOOR:
        stats["below_floor"] += 1
        return None
    rng = random.Random(int(hashlib.sha256(seedkey.encode()).hexdigest()[:12], 16))
    order = elig[:]; rng.shuffle(order)
    for l in order:
        form = need_form(l) if need_form else l
        subtlex_ok = (mode == "c4_primary") or (form in lex and abs(lex[form]["lg"] - target) <= BAND)
        c4_ok = abs(c4log(form, c4) - c4_target) <= C4_BAND
        if subtlex_ok and c4_ok:
            return l
    return None

def form0(l, need_form):
    """the surface form a lemma would take (for C4 lookup at eligibility time)."""
    return need_form(l) if need_form else l

def swap_pair(uid, pid, good, bad, family, pools, lex, c4, mode, stats):
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
        if in_locus and detnoun and is_noun:
            gw, bw = g[i].lower(), (b[i].lower() if i < len(b) else "")
            if pluralize(gw) == bw: sg_is, gpl, bpl = "g", False, True
            elif pluralize(bw) == gw: sg_is, gpl, bpl = "b", True, False
            else:
                return None
            lemma0 = gw if not gpl else singularize(gw)
            base = lex.get(lemma0, {}).get("lg") or lex.get(gw, {}).get("lg") or 2.0
            c4t = c4log(gw, c4)                                          # C4 of the ORIGINAL locus form
            newl = pick_c4(nouns_sg, base, f"{uid}|{pid}|{i}|dn", c4, c4t, mode, stats,
                           need_form=lambda l: pluralize(l), lex=lex)
            if not newl: return None
            gform = pluralize(newl) if gpl else newl
            bform = pluralize(newl) if bpl else newl
            gnew[i] = cap_like(w, gform)
            if i < len(bnew): bnew[i] = cap_like(bnew[i], bform)
            subs.append(("dn-noun", w, gnew[i])); continue
        if in_locus: continue
        if is_name:
            if family == "sv" and L and i < min(L):
                continue
            tl = lex.get(wl, {}).get("lg"); target = tl if tl is not None else names[len(names) // 2][1]
            c4t = c4log(wl, c4)
            nn = pick_c4(names, target, f"{uid}|{pid}|{i}|nm", c4, c4t, mode, stats, lex=lex)
            if nn:
                gnew[i] = cap_like(w, nn)
                for j, x in enumerate(bnew):
                    if x == w: bnew[j] = cap_like(x, nn)
                subs.append(("name", w, nn, tl is not None))
        elif is_noun:
            left = tags[i - 1][1] if i > 0 else "DT"
            if left not in NP_LEFT: continue
            plural = looks_plural(wl); lemma = singularize(wl) if plural else wl
            base = lex.get(wl, {}).get("lg") or lex.get(lemma, {}).get("lg") or 2.0
            c4t = c4log(wl, c4)
            newl = pick_c4(nouns_sg, base, f"{uid}|{pid}|{i}|nn", c4, c4t, mode, stats,
                           need_form=lambda l: (pluralize(l) if plural else l), lex=lex)
            if newl:
                form = pluralize(newl) if plural else newl
                gnew[i] = cap_like(w, form)
                for j, x in enumerate(bnew):
                    if x == w: bnew[j] = cap_like(x, form)
                subs.append(("noun", w, form))
        elif is_adj:
            nxt = tags[i + 1][1] if i + 1 < len(tags) else ""
            if nxt not in ("NN", "NNS", "JJ"): continue
            base = lex.get(wl, {}).get("lg") or 2.0
            c4t = c4log(wl, c4)
            na = pick_c4(adjs, base, f"{uid}|{pid}|{i}|jj", c4, c4t, mode, stats, lex=lex)
            if na:
                gnew[i] = cap_like(w, na)
                for j, x in enumerate(bnew):
                    if x == w: bnew[j] = cap_like(x, na)
                subs.append(("adj", w, na))
    gnew = fix_articles(gnew); bnew = fix_articles(bnew)
    # ---- Q3-A mechanical re-validation (BYTE-IDENTICAL to s210; drop, never repair) --------------
    if not subs: return None
    gs, bs = detok(gnew), detok(bnew)
    if gs == good and bs == bad: return None
    if gs == bs: return None
    orig_locus = locus_idx(nltk.word_tokenize(good), nltk.word_tokenize(bad))
    swap_locus = locus_idx(nltk.word_tokenize(gs), nltk.word_tokenize(bs))
    if len(swap_locus) != len(orig_locus): return None
    for s in (gs, bs):
        if re.search(r"\b[Aa] [aeiou]", s) or re.search(r"\b[Aa]n [^aeiou ]", s): return None
    # record the per-sub achieved C4 gaps (G-C4-match-adequacy input) for the frozen items
    sub_c4 = []
    for sub in subs:
        orig_form, new_form = sub[1].lower(), sub[2].lower()
        sub_c4.append([round(c4log(orig_form, c4), 4), round(c4log(new_form, c4), 4)])
    return {"pairID": pid, "good": good, "bad": bad, "good_swap": gs, "bad_swap": bs,
            "subs": subs, "nsub": len(subs), "ncontent": content, "sub_c4": sub_c4,
            "coverage": round(len(subs) / max(content, 1), 3)}

# ---- 4. sample loading + build --------------------------------------------
def family_of(uid):
    return "det_noun" if uid in DET_NOUN_FAMILY else ("sv" if "subject_verb" in uid else "deep")

def build_for_mode(sample, pools, lex, c4, mode):
    """Run the whole build under one mode ('dual' or 'c4_primary'); return (items, report, stats)."""
    items, report = {}, []
    stats = {"elig_sizes": [], "below_floor": 0, "n_eligible_positions": 0}
    for uid, sstratum in SEL_PARADIGMS.items():
        fam = family_of(uid)
        usable, drops = [], 0
        for p in sample[uid]:
            if len(usable) >= TARGET_N: break
            r = swap_pair(uid, str(p.get("pairID")), p["sentence_good"], p["sentence_bad"],
                          fam, pools, lex, c4, mode, stats)
            if r is None: drops += 1; continue
            usable.append(r)
        items[uid] = usable
        covs = [r["coverage"] for r in usable] or [0.0]
        nsubs = [r["nsub"] for r in usable] or [0]
        report.append({"uid": uid, "stratum": sstratum, "family": fam, "n_usable": len(usable),
                       "drops_in_scan": drops, "mean_coverage": round(sum(covs) / len(covs), 3),
                       "mean_nsub": round(sum(nsubs) / len(nsubs), 2),
                       "below_floor": len(usable) < USABLE_FLOOR})
    stats["n_eligible_positions"] = len(stats["elig_sizes"])
    return items, report, stats

def main():
    # 0. frozen disjoint sample (pinned at FREEZE)
    sample_path = HERE / "disjoint_sample.json"
    assert sample_path.exists(), "disjoint_sample.json (frozen at freeze) missing"
    disj = json.load(open(sample_path))
    sample = disj["sample"]                                   # uid -> [ {pairID, sentence_good, sentence_bad}, ... ]
    assert set(sample) == set(SEL_PARADIGMS), "disjoint sample paradigms != frozen selection"

    # 1. lexicon + pools
    lex = load_lexicon()
    pools = build_pools(lex)
    names, nouns_sg, adjs = pools
    pool_sha = sha256_bytes(json.dumps({"names": names, "nouns_sg": nouns_sg, "adjs": adjs},
                                       sort_keys=True).encode())

    # 2. C4 counting over the target vocab (S2 scale, PINNED)
    cooc = load_c4_adapter()
    targets = build_c4_targets(sample, pools)
    c4, c4_seen = count_c4(targets, cooc)

    # 3. build under Q1-A (dual-band); evaluate the BLIND Q1-A->Q1-B trigger on the empty/below-floor fraction
    items, report, stats = build_for_mode(sample, pools, lex, c4, "dual")
    below_frac = (stats["below_floor"] / stats["n_eligible_positions"]) if stats["n_eligible_positions"] else 0.0
    mode = "dual"
    fallback = {"triggered": bool(below_frac > TRIGGER_FRAC), "below_frac": round(below_frac, 4),
                "trigger_frac": TRIGGER_FRAC, "pool_floor": POOL_FLOOR}
    if fallback["triggered"]:
        mode = "c4_primary"
        items, report, stats = build_for_mode(sample, pools, lex, c4, "c4_primary")
        below_frac = (stats["below_floor"] / stats["n_eligible_positions"]) if stats["n_eligible_positions"] else 0.0
        fallback["c4_primary_below_frac"] = round(below_frac, 4)

    # F2 (freeze critic): compute the B3 adequacy set-mean C4 gap at BUILD time (blind, no accuracy) so a
    # MATCH-FAILURE is caught BEFORE the ~$1.3-1.6 probe spend. |signed set-mean gap| must be <= 0.05
    # (MAX_SETMEAN_C4_GAP in analyze_swap_c4.py) or the run lands STILL-INCONCLUSIVE-BY-MATCH-FAILURE.
    signed_gaps = [oc - nc for uid in SEL_PARADIGMS for p in items[uid] for oc, nc in p.get("sub_c4", [])]
    g_c4 = round(sum(signed_gaps) / len(signed_gaps), 4) if signed_gaps else 0.0
    MAX_SETMEAN_C4_GAP = 0.05
    adequacy = {"signed_set_mean_c4_gap": g_c4, "abs": round(abs(g_c4), 4), "n_subs": len(signed_gaps),
                "threshold": MAX_SETMEAN_C4_GAP, "adequate_at_build": bool(abs(g_c4) <= MAX_SETMEAN_C4_GAP)}

    elig = stats["elig_sizes"] or [0]
    out = {"mode": mode, "fallback": fallback, "build_adequacy": adequacy,
           "c4_band": C4_BAND, "c4_num_shards": C4_NUM_SHARDS,
           "c4_sentences_streamed": c4_seen, "subtlex_band": BAND, "target_n": TARGET_N,
           "pool_sizes": {"names": len(names), "nouns_sg": len(nouns_sg), "adjs": len(adjs)},
           "pool_sha_partial": pool_sha, "subtlex_xlsx_sha256": SUBTLEX_XLSX_SHA,
           "disjoint_sample_sha256": disj["sample_sha256"],
           "n_c4_targets": len(targets),
           "intersection_pool_size": {"min": int(min(elig)), "median": int(sorted(elig)[len(elig) // 2]),
                                        "mean": round(sum(elig) / len(elig), 2), "n_positions": len(elig),
                                        "n_below_floor": stats["below_floor"]},
           "selected": list(SEL_PARADIGMS), "strata": dict(SEL_PARADIGMS), "build_report": report}
    json.dump(out, open(HERE / "selection_c4.json", "w"), indent=1)
    json.dump({"mode": mode, "selected": list(SEL_PARADIGMS), "strata": dict(SEL_PARADIGMS),
               "items": items}, open(HERE / "items_swap_c4.json", "w"), indent=1)

    print("=== C4-MATCHED SWAP BUILD (s232) — mode:", mode, "===")
    print(f"C4 stream: {c4_seen} sentences ({C4_NUM_SHARDS} shards), {len(targets)} target words")
    print(f"B3 adequacy (BUILD-TIME, blind): signed set-mean C4 gap {g_c4:+.4f} (|·| {abs(g_c4):.4f} vs "
          f"<={MAX_SETMEAN_C4_GAP}) -> {'ADEQUATE' if adequacy['adequate_at_build'] else 'MATCH-FAILURE'}"
          + ("" if adequacy['adequate_at_build']
             else "  <<< DO NOT SPEND: run would land STILL-INCONCLUSIVE-BY-MATCH-FAILURE >>>"))
    print(f"intersection pool/position: min={min(elig)} median={sorted(elig)[len(elig)//2]} "
          f"mean={sum(elig)/len(elig):.1f}  below-floor(<{POOL_FLOOR})={stats['below_floor']}/{len(elig)} "
          f"({below_frac:.3f})  Q1-A->Q1-B trigger(>{TRIGGER_FRAC})={'FIRED' if fallback['triggered'] else 'not fired'}")
    print("\n=== BUILD REPORT (G-coverage floor 0.50; USABLE_FLOOR 60) ===")
    for r in report:
        print(f"  [{r['stratum']:7s}] {r['uid']:46s} n={r['n_usable']:3d} cov={r['mean_coverage']:.2f} "
              f"nsub={r['mean_nsub']:.1f} drops={r['drops_in_scan']}{'  <BELOW FLOOR>' if r['below_floor'] else ''}")
    print("\n=== AUDIT SAMPLE (2 pairs/paradigm) ===")
    for uid in SEL_PARADIGMS:
        for r in items[uid][:2]:
            print(f"[{uid}]"); print("  o+", r["good"]); print("  o-", r["bad"])
            print("  s+", r["good_swap"]); print("  s-", r["bad_swap"], f"(cov={r['coverage']})")


if __name__ == "__main__":
    main()
