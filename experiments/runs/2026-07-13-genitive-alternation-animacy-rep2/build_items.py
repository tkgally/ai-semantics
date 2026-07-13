#!/usr/bin/env python3
"""Build + certify + freeze the FRESH-ITEM genitive-alternation possessor-animacy stimuli (REP2).

This is the fresh-item REPLICATION of the s218 genitive-animacy probe, the A2a powered-re-run
pattern the s219 promotion review named as the exact strengthening path
(note/genitive-alternation-animacy-promotion-refusal-v1). The INSTRUMENT is byte-frozen from s218
(common.py / probe.py / analyze.py / build_cooc_gen.py are sha-identical; common.py differs only in
the HARD_STOP_USD budget constant, documented in-file). ONLY the item set is new:

  1. FRESH, DISJOINT items. Every typical possessor lemma and every nonce string is disjoint from
     the s218 frozen set (asserted in certification check (D) below, loaded from the s218
     stimuli.json). Typical possessums are fresh too; the disjointness guarantee is on the finding-
     bearing possessORs + nonce strings (one neutral nonce property-noun, "base", recurs from s218 --
     immaterial: possessa are held fixed within frame and cancel in the within-frame shift). So this
     is a genuine second run on new possessors, not a re-run of the frozen dir.
  2. POWERED gpt firewall leg. The nonce arm is enlarged 24 -> 36 frames (the derangement offset is
     n//2 = 18), because the s218 gpt nonce leg was the marginal member (mean +0.055, 16/24 frames,
     one-sided sign-p 0.076 -- it cleared the CI-LB rule only marginally). 36 paired nonce contrasts
     give the weak leg's sign test + bootstrap CI more power. Typical arm stays 36 frames.

Everything else is the ratified s218 design (decisions/resolved/genitive-alternation-anchor-and-
indicator, ADOPT DEFAULTS Q1-A / Q2-i / Q3 human-anchored; freeze conditions B1-B3, S1-S7, R1-R5):
graded forced-choice, possessum held fixed, s-pref = s_pts/(s_pts+of_pts); FINDING-BEARING MEASURE =
within-FRAME animacy shift shift(frame) = mean(s-pref|animate) - mean(s-pref|inanimate); human
direction (Dubois et al. 2023) animate -> s-genitive, shift > 0. TWO ARMS: TYPICAL (real possessors,
animate/collective/inanimate, carries graded monotonicity + the frozen marginal-propensity
covariate) and NONCE (rare/nonce possessors, animacy by gloss only, orthographically neutralized --
the shortcut-immune PRIMARY control that CARRIES the CONFIRM).

Outputs: stimuli.json (frozen, sha-pinned in PREREG) + a printed certification report.
Run: python3 build_items.py
"""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
S218_STIM = HERE.parent / "2026-07-13-genitive-alternation-animacy" / "stimuli.json"

# --- orthographic final-sibilancy proxy (same regex as s218; NEUTRALIZED by within-frame matching,
# and all authored possessors are chosen NON-sibilant-final so the flag is uniformly False). ---
_SIB_END = re.compile(r"(s|ss|x|z|zz|ce|se|ze|sh|ch|tch|ge|dge)$", re.I)


def ends_sibilant(noun: str) -> bool:
    return bool(_SIB_END.search(noun.strip().lower()))


def wc(np_: str) -> int:
    return len(np_.split())


# ---------------------------------------------------------------------------
# TYPICAL arm (36 frames). Each frame: a broadly-applicable attribute/eventive POSSESSUM sensible
# with an animate, a collective (group-of-humans), and an inanimate possessor; three possessors each
# a definite "the <one-word-noun>" (word length identical = 2 tokens; no bare proper-name possessor,
# critic S1), all non-sibilant-final. FRESH + DISJOINT from the s218 set (certified below). Levels
# self-audited against the Zaenen et al. (2004) five-level scheme via Dubois et al. (2023): animate =
# humans/animals; collective = groups of humans; inanimate = objects/abstractions.
# ---------------------------------------------------------------------------
TYPICAL = [
    dict(id="t01", possessum="survival",       animate="the sailor",   collective="the squadron",     inanimate="the canyon"),
    dict(id="t02", possessum="legacy",         animate="the pilot",    collective="the tribunal",     inanimate="the hurricane"),
    dict(id="t03", possessum="reputation",     animate="the hunter",   collective="the militia",      inanimate="the meteor"),
    dict(id="t04", possessum="destruction",    animate="the monk",     collective="the faction",      inanimate="the iceberg"),
    dict(id="t05", possessum="formation",      animate="the rebel",    collective="the guild",        inanimate="the wire"),
    dict(id="t06", possessum="character",      animate="the hermit",   collective="the parliament",   inanimate="the motor"),
    dict(id="t07", possessum="stability",      animate="the jockey",   collective="the jury",         inanimate="the tide"),
    dict(id="t08", possessum="duration",       animate="the peasant",  collective="the committee",    inanimate="the ravine"),
    dict(id="t09", possessum="temperature",    animate="the gambler",  collective="the delegation",   inanimate="the boulder"),
    dict(id="t10", possessum="emergence",      animate="the nomad",    collective="the syndicate",    inanimate="the drought"),
    dict(id="t11", possessum="isolation",      animate="the warrior",  collective="the clan",         inanimate="the valley"),
    dict(id="t12", possessum="transformation", animate="the maiden",   collective="the cabinet",      inanimate="the temple"),
    dict(id="t13", possessum="rise",           animate="the wizard",   collective="the legion",       inanimate="the geyser"),
    dict(id="t14", possessum="fall",           animate="the shepherd", collective="the troupe",       inanimate="the woodland"),
    dict(id="t15", possessum="mood",           animate="the rooster",  collective="the brotherhood",  inanimate="the stream"),
    dict(id="t16", possessum="density",        animate="the panther",  collective="the corporation",  inanimate="the moon"),
    dict(id="t17", possessum="silhouette",     animate="the otter",    collective="the assembly",     inanimate="the diamond"),
    dict(id="t18", possessum="capacity",       animate="the raven",    collective="the gang",         inanimate="the gravel"),
    dict(id="t19", possessum="depth",          animate="the sparrow",  collective="the clergy",       inanimate="the cylinder"),
    dict(id="t20", possessum="breadth",        animate="the python",   collective="the board",        inanimate="the dam"),
    dict(id="t21", possessum="journey",        animate="the jaguar",   collective="the throng",       inanimate="the dagger"),
    dict(id="t22", possessum="spirit",         animate="the bison",    collective="the commune",      inanimate="the bazaar"),
    dict(id="t23", possessum="energy",         animate="the heron",    collective="the sect",         inanimate="the pasture"),
    dict(id="t24", possessum="momentum",       animate="the lizard",   collective="the federation",   inanimate="the beacon"),
    dict(id="t25", possessum="aura",           animate="the beaver",   collective="the minority",     inanimate="the tundra"),
    dict(id="t26", possessum="structure",      animate="the donkey",   collective="the team",         inanimate="the monument"),
    dict(id="t27", possessum="essence",        animate="the rabbit",   collective="the faculty",      inanimate="the rotor"),
    dict(id="t28", possessum="temperament",    animate="the pigeon",   collective="the coalition",    inanimate="the spire"),
    dict(id="t29", possessum="profile",        animate="the hawk",     collective="the panel",        inanimate="the lagoon"),
    dict(id="t30", possessum="pulse",          animate="the mongrel",  collective="the staff",        inanimate="the citadel"),
    dict(id="t31", possessum="onset",          animate="the spider",   collective="the diaspora",     inanimate="the capacitor"),
    dict(id="t32", possessum="demise",         animate="the lobster",  collective="the society",      inanimate="the prairie"),
    dict(id="t33", possessum="vigor",          animate="the hamster",  collective="the public",       inanimate="the altar"),
    dict(id="t34", possessum="grandeur",       animate="the cobra",    collective="the horde",        inanimate="the sinkhole"),
    dict(id="t35", possessum="wellbeing",      animate="the buffalo",  collective="the cult",         inanimate="the windmill"),
    dict(id="t36", possessum="condition",      animate="the weasel",   collective="the league",       inanimate="the cyclone"),
]

# ---------------------------------------------------------------------------
# NONCE arm (36 frames -- enlarged from s218's 24 to POWER the gpt firewall leg). A fixed pool of 36
# nonce monosyllabic non-words (non-sibilant-final, no agentive -er, lowercase, no name-like caps),
# all DISJOINT from the s218 nonce pool (certified). Each frame uses two DISTINCT nonce strings; the
# pairing is a fixed derangement so string j is the ANIMATE possessor in frame j and the INANIMATE
# possessor in frame ((j + n//2) % n). => the multiset of strings in the animate slots EXACTLY equals
# the multiset in the inanimate slots (each string once-animate, once-inanimate), certified below.
# Animacy is carried ONLY by the gloss ("a small wild animal called a <s>" vs "a hard grey mineral
# called a <s>"). Possessums are neutral physical-property nouns sensible for both an animal and a
# mineral. The gloss strings are byte-identical to s218 (part of the frozen instrument).
# ---------------------------------------------------------------------------
NONCE_STRINGS = ["frab", "klim", "dorn", "glon", "prab", "bruk", "nid", "tulp", "wend", "grulp",
                 "flad", "snit", "brin", "clup", "dwan", "forn", "keb", "lut", "mork", "nib",
                 "ploon", "quan", "reld", "stib", "trob", "vorl", "wolt", "yorn", "zad", "blon",
                 "crin", "drup", "fint", "gorp", "helb", "jult"]
NONCE_POSSESSA = ["density", "hardness", "sheen", "grain", "contour", "luster", "tint", "ridge",
                  "bulk", "crest", "face", "spine", "girth", "span", "curve", "flank", "gloss",
                  "polish", "body", "build", "frame", "profile", "volume", "depth", "breadth",
                  "thickness", "coating", "underside", "apex", "base", "coloring", "heft",
                  "glimmer", "tone", "diameter", "silhouette"]
ANIM_GLOSS = "a small wild animal called a {s}"
INAN_GLOSS = "a hard grey mineral called a {s}"


def build_nonce():
    n = len(NONCE_STRINGS)  # 36
    frames = []
    for j in range(n):
        anim_s = NONCE_STRINGS[j]
        inan_s = NONCE_STRINGS[(j + n // 2) % n]
        frames.append(dict(
            id=f"n{j+1:02d}",
            possessum=NONCE_POSSESSA[j],
            animate=f"the {anim_s}", inanimate=f"the {inan_s}",
            animate_gloss=ANIM_GLOSS.format(s=anim_s),
            inanimate_gloss=INAN_GLOSS.format(s=inan_s),
        ))
    return frames


NONCE = build_nonce()

TYPICAL_LEVELS = ["animate", "collective", "inanimate"]
NONCE_LEVELS = ["animate", "inanimate"]


def s_phrase(possessor, possessum):
    """s-genitive: 'the judge's decision'. possessor is 'the <noun>' -> 'the <noun>'s <possessum>'."""
    return f"{possessor}'s {possessum}"


def of_phrase(possessor, possessum):
    """of-genitive: 'the decision of the judge' (possessor keeps its definite article)."""
    return f"the {possessum} of {possessor}"


def build():
    frames = []
    for fr in TYPICAL:
        frames.append(dict(fr, arm="typical", levels=TYPICAL_LEVELS))
    for fr in NONCE:
        frames.append(dict(fr, arm="nonce", levels=NONCE_LEVELS))

    trials = []
    for fr in frames:
        for level in fr["levels"]:
            possessor = fr[level]
            gloss = fr.get(f"{level}_gloss")  # nonce arm only
            for s_is_a in (True, False):   # A/B counterbalance of s-gen vs of-gen
                sg = s_phrase(possessor, fr["possessum"])
                og = of_phrase(possessor, fr["possessum"])
                a = sg if s_is_a else og
                b = og if s_is_a else sg
                trials.append({
                    "frame": fr["id"], "arm": fr["arm"], "level": level,
                    "possessum": fr["possessum"], "possessor": possessor,
                    "possessor_len": wc(possessor),
                    "possessor_sibilant": ends_sibilant(possessor.split()[-1]),
                    "gloss": gloss, "s_is_a": s_is_a,
                    "option_a": a, "option_b": b,
                })
    return frames, trials


# ---------------------------------------------------------------------------
# CERTIFICATION -- the s218 checks (1)-(4) + (N), PLUS a new (D) DISJOINTNESS check proving every
# typical possessor lemma and every nonce string is disjoint from the s218 frozen set (the load-
# bearing guarantee that this is a genuine fresh-item replication, not a re-run of the frozen dir).
# ---------------------------------------------------------------------------

def shortcut_readers():
    return {
        "always_s":       lambda t: 1.0,
        "always_of":      lambda t: 0.0,
        "always_A":       lambda t: 1.0 if t["s_is_a"] else 0.0,
        "always_B":       lambda t: 0.0 if t["s_is_a"] else 1.0,
        "position_A_bias": lambda t: 0.7 if t["s_is_a"] else 0.3,
        "len_shorter_s":  lambda t: 1.0 / (1.0 + 2.718281828 ** (0.5 * (t["possessor_len"] - 2))),
        "sibilant_of":    lambda t: 0.2 if t["possessor_sibilant"] else 0.8,
    }


def frame_shift(trials, frame_id, reader, hi="animate", lo="inanimate"):
    def mean_pref(level):
        vals = [reader(t) for t in trials if t["frame"] == frame_id and t["level"] == level]
        return sum(vals) / len(vals) if vals else None
    a, b = mean_pref(hi), mean_pref(lo)
    if a is None or b is None:
        return None
    return a - b


def s218_item_sets():
    """Load the s218 frozen possessor lemmas (typical) + nonce strings for the disjointness check."""
    if not S218_STIM.exists():
        return None
    stim = json.loads(S218_STIM.read_text())
    typ_lemmas, nonce_strings = set(), set()
    for fr in stim["frames"]:
        if fr["arm"] == "typical":
            for lv in ("animate", "collective", "inanimate"):
                typ_lemmas.add(fr[lv].split()[-1].lower())
        elif fr["arm"] == "nonce":
            for lv in ("animate", "inanimate"):
                nonce_strings.add(fr[lv].split()[-1].lower())
    return typ_lemmas, nonce_strings


def certify(frames, trials):
    report = {"checks": {}, "fail": []}

    # (1) within-frame match of length + sibilancy + definiteness across levels
    len_ok = sib_ok = def_ok = True
    for fr in frames:
        posrs = [fr[lv] for lv in fr["levels"]]
        lens = {wc(p) for p in posrs}
        sibs = {ends_sibilant(p.split()[-1]) for p in posrs}
        defs = {p.startswith("the ") for p in posrs}
        if len(lens) != 1:
            len_ok = False; report["fail"].append(f"(1) length mismatch in {fr['id']}: {posrs}")
        if len(sibs) != 1:
            sib_ok = False; report["fail"].append(f"(1) sibilancy mismatch in {fr['id']}: {posrs}")
        if defs != {True}:
            def_ok = False; report["fail"].append(f"(1) definiteness/bare-name issue in {fr['id']}: {posrs}")
    report["checks"]["(1) within-frame possessor LENGTH matched across levels"] = len_ok
    report["checks"]["(1) within-frame final-SIBILANCY matched across levels"] = sib_ok
    report["checks"]["(1) all possessors definite 'the <noun>' (no bare proper name, S1)"] = def_ok

    # (2) no bare proper name: no possessor noun is capitalized
    caps = [fr[lv] for fr in frames for lv in fr["levels"]
            if fr[lv].split()[-1][:1].isupper()]
    report["checks"]["(2) no capitalized (proper-name) possessor noun"] = not caps
    if caps:
        report["fail"].append(f"(2) capitalized possessor(s): {caps}")

    # (2b) all possessors non-sibilant-final (the neutralized design target)
    sibpos = [fr[lv] for fr in frames for lv in fr["levels"] if ends_sibilant(fr[lv].split()[-1])]
    report["checks"]["(2b) every possessor non-sibilant-final (uniform neutralization)"] = not sibpos
    if sibpos:
        report["fail"].append(f"(2b) sibilant-final possessor(s): {sibpos}")

    # (3) nonce arm orthographic neutralization: animate-slot string multiset == inanimate-slot
    nonce = [fr for fr in frames if fr["arm"] == "nonce"]
    anim_strings = sorted(fr["animate"] for fr in nonce)
    inan_strings = sorted(fr["inanimate"] for fr in nonce)
    report["checks"]["(3) nonce animate/inanimate slot string multisets EQUAL (R1)"] = anim_strings == inan_strings
    if anim_strings != inan_strings:
        report["fail"].append("(3) nonce slot multisets differ")
    ca, ci = Counter(fr["animate"] for fr in nonce), Counter(fr["inanimate"] for fr in nonce)
    report["checks"]["(3) each nonce string once-animate & once-inanimate"] = (
        set(ca.values()) == {1} and set(ci.values()) == {1} and set(ca) == set(ci))

    # (4) surface shortcut readers -> within-frame shift 0 on every frame
    readers = shortcut_readers()
    max_abs = {}
    for name, r in readers.items():
        shifts = [abs(frame_shift(trials, fr["id"], r)) for fr in frames]
        max_abs[name] = max(shifts)
    report["max_abs_frame_shift_per_shortcut_reader"] = {k: round(v, 6) for k, v in max_abs.items()}
    all_zero = all(v < 1e-9 for v in max_abs.values())
    report["checks"]["(4) no length/sibilancy/position/always-s/always-of reader yields ANY within-frame shift"] = all_zero
    if not all_zero:
        report["fail"].append("(4) a surface shortcut reader produced a nonzero within-frame shift")

    # (D) DISJOINTNESS from the s218 frozen set (the fresh-item-replication guarantee)
    s218 = s218_item_sets()
    if s218 is None:
        report["checks"]["(D) s218 stimuli.json present for disjointness check"] = False
        report["fail"].append("(D) could not load s218 stimuli.json -- cannot certify disjointness")
    else:
        s218_typ, s218_nonce = s218
        my_typ = {fr[lv].split()[-1].lower() for fr in frames if fr["arm"] == "typical"
                  for lv in ("animate", "collective", "inanimate")}
        my_nonce = {fr[lv].split()[-1].lower() for fr in frames if fr["arm"] == "nonce"
                    for lv in ("animate", "inanimate")}
        typ_overlap = sorted(my_typ & s218_typ)
        nonce_overlap = sorted(my_nonce & s218_nonce)
        report["disjointness"] = {
            "n_typical_lemmas": len(my_typ), "typical_overlap_with_s218": typ_overlap,
            "n_nonce_strings": len(my_nonce), "nonce_overlap_with_s218": nonce_overlap}
        report["checks"]["(D) typical possessor lemmas DISJOINT from s218 (0 shared)"] = not typ_overlap
        report["checks"]["(D) nonce strings DISJOINT from s218 (0 shared)"] = not nonce_overlap
        if typ_overlap:
            report["fail"].append(f"(D) typical possessor lemmas shared with s218: {typ_overlap}")
        if nonce_overlap:
            report["fail"].append(f"(D) nonce strings shared with s218: {nonce_overlap}")

    # counts
    n_typ = sum(1 for fr in frames if fr["arm"] == "typical")
    n_non = sum(1 for fr in frames if fr["arm"] == "nonce")
    report["checks"]["(N) >=40 frames total"] = (n_typ + n_non) >= 40
    report["checks"]["(N) nonce arm >=20 frames (critic S2/R3)"] = n_non >= 20
    report["checks"]["(N) nonce arm ENLARGED >=30 frames (rep2 power the gpt firewall leg)"] = n_non >= 30
    report["checks"]["(N) typical arm carries collective level (graded test, S7)"] = all(
        "collective" in fr["levels"] for fr in frames if fr["arm"] == "typical")

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    report["counts"] = {"n_frames": n_typ + n_non, "n_typical": n_typ, "n_nonce": n_non,
                        "n_trials": len(trials)}
    return report


def main():
    frames, trials = build()
    stim = {
        "design": "genitive-alternation possessor-animacy graded forced-choice (REP2, fresh-item "
                  "replication of s218); within-frame animacy shift; ratified "
                  "decisions/resolved/genitive-alternation-anchor-and-indicator (s218); typical arm "
                  "(animate/collective/inanimate) + ENLARGED nonce arm (animate/inanimate, "
                  "orthographically neutralized shortcut-immune primary control, 36 frames to power "
                  "the gpt firewall leg). Items disjoint from s218 (certified).",
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
    print("  max |within-frame shift| per surface shortcut reader:",
          report["max_abs_frame_shift_per_shortcut_reader"])
    if "disjointness" in report:
        d = report["disjointness"]
        print(f"  disjointness: {d['n_typical_lemmas']} typical lemmas "
              f"(overlap {d['typical_overlap_with_s218']}), {d['n_nonce_strings']} nonce strings "
              f"(overlap {d['nonce_overlap_with_s218']})")
    if report["fail"]:
        print("  FAILURES:")
        for f in report["fail"]:
            print("   -", f)

    # self-audit dump (critic ix): print a couple of example trials per arm
    print("\n--- example scored phrasings (self-audit) ---")
    for fr in (TYPICAL[0], TYPICAL[10], NONCE[0]):
        for lv in fr.get("levels", TYPICAL_LEVELS if fr in TYPICAL else NONCE_LEVELS):
            pos = fr[lv]
            print(f"  [{fr['id']}/{lv}] s: '{s_phrase(pos, fr['possessum'])}'  |  "
                  f"of: '{of_phrase(pos, fr['possessum'])}'"
                  + (f"   gloss: {fr.get(lv+'_gloss')}" if fr.get(lv+'_gloss') else ""))


if __name__ == "__main__":
    main()
