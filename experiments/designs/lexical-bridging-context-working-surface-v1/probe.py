"""Working-surface re-run of the lexical bridging-context probe v1 (session 79, 2026-06-22).

Tests whether v1's ungraded-COMMITMENT null (result/lexical-bridging-context-v1) survives a
WIDENED OUTPUT CHANNEL. v1 read the commitment off a constrained single-label channel
('Answer with ... and nothing else'); essay/output-channel-confound holds a forced-format
negative is channel-bounded until the channel is varied; open-question/gradience-population-
not-moment names this exact re-run as the discriminator.

FORMAT-ONLY BY CONSTRUCTION. This runner does NOT hand-copy the v1 task text. It LOADS the
parent v1 instrument.json (sha-pinned), asserts each variant 'old' clause is a verbatim
SUFFIX of the v1 system string, and replaces ONLY that suffix with the working-surface
clause. The task description is therefore byte-identical to v1. The only manipulations are:
(1) the answer-format clause (working surface + FINAL tag), and (2) max_tokens raised so the
visible channel can carry the working. Reasoning-effort is HELD CONSTANT at the v1 setting
(claude/gpt {"enabled": False}; gemini {"effort": "minimal"}) — the surface is opened ONLY in
the visible output channel.

Same 88 items as v1 (reads the same gitignored full-text staged by v1's prep.py +
map_wic_fulltext.py), same temperatures, same A sample count, same classes. Records per-call
completion_tokens / reasoning_tokens / content length / FINAL-tag presence for the UPTAKE
report the essay's uptake clause requires.

Run (spend-bearing, after pre-run-critic GO + budget pre-flight):
    OPENROUTER_API_KEY=... python3 probe.py            # full run
    OPENROUTER_API_KEY=... python3 probe.py --calib 3  # measured per-model calibration only
    OPENROUTER_API_KEY=... python3 probe.py --no-a     # drop A dispersion (cost control)
"""
import hashlib
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SELF_INSTRUMENT = os.path.join(HERE, "instrument.json")
PARENT_INSTRUMENT = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-v1", "instrument.json"))
DWUG_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "dwug", "lexical_bridging_v1_fulltext.jsonl"))
WIC_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "wic", "wic_poles_fulltext.jsonl"))
RAW = os.path.join(HERE, "raw")


def reasoning_for(model):
    """v1 setting, byte-identical — reasoning-effort held CONSTANT (see provenance)."""
    return {"effort": "minimal"} if model.startswith("google/") else {"enabled": False}


def max_tokens_for(model):
    """Output-channel width: room to externalize working (v1 used 64 for claude/gpt)."""
    return 4096 if model.startswith("google/") else 2048


def build_systems():
    """Construct the working-surface system prompts FROM v1, enforcing format-only."""
    parent = json.load(open(PARENT_INSTRUMENT, encoding="utf-8"))
    me = json.load(open(SELF_INSTRUMENT, encoding="utf-8"))
    # parent sha pin re-check (fail closed)
    parent_sha = hashlib.sha256(open(PARENT_INSTRUMENT, "rb").read()).hexdigest()
    pinned = me["_provenance"]["parent_instrument_sha256"]
    if parent_sha != pinned:
        sys.exit(f"PARENT SHA MISMATCH: {parent_sha} != pinned {pinned} — aborting.")
    ins = parent["instruments"]
    v1sys = {
        "b_rel": ins["B"]["framings"]["b_rel"]["system"],
        "b_conf": ins["B"]["framings"]["b_conf"]["system"],
        "c_third": ins["C"]["framings"]["c_third"]["system"],
        "topic": ins["Q3_context_control"]["framings"]["topic"]["system"],
        "a_forced": ins["A"]["framings"]["a_forced"]["system"],
    }
    repl = me["framing_answer_clause_replacements"]
    systems = {}
    for fr, s in v1sys.items():
        old, new = repl[fr]["old"], repl[fr]["new"]
        if not s.endswith(old):
            sys.exit(f"FORMAT-ONLY VIOLATION: '{fr}' v1 system does not end with the pinned "
                     f"'old' clause — aborting (would change task text).")
        systems[fr] = s[: len(s) - len(old)] + new
    # also surface the frozen A sample count / temperatures, taken from v1 (unchanged)
    a_cfg = {"n_samples": parent["instruments"]["A"]["n_samples"],
             "temperature": parent["instruments"]["A"]["temperature"]}
    return systems, a_cfg


def load_items():
    items = []
    if not os.path.exists(DWUG_FULLTEXT):
        sys.exit(f"missing {DWUG_FULLTEXT} — run v1 prep.py first.")
    for line in open(DWUG_FULLTEXT, encoding="utf-8"):
        it = json.loads(line); it["source"] = "dwug"; items.append(it)
    if os.path.exists(WIC_FULLTEXT):
        for line in open(WIC_FULLTEXT, encoding="utf-8"):
            it = json.loads(line); it["source"] = "wic"; items.append(it)
    else:
        print(f"NOTE: {WIC_FULLTEXT} absent — DWUG-only.")
    return items


def mark(ctx, span):
    a, b = span
    return ctx[:a] + "«" + ctx[a:b] + "»" + ctx[b:]


def user(it):
    lemma = it["lemma"].split("_")[0]
    return (f"Target word: {lemma}\nSentence 1: {mark(it['ctx1'], it['span1'])}\n"
            f"Sentence 2: {mark(it['ctx2'], it['span2'])}\n")


FINAL_RE = re.compile(r"final\s*:", re.IGNORECASE)


def final_segment(content):
    """Return (text_after_last_FINAL, had_tag). Falls back to whole content if no tag."""
    if not content:
        return "", False
    matches = list(FINAL_RE.finditer(content))
    if not matches:
        return content, False
    return content[matches[-1].end():], True


def parse_int100(c):
    if not c:
        return None
    m = re.findall(r"\d+", c)
    return max(0, min(100, int(m[0]))) if m else None


def parse_call_conf(c):
    if not c:
        return None, None
    cu = c.upper()
    call_ = "SAME" if "SAME" in cu else ("DIFFERENT" if "DIFF" in cu else None)
    return call_, parse_int100(c)


def parse_choice(c, opts):
    if not c:
        return None
    cu = c.upper()
    for o in opts:
        if o in cu:
            return o
    return None


def uptake(content, usage):
    u = usage or {}
    return {"content_chars": len(content or ""),
            "completion_tokens": u.get("completion_tokens"),
            "reasoning_tokens": (u.get("completion_tokens_details") or {}).get("reasoning_tokens")
            if isinstance(u.get("completion_tokens_details"), dict) else u.get("reasoning_tokens")}


def run_single(framing, sys_prompt, items, model, parse):
    recs = []
    for it in items:
        r = call(model, sys_prompt, user(it), temperature=0,
                 reasoning=reasoning_for(model), max_tokens=max_tokens_for(model))
        content = r.get("content")
        seg, had_tag = final_segment(content)
        rec = {"item_id": it["item_id"], "lemma": it["lemma"],
               "bridging_class": it["bridging_class"], "source": it["source"],
               "framing": framing, "raw": content, "final_seg": seg, "had_final_tag": had_tag,
               "human_median": it["human_median"], "error": r.get("error"),
               "usage": r.get("usage"), "uptake": uptake(content, r.get("usage"))}
        if framing == "b_conf":
            rec["pred"], rec["pred2"] = parse(seg)
        else:
            rec["pred"] = parse(seg)
        recs.append(rec)
    return recs


def run_dispersion(framing, sys_prompt, items, model, n_samples, temp, parse):
    recs = []
    for it in items:
        picks, usages, raws, tags, ups = [], [], [], [], []
        for _ in range(n_samples):
            r = call(model, sys_prompt, user(it), temperature=temp,
                     reasoning=reasoning_for(model), max_tokens=max_tokens_for(model))
            content = r.get("content")
            seg, had_tag = final_segment(content)
            picks.append(parse(seg)); usages.append(r.get("usage")); raws.append(content)
            tags.append(had_tag); ups.append(uptake(content, r.get("usage")))
        recs.append({"item_id": it["item_id"], "lemma": it["lemma"],
                     "bridging_class": it["bridging_class"], "source": it["source"],
                     "framing": framing, "picks": picks, "raws": raws,
                     "had_final_tag": tags, "uptake_list": ups,
                     "human_median": it["human_median"], "usage_list": usages})
    return recs


SINGLE_PARSE = {
    "b_rel": parse_int100,
    "b_conf": parse_call_conf,
    "c_third": (lambda c: parse_choice(c, ["SAME", "DIFFERENT", "UNCLEAR"])),
    "topic": parse_int100,
}


def file_complete(path, n_expected):
    """A framing file counts as done if it exists and has n_expected records."""
    if not os.path.exists(path):
        return False
    try:
        return len(json.load(open(path, encoding="utf-8"))) == n_expected
    except Exception:  # noqa: BLE001
        return False


def main():
    calib = None
    no_a = "--no-a" in sys.argv
    if "--calib" in sys.argv:
        calib = int(sys.argv[sys.argv.index("--calib") + 1])

    systems, a_cfg = build_systems()
    items = load_items()
    if calib:
        items = items[:calib]
        print(f"CALIBRATION: {len(items)} items/model (measured cost pre-flight)")
    n = len(items)
    print(f"{n} items (dwug={sum(1 for i in items if i['source']=='dwug')}, "
          f"wic={sum(1 for i in items if i['source']=='wic')}); no_a={no_a}")
    os.makedirs(RAW, exist_ok=True)
    suffix = "_calib" if calib else ""

    # RESUMABLE: iterate (slot, framing); skip framing files already complete (n records).
    # Each file is written immediately, so a killed run loses at most the in-flight framing
    # and a re-launch of the SAME command picks up where it stopped.
    for slot, model in PANEL.items():
        for framing, parse in SINGLE_PARSE.items():
            path = os.path.join(RAW, f"{framing}_{slot}{suffix}.json")
            if file_complete(path, n):
                print(f"skip {framing}_{slot} (complete)")
                continue
            print(f"run  {framing}_{slot} ...", flush=True)
            t0 = time.time()
            recs = run_single(framing, systems[framing], items, model, parse)
            json.dump(recs, open(path, "w"), indent=1)
            print(f"  done {framing}_{slot} ({round(time.time()-t0,1)}s)", flush=True)
        if not no_a:
            path = os.path.join(RAW, f"a_forced_{slot}{suffix}.json")
            if not file_complete(path, n):
                print(f"run  a_forced_{slot} ...", flush=True)
                a_recs = run_dispersion("a_forced", systems["a_forced"], items, model,
                                        a_cfg["n_samples"], a_cfg["temperature"],
                                        lambda c: parse_choice(c, ["SAME", "DIFFERENT"]))
                json.dump(a_recs, open(path, "w"), indent=1)
            else:
                print(f"skip a_forced_{slot} (complete)")

    # Cost + integrity summary, recomputed from whatever files exist on disk.
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        recs_lists, ncalls = [], 0
        for framing in SINGLE_PARSE:
            path = os.path.join(RAW, f"{framing}_{slot}{suffix}.json")
            if os.path.exists(path):
                rl = json.load(open(path, encoding="utf-8"))
                recs_lists.append(rl); ncalls += len(rl)
        apath = os.path.join(RAW, f"a_forced_{slot}{suffix}.json")
        if os.path.exists(apath):
            a_recs = json.load(open(apath, encoding="utf-8"))
            au = [{"usage": u} for r in a_recs for u in r["usage_list"]]
            recs_lists.append(au); ncalls += len(au)
        billed, have, missing = billed_cost(recs_lists)
        total += billed
        summary[slot] = {"model": model, "n_calls": ncalls,
                         "cost_usd_billed": round(billed, 5), "n_cost_missing": missing}
        print(json.dumps(summary[slot], indent=1))

    json.dump(summary, open(os.path.join(RAW, f"run_summary{suffix}.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")
    if calib:
        print(f"per-item/all-models: ${total/max(1,n):.5f}; FULL 88-item projection "
              f"(x {88/n:.1f}): ${total * 88 / n:.4f}" + ("  [A dropped]" if no_a else ""))


if __name__ == "__main__":
    main()
