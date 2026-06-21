#!/usr/bin/env python3
"""build.py -- assemble the SECOND-INSTRUMENT stimulus file from the FROZEN modal arms.

This run does NOT re-build or re-match stimuli. It REUSES the frozen, certified modal
items from the session-71 modal-arm-widening run verbatim (same sentences, same matched
content controls) and only attaches a DIFFERENT indicator: a forced-choice modal-force
paraphrase preference. So the frequency/length matching is inherited (already certified
there, file sha cccac581.../canonical fb605ed9...); this script's job is to (1) pull the
will/shall/must matched items, (2) attach the per-arm forced-choice options, and (3) assign
a counterbalanced hedge-option position (A or B), balanced ~50/50 within each arm so a
fixed-letter (position-bias) reader cancels in the within-item base->fn shift.

Indicator rationale: the NLI run left will->would near-null. Is that the *instrument*
(3-way NLI) being insensitive to the future->conditional shift, or the *relation* being
genuinely inferentially inert? This second instrument keeps the SAME single-token output
channel (one letter, no working surface -- controls the output-channel confound the project
already mapped) but changes the QUESTION TYPE from entailment to a graded modal-force
preference. must->might is the instrument-validity anchor (NLI flipped it at ceiling -- a
sensitive instrument must register it too); shall->should is the panel-split check; the
content-swap (premise_ct, modal UNCHANGED) is the falsify control (predicted shift ~0).
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "2026-06-21-modal-arm-widening", "stimuli.json")
OUT = os.path.join(HERE, "stimuli.json")

# Source freeze chain (recorded for audit): the modal-arm-widening certified stimuli.
SRC_FILE_SHA = "cccac581b39b14c3"      # leading 16 of sha256(file)
SRC_CANON_SHA = "fb605ed9863bcd87"     # leading 16 of canonical sha in that file

# Per-arm forced-choice options. STRONG = the base modal's force; HEDGE = the swapped
# modal's force. CRITICAL: option text contains NO modal lemma from the stimuli (no
# will/would/shall/should/must/might), so a modal-blind reader has no surface cue and the
# propositional content is identical base-vs-fn -> a non-reader yields shift 0.
ARM_OPTIONS = {
    "will": {  # future (categorical) -> conditional (irrealis)
        "strong": "The event is presented as something that definitely happens or is the case.",
        "hedge":  "The event is presented as conditional or hypothetical -- happening only if certain circumstances hold.",
    },
    "shall": {  # deontic obligation -> advisory
        "strong": "The action is presented as strictly required or mandatory.",
        "hedge":  "The action is presented as advisable or recommended, but not strictly required.",
    },
    "must": {  # necessity -> possibility (deontic->epistemic flavor cross; loud strength drop)
        "strong": "The action is presented as required or certain to occur.",
        "hedge":  "The action is presented as merely possible or optional -- not required and not certain.",
    },
}

MODAL_LEMMAS = ("will", "would", "shall", "should", "must", "might")


def main():
    src = json.load(open(SRC))
    items = [it for it in src["items"]
             if it["ftype"] in ARM_OPTIONS and it["arm"] == "matched"]
    out_items = []
    for ft in ("will", "shall", "must"):
        arm = sorted((it for it in items if it["ftype"] == ft), key=lambda x: x["id"])
        opt = ARM_OPTIONS[ft]
        # leak guard: no modal lemma appears in either option string
        blob = (opt["strong"] + " " + opt["hedge"]).lower()
        for lemma in MODAL_LEMMAS:
            assert f" {lemma} " not in f" {blob} ", f"modal lemma {lemma!r} leaked into {ft} options"
        # counterbalance hedge position: alternate A/B across the arm -> ~50/50, fixed per item
        for i, it in enumerate(arm):
            hedge_letter = "A" if i % 2 == 0 else "B"
            if hedge_letter == "A":
                optA, optB = opt["hedge"], opt["strong"]
            else:
                optA, optB = opt["strong"], opt["hedge"]
            out_items.append({
                "id": it["id"],
                "ftype": ft,
                "pos": it["pos"],
                "premise_base": it["premise_base"],   # base modal (strong)
                "premise_fn": it["premise_fn"],       # swapped modal (hedge)
                "premise_ct": it["premise_ct"],       # content swap, modal UNCHANGED (control)
                "optA": optA,
                "optB": optB,
                "hedge_letter": hedge_letter,
                # predicted: base -> strong-preferred; fn -> hedge-preferred (if instrument reads modal)
                "pred_base_pref": "strong",
                "pred_fn_pref": "hedge",
            })
    canon = json.dumps(out_items, sort_keys=True, separators=(",", ":")).encode()
    canon_sha = hashlib.sha256(canon).hexdigest()
    blob = {"items": out_items, "sha256": canon_sha,
            "source": {"run": "2026-06-21-modal-arm-widening",
                       "file_sha16": SRC_FILE_SHA, "canon_sha16": SRC_CANON_SHA}}
    json.dump(blob, open(OUT, "w"), indent=1, sort_keys=True)
    file_sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    from collections import Counter
    print(f"wrote {len(out_items)} items -> {OUT}")
    print("per-arm n:", dict(Counter(it["ftype"] for it in out_items)))
    print("hedge_letter balance per arm:")
    for ft in ("will", "shall", "must"):
        c = Counter(it["hedge_letter"] for it in out_items if it["ftype"] == ft)
        print(f"  {ft}: A(hedge-first)={c['A']} B(hedge-second)={c['B']}")
    print(f"canonical sha256: {canon_sha}")
    print(f"file sha256:      {file_sha}")


if __name__ == "__main__":
    main()
