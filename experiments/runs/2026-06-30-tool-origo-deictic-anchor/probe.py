#!/usr/bin/env python3
"""probe.py — the ONLY API caller for the as-if origo (tool-as-deictic-anchor) probe.

For each of the 45 frozen item-conditions (prep.py) and each panel model, runs a bounded
tool-calling loop and records (a) whether the model SPONTANEOUSLY issued a tool call, (b) which
tools it called, and (c) its FINAL natural-language answer. Scoring (resolution-to-tool-state,
spurious-override, hedge classification) is in analyze.py; this file only collects raw traces.

THE LOOP (tools available: test / control arms):
  turn 1: system + user + BOTH tools (get_current_time, get_current_location), tool_choice=auto.
    - if the assistant returns tool_calls -> SPONTANEOUS query. We append the assistant message and
      a NONCE tool result for each call (prep.TOOL_RETURNS), then continue.
    - else -> no spontaneous query; the assistant's content is the final answer.
  up to MAX_TURNS-1 tool rounds, then a final answer is taken from the last content.
The no-tool BASELINE arm sends no `tools` field (a plain completion over the same user text).

The system prompt NEVER mentions tools; tool_choice is auto — so a tool call is genuinely the
model's own move (spontaneity guard). Nonce returns (17:42 / 3021-11-08 / Qethport) are logged so
"resolved to tool-state" is unambiguous and cannot occur in the tool-free baseline.

FREEZE GUARD: refuses to run unless prep.py --check passes (frozen sha intact) and PREREG.md +
analyze.py exist — so items/spec cannot drift after the pre-run critic signs off.

Settings: temperature 0; gemini reasoning effort minimal (config/models.md caveat). Pre-flight
well under the $2.50 single-run flag (PREREG §cost); ABORT_USD guards a runaway bill.

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C] [--limit N] [--arm test|control|baseline]
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call_tools, billed_cost  # noqa: E402
from prep import ITEMS, SYS, TOOLS, TOOL_RETURNS, manifest_sha, FROZEN_SHA  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
ABORT_USD = 1.50  # pre-flight ~$0.25-0.8 billed expectation; hard stop well under the $2.50/run flag.
MAX_TURNS = 4     # 1 answer turn + up to 3 tool rounds (ample; items need at most one tool call).


def freeze_guard():
    out = subprocess.run([sys.executable, str(HERE / "prep.py"), "--check"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"FREEZE GUARD failed:\n{out.stdout}\n{out.stderr}")
    assert manifest_sha() == FROZEN_SHA, "manifest sha drift"
    for f in ("PREREG.md", "analyze.py"):
        if not (HERE / f).exists():
            sys.exit(f"FREEZE GUARD: missing {f}")


def run_item(model, it, reasoning, max_tokens):
    """Run the bounded tool loop for one item. Returns (record_fields, usage_list)."""
    tools = TOOLS if it["tools"] else None
    messages = [{"role": "system", "content": SYS},
                {"role": "user", "content": it["prompt"]}]
    called = []            # tool names called, in order (spontaneity trace)
    turn_contents = []     # assistant content at each turn (audit)
    usages = []
    final_content = ""
    error = None
    for turn in range(MAX_TURNS):
        r = call_tools(model, messages, tools=tools, max_tokens=max_tokens,
                       temperature=0, reasoning=reasoning)
        usages.append(r.get("usage", {}))
        msg = r.get("message")
        if msg is None:
            error = r.get("error")
            break
        content = msg.get("content") or ""
        turn_contents.append(content)
        tcs = msg.get("tool_calls")
        if tools and tcs:
            # Spontaneous tool call(s): echo the assistant turn, answer each with the NONCE return.
            messages.append({"role": "assistant", "content": msg.get("content"),
                             "tool_calls": tcs})
            for tc in tcs:
                name = tc.get("function", {}).get("name", "")
                called.append(name)
                ret = TOOL_RETURNS.get(name, {})
                messages.append({"role": "tool", "tool_call_id": tc.get("id", ""),
                                 "content": json.dumps(ret)})
            continue
        # No tool call this turn -> this content is the final answer.
        final_content = content
        break
    else:
        # Exhausted MAX_TURNS still calling tools; take the last content as final.
        final_content = turn_contents[-1] if turn_contents else ""
    rec = {
        "id": it["id"], "sid": it["sid"], "indexical": it["indexical"], "arm": it["arm"],
        "tools_available": it["tools"],
        "nonce_accept": it["nonce_accept"], "narrated_accept": it["narrated_accept"],
        "spontaneous_query": len(called) > 0,
        "tools_called": called,
        "n_turns": len(turn_contents),
        "final_content": final_content,
        "final_sha": hashlib.sha256(final_content.encode()).hexdigest()[:16],
        "usage": usages,          # list: one usage dict per turn
        "error": error,
    }
    return rec, usages


def run_model(slot, limit=None, arm=None):
    model = PANEL[slot]
    items = [it for it in ITEMS if (arm is None or it["arm"] == arm)]
    if limit:
        items = items[:limit]
    is_google = model.startswith("google/")
    reasoning = {"effort": "minimal"} if is_google else None
    max_tokens = 4096 if is_google else 512
    recs = []
    for it in items:
        rec, _ = run_item(model, it, reasoning, max_tokens)
        recs.append(rec)
        # running billed total across every turn of every record so far (abort guard)
        flat = [{"usage": u} for rr in recs for u in rr["usage"]]
        cost, have, miss = billed_cost([flat])
        if cost > ABORT_USD:
            sys.exit(f"ABORT: billed {cost:.4f} exceeds {ABORT_USD}")
    (RAW / f"{slot}.json").write_text(json.dumps(recs, indent=2, ensure_ascii=True) + "\n")
    flat = [{"usage": u} for rr in recs for u in rr["usage"]]
    cost, have, miss = billed_cost([flat])
    print(f"[{slot}] {model}: {len(recs)} items, billed ${cost:.4f} (cost on {have}, missing {miss})")
    return recs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"])
    ap.add_argument("--arm", choices=["test", "control", "baseline"])
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()
    freeze_guard()
    slots = [args.model] if args.model else ["A", "B", "C"]
    all_flat = []
    for slot in slots:
        recs = run_model(slot, args.limit, args.arm)
        all_flat.append([{"usage": u} for rr in recs for u in rr["usage"]])
        time.sleep(1)
    cost, have, miss = billed_cost(all_flat)
    print(f"TOTAL billed ${cost:.4f} (missing cost on {miss})")


if __name__ == "__main__":
    main()
