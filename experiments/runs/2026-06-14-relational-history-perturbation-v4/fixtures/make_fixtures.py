#!/usr/bin/env python3
"""make_fixtures.py — synthetic, deterministic, API-FREE sanity fixtures for v4.

Builds: a synthetic certification_report.fixture.json (8 certified descriptions/figure,
claude + gemini, 4 samples/pair -> 12 clusters/model); stimuli.fixture.json via the REAL
build_trials.build() (so the geometry asserts run); and synthetic raw/ probe records for
three idealized readers, to exercise the verdict tree end-to-end:

  fixtures/raw/        : claude = perfect CHRONOLOGY reader (picks the clast twin),
                         gemini = perfect TEXT-POSITION reader (picks the last-line twin).
                         Expected: claude FALSIFIED (RECENCY); gemini TEXT-POSITION ARTIFACT.
  fixtures/raw_null/   : both models = CONTENT-ONLY readers (deterministic coin between the
                         two twins). Expected: COMMUTATIVE-NULL-CERTIFIED.
  fixtures/raw_blind/  : claude is stamp-blind (fails stamp-respect controls).
                         Expected: METHODOLOGICAL NULL (stamp-blind).

Fixtures are synthetic and clearly labelled; they are NOT findings and must never be mixed
with raw/ run data.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNDIR = os.path.dirname(HERE)
sys.path.insert(0, RUNDIR)
import build_trials  # noqa: E402
from common import MODELS, DESCS_PER_FIG, N_SAMPLES, load_figures, figure_pairs  # noqa: E402


def synth_report():
    figs = load_figures()
    pairs = figure_pairs(figs)
    models = {}
    for m in MODELS:
        fig_out = {}
        for fid in sorted(figs):
            roster = [f"{m}-{fid}-desc{i}" for i in range(DESCS_PER_FIG)]
            fig_out[fid] = {"candidates_kept": DESCS_PER_FIG, "certified_n": DESCS_PER_FIG,
                            "roster": roster, "shortfall": False, "topup_used": False}
        pair_out = {str(pid): {"X": a, "Y": b, "n_samples": N_SAMPLES}
                    for pid, (a, b) in sorted(pairs.items())}
        models[m] = {"figures": fig_out, "pairs": pair_out,
                     "n_clusters": len(pairs) * N_SAMPLES}
    return {"schema": "v4 certification report FIXTURE (synthetic)",
            "anti_null_bias_disclosure": "(fixture)", "models": models, "census": []}


def derive_mixed(t, pick_cid):
    in_pair = pick_cid in (t["X"], t["Y"])
    return {"in_pair": in_pair,
            "picked_chron_last": (pick_cid == t["clast_cid"]) if in_pair else None,
            "picked_phys_last": (pick_cid == t["last_cid"]) if in_pair else None}


def _u(t, salt):
    """Deterministic per-TRIAL uniform in [0,1) (varies across every cell, so the
    clustered bootstrap sees real within-cluster variation -> non-degenerate CIs)."""
    key = f"{salt}:{t['cluster']}:{t['clast']}:{t['dpos']}:{t['variant']}"
    return (int(hashlib.sha256(key.encode()).hexdigest(), 16) % 10_000) / 10_000.0


def coin(t):
    """Deterministic content-only pick between the two twins (ignores stamps and order)."""
    return t["X"] if _u(t, "coin") < 0.5 else t["Y"]


def noisy(t, target_cid, p=0.85):
    """Follow `target_cid` with prob p, else pick an INDEPENDENT coin between the two twins
    (so a miss does not systematically bias the OTHER channel — a clean single-channel
    reader gives the other channel ~0.5, deterministic per trial)."""
    if _u(t, f"noisy:{target_cid}") < p:
        return target_cid
    return t["X"] if _u(t, f"miss:{target_cid}") < 0.5 else t["Y"]


def write_raw(outdir, stim, policy):
    os.makedirs(outdir, exist_ok=True)
    for m in MODELS:
        path = os.path.join(outdir, f"probe-{m}.jsonl")
        with open(path, "w") as f:
            for t in stim["trials"][m]:
                rec = dict(t)
                if t["kind"] == "mixed":
                    pick_cid = policy(m, t)
                    rec.update(derive_mixed(t, pick_cid))
                    rec["pick_cid"] = pick_cid
                else:
                    # controls: correct unless the model is stamp-blind on stamp_respect
                    blind = policy(m, t) == "__BLIND__"
                    if t["kind"] == "stamp_respect" and blind:
                        # pick the twin's twin (a wrong in-pair-ish pick) -> control fails
                        pick_cid = t["Y"] if t["target"] == t["X"] else t["X"]
                    else:
                        pick_cid = t["target"]
                    rec["pick_cid"] = pick_cid
                    rec["correct"] = (pick_cid == t["target"])
                rec.update({"model": m, "pick": "P?", "parse_mode": "strict",
                            "retried": False, "finish_reason": "stop", "raw": "P?",
                            "usage": [{}], "err": None})
                f.write(json.dumps(rec) + "\n")


def main():
    report = synth_report()
    json.dump(report, open(os.path.join(HERE, "certification_report.fixture.json"), "w"),
              indent=2)
    figs = load_figures()
    stim = build_trials.build(report, figs)
    build_trials.assert_geometry(stim)
    out = os.path.join(HERE, "stimuli.fixture.json")
    json.dump(stim, open(out, "w"), indent=2)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()
    n = {m: len(stim["trials"][m]) for m in MODELS}
    print(f"stimuli.fixture.json: trials/model {n}; geometry asserts PASSED; sha256={h[:12]}…")

    # scenario A: claude = chronology reader; gemini = text-position reader (85% noisy,
    # so CIs are non-degenerate and the effect clauses are genuinely exercised)
    def policy_A(m, t):
        if t["kind"] != "mixed":
            return "__OK__"
        return noisy(t, t["clast_cid"]) if m == "claude" else noisy(t, t["last_cid"])
    write_raw(os.path.join(HERE, "raw"), stim, policy_A)

    # scenario B: both content-only
    def policy_B(m, t):
        if t["kind"] != "mixed":
            return "__OK__"
        return coin(t)
    write_raw(os.path.join(HERE, "raw_null"), stim, policy_B)

    # scenario C: claude stamp-blind (fails stamp-respect); gemini content-only
    def policy_C(m, t):
        if t["kind"] != "mixed":
            return "__BLIND__" if m == "claude" else "__OK__"
        return coin(t)
    write_raw(os.path.join(HERE, "raw_blind"), stim, policy_C)
    print("wrote fixtures/raw (chron|pos), fixtures/raw_null (content), "
          "fixtures/raw_blind (stamp-blind claude).")


if __name__ == "__main__":
    main()
