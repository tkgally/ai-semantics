#!/usr/bin/env python3
"""prep.py — stimulus authoring for the conative preference/commitment double
contrast (run 2026-06-15-conative-preference-commitment-v1). NO model calls.

Implements experiments/designs/conative-preference-commitment-v1.md §2 exactly.
Running this EMITS the frozen stimuli.json (committed BEFORE any probe call) and
asserts the parity / LCC-isolation / counterbalancing checks (prints PASS/FAIL,
exits nonzero on FAIL), then prints the sha256[:16] freeze hash.

THE FOUR FAMILIES (40 items total)
----------------------------------
  transitive_conative : "Maria kicked the ball."         contact ENTAILED (headroom anchor)
  conative   (target) : "Maria kicked at the ball."      contact SUPPRESSED (licensed cancel)
  resist / LCC        : "Maria touched at the wall."     anomalous bare-at cue, NOT licensed
  transitive_resist   : "Maria touched the wall."        contact ENTAILED (resist baseline)

  12 conative verbs x {transitive_conative, conative}  = 24 items
   8 resist   verbs x {transitive_resist, resist}      = 16 items
                                                          = 40 items

The 12 conative verbs/objects/subjects are REUSED VERBATIM from
experiments/runs/2026-05-30-conative-cancel-probe-v2/build_items.py (the frozen
result/conative-cancel-direction-v2 set: kick/hit/punch/slash/stab/claw/swat/jab/
chop/scratch/hack/whack). The first 4 resist verbs (touch/embrace/break/shatter)
are reused from that same file's CONTROL list; the 4 added non-alternating contact
verbs (crush/smash/snap/split) robustly ENTAIL contact transitively and are
anomalous in "V at NP" (none takes the conative in Levin 1993).

TWO PARAPHRASE OPTIONS (Arm 1; lexical parity — differ ONLY by "did not necessarily")
  D (default reading): "<subj> made contact with the <obj>."
  C (cancel  reading): "<subj> did not necessarily make contact with the <obj>."
A/B letter assignment is SEED-COUNTERBALANCED per item (fixed seed 20260615);
the assignment is recorded per item (which letter = which reading).

ANCHOR (design §8): NLI conative items -> human-anchored (CxNLI conative gold =
non-entailment); paraphrase arm + resist/LCC arm = internal-contrast-only. The
expert-stipulated conative-correct paraphrase reading (cancel) is labelled
expert-stipulated. No anchor invented.

Run: python3 prep.py   (no API; writes stimuli.json + prints PASS/FAIL + sha256)
"""
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
SEED = 20260615

# ---- REUSED VERBATIM from conative-cancel-probe-v2/build_items.py CONATIVE ----
# Levin (1993) conative-alternation verbs (hit/swat/cut classes): the transitive
# robustly entails completed contact; the conative "V at NP" cancels it.
# (verb, past, typical_object)
CONATIVE = [
    ("kick",    "kicked",    "ball"),
    ("hit",     "hit",       "pinata"),
    ("punch",   "punched",   "bag"),
    ("slash",   "slashed",   "rope"),
    ("stab",    "stabbed",   "mattress"),
    ("claw",    "clawed",    "curtain"),
    ("swat",    "swatted",   "balloon"),
    ("jab",     "jabbed",    "pad"),
    ("chop",    "chopped",   "log"),
    ("scratch", "scratched", "post"),
    ("hack",    "hacked",    "branch"),
    ("whack",   "whacked",   "melon"),
]

# Non-alternating contact verbs — the resist / LCC arm (8 verbs, design §2).
# First 4 reused from conative-cancel-probe-v2 CONTROL (touch/embrace/break/shatter);
# 4 added non-alternating contact verbs (crush/smash/bump/split) — each robustly
# entails contact transitively and is anomalous in "V at NP" (none takes the
# conative in Levin 1993). Picked from the candidate set {crush, smash, snap,
# split, slam, bump} for clean transitive contact-entailment + a robustly
# anomalous "V at NP" string.
# PRE-RUN FIX (2026-06-15, independent pre-run critic GO-WITH-FIXES): "snap" was
# REMOVED and replaced with "bump". "snapped at the twig" reads as a lexicalized
# idiom (snap at = bite/lash out / speak sharply), so it would behave like a real
# at-construction and contaminate the lexical-cue control (inflating resist
# cancel-pref / withhold → shrinking Δ²; conservative-direction, but a control-purity
# defect). "bumped at the cart" carries no idiomatic at-reading and is robustly
# anomalous. smash/crush remain marginal (weak idiomaticity, conservative direction);
# named in design §2 + reported on the result page as a robustness caveat.
RESIST = [
    ("touch",   "touched",   "wall"),
    ("embrace", "embraced",  "child"),
    ("break",   "broke",     "vase"),
    ("shatter", "shattered", "window"),
    ("crush",   "crushed",   "can"),
    ("smash",   "smashed",   "plate"),
    ("bump",    "bumped",    "cart"),
    ("split",   "split",     "board"),
]

# Same subject within a verb's two conditions (true minimal pair); rotate so no
# name dominates. Reused verbatim from conative-cancel-probe-v2.
SUBJECTS = ["Maria", "Jordan", "Priya", "Tomas", "Lena", "Omar", "Nina", "Carlos",
            "Aisha", "Sam", "Wei", "Dana", "Hana", "Luca", "Iris", "Mara"]


def build_items():
    """Author the 40 frozen items with seed-counterbalanced A/B paraphrase
    assignment. Returns the item list."""
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
        # seed-counterbalanced A/B: which letter shows the CANCEL reading (C)?
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
            # the expert-stipulated correct reading: transitive entails contact ->
            # the DEFAULT reading D is correct here (headroom anchor).
            expert_correct_reading="D", expert_correct_note="expert-stipulated"))
        items.append(dict(
            item_id=f"con-{verb}-conative", family="conative",
            verb_class="conative", stem=stem,
            sentence=f"{subj} {past} at {obj_np}.",
            contact_proposition=contact_prop,
            paraphrase_D=para_D, paraphrase_C=para_C,
            option_A=opt_A, option_B=opt_B,
            cancel_letter=cancel_letter, default_letter=default_letter,
            # conative-correct reading = CANCEL (C): contact not guaranteed.
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
            # anomalous at-string: no licensed reading key -> expert reading NA
            # (internal-contrast-only; see design §8).
            expert_correct_reading=None, expert_correct_note="internal-contrast-only"))
    return items


def run_asserts(items):
    """Print PASS/FAIL for each mechanical check; return True iff all pass."""
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            ok = False

    # 1. exactly 40 items
    check(f"exactly 40 items (got {len(items)})", len(items) == 40)

    # family counts: 12 transitive_conative, 12 conative, 8 transitive_resist, 8 resist
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
        # C must equal D with "made contact" -> "did not necessarily make contact"
        expected_c = d.replace("made contact", "did not necessarily make contact")
        if c != expected_c:
            parity_ok = False
            print(f"   parity break: {it['item_id']}: {d!r} vs {c!r}")
    check("paraphrase options differ ONLY by 'did not necessarily'", parity_ok)

    # 3. every conative/resist sentence contains " at " and the matching
    #    transitive does NOT.
    at_ok = True
    for it in items:
        has_at = " at " in it["sentence"]
        if it["family"] in ("conative", "resist"):
            if not has_at:
                at_ok = False
                print(f"   missing ' at ': {it['item_id']}: {it['sentence']!r}")
        else:  # transitive_*
            if has_at:
                at_ok = False
                print(f"   unexpected ' at ': {it['item_id']}: {it['sentence']!r}")
    check("every conative/resist has ' at '; transitives do not", at_ok)

    # also assert the minimal-pair link: the at-sentence == transitive with "at"
    # inserted before the object NP (true minimal pair within a stem).
    mp_ok = True
    by_stem = {}
    for it in items:
        by_stem.setdefault(it["stem"], {})[it["family"]] = it
    for stem, fams in by_stem.items():
        t = fams.get("transitive_conative") or fams.get("transitive_resist")
        a = fams.get("conative") or fams.get("resist")
        if t and a:
            # transitive "<subj> <past> the <obj>." -> at-frame inserts "at "
            expected = t["sentence"].replace(" the ", " at the ", 1)
            if a["sentence"] != expected:
                mp_ok = False
                print(f"   minimal-pair break {stem}: {t['sentence']!r} -> "
                      f"{a['sentence']!r} (expected {expected!r})")
    check("at-frame is the transitive minimal pair + ' at '", mp_ok)

    # 4. A/B counterbalancing roughly balanced (cancel reading on A vs B)
    n_cancel_A = sum(1 for it in items if it["cancel_letter"] == "A")
    n_cancel_B = len(items) - n_cancel_A
    # roughly balanced: neither letter holds the cancel reading for >70% of items
    balanced = abs(n_cancel_A - n_cancel_B) <= int(0.4 * len(items))
    check(f"A/B counterbalancing roughly balanced "
          f"(cancel on A={n_cancel_A}, B={n_cancel_B})", balanced)

    # consistency: option_A/option_B actually carry the recorded readings
    map_ok = True
    for it in items:
        a_is_cancel = it["option_A"] == it["paraphrase_C"]
        if (it["cancel_letter"] == "A") != a_is_cancel:
            map_ok = False
            print(f"   letter-map break: {it['item_id']}")
        # the two options are exactly {D, C}
        if {it["option_A"], it["option_B"]} != {it["paraphrase_D"], it["paraphrase_C"]}:
            map_ok = False
            print(f"   option-set break: {it['item_id']}")
    check("recorded cancel_letter matches option_A/option_B content", map_ok)

    # unique item_ids
    check("item_ids unique", len({it["item_id"] for it in items}) == len(items))

    return ok


def main():
    items = build_items()
    payload = {
        "run": "2026-06-15-conative-preference-commitment-v1",
        "design": "experiments/designs/conative-preference-commitment-v1.md",
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
