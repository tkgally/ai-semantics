#!/usr/bin/env python3
"""build_trials.py -- freeze the DAIS Option-B graded-preference correlation REP2 stimuli (s250).

FRESH-ITEM REPLICATION of the s248 result (result/dais-graded-preference-correlation-v1). The
INSTRUMENT is byte-frozen: probe.py + analyze.py are sha-identical to s248; common.py differs only in
the two budget hard-stop constants (documented in that file). The ONLY thing that changes here is the
project lexicalization set -- a fresh subject, fresh recipient realizations, fresh theme nouns, and a
fresh random Arm-B verb subset (new seed) -- so this is a genuine fresh-item re-run on disjoint
stimuli, not a re-run of the same items. The verb list (200 DAIS verbs), the human targets, the
canonical Arm-A condition (shortDefinite), the 5 factor levels, and every statistic/threshold/band are
UNCHANGED from s248.

Two disjointness firewalls (both asserted at build, both must PASS before freeze):
  1. vs DAIS (B3, s248's firewall, byte-identical logic): 0 verbatim stimulus collisions with DAIS's
     released sentences; project recipient realizations avoid DAIS's 5 canonicals; project theme heads
     avoid DAIS's 333 theme heads; subject disjoint from DAIS's 8.
  2. vs the s248 v1 stimuli (NEW, the replication firewall): 0 rep2 stimulus strings appear in the
     committed s248 stimuli.json; the rep2 subject / recipient realizations / theme heads are disjoint
     from v1's. This is what makes rep2 a FRESH-ITEM replication (the sense-gradience-rep2 / dative-
     powered "0 shared items" standard).

Design: experiments/designs/dais-graded-preference-correlation-v1.md (RATIFIED s247). The replication +
promotion route is named in the design's Q3 ("a claim ... needs a fresh-item replication + a
cross-session promotion review") and the s248 result's "What it feeds".
"""
import csv
import hashlib
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCOUT = os.path.abspath(os.path.join(HERE, "..", "2026-07-17-dais-license-scout"))
V1 = os.path.abspath(os.path.join(HERE, "..", "2026-07-18-dais-option-b"))
RAW_CSV = os.path.abspath(os.path.join(HERE, "..", "..", "data", "dais", "data_cleaned.csv"))
MEANS_CSV = os.path.join(SCOUT, "verb_recipient_means.csv")
V1_STIM = os.path.join(V1, "stimuli.json")

# Pinned sha256 of the raw DAIS CSV (re-fetch via the scout prep.py; gitignored, NOT in the repo).
CSV_SHA = "01ee1b163003e354cddf1c6c6be1b386123cbbce3424163bf198e9fbc4c251f9"

# ---- FRESH project lexicalizations (Q1-A; disjoint from DAIS AND from s248 v1) --------------
# Single fixed subject: disjoint from DAIS's 8 (Alice/Mary/Juan/Linda/John/Maria/Michael/Bob) AND
# from v1's `Nadia`.
SUBJECT = "Priya"

# The 5 recipient conditions realized with FRESH project nouns, faithful to DAIS's length x
# definiteness factor structure (paper ex.3) but lexically disjoint from BOTH DAIS's
# him/the man/a man/the man from work/a man from work AND v1's her/the girl/a girl/the girl from
# college/a girl from college. "clerk"!="man"!="girl"; "them"!="him"!="her"; "from downtown"!="from
# work"!="from college". Word count + definiteness matched EXACTLY to the factor levels; the
# within-length definiteness contrast and the pronoun anchor preserved. CANONICAL Arm-A condition =
# shortDefinite (the same neutral matched baseline across all 200 verbs, as in v1).
RECIPIENTS = {
    "pronoun":         "them",
    "shortDefinite":   "the clerk",
    "shortIndefinite": "a clerk",
    "longDefinite":    "the clerk from downtown",
    "longIndefinite":  "a clerk from downtown",
}
CONDITION_ORDER = ["pronoun", "shortDefinite", "shortIndefinite", "longDefinite", "longIndefinite"]
CANONICAL_ARMA = "shortDefinite"

# Human canonical direction (mean DOpreference DECREASING across the ordered conditions), UNCHANGED
# from v1 -- the firsthand-reproduced DAIS gradient pronoun 37.7 > shortDef 30.5 > shortIndef 25.2 >
# longDef 20.8 > longIndef 18.3. Ranks 5..1 aligned to CONDITION_ORDER.
HUMAN_DIRECTION_RANKS = [5, 4, 3, 2, 1]

# B1 -- Arm-B per-verb monotonicity predicate + its chance null p0 (FROZEN, UNCHANGED from v1).
ARMB_RHO_THRESHOLD = 0.50
ARMB_NULL_P0 = 27.0 / 120.0  # = 0.225

# Arm-B verb subset: a FRESH freeze-frozen random 40 of the 100 alternating verbs (NEW seed -> a
# genuinely independent subset from v1's, so Arm B is fresh in both fillers AND verb sample).
ARMB_N = 40
ARMB_SEED = 20260250

# ---- FRESH theme assignment (Q1-A; every theme head-noun disjoint from DAIS AND v1) ---------
# The theme is held FIXED across an item's 5 recipient conditions; it cancels between the DOC and PD
# phrasings and never enters the correlation. One neutral theme per broad semantic bucket. Every
# head-noun below is asserted absent from DAIS's 333 theme head-nouns AND from v1's 10 theme heads
# (parcel/frisbee/dividend/anecdote/warning/confidence/ballad/sketch/memo/riddle).
THEME = {
    "concrete":  "a crate",       # physical transfer / conveyance   (v1: a parcel)
    "ballistic": "a boomerang",   # throw / kick / propel            (v1: a frisbee)
    "money":     "a rebate",      # payment / benefactive / financial (v1: a dividend)
    "tell":      "a fable",       # general telling / reporting       (v1: an anecdote)
    "loud":      "an alert",      # shouting / yelling / signalling   (v1: a warning)
    "soft":      "a confession",  # whispering / muttering            (v1: a confidence)
    "sing":      "a hymn",        # singing / chanting / whistling    (v1: a ballad)
    "visual":    "a diagram",     # showing / displaying              (v1: a sketch)
    "written":   "a postcard",    # emailed / faxed / posted          (v1: a memo)
    "ask":       "a puzzle",      # interrogative-flavoured           (v1: a riddle)
}

# Explicit per-verb bucket assignment -- UNCHANGED from v1 (bucketing affects only theme felicity,
# never the measurement; keeping it identical means only the theme LEXEME differs per bucket).
BUCKETS = {
    # --- alternating (100) ---
    "concrete": ["took", "gave", "brought", "sent", "offered", "passed", "sold", "handed",
                 "slipped", "shipped", "lent", "loaned", "smuggled", "ferried", "bused",
                 "trucked", "carted", "shuttled", "drove", "flew", "rowed", "wheeled", "towed",
                 "hauled", "lugged", "dragged", "tugged", "pulled", "pushed", "shoved", "heaved",
                 "slung", "fed", "carried", "peddled"],
    "ballistic": ["threw", "tossed", "kicked", "hit", "shot", "rolled", "floated", "flipped",
                  "bounced", "flung", "chucked", "flicked", "hurled", "punted", "lobbed",
                  "catapulted", "batted", "slammed", "slapped", "snuck", "pitched", "slid"],
    "money": ["paid", "owed", "granted", "awarded", "traded", "tipped", "rented", "leased",
              "repaid", "allocated", "alloted", "assigned", "guaranteed", "extended", "willed",
              "ceded", "bequeathed", "conceded", "yielded", "refunded", "advanced"],
    "written": ["wrote", "posted", "emailed", "mailed", "phoned", "wired", "faxed", "relayed",
                "telephoned", "forwarded", "radioed", "cabled"],
    "tell": ["told", "read", "promised", "cited", "quoted", "preached", "taught"],
    "visual": ["showed"],
    "loud": ["signaled"],
    "ask": ["asked"],
    # --- non-alternating (100) ---
    "tell2": ["said", "reported", "explained", "stated", "mentioned", "addressed", "referred",
              "announced", "expressed", "recommended", "repeated", "declared", "proposed",
              "submitted", "communicated", "asserted", "described", "conveyed", "dictated",
              "articulated", "recounted", "narrated", "denounced", "recited", "explicated",
              "confessed", "admitted", "administered"],
    "concrete2": ["provided", "delivered", "supplied", "distributed", "transferred", "transported",
                  "dispatched", "furnished", "delegated", "entrusted", "surrendered", "restored",
                  "returned", "raised", "lowered", "dropped", "lifted"],
    "money_na": ["contributed", "donated", "credited", "reimbursed", "remitted", "forfeited"],
    "visual2": ["presented", "revealed", "introduced", "demonstrated", "illustrated", "exhibited",
                "displayed"],
    "loud2": ["screamed", "shouted", "yelled", "roared", "barked", "hollered", "bellowed",
              "shrieked", "squealed", "growled", "snapped", "snarled", "screeched", "tweeted",
              "broadcasted"],
    "soft": ["whispered", "muttered", "murmured", "mumbled", "moaned", "groaned", "whined",
             "grumbled", "stuttered", "stammered", "drawled", "hissed", "croaked",
             "babbled", "cackled", "chirped", "wailed", "howled", "grunted", "blabbed", "squeaked"],
    "sing": ["sang", "chanted", "crooned", "warbled", "yodeled", "whistled"],
}
BUCKET_THEME = {"concrete": "concrete", "concrete2": "concrete", "ballistic": "ballistic",
                "money": "money", "money_na": "money",
                "written": "written", "tell": "tell", "tell2": "tell", "ask": "ask",
                "loud": "loud", "loud2": "loud", "soft": "soft", "sing": "sing",
                "visual": "visual", "visual2": "visual"}


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def load_raw_dais():
    if not os.path.exists(RAW_CSV):
        sys.exit(f"REFUSING: raw DAIS not found at {RAW_CSV}. Re-fetch: "
                 f"python3 {SCOUT}/prep.py (sha256-pinned; gitignored).")
    blob = open(RAW_CSV, "rb").read()
    if sha256_bytes(blob) != CSV_SHA:
        sys.exit("REFUSING: raw DAIS sha256 mismatch -- release drifted.")
    return list(csv.DictReader(open(RAW_CSV)))


def verb_bucket_map():
    m = {}
    for bucket, verbs in BUCKETS.items():
        for v in verbs:
            if v in m:
                sys.exit(f"BUILD ERROR: verb {v!r} assigned to two buckets.")
            m[v] = bucket
    return m


def theme_for(verb, vbmap):
    return THEME[BUCKET_THEME[vbmap[verb]]]


def doc_pd(verb, theme, recipient):
    """DOC = 'Subj verb recipient theme .'  PD = 'Subj verb theme to recipient .' (DAIS frame)."""
    doc = f"{SUBJECT} {verb} {recipient} {theme}."
    pd = f"{SUBJECT} {verb} {theme} to {recipient}."
    return doc, pd


def main():
    rows = load_raw_dais()

    vinfo = {}
    for r in rows:
        vinfo[r["verb"]] = (r["classification"], int(r["frequency_rank"]))
    verbs = sorted(vinfo)
    assert len(verbs) == 200, f"expected 200 verbs, got {len(verbs)}"

    vbmap = verb_bucket_map()
    missing = [v for v in verbs if v not in vbmap]
    if missing:
        sys.exit(f"BUILD ERROR: {len(missing)} verbs unbucketed: {missing}")
    extra = [v for v in vbmap if v not in vinfo]
    if extra:
        sys.exit(f"BUILD ERROR: bucketed verbs not in DAIS: {extra}")

    # ---- B3(a) disjointness inputs from raw DAIS (NOT committed) --------------------------
    dais_strings = set()
    for r in rows:
        dais_strings.add(r["DOsentence"].strip())
        dais_strings.add(r["PDsentence"].strip())
    dais_theme_heads = set()
    for r in rows:
        m = re.search(r" to (.+)$", r["PDsentence"])
        if m:
            rest = r["PDsentence"][:m.start()].split(None, 2)
            if len(rest) == 3:
                dais_theme_heads.add(rest[2].split()[-1].lower().strip(".,"))
    dais_recipient_realizations = {"him", "the man", "a man", "the man from work", "a man from work"}
    dais_subjects = {r["DOsentence"].split()[0] for r in rows}

    # ---- REPLICATION firewall inputs: the committed s248 v1 stimuli (NEW) ------------------
    v1 = json.load(open(V1_STIM))
    v1_strings = set()
    for t in v1["trials"]:
        v1_strings.add(t["doc"].strip())
        v1_strings.add(t["pd"].strip())
    v1_subject = v1["subject"]
    v1_recipient_realizations = set(v1["recipients"].values())
    v1_theme_heads = set()
    for t in v1["trials"]:
        v1_theme_heads.add(t["theme"].split()[-1].lower())

    # ---- B3(a) assertions vs DAIS ----------------------------------------------------------
    for cond, real in RECIPIENTS.items():
        assert real not in dais_recipient_realizations, \
            f"RECIPIENT {cond}={real!r} collides with a DAIS canonical realization (B3)."
    project_theme_heads = {t.split()[-1].lower() for t in THEME.values()}
    theme_collisions_dais = project_theme_heads & dais_theme_heads
    assert not theme_collisions_dais, f"THEME heads collide with DAIS (B3): {theme_collisions_dais}"
    assert SUBJECT not in dais_subjects, f"SUBJECT {SUBJECT!r} collides with a DAIS subject."

    # ---- REPLICATION assertions vs v1 (fresh-item firewall) --------------------------------
    assert SUBJECT != v1_subject, f"SUBJECT {SUBJECT!r} equals v1 subject -- not a fresh item."
    recip_overlap_v1 = set(RECIPIENTS.values()) & v1_recipient_realizations
    assert not recip_overlap_v1, f"RECIPIENT realizations overlap v1 (not fresh): {recip_overlap_v1}"
    theme_overlap_v1 = project_theme_heads & v1_theme_heads
    assert not theme_overlap_v1, f"THEME heads overlap v1 (not fresh): {theme_overlap_v1}"

    # ---- build trials ----------------------------------------------------------------------
    cb = random.Random(ARMB_SEED + 1)
    trials = []
    tid = 0
    for v in verbs:
        theme = theme_for(v, vbmap)
        doc, pd = doc_pd(v, theme, RECIPIENTS[CANONICAL_ARMA])
        trials.append({"tid": f"A-{tid}", "arm": "A", "verb": v, "condition": CANONICAL_ARMA,
                       "bucket": vbmap[v], "theme": theme, "doc": doc, "pd": pd,
                       "doc_is_a": cb.random() < 0.5, "classification": vinfo[v][0]})
        tid += 1
    # Arm-B verb subset: sample from the alternating verbs NOT in v1's Arm-B subset, so the Arm-B
    # 40 are FULLY verb-disjoint from v1 (the s250 freeze-vote FRESHNESS condition -- 100 alternating
    # verbs, v1 used 40 => a 60-verb v1-disjoint pool). Makes Arm B fresh in items AND verb sample.
    alt_verbs = sorted(v for v in verbs if vinfo[v][0] == "alternating")
    v1_armb = set(v1["armb_verbs"])
    alt_pool = [v for v in alt_verbs if v not in v1_armb]
    assert len(alt_pool) >= ARMB_N, f"not enough v1-disjoint alternating verbs: {len(alt_pool)}"
    rng = random.Random(ARMB_SEED)
    armb_verbs = sorted(rng.sample(alt_pool, ARMB_N))
    assert not (set(armb_verbs) & v1_armb), "Arm-B verbs overlap v1's subset (freshness firewall)."
    for v in armb_verbs:
        theme = theme_for(v, vbmap)
        for cond in CONDITION_ORDER:
            doc, pd = doc_pd(v, theme, RECIPIENTS[cond])
            trials.append({"tid": f"B-{tid}", "arm": "B", "verb": v, "condition": cond,
                           "bucket": vbmap[v], "theme": theme, "doc": doc, "pd": pd,
                           "doc_is_a": cb.random() < 0.5, "classification": "alternating"})
            tid += 1

    # ---- B3(a) verbatim disjointness vs DAIS (the crux) ------------------------------------
    collisions = []
    for t in trials:
        for s in (t["doc"].strip(), t["pd"].strip()):
            if s in dais_strings:
                collisions.append(s)
    assert not collisions, f"VERBATIM COLLISION with DAIS sentences (B3): {collisions[:5]}"

    # ---- REPLICATION verbatim disjointness vs v1 (fresh-item crux) -------------------------
    v1_collisions = []
    for t in trials:
        for s in (t["doc"].strip(), t["pd"].strip()):
            if s in v1_strings:
                v1_collisions.append(s)
    assert not v1_collisions, f"VERBATIM COLLISION with v1 stimuli (not fresh): {v1_collisions[:5]}"

    # ---- human targets (from the COMMITTED derived table only) -----------------------------
    means = {}
    for r in csv.DictReader(open(MEANS_CSV)):
        means[(r["verb"], r["recipient_condition"])] = float(r["mean_DOpreference"])
    human_arma_matched = {v: means[(v, CANONICAL_ARMA)] for v in verbs}
    human_arma_collapsed = {v: sum(means[(v, c)] for c in CONDITION_ORDER) / 5.0 for v in verbs}
    human_armb = {v: {c: means[(v, c)] for c in CONDITION_ORDER} for v in armb_verbs}

    human_targets = {
        "canonical_arma_condition": CANONICAL_ARMA,
        "condition_order": CONDITION_ORDER,
        "human_direction_ranks": HUMAN_DIRECTION_RANKS,
        "armb_rho_threshold": ARMB_RHO_THRESHOLD,
        "armb_null_p0": ARMB_NULL_P0,
        "armb_verbs": armb_verbs,
        "human_arma_matched": human_arma_matched,
        "human_arma_collapsed": human_arma_collapsed,
        "human_armb": human_armb,
    }
    freq_control = {v: {"classification": vinfo[v][0], "frequency_rank_within_class": vinfo[v][1]}
                    for v in verbs}

    def wc(s):
        return len(s.split())
    fidelity = {
        "note": ("REP2 (s250). Each project recipient realization vs the DAIS factor level it "
                 "instantiates -- length (word count) and definiteness matched to DAIS's factor "
                 "structure; lexemes project-chosen and disjoint from BOTH DAIS and v1 (fresh-item "
                 "replication). Theme held fixed per verb across the 5 conditions -- only the recipient "
                 "moves."),
        "subject": SUBJECT,
        "conditions": [
            {"condition": c, "project_realization": RECIPIENTS[c],
             "dais_canonical_realization": r, "v1_realization": v1["recipients"][c],
             "project_wc": wc(RECIPIENTS[c]), "dais_wc": wc(r),
             "definiteness": ("pronoun" if c == "pronoun" else
                              ("definite" if "Definite" in c and "Indef" not in c else "indefinite")),
             "length_class": ("pronoun" if c == "pronoun" else
                              ("short" if c.startswith("short") else "long"))}
            for c, r in zip(CONDITION_ORDER,
                            ["him", "the man", "a man", "the man from work", "a man from work"])
        ],
        "within_length_definiteness_contrasts": {
            "short": ["shortDefinite", "shortIndefinite"],
            "long": ["longDefinite", "longIndefinite"],
        },
        "example_item_gave": {c: {"doc": doc_pd("gave", THEME["concrete"], RECIPIENTS[c])[0],
                                  "pd": doc_pd("gave", THEME["concrete"], RECIPIENTS[c])[1]}
                              for c in CONDITION_ORDER},
    }

    disjointness = {
        "raw_dais_csv_sha256": CSV_SHA,
        "n_dais_sentence_strings": len(dais_strings),
        "n_dais_theme_head_nouns": len(dais_theme_heads),
        "dais_canonical_recipient_realizations_avoided": sorted(dais_recipient_realizations),
        "project_recipient_realizations": RECIPIENTS,
        "project_theme_head_nouns": sorted(project_theme_heads),
        "verbatim_collision_count_vs_dais": len(collisions),
        "recipient_collision_vs_dais": False,
        "theme_head_collision_vs_dais": sorted(theme_collisions_dais),
        "subject_collision_vs_dais": SUBJECT in dais_subjects,
        # replication firewall vs v1
        "v1_stimuli_sha256": sha256_bytes(open(V1_STIM, "rb").read()),
        "v1_subject": v1_subject,
        "v1_recipient_realizations": sorted(v1_recipient_realizations),
        "v1_theme_head_nouns": sorted(v1_theme_heads),
        "verbatim_collision_count_vs_v1": len(v1_collisions),
        "recipient_overlap_vs_v1": sorted(recip_overlap_v1),
        "theme_head_overlap_vs_v1": sorted(theme_overlap_v1),
        "subject_equals_v1": SUBJECT == v1_subject,
        "armb_verbs_shared_with_v1": sorted(set(armb_verbs) & set(v1["armb_verbs"])),
        "assertion": ("PASS -- no rep2 stimulus string, recipient realization, or theme head-noun "
                      "appears in DAIS's released sentences/factor realizations (B3) OR in the s248 v1 "
                      "stimuli (fresh-item replication firewall)."),
    }

    stim = {
        "design": "dais-graded-preference-correlation-v1",
        "replication_of": "result/dais-graded-preference-correlation-v1 (s248)",
        "session": 250,
        "subject": SUBJECT,
        "recipients": RECIPIENTS,
        "condition_order": CONDITION_ORDER,
        "canonical_arma_condition": CANONICAL_ARMA,
        "armb_verbs": armb_verbs,
        "armb_seed": ARMB_SEED,
        "n_arm_a": sum(1 for t in trials if t["arm"] == "A"),
        "n_arm_b": sum(1 for t in trials if t["arm"] == "B"),
        "trials": trials,
    }

    for name, obj in [("stimuli.json", stim), ("human_targets.json", human_targets),
                      ("freq_control.json", freq_control),
                      ("fidelity_audit.json", fidelity),
                      ("disjointness_manifest.json", disjointness)]:
        json.dump(obj, open(os.path.join(HERE, name), "w"), indent=2, sort_keys=True)

    print(f"BUILT: {stim['n_arm_a']} Arm-A + {stim['n_arm_b']} Arm-B trials "
          f"({stim['n_arm_a'] + stim['n_arm_b']} items x 3 models = "
          f"{(stim['n_arm_a'] + stim['n_arm_b']) * 3} calls).")
    print(f"Arm-B verbs ({ARMB_N}, seed {ARMB_SEED}): {armb_verbs}")
    print(f"Arm-B verbs shared with v1 subset: "
          f"{sorted(set(armb_verbs) & set(v1['armb_verbs']))}")
    print(f"DAIS firewall: {len(collisions)} verbatim / v1 firewall: {len(v1_collisions)} verbatim.")
    on_disk = sha256_bytes(open(os.path.join(HERE, "stimuli.json"), "rb").read())
    print(f"stimuli.json (on-disk) sha256 = {on_disk}")


if __name__ == "__main__":
    main()
