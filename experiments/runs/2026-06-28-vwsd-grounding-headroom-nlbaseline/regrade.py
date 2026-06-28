#!/usr/bin/env python3
"""Re-grade the VWSD NL-baseline adequacy audit under the RATIFIED VALID scorer.

Resolved decision: decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity
(ratified s128, ADOPT Q-A WITH MODIFICATIONS). Replaces the INVALID deterministic
literal-target-word-lemma recovery scorer (run.py:recovery_score — "high" only when a
lemma of the literal target word appears in the recovered phrase) with a HELD-OUT
TWO-JUDGE CATEGORY-MATCH re-grade of the ALREADY-STORED raw auditor guesses.

THE RATIFIED RULE (implemented here exactly):
  * Judges = the two held-out auditors panel.B gpt-5.4-mini + panel.C gemini-3.5-flash
    (both held out from the claude AUTHOR of the channel).
  * CROSS-ONLY band metric: a judge does NOT grade its own auditor-leg's guesses.
    gpt-judge grades gemini's 120 stored guesses; gemini-judge grades gpt's 120 stored
    guesses. Band metric = the TWO-JUDGE MEAN high-recovery rate over those two CROSS legs.
  * The full 2x2 (each judge grades BOTH guess sets) is run so inter-judge agreement and a
    self-vs-cross LENIENCY diagnostic are reportable; ONLY the two cross legs feed the band.
  * Referent-identity target = the HUMAN VWSD gold {word, phrase} (NOT gold_descriptor
    [the channel under audit -> Q-C circular], NOT a freshly-authored gloss [entangled]).
  * STRICT semantic-referent-identity instruction: literal string overlap declared
    insufficient-and-irrelevant; mandatory (a) word-referent / (b) recovered-referent /
    (c) verdict fields so every string-overlap rubber-stamp is hand-auditable.
  * none/partial/high: high = same depicted referent category; partial = related/
    superordinate/co-present but not the specific referent; none = unrelated/different.
  * Band [0.60, 0.95] CONFIRMED FIXED (P1/P2/P3, Q1-C NOT re-opened). >0.95 = ORACLE
    NO-GO; <0.60 = degenerate NO-GO; only IN BAND can clear the gate -- and even then only
    after this re-grade earns its OWN fresh independent pre-run-critic GO, BEFORE the
    reused IMAGE arm is read.

This script re-grades the STORED guesses only -> TEXT-ONLY, tiny, NO re-authoring spend,
NO images. It NEVER reads raw/image.json. The frozen rubric below is committed to git
BEFORE this is run (anti-cheat: rubric frozen before any re-graded number is seen).

Usage:
  export OPENROUTER_API_KEY=...
  python3 regrade.py regrade-preflight   # 4 items x the 4 (judge,src) combos = 16 calls
  python3 regrade.py regrade-full        # 120 items x 4 = 480 calls -> frozen/regrade.json
"""
import json, os, re, sys, hashlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"gpt": PANEL["B"], "gemini": PANEL["C"]}   # the two held-out judges = the two auditors
JUDGES = ["gpt", "gemini"]
SOURCES = ["gpt", "gemini"]          # auditor-leg that produced the stored guess
CROSS = [("gpt", "gemini"), ("gemini", "gpt")]   # (judge, source) legs that feed the band
BAND = (0.60, 0.95)

NLDESC = os.path.join(HERE, "frozen", "nl_descriptors.json")
RUN_ITEMS = os.path.join(HERE, "frozen", "run_items.json")
RAWDIR = os.path.join(HERE, "raw")
REGRADE = os.path.join(HERE, "frozen", "regrade.json")

# ---------- FROZEN RUBRIC (committed to git BEFORE this is run; do not tune post-hoc) ----------
JUDGE_SYS = (
    "You score whether a short RECOVERED PHRASE names the SAME real-world referent category "
    "as a TARGET WORD denotes in a given PHRASE. This is a purely SEMANTIC judgement of "
    "referent identity.\n"
    "You are shown: a TARGET WORD, a short PHRASE using it (the human-authored gold "
    "specification of the intended referent), and a RECOVERED PHRASE (someone's guess of what "
    "a picture depicts, made WITHOUT seeing the word). Decide whether the recovered phrase "
    "denotes the same referent category as the target word denotes in the phrase.\n"
    "CRUCIAL: literal word/string overlap is NEITHER sufficient NOR relevant. A recovered "
    "phrase that REPEATS the target word but denotes a DIFFERENT referent is NONE or PARTIAL. "
    "A recovered phrase that shares NO words with the target word but denotes the SAME "
    "referent is HIGH -- common name vs technical/Latinate name (e.g. 'thyme' for 'thymus', "
    "'macaw' for 'ara', 'eagle' for 'aquila'), spelling variants (e.g. 'mezcal' for "
    "'mescal'), and standard synonyms that pick out the same referent ALL count HIGH.\n"
    "Scoring:\n"
    "- HIGH: the recovered phrase names the same depicted referent category as the target "
    "word denotes in the phrase.\n"
    "- PARTIAL: the recovered phrase names something RELATED -- a hypernym/superordinate, the "
    "surrounding scene, or a co-present object -- but NOT the specific referent.\n"
    "- NONE: the recovered phrase names an unrelated thing, or a different object than the "
    "referent.\n"
    "First state the referent the target word denotes in the phrase, then the referent of "
    "the recovered phrase, then your verdict. Answer in EXACTLY this format, three lines:\n"
    "WORD_REFERENT: <the real-world referent the target word denotes in the phrase>\n"
    "RECOVERED_REFERENT: <the real-world referent the recovered phrase denotes>\n"
    "VERDICT: <HIGH|PARTIAL|NONE>"
)

def judge_user(word, phrase, recovered):
    return (f"TARGET WORD: {word}\nPHRASE: {phrase}\nRECOVERED PHRASE: {recovered}\n\n"
            "Does the recovered phrase name the same referent category as the target word "
            "denotes in the phrase? Give WORD_REFERENT, RECOVERED_REFERENT, and VERDICT.")

SCORE = {"HIGH": 2, "PARTIAL": 1, "NONE": 0}

def parse_verdict(txt):
    """Return (score 0/1/2 or None, word_ref, recovered_ref, verdict_str)."""
    if not txt:
        return None, "", "", ""
    wr = re.search(r"WORD_REFERENT:\s*(.+)", txt, re.I)
    rr = re.search(r"RECOVERED_REFERENT:\s*(.+)", txt, re.I)
    vm = re.search(r"VERDICT:\s*\*?\*?\s*(HIGH|PARTIAL|NONE)", txt, re.I)
    word_ref = wr.group(1).strip() if wr else ""
    rec_ref = rr.group(1).strip() if rr else ""
    if vm:
        v = vm.group(1).upper()
        return SCORE[v], word_ref, rec_ref, v
    # fallback: last standalone keyword
    kws = re.findall(r"\b(HIGH|PARTIAL|NONE)\b", txt, re.I)
    if kws:
        v = kws[-1].upper()
        return SCORE[v], word_ref, rec_ref, v
    return None, word_ref, rec_ref, ""

def grade_one(judge, word, phrase, recovered):
    r = call(MODELS[judge], JUDGE_SYS, judge_user(word, phrase, recovered), max_tokens=160,
             reasoning={"effort": "minimal"} if judge == "gemini" else None)
    score, wref, rref, vstr = parse_verdict(r.get("content"))
    return score, wref, rref, vstr, r

def load_audit():
    nld = json.load(open(NLDESC))
    return nld["audit"]   # {item_id: {word, phrase, gold_name, gold_descriptor, auditors{gpt,gemini}{recovered,...}}}

def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    h = z*((p*(1-p)/n + z*z/(4*n*n))**0.5)
    return (p, (c-h)/d, (c+h)/d)

def kappa_binary(a, b):
    """Cohen's kappa on two equal-length 0/1 label lists."""
    n = len(a)
    if n == 0:
        return None
    po = sum(1 for i in range(n) if a[i] == b[i]) / n
    pa1 = sum(a)/n; pb1 = sum(b)/n
    pe = pa1*pb1 + (1-pa1)*(1-pb1)
    return (po - pe) / (1 - pe) if (1 - pe) else None

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in ("regrade-preflight", "regrade-full"):
        sys.exit(__doc__)
    audit = load_audit()
    item_ids = sorted(audit.keys())
    if mode == "regrade-preflight":
        item_ids = item_ids[:4]

    # raw verdicts: list of records; grades[(judge,source)][item_id] = 0/1/2
    raw = []
    grades = {(j, s): {} for j in JUDGES for s in SOURCES}
    rubric_sha = hashlib.sha256(JUDGE_SYS.encode()).hexdigest()
    print(f"FROZEN RUBRIC sha256={rubric_sha}")
    print(f"re-grading {len(item_ids)} items x 4 (judge,source) legs = {len(item_ids)*4} calls "
          f"(cross legs feed band: {CROSS})\n")
    for iid in item_ids:
        e = audit[iid]
        word, phrase = e["word"], e["phrase"]
        for src in SOURCES:
            recovered = e["auditors"][src]["recovered"]
            for judge in JUDGES:
                score, wref, rref, vstr, r = grade_one(judge, word, phrase, recovered)
                grades[(judge, src)][iid] = score
                raw.append({"item_id": iid, "word": word, "phrase": phrase,
                            "guess_source": src, "recovered": recovered, "judge": judge,
                            "leg": "cross" if (judge, src) in CROSS else "self",
                            "score": score, "verdict": vstr, "word_referent": wref,
                            "recovered_referent": rref, "raw": r.get("content"),
                            "usage": r.get("usage", {}), "error": r.get("error")})
                if mode == "regrade-preflight":
                    print(f"  {iid} src={src} judge={judge} [{word}/{phrase}] "
                          f"recovered={recovered!r}\n     -> {vstr} (word_ref={wref!r} rec_ref={rref!r})")

    # ---- aggregate ----
    n = len(item_ids)
    nf = sum(1 for x in raw if x["score"] is None)
    print(f"\nPARSE: {len(raw)} calls, {nf} unparsed verdicts")

    def hi_rate(j, s):
        vals = [v for v in grades[(j, s)].values() if v is not None]
        d = {k: sum(1 for x in vals if x == k) for k in (0, 1, 2)}
        return d, (d[2]/len(vals) if vals else 0.0), len(vals)

    print("\nPER-LEG none/partial/high + high-recovery rate (4 legs; * = CROSS leg, feeds band):")
    leg_hi = {}
    for j in JUDGES:
        for s in SOURCES:
            d, hr, nn = hi_rate(j, s)
            leg_hi[(j, s)] = hr
            star = "*" if (j, s) in CROSS else " "
            kind = "cross" if (j, s) in CROSS else "self "
            print(f"  {star} judge={j:6s} grades source={s:6s} ({kind}): "
                  f"none/partial/high = {d[0]}/{d[1]}/{d[2]}  (n={nn})  high-rate={hr:.3f}")

    # band metric = two-judge mean high-recovery over the CROSS legs
    cross_hi = [leg_hi[c] for c in CROSS]
    mean_hi = sum(cross_hi)/len(cross_hi)
    print(f"\nBAND METRIC = two-judge MEAN high-recovery over CROSS legs "
          f"[gpt-judge x gemini-guesses={leg_hi[('gpt','gemini')]:.3f}, "
          f"gemini-judge x gpt-guesses={leg_hi[('gemini','gpt')]:.3f}] = {mean_hi:.3f}")
    if mean_hi < BAND[0]:
        verdict = f"OUT OF BAND, BELOW {BAND[0]} -> DEGENERATE NO-GO (defers, relaxes nothing)"
    elif mean_hi > BAND[1]:
        verdict = f"OUT OF BAND, ABOVE {BAND[1]} -> ORACLE NO-GO (defers, relaxes nothing)"
    else:
        verdict = f"IN BAND {BAND} -> channel admissible (still owes a fresh pre-run-critic GO)"
    print(f"  band {BAND} => {verdict}")

    # self-vs-cross leniency diagnostic (per source)
    print("\nLENIENCY DIAGNOSTIC (self-judge high-rate vs cross-judge high-rate, per source):")
    for s in SOURCES:
        self_j = s
        cross_j = [j for j in JUDGES if j != s][0]
        print(f"  source={s:6s}: self(judge={self_j}) high={leg_hi[(self_j,s)]:.3f}  vs  "
              f"cross(judge={cross_j}) high={leg_hi[(cross_j,s)]:.3f}  "
              f"(delta self-cross = {leg_hi[(self_j,s)]-leg_hi[(cross_j,s)]:+.3f})")

    # inter-judge agreement: on each source's 120 guesses, the two judges (self + cross) both graded
    print("\nINTER-JUDGE AGREEMENT (both judges grade the SAME guess set; one self, one cross):")
    all_exact = all_hi = tot = 0
    self_hi_list, cross_hi_list = [], []
    for s in SOURCES:
        j1, j2 = JUDGES  # gpt, gemini
        ex = hi = c = 0
        for iid in item_ids:
            a, b = grades[(j1, s)].get(iid), grades[(j2, s)].get(iid)
            if a is None or b is None:
                continue
            c += 1
            ex += (a == b)
            hi += ((a == 2) == (b == 2))
            self_hi_list.append(1 if grades[(s, s)][iid] == 2 else 0)
            cross_hi_list.append(1 if grades[([j for j in JUDGES if j != s][0], s)][iid] == 2 else 0)
        print(f"  source={s:6s}: exact 0/1/2 agree {ex}/{c}={ex/max(c,1):.3f}  "
              f"high-vs-not agree {hi}/{c}={hi/max(c,1):.3f}")
        all_exact += ex; all_hi += hi; tot += c
    kap = kappa_binary(self_hi_list, cross_hi_list)
    print(f"  POOLED: exact {all_exact}/{tot}={all_exact/max(tot,1):.3f}  "
          f"high-vs-not {all_hi}/{tot}={all_hi/max(tot,1):.3f}  "
          f"Cohen-kappa(high, self-vs-cross) = {kap if kap is None else round(kap,3)}")

    # cost
    tot_cost, have, miss = billed_cost([[x for x in raw]])
    print(f"\nBILLED: ${tot_cost:.5f} (have={have} missing={miss})")

    if mode == "regrade-full":
        os.makedirs(RAWDIR, exist_ok=True)
        json.dump(raw, open(os.path.join(RAWDIR, "regrade_calls.json"), "w"), indent=2)
        summary = {
            "rubric_sha256": rubric_sha, "band": list(BAND),
            "cross_legs": [list(c) for c in CROSS],
            "per_leg_high_rate": {f"{j}_grades_{s}": leg_hi[(j, s)] for j in JUDGES for s in SOURCES},
            "band_metric_two_judge_mean_high": mean_hi, "verdict": verdict,
            "grades": {f"{j}_grades_{s}": grades[(j, s)] for j in JUDGES for s in SOURCES},
        }
        json.dump(summary, open(REGRADE, "w"), indent=2, sort_keys=True)
        sha = hashlib.sha256(open(REGRADE, "rb").read()).hexdigest()
        rcsha = hashlib.sha256(open(os.path.join(RAWDIR, "regrade_calls.json"), "rb").read()).hexdigest()
        print(f"\nwrote {REGRADE} sha256={sha}")
        print(f"wrote raw/regrade_calls.json sha256={rcsha}")


if __name__ == "__main__":
    main()
