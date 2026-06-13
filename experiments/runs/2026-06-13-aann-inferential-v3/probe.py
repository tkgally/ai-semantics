#!/usr/bin/env python3
"""AANN inferential v3 — panel calls (paraphrase-FC primary + NLI convergent +
agreement discriminator + Tier-0). Implements the FROZEN design
experiments/designs/aann-construction-v3-inferential.md and PREREG.md.

DO NOT RUN until PREREG is frozen: PREREG-draft.md must pass the independent
pre-run critic and be committed as PREREG.md first (the governing decision
forbids any v3 call until cross-session ratification AND a pre-run critic). This
script ALSO refuses to run if analyze.py is absent (the analysis code must exist
at freeze time, before any call — the v2b house guard). The decision's
ratification fixes the yardstick, not a result; design+materials are frozen
here, runnable later.

FOUR ARMS (624 calls total = 208/model x 3; 23 base items after the object
class was dropped in the 2026-06-13 repair):
  paraphrase    23x2 = 46/model     PRIMARY: U/D forced choice, AANN vs control
                                    (the indicator is the AANN-vs-control SHIFT)
  nli          23x4 = 92/model      CONVERGENT: 2 hypotheses x {AANN, control}
                                    affirm/withhold; shift on unification/whole
  agreement    23x2 = 46/model      DISCRIMINATOR (load-bearing): was/were FC,
                                    {AANN, control}; singular-agreement shift
  tier0        24 pairs = 24/model  manipulation check; >=20/24 per model gate

Settings IDENTICAL to the ratified panel (config/models.md): temperature 0;
max_tokens 64 (A claude-sonnet-4.6, B gpt-5.4-mini) / 512 (C gemini-3.5-flash);
C runs reasoning effort minimal. A cap, not a purchase (gemini burns small caps
on hidden reasoning, 2026-05-28 calibration).

Counterbalancing is in the FROZEN stimuli (fc_letter_unification, agr_letter_was,
tier0 aann_position); the probe reads those letters and the analysis maps the
chosen LETTER back to its CONTENT (unification vs distributive; was vs were;
aann vs ill-formed), so position bias is blocked at the stimulus level.

Usage: python3 probe.py [--model A|B|C] [--arm paraphrase|nli|agreement|tier0]
Raw JSON per (model, arm) under raw/. Idempotent: re-running skips existing
files. Cost: billed usage.cost summed; calls with MISSING cost are counted and
logged, never silently discarded. ABORT_USD single-run flag enforced.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = STIMULI["items"]
TIER0 = STIMULI["tier0"]
ARMS = ["paraphrase", "nli", "agreement", "tier0"]

SYSTEM = "You are a careful native-speaker reader of English."

# ---- prompts (frozen wordings; single-token picks, same shape as v2/v2b) ----
P_PARA = (
    "Read the sentence, then choose which paraphrase best captures what it "
    "conveys. Respond with ONLY the letter A or B.\n\n"
    "Sentence: {premise}\n\nA: {a}\nB: {b}")
P_NLI = (
    "Premise: {premise}\n\nHypothesis: {hyp}\n\n"
    "Given the premise, is the hypothesis true? Respond with ONLY the word "
    "YES or NO.")
P_AGR = (
    "Choose the form that makes the sentence grammatical. Respond with ONLY "
    "the letter A or B.\n\n{frame}\n\nA: {a}\nB: {b}")
P_TIER0 = (
    "Which sentence sounds more natural in English? Respond with ONLY the "
    "letter A or B.\n\nA: {a}\nB: {b}")

ABORT_USD = 0.50  # PREREG single-run flag (pre-flight estimate ~ $0.13-0.25)


# B3 fix (2026-06-13 repair): strip markdown-bold asterisks / quotes / backticks
# as well as punctuation, so gemini's "**A**" / "**YES**" markdown-bold replies
# parse (the v2b markdown-bold failure reproduced here otherwise). Applied to both
# the full-string fast path and the per-token last-token scan.
_STRIP = ".,!:;'\"*`"


def parse_ab(text):
    """Full-string A/B first, else the LAST standalone A/B token (the v2b
    last-token convention; a preamble must not freeze the first letter)."""
    if text is None:
        return None
    t = text.strip().upper().strip(_STRIP).strip()
    if t in ("A", "B"):
        return t
    found = None
    for tok in t.replace("\n", " ").replace(":", " ").split():
        tok = tok.strip(_STRIP)
        if tok in ("A", "B"):
            found = tok
    return found


def parse_yesno(text):
    """Full-string YES/NO first, else the LAST standalone YES/NO token."""
    if text is None:
        return None
    t = text.strip().upper().strip(_STRIP).strip()
    if t in ("YES", "NO"):
        return t
    found = None
    for tok in t.replace("\n", " ").replace(":", " ").split():
        tok = tok.strip(_STRIP)
        if tok in ("YES", "NO"):
            found = tok
    return found


def ask(slot, user):
    kwargs = {"max_tokens": 512 if slot == "C" else 64}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], SYSTEM, user, temperature=0, **kwargs)


def tasks_for(arm):
    """Yield (meta, prompt, parser) tuples. meta is the raw row template; the
    counterbalanced LETTER mapping is recorded so analyze.py recovers content."""
    tasks = []
    if arm == "paraphrase":
        for it in ITEMS:
            uni_letter = it["fc_letter_unification"]
            a = it["paraphrase_unification"] if uni_letter == "A" \
                else it["paraphrase_distributive"]
            b = it["paraphrase_distributive"] if uni_letter == "A" \
                else it["paraphrase_unification"]
            for cond, premise in (("aann", it["aann"]), ("control", it["control"])):
                meta = {"id": it["id"], "arm": arm, "cond": cond,
                        "unification_letter": uni_letter}
                tasks.append((meta, P_PARA.format(premise=premise, a=a, b=b),
                              "ab"))
    elif arm == "nli":
        for it in ITEMS:
            for hyp_key in ("unification_hyp", "whole_eval_hyp"):
                hyp = it["nli"][hyp_key]
                for cond, premise in (("aann", it["aann"]),
                                      ("control", it["control"])):
                    meta = {"id": it["id"], "arm": arm, "cond": cond,
                            "hyp_key": hyp_key}
                    tasks.append((meta, P_NLI.format(premise=premise, hyp=hyp),
                                  "yesno"))
    elif arm == "agreement":
        for it in ITEMS:
            ag = it["agreement"]
            was_letter = ag["agr_letter_was"]
            a = "was" if was_letter == "A" else "were"
            b = "were" if was_letter == "A" else "was"
            for cond, frame in (("aann", ag["aann_frame"]),
                                ("control", ag["control_frame"])):
                meta = {"id": it["id"], "arm": arm, "cond": cond,
                        "was_letter": was_letter}
                tasks.append((meta, P_AGR.format(frame=frame, a=a, b=b), "ab"))
    else:  # tier0
        for p in TIER0:
            meta = {"id": p["id"], "arm": arm, "aann_position": p["aann_position"]}
            tasks.append((meta, P_TIER0.format(a=p["A"], b=p["B"]), "ab"))
    return tasks


PARSERS = {"ab": parse_ab, "yesno": parse_yesno}


def run_arm(slot, arm, records):
    out = RAW / f"{slot}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    tasks = tasks_for(arm)
    rows = []
    for i, (meta, user, pkind) in enumerate(tasks):
        parser = PARSERS[pkind]
        r = ask(slot, user)
        val = parser(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, user)  # one verbatim retry (PREREG), then missing
            val = parser(r["content"])
        row = dict(meta)
        row.update({"raw": r["content"], "value": val,
                    "usage": r.get("usage"), "error": r.get("error")})
        rows.append(row)
        records.append(r)
        if (i + 1) % 32 == 0:
            c, _, nmiss = billed_cost([records])
            print(f"  {slot}/{arm}: {i+1}/{len(tasks)} cost so far ${c:.4f}"
                  + (f" ({nmiss} missing usage.cost)" if nmiss else ""),
                  flush=True)
            if c >= ABORT_USD:
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                print(f"ABORT: single-run flag ${ABORT_USD} reached; wrote "
                      f"{out}.partial", flush=True)
                sys.exit(1)
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    print(f"{slot}/{arm}: {len(rows)} rows, {miss} missing -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    ap.add_argument("--arm", choices=ARMS, default=None)
    args = ap.parse_args()
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — the pre-registration has not "
                 "been frozen. PREREG-draft.md must pass the independent "
                 "pre-run critic (and the governing decision's cross-session "
                 "ratification, which is done) and be committed as PREREG.md "
                 "before any model call.")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — the analysis code must exist "
                 "at freeze time, before any model call; running calls without "
                 "committed analysis code is forbidden.")
    slots = [args.model] if args.model else ["A", "B", "C"]
    arms = [args.arm] if args.arm else ARMS
    records = []
    for slot in slots:
        for arm in arms:
            run_arm(slot, arm, records)
    total, _, n_missing_cost = billed_cost([records])
    print(f"TOTAL billed this invocation: ${total:.4f}")
    if n_missing_cost:
        print(f"WARNING: {n_missing_cost} call(s) reported no usage.cost — the "
              f"billed total above UNDERCOUNTS; flag in the budget ledger.")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} arms={arms} billed=${total:.4f} "
                f"missing_cost_calls={n_missing_cost}\n")


if __name__ == "__main__":
    main()
