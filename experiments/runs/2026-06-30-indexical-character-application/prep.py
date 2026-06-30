#!/usr/bin/env python3
"""prep.py — frozen stimulus set + gold key for the indexical CHARACTER-application probe.

Run 2026-06-30-indexical-character-application. Tests essay trigger (c) of
essay/indexical-character-learnable-content-supplied: does a panel model SYSTEMATICALLY
MIS-APPLY an indexical's convention-fixed rule (its Kaplanian CHARACTER) when the context
(the origo) is fully DESCRIBED in the premises? The essay's positive half claims the
character side is "distributionally native" (an AFFORDANCE, not a measured attainment); a
systematic mis-application would falsify it (trigger (c)). A near-ceiling pass cannot PROVE
an affordance, but is CONSISTENT with it and would have falsified it had the model failed.

These are the PROJECT'S OWN synthetic stimuli (no external corpus, no license) — so the full
text is committed here (recipe-not-corpus does not apply to self-authored items). Date golds
are COMPUTED from explicit base dates + signed day-offsets via datetime, so no gold is a
hand-typed date that could carry an arithmetic typo; weekday claims in the prompt text are
ASSERTED against datetime so a mis-stated weekday cannot ship.

Four conditions (40 items, single resolution target each):
  C1 plain          — one stated origo (speaker/date/place), resolve one indexical.
  C2 origo-shift    — multi-turn dialogue; 'I'/'you'/'me'/'your' REBIND per turn.
  C3 embedded       — reported speech with its OWN origo + a salient narrator-origo DISTRACTOR;
                      resolve to the EMBEDDED speaker's origo, not the narrator's.
  C4 temporal-arith — single explicit origo date; resolve a relative temporal indexical to an
                      absolute date (the secondary, exploratory facet — see PREREG §verdict).

Per-item grading (analyze.py): the model's FINAL answer is normalized (lowercased, punctuation
stripped) and the item passes iff ANY string in item["accept"] occurs as a substring. accept
lists are authored to admit the natural surface variants of the one correct content and nothing
else (a defensibly UNAMBIGUOUS key — the pre-run critic checks this).

Usage:
    python3 prep.py            # print the manifest sha + per-condition counts
    python3 prep.py --check    # assert structural invariants + frozen sha; exit non-zero on drift
    python3 prep.py --dump     # write items.json (id/cond/ind/atype/context/question/gold/accept)
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest. Set to None on first authoring, then pinned (the probe's
# FREEZE GUARD refuses to run unless this matches), so the item set cannot drift after the
# pre-run critic has signed off on it.
FROZEN_SHA = "503d907bc3f681f0992f8f53ad2b7252ae8ab7eecf711755518dee4a4b1301c8"


def iso(base, offset):
    """Absolute ISO date for `offset` days from `base` (base is 'YYYY-MM-DD')."""
    d = dt.date.fromisoformat(base) + dt.timedelta(days=offset)
    return d.isoformat()


def assert_weekday(base, name):
    """Guard: the weekday word used in a prompt must match the actual weekday of `base`."""
    wd = dt.date.fromisoformat(base).strftime("%A")
    assert wd == name, f"weekday mismatch for {base}: stated {name}, actual {wd}"


def date_accept(isodate):
    """Acceptable surface forms of one ISO date (ISO + a few natural English renderings)."""
    d = dt.date.fromisoformat(isodate)
    forms = {
        isodate,                                  # 2026-02-25
        d.strftime("%-d %B %Y").lower(),          # 25 february 2026
        d.strftime("%B %-d %Y").lower(),          # february 25 2026
        d.strftime("%B %-d, %Y").lower(),         # february 25, 2026
        d.strftime("%-d %b %Y").lower(),          # 25 feb 2026
    }
    return sorted(forms)


# ----------------------------------------------------------------------------------------------
# C1 — PLAIN: one explicitly stated origo, resolve one indexical to its content.
# ----------------------------------------------------------------------------------------------
C1 = [
    dict(id="c1-01", ind="I", atype="entity",
         context="On 14 March 2026, addressing her students in Berlin, Dr. Elena Lopez said: "
                 "\"I will hand back your essays next week.\"",
         question="Who does \"I\" refer to?", accept=["lopez", "elena"]),
    dict(id="c1-02", ind="you", atype="entity",
         context="Maria said to Tomas: \"You left your umbrella at my house yesterday.\"",
         question="Who does \"You\" refer to?", accept=["tomas"]),
    dict(id="c1-03", ind="here", atype="place",
         context="Speaking at a press conference in Nairobi, the health minister announced: "
                 "\"We will build the new children's hospital here.\"",
         question="Which place does \"here\" refer to?", accept=["nairobi"]),
    dict(id="c1-04", ind="now", atype="date",
         context="Writing in her diary on 2 July 2026, Priya noted: \"Right now everything "
                 "feels uncertain, but I am hopeful.\"",
         question="What calendar date does \"Right now\" refer to? Answer in YYYY-MM-DD.",
         accept=date_accept("2026-07-02")),
    dict(id="c1-05", ind="today", atype="date",
         context="In a speech delivered on 9 November 2026, the mayor declared: "
                 "\"Today we open the new public library.\"",
         question="What calendar date does \"Today\" refer to? Answer in YYYY-MM-DD.",
         accept=date_accept("2026-11-09")),
    dict(id="c1-06", ind="my", atype="entity",
         context="Carlos wrote to his sister: \"My car broke down again on the motorway.\"",
         question="Whose car is \"My car\"?", accept=["carlos"]),
    dict(id="c1-07", ind="this", atype="place",
         context="Addressing a rally in Lima, the candidate declared: "
                 "\"This city deserves a better transport system.\"",
         question="Which city does \"This city\" refer to?", accept=["lima"]),
    dict(id="c1-08", ind="you", atype="entity",
         context="Anna texted Ben: \"I think I saw you at the farmers' market this morning.\"",
         question="Who does \"you\" refer to?", accept=["ben"]),
    dict(id="c1-09", ind="I", atype="entity",
         context="During a radio interview, the novelist Haruki Stone remarked: "
                 "\"I wrote my first book when I was twenty.\"",
         question="Who does \"I\" refer to?", accept=["stone", "haruki"]),
    dict(id="c1-10", ind="here", atype="place",
         context="Stranded overnight at Denver International Airport, Jordan messaged a friend: "
                 "\"I'm going to be stuck here until the morning flights resume.\"",
         question="Which place does \"here\" refer to?", accept=["denver", "airport"]),
]

# ----------------------------------------------------------------------------------------------
# C2 — ORIGO-SHIFT: 'I'/'you'/'me'/'your' rebind to the speaker/addressee of EACH turn.
# Each dialogue states the speaker and addressee of every turn; questions target a NON-first turn
# so that a model that globally fixes 'I' to the first speaker fails.
# ----------------------------------------------------------------------------------------------
_D1 = ("Turn 1 — Ann (to Ben): \"I'll bring the signed documents tomorrow.\"\n"
       "Turn 2 — Ben (to Ann): \"Thanks. I'll review them and email you my notes by Friday.\"")
_D2 = ("Turn 1 — Carlos (to Dana): \"Can you send me the photos from the trip?\"\n"
       "Turn 2 — Dana (to Carlos): \"Of course. I already uploaded them to your shared folder.\"")
_D3 = ("Turn 1 — Elif (to Frank): \"I left my keys in your office.\"\n"
       "Turn 2 — Frank (to Elif): \"I found them. I'll drop them off at your place tonight.\"\n"
       "Turn 3 — Elif (to Frank): \"Perfect — I'll wait for you there.\"")
_D4 = ("Turn 1 — Grace (to Hiro): \"You promised you'd help me move on Saturday.\"\n"
       "Turn 2 — Hiro (to Grace): \"I did, and I'll be at your apartment by nine.\"")
_D5 = ("Turn 1 — Ines (to Jamal): \"I think you forgot to pay me back.\"\n"
       "Turn 2 — Jamal (to Ines): \"Sorry! I'll transfer the money to your account today.\"")
C2 = [
    dict(id="c2-01", ind="I", atype="entity", context=_D1,
         question="In Turn 2, who does \"I\" refer to?", accept=["ben"]),
    dict(id="c2-02", ind="you", atype="entity", context=_D1,
         question="In Turn 2, who does \"you\" refer to?", accept=["ann"]),
    dict(id="c2-03", ind="me", atype="entity", context=_D2,
         question="In Turn 1, who does \"me\" refer to?", accept=["carlos"]),
    dict(id="c2-04", ind="your", atype="entity", context=_D2,
         question="In Turn 2, whose shared folder is \"your shared folder\"?", accept=["carlos"]),
    dict(id="c2-05", ind="I", atype="entity", context=_D3,
         question="In Turn 2, who does \"I\" refer to?", accept=["frank"]),
    dict(id="c2-06", ind="your", atype="entity", context=_D3,
         question="In Turn 2, whose place is \"your place\"?", accept=["elif"]),
    dict(id="c2-07", ind="you", atype="entity", context=_D3,
         question="In Turn 3, who does \"you\" refer to?", accept=["frank"]),
    dict(id="c2-08", ind="I", atype="entity", context=_D4,
         question="In Turn 2, who does \"I\" refer to?", accept=["hiro"]),
    dict(id="c2-09", ind="your", atype="entity", context=_D4,
         question="In Turn 2, whose apartment is \"your apartment\"?", accept=["grace"]),
    dict(id="c2-10", ind="me", atype="entity", context=_D5,
         question="In Turn 1, who does \"me\" refer to (in \"pay me back\")?", accept=["ines"]),
]

# ----------------------------------------------------------------------------------------------
# C3 — EMBEDDED: reported speech with its own origo, plus a salient NARRATOR-origo distractor.
# The correct content is the EMBEDDED speaker's origo. Date golds computed from the embedded
# utterance's stated date, NOT the narrator's reading date (the distractor).
# ----------------------------------------------------------------------------------------------
C3 = [
    dict(id="c3-01", ind="I", atype="entity",
         context="A biographer, writing in 2025, records the following: Abraham Lincoln once "
                 "told a friend, \"I have been turning this problem over in my mind for years.\"",
         question="In the quoted sentence, who does \"I\" refer to?", accept=["lincoln"]),
    dict(id="c3-02", ind="here", atype="place",
         context="A journalist reporting from London interviewed a witness who had been in Cairo "
                 "during the storm. The witness said: \"I was standing right here when the roof "
                 "came down.\"",
         question="Which place does \"here\" refer to in the witness's sentence?",
         accept=["cairo"]),
    dict(id="c3-03", ind="you", atype="entity",
         context="In her memoir, Olga recalls a moment from her childhood: her grandmother knelt "
                 "down, looked at the young Olga, and said, \"You will do great things one day.\"",
         question="In the grandmother's sentence, who does \"you\" refer to?", accept=["olga"]),
    dict(id="c3-04", ind="tomorrow", atype="date",
         context="Reviewing a cold case on 10 June 2026, a detective read aloud a letter that the "
                 "suspect had written on 3 February 2026. The letter said: \"I am going to leave "
                 "the country tomorrow.\"",
         question="What calendar date does \"tomorrow\" refer to in the letter? Answer in "
                  "YYYY-MM-DD.",
         accept=date_accept("2026-02-04")),
    dict(id="c3-05", ind="I", atype="entity",
         context="At a conference in Toronto, Professor Adeyemi quoted a remark her mentor, "
                 "Professor Brandt, had made years earlier: \"I never trusted a tidy dataset.\"",
         question="In the quoted remark, who does \"I\" refer to?", accept=["brandt"]),
    dict(id="c3-06", ind="here", atype="place",
         context="A tour guide in Athens told the group about a soldier from Sparta. According to "
                 "the guide, the soldier had once written home: \"I wish I could stay here forever; "
                 "I have never seen mountains like these.\" The soldier wrote this while stationed "
                 "in the Alps.",
         question="Which place does \"here\" refer to in the soldier's letter?", accept=["alps"]),
    dict(id="c3-07", ind="tomorrow", atype="date",
         context="On 1 September 2026, a manager forwarded an old message a client had sent on "
                 "20 May 2026. The client's message read: \"Please ship the order tomorrow.\"",
         question="What calendar date does \"tomorrow\" refer to in the client's message? Answer "
                  "in YYYY-MM-DD.",
         accept=date_accept("2026-05-21")),
    dict(id="c3-08", ind="you", atype="entity",
         context="A historian describes a scene: the general, addressing his lieutenant Reyes "
                 "before the battle, said, \"You will lead the left flank at dawn.\"",
         question="In the general's sentence, who does \"you\" refer to?", accept=["reyes"]),
    dict(id="c3-09", ind="my", atype="entity",
         context="In a documentary, the narrator reads from the journal of the explorer Nansen: "
                 "\"My hands are too cold to write much tonight.\"",
         question="Whose hands are \"My hands\" in the journal entry?", accept=["nansen"]),
    dict(id="c3-10", ind="yesterday", atype="date",
         context="Speaking on 30 December 2026, an archivist described a postcard that a traveler "
                 "had written on 15 March 2026. The postcard said: \"We arrived yesterday after a "
                 "long crossing.\"",
         question="What calendar date does \"yesterday\" refer to on the postcard? Answer in "
                  "YYYY-MM-DD.",
         accept=date_accept("2026-03-14")),
]

# ----------------------------------------------------------------------------------------------
# C4 — TEMPORAL ARITHMETIC: single explicit origo date, resolve a relative temporal indexical.
# Secondary/exploratory facet. base/offset computed; weekday claims asserted. A DIRECTION error
# (treating 'yesterday' as future, etc.) is a rule error (folded into trigger-(c) consideration);
# a pure magnitude slip is reported separately (PREREG §verdict).
# ----------------------------------------------------------------------------------------------
def _c4(idn, base, weekday, offset, phrase, sentence_term):
    if weekday:
        assert_weekday(base, weekday)
    gold = iso(base, offset)
    wd = (" (a " + weekday + ")") if weekday else ""
    ctx = (f"Reference date: {dt.date.fromisoformat(base).strftime('%-d %B %Y')}{wd}. "
           f"On that date someone wrote: \"{sentence_term}\"")
    return dict(id=idn, ind=phrase, atype="date", context=ctx,
                question=f"What calendar date does \"{phrase}\" refer to? Answer in YYYY-MM-DD.",
                accept=date_accept(gold), gold_iso=gold, base_iso=base)

C4 = [
    _c4("c4-01", "2026-02-27", "Friday", -2, "the day before yesterday",
        "I finished the report the day before yesterday."),
    _c4("c4-02", "2026-02-27", "Friday", +2, "the day after tomorrow",
        "The results come out the day after tomorrow."),
    _c4("c4-03", "2026-07-10", "Friday", -1, "yesterday",
        "I posted the parcel yesterday."),
    _c4("c4-04", "2026-07-10", "Friday", +1, "tomorrow",
        "We set off tomorrow."),
    _c4("c4-05", "2026-04-15", "Wednesday", +3, "in three days",
        "The inspection happens in three days."),
    _c4("c4-06", "2026-04-15", "Wednesday", -3, "three days ago",
        "I sent the invoice three days ago."),
    _c4("c4-07", "2026-10-01", "Thursday", +7, "a week from today",
        "The lease ends a week from today."),
    _c4("c4-08", "2026-10-01", "Thursday", -14, "two weeks ago",
        "I moved in two weeks ago."),
    # weekday-relative, convention stated explicitly to keep the gold unambiguous.
    dict(id="c4-09", ind="next Monday", atype="date",
         context="Reference date: 5 May 2026 (a Tuesday). On that date someone wrote: "
                 "\"Let's meet next Monday.\" Here \"next Monday\" means the first Monday "
                 "strictly after the reference date.",
         question="What calendar date does \"next Monday\" refer to? Answer in YYYY-MM-DD.",
         accept=date_accept(iso("2026-05-05", 6)), gold_iso=iso("2026-05-05", 6),
         base_iso="2026-05-05"),
    dict(id="c4-10", ind="this coming Friday", atype="date",
         context="Reference date: 5 May 2026 (a Tuesday). On that date someone wrote: "
                 "\"The deadline is this coming Friday.\" Here \"this coming Friday\" means the "
                 "first Friday on or after the reference date.",
         question="What calendar date does \"this coming Friday\" refer to? Answer in YYYY-MM-DD.",
         accept=date_accept(iso("2026-05-05", 3)), gold_iso=iso("2026-05-05", 3),
         base_iso="2026-05-05"),
]
assert_weekday("2026-05-05", "Tuesday")

CONDS = {"C1": C1, "C2": C2, "C3": C3, "C4": C4}
ITEMS = []
for cond, lst in CONDS.items():
    for it in lst:
        rec = dict(it)
        rec["cond"] = cond
        ITEMS.append(rec)


def canonical():
    """Deterministic JSON of the scored fields, for the freeze-guard sha."""
    rows = [{k: it.get(k) for k in ("id", "cond", "ind", "atype", "context", "question",
                                    "accept")} for it in ITEMS]
    return json.dumps(rows, sort_keys=True, ensure_ascii=True)


def manifest_sha():
    return hashlib.sha256(canonical().encode()).hexdigest()


def assert_structure():
    ids = [it["id"] for it in ITEMS]
    assert len(ids) == len(set(ids)), "duplicate item id"
    assert len(ITEMS) == 40, f"expected 40 items, got {len(ITEMS)}"
    for c, lst in CONDS.items():
        assert len(lst) == 10, f"{c} must have 10 items, has {len(lst)}"
    for it in ITEMS:
        for f in ("id", "cond", "ind", "atype", "context", "question", "accept"):
            assert it.get(f), f"{it.get('id')} missing {f}"
        assert it["atype"] in ("entity", "place", "date"), it["id"]
        assert isinstance(it["accept"], list) and it["accept"], it["id"]
        # accept strings are pre-normalized (lowercase, no surrounding spaces)
        for a in it["accept"]:
            assert a == a.strip().lower(), f"{it['id']} accept not normalized: {a!r}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dump", action="store_true")
    args = ap.parse_args()
    assert_structure()
    sha = manifest_sha()
    if args.dump:
        (HERE / "items.json").write_text(json.dumps(ITEMS, indent=2, ensure_ascii=True) + "\n")
        print(f"wrote items.json ({len(ITEMS)} items)")
    if args.check:
        if FROZEN_SHA not in (None, "PIN_AFTER_AUTHoring") and sha != FROZEN_SHA:
            print(f"FREEZE DRIFT: manifest sha {sha} != frozen {FROZEN_SHA}", file=sys.stderr)
            sys.exit(1)
        print(f"OK structure; manifest sha {sha}")
        return
    counts = {c: len(lst) for c, lst in CONDS.items()}
    print(f"items={len(ITEMS)} counts={counts}")
    print(f"manifest sha = {sha}")


if __name__ == "__main__":
    main()
