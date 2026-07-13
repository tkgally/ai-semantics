#!/usr/bin/env python3
"""Build + certify + freeze the POWERED-MAGNITUDE typical arm (s222) for the genitive-animacy line.

This is the A2a-MERGED magnitude re-run NEXT.md s221 named: a NEW, fresh, TYPICAL-ONLY arm of 36
possessor-animacy frames, every possessor lemma DISJOINT from BOTH prior disjoint typical arms
(s218 + rep2), pooled with them in analyze_merged.py -> 108 pooled typical frames for a within-model
magnitude + bootstrap interval. The MEASUREMENT instrument is byte-frozen (probe.py / common.py /
build_cooc_gen.py sha-identical to rep2 up to the documented HARD_STOP budget constant); ONLY the
item set + the pooling ANALYSIS are new.

NO NONCE ARM. The shortcut firewall already replicated 3/3 twice (s218 + s220, both CI-LB>0 nonce,
the gpt leg decisive at rep2 25/36 sign-p 0.014); the magnitude the promoted claim owes is a
TYPICAL-arm quantity. This arm attaches magnitude; it does not re-litigate the firewall. (Dropping
nonce also keeps the paid run ~$0.81, inside the same-UTC-day headroom.)

Everything else is the ratified s218 design (decisions/resolved/genitive-alternation-anchor-and-
indicator, ADOPT DEFAULTS Q1-A / Q2-i / Q3 human-anchored; freeze conditions B1-B3, S1-S7, R1-R5):
graded forced-choice, possessum held fixed, s-pref = s_pts/(s_pts+of_pts); FINDING-BEARING MEASURE =
within-FRAME animacy shift shift(frame) = mean(s-pref|animate) - mean(s-pref|inanimate); human
direction (Dubois et al. 2023) animate -> s-genitive, shift > 0. The typical arm carries the
animate/collective/inanimate graded levels (S7) and the frozen marginal-propensity covariate
(corroboration).

Levels self-audited against the Zaenen et al. (2004) scheme via Dubois et al. (2023): animate =
an individual human OR animal; collective = a group of humans; inanimate = an object/place/thing.
All possessors are a definite "the <one-word-noun>" (length identical = 2 tokens, no bare proper
name, S1) and non-sibilant-final (uniform neutralization, S2b).

Outputs: stimuli.json (frozen, sha-pinned in PREREG) + a printed certification report.
Run: python3 build_items.py
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
PRIOR_STIMS = [RUNS / "2026-07-13-genitive-alternation-animacy" / "stimuli.json",
               RUNS / "2026-07-13-genitive-alternation-animacy-rep2" / "stimuli.json"]

_SIB_END = re.compile(r"(s|ss|x|z|zz|ce|se|ze|sh|ch|tch|ge|dge)$", re.I)


def ends_sibilant(noun: str) -> bool:
    return bool(_SIB_END.search(noun.strip().lower()))


def wc(np_: str) -> int:
    return len(np_.split())


# ---------------------------------------------------------------------------
# TYPICAL arm (36 fresh frames). Each: a broadly-applicable attribute/eventive POSSESSUM + an
# animate (individual human/animal), a collective (group of humans), an inanimate (object/place)
# possessor, each "the <one-word-noun>", non-sibilant-final, all DISJOINT from s218 AND rep2
# (certified (D) below). Candidate vocabulary generated blind to model responses; animacy classes +
# final selection are the lead's judgement.
# ---------------------------------------------------------------------------
TYPICAL = [
    dict(id="t01", possessum="state",       animate="the farmer",   collective="the band",          inanimate="the desert"),
    dict(id="t02", possessum="value",       animate="the baker",    collective="the troop",         inanimate="the island"),
    dict(id="t03", possessum="worth",       animate="the teacher",  collective="the squad",         inanimate="the cliff"),
    dict(id="t04", possessum="nature",      animate="the painter",  collective="the unit",          inanimate="the lake"),
    dict(id="t05", possessum="role",        animate="the singer",   collective="the company",       inanimate="the jungle"),
    dict(id="t06", possessum="position",    animate="the dancer",   collective="the firm",          inanimate="the plateau"),
    dict(id="t07", possessum="location",    animate="the writer",   collective="the agency",        inanimate="the cave"),
    dict(id="t08", possessum="decay",       animate="the driver",   collective="the bureau",        inanimate="the delta"),
    dict(id="t09", possessum="breakdown",   animate="the gardener", collective="the ministry",      inanimate="the plain"),
    dict(id="t10", possessum="integrity",   animate="the lawyer",   collective="the department",    inanimate="the orchard"),
    dict(id="t11", possessum="longevity",   animate="the doctor",   collective="the division",      inanimate="the cabin"),
    dict(id="t12", possessum="lifespan",    animate="the actor",    collective="the cohort",        inanimate="the mansion"),
    dict(id="t13", possessum="lifetime",    animate="the sculptor", collective="the mafia",         inanimate="the fort"),
    dict(id="t14", possessum="durability",  animate="the emperor",  collective="the clique",        inanimate="the bunker"),
    dict(id="t15", possessum="quality",     animate="the clerk",    collective="the cabal",         inanimate="the pier"),
    dict(id="t16", possessum="makeup",      animate="the cook",     collective="the junta",         inanimate="the dock"),
    dict(id="t17", possessum="peak",        animate="the knight",   collective="the regime",        inanimate="the factory"),
    dict(id="t18", possessum="tendency",    animate="the mayor",    collective="the fraternity",    inanimate="the library"),
    dict(id="t19", possessum="descent",     animate="the tiger",    collective="the sorority",      inanimate="the museum"),
    dict(id="t20", possessum="ascent",      animate="the lion",     collective="the cooperative",   inanimate="the table"),
    dict(id="t21", possessum="trajectory",  animate="the bear",     collective="the consortium",    inanimate="the mirror"),
    dict(id="t22", possessum="standing",    animate="the wolf",     collective="the partnership",   inanimate="the barrel"),
    dict(id="t23", possessum="function",    animate="the deer",     collective="the fellowship",    inanimate="the kettle"),
    dict(id="t24", possessum="direction",   animate="the goat",     collective="the personnel",     inanimate="the bottle"),
    dict(id="t25", possessum="form",        animate="the cow",      collective="the patrol",        inanimate="the hammer"),
    dict(id="t26", possessum="magnitude",   animate="the swan",     collective="the retinue",       inanimate="the ladder"),
    dict(id="t27", possessum="proportion",  animate="the eagle",    collective="the deputation",    inanimate="the wheel"),
    dict(id="t28", possessum="span",        animate="the dove",     collective="the commission",    inanimate="the valve"),
    dict(id="t29", possessum="extent",      animate="the frog",     collective="the administration", inanimate="the pipe"),
    dict(id="t30", possessum="scale",       animate="the snake",    collective="the government",    inanimate="the tank"),
    dict(id="t31", possessum="dimension",   animate="the whale",    collective="the directorate",   inanimate="the boiler"),
    dict(id="t32", possessum="footprint",   animate="the seal",     collective="the association",   inanimate="the socket"),
    dict(id="t33", possessum="mark",        animate="the badger",   collective="the foundation",    inanimate="the screen"),
    dict(id="t34", possessum="path",        animate="the raccoon",  collective="the convent",       inanimate="the camera"),
    dict(id="t35", possessum="composition", animate="the bull",     collective="the ensemble",      inanimate="the rocket"),
    dict(id="t36", possessum="height",      animate="the gorilla",  collective="the quartet",       inanimate="the statue"),
]

TYPICAL_LEVELS = ["animate", "collective", "inanimate"]


def s_phrase(possessor, possessum):
    return f"{possessor}'s {possessum}"


def of_phrase(possessor, possessum):
    return f"the {possessum} of {possessor}"


def build():
    frames = [dict(fr, arm="typical", levels=TYPICAL_LEVELS) for fr in TYPICAL]
    trials = []
    for fr in frames:
        for level in fr["levels"]:
            possessor = fr[level]
            for s_is_a in (True, False):
                sg = s_phrase(possessor, fr["possessum"])
                og = of_phrase(possessor, fr["possessum"])
                a = sg if s_is_a else og
                b = og if s_is_a else sg
                trials.append({
                    "frame": fr["id"], "arm": fr["arm"], "level": level,
                    "possessum": fr["possessum"], "possessor": possessor,
                    "possessor_len": wc(possessor),
                    "possessor_sibilant": ends_sibilant(possessor.split()[-1]),
                    "gloss": None, "s_is_a": s_is_a, "option_a": a, "option_b": b,
                })
    return frames, trials


def shortcut_readers():
    return {
        "always_s":        lambda t: 1.0,
        "always_of":       lambda t: 0.0,
        "always_A":        lambda t: 1.0 if t["s_is_a"] else 0.0,
        "always_B":        lambda t: 0.0 if t["s_is_a"] else 1.0,
        "position_A_bias": lambda t: 0.7 if t["s_is_a"] else 0.3,
        "len_shorter_s":   lambda t: 1.0 / (1.0 + 2.718281828 ** (0.5 * (t["possessor_len"] - 2))),
        "sibilant_of":     lambda t: 0.2 if t["possessor_sibilant"] else 0.8,
    }


def frame_shift(trials, frame_id, reader, hi="animate", lo="inanimate"):
    def mean_pref(level):
        vals = [reader(t) for t in trials if t["frame"] == frame_id and t["level"] == level]
        return sum(vals) / len(vals) if vals else None
    a, b = mean_pref(hi), mean_pref(lo)
    if a is None or b is None:
        return None
    return a - b


def prior_typical_lemmas():
    """Union of typical possessor lemmas across s218 + rep2 (the disjointness exclusion set)."""
    used = set()
    for p in PRIOR_STIMS:
        if not p.exists():
            return None
        stim = json.loads(p.read_text())
        for fr in stim["frames"]:
            if fr["arm"] == "typical":
                for lv in ("animate", "collective", "inanimate"):
                    used.add(fr[lv].split()[-1].lower())
    return used


def certify(frames, trials):
    report = {"checks": {}, "fail": []}

    len_ok = sib_ok = def_ok = True
    for fr in frames:
        posrs = [fr[lv] for lv in fr["levels"]]
        if len({wc(p) for p in posrs}) != 1:
            len_ok = False; report["fail"].append(f"(1) length mismatch in {fr['id']}: {posrs}")
        if len({ends_sibilant(p.split()[-1]) for p in posrs}) != 1:
            sib_ok = False; report["fail"].append(f"(1) sibilancy mismatch in {fr['id']}: {posrs}")
        if {p.startswith("the ") for p in posrs} != {True}:
            def_ok = False; report["fail"].append(f"(1) definiteness issue in {fr['id']}: {posrs}")
    report["checks"]["(1) within-frame possessor LENGTH matched across levels"] = len_ok
    report["checks"]["(1) within-frame final-SIBILANCY matched across levels"] = sib_ok
    report["checks"]["(1) all possessors definite 'the <noun>' (no bare proper name, S1)"] = def_ok

    caps = [fr[lv] for fr in frames for lv in fr["levels"] if fr[lv].split()[-1][:1].isupper()]
    report["checks"]["(2) no capitalized (proper-name) possessor noun"] = not caps
    if caps:
        report["fail"].append(f"(2) capitalized possessor(s): {caps}")

    sibpos = [fr[lv] for fr in frames for lv in fr["levels"] if ends_sibilant(fr[lv].split()[-1])]
    report["checks"]["(2b) every possessor non-sibilant-final (uniform neutralization)"] = not sibpos
    if sibpos:
        report["fail"].append(f"(2b) sibilant-final possessor(s): {sibpos}")

    readers = shortcut_readers()
    max_abs = {name: max(abs(frame_shift(trials, fr["id"], r)) for fr in frames)
               for name, r in readers.items()}
    report["max_abs_frame_shift_per_shortcut_reader"] = {k: round(v, 6) for k, v in max_abs.items()}
    all_zero = all(v < 1e-9 for v in max_abs.values())
    report["checks"]["(4) no length/sibilancy/position/always-s/always-of reader yields ANY within-frame shift"] = all_zero
    if not all_zero:
        report["fail"].append("(4) a surface shortcut reader produced a nonzero within-frame shift")

    prior = prior_typical_lemmas()
    my_typ = {fr[lv].split()[-1].lower() for fr in frames for lv in fr["levels"]}
    if prior is None:
        report["checks"]["(D) prior stimuli present for disjointness check"] = False
        report["fail"].append("(D) could not load s218/rep2 stimuli -- cannot certify disjointness")
    else:
        overlap = sorted(my_typ & prior)
        report["disjointness"] = {"n_typical_lemmas": len(my_typ),
                                  "n_prior_typical_lemmas": len(prior),
                                  "typical_overlap_with_s218_and_rep2": overlap}
        report["checks"]["(D) typical possessor lemmas DISJOINT from s218 AND rep2 (0 shared)"] = not overlap
        if overlap:
            report["fail"].append(f"(D) typical possessor lemmas shared with a prior arm: {overlap}")

    # also: no internal duplicate possessor lemma across the 36 new frames
    from collections import Counter
    dup = [w for w, c in Counter(fr[lv].split()[-1].lower() for fr in frames
                                 for lv in fr["levels"]).items() if c > 1]
    report["checks"]["(D2) no possessor lemma repeats within the new arm"] = not dup
    if dup:
        report["fail"].append(f"(D2) internal duplicate possessor lemma(s): {dup}")
    dpa = [w for w, c in Counter(fr["possessum"].lower() for fr in frames).items() if c > 1]
    report["checks"]["(D3) no possessum repeats within the new arm"] = not dpa
    if dpa:
        report["fail"].append(f"(D3) internal duplicate possessum(s): {dpa}")

    n_typ = len(frames)
    report["checks"]["(N) typical arm >= 30 frames (powers the merged-108 magnitude)"] = n_typ >= 30
    report["checks"]["(N) typical arm carries collective level (graded test, S7)"] = all(
        "collective" in fr["levels"] for fr in frames)

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    report["counts"] = {"n_frames": n_typ, "n_typical": n_typ, "n_nonce": 0, "n_trials": len(trials)}
    return report


def main():
    frames, trials = build()
    stim = {
        "design": "genitive-alternation possessor-animacy graded forced-choice (MAG, s222): a fresh "
                  "TYPICAL-ONLY arm (36 frames, animate/collective/inanimate), disjoint from s218 AND "
                  "rep2, pooled with them (analyze_merged.py) -> 108 pooled typical frames for a "
                  "within-model magnitude+interval. Measurement instrument byte-frozen from s218 "
                  "(decisions/resolved/genitive-alternation-anchor-and-indicator). No nonce arm (the "
                  "firewall already replicated 3/3 twice; magnitude is a typical-arm quantity).",
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
        print(f"  disjointness: {d['n_typical_lemmas']} new typical lemmas vs "
              f"{d['n_prior_typical_lemmas']} prior (overlap {d['typical_overlap_with_s218_and_rep2']})")
    if report["fail"]:
        print("  FAILURES:")
        for f in report["fail"]:
            print("   -", f)

    print("\n--- example scored phrasings (self-audit) ---")
    for fr in (frames[0], frames[18], frames[35]):
        for lv in TYPICAL_LEVELS:
            pos = fr[lv]
            print(f"  [{fr['id']}/{lv}] s: '{s_phrase(pos, fr['possessum'])}'  |  "
                  f"of: '{of_phrase(pos, fr['possessum'])}'")


if __name__ == "__main__":
    main()
