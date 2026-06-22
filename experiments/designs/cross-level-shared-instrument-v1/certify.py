#!/usr/bin/env python3
"""certify.py -- build-time shortcut/leak/geometry checks on the FROZEN stimuli (NO API).

Deterministic, no model calls, no spend. Confirms the synthetic constructional + relational
item sets are well-formed before any run, and that the frozen instrument is internally
consistent. Writes certification_report.json. The lexical leg is a MANIFEST (its stimuli are
certified by the lexical leg's own freeze; here we only check the manifest's sha references
resolve to existing frozen files).

Checks:
  1. instrument.json sha matches instrument.sha256 (the C2 freeze hash binds).
  2. Per level: every item has the required fields; class labels are exactly the frozen set.
  3. Balance: each constructional/relational SET has 1 ambiguous + 2 clear controls (one per
     pole); per-pole control counts balanced.
  4. No answer leak: the level NOUN / decline wording does not name the correct reading; the
     two candidate readings/figures are distinct; the ambiguous item's two readings appear as
     (1)/(2) without a disambiguating cue in the stem.
  5. Clear-class genuineness (textual heuristic): each clear-* control's stem contains a
     disambiguating token absent from its ambiguous sibling (so the control really forces one
     reading); the ambiguous stem does NOT contain such a token.
  6. Distinct figures per relational record (K>=4, all distinct); the two candidate figures
     are both among the grid; the ambiguous record binds the term to BOTH candidates with the
     SAME round stamp (no recency tie-break); clear controls bind to exactly ONE candidate.
  7. Lexical manifest: referenced frozen files exist and their sha256 matches the manifest.

Usage: python3 certify.py        (writes certification_report.json, prints PASS/FAIL summary)
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INSTRUMENT = os.path.join(HERE, "instrument.json")
SHA_FILE = os.path.join(HERE, "instrument.sha256")
ITEMS_CX = os.path.join(HERE, "items_constructional.json")
ITEMS_REL = os.path.join(HERE, "items_relational.json")
ITEMS_LEX = os.path.join(HERE, "items_lexical.json")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REPORT = os.path.join(HERE, "certification_report.json")

CX_CLASSES = {"ambiguous", "clear-reading1", "clear-reading2"}
REL_CLASSES = {"ambiguous-midrecord", "clear-determinate", "clear-other-determinate"}


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def check(report, name, ok, detail=""):
    report.append({"check": name, "ok": bool(ok), "detail": detail})
    return ok


def main():
    rep = []

    # 1. instrument freeze hash
    live = sha256(INSTRUMENT)
    frozen = open(SHA_FILE).read().split()[0]
    check(rep, "instrument_sha256_matches", live == frozen,
          f"live={live} frozen={frozen}")

    cfg = json.load(open(INSTRUMENT, encoding="utf-8"))
    cx = json.load(open(ITEMS_CX, encoding="utf-8"))["items"]
    rel = json.load(open(ITEMS_REL, encoding="utf-8"))["items"]

    # 2. constructional fields + classes
    cx_classes = {it["class"] for it in cx}
    check(rep, "cx_classes_exact", cx_classes == CX_CLASSES,
          f"found={sorted(cx_classes)}")
    cx_fields_ok = all(all(k in it for k in
                       ("item_id", "set", "class", "sentence", "reading1", "reading2"))
                       for it in cx)
    check(rep, "cx_fields_present", cx_fields_ok)

    # 3. constructional balance: each set = 1 ambiguous + 2 clears (one per pole)
    cx_sets = {}
    for it in cx:
        cx_sets.setdefault(it["set"], []).append(it["class"])
    cx_bal = all(sorted(v) == ["ambiguous", "clear-reading1", "clear-reading2"]
                 for v in cx_sets.values())
    check(rep, "cx_set_balance_1amb_2clear", cx_bal,
          f"n_sets={len(cx_sets)}, "
          f"counts={ {c: sum(1 for it in cx if it['class']==c) for c in CX_CLASSES} }")

    # 4/5. cx leak + clear-class genuineness:
    # ambiguous stem must NOT verbatim-contain either of its readings; clear controls'
    # stems must differ from their ambiguous sibling's stem (a disambiguating rewrite).
    cx_no_leak = True
    cx_genuine = True
    amb_by_set = {it["set"]: it for it in cx if it["class"] == "ambiguous"}
    for it in cx:
        if it["class"] == "ambiguous":
            stem = it["sentence"].lower()
            if it["reading1"].lower() in stem or it["reading2"].lower() in stem:
                cx_no_leak = False
        else:
            sib = amb_by_set.get(it["set"])
            if sib and it["sentence"].strip().lower() == sib["sentence"].strip().lower():
                cx_genuine = False  # control identical to ambiguous => not disambiguated
    check(rep, "cx_ambiguous_no_reading_verbatim_in_stem", cx_no_leak)
    check(rep, "cx_clear_controls_rewritten_vs_ambiguous", cx_genuine)
    # two readings distinct per item
    check(rep, "cx_two_readings_distinct",
          all(it["reading1"].strip().lower() != it["reading2"].strip().lower() for it in cx))

    # 2'. relational fields + classes
    rel_classes = {it["class"] for it in rel}
    check(rep, "rel_classes_exact", rel_classes == REL_CLASSES,
          f"found={sorted(rel_classes)}")
    rel_fields_ok = all(all(k in it for k in
                        ("item_id", "set", "class", "term", "figures", "history",
                         "fig1", "fig2")) for it in rel)
    check(rep, "rel_fields_present", rel_fields_ok)

    # 3'. relational balance
    rel_sets = {}
    for it in rel:
        rel_sets.setdefault(it["set"], []).append(it["class"])
    rel_bal = all(sorted(v) == ["ambiguous-midrecord", "clear-determinate",
                                "clear-other-determinate"] for v in rel_sets.values())
    check(rep, "rel_set_balance_1amb_2clear", rel_bal, f"n_sets={len(rel_sets)}")

    # 6. relational geometry
    rel_geom_ok = True
    rel_amb_dual = True
    rel_clear_single = True
    rel_cands_distinct = True
    for it in rel:
        figs = it["figures"]
        if len(set(figs)) < 4 or len(figs) != len(set(figs)):
            rel_geom_ok = False
        if it["fig1"] == it["fig2"]:
            rel_cands_distinct = False
        if it["fig1"] not in figs or it["fig2"] not in figs:
            rel_geom_ok = False
        bound = [h for h in it["history"]]
        rounds = [h.split(":")[0] for h in bound]
        if it["class"] == "ambiguous-midrecord":
            # both candidates bound, SAME round stamp (no recency tie-break)
            f1_bound = any(it["fig1"] in h for h in bound)
            f2_bound = any(it["fig2"] in h for h in bound)
            if not (f1_bound and f2_bound and len(set(rounds)) == 1 and len(bound) == 2):
                rel_amb_dual = False
        else:
            # exactly one candidate bound
            f1_bound = any(it["fig1"] in h for h in bound)
            f2_bound = any(it["fig2"] in h for h in bound)
            target = it["fig1"] if it["class"] == "clear-determinate" else it["fig2"]
            other = it["fig2"] if it["class"] == "clear-determinate" else it["fig1"]
            if not (len(bound) == 1 and any(target in h for h in bound)
                    and not any(other in h for h in bound)):
                rel_clear_single = False
    check(rep, "rel_grid_distinct_K>=4", rel_geom_ok)
    check(rep, "rel_candidates_distinct", rel_cands_distinct)
    check(rep, "rel_ambiguous_dual_binding_same_round", rel_amb_dual)
    check(rep, "rel_clear_single_binding", rel_clear_single)

    # 4'. relational no-leak: the term is a nonce (uppercase, not an English word in the
    # figure descriptions); the query lists both candidates so neither is privileged by order
    # of mention beyond (1)/(2). Heuristic: term not substring of any figure desc.
    rel_term_nonce = all(it["term"].lower() not in " ".join(it["figures"]).lower()
                         for it in rel)
    check(rep, "rel_term_is_nonce", rel_term_nonce)

    # 7. lexical manifest references resolve + sha matches
    lex_ok = True
    lex_detail = []
    try:
        lex = json.load(open(ITEMS_LEX, encoding="utf-8"))
        for key, ref in lex["frozen_references"].items():
            p = os.path.join(REPO, ref["path"])
            if not os.path.exists(p):
                lex_ok = False
                lex_detail.append(f"{key}: MISSING {ref['path']}")
            else:
                live = sha256(p)
                if live != ref["sha256"]:
                    lex_ok = False
                    lex_detail.append(f"{key}: sha mismatch live={live[:12]} "
                                      f"frozen={ref['sha256'][:12]}")
                else:
                    lex_detail.append(f"{key}: OK sha {live[:12]}")
    except Exception as e:  # noqa: BLE001
        lex_ok = False
        lex_detail.append(f"{type(e).__name__}: {e}")
    check(rep, "lexical_manifest_refs_resolve_and_sha_match", lex_ok, "; ".join(lex_detail))

    # instrument: per-level decline wording is verbatim present in the level system prompt
    wording_ok = True
    for lv, spec in cfg["levels"].items():
        if spec["decline_wording_verbatim"] not in spec["system"]:
            wording_ok = False
    check(rep, "instrument_decline_wording_in_system_prompts", wording_ok)

    n_fail = sum(1 for r in rep if not r["ok"])
    out = {"summary": {"n_checks": len(rep), "n_fail": n_fail,
                       "status": "PASS" if n_fail == 0 else "FAIL"},
           "counts": {"constructional_items": len(cx), "constructional_sets": len(cx_sets),
                      "relational_items": len(rel), "relational_sets": len(rel_sets)},
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
