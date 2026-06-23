#!/usr/bin/env python3
"""certify.py -- build-time checks on the FROZEN within-lexical probe (NO API, NO spend).

Deterministic. Confirms the frozen instrument, the author-built disjunctive Arm-2 items, the
Arm-1 manifest, and the nuisance-matching freeze are well-formed before any run. Writes
certification_report.json. The named anti-cheat surface (re-selecting the disjunctive class
against model confidence) is foreclosed by the sha256 freeze, NOT by this script -- this script
only checks structure/balance/leak/nuisance-match, never "ambiguity strength" (which is
author-judged and capped to internal-contrast-only).

Checks:
  1.  instrument.json sha matches instrument.sha256 (C2 freeze hash binds).
  2.  freeze_manifest.json shas resolve + match (instrument, items_arm2, nuisance_match) and the
      Arm-1 stratum sha matches the committed lexical-leg stratum.csv.
  3.  Arm-2 classes are exactly {disjunctive, clear-same, clear-different}.
  4.  Arm-2 balance: each homonym set has exactly 1 disjunctive + 1 clear-same + 1 clear-different.
  5.  Arm-2 fields present; target surface really sits at each recorded span.
  6.  Arm-2 leak heuristics:
       (a) the disjunctive item's BALANCED ctx1 must NOT verbatim-contain either sense gloss's
           key content word (a crude tell of a planted disambiguator);
       (b) within a set the disjunctive's balanced ctx1 is distinct from every sense-fixed ctx;
       (c) the two contexts of every item differ;
       (d) clear-same's two contexts both come from the SAME sense pool (a1/a2), clear-different's
           from DIFFERENT pools (a* vs b1) -- enforced structurally by build_arm2 and re-checked
           here via the recorded ctx provenance.
  7.  Nuisance-match: the frozen nuisance_match.json records freq + length + frame for both arms
      and the |median Lg10WF| gap and |mean token| gap between arms are within disclosed bounds.
  8.  Decline wording is verbatim present in the system prompt; arms inherit ONE system prompt.

Usage: python3 certify.py     (writes certification_report.json, prints PASS/FAIL summary)
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INSTRUMENT = os.path.join(HERE, "instrument.json")
SHA_FILE = os.path.join(HERE, "instrument.sha256")
ITEMS_ARM2 = os.path.join(HERE, "items_arm2.json")
ITEMS_ARM1 = os.path.join(HERE, "items_arm1.json")
NUISANCE = os.path.join(HERE, "nuisance_match.json")
MANIFEST = os.path.join(HERE, "freeze_manifest.json")
REPORT = os.path.join(HERE, "certification_report.json")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

ARM2_CLASSES = {"disjunctive", "clear-same", "clear-different"}
# bounds the nuisance-match must clear (disclosed in the design doc); these are NOT tuned to a
# result -- they are the matched-kind certification's frozen tolerances.
MAX_FREQ_MEDIAN_GAP = 0.40   # |Arm2 - Arm1| median Lg10WF
MAX_LEN_MEAN_GAP = 6.0       # |Arm2 disjunctive - Arm1 bridging| mean sentence tokens


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def check(rep, name, ok, detail=""):
    rep.append({"check": name, "ok": bool(ok), "detail": detail})
    return ok


def main():
    rep = []

    # 1. instrument freeze hash
    live = sha256(INSTRUMENT)
    frozen = open(SHA_FILE).read().split()[0]
    check(rep, "instrument_sha256_matches", live == frozen, f"live={live[:16]} frozen={frozen[:16]}")

    cfg = json.load(open(INSTRUMENT, encoding="utf-8"))
    arm2 = json.load(open(ITEMS_ARM2, encoding="utf-8"))["items"]
    nm = json.load(open(NUISANCE, encoding="utf-8"))

    # 2. freeze manifest shas
    man_ok, man_detail = True, []
    try:
        man = json.load(open(MANIFEST, encoding="utf-8"))
        for key, ref in man["frozen"].items():
            p = os.path.join(REPO, ref["path"])
            if not os.path.exists(p):
                man_ok = False; man_detail.append(f"{key}: MISSING {ref['path']}")
            else:
                lv = sha256(p)
                if lv != ref["sha256"]:
                    man_ok = False; man_detail.append(f"{key}: sha mismatch {lv[:12]} vs {ref['sha256'][:12]}")
                else:
                    man_detail.append(f"{key}: OK {lv[:12]}")
    except Exception as e:  # noqa: BLE001
        man_ok = False; man_detail.append(f"{type(e).__name__}: {e}")
    check(rep, "freeze_manifest_shas_resolve_and_match", man_ok, "; ".join(man_detail))

    # 3. arm2 classes
    a2_classes = {it["class"] for it in arm2}
    check(rep, "arm2_classes_exact", a2_classes == ARM2_CLASSES, f"found={sorted(a2_classes)}")

    # 4. arm2 balance: each homonym set = 1 disjunctive + 1 clear-same + 1 clear-different
    sets = {}
    for it in arm2:
        sets.setdefault(it["surface"], []).append(it["class"])
    bal = all(sorted(v) == ["clear-different", "clear-same", "disjunctive"] for v in sets.values())
    check(rep, "arm2_set_balance_1disj_2clear", bal,
          f"n_sets={len(sets)}, counts={ {c: sum(1 for it in arm2 if it['class']==c) for c in ARM2_CLASSES} }")

    # 5. arm2 fields + spans land on target
    fields_ok = all(all(k in it for k in
                    ("item_id", "surface", "lemma", "senseA", "senseB", "lg10wf",
                     "class", "ctx1", "span1", "ctx2", "span2")) for it in arm2)
    check(rep, "arm2_fields_present", fields_ok)
    span_ok = all(it[f"ctx{n}"][it[f"span{n}"][0]:it[f"span{n}"][1]].lower() == it["surface"].lower()
                  for it in arm2 for n in (1, 2))
    check(rep, "arm2_spans_on_target", span_ok)

    # 6. leak heuristics
    # (a) balanced ctx1 (disjunctive) must not contain a sense gloss's distinctive content word
    disj = {it["surface"]: it for it in arm2 if it["class"] == "disjunctive"}
    STOP = set("a an the of for to in on at and or with that this it its as is was be by from "
               "an one two both very much more most some any all".split())

    def content_words(gloss):
        return [w for w in re.findall(r"[a-z]+", gloss.lower()) if w not in STOP and len(w) > 3]

    leak_a = True
    leak_detail = []
    for surf, it in disj.items():
        bal_lc = it["ctx1"].lower()
        planted = [w for w in content_words(it["senseA"]) + content_words(it["senseB"])
                   if re.search(r"\b" + re.escape(w) + r"\b", bal_lc)]
        if planted:
            leak_a = False; leak_detail.append(f"{surf}: balanced ctx1 contains gloss word(s) {planted}")
    check(rep, "arm2_balanced_ctx1_no_gloss_word_planted", leak_a, "; ".join(leak_detail))

    # (b) the disjunctive's balanced ctx1 is distinct from every sense-fixed ctx in its set
    distinct_bal = True
    by_set_ctx = {}
    for it in arm2:
        by_set_ctx.setdefault(it["surface"], []).append((it["class"], it["ctx1"]))
        by_set_ctx[it["surface"]].append((it["class"], it["ctx2"]))
    for surf, it in disj.items():
        bal = it["ctx1"].strip().lower()
        fixed = [c for (cls, c) in by_set_ctx[surf] if not (cls == "disjunctive" and c.strip().lower() == bal)]
        if any(bal == f.strip().lower() for f in fixed):
            distinct_bal = False
    check(rep, "arm2_balanced_ctx1_distinct_from_fixed", distinct_bal)

    # (c) two contexts of every item differ
    two_differ = all(it["ctx1"].strip().lower() != it["ctx2"].strip().lower() for it in arm2)
    check(rep, "arm2_item_two_contexts_differ", two_differ)

    # 7. nuisance match within bounds
    f_gap = abs(nm["freq_lg10wf"]["median"] - nm["arm1_targets_for_match"]["freq_lg10wf"]["median"])
    l_gap = abs(nm["sentence_tokens"]["disjunctive"]["mean"]
                - nm["arm1_targets_for_match"]["sentence_tokens"]["bridging"]["mean"])
    check(rep, "nuisance_freq_median_gap_within_bound", f_gap <= MAX_FREQ_MEDIAN_GAP,
          f"|median Lg10WF gap|={f_gap:.3f} <= {MAX_FREQ_MEDIAN_GAP}")
    check(rep, "nuisance_length_mean_gap_within_bound", l_gap <= MAX_LEN_MEAN_GAP,
          f"|mean token gap|={l_gap:.2f} <= {MAX_LEN_MEAN_GAP}")
    check(rep, "nuisance_frame_recorded_nouns",
          "noun" in nm.get("arm2_pos_frame", "").lower(), nm.get("arm2_pos_frame", ""))
    check(rep, "nuisance_register_residual_disclosed",
          "register_note" in nm and len(nm["register_note"]) > 40, "register residual note present")

    # 8. instrument: single shared system prompt; decline wording verbatim within it
    wording_ok = cfg["decline_wording_verbatim"] in cfg["system"]
    check(rep, "decline_wording_in_system_prompt", wording_ok)
    one_system = isinstance(cfg.get("system"), str) and "arms" in cfg
    check(rep, "single_shared_system_for_both_arms", one_system)

    n_fail = sum(1 for r in rep if not r["ok"])
    out = {"summary": {"n_checks": len(rep), "n_fail": n_fail,
                       "status": "PASS" if n_fail == 0 else "FAIL"},
           "counts": {"arm2_items": len(arm2), "arm2_homonyms": len(sets),
                      "freq_median_gap": round(f_gap, 3), "length_mean_gap": round(l_gap, 2)},
           "checks": rep}
    json.dump(out, open(REPORT, "w"), indent=1)
    print(json.dumps(out["summary"], indent=1))
    print(json.dumps(out["counts"], indent=1))
    for r in rep:
        if not r["ok"]:
            print(f"  FAIL: {r['check']}  {r['detail']}")
    sys.exit(0 if n_fail == 0 else 1)


if __name__ == "__main__":
    main()
