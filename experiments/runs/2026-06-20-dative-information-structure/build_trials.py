#!/usr/bin/env python3
"""Build + certify + freeze the dative information-structure stimuli.

DESIGN (ratified decisions/resolved/dative-anchor-and-indicator, ADOPT MODIFIED).
The givenness manipulation lives in the *discourse context*, never in the NPs: the
SAME double-object (DOC) / prepositional-dative (PD) phrasing pair — identical words,
identical recipient/theme lengths, identical animacy — is rated under different prior
contexts that establish which referent is discourse-GIVEN. The primary measure is the
WITHIN-ITEM preference shift across contexts:

    shift(item) = pref(DOC | recipient-given) - pref(DOC | theme-given)

Human prediction: shift > 0 (given-before-new: a given recipient -> DOC; a given theme
-> PD). Because every surface feature of the test sentence is held identical across an
item's two contexts, ANY reader whose output depends only on the test sentence (its
lengths, its A/B order, an always-DOC/always-PD bias, a shorter-first / longer-first
end-weight rule) produces the SAME score in both contexts -> shift = 0 -> at chance on
the contrast. Only a reader that uses the prior context (tracks givenness) can move the
shift off zero. The certification below proves this for an enumerated shortcut-reader
family; condition (a) (within-pair length variance = 0) holds by construction.

Arms:
  - MAIN (>=30 items): recipient and theme of similar length; rated in recipient-given,
    theme-given, and both-new (neutral baseline) contexts.
  - CONTROL (>=12 items, condition (b)): a large recipient/theme length gap, so in the
    dissociating context information structure predicts the LONGER constituent first
    while end-weight (short-before-long) predicts the shorter first -> OPPOSITE absolute
    orderings. >=6 are long-recipient (recipient-given dissociates) and >=6 long-theme
    (theme-given dissociates).

Outputs: stimuli.json (frozen, sha-pinned in PREREG), and a printed certification report.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def wc(s: str) -> int:
    """Word count of an NP (the corpus's LengthOf* unit: whitespace tokens)."""
    return len(s.split())


# ---------------------------------------------------------------------------
# Items. Each: verb (past), subject NP, recipient NP, theme NP, and three prior
# contexts that establish givenness by PRIOR MENTION (no dative phrasing inside the
# context -> no answer leakage). Recipients are animate, themes inanimate (the canonical
# configuration); the test sentence NPs are IDENTICAL across the three contexts.
# rec_given : prior sentence mentions the recipient referent (recipient = discourse-given)
# thm_given : prior sentence mentions the theme referent   (theme     = discourse-given)
# neutral   : a scene-setter mentioning neither referent    (both new) -> baseline
# ---------------------------------------------------------------------------

MAIN = [
    dict(id="m01", verb="offered", subj="The board", rec="the new manager", thm="a larger office",
         rec_given="The new manager had just arrived from the Tokyo branch.",
         thm_given="A larger office had recently opened up on the top floor.",
         neutral="The quarterly review ran long that afternoon."),
    dict(id="m02", verb="handed", subj="The clerk", rec="the tired traveler", thm="a paper map",
         rec_given="The tired traveler had been waiting at the counter for an hour.",
         thm_given="A paper map of the old town sat in a rack by the door.",
         neutral="The station was unusually quiet for a Monday."),
    dict(id="m03", verb="sent", subj="The agency", rec="the local artist", thm="a small grant",
         rec_given="The local artist had applied to the program back in spring.",
         thm_given="A small grant had been set aside for community projects.",
         neutral="The funding cycle was wrapping up for the year."),
    dict(id="m04", verb="lent", subj="The neighbor", rec="the young couple", thm="a folding table",
         rec_given="The young couple had moved in across the street last month.",
         thm_given="A folding table was leaning, unused, against the garage wall.",
         neutral="The block party was only two days away."),
    dict(id="m05", verb="showed", subj="The guide", rec="the curious students", thm="an old letter",
         rec_given="The curious students had signed up for the morning tour.",
         thm_given="An old letter lay sealed in a case near the entrance.",
         neutral="The museum opened its doors right at nine."),
    dict(id="m06", verb="mailed", subj="The office", rec="the retired teacher", thm="a thank-you card",
         rec_given="The retired teacher had given forty years to the school.",
         thm_given="A thank-you card had been signed by the whole staff.",
         neutral="It was the last week before the summer break."),
    dict(id="m07", verb="brought", subj="The waiter", rec="the elderly diner", thm="a warm blanket",
         rec_given="The elderly diner had asked to sit near the window.",
         thm_given="A warm blanket was kept behind the host's stand.",
         neutral="A cold draft moved through the half-empty restaurant."),
    dict(id="m08", verb="awarded", subj="The committee", rec="the junior researcher", thm="a travel prize",
         rec_given="The junior researcher had presented the closing talk.",
         thm_given="A travel prize was announced at the end of the program.",
         neutral="The conference dinner stretched well past ten."),
    dict(id="m09", verb="passed", subj="The captain", rec="the new recruit", thm="a folded flag",
         rec_given="The new recruit stood at the end of the line.",
         thm_given="A folded flag rested on the small wooden table.",
         neutral="The ceremony began just after sunrise."),
    dict(id="m10", verb="read", subj="The nurse", rec="the anxious patient", thm="a short note",
         rec_given="The anxious patient had been awake since dawn.",
         thm_given="A short note had come up from the front desk.",
         neutral="The ward settled into its slow afternoon rhythm."),
    dict(id="m11", verb="sold", subj="The dealer", rec="the eager collector", thm="a rare coin",
         rec_given="The eager collector had flown in for the auction.",
         thm_given="A rare coin had surfaced in the latest consignment.",
         neutral="The salesroom filled steadily through the morning."),
    dict(id="m12", verb="taught", subj="The coach", rec="the nervous beginner", thm="a simple drill",
         rec_given="The nervous beginner had never held a racket before.",
         thm_given="A simple drill worked well for first-time players.",
         neutral="The court baked under the late June sun."),
    dict(id="m13", verb="threw", subj="The pitcher", rec="the rookie catcher", thm="a slow curve",
         rec_given="The rookie catcher had been called up that week.",
         thm_given="A slow curve was the pitch they had practiced.",
         neutral="The stadium lights flickered on at dusk."),
    dict(id="m14", verb="gave", subj="The judge", rec="the grateful winner", thm="a small trophy",
         rec_given="The grateful winner had trained for this all year.",
         thm_given="A small trophy waited on the edge of the stage.",
         neutral="The hall echoed with restless applause."),
    dict(id="m15", verb="served", subj="The chef", rec="the visiting critic", thm="a light dessert",
         rec_given="The visiting critic had booked the corner table.",
         thm_given="A light dessert finished the tasting menu.",
         neutral="The kitchen hummed through the dinner rush."),
    dict(id="m16", verb="offered", subj="The host", rec="the late arrival", thm="a spare seat",
         rec_given="The late arrival slipped in during the first act.",
         thm_given="A spare seat sat empty in the second row.",
         neutral="The theater dimmed its lights on cue."),
    dict(id="m17", verb="handed", subj="The teller", rec="the regular customer", thm="a deposit slip",
         rec_given="The regular customer came in every Friday at noon.",
         thm_given="A deposit slip lay ready on the polished counter.",
         neutral="The bank was calm between the lunchtime waves."),
    dict(id="m18", verb="sent", subj="The editor", rec="the freelance writer", thm="a brief reply",
         rec_given="The freelance writer had pitched the story twice.",
         thm_given="A brief reply was overdue by several days.",
         neutral="The newsroom thinned out toward evening."),
    dict(id="m19", verb="lent", subj="The librarian", rec="the visiting scholar", thm="a thick volume",
         rec_given="The visiting scholar had a reader's pass for the week.",
         thm_given="A thick volume sat behind the reference desk.",
         neutral="The reading room stayed hushed all morning."),
    dict(id="m20", verb="showed", subj="The agent", rec="the first-time buyer", thm="a sunny flat",
         rec_given="The first-time buyer had saved for years.",
         thm_given="A sunny flat had just come on the market.",
         neutral="The viewings were booked back to back."),
    dict(id="m21", verb="mailed", subj="The charity", rec="the longtime donor", thm="a glossy report",
         rec_given="The longtime donor had given since the very start.",
         thm_given="A glossy report covered the year's projects.",
         neutral="The mailing went out at the end of the quarter."),
    dict(id="m22", verb="brought", subj="The intern", rec="the senior partner", thm="a strong coffee",
         rec_given="The senior partner had a call in five minutes.",
         thm_given="A strong coffee was brewing in the break room.",
         neutral="The office filled up slowly after eight."),
    dict(id="m23", verb="awarded", subj="The school", rec="the top student", thm="a full scholarship",
         rec_given="The top student had led the class all year.",
         thm_given="A full scholarship was reserved for one graduate.",
         neutral="Graduation was set for the second of June."),
    dict(id="m24", verb="passed", subj="The surgeon", rec="the steady assistant", thm="a clean scalpel",
         rec_given="The steady assistant had scrubbed in early.",
         thm_given="A clean scalpel lay ready on the tray.",
         neutral="The operating room was cool and bright."),
    dict(id="m25", verb="read", subj="The father", rec="the sleepy toddler", thm="a short story",
         rec_given="The sleepy toddler had fought bedtime for an hour.",
         thm_given="A short story sat dog-eared on the nightstand.",
         neutral="The house went quiet after eight o'clock."),
    dict(id="m26", verb="sold", subj="The farmer", rec="the weekend visitor", thm="a ripe melon",
         rec_given="The weekend visitor stopped by the roadside stand.",
         thm_given="A ripe melon sat at the front of the crate.",
         neutral="The market drew a steady morning crowd."),
    dict(id="m27", verb="taught", subj="The mentor", rec="the eager apprentice", thm="a tricky knot",
         rec_given="The eager apprentice had started only that week.",
         thm_given="A tricky knot held the whole rig together.",
         neutral="The workshop smelled of sawdust and oil."),
    dict(id="m28", verb="threw", subj="The fan", rec="the smiling player", thm="a new ball",
         rec_given="The smiling player jogged over to the railing.",
         thm_given="A new ball had rolled to the edge of the field.",
         neutral="The crowd buzzed before the final whistle."),
    dict(id="m29", verb="gave", subj="The doctor", rec="the worried parent", thm="a clear answer",
         rec_given="The worried parent had sat in the waiting room all day.",
         thm_given="A clear answer was finally in the test results.",
         neutral="The clinic ran behind through the afternoon."),
    dict(id="m30", verb="served", subj="The barista", rec="the morning regular", thm="a hot drink",
         rec_given="The morning regular pushed through the door at seven.",
         thm_given="A hot drink was exactly what the weather called for.",
         neutral="The cafe windows fogged in the early chill."),
    dict(id="m31", verb="offered", subj="The manager", rec="the loyal employee", thm="a better role",
         rec_given="The loyal employee had stayed through the lean years.",
         thm_given="A better role had opened on the senior team.",
         neutral="The reorganization was announced on Monday."),
    dict(id="m32", verb="handed", subj="The officer", rec="the lost tourist", thm="a clear map",
         rec_given="The lost tourist had wandered far from the square.",
         thm_given="A clear map hung in the station window.",
         neutral="The afternoon crowds thinned near the river."),
]

# CONTROL arm: large length gap so end-weight has a definite prediction that OPPOSES
# information structure in the dissociating context. clong = long recipient (5-7 wds) +
# short theme (1-2 wds): in the recipient-given context, info -> DOC (given recipient
# first) but end-weight -> PD (heavy recipient last) -> dissociation. tlong = long theme
# + short recipient: in the theme-given context, info -> PD (given theme first) but
# end-weight -> DOC (heavy theme last) -> dissociation.

CONTROL = [
    # --- long recipient, short theme (recipient-given context dissociates) ---
    dict(id="clong1", verb="offered", subj="The firm", rec="the three newly promoted department heads", thm="a raise",
         rec_given="The three newly promoted department heads met on Tuesday.",
         thm_given="A raise had been approved in the new budget.",
         neutral="The fiscal year closed at the end of March."),
    dict(id="clong2", verb="sent", subj="The school", rec="the parents of the graduating seniors", thm="a letter",
         rec_given="The parents of the graduating seniors gathered in the hall.",
         thm_given="A letter went out from the principal's office.",
         neutral="Commencement week brought constant phone calls."),
    dict(id="clong3", verb="gave", subj="The captain", rec="the youngest sailor on the entire crew", thm="a medal",
         rec_given="The youngest sailor on the entire crew stepped forward.",
         thm_given="A medal had arrived from the admiralty that week.",
         neutral="The deck was scrubbed and ready by dawn."),
    dict(id="clong4", verb="handed", subj="The usher", rec="the couple celebrating their fiftieth anniversary", thm="a rose",
         rec_given="The couple celebrating their fiftieth anniversary arrived early.",
         thm_given="A rose was set aside at the welcome desk.",
         neutral="The banquet hall glittered under the chandeliers."),
    dict(id="clong5", verb="mailed", subj="The shop", rec="the customer who had complained last week", thm="a coupon",
         rec_given="The customer who had complained last week called again.",
         thm_given="A coupon was printed for the holiday sale.",
         neutral="The returns desk stayed busy all afternoon."),
    dict(id="clong6", verb="read", subj="The volunteer", rec="the residents of the new care home", thm="a poem",
         rec_given="The residents of the new care home settled into the lounge.",
         thm_given="A poem had been chosen for the occasion.",
         neutral="The afternoon light fell soft across the room."),
    # --- long theme, short recipient (theme-given context dissociates) ---
    dict(id="tlong1", verb="gave", subj="The donor", rec="the school", thm="the entire collection of antique maps",
         rec_given="The school had launched a fundraising drive that spring.",
         thm_given="The entire collection of antique maps had been appraised.",
         neutral="The estate sale was scheduled for the weekend."),
    dict(id="tlong2", verb="offered", subj="The studio", rec="the band", thm="a week in the newly renovated studio",
         rec_given="The band had been touring small clubs all year.",
         thm_given="A week in the newly renovated studio had opened up.",
         neutral="The recording calendar filled fast in autumn."),
    dict(id="tlong3", verb="sent", subj="The lab", rec="the team", thm="the results of the long-delayed experiment",
         rec_given="The team had been waiting on word for months.",
         thm_given="The results of the long-delayed experiment came back.",
         neutral="The funding review loomed at the end of the term."),
    dict(id="tlong4", verb="showed", subj="The curator", rec="the press", thm="the centerpiece of the new modern wing",
         rec_given="The press had gathered for the morning preview.",
         thm_given="The centerpiece of the new modern wing was unveiled.",
         neutral="The gallery buzzed ahead of the official opening."),
    dict(id="tlong5", verb="lent", subj="The archive", rec="the museum", thm="the diaries of the famous explorer",
         rec_given="The museum had requested a loan for its exhibit.",
         thm_given="The diaries of the famous explorer were catalogued at last.",
         neutral="The exhibition was set to open in the fall."),
    dict(id="tlong6", verb="sold", subj="The owner", rec="the city", thm="the last undeveloped lot on the waterfront",
         rec_given="The city had been negotiating quietly for a year.",
         thm_given="The last undeveloped lot on the waterfront went up for sale.",
         neutral="The harbor district was changing fast."),
]


def doc_phrase(it):   # double object: verb + recipient + theme
    return f"{it['verb']} {it['rec']} {it['thm']}"


def pd_phrase(it):    # prepositional dative: verb + theme + to + recipient
    return f"{it['verb']} {it['thm']} to {it['rec']}"


CONTEXTS = ["rec_given", "thm_given", "neutral"]
# Which contexts each arm uses. MAIN uses all three (neutral = both-new baseline);
# CONTROL uses the two givenness contexts (its dissociation lives there).
ARM_CONTEXTS = {"main": ["rec_given", "thm_given", "neutral"],
                "control": ["rec_given", "thm_given"]}


def build():
    items = []
    for it in MAIN:
        it = dict(it, arm="main")
        items.append(it)
    for it in CONTROL:
        it = dict(it, arm="control")
        items.append(it)

    trials = []
    for it in items:
        rl, tl = wc(it["rec"]), wc(it["thm"])
        for ctx in ARM_CONTEXTS[it["arm"]]:
            # order counterbalancing: DOC as option A, and DOC as option B
            for doc_is_a in (True, False):
                trials.append({
                    "item": it["id"],
                    "arm": it["arm"],
                    "context_kind": ctx,
                    "context": it[ctx],
                    "subject": it["subj"],
                    "verb": it["verb"],
                    "recipient": it["rec"],
                    "theme": it["thm"],
                    "recipient_len": rl,
                    "theme_len": tl,
                    "doc": f"{it['subj']} {doc_phrase(it)}.",
                    "pd": f"{it['subj']} {pd_phrase(it)}.",
                    "doc_is_a": doc_is_a,
                })
    return items, trials


# ---------------------------------------------------------------------------
# Certification. Prove no surface-only ("shortcut") reader beats chance on the
# information-structure contrast = within-item shift across the two givenness contexts.
# Each shortcut reader returns a DOC-preference in [0,1] from the TEST SENTENCE ONLY
# (lengths, phrasings, A/B order) -- never the context. The contrast for an item is
# pref(DOC|rec_given) - pref(DOC|thm_given); since the test sentence is identical across
# an item's contexts, every shortcut reader yields exactly 0. We assert that here.
# ---------------------------------------------------------------------------

def shortcut_readers():
    return {
        "always_DOC":     lambda t: 1.0,
        "always_PD":      lambda t: 0.0,
        "always_A":       lambda t: 1.0 if t["doc_is_a"] else 0.0,   # picks option A
        "always_B":       lambda t: 0.0 if t["doc_is_a"] else 1.0,   # picks option B
        # end-weight readers: prefer the phrasing whose FIRST np is shorter / longer.
        # DOC puts recipient first; PD puts theme first.
        "shorter_first":  lambda t: 1.0 if t["recipient_len"] < t["theme_len"] else (0.0 if t["recipient_len"] > t["theme_len"] else 0.5),
        "longer_first":   lambda t: 0.0 if t["recipient_len"] < t["theme_len"] else (1.0 if t["recipient_len"] > t["theme_len"] else 0.5),
        # length-proportional: smoothly prefers shorter-first by the length gap
        "length_prop":    lambda t: 1.0 / (1.0 + 2.718281828 ** (0.5 * (t["recipient_len"] - t["theme_len"]))),
        "position_A_bias": lambda t: 0.7 if t["doc_is_a"] else 0.3,
    }


def item_shift(trials, item_id, reader):
    """pref(DOC|rec_given) - pref(DOC|thm_given), averaged over A/B counterbalancing."""
    def mean_pref(ctx):
        vals = [reader(t) for t in trials if t["item"] == item_id and t["context_kind"] == ctx]
        return sum(vals) / len(vals) if vals else None
    a, b = mean_pref("rec_given"), mean_pref("thm_given")
    return a - b


def certify(items, trials):
    report = {"checks": {}, "fail": []}

    # (a) within-pair length variance = 0: DOC and PD of an item use the same NPs.
    a_ok = all(wc(it["rec"]) >= 1 and wc(it["thm"]) >= 1 for it in items)
    # by construction doc/pd reuse rec/thm verbatim; assert the phrasings share tokens
    for it in items:
        toks_doc = set(re.findall(r"[a-z]+", doc_phrase(it).lower()))
        toks_pd = set(re.findall(r"[a-z]+", pd_phrase(it).lower())) - {"to"}
        if toks_doc != toks_pd:
            a_ok = False
            report["fail"].append(f"(a) token mismatch DOC/PD for {it['id']}")
    report["checks"]["(a) within-pair identical NPs / length variance 0"] = a_ok

    # (d) item counts
    n_main = sum(1 for it in items if it["arm"] == "main")
    n_ctrl = sum(1 for it in items if it["arm"] == "control")
    report["checks"]["(d) >=30 main items"] = n_main >= 30
    report["checks"]["(d) neutral both-new baseline present"] = any(
        t["context_kind"] == "neutral" for t in trials)

    # (b) control arm: >=12 items, >=6 where info-structure predicts the LONGER
    # constituent first in the dissociating context.
    clong = [it for it in items if it["arm"] == "control" and wc(it["rec"]) > wc(it["thm"])]
    tlong = [it for it in items if it["arm"] == "control" and wc(it["thm"]) > wc(it["rec"])]
    # clong: recipient-given context -> info says recipient(longer) first; end-weight says
    #        theme(shorter) first -> opposite. tlong: theme-given context -> info says
    #        theme(longer) first; end-weight says recipient(shorter) first -> opposite.
    report["checks"]["(b) >=12 control items"] = n_ctrl >= 12
    report["checks"]["(b) >=6 control items where given=longer (long recipient)"] = len(clong) >= 6
    report["checks"]["(b) >=6 control items where given=longer (long theme)"] = len(tlong) >= 6

    # (c) length distributions matched across given conditions: trivially identical
    # because each item appears in BOTH givenness contexts with the same NPs. Assert it.
    rec_lens_recgiven = sorted(t["recipient_len"] for t in trials if t["context_kind"] == "rec_given")
    rec_lens_thmgiven = sorted(t["recipient_len"] for t in trials if t["context_kind"] == "thm_given")
    thm_lens_recgiven = sorted(t["theme_len"] for t in trials if t["context_kind"] == "rec_given")
    thm_lens_thmgiven = sorted(t["theme_len"] for t in trials if t["context_kind"] == "thm_given")
    report["checks"]["(c) recipient-length dist identical across given conditions"] = rec_lens_recgiven == rec_lens_thmgiven
    report["checks"]["(c) theme-length dist identical across given conditions"] = thm_lens_recgiven == thm_lens_thmgiven

    # NO ANSWER LEAKAGE: the context sentences must not themselves contain a ditransitive
    # DOC/PD phrasing of the item verb (which a model could pattern-match).
    leak = []
    for it in items:
        for ctx in ARM_CONTEXTS[it["arm"]]:
            if re.search(rf"\b{re.escape(it['verb'])}\b", it[ctx].lower()):
                leak.append(f"{it['id']}/{ctx}")
    report["checks"]["no item-verb appears in its own context (no dative-phrasing leak)"] = not leak
    if leak:
        report["fail"].append(f"verb leak in contexts: {leak}")

    # CORE certification: every shortcut reader yields shift = 0 on EVERY item.
    readers = shortcut_readers()
    max_abs_shift = {}
    for name, r in readers.items():
        shifts = [abs(item_shift(trials, it["id"], r)) for it in items]
        max_abs_shift[name] = max(shifts)
    report["max_abs_item_shift_per_shortcut_reader"] = {k: round(v, 6) for k, v in max_abs_shift.items()}
    all_zero = all(v < 1e-9 for v in max_abs_shift.values())
    report["checks"]["no length/position/order shortcut reader produces ANY within-item shift (all shifts = 0)"] = all_zero
    if not all_zero:
        report["fail"].append("a shortcut reader produced a nonzero shift")

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    return report


def main():
    items, trials = build()
    stim = {
        "design": "dative information-structure; within-item givenness-context shift; "
                  "graded forced-choice; ratified decisions/resolved/dative-anchor-and-indicator",
        "n_items": len(items),
        "n_main": sum(1 for it in items if it["arm"] == "main"),
        "n_control": sum(1 for it in items if it["arm"] == "control"),
        "n_trials": len(trials),
        "contexts_per_arm": ARM_CONTEXTS,
        "items": items,
        "trials": trials,
    }
    payload = json.dumps(stim, indent=2, ensure_ascii=False)
    (HERE / "stimuli.json").write_text(payload)
    sha = hashlib.sha256(payload.encode()).hexdigest()

    report = certify(items, trials)
    report["stimuli_sha256"] = sha
    (HERE / "certification.json").write_text(json.dumps(report, indent=2))

    print(f"stimuli.json: {len(items)} items "
          f"({stim['n_main']} main + {stim['n_control']} control), "
          f"{len(trials)} trials")
    print(f"stimuli_sha256: {sha}")
    print("CERTIFICATION:", "PASS" if report["ok"] else "FAIL")
    for k, v in report["checks"].items():
        print(f"  [{'OK' if v else 'XX'}] {k}")
    print("  max |within-item shift| per shortcut reader:",
          report["max_abs_item_shift_per_shortcut_reader"])
    if report["fail"]:
        print("  FAILURES:", report["fail"])


if __name__ == "__main__":
    main()
