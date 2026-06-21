#!/usr/bin/env python3
"""build.py -- assemble + freeze the MODAL-ARM-WIDENING stimulus set (session 71, 2026-06-21).

A FOCUSED FOLLOW-UP to the function-word-vs-content swap probe (run-v2, session 69) that
tested wiki/findings/conjectures/function-word-substitutability.md and CONFIRMED it 3/3 but
non-uniformly. Its companion essay
(wiki/findings/essays/function-words-not-one-category.md) reads the per-arm structure and
names revision trigger (a): the modal arm `will`->`would` was near-null in all three models,
but that is a ONE-PAIR observation. This probe WIDENS the modal arm to test whether the modal
null generalizes across modal types, or is specific to future->conditional.

It REUSES the ratified instrument (3-way NLI entailment-flip), the ratified matching discipline
(|dLg10WF| <= 0.10 at both ends, signed-dlen-matched content control, content gap >= function
gap so no surface-only reader reproduces the asymmetry -- certify.py), and the
internal-contrast-only posture (no new human claim). NO new operationalization decision is owed:
the inventory-widening method is already ratified
(wiki/decisions/resolved/function-word-count-vs-matching.md), the instrument is ratified
(wiki/decisions/resolved/function-word-anchor-design.md), and this is not a re-test of the
conjecture (already `tested`) but a per-arm characterization of modal behavior. (The >=200-item
count is the CONJECTURE-confirm bar, not this follow-up's bar; certify.py uses a per-arm power
gate instead -- see its docstring.)

ARMS (5):
  Modal sweep (the question):
    will -> would   (future -> conditional)        REPLICATION of run-v2's null; hyp "is going to".
    shall-> should  (deontic obligation -> advisory) NEW; hyp "is required to".
    must -> might   (deontic necessity -> epistemic possibility) NEW; hyp "is required to".
  In-run positive controls (prove the NLI instrument flips on a real inferential change here):
    some -> every   (existential -> universal)      REUSE run-v2 frames.
    because->although(causal -> concessive)          REUSE run-v2 frames (also supplies the adj class).

Each ITEM (same design as run-v2):
  premise_base : function word = swap-OUT, content word = OUT.
  premise_fn   : function word = swap-IN , content word = OUT.  (function word in PREMISE ONLY; predicted to FLIP.)
  premise_ct   : function word = swap-OUT, content word = IN.
  hyp_base     : content word = OUT.   hyp_ct : content word = IN.
  -> 3 NLI calls/item: (premise_base,hyp_base), (premise_fn,hyp_base), (premise_ct,hyp_ct).
     flip_fn = label(fn,hyp_base) != label(base,hyp_base) [predicted YES].
     flip_ct = label(ct,hyp_ct)   != label(base,hyp_base) [predicted NO].

Matching enforced HERE, drop-on-fail (binding conditions b-f), IDENTICAL to run-v2:
  (b) content-OUT within |dLg10WF| <= FREQ_TOL of the function-OUT word.
  (c) content-IN  within |dLg10WF| <= FREQ_TOL of the function-IN word (mirrored spread).
  (d) signed len(in)-len(out) == signed function dlen (per-pair).
  (e) per-arm count >= ARM_MIN AND >= 4 content semantic classes (certify.py).
  (f) sha256 of stimuli.json recorded in PREREG.md before the first probe call (probe.py guard).
"""
import hashlib
import json
import os
import sys

import freqlib as F

HERE = os.path.dirname(os.path.abspath(__file__))

FUNC = {
    "because": {"out": "because", "in": "although", "gloss": "subordinator: causal->concessive (REUSE run-v2; positive control)"},
    "some":    {"out": "some",    "in": "every",    "gloss": "quantifier: existential->universal (REUSE run-v2; positive control)"},
    "will":    {"out": "will",    "in": "would",    "gloss": "modal: future->conditional (REUSE run-v2; replication of the null)"},
    # MODAL-ARM-WIDENING (session 71). The two NEW modal pairs that test essay revision trigger (a):
    "shall":   {"out": "shall",   "in": "should",   "gloss": "modal: deontic obligation->advisory (NEW)"},
    "must":    {"out": "must",    "in": "might",     "gloss": "modal: deontic necessity->epistemic possibility (NEW)"},
}
for d in FUNC.values():
    d["out_lg"] = round(F.require(d["out"]), 4)
    d["in_lg"] = round(F.require(d["in"]), 4)
    d["gap"] = round(abs(d["out_lg"] - d["in_lg"]), 4)

FREQ_TOL = 0.10


def cap_first(s):
    return s[0].upper() + s[1:] if s else s


def verify_pair(ftype, out, inn):
    """Return (ok, reason, stats). Enforces (b),(c),(d) -- per-pair signed dlen. UNCHANGED from run-v2."""
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
    arms = [k for k in frames if not k.startswith("_") and k != "the_char"]
    for ftype in arms:
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
    # the_char arm optional (not used in the modal-widening set); kept for pipeline parity.
    for fr in frames.get("the_char", []):
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
    out_words = {}
    for it in matched:
        c = f"{it['ftype']}:{it['pos']}"
        by_class[c] = by_class.get(c, 0) + 1
        by_ft[it["ftype"]] = by_ft.get(it["ftype"], 0) + 1
        resid.setdefault(it["ftype"], []).append(it["content_gap"] - it["func_gap"])
        out_words.setdefault(c, {})
        out_words[c][it["cont_out"]] = out_words[c].get(it["cont_out"], 0) + 1
    diversity = {}
    single_word_classes = []
    for c, ow in sorted(out_words.items()):
        n_items = sum(ow.values())
        n_out = len(ow)
        diversity[c] = {"distinct_out_words": n_out, "items": n_items,
                        "items_per_out_word": round(n_items / n_out, 2),
                        "out_word_counts": dict(sorted(ow.items(), key=lambda x: -x[1]))}
        if n_out == 1:
            single_word_classes.append(c)
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
        "content_diversity_by_function_x_pos": diversity,
        "single_out_word_classes": single_word_classes,
        "dropped_pairs": dropped,
        "freq_tol": FREQ_TOL, "len_match": "signed dlen == function dlen (per-pair)",
    }
    json.dump(report, open(os.path.join(HERE, "matching-report.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"items: {len(items)} ({len(matched)} matched + {len(det)} det_char)")
    print(f"by function: {by_ft}")
    print(f"by function x pos: {by_class}")
    print(f"content semantic classes: {report['counts']['content_semantic_classes']}")
    print(f"gap residual mean by ftype: {report['gap_residual_mean_by_ftype']}")
    print(f"gap residual |max| by ftype: {report['gap_residual_absmax_by_ftype']}")
    print(f"single-out-word classes: {single_word_classes}")
    print(f"dropped pairs: {len(dropped)}")
    for d in dropped[:20]:
        print(f"   DROP {d['ftype']} {d['pair']}: {d['reason']}")
    print(f"stimuli.json sha256: {sha}")
    ARM_MIN = 15
    thin = {k: v for k, v in by_ft.items() if v < ARM_MIN}
    if thin:
        print(f"\n*** WARNING: arms below per-arm min {ARM_MIN}: {thin} ***")


if __name__ == "__main__":
    main()
