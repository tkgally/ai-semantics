"""Forced-decomposition (uptake-inducing) follow-up to the lexical bridging-context
working-surface re-run (session 82, 2026-06-22).

gpt-5.4-mini DECLINED the session-79 OFFERED working surface (>=85% bare one-token
answers), so its channel leg of result/lexical-bridging-context-working-surface-v1 is
untested (channel-not-taken-up). This probe FORCES uptake with a mandatory,
construction-neutral, answer-blind 3-step decomposition before the FINAL line, completing
the three-model channel check on the load-bearing ungraded-COMMITMENT posture.

SINGLE MANIPULATED VARIABLE vs the OFFERED surface: offered -> forced. This runner does NOT
hand-copy any task text. It loads the v1 instrument (sha-pinned) and the OFFERED
working-surface instrument (sha-pinned), reconstructs the offered system per framing exactly
as the working-surface probe does (v1 task description + offered answer clause), then
suffix-replaces ONLY the offered answer clause with the forced clause. So each forced system
= v1 task description (byte-identical) + forced clause; verify_format_only.py proves it and
prints the single-variable diff (offered opener -> forced 3-step preamble). Reasoning-effort
HELD CONSTANT at the v1/offered setting (gpt {"enabled": False}); the decomposition is
externalized in the VISIBLE channel only. gpt-only (PANEL slot B); a_forced dropped (cost,
characterizing-only). 4 framings x 88 items = 352 temp-0 calls.

Run (spend-bearing, after pre-run-critic GO + budget pre-flight):
    OPENROUTER_API_KEY=... python3 probe.py --calib 4   # measured per-item cost pre-flight
    OPENROUTER_API_KEY=... python3 probe.py              # full run (resumable)
"""
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import call, billed_cost  # noqa: E402

WORKERS = int(os.environ.get("PROBE_WORKERS", "8"))

# gpt-5.4-mini ONLY (claude/gemini already took up the OFFERED surface; see instrument.json
# panel_scope). Slot "B" mirrors config/models.md / openrouter.PANEL.
GPT_PANEL = {"B": "openai/gpt-5.4-mini"}
FRAMINGS = ["b_rel", "b_conf", "c_third", "topic"]  # verdict-bearing; a_forced dropped

HERE = os.path.dirname(os.path.abspath(__file__))
SELF_INSTRUMENT = os.path.join(HERE, "instrument.json")
OFFERED_INSTRUMENT = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-working-surface-v1", "instrument.json"))
V1_INSTRUMENT = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-v1", "instrument.json"))
DWUG_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "dwug", "lexical_bridging_v1_fulltext.jsonl"))
WIC_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "wic", "wic_poles_fulltext.jsonl"))
RAW = os.path.join(HERE, "raw")


def _sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def reasoning_for(model):
    """v1/offered setting, byte-identical: reasoning held CONSTANT (gpt {'enabled': False})."""
    return {"effort": "minimal"} if model.startswith("google/") else {"enabled": False}


def max_tokens_for(model):
    return 4096 if model.startswith("google/") else 2048


def build_systems():
    """Build the FORCED systems via the audited chain v1 -> offered -> forced (fail-closed)."""
    v1 = json.load(open(V1_INSTRUMENT, encoding="utf-8"))
    offered = json.load(open(OFFERED_INSTRUMENT, encoding="utf-8"))
    me = json.load(open(SELF_INSTRUMENT, encoding="utf-8"))

    v1_sha, off_sha = _sha(V1_INSTRUMENT), _sha(OFFERED_INSTRUMENT)
    prov = me["_provenance"]
    if v1_sha != prov["grandparent_v1_instrument_sha256"]:
        sys.exit(f"V1 SHA MISMATCH: {v1_sha} != {prov['grandparent_v1_instrument_sha256']}")
    if off_sha != prov["parent_offered_instrument_sha256"]:
        sys.exit(f"OFFERED SHA MISMATCH: {off_sha} != {prov['parent_offered_instrument_sha256']}")
    # cross-check: the offered instrument itself pins the v1 instrument
    if offered["_provenance"]["parent_instrument_sha256"] != v1_sha:
        sys.exit("CHAIN BROKEN: offered instrument's pinned v1 sha != actual v1 sha")

    ins = v1["instruments"]
    v1sys = {
        "b_rel": ins["B"]["framings"]["b_rel"]["system"],
        "b_conf": ins["B"]["framings"]["b_conf"]["system"],
        "c_third": ins["C"]["framings"]["c_third"]["system"],
        "topic": ins["Q3_context_control"]["framings"]["topic"]["system"],
    }
    off_repl = offered["framing_answer_clause_replacements"]
    fd_repl = me["framing_forced_clause_replacements"]
    systems = {}
    for fr in FRAMINGS:
        s_v1 = v1sys[fr]
        off_old, off_new = off_repl[fr]["old"], off_repl[fr]["new"]
        if not s_v1.endswith(off_old):
            sys.exit(f"FORMAT-ONLY VIOLATION ({fr}): v1 system does not end with the offered "
                     f"'old' clause -- chain broken.")
        s_off = s_v1[: len(s_v1) - len(off_old)] + off_new  # the OFFERED system
        fd_old, fd_new = fd_repl[fr]["old"], fd_repl[fr]["new"]
        if fd_old != off_new:
            sys.exit(f"CHAIN BROKEN ({fr}): forced 'old' != offered 'new' (not the offered clause).")
        if not s_off.endswith(fd_old):
            sys.exit(f"FORMAT-ONLY VIOLATION ({fr}): offered system does not end with the forced "
                     f"'old' clause -- chain broken.")
        systems[fr] = s_off[: len(s_off) - len(fd_old)] + fd_new  # the FORCED system
    return systems


def load_items():
    items = []
    if not os.path.exists(DWUG_FULLTEXT):
        sys.exit(f"missing {DWUG_FULLTEXT} -- run v1 prep.py first.")
    for line in open(DWUG_FULLTEXT, encoding="utf-8"):
        it = json.loads(line); it["source"] = "dwug"; items.append(it)
    if os.path.exists(WIC_FULLTEXT):
        for line in open(WIC_FULLTEXT, encoding="utf-8"):
            it = json.loads(line); it["source"] = "wic"; items.append(it)
    else:
        print(f"NOTE: {WIC_FULLTEXT} absent -- DWUG-only.")
    return items


def mark(ctx, span):
    a, b = span
    return ctx[:a] + "«" + ctx[a:b] + "»" + ctx[b:]


def user(it):
    lemma = it["lemma"].split("_")[0]
    return (f"Target word: {lemma}\nSentence 1: {mark(it['ctx1'], it['span1'])}\n"
            f"Sentence 2: {mark(it['ctx2'], it['span2'])}\n")


FINAL_RE = re.compile(r"final\s*:", re.IGNORECASE)
STEP_RE = re.compile(r"(?m)^\s*\d+[.)]")


def split_final(content):
    """(pre_final_text, text_after_last_FINAL, had_tag). No tag -> (whole, whole, False)."""
    if not content:
        return "", "", False
    ms = list(FINAL_RE.finditer(content))
    if not ms:
        return content, content, False
    last = ms[-1]
    return content[: last.start()], content[last.end():], True


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


SINGLE_PARSE = {
    "b_rel": parse_int100,
    "b_conf": parse_call_conf,
    "c_third": (lambda c: parse_choice(c, ["SAME", "DIFFERENT", "UNCLEAR"])),
    "topic": parse_int100,
}


def uptake(content, pre_final, n_steps, usage):
    """Metrics the uptake manipulation check needs (survive sanitize_raw: no corpus text)."""
    u = usage or {}
    rt = (u.get("completion_tokens_details") or {}).get("reasoning_tokens") \
        if isinstance(u.get("completion_tokens_details"), dict) else u.get("reasoning_tokens")
    return {"content_chars": len(content or ""),
            "pre_final_chars": len(pre_final or ""),
            "n_steps": n_steps,
            "completion_tokens": u.get("completion_tokens"),
            "reasoning_tokens": rt}


def _one(model, sys_prompt, it, temp):
    return it, call(model, sys_prompt, user(it), temperature=temp,
                    reasoning=reasoning_for(model), max_tokens=max_tokens_for(model))


def run_single(framing, sys_prompt, items, model, parse):
    out = [None] * len(items)
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(_one, model, sys_prompt, it, 0): i for i, it in enumerate(items)}
        for fut, i in futs.items():
            it, r = fut.result()
            content = r.get("content")
            pre, seg, had_tag = split_final(content)
            n_steps = len(STEP_RE.findall(pre or ""))
            rec = {"item_id": it["item_id"], "lemma": it["lemma"],
                   "bridging_class": it["bridging_class"], "source": it["source"],
                   "framing": framing, "raw": content, "final_seg": seg, "had_final_tag": had_tag,
                   "human_median": it["human_median"], "error": r.get("error"),
                   "usage": r.get("usage"),
                   "uptake": uptake(content, pre, n_steps, r.get("usage"))}
            if framing == "b_conf":
                rec["pred"], rec["pred2"] = parse(seg)
            else:
                rec["pred"] = parse(seg)
            out[i] = rec
    return out


def file_complete(path, n_expected):
    if not os.path.exists(path):
        return False
    try:
        return len(json.load(open(path, encoding="utf-8"))) == n_expected
    except Exception:  # noqa: BLE001
        return False


def main():
    calib = None
    if "--calib" in sys.argv:
        calib = int(sys.argv[sys.argv.index("--calib") + 1])

    systems = build_systems()
    items = load_items()
    if calib:
        items = items[:calib]
        print(f"CALIBRATION: {len(items)} items/framing (measured cost pre-flight)")
    n = len(items)
    print(f"{n} items (dwug={sum(1 for i in items if i['source']=='dwug')}, "
          f"wic={sum(1 for i in items if i['source']=='wic')}); gpt-only; framings={FRAMINGS}")
    os.makedirs(RAW, exist_ok=True)
    suffix = "_calib" if calib else ""

    for slot, model in GPT_PANEL.items():
        for framing in FRAMINGS:
            path = os.path.join(RAW, f"{framing}_{slot}{suffix}.json")
            if file_complete(path, n):
                print(f"skip {framing}_{slot} (complete)")
                continue
            print(f"run  {framing}_{slot} ...", flush=True)
            t0 = time.time()
            recs = run_single(framing, systems[framing], items, model, SINGLE_PARSE[framing])
            json.dump(recs, open(path, "w"), indent=1)
            print(f"  done {framing}_{slot} ({round(time.time()-t0,1)}s)", flush=True)

    # Cost + integrity summary
    summary, total = {}, 0.0
    for slot, model in GPT_PANEL.items():
        recs_lists, ncalls = [], 0
        for framing in FRAMINGS:
            path = os.path.join(RAW, f"{framing}_{slot}{suffix}.json")
            if os.path.exists(path):
                rl = json.load(open(path, encoding="utf-8"))
                recs_lists.append(rl); ncalls += len(rl)
        billed, have, missing = billed_cost(recs_lists)
        total += billed
        summary[slot] = {"model": model, "n_calls": ncalls,
                         "cost_usd_billed": round(billed, 5), "n_cost_missing": missing}
        print(json.dumps(summary[slot], indent=1))

    json.dump(summary, open(os.path.join(RAW, f"run_summary{suffix}.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")
    if calib:
        print(f"per-item/framing: ${total/max(1,n*len(FRAMINGS)):.6f}; FULL 88-item projection "
              f"(x {88/n:.1f}): ${total * 88 / n:.4f}")


if __name__ == "__main__":
    main()
