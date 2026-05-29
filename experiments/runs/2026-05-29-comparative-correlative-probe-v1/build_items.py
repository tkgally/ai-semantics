"""Build and freeze the comparative-correlative item set (probe v1, 2026-05-29).

Pre-registration: this script EMITS experiments/data/comparative-correlative/items.csv
and must be run and the CSV committed BEFORE any probe call (charter §8). The
scale pairs are hand-authored so covariation direction is NOT world-knowledge-obvious
(conjecture caveat): the construction, not plausibility, must supply the direction.

For each scale pair we emit four item forms that reuse the same scalar lexical material:
  cc-positive  : "the MORE x ..., the MORE y ..."   -> covariation direction = increase
  cc-inverse   : "the MORE x ..., the LESS y ..."   -> covariation direction = decrease
  ctrl-two     : two independent declarative clauses (both scales asserted, no dependency)
  ctrl-single  : a single comparative clause (only one scale mentioned)

Construction-correct answers, fixed here before the run:
  forced-choice (does dim2 increase / decrease / undetermined as dim1 increases):
    cc-positive -> increase ; cc-inverse -> decrease ; both controls -> undetermined
  NLI (premise = sentence, hypothesis = "As <dim1> increases, <dim2> increases."):
    cc-positive -> 0 entailment ; cc-inverse -> 2 contradiction ; both controls -> 1 neutral
"""
import csv, os

# pid, typicality, dim1 (short noun phrase), dim2 (short noun phrase),
# cc_pos, cc_inv, ctrl_two, ctrl_single
PAIRS = [
    # ---- typical: plausible-either-direction pairs (direction not obvious) ----
    ("lecture", "typical", "the lecture's length", "the students' engagement",
     "The longer the lecture ran, the more engaged the students became.",
     "The longer the lecture ran, the less engaged the students became.",
     "The lecture ran long. The students were highly engaged.",
     "The lecture ran longer than usual."),
    ("ticket", "typical", "the ticket price", "the size of the crowd",
     "The higher the ticket price, the larger the crowd grew.",
     "The higher the ticket price, the smaller the crowd grew.",
     "The ticket price was high. The crowd was large.",
     "The ticket price was higher than last year."),
    ("cafe", "typical", "the morning's cold", "the cafe's busyness",
     "The colder the morning, the busier the cafe got.",
     "The colder the morning, the quieter the cafe got.",
     "The morning was cold. The cafe was busy.",
     "The morning was colder than forecast."),
    ("building", "typical", "the building's age", "the rent",
     "The older the building, the higher the rent climbed.",
     "The older the building, the lower the rent climbed.",
     "The building was old. The rent was high.",
     "The building was older than the others."),
    ("lighting", "typical", "the brightness of the lighting", "the patients' tension",
     "The brighter the lighting, the tenser the patients felt.",
     "The brighter the lighting, the calmer the patients felt.",
     "The lighting was bright. The patients were tense.",
     "The lighting was brighter than before."),
    ("music", "typical", "the loudness of the music", "the diners' eating speed",
     "The louder the music, the faster the diners ate.",
     "The louder the music, the slower the diners ate.",
     "The music was loud. The diners ate fast.",
     "The music was louder than usual."),
    ("trail", "typical", "the steepness of the trail", "the number of hikers attempting it",
     "The steeper the trail, the more hikers attempted it.",
     "The steeper the trail, the fewer hikers attempted it.",
     "The trail was steep. Many hikers attempted it.",
     "The trail was steeper than the map suggested."),
    ("queue", "typical", "the length of the queue", "the customers' anger",
     "The longer the queue, the angrier the customers grew.",
     "The longer the queue, the calmer the customers grew.",
     "The queue was long. The customers were angry.",
     "The queue was longer than yesterday."),
    ("class", "typical", "the size of the class", "the test scores",
     "The larger the class, the higher the test scores rose.",
     "The larger the class, the lower the test scores rose.",
     "The class was large. The test scores were high.",
     "The class was larger than the year before."),
    ("dish", "typical", "the spiciness of the dish", "the size of the tip",
     "The spicier the dish, the bigger the tip became.",
     "The spicier the dish, the smaller the tip became.",
     "The dish was spicy. The tip was big.",
     "The dish was spicier than expected."),
    ("phone", "typical", "the newness of the phone", "how long the battery lasted",
     "The newer the phone, the longer the battery lasted.",
     "The newer the phone, the shorter the battery lasted.",
     "The phone was new. The battery lasted long.",
     "The phone was newer than the last model."),
    ("roast", "typical", "the darkness of the roast", "the blend's popularity",
     "The darker the roast, the more popular the blend became.",
     "The darker the roast, the less popular the blend became.",
     "The roast was dark. The blend was popular.",
     "The roast was darker than the house blend."),
    ("river", "typical", "the river's depth", "the ferry's speed",
     "The deeper the river, the faster the ferry crossed.",
     "The deeper the river, the slower the ferry crossed.",
     "The river was deep. The ferry crossed fast.",
     "The river was deeper than in spring."),
    ("garden", "typical", "the garden's size", "the gardener's pay",
     "The bigger the garden, the higher the gardener's pay went.",
     "The bigger the garden, the lower the gardener's pay went.",
     "The garden was big. The gardener's pay was high.",
     "The garden was bigger than the neighbour's."),
    # ---- atypical: deliberately absurd pairings (covariation can ONLY come from the
    #      construction; world knowledge gives no direction) ----
    ("pebble", "atypical", "the roundness of the pebble", "the length of the meeting",
     "The rounder the pebble, the longer the meeting ran.",
     "The rounder the pebble, the shorter the meeting ran.",
     "The pebble was round. The meeting ran long.",
     "The pebble was rounder than the others."),
    ("wallpaper", "atypical", "the greenness of the wallpaper", "the loudness of the applause",
     "The greener the wallpaper, the louder the applause grew.",
     "The greener the wallpaper, the quieter the applause grew.",
     "The wallpaper was green. The applause was loud.",
     "The wallpaper was greener than the trim."),
    ("soup", "atypical", "the saltiness of the soup", "the stock price",
     "The saltier the soup, the higher the stock price climbed.",
     "The saltier the soup, the lower the stock price climbed.",
     "The soup was salty. The stock price was high.",
     "The soup was saltier than the broth."),
    ("doorway", "atypical", "the width of the doorway", "the speed of the verdict",
     "The wider the doorway, the faster the verdict came.",
     "The wider the doorway, the slower the verdict came.",
     "The doorway was wide. The verdict came fast.",
     "The doorway was wider than the frame."),
    ("curtains", "atypical", "the blueness of the curtains", "the weight of the homework",
     "The bluer the curtains, the heavier the homework felt.",
     "The bluer the curtains, the lighter the homework felt.",
     "The curtains were blue. The homework felt heavy.",
     "The curtains were bluer than the rug."),
    ("map", "atypical", "the age of the map", "the sweetness of the lemonade",
     "The older the map, the sweeter the lemonade tasted.",
     "The older the map, the sourer the lemonade tasted.",
     "The map was old. The lemonade tasted sweet.",
     "The map was older than the atlas."),
]

FORMS = [
    ("cc-positive",   "increase",     "0"),
    ("cc-inverse",    "decrease",     "2"),
    ("ctrl-two",      "undetermined", "1"),
    ("ctrl-single",   "undetermined", "1"),
]

def sentence_for(pair, form):
    _, _, _, _, cc_pos, cc_inv, ctrl_two, ctrl_single = pair
    return {"cc-positive": cc_pos, "cc-inverse": cc_inv,
            "ctrl-two": ctrl_two, "ctrl-single": ctrl_single}[form]

def main():
    out = os.path.join(os.path.dirname(__file__), "..", "..",
                       "data", "comparative-correlative", "items.csv")
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rows = []
    for pair in PAIRS:
        pid, typ, dim1, dim2 = pair[0], pair[1], pair[2], pair[3]
        for form, fc_gold, nli_gold in FORMS:
            sent = sentence_for(pair, form)
            rows.append({
                "item_id": f"{pid}-{form}",
                "scale_pair": pid,
                "typicality": typ,
                "form": form,
                "dim1": dim1,
                "dim2": dim2,
                "sentence": sent,
                "fc_gold": fc_gold,        # forced-choice construction-correct answer
                "nli_hypothesis": f"As {dim1} increases, {dim2} increases.",
                "nli_gold": nli_gold,      # NLI construction-correct label (0/1/2)
            })
    cols = ["item_id","scale_pair","typicality","form","dim1","dim2",
            "sentence","fc_gold","nli_hypothesis","nli_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    n_pairs = len(PAIRS)
    n_typ = sum(1 for p in PAIRS if p[1] == "typical")
    print(f"wrote {len(rows)} items ({n_pairs} pairs x {len(FORMS)} forms) -> {out}")
    print(f"  typical pairs: {n_typ}, atypical pairs: {n_pairs - n_typ}")

if __name__ == "__main__":
    main()
