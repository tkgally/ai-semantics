#!/usr/bin/env python3
"""build_arm2.py -- author + freeze the DISJUNCTIVE-HOMONYM lexical arm (Arm 2).

Within-lexical scalar-vs-disjunctive probe (ratified gate
wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md, ADOPT DEFAULT Option B +
nuisance-matching freeze). Arm 2 is the NEW, author-built, genuinely-DISJUNCTIVE lexical
class: balanced-homonym contexts (two unrelated senses both fully licensed, no tie-break)
vs sense-fixed contexts. `internal-contrast-only` (Q2-b): NO human-comparison claim.

Each homonym carries four author-built contexts:
  bal : a BALANCED context -- the homonym's two unrelated senses are both fully licensed,
        with no disambiguating tie-break (the genuinely-disjunctive ctx1 of the moment item).
  a1  : a context that fixes sense A clearly.
  a2  : a second context that fixes sense A clearly.
  b1  : a context that fixes sense B clearly.

Three items per homonym (mirrors Arm 1's bridging / clear-same / clear-different):
  disjunctive      = (bal, a1)  -> ctx1 undetermined, ctx2 fixes sense A; genuinely both/neither
  clear-same       = (a1, a2)   -> both fix sense A -> SAME (control)
  clear-different  = (a2, b1)   -> A vs B -> DIFFERENT (control)

The probe presents the target word marked with guillemets in BOTH sentences and asks
SAME/DIFFERENT/UNCLEAR sense + 0-100 confidence (instrument inherited verbatim from the
cross-level lexical leg). Target spans are computed here (first whole-word, case-insensitive
occurrence of the surface form). NO model call. Writes items_arm2.json + a length/freq
measurement to nuisance_match.json (consumed by certify.py for the frozen match record).

Run: python3 build_arm2.py   (deterministic, no API)
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# (homonym surface, senseA gloss, senseB gloss, Lg10WF [SUBTLEX-US, looked up 2026-06-23],
#  contexts dict). The disjunctive item pairs `bal` with `a1` (sense A fixed); A/B labels are
#  arbitrary per homonym (no systematic bias from "ctx2 always fixes A").
HOMONYMS = [
    ("bank", "the sloping edge of a river", "a financial institution", 3.64, {
        "bal": "Early the next morning, once the heavy rain had finally stopped, the two of us walked all the way down to the bank and stood there together quietly for a while.",
        "a1":  "Laughing and shouting to each other, the boys slid down the steep grassy bank and waded straight out into the cold shallow water of the slow river.",
        "a2":  "A long uneven row of old willows leaned far out over the muddy bank, where the slow brown river curved past the ruined mill and the empty fields.",
        "b1":  "After lunch she went into town to the bank and asked the clerk behind the counter to move most of the money into her new savings account.",
    }),
    ("crane", "a tall long-legged wading bird", "a machine for lifting heavy loads", 3.23, {
        "bal": "High above the far end of the flooded field, just before the light failed completely, we could make out the crane standing motionless against the pale evening sky.",
        "a1":  "Moving with great care, the crane waded slowly through the shallow reed-fringed marsh, lowered its long grey neck, and in one swift motion speared a small silver fish.",
        "a2":  "Every spring, without fail, a single pair of crane returned to the same quiet wetland and built their large untidy nest among the tall swaying reeds.",
        "b1":  "Early that morning the crane swung a heavy steel girder high over the half-built office tower while the site workers in hard hats shouted instructions below.",
    }),
    ("file", "a folder or set of documents", "a hand tool for smoothing or grinding", 3.35, {
        "bal": "Without looking up from his work for even a moment, he reached across the bench and quietly picked up the file that someone had left lying there earlier.",
        "a1":  "She opened the thick brown paper file, spread the printed pages out across the wide desk, and began reading slowly through the old case notes.",
        "a2":  "The clerk pulled the missing file out of the grey cabinet, stamped the cover firmly in red ink, and carried it off down the long corridor.",
        "b1":  "Working steadily, the carpenter took a coarse metal file and ran it back and forth across the rough edge until at last the wood was perfectly smooth.",
    }),
    ("mole", "a small burrowing animal", "a spy hidden inside an organisation", 2.61, {
        "bal": "For several long and difficult weeks now, almost everyone there had been quietly but constantly talking about the mole, and still nobody knew quite what to do.",
        "a1":  "Some time during the night a busy mole had tunnelled right across the whole front lawn, leaving a long crooked line of soft brown heaps in the wet grass.",
        "a2":  "Pausing for just a second, the mole pushed its broad pink snout up through the loose dark soil, blinked once in the bright light, and quickly dug down again.",
        "b1":  "After the long internal inquiry the agency became certain that a mole had been passing the secret files to a foreign intelligence service for several years.",
    }),
    ("organ", "a functional part of the body", "a large keyboard musical instrument", 2.57, {
        "bal": "The organ had been badly damaged in an accident many years earlier, and the whole family knew perfectly well that it would be very hard to replace now.",
        "a1":  "After studying the latest scans, the surgeon carefully explained that the failing organ would have to be removed altogether before the infection had any chance to spread.",
        "a2":  "Racing against the clock, the medical team kept the donated organ packed in ice and rushed it right across the country to reach the waiting patient in time.",
        "b1":  "As the long service began, the great organ slowly filled the cold stone cathedral with sound while the player pressed the worn keys and pulled out the heavy stops.",
    }),
    ("trunk", "the woody main stem of a tree", "a large rigid travelling chest", 3.00, {
        "bal": "The old trunk turned out to be far too heavy for the two of us to lift between us, so in the end we simply dragged it slowly all the way along the ground.",
        "a1":  "Over the years thick green ivy had wound itself all the way up the rough cracked trunk of the ancient spreading oak that stood alone in the corner of the yard.",
        "a2":  "During the storm lightning had split the broad trunk of the old elm right down the middle, and pale sticky sap ran slowly down over the cracked grey bark.",
        "b1":  "Up in the dusty attic she finally unlocked the battered old leather trunk and lifted out a pile of carefully folded dresses and a bundle of yellowing letters.",
    }),
    ("tank", "an armoured military vehicle", "a large container for liquid or gas", 3.12, {
        "bal": "The huge rusting tank had been sitting quietly at the far edge of the ploughed field for as long as almost anyone still living in the small village could clearly recall.",
        "a1":  "With a deep rumble the tank rolled steadily forward across the broken muddy ground, its heavy main gun turning slowly to point toward the low distant ridge.",
        "a2":  "Two more tank advanced cautiously through the drifting grey smoke as the tired soldiers crouched low behind the shattered remains of an old stone field wall.",
        "b1":  "Muttering to himself, the plumber drained the rusty old water tank up in the loft and carefully fitted a brand new valve to stop the slow steady leak.",
    }),
    ("punch", "a blow struck with the fist", "a sweet mixed drink served at parties", 3.18, {
        "bal": "Nobody who had been at that loud and crowded party on Saturday night would forget the punch for a very long time afterwards, that much was certain.",
        "a1":  "He swung his arm back hard and landed a heavy punch square on the other man's jaw, and the whole watching crowd gasped aloud at once.",
        "a2":  "She ducked low under the first wild punch, stepped in quickly toward him, and drove her own fist hard into his unguarded ribs.",
        "b1":  "At the far end of the table she carefully ladled the sweet red fruit punch out into long rows of little paper cups for the waiting children.",
    }),
    ("plot", "the storyline of a narrative", "a small marked-out piece of ground", 2.77, {
        "bal": "The whole plot had changed almost beyond all recognition since the very last time that he had sat down and carefully looked over it in any real detail.",
        "a1":  "Almost exactly halfway through the long winding novel the plot suddenly twisted, and the quiet unassuming gardener turned out, against all expectation, to be the real killer.",
        "a2":  "Several reviewers complained at length that the expensive film's plot made very little sense and that whole stretches of scenes seemed to lead absolutely nowhere.",
        "b1":  "Working all weekend, they cleared the tangled weeds from the narrow overgrown plot behind the old cottage and planted two long neat rows of seed potatoes.",
    }),
    ("pupil", "the dark central opening of the eye", "a school student", 2.21, {
        "bal": "All through the long quiet lesson the new teacher simply could not stop looking at the pupil, and several long minutes slipped past before she finally glanced away.",
        "a1":  "Holding the small bright torch quite steady, the doctor watched closely as the pupil shrank to a tiny black dot right at the very centre of the patient's pale eye.",
        "a2":  "The instant she stepped out of the dark echoing hall into the blinding afternoon sun, each pupil narrowed sharply and painfully against the sudden harsh glare.",
        "b1":  "Without a word the shy new pupil handed in her finished homework, took her usual seat near the rain-streaked window, and quietly opened her heavy textbook to read.",
    }),
    ("ring", "a small circular band of jewellery", "a roped-off arena for boxing", 3.67, {
        "bal": "All evening long everyone's eyes kept drifting back toward the ring, right up until the moment the long and tiring evening finally reached its peak.",
        "a1":  "He slipped the thin gold ring carefully onto her finger, and she at once held her hand up high to the light to admire the way it shone.",
        "a2":  "The old silver ring had been passed down quietly through the family for several generations, and she never once took it off her finger.",
        "b1":  "The two exhausted boxers circled each other warily inside the ring while the referee in his white shirt watched their feet very closely.",
    }),
    ("club", "an organised society that people join", "a heavy stick used as a weapon", 3.70, {
        "bal": "The old club had been in his large scattered family for three whole generations by now, and although he rarely ever said so, he was quietly very proud of it.",
        "a1":  "Soon after moving to the area she joined the small friendly local chess club, paid the modest yearly fee, and went along faithfully to the meeting every single Friday.",
        "a2":  "At its crowded annual meeting the village social club voted by a clear majority to admit a batch of new members and to repair the worn and leaking roof.",
        "b1":  "With a furious shout the heavy-set guard raised a thick wooden club high above his head and brought it down hard, again and again, against the bolted door.",
    }),
]


def find_span(text, surface):
    """First whole-word, case-insensitive occurrence of surface -> (start, end). Raises if none."""
    for m in re.finditer(r"\b" + re.escape(surface) + r"\b", text, flags=re.IGNORECASE):
        return [m.start(), m.end()]
    raise ValueError(f"surface {surface!r} not found as a whole word in: {text!r}")


def toklen(s):
    return len(re.findall(r"\w+", s))


def main():
    items = []
    lengths = {"disjunctive": [], "clear-same": [], "clear-different": [], "balanced_ctx1": []}
    freqs = []
    for surface, sa, sb, lg, c in HOMONYMS:
        freqs.append(lg)
        # spans (target appears once as a whole word in each context)
        spans = {k: find_span(v, surface) for k, v in c.items()}
        base = {"lemma": f"{surface}_nn", "surface": surface,
                "senseA": sa, "senseB": sb, "lg10wf": lg, "arm": "disjunctive-homonym"}

        # disjunctive (ambiguous / moment-pole class): bal (undetermined) + a1 (sense A fixed)
        items.append({**base, "item_id": f"dj-{surface}", "class": "disjunctive",
                      "ctx1": c["bal"], "span1": spans["bal"],
                      "ctx2": c["a1"], "span2": spans["a1"]})
        lengths["disjunctive"] += [toklen(c["bal"]), toklen(c["a1"])]
        lengths["balanced_ctx1"].append(toklen(c["bal"]))
        # clear-same control: a1 + a2 (both fix sense A) -> SAME
        items.append({**base, "item_id": f"cs-{surface}", "class": "clear-same",
                      "ctx1": c["a1"], "span1": spans["a1"],
                      "ctx2": c["a2"], "span2": spans["a2"]})
        lengths["clear-same"] += [toklen(c["a1"]), toklen(c["a2"])]
        # clear-different control: a2 + b1 (A vs B) -> DIFFERENT
        items.append({**base, "item_id": f"cd-{surface}", "class": "clear-different",
                      "ctx1": c["a2"], "span1": spans["a2"],
                      "ctx2": c["b1"], "span2": spans["b1"]})
        lengths["clear-different"] += [toklen(c["a2"]), toklen(c["b1"])]

    # sanity: target surface really sits at the recorded span in each context
    for it in items:
        for n in (1, 2):
            a, b = it[f"span{n}"]
            assert it[f"ctx{n}"][a:b].lower() == it["surface"].lower(), it["item_id"]

    out = {"_provenance": {
        "design": "experiments/designs/within-lexical-scalar-vs-disjunctive-v1.md",
        "gate": "wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md",
        "arm": "Arm 2 -- disjunctive-homonym (author-built, internal-contrast-only, Q2-b)",
        "anchor": "internal-contrast-only (NO human-comparison claim; author-stipulated balanced homonyms)",
        "instrument": "inherited verbatim from cross-level lexical leg (SAME/DIFFERENT/UNCLEAR + 0-100 conf)",
        "note": "Balanced (bal) contexts leave the homonym's two unrelated senses both licensed with no "
                "tie-break; sense-fixed contexts (a1/a2/b1) fix one sense. The disjunctive item pairs a "
                "balanced ctx1 with a sense-A-fixed ctx2 so the same/different-SENSE judgment is genuinely "
                "both/neither. NO probe was run when this file was authored.",
    }, "items": items}
    json.dump(out, open(os.path.join(HERE, "items_arm2.json"), "w"), indent=1, ensure_ascii=False)

    import statistics as st
    nm = {
        "n_homonyms": len(HOMONYMS),
        "n_items": len(items),
        "freq_lg10wf": {"mean": round(st.mean(freqs), 3), "median": round(st.median(freqs), 3),
                        "min": min(freqs), "max": max(freqs), "values": freqs},
        "sentence_tokens": {k: {"mean": round(st.mean(v), 2), "median": st.median(v),
                                "min": min(v), "max": max(v), "n": len(v)}
                            for k, v in lengths.items()},
        "arm1_targets_for_match": {
            "freq_lg10wf": {"mean": 2.98, "median": 3.15, "min": 1.11, "max": 4.13,
                            "_source": "DWUG bridging-class lemmas, SUBTLEX-US Lg10WF, measured 2026-06-23"},
            "sentence_tokens": {"all": {"mean": 27.2, "median": 24.0, "min": 8, "max": 66},
                                "bridging": {"mean": 28.0, "median": 25.0},
                                "_source": "DWUG fulltext (gitignored), measured 2026-06-23"},
            "pos_frame": "43 nn / 5 vb (mostly nn1 nouns)"},
        "arm2_pos_frame": "12/12 homonym targets are common nouns (nn), used as nouns in every context",
        "register_note": "Arm 1 = DWUG/COHA corpus prose (literary/journalistic, 1810s-2010s); Arm 2 = "
                         "author-built contemporary plain declarative prose. This register difference is "
                         "the irreducible residual (an author cannot make Arm 2 corpus-attested). It cuts "
                         "TOWARD survival (cleaner contemporary prose is, if anything, EASIER), so a "
                         "collapse finding is the harder one to obtain under it -- disclosed and led with.",
    }
    json.dump(nm, open(os.path.join(HERE, "nuisance_match.json"), "w"), indent=1)
    print(f"wrote items_arm2.json ({len(items)} items, {len(HOMONYMS)} homonyms)")
    print(json.dumps(nm, indent=1))


if __name__ == "__main__":
    main()
