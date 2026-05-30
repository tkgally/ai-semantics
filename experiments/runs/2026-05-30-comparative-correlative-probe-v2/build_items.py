"""Build + freeze the off-ceiling comparative-correlative v2 item set (2026-05-30).

Pre-registration (charter s8): EMITS experiments/data/comparative-correlative-v2/items.csv,
run + committed BEFORE any probe call. Operationalizes design/comparative-correlative-v2
under the RATIFIED difficulty gate (decisions/resolved/cc-v2-difficulty-operationalization,
2026-05-29: UNIFY + adopt default -> conflicting-cue primary + multi-step + near-miss
controls + graded ladder; defer embedded-CC to v3; report-the-rate). No new decision.
Behavioral NLI + forced-choice, temperature 0, no logprobs -> existing 3-family panel.
Reuses the v1 instrument verbatim (NLI hypothesis "As <dim1> increases, <dim2> increases.";
FC asks INCREASE/DECREASE/UNDETERMINED for dim2 as dim1 increases).

WHY v2 (escape the v1 ceiling)
------------------------------
v1 (result/comparative-correlative-covariation-v1) was a CEILING positive: the panel
asserted the covariation direction for ~100% of clear CCs, flipped on inverse CCs, and
matched the Scivetti human baseline. Its lead caveat: ceiling on an easy instrument cannot
tell "robust constructional competence" from "the task was too easy." v2 raises difficulty
along axes a form-only / plausibility-leaning reader should fail while a model genuinely
deploying the covariation MEANING should survive.

ARMS (graded difficulty ladder; difficulty frozen here BEFORE the run)
---------------------------------------------------------------------
  baseline       (d1): clear CC, direction-NOT-world-obvious pair (the v1 anchor / ladder
                       bottom). cc-positive -> increase ; cc-inverse -> decrease.
  conflicting-cue(d2): THE KEY MANIPULATION. A pair whose real-world covariation is
                       UNAMBIGUOUS, stated by the construction in the OPPOSITE direction.
                       Construction-correct answer = the STATED direction; a plausibility-
                       leaning model follows world knowledge instead. (e.g. "The harder it
                       rained, the LESS the reservoir filled" -> construction says DECREASE;
                       world knowledge says increase.) This is the sharpest discriminator
                       and the one v1 omitted.
  paraphrase     (d2): near-miss FORM control. The SAME covariation in a non-paired-`the`
                       form ("As X got -er, Y got -er") -> tests whether the covariation
                       reading is tied to the exact `the X-er, the Y-er` template or
                       generalizes to the covariation meaning. Gold = the stated direction.
  multi-step     (d3): TWO chained CCs; the hypothesis probes the CHAIN ENDPOINTS (dim1 ->
                       dim2 through a mediator), so the model must COMPOSE two covariation
                       signs. Gold = product of the two step signs (computed + checked below).

INDICATOR / READING RULE (RATIFIED report-the-rate; no manufactured pass bar)
  Per arm x model x instrument: construction-correct rate (FC = stated/composed direction;
  NLI = 0/1/2 matching). Headline = the conflicting-cue follow-construction rate + the
  multi-step composition rate + the degradation SHAPE across d1<d2<d3 (graceful monotone vs
  brittle cliff). A cue-following / composition-collapse pattern is the informative
  partial-null that qualifies v1's ceiling as task-easiness. No threshold tuned post-run.

HUMAN ANCHOR: pending / internal-contrast-only (Option-4 logic). The Scivetti CC subset has
NO conflicting-cue / multi-step items; those arms have no in-repo human norm -> NO human-level
claim on them (design s4). The baseline arm keeps the v1 phenomenon-level Scivetti CC anchor.
No human label invented.

Run: python3 build_items.py   (no API; writes the frozen CSV)
"""
import csv, hashlib, os

# Each row: (item_id, arm, difficulty, sentence, dim1, dim2, direction_gold)
# direction_gold in {increase, decrease, undetermined}; the CONSTRUCTION/composition-correct
# answer (NOT world knowledge). NLI hypothesis is always "As <dim1> increases, <dim2>
# increases." so nli_gold = {increase:0 entail, decrease:2 contradiction, undetermined:1}.

ROWS_RAW = [
    # ---- baseline (d1): clear CC, direction not world-obvious (ladder bottom / anchor) ----
    ("base-lecture-pos","baseline","1",
     "The longer the lecture ran, the more engaged the students became.",
     "the lecture's length","the students' engagement","increase"),
    ("base-ticket-inv","baseline","1",
     "The higher the ticket price, the smaller the crowd grew.",
     "the ticket price","the crowd size","decrease"),
    ("base-building-pos","baseline","1",
     "The older the building, the higher the rent climbed.",
     "the building's age","the rent","increase"),
    ("base-music-inv","baseline","1",
     "The louder the music, the slower the diners ate.",
     "the music's loudness","the diners' eating speed","decrease"),

    # ---- conflicting-cue (d2): real-world direction UNAMBIGUOUS, construction states OPPOSITE
    # construction-correct = STATED direction; world-knowledge-following = the opposite ----
    ("conf-reservoir","conflicting-cue","2",   # world: more rain -> fuller; stated: less
     "The harder it rained, the less the reservoir filled.",
     "the rainfall","the reservoir's water level","decrease"),
    ("conf-altitude","conflicting-cue","2",    # world: higher -> less oxygen; stated: more
     "The higher the climbers ascended, the more oxygen filled the air around them.",
     "the climbers' altitude","the amount of oxygen in the air","increase"),
    ("conf-training","conflicting-cue","2",    # world: more training -> stronger; stated: weaker
     "The more she trained, the weaker her muscles grew.",
     "the amount she trained","her muscle strength","decrease"),
    ("conf-sunlight","conflicting-cue","2",    # world: more sun -> more growth; stated: less
     "The more sunlight the plants received, the less they grew.",
     "the sunlight the plants received","the plants' growth","decrease"),
    ("conf-speed","conflicting-cue","2",       # world: faster -> shorter trip; stated: longer
     "The faster the car drove, the longer the trip took.",
     "the car's speed","the trip's duration","increase"),
    ("conf-debt","conflicting-cue","2",        # world: borrow more -> more debt; stated: less
     "The more money he borrowed, the smaller his debt became.",
     "the money he borrowed","his debt","decrease"),

    # ---- paraphrase (d2): same covariation, non-paired-`the` FORM (form-generalization) ----
    ("para-lecture-pos","paraphrase","2",
     "As the lecture ran longer, the students became more engaged.",
     "the lecture's length","the students' engagement","increase"),
    ("para-building-inv","paraphrase","2",
     "As the building got older, its rent fell ever lower.",
     "the building's age","the rent","decrease"),
    ("para-trail-pos","paraphrase","2",
     "As the trail grew steeper, more hikers attempted it.",
     "the trail's steepness","the number of hikers attempting it","increase"),
    ("para-cafe-inv","paraphrase","2",
     "As the morning got colder, the cafe grew quieter.",
     "the morning's coldness","the cafe's busyness","decrease"),

    # ---- multi-step (d3): TWO chained CCs; hypothesis probes dim1 -> dim2 (chain endpoints).
    # gold = product of the two step signs. Composition shown per item. ----
    ("multi-flood","multi-step","3",   # rain(+)->river ; river(+)->flooding  => (+)(+)=+
     "The more it rained, the higher the river rose. And the higher the river rose, the more the fields flooded.",
     "the rainfall","the flooding of the fields","increase"),
    ("multi-fish","multi-step","3",    # output(+)->pollution ; pollution(-)->fish  => (+)(-)=-
     "The more the factory produced, the more it polluted the bay. And the more it polluted the bay, the fewer fish survived.",
     "the factory's output","the number of surviving fish","decrease"),
    ("multi-bears","multi-step","3",   # cold(-)->foraging ; foraging(-)->fat  => (-)(-)=+
     "The colder the winter grew, the less the bears foraged. And the less the bears foraged, the thinner they became.",
     "the winter's coldness","the bears' thinness","increase"),
    ("multi-economy","multi-step","3", # rate(-)->borrowing ; borrowing(+)->growth  => (-)(+)=-
     "The higher the interest rate climbed, the less people borrowed. And the less people borrowed, the slower the economy grew.",
     "the interest rate","the economy's growth rate","decrease"),
    ("multi-team","multi-step","3",    # practice(+)->skill ; skill(+)->wins  => (+)(+)=+
     "The more the team practiced, the sharper their play became. And the sharper their play became, the more games they won.",
     "the team's practice","the number of games they won","increase"),
]

# Composition cross-check (asserts the gold for the multi-step arm matches the sign product).
COMP_CHECK = {
    "multi-flood": (+1, +1),
    "multi-fish": (+1, -1),
    "multi-bears": (-1, -1),
    "multi-economy": (-1, +1),
    "multi-team": (+1, +1),
}
SIGN_TO_DIR = {+1: "increase", -1: "decrease"}

NLI_GOLD = {"increase": "0", "decrease": "2", "undetermined": "1"}
FC_GOLD = {"increase": "INCREASE", "decrease": "DECREASE", "undetermined": "UNDETERMINED"}


def rows():
    out = []
    for (iid, arm, diff, sent, dim1, dim2, dgold) in ROWS_RAW:
        if arm == "multi-step":
            s1, s2 = COMP_CHECK[iid]
            expected = SIGN_TO_DIR[s1 * s2]
            assert expected == dgold, f"{iid}: composition {s1}*{s2} -> {expected} != gold {dgold}"
        hyp = f"As {dim1} increases, {dim2} increases."
        out.append(dict(item_id=iid, arm=arm, difficulty=diff, sentence=sent,
                        dim1=dim1, dim2=dim2, direction_gold=dgold,
                        nli_hypothesis=hyp, nli_gold=NLI_GOLD[dgold], fc_gold=FC_GOLD[dgold]))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                       "comparative-correlative-v2", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "arm", "difficulty", "sentence", "dim1", "dim2", "direction_gold",
            "nli_hypothesis", "nli_gold", "fc_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    from collections import Counter
    by = Counter(r["arm"] for r in rs)
    print(f"wrote {len(rs)} items -> {out}")
    print(f"  arms: {dict(by)}")
    print(f"  (multi-step composition gold cross-checked against sign products)")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
