#!/usr/bin/env python3
"""harvest.py — the PRE-HEADLINE baseline/headroom arm for the third-construction
(caused-motion) preference/commitment double contrast
(run 2026-06-15-third-construction-preference-commitment-v1). Calls the API.

Implements design §5 (the PRE-REGISTERED HARD GATE G1-G4) under the RATIFIED
decision decisions/resolved/aann-uniqueness-third-construction (Option A; Option C
the binding fallback). Authorized by the INDEPENDENT PRE-RUN CRITIC GO (this session)
which authorized the HARVEST ARM ONLY (~288-360 calls) and GATED the headline on the
harvest clearing G2 for >= 2/3 models, with a FAIL routing to Option C (no retuning).

WHAT IT DOES
------------
  * loads candidates.json (frozen by prep.py; 48 marginal + 12 clean items);
  * runs TWO instruments on EVERY candidate item, both well-formed frames:
      paraphrase forced-choice  -> affirm = chose the construction reading C
      NLI entailment            -> affirm = NLI == 0 (entailment)
  * affirm-causation := (FC chose C) OR (NLI == 0), pooled as design §5 specifies;
  * computes G1 (per-model marginal affirm rate), G3 (per-model clean affirm rate),
    evaluates G2 (per-model marginal <= 0.50; target <= 0.30) and G4 (>= 2/3 models
    clear G2), plus per-verb pooled affirm rates for the §3 subset-selection rule;
  * writes harvest.json with raw rows + the deterministic gate verdict + the
    pre-registered selected-verb list. Does NOT freeze stimuli.json — that is a
    SEPARATE verification-gated step (critic condition 5: an independent post-harvest
    reading recomputes G1-G4 before any headline stimuli are frozen).

Settings: temperature 0; gemini (slot C) reasoning effort minimal via the shared lib.
ABORT_USD = 0.30 (pre-flight ~$0.05-0.12); abort if running billed cost exceeds it.
Idempotent: re-running skips existing raw/*.json. Billed usage.cost summed; missing
cost counted, never dropped.

Usage: OPENROUTER_API_KEY=... python3 harvest.py [--model A|B|C] [--arm paraphrase|nli]
       python3 harvest.py --evaluate-only     (recompute gate from existing raw/, no API)
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
CAND = json.load(open(HERE / "candidates.json"))
ITEMS = CAND["items"]
RULE = CAND["selection_rule"]
ARMS = ["paraphrase", "nli"]
MODELS = ["A", "B", "C"]
ABORT_USD = 0.30

# ---- NLI instrument: REUSED VERBATIM from conative-preference-commitment-v1 ----
NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)
PARA_SYS = "You are a careful native-speaker reader of English."
P_PARA = (
    "Read the sentence, then choose which paraphrase the sentence better "
    "supports. Respond with ONLY the letter A or B.\n\n"
    "Sentence: {sentence}\n\nA: {a}\nB: {b}")

_STRIP = ".,!:;'\"*`"


def parse_nli(c):
    if not c:
        return None
    digs = re.findall(r"[012]", c)
    return digs[-1] if digs else None


def parse_ab(text):
    if text is None:
        return None
    t = text.strip().upper().strip(_STRIP).strip()
    if t in ("A", "B"):
        return t
    found = None
    for tok in t.replace("\n", " ").replace(":", " ").split():
        tok = tok.strip(_STRIP)
        if tok in ("A", "B"):
            found = tok
    return found


PARSERS = {"paraphrase": parse_ab, "nli": parse_nli}


def ask(slot, system, user):
    kwargs = {"reasoning": {"effort": "minimal"}} if slot == "C" else {}
    return call(PANEL[slot], system, user, temperature=0, **kwargs)


def tasks_for(arm):
    tasks = []
    for it in ITEMS:
        if arm == "paraphrase":
            user = P_PARA.format(sentence=it["sentence"], a=it["option_A"], b=it["option_B"])
            sysmsg = PARA_SYS
        else:
            user = f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"
            sysmsg = NLI_SYS
        meta = {"item_id": it["item_id"], "family": it["family"],
                "marginality": it["marginality"], "verb": it["verb"],
                "obj": it["obj"], "arm": arm,
                "construction_letter": it["construction_letter"]}
        tasks.append((meta, sysmsg, user))
    return tasks


def affirm_of(arm, meta, val):
    """affirm-causation := FC chose the construction-reading letter, or NLI == 0."""
    if val is None:
        return None
    if arm == "paraphrase":
        return 1 if val == meta["construction_letter"] else 0
    return 1 if val == "0" else 0


def run_arm(slot, arm, records):
    out = RAW / f"{slot}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    rows = []
    for i, (meta, system, user) in enumerate(tasks_for(arm)):
        r = ask(slot, system, user)
        val = PARSERS[arm](r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, system, user)
            val = PARSERS[arm](r["content"])
        row = dict(meta)
        row.update({"raw": r["content"], "value": val,
                    "affirm": affirm_of(arm, meta, val),
                    "usage": r.get("usage"), "error": r.get("error")})
        rows.append(row)
        records.append(r)
        if (i + 1) % 20 == 0:
            c, _, nmiss = billed_cost([records])
            print(f"  {slot}/{arm}: {i+1}/{len(rows)} cost ${c:.4f}"
                  + (f" ({nmiss} missing)" if nmiss else ""), flush=True)
            if c >= ABORT_USD:
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                sys.exit(f"ABORT: ${ABORT_USD} reached; wrote {out}.partial")
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    print(f"{slot}/{arm}: {len(rows)} rows, {miss} missing -> {out}")


def load_rows():
    rows = []
    for slot in MODELS:
        for arm in ARMS:
            f = RAW / f"{slot}-{arm}.json"
            if f.exists():
                for r in json.load(open(f)):
                    r["model"] = slot
                    rows.append(r)
    return rows


def rate(rows):
    a = [r["affirm"] for r in rows if r["affirm"] is not None]
    return (sum(a) / len(a), len(a)) if a else (None, 0)


def evaluate():
    """Compute and print G1-G4 + per-verb rates; return the gate-verdict dict."""
    rows = load_rows()
    if not rows:
        print("no raw rows yet — run the arms first."); return None
    verdict = {"per_model": {}, "per_verb": {}, "rule": RULE}
    print("\n=== HEADROOM GATE EVALUATION (design §5) ===")
    g2_pass = []
    for slot in MODELS:
        mrows = [r for r in rows if r["model"] == slot and r["family"] == "marginal"]
        crows = [r for r in rows if r["model"] == slot and r["family"] == "clean"]
        g1, n1 = rate(mrows)                       # G1 marginal affirm
        g3, n3 = rate(crows)                       # G3 clean affirm
        p2 = g1 is not None and g1 <= RULE["g2_per_model_ceiling"]
        p2t = g1 is not None and g1 <= RULE["g2_per_model_target"]
        p3 = g3 is not None and g3 >= RULE["g3_clean_floor"]
        g2_pass.append(p2)
        verdict["per_model"][slot] = {
            "marginal_affirm_G1": g1, "n_marginal": n1,
            "clean_affirm_G3": g3, "n_clean": n3,
            "G2_pass_ceiling_0.50": p2, "G2_pass_target_0.30": p2t,
            "G3_pass_floor_0.85": p3}
        print(f"  {slot} ({PANEL[slot]}): marginal G1={g1:.3f} (n={n1})  "
              f"clean G3={g3:.3f} (n={n3})  "
              f"G2{'PASS' if p2 else 'FAIL'}(<=0.50){'/target' if p2t else ''}  "
              f"G3{'PASS' if p3 else 'FAIL'}(>=0.85)")
    n_pass = sum(g2_pass)
    g4 = n_pass >= RULE["g4_min_models_pass"]
    verdict["G4_models_passing_G2"] = n_pass
    verdict["G4_gate"] = "PASS" if g4 else "FAIL"
    print(f"\n  G4: {n_pass}/3 models clear G2 (<=0.50)  ->  "
          f"{'PASS — headroom exists; proceed to subset selection' if g4 else 'FAIL — route to OPTION C (AANN-specific so far; no retuning)'}")

    # ---- per-verb pooled affirm rate (over models x instruments x objects) ----
    print("\n=== PER-VERB pooled affirm rate (marginal arm; for §3 subset selection) ===")
    verbs = {}
    for r in rows:
        if r["family"] != "marginal":
            continue
        verbs.setdefault(r["verb"], {"rows": [], "marginality": r["marginality"]})
        verbs[r["verb"]]["rows"].append(r)
    selected = []
    for v in sorted(verbs, key=lambda k: rate(verbs[k]["rows"])[0]):
        vr, vn = rate(verbs[v]["rows"])
        keep = vr is not None and vr <= RULE["verb_retain_ceiling"]
        target = vr is not None and vr <= RULE["verb_retain_target"]
        verdict["per_verb"][v] = {"affirm": vr, "n": vn,
                                  "marginality": verbs[v]["marginality"],
                                  "retain_<=0.50": keep, "<=0.30_target": target}
        if keep:
            selected.append(v)
        print(f"  {v:11s} [{verbs[v]['marginality']:17s}] affirm={vr:.3f} (n={vn})  "
              f"{'RETAIN' if keep else 'drop'}{' (<=0.30)' if target else ''}")
    verdict["selected_verbs"] = selected
    verdict["n_selected"] = len(selected)
    min_v = RULE["min_verbs_retained"]
    enough = len(selected) >= min_v
    verdict["subset_min_met"] = enough
    print(f"\n  subset: {len(selected)} verbs retain (<=0.50); need >= {min_v}  ->  "
          f"{'OK' if enough else 'INSUFFICIENT'}")
    headline_ok = g4 and enough
    verdict["headline_authorized"] = headline_ok
    print(f"\n  HEADLINE AUTHORIZED: {headline_ok}  "
          f"({'G4 PASS and >=10 verbs retained' if headline_ok else 'gate or subset failed -> OPTION C terminal close'})")
    json.dump(verdict, open(HERE / "harvest.json", "w"), indent=1)
    print(f"\nwrote gate verdict -> {HERE / 'harvest.json'}")
    return verdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=MODELS, default=None)
    ap.add_argument("--arm", choices=ARMS, default=None)
    ap.add_argument("--evaluate-only", action="store_true")
    args = ap.parse_args()
    if not args.evaluate_only:
        slots = [args.model] if args.model else MODELS
        arms = [args.arm] if args.arm else ARMS
        records = []
        for slot in slots:
            for arm in arms:
                run_arm(slot, arm, records)
        total, _, nmiss = billed_cost([records])
        print(f"\nTOTAL billed this invocation: ${total:.4f}"
              + (f"  ({nmiss} missing usage.cost — undercounts)" if nmiss else ""))
        with open(RAW / "cost-log.txt", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                    f"harvest slots={slots} arms={arms} billed=${total:.4f} "
                    f"missing_cost_calls={nmiss}\n")
    evaluate()


if __name__ == "__main__":
    main()
