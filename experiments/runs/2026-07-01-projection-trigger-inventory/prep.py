#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the PROJECTION TRIGGER-INVENTORY probe.

Run 2026-07-01-projection-trigger-inventory (session 160). A GENERALIZATION test of the
session-158 PROJECTION probe (run 2026-07-01-presupposition-projection): does the within-model
PRESUPPOSITION-vs-ENTAILMENT projection asymmetry that s158 measured extend to FOUR ADDITIONAL
trigger families the source explicitly names (SEP §1.1: "The list continues with temporal clauses
('before', 'after', 'since'), manner adverbs, sortally restricted predicates ('bachelor'),
quantifiers, names, and intonation (focus, contrast)")? The diagnostic is unchanged — the source's
own "hallmark of presuppositions" (SEP §1.2): under an entailment-cancelling operator the ordinary
entailments drop but the presupposition survives.

This run REUSES the s158 measurement path byte-for-byte: the same SYS system prompt, the same QUERY
wrapper, the same FRAMES, the same build_items()/manifest_sha() shape, the same probe.py and
analyze.py (verbatim), and the same verdict thresholds. ONLY the 12 base scenarios change — the four
s158 families (factive / aspectual / definite / cleft) are replaced by four NEW source-named
families (temporal / manner / only / quantifier). Because the scoring path is identical, the
ratified internal-contrast argument for s158 transfers to this run.

STRICT SCOPE (load-bearing; see PREREG §scope-cap). The primary measure is a WITHIN-MODEL contrast
between two legs of the SAME base sentence — a PRESUPPOSITION target vs. a MATCHED ENTAILMENT target
— across four embedding frames. It makes NO human comparison (no human projectivity baseline is
claimed, measured, or needed). Its terminal anchor status (`internal-contrast-only`) is NOT
self-ratified this session: a wiki/decisions/open/ entry is opened when the result is written, and
the result carries `anchor: pending` contingent on that decision until an independent later session
ratifies. This prep freezes the stimuli only; the scope discipline lives in PREREG.md + the result.

DESIGN — 12 matched base scenarios across 4 trigger families (3 each):
  temporal   — temporal-clause trigger (before / after / since). P = the subordinate-clause event
               happened (projects); E = the main-clause event (the ordinary assertion, cancels).
  manner     — manner-adverb trigger (reluctantly / cleverly / loudly). P = the underlying action
               happened (the VP occurred, projects); E = the manner property held (that it was done
               in that manner, cancels).
  only       — exclusive/focus trigger "only" (the source's "intonation (focus, contrast)" class,
               lexicalized as *only*). P = the prejacent (that the focused subject did the thing,
               projects); E = the exhaustive/exclusive claim (that no one else did, cancels).
  quantifier — presuppositional quantifier / restrictor (both / neither / each of the two). P = the
               existence/cardinality presupposition (the salient two-member set exists, projects);
               E = the scopal predication (that the predicate held of them, cancels).

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

# Frozen sha of the canonical manifest (scenarios + frames + system/query templates). Set to "PINME"
# on first authoring; pinned by the orchestrator once the design is frozen (after the pre-run critic
# signs off). The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA.
FROZEN_SHA = "d0aa515e239413cda77a9b3968af56f95ae05be59ba32761ef3dd5ec6fa17b59"

# ---------------------------------------------------------------------------------------------
# Neutral system prompt. It must NOT hint at presupposition, projection, or the "right" answer.
# (IDENTICAL to s158 — the scoring path is byte-for-byte the same measurement.)
# ---------------------------------------------------------------------------------------------
SYS = "You are a careful reader. Answer the user's question directly."

# The forced-choice query wrapper. {sentence} is the framed base; {target} is the P or E inference.
# The three-way YES / NO / UNCLEAR keeps a cancelled entailment from being forced into a false YES:
# a model that thinks the inference is merely open can say UNCLEAR rather than YES.
# (IDENTICAL to s158.)
QUERY = (
    'Consider only the following statement:\n\n'
    '"{sentence}"\n\n'
    'Taking that statement at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The four embedding frames, in fixed order. The three cancelling frames (the source's own list,
# SEP §1.2) are negation / question / conditional-antecedent. `plain` is the sanity baseline.
# (IDENTICAL to s158.)
FRAMES = ["plain", "negation", "question", "conditional"]
CANCELLING = ("negation", "question", "conditional")

# ---------------------------------------------------------------------------------------------
# 12 matched base scenarios. Each carries the four framed sentences and the two target inferences.
# P (presup) is expected to PROJECT (survive all frames); E (entail) is expected to hold in `plain`
# and be CANCELLED under negation / question / conditional. Targets are written as sentence
# fragments completing "does it follow that: {target}" (so they read grammatically after the colon).
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ---- TEMPORAL clause (P = subordinate-clause event; E = main-clause assertion) ----
    {"sid": "tmp1", "family": "temporal",
     "presup": "Priya left the office?",
     "entail": "Nadia phoned her sister?",
     "plain": "Nadia phoned her sister before Priya left the office.",
     "negation": "Nadia didn't phone her sister before Priya left the office.",
     "question": "Did Nadia phone her sister before Priya left the office?",
     "conditional": "If Nadia phoned her sister before Priya left the office, the news spread quickly."},
    {"sid": "tmp2", "family": "temporal",
     "presup": "the storm reached the coast?",
     "entail": "the crew secured the boats?",
     "plain": "The crew secured the boats after the storm reached the coast.",
     "negation": "The crew didn't secure the boats after the storm reached the coast.",
     "question": "Did the crew secure the boats after the storm reached the coast?",
     "conditional": "If the crew secured the boats after the storm reached the coast, the harbor was calm."},
    {"sid": "tmp3", "family": "temporal",
     "presup": "Grigson took over the firm?",
     "entail": "the office moved downtown?",
     "plain": "The office has moved downtown since Grigson took over the firm.",
     "negation": "The office hasn't moved downtown since Grigson took over the firm.",
     "question": "Has the office moved downtown since Grigson took over the firm?",
     "conditional": "If the office has moved downtown since Grigson took over the firm, the rent went up."},
    # ---- MANNER adverb (P = the action occurred; E = the manner property held) ----
    {"sid": "man1", "family": "manner",
     "presup": "Owen signed the contract?",
     "entail": "Owen was reluctant to sign the contract?",
     "plain": "Owen reluctantly signed the contract.",
     "negation": "Owen didn't reluctantly sign the contract.",
     "question": "Did Owen reluctantly sign the contract?",
     "conditional": "If Owen reluctantly signed the contract, the deal was rushed."},
    {"sid": "man2", "family": "manner",
     "presup": "Lena solved the puzzle?",
     "entail": "Lena solved the puzzle in a clever way?",
     "plain": "Lena cleverly solved the puzzle.",
     "negation": "Lena didn't cleverly solve the puzzle.",
     "question": "Did Lena cleverly solve the puzzle?",
     "conditional": "If Lena cleverly solved the puzzle, the judges were impressed."},
    {"sid": "man3", "family": "manner",
     "presup": "the mayor announced the closure?",
     "entail": "the mayor announced the closure in a loud manner?",
     "plain": "The mayor loudly announced the closure.",
     "negation": "The mayor didn't loudly announce the closure.",
     "question": "Did the mayor loudly announce the closure?",
     "conditional": "If the mayor loudly announced the closure, the crowd heard it."},
    # ---- ONLY (focus/exclusive) (P = the prejacent; E = the exhaustive claim) ----
    {"sid": "onl1", "family": "only",
     "presup": "Dana signed the petition?",
     "entail": "nobody other than Dana signed the petition?",
     "plain": "Dana was the only one who signed the petition.",
     "negation": "Dana wasn't the only one who signed the petition.",
     "question": "Was Dana the only one who signed the petition?",
     "conditional": "If Dana was the only one who signed the petition, the vote was close."},
    {"sid": "onl2", "family": "only",
     "presup": "the intern flagged the error?",
     "entail": "nobody other than the intern flagged the error?",
     "plain": "The intern was the only person who flagged the error.",
     "negation": "The intern wasn't the only person who flagged the error.",
     "question": "Was the intern the only person who flagged the error?",
     "conditional": "If the intern was the only person who flagged the error, the review was thorough."},
    {"sid": "onl3", "family": "only",
     "presup": "the north branch reported a profit?",
     "entail": "no branch other than the north branch reported a profit?",
     "plain": "The north branch was the only branch that reported a profit.",
     "negation": "The north branch wasn't the only branch that reported a profit.",
     "question": "Was the north branch the only branch that reported a profit?",
     "conditional": "If the north branch was the only branch that reported a profit, the quarter was weak."},
    # ---- QUANTIFIER (both/neither/each of the two) (P = the two-member set exists; E = the predication) ----
    {"sid": "qnt1", "family": "quantifier",
     "presup": "there were two auditors?",
     "entail": "the auditors flagged the report?",
     "plain": "Both auditors flagged the report.",
     "negation": "Neither of the two auditors flagged the report.",
     "question": "Did both auditors flag the report?",
     "conditional": "If both auditors flagged the report, the filing was delayed."},
    {"sid": "qnt2", "family": "quantifier",
     "presup": "there were two candidates?",
     "entail": "the candidates passed the interview?",
     "plain": "Both candidates passed the interview.",
     "negation": "Neither of the two candidates passed the interview.",
     "question": "Did both candidates pass the interview?",
     "conditional": "If both candidates passed the interview, the panel was pleased."},
    {"sid": "qnt3", "family": "quantifier",
     "presup": "there were two witnesses?",
     "entail": "the witnesses identified the suspect?",
     "plain": "Each of the two witnesses identified the suspect.",
     "negation": "Neither of the two witnesses identified the suspect.",
     "question": "Did each of the two witnesses identify the suspect?",
     "conditional": "If each of the two witnesses identified the suspect, the case was strong."},
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
    if by_fam != {"temporal": 3, "manner": 3, "only": 3, "quantifier": 3}:
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
                         for k in ('temporal', 'manner', 'only', 'quantifier')})


if __name__ == "__main__":
    main()
