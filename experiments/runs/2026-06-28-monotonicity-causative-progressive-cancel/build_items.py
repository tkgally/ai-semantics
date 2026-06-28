"""Build + freeze the CAUSATIVE-INCHOATIVE PROGRESSIVE cancel-suppression CALIBRATION
(2026-06-28, session 140).

The next empirical step named by result/monotonicity-verbal-cancel-survey-v1 (s139) and
open-question/within-verbal-cancel-at-ceiling. The s139 survey B2-confirmed that the
causative-inchoative RESULT-STATE default is held at ceiling (NLI affirm 1.00, 3/3 models:
"Sam broke the vase" |= "The vase broke"). It also identified the causative-inchoative
family as the one B2-passing verbal default that admits a GENUINE same-verb constructional
cancel -- the PROGRESSIVE / imperfective paradox ("Sam was breaking the vase" does NOT
entail "The vase broke"). The standing lesson (s135/C1) is binding: do NOT assume the
construction cancels -- MEASURE it. This probe measures whether the progressive actually
SUPPRESSES the held result entailment, in the matched conflicting-cue paradigm of
result/conative-cancel-direction-v2 (the project's frozen cancel-arm template).

THREE CONDITIONS per verb (verb + object held constant; hypothesis = "The <obj> <inch>."):
  default     (diff 1): "Sam broke the vase."                |= "The vase broke."   YES
                        -- the held lexical default (B2-confirmed at ceiling in s139),
                        the licensing/ceiling anchor (what the construction must suppress).
  progressive (diff 2): "Sam was breaking the vase."         -> suppress? gold NO
                        -- the imperfective paradox: the progressive of a change-of-state
                        verb does NOT entail culmination. LOW affirm = good suppression.
  cue         (diff 3): "Sam was breaking the vase, AND <result consequence>." -> YES
                        -- an explicit real-world consequence that ENTAILS the result
                        occurred WITHOUT echoing the hypothesis verb; a model tracking the
                        result should re-affirm. Mirror of the conative cue arm.

DERIVED (matched to conative-cancel-v2, report-the-rate; NO pass bar tuned after data):
  suppression_no_cue = 100 - progressive_affirm   (construction-following, no cue)
  cue_following      = cue_affirm                  (does the explicit cue re-license?)
  prog_to_cue_shift  = cue_affirm - progressive_affirm

READING (what a clean suppression signal looks like, stated BEFORE the run):
  - default affirm ~ ceiling (re-confirms s139), progressive_affirm meaningfully BELOW it
    (suppression_no_cue > 0), cue re-licensing (cue_affirm > progressive_affirm). This is
    the conative-shaped pattern; on it, the matched within-verbal add-vs-cancel BATTERY can
    be built (frozen resultative ADD arm sha 80bd4b60b55a3e60 + this progressive CANCEL arm),
    read by the frozen s134 thresholds -> the clean within-verbal generalization confirm that
    discharges the M2 domain mismatch.
  - If the progressive does NOT suppress (progressive_affirm stays ~ default, the C1-style
    aspectual-weakness outcome under strict NLI), that is itself the sharpened principled-limit
    finding: held verbal defaults exist (s139) but the panel resists their aspectual cancel.
  This is a CALIBRATION of the cancel arm; it does NOT by itself test the conjecture (no ADD
  arm paired). `internal-contrast-only`; no human anchor, no human-comparison claim.

Verb pool = the 6 s139 B2-confirmed causative-inchoative verbs, SAME subject/object triples
(so the default condition is identical to the s139 default it re-uses):
  break/vase, shatter/window, melt/snowman, tear/page, crack/egg, dissolve/tablet.

Run: python3 build_items.py   (no API; writes + sha256-hashes the frozen CSV)
"""
import csv
import hashlib
import os

# (subject, verb_past, verb_prog, object, inchoative_past, result_consequence)
#   default     = "<Subj> <verb_past> the <obj>."
#   progressive = "<Subj> was <verb_prog> the <obj>."
#   cue         = "<Subj> was <verb_prog> the <obj>, and <result_consequence>."
#   hypothesis (throughout) = "The <obj> <inchoative_past>."
# The cue consequence ENTAILS the result occurred without echoing "<inchoative_past>".
ITEMS = [
    ("Sam",   "broke",     "breaking",     "vase",    "broke",
     "the pieces scattered across the floor"),
    ("Mara",  "shattered",  "shattering",  "window",  "shattered",
     "glass sprayed across the room"),
    ("Devin", "melted",     "melting",     "snowman", "melted",
     "a puddle spread across the lawn"),
    ("Priya", "tore",       "tearing",     "page",    "tore",
     "the two halves came apart in her hands"),
    ("Lena",  "cracked",    "cracking",    "egg",     "cracked",
     "yolk ran down the side of the bowl"),
    ("Omar",  "dissolved",  "dissolving",  "tablet",  "dissolved",
     "the water turned cloudy"),
]


def rows():
    out = []
    for subj, vpast, vprog, obj, inch, cons in ITEMS:
        hyp = f"The {obj} {inch}."
        base = dict(construction="causative-progressive", stem=vpast)
        out.append(dict(item_id=f"cpc-{obj}-default", condition="default", difficulty="1",
                        sentence=f"{subj} {vpast} the {obj}.", nli_hypothesis=hyp,
                        nli_gold="0", fc_gold="YES", **base))
        out.append(dict(item_id=f"cpc-{obj}-progressive", condition="progressive",
                        difficulty="2", sentence=f"{subj} was {vprog} the {obj}.",
                        nli_hypothesis=hyp, nli_gold="1", fc_gold="NO", **base))
        out.append(dict(item_id=f"cpc-{obj}-cue", condition="cue", difficulty="3",
                        sentence=f"{subj} was {vprog} the {obj}, and {cons}.",
                        nli_hypothesis=hyp, nli_gold="0", fc_gold="YES", **base))
    return out


def main():
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "data",
        "monotonicity-causative-progressive-cancel", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "construction", "stem", "condition", "difficulty",
            "sentence", "nli_hypothesis", "nli_gold", "fc_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    print(f"wrote {len(rs)} causative-progressive cancel items ({len(ITEMS)} verbs x 3) -> {out}")
    print(f"  conditions: default (gold YES) / progressive (gold NO=suppress) / cue (gold YES)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
