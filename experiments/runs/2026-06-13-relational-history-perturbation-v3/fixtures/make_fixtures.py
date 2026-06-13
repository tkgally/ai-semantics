#!/usr/bin/env python3
"""make_fixtures.py — deterministic SYNTHETIC fixtures for local sanity checks.

No API calls; no finding-bearing data. Generates:
  fixtures/certification_report.fixture.json  (synthetic certified rosters, 6/figure)
  fixtures/stimuli.fixture.json               (via build_trials.build — geometry check)
  fixtures/raw/probe-{claude,gpt,gemini}.jsonl (synthetic probe records)

The synthetic behaviour patterns exercise three branches of the pre-registered verdict
mapper in analyze.py (expected when run with `analyze.py --raw-dir fixtures/raw`):
  claude : all 9 clusters gated; picks chron-last in 5-6/6 orders BOTH directions
           -> FALSIFIED (RECENCY)
  gpt    : all 9 clusters gated; per-cluster chron-last counts cycle 3/2/4 of 6 (mean
           0.5, non-degenerate CI) with 54 in-pair trials/direction
           -> COMMUTATIVE-NULL-CERTIFIED
  gemini : only 2 clusters pass the manipulation gate -> METHODOLOGICAL NULL

These are FIXTURES: synthetic, labelled as such, never to be confused with run data
(which lives in raw/, written only by probe.py).
"""
import json
import os
import sys

FIX = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(FIX)
sys.path.insert(0, RUN)
import build_trials  # noqa: E402
from common import MODELS, load_figures, figure_pairs, DESCS_PER_FIG, N_SAMPLES  # noqa: E402

REPORT_PATH = os.path.join(FIX, "certification_report.fixture.json")
STIM_PATH = os.path.join(FIX, "stimuli.fixture.json")
RAW_DIR = os.path.join(FIX, "raw")


def make_report(figs, pairs):
    models = {}
    for m in MODELS:
        fig_out = {}
        for fid in sorted(figs):
            roster = [f"synthetic {m} {fid} description {i}" for i in range(DESCS_PER_FIG)]
            fig_out[fid] = {"candidates_kept": DESCS_PER_FIG,
                            "certified_n": DESCS_PER_FIG, "roster": roster,
                            "shortfall": False, "topup_used": False}
        pair_out = {str(pid): {"X": a, "Y": b, "n_samples": N_SAMPLES}
                    for pid, (a, b) in sorted(pairs.items())}
        models[m] = {"figures": fig_out, "pairs": pair_out,
                     "n_clusters": N_SAMPLES * len(pairs)}
    return {"schema": "SYNTHETIC FIXTURE — not run data",
            "anti_null_bias_disclosure": "fixture", "models": models, "census": []}


def synth_records(stim):
    """Deterministic picks per the patterns documented in the module docstring."""
    # gemini gated clusters: pair 0, samples 0 and 1 only
    gemini_gated = {(0, 0), (0, 1)}
    cluster_index = {}  # (m, pair, sample) -> running index for pattern cycling

    def ci_of(m, t):
        k = (m, t["pair"], t["sample"])
        if k not in cluster_index:
            cluster_index[k] = len([x for x in cluster_index if x[0] == m])
        return cluster_index[k]

    out = {m: [] for m in MODELS}
    order_pos = {o: i for i, o in enumerate(stim["orders"])}
    # gpt null pattern: per-cluster chron-pick ORDER SETS chosen so that BOTH rho_chron
    # and rho_phys sit at mean 0.5 in BOTH directions with non-degenerate cluster
    # variation. (Note: for YXXY/XYYX the chron-first and chron-last lines are the SAME
    # twin, so "picked the non-last twin" is not always "picked the phys-first twin" in
    # rev — the sets below account for that: chron counts cycle 3/2/4, rev phys 3/4/2.)
    GPT_CHRON = ({"XXYY", "XYXY", "YXXY"},
                 {"XXYY", "YXXY"},
                 {"XXYY", "XYXY", "YXXY", "YYXX"})
    for m in MODELS:
        for t in stim["trials"][m]:
            rec = dict(t)
            rec["model"] = m
            rec["parse_mode"] = "strict"
            rec["retried"] = False
            rec["raw"] = "SYNTHETIC"
            rec["usage"] = []
            rec["err"] = None
            if t["kind"] == "consistent":
                if m == "gemini" and (t["pair"], t["sample"]) not in gemini_gated:
                    # fail the gate: the X-twin control picks the wrong twin
                    ok = (t["target"] != t["X"])
                else:
                    ok = True
                rec["pick_cid"] = t["target"] if ok else \
                    (t["Y"] if t["target"] == t["X"] else t["X"])
                rec["pick"] = "P?"
                rec["correct"] = ok
            else:
                ci = ci_of(m, t)
                pos = order_pos[t["order"]]
                if m == "claude":      # recency: 6/6 on even clusters, 5/6 on odd
                    chron = not (ci % 2 == 1 and pos == 0)
                elif m == "gpt":       # chron counts cycle 3/2/4 of 6 -> mean exactly 0.5
                    chron = t["order"] in GPT_CHRON[ci % 3]
                else:                  # gemini: pattern irrelevant (guard fails)
                    chron = pos % 2 == 0
                other = t["X"] if t["last"] == t["Y"] else t["Y"]
                rec["pick_cid"] = t["last"] if chron else other
                rec["pick"] = "P?"
                rec["in_pair"] = True
                rec["picked_chron_last"] = chron
                phys_last = t["last"] if t["direction"] == "fwd" else t["first"]
                rec["picked_phys_last"] = rec["pick_cid"] == phys_last
            out[m].append(rec)
    return out


def main():
    figs = load_figures()
    pairs = figure_pairs(figs)
    report = make_report(figs, pairs)
    json.dump(report, open(REPORT_PATH, "w"), indent=2)
    stim = build_trials.build(report, figs)
    json.dump(stim, open(STIM_PATH, "w"), indent=2)
    for m in MODELS:
        n = len(stim["trials"][m])
        mixed = sum(1 for t in stim["trials"][m] if t["kind"] == "mixed")
        assert (n, mixed) == (126, 108), f"geometry: {m} {n}/{mixed}"
    os.makedirs(RAW_DIR, exist_ok=True)
    recs = synth_records(stim)
    for m in MODELS:
        with open(os.path.join(RAW_DIR, f"probe-{m}.jsonl"), "w") as f:
            for r in recs[m]:
                f.write(json.dumps(r) + "\n")
    print("fixtures written. Expected verdicts under `python3 analyze.py --raw-dir "
          "fixtures/raw`:\n  claude: FALSIFIED (RECENCY)\n  gpt: "
          "COMMUTATIVE-NULL-CERTIFIED\n  gemini: METHODOLOGICAL NULL")


if __name__ == "__main__":
    main()
