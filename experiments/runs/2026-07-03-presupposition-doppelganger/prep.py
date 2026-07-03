#!/usr/bin/env python3
"""prep.py — frozen stimulus set for the PRESUPPOSITION DOPPELGÄNGER (matched surface-cue) probe.

Run 2026-07-03-presupposition-doppelganger. Program item A1a. Tests
design/presupposition-doppelganger-control-v1 (ratified gate:
decisions/resolved/presupposition-doppelganger-control-design, s173). The one question: does the
presupposition/projection corner beat a MATCHED SURFACE-CUE DOPPELGÄNGER — items carrying the SAME
trigger word-form and local frame but WITHOUT the presuppositional structure — or does the
doppelgänger endorse the same content just as much (a MEASURED shadow-saturated corner)?

STRICT SCOPE (load-bearing; see PREREG §scope-cap). The primary measure is a WITHIN-MODEL residual
between two legs of the SAME base scenario — a TRIGGER leg (presupposes P) vs. a D1 DOPPELGÄNGER leg
(a minimally different NON-presupposing predicate in the same frame, same target P) — pooled over the
two PROJECTING frames (negation + question). It makes NO human comparison. Its terminal anchor status
(`internal-contrast-only`) is surfaced via the (now resolved) doppelgänger decision and is NOT
self-ratified in this run session; the result carries `anchor: pending` until an independent later
session confirms.

THE TWO OUTCOMES ARE NOT EPISTEMICALLY SYMMETRIC (pre-run critic B1/B2, applied to the design/decision
s172; upheld on ratification s173):
  - NULL residual (trigger ≈ doppelgänger) = SHADOW-SATURATED = the cleanly-licensed diagnostic prize:
    the model endorses P equally for "didn't realize that S" and "didn't suspect that S", so it is not
    tracking presuppositional structure. This is the higher-value, first-class MEASURED outcome.
  - POSITIVE residual does NOT establish "beats the distributional shadow" and does NOT move the corner
    to the beater side: a VERB-SENSITIVE surface-cue follower reconstructs a D1 residual (D1 varies the
    WORD — realize vs. suspect differ distributionally — unlike the comparative-correlative beater which
    varies only the construction over the SAME words). A positive residual claims at most "endorsement
    keyed to the trigger word-form above bare complement presence"; it warrants re-examination, weighted
    toward the CLEFT family (the one leg holding content words constant), and does NOT fire the essay's
    revision trigger.

BINDING CONDITIONS honored here (from the ratified decision, S1–S4 / N1–N2):
  - S1: the DEFINITE family is DROPPED from the powered/verdict-bearing residual. Its D1 is not a matched
        control (trigger and doppelgänger share almost no surface material; the cue does not degrade, it
        is a different sentence). Definite scenarios are marked `powered=False` and are EXPLORATORY /
        descriptive only — never entering the verdict (analyze.py enforces this).
  - S2: the three retained families are HETEROGENEOUS control types (cleft = clean construction-grain;
        factive/aspectual = lexical, subject to B1's confound). analyze.py reports PER-FAMILY as PRIMARY,
        the pooled-powered residual as secondary; the cleft family carries the most interpretable signal.
  - S3: honest N. Only the two PROJECTING frames carry the residual, so the powered residual rests on
        ~72 residual-bearing conditions/model (3 powered families × 6 scenarios × 2 legs × 2 projecting
        frames = 36 trigger + 36 doppelgänger). NOT the full item count. Six scenarios per powered
        family (up from the 3-per-family founding pilots) hold residual-N up after dropping definites.
  - S4: analyze.py reports verdict-map SENSITIVITY under nearby cutoffs.
  - N1: a sanity failure may reduce the panel to 2 models; analyze.py flags any 2/2 verdict.
  - N2: dropping the conditional frame from the primary RAISES trigger_project and works AGAINST the
        (preferred) null — evidence the exclusion is not a positive-hunt; conditional reported descriptively.

The conditional-frame exclusion is PRE-REGISTERED, grounded in result/presupposition-projection-v1
(2026-07-01, predates this design), which found projection collapses under the conditional antecedent
for every model (P-survival 0.42 / 0.17 / 0.17) — both legs near-floor there, uninformative for the
shadow question. Reported descriptively as `conditional_residual`.

Grading + verdict is in analyze.py (NO API calls); this file only freezes the items + a manifest sha.
The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA. These are the PROJECT'S
OWN synthetic items (no external corpus / license); full text committed here. Doppelgänger substitutions
are the project's own construction (the complement of the source's trigger inventory: a non-factive for
a factive, etc.); that the substitutes are non-presupposing is standard linguistic knowledge, carried at
the project's own risk, not attributed to the source (see PREREG §provenance).

Usage:
    python3 prep.py            # print manifest sha + per-family/frame counts
    python3 prep.py --check    # assert structural invariants + frozen sha; non-zero on drift
    python3 prep.py --dump     # write items.json
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Frozen sha of the canonical manifest. "PINME" until the design is frozen (before the pre-run critic
# signs off). The probe's FREEZE GUARD refuses to run unless manifest_sha() == FROZEN_SHA.
FROZEN_SHA = "4500fc5b2c66a6d35355ed80b6f7d7a60090ce80476cf8faf0533ac8d97a183a"

# Neutral system prompt — must NOT hint at presupposition, projection, triggers, doppelgängers, or the
# "right" answer. Identical to the two sibling presupposition runs.
SYS = "You are a careful reader. Answer the user's question directly."

# Forced-choice wrapper. {sentence} is the framed base (or the D2 metalinguistic sentence); {target}
# is the presupposed content P. Identical to the sibling runs.
QUERY = (
    'Consider only the following statement:\n\n'
    '"{sentence}"\n\n'
    'Taking that statement at face value, does it follow that: {target}\n\n'
    'Answer with exactly one word — YES, NO, or UNCLEAR — and nothing else.'
)

# The four embedding frames for the D1 battery, fixed order. The residual is carried by the two
# PROJECTING frames; the conditional is descriptive; plain is a surface-following read.
FRAMES = ["plain", "negation", "question", "conditional"]
CANCELLING = ("negation", "question", "conditional")
PROJECTING = ("negation", "question")   # the frames that carry the primary residual (S3)

# ---------------------------------------------------------------------------------------------
# Scenarios. Each carries:
#   presup   — the backgrounded content P the TRIGGER presupposes (a fragment ending in '?', so it
#              reads grammatically after "does it follow that: ").
#   t_*      — the TRIGGER leg framed sentences (plain/negation/question/conditional).
#   d_*      — the D1 DOPPELGÄNGER leg: a minimally different NON-presupposing predicate, SAME target P,
#              as much surrounding material held constant as the substitution allows.
#   d2       — the D2 structure-defeat leg: the trigger WORD-FORM kept, presupposition defeated by a
#              metalinguistic / quotation framing (single sentence; does not embed under the 4 frames).
#              Descriptive only.
# powered=True families (factive/aspectual/cleft) enter the verdict; powered=False (definite) is
# exploratory/descriptive only (S1).
# ---------------------------------------------------------------------------------------------
SCEN = [
    # ================= FACTIVE (trigger factive verb → P = complement fact; doppel non-factive) ======
    # matched control: "Xed that S" (factive, projects S under neg/question) vs "suspected that S"
    # (non-factive, entails S in no frame). Same complement clause on the surface.
    {"sid": "fac1", "family": "factive", "powered": True,
     "presup": "the accounts had been falsified?",
     "t_plain": "The auditor realized that the accounts had been falsified.",
     "t_negation": "The auditor didn't realize that the accounts had been falsified.",
     "t_question": "Did the auditor realize that the accounts had been falsified?",
     "t_conditional": "If the auditor realized that the accounts had been falsified, she resigned.",
     "d_plain": "The auditor suspected that the accounts had been falsified.",
     "d_negation": "The auditor didn't suspect that the accounts had been falsified.",
     "d_question": "Did the auditor suspect that the accounts had been falsified?",
     "d_conditional": "If the auditor suspected that the accounts had been falsified, she resigned.",
     "d2": "In a grammar exercise, a student was asked to write the sentence \"The auditor realized that the accounts had been falsified,\" though whether the accounts had actually been falsified was left entirely open."},
    {"sid": "fac2", "family": "factive", "powered": True,
     "presup": "the ledger had been altered?",
     "t_plain": "The inspector discovered that the ledger had been altered.",
     "t_negation": "The inspector didn't discover that the ledger had been altered.",
     "t_question": "Did the inspector discover that the ledger had been altered?",
     "t_conditional": "If the inspector discovered that the ledger had been altered, the report was delayed.",
     "d_plain": "The inspector suspected that the ledger had been altered.",
     "d_negation": "The inspector didn't suspect that the ledger had been altered.",
     "d_question": "Did the inspector suspect that the ledger had been altered?",
     "d_conditional": "If the inspector suspected that the ledger had been altered, the report was delayed.",
     "d2": "A textbook printed the example sentence \"The inspector discovered that the ledger had been altered,\" using it only to illustrate a verb, so whether the ledger had really been altered was never asserted."},
    {"sid": "fac3", "family": "factive", "powered": True,
     "presup": "the results were final?",
     "t_plain": "Maria knew that the results were final.",
     "t_negation": "Maria didn't know that the results were final.",
     "t_question": "Did Maria know that the results were final?",
     "t_conditional": "If Maria knew that the results were final, she submitted the appeal.",
     "d_plain": "Maria believed that the results were final.",
     "d_negation": "Maria didn't believe that the results were final.",
     "d_question": "Did Maria believe that the results were final?",
     "d_conditional": "If Maria believed that the results were final, she submitted the appeal.",
     "d2": "As a test of punctuation, someone copied out the words \"Maria knew that the results were final,\" with no claim being made about whether the results were in fact final."},
    {"sid": "fac4", "family": "factive", "powered": True,
     "presup": "the fuel line was cracked?",
     "t_plain": "The mechanic noticed that the fuel line was cracked.",
     "t_negation": "The mechanic didn't notice that the fuel line was cracked.",
     "t_question": "Did the mechanic notice that the fuel line was cracked?",
     "t_conditional": "If the mechanic noticed that the fuel line was cracked, the flight was grounded.",
     "d_plain": "The mechanic suspected that the fuel line was cracked.",
     "d_negation": "The mechanic didn't suspect that the fuel line was cracked.",
     "d_question": "Did the mechanic suspect that the fuel line was cracked?",
     "d_conditional": "If the mechanic suspected that the fuel line was cracked, the flight was grounded.",
     "d2": "The sentence \"The mechanic noticed that the fuel line was cracked\" appeared on a typing drill, chosen for its length alone, so nothing was being asserted about the fuel line's condition."},
    {"sid": "fac5", "family": "factive", "powered": True,
     "presup": "the dosage had been changed?",
     "t_plain": "The nurse realized that the dosage had been changed.",
     "t_negation": "The nurse didn't realize that the dosage had been changed.",
     "t_question": "Did the nurse realize that the dosage had been changed?",
     "t_conditional": "If the nurse realized that the dosage had been changed, the chart was corrected.",
     "d_plain": "The nurse assumed that the dosage had been changed.",
     "d_negation": "The nurse didn't assume that the dosage had been changed.",
     "d_question": "Did the nurse assume that the dosage had been changed?",
     "d_conditional": "If the nurse assumed that the dosage had been changed, the chart was corrected.",
     "d2": "In a handwriting sample, the line \"The nurse realized that the dosage had been changed\" was reproduced for practice, leaving open whether the dosage had been changed at all."},
    {"sid": "fac6", "family": "factive", "powered": True,
     "presup": "the documents were forged?",
     "t_plain": "The editor learned that the documents were forged.",
     "t_negation": "The editor didn't learn that the documents were forged.",
     "t_question": "Did the editor learn that the documents were forged?",
     "t_conditional": "If the editor learned that the documents were forged, the story was pulled.",
     "d_plain": "The editor claimed that the documents were forged.",
     "d_negation": "The editor didn't claim that the documents were forged.",
     "d_question": "Did the editor claim that the documents were forged?",
     "d_conditional": "If the editor claimed that the documents were forged, the story was pulled.",
     "d2": "A style guide quoted \"The editor learned that the documents were forged\" purely as an example of reported speech, without taking any position on whether the documents were forged."},
    # ============= ASPECTUAL / CHANGE-OF-STATE (trigger presupposes prior state; doppel none) =========
    # matched control: "stopped/resumed/continued V-ing" (presupposes prior V-ing) vs "considered V-ing"
    # (no prior V-ing). Gerund complement held constant.
    {"sid": "asp1", "family": "aspectual", "powered": True,
     "presup": "the refinery used to flare gas at night?",
     "t_plain": "The refinery stopped flaring gas at night.",
     "t_negation": "The refinery didn't stop flaring gas at night.",
     "t_question": "Did the refinery stop flaring gas at night?",
     "t_conditional": "If the refinery stopped flaring gas at night, complaints fell.",
     "d_plain": "The refinery considered flaring gas at night.",
     "d_negation": "The refinery didn't consider flaring gas at night.",
     "d_question": "Did the refinery consider flaring gas at night?",
     "d_conditional": "If the refinery considered flaring gas at night, complaints fell.",
     "d2": "For a proofreading task, the sentence \"The refinery stopped flaring gas at night\" was inserted as filler, so no claim was made about whether the refinery had ever flared gas at night."},
    {"sid": "asp2", "family": "aspectual", "powered": True,
     "presup": "the ministry used to subsidize diesel?",
     "t_plain": "The ministry stopped subsidizing diesel.",
     "t_negation": "The ministry didn't stop subsidizing diesel.",
     "t_question": "Did the ministry stop subsidizing diesel?",
     "t_conditional": "If the ministry stopped subsidizing diesel, prices rose.",
     "d_plain": "The ministry considered subsidizing diesel.",
     "d_negation": "The ministry didn't consider subsidizing diesel.",
     "d_question": "Did the ministry consider subsidizing diesel?",
     "d_conditional": "If the ministry considered subsidizing diesel, prices rose.",
     "d2": "An economics quiz listed \"The ministry stopped subsidizing diesel\" as a sentence to parse, leaving entirely open whether the ministry had subsidized diesel before."},
    {"sid": "asp3", "family": "aspectual", "powered": True,
     "presup": "the agency had published the figures before?",
     "t_plain": "The agency resumed publishing the figures.",
     "t_negation": "The agency didn't resume publishing the figures.",
     "t_question": "Did the agency resume publishing the figures?",
     "t_conditional": "If the agency resumed publishing the figures, markets steadied.",
     "d_plain": "The agency considered publishing the figures.",
     "d_negation": "The agency didn't consider publishing the figures.",
     "d_question": "Did the agency consider publishing the figures?",
     "d_conditional": "If the agency considered publishing the figures, markets steadied.",
     "d2": "The clause \"The agency resumed publishing the figures\" was used in a translation exercise as raw material, with no assertion about whether the agency had published the figures previously."},
    {"sid": "asp4", "family": "aspectual", "powered": True,
     "presup": "the official had been denying the allegations?",
     "t_plain": "The official continued denying the allegations.",
     "t_negation": "The official didn't continue denying the allegations.",
     "t_question": "Did the official continue denying the allegations?",
     "t_conditional": "If the official continued denying the allegations, the inquiry widened.",
     "d_plain": "The official considered denying the allegations.",
     "d_negation": "The official didn't consider denying the allegations.",
     "d_question": "Did the official consider denying the allegations?",
     "d_conditional": "If the official considered denying the allegations, the inquiry widened.",
     "d2": "A courtroom-drama script printed the stage line \"The official continued denying the allegations\" as sample dialogue, so it made no claim about whether the official had been denying them earlier."},
    {"sid": "asp5", "family": "aspectual", "powered": True,
     "presup": "the plant used to import cobalt?",
     "t_plain": "The plant stopped importing cobalt.",
     "t_negation": "The plant didn't stop importing cobalt.",
     "t_question": "Did the plant stop importing cobalt?",
     "t_conditional": "If the plant stopped importing cobalt, output dropped.",
     "d_plain": "The plant considered importing cobalt.",
     "d_negation": "The plant didn't consider importing cobalt.",
     "d_question": "Did the plant consider importing cobalt?",
     "d_conditional": "If the plant considered importing cobalt, output dropped.",
     "d2": "On a spelling worksheet the sentence \"The plant stopped importing cobalt\" was given to copy out, leaving open whether the plant had ever imported cobalt."},
    {"sid": "asp6", "family": "aspectual", "powered": True,
     "presup": "the lab had tested the compound before?",
     "t_plain": "The lab resumed testing the compound.",
     "t_negation": "The lab didn't resume testing the compound.",
     "t_question": "Did the lab resume testing the compound?",
     "t_conditional": "If the lab resumed testing the compound, the trial advanced.",
     "d_plain": "The lab considered testing the compound.",
     "d_negation": "The lab didn't consider testing the compound.",
     "d_question": "Did the lab consider testing the compound?",
     "d_conditional": "If the lab considered testing the compound, the trial advanced.",
     "d2": "A lab-report template used \"The lab resumed testing the compound\" as placeholder text, asserting nothing about whether the lab had tested the compound before."},
    # ================= CLEFT (trigger it-cleft → P = existential; doppel plain assertion) =============
    # cleanest control: trigger and doppelgänger share the SAME content words; only the cleft structure
    # differs (B1 exception — the one construction-grain leg). Discriminating cell = NEGATION.
    {"sid": "cle1", "family": "cleft", "powered": True,
     "presup": "someone authorized the transfer?",
     "t_plain": "It was the deputy who authorized the transfer.",
     "t_negation": "It wasn't the deputy who authorized the transfer.",
     "t_question": "Was it the deputy who authorized the transfer?",
     "t_conditional": "If it was the deputy who authorized the transfer, the audit stands.",
     "d_plain": "The deputy authorized the transfer.",
     "d_negation": "The deputy didn't authorize the transfer.",
     "d_question": "Did the deputy authorize the transfer?",
     "d_conditional": "If the deputy authorized the transfer, the audit stands.",
     "d2": "A grammar handout printed \"It was the deputy who authorized the transfer\" only to illustrate cleft sentences, making no claim about whether anyone had authorized a transfer."},
    {"sid": "cle2", "family": "cleft", "powered": True,
     "presup": "someone broke the seal?",
     "t_plain": "It was the contractor who broke the seal.",
     "t_negation": "It wasn't the contractor who broke the seal.",
     "t_question": "Was it the contractor who broke the seal?",
     "t_conditional": "If it was the contractor who broke the seal, the sample is void.",
     "d_plain": "The contractor broke the seal.",
     "d_negation": "The contractor didn't break the seal.",
     "d_question": "Did the contractor break the seal?",
     "d_conditional": "If the contractor broke the seal, the sample is void.",
     "d2": "The line \"It was the contractor who broke the seal\" was used in a typing test as sample text, so it asserted nothing about whether any seal had been broken."},
    {"sid": "cle3", "family": "cleft", "powered": True,
     "presup": "someone leaked the figures?",
     "t_plain": "It was the analyst who leaked the figures.",
     "t_negation": "It wasn't the analyst who leaked the figures.",
     "t_question": "Was it the analyst who leaked the figures?",
     "t_conditional": "If it was the analyst who leaked the figures, the desk is compromised.",
     "d_plain": "The analyst leaked the figures.",
     "d_negation": "The analyst didn't leak the figures.",
     "d_question": "Did the analyst leak the figures?",
     "d_conditional": "If the analyst leaked the figures, the desk is compromised.",
     "d2": "A writing guide quoted \"It was the analyst who leaked the figures\" purely as an example of emphasis, without claiming that any figures had been leaked."},
    {"sid": "cle4", "family": "cleft", "powered": True,
     "presup": "someone blocked the permit?",
     "t_plain": "It was the mayor who blocked the permit.",
     "t_negation": "It wasn't the mayor who blocked the permit.",
     "t_question": "Was it the mayor who blocked the permit?",
     "t_conditional": "If it was the mayor who blocked the permit, the project stalls.",
     "d_plain": "The mayor blocked the permit.",
     "d_negation": "The mayor didn't block the permit.",
     "d_question": "Did the mayor block the permit?",
     "d_conditional": "If the mayor blocked the permit, the project stalls.",
     "d2": "For a punctuation drill the sentence \"It was the mayor who blocked the permit\" was written out, leaving open whether any permit had been blocked."},
    {"sid": "cle5", "family": "cleft", "powered": True,
     "presup": "someone opened the package?",
     "t_plain": "It was the courier who opened the package.",
     "t_negation": "It wasn't the courier who opened the package.",
     "t_question": "Was it the courier who opened the package?",
     "t_conditional": "If it was the courier who opened the package, the chain is broken.",
     "d_plain": "The courier opened the package.",
     "d_negation": "The courier didn't open the package.",
     "d_question": "Did the courier open the package?",
     "d_conditional": "If the courier opened the package, the chain is broken.",
     "d2": "A language app displayed \"It was the courier who opened the package\" as a sentence to translate, asserting nothing about whether the package had been opened."},
    {"sid": "cle6", "family": "cleft", "powered": True,
     "presup": "someone reset the alarm?",
     "t_plain": "It was the technician who reset the alarm.",
     "t_negation": "It wasn't the technician who reset the alarm.",
     "t_question": "Was it the technician who reset the alarm?",
     "t_conditional": "If it was the technician who reset the alarm, the log is wrong.",
     "d_plain": "The technician reset the alarm.",
     "d_negation": "The technician didn't reset the alarm.",
     "d_question": "Did the technician reset the alarm?",
     "d_conditional": "If the technician reset the alarm, the log is wrong.",
     "d2": "The clause \"It was the technician who reset the alarm\" appeared in a proofreading exercise as filler, so it made no claim about whether the alarm had been reset."},
    # ============= DEFINITE (EXPLORATORY — powered=False; cue degrades, S1) ============================
    # NOT a matched control: removing the existence presupposition forces an intensional/indefinite frame
    # that shares almost no surface material with the definite trigger. Carried descriptively only.
    {"sid": "def1", "family": "definite", "powered": False,
     "presup": "a consultant audited the merger?",
     "t_plain": "The consultant who audited the merger flew to Geneva.",
     "t_negation": "The consultant who audited the merger didn't fly to Geneva.",
     "t_question": "Did the consultant who audited the merger fly to Geneva?",
     "t_conditional": "If the consultant who audited the merger flew to Geneva, the deal is closing.",
     "d_plain": "Regulators were looking for a consultant to audit the merger.",
     "d_negation": "Regulators weren't looking for a consultant to audit the merger.",
     "d_question": "Were regulators looking for a consultant to audit the merger?",
     "d_conditional": "If regulators were looking for a consultant to audit the merger, the deal is stalling.",
     "d2": "A style manual printed \"The consultant who audited the merger flew to Geneva\" as an example of a relative clause, without claiming that any consultant had audited a merger."},
    {"sid": "def2", "family": "definite", "powered": False,
     "presup": "an engineer signed off on the bridge?",
     "t_plain": "The engineer who signed off on the bridge retired.",
     "t_negation": "The engineer who signed off on the bridge didn't retire.",
     "t_question": "Did the engineer who signed off on the bridge retire?",
     "t_conditional": "If the engineer who signed off on the bridge retired, the file reopens.",
     "d_plain": "The board wanted an engineer to sign off on the bridge.",
     "d_negation": "The board didn't want an engineer to sign off on the bridge.",
     "d_question": "Did the board want an engineer to sign off on the bridge?",
     "d_conditional": "If the board wanted an engineer to sign off on the bridge, the file reopens.",
     "d2": "The sentence \"The engineer who signed off on the bridge retired\" was used in a reading test as sample material, asserting nothing about whether any engineer had signed off on a bridge."},
    {"sid": "def3", "family": "definite", "powered": False,
     "presup": "a witness identified the suspect?",
     "t_plain": "The witness who identified the suspect testified.",
     "t_negation": "The witness who identified the suspect didn't testify.",
     "t_question": "Did the witness who identified the suspect testify?",
     "t_conditional": "If the witness who identified the suspect testified, the defense objected.",
     "d_plain": "Prosecutors hoped for a witness to identify the suspect.",
     "d_negation": "Prosecutors didn't hope for a witness to identify the suspect.",
     "d_question": "Did prosecutors hope for a witness to identify the suspect?",
     "d_conditional": "If prosecutors hoped for a witness to identify the suspect, the defense objected.",
     "d2": "A grammar worksheet quoted \"The witness who identified the suspect testified\" only to mark the relative clause, leaving open whether any witness had identified a suspect."},
    {"sid": "def4", "family": "definite", "powered": False,
     "presup": "a doctor treated the outbreak?",
     "t_plain": "The doctor who treated the outbreak resigned.",
     "t_negation": "The doctor who treated the outbreak didn't resign.",
     "t_question": "Did the doctor who treated the outbreak resign?",
     "t_conditional": "If the doctor who treated the outbreak resigned, the ward is short-staffed.",
     "d_plain": "Officials were seeking a doctor to treat the outbreak.",
     "d_negation": "Officials weren't seeking a doctor to treat the outbreak.",
     "d_question": "Were officials seeking a doctor to treat the outbreak?",
     "d_conditional": "If officials were seeking a doctor to treat the outbreak, the ward is short-staffed.",
     "d2": "For a dictation exercise the line \"The doctor who treated the outbreak resigned\" was read aloud, making no claim about whether any doctor had treated an outbreak."},
]


def build_items():
    """Flatten scenarios into item-conditions.

    D1 battery: each scenario × {trigger, doppel} legs × 4 frames.
    D2 leg:     each scenario × one metalinguistic sentence (frame='metalinguistic', leg='d2').
    """
    items = []
    for s in SCEN:
        P = s["presup"]
        for frame in FRAMES:
            for leg, pref in (("trigger", "t_"), ("doppel", "d_")):
                sentence = s[pref + frame]
                items.append({
                    "id": f"{s['sid']}-{leg}-{frame}",
                    "sid": s["sid"], "family": s["family"], "powered": s["powered"],
                    "leg": leg, "frame": frame,
                    "cancelling": frame in CANCELLING,
                    "projecting": frame in PROJECTING,
                    "target": P, "sentence": sentence,
                    "prompt": QUERY.format(sentence=sentence, target=P),
                })
        # D2 structure-defeat (descriptive; single framing, does not cross the 4 frames)
        items.append({
            "id": f"{s['sid']}-d2-metalinguistic",
            "sid": s["sid"], "family": s["family"], "powered": s["powered"],
            "leg": "d2", "frame": "metalinguistic",
            "cancelling": False, "projecting": False,
            "target": P, "sentence": s["d2"],
            "prompt": QUERY.format(sentence=s["d2"], target=P),
        })
    return items


ITEMS = build_items()

POWERED_FAMILIES = ("factive", "aspectual", "cleft")


def manifest_sha():
    """Stable sha over everything that defines the frozen stimulus/behavioral spec."""
    canon = json.dumps({
        "sys": SYS, "query": QUERY, "frames": FRAMES,
        "projecting": list(PROJECTING), "scenarios": SCEN,
    }, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(canon.encode()).hexdigest()


def check():
    errs = []
    by_fam = {}
    for s in SCEN:
        by_fam[s["family"]] = by_fam.get(s["family"], 0) + 1
    if by_fam != {"factive": 6, "aspectual": 6, "cleft": 6, "definite": 4}:
        errs.append(f"family balance off: {by_fam}")
    # powered flag must match family (definite exploratory-only per S1)
    for s in SCEN:
        want = s["family"] in POWERED_FAMILIES
        if s["powered"] != want:
            errs.append(f"{s['sid']}: powered flag {s['powered']} != expected {want}")
    sids = [s["sid"] for s in SCEN]
    if len(set(sids)) != len(sids):
        errs.append("duplicate sid")
    for s in SCEN:
        for frame in FRAMES:
            if not s.get("t_" + frame):
                errs.append(f"{s['sid']}: missing t_{frame}")
            if not s.get("d_" + frame):
                errs.append(f"{s['sid']}: missing d_{frame}")
        if not s.get("d2"):
            errs.append(f"{s['sid']}: missing d2")
        if not s["presup"].rstrip().endswith("?"):
            errs.append(f"{s['sid']}: presup target should end with '?'")
        if s["t_negation"] == s["t_plain"]:
            errs.append(f"{s['sid']}: trigger negation identical to plain")
        if not s["t_question"].rstrip().endswith("?"):
            errs.append(f"{s['sid']}: trigger question frame not interrogative")
        if not s["t_conditional"].lower().startswith("if "):
            errs.append(f"{s['sid']}: trigger conditional does not start with 'If'")
        if not s["d_conditional"].lower().startswith("if "):
            errs.append(f"{s['sid']}: doppel conditional does not start with 'If'")
        # the trigger and doppel legs must actually differ
        for frame in FRAMES:
            if s["t_" + frame] == s["d_" + frame]:
                errs.append(f"{s['sid']}: trigger==doppel in {frame}")
    # item counts
    n_expected = len(SCEN) * (2 * len(FRAMES) + 1)   # 2 legs × 4 frames + 1 D2
    if len(ITEMS) != n_expected:
        errs.append(f"expected {n_expected} items, got {len(ITEMS)}")
    # residual-bearing count (S3 honest N): powered families, both legs, projecting frames
    resid_bearing = sum(1 for it in ITEMS
                        if it["powered"] and it["leg"] in ("trigger", "doppel")
                        and it["projecting"])
    if resid_bearing != len(POWERED_FAMILIES) * 6 * 2 * len(PROJECTING):
        errs.append(f"residual-bearing count off: {resid_bearing}")
    if errs:
        print("FAIL:\n  " + "\n  ".join(errs))
        return 1
    sha = manifest_sha()
    if FROZEN_SHA not in (None, "PINME") and sha != FROZEN_SHA:
        print(f"FAIL: manifest sha drift\n  frozen={FROZEN_SHA}\n  actual={sha}")
        return 1
    print(f"OK: {len(SCEN)} scenarios ({by_fam}), {len(ITEMS)} item-conditions, "
          f"residual-bearing={resid_bearing} (powered, projecting), sha={sha}")
    if FROZEN_SHA in (None, "PINME"):
        print(f"  (NOT YET PINNED — set FROZEN_SHA = \"{sha}\")")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dump", action="store_true")
    args = ap.parse_args()
    if args.check:
        sys.exit(check())
    if args.dump:
        (HERE / "items.json").write_text(json.dumps(ITEMS, indent=2, ensure_ascii=True) + "\n")
        print(f"wrote items.json ({len(ITEMS)} item-conditions)")
        return
    print(f"scenarios={len(SCEN)} items={len(ITEMS)} sha={manifest_sha()}")
    print("per-family:", {k: sum(1 for s in SCEN if s['family'] == k)
                         for k in ('factive', 'aspectual', 'cleft', 'definite')})


if __name__ == "__main__":
    main()
