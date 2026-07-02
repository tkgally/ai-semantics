#!/usr/bin/env python3
"""analyze.py — scoring + decomposition verdict for the commitment-framing probe. NO API CALLS.

Reads raw/*.json. For each item the model answered YES / NO / UNCLEAR; `endorsed` == YES. Per
(model, arm) over the 12 scenarios x 2 targets:

  presup_endorse  — P-endorse rate in this arm (12 items).
  entail_endorse  — E-endorse rate in this arm (12 items). The YES-BIAS CONTROL: a framing that
                    just makes the model say YES to everything lifts E too.
  gap             — presup_endorse - entail_endorse (the within-arm projection signal).

Six arms (see PREREG). Every arm holds the sentence constant (cond_antecedent); only the query
wrapper (SCENE x WORDING) varies.

Derived per model (all within-model, sentence held constant):
  scene_effect   = scene-only.P - base.P          (pure speaker-scene lift on the neutral question)
  wording_effect = commit.P - scene-only.P        (pure "committed" lift net of scene)
  commit_vs_bg   = commit.P - background.P         (near 0 => commit read as backgrounding)
  commit_vs_ai   = commit.P - atissue.P            (near 0 => commit read as at-issue)
  pole_spread    = background.P - atissue.P        (must be wide enough for the poles to discriminate)

VERDICT map (thresholds pre-registered in PREREG.md — NOT tuned here; may be tightened, never
loosened after seeing results):
  BAND              = 0.15   |Δ| below this = "same as" (commit clusters with a pole; effect is null)
  EFFECT            = 0.30   |Δ| at/above this = a real, attributable effect (scene / wording)
  POLE_MIN          = 0.30   background.P - atissue.P must be >= this for the poles to discriminate
  BASE_COLLAPSE_MAX = 0.60   base.P must be BELOW this for >=2/3 models (s159 collapse replicated)
  YESBIAS           = 0.60   per-arm entail_endorse at/above this flags a yes-shift confound on that arm
  GATE0_CLAUDE_RESCUE  = 0.60   claude commit.P must be >= this (rescued) for Gate 0
  GATE0_GPT_SUPPRESS   = 0.25   gpt commit.P must be <= this (suppressed) for Gate 0

Gate 0 (design validity): base reproduces the s159 collapse (base.P < BASE_COLLAPSE_MAX for >=2/3
models) AND the commit model-difference reappears (claude commit.P >= GATE0_CLAUDE_RESCUE AND gpt
commit.P <= GATE0_GPT_SUPPRESS). If either fails -> REPLICATION-ANOMALY, no reading claim.

Per-model advisory-c classification (source of the commit effect):
  WORDING-DRIVEN — |scene_effect| < BAND  and |wording_effect| >= EFFECT  (the word did it)
  SCENE-DRIVEN   — |scene_effect| >= EFFECT and |wording_effect| < BAND    (the scene did it)
  COUPLED        — both >= BAND  (no clean separation; advisory-c stands)
  NULL           — neither >= BAND  (the commit effect did not reproduce for this model)

Per-model reading classification (only meaningful where pole_spread >= POLE_MIN):
  BACKGROUNDING-READER — |commit_vs_bg| <= BAND and commit_vs_ai >= BAND   (predicted: claude)
  AT-ISSUE-READER      — |commit_vs_ai| <= BAND and commit_vs_bg <= -BAND  (predicted: gpt)
  UNDIFFERENTIATED     — otherwise, or pole_spread < POLE_MIN              (first-class null)

Overall verdict:
  CLEAN-DECOMPOSITION  — Gate 0 passes AND claude BACKGROUNDING-READER AND gpt AT-ISSUE-READER.
  PARTIAL              — Gate 0 passes and exactly one of {claude, gpt} classifies as hypothesised.
  NO-DECOMPOSITION     — Gate 0 passes but the key models are UNDIFFERENTIATED and/or COUPLED (NULL).
  REPLICATION-ANOMALY  — Gate 0 fails.

Usage: python3 analyze.py     # prints per-model/arm tables + verdict; writes results.json
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

BAND = 0.15
EFFECT = 0.30
POLE_MIN = 0.30
BASE_COLLAPSE_MAX = 0.60
YESBIAS = 0.60
GATE0_CLAUDE_RESCUE = 0.60
GATE0_GPT_SUPPRESS = 0.25

ARMS = ("base", "scene-only", "commit", "background", "atissue", "background-noscene")
# Slot -> the model whose Gate-0 role is checked. A = claude (rescued), B = gpt (suppressed).
SLOT_LABEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}


def parse_endorse(answer):
    """Return 'YES' / 'NO' / 'UNCLEAR' / None from the model's raw answer (first standalone token)."""
    if not answer:
        return None
    m = re.search(r"\b(yes|no|unclear)\b", answer.strip(), re.IGNORECASE)
    return m.group(1).upper() if m else None


def rate(x, n):
    return round(x / n, 3) if n else 0.0


def summarize(slot, recs):
    cells = {a: {"presup": [0, 0], "entail": [0, 0]} for a in ARMS}  # [endorsed, n]
    unparsed = 0
    for r in recs:
        e = parse_endorse(r.get("answer"))
        if e is None:
            unparsed += 1
        endorsed = 1 if e == "YES" else 0
        cells[r["arm"]][r["target_type"]][0] += endorsed
        cells[r["arm"]][r["target_type"]][1] += 1
    per_arm = {}
    for a in ARMS:
        p = rate(cells[a]["presup"][0], cells[a]["presup"][1])
        en = rate(cells[a]["entail"][0], cells[a]["entail"][1])
        per_arm[a] = {"presup_endorse": p, "entail_endorse": en, "gap": round(p - en, 3),
                      "yesbias_flag": en >= YESBIAS}
    P = {a: per_arm[a]["presup_endorse"] for a in ARMS}
    scene_effect = round(P["scene-only"] - P["base"], 3)
    wording_effect = round(P["commit"] - P["scene-only"], 3)
    commit_vs_bg = round(P["commit"] - P["background"], 3)
    commit_vs_ai = round(P["commit"] - P["atissue"], 3)
    pole_spread = round(P["background"] - P["atissue"], 3)

    # advisory-c classification (source of the commit effect)
    if abs(scene_effect) < BAND and abs(wording_effect) >= EFFECT:
        advisory_c = "WORDING-DRIVEN"
    elif abs(scene_effect) >= EFFECT and abs(wording_effect) < BAND:
        advisory_c = "SCENE-DRIVEN"
    elif abs(scene_effect) >= BAND and abs(wording_effect) >= BAND:
        advisory_c = "COUPLED"
    else:
        advisory_c = "NULL"

    # reading classification (only meaningful where the poles discriminate)
    if pole_spread < POLE_MIN:
        reading = "UNDIFFERENTIATED"
    elif abs(commit_vs_bg) <= BAND and commit_vs_ai >= BAND:
        reading = "BACKGROUNDING-READER"
    elif abs(commit_vs_ai) <= BAND and commit_vs_bg <= -BAND:
        reading = "AT-ISSUE-READER"
    else:
        reading = "UNDIFFERENTIATED"

    return {
        "slot": slot, "label": SLOT_LABEL.get(slot, slot), "n": len(recs), "unparsed": unparsed,
        "per_arm": per_arm,
        "base_collapsed": P["base"] < BASE_COLLAPSE_MAX,
        "derived": {"scene_effect": scene_effect, "wording_effect": wording_effect,
                    "commit_vs_bg": commit_vs_bg, "commit_vs_ai": commit_vs_ai,
                    "pole_spread": pole_spread},
        "advisory_c": advisory_c,
        "reading": reading,
    }


def verdict(per_model):
    by_slot = {m["slot"]: m for m in per_model}
    n = len(per_model)
    base_ok = sum(1 for m in per_model if m["base_collapsed"])
    base_replicated = base_ok >= 2

    claude = by_slot.get("A")
    gpt = by_slot.get("B")
    claude_rescued = bool(claude) and claude["per_arm"]["commit"]["presup_endorse"] >= GATE0_CLAUDE_RESCUE
    gpt_suppressed = bool(gpt) and gpt["per_arm"]["commit"]["presup_endorse"] <= GATE0_GPT_SUPPRESS
    gate0 = base_replicated and claude_rescued and gpt_suppressed

    claude_hyp = bool(claude) and claude["reading"] == "BACKGROUNDING-READER"
    gpt_hyp = bool(gpt) and gpt["reading"] == "AT-ISSUE-READER"

    if not gate0:
        reasons = []
        if not base_replicated:
            reasons.append(f"base collapse not replicated ({base_ok}/{n} below {BASE_COLLAPSE_MAX})")
        if not claude_rescued:
            cp = claude["per_arm"]["commit"]["presup_endorse"] if claude else None
            reasons.append(f"claude commit.P={cp} < {GATE0_CLAUDE_RESCUE} (not rescued)")
        if not gpt_suppressed:
            gp = gpt["per_arm"]["commit"]["presup_endorse"] if gpt else None
            reasons.append(f"gpt commit.P={gp} > {GATE0_GPT_SUPPRESS} (not suppressed)")
        headline = "REPLICATION-ANOMALY: " + "; ".join(reasons) + \
                   ". The commit model-difference is not present this run; no reading claim."
        overall = "REPLICATION-ANOMALY"
    elif claude_hyp and gpt_hyp:
        overall = "CLEAN-DECOMPOSITION"
        headline = (f"CLEAN-DECOMPOSITION: Gate 0 passes; claude=BACKGROUNDING-READER, "
                    f"gpt=AT-ISSUE-READER. The commit model-difference IS a difference in how "
                    f"'committed' is read (advisory-c: claude {claude['advisory_c']}, "
                    f"gpt {gpt['advisory_c']}).")
    elif claude_hyp or gpt_hyp:
        overall = "PARTIAL"
        which = "claude only" if claude_hyp else "gpt only"
        headline = (f"PARTIAL: Gate 0 passes; the reading split holds for {which} "
                    f"(claude={claude['reading']}, gpt={gpt['reading']}).")
    else:
        overall = "NO-DECOMPOSITION"
        headline = (f"NO-DECOMPOSITION (NULL): Gate 0 passes but neither key model reads commit as "
                    f"hypothesised (claude={claude['reading']}, gpt={gpt['reading']}); "
                    f"both readings survive.")

    return {
        "gate0": gate0, "base_replicated": base_replicated, "base_ok": base_ok, "n": n,
        "claude_rescued": claude_rescued, "gpt_suppressed": gpt_suppressed,
        "claude_reading": claude["reading"] if claude else None,
        "gpt_reading": gpt["reading"] if gpt else None,
        "claude_advisory_c": claude["advisory_c"] if claude else None,
        "gpt_advisory_c": gpt["advisory_c"] if gpt else None,
        "overall": overall, "headline": headline,
    }


def main():
    per_model = []
    for slot in ("A", "B", "C"):
        f = HERE / "raw" / f"{slot}.json"
        if not f.exists():
            print(f"(missing raw/{slot}.json — skipping)")
            continue
        recs = json.loads(f.read_text())
        per_model.append(summarize(slot, recs))
    if not per_model:
        sys.exit("no raw results found")
    print("=" * 88)
    for m in per_model:
        d = m["derived"]
        print(f"\n[{m['slot']}] {m['label']}  n={m['n']}  unparsed={m['unparsed']}  "
              f"base_collapsed={m['base_collapsed']}")
        for a in ARMS:
            pa = m["per_arm"][a]
            yb = "  [YES-BIAS]" if pa["yesbias_flag"] else ""
            print(f"    {a:20s} P={pa['presup_endorse']:.2f}  E={pa['entail_endorse']:.2f}"
                  f"  gap={pa['gap']:+.2f}{yb}")
        print(f"    -> scene_effect={d['scene_effect']:+.2f}  wording_effect={d['wording_effect']:+.2f}"
              f"  commit_vs_bg={d['commit_vs_bg']:+.2f}  commit_vs_ai={d['commit_vs_ai']:+.2f}"
              f"  pole_spread={d['pole_spread']:+.2f}")
        print(f"    -> advisory_c={m['advisory_c']}   reading={m['reading']}")
    v = verdict(per_model)
    print("\n" + "=" * 88)
    print(f"GATE 0: {'PASS' if v['gate0'] else 'FAIL'}  "
          f"(base_replicated={v['base_replicated']} {v['base_ok']}/{v['n']}, "
          f"claude_rescued={v['claude_rescued']}, gpt_suppressed={v['gpt_suppressed']})")
    print(f"VERDICT: {v['headline']}")
    (HERE / "results.json").write_text(json.dumps(
        {"thresholds": {"BAND": BAND, "EFFECT": EFFECT, "POLE_MIN": POLE_MIN,
                        "BASE_COLLAPSE_MAX": BASE_COLLAPSE_MAX, "YESBIAS": YESBIAS,
                        "GATE0_CLAUDE_RESCUE": GATE0_CLAUDE_RESCUE,
                        "GATE0_GPT_SUPPRESS": GATE0_GPT_SUPPRESS},
         "verdict": v, "per_model": per_model}, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
