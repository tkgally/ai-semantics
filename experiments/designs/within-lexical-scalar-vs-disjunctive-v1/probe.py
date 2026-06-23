"""Within-lexical scalar-vs-disjunctive probe runner (build session 2026-06-23).

BUILT + FROZEN. Running is gated by a FRESH independent pre-run critic GO/NO-GO against the
frozen instrument.json (sha in instrument.sha256) + freeze_manifest.json, and a budget
pre-flight (config/budget.md). REFUSES to run unless invoked with
`--run --i-have-pre-run-critic-go`.

Operationalizes experiments/designs/within-lexical-scalar-vs-disjunctive-v1.md under the
RESOLVED gate wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md (ADOPT DEFAULT,
Option B + nuisance-matching freeze). ONE frozen lexical commitment instrument
(SAME/DIFFERENT/UNCLEAR + 0-100 confidence) is applied IDENTICALLY to two within-lexical arms:

  Arm 1 (scalar)      : DWUG bridging vs clear-same/clear-different (usage-similarity-capped)
  Arm 2 (disjunctive) : author-built balanced-homonym vs clear-same/clear-different (internal-contrast-only)

C1: the categorical DECLINE (%UNCLEAR), not the confidence integer, is load-bearing for the
moment pole. analyze.py is a SEPARATE step; this runner only collects raw outputs.

DATA/LICENCE: Arm 2 items are author-built and committed (items_arm2.json). Arm 1 is a MANIFEST
(items_arm1.json) referencing the gitignored DWUG fulltext frozen by the lexical leg; stage it
with experiments/designs/lexical-bridging-context-v1/prep.py first (or pass --skip-scalar to run
Arm 2 alone). NO DWUG corpus text is ever written into committed raw (Arm-1 raw carries item-id +
class + short labels only).

Run (a LATER, spend-bearing session, after the pre-run-critic GO + budget pre-flight):
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
ITEMS_ARM2 = os.path.join(HERE, "items_arm2.json")
RAW = os.path.join(HERE, "raw")
# Arm-1 fulltext staged by the lexical leg's prep.py (gitignored)
DWUG_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "dwug", "lexical_bridging_v1_fulltext.jsonl"))

ABORT_USD = 0.60  # hard stop; matches instrument.json cost_control.abort_usd


def reasoning_for(model):
    """Cheapest working reasoning setting per model (cost-control knob, NOT a frozen instrument
    value). gemini rejects suppression as of 2026-06-22 -> sanctioned {"effort":"minimal"}
    fallback (reasoning_tokens=0); claude/gpt accept full suppression."""
    return {"effort": "minimal"} if model.startswith("google/") else {"enabled": False}


def parse_commit_conf(content):
    """Returns (call, conf): call in {SAME, DIFFERENT, UNCLEAR, None}; conf int 0-100 or None.

    Confidence is the integer that FOLLOWS the chosen call token (the robust parser established
    by the cross-level run). For SAME/DIFFERENT/UNCLEAR there is no digit-in-token issue, so this
    equals the first-integer parse, but the after-token rule is kept for any reason-then-answer
    reply. The frozen format is '<TOKEN> <integer 0-100>, and nothing else'."""
    if not content:
        return None, None
    cu = content.upper()
    call_, after = None, None
    # precedence: first-appearing of the three tokens in the reply
    best_i = None
    for tok in ("SAME", "DIFFERENT", "UNCLEAR"):
        i = cu.find(tok)
        if i != -1 and (best_i is None or i < best_i):
            best_i, call_, after = i, tok, i + len(tok)
    seg = content[after:] if after is not None else content
    m = re.search(r"\d+", seg)
    conf = max(0, min(100, int(m.group()))) if m else None
    return call_, conf


def mark(ctx, span):
    a, b = span
    return ctx[:a] + "«" + ctx[a:b] + "»" + ctx[b:]


def user_lexical(it):
    lemma = it["lemma"].split("_")[0]
    s1 = mark(it["ctx1"], it["span1"])
    s2 = mark(it["ctx2"], it["span2"])
    return f"Target word: {lemma}\nSentence 1: {s1}\nSentence 2: {s2}\n"


def load_arm1():
    """Arm-1 items from the staged gitignored DWUG fulltext (bridging + clear-same/different)."""
    if not os.path.exists(DWUG_FULLTEXT):
        print(f"NOTE: {DWUG_FULLTEXT} absent -- Arm 1 needs the gitignored DWUG fulltext staged "
              "by lexical-bridging-context-v1/prep.py. Use --skip-scalar to run Arm 2 alone.")
        return None
    items = []
    with open(DWUG_FULLTEXT, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            items.append({"item_id": r["item_id"], "lemma": r["lemma"],
                          "class": r["bridging_class"],
                          "ctx1": r["ctx1"], "span1": r["span1"],
                          "ctx2": r["ctx2"], "span2": r["span2"],
                          "cluster": r["lemma"]})
    return items


def load_arm2():
    items = json.load(open(ITEMS_ARM2, encoding="utf-8"))["items"]
    for it in items:
        it["cluster"] = it["surface"]
    return items


def run_arm(arm, items, sys_prompt, model, abort_state):
    recs = []
    for it in items:
        if abort_state["total"] >= ABORT_USD:
            print(f"  ABORT: billed ${abort_state['total']:.4f} >= ABORT_USD ${ABORT_USD}")
            break
        r = call(model, sys_prompt, user_lexical(it), temperature=0,
                 reasoning=reasoning_for(model))
        call_, conf = parse_commit_conf(r.get("content"))
        u = r.get("usage") or {}
        abort_state["total"] += (u.get("cost") or 0.0)
        # raw carries NO corpus text for Arm 1 (item-id + class + cluster pointer only);
        # Arm 2 prose is author-built + already committed, so it is safe to keep its text.
        rec = {"arm": arm, "item_id": it["item_id"], "class": it["class"],
               "cluster": it["cluster"], "call": call_, "conf": conf,
               "raw": r.get("content"), "error": r.get("error"), "usage": r.get("usage")}
        if arm == "scalar":
            rec.pop("raw", None)  # never persist DWUG corpus text (it can echo in raw)
        recs.append(rec)
    return recs


def main():
    cfg = json.load(open(INSTRUMENT, encoding="utf-8"))
    sys_prompt = cfg["system"]
    os.makedirs(RAW, exist_ok=True)
    skip_scalar = "--skip-scalar" in sys.argv

    arm1 = None if skip_scalar else load_arm1()
    arm2 = load_arm2()
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        abort_state = {"total": total}
        bundles = []
        if arm1:
            bundles.append(("scalar", run_arm("scalar", arm1, sys_prompt, model, abort_state)))
        bundles.append(("disjunctive",
                        run_arm("disjunctive", arm2, sys_prompt, model, abort_state)))
        for arm, recs in bundles:
            json.dump(recs, open(os.path.join(RAW, f"{arm}_{slot}.json"), "w"), indent=1,
                      ensure_ascii=False)
        billed, have, missing = billed_cost([recs for _, recs in bundles])
        total += billed
        summary[slot] = {"model": model, "cost_usd_billed": round(billed, 5),
                         "n_cost_missing": missing, "elapsed_s": round(time.time() - t0, 1)}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")


REFUSAL = """\
========================================================================
REFUSED. This probe is BUILT + FROZEN but NOT cleared to run.
No money has been spent and none will be by this invocation.

A run requires, in a LATER session:
  1. a FRESH independent pre-run critic GO/NO-GO against the frozen
     instrument.json (sha in instrument.sha256) + freeze_manifest.json --
     a NO-GO defers the run (it does not relax a band);
  2. a budget pre-flight per config/budget.md (est. $0.10-0.25; well under
     the $5/day cap), then ABORT_USD={abort} as a hard stop;
  3. for Arm 1, the gitignored DWUG fulltext staged by
     lexical-bridging-context-v1/prep.py (or pass --skip-scalar).

When all three hold, invoke:
  OPENROUTER_API_KEY=... python3 probe.py --run --i-have-pre-run-critic-go
========================================================================
""".format(abort=ABORT_USD)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--i-have-pre-run-critic-go", action="store_true")
    ap.add_argument("--skip-scalar", action="store_true")
    args, _ = ap.parse_known_args()
    if not (args.run and args.i_have_pre_run_critic_go):
        print(REFUSAL)
        sys.exit(1)
    main()
