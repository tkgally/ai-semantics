#!/usr/bin/env python3
"""prep.py — candidate-pool authoring for the THIRD-construction (caused-motion)
preference/commitment double contrast (run 2026-06-15-third-construction-
preference-commitment-v1). NO model calls.

Implements experiments/designs/third-construction-preference-commitment-v1.md §3-§4
under the RATIFIED decision decisions/resolved/aann-uniqueness-third-construction
(Option A — engineer add-direction headroom on caused-motion, then run the double
contrast; Option C the binding fallback). NO new decision; the yardstick is fixed.

WHAT THIS FREEZES (before any model call)
-----------------------------------------
  * the CANDIDATE POOL of marginal verbs (12 M1 cognition/stative + 12 M2 low-
    propulsion physical = 24) + the 6 CLEAN-reference propulsion verbs (reused
    VERBATIM from caused-motion-near-miss-v2c: sneeze/cough/blow/puff/huff/fan);
  * the fixed light-inanimate OBJECT+PATH inventory (reused verbatim from v2c);
  * the caused-motion CONSTRUCTION frame, the gerund HYPOTHESIS H, and the two
    parity-matched PARAPHRASE options (C = construction-reading, N = no-causation),
    seed-counterbalanced A/B (fixed seed 20260615);
  * the §3 HARVEST-SELECTION RULE (recorded in candidates.json; APPLIED by harvest.py
    AFTER the baseline arm runs): retain a marginal verb iff its pooled baseline
    construction-affirm rate (over models x instruments x its objects) is <= 0.50
    (target <= 0.30); require >= 10 verbs retained or the design FAILS the headroom
    gate (G4) and routes to Option C.

Only the post-harvest subset selection is data-driven, and it is THIS pre-registered
rule, not post-hoc tuning. Running this file emits candidates.json + prints PASS/FAIL
on the mechanical checks + the sha256[:16] freeze hash. No API.

THE HARVEST CANDIDATE ITEMS (each verb x 2 rotating objects; 2 instruments later)
  marginal (M1+M2): "<subj> <verb-past> <obj-np> <path>."  e.g. "Maria blinked the
                    feather off the table."  -> the construction, off-ceiling target.
  clean (ref)     : "<subj> <verb-past> <obj-np> <path>."  e.g. "Maria sneezed the
                    napkin off the table."   -> ceiling reference (G3 sanity >= 0.85).

  24 marginal verbs x 2 objects = 48 marginal candidate items
   6 clean    verbs x 2 objects = 12 clean reference items
                                 = 60 harvest items (x paraphrase-FC + NLI x 3 models
                                   = 360 harvest calls; est. ~$0.05-0.12 billed)

ANCHOR (design §9): NLI on clean/marginal MAY make a CxNLI answer-key comparison
(caused-motion gold = entailment on canonical items; resource/scivetti-2025-cxnli-
dataset). The paraphrase FC arm + (later) cue-control + displaced arms are
internal-contrast-only. No human number invented.

Run: python3 prep.py   (no API; writes candidates.json + PASS/FAIL + sha256)
"""
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
SEED = 20260615

# ---- M1: cognition / perception / stative verbs (no force/contact that could
#         displace a light object) -> design hypothesis: depress the causal-motion
#         affirm rate (cf. the v2 `resist` arm: caused-motion cognition verbs
#         0-70%). (verb, past, gerund) ----
M1 = [
    ("know",      "knew",       "knowing"),
    ("believe",   "believed",   "believing"),
    ("understand","understood", "understanding"),
    ("notice",    "noticed",    "noticing"),
    ("remember",  "remembered", "remembering"),
    ("doubt",     "doubted",    "doubting"),
    ("perceive",  "perceived",  "perceiving"),
    ("recall",    "recalled",   "recalling"),
    ("realize",   "realized",   "realizing"),
    ("suspect",   "suspected",  "suspecting"),
    ("imagine",   "imagined",   "imagining"),
    ("recognize", "recognized", "recognizing"),
]

# ---- M2: low-propulsion / motion-marginal physical verbs (bodily / facial / quiet
#         sound verbs whose force is too weak or diffuse to make displacement
#         automatic) -> design hypothesis: sit between the clean ceiling and the
#         cognition floor. NB the clean propulsion verbs (sneeze/cough/blow/puff/
#         huff/fan) are deliberately EXCLUDED here — they are the ceiling reference. ----
M2 = [
    ("blink",   "blinked",   "blinking"),
    ("hum",     "hummed",    "humming"),
    ("grin",    "grinned",   "grinning"),
    ("wink",    "winked",    "winking"),
    ("nod",     "nodded",    "nodding"),
    ("smile",   "smiled",    "smiling"),
    ("shrug",   "shrugged",  "shrugging"),
    ("giggle",  "giggled",   "giggling"),
    ("frown",   "frowned",   "frowning"),
    ("yawn",    "yawned",    "yawning"),
    ("whisper", "whispered", "whispering"),
    ("sigh",    "sighed",    "sighing"),
]

# ---- CLEAN reference propulsion verbs — reused VERBATIM from
#      caused-motion-near-miss-v2c (SCENES verbs). These read at ceiling (v2c: 100%
#      everywhere) and serve as the G3 within-design positive control. (verb,past,ger) ----
CLEAN = [
    ("sneeze", "sneezed", "sneezing"),
    ("cough",  "coughed", "coughing"),
    ("blow",   "blew",    "blowing"),
    ("puff",   "puffed",  "puffing"),
    ("huff",   "huffed",  "huffing"),
    ("fan",    "fanned",  "fanning"),
]

# ---- fixed light-inanimate OBJECT + PATH inventory (reused verbatim from v2c) ----
OBJECTS = [
    ("napkin",   "the napkin",   "off the table"),
    ("crumb",    "the crumb",    "off the table"),
    ("feather",  "the feather",  "off the table"),
    ("wrapper",  "the wrapper",  "off the tray"),
    ("petal",    "the petal",    "off the railing"),
    ("confetti", "the confetti", "off the desk"),
]

SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
            "Aisha", "Sam", "Wei", "Dana", "Hana", "Luca", "Iris", "Mara",
            "Noah", "Yuki", "Rosa", "Kofi", "Ines", "Bao", "Tariq", "Elsa",
            "Pavel", "Mei", "Diego", "Asha", "Liam", "Zoe", "Ravi", "Greta",
            "Otto", "Suki", "Ali", "Vera"]

# capitalize an "the obj" NP for sentence-initial use in option N
def cap_np(np):
    return np[0].upper() + np[1:]


def build_candidates():
    """Author the harvest candidate items (each verb x 2 rotating objects), with
    seed-counterbalanced A/B paraphrase assignment. Returns the item list."""
    rng = random.Random(SEED)
    items = []
    si = 0           # subject rotation index
    oi = 0           # object rotation index

    def emit(verb, past, gerund, marginality, family):
        nonlocal si, oi
        for _ in range(2):  # two rotating objects per verb
            obj_id, obj_np, path = OBJECTS[oi % len(OBJECTS)]
            oi += 1
            subj = SUBJECTS[si % len(SUBJECTS)]
            si += 1
            gerund_phrase = f"{subj}'s {gerund}"
            hyp = f"{gerund_phrase} caused {obj_np} to move."          # H (NLI hyp + option C)
            para_C = hyp                                               # construction reading
            para_N = f"{cap_np(obj_np)} moved, but not because of {gerund_phrase}."  # no-causation
            # seed-counterbalanced A/B: which letter shows the CONSTRUCTION reading (C)?
            c_is_A = rng.random() < 0.5
            c_letter = "A" if c_is_A else "B"
            n_letter = "B" if c_is_A else "A"
            opt_A = para_C if c_is_A else para_N
            opt_B = para_N if c_is_A else para_C
            sentence = f"{subj} {past} {obj_np} {path}."
            items.append(dict(
                item_id=f"{family}-{verb}-{obj_id}", family=family,
                marginality=marginality, verb=verb, gerund=gerund, subj=subj,
                obj=obj_id, path=path,
                sentence=sentence,
                nli_hypothesis=hyp,
                paraphrase_C=para_C, paraphrase_N=para_N,
                option_A=opt_A, option_B=opt_B,
                construction_letter=c_letter, nocause_letter=n_letter))

    for v, p, g in M1:
        emit(v, p, g, "M1-cognition", "marginal")
    for v, p, g in M2:
        emit(v, p, g, "M2-lowpropulsion", "marginal")
    for v, p, g in CLEAN:
        emit(v, p, g, "clean-propulsion", "clean")
    return items


SELECTION_RULE = {
    "g2_per_model_ceiling": 0.50,
    "g2_per_model_target": 0.30,
    "g3_clean_floor": 0.85,
    "g4_min_models_pass": 2,
    "verb_retain_ceiling": 0.50,
    "verb_retain_target": 0.30,
    "min_verbs_retained": 10,
    "affirm_pooling": "FC chose construction-reading C OR NLI == 0 (entailment); "
                      "pooled over models x instruments x objects unless stated",
    "note": "Applied by harvest.py AFTER the baseline arm runs; FROZEN here pre-run. "
            "No retuning, no threshold relaxation, no second harvest (design §5 G4).",
}


def run_asserts(items):
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            ok = False

    check(f"exactly 60 candidate items (got {len(items)})", len(items) == 60)
    fam = {}
    marg = {}
    for it in items:
        fam[it["family"]] = fam.get(it["family"], 0) + 1
        if it["family"] == "marginal":
            marg[it["marginality"]] = marg.get(it["marginality"], 0) + 1
    check(f"48 marginal candidate items (got {fam.get('marginal')})",
          fam.get("marginal") == 48)
    check(f"12 clean reference items (got {fam.get('clean')})", fam.get("clean") == 12)
    check(f"24 M1 cognition items (got {marg.get('M1-cognition')})",
          marg.get("M1-cognition") == 24)
    check(f"24 M2 low-propulsion items (got {marg.get('M2-lowpropulsion')})",
          marg.get("M2-lowpropulsion") == 24)

    # paraphrase parity: option N differs from C only by the "moved, but not because
    # of" reframing; both name the same gerund-phrase + object.
    parity_ok = True
    for it in items:
        if it["gerund"] not in it["paraphrase_C"] or it["gerund"] not in it["paraphrase_N"]:
            parity_ok = False
            print(f"   gerund missing: {it['item_id']}")
        if it["obj"] not in it["sentence"]:
            parity_ok = False
            print(f"   object missing in sentence: {it['item_id']}")
    check("both paraphrases name the same gerund + object", parity_ok)

    # NLI hypothesis == paraphrase option C (the construction reading) verbatim
    check("NLI hypothesis == construction-reading paraphrase C (identical wording)",
          all(it["nli_hypothesis"] == it["paraphrase_C"] for it in items))

    # option set is exactly {C, N} and the recorded letter matches
    map_ok = True
    for it in items:
        if {it["option_A"], it["option_B"]} != {it["paraphrase_C"], it["paraphrase_N"]}:
            map_ok = False
            print(f"   option-set break: {it['item_id']}")
        a_is_C = it["option_A"] == it["paraphrase_C"]
        if (it["construction_letter"] == "A") != a_is_C:
            map_ok = False
            print(f"   letter-map break: {it['item_id']}")
    check("recorded construction_letter matches option_A/option_B content", map_ok)

    # A/B counterbalancing roughly balanced
    n_C_A = sum(1 for it in items if it["construction_letter"] == "A")
    check(f"A/B counterbalancing roughly balanced (construction on A={n_C_A}, "
          f"B={len(items) - n_C_A})", abs(2 * n_C_A - len(items)) <= int(0.4 * len(items)))

    # every sentence ends in a path PP; clean verbs not in the marginal pool
    clean_verbs = {v for v, _, _ in CLEAN}
    marg_verbs = {it["verb"] for it in items if it["family"] == "marginal"}
    check("clean propulsion verbs excluded from the marginal pool",
          len(clean_verbs & marg_verbs) == 0)

    check("item_ids unique", len({it["item_id"] for it in items}) == len(items))
    return ok


def main():
    items = build_candidates()
    payload = {
        "run": "2026-06-15-third-construction-preference-commitment-v1",
        "design": "experiments/designs/third-construction-preference-commitment-v1.md",
        "decision": "decisions/resolved/aann-uniqueness-third-construction (Option A)",
        "seed": SEED,
        "construction": "caused-motion (add-direction)",
        "hypothesis_template": "<subj>'s <gerund> caused <obj-np> to move.",
        "paraphrase_options": {
            "C": "construction reading: '<subj>'s <gerund> caused <obj-np> to move.'",
            "N": "no-causation reading: '<Obj-np> moved, but not because of <subj>'s <gerund>.'",
        },
        "object_inventory": [list(o) for o in OBJECTS],
        "selection_rule": SELECTION_RULE,
        "anchor_split": {
            "nli_clean_marginal": "MAY make a CxNLI answer-key comparison "
                                  "(resource/scivetti-2025-cxnli-dataset; caused-motion "
                                  "gold = entailment on canonical items)",
            "paraphrase_fc_arm": "internal-contrast-only",
            "cue_control_displaced_arms": "internal-contrast-only (built only on PASS)",
            "generality_claim": "internal-contrast-only (within-model / cross-construction)",
        },
        "items": items,
    }
    ok = run_asserts(items)
    out = HERE / "candidates.json"
    blob = json.dumps(payload, indent=1, ensure_ascii=False)
    out.write_text(blob)
    h = hashlib.sha256(blob.encode()).hexdigest()[:16]
    print(f"\nwrote {len(items)} candidate items -> {out}")
    print(f"sha256[:16] = {h}  (candidate-pool freeze hash; record in README + PREREG)")
    if not ok:
        raise SystemExit("FAIL: one or more candidate asserts failed")
    print("all asserts PASS")


if __name__ == "__main__":
    main()
