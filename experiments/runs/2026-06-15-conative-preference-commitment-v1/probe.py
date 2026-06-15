#!/usr/bin/env python3
"""probe.py — panel calls for the conative preference/commitment double contrast
(run 2026-06-15-conative-preference-commitment-v1). The ONLY file that calls the API.

Operationalizes experiments/designs/conative-preference-commitment-v1.md §3 with the
project's OWN frozen stimuli (stimuli.json, frozen by prep.py BEFORE this runs),
under the RATIFIED decision decisions/resolved/fresh-construction-inferential-
generalization (Option A — the conative). NO new decision; the yardstick is fixed.

TWO ARMS, both on every one of the 40 frozen items:
  Arm 1 — paraphrase forced-choice (the PREFERENCE signal, the WEAKER instrument):
      ask which paraphrase the sentence better supports; answer with exactly A or B.
      The two lettered options are in the item's SEED-COUNTERBALANCED order; the
      chosen letter is mapped (by analyze.py) via the item's assignment to reading
      C (cancel) / D (default). Preference measure = P(cancel-reading C chosen).
  Arm 2 — NLI entailment (the COMMITMENT signal, the load-bearing DISCRIMINATOR):
      premise = sentence; hypothesis = the contact proposition -> 0/1/2
      (entailment / neutral / contradiction). REUSES the frozen conative-cancel-v2
      NLI_SYS + parse_nli VERBATIM. Withhold = P(NLI != 0).

Settings: temperature 0; gemini (slot C) reasoning effort minimal via the shared
lib; max_tokens default (64 for A/B, 4096 for google/*) from openrouter.call.

FREEZE GUARD (design §9, inherited binding condition I8): refuses to run unless a
frozen PREREG.md exists in this dir AND analyze.py is present. ABORT_USD = 0.50:
abort if the running billed cost exceeds it. Billed usage.cost is summed and
written to raw/cost-log.txt; calls with missing cost are counted, never dropped.

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C] [--arm paraphrase|nli]
Raw JSON per (model, arm) under raw/. Idempotent: re-running skips existing files.

DO NOT RUN until PREREG.md is frozen (PREREG-draft.md must pass a fresh independent
pre-run critic GO and be committed as PREREG.md first).
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = STIMULI["items"]
ARMS = ["paraphrase", "nli"]

ABORT_USD = 0.50  # single-run flag (pre-flight estimate ~ $0.04-0.08); abort if
#                   running billed cost exceeds it. Far under the $5.00/day cap.

# ---- NLI instrument: REUSED VERBATIM from conative-cancel-probe-v2/probe.py ----
NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)

# ---- paraphrase forced-choice instrument (Arm 1) ----
PARA_SYS = "You are a careful native-speaker reader of English."
P_PARA = (
    "Read the sentence, then choose which paraphrase the sentence better "
    "supports. Respond with ONLY the letter A or B.\n\n"
    "Sentence: {sentence}\n\nA: {a}\nB: {b}")


def parse_nli(c):
    """VERBATIM from conative-cancel-probe-v2: last 0/1/2 digit."""
    if not c:
        return None
    digs = re.findall(r"[012]", c)
    return digs[-1] if digs else None


# A/B parsing in the v6 last-token style (markdown-bold / punctuation tolerant).
_STRIP = ".,!:;'\"*`"


def parse_ab(text):
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


def ask(slot, system, user):
    """One call. Gemini (slot C) runs reasoning effort minimal via the lib; the
    lib sets max_tokens (64 A/B, 4096 google) and the usage.cost include flag."""
    kwargs = {}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], system, user, temperature=0, **kwargs)


def tasks_for(arm):
    """Yield (meta, system, user, parser_kind). The counterbalanced A/B options
    are read from the frozen stimuli; analyze.py maps the chosen letter to the
    reading via the item's cancel_letter."""
    tasks = []
    if arm == "paraphrase":
        for it in ITEMS:
            user = P_PARA.format(sentence=it["sentence"],
                                 a=it["option_A"], b=it["option_B"])
            meta = {"item_id": it["item_id"], "family": it["family"],
                    "verb_class": it["verb_class"], "stem": it["stem"],
                    "arm": arm, "cancel_letter": it["cancel_letter"],
                    "default_letter": it["default_letter"]}
            tasks.append((meta, PARA_SYS, user, "ab"))
    else:  # nli
        for it in ITEMS:
            user = (f"Premise: {it['sentence']}\nHypothesis: "
                    f"{it['contact_proposition']}\nRelation:")
            meta = {"item_id": it["item_id"], "family": it["family"],
                    "verb_class": it["verb_class"], "stem": it["stem"],
                    "arm": arm}
            tasks.append((meta, NLI_SYS, user, "nli"))
    return tasks


PARSERS = {"ab": parse_ab, "nli": parse_nli}


def run_arm(slot, arm, records):
    out = RAW / f"{slot}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    tasks = tasks_for(arm)
    rows = []
    for i, (meta, system, user, pkind) in enumerate(tasks):
        parser = PARSERS[pkind]
        r = ask(slot, system, user)
        val = parser(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, system, user)  # one verbatim retry, then missing
            val = parser(r["content"])
        row = dict(meta)
        row.update({"raw": r["content"], "value": val,
                    "usage": r.get("usage"), "error": r.get("error")})
        rows.append(row)
        records.append(r)
        if (i + 1) % 20 == 0:
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
    # ---- FREEZE GUARD (design §9) ----
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — the pre-registration has not been "
                 "frozen. PREREG-draft.md must pass a FRESH independent pre-run "
                 "critic GO and be committed as PREREG.md before any model call.")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — the analysis code must exist at "
                 "freeze time, before any model call.")
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
