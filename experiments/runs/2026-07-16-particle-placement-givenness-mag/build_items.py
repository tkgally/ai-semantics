#!/usr/bin/env python3
"""Build + certify + freeze the VERB-PARTICLE-PLACEMENT object-givenness stimuli -- MAGNITUDE (MAG) arm
(program A5 3rd sibling / A2a powered-magnitude habit; session 238).

WHY THIS RUN. The verb-particle placement object-givenness line is a PROMOTED, standing `claim`
(wiki/findings/claims/particle-placement-givenness.md, `status: supported`, s229) but scoped
DIRECTION-ONLY with NO within-model magnitude attached (its fence (j)): "no powered/pooled magnitude arm
was run ... A magnitude would be a future powered arm." Unlike the genitive (fence (i) magnitude ATTACHED
s222) and the dative (magnitude attached s175), the particle claim carries no size for its load-bearing,
shortcut-immune referential effect. This run attaches a WITHIN-MODEL MAGNITUDE + bootstrap interval to that
effect by adding a THIRD disjoint FIREWALL arm and POOLING the three firewall runs (the A2a-merged pattern
that attached the genitive's magnitude, s222 N=108, and the dative's, s175 N=100).

The magnitude-bearing quantity for THIS claim is the byte-identical discourse-givenness FIREWALL shift
    shift2(frame) = mean(split-pref | GIVEN) - mean(split-pref | NEW-MENTIONED)                 [decisive]
because the firewall is the LOAD-BEARING, shortcut-immune arm (Arm 1 definiteness is confoundable; gpt
SHADOWs it). So this arm is FIREWALL-ONLY -- the exact analog of the genitive MAG run being TYPICAL-ONLY
(there the typical arm carried the magnitude and the nonce firewall was dropped, having replicated 3/3
twice; here the firewall carries the magnitude and the definiteness/length arms are dropped). The claim's
scope is 2/3 (claude + gemini confirm the firewall; gpt is a persistent, replicated SHADOW), so the
magnitude attaches to claude + gemini and gpt is reported as a displayed SHADOW, never averaged.

NO NEW DECISION. A within-design powered re-run under the resolved, ratified design
decisions/resolved/particle-placement-anchor-and-indicator (s225, ADOPT-WITH-MODIFICATION), re-using the
byte-frozen MEASUREMENT instrument (probe.py, common.py sha-identical to v1/rep2; freq_control.json kept
byte-identical to satisfy probe.py's freeze gate -- the firewall-only magnitude analysis does NOT use the
Arm-1 covariate) on NEW disjoint items with a NEW pooled analysis (analyze_merged.py). Carries a fresh-agent
pre-run critic + one non-Anthropic decorrelation vote, but no new cross-session ratification -- the
dative-s175 / genitive-mag-s222 pattern.

BYTE-FROZEN INSTRUMENT (sha-verified identical to v1/rep2): probe.py, common.py (only HARD_STOP_USD
differs, documented in-file -- firewall-only is ~864 calls not ~2,016), freq_control.json. NEW here: this
build_items.py (fresh disjoint FIREWALL-ONLY frames) + analyze_merged.py (the pooled magnitude). The
firewall CONTEXT template-triple CTX is re-used BYTE-IDENTICAL from v1/rep2 (frame-agnostic, certified
parallel; only {noun}/{subj} fill).

Human direction (Kim et al. 2016 / Gries 1999): given object -> SPLIT, so shift2 > 0. The magnitude the
run reports is an INTERNAL within-model quantity (Kim/Gries give no model-scale effect size), so it is a
within-model contrast, not a human-comparison of sizes (the anchor stays direction-only).

Outputs: stimuli.json (frozen, sha-pinned in PREREG) + a printed certification report.
Run: python3 build_items.py
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
V1_STIM = RUNS / "2026-07-14-particle-placement-givenness" / "stimuli.json"
REP2_STIM = RUNS / "2026-07-15-particle-placement-givenness-rep2" / "stimuli.json"
FREQ_JSON = HERE / "freq_control.json"
# VERB_LEMMA mirrors the byte-frozen analyze.py (past-tense form -> lemma) for the (D3) coverage check.
VERB_LEMMA = {
    "picked": "pick", "put": "put", "took": "take", "threw": "throw", "pulled": "pull",
    "wiped": "wipe", "hung": "hang", "locked": "lock", "folded": "fold", "rolled": "roll",
    "packed": "pack", "wrapped": "wrap", "carried": "carry", "set": "set", "lifted": "lift",
    "handed": "hand", "cleared": "clear", "shut": "shut", "brought": "bring", "turned": "turn",
    "cut": "cut", "hauled": "haul",
}

# ---------------------------------------------------------------------------
# 48 FRESH DISJOINT FRAMES (mag). Each: a subject NAME (distinct, none is the monitor's), a literal
# SEPARABLE transitive phrasal verb (past tense) + particle, a concrete INANIMATE count-noun object head.
# Same authoring discipline as v1/rep2: all full lexical NPs (no pronouns); concrete inanimate count
# objects natural in BOTH orders with a definite full-NP object (Kim et al. 2016 / Gries 1999).
#
# DISJOINTNESS + BYTE-FROZEN COVERAGE (all certified below):
#  * Every (verb, particle) pair is drawn from the frozen 38-pair set (freq_control.json per-pair keys +
#    analyze.py VERB_LEMMA cover every frame). 10 flexible pairs recur with a SECOND distinct fresh noun to
#    reach 48 frames; identity is the (verb, particle, noun) TRIPLE.
#  * Every object noun is FRESH -- disjoint from BOTH v1's AND rep2's noun sets (the mag arm pools with
#    both, so its frames must be disjoint from both) -- so all 48 (verb, particle, noun) triples are
#    disjoint from the 88 prior (certification check (D), extended to v1 U rep2).
# fields: subj, verb, prt, noun  (FIREWALL-ONLY: no `long` -- Arm 3 length is dropped)
# ---------------------------------------------------------------------------
FRAMES = [
    dict(id="f01", subj="Aisha",   verb="brought", prt="in",    noun="satchel"),
    dict(id="f02", subj="Bertil",  verb="carried", prt="down",  noun="duffel"),
    dict(id="f03", subj="Chidi",   verb="carried", prt="in",    noun="planter"),
    dict(id="f04", subj="Dagny",   verb="carried", prt="off",   noun="trophy"),
    dict(id="f05", subj="Esteban", verb="cleared", prt="away",  noun="dish"),
    dict(id="f06", subj="Farida",  verb="cleared", prt="off",   noun="beaker"),
    dict(id="f07", subj="Gunnar",  verb="cut",     prt="off",   noun="tag"),
    dict(id="f08", subj="Halima",  verb="folded",  prt="up",    noun="poncho"),
    dict(id="f09", subj="Ismael",  verb="handed",  prt="over",  noun="dossier"),
    dict(id="f10", subj="Johanna", verb="hung",    prt="up",    noun="smock"),
    dict(id="f11", subj="Kwame",   verb="hauled",  prt="up",    noun="anchor"),
    dict(id="f12", subj="Liesel",  verb="lifted",  prt="off",   noun="canopy"),
    dict(id="f13", subj="Mohan",   verb="lifted",  prt="up",    noun="trunk"),
    dict(id="f14", subj="Nadia",   verb="locked",  prt="up",    noun="strongbox"),
    dict(id="f15", subj="Osvaldo", verb="packed",  prt="away",  noun="duvet"),
    dict(id="f16", subj="Priya",   verb="packed",  prt="up",    noun="loom"),
    dict(id="f17", subj="Quentin", verb="picked",  prt="out",   noun="splinter"),
    dict(id="f18", subj="Rosa",    verb="picked",  prt="up",    noun="skillet"),
    dict(id="f19", subj="Soren",   verb="pulled",  prt="down",  noun="awning"),
    dict(id="f20", subj="Thandi",  verb="pulled",  prt="off",   noun="decal"),
    dict(id="f21", subj="Umberto", verb="pulled",  prt="out",   noun="nail"),
    dict(id="f22", subj="Valeria", verb="put",     prt="away",  noun="ladle"),
    dict(id="f23", subj="Wynne",   verb="put",     prt="back",  noun="tome"),
    dict(id="f24", subj="Xiulan",  verb="put",     prt="down",  noun="basin"),
    dict(id="f25", subj="Yosef",   verb="put",     prt="out",   noun="candle"),
    dict(id="f26", subj="Zara",    verb="rolled",  prt="out",   noun="carpet"),
    dict(id="f27", subj="Anton",   verb="rolled",  prt="up",    noun="scroll"),
    dict(id="f28", subj="Brisa",   verb="set",     prt="down",  noun="goblet"),
    dict(id="f29", subj="Cato",    verb="set",     prt="up",    noun="gazebo"),
    dict(id="f30", subj="Delphine",verb="shut",    prt="off",   noun="nozzle"),
    dict(id="f31", subj="Emeka",   verb="took",    prt="apart", noun="motor"),
    dict(id="f32", subj="Frida",   verb="took",    prt="down",  noun="trellis"),
    dict(id="f33", subj="Goran",   verb="took",    prt="off",   noun="hubcap"),
    dict(id="f34", subj="Hana",    verb="took",    prt="out",   noun="cartridge"),
    dict(id="f35", subj="Iker",    verb="threw",   prt="out",   noun="husk"),
    dict(id="f36", subj="Juno",    verb="turned",  prt="off",   noun="faucet"),
    dict(id="f37", subj="Kiran",   verb="wiped",   prt="off",   noun="lens"),
    dict(id="f38", subj="Lucia",   verb="wrapped", prt="up",    noun="gift"),
    dict(id="f39", subj="Milo",    verb="picked",  prt="up",    noun="cauldron"),
    dict(id="f40", subj="Nkechi",  verb="put",     prt="down",  noun="cask"),
    dict(id="f41", subj="Otto",    verb="took",    prt="out",   noun="vial"),
    dict(id="f42", subj="Perla",   verb="lifted",  prt="up",    noun="slab"),
    dict(id="f43", subj="Rasheed", verb="pulled",  prt="off",   noun="gasket"),
    dict(id="f44", subj="Signe",   verb="set",     prt="up",    noun="marquee"),
    dict(id="f45", subj="Teodoro", verb="hung",    prt="up",    noun="wreath"),
    dict(id="f46", subj="Ula",     verb="carried", prt="off",   noun="casket"),
    dict(id="f47", subj="Vikram",  verb="cleared", prt="away",  noun="tureen"),
    dict(id="f48", subj="Wilma",   verb="took",    prt="off",   noun="sheath"),
]

# ---------------------------------------------------------------------------
# Arm-2 CONTEXT TEMPLATE-TRIPLE -- RE-USED BYTE-IDENTICAL from v1/rep2 (frame-agnostic; certified parallel:
# 2 clauses, 1 comma, declarative, 14 words each incl. the subject token; object noun appears exactly once
# in GIVEN and NEW-MENTIONED and zero times in NEW; no verb-particle / fronting / heavy-NP of the object).
# ---------------------------------------------------------------------------
CTX = {
    "given":   "A {noun} had been sitting nearby since dawn, and {subj} kept glancing at it.",
    "newment": "A {noun} could be handy at times, or so {subj} always liked to think.",
    "new":     "The early morning had been calm and grey, and {subj} moved about without hurry.",
}
ARM2_LEVELS = ["given", "newment", "new"]


def scored(subj, verb, prt, obj_np):
    """(joined V-Prt-DO, split V-DO-Prt) full sentences of the SAME proposition."""
    joined = f"{subj} {verb} {prt} {obj_np}."
    split = f"{subj} {verb} {obj_np} {prt}."
    return joined, split


def wc(s):
    return len(s.split())


def build():
    """FIREWALL-ONLY: emit only the Arm-2 discourse-givenness firewall trials (the magnitude-bearing arm).
    Arm 1 (definiteness) and Arm 3 (length) are DROPPED -- the magnitude the claim owes is the firewall
    shift2, and the definiteness direction + firewall survival already replicated 2/2 runs (the genitive
    MAG typical-only analog)."""
    frames, trials = [], []
    for fr in FRAMES:
        subj, verb, prt, noun = fr["subj"], fr["verb"], fr["prt"], fr["noun"]
        the_np = f"the {noun}"
        frames.append(dict(fr, arms={"firewall": ARM2_LEVELS}))

        def emit(arm, condition, obj_np, context):
            joined, split = scored(subj, verb, prt, obj_np)
            for split_is_a in (True, False):   # A/B counterbalance
                a = split if split_is_a else joined
                b = joined if split_is_a else split
                trials.append({
                    "frame": fr["id"], "arm": arm, "condition": condition,
                    "subject": subj, "verb": verb, "particle": prt, "object_head": noun,
                    "object_np": obj_np, "context": context,
                    "joined": joined, "split": split,
                    "split_is_a": split_is_a, "option_a": a, "option_b": b,
                })

        # Arm 2 -- firewall (byte-identical "the <noun>"; context varies). ONLY arm.
        for lv in ARM2_LEVELS:
            ctx = CTX[lv].format(noun=noun, subj=subj)
            emit("firewall", lv, the_np, ctx)
    return frames, trials


# ---------------------------------------------------------------------------
# CERTIFICATION (same machinery as v1/rep2, scoped to the firewall arm; (D) extended to v1 U rep2).
# ---------------------------------------------------------------------------
PRONOUNS = {"it", "him", "her", "them", "this", "that", "these", "those", "one"}
PARTICLE_WORDS = {"up", "down", "off", "out", "in", "over", "away", "back", "apart", "on"}


def scored_readers():
    return {
        "always_split":  lambda t: 1.0,
        "always_joined": lambda t: 0.0,
        "always_A":      lambda t: 1.0 if t["split_is_a"] else 0.0,
        "always_B":      lambda t: 0.0 if t["split_is_a"] else 1.0,
        "position_A_bias": lambda t: 0.7 if t["split_is_a"] else 0.3,
        "len_shorter_split": lambda t: 1.0 if len(t["split"]) <= len(t["joined"]) else 0.0,
        "objstr_the_split": lambda t: 0.6 if t["object_np"].startswith("the ") else 0.4,
    }


def frame_shift(trials, frame_id, arm, reader, hi, lo):
    def mean_pref(cond):
        vals = [reader(t) for t in trials
                if t["frame"] == frame_id and t["arm"] == arm and t["condition"] == cond]
        return sum(vals) / len(vals) if vals else None
    a, b = mean_pref(hi), mean_pref(lo)
    if a is None or b is None:
        return None
    return a - b


def certify(frames, trials):
    report = {"checks": {}, "fail": []}

    # (1) Arm-2 scored strings byte-identical across given/newment/new within every frame
    bi_ok = True
    for fr in frames:
        fid = fr["id"]
        joined_set, split_set = set(), set()
        for t in trials:
            if t["frame"] == fid and t["arm"] == "firewall":
                joined_set.add(t["joined"]); split_set.add(t["split"])
        if len(joined_set) != 1 or len(split_set) != 1:
            bi_ok = False
            report["fail"].append(f"(1) Arm-2 scored strings differ within {fid}: "
                                  f"{sorted(joined_set)} / {sorted(split_set)}")
    report["checks"]["(1) Arm-2 scored strings BYTE-IDENTICAL across given/newment/new per frame"] = bi_ok

    # (2) scored-string shortcut readers -> within-frame Arm-2 shift 0 on every frame
    readers = scored_readers()
    max_abs = {}
    for name, r in readers.items():
        shifts = []
        for fr in frames:
            for hi, lo in (("given", "newment"), ("given", "new")):
                s = frame_shift(trials, fr["id"], "firewall", r, hi, lo)
                if s is not None:
                    shifts.append(abs(s))
        max_abs[name] = max(shifts) if shifts else None
    report["max_abs_arm2_frame_shift_per_scored_reader"] = {k: round(v, 9) for k, v in max_abs.items()}
    all_zero = all((v is not None and v < 1e-9) for v in max_abs.values())
    report["checks"]["(2) no scored-string shortcut reader yields ANY within-frame Arm-2 shift"] = all_zero
    if not all_zero:
        report["fail"].append("(2) a scored-string shortcut reader produced a nonzero Arm-2 within-frame shift")

    # (3) Arm-2 context parallelism per frame
    clause_ok = comma_ok = wc_ok = noun_ok = leak_ok = True
    for fr in frames:
        noun = fr["noun"]
        ctxs = {lv: CTX[lv].format(noun=noun, subj=fr["subj"]) for lv in ARM2_LEVELS}
        commas = {c.count(",") for c in ctxs.values()}
        if commas != {1}:
            comma_ok = False; report["fail"].append(f"(3) comma count != 1 uniformly in {fr['id']}: {commas}")
        wcs = {wc(c) for c in ctxs.values()}
        if len(wcs) != 1:
            wc_ok = False; report["fail"].append(f"(3) word count mismatch in {fr['id']}: -> {wcs}")
        if any(c.rstrip().endswith(("?", "!")) for c in ctxs.values()):
            clause_ok = False; report["fail"].append(f"(3) non-declarative context in {fr['id']}")

        def noun_count(s):
            return len(re.findall(r"\b" + re.escape(noun) + r"\b", s.lower()))
        ng, nm, nn = noun_count(ctxs["given"]), noun_count(ctxs["newment"]), noun_count(ctxs["new"])
        if not (ng == 1 and nm == 1 and nn == 0):
            noun_ok = False
            report["fail"].append(f"(3) noun-mention pattern wrong in {fr['id']}: "
                                  f"given={ng} newment={nm} new={nn} (want 1/1/0)")
        for lv, c in ctxs.items():
            toks = re.findall(r"[a-z]+", c.lower())
            if noun in toks:
                i = toks.index(noun)
                nbrs = toks[max(0, i - 1):i] + toks[i + 1:i + 2]
                if any(w in PARTICLE_WORDS for w in nbrs):
                    leak_ok = False
                    report["fail"].append(f"(3) particle word adjacent to object noun in {fr['id']}/{lv}: {c}")
    report["checks"]["(3) Arm-2 contexts: uniform comma count (1)"] = comma_ok
    report["checks"]["(3) Arm-2 contexts: matched word count across given/newment/new"] = wc_ok
    report["checks"]["(3) Arm-2 contexts: all declarative"] = clause_ok
    report["checks"]["(3) Arm-2 contexts: object noun 1/1/0 in given/newment/new"] = noun_ok
    report["checks"]["(3) Arm-2 contexts: no particle word adjacent to the object noun (no leak)"] = leak_ok

    # (4) all objects full lexical NP (no pronoun head), non-empty
    pron = []
    for t in trials:
        head = t["object_head"].lower()
        if head in PRONOUNS or not head:
            pron.append((t["frame"], t["object_head"]))
    report["checks"]["(4) every object a full lexical NP (no pronoun head)"] = not pron
    if pron:
        report["fail"].append(f"(4) pronoun/empty object head(s): {pron[:5]}")

    # (5) counts + firewall-only
    def per_frame(arm):
        return len([t for t in trials if t["frame"] == frames[0]["id"] and t["arm"] == arm])
    n_frames = len(frames)
    arm2_pf = per_frame("firewall")
    report["checks"]["(N) >=40 frames"] = n_frames >= 40
    report["checks"]["(N) FIREWALL-ONLY: 6 firewall trials/frame, no definiteness/length trials"] = (
        arm2_pf == 6 and per_frame("definiteness") == 0 and per_frame("length") == 0)
    report["counts"] = {"n_frames": n_frames, "n_trials": len(trials),
                        "trials_per_frame": {"firewall": arm2_pf, "definiteness": per_frame("definiteness"),
                                             "length": per_frame("length")}}

    # (D) DISJOINTNESS FROM v1 U rep2 (the mag gate). Identity = the (verb, particle, noun) triple.
    prior_triples, prior_nouns = set(), set()
    for path in (V1_STIM, REP2_STIM):
        s = json.loads(path.read_text())
        for fr in s["frames"]:
            prior_triples.add((fr["verb"], fr["prt"], fr["noun"])); prior_nouns.add(fr["noun"])
    my_triples = [(fr["verb"], fr["prt"], fr["noun"]) for fr in frames]
    shared_triples = sorted(set(my_triples) & prior_triples)
    shared_nouns = sorted({fr["noun"] for fr in frames} & prior_nouns)
    dup_triples = sorted({t for t in my_triples if my_triples.count(t) > 1})
    dup_nouns = sorted({fr["noun"] for fr in frames if [f["noun"] for f in frames].count(fr["noun"]) > 1})
    report["checks"]["(D1) no mag (verb,prt,noun) triple shared with v1 U rep2"] = not shared_triples
    report["checks"]["(D1b) all 48 mag triples distinct within mag"] = not dup_triples
    report["checks"]["(D2) no mag object noun appears in v1 U rep2 noun set"] = not shared_nouns
    report["checks"]["(D2b) all 48 mag object nouns distinct within mag"] = not dup_nouns
    if shared_triples:
        report["fail"].append(f"(D1) triple(s) shared with prior: {shared_triples[:5]}")
    if dup_triples:
        report["fail"].append(f"(D1b) duplicate mag triple(s): {dup_triples[:5]}")
    if shared_nouns:
        report["fail"].append(f"(D2) noun(s) shared with prior: {shared_nouns[:5]}")
    if dup_nouns:
        report["fail"].append(f"(D2b) duplicate mag noun(s): {dup_nouns[:5]}")

    freq = json.loads(FREQ_JSON.read_text())["per_pair"]
    missing_cov, missing_lemma = [], []
    for fr in frames:
        lemma = VERB_LEMMA.get(fr["verb"])
        if lemma is None:
            missing_lemma.append(fr["verb"]); continue
        if f"{lemma}+{fr['prt'].lower()}" not in freq:
            missing_cov.append(f"{lemma}+{fr['prt']}")
    report["checks"]["(D3) every mag verb in the byte-frozen VERB_LEMMA"] = not missing_lemma
    report["checks"]["(D3) every mag (verb_lemma,prt) pair in the byte-frozen freq_control.json"] = not missing_cov
    if missing_lemma:
        report["fail"].append(f"(D3) verb(s) absent from VERB_LEMMA: {sorted(set(missing_lemma))}")
    if missing_cov:
        report["fail"].append(f"(D3) pair(s) absent from freq_control.json: {sorted(set(missing_cov))}")
    report["disjointness"] = {"n_prior_triples": len(prior_triples), "n_mag_triples": len(set(my_triples)),
                              "shared_triples": shared_triples, "shared_nouns": shared_nouns,
                              "n_distinct_pairs_used": len({(v, p) for v, p, _ in my_triples})}

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    return report


def main():
    frames, trials = build()
    stim = {
        "design": "verb-particle placement object-givenness graded forced-choice; within-frame "
                  "split-preference FIREWALL shift; ratified decisions/resolved/particle-placement-anchor-"
                  "and-indicator (s225); MAGNITUDE (mag) arm -- Arm 2 discourse-givenness firewall ONLY "
                  "(byte-identical scored strings, three-condition GIVEN/NEW-MENTIONED/NEW, decisive "
                  "GIVEN-NEW-MENTIONED, LOAD-BEARING). Arms 1 (definiteness) & 3 (length) DROPPED -- the "
                  "magnitude the claim owes is the firewall shift2 (genitive-MAG typical-only analog).",
        "context_template": CTX,
        "frames": frames,
        "trials": trials,
    }
    payload = json.dumps(stim, indent=2, ensure_ascii=False)
    (HERE / "stimuli.json").write_text(payload)
    sha = hashlib.sha256(payload.encode()).hexdigest()

    report = certify(frames, trials)
    report["stimuli_sha256"] = sha
    (HERE / "certification.json").write_text(json.dumps(report, indent=2))

    print(f"stimuli.json: {report['counts']}")
    print(f"stimuli_sha256: {sha}")
    print("CERTIFICATION:", "PASS" if report["ok"] else "FAIL")
    for k, v in report["checks"].items():
        print(f"  [{'OK' if v else 'XX'}] {k}")
    print("  max |Arm-2 within-frame shift| per scored-string reader:",
          report["max_abs_arm2_frame_shift_per_scored_reader"])
    if report["fail"]:
        print("  FAILURES:")
        for f in report["fail"]:
            print("   -", f)

    # self-audit dump: example scored strings + contexts
    print("\n--- example items (self-audit) ---")
    for fid in ("f01", "f25", "f40"):
        exs = [t for t in trials if t["frame"] == fid and t["split_is_a"]]
        fr = next(f for f in frames if f["id"] == fid)
        print(f"[{fid}] {fr['subj']} {fr['verb']} {fr['prt']} + '{fr['noun']}'")
        for t in exs:
            print(f"   {t['arm']}/{t['condition']}: joined='{t['joined']}' | split='{t['split']}'"
                  f"\n       ctx: {t['context']}")


if __name__ == "__main__":
    main()
