#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the COMMITMENT-FRAMING DECOMPOSITION probe (session 166).

Narrower follow-up to run 2026-07-01-conditional-projection-rescue (session 159), whose result
result/conditional-projection-rescue-v1 (verdict ROBUST-COLLAPSE) found a striking MODEL DIFFERENCE
inside its commit arm: an explicit "everything the speaker is thereby committed to" framing RESCUED
claude's conditional-antecedent presupposition endorsement (0.42 -> 0.75, E flat) but SUPPRESSED
gpt's (0.17 -> 0.00). The parent left this open (its own words): "Opens a possible narrower follow-up
(why does an explicit commitment framing rescue claude but suppress gpt? — a model-difference in how
'speaker commitment' is read), left for a later session."

THE ONE QUESTION (nothing wider). Decompose that model difference along TWO axes, holding the
sentence constant (always the s159 cond_antecedent sentence — position is NOT a factor here):
  (1) advisory-c confound: is the commit effect driven by the SPEAKER SCENE ("a speaker asserts")
      or by the WORDING ("committed to")?  Read off base -> scene-only -> commit.
  (2) the reading hypothesis H: does each model read "committed to" at a BACKGROUNDING-INCLUSIVE pole
      ("takes for granted", reaches the projecting P) or an AT-ISSUE-RESTRICTIVE pole ("the main
      point", reaches neither backgrounded P nor antecedent-trapped E)?  Read off where each model's
      neutral-worded commit.P falls between its own background.P and its own atissue.P.

H predicts claude's commit clusters at the BACKGROUNDING pole (P high, E low) and gpt's clusters at
the AT-ISSUE pole (P and E both low). A symmetric null (commit between the poles, or the poles fail
to separate the models) is first-class (see verdict map in analyze.py).

STRICT SCOPE (load-bearing; see PREREG §scope). The primary measure is a WITHIN-MODEL contrast: how
a model's own P/E endorsement moves across query framings that hold the sentence constant, and where
its neutral commit arm falls relative to two deliberately-poled anchor arms. It makes NO human
comparison (no human projectivity or commitment baseline is claimed, measured, or needed). Its
terminal anchor status `internal-contrast-only` was RATIFIED for the parent line
(decisions/resolved/presupposition-projection-internal-contrast-anchor, session 159, adversarial
review); this follow-up stays strictly within that ratified within-model contrast, so it carries
`anchor: internal-contrast-only` and opens NO new anchor decision.

DESIGN — 12 matched base scenarios (REUSED VERBATIM from s159's frozen prep.py: same sids, same
presup/entail targets, same antecedent-conditional sentence) x 6 arms x 2 targets (P/E) = 144
item-conditions per model, 432 calls across the 3-model panel. Every arm uses the SAME sentence
(cond_antecedent); only the QUERY WRAPPER (speaker scene x question wording) varies, so every
cross-arm difference is a pure framing effect on one fixed sentence.

  base       (no-scene, plain)      s159 QUERY_PLAIN VERBATIM — must reproduce the collapse.
  scene-only (scene,    plain)      pure speaker-scene effect (no commitment wording).
  commit     (scene,    commit)     s159 QUERY_COMMIT VERBATIM — the effect being decomposed.
  background (scene,    background) backgrounding-INCLUSIVE POLE ("takes for granted").
  atissue    (scene,    atissue)    at-issue-RESTRICTIVE POLE ("directly putting forward as main point").
  background-noscene (no-scene, background)  corroborates the SCENE effect on the backgrounding
                                             question; lets `background` wording be seen without a scene.

Grading + verdict is in analyze.py (NO API calls); this file only freezes the items + a manifest sha.
The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA, so the set cannot drift
after the pre-run critic signs off. These are the PROJECT'S OWN synthetic items (no external corpus).

Usage:
    python3 prep.py            # print manifest sha + per-arm counts
    python3 prep.py --check    # assert structural invariants + frozen sha; non-zero on drift
    python3 prep.py --dump     # write items.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest. "PINME" until the design is frozen (after the pre-run
# critic signs off); pinned once. The probe's FREEZE GUARD refuses to run unless it matches.
FROZEN_SHA = "2b4f69a75efb42250d75d196f10259594adcf9f202523c439d2a7ba7c41d5da2"

# Neutral system prompt — identical to s158/s159; must NOT hint at presupposition / projection /
# commitment / the "right" answer.
SYS = "You are a careful reader. Answer the user's question directly."

# ---------------------------------------------------------------------------------------------
# The six query wrappers. {sentence} is the framed sentence; {target} is the P or E inference
# (already ends in '?'). Every wrapper ends with the s158/s159 tail VERBATIM.
#   QUERY_PLAIN  == s159 QUERY_PLAIN  BYTE-FOR-BYTE  (base arm; the s159 collapse replication).
#   QUERY_COMMIT == s159 QUERY_COMMIT BYTE-FOR-BYTE  (commit arm; the effect being decomposed).
# The other four are new wrappers over the same fixed sentences.
# ---------------------------------------------------------------------------------------------
QUERY_PLAIN = (
    'Consider only the following statement:\n\n'
    '"{sentence}"\n\n'
    'Taking that statement at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_SCENE_PLAIN = (
    'A speaker sincerely and carefully asserts:\n\n'
    '"{sentence}"\n\n'
    'Taking that assertion at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_COMMIT = (
    'A speaker sincerely and carefully asserts:\n\n'
    '"{sentence}"\n\n'
    'Considering everything the speaker is thereby committed to, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_BACKGROUND = (
    'A speaker sincerely and carefully asserts:\n\n'
    '"{sentence}"\n\n'
    'Considering everything the speaker takes for granted in saying this, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_ATISSUE = (
    'A speaker sincerely and carefully asserts:\n\n'
    '"{sentence}"\n\n'
    'Considering only what the speaker is directly putting forward as the main point, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_BACKGROUND_NOSCENE = (
    'Consider only the following statement:\n\n'
    '"{sentence}"\n\n'
    'Considering everything the statement takes for granted, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The six arms, in fixed order. Each carries its two factor labels (scene x wording) and its query.
# Every arm uses the SAME sentence field: cond_antecedent (position is not a factor in this probe).
ARMS = [
    {"arm": "base",               "scene": "no-scene", "wording": "plain",      "query": QUERY_PLAIN},
    {"arm": "scene-only",         "scene": "scene",    "wording": "plain",      "query": QUERY_SCENE_PLAIN},
    {"arm": "commit",             "scene": "scene",    "wording": "commit",     "query": QUERY_COMMIT},
    {"arm": "background",         "scene": "scene",    "wording": "background", "query": QUERY_BACKGROUND},
    {"arm": "atissue",            "scene": "scene",    "wording": "atissue",    "query": QUERY_ATISSUE},
    {"arm": "background-noscene", "scene": "no-scene", "wording": "background", "query": QUERY_BACKGROUND_NOSCENE},
]
SENTENCE_KEY = "cond_antecedent"  # every arm holds this sentence constant.

# ---------------------------------------------------------------------------------------------
# 12 matched base scenarios. presup (P) / entail (E) / cond_antecedent are REUSED VERBATIM from
# s158/s159's frozen prep.py (SCEN). cond_consequent is intentionally NOT carried (position is not
# a factor here). P is the projecting / backgrounded target; E is the at-issue but antecedent-
# trapped target and doubles as the per-arm yes-bias control.
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---------------- FACTIVE (P = complement fact; E = subject's coming-to-know) ----------------
    {"sid": "fac1", "family": "factive",
     "presup": "the door was locked?",
     "entail": "Sam was aware that the door was locked?",
     "cond_antecedent": "If Sam realized that the door was locked, he went back for the key."},
    {"sid": "fac2", "family": "factive",
     "presup": "the ledger had been altered?",
     "entail": "the auditor found out that the ledger had been altered?",
     "cond_antecedent": "If the auditor discovered that the ledger had been altered, the report was delayed."},
    {"sid": "fac3", "family": "factive",
     "presup": "the results were final?",
     "entail": "Maria was aware that the results were final?",
     "cond_antecedent": "If Maria knew that the results were final, she submitted the appeal."},
    # ------------- ASPECTUAL / CHANGE-OF-STATE (P = prior state; E = current state) -------------
    {"sid": "asp1", "family": "aspectual",
     "presup": "the company used to fund the lab?",
     "entail": "the company is not funding the lab now?",
     "cond_antecedent": "If the company stopped funding the lab, the staff applied for new grants."},
    {"sid": "asp2", "family": "aspectual",
     "presup": "the senator had been denying the charges?",
     "entail": "the senator is denying the charges now?",
     "cond_antecedent": "If the senator continued to deny the charges, the hearing was extended."},
    {"sid": "asp3", "family": "aspectual",
     "presup": "the factory had produced before?",
     "entail": "the factory is producing now?",
     "cond_antecedent": "If the factory resumed production, the town's economy recovered."},
    # ---------- DEFINITE DESCRIPTION (P = existence of referent; E = main predication) ----------
    {"sid": "def1", "family": "definite",
     "presup": "there is a new director?",
     "entail": "the merger was cancelled?",
     "cond_antecedent": "If the new director cancelled the merger, the shareholders were notified."},
    {"sid": "def2", "family": "definite",
     "presup": "someone saw the crash?",
     "entail": "the witness testified?",
     "cond_antecedent": "If the witness who saw the crash testified, the defense objected."},
    {"sid": "def3", "family": "definite",
     "presup": "the prime minister gave a speech?",
     "entail": "the union was angered?",
     "cond_antecedent": "If the prime minister's speech angered the union, negotiations stalled."},
    # --------------- CLEFT (P = existential; E = exhaustive identification) ---------------
    {"sid": "cle1", "family": "cleft",
     "presup": "someone leaked the memo?",
     "entail": "the intern leaked the memo?",
     "cond_antecedent": "If it was the intern who leaked the memo, the manager was informed."},
    {"sid": "cle2", "family": "cleft",
     "presup": "someone broke the vase?",
     "entail": "the cat broke the vase?",
     "cond_antecedent": "If it was the cat that broke the vase, the children were relieved."},
    {"sid": "cle3", "family": "cleft",
     "presup": "someone won the contract?",
     "entail": "the smaller firm won the contract?",
     "cond_antecedent": "If it was the smaller firm that won the contract, the board was surprised."},
]


def build_items():
    """Flatten scenarios into 144 item-conditions (12 scenarios x 6 arms x 2 targets)."""
    items = []
    for s in SCEN:
        sentence = s[SENTENCE_KEY]
        for a in ARMS:
            for tt in ("presup", "entail"):
                items.append({
                    "id": f"{s['sid']}-{a['arm']}-{tt}",
                    "sid": s["sid"],
                    "family": s["family"],
                    "arm": a["arm"],
                    "scene": a["scene"],
                    "wording": a["wording"],
                    "target_type": tt,
                    "sentence": sentence,
                    "target": s[tt],
                    "prompt": a["query"].format(sentence=sentence, target=s[tt]),
                })
    return items


ITEMS = build_items()


def manifest_sha():
    """Stable sha over everything that defines the frozen stimulus/behavioral spec."""
    canon = json.dumps({
        "sys": SYS,
        "queries": {
            "plain": QUERY_PLAIN,
            "scene_plain": QUERY_SCENE_PLAIN,
            "commit": QUERY_COMMIT,
            "background": QUERY_BACKGROUND,
            "atissue": QUERY_ATISSUE,
            "background_noscene": QUERY_BACKGROUND_NOSCENE,
        },
        "arms": [{"arm": a["arm"], "scene": a["scene"], "wording": a["wording"]} for a in ARMS],
        "sentence_key": SENTENCE_KEY,
        "scenarios": SCEN,
    }, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(canon.encode()).hexdigest()


def check():
    errs = []
    if len(SCEN) != 12:
        errs.append(f"expected 12 scenarios, got {len(SCEN)}")
    if len(ITEMS) != 144:
        errs.append(f"expected 144 item-conditions, got {len(ITEMS)}")
    by_fam = {}
    for s in SCEN:
        by_fam[s["family"]] = by_fam.get(s["family"], 0) + 1
    if by_fam != {"factive": 3, "aspectual": 3, "definite": 3, "cleft": 3}:
        errs.append(f"family balance off: {by_fam}")
    sids = [s["sid"] for s in SCEN]
    if len(set(sids)) != len(sids):
        errs.append("duplicate sid")
    for s in SCEN:
        for key in ("presup", "entail", "cond_antecedent"):
            if not s.get(key):
                errs.append(f"{s['sid']}: missing {key}")
        for tt in ("presup", "entail"):
            if not s[tt].rstrip().endswith("?"):
                errs.append(f"{s['sid']}: {tt} target should end with '?'")
        if not s["cond_antecedent"].lower().startswith("if "):
            errs.append(f"{s['sid']}: cond_antecedent does not start with 'If'")
    # base and commit wrappers must reproduce s159 byte-for-byte (guard against silent drift).
    S159_PLAIN = (
        'Consider only the following statement:\n\n'
        '"{sentence}"\n\n'
        'Taking that statement at face value, does it follow that: {target}\n\n'
        'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
    )
    S159_COMMIT = (
        'A speaker sincerely and carefully asserts:\n\n'
        '"{sentence}"\n\n'
        'Considering everything the speaker is thereby committed to, does it follow that: {target}\n\n'
        'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
    )
    if QUERY_PLAIN != S159_PLAIN:
        errs.append("base (QUERY_PLAIN) drifted from s159 QUERY_PLAIN")
    if QUERY_COMMIT != S159_COMMIT:
        errs.append("commit (QUERY_COMMIT) drifted from s159 QUERY_COMMIT")
    # per-arm and per-target balance
    by_arm = {}
    by_tt = {}
    for it in ITEMS:
        by_arm[it["arm"]] = by_arm.get(it["arm"], 0) + 1
        by_tt[it["target_type"]] = by_tt.get(it["target_type"], 0) + 1
    if set(by_arm.values()) != {24}:
        errs.append(f"per-arm item balance off: {by_arm}")
    if set(by_tt.values()) != {72}:
        errs.append(f"per-target balance off: {by_tt}")
    if errs:
        print("FAIL:\n  " + "\n  ".join(errs))
        return 1
    sha = manifest_sha()
    if FROZEN_SHA not in (None, "PINME") and sha != FROZEN_SHA:
        print(f"FAIL: manifest sha drift\n  frozen={FROZEN_SHA}\n  actual={sha}")
        return 1
    print(f"OK: 12 scenarios, 144 item-conditions, families {by_fam}, arms {by_arm}, sha={sha}")
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
    print("per-arm:", {a["arm"]: sum(1 for it in ITEMS if it["arm"] == a["arm"]) for a in ARMS})


if __name__ == "__main__":
    main()
