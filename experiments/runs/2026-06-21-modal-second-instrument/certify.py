#!/usr/bin/env python3
"""certify.py -- mechanical pre-run checks for the second-instrument forced-choice probe.

The frequency/length MATCHING is inherited from the modal-arm-widening run (certified there;
not re-checked). What this script certifies is specific to the NEW indicator: that no
shortcut reader of the forced-choice instrument can manufacture a spurious base->fn shift.

Checks (all must pass -> "ok": true):
  1. per-arm n >= 15 (per-arm power gate, same as modal-arm-widening).
  2. hedge-position balance: |#hedge-first - #hedge-second| <= 1 per arm, so a fixed-letter
     (position-bias) reader contributes ~0 to mean(shift) and cancels within-item.
  3. no modal lemma (will/would/shall/should/must/might) appears in any option string -> a
     modal-blind reader has no surface cue to prefer strong vs hedge.
  4. content identity base-vs-fn: premise_base and premise_fn differ ONLY in the modal word
     (same subject/verb/object), so the only thing a base->fn shift can track is the modal.
  5. content-control identity base-vs-ct: premise_ct keeps the SAME modal as premise_base
     (the content word is what changes) -> a reader that flips on the modal yields shift_ct 0.
"""
import hashlib
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = os.path.join(HERE, "stimuli.json")
MODAL_LEMMAS = ("will", "would", "shall", "should", "must", "might")


def tokens(s):
    return s.rstrip(".").split()


def main():
    d = json.load(open(STIM))
    items = d["items"]
    fails = []
    checks = {}

    # 1. per-arm n
    arm_n = Counter(it["ftype"] for it in items)
    checks["arm_n"] = dict(arm_n)
    for ft, n in arm_n.items():
        if n < 15:
            fails.append(f"arm {ft} n={n} < 15")

    # 2. hedge-position balance
    bal = {}
    for ft in arm_n:
        c = Counter(it["hedge_letter"] for it in items if it["ftype"] == ft)
        bal[ft] = {"hedge_A": c["A"], "hedge_B": c["B"]}
        if abs(c["A"] - c["B"]) > 1:
            fails.append(f"arm {ft} hedge-position imbalance A={c['A']} B={c['B']}")
    checks["hedge_balance"] = bal

    # 3. no modal lemma in options
    leak = 0
    for it in items:
        blob = (it["optA"] + " " + it["optB"]).lower()
        for lemma in MODAL_LEMMAS:
            if lemma in tokens(blob):
                fails.append(f"{it['id']}: modal lemma {lemma!r} in options")
                leak += 1
    checks["option_modal_leaks"] = leak

    # 4. base vs fn differ in exactly one token (the modal)
    n_one_token = 0
    for it in items:
        tb, tf = tokens(it["premise_base"]), tokens(it["premise_fn"])
        if len(tb) != len(tf):
            fails.append(f"{it['id']}: base/fn length differ")
            continue
        diffs = [(a, b) for a, b in zip(tb, tf) if a != b]
        if len(diffs) != 1:
            fails.append(f"{it['id']}: base/fn differ in {len(diffs)} tokens {diffs}")
            continue
        a, b = diffs[0]
        if a.lower() not in MODAL_LEMMAS or b.lower() not in MODAL_LEMMAS:
            fails.append(f"{it['id']}: base/fn single diff not modal: {diffs}")
            continue
        n_one_token += 1
    checks["base_fn_single_modal_diff"] = n_one_token

    # 5. base vs ct keep the SAME modal (content word changes, modal does not)
    n_ct_same_modal = 0
    for it in items:
        tb, tc = tokens(it["premise_base"]), tokens(it["premise_ct"])
        mb = [t for t in tb if t.lower() in MODAL_LEMMAS]
        mc = [t for t in tc if t.lower() in MODAL_LEMMAS]
        if mb and mc and mb == mc:
            n_ct_same_modal += 1
        else:
            fails.append(f"{it['id']}: base/ct modal differs base={mb} ct={mc}")
    checks["base_ct_same_modal"] = n_ct_same_modal

    ok = not fails
    out = {"ok": ok, "fails": fails, "checks": checks,
           "stimuli_sha256": d["sha256"],
           "stimuli_file_sha256": hashlib.sha256(open(STIM, "rb").read()).hexdigest()}
    json.dump(out, open(os.path.join(HERE, "certification.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))
    print("\nOK" if ok else f"\nFAIL ({len(fails)})")


if __name__ == "__main__":
    main()
