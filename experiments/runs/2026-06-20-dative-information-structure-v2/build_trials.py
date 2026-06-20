#!/usr/bin/env python3
"""Build + certify + freeze the dative information-structure stimuli — V2 REPLICATION.

This is a fresh, DISJOINT item set replicating the v1 instrument
(2026-06-20-dative-information-structure) on the SAME ratified operationalization
(decisions/resolved/dative-anchor-and-indicator, ADOPT MODIFIED). No design change, no
new decision: every scenario (subjects, recipients, themes, discourse contexts) is newly
authored and shares no item with v1. The point is replication — to firm up the v1
direction-of-effect (3/3 CONFIRM) and, in particular, test whether the order-of-magnitude
effect-size spread (gemini +0.524 >> claude +0.327 >> gpt +0.056) reproduces on fresh
items, which is revision trigger (c) of essay/concordant-verdict-hides-spread.

DESIGN (identical to v1). The givenness manipulation lives in the *discourse context*,
never in the NPs: the SAME double-object (DOC) / prepositional-dative (PD) phrasing pair
— identical words, identical recipient/theme lengths, identical animacy — is rated under
different prior contexts that establish which referent is discourse-GIVEN. The primary
measure is the WITHIN-ITEM preference shift across contexts:

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
  - MAIN (>=30 items): recipient and theme of equal word length (3/3), rated in
    recipient-given, theme-given, and both-new (neutral baseline) contexts.
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
# All 32 main items are newly authored for v2; none appears in the v1 stimulus set.
# ---------------------------------------------------------------------------

MAIN = [
    dict(id="m01", verb="promised", subj="The mayor", rec="the angry residents", thm="a quick fix",
         rec_given="The angry residents had packed the council meeting.",
         thm_given="A quick fix was needed before the winter storms.",
         neutral="The city budget debate dragged into the night."),
    dict(id="m02", verb="paid", subj="The producer", rec="the session musician", thm="a flat fee",
         rec_given="The session musician had played on every track.",
         thm_given="A flat fee covered the whole afternoon's work.",
         neutral="The recording booth sat dark between takes."),
    dict(id="m03", verb="told", subj="The lawyer", rec="the uneasy client", thm="a blunt assessment",
         rec_given="The uneasy client had called three times that morning.",
         thm_given="A blunt assessment was the only honest option.",
         neutral="The firm's hallways emptied out by six."),
    dict(id="m04", verb="wrote", subj="The novelist", rec="the young fan", thm="a kind note",
         rec_given="The young fan had waited in line for hours.",
         thm_given="A kind note seemed the least she could manage.",
         neutral="The bookstore lights stayed on past closing."),
    dict(id="m05", verb="offered", subj="The college", rec="the transfer student", thm="a partial waiver",
         rec_given="The transfer student had strong grades from abroad.",
         thm_given="A partial waiver remained in the aid budget.",
         neutral="The admissions office faced a busy spring."),
    dict(id="m06", verb="handed", subj="The bailiff", rec="the waiting juror", thm="a printed form",
         rec_given="The waiting juror had sat in the hall since eight.",
         thm_given="A printed form was required before entry.",
         neutral="The courthouse steps gleamed after the rain."),
    dict(id="m07", verb="lent", subj="The professor", rec="the grateful student", thm="a rare textbook",
         rec_given="The grateful student had asked after the seminar.",
         thm_given="A rare textbook sat on the office shelf.",
         neutral="The semester's first snow fell that week."),
    dict(id="m08", verb="sold", subj="The gallery", rec="the private buyer", thm="a small sketch",
         rec_given="The private buyer had flown in for the opening.",
         thm_given="A small sketch hung near the back wall.",
         neutral="The art fair drew crowds all weekend."),
    dict(id="m09", verb="taught", subj="The veteran", rec="the keen cadet", thm="a useful trick",
         rec_given="The keen cadet had volunteered for extra drills.",
         thm_given="A useful trick made the climb much safer.",
         neutral="The training camp woke before dawn."),
    dict(id="m10", verb="served", subj="The bartender", rec="the weary trucker", thm="a cold soda",
         rec_given="The weary trucker had driven through the night.",
         thm_given="A cold soda was the special that evening.",
         neutral="The roadside diner buzzed with late traffic."),
    dict(id="m11", verb="mailed", subj="The publisher", rec="the debut author", thm="a signed copy",
         rec_given="The debut author had waited two years for this.",
         thm_given="A signed copy went to a lucky few.",
         neutral="The warehouse shipped orders all morning."),
    dict(id="m12", verb="brought", subj="The aide", rec="the busy senator", thm="a fresh briefing",
         rec_given="The busy senator had back-to-back hearings.",
         thm_given="A fresh briefing covered the overnight news.",
         neutral="The capitol corridors hummed with staffers."),
    dict(id="m13", verb="showed", subj="The realtor", rec="the curious couple", thm="a corner unit",
         rec_given="The curious couple had browsed online for weeks.",
         thm_given="A corner unit had just come on the market.",
         neutral="The downtown towers caught the morning sun."),
    dict(id="m14", verb="passed", subj="The referee", rec="the home captain", thm="a yellow card",
         rec_given="The home captain had argued every call.",
         thm_given="A yellow card seemed unavoidable by then.",
         neutral="The stadium roared through the second half."),
    dict(id="m15", verb="gave", subj="The principal", rec="the shy pupil", thm="a gold star",
         rec_given="The shy pupil had finally raised her hand.",
         thm_given="A gold star meant a lot at that age.",
         neutral="The classroom buzzed before the bell."),
    dict(id="m16", verb="sent", subj="The committee", rec="the hopeful applicant", thm="a warm reply",
         rec_given="The hopeful applicant had written in twice already.",
         thm_given="A warm reply had been drafted that morning.",
         neutral="The grant season wound down in May."),
    dict(id="m17", verb="read", subj="The teacher", rec="the restless class", thm="a short fable",
         rec_given="The restless class had been cooped up indoors.",
         thm_given="A short fable fit the last ten minutes.",
         neutral="The rain drummed against the tall windows."),
    dict(id="m18", verb="threw", subj="The keeper", rec="the open winger", thm="a long pass",
         rec_given="The open winger had sprinted down the flank.",
         thm_given="A long pass could spring the counter.",
         neutral="The floodlights buzzed over the wet pitch."),
    dict(id="m19", verb="loaned", subj="The bank", rec="the small vendor", thm="a modest sum",
         rec_given="The small vendor had banked there for years.",
         thm_given="A modest sum would cover the new stall.",
         neutral="The market district reopened after repairs."),
    dict(id="m20", verb="awarded", subj="The academy", rec="the bold director", thm="a top honor",
         rec_given="The bold director had divided the critics.",
         thm_given="A top honor had not gone to a debut in years.",
         neutral="The ceremony ran long into the evening."),
    dict(id="m21", verb="offered", subj="The team", rec="the free agent", thm="a short deal",
         rec_given="The free agent had drawn interest from rivals.",
         thm_given="A short deal hedged against the injury risk.",
         neutral="The transfer window closed at midnight."),
    dict(id="m22", verb="fed", subj="The keeper", rec="the orphaned cub", thm="a warm bottle",
         rec_given="The orphaned cub had refused food all day.",
         thm_given="A warm bottle sat ready by the heater.",
         neutral="The sanctuary closed to visitors at dusk."),
    dict(id="m23", verb="sold", subj="The breeder", rec="the eager hobbyist", thm="a young pup",
         rec_given="The eager hobbyist had researched the breed for months.",
         thm_given="A young pup was ready to leave the litter.",
         neutral="The county fair opened under clear skies."),
    dict(id="m24", verb="promised", subj="The coach", rec="the benched striker", thm="a fair shot",
         rec_given="The benched striker had trained twice as hard.",
         thm_given="A fair shot was all anyone could ask.",
         neutral="The locker room fell quiet before kickoff."),
    dict(id="m25", verb="paid", subj="The client", rec="the freelance coder", thm="a final invoice",
         rec_given="The freelance coder had shipped the last feature.",
         thm_given="A final invoice closed out the project.",
         neutral="The startup office cleared out for the holidays."),
    dict(id="m26", verb="told", subj="The captain", rec="the green sailor", thm="a tall tale",
         rec_given="The green sailor had never left port before.",
         thm_given="A tall tale passed the long night watch.",
         neutral="The harbor fog rolled in after dark."),
    dict(id="m27", verb="showed", subj="The archivist", rec="the keen historian", thm="a faded map",
         rec_given="The keen historian had requested access for weeks.",
         thm_given="A faded map turned up in the basement.",
         neutral="The reading room smelled of old paper."),
    dict(id="m28", verb="brought", subj="The waiter", rec="the picky regular", thm="a fresh menu",
         rec_given="The picky regular had complained last visit.",
         thm_given="A fresh menu had launched that very day.",
         neutral="The bistro filled quickly after seven."),
    dict(id="m29", verb="mailed", subj="The clinic", rec="the worried mother", thm="a lab result",
         rec_given="The worried mother had called the front desk daily.",
         thm_given="A lab result had finally come back.",
         neutral="The waiting room TV murmured all afternoon."),
    dict(id="m30", verb="lent", subj="The studio", rec="the indie band", thm="a vintage amp",
         rec_given="The indie band had booked the cheaper slot.",
         thm_given="A vintage amp gathered dust in the closet.",
         neutral="The mixing console glowed in the dim room."),
    dict(id="m31", verb="gave", subj="The vet", rec="the limping dog", thm="a quick exam",
         rec_given="The limping dog had been favoring one paw.",
         thm_given="A quick exam would rule out a fracture.",
         neutral="The clinic kennels quieted down by noon."),
    dict(id="m32", verb="served", subj="The host", rec="the guest chef", thm="a rare vintage",
         rec_given="The guest chef had flown in from Lyon.",
         thm_given="A rare vintage had been saved for the night.",
         neutral="The dinner party stretched past midnight."),
]

# CONTROL arm: large length gap so end-weight has a definite prediction that OPPOSES
# information structure in the dissociating context. clong = long recipient + short theme:
# in the recipient-given context, info -> DOC (given recipient first) but end-weight -> PD
# (heavy recipient last) -> dissociation. tlong = long theme + short recipient: in the
# theme-given context, info -> PD (given theme first) but end-weight -> DOC (heavy theme
# last) -> dissociation. tlong recipients are institutions (coded inanimate, conservative,
# in the SECONDARY corpus-gradient only -- see analyze.py INANIMATE_REC_ITEMS).
# All 12 control items are newly authored for v2.

CONTROL = [
    # --- long recipient, short theme (recipient-given context dissociates) ---
    dict(id="clong1", verb="offered", subj="The firm", rec="the two longest-serving floor supervisors", thm="a bonus",
         rec_given="The two longest-serving floor supervisors met after the shift.",
         thm_given="A bonus had been set aside for the holidays.",
         neutral="The plant ran double shifts all summer."),
    dict(id="clong2", verb="sent", subj="The school", rec="the families of the incoming first-years", thm="a guide",
         rec_given="The families of the incoming first-years gathered in the gym.",
         thm_given="A guide had been printed over the summer.",
         neutral="Orientation week always brought a flurry of calls."),
    dict(id="clong3", verb="gave", subj="The general", rec="the youngest officer in the entire regiment", thm="a medal",
         rec_given="The youngest officer in the entire regiment saluted sharply.",
         thm_given="A medal had arrived from the capital that week.",
         neutral="The parade ground baked under the noon sun."),
    dict(id="clong4", verb="handed", subj="The clerk", rec="the man at the very back of the line", thm="a pen",
         rec_given="The man at the very back of the line sighed loudly.",
         thm_given="A pen lay chained to the counter.",
         neutral="The post office crawled through the lunch hour."),
    dict(id="clong5", verb="mailed", subj="The store", rec="the customer who returned the broken blender", thm="a refund",
         rec_given="The customer who returned the broken blender wrote again.",
         thm_given="A refund had been approved by the manager.",
         neutral="The service counter stayed busy past closing."),
    dict(id="clong6", verb="read", subj="The teacher", rec="the children in the very front row", thm="a poem",
         rec_given="The children in the very front row leaned forward eagerly.",
         thm_given="A poem had been chosen for the assembly.",
         neutral="The auditorium lights dimmed for the show."),
    # --- long theme, short recipient (theme-given context dissociates) ---
    dict(id="tlong1", verb="gave", subj="The collector", rec="the museum", thm="the entire set of medieval coins",
         rec_given="The museum had been courting donors for months.",
         thm_given="The entire set of medieval coins was authenticated.",
         neutral="The estate's contents went to auction in spring."),
    dict(id="tlong2", verb="offered", subj="The label", rec="the duo", thm="a slot on the summer festival tour",
         rec_given="The duo had built a following online.",
         thm_given="A slot on the summer festival tour opened up.",
         neutral="The booking calendar filled fast that year."),
    dict(id="tlong3", verb="sent", subj="The lab", rec="the agency", thm="the findings of the multi-year safety study",
         rec_given="The agency had been awaiting the data for months.",
         thm_given="The findings of the multi-year safety study were finalized.",
         neutral="The review board convened at quarter's end."),
    dict(id="tlong4", verb="showed", subj="The architect", rec="the council", thm="the model of the proposed civic center",
         rec_given="The council had debated the site for years.",
         thm_given="The model of the proposed civic center was unveiled.",
         neutral="The planning office buzzed before the vote."),
    dict(id="tlong5", verb="lent", subj="The library", rec="the festival", thm="the manuscripts of the celebrated playwright",
         rec_given="The festival had requested rare items for display.",
         thm_given="The manuscripts of the celebrated playwright were insured.",
         neutral="The exhibit hall was readied through the night."),
    dict(id="tlong6", verb="sold", subj="The developer", rec="the trust", thm="the last stretch of undeveloped coastline",
         rec_given="The trust had been raising funds for the purchase.",
         thm_given="The last stretch of undeveloped coastline came to market.",
         neutral="The shoreline drew hikers every weekend."),
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
        "design": "dative information-structure V2 REPLICATION; within-item givenness-context "
                  "shift; graded forced-choice; ratified decisions/resolved/dative-anchor-and-indicator; "
                  "fresh disjoint item set (no v1 item reused)",
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
