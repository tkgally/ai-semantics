"""Build + freeze the WITHIN-VERBAL cancel-default B2 CALIBRATION SURVEY
(2026-06-28, session 139).

Path (ii) of open-question/within-verbal-cancel-at-ceiling: a small structured
survey that triages a handful of candidate NEW *verbal* cancel defaults through cheap
B2 default-at-ceiling calibrations, BEFORE any matched asymmetry battery is built. The
binding scarcity the open-question names: a clean within-verbal generalization confirm
of conjecture/constructional-monotonicity-asymmetry needs a *verbal* lexical default
the strict-NLI panel holds as a categorical entailment at ceiling (B2), which a
construction could then be shown to suppress less reliably than a matched verbal ADD arm
accumulates. The two verbal defaults tried so far floored B2:
  - s135 for-durative single-occurrence ("flashed" -> "only once"): 0.00/0.00/0.00 (a
    Gricean quantity IMPLICATURE; structural NO-GO).
  - C1 telic completion ("built the house" -> "finished building it"): 0.25/0.375/0.75
    (a defeasible aspectual default; 0/3 at ceiling).
The only B2-PASSING cancel default to date is NOMINAL (C2 taxonomic "a gun" -> "a
weapon", 1.00/1.00/1.00), forcing the M2 verbal-add/nominal-cancel domain mismatch.

THIS IS A CALIBRATION SURVEY ONLY. It measures, for each candidate verbal family,
whether the DEFAULT entailment is a model-held categorical entailment at the B2 ceiling.
It builds NO cancel arm and runs NO asymmetry battery. The s135/C1 lesson is binding:
do NOT assume a verbal default is at ceiling -- MEASURE it. No human anchor; within-model
feasibility calibration, `internal-contrast-only`; no human-comparison claim invented.

CANDIDATE VERBAL CANCEL-DEFAULT FAMILIES (named in the open-question, plus one):
  A. IMPLICATIVE (open-question names this): a positive implicative matrix verb entails
     its infinitival complement -- "Sam managed to open the door." |= "Sam opened the
     door." Classically near-categorical (Karttunen 1971 implicatives). The eventual
     CANCEL side would be a non-/negative-implicative frame -- whether that is a
     *constructional* add-vs-cancel of the conative type, rather than a lexical-class
     swap, is a DESIGN question, scrutinized in the result, NOT settled here.
  B. FACTIVE (added; same logic): a factive verb entails its that-complement -- "Sam
     realized that the door was open." |= "The door was open." Also classically
     near-categorical. Same downstream cancel-design caveat.
  C. CAUSATIVE-INCHOATIVE / AFFECTED-OBJECT (the open-question's "conative-adjacent
     affected-object family", chosen DISTINCT from the original conative contact-by-motion
     verbs to avoid re-reading the conative): a transitive change-of-state verb entails
     the inchoative result -- "Sam broke the vase." |= "The vase broke." Object-
     affectedness as a held lexical entailment; the natural cancel (imperfective /
     progressive) overlaps C1's aspectual territory, flagged in the result.

WHY THREE FAMILIES, ONE FROZEN SET: the survey's job is to locate which verbal defaults
(if any) the panel holds at ceiling. Implicative + factive are the strongest candidates
for a HELD entailment; the causative-inchoative arm tests whether a *constructionally
cancellable* affected-object default is also held. The per-family B2 gates are computed
independently (analyze_calib.py).

FROZEN B2 GATE per family (NOT relaxable; same bar as C1/C2 STEP 1b):
  default affirm >= 0.80 in >= 2/3 models, strict NLI (NLI primary, label 0 =
  entailment), temperature 0, the ratified panel.
  GATE PER FAMILY -> a family that PASSES is a candidate B2-passing NEW verbal default;
  the result then scrutinizes whether it admits a clean *constructional* cancel (vs a
  lexical swap) and, if so, flags a next-session matched battery (reusing the frozen
  B2-passing resultative ADD arm sha 80bd4b60b55a3e60). A family that FLOORS feeds the
  principled-limit closure. NO gate is relaxed after data.

Run: python3 build_items.py   (no API; writes + sha256-hashes the frozen CSV)
"""
import csv
import hashlib
import os

VOWELS = "aeiou"


def art(word):
    return "an" if word[0].lower() in VOWELS else "a"


# ---------------------------------------------------------------------------
# A. IMPLICATIVE: (subject, matrix_past, complement_infinitive_phrase, complement_past)
#   default  = "<Subj> <matrix_past> to <complement_inf>."
#   hypothesis (held entailment) = "<Subj> <complement_past>."
# Positive implicatives (Karttunen): manage, remember, bother, happen, dare, get.
IMPLICATIVE = [
    ("Sam",   "managed",    "open the door",     "opened the door"),
    ("Mara",  "remembered", "lock the gate",     "locked the gate"),
    ("Devin", "bothered",   "read the contract", "read the contract"),
    ("Priya", "happened",   "meet the senator",  "met the senator"),
    ("Lena",  "dared",      "enter the cave",    "entered the cave"),
    ("Omar",  "got",        "taste the soup",    "tasted the soup"),
]

# ---------------------------------------------------------------------------
# B. FACTIVE: (subject, factive_past, that_clause, hypothesis_clause)
#   default  = "<Subj> <factive_past> that <that_clause>."
#   hypothesis (held entailment) = "<Hypothesis_clause>."  (the complement asserted)
# Factives (presuppose/entail complement): realize, discover, regret, admit, notice, forget.
FACTIVE = [
    ("Sam",   "realized",   "the door was open",        "The door was open."),
    ("Mara",  "discovered", "the safe was empty",        "The safe was empty."),
    ("Devin", "regretted",  "the team had lost",         "The team had lost."),
    ("Priya", "admitted",   "the report was late",       "The report was late."),
    ("Lena",  "noticed",    "the light was on",          "The light was on."),
    ("Omar",  "forgot",     "the store was closed",      "The store was closed."),
]

# ---------------------------------------------------------------------------
# C. CAUSATIVE-INCHOATIVE / AFFECTED-OBJECT: (subject, verb_past, object, inchoative_past)
#   default  = "<Subj> <verb_past> the <object>."
#   hypothesis (held entailment) = "The <object> <inchoative_past>."
# Change-of-state verbs (causative |= inchoative), DISTINCT from conative contact-by-motion.
# Count-noun objects with definite article (avoids mass-noun ungrammaticality).
CAUSATIVE = [
    ("Sam",   "broke",     "vase",    "broke"),
    ("Mara",  "shattered", "window",  "shattered"),
    ("Devin", "melted",    "snowman", "melted"),
    ("Priya", "tore",      "page",    "tore"),
    ("Lena",  "cracked",   "egg",     "cracked"),
    ("Omar",  "dissolved", "tablet",  "dissolved"),
]


def rows():
    out = []
    for subj, matrix, comp_inf, comp_past in IMPLICATIVE:
        out.append(dict(
            item_id=f"vcs-impl-{matrix}", arm="cancel-survey", family="implicative",
            construction="implicative-complement", stem=matrix, condition="default",
            sentence=f"{subj} {matrix} to {comp_inf}.",
            nli_hypothesis=f"{subj} {comp_past}.",
            nli_gold="0", fc_gold="YES", affirm_correct="1", calib="1"))
    for subj, fact, that_cl, hyp in FACTIVE:
        out.append(dict(
            item_id=f"vcs-fact-{fact}", arm="cancel-survey", family="factive",
            construction="factive-complement", stem=fact, condition="default",
            sentence=f"{subj} {fact} that {that_cl}.",
            nli_hypothesis=hyp,
            nli_gold="0", fc_gold="YES", affirm_correct="1", calib="1"))
    for subj, vpast, obj, inch in CAUSATIVE:
        out.append(dict(
            item_id=f"vcs-caus-{vpast}", arm="cancel-survey", family="causative-inchoative",
            construction="causative-inchoative", stem=vpast, condition="default",
            sentence=f"{subj} {vpast} the {obj}.",
            nli_hypothesis=f"The {obj} {inch}.",
            nli_gold="0", fc_gold="YES", affirm_correct="1", calib="1"))
    return out


def main():
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "data",
        "monotonicity-verbal-cancel-survey", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "arm", "family", "construction", "stem", "condition",
            "sentence", "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct", "calib"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    fams = {}
    for r in rs:
        fams.setdefault(r["family"], 0)
        fams[r["family"]] += 1
    print(f"wrote {len(rs)} within-verbal cancel-default calibration items -> {out}")
    for fam, n in sorted(fams.items()):
        print(f"  family {fam}: {n} items")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
