"""Byte-identical repeated-runs (K=5) measurement of the FROZEN forced-decomposition
lexical commitment instrument (sha dceafa9d...), to de-noise the session-82/82b
decline-axis disagreement on gpt's bridging %UNCLEAR.

THE DISAGREEMENT (NEXT.md backlog 3): two routine sessions ran independent
forced-decomposition gpt re-runs for the same slot. Session 82 (PR #128) read gpt's
bridging decline at 8.3% (2/24) -> MIXED/WEAK; the concurrent session 82b read 0.0%
(0/24) -> channel-CONTROLLED null. The two disagree by ~2 of 24 bridging items, at or
under the documented ~12% temp-0 label jitter (essay/point-estimate-is-a-draw). The
clean resolver named in NEXT.md is a byte-identical repeated-runs (K>=5) test.

THIS IS A NOISE-FLOOR MEASUREMENT, not a re-score-to-a-verdict (the
essay/undischargeable-negative threaded needle: re-running to MEASURE the floor is
licit; re-running to "firm a null" buys nothing). It reuses the frozen probe's
build_systems()/load_items()/run_single() VERBATIM (fail-closed on any sha drift), so
every call is byte-identical to session 82's run; the ONLY change is repeat count.

SCOPE: gpt-only (the disputed leg). Verdict-bearing COMMITMENT framings ONLY --
c_third (decline; the disputed axis) + b_conf (confidence; the other commitment
instrument the MIXED/WEAK-vs-null verdict combines). Position (b_rel) and the topic
control are NOT re-run: position is not in dispute (it replicates CI-strict between the
clear classes across ALL THREE channels in session 82), so re-running it would only add
cost. K=5 temp-0 draws per item per framing; reasoning held constant (gpt enabled:False),
exactly as the frozen instrument.

The committed raw is SANITIZED at write time: only item_id/lemma/class/source/framing/
pred(/pred2)/had_final_tag/human_median/error/usage/uptake (counts) -- NEVER the model's
`raw` content or `final_seg` (which can quote the licensed DWUG/WiC corpus). analyze.py
uses none of the dropped fields.

Run (spend-bearing, after pre-run-critic GO + budget pre-flight):
    OPENROUTER_API_KEY=... python3 repeated_probe.py --calib 4   # measured cost pre-flight
    OPENROUTER_API_KEY=... python3 repeated_probe.py             # K=5 full (resumable)
"""
import hashlib
import importlib.util
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-forced-decomposition-v1"))
FROZEN_PROBE = os.path.join(FROZEN, "probe.py")
FROZEN_INSTRUMENT = os.path.join(FROZEN, "instrument.json")
EXPECT_SHA = "dceafa9d976cb47c71505d0e6f6f8df205595ccfcd6942f4c96dbffc02e97d42"

K = int(os.environ.get("KRUNS", "5"))
FRAMINGS = ["c_third", "b_conf"]  # commitment instruments only (decline + confidence)
RAW = os.path.join(HERE, "raw")

# Import the frozen forced-decomposition probe VERBATIM (it is never modified here).
_spec = importlib.util.spec_from_file_location("fdprobe", FROZEN_PROBE)
fd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fd)

KEEP = ("item_id", "lemma", "bridging_class", "source", "framing", "pred", "pred2",
        "had_final_tag", "human_median", "error", "usage", "uptake")


def sanitize(rec):
    return {k: rec[k] for k in KEEP if k in rec}


def main():
    calib = None
    if "--calib" in sys.argv:
        calib = int(sys.argv[sys.argv.index("--calib") + 1])

    # Fail-closed: the frozen instrument must be byte-identical to session 82's.
    sha = hashlib.sha256(open(FROZEN_INSTRUMENT, "rb").read()).hexdigest()
    if sha != EXPECT_SHA:
        sys.exit(f"FROZEN INSTRUMENT SHA MISMATCH: {sha} != {EXPECT_SHA}")
    systems = fd.build_systems()   # byte-identical reconstruction; fail-closed chain checks
    items = fd.load_items()
    if calib:
        items = items[:calib]
        print(f"CALIBRATION: {len(items)} items/framing, 1 run")
    n = len(items)
    model = fd.GPT_PANEL["B"]
    print(f"frozen sha OK ({sha[:8]}...); {n} items; model={model}; framings={FRAMINGS}; "
          f"K={1 if calib else K}")
    os.makedirs(RAW, exist_ok=True)
    suffix = "_calib" if calib else ""
    kruns = 1 if calib else K

    for k in range(1, kruns + 1):
        for fr in FRAMINGS:
            path = os.path.join(RAW, f"run{k}_{fr}{suffix}.json")
            if fd.file_complete(path, n):
                print(f"skip run{k}_{fr} (complete)")
                continue
            print(f"run{k} {fr} ...", flush=True)
            t0 = time.time()
            recs = fd.run_single(fr, systems[fr], items, model, fd.SINGLE_PARSE[fr])
            recs = [sanitize(r) for r in recs]
            json.dump(recs, open(path, "w"), indent=1)
            print(f"  done run{k}_{fr} ({round(time.time() - t0, 1)}s)", flush=True)

    # Cost + integrity summary (billed usage.cost, summed across all runs).
    per = []
    for k in range(1, kruns + 1):
        for fr in FRAMINGS:
            path = os.path.join(RAW, f"run{k}_{fr}{suffix}.json")
            if os.path.exists(path):
                per.append(json.load(open(path, encoding="utf-8")))
    billed, _have, missing = fd.billed_cost(per)
    ncalls = sum(len(x) for x in per)
    summ = {"model": model, "k": kruns, "framings": FRAMINGS, "n_items": n,
            "n_calls": ncalls, "cost_usd_billed": round(billed, 5),
            "n_cost_missing": missing, "frozen_instrument_sha256": sha}
    json.dump(summ, open(os.path.join(RAW, f"run_summary{suffix}.json"), "w"), indent=1)
    print(json.dumps(summ, indent=1))
    if calib:
        per_call = billed / max(1, ncalls)
        full = K * len(FRAMINGS) * 88
        print(f"per-call ${per_call:.6f}; FULL K={K} x {len(FRAMINGS)} framings x 88 items "
              f"= {full} calls -> ${per_call * full:.4f}")


if __name__ == "__main__":
    main()
