#!/usr/bin/env python3
"""Audit that the working-surface variant changes ONLY the output channel.

For each framing, this loads the parent (v1) instrument.json and this variant's
replacement map, and prints:
  - whether the variant's 'old' clause is a VERBATIM SUFFIX of the v1 system string
    (so the task-description prefix is byte-identical by construction), and
  - the longest common prefix between v1's system string and the variant's system
    string (the byte-identical task description), and
  - the differing tails (v1 answer-format clause vs the working-surface clause).

A pre-run critic runs this to confirm the diff is FORMAT-ONLY: identical task text,
differing only in the trailing answer-format instruction. It also re-checks the parent
sha256 pin and prints the variant instrument sha256. No API calls, no data needed.
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.abspath(os.path.join(HERE, "..", "lexical-bridging-context-v1", "instrument.json"))
SELF = os.path.join(HERE, "instrument.json")


def common_prefix(a, b):
    n = 0
    for ca, cb in zip(a, b):
        if ca != cb:
            break
        n += 1
    return a[:n]


def v1_system(cfg, framing):
    ins = cfg["instruments"]
    table = {
        "b_rel": ins["B"]["framings"]["b_rel"]["system"],
        "b_conf": ins["B"]["framings"]["b_conf"]["system"],
        "c_third": ins["C"]["framings"]["c_third"]["system"],
        "topic": ins["Q3_context_control"]["framings"]["topic"]["system"],
        "a_forced": ins["A"]["framings"]["a_forced"]["system"],
    }
    return table[framing]


def main():
    parent = json.load(open(PARENT, encoding="utf-8"))
    me = json.load(open(SELF, encoding="utf-8"))

    # parent sha pin re-check
    parent_sha = hashlib.sha256(open(PARENT, "rb").read()).hexdigest()
    pinned = me["_provenance"]["parent_instrument_sha256"]
    print(f"parent instrument sha256 = {parent_sha}")
    print(f"  pinned in provenance   = {pinned}")
    print(f"  MATCH = {parent_sha == pinned}\n")

    self_sha = hashlib.sha256(open(SELF, "rb").read()).hexdigest()
    print(f"this variant instrument sha256 = {self_sha}\n")

    repl = me["framing_answer_clause_replacements"]
    all_ok = True
    for framing in ["b_rel", "b_conf", "c_third", "topic", "a_forced"]:
        v1s = v1_system(parent, framing)
        old = repl[framing]["old"]
        new = repl[framing]["new"]
        is_suffix = v1s.endswith(old)
        ws = v1s[: len(v1s) - len(old)] + new if is_suffix else None
        cp = common_prefix(v1s, ws) if ws is not None else ""
        print(f"=== {framing} ===")
        print(f"  v1 'old' clause is a VERBATIM SUFFIX of v1 system: {is_suffix}")
        if not is_suffix:
            all_ok = False
            print("  !! 'old' is NOT a suffix of v1 — FORMAT-ONLY claim FAILS.")
            continue
        # The shared (byte-identical) task description is everything before 'old'.
        shared = v1s[: len(v1s) - len(old)]
        # Sanity: common prefix of v1 and ws must equal the shared task description.
        prefix_ok = cp == shared
        all_ok = all_ok and prefix_ok
        print(f"  byte-identical shared task description ({len(shared)} chars):")
        print(f"    ...{shared[-90:]!r}")
        print(f"  v1 answer clause (REMOVED):\n    {old!r}")
        print(f"  working-surface answer clause (ADDED):\n    {new!r}")
        print(f"  common-prefix == shared task description: {prefix_ok}\n")

    print("FORMAT-ONLY DIFF CONFIRMED" if all_ok else "FORMAT-ONLY DIFF *NOT* CONFIRMED")


if __name__ == "__main__":
    main()
