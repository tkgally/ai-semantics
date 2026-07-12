"""Analyze the Japanese CC replication (A6, 2026-07-13, s215) — magnitudes WITH intervals.

Byte-parallel to the frozen English POWERED analyzer
(experiments/runs/2026-07-02-comparative-correlative-powered/analyze.py): the SAME quantities
(assertion-rate T1 gap, inverse-flip, positive-increase, typical-vs-atypical robustness, atypical
assertion, NLI cc-vs-ctrl gap, FC/NLI CC accuracy) with 95% CIs via a CLUSTER bootstrap over scale
PAIRS (2000 resamples, fixed seed) — the honest interval for the nested four-form design. The
frozen thresholds (T1>=30pp / T2>=70% / T3 within 15pp) are reported for continuity with English v1
but the deliverable is the point estimate + CI.

ADDED for the Japanese run: the Q2-B FREQUENCY/CO-OCCURRENCE CONTROL readout (freeze condition vi),
reading the FROZEN freq_control.json (UD Japanese-GSD content-word frequency + per-pair co-occurrence,
built before the run by build_cooc_de.py). It reports whether the CC covariation-assertion tracks
corpus frequency/association — the residual-frequency loophole a cross-linguistic anti-template
argument must close. The PRIMARY co-occurrence control remains the typical-vs-atypical split.

Emits raw/results.json (machine) and prints a human table. No item-level cherry-picking; no retuning.
"""
import json, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
FREQ = os.path.join(HERE, "freq_control.json")
PANEL = ["A", "B", "C"]
MODELS = {"A": "anthropic/claude-sonnet-4.6",
          "B": "openai/gpt-5.4-mini",
          "C": "google/gemini-3.5-flash"}
B_BOOT = 2000
SEED = 20260713


def load(arm, slot):
    return json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))


# ---- point statistics (identical to the English analyzer) ----
def _asrt(recs):
    p = [r for r in recs if r["pred"] is not None]
    if not p:
        return None
    return sum(1 for r in p if r["pred"] in ("increase", "decrease")) / len(p)


def _acc(recs, pred_key, gold_key):
    p = [r for r in recs if r[pred_key] is not None]
    if not p:
        return None
    return sum(1 for r in p if str(r[pred_key]) == str(r[gold_key])) / len(p)


def _flip(recs):
    inv = [r for r in recs if r["form"] == "cc-inverse" and r["pred"] is not None]
    if not inv:
        return None
    return sum(1 for r in inv if r["pred"] == "decrease") / len(inv)


def _posinc(recs):
    pos = [r for r in recs if r["form"] == "cc-positive" and r["pred"] is not None]
    if not pos:
        return None
    return sum(1 for r in pos if r["pred"] == "increase") / len(pos)


def stat_t1_gap(fc, nli):
    cc = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")]
    ctrl = [r for r in fc if r["form"] in ("ctrl-two", "ctrl-single")]
    a, b = _asrt(cc), _asrt(ctrl)
    return None if a is None or b is None else (a - b) * 100


def stat_flip(fc, nli):
    v = _flip(fc)
    return None if v is None else v * 100


def stat_posinc(fc, nli):
    v = _posinc(fc)
    return None if v is None else v * 100


def stat_typ_minus_atyp(fc, nli):
    cc = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")]
    typ = _acc([r for r in cc if r["typicality"] == "typical"], "pred", "fc_gold")
    aty = _acc([r for r in cc if r["typicality"] == "atypical"], "pred", "fc_gold")
    return None if typ is None or aty is None else (typ - aty) * 100


def stat_atyp_assert(fc, nli):
    cc_aty = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")
              and r["typicality"] == "atypical"]
    v = _asrt(cc_aty)
    return None if v is None else v * 100


def stat_nli_gap(fc, nli):
    cc = _acc([r for r in nli if r["form"] in ("cc-positive", "cc-inverse")], "pred", "nli_gold")
    ctrl = _acc([r for r in nli if r["form"] in ("ctrl-two", "ctrl-single")], "pred", "nli_gold")
    return None if cc is None or ctrl is None else (cc - ctrl) * 100


def stat_fc_cc_accuracy(fc, nli):
    v = _acc([r for r in fc if r["form"] in ("cc-positive", "cc-inverse")], "pred", "fc_gold")
    return None if v is None else v * 100


def stat_nli_cc_accuracy(fc, nli):
    v = _acc([r for r in nli if r["form"] in ("cc-positive", "cc-inverse")], "pred", "nli_gold")
    return None if v is None else v * 100


STATS = {
    "fc_cc_accuracy_pct": stat_fc_cc_accuracy,
    "fc_T1_assertion_gap_pp": stat_t1_gap,
    "fc_inverse_flip_pct": stat_flip,
    "fc_positive_increase_pct": stat_posinc,
    "fc_typ_minus_atyp_pp": stat_typ_minus_atyp,
    "fc_atypical_assertion_pct": stat_atyp_assert,
    "nli_cc_accuracy_pct": stat_nli_cc_accuracy,
    "nli_cc_vs_ctrl_gap_pp": stat_nli_gap,
}


def cluster_bootstrap(fc, nli, statfn):
    pairs = sorted({r["scale_pair"] for r in fc})
    fc_by = {p: [r for r in fc if r["scale_pair"] == p] for p in pairs}
    nli_by = {p: [r for r in nli if r["scale_pair"] == p] for p in pairs}
    rng = random.Random(SEED)
    vals = []
    n = len(pairs)
    for _ in range(B_BOOT):
        draw = [pairs[rng.randrange(n)] for _ in range(n)]
        fcs, nlis = [], []
        for p in draw:
            fcs.extend(fc_by[p])
            nlis.extend(nli_by[p])
        v = statfn(fcs, nlis)
        if v is not None:
            vals.append(v)
    if not vals:
        return None, None
    vals.sort()
    lo = vals[int(0.025 * len(vals))]
    hi = vals[min(len(vals) - 1, int(0.975 * len(vals)))]
    return round(lo, 1), round(hi, 1)


def analyze_slot(slot):
    fc = load("constructed-fc", slot)
    nli = load("constructed-nli", slot)
    out = {"model": MODELS[slot], "n_fc": len(fc), "n_nli": len(nli),
           "na": {"fc": sum(1 for r in fc if r["pred"] is None),
                  "nli": sum(1 for r in nli if r["pred"] is None)},
           "point": {}, "ci95": {}}
    for name, fn in STATS.items():
        pt = fn(fc, nli)
        out["point"][name] = None if pt is None else round(pt, 1)
        out["ci95"][name] = cluster_bootstrap(fc, nli, fn)
    return out


# ---- Q2-B frequency/co-occurrence control ----
def _spearman(xs, ys):
    """Spearman rho with average ranks; returns None if <3 valid or no variance."""
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    if len(pairs) < 3:
        return None
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        r = [0.0] * len(vals)
        i = 0
        while i < len(vals):
            j = i
            while j + 1 < len(vals) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    xr, yr = ranks([p[0] for p in pairs]), ranks([p[1] for p in pairs])
    n = len(pairs)
    mx, my = sum(xr) / n, sum(yr) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xr, yr))
    dx = sum((a - mx) ** 2 for a in xr) ** 0.5
    dy = sum((b - my) ** 2 for b in yr) ** 0.5
    if dx == 0 or dy == 0:
        return None  # no variance (e.g. assertion at ceiling) -> correlation undefined
    return round(num / (dx * dy), 3)


def freq_control(res_per_slot):
    """Test whether the CC covariation reading tracks UD-Japanese-GSD corpus frequency/co-occurrence."""
    freq = json.load(open(FREQ))
    pairs_meta = freq["pairs"]
    out = {"recipe": freq["recipe"], "corpus_meta": freq["corpus_meta"], "per_model": {}}
    for slot in PANEL:
        fc = load("constructed-fc", slot)
        by_pair = {}
        for r in fc:
            by_pair.setdefault(r["scale_pair"], []).append(r)
        pids = sorted(by_pair)
        cc_assert, ctrl_assert, iso_gap, meanf, cooc, typ = [], [], [], [], [], []
        for pid in pids:
            rs = by_pair[pid]
            cc = [r for r in rs if r["form"] in ("cc-positive", "cc-inverse")]
            ct = [r for r in rs if r["form"] in ("ctrl-two", "ctrl-single")]
            cc_assert.append(_asrt(cc))
            ctrl_assert.append(_asrt(ct))
            a, b = _asrt(cc), _asrt(ct)
            iso_gap.append(None if a is None or b is None else (a - b) * 100)
            meanf.append(pairs_meta[pid]["mean_freq_per_million"])
            cooc.append(pairs_meta[pid]["cooc_sentences_ge2"])
            typ.append(pairs_meta[pid]["typicality"])
        out["per_model"][slot] = {
            "model": MODELS[slot],
            "spearman_ccassert_vs_meanfreq": _spearman(cc_assert, meanf),
            "spearman_isogap_vs_meanfreq": _spearman(iso_gap, meanf),
            "spearman_ctrlassert_vs_cooc": _spearman(ctrl_assert, cooc),
            "cc_assert_typical_mean": round(
                sum(v for v, t in zip(cc_assert, typ) if t == "typical" and v is not None)
                / max(1, sum(1 for v, t in zip(cc_assert, typ) if t == "typical" and v is not None)), 3),
            "cc_assert_atypical_mean": round(
                sum(v for v, t in zip(cc_assert, typ) if t == "atypical" and v is not None)
                / max(1, sum(1 for v, t in zip(cc_assert, typ) if t == "atypical" and v is not None)), 3),
        }
    # corpus-side typical/atypical frequency + co-occurrence (built before the run)
    typ_pairs = [p for p in pairs_meta.values() if p["typicality"] == "typical"]
    aty_pairs = [p for p in pairs_meta.values() if p["typicality"] == "atypical"]
    avg = lambda xs, k: round(sum(x[k] for x in xs) / len(xs), 2)
    out["corpus_side_split"] = {
        "typical_mean_freq_per_million": avg(typ_pairs, "mean_freq_per_million"),
        "atypical_mean_freq_per_million": avg(aty_pairs, "mean_freq_per_million"),
        "typical_cooc_ge2": avg(typ_pairs, "cooc_sentences_ge2"),
        "atypical_cooc_ge2": avg(aty_pairs, "cooc_sentences_ge2"),
    }
    return out


def main():
    res = {slot: analyze_slot(slot) for slot in PANEL}

    T1 = sum(1 for s in PANEL if (res[s]["point"]["fc_T1_assertion_gap_pp"] or -999) >= 30)
    T2 = sum(1 for s in PANEL if (res[s]["point"]["fc_inverse_flip_pct"] or -1) >= 70)
    T3 = sum(1 for s in PANEL if res[s]["point"]["fc_typ_minus_atyp_pp"] is not None
             and abs(res[s]["point"]["fc_typ_minus_atyp_pp"]) <= 15
             and (res[s]["point"]["fc_atypical_assertion_pct"] or 0) > 50)
    gates = {"T1_ge_30pp": f"{T1}/3", "T2_flip_ge_70pct": f"{T2}/3",
             "T3_atypical_within_15pp": f"{T3}/3", "confirm": ">=2/3 each"}

    print("\n===== JAPANESE COMPARATIVE-CORRELATIVE REPLICATION (A6) — MAGNITUDES + 95% CI =====")
    print("34 Japanese scale pairs x 4 forms = 136 items; cluster bootstrap over pairs, B=2000, seed fixed.\n")
    for name in STATS:
        print(f"--- {name} ---")
        for s in PANEL:
            pt = res[s]["point"][name]
            lo, hi = res[s]["ci95"][name]
            ptxt = "  NA" if pt is None else f"{pt:6.1f}"
            citxt = "" if lo is None else f"  [{lo:.1f}, {hi:.1f}]"
            print(f"  {MODELS[s][:26]:<26} {ptxt}{citxt}")
        print()
    print("Frozen-threshold gates (continuity with English v1; not the deliverable):")
    for k, v in gates.items():
        print(f"  {k}: {v}")

    fq = freq_control(res)
    print("\n--- Q2-B frequency/co-occurrence control (UD Japanese-GSD) ---")
    print(f"  corpus-side split: {fq['corpus_side_split']}")
    for s in PANEL:
        m = fq["per_model"][s]
        print(f"  {MODELS[s][:26]:<26} rho(CCassert,freq)={m['spearman_ccassert_vs_meanfreq']} "
              f"rho(isogap,freq)={m['spearman_isogap_vs_meanfreq']} "
              f"rho(ctrlassert,cooc)={m['spearman_ctrlassert_vs_cooc']} "
              f"CCassert typ={m['cc_assert_typical_mean']} atyp={m['cc_assert_atypical_mean']}")

    out = {"per_model": res, "gates": gates, "freq_control": fq,
           "meta": {"b_boot": B_BOOT, "seed": SEED, "n_pairs": 34, "n_items": 136,
                    "bootstrap": "cluster over scale_pair", "language": "Japanese",
                    "ported_from": "2026-07-02-comparative-correlative-powered"}}
    with open(os.path.join(RAW, "results.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
