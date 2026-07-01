#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the as-if origo probe. NO API CALLS (reads raw/*.json).

Per item, from the FINAL answer text:
  * resolved_to_nonce  — the answer contains a nonce token for the item's indexical
                         (prep.NONCE_ACCEPT), i.e. the model bound 'now'/'today'/'here' to the
                         value the clock/location TOOL returned (17:42 / 3021-11-08 / Qethport).
  * resolved_to_narrated (control only) — the answer contains one of the scenario's narrated
                         surface variants (descriptive; the load-bearing control gate is
                         nonce-ABSENCE, robust regardless of narrated-accept coverage).
  * hedged (baseline heuristic) — the answer contains a no-access / uncertainty phrase.

Per (model, arm) rates:
  test:     spontaneous_query_rate, resolution_to_tool_state_rate (== resolved_to_nonce rate)
  control:  spurious_override_rate (== resolved_to_nonce rate; should be LOW),
            resolve_from_narrated_rate (descriptive), tool_query_rate
  baseline: nonce_rate (structurally 0 — no tool), hedge_rate (heuristic), answered_rate

VERDICT (thresholds pre-registered in PREREG.md — NOT tuned here):
  T   = 0.80  (test spontaneous-query and resolution thresholds)
  OVR = 0.20  (control spurious-override ceiling)
  CONFIRM : >= 2 of 3 models have test spontaneous_query_rate >= T AND
            resolution_to_tool_state_rate >= T, AND each of those models' control
            spurious_override_rate <= OVR.
  NULL    : >= 2 of 3 models have spontaneous_query_rate < T OR resolution_to_tool_state_rate < T.
  MIXED   : anything else (models split; query-without-resolve; control override > OVR on a model
            that otherwise clears the test thresholds).

Usage: python3 analyze.py     # prints per-model tables + verdict; writes results.json
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

T = 0.80     # pre-registered test-arm threshold (spontaneous-query and resolution)
OVR = 0.20   # pre-registered control-arm spurious-override ceiling

HEDGE_MARKERS = [
    "don't have", "do not have", "cannot", "can't", "unable", "no access",
    "not able", "i don't know", "i do not know", "real-time", "real time",
    "current time or date", "access to the current", "as an ai", "i'm not able",
    "don't actually", "no way to know", "isn't something i", "not something i can",
]


def contains_any(text, tokens):
    low = (text or "").lower()
    return any(tok.lower() in low for tok in tokens)


def score_records(recs):
    """Return per-arm aggregates for one model's records."""
    arms = {}
    for r in recs:
        arm = r["arm"]
        a = arms.setdefault(arm, {"n": 0, "spont": 0, "nonce": 0, "narrated": 0,
                                   "hedge": 0, "answered": 0, "items": []})
        a["n"] += 1
        nonce = contains_any(r["final_content"], r_nonce(r))
        narrated = contains_any(r["final_content"], r_narrated(r))
        hedged = contains_any(r["final_content"], HEDGE_MARKERS)
        if r.get("spontaneous_query"):
            a["spont"] += 1
        if nonce:
            a["nonce"] += 1
        if narrated:
            a["narrated"] += 1
        if hedged:
            a["hedge"] += 1
        if not hedged and (r["final_content"] or "").strip():
            a["answered"] += 1
        a["items"].append({"id": r["id"], "spont": r.get("spontaneous_query"),
                           "tools_called": r.get("tools_called"), "nonce": nonce,
                           "narrated": narrated, "hedged": hedged,
                           "final": (r["final_content"] or "")[:200]})
    return arms


# The accept lists are frozen in the item, so read them straight off each record. (prep also holds
# NONCE_ACCEPT keyed by indexical; the record carries the resolved list already.)
def r_nonce(r):
    return r.get("nonce_accept") or []


def r_narrated(r):
    return r.get("narrated_accept") or []


def rate(x, n):
    return round(x / n, 3) if n else 0.0


def summarize(slot, recs):
    arms = score_records(recs)
    out = {"slot": slot}
    t = arms.get("test", {})
    c = arms.get("control", {})
    b = arms.get("baseline", {})
    out["test"] = {
        "n": t.get("n", 0),
        "spontaneous_query_rate": rate(t.get("spont", 0), t.get("n", 0)),
        "resolution_to_tool_state_rate": rate(t.get("nonce", 0), t.get("n", 0)),
    }
    out["control"] = {
        "n": c.get("n", 0),
        "tool_query_rate": rate(c.get("spont", 0), c.get("n", 0)),
        "spurious_override_rate": rate(c.get("nonce", 0), c.get("n", 0)),
        "resolve_from_narrated_rate": rate(c.get("narrated", 0), c.get("n", 0)),
    }
    out["baseline"] = {
        "n": b.get("n", 0),
        "nonce_rate": rate(b.get("nonce", 0), b.get("n", 0)),   # structurally 0 (no tool)
        "hedge_rate": rate(b.get("hedge", 0), b.get("n", 0)),
        "answered_rate": rate(b.get("answered", 0), b.get("n", 0)),
    }
    out["_arms_detail"] = arms
    return out


def verdict(per_model):
    """Apply the pre-registered thresholds. Returns (label, rationale)."""
    clears_test = []   # models clearing BOTH test thresholds
    fails_test = []    # models failing at least one test threshold
    override_ok = {}   # model -> control spurious_override_rate <= OVR
    for m in per_model:
        sl = m["slot"]
        sq = m["test"]["spontaneous_query_rate"]
        rr = m["test"]["resolution_to_tool_state_rate"]
        ov = m["control"]["spurious_override_rate"]
        override_ok[sl] = ov <= OVR
        if sq >= T and rr >= T:
            clears_test.append(sl)
        else:
            fails_test.append(sl)
    confirm_models = [sl for sl in clears_test if override_ok[sl]]
    if len(confirm_models) >= 2:
        return ("CONFIRM",
                f"{len(confirm_models)}/3 models ({','.join(confirm_models)}) clear both test "
                f"thresholds (>= {T}) AND keep control spurious-override <= {OVR}.")
    if len(fails_test) >= 2:
        return ("NULL",
                f"{len(fails_test)}/3 models ({','.join(fails_test)}) fall below a test threshold "
                f"(< {T} on spontaneous-query and/or resolution).")
    return ("MIXED",
            f"clears_test={clears_test} (override_ok={[s for s in clears_test if override_ok[s]]}), "
            f"fails_test={fails_test}; no >=2 majority for either pole.")


def main():
    per_model = []
    for slot in ("A", "B", "C"):
        f = HERE / "raw" / f"{slot}.json"
        if not f.exists():
            print(f"(missing raw/{slot}.json — skipping)")
            continue
        recs = json.loads(f.read_text())
        per_model.append(summarize(slot, recs))
    if not per_model:
        sys.exit("no raw results found")
    print("=" * 78)
    for m in per_model:
        print(f"\n[{m['slot']}]")
        print(f"  test     n={m['test']['n']:2d}  spontaneous_query={m['test']['spontaneous_query_rate']:.2f}"
              f"  resolution_to_tool_state={m['test']['resolution_to_tool_state_rate']:.2f}")
        print(f"  control  n={m['control']['n']:2d}  tool_query={m['control']['tool_query_rate']:.2f}"
              f"  spurious_override={m['control']['spurious_override_rate']:.2f}"
              f"  resolve_from_narrated={m['control']['resolve_from_narrated_rate']:.2f}")
        print(f"  baseline n={m['baseline']['n']:2d}  nonce={m['baseline']['nonce_rate']:.2f}"
              f"  hedge={m['baseline']['hedge_rate']:.2f}  answered={m['baseline']['answered_rate']:.2f}")
    label, rationale = verdict(per_model)
    print("\n" + "=" * 78)
    print(f"VERDICT: {label}\n  {rationale}")
    # strip heavy detail before writing the headline results file
    slim = []
    for m in per_model:
        mm = {k: v for k, v in m.items() if k != "_arms_detail"}
        slim.append(mm)
    (HERE / "results.json").write_text(json.dumps(
        {"thresholds": {"T": T, "OVR": OVR}, "verdict": label, "rationale": rationale,
         "per_model": slim}, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
