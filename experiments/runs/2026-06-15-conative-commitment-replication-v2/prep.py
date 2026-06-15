#!/usr/bin/env python3
"""prep.py — stimulus authoring for the conative COMMITMENT-ONLY replication
double contrast (run 2026-06-15-conative-commitment-replication-v2). NO model calls.

A clean DIRECT REPLICATION of the single positive effect found in
result/conative-preference-commitment-v1: claude-sonnet-4.6's COMMITMENT-ONLY
double contrast (Δ²_commit = +0.46, 95% CI [0.08, 0.79]) — the conative shifts the
NLI commitment more than the matched anomalous "at"-string, with NO paraphrase
shift. That effect was a SINGLE model, a WIDE CI (n = 12 conative vs 8 resist),
and an anomaly (the mirror of the AANN dissociation). This run asks the one
question a replication answers: is it a STABLE, replicable single-model property,
or noise from one item set?

Same instrument, thresholds, scoring, panel as v1; ONLY the verbs/objects change —
a FRESH, DISJOINT verb set (no verb reused from the v1 run). Structure mirrors v1:
12 conative-alternation verbs (hit/poke/bite class) + 8 non-alternating contact
verbs (touch class + change-of-state class) forced into the anomalous "V at NP"
frame as the lexical-cue control. The point of fresh verbs is to test whether the
v1 effect survives a wholly independent lexical sample, NOT to re-tune anything.

THE FOUR FAMILIES (40 items total) — identical schema to v1
----------------------------------------------------------
  transitive_conative : "Lena slapped the desk."          contact ENTAILED (headroom anchor)
  conative   (target) : "Lena slapped at the desk."       contact SUPPRESSED (licensed cancel)
  resist / LCC        : "Omar hugged at the teddy."        anomalous bare-at cue, NOT licensed
  transitive_resist   : "Omar hugged the teddy."           contact ENTAILED (resist baseline)

  12 conative verbs x {transitive_conative, conative}  = 24 items
   8 resist   verbs x {transitive_resist, resist}      = 16 items
                                                          = 40 items

FRESH VERB SETS (disjoint from v1's kick/hit/punch/slash/stab/claw/swat/jab/chop/
scratch/hack/whack [conative] and touch/embrace/break/shatter/crush/smash/bump/
split [resist]):

  CONATIVE (12): slap, smack, pound, beat, strike, rap, tap, bash, batter, poke,
  bite, thump. All undergo the Levin (1993) conative alternation (hit verbs +
  poke/bite): the transitive robustly entails completed contact; "V at NP" cancels
  the contact guarantee (force-and-motion-directed-at-a-target semantics).

  RESIST (8): hug, caress, cradle (Levin touch verbs — lexicalize contact, do NOT
  undergo the conative because they lack the directed-force/motion semantics) +
  crumple, squash, flatten, dent, mangle (change-of-state verbs — like v1's break/
  shatter/crush/smash; non-alternating, robustly entail contact transitively,
  anomalous in "V at NP" with NO lexicalized idiomatic "at"-reading). The strong
  contaminant lesson from v1 (snap → "snap at" = bite/lash-out idiom, removed
  pre-run) is honored: none of these eight carries a fixed idiomatic at-reading.
  Verbs flagged as POSSIBLY marginal for the independent pre-run critic to vet:
  squash/flatten/dent (a "made <X>ing attempts toward" reading is conceivable but
  not lexicalized) — same conservative direction as v1's smash/crush (would only
  SHRINK Δ², never manufacture a false positive). The result page must report a
  with/without robustness check on any verb the critic flags.

TWO PARAPHRASE OPTIONS (Arm 1; lexical parity — differ ONLY by "did not necessarily")
  D (default reading): "<subj> made contact with the <obj>."
  C (cancel  reading): "<subj> did not necessarily make contact with the <obj>."
A/B letter assignment is SEED-COUNTERBALANCED per item (fixed seed 20260615,
identical scheme to v1); the assignment is recorded per item.

ANCHOR (identical split to v1, design §8): NLI conative items -> human-anchored
(CxNLI conative gold = non-entailment); paraphrase arm + resist/LCC arm =
internal-contrast-only. The expert-stipulated conative-correct paraphrase reading
(cancel) is labelled expert-stipulated. No anchor invented.

Run: python3 prep.py   (no API; writes stimuli.json + prints PASS/FAIL + sha256)
"""
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
SEED = 20260615  # identical counterbalancing scheme to v1; fresh verbs give fresh items

# ---- FRESH conative-alternation verbs (Levin 1993 hit/poke/bite classes) --------
# Disjoint from the v1 set. The transitive robustly entails completed contact; the
# conative "V at NP" cancels the contact guarantee.
# (verb, past, typical_object)
CONATIVE = [
    ("slap",    "slapped",   "desk"),
    ("smack",   "smacked",   "ball"),
    ("pound",   "pounded",   "door"),
    ("beat",    "beat",      "rug"),
    ("strike",  "struck",    "gong"),
    ("rap",     "rapped",    "table"),
    ("tap",     "tapped",    "window"),
    ("bash",    "bashed",    "wall"),
    ("batter",  "battered",  "gate"),
    ("poke",    "poked",     "cushion"),
    ("bite",    "bit",       "apple"),
    ("thump",   "thumped",   "crate"),
]

# ---- FRESH non-alternating contact verbs — the resist / LCC arm (8 verbs) -------
# Disjoint from the v1 set. Touch verbs (hug/caress/cradle: lexicalize contact, no
# directed-force/motion semantics -> no conative) + change-of-state verbs
# (crumple/squash/flatten/dent/mangle: like v1's break/shatter/crush/smash). Each
# robustly entails contact transitively and is anomalous in "V at NP" with NO
# lexicalized idiomatic at-reading (the snap-at lesson from v1).
RESIST = [
    ("hug",     "hugged",    "teddy"),
    ("caress",  "caressed",  "cheek"),
    ("cradle",  "cradled",   "infant"),
    ("crumple", "crumpled",  "letter"),
    ("squash",  "squashed",  "beetle"),
    ("flatten", "flattened", "carton"),
    ("dent",    "dented",    "fender"),
    ("mangle",  "mangled",   "wire"),
]

# Same subject within a verb's two conditions (true minimal pair); rotate so no
# name dominates. Reused verbatim from the v1 run (pure naming inventory; not a verb).
SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
            "Aisha", "Sam", "Wei", "Dana", "Hana", "Luca", "Iris", "Mara"]


def build_items():
    """Author the 40 frozen items with seed-counterbalanced A/B paraphrase
    assignment. Returns the item list. (Identical authoring logic to the v1 run;
    only the verb tables above differ.)"""
    rng = random.Random(SEED)
    items = []
    si = 0
    # ---- conative-verb families: transitive_conative + conative ----
    for verb, past, obj in CONATIVE:
        subj = SUBJECTS[si % len(SUBJECTS)]
        si += 1
        obj_np = f"the {obj}"
        contact_prop = f"{subj} made contact with {obj_np}."
        para_D = f"{subj} made contact with {obj_np}."                       # default
        para_C = f"{subj} did not necessarily make contact with {obj_np}."   # cancel
        cancel_is_A = rng.random() < 0.5
        cancel_letter = "A" if cancel_is_A else "B"
        default_letter = "B" if cancel_is_A else "A"
        opt_A = para_C if cancel_is_A else para_D
        opt_B = para_D if cancel_is_A else para_C
        stem = f"{verb}-{subj}"
        items.append(dict(
            item_id=f"con-{verb}-transitive", family="transitive_conative",
            verb_class="conative", stem=stem,
            sentence=f"{subj} {past} {obj_np}.",
            contact_proposition=contact_prop,
            paraphrase_D=para_D, paraphrase_C=para_C,
            option_A=opt_A, option_B=opt_B,
            cancel_letter=cancel_letter, default_letter=default_letter,
            expert_correct_reading="D", expert_correct_note="expert-stipulated"))
        items.append(dict(
            item_id=f"con-{verb}-conative", family="conative",
            verb_class="conative", stem=stem,
            sentence=f"{subj} {past} at {obj_np}.",
            contact_proposition=contact_prop,
            paraphrase_D=para_D, paraphrase_C=para_C,
            option_A=opt_A, option_B=opt_B,
            cancel_letter=cancel_letter, default_letter=default_letter,
            expert_correct_reading="C", expert_correct_note="expert-stipulated"))
    # ---- resist-verb families: transitive_resist + resist (LCC) ----
    for verb, past, obj in RESIST:
        subj = SUBJECTS[si % len(SUBJECTS)]
        si += 1
        obj_np = f"the {obj}"
        contact_prop = f"{subj} made contact with {obj_np}."
        para_D = f"{subj} made contact with {obj_np}."
        para_C = f"{subj} did not necessarily make contact with {obj_np}."
        cancel_is_A = rng.random() < 0.5
        cancel_letter = "A" if cancel_is_A else "B"
        default_letter = "B" if cancel_is_A else "A"
        opt_A = para_C if cancel_is_A else para_D
        opt_B = para_D if cancel_is_A else para_C
        stem = f"{verb}-{subj}"
        items.append(dict(
            item_id=f"res-{verb}-transitive", family="transitive_resist",
            verb_class="resist", stem=stem,
            sentence=f"{subj} {past} {obj_np}.",
            contact_proposition=contact_prop,
            paraphrase_D=para_D, paraphrase_C=para_C,
            option_A=opt_A, option_B=opt_B,
            cancel_letter=cancel_letter, default_letter=default_letter,
            expert_correct_reading="D", expert_correct_note="expert-stipulated"))
        items.append(dict(
            item_id=f"res-{verb}-resist", family="resist",
            verb_class="resist", stem=stem,
            sentence=f"{subj} {past} at {obj_np}.",
            contact_proposition=contact_prop,
            paraphrase_D=para_D, paraphrase_C=para_C,
            option_A=opt_A, option_B=opt_B,
            cancel_letter=cancel_letter, default_letter=default_letter,
            expert_correct_reading=None, expert_correct_note="internal-contrast-only"))
    return items


def run_asserts(items):
    """Print PASS/FAIL for each mechanical check; return True iff all pass.
    Identical checks to the v1 run, plus a DISJOINTNESS check against v1's verbs."""
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            ok = False

    # 1. exactly 40 items
    check(f"exactly 40 items (got {len(items)})", len(items) == 40)

    fam = {}
    for it in items:
        fam[it["family"]] = fam.get(it["family"], 0) + 1
    check(f"12 transitive_conative (got {fam.get('transitive_conative')})",
          fam.get("transitive_conative") == 12)
    check(f"12 conative (got {fam.get('conative')})", fam.get("conative") == 12)
    check(f"8 transitive_resist (got {fam.get('transitive_resist')})",
          fam.get("transitive_resist") == 8)
    check(f"8 resist (got {fam.get('resist')})", fam.get("resist") == 8)

    # 2. paraphrase options differ ONLY by "did not necessarily" (lexical parity)
    parity_ok = True
    for it in items:
        d = it["paraphrase_D"]
        c = it["paraphrase_C"]
        expected_c = d.replace("made contact", "did not necessarily make contact")
        if c != expected_c:
            parity_ok = False
            print(f"   parity break: {it['item_id']}: {d!r} vs {c!r}")
    check("paraphrase options differ ONLY by 'did not necessarily'", parity_ok)

    # 3. every conative/resist sentence contains " at " and the matching transitive
    #    does NOT.
    at_ok = True
    for it in items:
        has_at = " at " in it["sentence"]
        if it["family"] in ("conative", "resist"):
            if not has_at:
                at_ok = False
                print(f"   missing ' at ': {it['item_id']}: {it['sentence']!r}")
        else:
            if has_at:
                at_ok = False
                print(f"   unexpected ' at ': {it['item_id']}: {it['sentence']!r}")
    check("every conative/resist has ' at '; transitives do not", at_ok)

    # minimal-pair link: at-sentence == transitive with "at" inserted before obj NP
    mp_ok = True
    by_stem = {}
    for it in items:
        by_stem.setdefault(it["stem"], {})[it["family"]] = it
    for stem, fams in by_stem.items():
        t = fams.get("transitive_conative") or fams.get("transitive_resist")
        a = fams.get("conative") or fams.get("resist")
        if t and a:
            expected = t["sentence"].replace(" the ", " at the ", 1)
            if a["sentence"] != expected:
                mp_ok = False
                print(f"   minimal-pair break {stem}: {t['sentence']!r} -> "
                      f"{a['sentence']!r} (expected {expected!r})")
    check("at-frame is the transitive minimal pair + ' at '", mp_ok)

    # 4. A/B counterbalancing roughly balanced
    n_cancel_A = sum(1 for it in items if it["cancel_letter"] == "A")
    n_cancel_B = len(items) - n_cancel_A
    balanced = abs(n_cancel_A - n_cancel_B) <= int(0.4 * len(items))
    check(f"A/B counterbalancing roughly balanced "
          f"(cancel on A={n_cancel_A}, B={n_cancel_B})", balanced)

    map_ok = True
    for it in items:
        a_is_cancel = it["option_A"] == it["paraphrase_C"]
        if (it["cancel_letter"] == "A") != a_is_cancel:
            map_ok = False
            print(f"   letter-map break: {it['item_id']}")
        if {it["option_A"], it["option_B"]} != {it["paraphrase_D"], it["paraphrase_C"]}:
            map_ok = False
            print(f"   option-set break: {it['item_id']}")
    check("recorded cancel_letter matches option_A/option_B content", map_ok)

    check("item_ids unique", len({it["item_id"] for it in items}) == len(items))

    # 5. DISJOINTNESS from the v1 run (the replication precondition): no verb reused.
    V1_CONATIVE = {"kick", "hit", "punch", "slash", "stab", "claw", "swat", "jab",
                   "chop", "scratch", "hack", "whack"}
    V1_RESIST = {"touch", "embrace", "break", "shatter", "crush", "smash", "bump",
                 "split"}
    these_con = {v for v, _, _ in CONATIVE}
    these_res = {v for v, _, _ in RESIST}
    check("12 fresh conative verbs", len(these_con) == 12)
    check("8 fresh resist verbs", len(these_res) == 8)
    check("conative verbs DISJOINT from v1 conative set",
          these_con.isdisjoint(V1_CONATIVE))
    check("resist verbs DISJOINT from v1 resist set",
          these_res.isdisjoint(V1_RESIST))
    check("conative and resist pools DISJOINT from each other",
          these_con.isdisjoint(these_res))

    return ok


def main():
    items = build_items()
    payload = {
        "run": "2026-06-15-conative-commitment-replication-v2",
        "design": "experiments/designs/conative-commitment-replication-v2.md",
        "replicates": "experiments/runs/2026-06-15-conative-preference-commitment-v1 "
                      "(claude COMMITMENT-ONLY Δ²_commit=+0.46)",
        "seed": SEED,
        "families": ["transitive_conative", "conative", "resist", "transitive_resist"],
        "paraphrase_options": {
            "D": "default reading: '<subj> made contact with the <obj>.'",
            "C": "cancel reading: '<subj> did not necessarily make contact with the <obj>.'",
        },
        "anchor_split": {
            "nli_conative": "human-anchored (resource/scivetti-2025-cxnli-dataset; "
                            "CxNLI conative gold = non-entailment)",
            "paraphrase_arm": "internal-contrast-only",
            "resist_lcc_arm": "internal-contrast-only",
        },
        "items": items,
    }
    ok = run_asserts(items)
    out = HERE / "stimuli.json"
    blob = json.dumps(payload, indent=1, ensure_ascii=False)
    out.write_text(blob)
    h = hashlib.sha256(blob.encode()).hexdigest()[:16]
    print(f"\nwrote {len(items)} items -> {out}")
    print(f"sha256[:16] = {h}  (freeze hash; record in README + PREREG)")
    if not ok:
        raise SystemExit("FAIL: one or more stimulus asserts failed")
    print("all asserts PASS")


if __name__ == "__main__":
    main()
