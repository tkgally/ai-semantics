#!/usr/bin/env python3
"""AANN inferential v4 — stimulus authoring (NO model calls).

Authors the frozen items for the inferential probe v4 and writes stimuli.json.
The items are HAND-AUTHORED here (not model-generated). v4's single structural
change from v3 is the CONTROL GEOMETRY: every base item now carries THREE premise
frames so the paraphrase/NLI headline is a DOUBLE contrast (Δ²) that nets out the
imported lexical cue (governing decisions: aann-inferential-default-coincidence
Option A + its six binding conditions; aann-inferential-operationalization's eight
inherited conditions). The three frames:

  1. AANN  — v3's `aann` sentence verbatim (the construction).
              "We spent a beautiful three days in Rome."
  2. DDC   — distributive-default control: an explicitly itemizing premise whose
              baseline reading is genuinely DISTRIBUTIVE, adjective predicated
              per-unit. This is the N1 headroom frame (its baseline unification
              rate must be off-ceiling for the design to have purchase).
              "On each of the three days in Rome, it was beautiful."
  3. LCC   — lexical-cue control: the SAME itemizing cue ("on each of the {num}
              ... {noun}") but with the adjective ATTRIBUTIVE on the plural noun
              and NO AANN — an ordinary plural. The construction-isolating
              control: algebraically Δ² = P(uni|AANN) − P(uni|LCC), so the LCC is
              authored so its ONLY difference from a unification-licensing reading
              is the absence of the AANN construction.
              "On each of the three beautiful days in Rome, we relaxed."

The paraphrase options (unification U / distributive D), the NLI hypotheses, the
agreement sub-probe (AANN vs BARE-PLURAL control, NOT the DDC — binding Condition
N4), and the Tier-0 manipulation check are UNCHANGED from v3 (reused verbatim).
The 23 base items (temporal 13 + distance 10) are the v3 set; the object/mass
class STAYS DROPPED.

Frozen discipline (inherited Condition I8): everything here is fixed before any
model call. This script asserts the mechanical guarantees the design promises:
  - lexical-overlap PARITY between the U and D PARAPHRASE OPTIONS (Condition N3 /
    inherited I2, UNCHANGED): neither option shares more premise content lemmas
    than the other (equal, or within a tolerance of 1, direction recorded);
  - A/B COUNTERBALANCE of the U/D paraphrase order, the was/were order, and the
    Tier-0 AANN position is balanced across items (seeded);
  - EVERY base item carries all THREE premise frames (AANN/DDC/LCC), and the LCC
    carries the DDC's itemizing "on each of … {noun}" cue (the construction-
    isolating guarantee, Condition N2);
  - per-item `control_lexical_delta` (Condition N3): the count of content words
    the DDC adds/removes vs the AANN premise; the LCC carries the same cue.

Run: python3 prep.py   (writes stimuli.json; makes NO network calls)
"""
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).parent
SEED = 20260613
rng = random.Random(SEED)

# ---------------------------------------------------------------------------
# Expert-stipulated key (Condition N5 / inherited I5). The unification reading is
# the AANN-licensed answer. This is the DESIGN AUTHOR'S coding of the published
# AANN semantics — the unification/whole-evaluation analysis the conjecture page
# describes and the constraint literature NAMES (Solt 2007 unit-coercion;
# Dalrymple & King 2019; Bylinina & Nouwen 2018). Those papers are NOT in-repo;
# they are named only as the analyses this stipulation rests on. NO quotes are
# fabricated from them. The key is a SCORING KEY, not a human anchor.
KEY_PROVENANCE = (
    "EXPERT-STIPULATED. The unification/whole-evaluation reading is the "
    "AANN-licensed answer per the design author's coding of the published AANN "
    "semantics (Solt 2007 unit-coercion; Dalrymple & King 2019; Bylinina & "
    "Nouwen 2018 — named as the analyses the stipulation rests on, NOT quoted; "
    "they are not in-repo). This is a scoring key, not a behavioral-human anchor."
)

# Chief-cost statement (verbatim, binding on the result page; v4-adapted per
# Condition N5 — "v3" swapped to "v4").
CHIEF_COST = (
    "The v4 can never say 'models draw the inference the way humans do' — only "
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
    lowercase, strip trailing 's'/'ing'/'ly' so 'days'~'day', 'gruelling'
    stays distinct). Stopwords removed; numerals kept as words."""
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
    premise (symmetric difference of content-lemma sets). Descriptive: it
    quantifies the premise asymmetry the LCC arm neutralizes by carrying the
    same itemizing cue."""
    a, d = content_lemmas(aann), content_lemmas(ddc)
    return len(a ^ d)


# ---------------------------------------------------------------------------
# Paraphrase-option + NLI builders — UNCHANGED from v3 (identical wordings).
# The two paraphrase OPTIONS are presented identically across all three premise
# frames, per the design (§3.1). Parity is between the two OPTIONS, measured
# against the AANN premise, exactly as in v3 (Condition N3 unchanged).
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
# BASE ITEMS. Hand-authored. The 23 v3 items (temporal 13 + distance 10) — same
# AANN sentences, adjectives, numerals, nouns, noun classes, local_fluency, and
# key_disputed flags as v3's RAW_ITEMS. The object/mass class STAYS DROPPED.
#
# Each tuple now adds, BY HAND, the v4 control geometry:
#   pp        — the locative / prepositional tail of the AANN sentence, reused so
#               the DDC and LCC read natural and share the AANN's setting.
#   lcc_verb  — a short main-clause continuation for the LCC (an ordinary plural
#               whose itemizing cue matches the DDC's, with the adjective made
#               ATTRIBUTIVE on the plural noun and NO AANN).
#
# DDC template (distributive-default, adjective predicated PER-UNIT):
#   "On each of the {num} {noun} {pp}, it was {adj}."
# LCC template (same itemizing cue, adjective ATTRIBUTIVE, no AANN, ordinary
#   plural):
#   "On each of the {num} {adj} {noun} {pp}, {lcc_verb}."
#
# Each DDC/LCC was read by hand for naturalness + an unambiguously distributive
# baseline (the "on each of …" frame forces a per-unit reading: it is precisely
# the frame that resists the whole-stretch unification reading). The LCC differs
# from the DDC only in moving the adjective from per-unit predicate to attributive
# modifier and supplying a plural main clause — so the LCC's only difference from
# a unification-licensing reading is the absence of the AANN construction.
#
# fields: adj, num, noun, nounclass, aann, control(bare plural), pp, lcc_verb,
#         local_fluency, key_disputed(reason|None)
# ---------------------------------------------------------------------------

RAW_ITEMS = [
    # ---- temporal ----
    ("beautiful", "three", "days", "temporal",
     "We spent a beautiful three days in Rome.",
     "We spent three beautiful days in Rome.",
     "in Rome", "we relaxed", "neutral", None),
    ("gruelling", "five", "days", "temporal",
     "She endured a gruelling five days at sea.",
     "She endured five gruelling days at sea.",
     "at sea", "she stood her watch", "neutral", None),
    ("glorious", "two", "weeks", "temporal",
     "They had a glorious two weeks on the coast.",
     "They had two glorious weeks on the coast.",
     "on the coast", "they swam", "neutral", None),
    ("miserable", "three", "weeks", "temporal",
     "He survived a miserable three weeks in quarantine.",
     "He survived three miserable weeks in quarantine.",
     "in quarantine", "he waited", "distributive", None),
    ("restful", "four", "months", "temporal",
     "We took a restful four months off work.",
     "We took four restful months off work.",
     "off work", "we read", "neutral", None),
    ("punishing", "six", "months", "temporal",
     "The crew faced a punishing six months of drought.",
     "The crew faced six punishing months of drought.",
     "of drought", "the crew rationed water", "distributive", None),
    ("memorable", "two", "years", "temporal",
     "She had a memorable two years abroad.",
     "She had two memorable years abroad.",
     "abroad", "she studied", "neutral", None),
    ("turbulent", "three", "years", "temporal",
     "The country endured a turbulent three years.",
     "The country endured three turbulent years.",
     "of crisis", "the country struggled", "distributive", None),
    ("sleepless", "three", "hours", "temporal",
     "He passed a sleepless three hours before dawn.",
     "He passed three sleepless hours before dawn.",
     "before dawn", "he paced", "neutral", None),
    ("hectic", "five", "hours", "temporal",
     "We worked a hectic five hours straight.",
     "We worked five hectic hours straight.",
     "at the office", "we took calls", "distributive", None),
    ("blissful", "four", "days", "temporal",
     "We enjoyed a blissful four days by the lake.",
     "We enjoyed four blissful days by the lake.",
     "by the lake", "we fished", "neutral", None),
    ("brutal", "six", "weeks", "temporal",
     "Recruits faced a brutal six weeks of training.",
     "Recruits faced six brutal weeks of training.",
     "of training", "the recruits drilled", "distributive", None),
    ("frantic", "two", "days", "temporal",
     "They had a frantic two days before the launch.",
     "They had two frantic days before the launch.",
     "before the launch", "they rehearsed", "distributive", None),
    # ---- distance ----
    ("scenic", "five", "miles", "distance",
     "We hiked a scenic five miles along the ridge.",
     "We hiked five scenic miles along the ridge.",
     "along the ridge", "we paused", "neutral", None),
    ("gruelling", "ten", "miles", "distance",
     "She ran a gruelling ten miles in the heat.",
     "She ran ten gruelling miles in the heat.",
     "in the heat", "she pushed on", "neutral", None),
    ("muddy", "three", "miles", "distance",
     "They trudged a muddy three miles to the camp.",
     "They trudged three muddy miles to the camp.",
     "to the camp", "they slipped", "distributive", None),
    ("punishing", "twenty", "miles", "distance",
     "He cycled a punishing twenty miles uphill.",
     "He cycled twenty punishing miles uphill.",
     "uphill", "he stood on the pedals", "neutral", None),
    ("breathtaking", "two", "miles", "distance",
     "We drove a breathtaking two miles along the cliff.",
     "We drove two breathtaking miles along the cliff.",
     "along the cliff", "we slowed", "neutral", None),
    ("steep", "four", "miles", "distance",
     "The trail climbed a steep four miles to the pass.",
     "The trail climbed four steep miles to the pass.",
     "to the pass", "the trail switchbacked", "distributive", None),
    ("lonely", "thirty", "yards", "distance",
     "She swam a lonely thirty yards to shore.",
     "She swam thirty lonely yards to shore.",
     "to shore", "she stroked on", "neutral",
     "yard-count items are at the edge of the AANN measure-noun inventory; "
     "Mahowald's distance class centers on miles, so 'yards' coding is less "
     "settled"),
    ("treacherous", "eight", "miles", "distance",
     "We sailed a treacherous eight miles around the headland.",
     "We sailed eight treacherous miles around the headland.",
     "around the headland", "we trimmed the sails", "distributive", None),
    ("dazzling", "seven", "miles", "distance",
     "We skied a dazzling seven miles of fresh powder.",
     "We skied seven dazzling miles of fresh powder.",
     "of fresh powder", "we carved turns", "neutral", None),
    ("relentless", "twelve", "miles", "distance",
     "She marched a relentless twelve miles through the storm.",
     "She marched twelve relentless miles through the storm.",
     "through the storm", "she kept her footing", "distributive", None),
]

# 23 base items: temporal 13, distance 10 (object/mass class stays dropped).
assert len(RAW_ITEMS) == 23, len(RAW_ITEMS)


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
        # paraphrase-option lexical-overlap parity (Condition N3, UNCHANGED):
        # both options measured against the AANN premise.
        ov_u = overlap_count(aann, uni)
        ov_d = overlap_count(aann, dis)
        # per-item control-premise lexical asymmetry (Condition N3): how much the
        # DDC differs lexically from the AANN premise; the LCC carries the same
        # itemizing cue so it neutralizes exactly this asymmetry.
        ctrl_delta = lexical_delta(aann, ddc)
        # seeded counterbalance of the U/D letter and the was/were letter
        fc_letter_uni = "A" if rng.random() < 0.5 else "B"
        agr_letter_was = "A" if rng.random() < 0.5 else "B"
        item = {
            "id": f"v4-{nclass}-{adj}-{num}-{noun}",
            "adj": adj, "num": num, "noun": noun, "nounclass": nclass,
            # ---- THREE premise frames (the v4 double-contrast geometry) ----
            "frames": {
                "aann": aann,             # the construction (verbatim v3)
                "ddc": ddc,               # distributive-default control (N1)
                "lcc": lcc,               # lexical-cue control (N2)
            },
            "aann": aann,                 # kept top-level for compatibility/clarity
            "control_bare_plural": control,  # bare plural — agreement arm only (N4)
            "pp": pp,
            "lcc_verb": lcc_verb,
            # ---- Arm A paraphrase forced choice (same 2 options, all 3 frames)
            "paraphrase_unification": uni,
            "paraphrase_distributive": dis,
            "fc_letter_unification": fc_letter_uni,   # counterbalance (block bias)
            "lexical_overlap": {"unification": ov_u, "distributive": ov_d,
                                "parity_ok": abs(ov_u - ov_d) <= 1,
                                "direction": ("equal" if ov_u == ov_d
                                              else "unification" if ov_u > ov_d
                                              else "distributive")},
            "control_lexical_delta": ctrl_delta,   # Condition N3 (DDC vs AANN)
            # ---- Arm B NLI hypotheses (affirm/withhold), all 3 frames
            "nli": {
                "unification_hyp": NLI_uni(num, noun),
                "whole_eval_hyp": NLI_whole(num, noun, adj),
                "distributive_foil": NLI_distrib(num, noun, adj),
            },
            # ---- Agreement sub-probe (load-bearing; control = BARE PLURAL, N4)
            "agreement": {
                "aann_frame": (f"A {adj} {num} {noun} ___ what we needed."),
                "control_frame": (f"{num.capitalize()} {adj} {noun} ___ what "
                                  f"we needed."),
                "aann_expected": "was",      # singular reflex
                "control_expected": "were",  # plural
                "agr_letter_was": agr_letter_was,  # counterbalance
            },
            "local_fluency": local_fluency,   # which paraphrase is locally fluent
            "expected_inference_key": "unification",  # the AANN-licensed answer
            "key_provenance": "expert-stipulated",
            "key_disputed": bool(disputed),
            "key_dispute_reason": disputed,
        }
        items.append(item)

    # ---- THREE-FRAME presence + LCC-cue assertion (Condition N2, new in v4) ----
    for it in items:
        assert set(it["frames"]) == {"aann", "ddc", "lcc"}, it["id"]
        assert all(it["frames"][f] for f in ("aann", "ddc", "lcc")), it["id"]
        # AANN frame is the verbatim v3 sentence
        assert it["frames"]["aann"] == it["aann"], it["id"]
        # the DDC and LCC both carry the itemizing "on each of the {num} ...
        # {noun}" cue; the LCC carries the SAME cue as the DDC without the AANN.
        cue = f"on each of the {it['num']} "
        assert it["frames"]["ddc"].lower().startswith(cue), it["id"]
        assert it["frames"]["lcc"].lower().startswith(cue), it["id"]
        assert it["noun"] in it["frames"]["ddc"], it["id"]
        assert it["noun"] in it["frames"]["lcc"], it["id"]
        # the LCC has NO AANN ("a {adj} {num} {noun}") span; the DDC has none
        # either (the AANN article+adj+num+plural span is the construction).
        aann_span = f"a {it['adj']} {it['num']} {it['noun']}"
        assert aann_span not in it["frames"]["lcc"].lower(), it["id"]
        assert aann_span not in it["frames"]["ddc"].lower(), it["id"]
        # the LCC carries the adjective ATTRIBUTIVE on the plural noun
        assert f"{it['adj']} {it['noun']}" in it["frames"]["lcc"], it["id"]

    # ---- paraphrase-option lexical-overlap parity assertion (Condition N3) ----
    # SCOPE (carried from v3, S2): the parity check measures how much *premise
    # content* (adjective, numeral, measure noun) each PARAPHRASE OPTION shares
    # with the AANN premise. It DELIBERATELY excludes the unification/distributive
    # contrast vocabulary via STOPWORDS, because those words ARE the manipulation
    # and must not be scored as overlap. Because the U/D templates are parallel by
    # construction, parity holds at equality. The metric is a construction-time
    # guarantee on the OPTIONS — UNCHANGED from v3; the premise asymmetry the v4
    # control geometry introduces is tracked separately by control_lexical_delta
    # and neutralized by the LCC arm.
    bad = [it["id"] for it in items if not it["lexical_overlap"]["parity_ok"]]
    assert not bad, f"paraphrase-option parity violated (|U-D|>1) for: {bad}"

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
    # UNCHANGED from v3: built from the first 6 base AANN sentences (6 x 4 = 24),
    # AANN position counterbalanced.
    tier0 = []
    variants = ["reverse_mods", "no_mod", "no_plural", "no_a"]
    for it in items[:6]:
        adj, num, noun = it["adj"], it["num"], it["noun"]
        wf = it["aann"]            # well-formed AANN
        span = f"a {adj} {num} {noun}"
        edits = {
            "reverse_mods": f"a {num} {adj} {noun}",     # a three beautiful days
            "no_mod":       f"a {num} {noun}",           # a three days
            "no_plural":    f"a {adj} {num} {noun_sg(noun)}",  # a beautiful three day
            "no_a":         f"{adj} {num} {noun}",       # beautiful three days
        }
        assert span in wf, (span, wf)
        for v in variants:
            ill = wf.replace(span, edits[v])
            aann_pos = "A" if rng.random() < 0.5 else "B"  # counterbalanced
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
        "design": "experiments/designs/aann-construction-v4-inferential.md",
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
            "aann": "the construction (verbatim v3 AANN sentence)",
            "ddc": "distributive-default control (N1 headroom frame); "
                   "'On each of the {num} {noun} {pp}, it was {adj}.'",
            "lcc": "lexical-cue control (N2 construction-isolating arm); same "
                   "itemizing cue, attributive adjective, no AANN; "
                   "'On each of the {num} {adj} {noun} {pp}, {verb}.'",
            "agreement_control": "BARE PLURAL (N4) — agreement arm only, NOT the "
                                 "DDC; 'Three beautiful days ___ what we needed.'",
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
    deltas = [it["control_lexical_delta"] for it in out["items"]]
    print(f"  control_lexical_delta (DDC vs AANN): "
          f"min {min(deltas)} / max {max(deltas)} / "
          f"mean {sum(deltas)/len(deltas):.1f}")


if __name__ == "__main__":
    main()
