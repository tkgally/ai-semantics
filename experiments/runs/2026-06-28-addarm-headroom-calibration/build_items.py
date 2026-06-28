"""Build + freeze the ADD-ARM HEADROOM CALIBRATION item set (2026-06-28, session 133).

Pre-registration (charter s8): EMITS experiments/data/addarm-headroom-calibration/items.csv,
run + committed BEFORE any probe call, sha256-hashed. This discharges (or fails to
discharge) the s132 KEEP-OPEN BLOCKER on the operationalization decision
(wiki/decisions/open/constructional-monotonicity-generalization-operationalization):
"Demonstrated add-arm headroom on frozen calibration items" -- show, on frozen items
BEFORE any main run, that a genuinely NON-result-entailing control exists and the add
arm has real licensing-no-cue headroom against it -- OR name a cleaner add construction.
The design-level companion is open-question/constructional-monotonicity-addarm-headroom.

WHAT THIS MEASURES (the headroom question, stated sharply)
---------------------------------------------------------
For a candidate ADD construction, the discriminating quantity is the no-cue LICENSING GAP:

  construction arm: "<subj> hammered the metal flat."   -> hyp "The metal became flat."
                    The construction LICENSES the added entailment. Want CEILING affirm.
  control arm     : "<subj> hammered the metal."        -> hyp "The metal became flat."
                    Same verb + arguments, construction REMOVED. Does the bare default
                    already supply the added entailment? Want OFF-CEILING (low) affirm.

  per-verb headroom = construction_affirm - control_affirm.

A verb has REAL headroom only if the construction licenses the entailment (high) AND the
control does NOT already supply it (low). If the control is already at ceiling on the
entailment -- the AANN default-coincidence trap -- the construction's contribution has
nowhere to show, and "add easy" becomes a tautology of the arm construction rather than a
finding (open-question/constructional-monotonicity-addarm-headroom, "Why the resultative
add arm risks degeneracy").

TWO CANDIDATE CONSTRUCTIONS (both flagged live by the s132 feasibility page)
---------------------------------------------------------------------------
- RESULTATIVE: the decision's PROVISIONAL add arm (Option A1 used as A3's new-pair leg),
  flagged AT-RISK / undemonstrated. Verbs span the canonicity spectrum: some manner verbs
  whose bare default plausibly does NOT entail the result (hammer flat, kick open, paint
  white...), some telic verbs whose default plausibly DOES (wipe clean, freeze solid,
  sharpen sharp...). The calibration sorts them empirically.
- INTRANSITIVE-MOTION: a Scivetti construction flagged PLAUSIBLE-BUT-UNVERIFIED. Manner-of-
  motion verb + directional PP adds translational motion (change of location). Verbs span:
  manner verbs with no inherent displacement (spin, float, sway...) vs verbs whose bare
  default already entails displacement (roll, slide, drift). Added entailment phrased
  GENERICALLY ("moved to a different place"), NOT goal-specific, so an off-ceiling control
  reflects the construction's contribution, not an unmentioned goal noun.

FROZEN READING RULE (the headroom gate) -- set HERE, before any data; see PREREG.md.
A verb is HEADROOM-CLEAN if, in the panel aggregate (mean of 3 models, NLI primary):
  construction licensing affirm >= 0.80 (at/near ceiling) AND control default affirm <= 0.40
  (off ceiling; ~chance for a 3-way YES/NO/CANT_TELL, baseline ~0.33).
A CONSTRUCTION DEMONSTRATES HEADROOM if >= 4 of its 12 verbs are headroom-clean in the
panel aggregate AND >= 1 such verb is headroom-clean in >= 2/3 models individually.
Falsify arm is LIVE: if a construction's controls are mostly at ceiling (the degeneracy
worry borne out) it FAILS the gate, recorded as such -- no threshold relaxed after data.

HUMAN ANCHOR: none asserted. This is an INTERNAL design-feasibility calibration -- it
makes NO human-comparison claim (it measures only within-model construction-vs-control
affirm rates to decide whether a future battery's add arm can be built). No human label
invented. (The future battery's anchor posture is the decision's job, not this page's.)

Run: python3 build_items.py   (no API; writes + hashes the frozen CSV)
"""
import csv
import hashlib
import os

# ---------------------------------------------------------------------------
# RESULTATIVE: (verb, past, object, result_adjective)
# result hypothesis = "The <object> became <result_adjective>."
# Verbs chosen to span the control-canonicity spectrum (see module docstring).
# PREDICTED off-ceiling control (manner verb; bare default does NOT entail result):
#   hammer/flat, paint/white, kick/open, push/open, cut/short, beat/stiff,
#   boil/thick, squeeze/dry
# PREDICTED at/near-ceiling control (telic verb; bare default ~entails result -> trap):
#   wipe/clean, scrub/clean, freeze/solid, sharpen/sharp
# The probe SORTS them; predictions are not used in scoring.
RESULTATIVE = [
    ("hammer",  "hammered",  "metal",   "flat"),
    ("paint",   "painted",   "fence",   "white"),
    ("kick",    "kicked",    "door",    "open"),
    ("push",    "pushed",    "gate",    "open"),
    ("cut",     "cut",       "rope",    "short"),
    ("beat",    "beat",      "cream",   "stiff"),
    ("boil",    "boiled",    "sauce",   "thick"),
    ("squeeze", "squeezed",  "sponge",  "dry"),
    ("wipe",    "wiped",     "counter", "clean"),
    ("scrub",   "scrubbed",  "pot",     "clean"),
    ("freeze",  "froze",     "pond",    "solid"),
    ("sharpen", "sharpened", "knife",   "sharp"),
]

# ---------------------------------------------------------------------------
# INTRANSITIVE-MOTION: (verb, past, subject_noun, directional_PP)
# displacement hypothesis = "The <subject_noun> moved to a different place."
# PREDICTED off-ceiling control (manner verb; bare default does NOT entail displacement):
#   spin, float, sway, bob, wobble, swing, twirl, rock, bounce
# PREDICTED at/near-ceiling control (verb default ~entails displacement -> trap):
#   roll, slide, drift
INTRANS_MOTION = [
    ("spin",   "spun",     "coin",    "across the table"),
    ("float",  "floated",  "bottle",  "into the cave"),
    ("sway",   "swayed",   "lantern", "toward the door"),
    ("bob",    "bobbed",   "buoy",    "out past the pier"),
    ("wobble", "wobbled",  "top",     "off the shelf"),
    ("swing",  "swung",    "rope",    "over the fence"),
    ("twirl",  "twirled",  "dancer",  "across the stage"),
    ("rock",   "rocked",   "cradle",  "across the floor"),
    ("bounce", "bounced",  "ball",    "over the wall"),
    ("roll",   "rolled",   "barrel",  "down the hill"),
    ("slide",  "slid",     "puck",    "into the net"),
    ("drift",  "drifted",  "boat",    "toward the rocks"),
]

SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
            "Aisha", "Sam", "Wei", "Dana"]


def rows():
    out, si = [], 0
    # RESULTATIVE: transitive resultative needs a human subject.
    for verb, past, obj, res in RESULTATIVE:
        subj = SUBJECTS[si % len(SUBJECTS)]; si += 1
        obj_np = f"the {obj}"
        hyp = f"The {obj} became {res}."
        # construction arm: licenses the added (result-state) entailment -> want ceiling
        out.append(dict(item_id=f"res-{verb}-construction", construction="resultative",
            stem=verb, condition="construction", difficulty="1",
            sentence=f"{subj} {past} {obj_np} {res}.",
            nli_hypothesis=hyp, nli_gold="0", fc_gold="YES", affirm_correct="1"))
        # control arm: bare transitive, construction removed -> measurement (report-the-rate)
        out.append(dict(item_id=f"res-{verb}-control", construction="resultative",
            stem=verb, condition="control", difficulty="2",
            sentence=f"{subj} {past} {obj_np}.",
            nli_hypothesis=hyp, nli_gold="NA", fc_gold="NA", affirm_correct="NA"))
    # INTRANSITIVE-MOTION: the moving thing is the subject; no separate agent.
    for verb, past, noun, pp in INTRANS_MOTION:
        noun_np = f"The {noun}"
        hyp = f"The {noun} moved to a different place."
        out.append(dict(item_id=f"im-{verb}-construction", construction="intrans-motion",
            stem=verb, condition="construction", difficulty="1",
            sentence=f"{noun_np} {past} {pp}.",
            nli_hypothesis=hyp, nli_gold="0", fc_gold="YES", affirm_correct="1"))
        out.append(dict(item_id=f"im-{verb}-control", construction="intrans-motion",
            stem=verb, condition="control", difficulty="2",
            sentence=f"{noun_np} {past}.",
            nli_hypothesis=hyp, nli_gold="NA", fc_gold="NA", affirm_correct="NA"))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                       "addarm-headroom-calibration", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "construction", "stem", "condition", "difficulty", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    nres = sum(1 for r in rs if r["construction"] == "resultative")
    print(f"wrote {len(rs)} items ({nres} resultative + {len(rs)-nres} intrans-motion) -> {out}")
    print(f"  resultative: {len(RESULTATIVE)} verbs x (construction/control); "
          f"intrans-motion: {len(INTRANS_MOTION)} verbs x (construction/control)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in PREREG + README)")


if __name__ == "__main__":
    main()
