#!/usr/bin/env python3
"""build.py -- assemble + freeze the function-word-vs-content-word swap stimulus set.

Design (ratified wiki/decisions/resolved/function-word-anchor-design.md; conjecture
wiki/findings/conjectures/function-word-substitutability.md). See frames.json for the
authored carriers. Each ITEM:

  premise_base : function word = swap-OUT (because/some/will), content word = OUT.
  premise_fn   : function word = swap-IN  (although/every/would), content word = OUT.
                 (function word appears in the PREMISE ONLY; predicted to FLIP the label.)
  premise_ct   : function word = swap-OUT, content word = IN.
  hyp_base     : content word = OUT.   hyp_ct : content word = IN.
  -> 3 NLI calls/item: (premise_base,hyp_base), (premise_fn,hyp_base), (premise_ct,hyp_ct).
     flip_fn = label(fn,hyp_base) != label(base,hyp_base) [predicted YES].
     flip_ct = label(ct,hyp_ct)   != label(base,hyp_base) [predicted NO].

Matching enforced HERE, drop-on-fail (binding conditions b-f):
  (b) content-OUT within |dLg10WF| <= FREQ_TOL of the function-OUT word.
  (c) content-IN  within |dLg10WF| <= FREQ_TOL of the function-IN word  => the content
      within-pair gap mirrors the function within-pair gap (mirrored spread; achieved
      distribution reported in matching-report.json).
  (d) |len(out)-len(in)| <= LEN_TOL (content swap length-neutral); char-bigram proxy reported.
  (e) >=200 matched items + >=4 content semantic classes (per-class counts reported).
  (f) sha256 of stimuli.json recorded in PREREG.md before the first probe call (probe.py guard).

the->a: NO frequency-matched content control exists (no open-class word reaches Lg10WF ~6.0);
the_char frames run as a FUNCTION-ONLY characterizing arm (arm='det_char'), excluded from the
primary matched contrast.
"""
import hashlib
import json
import os
import sys

import freqlib as F

HERE = os.path.dirname(os.path.abspath(__file__))

FUNC = {
    "because": {"out": "because", "in": "although", "gloss": "subordinator: causal->concessive"},
    "some":    {"out": "some",    "in": "every",    "gloss": "quantifier: existential->universal"},
    "will":    {"out": "will",    "in": "would",    "gloss": "modal: future->conditional"},
}
for d in FUNC.values():
    d["out_lg"] = round(F.require(d["out"]), 4)
    d["in_lg"] = round(F.require(d["in"]), 4)
    d["gap"] = round(abs(d["out_lg"] - d["in_lg"]), 4)

FREQ_TOL = 0.10


def cap_first(s):
    return s[0].upper() + s[1:] if s else s


def verify_pair(ftype, out, inn):
    """Return (ok, reason, stats). Enforces conditions (b),(c),(d).

    (d) is enforced as a SIGNED length match: the content swap must change orthographic
    length by EXACTLY the same delta as the function swap (because->although, some->every,
    will->would are all +1 char). This is what makes a length-only reader unable to
    separate the function and content conditions (certify.py condition (i)) -- a |dlen|<=1
    tolerance would leave many content swaps length-neutral (delta 0) while every function
    swap is +1, which a length-only reader exploits.
    """
    olg, ilg = F.lg10wf(out), F.lg10wf(inn)
    if olg is None:
        return False, f"out {out!r} not in norm", {}
    if ilg is None:
        return False, f"in {inn!r} not in norm", {}
    fo, fi = FUNC[ftype]["out_lg"], FUNC[ftype]["in_lg"]
    func_dlen = len(FUNC[ftype]["in"]) - len(FUNC[ftype]["out"])
    stats = {"out_lg": round(olg, 4), "in_lg": round(ilg, 4),
             "content_gap": round(abs(olg - ilg), 4), "func_gap": FUNC[ftype]["gap"],
             "d_out_func": round(olg - fo, 4), "d_in_func": round(ilg - fi, 4),
             "len_out": len(out), "len_in": len(inn),
             "dlen": len(inn) - len(out), "func_dlen": func_dlen}
    if abs(olg - fo) > FREQ_TOL:
        return False, f"(b) out {out} dLg10WF {olg-fo:+.3f} > {FREQ_TOL} from {ftype}-out", stats
    if abs(ilg - fi) > FREQ_TOL:
        return False, f"(c) in {inn} dLg10WF {ilg-fi:+.3f} > {FREQ_TOL} from {ftype}-in", stats
    if (len(inn) - len(out)) != func_dlen:
        return False, (f"(d) signed dlen {len(inn)-len(out):+d} != function dlen "
                       f"{func_dlen:+d}"), stats
    return True, "ok", stats


def make():
    frames = json.load(open(os.path.join(HERE, "frames.json")))
    items, dropped = [], []
    for ftype in ("because", "some", "will"):
        fout, fin = FUNC[ftype]["out"], FUNC[ftype]["in"]
        for fr in frames[ftype]:
            cap = fr.get("cap", False)
            fwo = cap_first(fout) if cap else fout
            fwi = cap_first(fin) if cap else fin
            for out, inn in fr["pairs"]:
                ok, reason, st = verify_pair(ftype, out, inn)
                if not ok:
                    dropped.append({"ftype": ftype, "pair": [out, inn], "reason": reason})
                    continue
                p_base = fr["premise"].format(fw=fout, Fw=fwo, cw=out)
                p_fn = fr["premise"].format(fw=fin, Fw=fwi, cw=out)
                p_ct = fr["premise"].format(fw=fout, Fw=fwo, cw=inn)
                h_base = fr["hyp"].format(cw=out)
                h_ct = fr["hyp"].format(cw=inn)
                items.append({
                    "ftype": ftype, "pos": fr["slot"], "arm": "matched",
                    "func_out": fout, "func_in": fin, "cont_out": out, "cont_in": inn,
                    "pred_base": fr["base"], "pred_fn": fr["fn"],
                    "premise_base": p_base, "premise_fn": p_fn, "premise_ct": p_ct,
                    "hyp_base": h_base, "hyp_ct": h_ct,
                    "func_gap": FUNC[ftype]["gap"], **st,
                })
    for fr in frames["the_char"]:
        p_base = fr["premise"].format(Fw="The")
        p_fn = fr["premise"].format(Fw="A")
        items.append({
            "ftype": "the", "pos": "det", "arm": "det_char",
            "func_out": "the", "func_in": "a", "cont_out": None, "cont_in": None,
            "pred_base": fr["base"], "pred_fn": fr["fn"],
            "premise_base": p_base, "premise_fn": p_fn, "premise_ct": None,
            "hyp_base": fr["hyp"], "hyp_ct": None,
            "func_gap": round(abs(F.require("the") - F.require("a")), 4),
        })
    # dedupe + assign stable ids
    seen, uniq = set(), []
    for it in items:
        k = (it["premise_base"], it["hyp_base"], it["premise_fn"], it["premise_ct"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(it)
    for i, it in enumerate(sorted(uniq, key=lambda x: (x["ftype"], x["pos"],
                                                       x["premise_base"]))):
        it["id"] = f"{it['ftype']}-{it['pos']}-{i:03d}"
    return uniq, dropped


def main():
    items, dropped = make()
    matched = [it for it in items if it["arm"] == "matched"]
    det = [it for it in items if it["arm"] == "det_char"]
    payload = {"items": sorted(items, key=lambda x: x["id"])}
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    sha = hashlib.sha256(blob).hexdigest()
    payload["sha256"] = sha
    json.dump(payload, open(os.path.join(HERE, "stimuli.json"), "w"),
              ensure_ascii=False, indent=1, sort_keys=True)

    by_class, by_ft = {}, {}
    resid = {}
    for it in matched:
        c = f"{it['ftype']}:{it['pos']}"
        by_class[c] = by_class.get(c, 0) + 1
        by_ft[it["ftype"]] = by_ft.get(it["ftype"], 0) + 1
        resid.setdefault(it["ftype"], []).append(it["content_gap"] - it["func_gap"])
    report = {
        "function_pairs": {k: {"out_lg": v["out_lg"], "in_lg": v["in_lg"],
                               "gap": v["gap"], "gloss": v["gloss"]}
                           for k, v in FUNC.items()},
        "counts": {"matched_total": len(matched), "det_char": len(det),
                   "by_function": by_ft, "by_function_x_pos": by_class,
                   "content_semantic_classes": sorted({it["pos"] for it in matched})},
        "gap_residual_mean_by_ftype": {k: round(sum(v) / len(v), 4)
                                       for k, v in resid.items()},
        "gap_residual_absmax_by_ftype": {k: round(max(abs(x) for x in v), 4)
                                         for k, v in resid.items()},
        "dropped_pairs": dropped,
        "freq_tol": FREQ_TOL, "len_match": "signed dlen == function dlen (all +1)",
    }
    json.dump(report, open(os.path.join(HERE, "matching-report.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"items: {len(items)} ({len(matched)} matched + {len(det)} det_char)")
    print(f"by function: {by_ft}")
    print(f"by function x pos: {by_class}")
    print(f"content semantic classes: {report['counts']['content_semantic_classes']}")
    print(f"gap residual mean by ftype: {report['gap_residual_mean_by_ftype']}")
    print(f"gap residual |max| by ftype: {report['gap_residual_absmax_by_ftype']}")
    print(f"dropped pairs: {len(dropped)}")
    for d in dropped[:12]:
        print(f"   DROP {d['ftype']} {d['pair']}: {d['reason']}")
    print(f"stimuli.json sha256: {sha}")
    if len(matched) < 200:
        print(f"\n*** WARNING: matched={len(matched)} < 200 (binding condition e). ***")


if __name__ == "__main__":
    main()
