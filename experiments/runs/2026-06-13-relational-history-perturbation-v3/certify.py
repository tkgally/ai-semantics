#!/usr/bin/env python3
"""certify.py — per-description certification (v3 fix 2) -> certification_report.json.

Design (experiments/designs/relational-history-perturbation-v3.md §Stimuli plan): each
distinct harvested candidate gets ONE certification call — a fresh SAME-MODEL matcher,
probe-shaped prompt, the single description line, no nonce, no history: which figure is
described? Certified iff correct. The first 6 certified descriptions per figure
(deterministic harvest order) are frozen in; 6 = 3 samples x 2 descriptions.

MECHANICAL CHECKS (run before any model-based check, deterministic, no API):
  - non-empty after normalization;
  - <= 12 words (the requested v1 budget, enforced; over-budget candidates are logged
    and dropped, never silently kept);
  - deduplication WITHIN the figure and AGAINST THE TWIN's set (case-insensitive,
    whitespace-normalized; second occurrence in canonical processing order is dropped —
    a description shared with the twin cannot discriminate the pair).

MODEL-BASED CHECK: one forced-format certification call per surviving candidate (same
elicitation/parse/retry discipline as the probe, from common.py; certification uses the
same model whose record the description will populate — the convention under test is
model-internal; design open issue 5 flags an optional cross-model cross-check for the
critic).

ANTI-NULL BIAS, DISCLOSED (embedded verbatim in the report): certification selects for
individually discriminative lines, which SHARPENS the X-vs-Y conflict — it biases AGAINST
the ~0.5-noise-toward-the-null failure mode (v2 critic B2), not toward the conjecture's
bet.

Certification raw is STIMULUS-CONSTRUCTION data: kept, never analyzed as findings.
Idempotent: candidates already certified in raw/certification.jsonl are not re-called,
so the harvest -> certify -> topup -> certify loop only pays for new candidates.

Usage (from repo root or this dir):
  python3 certify.py plan   # no API calls: lists pending certification calls + estimate
  python3 certify.py run    # certification calls + (re)writes certification_report.json
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (MODELS, MODEL_SEED_OFFSET, SEED0, WORD_BUDGET, N_SAMPLES,  # noqa: E402
                    DESCS_PER_FIG, RAW, CERT_SYS, load_figures, figure_pairs,
                    grid_block, call_forced, flat_cost, ledger_append, check_hard_stop,
                    append_jsonl, read_jsonl)

HARVEST_PATH = os.path.join(RAW, "harvest.jsonl")
CERT_PATH = os.path.join(RAW, "certification.jsonl")
REPORT_PATH = os.path.join(HERE, "certification_report.json")
EST_PER_CALL = 0.0013  # probe-shaped (v2 billed ~$0.0013/call)

ANTI_NULL_BIAS_DISCLOSURE = (
    "Certification selects for individually discriminative lines, which sharpens the "
    "X-vs-Y conflict - i.e. it biases AGAINST the ~0.5-noise-toward-the-null failure mode "
    "the v2 critic identified (B2), not toward the conjecture's bet. (Design "
    "relational-history-perturbation-v3, 'Known bias direction, disclosed'.)")


def norm(desc):
    return " ".join(desc.split()).casefold()


def gather_candidates():
    """Deterministic candidate roster per (model, fig): harvest-phase calls first, then
    top-ups, list order within each call preserved. Mechanical checks applied here."""
    figs = load_figures()
    pairs = figure_pairs(figs)
    twin = {}
    for a, b in pairs.values():
        twin[a], twin[b] = b, a
    recs = read_jsonl(HARVEST_PATH)
    if not recs:
        sys.exit("no raw/harvest.jsonl — run harvest.py harvest first.")
    raw_lists = {}  # (model, fig) -> [desc, ...] in deterministic order
    for phase in ("harvest", "topup"):
        for r in recs:
            if r["phase"] == phase:
                raw_lists.setdefault((r["model"], r["fig"]), []).extend(r["candidates"])
    kept, census = {}, []
    for m in MODELS:                                # fixed model order
        seen = {}                                   # fig -> set of normalized kept descs
        for pid in sorted(pairs):                   # canonical processing order
            for fid in pairs[pid]:                  # X then Y within the pair
                seen.setdefault(fid, set())
                kept.setdefault((m, fid), [])
                for desc in raw_lists.get((m, fid), []):
                    n = norm(desc)
                    drop = None
                    if not n:
                        drop = "empty"
                    elif len(desc.split()) > WORD_BUDGET:
                        drop = f"over-budget (> {WORD_BUDGET} words)"
                    elif n in seen[fid]:
                        drop = "duplicate within figure"
                    elif n in seen.get(twin[fid], set()):
                        drop = "duplicate of a twin description"
                    census.append({"model": m, "fig": fid, "desc": desc,
                                   "mechanical_drop": drop})
                    if drop is None:
                        seen[fid].add(n)
                        kept[(m, fid)].append(desc)
    return figs, pairs, kept, census


def cert_array(mname, fig_index, cand_index, figs):
    """Fresh deterministic matcher array per certification call."""
    rng = random.Random(SEED0 ^ 0xCE7 ^ (MODEL_SEED_OFFSET[mname] * 1009)
                        ^ (fig_index * 101) ^ cand_index)
    ids = sorted(figs)
    rng.shuffle(ids)
    return [(f"P{i+1}", cid) for i, cid in enumerate(ids)]


def pending_calls(kept, prior):
    todo = []
    for m in MODELS:
        for fi, fid in enumerate(sorted({f for (mm, f) in kept if mm == m})):
            for ci, desc in enumerate(kept[(m, fid)]):
                if (m, fid, norm(desc)) not in prior:
                    todo.append((m, fid, fi, ci, desc))
    return todo


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
    figs, pairs, kept, census = gather_candidates()
    prior = {(r["model"], r["fig"], norm(r["desc"])) for r in read_jsonl(CERT_PATH)}
    todo = pending_calls(kept, prior)
    if mode == "plan":
        n_mech = sum(1 for c in census if c["mechanical_drop"])
        print(f"PLAN: {len(census)} parsed candidates, {n_mech} mechanically dropped, "
              f"{len(todo)} certification calls pending (1 per surviving uncertified "
              f"candidate), est. ${len(todo) * EST_PER_CALL:.3f} "
              f"(design table: <=144 ~ $0.17). No API call made by `plan`.")
        return
    if mode != "run":
        print("usage: certify.py [plan|run]")
        return

    if todo:
        check_hard_stop(len(todo) * EST_PER_CALL, "certification")
        new = []
        for m, fid, fi, ci, desc in todo:
            p_order = cert_array(m, fi, ci, figs)
            p_block = grid_block(p_order, figs)
            labels = {l for l, _ in p_order}
            label_list = ", ".join(l for l, _ in p_order)
            user = (f"Your figures:\n{p_block}\n\n"
                    f"Your partner describes ONE target figure as:\n\"{desc}\"\n\n"
                    f"Which of your figures is it? Reply with exactly one label "
                    f"({label_list}) and nothing else.")
            r, pick, pmode, retried, usages = call_forced(
                MODELS[m], CERT_SYS.format(example=p_order[0][0]), user, labels, label_list)
            pick_cid = next((c for l, c in p_order if l == pick), None)
            rec = {"model": m, "fig": fid, "desc": desc, "pick": pick,
                   "pick_cid": pick_cid, "certified": pick_cid == fid,
                   "parse_mode": pmode, "retried": retried, "raw": r.get("content"),
                   "p_order": p_order, "usage": usages, "err": r.get("error")}
            append_jsonl(CERT_PATH, rec)
            new.append(rec)
            print(f"  {m:7s} {fid} cand{ci}: {'CERT' if rec['certified'] else 'fail'} "
                  f"({pmode}) \"{desc[:48]}\"")
        tot, have, miss = flat_cost(new)
        ledger_append("certification", len(new), tot, miss,
                      "stimulus-construction data; never analyzed as findings")
    else:
        print("no pending certification calls (idempotent re-run).")

    # ---- (re)build the report: frozen roster + census --------------------------------
    cert_by = {(r["model"], r["fig"], norm(r["desc"])): r for r in read_jsonl(CERT_PATH)}
    topup_used = {(r["model"], r["fig"]) for r in read_jsonl(HARVEST_PATH)
                  if r["phase"] == "topup"}
    models_out = {}
    for m in MODELS:
        fig_out = {}
        for fid in sorted(figs):
            certified = []
            for desc in kept.get((m, fid), []):
                cr = cert_by.get((m, fid, norm(desc)))
                if cr and cr["certified"]:
                    certified.append(desc)
            roster = certified[:DESCS_PER_FIG]   # first 6 certified, harvest order
            fig_out[fid] = {"candidates_kept": len(kept.get((m, fid), [])),
                            "certified_n": len(certified),
                            "roster": roster,
                            "shortfall": len(certified) < DESCS_PER_FIG,
                            "topup_used": (m, fid) in topup_used}
        pair_out, n_clusters = {}, 0
        for pid, (a, b) in sorted(pairs.items()):
            ns = min(N_SAMPLES, len(fig_out[a]["roster"]) // 2,
                     len(fig_out[b]["roster"]) // 2)
            pair_out[str(pid)] = {"X": a, "Y": b, "n_samples": ns}
            n_clusters += ns
        models_out[m] = {"figures": fig_out, "pairs": pair_out, "n_clusters": n_clusters}

    full_census = []
    for c in census:
        cr = cert_by.get((c["model"], c["fig"], norm(c["desc"])))
        full_census.append({**c,
                            "certified": (cr["certified"] if cr else None),
                            "cert_pick": (cr["pick_cid"] if cr else None),
                            "cert_parse_mode": (cr["parse_mode"] if cr else None),
                            "cert_retried": (cr["retried"] if cr else None)})
    report = {"schema": "relational-history-perturbation-v3 certification report",
              "anti_null_bias_disclosure": ANTI_NULL_BIAS_DISCLOSURE,
              "criteria": {"mechanical": ["non-empty", f"<= {WORD_BUDGET} words",
                                          "dedup within figure",
                                          "dedup against twin set"],
                           "model_based": "fresh same-model matcher, single description "
                                          "line, no nonce, no history; certified iff the "
                                          "parsed pick is the described figure",
                           "roster_rule": f"first {DESCS_PER_FIG} certified per figure, "
                                          "deterministic harvest order"},
              "models": models_out, "census": full_census}
    json.dump(report, open(REPORT_PATH, "w"), indent=2)
    print(f"\ncertification_report.json written.")
    for m in MODELS:
        md = models_out[m]
        per_fig = {fid: f"{d['certified_n']}/6" for fid, d in md["figures"].items()}
        shorts = [fid for fid, d in md["figures"].items() if d["shortfall"]]
        print(f"  {m:7s}: clusters={md['n_clusters']}/9  certified {per_fig}"
              + (f"  SHORTFALL {shorts} -> run harvest.py topup" if shorts else ""))
    short_any = any(d["shortfall"] and not d["topup_used"]
                    for md in models_out.values() for d in md["figures"].values())
    if short_any:
        print("NEXT: harvest.py topup, then certify.py run again (one top-up max per "
              "figure; persisting shortfall drops the sample count — record it in PREREG "
              "before the freeze).")


if __name__ == "__main__":
    main()
