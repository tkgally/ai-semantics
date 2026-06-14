#!/usr/bin/env python3
"""AANN agreement-reflex generalization v5 — panel calls (held-out agreement
single-contrast headline + a DESCRIPTIVE count-noun ceiling-diagnostic arm +
Tier-0 was/were manipulation check). Implements the FROZEN design
experiments/designs/aann-agreement-reflex-generalization-v5.md and PREREG.md.

DO NOT RUN until PREREG is frozen: PREREG-draft.md must pass a FRESH independent
pre-run critic and be committed as PREREG.md first. This script ALSO refuses to
run if analyze.py is absent (the analysis code must exist at freeze time, before
any call — the v2b/v3/v4 house guard). Design + materials are frozen here,
runnable later. **This probe has NOT been run; no v5 numbers exist.**

WHAT v5 IS. NEXT.md backlog 2(a): does gpt-5.4-mini's singular-agreement reflex
(+0.74 v3 / +0.65 v4) GENERALIZE across the panel and to HELD-OUT items? It
REUSES the v4 agreement arm UNCHANGED as its HEADLINE instrument (no new
decision; stays inside the ratified instrument class —
decisions/resolved/aann-inferential-operationalization, the agreement sub-probe
the "load-bearing discriminator"). The single change vs v4: the items are FRESH
held-out adjective x measure-noun combinations (none reused from v3/v4), and the
agreement single contrast is now the headline, not a sub-probe of a paraphrase
design.

THREE ARMS (246 calls total = 82/model x 3; 30 held-out items, 10 diagnostic,
12 tier0):
  agreement   30x2 = 60/model   HEADLINE: was/were FC over {aann, bare-plural
                                control}; indicator = P(was|AANN) - P(was|control)
  diagnostic  10x1 = 10/model   DESCRIPTIVE-ONLY (NEVER verdict-bearing): a
                                genuine COUNT-noun bare plural; tests whether a
                                model CAN pick "were" for a real count plural
  tier0       12x1 = 12/model   manipulation check: clear singular/plural
                                subjects; >= threshold per model gate

Settings IDENTICAL to the ratified panel (config/models.md): temperature 0;
max_tokens 64 (A claude-sonnet-4.6, B gpt-5.4-mini) / 512 (C gemini-3.5-flash);
C runs reasoning effort minimal. A cap, not a purchase (gemini burns small caps
on hidden reasoning, 2026-05-28 calibration).

Counterbalancing is in the FROZEN stimuli (agreement.agr_letter_was,
diagnostic.agr_letter_was, tier0.agr_letter_was); the probe reads those letters
and the analysis maps the chosen LETTER back to its CONTENT (was vs were), so
position bias is blocked at the stimulus level.

Usage: python3 probe.py [--model A|B|C] [--arm agreement|diagnostic|tier0]
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
DIAGNOSTIC = STIMULI["diagnostic"]
TIER0 = STIMULI["tier0"]
ARMS = ["agreement", "diagnostic", "tier0"]

SYSTEM = "You are a careful native-speaker reader of English."

# ---- prompts (frozen wordings; single-token A/B picks, mirror v4's P_AGR) ----
# A/B forced choice over the two agreement forms (was/were). The frame carries a
# blank "___" the chosen form fills; identical shape to the v4 agreement arm.
P_AGR = (
    "Choose the form that makes the sentence grammatical. Respond with ONLY "
    "the letter A or B.\n\n{frame}\n\nA: {a}\nB: {b}")

ABORT_USD = 0.25  # PREREG single-run flag (pre-flight estimate ~ $0.03-0.06)


# B3 fix (carried from v3/v4): strip markdown-bold asterisks / quotes / backticks
# as well as punctuation, so a "**A**" markdown-bold reply parses. Applied to both
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


def ask(slot, user):
    kwargs = {"max_tokens": 512 if slot == "C" else 64}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], SYSTEM, user, temperature=0, **kwargs)


def tasks_for(arm):
    """Yield (meta, prompt) tuples. meta is the raw row template; the
    counterbalanced LETTER mapping is recorded so analyze.py recovers content.

    agreement  : 2 conditions per item (aann / bare-plural control), the headline
                 single contrast (UNCHANGED from the v4 agreement arm).
    diagnostic : 1 frame per item (a genuine COUNT-noun bare plural), DESCRIPTIVE
                 ONLY; the cond is recorded "count_control" so analyze.py never
                 folds it into a verdict.
    tier0      : 1 frame per item (clear singular/plural subject), manipulation
                 check.
    """
    tasks = []
    if arm == "agreement":
        for it in ITEMS:
            ag = it["agreement"]
            was_letter = ag["agr_letter_was"]
            a = "was" if was_letter == "A" else "were"
            b = "were" if was_letter == "A" else "was"
            for cond, frame in (("aann", ag["aann_frame"]),
                                ("control", ag["control_frame"])):
                meta = {"id": it["id"], "arm": arm, "cond": cond,
                        "was_letter": was_letter}
                tasks.append((meta, P_AGR.format(frame=frame, a=a, b=b)))
    elif arm == "diagnostic":
        # DESCRIPTIVE-ONLY count-noun control. cond is fixed "count_control" so
        # analyze.py treats it as a descriptive ceiling diagnostic, never a verdict.
        for d in DIAGNOSTIC:
            dg = d["diagnostic"]
            was_letter = dg["agr_letter_was"]
            a = "was" if was_letter == "A" else "were"
            b = "were" if was_letter == "A" else "was"
            meta = {"id": d["id"], "arm": arm, "cond": "count_control",
                    "was_letter": was_letter, "expected": dg["expected"]}
            tasks.append((meta, P_AGR.format(frame=dg["control_frame"], a=a, b=b)))
    else:  # tier0
        for p in TIER0:
            was_letter = p["agr_letter_was"]
            meta = {"id": p["id"], "arm": arm, "was_letter": was_letter,
                    "grammatical_form": p["grammatical_form"]}
            tasks.append((meta, P_AGR.format(frame=p["frame"], a=p["A"], b=p["B"])))
    return tasks


def run_arm(slot, arm, records):
    out = RAW / f"{slot}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    tasks = tasks_for(arm)
    rows = []
    for i, (meta, user) in enumerate(tasks):
        r = ask(slot, user)
        val = parse_ab(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, user)  # one verbatim retry (PREREG), then missing
            val = parse_ab(r["content"])
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
                 "been frozen. PREREG-draft.md must pass the FRESH independent "
                 "pre-run critic and be committed as PREREG.md before any model "
                 "call. (v5 stays inside the ratified agreement-instrument class "
                 "— no NEW decision — but the freeze + critic gate still binds.)")
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
