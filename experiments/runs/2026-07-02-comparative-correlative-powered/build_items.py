"""Build and freeze the FRESH item set for the comparative-correlative POWERED re-run
(A2a; 2026-07-02). Powered N per PROTOCOL.md §4 (~100-150 items).

This re-uses the FROZEN v1 instrument (experiments/runs/2026-05-29-comparative-correlative-probe-v1)
verbatim — same four item forms, same forced-choice + NLI prompts, same parsing, same panel,
same thresholds — and changes ONLY the item set: 34 fresh scale pairs (24 typical + 10 atypical),
DISJOINT from v1's 20 pairs, to attach a magnitude+interval to the direction/ordering finding
promoted in claim/comparative-correlative-covariation (whose Bounds says the magnitude is
"owed to the A2a powered re-run").

Pre-registration: this script EMITS experiments/data/comparative-correlative-powered/items.csv
and must be run and the CSV committed BEFORE any probe call (charter §8). Scale pairs are
hand-authored so the covariation direction is NOT world-knowledge-obvious (typical) or is
deliberately absurd (atypical) — the construction, not plausibility, must supply the direction.

For each scale pair we emit four forms reusing the same scalar lexical material:
  cc-positive  : "The MORE x ..., the MORE y ..."   -> covariation direction = increase
  cc-inverse   : "The MORE x ..., the LESS y ..."   -> covariation direction = decrease
  ctrl-two     : two independent declarative clauses (both scales asserted, no dependency)
  ctrl-single  : a single comparative clause (only one scale mentioned)

Construction-correct answers (fixed here, before the run):
  forced-choice (as dim1 increases, does dim2 increase / decrease / undetermined):
    cc-positive -> increase ; cc-inverse -> decrease ; both controls -> undetermined
  NLI (premise = sentence, hypothesis = "As <dim1> increases, <dim2> increases."):
    cc-positive -> 0 entailment ; cc-inverse -> 2 contradiction ; both controls -> 1 neutral
"""
import csv, os

# pid, typicality, dim1 (short NP, phrased so "<dim1> increases" reads naturally),
# dim2 (short NP), cc_pos, cc_inv, ctrl_two, ctrl_single
PAIRS = [
    # ---- typical: plausible-either-direction pairs (direction not obvious) ----
    ("novel", "typical", "the novel's thickness", "the reader's patience",
     "The thicker the novel, the more patient the reader stayed.",
     "The thicker the novel, the less patient the reader stayed.",
     "The novel was thick. The reader was patient.",
     "The novel was thicker than the last one."),
    ("ovens", "typical", "the ovens' heat", "the number of customers",
     "The hotter the ovens ran, the more customers arrived.",
     "The hotter the ovens ran, the fewer customers arrived.",
     "The ovens ran hot. Many customers arrived.",
     "The ovens ran hotter than usual."),
    ("seminar", "typical", "the seminar's size", "the amount of discussion",
     "The larger the seminar, the more discussion it generated.",
     "The larger the seminar, the less discussion it generated.",
     "The seminar was large. The discussion was lively.",
     "The seminar was larger than the lecture."),
    ("summer", "typical", "the summer's dryness", "the sweetness of the apples",
     "The drier the summer, the sweeter the apples grew.",
     "The drier the summer, the more sour the apples grew.",
     "The summer was dry. The apples were sweet.",
     "The summer was drier than the year before."),
    ("highway", "typical", "the highway's width", "the drivers' speed",
     "The wider the highway, the faster the drivers went.",
     "The wider the highway, the slower the drivers went.",
     "The highway was wide. The drivers went fast.",
     "The highway was wider than the old road."),
    ("gallery", "typical", "the gallery's dimness", "the visitors' whispering",
     "The dimmer the gallery, the more the visitors whispered.",
     "The dimmer the gallery, the less the visitors whispered.",
     "The gallery was dim. The visitors whispered.",
     "The gallery was dimmer than the lobby."),
    ("startup", "typical", "the startup's size", "the investors' caution",
     "The bigger the startup, the more cautious the investors turned.",
     "The bigger the startup, the less cautious the investors turned.",
     "The startup was big. The investors were cautious.",
     "The startup was bigger than its rival."),
    ("harbor", "typical", "the harbor's busyness", "the price of fish",
     "The busier the harbor, the higher the price of fish climbed.",
     "The busier the harbor, the lower the price of fish climbed.",
     "The harbor was busy. The price of fish was high.",
     "The harbor was busier than in winter."),
    ("clinic", "typical", "the waiting room's warmth", "the patients' drowsiness",
     "The warmer the waiting room, the drowsier the patients felt.",
     "The warmer the waiting room, the more alert the patients felt.",
     "The waiting room was warm. The patients were drowsy.",
     "The waiting room was warmer than the hall."),
    ("vineyard", "typical", "the vineyard slope's steepness", "the pickers' wages",
     "The steeper the vineyard slope, the higher the pickers' wages rose.",
     "The steeper the vineyard slope, the lower the pickers' wages rose.",
     "The vineyard slope was steep. The pickers' wages were high.",
     "The vineyard slope was steeper than the orchard's."),
    ("pool", "typical", "the pool's coldness", "the swimmers' lap count",
     "The colder the pool, the more laps the swimmers did.",
     "The colder the pool, the fewer laps the swimmers did.",
     "The pool was cold. The swimmers did many laps.",
     "The pool was colder than the sea."),
    ("shelves", "typical", "the library shelves' height", "the librarians' walking pace",
     "The taller the shelves, the faster the librarians walked.",
     "The taller the shelves, the slower the librarians walked.",
     "The shelves were tall. The librarians walked fast.",
     "The shelves were taller than the reading desks."),
    ("band", "typical", "the band's loudness", "the size of the dancing crowd",
     "The louder the band, the larger the dancing crowd swelled.",
     "The louder the band, the smaller the dancing crowd swelled.",
     "The band was loud. The dancing crowd was large.",
     "The band was louder than the opening act."),
    ("field", "typical", "the field's flatness", "the farmers' yield",
     "The flatter the field, the greater the farmers' yield became.",
     "The flatter the field, the smaller the farmers' yield became.",
     "The field was flat. The farmers' yield was great.",
     "The field was flatter than the hillside."),
    ("brochure", "typical", "the brochure's glossiness", "the buyers' trust",
     "The glossier the brochure, the more the buyers trusted it.",
     "The glossier the brochure, the less the buyers trusted it.",
     "The brochure was glossy. The buyers trusted it.",
     "The brochure was glossier than the flyer."),
    ("theater", "typical", "the theater's darkness", "the audience's restlessness",
     "The darker the theater, the more restless the audience grew.",
     "The darker the theater, the calmer the audience grew.",
     "The theater was dark. The audience was restless.",
     "The theater was darker than the foyer."),
    ("curry", "typical", "the curry's spiciness", "the diners' talkativeness",
     "The spicier the curry, the more talkative the diners became.",
     "The spicier the curry, the quieter the diners became.",
     "The curry was spicy. The diners were talkative.",
     "The curry was spicier than the starter."),
    ("syllabus", "typical", "the syllabus's length", "the students' enthusiasm",
     "The longer the syllabus, the more enthusiastic the students seemed.",
     "The longer the syllabus, the less enthusiastic the students seemed.",
     "The syllabus was long. The students were enthusiastic.",
     "The syllabus was longer than last term's."),
    ("current", "typical", "the current's speed", "the anglers' frustration",
     "The faster the current, the more frustrated the anglers got.",
     "The faster the current, the less frustrated the anglers got.",
     "The current was fast. The anglers were frustrated.",
     "The current was faster than at dawn."),
    ("kitchen", "typical", "the kitchen's tidiness", "the cooks' chatter",
     "The tidier the kitchen, the more the cooks chattered.",
     "The tidier the kitchen, the less the cooks chattered.",
     "The kitchen was tidy. The cooks chattered.",
     "The kitchen was tidier than the pantry."),
    ("footpath", "typical", "the footpath's narrowness", "the hikers' spacing",
     "The narrower the footpath, the wider the hikers spaced themselves.",
     "The narrower the footpath, the closer the hikers spaced themselves.",
     "The footpath was narrow. The hikers spaced themselves widely.",
     "The footpath was narrower than the fire road."),
    ("auction", "typical", "the auction room's brightness", "the collectors' lingering",
     "The brighter the auction room, the longer the collectors lingered.",
     "The brighter the auction room, the less the collectors lingered.",
     "The auction room was bright. The collectors lingered.",
     "The auction room was brighter than the vault."),
    ("soil", "typical", "the soil's sandiness", "the gardener's watering",
     "The sandier the soil, the more the gardener watered.",
     "The sandier the soil, the less the gardener watered.",
     "The soil was sandy. The gardener watered often.",
     "The soil was sandier than the loam bed."),
    ("venue", "typical", "the venue's size", "the fans' rowdiness",
     "The larger the venue, the rowdier the fans got.",
     "The larger the venue, the tamer the fans got.",
     "The venue was large. The fans were rowdy.",
     "The venue was larger than the club."),
    # ---- atypical: deliberately absurd pairings (covariation can ONLY come from the
    #      construction; world knowledge gives no direction) ----
    ("teacup", "atypical", "the teacup's roundness", "the length of the traffic jam",
     "The rounder the teacup, the longer the traffic jam stretched.",
     "The rounder the teacup, the shorter the traffic jam stretched.",
     "The teacup was round. The traffic jam was long.",
     "The teacup was rounder than the mug."),
    ("carpet", "atypical", "the carpet's redness", "the speed of the elevator",
     "The redder the carpet, the faster the elevator rose.",
     "The redder the carpet, the slower the elevator rose.",
     "The carpet was red. The elevator rose fast.",
     "The carpet was redder than the drapes."),
    ("pancake", "atypical", "the pancake's fluffiness", "the height of the mountain",
     "The fluffier the pancake, the taller the mountain loomed.",
     "The fluffier the pancake, the shorter the mountain loomed.",
     "The pancake was fluffy. The mountain loomed tall.",
     "The pancake was fluffier than the waffle."),
    ("stapler", "atypical", "the stapler's heaviness", "the brightness of the sunset",
     "The heavier the stapler, the brighter the sunset burned.",
     "The heavier the stapler, the dimmer the sunset burned.",
     "The stapler was heavy. The sunset burned bright.",
     "The stapler was heavier than the tape dispenser."),
    ("sock", "atypical", "the sock's stripiness", "the loudness of the thunder",
     "The stripier the sock, the louder the thunder cracked.",
     "The stripier the sock, the quieter the thunder cracked.",
     "The sock was stripy. The thunder cracked loud.",
     "The sock was stripier than the glove."),
    ("lampshade", "atypical", "the lampshade's width", "the sourness of the yogurt",
     "The wider the lampshade, the sourer the yogurt tasted.",
     "The wider the lampshade, the sweeter the yogurt tasted.",
     "The lampshade was wide. The yogurt tasted sour.",
     "The lampshade was wider than the base."),
    ("keyboard", "atypical", "the keyboard's dustiness", "the size of the harvest",
     "The dustier the keyboard, the bigger the harvest came in.",
     "The dustier the keyboard, the smaller the harvest came in.",
     "The keyboard was dusty. The harvest came in big.",
     "The keyboard was dustier than the monitor."),
    ("balloon", "atypical", "the balloon's shininess", "the depth of the well",
     "The shinier the balloon, the deeper the well ran.",
     "The shinier the balloon, the shallower the well ran.",
     "The balloon was shiny. The well ran deep.",
     "The balloon was shinier than the ribbon."),
    ("envelope", "atypical", "the envelope's crumpledness", "the speed of the train",
     "The more crumpled the envelope, the faster the train ran.",
     "The more crumpled the envelope, the slower the train ran.",
     "The envelope was crumpled. The train ran fast.",
     "The envelope was more crumpled than the parcel."),
    ("pinecone", "atypical", "the pinecone's stickiness", "the price of the haircut",
     "The stickier the pinecone, the pricier the haircut became.",
     "The stickier the pinecone, the cheaper the haircut became.",
     "The pinecone was sticky. The haircut was pricey.",
     "The pinecone was stickier than the acorn."),
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
                       "data", "comparative-correlative-powered", "items.csv")
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # guard (ENFORCED): no scale_pair id may collide with v1's frozen pairs. These are v1's
    # actual ids (experiments/runs/2026-05-29-comparative-correlative-probe-v1/build_items.py);
    # our v1 "trail" pair was renamed "footpath" precisely so this assertion stays clean.
    v1_pairs = {"lecture", "ticket", "cafe", "building", "lighting", "music", "trail",
                "queue", "class", "dish", "phone", "roast", "river", "garden",
                "pebble", "wallpaper", "soup", "doorway", "curtains", "map"}
    collide = {p[0] for p in PAIRS} & v1_pairs
    assert not collide, f"scale_pair id collides with v1 frozen set: {sorted(collide)}"
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
                "fc_gold": fc_gold,
                "nli_hypothesis": f"As {dim1} increases, {dim2} increases.",
                "nli_gold": nli_gold,
            })
    cols = ["item_id", "scale_pair", "typicality", "form", "dim1", "dim2",
            "sentence", "fc_gold", "nli_hypothesis", "nli_gold"]
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
