#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the AS-IF ORIGO probe (tool as deictic anchor).

Run 2026-06-30-tool-origo-deictic-anchor. Tests question (iii) — the ONLY behaviorally
testable residue — of conjecture/tool-origo-deictic-anchor (which refines
essay/origo-supplied-not-occupied): given a clock/location TOOL is available, does the panel
SPONTANEOUSLY treat tool-state as the deictic anchor for an UNANCHORED 'now'/'here'/'today' —
issuing the tool call without being told to, and binding the indexical's content to what the
tool returns?

STRICT SCOPE (load-bearing; see PREREG §scope-cap): a positive is an AS-IF behavioral contrast
at anchor: internal-contrast-only strength. It does NOT certify that the model "occupies" a
Kaplanian context (the tool-return is itself DESCRIBED text — the sibling essay's channel claim),
and it makes NO human comparison. This prep freezes the stimuli only; the scope discipline lives
in PREREG.md and the eventual result page.

THREE ARMS over 15 matched base scenarios (5 time / 5 date / 5 location) = 45 item-conditions:
  test     — UNANCHORED context (no narrated origo) + indexical question, tools AVAILABLE.
             As-if positive: spontaneous tool query + final answer bound to the tool's NONCE value.
  control  — ANCHORED context (a narrated origo, values DISTINCT from the nonce) + same question,
             tools AVAILABLE. Correct: resolve from the narrated origo and do NOT spuriously
             override it with the tool (final answer must NOT contain the nonce value).
  baseline — the SAME unanchored context as `test`, but NO tool exposed. Characterizes the
             deflationary fallback (refuse / hedge / parametric default) when no tool exists.

WHY NONCE TOOL RETURNS. get_current_time() returns time 17:42 on date 3021-11-08; the
year 3021 and the string 'Qethport'/'Vandrel' cannot be a training-prior coincidence, so
"the final answer contains the nonce value" is attributable to the tool and cannot appear in the
no-tool baseline at all (a structural guarantee that the test-arm resolution signal is
tool-attributable — see PREREG §baseline). This is these are the PROJECT'S OWN synthetic items
(no external corpus/license), so the full text is committed here.

Grading is in analyze.py; this file only freezes the items + a manifest sha (the probe's FREEZE
GUARD refuses to run unless the sha matches, so the set cannot drift after the pre-run critic
signs off).

Usage:
    python3 prep.py            # print manifest sha + per-arm/indexical counts
    python3 prep.py --check    # assert structural invariants + frozen sha; non-zero on drift
    python3 prep.py --dump     # write items.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest (scenarios + nonce returns + system prompt + tool schemas).
# None on first authoring; pinned once the pre-run critic signs off. The probe's FREEZE GUARD
# refuses to run unless manifest_sha() == FROZEN_SHA.
FROZEN_SHA = "74763523f7070a13f37d8970fd229f51eb3a452a3d2c82aeb6c58ea389ffcec3"

# ---------------------------------------------------------------------------------------------
# Neutral system prompt — MUST NOT mention tools or instruct their use (spontaneity guard).
# ---------------------------------------------------------------------------------------------
SYS = "You are a helpful assistant. Answer the user directly and concisely."

# ---------------------------------------------------------------------------------------------
# The two tools, exposed together on every tool-arm item so the tool is not the ONLY salient
# affordance and the model must pick the RELEVANT one (order/format guard). Parameter-free.
# ---------------------------------------------------------------------------------------------
TOOLS = [
    {"type": "function", "function": {
        "name": "get_current_time",
        "description": "Returns the current wall-clock time and calendar date.",
        "parameters": {"type": "object", "properties": {}, "required": []}}},
    {"type": "function", "function": {
        "name": "get_current_location",
        "description": "Returns the current geographic location.",
        "parameters": {"type": "object", "properties": {}, "required": []}}},
]

# Nonce returns — highly distinctive, un-memorizable. Deterministic (stubbed-and-logged), so
# "resolved to tool-state" == the final answer contains one of the nonce tokens below.
TOOL_RETURNS = {
    "get_current_time": {"time": "17:42", "date": "3021-11-08",
                         "weekday": "Tuesday", "timezone": "UTC+05:30"},
    "get_current_location": {"city": "Qethport", "region": "Vandrel Province",
                             "country": "Meridonia"},
}
# Tokens (case-insensitive) whose presence in the FINAL answer marks resolution-to-tool-state,
# keyed by the indexical the scenario asks about.
NONCE_ACCEPT = {
    "time": ["17:42", "5:42"],
    "date": ["3021", "november 8", "nov 8", "8 november", "11-08", "11/08", "11/8"],
    "location": ["qethport", "vandrel", "meridonia"],
}

# ---------------------------------------------------------------------------------------------
# 15 matched base scenarios. Each: sid, indexical, unanchored (test/baseline text), anchored
# (control text, narrates an origo DISTINCT from the nonce), narrated_accept (surface variants of
# the narrated value, for the descriptive resolve-from-narrated rate). The control gate itself is
# nonce-ABSENCE, which is robust regardless of narrated_accept coverage.
# Filler is kept origo-CLEAN in the unanchored text: no time/date/place is stated there.
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---- TIME (indexical 'now', clock time) ----
    {"sid": "t1", "indexical": "time",
     "unanchored": "I'm deciding whether to start a load of laundry or leave it for later. What time is it right now?",
     "anchored": "It's 10:15 in the morning and I'm deciding whether to start a load of laundry or leave it for later. What time is it right now?",
     "narrated_accept": ["10:15"]},
    {"sid": "t2", "indexical": "time",
     "unanchored": "My friend said to call her the moment it gets late enough to matter. What time is it now?",
     "anchored": "It is 23:40 (twenty minutes before midnight). My friend said to call her the moment it gets late enough to matter. What time is it now?",
     "narrated_accept": ["23:40", "11:40"]},
    {"sid": "t3", "indexical": "time",
     "unanchored": "I want to know if I still have time for a quick walk before my first commitment. Can you tell me the current time?",
     "anchored": "The clock on the wall reads 08:05. I want to know if I still have time for a quick walk before my first commitment. Can you tell me the current time?",
     "narrated_accept": ["08:05", "8:05"]},
    {"sid": "t4", "indexical": "time",
     "unanchored": "Someone asked me how long until the afternoon is over and I realized I've lost track. What's the time at the moment?",
     "anchored": "Right now it is 14:20 in the afternoon. Someone asked me how long until the afternoon is over and I realized I've lost track. What's the time at the moment?",
     "narrated_accept": ["14:20", "2:20"]},
    {"sid": "t5", "indexical": "time",
     "unanchored": "I'm trying to work out whether dinner should be starting around now. What time is it currently?",
     "anchored": "It is currently 19:00, exactly seven in the evening. I'm trying to work out whether dinner should be starting around now. What time is it currently?",
     "narrated_accept": ["19:00", "7:00", "7 "]},
    # ---- DATE (indexical 'today') ----
    {"sid": "d1", "indexical": "date",
     "unanchored": "I need to fill in the 'date' field at the top of a form and I've completely blanked. What is today's date?",
     "anchored": "Today is Tuesday, 30 June 2026. I need to fill in the 'date' field at the top of a form and I've completely blanked. What is today's date?",
     "narrated_accept": ["30 june", "june 30", "2026-06-30", "06-30", "6/30"]},
    {"sid": "d2", "indexical": "date",
     "unanchored": "A colleague asked me to date-stamp a note and I want to get it right. What's the date today?",
     "anchored": "It is 14 March 2025. A colleague asked me to date-stamp a note and I want to get it right. What's the date today?",
     "narrated_accept": ["14 march", "march 14", "2025-03-14", "03-14", "3/14"]},
    {"sid": "d3", "indexical": "date",
     "unanchored": "I'm about to sign a document and it needs the current date next to my signature. What is the date right now?",
     "anchored": "As of today, 1 December 2024, I'm about to sign a document and it needs the current date next to my signature. What is the date right now?",
     "narrated_accept": ["1 december", "december 1", "2024-12-01", "12-01", "12/1"]},
    {"sid": "d4", "indexical": "date",
     "unanchored": "My planner is open to a blank page and I can't remember what day of the month it is. Can you tell me today's date?",
     "anchored": "My planner is open to today's page, 19 January 2026, and I can't remember quite how I got here. Can you tell me today's date?",
     "narrated_accept": ["19 january", "january 19", "2026-01-19", "01-19", "1/19"]},
    {"sid": "d5", "indexical": "date",
     "unanchored": "I'm writing the opening line of a journal entry and it always starts with the date. What's today's date?",
     "anchored": "I'm writing the opening line of a journal entry for today, 22 September 2023, and it always starts with the date. What's today's date?",
     "narrated_accept": ["22 september", "september 22", "2023-09-22", "09-22", "9/22"]},
    # ---- LOCATION (indexical 'here') ----
    {"sid": "l1", "indexical": "location",
     "unanchored": "I just woke up from a nap on a long trip and I'm disoriented. What city are we in right now?",
     "anchored": "We arrived in Kyoto this morning and I just woke up from a nap. I'm disoriented. What city are we in right now?",
     "narrated_accept": ["kyoto"]},
    {"sid": "l2", "indexical": "location",
     "unanchored": "Someone's asking me to drop a pin for where we are, and honestly I've lost the thread. Where are we located at the moment?",
     "anchored": "We've been walking around Lisbon all afternoon, and now someone's asking me to drop a pin for where we are. Where are we located at the moment?",
     "narrated_accept": ["lisbon"]},
    {"sid": "l3", "indexical": "location",
     "unanchored": "I want to label a photo I just took with the place it was taken, but my mind's gone blank. What place are we in right now?",
     "anchored": "I want to label a photo I just took here in Nairobi with the place it was taken. What place are we in right now?",
     "narrated_accept": ["nairobi"]},
    {"sid": "l4", "indexical": "location",
     "unanchored": "A form is asking for my current city and I've frozen up. Where are we right now?",
     "anchored": "A form is asking for my current city, which is Montreal, and I've frozen up on the spelling. Where are we right now?",
     "narrated_accept": ["montreal"]},
    {"sid": "l5", "indexical": "location",
     "unanchored": "I'm texting a friend 'guess where I am' and I want to describe the surroundings, but first — where is this, exactly?",
     "anchored": "I'm texting a friend from Wellington: 'guess where I am.' I want to describe the surroundings, but first — where is this, exactly?",
     "narrated_accept": ["wellington"]},
]


def build_items():
    """Flatten the scenarios into 45 item-conditions (3 arms x 15 scenarios)."""
    items = []
    for s in SCEN:
        na = NONCE_ACCEPT[s["indexical"]]
        for arm, text, tools in (
            ("test", s["unanchored"], True),
            ("control", s["anchored"], True),
            ("baseline", s["unanchored"], False),
        ):
            items.append({
                "id": f"{s['sid']}-{arm}",
                "sid": s["sid"],
                "indexical": s["indexical"],
                "arm": arm,
                "tools": tools,
                "prompt": text,
                "nonce_accept": na,
                "narrated_accept": s["narrated_accept"],
            })
    return items


ITEMS = build_items()

# Imperative phrases that would leak "use the tool" and void spontaneity (guard checks absence).
_FORBIDDEN = ["use the tool", "call the tool", "get_current", "use a tool", "the function",
              "call get", "tool call", "use your tool"]


def manifest_sha():
    """Stable sha over everything that defines the frozen stimulus/behavioral spec."""
    canon = json.dumps({
        "sys": SYS,
        "tools": TOOLS,
        "tool_returns": TOOL_RETURNS,
        "nonce_accept": NONCE_ACCEPT,
        "scenarios": SCEN,
    }, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(canon.encode()).hexdigest()


def check():
    errs = []
    # structural counts
    if len(SCEN) != 15:
        errs.append(f"expected 15 scenarios, got {len(SCEN)}")
    if len(ITEMS) != 45:
        errs.append(f"expected 45 item-conditions, got {len(ITEMS)}")
    by_ind = {}
    for s in SCEN:
        by_ind[s["indexical"]] = by_ind.get(s["indexical"], 0) + 1
    if by_ind != {"time": 5, "date": 5, "location": 5}:
        errs.append(f"indexical balance off: {by_ind}")
    sids = [s["sid"] for s in SCEN]
    if len(set(sids)) != len(sids):
        errs.append("duplicate sid")
    # per-scenario invariants
    all_nonce_tokens = [t for toks in NONCE_ACCEPT.values() for t in toks]
    for s in SCEN:
        for key in ("unanchored", "anchored", "narrated_accept"):
            if not s.get(key):
                errs.append(f"{s['sid']}: missing {key}")
        low_u = s["unanchored"].lower()
        low_a = s["anchored"].lower()
        # spontaneity: no imperative-to-use-tool leak in either arm's text
        for bad in _FORBIDDEN:
            if bad in low_u or bad in low_a:
                errs.append(f"{s['sid']}: forbidden tool-imperative '{bad}'")
        # unanchored text must be origo-CLEAN: contain none of its own narrated values
        for nv in s["narrated_accept"]:
            if nv.lower() in low_u:
                errs.append(f"{s['sid']}: unanchored text leaks narrated value '{nv}'")
        # neither arm's TEXT may contain a nonce token (nonce lives only in the tool return)
        for nt in all_nonce_tokens:
            if nt.lower() in low_u or nt.lower() in low_a:
                errs.append(f"{s['sid']}: text contains nonce token '{nt}'")
        # anchored text must actually carry its narrated value (origo present)
        if not any(nv.lower() in low_a for nv in s["narrated_accept"]):
            errs.append(f"{s['sid']}: anchored text does not carry any narrated value")
    if errs:
        print("FAIL:\n  " + "\n  ".join(errs))
        return 1
    sha = manifest_sha()
    if FROZEN_SHA is not None and sha != FROZEN_SHA:
        print(f"FAIL: manifest sha drift\n  frozen={FROZEN_SHA}\n  actual={sha}")
        return 1
    print(f"OK: 15 scenarios, 45 item-conditions, balance {by_ind}, sha={sha}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dump", action="store_true")
    args = ap.parse_args()
    if args.check:
        sys.exit(check())
    if args.dump:
        (HERE / "items.json").write_text(json.dumps(ITEMS, indent=2, ensure_ascii=True) + "\n")
        print(f"wrote items.json ({len(ITEMS)} item-conditions)")
        return
    print(f"scenarios=15 items={len(ITEMS)} sha={manifest_sha()}")
    print("per-indexical:", {k: sum(1 for s in SCEN if s['indexical'] == k)
                             for k in ('time', 'date', 'location')})


if __name__ == "__main__":
    main()
