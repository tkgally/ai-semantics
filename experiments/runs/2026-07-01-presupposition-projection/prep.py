#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the PRESUPPOSITION / PROJECTION probe.

Run 2026-07-01-presupposition-projection. Tests the open question
open-question/presupposition-projection-corner (opened session 157): does an LLM treat a
presupposition as PROJECTING — surviving negation / question / conditional-antecedent embedding —
MORE than a matched ordinary ENTAILMENT does? The diagnostic is the source's own "hallmark of
presuppositions" (SEP §1.2): under an entailment-cancelling operator the ordinary entailments drop
but the presupposition survives.

STRICT SCOPE (load-bearing; see PREREG §scope-cap). The primary measure is a WITHIN-MODEL contrast
between two legs of the SAME base sentence — a PRESUPPOSITION target vs. a MATCHED ENTAILMENT target
— across four embedding frames. It makes NO human comparison (no human projectivity baseline is
claimed, measured, or needed). Its terminal anchor status (`internal-contrast-only`) is NOT
self-ratified this session: a wiki/decisions/open/ entry is opened when the result is written, and
the result carries `anchor: pending` contingent on that decision until an independent later session
ratifies. This prep freezes the stimuli only; the scope discipline lives in PREREG.md + the result.

DESIGN — 12 matched base scenarios across 4 trigger families (3 each):
  factive   — factive verb (realize / discover / know). P = the complement fact; E = the subject's
              coming-to-know / awareness (the main assertion).
  aspectual — change-of-state / aspectual verb (stop / continue / resume). P = the prior state;
              E = the current state.
  definite  — definite description / possessive / relative-clause definite. P = existence of the
              definite's referent; E = the main predication.
  cleft     — it-cleft. P = the existential ("someone Y-ed"); E = the exhaustive identification
              ("X specifically Y-ed").

Each base is embedded under FOUR frames — plain / negation / question / conditional-antecedent —
and each framed sentence is queried against BOTH targets (P and E):
  12 scenarios x 2 targets x 4 frames = 96 item-conditions.

The projection SIGNATURE (per model): P endorsed across ALL four frames (survives the three
entailment-cancelling frames), while E is endorsed in the PLAIN frame but DROPS under the three
cancelling frames. Both legs endorsed in the plain frame is a built-in SANITY control: if a model
will not even endorse P or E when the base is plainly asserted, its cancelling-frame behavior is
uninterpretable (control failure), exactly as the origo probe's anchored-control arm guarded the
strong reading.

Grading + verdict is in analyze.py (NO API calls); this file only freezes the items + a manifest
sha. The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA, so the set cannot
drift after the pre-run critic signs off. These are the PROJECT'S OWN synthetic items (no external
corpus / license), so the full text is committed here.

Usage:
    python3 prep.py            # print manifest sha + per-family/frame counts
    python3 prep.py --check    # assert structural invariants + frozen sha; non-zero on drift
    python3 prep.py --dump     # write items.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest (scenarios + frames + system/query templates). None on first
# authoring; pinned once the design is frozen (before the pre-run critic signs off). The probe's
# FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA.
FROZEN_SHA = "e3a04cdd7e3ebbc955b916c15c7d11349ee4d5eb2dbf612c5de12cc1cf6877f9"

# ---------------------------------------------------------------------------------------------
# Neutral system prompt. It must NOT hint at presupposition, projection, or the "right" answer.
# ---------------------------------------------------------------------------------------------
SYS = "You are a careful reader. Answer the user's question directly."

# The forced-choice query wrapper. {sentence} is the framed base; {target} is the P or E inference.
# The three-way YES / NO / UNCLEAR keeps a cancelled entailment from being forced into a false YES:
# a model that thinks the inference is merely open can say UNCLEAR rather than YES.
QUERY = (
    'Consider only the following statement:\n\n'
    '"{sentence}"\n\n'
    'Taking that statement at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The four embedding frames, in fixed order. The three cancelling frames (the source's own list,
# SEP §1.2) are negation / question / conditional-antecedent. `plain` is the sanity baseline.
FRAMES = ["plain", "negation", "question", "conditional"]
CANCELLING = ("negation", "question", "conditional")

# ---------------------------------------------------------------------------------------------
# 12 matched base scenarios. Each carries the four framed sentences and the two target inferences.
# P (presup) is expected to PROJECT (survive all frames); E (entail) is expected to hold in `plain`
# and be CANCELLED under negation / question / conditional. Targets are written as sentence
# fragments completing "does it follow that: {target}" (so they read grammatically after the colon).
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---------------- FACTIVE (P = complement fact; E = subject's coming-to-know) ----------------
    {"sid": "fac1", "family": "factive",
     "presup": "the door was locked?",
     "entail": "Sam was aware that the door was locked?",
     "plain": "Sam realized that the door was locked.",
     "negation": "Sam didn't realize that the door was locked.",
     "question": "Did Sam realize that the door was locked?",
     "conditional": "If Sam realized that the door was locked, he went back for the key."},
    {"sid": "fac2", "family": "factive",
     "presup": "the ledger had been altered?",
     "entail": "the auditor found out that the ledger had been altered?",
     "plain": "The auditor discovered that the ledger had been altered.",
     "negation": "The auditor didn't discover that the ledger had been altered.",
     "question": "Did the auditor discover that the ledger had been altered?",
     "conditional": "If the auditor discovered that the ledger had been altered, the report was delayed."},
    {"sid": "fac3", "family": "factive",
     "presup": "the results were final?",
     "entail": "Maria was aware that the results were final?",
     "plain": "Maria knew that the results were final.",
     "negation": "Maria didn't know that the results were final.",
     "question": "Did Maria know that the results were final?",
     "conditional": "If Maria knew that the results were final, she submitted the appeal."},
    # ------------- ASPECTUAL / CHANGE-OF-STATE (P = prior state; E = current state) -------------
    {"sid": "asp1", "family": "aspectual",
     "presup": "the company used to fund the lab?",
     "entail": "the company is not funding the lab now?",
     "plain": "The company stopped funding the lab.",
     "negation": "The company didn't stop funding the lab.",
     "question": "Did the company stop funding the lab?",
     "conditional": "If the company stopped funding the lab, the staff applied for new grants."},
    {"sid": "asp2", "family": "aspectual",
     "presup": "the senator had been denying the charges?",
     "entail": "the senator is denying the charges now?",
     "plain": "The senator continued to deny the charges.",
     "negation": "The senator didn't continue to deny the charges.",
     "question": "Did the senator continue to deny the charges?",
     "conditional": "If the senator continued to deny the charges, the hearing was extended."},
    {"sid": "asp3", "family": "aspectual",
     "presup": "the factory had produced before?",
     "entail": "the factory is producing now?",
     "plain": "The factory resumed production.",
     "negation": "The factory didn't resume production.",
     "question": "Did the factory resume production?",
     "conditional": "If the factory resumed production, the town's economy recovered."},
    # ---------- DEFINITE DESCRIPTION (P = existence of referent; E = main predication) ----------
    {"sid": "def1", "family": "definite",
     "presup": "there is a new director?",
     "entail": "the merger was cancelled?",
     "plain": "The new director cancelled the merger.",
     "negation": "The new director didn't cancel the merger.",
     "question": "Did the new director cancel the merger?",
     "conditional": "If the new director cancelled the merger, the shareholders were notified."},
    {"sid": "def2", "family": "definite",
     "presup": "someone saw the crash?",
     "entail": "the witness testified?",
     "plain": "The witness who saw the crash testified.",
     "negation": "The witness who saw the crash didn't testify.",
     "question": "Did the witness who saw the crash testify?",
     "conditional": "If the witness who saw the crash testified, the defense objected."},
    {"sid": "def3", "family": "definite",
     "presup": "the prime minister gave a speech?",
     "entail": "the union was angered?",
     "plain": "The prime minister's speech angered the union.",
     "negation": "The prime minister's speech didn't anger the union.",
     "question": "Did the prime minister's speech anger the union?",
     "conditional": "If the prime minister's speech angered the union, negotiations stalled."},
    # --------------- CLEFT (P = existential; E = exhaustive identification) ---------------
    {"sid": "cle1", "family": "cleft",
     "presup": "someone leaked the memo?",
     "entail": "the intern leaked the memo?",
     "plain": "It was the intern who leaked the memo.",
     "negation": "It wasn't the intern who leaked the memo.",
     "question": "Was it the intern who leaked the memo?",
     "conditional": "If it was the intern who leaked the memo, the manager was informed."},
    {"sid": "cle2", "family": "cleft",
     "presup": "someone broke the vase?",
     "entail": "the cat broke the vase?",
     "plain": "It was the cat that broke the vase.",
     "negation": "It wasn't the cat that broke the vase.",
     "question": "Was it the cat that broke the vase?",
     "conditional": "If it was the cat that broke the vase, the children were relieved."},
    {"sid": "cle3", "family": "cleft",
     "presup": "someone won the contract?",
     "entail": "the smaller firm won the contract?",
     "plain": "It was the smaller firm that won the contract.",
     "negation": "It wasn't the smaller firm that won the contract.",
     "question": "Was it the smaller firm that won the contract?",
     "conditional": "If it was the smaller firm that won the contract, the board was surprised."},
]


def build_items():
    """Flatten scenarios into 96 item-conditions (12 scenarios x 2 targets x 4 frames)."""
    items = []
    for s in SCEN:
        for frame in FRAMES:
            sentence = s[frame]
            for tt in ("presup", "entail"):
                items.append({
                    "id": f"{s['sid']}-{frame}-{tt}",
                    "sid": s["sid"],
                    "family": s["family"],
                    "frame": frame,
                    "cancelling": frame in CANCELLING,
                    "target_type": tt,
                    "sentence": sentence,
                    "target": s[tt],
                    "prompt": QUERY.format(sentence=sentence, target=s[tt]),
                })
    return items


ITEMS = build_items()


def manifest_sha():
    """Stable sha over everything that defines the frozen stimulus/behavioral spec."""
    canon = json.dumps({
        "sys": SYS,
        "query": QUERY,
        "frames": FRAMES,
        "scenarios": SCEN,
    }, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(canon.encode()).hexdigest()


def check():
    errs = []
    if len(SCEN) != 12:
        errs.append(f"expected 12 scenarios, got {len(SCEN)}")
    if len(ITEMS) != 96:
        errs.append(f"expected 96 item-conditions, got {len(ITEMS)}")
    by_fam = {}
    for s in SCEN:
        by_fam[s["family"]] = by_fam.get(s["family"], 0) + 1
    if by_fam != {"factive": 3, "aspectual": 3, "definite": 3, "cleft": 3}:
        errs.append(f"family balance off: {by_fam}")
    sids = [s["sid"] for s in SCEN]
    if len(set(sids)) != len(sids):
        errs.append("duplicate sid")
    for s in SCEN:
        for key in FRAMES + ["presup", "entail"]:
            if not s.get(key):
                errs.append(f"{s['sid']}: missing {key}")
        # targets must read as a fragment ending in '?' (they complete "does it follow that: ...")
        for tt in ("presup", "entail"):
            if not s[tt].rstrip().endswith("?"):
                errs.append(f"{s['sid']}: {tt} target should end with '?'")
        # sanity: negation frame differs from plain; question frame ends with '?'
        if s["negation"] == s["plain"]:
            errs.append(f"{s['sid']}: negation frame identical to plain")
        if not s["question"].rstrip().endswith("?"):
            errs.append(f"{s['sid']}: question frame not interrogative")
        if not s["conditional"].lower().startswith("if "):
            errs.append(f"{s['sid']}: conditional frame does not start with 'If'")
    # per-frame item balance
    by_frame = {}
    for it in ITEMS:
        by_frame[it["frame"]] = by_frame.get(it["frame"], 0) + 1
    if set(by_frame.values()) != {24}:
        errs.append(f"per-frame item balance off: {by_frame}")
    if errs:
        print("FAIL:\n  " + "\n  ".join(errs))
        return 1
    sha = manifest_sha()
    if FROZEN_SHA not in (None, "PINME") and sha != FROZEN_SHA:
        print(f"FAIL: manifest sha drift\n  frozen={FROZEN_SHA}\n  actual={sha}")
        return 1
    print(f"OK: 12 scenarios, 96 item-conditions, families {by_fam}, sha={sha}")
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


if __name__ == "__main__":
    main()
