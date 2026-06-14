#!/usr/bin/env python3
"""AANN inferential v6 — POWERED PANEL REPLICATION of v4 (stimulus authoring; NO
model calls).

v6 in the unified AANN version sequence (v5 was the agreement-reflex
generalization; this is the powered replication of the *inferential* v4 result).
It changes NOTHING about the instrument, the analysis code, or the decision rule
— it reuses the FROZEN v4 design's three-frame double-contrast geometry, the same
paraphrase / NLI / agreement / Tier-0 arms, the same templates, the same
thresholds, and the same verdict map (analyze.py is copied from v4 near-verbatim).
Its ONLY change is the ITEM SET:

  1. WIDER N. 40 hand-authored base items (temporal 20 / distance 20), nearly
     doubling v4's 23 (temporal 13 / distance 10) and REBALANCING the distance
     class (10 -> 20) so the per-class power is symmetric. Powers the "does the
     v4 paraphrase shift hold up?" question and the "does gpt's cross-instrument
     convergence replicate?" question.
  2. FRESH ADJECTIVES (held-out). All 40 adjectives are DISJOINT from v4's 21
     and from the agreement-reflex-v5 probe's 30 — so a positive here is the
     construction generalizing to a fresh, larger adjective inventory, not a
     re-measurement of the same items. (The object/mass noun class stays dropped,
     as in v3/v4.)

Everything else is identical to v4 by design. The three premise frames per item:

  1. AANN  — the construction.  "We spent a magical three days in Venice."
  2. DDC   — distributive-default control (N1 headroom frame): an explicitly
             itemizing premise whose baseline reading is genuinely DISTRIBUTIVE,
             adjective predicated per-unit.
             "On each of the three days in Venice, it was magical."
  3. LCC   — lexical-cue control (N2 construction-isolating arm): the SAME
             itemizing cue but the adjective ATTRIBUTIVE on the plural noun and
             NO AANN — an ordinary plural. Algebraically
             Δ² = P(uni|AANN) − P(uni|LCC).
             "On each of the three magical days in Venice, we wandered."

The paraphrase options (unification U / distributive D), the NLI hypotheses, the
agreement sub-probe (AANN vs BARE-PLURAL control, NOT the DDC — binding Condition
N4), and the Tier-0 manipulation check are UNCHANGED templates (the v4/v3 wordings).

Frozen discipline (inherited Condition I8): everything here is fixed before any
model call. This script asserts the mechanical guarantees the design promises
(identical to v4): paraphrase-option lexical-overlap PARITY (Condition N3), A/B
counterbalance, three-frame presence + LCC-cue (Condition N2), per-item
control_lexical_delta (Condition N3).

Run: python3 prep.py   (writes stimuli.json; makes NO network calls)
"""
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).parent
SEED = 20260614
rng = random.Random(SEED)

# ---------------------------------------------------------------------------
# Expert-stipulated key (Condition N5 / inherited I5) — IDENTICAL to v4. The
# unification reading is the AANN-licensed answer per the design author's coding
# of the published AANN semantics (Solt 2007 unit-coercion; Dalrymple & King
# 2019; Bylinina & Nouwen 2018). Those papers are NOT in-repo; named only as the
# analyses this stipulation rests on. NO quotes are fabricated from them. A
# SCORING KEY, not a human anchor.
KEY_PROVENANCE = (
    "EXPERT-STIPULATED. The unification/whole-evaluation reading is the "
    "AANN-licensed answer per the design author's coding of the published AANN "
    "semantics (Solt 2007 unit-coercion; Dalrymple & King 2019; Bylinina & "
    "Nouwen 2018 — named as the analyses the stipulation rests on, NOT quoted; "
    "they are not in-repo). This is a scoring key, not a behavioral-human anchor."
)

# Chief-cost statement (verbatim, binding on the result page; v6-adapted per
# Condition N5 — "v4" swapped to "v6").
CHIEF_COST = (
    "The v6 can never say 'models draw the inference the way humans do' — only "
    "that the construction shifts inferential behaviour relative to a matched "
    "control, in the direction the published semantics predicts."
)

STOPWORDS = set(
    "a an the and or of in on at to for was were is are be been it its they "
    "them each one single continuous stretch whole individually that this we "
    "i he she his her their there as what we needed which formed taken".split()
)


def content_lemmas(s):
    """Crude content-word set for the lexical-overlap parity check (lemma-ish:
    lowercase, strip trailing 's'/'ing'/'ly'). Stopwords removed; numerals kept.
    IDENTICAL to v4."""
    toks = re.findall(r"[a-z]+", s.lower())
    out = set()
    for t in toks:
        if t in STOPWORDS:
            continue
        lem = t
        if lem.endswith("ly") and len(lem) > 4:
            lem = lem[:-2]
        if lem.endswith("ing") and len(lem) > 5:
            lem = lem[:-3]
        if lem.endswith("s") and len(lem) > 3:
            lem = lem[:-1]
        out.add(lem)
    return out


def overlap_count(premise, paraphrase):
    return len(content_lemmas(premise) & content_lemmas(paraphrase))


def lexical_delta(aann, ddc):
    """Condition N3: count of content lemmas the DDC adds/removes vs the AANN
    premise (symmetric difference). Descriptive. IDENTICAL to v4."""
    a, d = content_lemmas(aann), content_lemmas(ddc)
    return len(a ^ d)


# ---------------------------------------------------------------------------
# Paraphrase-option + NLI builders — IDENTICAL templates to v4/v3 (same wordings).
# ---------------------------------------------------------------------------

def U(num, noun, adj):
    return (f"The {num} {noun} formed one continuous stretch, "
            f"{adj} as a whole.")


def D(num, noun, adj):
    return (f"Each of the {num} {noun} was individually {adj}.")


def NLI_uni(num, noun):
    return f"The {num} {noun} were a single continuous stretch."


def NLI_whole(num, noun, adj):
    return f"The stretch as a whole was {adj}."


def NLI_distrib(num, noun, adj):
    return f"Each {noun_sg(noun)} individually was {adj}."


def noun_sg(noun):
    return {"days": "day", "hours": "hour", "weeks": "week", "months": "month",
            "years": "year", "miles": "mile", "yards": "yard", "pounds": "pound",
            "dollars": "dollar", "acres": "acre", "kilos": "kilo"}.get(noun, noun)


# ---------------------------------------------------------------------------
# BASE ITEMS. Hand-authored. 40 FRESH items (temporal 20 + distance 20). All 40
# adjectives are consonant-initial (so the AANN "a" article reads naturally, as
# in v4) and DISJOINT from v4's 21 adjectives and the agreement-reflex-v5
# probe's 30 adjectives. The object/mass class stays dropped.
#
# fields: adj, num, noun, nounclass, aann, control(bare plural), pp, lcc_verb,
#         local_fluency, key_disputed(reason|None)
# DDC template: "On each of the {num} {noun} {pp}, it was {adj}."
# LCC template: "On each of the {num} {adj} {noun} {pp}, {lcc_verb}."
# Each DDC/LCC read by hand for naturalness + an unambiguously distributive
# baseline ("on each of …" forces per-unit reading); the LCC differs from the
# DDC only by making the adjective attributive + supplying a plural main clause,
# so its only difference from a unification-licensing reading is the absence of
# the AANN construction. Adjectives are evaluatively-loaded; items where
# world-knowledge ALONE forces unification were excluded at authoring.
# ---------------------------------------------------------------------------

RAW_ITEMS = [
    # ---- temporal (20) ----
    ("magical", "three", "days", "temporal",
     "We spent a magical three days in Venice.",
     "We spent three magical days in Venice.",
     "in Venice", "we wandered", "neutral", None),
    ("dreadful", "four", "days", "temporal",
     "He endured a dreadful four days in hospital.",
     "He endured four dreadful days in hospital.",
     "in hospital", "he lay still", "distributive", None),
    ("splendid", "two", "weeks", "temporal",
     "They had a splendid two weeks in Provence.",
     "They had two splendid weeks in Provence.",
     "in Provence", "they painted", "neutral", None),
    ("dreary", "five", "days", "temporal",
     "She passed a dreary five days indoors.",
     "She passed five dreary days indoors.",
     "indoors", "she read", "distributive", None),
    ("peaceful", "four", "days", "temporal",
     "We enjoyed a peaceful four days by the river.",
     "We enjoyed four peaceful days by the river.",
     "by the river", "we dozed", "neutral", None),
    ("stressful", "three", "weeks", "temporal",
     "He worked a stressful three weeks before the merger.",
     "He worked three stressful weeks before the merger.",
     "before the merger", "he stayed late", "distributive", None),
    ("golden", "two", "years", "temporal",
     "They had a golden two years in the sun.",
     "They had two golden years in the sun.",
     "in the sun", "they prospered", "neutral", None),
    ("bleak", "six", "months", "temporal",
     "We faced a bleak six months of winter.",
     "We faced six bleak months of winter.",
     "of winter", "we huddled inside", "distributive", None),
    ("hellish", "three", "days", "temporal",
     "She survived a hellish three days in transit.",
     "She survived three hellish days in transit.",
     "in transit", "she waited", "distributive", None),
    ("delightful", "two", "weeks", "temporal",
     "We had a delightful two weeks on the farm.",
     "We had two delightful weeks on the farm.",
     "on the farm", "we baked bread", "neutral", None),
    ("tense", "five", "hours", "temporal",
     "They endured a tense five hours of talks.",
     "They endured five tense hours of talks.",
     "of talks", "they negotiated", "distributive", None),
    ("sombre", "three", "days", "temporal",
     "He spent a sombre three days in mourning.",
     "He spent three sombre days in mourning.",
     "in mourning", "he grieved", "distributive", None),
    ("carefree", "four", "days", "temporal",
     "We had a carefree four days at the beach.",
     "We had four carefree days at the beach.",
     "at the beach", "we swam", "neutral", None),
    ("lively", "three", "weeks", "temporal",
     "We had a lively three weeks on tour.",
     "We had three lively weeks on tour.",
     "on tour", "we performed", "neutral", None),
    ("draining", "six", "weeks", "temporal",
     "He had a draining six weeks of treatment.",
     "He had six draining weeks of treatment.",
     "of treatment", "he rested", "distributive", None),
    ("restorative", "two", "weeks", "temporal",
     "We took a restorative two weeks in the mountains.",
     "We took two restorative weeks in the mountains.",
     "in the mountains", "we hiked", "neutral", None),
    ("monotonous", "four", "months", "temporal",
     "They endured a monotonous four months at the outpost.",
     "They endured four monotonous months at the outpost.",
     "at the outpost", "they drilled", "distributive", None),
    ("cheerful", "three", "days", "temporal",
     "We spent a cheerful three days at the fair.",
     "We spent three cheerful days at the fair.",
     "at the fair", "we played games", "neutral", None),
    ("gloomy", "five", "days", "temporal",
     "He passed a gloomy five days in the rain.",
     "He passed five gloomy days in the rain.",
     "in the rain", "he sulked", "distributive", None),
    ("blessed", "two", "weeks", "temporal",
     "They had a blessed two weeks of calm.",
     "They had two blessed weeks of calm.",
     "of calm", "they gave thanks", "neutral", None),
    # ---- distance (20) ----
    ("picturesque", "six", "miles", "distance",
     "We hiked a picturesque six miles along the coast.",
     "We hiked six picturesque miles along the coast.",
     "along the coast", "we paused for photos", "neutral", None),
    ("savage", "two", "miles", "distance",
     "They climbed a savage two miles to the summit.",
     "They climbed two savage miles to the summit.",
     "to the summit", "they roped up", "distributive", None),
    ("windswept", "four", "miles", "distance",
     "We walked a windswept four miles along the cliffs.",
     "We walked four windswept miles along the cliffs.",
     "along the cliffs", "we leaned into the gale", "distributive", None),
    ("desolate", "ten", "miles", "distance",
     "She drove a desolate ten miles across the plain.",
     "She drove ten desolate miles across the plain.",
     "across the plain", "she saw no one", "neutral", None),
    ("rough", "eight", "miles", "distance",
     "We sailed a rough eight miles to the harbour.",
     "We sailed eight rough miles to the harbour.",
     "to the harbour", "we held on", "distributive", None),
    ("taxing", "twelve", "miles", "distance",
     "He trudged a taxing twelve miles home.",
     "He trudged twelve taxing miles home.",
     "home", "he limped", "distributive", None),
    ("stunning", "five", "miles", "distance",
     "We drove a stunning five miles through the canyon.",
     "We drove five stunning miles through the canyon.",
     "through the canyon", "we gazed out", "neutral", None),
    ("blistering", "six", "miles", "distance",
     "She ran a blistering six miles in the heat.",
     "She ran six blistering miles in the heat.",
     "in the heat", "she gasped", "distributive", None),
    ("gorgeous", "seven", "miles", "distance",
     "We cycled a gorgeous seven miles by the vineyards.",
     "We cycled seven gorgeous miles by the vineyards.",
     "by the vineyards", "we coasted", "neutral", None),
    ("backbreaking", "three", "miles", "distance",
     "They hauled the gear a backbreaking three miles uphill.",
     "They hauled the gear three backbreaking miles uphill.",
     "uphill", "they strained", "distributive", None),
    ("hazardous", "four", "miles", "distance",
     "We crossed a hazardous four miles of ice.",
     "We crossed four hazardous miles of ice.",
     "of ice", "we roped together", "distributive", None),
    ("sandy", "five", "miles", "distance",
     "We slogged a sandy five miles down the beach.",
     "We slogged five sandy miles down the beach.",
     "down the beach", "we sank with each step", "distributive", None),
    ("verdant", "two", "miles", "distance",
     "We strolled a verdant two miles through the valley.",
     "We strolled two verdant miles through the valley.",
     "through the valley", "we admired the green", "neutral", None),
    ("pristine", "six", "miles", "distance",
     "We skied a pristine six miles of backcountry.",
     "We skied six pristine miles of backcountry.",
     "of backcountry", "we cut fresh tracks", "neutral", None),
    ("bumpy", "nine", "miles", "distance",
     "We rode a bumpy nine miles on the dirt track.",
     "We rode nine bumpy miles on the dirt track.",
     "on the dirt track", "we jolted along", "distributive", None),
    ("majestic", "eight", "miles", "distance",
     "We hiked a majestic eight miles below the peaks.",
     "We hiked eight majestic miles below the peaks.",
     "below the peaks", "we stopped often", "neutral", None),
    ("freezing", "forty", "yards", "distance",
     "She swam a freezing forty yards to the boat.",
     "She swam forty freezing yards to the boat.",
     "to the boat", "she gasped at the cold", "distributive",
     "yard-count items are at the edge of the AANN measure-noun inventory; "
     "Mahowald's distance class centers on miles, so 'yards' coding is less "
     "settled"),
    ("vertiginous", "three", "miles", "distance",
     "We climbed a vertiginous three miles up the face.",
     "We climbed three vertiginous miles up the face.",
     "up the face", "we clung to the rock", "distributive", None),
    ("lush", "four", "miles", "distance",
     "We wandered a lush four miles through the rainforest.",
     "We wandered four lush miles through the rainforest.",
     "through the rainforest", "we heard birdsong", "neutral", None),
    ("sodden", "five", "miles", "distance",
     "We waded a sodden five miles through the marsh.",
     "We waded five sodden miles through the marsh.",
     "through the marsh", "we were soaked", "distributive", None),
]

# 40 base items: temporal 20, distance 20 (object/mass class stays dropped).
assert len(RAW_ITEMS) == 40, len(RAW_ITEMS)


def DDC(num, noun, adj, pp):
    """Distributive-default control: adjective predicated PER-UNIT under an
    explicitly itemizing 'on each of …' frame whose baseline is distributive."""
    return f"On each of the {num} {noun} {pp}, it was {adj}.".replace("  ", " ")


def LCC(num, noun, adj, pp, lcc_verb):
    """Lexical-cue control: same itemizing 'on each of …' cue, adjective
    ATTRIBUTIVE on the plural noun, NO AANN, ordinary plural main clause."""
    return (f"On each of the {num} {adj} {noun} {pp}, "
            f"{lcc_verb}.").replace("  ", " ")


def build():
    items = []
    for (adj, num, noun, nclass, aann, control, pp, lcc_verb,
         local_fluency, disputed) in RAW_ITEMS:
        uni = U(num, noun, adj)
        dis = D(num, noun, adj)
        ddc = DDC(num, noun, adj, pp)
        lcc = LCC(num, noun, adj, pp, lcc_verb)
        ov_u = overlap_count(aann, uni)
        ov_d = overlap_count(aann, dis)
        ctrl_delta = lexical_delta(aann, ddc)
        fc_letter_uni = "A" if rng.random() < 0.5 else "B"
        agr_letter_was = "A" if rng.random() < 0.5 else "B"
        item = {
            "id": f"v6-{nclass}-{adj}-{num}-{noun}",
            "adj": adj, "num": num, "noun": noun, "nounclass": nclass,
            "frames": {"aann": aann, "ddc": ddc, "lcc": lcc},
            "aann": aann,
            "control_bare_plural": control,  # bare plural — agreement arm only (N4)
            "pp": pp,
            "lcc_verb": lcc_verb,
            "paraphrase_unification": uni,
            "paraphrase_distributive": dis,
            "fc_letter_unification": fc_letter_uni,
            "lexical_overlap": {"unification": ov_u, "distributive": ov_d,
                                "parity_ok": abs(ov_u - ov_d) <= 1,
                                "direction": ("equal" if ov_u == ov_d
                                              else "unification" if ov_u > ov_d
                                              else "distributive")},
            "control_lexical_delta": ctrl_delta,
            "nli": {
                "unification_hyp": NLI_uni(num, noun),
                "whole_eval_hyp": NLI_whole(num, noun, adj),
                "distributive_foil": NLI_distrib(num, noun, adj),
            },
            "agreement": {
                "aann_frame": (f"A {adj} {num} {noun} ___ what we needed."),
                "control_frame": (f"{num.capitalize()} {adj} {noun} ___ what "
                                  f"we needed."),
                "aann_expected": "was",
                "control_expected": "were",
                "agr_letter_was": agr_letter_was,
            },
            "local_fluency": local_fluency,
            "expected_inference_key": "unification",
            "key_provenance": "expert-stipulated",
            "key_disputed": bool(disputed),
            "key_dispute_reason": disputed,
        }
        items.append(item)

    # ---- THREE-FRAME presence + LCC-cue assertion (Condition N2) ----
    for it in items:
        assert set(it["frames"]) == {"aann", "ddc", "lcc"}, it["id"]
        assert all(it["frames"][f] for f in ("aann", "ddc", "lcc")), it["id"]
        assert it["frames"]["aann"] == it["aann"], it["id"]
        cue = f"on each of the {it['num']} "
        assert it["frames"]["ddc"].lower().startswith(cue), it["id"]
        assert it["frames"]["lcc"].lower().startswith(cue), it["id"]
        assert it["noun"] in it["frames"]["ddc"], it["id"]
        assert it["noun"] in it["frames"]["lcc"], it["id"]
        aann_span = f"a {it['adj']} {it['num']} {it['noun']}"
        assert aann_span not in it["frames"]["lcc"].lower(), it["id"]
        assert aann_span not in it["frames"]["ddc"].lower(), it["id"]
        assert f"{it['adj']} {it['noun']}" in it["frames"]["lcc"], it["id"]
        # the AANN premise literally carries the construction span (also the
        # Tier-0 builder relies on this for the first 6 items)
        assert aann_span in it["aann"].lower(), it["id"]

    # ---- paraphrase-option lexical-overlap parity assertion (Condition N3) ----
    bad = [it["id"] for it in items if not it["lexical_overlap"]["parity_ok"]]
    assert not bad, f"paraphrase-option parity violated (|U-D|>1) for: {bad}"

    # ---- adjective freshness assertion (the v6 held-out guarantee) ----
    adjs = [it["adj"] for it in items]
    assert len(set(adjs)) == len(adjs), "duplicate adjective in v6 set"
    V4_ADJS = {"beautiful", "blissful", "breathtaking", "brutal", "dazzling",
               "frantic", "glorious", "gruelling", "hectic", "lonely",
               "memorable", "miserable", "muddy", "punishing", "relentless",
               "restful", "scenic", "sleepless", "steep", "treacherous",
               "turbulent"}
    V5_REFLEX_ADJS = {"agonising", "arduous", "boggy", "chaotic", "craggy",
                      "dismal", "dusty", "exhausting", "festive", "frigid",
                      "grim", "gritty", "harrowing", "idyllic", "jagged",
                      "joyful", "jubilant", "marshy", "perilous", "productive",
                      "rewarding", "rocky", "rugged", "serene", "slick",
                      "snowy", "sweltering", "tedious", "winding", "wretched"}
    clash = set(adjs) & (V4_ADJS | V5_REFLEX_ADJS)
    assert not clash, f"v6 adjectives must be held-out; clash: {sorted(clash)}"
    # all consonant-initial (so the AANN "a" article reads naturally)
    vowel_initial = [a for a in adjs if a[0] in "aeiou"]
    assert not vowel_initial, f"vowel-initial adjective(s): {vowel_initial}"

    # ---- counterbalance balance assertion (block position bias) ----
    n_u_is_a = sum(1 for it in items if it["fc_letter_unification"] == "A")
    n_was_is_a = sum(1 for it in items
                     if it["agreement"]["agr_letter_was"] == "A")
    half = len(items) / 2
    tol = max(5, round(len(items) * 0.25))
    assert abs(n_u_is_a - half) <= tol, n_u_is_a
    assert abs(n_was_is_a - half) <= tol, n_was_is_a

    # ---- under-pressure subset (inherited Condition I4) ----
    under_pressure = [it["id"] for it in items
                      if it["local_fluency"] == "distributive"]
    assert len(under_pressure) >= 6, len(under_pressure)

    # ---- disputed-coding subset (inherited Condition I6) ----
    disputed_ids = [it["id"] for it in items if it["key_disputed"]]

    # ---- Tier-0 pairs: well-formed AANN vs 4 Mahowald degenerate variants ----
    # UNCHANGED builder: first 6 base AANN sentences (6 x 4 = 24), counterbalanced.
    tier0 = []
    variants = ["reverse_mods", "no_mod", "no_plural", "no_a"]
    for it in items[:6]:
        adj, num, noun = it["adj"], it["num"], it["noun"]
        wf = it["aann"]
        span = f"a {adj} {num} {noun}"
        edits = {
            "reverse_mods": f"a {num} {adj} {noun}",
            "no_mod":       f"a {num} {noun}",
            "no_plural":    f"a {adj} {num} {noun_sg(noun)}",
            "no_a":         f"{adj} {num} {noun}",
        }
        assert span in wf, (span, wf)
        for v in variants:
            ill = wf.replace(span, edits[v])
            aann_pos = "A" if rng.random() < 0.5 else "B"
            pair = {"id": f"tier0-{adj}-{num}-{noun}-{v}", "contrast": v,
                    "aann_position": aann_pos}
            if aann_pos == "A":
                pair["A"], pair["B"] = wf, ill
            else:
                pair["A"], pair["B"] = ill, wf
            tier0.append(pair)
    assert len(tier0) == 24, len(tier0)

    n_t0_aann_a = sum(1 for p in tier0 if p["aann_position"] == "A")

    out = {
        "seed": SEED,
        "design": "experiments/designs/aann-construction-v6-inferential.md",
        "replication_of": "experiments/runs/2026-06-13-aann-inferential-v4",
        "governing_decisions": [
            "wiki/decisions/resolved/aann-inferential-default-coincidence.md",
            "wiki/decisions/resolved/aann-inferential-operationalization.md",
        ],
        "anchor": "internal-contrast-only",
        "chief_cost_statement": CHIEF_COST,
        "expected_inference_key_provenance": KEY_PROVENANCE,
        "primary_instrument": "A (paraphrase forced-choice)",
        "convergent_instrument": "B (entailment NLI)",
        "load_bearing_discriminator": "agreement (was/were) sub-probe",
        "frame_inventory": {
            "aann": "the construction (the AANN sentence)",
            "ddc": "distributive-default control (N1 headroom frame); "
                   "'On each of the {num} {noun} {pp}, it was {adj}.'",
            "lcc": "lexical-cue control (N2 construction-isolating arm); same "
                   "itemizing cue, attributive adjective, no AANN; "
                   "'On each of the {num} {adj} {noun} {pp}, {verb}.'",
            "agreement_control": "BARE PLURAL (N4) — agreement arm only, NOT the "
                                 "DDC; 'Three magical days ___ what we needed.'",
        },
        "headline_statistic": "double-contrast Delta^2 = P(uni|AANN) - P(uni|LCC) "
                              "= (AANN shift) - (lexical-cue shift)",
        "noun_classes": sorted({it["nounclass"] for it in items}),
        "counts": {
            "base_items": len(items),
            "by_nounclass": {c: sum(1 for it in items if it["nounclass"] == c)
                             for c in sorted({it["nounclass"] for it in items})},
            "frames_per_item": 3,
            "under_pressure_distributive": len(under_pressure),
            "key_disputed": len(disputed_ids),
            "tier0_pairs": len(tier0),
            "fc_unification_letter_A": n_u_is_a,
            "agr_was_letter_A": n_was_is_a,
            "tier0_aann_letter_A": n_t0_aann_a,
        },
        "under_pressure_ids": under_pressure,
        "key_disputed_ids": disputed_ids,
        "items": items,
        "tier0": tier0,
    }
    return out


def main():
    out = build()
    (HERE / "stimuli.json").write_text(json.dumps(out, indent=1))
    c = out["counts"]
    print("wrote stimuli.json (NO model calls)")
    print(f"  base items: {c['base_items']}  by class: {c['by_nounclass']}")
    print(f"  frames per item: {c['frames_per_item']} (aann / ddc / lcc)")
    print(f"  under-pressure (distributive locally-fluent): "
          f"{c['under_pressure_distributive']}")
    print(f"  key-disputed (item-level flags): {c['key_disputed']} "
          f"-> {out['key_disputed_ids']}")
    print(f"  tier0 pairs: {c['tier0_pairs']}")
    print(f"  counterbalance: U-letter=A on {c['fc_unification_letter_A']}"
          f"/{c['base_items']}; was-letter=A on {c['agr_was_letter_A']}"
          f"/{c['base_items']}; tier0-AANN=A on {c['tier0_aann_letter_A']}/24")
    print("  paraphrase-option parity: PASS (asserted)")
    print("  three-frame presence + LCC-cue: PASS (asserted)")
    print("  adjective held-out (vs v4 + reflex-v5) + consonant-initial: PASS")
    deltas = [it["control_lexical_delta"] for it in out["items"]]
    print(f"  control_lexical_delta (DDC vs AANN): "
          f"min {min(deltas)} / max {max(deltas)} / "
          f"mean {sum(deltas)/len(deltas):.1f}")


if __name__ == "__main__":
    main()
