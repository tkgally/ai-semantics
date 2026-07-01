#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the PRESUPPOSITION / ACCOMMODATION probe.

Run 2026-07-01-presupposition-accommodation. Tests the open question
open-question/presupposition-accommodation-corner (opened session 161): when a sentence carries a
presupposition whose backgrounded content is NOT already established in the context, does a current
model ACCOMMODATE it — treat the unmet content as given — and is that gated by whether the context
merely leaves it open (neutral) versus explicitly CONTRADICTS it? The diagnostic follows the SEP
survey's §5 accommodation material (Karttunen 1974:191, quoted in the source page): a hearer who
meets an unsatisfied presupposition may quietly extend the context to accommodate it.

STRICT SCOPE (load-bearing; see PREREG §scope-cap). The primary measure is a WITHIN-MODEL contrast
across three CONTEXT conditions on the SAME trigger sentence — supported / neutral / contradicting.
It makes NO human comparison (no human accommodation baseline is claimed, measured, or needed). Its
terminal anchor status (`internal-contrast-only`) is NOT self-ratified this session: a
wiki/decisions/open/ entry is opened when the result is written, and the result carries
`anchor: pending` contingent on that decision until an independent later session ratifies. This prep
freezes the stimuli only; the scope discipline lives in PREREG.md + the result.

DESIGN — 12 base scenarios across 4 trigger families (3 each), same inventory shape as the sibling
projection run (2026-07-01-presupposition-projection) but on a DIFFERENT manipulation axis (context
support, not embedding):
  factive   — factive verb (realize / discover / know). P = the complement fact.
  aspectual — change-of-state / aspectual verb (stop / continue / resume). P = the prior state.
  definite  — definite description / possessive / relative-clause definite. P = existence of referent.
  cleft     — it-cleft. P = the existential ("someone Y-ed").

Each scenario has ONE trigger sentence (carrying P, held CONSTANT across conditions) and three
one-sentence CONTEXTS that precede it:
  supported     — a context sentence that EXPLICITLY STATES P (a manipulation check / sanity floor:
                  P is now literally asserted in the discourse, so a reader who cannot endorse it
                  cannot read the text — control failure, not accommodation).
  neutral       — a topic-adjacent context sentence that bears on P NEITHER way (the accommodation
                  test: with nothing establishing P and nothing against it, does the model supply P?).
  contradicting — a context sentence that EXPLICITLY DENIES P (the gate: does the model DECLINE to
                  accommodate an impossible presupposition, rather than endorsing regardless?).

  12 scenarios x 3 context conditions = 36 item-conditions.

The context-gated-accommodation SIGNATURE (per model): endorse P in supported (retrieval) AND in
neutral (accommodation), but DECLINE P in contradicting (the gate). Endorsing in ALL THREE
(including contradicting) is a blanket yes-bias, not accommodation; endorsing in NONE (not even
neutral) is no accommodation. Grading + verdict is in analyze.py (NO API calls).

The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA, so the set cannot drift
after the pre-run critic signs off. These are the PROJECT'S OWN synthetic items (no external corpus /
license), so the full text is committed here.

Usage:
    python3 prep.py            # print manifest sha + per-family/condition counts
    python3 prep.py --check    # assert structural invariants + frozen sha; non-zero on drift
    python3 prep.py --dump     # write items.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest (scenarios + conditions + system/query templates). Pinned
# once the design is frozen (before the pre-run critic signs off). The probe's FREEZE GUARD refuses
# to run unless manifest_sha() == FROZEN_SHA.
FROZEN_SHA = "4930d4994ea2650cffa13a539f0fd2707490975c7f895fc810710c9baa9ce15c"

# ---------------------------------------------------------------------------------------------
# Neutral system prompt. It must NOT hint at presupposition, accommodation, or the "right" answer.
# ---------------------------------------------------------------------------------------------
SYS = "You are a careful reader. Answer the user's question directly."

# The forced-choice query wrapper. {text} is the two-sentence discourse (context + trigger);
# {target} is the presupposition P. The three-way YES / NO / UNCLEAR lets a model that will not
# accommodate answer UNCLEAR (or NO under contradiction) rather than be forced into a YES.
QUERY = (
    'Consider only the following text:\n\n'
    '"{text}"\n\n'
    'Taking that text at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The three context conditions, in fixed order.
CONDITIONS = ["supported", "neutral", "contradicting"]

# ---------------------------------------------------------------------------------------------
# 12 base scenarios. Each carries ONE trigger sentence (holds P constant) and three context
# sentences. The full discourse for a condition is: context + " " + trigger. `presup` is the target
# P, written as a fragment completing "does it follow that: {target}" (so it reads grammatically
# after the colon). supported STATES P; contradicting DENIES P; neutral is topic-adjacent and bears
# on P neither way (no lexical overlap with P's content).
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---------------- FACTIVE (P = the complement fact) ----------------
    {"sid": "fac1", "family": "factive",
     "trigger": "Sam realized that the safe had been left open.",
     "presup": "the safe had been left open?",
     "supported": "The safe had been left open all night.",
     "neutral": "The office was on the fourth floor.",
     "contradicting": "The safe had been securely locked the whole time."},
    {"sid": "fac2", "family": "factive",
     "trigger": "The auditor discovered that the figures had been changed.",
     "presup": "the figures had been changed?",
     "supported": "Someone had altered the figures before the review.",
     "neutral": "The audit took place in early spring.",
     "contradicting": "The figures were exactly as originally recorded."},
    {"sid": "fac3", "family": "factive",
     "trigger": "Maria knew that the flight had been cancelled.",
     "presup": "the flight had been cancelled?",
     "supported": "The airline cancelled the flight that morning.",
     "neutral": "Maria worked as a translator.",
     "contradicting": "The flight departed on schedule as planned."},
    # ------------- ASPECTUAL / CHANGE-OF-STATE (P = the prior state) -------------
    {"sid": "asp1", "family": "aspectual",
     "trigger": "The company stopped funding the lab.",
     "presup": "the company used to fund the lab?",
     "supported": "For years the company had funded the lab.",
     "neutral": "The lab was located downtown.",
     "contradicting": "The company had never funded the lab."},
    {"sid": "asp2", "family": "aspectual",
     "trigger": "The senator continued to deny the charges.",
     "presup": "the senator had already been denying the charges?",
     "supported": "The senator had been denying the charges for weeks.",
     "neutral": "The senator represented a coastal state.",
     "contradicting": "The senator had said nothing about the charges before."},
    {"sid": "asp3", "family": "aspectual",
     "trigger": "The factory resumed production.",
     "presup": "the factory had produced before?",
     "supported": "The factory had been producing until the shutdown.",
     "neutral": "The factory stood beside a river.",
     "contradicting": "The factory had never produced anything before."},
    # ---------- DEFINITE / POSSESSIVE (P = existence of the referent) ----------
    {"sid": "def1", "family": "definite",
     "trigger": "The committee rejected Priya's proposal.",
     "presup": "Priya had made a proposal?",
     "supported": "Priya submitted a written proposal last week.",
     "neutral": "The committee met on a Thursday.",
     "contradicting": "Priya submitted no proposal in this cycle."},
    {"sid": "def2", "family": "definite",
     "trigger": "The new director cancelled the merger.",
     "presup": "there was a new director?",
     "supported": "The firm had recently appointed a new director.",
     "neutral": "The firm's offices were being renovated.",
     "contradicting": "The firm had no director at the time."},
    {"sid": "def3", "family": "definite",
     "trigger": "The witness who saw the crash testified.",
     "presup": "someone saw the crash?",
     "supported": "A bystander had seen the crash happen.",
     "neutral": "The trial was held in July.",
     "contradicting": "No one had seen the crash."},
    # --------------- CLEFT (P = the existential) ---------------
    {"sid": "cle1", "family": "cleft",
     "trigger": "It was the intern who leaked the memo.",
     "presup": "someone leaked the memo?",
     "supported": "The memo had been leaked to the press.",
     "neutral": "The memo was two pages long.",
     "contradicting": "The memo was never leaked to anyone."},
    {"sid": "cle2", "family": "cleft",
     "trigger": "It was the smaller firm that won the contract.",
     "presup": "someone won the contract?",
     "supported": "The contract had been awarded to one of the bidders.",
     "neutral": "The contract ran for three years.",
     "contradicting": "The contract was never awarded to anyone."},
    {"sid": "cle3", "family": "cleft",
     "trigger": "It was the neighbor who called the police.",
     "presup": "someone called the police?",
     "supported": "The police had received a call that night.",
     "neutral": "The street was quiet and tree-lined.",
     "contradicting": "No one called the police."},
]


def build_items():
    """Flatten scenarios into 36 item-conditions (12 scenarios x 3 context conditions)."""
    items = []
    for s in SCEN:
        for cond in CONDITIONS:
            text = s[cond] + " " + s["trigger"]
            items.append({
                "id": f"{s['sid']}-{cond}",
                "sid": s["sid"],
                "family": s["family"],
                "condition": cond,
                "text": text,
                "target": s["presup"],
                "prompt": QUERY.format(text=text, target=s["presup"]),
            })
    return items


ITEMS = build_items()


def manifest_sha():
    """Stable sha over everything that defines the frozen stimulus/behavioral spec."""
    canon = json.dumps({
        "sys": SYS,
        "query": QUERY,
        "conditions": CONDITIONS,
        "scenarios": SCEN,
    }, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(canon.encode()).hexdigest()


def check():
    errs = []
    if len(SCEN) != 12:
        errs.append(f"expected 12 scenarios, got {len(SCEN)}")
    if len(ITEMS) != 36:
        errs.append(f"expected 36 item-conditions, got {len(ITEMS)}")
    by_fam = {}
    for s in SCEN:
        by_fam[s["family"]] = by_fam.get(s["family"], 0) + 1
    if by_fam != {"factive": 3, "aspectual": 3, "definite": 3, "cleft": 3}:
        errs.append(f"family balance off: {by_fam}")
    sids = [s["sid"] for s in SCEN]
    if len(set(sids)) != len(sids):
        errs.append("duplicate sid")
    for s in SCEN:
        for key in CONDITIONS + ["trigger", "presup"]:
            if not s.get(key):
                errs.append(f"{s['sid']}: missing {key}")
        # target must read as a fragment ending in '?' (it completes "does it follow that: ...")
        if not s["presup"].rstrip().endswith("?"):
            errs.append(f"{s['sid']}: presup target should end with '?'")
        # the three context sentences must be distinct
        if len({s["supported"], s["neutral"], s["contradicting"]}) != 3:
            errs.append(f"{s['sid']}: context sentences not all distinct")
    # per-condition item balance
    by_cond = {}
    for it in ITEMS:
        by_cond[it["condition"]] = by_cond.get(it["condition"], 0) + 1
    if set(by_cond.values()) != {12}:
        errs.append(f"per-condition item balance off: {by_cond}")
    if errs:
        print("FAIL:\n  " + "\n  ".join(errs))
        return 1
    sha = manifest_sha()
    if FROZEN_SHA not in (None, "PINME") and sha != FROZEN_SHA:
        print(f"FAIL: manifest sha drift\n  frozen={FROZEN_SHA}\n  actual={sha}")
        return 1
    print(f"OK: 12 scenarios, 36 item-conditions, families {by_fam}, sha={sha}")
    if FROZEN_SHA in (None, "PINME"):
        print(f"  (NOT YET PINNED — set FROZEN_SHA = \"{sha}\")")
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
    print(f"scenarios={len(SCEN)} items={len(ITEMS)} sha={manifest_sha()}")
    print("per-family:", {k: sum(1 for s in SCEN if s['family'] == k)
                         for k in ('factive', 'aspectual', 'definite', 'cleft')})
    print("per-condition:", {c: sum(1 for it in ITEMS if it['condition'] == c) for c in CONDITIONS})


if __name__ == "__main__":
    main()
