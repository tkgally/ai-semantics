#!/usr/bin/env python3
"""AANN inferential v3 — stimulus authoring (NO model calls).

Authors the frozen items for the inferential probe and writes stimuli.json.
The items are HAND-AUTHORED here (not model-generated): each base item carries
its AANN sentence, its lexically-matched non-AANN control, the unification (U) /
distributive (D) paraphrase pair, the NLI hypotheses, the was/were agreement
pair, the noun class, the per-item local-fluency direction, the EXPERT-STIPULATED
expected-inference key, and any item-level literature-dispute flag. The Tier-0
forced-choice pairs (well-formed vs the 4 Mahowald degenerate variants) are built
mechanically from the base AANN frames.

Frozen discipline (Condition 8): everything here is fixed before any model call.
This script asserts the two mechanical guarantees the design promises:
  - lexical-overlap PARITY between U and D paraphrases (Condition 2): neither
    paraphrase shares more premise content lemmas than the other (equal, or
    within a tolerance of 1 with the direction recorded);
  - A/B COUNTERBALANCE of the U/D paraphrase order and of the was/were order is
    balanced across items (seeded), to block position bias.

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
# Expert-stipulated key (Condition 5/6). The unification reading is the
# AANN-licensed answer. This is the DESIGN AUTHOR'S coding of the published AANN
# semantics — the unification/whole-evaluation analysis the conjecture page
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

CHIEF_COST = (
    "The v3 can never say 'models draw the inference the way humans do' — only "
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


# ---------------------------------------------------------------------------
# BASE ITEMS. Hand-authored. Each tuple:
#   id, adj, num, noun, nounclass, aann, control, U-paraphrase, D-paraphrase,
#   nli_premise_subject_aann, nli_premise_subject_control,
#   agr_aann, agr_control, local_fluency, key_disputed(reason|None)
# Adjectives kept evaluatively-loaded (the construction's semantics is partly
# evaluative). Items where world-knowledge ALONE forces unification are avoided.
# nounclass in {temporal, distance, object} (Mahowald measure-noun classes).
#
# The U and D paraphrases are written to keep premise content-lemma overlap
# EQUAL (parity asserted below). Both describe the same numeral+noun, differing
# only in unification ("one continuous stretch, ... as a whole") vs distributive
# ("each ... individually"); the evaluative adjective appears in BOTH.
# ---------------------------------------------------------------------------

# helper builders keep U/D wording templates parallel so overlap parity holds
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
            "years": "year", "miles": "mile", "yards": "yards", "pounds": "pound",
            "dollars": "dollar", "acres": "acre", "kilos": "kilo"}.get(noun, noun)


RAW_ITEMS = [
    # ---- temporal ----
    ("beautiful", "three", "days", "temporal",
     "We spent a beautiful three days in Rome.",
     "We spent three beautiful days in Rome.", "neutral", None),
    ("gruelling", "five", "days", "temporal",
     "She endured a gruelling five days at sea.",
     "She endured five gruelling days at sea.", "neutral", None),
    ("glorious", "two", "weeks", "temporal",
     "They had a glorious two weeks on the coast.",
     "They had two glorious weeks on the coast.", "neutral", None),
    ("miserable", "three", "weeks", "temporal",
     "He survived a miserable three weeks in quarantine.",
     "He survived three miserable weeks in quarantine.", "distributive", None),
    ("restful", "four", "months", "temporal",
     "We took a restful four months off work.",
     "We took four restful months off work.", "neutral", None),
    ("punishing", "six", "months", "temporal",
     "The crew faced a punishing six months of drought.",
     "The crew faced six punishing months of drought.", "distributive", None),
    ("memorable", "two", "years", "temporal",
     "She had a memorable two years abroad.",
     "She had two memorable years abroad.", "neutral", None),
    ("turbulent", "three", "years", "temporal",
     "The country endured a turbulent three years.",
     "The country endured three turbulent years.", "distributive", None),
    ("sleepless", "three", "hours", "temporal",
     "He passed a sleepless three hours before dawn.",
     "He passed three sleepless hours before dawn.", "neutral", None),
    ("hectic", "five", "hours", "temporal",
     "We worked a hectic five hours straight.",
     "We worked five hectic hours straight.", "distributive", None),
    # ---- distance ----
    ("scenic", "five", "miles", "distance",
     "We hiked a scenic five miles along the ridge.",
     "We hiked five scenic miles along the ridge.", "neutral", None),
    ("gruelling", "ten", "miles", "distance",
     "She ran a gruelling ten miles in the heat.",
     "She ran ten gruelling miles in the heat.", "neutral", None),
    ("muddy", "three", "miles", "distance",
     "They trudged a muddy three miles to the camp.",
     "They trudged three muddy miles to the camp.", "distributive", None),
    ("punishing", "twenty", "miles", "distance",
     "He cycled a punishing twenty miles uphill.",
     "He cycled twenty punishing miles uphill.", "neutral", None),
    ("breathtaking", "two", "miles", "distance",
     "We drove a breathtaking two miles along the cliff.",
     "We drove two breathtaking miles along the cliff.", "neutral", None),
    ("steep", "four", "miles", "distance",
     "The trail climbed a steep four miles to the pass.",
     "The trail climbed four steep miles to the pass.", "distributive", None),
    ("lonely", "thirty", "yards", "distance",
     "She swam a lonely thirty yards to shore.",
     "She swam thirty lonely yards to shore.", "neutral",
     "yard-count items are at the edge of the AANN measure-noun inventory; "
     "Mahowald's distance class centers on miles, so 'yards' coding is less "
     "settled"),
    ("treacherous", "eight", "miles", "distance",
     "We sailed a treacherous eight miles around the headland.",
     "We sailed eight treacherous miles around the headland.", "distributive", None),
    # ---- object / measure ----
    ("remarkable", "thirty", "pounds", "object",
     "He lost a remarkable thirty pounds last year.",
     "He lost thirty remarkable pounds last year.", "neutral",
     "weight-loss 'pounds' is a canonical AANN object-measure case, but the "
     "control 'thirty remarkable pounds' is itself marginal, so the control "
     "baseline is weaker here"),
    ("staggering", "fifty", "pounds", "object",
     "She gained a staggering fifty pounds of muscle.",
     "She gained fifty staggering pounds of muscle.", "neutral", None),
    ("tidy", "two", "thousand", "object",
     "We saved a tidy two thousand dollars that month.",
     "We saved two thousand tidy dollars that month.", "neutral",
     "'two thousand dollars' with the numeral 'thousand' stretches the AANN "
     "numeral slot; coding kept but flagged"),
    ("hefty", "five", "hundred", "object",
     "He paid a hefty five hundred dollars in fees.",
     "He paid five hundred hefty dollars in fees.", "neutral",
     "numeral 'hundred' + dollars: same numeral-slot caveat as the 'thousand' "
     "item"),
    ("generous", "forty", "acres", "object",
     "They farmed a generous forty acres of wheat.",
     "They farmed forty generous acres of wheat.", "neutral", None),
    ("sprawling", "ten", "acres", "object",
     "She bought a sprawling ten acres of woodland.",
     "She bought ten sprawling acres of woodland.", "neutral", None),
    ("precious", "three", "kilos", "object",
     "We carried a precious three kilos of seed.",
     "We carried three precious kilos of seed.", "neutral", None),
    ("ruinous", "twenty", "thousand", "object",
     "The repair cost a ruinous twenty thousand dollars.",
     "The repair cost twenty thousand ruinous dollars.", "distributive",
     "numeral 'thousand' + dollars: numeral-slot caveat as above"),
    # ---- a few more temporal/distance to reach 32, balanced classes ----
    ("blissful", "four", "days", "temporal",
     "We enjoyed a blissful four days by the lake.",
     "We enjoyed four blissful days by the lake.", "neutral", None),
    ("brutal", "six", "weeks", "temporal",
     "Recruits faced a brutal six weeks of training.",
     "Recruits faced six brutal weeks of training.", "distributive", None),
    ("frantic", "two", "days", "temporal",
     "They had a frantic two days before the launch.",
     "They had two frantic days before the launch.", "distributive", None),
    ("dazzling", "seven", "miles", "distance",
     "We skied a dazzling seven miles of fresh powder.",
     "We skied seven dazzling miles of fresh powder.", "neutral", None),
    ("relentless", "twelve", "miles", "distance",
     "She marched a relentless twelve miles through the storm.",
     "She marched twelve relentless miles through the storm.", "distributive", None),
    ("modest", "two", "hundred", "object",
     "He earned a modest two hundred dollars from the sale.",
     "He earned two hundred modest dollars from the sale.", "neutral",
     "numeral 'hundred' + dollars: numeral-slot caveat as above"),
]

assert len(RAW_ITEMS) == 32, len(RAW_ITEMS)


def build():
    items = []
    for i, (adj, num, noun, nclass, aann, control, local_fluency, disputed) in \
            enumerate(RAW_ITEMS):
        uni = U(num, noun, adj)
        dis = D(num, noun, adj)
        # lexical-overlap parity check (Condition 2): both paraphrases measured
        # against the AANN premise. Templates are parallel by construction, but
        # we assert it mechanically and record the counts.
        ov_u = overlap_count(aann, uni)
        ov_d = overlap_count(aann, dis)
        # seeded counterbalance of the U/D letter and the was/were letter
        fc_letter_uni = "A" if rng.random() < 0.5 else "B"
        agr_letter_was = "A" if rng.random() < 0.5 else "B"
        item = {
            "id": f"v3-{nclass}-{adj}-{num}-{noun}",
            "adj": adj, "num": num, "noun": noun, "nounclass": nclass,
            "aann": aann, "control": control,
            # Arm A paraphrase forced choice
            "paraphrase_unification": uni,
            "paraphrase_distributive": dis,
            "fc_letter_unification": fc_letter_uni,   # counterbalance (block bias)
            "lexical_overlap": {"unification": ov_u, "distributive": ov_d,
                                "parity_ok": abs(ov_u - ov_d) <= 1,
                                "direction": ("equal" if ov_u == ov_d
                                              else "unification" if ov_u > ov_d
                                              else "distributive")},
            # Arm B NLI hypotheses (affirm/withhold)
            "nli": {
                "unification_hyp": NLI_uni(num, noun),
                "whole_eval_hyp": NLI_whole(num, noun, adj),
                "distributive_foil": NLI_distrib(num, noun, adj),
            },
            # Agreement sub-probe (load-bearing discriminator)
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

    # ---- lexical-overlap parity assertion (Condition 2) ----
    bad = [it["id"] for it in items if not it["lexical_overlap"]["parity_ok"]]
    assert not bad, f"lexical-overlap parity violated (|U-D|>1) for: {bad}"

    # ---- counterbalance balance assertion (Condition 1/2: block position bias)
    n_u_is_a = sum(1 for it in items if it["fc_letter_unification"] == "A")
    n_was_is_a = sum(1 for it in items
                     if it["agreement"]["agr_letter_was"] == "A")
    # seeded; require roughly balanced (within 6 of half for 32 items)
    assert abs(n_u_is_a - 16) <= 6, n_u_is_a
    assert abs(n_was_is_a - 16) <= 6, n_was_is_a

    # ---- under-pressure subset (Condition 4) ----
    under_pressure = [it["id"] for it in items
                      if it["local_fluency"] == "distributive"]
    assert len(under_pressure) >= 6, len(under_pressure)

    # ---- disputed-coding subset (Condition 6) ----
    disputed_ids = [it["id"] for it in items if it["key_disputed"]]

    # ---- Tier-0 pairs: well-formed AANN vs 4 Mahowald degenerate variants ----
    # built from the first 6 base AANN sentences, like v2/v2b (6 tuples x 4 = 24)
    tier0 = []
    variants = ["reverse_mods", "no_mod", "no_plural", "no_a"]
    for it in items[:6]:
        adj, num, noun = it["adj"], it["num"], it["noun"]
        wf = it["aann"]            # well-formed AANN
        # degenerate edits on the noun-phrase span "a <adj> <num> <noun>"
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

    out = {
        "seed": SEED,
        "design": "experiments/designs/aann-construction-v3-inferential.md",
        "governing_decision":
            "wiki/decisions/resolved/aann-inferential-operationalization.md",
        "anchor": "internal-contrast-only",
        "chief_cost_statement": CHIEF_COST,
        "expected_inference_key_provenance": KEY_PROVENANCE,
        "primary_instrument": "A (paraphrase forced-choice)",
        "convergent_instrument": "B (entailment NLI)",
        "load_bearing_discriminator": "agreement (was/were) sub-probe",
        "noun_classes": sorted({it["nounclass"] for it in items}),
        "counts": {
            "base_items": len(items),
            "by_nounclass": {c: sum(1 for it in items if it["nounclass"] == c)
                             for c in sorted({it["nounclass"] for it in items})},
            "under_pressure_distributive": len(under_pressure),
            "key_disputed": len(disputed_ids),
            "tier0_pairs": len(tier0),
            "fc_unification_letter_A": n_u_is_a,
            "agr_was_letter_A": n_was_is_a,
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
    print(f"  under-pressure (distributive locally-fluent): "
          f"{c['under_pressure_distributive']}")
    print(f"  key-disputed (item-level flags): {c['key_disputed']} "
          f"-> {out['key_disputed_ids']}")
    print(f"  tier0 pairs: {c['tier0_pairs']}")
    print(f"  counterbalance: U-letter=A on {c['fc_unification_letter_A']}/32; "
          f"was-letter=A on {c['agr_was_letter_A']}/32")
    print("  lexical-overlap parity: PASS (asserted)")


if __name__ == "__main__":
    main()
