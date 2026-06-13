#!/usr/bin/env python3
"""probe.py — relational history-perturbation probe v3 (the finding-bearing instrument).

Adapted from v2 probe.py; v3 changes per the design
(experiments/designs/relational-history-perturbation-v3.md):

- FIX 1 (elicitation): forced single-label format ("reply with EXACTLY ONE figure label
  and NOTHING ELSE"), completion cap 512 (v2: 128) so truncation is RARE — not
  impossible. Critic blocker 2 (2026-06-13): a reply with finish_reason == "length" is
  NEVER parsed for a pick (its text is a truncated prefix) — parse-fail -> stern retry
  -> NA; finish_reason recorded per call. gemini keeps reasoning effort "minimal";
  pre-registered strict parse rule (strict / non-strict / NA-after-one-stern-retry)
  with per-record compliance flags.
- FREEZE GATE: every mode refuses to run unless PREREG.md exists in this directory
  (PREREG-draft.md does NOT count); `preflight` and `full` additionally require the
  sha256 of stimuli.json to appear verbatim in PREREG.md, and a passed liveness
  format-gate (raw/liveness.json, all three models parseable).
- COST GATES: pre-registered HARD STOP at $1.50 projected total (common.py ledger);
  `full` re-checks cumulative billed cost after every record AND runs a PER-MODEL
  CHECKPOINT (critic S2) before each model's batch — projected total from REALIZED
  per-call billed costs (this run's own figures where available, per-model preflight
  figures otherwise) must stay <= $1.50 or it aborts. Preflight covers gpt AND claude
  controls (critic S2: the projection must see the priciest model, not gpt-only).
- Raw output is JSONL per model (raw/probe-<model>.jsonl), appended record-by-record
  (crash-safe); re-running `full` skips already-recorded trial uids (transport-crash
  resume; it is NOT a license to continue past a cost abort).

Everything else mirrors v2 byte-identically where the design says "unchanged": the
history intro per direction, the '- partner said "…" -> you FOUND it' line format, no
round-number labels, one frozen matcher array per cluster (now read from stimuli.json),
liveness/preflight raw never analyzed (`full` is the only finding-bearing dataset).

Usage (from repo root or this dir):
  python3 probe.py liveness    # 3 calls, one per model — the format gate; never analyzed
  python3 probe.py preflight   # 18 calls (9 gpt + 9 claude controls); never analyzed
  python3 probe.py full        # 432 calls (+retries) -> raw/probe-<model>.jsonl
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (MODELS, RAW, HARD_STOP_USD, PROBE_SYS, INTRO,  # noqa: E402
                    call_forced, flat_cost, grid_block, ledger_append, ledger_total,
                    check_hard_stop, append_jsonl, read_jsonl)

STIMULI_PATH = os.path.join(HERE, "stimuli.json")
PREREG_PATH = os.path.join(HERE, "PREREG.md")
LIVENESS_PATH = os.path.join(RAW, "liveness.json")
EST_PER_CALL_FALLBACK = 0.0015  # used only if no preflight billed figure exists


def trial_uid(t):
    if t["kind"] == "mixed":
        return f"mixed:{t['pair']}:{t['sample']}:{t['order']}:{t['direction']}"
    # controls now run in BOTH directions (critic S1), so direction is part of the uid
    return f"consistent:{t['pair']}:{t['sample']}:{t['target']}:{t['direction']}"


def freeze_gate(mode):
    """REFUSE to run unless PREREG.md exists (PREREG-draft.md does not count); for
    preflight/full also require the frozen stimuli hash in PREREG.md + liveness pass."""
    if not os.path.exists(PREREG_PATH):
        sys.exit("FREEZE GATE: PREREG.md does not exist in the run dir. The PREREG is "
                 "frozen only after the independent pre-run critic pass "
                 "(PREREG-draft.md does NOT count). Refusing to run.")
    if mode == "liveness":
        return
    prereg = open(PREREG_PATH).read()
    h = hashlib.sha256(open(STIMULI_PATH, "rb").read()).hexdigest()
    if h not in prereg:
        sys.exit(f"FREEZE GATE: stimuli.json sha256 {h[:12]}… is not recorded in "
                 "PREREG.md. Commit the frozen hash (post-critic) before any "
                 "finding-bearing call. Refusing to run.")
    if not os.path.exists(LIVENESS_PATH):
        sys.exit("FORMAT GATE: no raw/liveness.json — run `probe.py liveness` first; all "
                 "three models must return a parseable label under the forced format.")
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
    lines = t["lines"] if t["direction"] == "fwd" else list(reversed(t["lines"]))
    hist = "\n".join(f'- partner said "{d}" -> you FOUND it' for d in lines)
    user = (f"Your figures:\n{p_block}\n\n{INTRO[t['direction']]}\n{hist}\n\n"
            f"The target is referred to as: \"{t['nonce']}\"\n\n"
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
        rec["picked_chron_last"] = (pick_cid == t["last"]) if rec["in_pair"] else None
        phys_last = t["last"] if t["direction"] == "fwd" else t["first"]
        rec["picked_phys_last"] = (pick_cid == phys_last) if rec["in_pair"] else None
    else:
        rec["correct"] = (pick_cid == t["target"])
    return rec


PREFLIGHT_MODELS = ("gpt", "claude")  # critic S2: must include claude, not gpt-only
LEDGER = os.path.join(RAW, "cost-ledger.json")


def preflight_subset(stim, mname):
    """One control per cluster (the X-twin fwd control): 9 trials/model. Never analyzed;
    `full` re-runs the same trials as finding-bearing data and supersedes."""
    return [t for t in stim["trials"][mname] if t["kind"] == "consistent"
            and t["direction"] == "fwd" and t["target"] == t["X"]]


def preflight_per_call(mname):
    """Billed per-call figure from the per-model preflight ledger entry; gemini (not
    preflighted — cheaper than gpt per the rate history) proxies via gpt's figure."""
    entries = (json.load(open(LEDGER)) if os.path.exists(LEDGER) else [])
    want = mname if mname in PREFLIGHT_MODELS else "gpt"
    for e in reversed(entries):
        if e["phase"] == f"preflight:{want}" and e["calls"]:
            return e["billed_usd"] / e["calls"]
    return EST_PER_CALL_FALLBACK


def per_call_est(mname, run_recs):
    """Realized per-call billed cost for mname FROM THIS RUN where available (critic S2:
    the per-model checkpoint projects from realized costs), else its preflight figure."""
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
        # Format gate (design §Elicitation): one mixed trial per model; all three must
        # return a parseable label under the forced format. Never analyzed.
        check_hard_stop(3 * EST_PER_CALL_FALLBACK, "liveness")
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
            print("FORMAT GATE PASSED (all three parseable).")
        else:
            print("FORMAT GATE FAILED — fix elicitation, log it in PREREG.md, re-run.")

    elif mode == "preflight":
        # critic S2: gpt AND claude controls (one per cluster each, 9 + 9 = 18 calls),
        # so the $1.50 projection sees the priciest model, not gpt-only. Never analyzed.
        all_recs = []
        for mname in PREFLIGHT_MODELS:
            ctrl = preflight_subset(stim, mname)
            check_hard_stop(len(ctrl) * EST_PER_CALL_FALLBACK, f"preflight:{mname}")
            recs = [run_one(mname, t, stim) for t in ctrl]
            all_recs += recs
            tot, have, miss = flat_cost(recs)
            nfail = sum(1 for r in recs if r["pick"] is None)
            nstrict = sum(1 for r in recs if r["parse_mode"] == "strict")
            acc = sum(1 for r in recs if r.get("correct")) / len(recs)
            ledger_append(f"preflight:{mname}", len(recs), tot, miss,
                          f"{mname} controls; never analyzed")
            print(f"PREFLIGHT ({mname}, {len(recs)} controls): {nfail} NA, "
                  f"strict={nstrict}/{len(recs)}, control acc={acc:.2f}, "
                  f"billed=${tot:.5f} (${tot / len(recs):.5f}/call)")
            if acc < 1.0:
                print("  NOTE: certified stimuli should put control accuracy near "
                      "ceiling — if it is low here, stop and investigate before `full`.")
        json.dump(all_recs, open(os.path.join(RAW, "preflight.json"), "w"), indent=2)
        proj = sum(len(stim["trials"][m]) * preflight_per_call(m) for m in MODELS)
        n_full = sum(len(stim["trials"][m]) for m in MODELS)
        print(f"  full-run extrapolation (per-model per-call figures; gemini via gpt "
              f"proxy): {n_full} calls ~= ${proj:.3f} — NOT analyzed; full supersedes")

    elif mode == "full":
        # global pre-check from per-model preflight figures (claude included, critic S2)
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
            # PER-MODEL CHECKPOINT (critic S2): projected total = spent so far +
            # remaining trials priced at REALIZED per-call billed costs (this run's own
            # figures where available, per-model preflight figures otherwise).
            spent_now = prior_spend + flat_cost(run_recs)[0]
            proj_rest = sum(len(todos[m2]) * per_call_est(m2, run_recs)
                            for m2 in order[i:])
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
