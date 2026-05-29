"""Analyze the conative minimal-pair probe v1 (2026-05-29).

Primary indicator: "affirm completed-contact rate" per frame (FC answer YES, or NLI
label 0 = entailment), for the conative-class verbs. The conjecture (P1) predicts:
  gap = transitive_affirm - conative_affirm >= 30pp, in >=2/3 models, replicating
  across verbs (not driven by one verb).
P3 (frequency/memorization): the conative non-completion reading PERSISTS for atypical
  (low-frequency) objects -> the typical-vs-atypical gap difference is within 15pp.
P2 (verb-class): the contact-cancellation is WEAKER for control (non-alternating) verbs.

No threshold retuning: thresholds are the ratified ones (30 / 15 pp); we report raw
rates and let the result page interpret. All numbers derive from the committed raw/.
"""
import csv, json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
ITEMS = os.path.abspath(os.path.join(HERE, "..", "..", "data", "conative", "items.csv"))
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}


def affirm(arm, pred):
    if pred is None:
        return None
    return pred == "0" if arm == "nli" else pred == "YES"


def rate(recs, pred_field="affirm"):
    vals = [r[pred_field] for r in recs if r[pred_field] is not None]
    return (sum(vals) / len(vals), len(vals)) if vals else (None, 0)


def main():
    items = {r["item_id"]: r for r in csv.DictReader(open(ITEMS))}
    out = {"per_model": {}, "thresholds": {"gap_pp": 30, "atypical_within_pp": 15}}
    print("\n===== CONATIVE MINIMAL-PAIR PROBE v1 — affirm completed-contact rate =====")
    print("Predicted (P1): transitive affirms contact, conative does not, gap >=30pp.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))
            for r in recs:
                r["affirm"] = affirm(arm, r["pred"])
            con = [r for r in recs if r["verb_class"] == "conative"]
            ctl = [r for r in recs if r["verb_class"] == "control"]
            def split(rs, frame, otype=None):
                return [r for r in rs if r["frame"] == frame
                        and (otype is None or r["object_type"] == otype)]
            t_aff, t_n = rate(split(con, "transitive"))
            c_aff, c_n = rate(split(con, "conative"))
            gap = None if t_aff is None or c_aff is None else round((t_aff - c_aff) * 100, 1)
            # per-verb gap (replication across verbs)
            verbs = sorted(set(r["verb"] for r in con))
            pv = {}
            for v in verbs:
                vt, _ = rate([r for r in con if r["verb"] == v and r["frame"] == "transitive"])
                vc, _ = rate([r for r in con if r["verb"] == v and r["frame"] == "conative"])
                pv[v] = None if vt is None or vc is None else round((vt - vc) * 100, 1)
            n_pos = sum(1 for g in pv.values() if g is not None and g > 0)
            n_ge30 = sum(1 for g in pv.values() if g is not None and g >= 30)
            # typical vs atypical gap (P3)
            def gap_for(otype):
                tt, _ = rate(split(con, "transitive", otype))
                cc, _ = rate(split(con, "conative", otype))
                return None if tt is None or cc is None else round((tt - cc) * 100, 1)
            gtyp, gatyp = gap_for("typical"), gap_for("atypical")
            # control (P2)
            ct_t, _ = rate(split(ctl, "transitive"))
            ct_c, _ = rate(split(ctl, "conative"))
            ctl_gap = None if ct_t is None or ct_c is None else round((ct_t - ct_c) * 100, 1)
            m[arm] = {
                "transitive_affirm": None if t_aff is None else round(t_aff * 100, 1),
                "conative_affirm": None if c_aff is None else round(c_aff * 100, 1),
                "gap_pp": gap, "n_transitive": t_n, "n_conative": c_n,
                "per_verb_gap_pp": pv, "verbs_with_positive_gap": f"{n_pos}/{len(verbs)}",
                "verbs_with_gap_ge30": f"{n_ge30}/{len(verbs)}",
                "gap_typical_pp": gtyp, "gap_atypical_pp": gatyp,
                "atypical_minus_typical_pp": None if gtyp is None or gatyp is None
                    else round(gatyp - gtyp, 1),
                "control_transitive_affirm": None if ct_t is None else round(ct_t * 100, 1),
                "control_conative_affirm": None if ct_c is None else round(ct_c * 100, 1),
                "control_gap_pp": ctl_gap,
                "na": sum(1 for r in recs if r["pred"] is None),
            }
        out["per_model"][slot] = m
        for arm in ("nli", "fc"):
            a = m[arm]
            print(f"[{name:<18} {arm.upper():<3}] trans={a['transitive_affirm']}%  "
                  f"conative={a['conative_affirm']}%  GAP={a['gap_pp']}pp  "
                  f"(verbs +gap {a['verbs_with_positive_gap']}, >=30 {a['verbs_with_gap_ge30']}; "
                  f"typ {a['gap_typical_pp']} / atyp {a['gap_atypical_pp']}; "
                  f"ctrl gap {a['control_gap_pp']}; NA {a['na']})")
        print()
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"wrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
