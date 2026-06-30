#!/usr/bin/env python3
"""analyze.py — FROZEN scoring + pre-registered verdict map (no API calls).

Reads raw/{A,B,C}.json (written by probe.py) and scores each answer by substring-accept against
the frozen key (prep.py). Reports per-condition and per-indexical accuracy, the pre-registered
trigger-(c) verdict, and a C4 date-error breakdown. Writes results.json.

PRE-REGISTERED VERDICT (frozen before any call; see PREREG.md §verdict):
  * HEADLINE = pooled C1+C2+C3 CHARACTER-RULE accuracy per model (resolving 'I'/'you'/'here'/
    'now'/'today' and the embedded-origo binding to the correct DESCRIBED content).
  * essay trigger (c) FIRES for a model iff its pooled C1-C3 accuracy < 0.85 AND the misses are
    genuine WRONG-ENTITY / WRONG-ORIGO resolutions (not empty/parse-format failures).
  * A near-ceiling pass (>= 0.85, the expected outcome) is a NON-falsification: it is CONSISTENT
    with the essay's "character is distributionally native" AFFORDANCE half but does not PROVE it
    (an affordance is not provable from a ceiling; a failure would have falsified it).
  * C4 (temporal arithmetic) is SECONDARY/exploratory, reported descriptively. A DIRECTION error
    (e.g. 'yesterday' resolved to a FUTURE date) is a rule error and is flagged for trigger-(c)
    consideration; a pure MAGNITUDE slip (right direction, wrong count) is reported separately and
    fenced OUT of the trigger-(c) judgement.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from prep import ITEMS  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
SLOTS = ["A", "B", "C"]
MODEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
CHAR_CONDS = ("C1", "C2", "C3")
BY_ID = {it["id"]: it for it in ITEMS}


def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 -]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def correct(rec):
    a = norm(rec.get("answer"))
    return any(acc in a for acc in rec["accept"])


def iso_in(s):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", s or "")
    return m.group(1) if m else None


def c4_error_kind(rec):
    """Classify a C4 miss: 'direction' | 'magnitude' | 'noparse'."""
    it = BY_ID[rec["id"]]
    gold = date.fromisoformat(it["gold_iso"])
    base = date.fromisoformat(it["base_iso"])
    got = iso_in(rec.get("answer"))
    if not got:
        return "noparse"
    try:
        gd = date.fromisoformat(got)
    except ValueError:
        return "noparse"
    gold_sign = (gold - base).days
    got_sign = (gd - base).days
    if (gold_sign > 0) != (got_sign > 0) or got_sign == 0 and gold_sign != 0:
        return "direction"
    return "magnitude"


def main():
    data = {}
    for slot in SLOTS:
        p = RAW / f"{slot}.json"
        if not p.exists():
            sys.exit(f"missing {p} — run probe.py first")
        data[slot] = json.loads(p.read_text())

    results = {"model": {}, "verdict": {}}
    print(f"{'model':18} {'C1':>6} {'C2':>6} {'C3':>6} | {'char(C1-3)':>11} | "
          f"{'C4':>6} {'overall':>8}")
    for slot in SLOTS:
        recs = data[slot]
        by_cond = {c: [r for r in recs if r["cond"] == c] for c in ("C1", "C2", "C3", "C4")}
        acc = {c: sum(correct(r) for r in rs) / len(rs) for c, rs in by_cond.items()}
        char_recs = [r for r in recs if r["cond"] in CHAR_CONDS]
        char_acc = sum(correct(r) for r in char_recs) / len(char_recs)
        overall = sum(correct(r) for r in recs) / len(recs)
        # trigger-(c) gate: misses must be genuine wrong-entity (non-empty, parsed) resolutions
        char_misses = [r for r in char_recs if not correct(r)]
        wrong_entity = [r for r in char_misses if r["parse_mode"] != "empty" and r.get("answer")]
        fires = (char_acc < 0.85) and (len(wrong_entity) >= len(char_misses) - 0) \
            and len(char_misses) > 0
        # C4 error breakdown
        c4_kinds = {"direction": 0, "magnitude": 0, "noparse": 0}
        for r in by_cond["C4"]:
            if not correct(r):
                c4_kinds[c4_error_kind(r)] += 1
        n_parse_fail = sum(1 for r in recs if r["parse_mode"] == "empty")
        n_fallback = sum(1 for r in recs if r["parse_mode"] == "fallback")
        results["model"][slot] = {
            "name": MODEL[slot], "acc_by_cond": acc, "char_acc": char_acc, "overall": overall,
            "char_misses": [r["id"] for r in char_misses],
            "c4_error_kinds": c4_kinds, "trigger_c_fires": fires,
            "n_parse_empty": n_parse_fail, "n_parse_fallback": n_fallback,
        }
        print(f"{MODEL[slot]:18} {acc['C1']:>6.3f} {acc['C2']:>6.3f} {acc['C3']:>6.3f} | "
              f"{char_acc:>11.3f} | {acc['C4']:>6.3f} {overall:>8.3f}")

    any_fire = any(results["model"][s]["trigger_c_fires"] for s in SLOTS)
    results["verdict"] = {
        "trigger_c_fires_any_model": any_fire,
        "reading": ("FALSIFICATION: at least one model systematically mis-applies indexical "
                    "character to a described context (trigger (c) FIRES)." if any_fire else
                    "NON-FALSIFICATION: all models apply indexical character at/above the 0.85 "
                    "bar on described contexts (C1-C3); consistent with the essay's "
                    "'distributionally native' affordance half, does not prove it."),
    }
    print("\nVERDICT:", results["verdict"]["reading"])
    for slot in SLOTS:
        m = results["model"][slot]
        if m["char_misses"]:
            print(f"  {m['name']} C1-C3 misses: {m['char_misses']}")
        c4e = m["c4_error_kinds"]
        if sum(c4e.values()):
            print(f"  {m['name']} C4 errors: {c4e}")
    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
