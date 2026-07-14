#!/usr/bin/env python3
"""Build + certify + freeze the VERB-PARTICLE-PLACEMENT object-givenness stimuli -- REP2, the FRESH-ITEM
powered replication (program A5, 3rd sibling; session 228).

WHY THIS RUN. v1 (2026-07-14-particle-placement-givenness, s225/s226) was PANEL CONFIRM but a SINGLE run,
so it earned no `claim` (PROTOCOL §3 promotes only REPLICATED ∧ controls-survived). This rep2 re-tests
the given/definite-object -> SPLIT direction + the byte-identical discourse-givenness firewall survival on
DISJOINT items, and -- the genitive-rep2 (s220) move -- ENLARGES the load-bearing firewall arm (40 -> 48
frames) to power the marginal gpt firewall leg (v1: gpt firewall +0.018, CI [-0.017,0.055], a pre-named
SHADOW). A second independent run + surviving controls is the path a cross-session promotion review needs
to write a direction-only particle `claim` and migrate the shadow-depth-table-v4 row result-cited ->
claim-cited.

BYTE-FROZEN INSTRUMENT (sha-verified identical to v1): probe.py, analyze.py, build_cooc_particle.py,
freq_control.json (the covariate is UNCHANGED -- every rep2 verb+particle pair is drawn from v1's frozen
38-pair set, so freq_control.json's per-pair keys and analyze.py's VERB_LEMMA cover every frame). common.py
differs ONLY in HARD_STOP_USD (3.50 -> 3.80; the item count grew, documented in-file). NEW here: this
build_items.py (fresh disjoint FRAMES) + a certification check (D) proving triple-disjointness from v1.
NO NEW DECISION -- a within-design powered re-run under the resolved decision
particle-placement-anchor-and-indicator (s225); the dative-s175 / genitive-rep2-s220 pattern.

RATIFIED design: decisions/resolved/particle-placement-anchor-and-indicator (s225, ADOPT-WITH-
MODIFICATION Q1-A / Q2-i / Q3 human-anchored on direction; + binding freeze conditions R1-R7 and the
s224 freeze conditions (i)-(x)). Instrument: graded forced-choice (port of the validated dative/genitive
instrument) -- hold verb + particle + object head-noun fixed, distribute 100 points by naturalness
between the JOINED order ("picked up the box", V-Prt-DO) and the SPLIT order ("picked the box up",
V-DO-Prt). split-pref = split_pts/(split_pts+joined_pts).

FINDING-BEARING MEASURES: within-FRAME shifts (a frame = a fixed verb+particle+object-head-noun).
  Arm 1 (definiteness, anchor-exact, CONFOUNDABLE, NOT decisive):
      shift1(frame) = mean(split-pref | definite "the box") - mean(split-pref | indefinite "a box")
  Arm 2 (discourse-givenness FIREWALL, byte-identical scored strings, LOAD-BEARING, three conditions):
      shift2(frame) = mean(split-pref | GIVEN) - mean(split-pref | NEW-MENTIONED)   [decisive]
      + descriptive GIVEN - NEW
  Arm 3 (length, convergent-validity leg, SECONDARY, non-gating -- R5):
      shift3(frame) = mean(split-pref | short "the box") - mean(split-pref | long "the box <heavy NP>")
Human direction (Kim et al. 2016 / Gries 1999): definite/given/short object -> SPLIT, so shift > 0.

WHY ARM 2 IS THE LOAD-BEARING CONTROL. In Arm 2 the object string is held BYTE-IDENTICAL ("the <noun>")
across GIVEN / NEW-MENTIONED / NEW; the givenness manipulation lives ONLY in the preceding discourse
context. So the two scored order-strings ("<V> <Prt> the <noun>" / "<V> the <noun> <Prt>") are
byte-identical across the three conditions -> ANY reader whose split-preference depends only on the
scored strings (always-split / always-joined / string-frequency / determiner-collocation / position)
yields within-frame shift2 = 0 BY CONSTRUCTION (certified below). A non-zero shift2 can only come from
integrating the discourse context. The THREE-condition design (B-crit-1 / R2): GIVEN and NEW-MENTIONED
both mention the object NOUN at matched recency (one token, one sentence prior), differing only in
whether the SCORED referent is evoked-and-topical (GIVEN) vs referentially new (NEW-MENTIONED, the noun
appears only in a gnomic/generic clause that introduces no token) -> the decisive GIVEN - NEW-MENTIONED
contrast holds object-noun lexical priming/recency CONSTANT and isolates REFERENTIAL givenness, not mere
lexical recency. The NEW condition (noun absent) is descriptive only.

CONTEXT PARALLELISM (freeze (viii), R2, R3). The three context sentences per frame are generated from a
single parallel template-triple: matched clause count (2), sentence type (declarative), one comma,
matched word count (GIVEN 14 / NEW-MENTIONED 14 / NEW 14 incl. the subject token), the object noun
appearing exactly once in GIVEN and NEW-MENTIONED and zero times in NEW, and NO verb-particle / no
fronting / clefting / topicalization / passive / heavy-NP of the object in any context (no
answer-leakage, no structural-priming leak). The definite scored object is a standard narrative definite
in all three (anaphoric in GIVEN, accommodated-situational in NEW-MENTIONED and NEW) -- comparable
felicity (R3). This parallelism is INDEPENDENTLY certified (a non-authoring agent) before freeze; if it
cannot be guaranteed, the run defers or falls to the Option-B two-condition rescope (R7).

Outputs: stimuli.json (frozen, sha-pinned in PREREG) + a printed certification report.
Run: python3 build_items.py
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
# v1's frozen stimuli (for the (D) disjointness check) + this dir's byte-frozen covariate.
V1_STIM = HERE.parent / "2026-07-14-particle-placement-givenness" / "stimuli.json"
FREQ_JSON = HERE / "freq_control.json"
# VERB_LEMMA mirrors the byte-frozen analyze.py (past-tense form -> lemma) for the (D3) coverage check;
# analyze.py itself imports numpy, so we copy the dict rather than import it (build_items has no numpy dep).
VERB_LEMMA = {
    "picked": "pick", "put": "put", "took": "take", "threw": "throw", "pulled": "pull",
    "wiped": "wipe", "hung": "hang", "locked": "lock", "folded": "fold", "rolled": "roll",
    "packed": "pack", "wrapped": "wrap", "carried": "carry", "set": "set", "lifted": "lift",
    "handed": "hand", "cleared": "clear", "shut": "shut", "brought": "bring", "turned": "turn",
    "cut": "cut", "hauled": "haul",
}

# ---------------------------------------------------------------------------
# 48 FRESH DISJOINT FRAMES (rep2). Each: a subject NAME (distinct, none is the monitor's), a literal
# SEPARABLE transitive phrasal verb (past tense) + particle, a concrete INANIMATE count-noun object head,
# and a heavy-NP long modifier (Arm 3 long object). Same authoring discipline as v1: all full lexical NPs
# (no pronouns -- pronominal objects are near-categorically split, a categorical not graded fact);
# concreteness + animacy + (within frame) VP idiomaticity held constant across every arm/condition; all
# canonical separable phrasal verbs natural in BOTH orders with a definite full-NP object (Kim et al.
# 2016 / Gries 1999).
#
# DISJOINTNESS + BYTE-FROZEN COVARIATE (the two rep2 constraints, both certified below):
#  * Every (verb, particle) pair is drawn from v1's frozen 38-pair set (so freq_control.json's per-pair
#    keys and analyze.py's VERB_LEMMA -- both byte-frozen -- cover every frame). 10 flexible pairs recur
#    with a SECOND distinct fresh noun to reach 48 frames (the firewall enlargement); a frame's identity
#    is the (verb, particle, noun) TRIPLE, so recurrence with a new noun is a new frame.
#  * Every object noun is FRESH -- disjoint from v1's noun set -- so all 48 (verb, particle, noun) triples
#    are disjoint from v1's 40 (certification check (D)).
# fields: subj, verb, prt, noun, long  (long = the heavy postmodifier appended after "the <noun>")
# ---------------------------------------------------------------------------
FRAMES = [
    dict(id="f01", subj="Tariq",   verb="brought", prt="in",    noun="hamper",   long="of linen from the landing"),
    dict(id="f02", subj="Sanne",   verb="carried", prt="down",  noun="sack",     long="of grain from the loft"),
    dict(id="f03", subj="Mateo",   verb="carried", prt="in",    noun="urn",      long="that had stood on the porch"),
    dict(id="f04", subj="Yuki",    verb="carried", prt="off",   noun="platter",  long="still heaped with pastries"),
    dict(id="f05", subj="Fatima",  verb="cleared", prt="away",  noun="bowl",     long="smeared with dried paint"),
    dict(id="f06", subj="Lars",    verb="cleared", prt="off",   noun="saucer",   long="ringed with old coffee stains"),
    dict(id="f07", subj="Camila",  verb="cut",     prt="off",   noun="cord",     long="fraying near the wall socket"),
    dict(id="f08", subj="Idris",   verb="folded",  prt="up",    noun="quilt",    long="spread across the low couch"),
    dict(id="f09", subj="Noor",    verb="handed",  prt="over",  noun="ledger",   long="filled with unsettled accounts"),
    dict(id="f10", subj="Sven",    verb="hung",    prt="up",    noun="apron",    long="spattered from the morning's baking"),
    dict(id="f11", subj="Anika",   verb="hauled",  prt="up",    noun="keg",      long="from the flooded cellar"),
    dict(id="f12", subj="Pedro",   verb="lifted",  prt="off",   noun="grille",   long="clogged with autumn leaves"),
    dict(id="f13", subj="Rania",   verb="lifted",  prt="up",    noun="hatch",    long="set into the workshop floor"),
    dict(id="f14", subj="Emil",    verb="locked",  prt="up",    noun="chest",    long="packed with the winter blankets"),
    dict(id="f15", subj="Saana",   verb="packed",  prt="away",  noun="hammock",  long="slung between the two posts"),
    dict(id="f16", subj="Viktor",  verb="packed",  prt="up",    noun="canvas",   long="rolled against the studio wall"),
    dict(id="f17", subj="Leyla",   verb="picked",  prt="out",   noun="pebble",   long="wedged in the boot's tread"),
    dict(id="f18", subj="Kai",     verb="picked",  prt="up",    noun="barrel",   long="left standing by the gate"),
    dict(id="f19", subj="Marta",   verb="pulled",  prt="down",  noun="curtain",  long="faded along its upper hem"),
    dict(id="f20", subj="Hassan",  verb="pulled",  prt="off",   noun="sticker",  long="stuck fast to the windscreen"),
    dict(id="f21", subj="Britta",  verb="pulled",  prt="out",   noun="peg",      long="driven deep into the turf"),
    dict(id="f22", subj="Rui",     verb="put",     prt="away",  noun="flask",    long="still warm from the tea"),
    dict(id="f23", subj="Zainab",  verb="put",     prt="back",  noun="pitcher",  long="that lived on the dresser"),
    dict(id="f24", subj="Anders",  verb="put",     prt="down",  noun="pot",      long="heavy with simmering stew"),
    dict(id="f25", subj="Carmen",  verb="put",     prt="out",   noun="lantern",  long="swinging from the low beam"),
    dict(id="f26", subj="Pavel",   verb="rolled",  prt="out",   noun="mat",      long="kept behind the front door"),
    dict(id="f27", subj="Ines",    verb="rolled",  prt="up",    noun="blanket",  long="left crumpled on the bench"),
    dict(id="f28", subj="Malik",   verb="set",     prt="down",  noun="vase",     long="brimming with cut peonies"),
    dict(id="f29", subj="Freya",   verb="set",     prt="up",    noun="tripod",   long="borrowed for the evening shoot"),
    dict(id="f30", subj="Otto",    verb="shut",    prt="off",   noun="tap",      long="dripping over the stone sink"),
    dict(id="f31", subj="Salma",   verb="took",    prt="apart", noun="clock",    long="that had stopped in the night"),
    dict(id="f32", subj="Nikolai", verb="took",    prt="down",  noun="portrait", long="hung above the cold hearth"),
    dict(id="f33", subj="Elin",    verb="took",    prt="off",   noun="cap",      long="screwed tight on the flask"),
    dict(id="f34", subj="Jamal",   verb="took",    prt="out",   noun="canister", long="shelved above the spare tins"),
    dict(id="f35", subj="Agnes",   verb="threw",   prt="out",   noun="wrapper",  long="balled up beside the till"),
    dict(id="f36", subj="Bilal",   verb="turned",  prt="off",   noun="burner",   long="glowing under the empty pan"),
    dict(id="f37", subj="Katya",   verb="wiped",   prt="off",   noun="blade",    long="dulled by the garden soil"),
    dict(id="f38", subj="Tobias",  verb="wrapped", prt="up",    noun="bundle",   long="bound for the morning post"),
    dict(id="f39", subj="Amina",   verb="picked",  prt="up",    noun="jug",      long="left on the scrubbed table"),
    dict(id="f40", subj="Rasmus",  verb="put",     prt="down",  noun="tin",      long="dented at one worn corner"),
    dict(id="f41", subj="Neha",    verb="took",    prt="out",   noun="bottle",   long="chilling in the door rack"),
    dict(id="f42", subj="Georg",   verb="lifted",  prt="up",    noun="grate",    long="set over the drain channel"),
    dict(id="f43", subj="Dalia",   verb="pulled",  prt="off",   noun="label",    long="curling at its gummed edge"),
    dict(id="f44", subj="Miro",    verb="set",     prt="up",    noun="screen",   long="used for the slide talks"),
    dict(id="f45", subj="Suki",    verb="hung",    prt="up",    noun="towel",    long="damp from the afternoon swim"),
    dict(id="f46", subj="Bjorn",   verb="carried", prt="off",   noun="pallet",   long="stacked with empty jars"),
    dict(id="f47", subj="Reza",    verb="cleared", prt="away",  noun="mug",      long="cold since the early meeting"),
    dict(id="f48", subj="Hedda",   verb="took",    prt="off",   noun="shade",    long="clipped over the reading lamp"),
]

# ---------------------------------------------------------------------------
# Arm-2 CONTEXT TEMPLATE-TRIPLE (parallel by construction; freeze (viii)/R2/R3). {noun} and {subj}
# filled per frame. GIVEN evokes + topicalizes the object referent (discourse-given); NEW-MENTIONED
# mentions the object NOUN in a gnomic/generic clause that introduces NO token (noun primed, referent
# new); NEW mentions neither the noun nor a token (referent new, noun not primed). Matched: 2 clauses,
# 1 comma, declarative, 14 words each (incl. the subject token); the object noun appears exactly once
# in GIVEN and NEW-MENTIONED and zero times in NEW; NO verb-particle, fronting, clefting, passive, or
# heavy-NP of the object in any context.
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
    frames, trials = [], []
    for fr in FRAMES:
        subj, verb, prt, noun = fr["subj"], fr["verb"], fr["prt"], fr["noun"]
        the_np = f"the {noun}"
        a_np = f"a {noun}"
        long_np = f"the {noun} {fr['long']}"
        frames.append(dict(fr, arms={"definiteness": ["definite", "indefinite"],
                                     "firewall": ARM2_LEVELS, "length": ["short", "long"]}))

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

        # Arm 1 -- definiteness (no discourse context; the object string itself varies)
        emit("definiteness", "definite", the_np, None)
        emit("definiteness", "indefinite", a_np, None)
        # Arm 2 -- firewall (byte-identical "the <noun>"; context varies)
        for lv in ARM2_LEVELS:
            ctx = CTX[lv].format(noun=noun, subj=subj)
            emit("firewall", lv, the_np, ctx)
        # Arm 3 -- length (no discourse context; object length varies)
        emit("length", "short", the_np, None)
        emit("length", "long", long_np, None)
    return frames, trials


# ---------------------------------------------------------------------------
# CERTIFICATION. Prove: (1) Arm-2 scored strings BYTE-IDENTICAL across given/newment/new within every
# frame (so any scored-string reader yields within-frame shift2 = 0); (2) enumerated scored-string
# shortcut readers each yield within-frame Arm-2 shift 0 on EVERY frame (by construction); (3) Arm-2
# context parallelism: within each frame the three contexts share clause count, comma count, sentence
# type, and word count, the object noun appears once in given & newment and zero times in new, and no
# context carries a verb-particle / fronting / heavy-NP of the object; (4) all objects full lexical NP
# (no pronoun), inanimate, non-empty; (5) counts (>=40 frames; Arm-2 firewall trials/frame >= Arm-1
# definiteness trials/frame -- the load-bearing arm >= the confoundable arm). Arms 1 & 3 scored strings
# DO differ across conditions by design (confoundable / convergent), so surface readers are NOT immune
# there -- stated, not certified-immune (the genitive typical-arm analog).
# ---------------------------------------------------------------------------
PRONOUNS = {"it", "him", "her", "them", "this", "that", "these", "those", "one"}
# particle words that would signal a placement cue if they sat next to an object in a context
PARTICLE_WORDS = {"up", "down", "off", "out", "in", "over", "away", "back", "apart", "on"}


def scored_readers():
    # each maps a TRIAL to a split-preference in [0,1] from the SCORED STRINGS/AB ONLY (never context).
    return {
        "always_split":  lambda t: 1.0,
        "always_joined": lambda t: 0.0,
        "always_A":      lambda t: 1.0 if t["split_is_a"] else 0.0,
        "always_B":      lambda t: 0.0 if t["split_is_a"] else 1.0,
        "position_A_bias": lambda t: 0.7 if t["split_is_a"] else 0.3,
        # length reader: prefers the shorter option string (end-weight analog on the scored strings)
        "len_shorter_split": lambda t: 1.0 if len(t["split"]) <= len(t["joined"]) else 0.0,
        # object-string reader: keys only on the scored object NP (definite/indefinite/length)
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
        # clause count proxy = comma-separated + coordinated finite clauses -> here every template has
        # exactly one comma splitting two finite clauses; check comma count == 1 and word count equal
        commas = {c.count(",") for c in ctxs.values()}
        if commas != {1}:
            comma_ok = False; report["fail"].append(f"(3) comma count != 1 uniformly in {fr['id']}: {commas}")
        wcs = {wc(c) for c in ctxs.values()}
        if len(wcs) != 1:
            wc_ok = False; report["fail"].append(f"(3) word count mismatch in {fr['id']}: "
                                                 f"{{lv: wc(c) for lv,c in ctxs.items()}} -> {wcs}")
        # every template is two declarative finite clauses joined by a coordinator (and/or) -> proxy:
        # ends with '.', no '?' or '!'
        if any(c.rstrip().endswith(("?", "!")) for c in ctxs.values()):
            clause_ok = False; report["fail"].append(f"(3) non-declarative context in {fr['id']}")
        # noun appears exactly once in given & newment, zero in new (word-boundary, lowercased)
        def noun_count(s):
            return len(re.findall(r"\b" + re.escape(noun) + r"\b", s.lower()))
        ng, nm, nn = noun_count(ctxs["given"]), noun_count(ctxs["newment"]), noun_count(ctxs["new"])
        if not (ng == 1 and nm == 1 and nn == 0):
            noun_ok = False
            report["fail"].append(f"(3) noun-mention pattern wrong in {fr['id']}: "
                                  f"given={ng} newment={nm} new={nn} (want 1/1/0)")
        # no verb-particle / no object-noun-adjacent particle word in any context (answer-leakage guard)
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

    # (5) counts + arm power
    def per_frame(arm):
        return len([t for t in trials if t["frame"] == frames[0]["id"] and t["arm"] == arm])
    n_frames = len(frames)
    arm2_pf, arm1_pf = per_frame("firewall"), per_frame("definiteness")
    report["checks"]["(N) >=40 frames"] = n_frames >= 40
    report["checks"]["(N) Arm-2 firewall trials/frame >= Arm-1 definiteness trials/frame (R7 / freeze iv)"] = arm2_pf >= arm1_pf
    report["counts"] = {"n_frames": n_frames, "n_trials": len(trials),
                        "trials_per_frame": {"definiteness": arm1_pf, "firewall": arm2_pf,
                                             "length": per_frame("length")}}

    # (D) DISJOINTNESS FROM v1 (the rep2 gate). A frame's identity is the (verb, particle, noun) triple.
    # Assert (D1) no rep2 triple equals any v1 triple; (D2) no rep2 object noun appears in v1's noun set
    # (the stronger item-freshness guarantee); (D3) every rep2 (verb_lemma, particle) pair is present in
    # the byte-frozen freq_control.json per-pair keys AND its verb is in analyze.py's VERB_LEMMA (so the
    # byte-frozen covariate + analysis cover every frame). D1/D2 read v1's frozen stimuli.json directly.
    v1_stim = json.loads(V1_STIM.read_text())
    v1_triples = {(fr["verb"], fr["prt"], fr["noun"]) for fr in v1_stim["frames"]}
    v1_nouns = {fr["noun"] for fr in v1_stim["frames"]}
    my_triples = [(fr["verb"], fr["prt"], fr["noun"]) for fr in frames]
    shared_triples = sorted(set(my_triples) & v1_triples)
    shared_nouns = sorted({fr["noun"] for fr in frames} & v1_nouns)
    dup_triples = sorted({t for t in my_triples if my_triples.count(t) > 1})
    report["checks"]["(D1) no rep2 (verb,prt,noun) triple shared with v1"] = not shared_triples
    report["checks"]["(D1b) all 48 rep2 triples distinct within rep2"] = not dup_triples
    report["checks"]["(D2) no rep2 object noun appears in v1's noun set"] = not shared_nouns
    if shared_triples:
        report["fail"].append(f"(D1) triple(s) shared with v1: {shared_triples[:5]}")
    if dup_triples:
        report["fail"].append(f"(D1b) duplicate rep2 triple(s): {dup_triples[:5]}")
    if shared_nouns:
        report["fail"].append(f"(D2) noun(s) shared with v1: {shared_nouns[:5]}")

    freq = json.loads(FREQ_JSON.read_text())["per_pair"]
    missing_cov, missing_lemma = [], []
    for fr in frames:
        lemma = VERB_LEMMA.get(fr["verb"])
        if lemma is None:
            missing_lemma.append(fr["verb"])
            continue
        if f"{lemma}+{fr['prt'].lower()}" not in freq:
            missing_cov.append(f"{lemma}+{fr['prt']}")
    report["checks"]["(D3) every rep2 verb in the byte-frozen VERB_LEMMA"] = not missing_lemma
    report["checks"]["(D3) every rep2 (verb_lemma,prt) pair in the byte-frozen freq_control.json"] = not missing_cov
    if missing_lemma:
        report["fail"].append(f"(D3) verb(s) absent from VERB_LEMMA: {sorted(set(missing_lemma))}")
    if missing_cov:
        report["fail"].append(f"(D3) pair(s) absent from freq_control.json: {sorted(set(missing_cov))}")
    report["disjointness"] = {"n_v1_triples": len(v1_triples), "n_rep2_triples": len(set(my_triples)),
                              "shared_triples": shared_triples, "shared_nouns": shared_nouns,
                              "n_distinct_pairs_reused": len({(v, p) for v, p, _ in my_triples})}

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    return report


def main():
    frames, trials = build()
    stim = {
        "design": "verb-particle placement object-givenness graded forced-choice; within-frame "
                  "split-preference shifts; ratified decisions/resolved/particle-placement-anchor-and-"
                  "indicator (s225); Arm 1 definiteness (anchor-exact, confoundable) + Arm 2 discourse-"
                  "givenness firewall (byte-identical scored strings, three-condition GIVEN/NEW-MENTIONED/"
                  "NEW, decisive GIVEN-NEW-MENTIONED, LOAD-BEARING shortcut control) + Arm 3 length "
                  "(convergent-validity leg, SECONDARY, non-gating).",
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

    # self-audit dump (freeze ix): example scored strings + contexts per arm
    print("\n--- example items (self-audit) ---")
    for fid in ("f01", "f23"):
        exs = [t for t in trials if t["frame"] == fid and t["split_is_a"]]
        fr = next(f for f in frames if f["id"] == fid)
        print(f"[{fid}] {fr['subj']} {fr['verb']} {fr['prt']} + '{fr['noun']}'")
        for t in exs:
            ctx = f"   ctx: {t['context']}" if t["context"] else ""
            print(f"   {t['arm']}/{t['condition']}: joined='{t['joined']}' | split='{t['split']}'{ctx}")


if __name__ == "__main__":
    main()
