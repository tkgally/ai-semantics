"""Analyze the coercion-as-sense-modulation bridge probe (v1, 2026-05-30).

Per model x framing: mean relatedness per arm. Headline (report-the-rate, internal-contrast):
  - COERCION SENSE-SHIFT GAP = mean(control-elab) - mean(coerced)  [pooled, and cm/way split].
    A POSITIVE gap = the model rates the coerced verb as LESS sense-related than a length-
    matched non-coercing elaboration => it registers constructional coercion AS lexical sense
    modulation. A ~0 gap = it does not (coerced ~ same sense as the bare use).
  - per-verb gap: fraction of cm/way verbs with control > coerced (within-verb sign test).
  - CALIBRATION: mean(polysemy-anchor) must read LOW (a real sense shift) for a coerced~control
    null to be interpretable; the coerced arm is contextualized between control (high) and
    polysemy-anchor (low).
durel 1-4 and cont 0-100 reported separately. No threshold tuned post-run.
"""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
ARMS = ["control-elab", "coerced-cm", "coerced-way", "polysemy-anchor"]


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 2) if xs else None


def main():
    out = {"per_model": {}, "reading_rule": "mean relatedness per arm; headline = coercion "
           "sense-shift gap (control-elab minus coerced) + per-verb sign + polysemy calibration"}
    print("\n===== COERCION-AS-SENSE-MODULATION v1 — mean relatedness per arm =====")
    print("control-elab=non-coercing elaboration (high anchor) | coerced-cm/way=coercion | "
          "polysemy-anchor=real sense shift (low anchor). gap=control-coerced.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for fr in ("durel", "cont"):
            recs = json.load(open(os.path.join(RAW, f"{fr}_{slot}.json")))
            byarm = defaultdict(list)
            byverb = defaultdict(dict)  # verb -> arm -> pred
            for r in recs:
                byarm[r["arm"]].append(r["pred"])
                byverb[r["verb"]][r["arm"]] = r["pred"]
            arm_means = {a: mean(byarm[a]) for a in ARMS}
            coerced_all = byarm["coerced-cm"] + byarm["coerced-way"]
            gap_cm = (arm_means["control-elab"] - mean(byarm["coerced-cm"])
                      if arm_means["control-elab"] is not None else None)
            gap_way = (arm_means["control-elab"] - mean(byarm["coerced-way"])
                       if arm_means["control-elab"] is not None else None)
            gap_pool = (arm_means["control-elab"] - mean(coerced_all)
                        if arm_means["control-elab"] is not None else None)
            # within-verb sign: control > coerced ?
            pos = tot = 0
            for verb, d in byverb.items():
                co = d.get("coerced-cm", d.get("coerced-way"))
                ce = d.get("control-elab")
                if co is not None and ce is not None:
                    tot += 1
                    if ce > co:
                        pos += 1
            m[fr] = {"arm_means": arm_means,
                     "gap_pooled": round(gap_pool, 2) if gap_pool is not None else None,
                     "gap_cm": round(gap_cm, 2) if gap_cm is not None else None,
                     "gap_way": round(gap_way, 2) if gap_way is not None else None,
                     "within_verb_control>coerced": f"{pos}/{tot}"}
        out["per_model"][slot] = m
        for fr in ("durel", "cont"):
            c = m[fr]
            am = c["arm_means"]
            print(f"[{name:<18} {fr:<5}] control={am['control-elab']} "
                  f"coerced-cm={am['coerced-cm']} coerced-way={am['coerced-way']} "
                  f"poly={am['polysemy-anchor']}  | gap(pool)={c['gap_pooled']} "
                  f"(cm={c['gap_cm']} way={c['gap_way']})  within-verb={c['within_verb_control>coerced']}")
        print()
    print("--- headline: coercion sense-shift gap (control - coerced), positive => coercion "
          "registers as sense modulation ---")
    for fr in ("durel", "cont"):
        gp = [out["per_model"][s][fr]["gap_pooled"] for s in PANEL]
        poly = [out["per_model"][s][fr]["arm_means"]["polysemy-anchor"] for s in PANEL]
        ctrl = [out["per_model"][s][fr]["arm_means"]["control-elab"] for s in PANEL]
        print(f"  {fr:<5}: gap_pooled={gp}  (control={ctrl}, polysemy-anchor[low cal]={poly})")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
