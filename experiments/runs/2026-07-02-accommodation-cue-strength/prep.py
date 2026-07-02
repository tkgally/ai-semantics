#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the ACCOMMODATION / CUE-STRENGTH probe.

Run 2026-07-02-accommodation-cue-strength. FOLLOW-UP to
[result/presupposition-accommodation-v1] (run 2026-07-01-presupposition-accommodation, verdict
GATED-ACCOMMODATION 3/3). v1 found a PARTIAL gate: under a single "contradicting" context the panel
still endorsed the explicitly-denied presupposition a third to a half of the time (contradicting-
endorse 0.33 / 0.58 / 0.42). This probe tests the cue-strength arm of
[conjecture/presupposition-environment-gated-both-directions]: its CONFIRMATION criterion is
"Accommodation's partial gate turning out to be graded by cue strength (a stronger surface
contradiction gates harder)". So we split the single v1 contradiction into TWO graded strengths —
a hedged/weak denial and an emphatic/strong denial of the SAME presupposition — and ask whether the
stronger surface contradiction gates HARDER (lower endorsement).

STRICT SCOPE (load-bearing; see PREREG §scope-cap). The primary measure is a WITHIN-MODEL contrast
across four CONTEXT conditions on the SAME trigger sentence — supported / neutral / weak_contra /
strong_contra. It makes NO human comparison (no human accommodation baseline is claimed, measured, or
needed). Its terminal anchor status is `internal-contrast-only`, INHERITING the ratified precedent
[decisions/resolved/presupposition-accommodation-internal-contrast-anchor] (opened session 162,
ratified session 163). NO new decision is opened. The scope discipline lives in PREREG.md + the
result the run session writes.

DESIGN — reuses the SAME 12 base scenarios and the SAME held-constant trigger sentences and
presupposition targets as v1's prep.py (4 trigger families x 3):
  factive   — factive verb (realize / discover / know). P = the complement fact.
  aspectual — change-of-state / aspectual verb (stop / continue / resume). P = the prior state.
  definite  — definite description / possessive / relative-clause definite. P = existence of referent.
  cleft     — it-cleft. P = the existential ("someone Y-ed").

FOUR context conditions (was three in v1) — the cue-strength grade:
  supported     — reuse v1's supported sentence VERBATIM (sanity / retrieval floor: P explicitly
                  stated, so a reader who cannot endorse it here cannot read the text).
  neutral       — reuse v1's neutral sentence VERBATIM, EXCEPT for cle2 (see below): bears on P
                  neither way (the accommodation test).
  weak_contra   — a MILD / hedged denial of P (evidential/epistemic downtoner over the negation:
                  "it was unclear whether", "reportedly not", "apparently not", "seemingly", "it was
                  doubtful that"). It denies P, but weakly.
  strong_contra — an EMPHATIC / categorical denial of the SAME P (intensifiers + absolute
                  quantifiers: "definitely not ... at all", "never ... at all", "no one at all",
                  "absolutely nothing", "whatsoever", "in any way"). This STRENGTHENS v1's single
                  contradiction, kept truthful and grammatical.

  The weak/strong pair targets the SAME propositional content (both deny the same P) and differs
  ONLY in surface strength — that is the manipulation. Register and length are kept close (the
  per-item context word counts and their weak-vs-strong delta are asserted in check(); the deltas
  are small and MIXED in sign across the 12 items, so length is not systematically confounded with
  strength — see PREREG §confounds).

  12 scenarios x 4 context conditions = 48 item-conditions.

THE cle2 FIX (loud — v1 SHOULD-FIX #1). v1's cle2 neutral was "The contract ran for three years",
which pragmatically implies the contract was in force (awarded to someone) and so LEAKED toward the
existential P ("someone won the contract"). Here cle2's neutral is replaced with a FULLY ORTHOGONAL
setting fact — "The conference room overlooked the harbor." — that bears on P neither way and has no
lexical/pragmatic overlap with winning a contract. This is the ONLY change to a reused v1 sentence;
every other supported/neutral sentence is verbatim v1.

The GRADED-GATE SIGNATURE (per model): endorse P in supported (retrieval) AND in neutral
(accommodation), with endorsement DECREASING as contradiction strength rises
(weak_contra_endorse > strong_contra_endorse). strength_gradient = weak - strong > 0 is the
conjecture's prediction. A FLAT gate (weak approx strong) is the honest NULL on the graded arm.
Grading + verdict is in analyze.py (NO API calls).

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
FROZEN_SHA = "55ad85693de0b1f343d28b810cf06e0b09316559abcbc490d2fd881ead55a36a"

# ---------------------------------------------------------------------------------------------
# Neutral system prompt. It must NOT hint at presupposition, accommodation, or the "right" answer.
# Reused VERBATIM from v1 (2026-07-01-presupposition-accommodation) so the only change vs v1 is the
# added cue-strength conditions + the cle2 neutral fix.
# ---------------------------------------------------------------------------------------------
SYS = "You are a careful reader. Answer the user's question directly."

# The forced-choice query wrapper (reused VERBATIM from v1). {text} is the two-sentence discourse
# (context + trigger); {target} is the presupposition P. The three-way YES / NO / UNCLEAR lets a
# model that will not accommodate answer UNCLEAR (or NO under contradiction) rather than be forced
# into a YES.
QUERY = (
    'Consider only the following text:\n\n'
    '"{text}"\n\n'
    'Taking that text at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The four context conditions, in fixed order.
CONDITIONS = ["supported", "neutral", "weak_contra", "strong_contra"]

# ---------------------------------------------------------------------------------------------
# 12 base scenarios. Each carries ONE trigger sentence (holds P constant, VERBATIM from v1) and four
# context sentences. The full discourse for a condition is: context + " " + trigger. `presup` is the
# target P (VERBATIM from v1), written as a fragment completing "does it follow that: {target}".
#   supported / neutral  — verbatim v1 (EXCEPT cle2 neutral, the leak fix, flagged inline).
#   weak_contra          — hedged denial of P (evidential/epistemic downtoner over the negation).
#   strong_contra        — emphatic categorical denial of the SAME P (intensifiers/absolutes).
# weak & strong deny the SAME proposition and differ ONLY in surface strength.
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---------------- FACTIVE (P = the complement fact) ----------------
    {"sid": "fac1", "family": "factive",
     "trigger": "Sam realized that the safe had been left open.",
     "presup": "the safe had been left open?",
     "supported": "The safe had been left open all night.",
     "neutral": "The office was on the fourth floor.",
     "weak_contra": "It was unclear whether the safe had been left open.",
     "strong_contra": "The safe had definitely not been left open at all."},
    {"sid": "fac2", "family": "factive",
     "trigger": "The auditor discovered that the figures had been changed.",
     "presup": "the figures had been changed?",
     "supported": "Someone had altered the figures before the review.",
     "neutral": "The audit took place in early spring.",
     "weak_contra": "It was doubtful that the figures had been changed.",
     "strong_contra": "The figures had certainly not been changed in any way."},
    {"sid": "fac3", "family": "factive",
     "trigger": "Maria knew that the flight had been cancelled.",
     "presup": "the flight had been cancelled?",
     "supported": "The airline cancelled the flight that morning.",
     "neutral": "Maria worked as a translator.",
     "weak_contra": "The flight had reportedly not been cancelled that day.",
     "strong_contra": "The flight had definitely not been cancelled at all."},
    # ------------- ASPECTUAL / CHANGE-OF-STATE (P = the prior state) -------------
    {"sid": "asp1", "family": "aspectual",
     "trigger": "The company stopped funding the lab.",
     "presup": "the company used to fund the lab?",
     "supported": "For years the company had funded the lab.",
     "neutral": "The lab was located downtown.",
     "weak_contra": "The company had apparently not funded the lab before.",
     "strong_contra": "The company had never once funded the lab before."},
    {"sid": "asp2", "family": "aspectual",
     "trigger": "The senator continued to deny the charges.",
     "presup": "the senator had already been denying the charges?",
     "supported": "The senator had been denying the charges for weeks.",
     "neutral": "The senator represented a coastal state.",
     "weak_contra": "The senator had seemingly said nothing about the charges before.",
     "strong_contra": "The senator had said absolutely nothing about the charges before."},
    {"sid": "asp3", "family": "aspectual",
     "trigger": "The factory resumed production.",
     "presup": "the factory had produced before?",
     "supported": "The factory had been producing until the shutdown.",
     "neutral": "The factory stood beside a river.",
     "weak_contra": "The factory had apparently not produced anything before.",
     "strong_contra": "The factory had never produced anything at all before."},
    # ---------- DEFINITE / POSSESSIVE (P = existence of the referent) ----------
    {"sid": "def1", "family": "definite",
     "trigger": "The committee rejected Priya's proposal.",
     "presup": "Priya had made a proposal?",
     "supported": "Priya submitted a written proposal last week.",
     "neutral": "The committee met on a Thursday.",
     "weak_contra": "Priya had seemingly not submitted a proposal this cycle.",
     "strong_contra": "Priya had submitted no proposal whatsoever this cycle."},
    {"sid": "def2", "family": "definite",
     "trigger": "The new director cancelled the merger.",
     "presup": "there was a new director?",
     "supported": "The firm had recently appointed a new director.",
     "neutral": "The firm's offices were being renovated.",
     "weak_contra": "The firm had apparently not appointed a new director.",
     "strong_contra": "The firm had appointed no new director at all."},
    {"sid": "def3", "family": "definite",
     "trigger": "The witness who saw the crash testified.",
     "presup": "someone saw the crash?",
     "supported": "A bystander had seen the crash happen.",
     "neutral": "The trial was held in July.",
     "weak_contra": "Apparently no one had seen the crash happen.",
     "strong_contra": "No one at all had seen the crash happen."},
    # --------------- CLEFT (P = the existential) ---------------
    {"sid": "cle1", "family": "cleft",
     "trigger": "It was the intern who leaked the memo.",
     "presup": "someone leaked the memo?",
     "supported": "The memo had been leaked to the press.",
     "neutral": "The memo was two pages long.",
     "weak_contra": "The memo had seemingly not been leaked to anyone.",
     "strong_contra": "The memo was never leaked to anyone at all."},
    {"sid": "cle2", "family": "cleft",
     "trigger": "It was the smaller firm that won the contract.",
     "presup": "someone won the contract?",
     "supported": "The contract had been awarded to one of the bidders.",
     # cle2 NEUTRAL FIX (v1 SHOULD-FIX #1): v1's "The contract ran for three years" leaked toward P
     # (a running contract implies it was awarded). Replaced with a fully orthogonal setting fact
     # that bears on "someone won the contract" neither way and has no award/win/bid overlap.
     "neutral": "The conference room overlooked the harbor.",
     "weak_contra": "The contract had apparently not been awarded to anyone.",
     "strong_contra": "The contract was never awarded to anyone at all."},
    {"sid": "cle3", "family": "cleft",
     "trigger": "It was the neighbor who called the police.",
     "presup": "someone called the police?",
     "supported": "The police had received a call that night.",
     "neutral": "The street was quiet and tree-lined.",
     "weak_contra": "Apparently no one had called the police that night.",
     "strong_contra": "No one at all had called the police that night."},
]


def build_items():
    """Flatten scenarios into 48 item-conditions (12 scenarios x 4 context conditions)."""
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
    if len(ITEMS) != 48:
        errs.append(f"expected 48 item-conditions, got {len(ITEMS)}")
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
        # the four context sentences must be distinct
        if len({s["supported"], s["neutral"], s["weak_contra"], s["strong_contra"]}) != 4:
            errs.append(f"{s['sid']}: context sentences not all distinct")
        # weak vs strong length kept close: |word-count delta| <= 2 (surface strength, not verbosity)
        wc_weak = len(s["weak_contra"].split())
        wc_strong = len(s["strong_contra"].split())
        if abs(wc_weak - wc_strong) > 2:
            errs.append(f"{s['sid']}: weak/strong length delta {abs(wc_weak - wc_strong)} > 2 "
                        f"(weak={wc_weak}, strong={wc_strong})")
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
    print(f"OK: 12 scenarios, 48 item-conditions, families {by_fam}, sha={sha}")
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
