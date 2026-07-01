#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the CONDITIONAL-PROJECTION-RESCUE follow-up probe.

Follow-up to run 2026-07-01-presupposition-projection (session 158), whose result
result/presupposition-projection-v1 found verdict PROJECTION (2/3) BUT an across-panel
COLLAPSE of projection under the conditional-antecedent frame: presupposition-survival under the
conditional frame was 0.42 / 0.17 / 0.17 (claude / gpt / gemini), at or near the matched-entailment
leg, while negation was textbook-clean and questions projected strongly.

THE ONE QUESTION (nothing wider). Is that conditional-antecedent collapse RESCUABLE by an explicit
framing, or is it a robust limit of the text-trained projection behavior? Three rescue levers, each
a within-model minimal-pair against a BASE arm that REPLICATES the s158 conditional cell verbatim:

  BASE    — the s158 conditional-antecedent frame + neutral query, VERBATIM. Replication anchor:
            presup-endorse here should reproduce the s158 collapse (low; ~0.42/0.17/0.17).
  COMMIT  — same antecedent-conditional sentence, but the query reframes it as a sincere speaker
            ASSERTION and asks what the speaker is thereby COMMITTED to. (Rescue lever a: a speaker
            asserting a conditional is committed to the antecedent's presupposition but NOT to the
            antecedent's truth — so COMMIT should lift P and not E if the model tracks commitment.)
  CONSEQ  — the SAME trigger relocated to the CONSEQUENT of a conditional with a neutral, unrelated
            antecedent. (Rescue lever b: a non-antecedent position. Standard filtering theory says a
            consequent presupposition projects when the antecedent does not establish it; this
            isolates whether the collapse is ANTECEDENT-POSITION-specific vs. conditional-general.
            Doubles as a within-run position control.)
  BELIEF  — same antecedent-conditional sentence, query asks whether the SPEAKER BELIEVES the target.
            (Rescue lever c: a speaker-belief frame. A speaker uttering the conditional believes its
            antecedent's presupposition, not the antecedent — so BELIEF should lift P and not E.)

STRICT SCOPE (load-bearing; see PREREG §scope-cap). The primary measure is a WITHIN-MODEL contrast:
(i) P-vs-E endorsement WITHIN each arm (the E leg is the yes-bias control — a global yes-shift from a
framing lifts E too), and (ii) P endorsement ACROSS arms (does a framing lift P above BASE). It makes
NO human comparison (no human projectivity baseline is claimed, measured, or needed). Its terminal
anchor status `internal-contrast-only` was RATIFIED for the parent line
(decisions/resolved/presupposition-projection-internal-contrast-anchor, session 159, adversarial
review); this follow-up stays strictly within that ratified within-model contrast, so it carries
`anchor: internal-contrast-only` and opens NO new anchor decision.

DESIGN — 12 matched base scenarios (REUSED VERBATIM from s158's frozen prep.py: same sids, same
presup/entail targets, same antecedent-conditional sentences) x 4 arms x 2 targets (P/E) = 96
item-conditions per model, 288 calls across the 3-model panel.

Grading + verdict is in analyze.py (NO API calls); this file only freezes the items + a manifest sha.
The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA, so the set cannot drift
after the pre-run critic signs off. These are the PROJECT'S OWN synthetic items (no external corpus).

Usage:
    python3 prep.py            # print manifest sha + per-family/arm counts
    python3 prep.py --check    # assert structural invariants + frozen sha; non-zero on drift
    python3 prep.py --dump     # write items.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest. "PINME" until the design is frozen (before the pre-run
# critic signs off); pinned once. The probe's FREEZE GUARD refuses to run unless it matches.
FROZEN_SHA = "c88ef626abd1f0b8cb22e19dd27b7b96b7016ed634b79de3cabe2e399079fe54"

# Neutral system prompt — identical to s158; must NOT hint at presupposition / projection / answer.
SYS = "You are a careful reader. Answer the user's question directly."

# ---------------------------------------------------------------------------------------------
# The three query wrappers. {sentence} is the framed sentence; {target} is the P or E inference
# (already ends in '?'). QUERY_PLAIN is s158's conditional-frame query VERBATIM (so BASE truly
# replicates the s158 conditional cell). CONSEQ reuses QUERY_PLAIN (isolates trigger POSITION);
# COMMIT and BELIEF reframe the query (isolate FRAMING) over the same antecedent-conditional.
# ---------------------------------------------------------------------------------------------
QUERY_PLAIN = (
    'Consider only the following statement:\n\n'
    '"{sentence}"\n\n'
    'Taking that statement at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_COMMIT = (
    'A speaker sincerely and carefully asserts:\n\n'
    '"{sentence}"\n\n'
    'Considering everything the speaker is thereby committed to, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)
QUERY_BELIEF = (
    'A speaker sincerely and carefully asserts:\n\n'
    '"{sentence}"\n\n'
    'Does the speaker believe that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The four arms, in fixed order. Each names its sentence field and its query template.
ARMS = [
    {"arm": "base",   "sentence_key": "cond_antecedent", "query": QUERY_PLAIN},
    {"arm": "commit", "sentence_key": "cond_antecedent", "query": QUERY_COMMIT},
    {"arm": "conseq", "sentence_key": "cond_consequent", "query": QUERY_PLAIN},
    {"arm": "belief", "sentence_key": "cond_antecedent", "query": QUERY_BELIEF},
]
RESCUE_ARMS = ("commit", "conseq", "belief")

# ---------------------------------------------------------------------------------------------
# 12 matched base scenarios. presup / entail / cond_antecedent are REUSED VERBATIM from s158's
# frozen prep.py (SCEN). cond_consequent is NEW: the same trigger clause relocated to the
# consequent of a conditional whose antecedent is neutral and unrelated (does not establish P or E).
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---------------- FACTIVE (P = complement fact; E = subject's coming-to-know) ----------------
    {"sid": "fac1", "family": "factive",
     "presup": "the door was locked?",
     "entail": "Sam was aware that the door was locked?",
     "cond_antecedent": "If Sam realized that the door was locked, he went back for the key.",
     "cond_consequent": "If the porch light was off, Sam realized that the door was locked."},
    {"sid": "fac2", "family": "factive",
     "presup": "the ledger had been altered?",
     "entail": "the auditor found out that the ledger had been altered?",
     "cond_antecedent": "If the auditor discovered that the ledger had been altered, the report was delayed.",
     "cond_consequent": "If the review was thorough, the auditor discovered that the ledger had been altered."},
    {"sid": "fac3", "family": "factive",
     "presup": "the results were final?",
     "entail": "Maria was aware that the results were final?",
     "cond_antecedent": "If Maria knew that the results were final, she submitted the appeal.",
     "cond_consequent": "If the email arrived on time, Maria knew that the results were final."},
    # ------------- ASPECTUAL / CHANGE-OF-STATE (P = prior state; E = current state) -------------
    {"sid": "asp1", "family": "aspectual",
     "presup": "the company used to fund the lab?",
     "entail": "the company is not funding the lab now?",
     "cond_antecedent": "If the company stopped funding the lab, the staff applied for new grants.",
     "cond_consequent": "If the meeting was short, the company stopped funding the lab."},
    {"sid": "asp2", "family": "aspectual",
     "presup": "the senator had been denying the charges?",
     "entail": "the senator is denying the charges now?",
     "cond_antecedent": "If the senator continued to deny the charges, the hearing was extended.",
     "cond_consequent": "If the vote was close, the senator continued to deny the charges."},
    {"sid": "asp3", "family": "aspectual",
     "presup": "the factory had produced before?",
     "entail": "the factory is producing now?",
     "cond_antecedent": "If the factory resumed production, the town's economy recovered.",
     "cond_consequent": "If the weather cleared, the factory resumed production."},
    # ---------- DEFINITE DESCRIPTION (P = existence of referent; E = main predication) ----------
    {"sid": "def1", "family": "definite",
     "presup": "there is a new director?",
     "entail": "the merger was cancelled?",
     "cond_antecedent": "If the new director cancelled the merger, the shareholders were notified.",
     "cond_consequent": "If the quarter went badly, the new director cancelled the merger."},
    {"sid": "def2", "family": "definite",
     "presup": "someone saw the crash?",
     "entail": "the witness testified?",
     "cond_antecedent": "If the witness who saw the crash testified, the defense objected.",
     "cond_consequent": "If the trial proceeded, the witness who saw the crash testified."},
    {"sid": "def3", "family": "definite",
     "presup": "the prime minister gave a speech?",
     "entail": "the union was angered?",
     "cond_antecedent": "If the prime minister's speech angered the union, negotiations stalled.",
     "cond_consequent": "If the economy worsened, the prime minister's speech angered the union."},
    # --------------- CLEFT (P = existential; E = exhaustive identification) ---------------
    {"sid": "cle1", "family": "cleft",
     "presup": "someone leaked the memo?",
     "entail": "the intern leaked the memo?",
     "cond_antecedent": "If it was the intern who leaked the memo, the manager was informed.",
     "cond_consequent": "If the security review ran, it was the intern who leaked the memo."},
    {"sid": "cle2", "family": "cleft",
     "presup": "someone broke the vase?",
     "entail": "the cat broke the vase?",
     "cond_antecedent": "If it was the cat that broke the vase, the children were relieved.",
     "cond_consequent": "If the shelf was unstable, it was the cat that broke the vase."},
    {"sid": "cle3", "family": "cleft",
     "presup": "someone won the contract?",
     "entail": "the smaller firm won the contract?",
     "cond_antecedent": "If it was the smaller firm that won the contract, the board was surprised.",
     "cond_consequent": "If the bids were sealed, it was the smaller firm that won the contract."},
]


def build_items():
    """Flatten scenarios into 96 item-conditions (12 scenarios x 4 arms x 2 targets)."""
    items = []
    for s in SCEN:
        for a in ARMS:
            sentence = s[a["sentence_key"]]
            for tt in ("presup", "entail"):
                items.append({
                    "id": f"{s['sid']}-{a['arm']}-{tt}",
                    "sid": s["sid"],
                    "family": s["family"],
                    "arm": a["arm"],
                    "rescue": a["arm"] in RESCUE_ARMS,
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
        "queries": {"plain": QUERY_PLAIN, "commit": QUERY_COMMIT, "belief": QUERY_BELIEF},
        "arms": [{"arm": a["arm"], "sentence_key": a["sentence_key"]} for a in ARMS],
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
        for key in ("presup", "entail", "cond_antecedent", "cond_consequent"):
            if not s.get(key):
                errs.append(f"{s['sid']}: missing {key}")
        for tt in ("presup", "entail"):
            if not s[tt].rstrip().endswith("?"):
                errs.append(f"{s['sid']}: {tt} target should end with '?'")
        # both conditional sentences must be genuine conditionals starting with 'If '
        for key in ("cond_antecedent", "cond_consequent"):
            if not s[key].lower().startswith("if "):
                errs.append(f"{s['sid']}: {key} does not start with 'If'")
        # position invariant: in cond_antecedent the trigger leads (right after 'If '); in
        # cond_consequent a DIFFERENT (neutral) antecedent leads, so the two must differ.
        if s["cond_antecedent"] == s["cond_consequent"]:
            errs.append(f"{s['sid']}: antecedent and consequent sentences identical")
    # per-arm and per-target balance
    by_arm = {}
    by_tt = {}
    for it in ITEMS:
        by_arm[it["arm"]] = by_arm.get(it["arm"], 0) + 1
        by_tt[it["target_type"]] = by_tt.get(it["target_type"], 0) + 1
    if set(by_arm.values()) != {24}:
        errs.append(f"per-arm item balance off: {by_arm}")
    if set(by_tt.values()) != {48}:
        errs.append(f"per-target balance off: {by_tt}")
    if errs:
        print("FAIL:\n  " + "\n  ".join(errs))
        return 1
    sha = manifest_sha()
    if FROZEN_SHA not in (None, "PINME") and sha != FROZEN_SHA:
        print(f"FAIL: manifest sha drift\n  frozen={FROZEN_SHA}\n  actual={sha}")
        return 1
    print(f"OK: 12 scenarios, 96 item-conditions, families {by_fam}, arms {by_arm}, sha={sha}")
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
