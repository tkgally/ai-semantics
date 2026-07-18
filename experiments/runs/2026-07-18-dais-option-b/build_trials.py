#!/usr/bin/env python3
"""build_trials.py -- freeze the DAIS Option-B graded-preference correlation stimuli (s248).

Design: experiments/designs/dais-graded-preference-correlation-v1.md (RATIFIED s247,
Q1-A/Q2-A/Q3-A + freeze BLOCKERS B1-B3 / SHOULD-FIX S1-S3;
decisions/resolved/dais-graded-preference-correlation-design.md).

WHAT THIS PRODUCES (all committed; NO raw DAIS rows ever committed):
  stimuli.json          -- Arm A (200 verbs x 1 canonical condition) + Arm B (40 alt verbs x 5
                           conditions) trials; project-constructed DOC/PD phrasings.
  human_targets.json    -- per-verb + per-(verb,condition) human mean DOpreference (from the
                           committed verb_recipient_means.csv only) + the Arm-B monotonicity target
                           order + the pinned null p0 (B1).
  freq_control.json     -- per-verb classification + within-class frequency_rank (Arm-A B2 control);
                           AGGREGATE per-verb only, never raw sentence rows.
  fidelity_audit.json   -- B3(b): the 5 recipient conditions' project realization pinned + a
                           per-condition length/definiteness audit vs DAIS's factor structure.
  disjointness_manifest.json -- B3(a): verbatim + recipient-lexicalization + theme-head disjointness
                           assertions vs the gitignored raw DAIS sentences.

Q1-A (contamination-safe): DAIS supplies ONLY the verb list + the human ratings. Every DOC/PD
string is built from PROJECT-chosen subject / recipient / theme lexicalizations. A freeze-time
assertion confirms no stimulus string appears verbatim in DAIS's released DOsentence/PDsentence,
that the 5 project recipient realizations avoid DAIS's canonical him/the man/a man/the man from
work/a man from work, and that no project theme head-noun sits in DAIS's 333 theme heads (B3).
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
RAW_CSV = os.path.abspath(os.path.join(HERE, "..", "..", "data", "dais", "data_cleaned.csv"))
MEANS_CSV = os.path.join(SCOUT, "verb_recipient_means.csv")

# Pinned sha256 of the raw DAIS CSV (re-fetch via the scout prep.py; gitignored, NOT in the repo).
CSV_SHA = "01ee1b163003e354cddf1c6c6be1b386123cbbce3424163bf198e9fbc4c251f9"

# ---- FROZEN project lexicalizations (Q1-A; disjoint from DAIS -- B3) ------------------------
# Single fixed subject, disjoint from DAIS's 8 (Alice/Mary/Juan/Linda/John/Maria/Michael/Bob).
SUBJECT = "Nadia"

# The 5 recipient conditions realized with PROJECT nouns, faithful to DAIS's length x definiteness
# factor structure (paper ex.3) but lexically disjoint from DAIS's him/the man/a man/the man from
# work/a man from work. "girl"!="man"; "her"!="him"; "from college"!="from work". The within-length
# definiteness contrast (shortDef vs shortIndef; longDef vs longIndef) and the pronoun anchor are
# preserved exactly. CANONICAL Arm-A condition = shortDefinite (a mid-surface neutral baseline,
# the SAME across all 200 verbs).
RECIPIENTS = {
    "pronoun":        "her",
    "shortDefinite":  "the girl",
    "shortIndefinite": "a girl",
    "longDefinite":   "the girl from college",
    "longIndefinite": "a girl from college",
}
CONDITION_ORDER = ["pronoun", "shortDefinite", "shortIndefinite", "longDefinite", "longIndefinite"]
CANONICAL_ARMA = "shortDefinite"

# Human canonical direction (mean DOpreference DECREASING across the ordered conditions -- the
# firsthand-reproduced DAIS gradient pronoun 37.7 > shortDef 30.5 > shortIndef 25.2 > longDef 20.8
# > longIndef 18.3). Ranks 5..1 aligned to CONDITION_ORDER.
HUMAN_DIRECTION_RANKS = [5, 4, 3, 2, 1]

# B1 -- Arm-B per-verb monotonicity predicate + its chance null p0 (FROZEN, computed exactly).
# SUCCESS(verb) := Spearman rho_s(model 5 condition-mean DO-prefs, HUMAN_DIRECTION_RANKS) >= +0.50.
# NULL p0 := P(rho_s >= 0.50 | model condition means a uniform random permutation of 5 distinct
# values) = 27/120 = 0.225 (enumerated over all 120 permutations; see PREREG). A verb whose 5
# condition means are ALL TIED (rho_s undefined) counts as a NON-success (a flat gradient is not
# monotone-in-human-direction). The per-model per-verb success RATE over the 40 Arm-B verbs is
# tested one-sided binomial H0: rate <= p0.
ARMB_RHO_THRESHOLD = 0.50
ARMB_NULL_P0 = 27.0 / 120.0  # = 0.225

# Arm-B verb subset: a freeze-frozen random 40 of the 100 alternating verbs (fixed seed).
ARMB_N = 40
ARMB_SEED = 20260718

# ---- FROZEN theme assignment (Q1-A; every theme head-noun disjoint from DAIS -- B3) ---------
# The theme is held FIXED across an item's 5 recipient conditions, so ONLY the recipient factor
# moves. The theme cancels between the DOC and PD phrasings of a verb (same theme both sides), so
# its role is to make the pair well-formed and interpretable; it never enters the correlation. One
# neutral theme per broad semantic bucket keeps the fidelity audit trivial. Every head-noun below
# is asserted absent from DAIS's 333 theme head-nouns at build time.
THEME = {
    "concrete":  "a parcel",     # physical transfer / conveyance
    "ballistic": "a frisbee",    # throw / kick / propel
    "money":     "a dividend",   # payment / benefactive / financial
    "tell":      "an anecdote",  # general telling / reporting / narrating
    "loud":      "a warning",    # shouting / yelling / signalling
    "soft":      "a confidence",  # whispering / muttering / low vocalizing
    "sing":      "a ballad",     # singing / chanting / whistling
    "visual":    "a sketch",     # showing / displaying / demonstrating
    "written":   "a memo",       # emailed / faxed / posted / transmitted
    "ask":       "a riddle",     # interrogative-flavoured
}

# Explicit per-verb bucket assignment (past-tense forms, matching DAIS's `verb` column). Curated by
# semantics; audited by reading the generated sentences (fidelity_audit + a spot read). Every one of
# the 200 DAIS verbs is assigned. Bucketing affects only theme felicity, never the measurement.
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
    """Read the gitignored raw DAIS CSV (re-fetch via the scout prep.py). Returns rows; verifies
    the pinned sha256 so the freeze is against the exact catalogued release."""
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

    # verb -> (classification, within-class frequency_rank)  [AGGREGATE per-verb; B2 control]
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
    # DAIS theme head-nouns (last token of the theme phrase in each PDsentence "Subj verb theme to R")
    dais_theme_heads = set()
    for r in rows:
        m = re.search(r" to (.+)$", r["PDsentence"])
        if m:
            rest = r["PDsentence"][:m.start()].split(None, 2)
            if len(rest) == 3:
                dais_theme_heads.add(rest[2].split()[-1].lower().strip(".,"))
    dais_recipient_realizations = {"him", "the man", "a man", "the man from work", "a man from work"}

    # ---- B3(a) assertions: recipients + theme heads disjoint -------------------------------
    for cond, real in RECIPIENTS.items():
        assert real not in dais_recipient_realizations, \
            f"RECIPIENT {cond}={real!r} collides with a DAIS canonical realization (B3)."
    project_theme_heads = {t.split()[-1].lower() for t in THEME.values()}
    theme_collisions = project_theme_heads & dais_theme_heads
    assert not theme_collisions, f"THEME head-nouns collide with DAIS themes (B3): {theme_collisions}"
    # project subject disjoint from DAIS subjects
    dais_subjects = {r["DOsentence"].split()[0] for r in rows}
    assert SUBJECT not in dais_subjects, f"SUBJECT {SUBJECT!r} collides with a DAIS subject."

    # ---- build trials ----------------------------------------------------------------------
    # Counterbalancing: which phrasing is shown as option A is frozen per trial by a seeded RNG, so
    # the graded parse is position-based (target-blind) and DOC<->A/B balance is fixed at freeze.
    cb = random.Random(ARMB_SEED + 1)
    trials = []
    tid = 0
    # Arm A: 200 verbs x canonical condition
    for v in verbs:
        theme = theme_for(v, vbmap)
        doc, pd = doc_pd(v, theme, RECIPIENTS[CANONICAL_ARMA])
        trials.append({"tid": f"A-{tid}", "arm": "A", "verb": v, "condition": CANONICAL_ARMA,
                       "bucket": vbmap[v], "theme": theme, "doc": doc, "pd": pd,
                       "doc_is_a": cb.random() < 0.5, "classification": vinfo[v][0]})
        tid += 1
    # Arm B: 40 random alternating verbs x 5 conditions
    alt_verbs = sorted(v for v in verbs if vinfo[v][0] == "alternating")
    rng = random.Random(ARMB_SEED)
    armb_verbs = sorted(rng.sample(alt_verbs, ARMB_N))
    for v in armb_verbs:
        theme = theme_for(v, vbmap)
        for cond in CONDITION_ORDER:
            doc, pd = doc_pd(v, theme, RECIPIENTS[cond])
            trials.append({"tid": f"B-{tid}", "arm": "B", "verb": v, "condition": cond,
                           "bucket": vbmap[v], "theme": theme, "doc": doc, "pd": pd,
                           "doc_is_a": cb.random() < 0.5, "classification": "alternating"})
            tid += 1

    # ---- B3(a) verbatim disjointness assertion (the crux) ----------------------------------
    collisions = []
    for t in trials:
        for s in (t["doc"].strip(), t["pd"].strip()):
            if s in dais_strings:
                collisions.append(s)
    assert not collisions, f"VERBATIM COLLISION with DAIS sentences (B3): {collisions[:5]}"

    # ---- human targets (from the COMMITTED derived table only) -----------------------------
    means = {}
    for r in csv.DictReader(open(MEANS_CSV)):
        means[(r["verb"], r["recipient_condition"])] = float(r["mean_DOpreference"])
    # per-verb human mean at the canonical Arm-A condition (matched) + collapsed mean (robustness)
    human_arma_matched = {v: means[(v, CANONICAL_ARMA)] for v in verbs}
    human_arma_collapsed = {v: sum(means[(v, c)] for c in CONDITION_ORDER) / 5.0 for v in verbs}
    # per-(verb,condition) for Arm B
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

    # ---- B3(b) fidelity audit table --------------------------------------------------------
    def wc(s):
        return len(s.split())
    fidelity = {
        "note": ("Each project recipient realization vs the DAIS factor level it instantiates. "
                 "Length (word count) and definiteness are matched to DAIS's factor structure; the "
                 "lexemes are project-chosen and disjoint (B3). Theme held fixed per verb across the "
                 "5 conditions -- only the recipient moves."),
        "subject": SUBJECT,
        "conditions": [
            {"condition": c, "project_realization": RECIPIENTS[c],
             "dais_canonical_realization": r, "project_wc": wc(RECIPIENTS[c]),
             "dais_wc": wc(r),
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
        "verbatim_collision_count": len(collisions),
        "recipient_collision": False,
        "theme_head_collision": sorted(theme_collisions),
        "subject_collision": SUBJECT in dais_subjects,
        "assertion": "PASS -- no project stimulus string, recipient realization, or theme head-noun "
                     "appears in DAIS's released sentences / factor realizations (B3).",
    }

    stim = {
        "design": "dais-graded-preference-correlation-v1",
        "session": 248,
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

    stim_sha = sha256_bytes(json.dumps(stim, sort_keys=True, indent=2).encode())
    print(f"BUILT: {stim['n_arm_a']} Arm-A + {stim['n_arm_b']} Arm-B trials "
          f"({stim['n_arm_a'] + stim['n_arm_b']} items x 3 models = "
          f"{(stim['n_arm_a'] + stim['n_arm_b']) * 3} calls).")
    print(f"Arm-B verbs ({ARMB_N}): {armb_verbs}")
    print(f"Arm-B null p0 = {ARMB_NULL_P0:.4f} (rho_s>={ARMB_RHO_THRESHOLD}); "
          "PREREG must record the stimuli.json sha below BEFORE any model call:")
    # NOTE: the committed stimuli.json is re-serialized by json.dump with sort_keys+indent, so the
    # sha the probe checks is of the FILE on disk, computed by probe.py::_require_frozen. Print the
    # on-disk sha for PREREG.
    on_disk = sha256_bytes(open(os.path.join(HERE, "stimuli.json"), "rb").read())
    print(f"stimuli.json (on-disk) sha256 = {on_disk}")


if __name__ == "__main__":
    main()
