#!/usr/bin/env python3
"""Build + certify + freeze the GENITIVE-ALTERNATION possessor-animacy stimuli (program A5).

Ratified design: decisions/resolved/genitive-alternation-anchor-and-indicator (s218, ADOPT
DEFAULTS Q1-A / Q2-i / Q3 human-anchored; + freeze conditions B1-B3, S1-S7, R1-R5). Instrument:
graded forced-choice (port of the validated dative/CC instrument) -- hold the possessum fixed,
distribute 100 points by naturalness between the s-genitive ("the judge's decision") and the
of-genitive ("the decision of the judge"). s-pref = s_pts/(s_pts+of_pts).

FINDING-BEARING MEASURE: within-FRAME animacy shift
    shift(frame) = mean(s-pref | animate possessor) - mean(s-pref | inanimate possessor)
Human direction (Dubois et al. 2023): animate -> s-genitive, so shift > 0.

WHY A FRAME IS THE UNIT. Unlike the dative (givenness lived in the context, the two scored
phrasings were byte-identical), animacy is a LEXICAL property of the possessor, so the possessor
word DIFFERS across animacy conditions while the possessum + frame are held byte-identical. The
resampling unit is the FRAME (a fixed possessum), per critic S3. Because the possessor word moves,
the shift is NOT surface-immune by construction; it is made immune to length / final-sibilancy /
position / always-s / always-of readers by WITHIN-FRAME MATCHING (certified below), and immune to
the marginal-frequency reader by the TWO shadow controls (the nonce arm + the frozen covariate),
NOT by construction (critic S4).

TWO ARMS.
  TYPICAL (real, common possessors): animate + collective + inanimate levels; carries the graded
    monotonicity test (animate > collective > inanimate) and feeds the frozen marginal-propensity
    covariate regression.
  NONCE (rare/nonce possessors -- the shortcut-immune PRIMARY control, critic B1 + R1/R3): animate
    + inanimate levels only. Animacy is conveyed by the FRAME/GLOSS ("a small animal called a narb"
    vs "a mineral called a narb"), NEVER by the nonce string's own orthography; and the nonce
    strings are BALANCED so the exact same multiset of strings fills the animate and the inanimate
    slots (each string is used once-animate, once-inanimate) -- so no orthographic form cue can
    telegraph animacy (R1). A nonce possessor has no per-lemma corpus genitive statistic, so a
    no-animacy marginal-frequency reader cannot score a spurious shift here.

Outputs: stimuli.json (frozen, sha-pinned in PREREG) + a printed certification report.
Run: python3 build_items.py
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

# --- orthographic final-sibilancy proxy (Dubois names final sibilancy of the possessor as an
# independent constraint on the s-genitive; we NEUTRALIZE it by matching within frame). A word is
# flagged sibilant-final if it ends in a sibilant/affricate grapheme cluster. All authored
# possessors are chosen NON-sibilant-final so the flag is uniformly False and trivially matched;
# the certification asserts within-frame equality regardless. ---
_SIB_END = re.compile(r"(s|ss|x|z|zz|ce|se|ze|sh|ch|tch|ge|dge)$", re.I)


def ends_sibilant(noun: str) -> bool:
    return bool(_SIB_END.search(noun.strip().lower()))


def wc(np_: str) -> int:
    return len(np_.split())


# ---------------------------------------------------------------------------
# TYPICAL arm. Each frame: a broadly-applicable attribute/eventive POSSESSUM that is sensible with
# an animate, a collective (group-of-humans), and an inanimate possessor; three possessors each a
# definite "the <one-word-noun>" (so word length is identical = 2 tokens by construction, and no
# bare proper-name possessor -- critic S1), all non-sibilant-final. Self-audited against the Zaenen
# et al. (2004) five-level scheme via Dubois et al. (2023): animate = humans/animals; collective =
# groups of humans; inanimate = objects / abstractions.
# ---------------------------------------------------------------------------
TYPICAL = [
    dict(id="t01", possessum="collapse",   animate="the patient",   collective="the empire",     inanimate="the tunnel"),
    dict(id="t02", possessum="arrival",    animate="the captain",   collective="the convoy",     inanimate="the monsoon"),
    dict(id="t03", possessum="return",     animate="the widow",     collective="the regiment",   inanimate="the comet"),
    dict(id="t04", possessum="departure",  animate="the tenant",    collective="the caravan",    inanimate="the glacier"),
    dict(id="t05", possessum="strength",   animate="the athlete",   collective="the union",      inanimate="the cable"),
    dict(id="t06", possessum="power",      animate="the tyrant",    collective="the council",    inanimate="the engine"),
    dict(id="t07", possessum="speed",      animate="the cheetah",   collective="the platoon",    inanimate="the current"),
    dict(id="t08", possessum="size",       animate="the infant",    collective="the herd",       inanimate="the crater"),
    dict(id="t09", possessum="weight",     animate="the stallion",  collective="the battalion",  inanimate="the anchor"),
    dict(id="t10", possessum="influence",  animate="the tutor",     collective="the senate",     inanimate="the climate"),
    dict(id="t11", possessum="presence",   animate="the guardian",  collective="the garrison",   inanimate="the mountain"),
    dict(id="t12", possessum="decline",    animate="the sultan",    collective="the dynasty",    inanimate="the harbor"),
    dict(id="t13", possessum="history",    animate="the veteran",   collective="the tribe",      inanimate="the volcano"),
    dict(id="t14", possessum="future",     animate="the orphan",    collective="the nation",     inanimate="the forest"),
    dict(id="t15", possessum="origin",     animate="the migrant",   collective="the colony",     inanimate="the river"),
    dict(id="t16", possessum="movement",   animate="the serpent",   collective="the crowd",      inanimate="the planet"),
    dict(id="t17", possessum="color",      animate="the parrot",    collective="the flock",      inanimate="the crystal"),
    dict(id="t18", possessum="shape",      animate="the beetle",    collective="the swarm",      inanimate="the pebble"),
    dict(id="t19", possessum="sound",      animate="the cricket",   collective="the orchestra",  inanimate="the turbine"),
    dict(id="t20", possessum="resilience", animate="the survivor",  collective="the community",  inanimate="the levee"),
    dict(id="t21", possessum="edge",       animate="the predator",  collective="the brigade",    inanimate="the blade"),
    dict(id="t22", possessum="recovery",   animate="the addict",    collective="the region",     inanimate="the market"),
    dict(id="t23", possessum="growth",     animate="the piglet",    collective="the township",   inanimate="the meadow"),
    dict(id="t24", possessum="glow",       animate="the firefly",   collective="the congregation", inanimate="the lantern"),
    dict(id="t25", possessum="warmth",     animate="the toddler",   collective="the family",     inanimate="the cavern"),
    dict(id="t26", possessum="age",        animate="the falcon",    collective="the kingdom",    inanimate="the cathedral"),
    dict(id="t27", possessum="motion",     animate="the dolphin",   collective="the fleet",      inanimate="the piston"),
    dict(id="t28", possessum="downfall",   animate="the dictator",  collective="the cartel",     inanimate="the tower"),
    dict(id="t29", possessum="expansion",  animate="the merchant",  collective="the republic",   inanimate="the reef"),
    dict(id="t30", possessum="ruin",       animate="the landlord",  collective="the household",  inanimate="the castle"),
    dict(id="t31", possessum="endurance",  animate="the camel",     collective="the crew",       inanimate="the battery"),
    dict(id="t32", possessum="weakness",   animate="the champion",  collective="the platoon",    inanimate="the girder"),
    dict(id="t33", possessum="rhythm",     animate="the drummer",   collective="the choir",      inanimate="the pendulum"),
    dict(id="t34", possessum="fate",       animate="the prisoner",  collective="the settlement", inanimate="the vessel"),
    dict(id="t35", possessum="behavior",   animate="the toddler",   collective="the mob",        inanimate="the reactor"),
    dict(id="t36", possessum="advance",    animate="the soldier",   collective="the army",       inanimate="the storm"),
]

# ---------------------------------------------------------------------------
# NONCE arm (critic B1 PRIMARY control + R1 orthographic neutralization). A fixed pool of 24 nonce
# monosyllabic non-words (non-sibilant-final, no agentive -er, lowercase, no name-like caps). Each
# frame uses two DISTINCT nonce strings; the pairing is a fixed derangement so that string j is the
# ANIMATE possessor in frame j and the INANIMATE possessor in frame ((j+12) % 24). => the multiset
# of strings in the animate slots EXACTLY equals the multiset in the inanimate slots (each string
# once-animate, once-inanimate), certified below. Animacy is carried ONLY by the gloss in the
# context ("a small wild animal called a <s>" vs "a hard grey mineral called a <s>"). Possessums are
# neutral physical-property nouns sensible for both an animal and a mineral.
# ---------------------------------------------------------------------------
NONCE_STRINGS = ["narb", "pell", "tob", "dut", "kib", "vorn", "glim", "bron", "plom", "trud",
                 "gorb", "mip", "drant", "kell", "yomp", "blit", "cral", "druv", "wamp", "nolt",
                 "quib", "thrap", "vune", "morl"]
NONCE_POSSESSA = ["weight", "size", "color", "shape", "surface", "edge", "texture", "outline",
                  "core", "tip", "rim", "base", "top", "mass", "length", "width", "height", "form",
                  "hue", "age", "name", "position", "warmth", "motion"]
ANIM_GLOSS = "a small wild animal called a {s}"
INAN_GLOSS = "a hard grey mineral called a {s}"


def build_nonce():
    n = len(NONCE_STRINGS)  # 24
    frames = []
    for j in range(n):
        anim_s = NONCE_STRINGS[j]
        inan_s = NONCE_STRINGS[(j + 12) % n]
        frames.append(dict(
            id=f"n{j+1:02d}",
            possessum=NONCE_POSSESSA[j],
            animate=f"the {anim_s}", inanimate=f"the {inan_s}",
            animate_gloss=ANIM_GLOSS.format(s=anim_s),
            inanimate_gloss=INAN_GLOSS.format(s=inan_s),
        ))
    return frames


NONCE = build_nonce()

# --- animacy levels present in each arm ---
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
# CERTIFICATION. Prove: (1) within every frame, all animacy levels share possessor word length and
# final-sibilancy flag and definiteness (so length/sibilancy/definiteness readers give shift 0);
# (2) no bare proper-name possessor (all lowercase common nouns / nonce, critic S1); (3) the nonce
# animate/inanimate slot string multisets are equal (R1 orthographic neutralization); (4) the
# enumerated surface shortcut readers (length, sibilancy, position, always-s, always-of) each yield
# within-frame shift = 0 on EVERY frame. The MARGINAL-FREQUENCY reader is deliberately NOT covered
# here (critic S4) -- it is addressed by the nonce arm + frozen covariate, not by construction.
# ---------------------------------------------------------------------------

def shortcut_readers():
    # each returns an s-preference in [0,1] from the TEST TRIAL ONLY (never animacy/meaning).
    return {
        "always_s":       lambda t: 1.0,
        "always_of":      lambda t: 0.0,
        "always_A":       lambda t: 1.0 if t["s_is_a"] else 0.0,
        "always_B":       lambda t: 0.0 if t["s_is_a"] else 1.0,
        "position_A_bias": lambda t: 0.7 if t["s_is_a"] else 0.3,
        # length reader: prefers s-gen more when possessor is shorter (end-weight analog). Constant
        # within a frame because possessor length is matched across levels -> shift 0.
        "len_shorter_s":  lambda t: 1.0 / (1.0 + 2.718281828 ** (0.5 * (t["possessor_len"] - 2))),
        # sibilancy reader: disprefers s-gen for a sibilant-final possessor.
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
    # each nonce string used exactly once-animate and once-inanimate
    from collections import Counter
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

    # counts
    n_typ = sum(1 for fr in frames if fr["arm"] == "typical")
    n_non = sum(1 for fr in frames if fr["arm"] == "nonce")
    report["checks"]["(N) >=40 frames total"] = (n_typ + n_non) >= 40
    report["checks"]["(N) nonce arm >=20 frames (critic S2/R3)"] = n_non >= 20
    report["checks"]["(N) typical arm carries collective level (graded test, S7)"] = all(
        "collective" in fr["levels"] for fr in frames if fr["arm"] == "typical")

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    report["counts"] = {"n_frames": n_typ + n_non, "n_typical": n_typ, "n_nonce": n_non,
                        "n_trials": len(trials)}
    return report


def main():
    frames, trials = build()
    stim = {
        "design": "genitive-alternation possessor-animacy graded forced-choice; within-frame "
                  "animacy shift; ratified decisions/resolved/genitive-alternation-anchor-and-indicator "
                  "(s218); typical arm (animate/collective/inanimate) + nonce arm (animate/inanimate, "
                  "orthographically neutralized shortcut-immune primary control).",
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
