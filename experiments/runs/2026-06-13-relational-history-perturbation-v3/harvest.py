#!/usr/bin/env python3
"""harvest.py — fresh description harvest for ALL THREE models (v3 fix 2, uniform).

Design (experiments/designs/relational-history-perturbation-v3.md §Stimuli plan):
per (model x figure), ONE harvest call mirroring the v1 director framing — the 6-figure
array with the target marked, the v1 <=12-word budget — requesting 8 candidate
descriptions in a numbered list, temperature 0.

BATCH-HARVEST RATIONALE, DISCLOSED (design open issue 2 for the pre-run critic): 8
candidates in one numbered-list call is cheap and deterministic (temperature 0); the
worry that list-generation yields a different register than one-at-a-time generation is
explicitly left to the critic — if the critic rules the other way, switch to
one-description-per-call at temperature 0.8 BEFORE the stimuli freeze.

SHORTFALL PROCEDURE (pre-registered): if, after certification, a figure has fewer than 6
certified descriptions, `harvest.py topup` makes ONE top-up call for that figure at
temperature 0.8, logged with phase="topup". If still short after re-certification, that
model's sample count drops and the reduced cluster count is recorded in PREREG.md BEFORE
the stimuli freeze.

Harvest raw is STIMULUS-CONSTRUCTION data: kept, never analyzed as findings (v2 rule S2,
extended).

MECHANICAL FILTERS AT HARVEST TIME (critic S4, 2026-06-13): the <=12-word budget is
enforced HERE, before certification — over-budget lines are logged in the harvest record
(`dropped_over_budget`) and never become candidates, so they cannot reach a certification
call. certify.py keeps its own budget check as defense in depth. A length-truncated
harvest reply (finish_reason == "length", critic blocker 2) drops its LAST parsed line
(possibly cut mid-text), logged as `dropped_truncated_tail`. Deduplication (within figure
+ against the twin) stays in certify.py, which needs the cross-figure view.

Usage (from repo root or this dir):
  python3 harvest.py plan      # no API calls: prints planned calls + cost estimate
  python3 harvest.py harvest   # 18 calls (3 models x 6 figures), temperature 0
  python3 harvest.py topup     # <=18 calls, temperature 0.8, only for shortfall figures
"""
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (MODELS, MODEL_SEED_OFFSET, SEED0, N_CAND, WORD_BUDGET, RAW,  # noqa: E402
                    call_fr, load_figures, grid_block, reasoning_for, flat_cost,
                    ledger_append, check_hard_stop, append_jsonl, read_jsonl)

HARVEST_PATH = os.path.join(RAW, "harvest.jsonl")
REPORT_PATH = os.path.join(HERE, "certification_report.json")
EST_PER_CALL = 0.003  # director-shaped, generous (design table: <=36 calls ~ $0.05)

# v1 director framing (game.py DIRECTOR_SYS), adapted only to ask for a numbered list of
# N_CAND candidates instead of a single description.
HARVEST_SYS = (
    "You are playing a reference game with a partner. You both see the SAME set of abstract "
    "figures, but each in a DIFFERENT private order with DIFFERENT labels, so you CANNOT refer to "
    "a figure by its label or position -- only by describing what it looks like. Each figure is an "
    "8x8 grid of '#' (filled) and '.' (empty). You are the DIRECTOR: describe the TARGET figure so "
    "your partner can pick it out of their own copies. Give {n} DIFFERENT candidate descriptions "
    "of the TARGET, each at most {budget} words; a short memorable label is best. Reply with ONLY "
    "a numbered list (1. to {n}.), one description per line, no preamble.")

NUM_RE = re.compile(r"^\s*\d+\s*[.)]\s*(.+?)\s*$")


def director_array(mname, figs):
    """One deterministic director permutation per model, constant across its 6 harvest
    calls (mirrors v1, where the director array was constant within a game)."""
    rng = random.Random(SEED0 ^ 0xD17 ^ MODEL_SEED_OFFSET[mname])
    ids = sorted(figs)
    rng.shuffle(ids)
    order = [(f"D{i+1}", cid) for i, cid in enumerate(ids)]
    label_of = {cid: lab for lab, cid in order}
    return order, label_of


def parse_candidates(txt):
    """Numbered-list lines -> candidate strings (normalized whitespace, outer quotes off)."""
    out = []
    for ln in (txt or "").splitlines():
        m = NUM_RE.match(ln)
        if m:
            c = " ".join(m.group(1).strip().strip('"').split())
            if c:
                out.append(c)
    return out


def harvest_call(mname, model, figs, fid, temperature, phase):
    d_order, d_label = director_array(mname, figs)
    d_block = grid_block(d_order, figs)
    user = (f"Your figures:\n{d_block}\n\nTARGET: {d_label[fid]}\n"
            f"Give {N_CAND} different candidate descriptions of the TARGET "
            f"(each <= {WORD_BUDGET} words).")
    r = call_fr(model, HARVEST_SYS.format(n=N_CAND, budget=WORD_BUDGET), user,
                max_tokens=512, temperature=temperature, reasoning=reasoning_for(model))
    cands = parse_candidates(r.get("content"))
    # critic blocker 2: a length-truncated list's LAST parsed line may be cut mid-text —
    # drop it (logged), never let a truncated tail become a candidate.
    dropped_tail = []
    if r.get("finish_reason") == "length" and cands:
        dropped_tail = [cands.pop()]
    # critic S4: enforce the <=12-word budget mechanically AT HARVEST, before
    # certification — over-budget lines never reach a certification call.
    over = [c for c in cands if len(c.split()) > WORD_BUDGET]
    cands = [c for c in cands if len(c.split()) <= WORD_BUDGET]
    rec = {"phase": phase, "model": mname, "fig": fid, "temperature": temperature,
           "n_candidates": len(cands), "candidates": cands,
           "dropped_over_budget": over, "dropped_truncated_tail": dropped_tail,
           "finish_reason": r.get("finish_reason"),
           "raw": r.get("content"), "usage": [r.get("usage", {})], "err": r.get("error")}
    append_jsonl(HARVEST_PATH, rec)
    note = (f"  ERR={r.get('error')}" if r.get("error") else "") + \
           (f"  over-budget dropped={len(over)}" if over else "") + \
           ("  TRUNCATED tail dropped" if dropped_tail else "")
    print(f"  {mname:7s} {fid} [{phase} t={temperature}]: {len(cands)} candidates{note}")
    return rec


def shortfall_figs():
    """(model, fig) pairs with < 6 certified descriptions, per certification_report.json."""
    if not os.path.exists(REPORT_PATH):
        sys.exit("topup requires certification_report.json — run certify.py first.")
    rep = json.load(open(REPORT_PATH))
    out = []
    for m, md in rep["models"].items():
        for fid, fd in sorted(md["figures"].items()):
            if fd["certified_n"] < 6:
                out.append((m, fid, fd["certified_n"]))
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
    figs = load_figures()
    if mode == "plan":
        n = len(MODELS) * len(figs)
        print(f"PLAN: harvest = {n} calls (3 models x 6 figures, 1 call each, temperature 0); "
              f"topup <= {n} more at temperature 0.8 (shortfall only).")
        print(f"  est. ${n * EST_PER_CALL:.3f} harvest (+ up to the same in top-ups); "
              f"design table: <=36 calls ~ $0.05. No API call made by `plan`.")
        return
    if mode == "harvest":
        existing = [r for r in read_jsonl(HARVEST_PATH) if r["phase"] == "harvest"]
        done = {(r["model"], r["fig"]) for r in existing}
        todo = [(m, fid) for m in MODELS for fid in sorted(figs) if (m, fid) not in done]
        if not todo:
            sys.exit("harvest already complete (all 18 records in raw/harvest.jsonl).")
        check_hard_stop(len(todo) * EST_PER_CALL, "harvest")
        recs = [harvest_call(m, MODELS[m], figs, fid, 0, "harvest") for m, fid in todo]
        tot, have, miss = flat_cost(recs)
        ledger_append("harvest", len(recs), tot, miss,
                      "stimulus-construction data; never analyzed as findings")
    elif mode == "topup":
        prior_topup = {(r["model"], r["fig"]) for r in read_jsonl(HARVEST_PATH)
                       if r["phase"] == "topup"}
        short = shortfall_figs()
        todo = [(m, fid, n) for m, fid, n in short if (m, fid) not in prior_topup]
        skipped = [(m, fid) for m, fid, _ in short if (m, fid) in prior_topup]
        for m, fid in skipped:
            print(f"  {m} {fid}: still short AFTER its one top-up — sample count drops; "
                  f"record the reduced cluster count in PREREG.md before the freeze.")
        if not todo:
            print("no figures need (or are still eligible for) a top-up.")
            return
        check_hard_stop(len(todo) * EST_PER_CALL, "topup")
        recs = []
        for m, fid, n in todo:
            print(f"  top-up {m} {fid} (certified so far: {n}/6)")
            recs.append(harvest_call(m, MODELS[m], figs, fid, 0.8, "topup"))
        tot, have, miss = flat_cost(recs)
        ledger_append("harvest-topup", len(recs), tot, miss,
                      "one top-up per shortfall figure at temperature 0.8 (pre-registered)")
        print("re-run certify.py to certify the new candidates.")
    else:
        print("usage: harvest.py [plan|harvest|topup]")


if __name__ == "__main__":
    main()
