#!/usr/bin/env python3
"""probe.py — relational history-perturbation probe v4 (the finding-bearing instrument).

Adapted from v3 probe.py; v4 changes per the design
(experiments/designs/relational-history-perturbation-v4.md):

- STAMPED rendering: each evidence line is "- Round k: ...", and the INTRO states the round
  number (not line order) carries chronology. This is what makes Delta_chron (stamp) and
  Delta_pos (line order) separable within one arm.
- PANEL: claude + gemini only (gpt dropped from the finding-bearing panel).
- CONTROLS: per cluster, 2 consistent (monotonic stamps) + 2 stamp-respect (shuffled
  stamps); the manipulation gate = all 4 correct. stamp-respect is the v4-specific control
  that licenses the Delta_chron reading.

Carried verbatim from v3: the forced single-label elicitation, the never-parse-truncated
rule (critic blocker 2), the freeze gate (PREREG.md must exist; preflight/full require the
stimuli sha256 in PREREG.md + a passed liveness gate), the cost ledger + per-record hard
stop + per-model checkpoint, crash-safe JSONL resume.

Usage (from repo root or this dir):
  python3 probe.py liveness    # 2 calls, one per model — the format gate; never analyzed
  python3 probe.py preflight   # consistent controls (1/cluster) per model; never analyzed
  python3 probe.py full        # all trials -> raw/probe-<model>.jsonl
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (MODELS, RAW, HARD_STOP_USD, PROBE_SYS, INTRO,  # noqa: E402
                    call_forced, flat_cost, grid_block, render_history, ledger_append,
                    ledger_total, check_hard_stop, append_jsonl, read_jsonl)

STIMULI_PATH = os.path.join(HERE, "stimuli.json")
PREREG_PATH = os.path.join(HERE, "PREREG.md")
LIVENESS_PATH = os.path.join(RAW, "liveness.json")
EST_PER_CALL_FALLBACK = 0.0015


def trial_uid(t):
    if t["kind"] == "mixed":
        return f"mixed:{t['pair']}:{t['sample']}:{t['clast']}:{t['dpos']}:{t['variant']}"
    return f"{t['kind']}:{t['pair']}:{t['sample']}:{t['target']}"


def freeze_gate(mode):
    if not os.path.exists(PREREG_PATH):
        sys.exit("FREEZE GATE: PREREG.md does not exist in the run dir. The PREREG is "
                 "frozen only after the independent pre-run critic pass "
                 "(PREREG-draft.md does NOT count). Refusing to run.")
    if mode == "liveness":
        return
    prereg = open(PREREG_PATH).read()
    h = hashlib.sha256(open(STIMULI_PATH, "rb").read()).hexdigest()
    if h not in prereg:
        sys.exit(f"FREEZE GATE: stimuli.json sha256 {h[:12]}... is not recorded in "
                 "PREREG.md. Commit the frozen hash (post-critic) before any "
                 "finding-bearing call. Refusing to run.")
    if not os.path.exists(LIVENESS_PATH):
        sys.exit("FORMAT GATE: no raw/liveness.json — run `probe.py liveness` first; all "
                 "models must return a parseable label under the forced format.")
    live = json.load(open(LIVENESS_PATH))
    bad = [m for m in MODELS if not live.get(m, {}).get("pass")]
    if bad:
        sys.exit(f"FORMAT GATE: liveness failed for {bad} — fix elicitation (and log the "
                 "fix in PREREG.md) before preflight/full.")


def build_user(t, stim):
    p_order = [tuple(x) for x in stim["clusters"][t["cluster"]]]
    p_block = grid_block(p_order, stim["figures"])
    labels = {l for l, _ in p_order}
    label_list = ", ".join(l for l, _ in p_order)
    hist = render_history([(k, d) for k, d in t["stamped"]])
    user = (f"Your figures:\n{p_block}\n\n{INTRO.format(nonce=t['nonce'])}\n{hist}\n\n"
            f"The target is referred to as: \"{t['nonce']}\".\n\n"
            f"Which of your figures is it? Reply with exactly one label ({label_list}) "
            f"and nothing else.")
    return p_order, labels, label_list, user


def run_one(mname, t, stim):
    p_order, labels, label_list, user = build_user(t, stim)
    r, pick, pmode, retried, usages = call_forced(
        MODELS[mname], PROBE_SYS.format(example=p_order[0][0]), user, labels, label_list)
    pick_cid = next((c for l, c in p_order if l == pick), None)
    rec = dict(t)
    rec.update({"model": mname, "uid": trial_uid(t), "pick": pick, "pick_cid": pick_cid,
                "parse_mode": pmode, "retried": retried,
                "finish_reason": r.get("finish_reason"), "raw": r.get("content"),
                "usage": usages, "err": r.get("error")})
    if t["kind"] == "mixed":
        rec["in_pair"] = pick_cid in (t["X"], t["Y"])
        rec["picked_chron_last"] = (pick_cid == t["clast_cid"]) if rec["in_pair"] else None
        rec["picked_phys_last"] = (pick_cid == t["last_cid"]) if rec["in_pair"] else None
    else:
        rec["correct"] = (pick_cid == t["target"])
    return rec


LEDGER = os.path.join(RAW, "cost-ledger.json")


def preflight_subset(stim, mname):
    """One consistent control per cluster (X-twin). Never analyzed; `full` supersedes."""
    return [t for t in stim["trials"][mname] if t["kind"] == "consistent"
            and t["target"] == t["X"]]


def preflight_per_call(mname):
    entries = (json.load(open(LEDGER)) if os.path.exists(LEDGER) else [])
    for e in reversed(entries):
        if e["phase"] == f"preflight:{mname}" and e["calls"]:
            return e["billed_usd"] / e["calls"]
    # fall back to any model's preflight figure, else the static fallback
    for e in reversed(entries):
        if e["phase"].startswith("preflight:") and e["calls"]:
            return e["billed_usd"] / e["calls"]
    return EST_PER_CALL_FALLBACK


def per_call_est(mname, run_recs):
    mine = [r for r in run_recs if r["model"] == mname]
    if mine:
        tot, have, _ = flat_cost(mine)
        if have:
            return tot / len(mine)
    return preflight_per_call(mname)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    if mode not in ("liveness", "preflight", "full"):
        print("usage: probe.py [liveness|preflight|full]")
        return
    freeze_gate(mode)
    stim = json.load(open(STIMULI_PATH))
    os.makedirs(RAW, exist_ok=True)

    if mode == "liveness":
        check_hard_stop(len(MODELS) * EST_PER_CALL_FALLBACK, "liveness")
        out, recs = {}, []
        for mname in MODELS:
            t = next(t for t in stim["trials"][mname] if t["kind"] == "mixed")
            r = run_one(mname, t, stim)
            out[mname] = {"pick": r["pick"], "parse_mode": r["parse_mode"],
                          "retried": r["retried"], "pass": r["pick"] is not None,
                          "raw": r["raw"]}
            recs.append(r)
            print(f"  {mname:7s}: pick={r['pick']!r} mode={r['parse_mode']} "
                  f"retried={r['retried']} raw={str(r['raw'])[:60]!r}")
        json.dump(out, open(LIVENESS_PATH, "w"), indent=2)
        tot, have, miss = flat_cost(recs)
        ledger_append("liveness", len(recs), tot, miss, "format gate; never analyzed")
        if all(v["pass"] for v in out.values()):
            print("FORMAT GATE PASSED (all models parseable).")
        else:
            print("FORMAT GATE FAILED — fix elicitation, log it in PREREG.md, re-run.")

    elif mode == "preflight":
        all_recs = []
        for mname in MODELS:
            ctrl = preflight_subset(stim, mname)
            check_hard_stop(len(ctrl) * EST_PER_CALL_FALLBACK, f"preflight:{mname}")
            recs = [run_one(mname, t, stim) for t in ctrl]
            all_recs += recs
            tot, have, miss = flat_cost(recs)
            nfail = sum(1 for r in recs if r["pick"] is None)
            nstrict = sum(1 for r in recs if r["parse_mode"] == "strict")
            acc = sum(1 for r in recs if r.get("correct")) / len(recs)
            ledger_append(f"preflight:{mname}", len(recs), tot, miss,
                          f"{mname} consistent controls; never analyzed")
            print(f"PREFLIGHT ({mname}, {len(recs)} controls): {nfail} NA, "
                  f"strict={nstrict}/{len(recs)}, control acc={acc:.2f}, "
                  f"billed=${tot:.5f} (${tot / len(recs):.5f}/call)")
            if acc < 1.0:
                print("  NOTE: certified stimuli should put control accuracy near "
                      "ceiling — if it is low here, stop and investigate before `full`.")
        json.dump(all_recs, open(os.path.join(RAW, "preflight.json"), "w"), indent=2)
        proj = sum(len(stim["trials"][m]) * preflight_per_call(m) for m in MODELS)
        n_full = sum(len(stim["trials"][m]) for m in MODELS)
        print(f"  full-run extrapolation (per-model per-call figures): {n_full} calls "
              f"~= ${proj:.3f} — NOT analyzed; full supersedes")

    elif mode == "full":
        proj0 = sum(len(stim["trials"][m]) * preflight_per_call(m) for m in MODELS)
        check_hard_stop(proj0 * 1.2, "full (1.2x retry headroom)")
        prior_spend = ledger_total()
        run_recs = []
        todos = {}
        for mname in MODELS:
            done = {r["uid"] for r in read_jsonl(os.path.join(RAW, f"probe-{mname}.jsonl"))}
            todos[mname] = [t for t in stim["trials"][mname] if trial_uid(t) not in done]
        order = list(MODELS)
        for i, mname in enumerate(order):
            path = os.path.join(RAW, f"probe-{mname}.jsonl")
            todo = todos[mname]
            done_n = len(stim["trials"][mname]) - len(todo)
            spent_now = prior_spend + flat_cost(run_recs)[0]
            proj_rest = sum(len(todos[m2]) * per_call_est(m2, run_recs) for m2 in order[i:])
            print(f"=== {mname} === ({len(todo)} to run, {done_n} already recorded)")
            print(f"  [checkpoint] spent ${spent_now:.4f} + projected remaining "
                  f"${proj_rest:.4f} = ${spent_now + proj_rest:.4f} "
                  f"(hard stop ${HARD_STOP_USD:.2f})")
            if spent_now + proj_rest > HARD_STOP_USD:
                tot, have, miss = flat_cost(run_recs)
                if run_recs:
                    ledger_append("full(ABORTED)", len(run_recs), tot, miss,
                                  "per-model checkpoint: projected total over hard stop")
                sys.exit(f"HARD STOP (per-model checkpoint before {mname}): projected "
                         f"total ${spent_now + proj_rest:.4f} > ${HARD_STOP_USD:.2f}. "
                         f"Raw kept; re-design, don't push through.")
            for t in todo:
                rec = run_one(mname, t, stim)
                append_jsonl(path, rec)
                run_recs.append(rec)
                spent_now = prior_spend + flat_cost(run_recs)[0]
                if spent_now >= HARD_STOP_USD:
                    tot, have, miss = flat_cost(run_recs)
                    ledger_append("full(ABORTED)", len(run_recs), tot, miss,
                                  "hard stop hit mid-run")
                    sys.exit(f"HARD STOP MID-RUN: cumulative billed ${spent_now:.4f} >= "
                             f"${HARD_STOP_USD:.2f}. Raw kept; re-design, don't push "
                             f"through.")
            t_m, _, _ = flat_cost([r for r in run_recs if r["model"] == mname])
            print(f"  {mname}: billed this run ${t_m:.5f}")
        tot, have, miss = flat_cost(run_recs)
        ledger_append("full", len(run_recs), tot, miss, "THE finding-bearing dataset")
        nrec = sum(len(read_jsonl(os.path.join(RAW, f"probe-{m}.jsonl"))) for m in MODELS)
        na = retr = strict = 0
        for m in MODELS:
            for r in read_jsonl(os.path.join(RAW, f"probe-{m}.jsonl")):
                na += r["pick"] is None
                retr += bool(r.get("retried"))
                strict += r.get("parse_mode") == "strict"
        print(f"\nFULL: {nrec} records on disk ({na} NA, {retr} retried, "
              f"{strict} strict), this run billed=${tot:.5f} "
              f"(have={have} missing={miss})")


if __name__ == "__main__":
    main()
