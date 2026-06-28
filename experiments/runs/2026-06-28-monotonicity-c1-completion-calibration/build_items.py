"""Build + freeze the C1 TELIC-COMPLETION DEFAULT B2 CALIBRATION set
(2026-06-28, session 137).

STEP 1 of the FROZEN build instruction in
decisions/resolved/monotonicity-cancel-arm-redesign (ratified s136, ADOPT C1
conditional on its own B2 calibration). This is a *calibration only*: it measures
whether the completion default of a simple-past accomplishment is a model-held
entailment at the B2 ceiling, BEFORE any matched asymmetry battery is built or run.
The s135 lesson is binding: do NOT assume the completion default is at ceiling --
MEASURE it. A NO-GO here does not relax the bar; it triggers STEP 1b (C2 privative,
after M2's written conjecture-scope amendment).

THE C1 CANCEL DIRECTION (telic-completion accomplishment cancellation):
  DEFAULT (this calibration): a simple-past accomplishment with a quantized/definite
    object plausibly ENTAILS culmination/completion --
      "Maria built the house."  |=  "Maria finished building the house."
    The bare-frame completion default is what STEP 2's matched cancel arm would later
    SUPPRESS, so it must itself sit at ceiling on the bare frame (B2, MOD-3).
  CANCELLING CONSTRUCTION (held OUT of this calibration; built only on a GO in STEP 2):
    the *for*-durative / atelic frame coerces a non-culminating reading (the
    imperfective paradox): "Maria built the house for two hours" need not entail she
    finished building it. NOT run here -- only the DEFAULT cell is calibrated, exactly
    as s135 held the cancel SUPPRESSION cell out of its calib subset (anti-cheat: the
    asymmetry magnitude must not be computable at the gate).

FROZEN COMPLETION-HYPOTHESIS PHRASING (decision STEP 1: "pick one phrasing, freeze it"):
  hypothesis = "<Subject> finished <gerund> <object>."   (the standard accomplishment
  culmination diagnostic; uniform across all eight verbs).

VERB POOL (decision STEP 1: >=6-8 genuine accomplishment verbs whose bare simple-past
plausibly entails culmination, DISJOINT from the resultative ADD pool
{beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe} -- note `paint` is
in the add pool, so no accomplishment item is a resultative). 8 verbs, all
incremental-theme accomplishments with a definite object:
  build, write, read, bake, knit, mow, draw, dig.

FROZEN B2 GATE (decision STEP 1, NOT relaxable):
  completion default affirm ("finished V-ing") >= 0.80 in >= 2/3 models, strict NLI
  (NLI primary, label 0 = entailment), temperature 0, the ratified panel
  (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash).
  GO   -> STEP 2 (build the matched C1 cancel arm; reuse the frozen B2-passing ADD arm).
  NO-GO -> record a verified C1-NO-GO result, then STEP 1b (C2 privative, after M2).

HUMAN ANCHOR: none. This is a within-model feasibility calibration, `internal-contrast-only`
by the ratified conflicting-cue-human-anchor decision; no human-comparison claim, no human
label invented.

Run: python3 build_items.py   (no API; writes + sha256-hashes the frozen CSV)
"""
import csv
import hashlib
import os

# ---------------------------------------------------------------------------
# C1 accomplishment pool: (verb, past, gerund, object_noun)
#   default sentence  = "<Subject> <past> the <object_noun>."
#   completion hypothesis = "<Subject> finished <gerund> the <object_noun>."
# Disjoint from the resultative ADD pool (build/write/read/bake/knit/mow/draw/dig vs
# beat/boil/cut/hammer/kick/paint/push/scrub/squeeze/wipe -- no overlap). Each is an
# incremental-theme accomplishment with a quantized definite object, whose simple past
# plausibly entails culmination.
ACCOMPLISHMENT = [
    ("build", "built",   "building", "house"),
    ("write", "wrote",   "writing",  "letter"),
    ("read",  "read",    "reading",  "book"),
    ("bake",  "baked",   "baking",   "cake"),
    ("knit",  "knitted", "knitting", "sweater"),
    ("mow",   "mowed",   "mowing",   "lawn"),
    ("draw",  "drew",    "drawing",  "portrait"),
    ("dig",   "dug",     "digging",  "tunnel"),
]
# Subjects rotate so no name dominates (same convention as the s135 add arm).
SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos"]


def rows():
    out = []
    for i, (verb, past, ger, obj) in enumerate(ACCOMPLISHMENT):
        subj = SUBJECTS[i % len(SUBJECTS)]
        sent = f"{subj} {past} the {obj}."
        hyp = f"{subj} finished {ger} the {obj}."
        out.append(dict(
            item_id=f"c1cal-{verb}-default", arm="cancel-c1",
            construction="telic-completion", stem=verb, condition="default",
            sentence=sent, nli_hypothesis=hyp,
            nli_gold="0", fc_gold="YES", affirm_correct="1", calib="1",
        ))
    return out


def main():
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "data",
        "monotonicity-c1-completion-calibration", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "arm", "construction", "stem", "condition", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct", "calib"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    # disjointness self-check vs the resultative ADD pool (decision STEP 1)
    add_pool = {"beat", "boil", "cut", "hammer", "kick", "paint", "push",
                "scrub", "squeeze", "wipe"}
    c1_verbs = {v[0] for v in ACCOMPLISHMENT}
    overlap = add_pool & c1_verbs
    print(f"wrote {len(rs)} C1 completion-default calibration items -> {out}")
    print(f"  verbs ({len(c1_verbs)}): {sorted(c1_verbs)}")
    print(f"  ADD-pool disjointness check: overlap = {overlap or 'NONE (clean)'}")
    print(f"  completion hypothesis phrasing (frozen): "
          f"'<Subj> finished <gerund> the <object>.'")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
