"""Build + freeze the MATCHED-DIFFICULTY ADD-vs-CANCEL MONOTONICITY-GENERALIZATION
BATTERY item set (2026-06-28, session 135).

Pre-registration (charter s8): EMITS
experiments/data/monotonicity-generalization-battery/items.csv, run + committed BEFORE
any probe call, sha256-hashed. This is the SOLE DECISIVE TEST of
conjecture/constructional-monotonicity-asymmetry, operationalized + RATIFIED s134 in
decisions/resolved/constructional-monotonicity-generalization-operationalization
(ADOPT-WITH-MODS). The yardstick (pair, B2 ceiling gate, frozen thresholds) is FIXED by
that decision; this session BUILDS + RUNS it, re-tuning nothing.

THE FROZEN PAIR (ratified, prereq 3) -- a genuinely NEW add/cancel pair beyond
caused-motion / way / conative:
  ADD arm    = the RESULTATIVE construction. Adds the result-state entailment the bare
               verb lacks: "Maria hammered the metal flat." |= "The metal became flat.";
               bare "Maria hammered the metal." |/= it. Verified headroom-clean verb pool
               from the s133 calibration (result/addarm-headroom-calibration-v1),
               EXCLUDING trap verbs freeze, sharpen (telic; control already at ceiling).
  CANCEL arm = the *for*-DURATIVE ASPECTUAL coercion of a SEMELFACTIVE/punctual verb.
               Cancels the single-bounded-event default: "The light flashed." |= "...
               only once."; "The light flashed for ten minutes." coerces iteration ->
               cancels "only once". Verb pool DISJOINT from the ADD pool (MOD-1: kick,
               bounce removed) and de-duplicated (MOD-2).

THE MATCHED CONFLICTING-CUE PARADIGM (template: result/conative-cancel-direction-v2).
Each arm has three conditions; the DISCRIMINATING cell is the no-cue construction reading:
  ADD:    control      "Maria hammered the metal."              -> bare default (want low; B2 control)
          construction "Maria hammered the metal flat."         -> LICENSING-no-cue (want ceiling)  = add_no_cue
          cue          "...flat, but the metal did not become flat." -> explicit DENIAL; follow cue = WITHHOLD
  CANCEL: default      "The light flashed."                     -> lexical default "only once" (want ceiling; B2 default)
          construction "The light flashed for ten minutes."     -> SUPPRESSION; suppression_no_cue = 100 - affirm
          cue          "...for ten minutes, but it flashed only once." -> explicit RE-ASSERTION; follow cue = AFFIRM
The ADD cue DENIES the licensed inference (mirror: model should withhold); the CANCEL cue
RE-ASSERTS the suppressed default (mirror: model should affirm). Both cue sentences are
deliberately internally-conflicting, exactly as cc-v2's cue arm was.

FROZEN THRESHOLDS (prereq 2; set in the ratified decision BEFORE any data) -- read by
analyze.py, NEVER re-tuned after data:
  B2 blocking ceiling gate (on the frozen CALIB subset below, before the main read):
    ADD admitted only if construction licensing-no-cue affirm >= 0.80 AND bare control
        affirm <= 0.40, in >= 2/3 models;
    CANCEL admitted only if lexical-default affirm ("only once") >= 0.80, in >= 2/3 models
        (MOD-3: contestable default; NO-GO re-pairs the cancel coercion before spend).
    If either fails -> reject/re-pair the pair BEFORE the main run.
  Asymmetry direction (the "cliff" analogue): on the no-cue cell,
    add_no_cue - cancel_no_cue >= 20 pp in >= 2/3 models  -> CONFIRMS (confirm-leg 1);
    |add_no_cue - cancel_no_cue| < 20 pp in >= 2/3 models  -> SYMMETRIC -> falsifies;
    cancel_no_cue - add_no_cue >= 20 pp in >= 2/3 models  -> REVERSAL -> falsifies.
  Instrument fragility (confirm-leg 2): cancel arm's NLI-vs-FC disagreement on the no-cue
    cell must exceed the add arm's by >= 10 pp in >= 2/3 models.
  Cue-arm reading rule (inherited cc-v2): >= 70% follow-cue in >= 2/3 = robust;
    ~chance / construction-following = informative partial-null.

HUMAN ANCHOR: none asserted -- the new-pair leg is `internal-contrast-only` by ratified
decision (decisions/resolved/conflicting-cue-human-anchor). It makes NO human-comparison
claim; it is a within-model add-vs-cancel direction contrast. No human label invented.
(A3's anchored-replication leg was DROPPED, prereq 4.)

Run: python3 build_items.py   (no API; writes + hashes the frozen CSV)
"""
import csv
import hashlib
import os

# ---------------------------------------------------------------------------
# ADD arm: RESULTATIVE -- (verb, past, object, result_adjective)
# result hypothesis = "The <object> became <result_adjective>."
# Verb pool = the s133 calibration's headroom-clean resultative verbs, EXCLUDING the
# verified trap verbs freeze, sharpen (telic; control already at ceiling). 10 verbs.
RESULTATIVE = [
    ("beat",    "beat",      "cream",   "stiff"),
    ("boil",    "boiled",    "sauce",   "thick"),
    ("cut",     "cut",       "rope",    "short"),
    ("hammer",  "hammered",  "metal",   "flat"),
    ("kick",    "kicked",    "door",    "open"),
    ("paint",   "painted",   "fence",   "white"),
    ("push",    "pushed",    "gate",    "open"),
    ("scrub",   "scrubbed",  "pot",     "clean"),
    ("squeeze", "squeezed",  "sponge",  "dry"),
    ("wipe",    "wiped",     "counter", "clean"),
]
# ADD subjects (transitive resultative needs a human agent); rotate so no name dominates.
ADD_SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
                "Aisha", "Sam"]

# ---------------------------------------------------------------------------
# CANCEL arm: *for*-DURATIVE ASPECTUAL coercion of a SEMELFACTIVE/punctual verb.
# (verb, past, subject_np, complement)  -- complement may be "" (intransitive).
# default hypothesis = "<subject_np> <past> only once." (complement dropped in hyp).
# construction = "<subject_np> <past> <complement> for ten minutes." (coerces iteration).
# Pool DISJOINT from the RESULTATIVE pool (MOD-1) and de-duplicated (MOD-2). 7 verbs.
DURATIVE = "for ten minutes"   # uniform for-durative; coerces iteration on a semelfactive
CANCEL = [
    ("flash", "flashed", "The light",   ""),
    ("knock", "knocked", "The visitor", "on the door"),
    ("tap",   "tapped",  "The user",    "on the screen"),
    ("blink", "blinked", "The driver",  ""),
    ("jump",  "jumped",  "The dancer",  ""),
    ("cough", "coughed", "The patient", ""),
    ("nod",   "nodded",  "The student", ""),
]

# FROZEN B2 CALIBRATION SUBSET (decision prereq 2: "a frozen calibration subset of the
# MAIN items"). 4 add verbs + 4 cancel verbs, B2 cells only (add construction+control,
# cancel default). Run + gated BEFORE the main read; chosen here, before any data.
CALIB_ADD = {"hammer", "kick", "cut", "push"}
CALIB_CANCEL = {"flash", "cough", "jump", "nod"}


def rows():
    out = []
    # ADD arm: RESULTATIVE -> control / construction / cue
    for i, (verb, past, obj, res) in enumerate(RESULTATIVE):
        subj = ADD_SUBJECTS[i % len(ADD_SUBJECTS)]
        obj_np = f"the {obj}"
        hyp = f"The {obj} became {res}."
        calib = "1" if verb in CALIB_ADD else "0"
        conds = [
            # condition, sentence, nli_gold, fc_gold, affirm_correct, calib
            ("control",      f"{subj} {past} {obj_np}.",
             "NA", "NA", "NA", calib),
            ("construction", f"{subj} {past} {obj_np} {res}.",
             "0", "YES", "1", calib),
            ("cue",          f"{subj} {past} {obj_np} {res}, but {obj_np} did not become {res}.",
             "2", "NO", "0", "0"),
        ]
        for cond, sent, ng, fg, ac, cl in conds:
            out.append(dict(item_id=f"add-{verb}-{cond}", arm="add",
                construction="resultative", stem=verb, condition=cond,
                sentence=sent, nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg,
                affirm_correct=ac, calib=cl))
    # CANCEL arm: for-durative -> default / construction / cue
    for verb, past, subj_np, comp in CANCEL:
        comp_sp = f" {comp}" if comp else ""
        hyp = f"{subj_np} {past} only once."
        calib = "1" if verb in CALIB_CANCEL else "0"
        # ANTI-CHEAT: only the DEFAULT cell is in the B2 calib subset. The cancel
        # SUPPRESSION (construction) cell -- the cancel_no_cue asymmetry side -- is held
        # OUT of calib so the asymmetry magnitude is NOT computable before the pre-run
        # critic GO and the main read. (The add construction cell is unavoidably both a
        # B2 cell and the add_no_cue side, so the add side alone is visible at calib; the
        # decisive asymmetry needs cancel_no_cue, which is not.)
        conds = [
            ("default",      f"{subj_np} {past}{comp_sp}.",
             "0", "YES", "1", calib),
            ("construction", f"{subj_np} {past}{comp_sp} {DURATIVE}.",
             "2", "NO", "0", "0"),
            ("cue",          f"{subj_np} {past}{comp_sp} {DURATIVE}, but {subj_np.lower()} {past} only once.",
             "0", "YES", "1", "0"),
        ]
        for cond, sent, ng, fg, ac, cl in conds:
            out.append(dict(item_id=f"can-{verb}-{cond}", arm="cancel",
                construction="for-durative", stem=verb, condition=cond,
                sentence=sent, nli_hypothesis=hyp, nli_gold=ng, fc_gold=fg,
                affirm_correct=ac, calib=cl))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                       "monotonicity-generalization-battery", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "arm", "construction", "stem", "condition", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct", "calib"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    nadd = sum(1 for r in rs if r["arm"] == "add")
    ncalib = sum(1 for r in rs if r["calib"] == "1")
    # disjointness self-check (MOD-1): no cancel verb appears in the add pool
    add_verbs = {v[0] for v in RESULTATIVE}
    can_verbs = {v[0] for v in CANCEL}
    overlap = add_verbs & can_verbs
    print(f"wrote {len(rs)} items ({nadd} add + {len(rs)-nadd} cancel) -> {out}")
    print(f"  add: {len(RESULTATIVE)} resultative verbs x (control/construction/cue); "
          f"cancel: {len(CANCEL)} for-durative verbs x (default/construction/cue)")
    print(f"  calib-subset items: {ncalib}  (add {sorted(CALIB_ADD)} + cancel {sorted(CALIB_CANCEL)})")
    print(f"  MOD-1 disjointness check: add/cancel verb overlap = {overlap or 'NONE (clean)'}")
    print(f"  MOD-2 dedup check: cancel pool distinct = {len(can_verbs) == len(CANCEL)}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
