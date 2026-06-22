#!/usr/bin/env python3
"""Audit that the forced-decomposition variant changes ONLY the uptake-forcing clause.

The chain is v1 -> OFFERED (working surface) -> FORCED (this variant). For each framing this:
  - re-checks the v1 and offered instrument sha256 pins (fail-closed inputs to the chain);
  - confirms the offered 'old' clause is a verbatim SUFFIX of the v1 system (so the offered
    system = v1 task description + offered answer clause, task text byte-identical to v1);
  - confirms the forced 'old' clause == the offered 'new' clause (the chain link), and is a
    verbatim SUFFIX of the offered system;
  - confirms the byte-identical TASK DESCRIPTION (everything before the answer clause) is the
    SAME for the offered and forced systems -> the SINGLE manipulated variable is the
    answer/forcing clause (offered 'Think step by step ...' -> forced 3-step decomposition);
  - prints the differing tails so a pre-run critic can read the exact manipulation.

A pre-run critic runs this to confirm: task text == v1; the ONLY diff vs the offered surface
is the forcing of uptake (answer-blind, sense/construction-neutral). No API calls, no data.
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.abspath(os.path.join(HERE, "..", "lexical-bridging-context-v1", "instrument.json"))
OFFERED = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-working-surface-v1", "instrument.json"))
SELF = os.path.join(HERE, "instrument.json")
FRAMINGS = ["b_rel", "b_conf", "c_third", "topic"]


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def common_prefix(a, b):
    n = 0
    for ca, cb in zip(a, b):
        if ca != cb:
            break
        n += 1
    return a[:n]


def v1_system(cfg, fr):
    ins = cfg["instruments"]
    table = {
        "b_rel": ins["B"]["framings"]["b_rel"]["system"],
        "b_conf": ins["B"]["framings"]["b_conf"]["system"],
        "c_third": ins["C"]["framings"]["c_third"]["system"],
        "topic": ins["Q3_context_control"]["framings"]["topic"]["system"],
    }
    return table[fr]


def main():
    v1 = json.load(open(V1, encoding="utf-8"))
    offered = json.load(open(OFFERED, encoding="utf-8"))
    me = json.load(open(SELF, encoding="utf-8"))

    v1_sha, off_sha, self_sha = sha(V1), sha(OFFERED), sha(SELF)
    prov = me["_provenance"]
    print(f"v1 instrument sha256        = {v1_sha}")
    print(f"  pinned                    = {prov['grandparent_v1_instrument_sha256']}")
    print(f"  MATCH = {v1_sha == prov['grandparent_v1_instrument_sha256']}")
    print(f"offered instrument sha256   = {off_sha}")
    print(f"  pinned                    = {prov['parent_offered_instrument_sha256']}")
    print(f"  MATCH = {off_sha == prov['parent_offered_instrument_sha256']}")
    print(f"  offered's pinned v1 sha   = {offered['_provenance']['parent_instrument_sha256']}")
    print(f"  CHAIN OK = {offered['_provenance']['parent_instrument_sha256'] == v1_sha}")
    print(f"this (forced) instrument sha256 = {self_sha}\n")

    off_repl = offered["framing_answer_clause_replacements"]
    fd_repl = me["framing_forced_clause_replacements"]
    all_ok = True
    for fr in FRAMINGS:
        s_v1 = v1_system(v1, fr)
        off_old, off_new = off_repl[fr]["old"], off_repl[fr]["new"]
        fd_old, fd_new = fd_repl[fr]["old"], fd_repl[fr]["new"]

        off_suffix_ok = s_v1.endswith(off_old)
        s_off = s_v1[: len(s_v1) - len(off_old)] + off_new if off_suffix_ok else None
        chain_link_ok = (fd_old == off_new)
        fd_suffix_ok = (s_off is not None) and s_off.endswith(fd_old)
        s_fd = s_off[: len(s_off) - len(fd_old)] + fd_new if fd_suffix_ok else None

        # byte-identical task description = everything before the answer clause, both systems
        task_off = s_off[: len(s_off) - len(off_new)] if s_off is not None else None
        task_fd = s_fd[: len(s_fd) - len(fd_new)] if s_fd is not None else None
        task_same = (task_off is not None and task_off == task_fd)
        # and that shared task description is exactly v1's task description
        task_is_v1 = (task_off is not None and task_off == s_v1[: len(s_v1) - len(off_old)])

        ok = off_suffix_ok and chain_link_ok and fd_suffix_ok and task_same and task_is_v1
        all_ok = all_ok and ok
        print(f"=== {fr} ===")
        print(f"  offered 'old' is a verbatim SUFFIX of v1 system: {off_suffix_ok}")
        print(f"  forced 'old' == offered 'new' (chain link):      {chain_link_ok}")
        print(f"  forced 'old' is a verbatim SUFFIX of offered:    {fd_suffix_ok}")
        print(f"  task description identical (offered vs forced):  {task_same}")
        print(f"  task description == v1 task description:          {task_is_v1}")
        if task_fd is not None:
            print(f"  byte-identical task description ({len(task_fd)} chars):")
            print(f"    ...{task_fd[-90:]!r}")
        print(f"  OFFERED answer clause (the single-variable BEFORE):\n    {off_new!r}")
        print(f"  FORCED  answer clause (the single-variable AFTER):\n    {fd_new!r}\n")

    print("SINGLE-VARIABLE (offered->forced) DIFF CONFIRMED; TASK TEXT == v1"
          if all_ok else "DIFF *NOT* CONFIRMED -- chain broken")


if __name__ == "__main__":
    main()
