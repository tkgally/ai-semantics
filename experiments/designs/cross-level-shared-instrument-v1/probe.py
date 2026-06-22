"""Cross-level shared-instrument probe runner (build session 2026-06-22; NOT yet run).

BUILT + FROZEN, NOT RUN. No probe was run and NO money was spent in the build session
that wrote this file. Running is DEFERRED to a later session, gated by a fresh independent
pre-run critic GO/NO-GO against the frozen instrument.json (sha in instrument.sha256) and a
budget pre-flight (config/budget.md). This runner REFUSES to run unless invoked with
`--run --i-have-pre-run-critic-go` (see the refusal banner in __main__).

Operationalizes experiments/designs/cross-level-shared-instrument-v1.md under the RESOLVED
gate wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md (Option A +
binding conditions C1-C4). It applies ONE frozen shared commitment instrument identically at
three levels:

  lexical       : SAME/DIFFERENT/UNCLEAR + 0-100 confidence on a word's sense across two uses
  constructional: READING1/READING2/UNCLEAR + 0-100 confidence on a sentence's reading
  relational    : FIGURE1/FIGURE2/UNCLEAR + 0-100 confidence on a term's referent in a record

C1: the categorical DECLINE (%UNCLEAR), not the confidence integer, is load-bearing for the
moment pole. Both ride in ONE elicitation (one call per item). The analysis is a SEPARATE step
(analyze.py); this runner only collects raw outputs.

DATA/LICENCE: the constructional + relational items are synthetic and live in this repo
(items_constructional.json / items_relational.json). The lexical items are a MANIFEST
(items_lexical.json) referencing the gitignored DWUG/WiC fulltext frozen by the lexical leg;
the lexical arm reads that staged fulltext exactly as experiments/designs/
lexical-bridging-context-v1/probe.py does (stage it with that leg's prep.py / prep_wic.py
first, or run the constructional+relational arms alone with --skip-lexical).

Run (a LATER, spend-bearing session, after the pre-run-critic GO and a budget pre-flight):
    OPENROUTER_API_KEY=... python3 probe.py --run --i-have-pre-run-critic-go
"""
import argparse
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
INSTRUMENT = os.path.join(HERE, "instrument.json")
ITEMS_CX = os.path.join(HERE, "items_constructional.json")
ITEMS_REL = os.path.join(HERE, "items_relational.json")
RAW = os.path.join(HERE, "raw")
# lexical fulltext staged by the lexical leg's prep.py / prep_wic.py (gitignored)
DWUG_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "dwug", "lexical_bridging_v1_fulltext.jsonl"))
WIC_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "wic", "wic_poles_fulltext.jsonl"))

ABORT_USD = 0.60  # hard stop; matches instrument.json cost_control.abort_usd


def reasoning_for(model):
    """Cheapest working reasoning setting per model (cost-control knob, NOT a frozen
    instrument value). google/gemini-3.5-flash rejects suppression as of 2026-06-22, so it
    takes the sanctioned {"effort": "minimal"} fallback (reasoning_tokens=0); claude/gpt
    accept full suppression. No instrument value changes."""
    return {"effort": "minimal"} if model.startswith("google/") else {"enabled": False}


# ----- parsers (per-level pole tokens differ; UNCLEAR is shared) ------------------------
def parse_commit_conf(content, pole1, pole2):
    """Returns (call, conf): call in {pole1, pole2, 'UNCLEAR', None}; conf int 0-100 or None."""
    if not content:
        return None, None
    cu = content.upper()
    call_ = None
    for tok in (pole1, pole2, "UNCLEAR"):
        if tok in cu:
            call_ = tok
            break
    nums = re.findall(r"\d+", content)
    conf = max(0, min(100, int(nums[0]))) if nums else None
    return call_, conf


# ----- per-level user-prompt builders ----------------------------------------------------
def mark(ctx, span):
    a, b = span
    return ctx[:a] + "«" + ctx[a:b] + "»" + ctx[b:]


def user_lexical(it):
    lemma = it["lemma"].split("_")[0]
    s1 = mark(it["ctx1"], it["span1"])
    s2 = mark(it["ctx2"], it["span2"])
    return f"Target word: {lemma}\nSentence 1: {s1}\nSentence 2: {s2}\n"


def user_constructional(it):
    return (f"Sentence: {it['sentence']}\n"
            f"(1) {it['reading1']}\n(2) {it['reading2']}\n")


def user_relational(it):
    lines = ["Your figures:"]
    for f in it["figures"]:
        lines.append(f"- {f}")
    lines.append("")
    lines.append(f'Here is a record of how you and your partner used the term "{it["term"]}" '
                 "over several stamped rounds (a higher round number means more recently):")
    for h in it["history"]:
        lines.append(f"- {h}")
    lines.append("")
    lines.append(f'Question: Which of your figures does the term "{it["term"]}" refer to here?')
    lines.append(f"Candidate (1): {it['fig1']}.  Candidate (2): {it['fig2']}.")
    return "\n".join(lines) + "\n"


# ----- loaders ---------------------------------------------------------------------------
def load_lexical():
    items = []
    if not os.path.exists(DWUG_FULLTEXT):
        print(f"NOTE: {DWUG_FULLTEXT} absent -- lexical arm needs the gitignored DWUG "
              "fulltext staged by the lexical leg's prep.py. Use --skip-lexical to run the "
              "constructional+relational arms alone.")
        return None
    with open(DWUG_FULLTEXT, encoding="utf-8") as f:
        for line in f:
            it = json.loads(line)
            it["source"] = "dwug"
            items.append(it)
    if os.path.exists(WIC_FULLTEXT):
        with open(WIC_FULLTEXT, encoding="utf-8") as f:
            for line in f:
                it = json.loads(line)
                it["source"] = "wic"
                items.append(it)
    return items


def run_level(level, items, sys_prompt, user_fn, pole1, pole2, model, abort_state):
    recs = []
    for it in items:
        if abort_state["total"] >= ABORT_USD:
            print(f"  ABORT: billed ${abort_state['total']:.4f} >= ABORT_USD ${ABORT_USD}")
            break
        r = call(model, sys_prompt, user_fn(it), temperature=0,
                 reasoning=reasoning_for(model))
        call_, conf = parse_commit_conf(r.get("content"), pole1, pole2)
        u = r.get("usage") or {}
        abort_state["total"] += (u.get("cost") or 0.0)
        recs.append({"level": level, "item_id": it["item_id"],
                     "class": it.get("class") or it.get("bridging_class"),
                     "lemma": it.get("lemma"),  # carried forward so analyze.py clusters lexical by lemma (None for cx/rel)
                     "raw": r.get("content"), "call": call_, "conf": conf,
                     "error": r.get("error"), "usage": r.get("usage")})
    return recs


def main():
    cfg = json.load(open(INSTRUMENT, encoding="utf-8"))
    cx = json.load(open(ITEMS_CX, encoding="utf-8"))["items"]
    rel = json.load(open(ITEMS_REL, encoding="utf-8"))["items"]
    os.makedirs(RAW, exist_ok=True)
    skip_lex = "--skip-lexical" in sys.argv

    lex_items = None if skip_lex else load_lexical()
    L = cfg["levels"]
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        abort_state = {"total": total}
        bundles = []
        if lex_items:
            bundles.append(run_level("lexical", lex_items, L["lexical"]["system"],
                                     user_lexical, "SAME", "DIFFERENT", model, abort_state))
        bundles.append(run_level("constructional", cx, L["constructional"]["system"],
                                 user_constructional, "READING1", "READING2", model,
                                 abort_state))
        bundles.append(run_level("relational", rel, L["relational"]["system"],
                                 user_relational, "FIGURE1", "FIGURE2", model, abort_state))
        for b in bundles:
            if b:
                json.dump(b, open(os.path.join(RAW, f"{b[0]['level']}_{slot}.json"), "w"),
                          indent=1)
        billed, have, missing = billed_cost(bundles)
        total += billed
        summary[slot] = {"model": model, "cost_usd_billed": round(billed, 5),
                         "n_cost_missing": missing,
                         "elapsed_s": round(time.time() - t0, 1)}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")


REFUSAL = """\
========================================================================
REFUSED. This probe is BUILT + FROZEN but NOT cleared to run.
No money has been spent and none will be by this invocation.

A run requires, in a LATER session:
  1. a FRESH independent pre-run critic GO/NO-GO against the frozen
     instrument.json (sha in instrument.sha256) -- a NO-GO defers the run;
  2. a budget pre-flight per config/budget.md (est. $0.10-0.25; well under
     the $5/day cap), then ABORT_USD={abort} as a hard stop;
  3. for the lexical arm, the gitignored DWUG/WiC fulltext staged by the
     lexical leg's prep.py / prep_wic.py (or pass --skip-lexical).

When all three hold, invoke:
  OPENROUTER_API_KEY=... python3 probe.py --run --i-have-pre-run-critic-go
========================================================================
""".format(abort=ABORT_USD)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--i-have-pre-run-critic-go", action="store_true")
    ap.add_argument("--skip-lexical", action="store_true")
    args, _ = ap.parse_known_args()
    if not (args.run and args.i_have_pre_run_critic_go):
        print(REFUSAL)
        sys.exit(1)
    main()
