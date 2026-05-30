"""Build + freeze the embedded-CC (operator-scope) comparative-correlative v3 item set
(2026-05-30).

Pre-registration (charter s8): EMITS experiments/data/comparative-correlative-v3/items.csv,
run + committed BEFORE any probe call. Operationalizes the embedded-CC arm that the v2
design DEFERRED, under the RATIFIED difficulty gate
(decisions/resolved/cc-v2-difficulty-operationalization, 2026-05-29: "...defer embedded-CC
to v3..."). No new decision. Behavioral NLI + forced-choice, temperature 0, no logprobs ->
existing 3-family panel. Reuses the v1/v2 instrument verbatim (NLI hypothesis is ALWAYS the
POSITIVE covariation "As <dim1> increases, <dim2> increases."; FC asks INCREASE / DECREASE /
UNDETERMINED for dim2 as dim1 increases).

WHY v3 (the embedding / operator-scope wedge)
---------------------------------------------
v1 + v2 found the CC covariation reading robust AT/ABOVE ceiling, incl. multi-step
composition. Both probed the CC as an ASSERTED relation. v3 asks the sharper "meaning vs
template" question: when the very same `the more X, the more Y` is placed UNDER an operator
that cancels or suspends its assertion -- sentential NEGATION ("it is not the case that...")
or EPISTEMIC hedging ("it remains unproven whether...") -- does the model track the operator
scope (withhold the bare covariation direction), or does it fire a surface
"the-more...the-more -> INCREASE" template regardless? A template-firer affirms the positive
direction everywhere; a model deploying the covariation MEANING + operator scope withholds it
under negation/modality.

ARMS (graded ladder; difficulty + golds frozen here BEFORE the run)
------------------------------------------------------------------
  baseline-pos   (d1): plain POSITIVE CC, asserted. correct = INCREASE / entail. [ceiling anchor]
  baseline-inv   (d1): plain INVERSE CC, asserted. correct = DECREASE / contradiction.
                       [DIRECTION anchor -- guards against an INCREASE-bias readout, the gap
                        v2's set lacked (v2 NIT: no undetermined/decrease-discriminating arm)]
  negation       (d2): negated POSITIVE CC ("It is not the case that the more X, the more Y").
                       THE key manipulation. The asserted positive covariation is DENIED.
                       FC correct = UNDETERMINED (denial of "increase" does not assert a
                       direction); NLI correct = CONTRADICTION (2) -- the premise denies
                       exactly the positive hypothesis.
  modal-epistemic(d2): epistemically-HEDGED positive CC ("It remains unproven whether the
                       more X, the more Y"). The relation is presented as merely possible /
                       unconfirmed, NOT asserted. FC correct = UNDETERMINED; NLI correct =
                       NEUTRAL (1) -- "X debates whether P" does not entail P.
  negation-inv   (d3): negated INVERSE CC ("It is not the case that the more X, the LESS Y").
                       CONTROL against a shallow "see 'not' -> UNDETERMINED" heuristic:
                       negating a DECREASE does NOT entail an increase. FC correct =
                       UNDETERMINED; NLI correct = NEUTRAL (1) (positive hypothesis neither
                       entailed nor contradicted). Combined with `negation` (NLI gold = 2,
                       not 1) this discriminates operator-scope tracking from a flat
                       not->undetermined rule.

INDICATOR / READING RULE (RATIFIED report-the-rate; no manufactured pass bar)
  Per arm x model x instrument: operator-correct rate (pred == the per-arm, per-instrument
  gold below). Headline (report-the-rate):
    - the EMBEDDING-CANCELLATION rate = fraction of embedded items (negation + modal +
      negation-inv) where the model does NOT answer the bare positive direction
      (FC != INCREASE / NLI != 0) -- the off-template signal;
    - the per-arm operator-correct rate;
    - the degradation SHAPE across d1<d2<d3.
  FC is the PRIMARY instrument for the embedded arms (FC gold = UNDETERMINED is uniform and
  least gold-contestable). NLI is secondary (its per-arm gold 2/1/1 encodes the finer
  entailment status; the negation NLI gold = contradiction is defensible but pragmatically
  debatable -- see the run README NIT). No threshold tuned post-run.

HUMAN ANCHOR: pending / internal-contrast-only (Option-4 logic, same as v2). The Scivetti CC
subset has NO negated / hedged CC items -> no in-repo human norm on the embedded arms -> NO
human-level claim on them. The baseline arms keep the v1/v2 phenomenon-level Scivetti CC
anchor. No human label invented. (Tracked by decisions/open/conflicting-cue-human-anchor.)

Run: python3 build_items.py   (no API; writes the frozen CSV)
"""
import csv
import hashlib
import os

# Each row: (item_id, arm, difficulty, sentence, dim1, dim2, nli_gold, fc_gold)
#   nli_gold in {"0" entail, "1" neutral, "2" contradiction}  (for the POSITIVE hypothesis
#     "As <dim1> increases, <dim2> increases.")
#   fc_gold  in {"INCREASE","DECREASE","UNDETERMINED"}
# The two golds are set INDEPENDENTLY per row (the embedded arms decouple them): see arm doc.
ROWS_RAW = [
    # ---- baseline-pos (d1): plain positive CC, asserted -> entail / INCREASE ----
    ("bpos-meeting", "baseline-pos", "1",
     "The longer the meeting dragged on, the more restless the staff became.",
     "the meeting's length", "the staff's restlessness", "0", "INCREASE"),
    ("bpos-tower", "baseline-pos", "1",
     "The taller the tower grew, the more tourists it attracted.",
     "the tower's height", "the number of tourists", "0", "INCREASE"),
    ("bpos-room", "baseline-pos", "1",
     "The darker the room got, the harder it became to read.",
     "the room's darkness", "the difficulty of reading", "0", "INCREASE"),

    # ---- baseline-inv (d1): plain inverse CC, asserted -> contradiction / DECREASE ----
    ("binv-shelf", "baseline-inv", "1",
     "The higher the shelf, the fewer people could reach it.",
     "the shelf's height", "the number of people who could reach it", "2", "DECREASE"),
    ("binv-water", "baseline-inv", "1",
     "The colder the water became, the less the children wanted to swim.",
     "the water's coldness", "the children's desire to swim", "2", "DECREASE"),
    ("binv-fog", "baseline-inv", "1",
     "The thicker the fog grew, the slower the traffic moved.",
     "the fog's thickness", "the traffic's speed", "2", "DECREASE"),

    # ---- negation (d2): negated POSITIVE CC -> the positive relation is DENIED.
    #      FC = UNDETERMINED ; NLI = contradiction (premise denies the positive hypothesis) ----
    ("neg-team", "negation", "2",
     "It is not true that the more the team trained, the better they performed.",
     "the amount the team trained", "the team's performance", "2", "UNDETERMINED"),
    ("neg-book", "negation", "2",
     "It is not the case that the longer the book, the more readers enjoyed it.",
     "the book's length", "readers' enjoyment", "2", "UNDETERMINED"),
    ("neg-ads", "negation", "2",
     "It is simply false that the more the product was advertised, the more it sold.",
     "the amount of advertising", "the product's sales", "2", "UNDETERMINED"),
    ("neg-push", "negation", "2",
     "Contrary to the coach's claim, it was not true that the harder the players pushed, the more games they won.",
     "how hard the players pushed", "the number of games they won", "2", "UNDETERMINED"),

    # ---- modal-epistemic (d2): hedged positive CC -> relation merely possible, NOT asserted.
    #      FC = UNDETERMINED ; NLI = neutral (does not entail the positive) ----
    ("mod-exercise", "modal-epistemic", "2",
     "It remains unproven whether the more people exercise, the longer they live.",
     "the amount people exercise", "their lifespan", "1", "UNDETERMINED"),
    ("mod-reading", "modal-epistemic", "2",
     "Researchers still debate whether the more a child reads, the larger their vocabulary grows.",
     "the amount a child reads", "the child's vocabulary size", "1", "UNDETERMINED"),
    ("mod-dose", "modal-epistemic", "2",
     "No one has confirmed whether the higher the dose, the faster the recovery.",
     "the dose", "the recovery speed", "1", "UNDETERMINED"),

    # ---- negation-inv (d3): negated INVERSE CC -> negating a DECREASE does NOT entail an
    #      increase. CONTROL vs a flat "see 'not' -> UNDETERMINED" rule.
    #      FC = UNDETERMINED ; NLI = neutral (positive hypothesis neither entailed nor denied) ----
    ("negi-practice", "negation-inv", "3",
     "It is not the case that the more she practiced, the worse she played.",
     "the amount she practiced", "how well she played", "1", "UNDETERMINED"),
    ("negi-spend", "negation-inv", "3",
     "It isn't true that the more the company spent, the less it earned.",
     "the company's spending", "the company's earnings", "1", "UNDETERMINED"),
    ("negi-alarm", "negation-inv", "3",
     "It was never the case that the louder the alarm, the fewer people ignored it.",
     "the alarm's loudness", "the number of people who ignored it", "1", "UNDETERMINED"),
]

# Cross-check: the NLI hypothesis is ALWAYS the positive covariation, so a positive-asserted
# CC -> 0, an inverse-asserted CC -> 2; embedded arms decouple (negation of positive -> 2;
# modal/negated-inverse -> 1). FC gold for every embedded arm is UNDETERMINED. Assert the
# shape so a typo cannot silently ship a wrong gold.
ARM_FC = {"baseline-pos": "INCREASE", "baseline-inv": "DECREASE",
          "negation": "UNDETERMINED", "modal-epistemic": "UNDETERMINED",
          "negation-inv": "UNDETERMINED"}
ARM_NLI = {"baseline-pos": "0", "baseline-inv": "2",
           "negation": "2", "modal-epistemic": "1", "negation-inv": "1"}


def rows():
    out = []
    for (iid, arm, diff, sent, dim1, dim2, nli_gold, fc_gold) in ROWS_RAW:
        assert fc_gold == ARM_FC[arm], f"{iid}: fc_gold {fc_gold} != arm default {ARM_FC[arm]}"
        assert nli_gold == ARM_NLI[arm], f"{iid}: nli_gold {nli_gold} != arm default {ARM_NLI[arm]}"
        hyp = f"As {dim1} increases, {dim2} increases."
        out.append(dict(item_id=iid, arm=arm, difficulty=diff, sentence=sent,
                        dim1=dim1, dim2=dim2, nli_hypothesis=hyp,
                        nli_gold=nli_gold, fc_gold=fc_gold))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                       "comparative-correlative-v3", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "arm", "difficulty", "sentence", "dim1", "dim2",
            "nli_hypothesis", "nli_gold", "fc_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    from collections import Counter
    by = Counter(r["arm"] for r in rs)
    print(f"wrote {len(rs)} items -> {out}")
    print(f"  arms: {dict(by)}")
    print(f"  (per-arm nli_gold/fc_gold cross-checked against ARM_NLI/ARM_FC)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
