"""Build + freeze the caused-motion NEAR-MISS FORM-CONTROL item set (v2c, 2026-05-30).

Pre-registration (charter s8): EMITS experiments/data/caused-motion-near-miss-v2c/items.csv,
run + committed BEFORE any probe call. This runs the **near-miss form control** arm that the
off-ceiling coercion v2 (design/argument-structure-coercion-v2 s3d) specified and v2/v2b
DEFERRED ("the other deferred arms -- near-miss form controls and multi-step composition --
remain for a later run", coercion-implicit-cue-v2b s Scope). Governed by the SAME ratified
gate (decisions/resolved/cc-v2-difficulty-operationalization: report-the-rate, internal-
contrast-only). **No new decision.** Behavioral NLI + forced-choice, temperature 0, no
logprobs -> existing 3-family panel. Instrument reused verbatim from the caused-motion v1/v2b
harness (NLI 0/1/2; FC "is this statement true: <hyp>" YES/NO/CANT_TELL).

WHY v2c (bound the construction floor)
--------------------------------------
v1 (result/caused-motion-minimal-pair-divergence-v1) found the panel affirms the caused-motion
construction's causation-of-motion entailment onto NON-motion verbs at ceiling (90-100%). v1's
controls were ABSENT-construction (no displacement / other-cause). v2c adds the harder
near-miss: hold the verb + object + displacement OUTCOME roughly constant, and vary only the
FORM between (a) the caused-motion CONSTRUCTION ("Maria sneezed the napkin off the table") and
(b) near-miss frames that report the same verb and the same end-state WITHOUT
construction-licensing the causation -- a coordinated "and" frame and a temporal-sequence
frame. The caused-motion construction ENTAILS that the subject's action caused the object to
move; the near-miss frames leave the causal link open (the displacement could be coincidental).

  DISCRIMINATOR: if the panel affirms "<subj>'s <action> caused <obj> to move" at the SAME
  high rate for the near-miss frames as for the construction, the v1/v2 ceiling is NOT
  construction-specific -- it reflects a looser "verb happened + object ended up displaced ->
  caused it" shape (or a Gricean post-hoc-ergo-propter-hoc default). If affirm drops on the
  near-miss frames, the inference is keyed on the CONSTRUCTION FORM (genuine constructional
  causation), tightening v1's floor.

ARMS (form held-out; difficulty frozen here BEFORE the run)
-----------------------------------------------------------
  cm-construction (d1): the caused-motion construction. "<Subj> <verbed> <obj> <path-PP>."
                        affirm_gold = affirm (the construction entails the causation; v1 anchor).
  near-coord      (d2): coordinated near-miss. "<Subj> <verbed>, and <obj> ended up <endpoint>."
                        Same verb + end-state, NO construction-licensed causation. The causation
                        is NOT entailed (the and-conjunction reports co-occurrence) ->
                        affirm_gold = withhold (entailment-correct: NLI neutral / FC CANT_TELL).
  near-seq        (d3): temporal-sequence near-miss. "<Subj> <verbed>. Moments later, <obj>
                        was <endpoint>." Even weaker causal link -> affirm_gold = withhold.

INDICATOR / READING RULE (RATIFIED report-the-rate; no manufactured pass bar)
  Per arm x model x instrument: affirm-causation rate (FC YES / NLI entailment 0). Headline:
  the CONSTRUCTION-vs-NEAR-MISS GAP (cm-construction affirm minus near-miss affirm) per model
  per instrument -- the internal contrast. A small gap (near-miss affirmed too) is the
  informative partial-null (the ceiling is not construction-specific); a large gap is evidence
  the causation inference is keyed on the construction form. No threshold tuned post-run.

GOLD CONTESTABILITY (disclosed, not retuned): the near-miss "withhold" gold is the strict
ENTAILMENT reading. A Gricean reader may pragmatically infer the sneeze caused the displacement
from the coordinated frame, so a model that AFFIRMS near-miss is not simply "wrong" -- which is
exactly why the headline is the within-item GAP (report-the-rate), not accuracy against the
near-miss gold. The near-miss gold is used only to label the entailment-correct direction.

HUMAN ANCHOR: pending / internal-contrast-only (Option-4 logic, same as v2/v2b). Scivetti has
no near-miss coordinated/sequence coercion items -> no in-repo human norm on the near-miss
arms. The cm-construction arm keeps the v1 phenomenon-level caused-motion anchor
(resource/scivetti-2025-cxnli-dataset). No human label invented. (Tracked by
decisions/open/conflicting-cue-human-anchor.)

Run: python3 build_items.py   (no API; writes the frozen CSV)
"""
import csv
import hashlib
import os

# 8 scenes: NON-motion (bodily / sound / air-displacement) verb whose lexical semantics do
# NOT encode caused motion -> the construction is doing the work. Each tuple:
#   (scene_id, subj, verb_past, gerund, obj, path_pp, endpoint)
# path_pp = the construction's directional ("off the table"); endpoint = the near-miss end-state
# ("off the table" as a state). gerund used in the hypothesis ("<Subj>'s <gerund> caused ...").
# All 8 are CLEAN INANIMATE-PROPULSION scenes (the pre-run critic flagged the earlier
# animate "whistled the dog" [signaling], "clapped the pigeon" [startle], and anomalous
# "laughed the straw" items as heterogeneous causal relations that would muddy the
# "construction affirmed at ceiling" anchor; replaced before the run with light inanimate
# objects + non-motion propulsion verbs so the construction's physical-causation reading is
# uniform). Verb repeats across scenes are fine — all are clean propulsion.
SCENES = [
    ("napkin", "Maria", "sneezed", "sneezing", "the napkin", "off the table", "off the table"),
    ("crumb", "Tom", "coughed", "coughing", "the crumb", "across the table", "across the table"),
    ("dust", "Sam", "blew", "blowing", "the dust", "off the shelf", "off the shelf"),
    ("feather", "Marco", "puffed", "puffing", "the feather", "off his palm", "off his palm"),
    ("wrapper", "Lena", "huffed", "huffing", "the wrapper", "off the tray", "off the tray"),
    ("smoke", "Priya", "fanned", "fanning", "the smoke", "out of the room", "out of the room"),
    ("petal", "Ben", "blew", "blowing", "the petal", "off the railing", "off the railing"),
    ("confetti", "Leo", "puffed", "puffing", "the confetti", "off the desk", "off the desk"),
]

# arm -> (difficulty, affirm_gold). affirm_gold in {"affirm","withhold"} = the entailment-correct
# direction (NLI entailment 0 / FC YES  vs  NLI not-0 / FC not-YES).
ARMS = {"cm-construction": ("1", "affirm"),
        "near-coord": ("2", "withhold"),
        "near-seq": ("3", "withhold")}


def sentence(arm, s):
    _, subj, verb, _g, obj, path, end = s
    if arm == "cm-construction":
        return f"{subj} {verb} {obj} {path}."
    if arm == "near-coord":
        return f"{subj} {verb}, and {obj} ended up {end}."
    if arm == "near-seq":
        return f"{subj} {verb}. Moments later, {obj} was {end}."
    raise ValueError(arm)


def rows():
    out = []
    for s in SCENES:
        scene_id, subj, _v, gerund, obj, _p, _e = s
        hyp = f"{subj}'s {gerund} caused {obj} to move."
        for arm, (diff, gold) in ARMS.items():
            out.append(dict(item_id=f"{arm}-{scene_id}", scene=scene_id, arm=arm,
                            difficulty=diff, sentence=sentence(arm, s),
                            nli_hypothesis=hyp, affirm_gold=gold))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                       "caused-motion-near-miss-v2c", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    # cross-check: every scene appears once per arm; hypothesis identical across arms within scene
    by_scene = {}
    for r in rs:
        by_scene.setdefault(r["scene"], set()).add(r["nli_hypothesis"])
    for sc, hyps in by_scene.items():
        assert len(hyps) == 1, f"{sc}: hypothesis differs across arms ({hyps})"
    cols = ["item_id", "scene", "arm", "difficulty", "sentence", "nli_hypothesis", "affirm_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    from collections import Counter
    by = Counter(r["arm"] for r in rs)
    print(f"wrote {len(rs)} items -> {out}")
    print(f"  arms: {dict(by)}  (8 scenes x 3 forms)")
    print(f"  (hypothesis identical across the 3 forms within each scene -> clean form contrast)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
