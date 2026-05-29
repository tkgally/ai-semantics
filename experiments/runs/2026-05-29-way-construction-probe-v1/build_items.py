"""Build and freeze the way-construction minimal-pair item set (probe v1, 2026-05-29).

Pre-registration (charter §8): EMITS experiments/data/way-construction/items.csv and must
be run and committed BEFORE any probe call. Instantiates conjecture/way-construction with
the project's OWN stimuli (not Scivetti's items), under the ratified constructional-
divergence-operationalization (both instruments NLI + forced-choice; gap >=30pp;
way rate >=70% per the conjecture's confirm bar). The way design's §2 logprob indicator is
unavailable (panel exposes no logprobs on OpenRouter), so we use the design's own ratified
fallback: temperature=0 greedy completion + parse, exactly as conative/caused-motion ran.

DESIGN (frozen here, before the run)
------------------------------------
Goldberg's (1995, ch. 9) way-construction `Subj V POSS way PATH-PP` coerces a self-motion /
path-traversal entailment onto NON-motion verbs:
  "Mia whistled her way down the hall."  -> Mia moved from one place to another (traversed
   the hall), even though *whistle* denotes no displacement.
The verb is held CONSTANT across forms; only the construction varies, so an affirmed
path-traversal inference for the *way* form that vanishes for the location control cannot
come from the verb -- it must be CONSTRUCTIONAL.

PRIMARY INDICATOR: "affirm path-traversal rate" on the hypothesis
  "<Subj> moved from one place to another."   (FC answer YES, or NLI label 0 = entailment).
Conjecture confirm bar: way rate >=70% with a >=30pp gap vs. the location control, in
>=2/3 models, holding for the anti-motion verb category (P3 / verb-reading guard).

ADVERSARIAL PRE-RUN PASS (2026-05-29) -- fixes applied BEFORE freezing
---------------------------------------------------------------------
A read-only adversarial review of the first draft flagged BLOCKERS: several path-PPs were
TEMPORAL/EVENTIVE/ABSTRACT ("through the afternoon/journey/party/flight/speech/report",
"down the list", "up the company"), for which "moved from one place to another" is NOT
entailed -- so a YES gold there was indefensible and would corrupt the activity/anti-motion
rates and make a P3 confirm/null uninterpretable. Also: conveyance controls ("on the train",
"on the flight") make the LOC control's own gold wrong (the train/flight moves the subject),
and several ctrl-motion sentences were incoherent ("sat as she walked"). Fixes:
  * EVERY path-PP is now a genuine SPATIAL path (a place you traverse on foot).
  * EVERY loc control is a plain locative of the SAME scene (no conveyance frames).
  * ctrl-motion reframed to a coherent "MOTION-verb main clause + non-motion gerund adjunct"
    ("Mia walked down the hall, whistling.") -- always grammatical, motion lexicalized.
  * The verb 'work' (which only hosts an ABSTRACT-progress way-reading) was removed from the
    positive arms and kept only as an idiomatic over-generalization guard.
KNOWN, DOCUMENTED LIMIT (reviewer S2): way uses a directional PP ("down the hall"), loc uses
a locative ("in the hall"); the BARE directional form ("*Mia whistled down the hall") is
ungrammatical for these non-motion verbs WITHOUT the construction -- which is itself the
construction's signature, but means the way-vs-loc gap is not a pure "way"-string toggle.
The idiomatic guard (surface "POSS way" + NON-spatial goal -> should be low) bounds the
"is it just the 'way' string?" worry. Both are stated in the result's Limits, not tuned away.

FOUR FORMS (the first three share one verb; idiomatic is a separate over-generalization set):
  way        way-construction; SPATIAL path   -> traversal: YES   (NLI 0)
             "Mia whistled her way down the hall."
  ctrl-loc   same verb, LOCATIVE of same scene (the DISCRIMINATING control; no traversal)
             "Mia whistled in the hall."      -> traversal: CANT_TELL (NLI 1, neutral)
  ctrl-motion MOTION verb main + non-motion gerund (positive floor: motion lexicalized, so
             the indicator MUST fire here if the model understands the hypothesis)
             "Mia walked down the hall, whistling." -> traversal: YES (NLI 0)
  idiomatic  bleached / metaphorical 'POSS way' with a NON-spatial goal (over-generalization
             guard): "Elena talked her way out of trouble." -> literal traversal: CANT_TELL

ARMS (P3 / verb-reading guard): three NON-motion verb categories --
  - manner   (sound/expression; canonical way hosts):    whistle, hum, laugh, mutter, sing, sob
  - activity (consumption/social; no displacement):       eat, drink, chat, joke, gossip, snack
  - anti-motion (posture/stative; the STRESS test):       wait, rest, kneel, crouch, pause, linger
The anti-motion category is the stress test of prediction 3: a way rate that COLLAPSES there
(while holding for manner/activity) is the diagnostic "model is reading the verb, not the
construction" failure mode -- an informative DISTRIBUTIONAL finding, reported, not retuned away.
These way-items are deliberately MARKED (anti-motion + way) but each path-PP is spatial so the
traversal gold holds IF the string is read as a way-construction at all.

Run: python3 build_items.py   (no API; just writes the frozen CSV)
"""
import csv, hashlib, os

# (verb, past, gerund, category, subject, pron_subj, poss, path_pp, loc_pp, motion_past)
# ctrl-motion sentence = "{subject} {motion_past} {path_pp}, {gerund}."  (motion lexicalized)
VERBS = [
    # --- non-motion manner (sound / expression; canonical way-construction hosts) ---
    ("whistle", "whistled", "whistling", "manner", "Mia", "she", "her",
     "down the hall", "in the hall", "walked"),
    ("hum", "hummed", "humming", "manner", "Theo", "he", "his",
     "through the crowd", "in the crowd", "pushed"),
    ("laugh", "laughed", "laughing", "manner", "Priya", "she", "her",
     "across the room", "in the room", "strode"),
    ("mutter", "muttered", "muttering", "manner", "Karl", "he", "his",
     "along the corridor", "in the corridor", "walked"),
    ("sing", "sang", "singing", "manner", "Lena", "she", "her",
     "up the stairs", "on the stairs", "climbed"),
    ("sob", "sobbed", "sobbing", "manner", "Dani", "they", "their",
     "out of the office", "in the office", "walked"),
    # --- non-motion activity (consumption / social; no displacement implied) ---
    ("eat", "ate", "eating", "activity", "Sofia", "she", "her",
     "across the buffet", "at the buffet", "moved"),
    ("drink", "drank", "drinking", "activity", "Nico", "he", "his",
     "down the bar", "at the bar", "moved"),
    ("chat", "chatted", "chatting", "activity", "Hana", "she", "her",
     "through the gallery", "in the gallery", "wandered"),
    ("joke", "joked", "joking", "activity", "Owen", "he", "his",
     "down the aisle", "in the aisle", "walked"),
    ("gossip", "gossiped", "gossiping", "activity", "Bea", "she", "her",
     "across the lobby", "in the lobby", "walked"),
    ("snack", "snacked", "snacking", "activity", "Tara", "she", "her",
     "through the food court", "in the food court", "wandered"),
    # --- anti-motion / stative (posture/state; the STRESS test, P3) ---
    ("wait", "waited", "waiting", "anti-motion", "Felix", "he", "his",
     "up the queue", "in the queue", "edged"),
    ("rest", "rested", "resting", "anti-motion", "Pavel", "he", "his",
     "up the mountain", "on the mountain", "climbed"),
    ("kneel", "knelt", "kneeling", "anti-motion", "Raj", "he", "his",
     "along the pew", "at the pew", "shuffled"),
    ("crouch", "crouched", "crouching", "anti-motion", "Cora", "she", "her",
     "through the tunnel", "in the tunnel", "crept"),
    ("pause", "paused", "pausing", "anti-motion", "Ines", "she", "her",
     "down the hallway", "in the hallway", "walked"),
    ("linger", "lingered", "lingering", "anti-motion", "Wendy", "she", "her",
     "through the museum", "in the museum", "wandered"),
]

# Idiomatic / bleached 'POSS way' with a NON-spatial goal -- literal path-traversal NOT
# entailed. Over-generalization guard: a high affirm rate here = surface-string detection.
# Verbs here are DISJOINT from the positive arms (no verb is scored both ways).
IDIOMATIC = [
    ("talk", "Elena", "her", "Elena talked her way out of trouble."),
    ("work", "Marcus", "his", "Marcus worked his way up the company."),
    ("find", "Dora", "her", "Dora found her way around the new software."),
    ("lose", "Daniel", "his", "Daniel lost his way in his career."),
    ("argue", "the partners", "their", "The partners argued their way to a compromise."),
    ("scheme", "Vera", "her", "Vera schemed her way into politics."),
]

HYP_TEMPLATE = "{subj} moved from one place to another."


def cap(s):
    return s[0].upper() + s[1:]


def rows():
    out = []
    for (v, past, ger, cat, subj, pron, poss, path_pp, loc_pp, mv) in VERBS:
        hyp = HYP_TEMPLATE.format(subj=subj)
        way = f"{subj} {past} {poss} way {path_pp}."
        ctrl_loc = f"{subj} {past} {loc_pp}."
        ctrl_motion = f"{subj} {mv} {path_pp}, {ger}."
        forms = [
            # form, sentence, nli_gold, fc_gold, affirm_correct (1 = affirming traversal is correct)
            ("way", way, "0", "YES", "1"),
            ("ctrl-loc", ctrl_loc, "1", "CANT_TELL", "0"),
            ("ctrl-motion", ctrl_motion, "0", "YES", "1"),
        ]
        for form, sent, nli_gold, fc_gold, ac in forms:
            out.append(dict(
                item_id=f"{v}-{form}", verb=v, category=cat, form=form,
                subject=subj, sentence=sent, nli_hypothesis=hyp,
                nli_gold=nli_gold, fc_gold=fc_gold, affirm_correct=ac))
    for (v, subj, poss, sent) in IDIOMATIC:
        hyp = HYP_TEMPLATE.format(subj=cap(subj))
        out.append(dict(
            item_id=f"{v}-idiomatic", verb=v, category="idiomatic", form="idiomatic",
            subject=subj, sentence=sent, nli_hypothesis=hyp,
            nli_gold="1", fc_gold="CANT_TELL", affirm_correct="0"))
    return out


def main():
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                       "data", "way-construction", "items.csv"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rs = rows()
    cols = ["item_id", "verb", "category", "form", "subject", "sentence",
            "nli_hypothesis", "nli_gold", "fc_gold", "affirm_correct"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    h = hashlib.sha256(open(out, "rb").read()).hexdigest()[:16]
    ncat = {}
    for r in rs:
        ncat[r["category"]] = ncat.get(r["category"], 0) + 1
    print(f"wrote {len(rs)} items ({len(VERBS)} verbs x 3 forms + {len(IDIOMATIC)} idiomatic) -> {out}")
    print(f"  by category: {ncat}")
    print(f"  sha256[:16] = {h}  (freeze hash; record in design + README)")


if __name__ == "__main__":
    main()
