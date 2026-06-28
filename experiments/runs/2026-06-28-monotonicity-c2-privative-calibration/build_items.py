"""Build + freeze the C2 PRIVATIVE-MODIFIER category-default B2 CALIBRATION set
(2026-06-28, session 137).

STEP 1b of the FROZEN build instruction in
decisions/resolved/monotonicity-cancel-arm-redesign (ratified s136). Reached because
STEP 1 (C1 telic-completion) was a B2 NO-GO
(result/monotonicity-c1-completion-calibration-v1). M2 (the deliberate written
conjecture-scope amendment broadening to a nominal/adjectival privative cancel arm) was
applied BEFORE this build, in
wiki/findings/conjectures/constructional-monotonicity-asymmetry.md.

Like STEP 1 this is a *calibration only*: it measures whether a bare head noun's
CATEGORY-membership default is a model-held entailment at the B2 ceiling, BEFORE any
matched asymmetry battery is built or run. The s135/C1 lesson is binding: do NOT assume
the category default is at ceiling -- MEASURE it. A NO-GO here triggers STEP 3
(principled-limit closure: the matched cancel arm is un-instrumentable at ceiling on the
strict-NLI panel without a categorically-held lexical-entailment default).

THE C2 CANCEL DIRECTION (privative-modifier cancellation):
  DEFAULT (this calibration): a bare head noun ENTAILS its superordinate category --
      "Sam bought a gun."  |=  "Sam bought a weapon."
    The category default is what STEP 2's cancel arm would SUPPRESS, so it must itself
    sit at ceiling on the bare frame (B2).
  CANCELLING CONSTRUCTION (held OUT of this calibration; built only on a GO in STEP 2):
    a PRIVATIVE modifier cancels category membership (the imperfective-paradox analogue
    in the nominal domain): "Sam bought a fake gun" does not entail "Sam bought a weapon".
    The privative modifier frozen for each item is recorded below for STEP 2 but is NOT
    run here (anti-cheat: the asymmetry magnitude must not be computable at the gate).

FROZEN CATEGORY-HYPOTHESIS PHRASING (one frozen phrasing per the STEP-1 convention):
  hypothesis = "<Subject> <past_verb> a/an <category>."   -- the same verb frame as the
  premise, with the head noun replaced by its superordinate category.

NOUN POOL (decision STEP 1b: >=6-8 pairs; bare noun |= category, cancellable by a
privative modifier). 8 items, diverse categories (weapon x2, gemstone, flower, animal,
fruit, jewel, musical instrument):
  gun, diamond, rose, tiger, apple, pearl, sword, violin.

FROZEN B2 GATE (decision STEP 1b, NOT relaxable):
  category-membership default affirm ("a gun" -> "a weapon") >= 0.80 in >= 2/3 models,
  strict NLI (NLI primary, label 0 = entailment), temperature 0, the ratified panel.
  GO   -> STEP 2 (build matched C2 cancel arm; reuse frozen B2-passing resultative ADD
          arm; amended conjecture scope; the add-verbal/cancel-nominal domain mismatch is
          a recorded live caveat on the eventual result).
  NO-GO -> STEP 3 principled-limit closure (M3: triggered ONLY by a measured B2 NO-GO).

HUMAN ANCHOR: none. Within-model feasibility calibration, `internal-contrast-only`; no
human-comparison claim, no human label invented.

Run: python3 build_items.py   (no API; writes + sha256-hashes the frozen CSV)
"""
import csv
import hashlib
import os

# ---------------------------------------------------------------------------
# C2 privative pool: (noun, subject, past_verb, category, privative_modifier)
#   default sentence  = "<Subject> <past_verb> a/an <noun>."
#   category hypothesis = "<Subject> <past_verb> a/an <category>."
#   privative cancel (STEP 2 only) = "<Subject> <past_verb> a/an <privative> <noun>."
# Each is a clean taxonomic (bare noun |= category) entailment, cancellable by a standard
# privative modifier (fake / artificial / toy / imitation / plastic).
PRIVATIVE = [
    ("gun",     "Sam",    "bought",       "weapon",            "fake"),
    ("diamond", "Priya",  "bought",       "gemstone",          "fake"),
    ("rose",    "Jordan", "bought",       "flower",            "artificial"),
    ("tiger",   "Lena",   "saw",          "animal",            "toy"),
    ("apple",   "Omar",   "held",         "fruit",             "plastic"),
    ("pearl",   "Nina",   "wore",         "jewel",             "imitation"),
    ("sword",   "Carlos", "carried",      "weapon",            "toy"),
    ("violin",  "Maria",  "played",       "musical instrument","toy"),
]

VOWELS = "aeiou"


def art(word):
    return "an" if word[0].lower() in VOWELS else "a"


def rows():
    out = []
    for noun, subj, verb, cat, priv in PRIVATIVE:
        sent = f"{subj} {verb} {art(noun)} {noun}."
        hyp = f"{subj} {verb} {art(cat)} {cat}."
        out.append(dict(
            item_id=f"c2cal-{noun}-default", arm="cancel-c2",
            construction="privative", stem=noun, condition="default",
            sentence=sent, nli_hypothesis=hyp,
            nli_gold="0", fc_gold="YES", affirm_correct="1", calib="1",
            privative_modifier=priv))
    return out


def main():
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "data",
        "monotonicity-c2-privative-calibration", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "arm", "construction", "stem", "condition", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct", "calib",
            "privative_modifier"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    nouns = {p[0] for p in PRIVATIVE}
    print(f"wrote {len(rs)} C2 category-default calibration items -> {out}")
    print(f"  nouns ({len(nouns)}): {sorted(nouns)}")
    print(f"  category hypothesis phrasing (frozen): "
          f"'<Subj> <verb> a/an <category>.'")
    print(f"  privative modifiers (STEP 2, held out here): "
          f"{[(p[0], p[4]) for p in PRIVATIVE]}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
